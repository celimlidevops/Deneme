"""Newton-Raphson AC yük akışı, sıfırdan.

Canlı kodlama sorusunda yazılacak iskelet budur:
  1. Ybus kur
  2. Güç enjeksiyonunu hesapla
  3. Artık (mismatch) vektörünü çıkar
  4. Jacobian kur, doğrusal sistemi çöz
  5. Açı ve gerilimi güncelle, yakınsayana kadar tekrarla
  6. PV barada Q limitini denetle, aşıldıysa PQ'ya çevir

Sözleşme: her şey per-unit, açı radyan, enjeksiyon üretimde pozitif.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

SLACK, PV, PQ = "slack", "pv", "pq"


class YakinsamaHatasi(RuntimeError):
    """Çözüm bulunamadı. Artık geçmişi teşhis için saklanır."""

    def __init__(self, mesaj: str, artiklar: list[float]):
        super().__init__(mesaj)
        self.artiklar = artiklar


@dataclass(frozen=True)
class Hat:
    i: int
    j: int
    r: float
    x: float
    b: float = 0.0  # hattın toplam şönt süseptansı, iki uca yarı yarıya


@dataclass
class Sonuc:
    v: np.ndarray
    teta: np.ndarray
    s: np.ndarray
    iterasyon: int
    tip: list[str]
    artiklar: list[float] = field(default_factory=list)


def ybus_kur(n: int, hatlar: list[Hat]) -> np.ndarray:
    y_bus = np.zeros((n, n), dtype=complex)
    for h in hatlar:
        if h.r == 0 and h.x == 0:
            raise ValueError("sıfır empedanslı hat: baraları birleştir")
        y = 1 / complex(h.r, h.x)
        y_bus[h.i, h.i] += y + 1j * h.b / 2
        y_bus[h.j, h.j] += y + 1j * h.b / 2
        y_bus[h.i, h.j] -= y
        y_bus[h.j, h.i] -= y
    return y_bus


def guc_enjeksiyonu(y_bus: np.ndarray, v: np.ndarray, teta: np.ndarray) -> np.ndarray:
    vc = v * np.exp(1j * teta)
    return vc * np.conj(y_bus @ vc)


def jacobian_acik(
    y_bus: np.ndarray, v: np.ndarray, teta: np.ndarray, pvpq: list[int], pq: list[int]
) -> np.ndarray:
    """Ders kitabı formülleriyle Jacobian. Tahtada anlatılan hali budur."""
    g, b = y_bus.real, y_bus.imag
    s = guc_enjeksiyonu(y_bus, v, teta)
    p, q = s.real, s.imag
    n = len(v)
    h = np.zeros((n, n))
    nn = np.zeros((n, n))
    m = np.zeros((n, n))
    ll = np.zeros((n, n))
    for i in range(n):
        for k in range(n):
            if i == k:
                h[i, i] = -q[i] - b[i, i] * v[i] ** 2
                nn[i, i] = p[i] / v[i] + g[i, i] * v[i]
                m[i, i] = p[i] - g[i, i] * v[i] ** 2
                ll[i, i] = q[i] / v[i] - b[i, i] * v[i]
            else:
                t = teta[i] - teta[k]
                h[i, k] = v[i] * v[k] * (g[i, k] * np.sin(t) - b[i, k] * np.cos(t))
                nn[i, k] = v[i] * (g[i, k] * np.cos(t) + b[i, k] * np.sin(t))
                m[i, k] = -v[i] * v[k] * (g[i, k] * np.cos(t) + b[i, k] * np.sin(t))
                ll[i, k] = v[i] * (g[i, k] * np.sin(t) - b[i, k] * np.cos(t))
    return np.block(
        [
            [h[np.ix_(pvpq, pvpq)], nn[np.ix_(pvpq, pq)]],
            [m[np.ix_(pq, pvpq)], ll[np.ix_(pq, pq)]],
        ]
    )


def jacobian_matris(
    y_bus: np.ndarray, v: np.ndarray, teta: np.ndarray, pvpq: list[int], pq: list[int]
) -> np.ndarray:
    """Aynı Jacobian, döngüsüz. Büyük şebekede kullanılan hali budur."""
    vc = v * np.exp(1j * teta)
    akim = y_bus @ vc
    birim = vc / v
    ds_dteta = 1j * np.diag(vc) @ np.conj(np.diag(akim) - y_bus @ np.diag(vc))
    ds_dv = np.diag(vc) @ np.conj(y_bus @ np.diag(birim)) + np.conj(np.diag(akim)) @ np.diag(birim)
    return np.block(
        [
            [ds_dteta.real[np.ix_(pvpq, pvpq)], ds_dv.real[np.ix_(pvpq, pq)]],
            [ds_dteta.imag[np.ix_(pq, pvpq)], ds_dv.imag[np.ix_(pq, pq)]],
        ]
    )


def nr_coz(
    y_bus: np.ndarray,
    tip: list[str],
    p: np.ndarray,
    q: np.ndarray,
    v_baslangic: np.ndarray,
    q_min: np.ndarray | None = None,
    q_max: np.ndarray | None = None,
    tol: float = 1e-8,
    azami_iterasyon: int = 30,
) -> Sonuc:
    """p, q: net enjeksiyon (üretim eksi yük). q_min/q_max de net enjeksiyon sınırıdır."""
    n = len(tip)
    if tip.count(SLACK) != 1:
        raise ValueError("tam bir salınım barası gerekli")
    tip = list(tip)
    q = q.astype(float).copy()
    v = v_baslangic.astype(float).copy()
    teta = np.zeros(n)
    artiklar: list[float] = []

    for iterasyon in range(1, azami_iterasyon + 1):
        pvpq = [i for i in range(n) if tip[i] != SLACK]
        pq = [i for i in range(n) if tip[i] == PQ]
        s = guc_enjeksiyonu(y_bus, v, teta)
        artik = np.concatenate([p[pvpq] - s.real[pvpq], q[pq] - s.imag[pq]])
        en_buyuk = float(np.max(np.abs(artik))) if artik.size else 0.0
        artiklar.append(en_buyuk)

        if not np.isfinite(en_buyuk):
            raise YakinsamaHatasi("artık sonsuza gitti", artiklar)

        if en_buyuk < tol:
            degisti = False
            for i in range(n):
                if tip[i] != PV:
                    continue
                if q_max is not None and s.imag[i] > q_max[i] + tol:
                    tip[i], q[i], degisti = PQ, q_max[i], True
                elif q_min is not None and s.imag[i] < q_min[i] - tol:
                    tip[i], q[i], degisti = PQ, q_min[i], True
            if not degisti:
                return Sonuc(v, teta, s, iterasyon, tip, artiklar)
            continue

        jac = csr_matrix(jacobian_matris(y_bus, v, teta, pvpq, pq))
        duzeltme = spsolve(jac, artik)
        duzeltme = np.atleast_1d(duzeltme)
        teta[pvpq] += duzeltme[: len(pvpq)]
        v[pq] += duzeltme[len(pvpq) :]

    raise YakinsamaHatasi(f"{azami_iterasyon} iterasyonda yakınsamadı", artiklar)


def hat_kaybi(hatlar: list[Hat], v: np.ndarray, teta: np.ndarray) -> float:
    vc = v * np.exp(1j * teta)
    kayip = 0.0
    for h in hatlar:
        akim = (vc[h.i] - vc[h.j]) / complex(h.r, h.x)
        kayip += abs(akim) ** 2 * h.r
    return kayip


def ornek_sebeke() -> tuple[list[Hat], list[str], np.ndarray, np.ndarray, np.ndarray]:
    hatlar = [Hat(0, 1, 0.02, 0.10), Hat(0, 2, 0.04, 0.20), Hat(1, 2, 0.05, 0.25)]
    tip = [SLACK, PV, PQ]
    p = np.array([0.0, 0.5, -0.8])
    q = np.array([0.0, 0.0, -0.3])
    v0 = np.array([1.0, 1.02, 1.0])
    return hatlar, tip, p, q, v0


def _ornek() -> None:
    hatlar, tip, p, q, v0 = ornek_sebeke()
    y_bus = ybus_kur(3, hatlar)

    serbest = nr_coz(y_bus, tip, p, q, v0)
    print("NR yük akışı, Q limiti yok")
    print(f"  iterasyon: {serbest.iterasyon}, artıklar: {[f'{a:.2e}' for a in serbest.artiklar]}")
    print(f"  V pu: {np.round(serbest.v, 5)}")
    print(f"  açı derece: {np.round(np.degrees(serbest.teta), 4)}")
    print(f"  P pu: {np.round(serbest.s.real, 5)}")
    print(f"  Q pu: {np.round(serbest.s.imag, 5)}")
    print(f"  kayıp pu: {hat_kaybi(hatlar, serbest.v, serbest.teta):.5f}")

    limitli = nr_coz(y_bus, tip, p, q, v0, q_max=np.array([9.0, 0.10, 9.0]))
    print("NR yük akışı, bara 1 Q üst sınırı 0.10")
    print(f"  bara tipleri: {limitli.tip}")
    print(f"  V pu: {np.round(limitli.v, 5)}")
    print(f"  Q pu: {np.round(limitli.s.imag, 5)}")


if __name__ == "__main__":
    _ornek()
