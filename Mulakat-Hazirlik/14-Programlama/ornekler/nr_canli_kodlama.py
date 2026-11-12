"""Canlı kodlamada 15-20 dakikada yazılacak sürüm: seyrek Ybus + Newton-Raphson.

Bakmadan yazabilene kadar tekrar et. Tam sürüm (Q limiti, hata sınıfı) nr_yuk_akisi.py içinde.
Sözleşme: her şey per-unit, açı radyan, enjeksiyon üretimde pozitif.
"""

import numpy as np
from scipy.sparse import bmat, coo_matrix, diags
from scipy.sparse.linalg import spsolve


def ybus(n, hatlar):
    """hatlar: (i, j, r, x) listesi. Aynı hücreye düşen girdileri COO kendisi toplar."""
    i, j, r, x = (np.array(sutun) for sutun in zip(*hatlar))
    y = 1 / (r + 1j * x)
    satir, sutun = np.r_[i, j, i, j], np.r_[i, j, j, i]
    return coo_matrix((np.r_[y, y, -y, -y], (satir, sutun)), shape=(n, n)).tocsc()


def yuk_akisi(y, p, q, pv, pq, v0, tol=1e-8, azami=20):
    """p, q: net enjeksiyon. pv, pq: bara indisleri; salınım barası ikisinde de yok."""
    v, teta = v0.astype(float).copy(), np.zeros(len(v0))
    pvpq = np.r_[pv, pq].astype(int)
    for tur in range(azami):
        vc = v * np.exp(1j * teta)
        akim = y @ vc
        s = vc * np.conj(akim)
        artik = np.r_[p[pvpq] - s.real[pvpq], q[pq] - s.imag[pq]]
        if np.max(np.abs(artik)) < tol:
            return v, teta, tur

        ds_dteta = (1j * diags(vc) @ (diags(akim) - y @ diags(vc)).conj()).tocsr()
        ds_dv = (diags(vc) @ (y @ diags(vc / v)).conj() + diags(akim.conj() * vc / v)).tocsr()
        jac = bmat(
            [
                [ds_dteta.real[pvpq][:, pvpq], ds_dv.real[pvpq][:, pq]],
                [ds_dteta.imag[pq][:, pvpq], ds_dv.imag[pq][:, pq]],
            ],
            format="csc",
        )
        dx = spsolve(jac, artik)
        teta[pvpq] += dx[: len(pvpq)]
        v[pq] += dx[len(pvpq) :]
    raise RuntimeError(f"{azami} turda yakınsamadı, son artık {np.max(np.abs(artik)):.2e}")


if __name__ == "__main__":
    y = ybus(3, [(0, 1, 0.02, 0.10), (0, 2, 0.04, 0.20), (1, 2, 0.05, 0.25)])
    v, teta, tur = yuk_akisi(
        y,
        p=np.array([0.0, 0.5, -0.8]),
        q=np.array([0.0, 0.0, -0.3]),
        pv=[1],
        pq=[2],
        v0=np.array([1.0, 1.02, 1.0]),
    )
    print(f"{tur} tur, V = {np.round(v, 5)}, açı = {np.round(np.degrees(teta), 4)} derece")
    assert np.allclose(v, [1.0, 1.02, 0.95146], atol=1e-5), "nr_yuk_akisi.py ile aynı sonuç bekleniyor"
    assert np.allclose(y.toarray().sum(axis=1), 0), "şönt yokken Ybus satır toplamı sıfır olmalı"
