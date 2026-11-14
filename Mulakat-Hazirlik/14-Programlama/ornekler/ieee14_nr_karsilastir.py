"""IEEE 14 bara Newton-Raphson yük akışı ve pandapower karşılaştırması.

Kendi NR çözücümüz ile pandapower.networks.case14() sonuçlarını yan yana koyar.
Mülakatta: 'NumPy ile IEEE 14 yazdım, pandapower ile doğruladım' diyebilirsin.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from nr_yuk_akisi import Hat, SLACK, PV, PQ, nr_coz, ybus_kur

# MATPOWER case14 / pandapower case14 ile uyumlu klasik veri (100 MVA baz)
# Bara tipi: 1=PQ, 2=PV, 3=slack  →  bizim SLACK/PV/PQ
BUS = np.array(
    [
        # bus Pd Qd Vm tip  (Vm başlangıç / PV setpoint)
        [1, 0.0, 0.0, 1.06, 3],
        [2, 21.7, 12.7, 1.045, 2],
        [3, 94.2, 19.0, 1.01, 2],
        [4, 47.8, -3.9, 1.0, 1],
        [5, 7.6, 1.6, 1.0, 1],
        [6, 11.2, 7.5, 1.07, 2],
        [7, 0.0, 0.0, 1.0, 1],
        [8, 0.0, 0.0, 1.09, 2],
        [9, 29.5, 16.6, 1.0, 1],
        [10, 9.0, 5.8, 1.0, 1],
        [11, 3.5, 1.8, 1.0, 1],
        [12, 6.1, 1.6, 1.0, 1],
        [13, 13.5, 5.8, 1.0, 1],
        [14, 14.9, 5.0, 1.0, 1],
    ],
    dtype=float,
)

GEN = np.array(
    [
        # bus Pg Qg Vg
        [1, 232.4, -16.9, 1.06],
        [2, 40.0, 42.4, 1.045],
        [3, 0.0, 23.4, 1.01],
        [6, 0.0, 12.2, 1.07],
        [8, 0.0, 17.4, 1.09],
    ],
    dtype=float,
)

# f, t, r, x, b (toplam şönt), tap (1.0 = yok)
BRANCH = np.array(
    [
        [1, 2, 0.01938, 0.05917, 0.0528, 1.0],
        [1, 5, 0.05403, 0.22304, 0.0492, 1.0],
        [2, 3, 0.04699, 0.19797, 0.0438, 1.0],
        [2, 4, 0.05811, 0.17632, 0.0340, 1.0],
        [2, 5, 0.05695, 0.17388, 0.0346, 1.0],
        [3, 4, 0.06701, 0.17103, 0.0128, 1.0],
        [4, 5, 0.01335, 0.04211, 0.0, 1.0],
        [4, 7, 0.0, 0.20912, 0.0, 0.978],
        [4, 9, 0.0, 0.55618, 0.0, 0.969],
        [5, 6, 0.0, 0.25202, 0.0, 0.932],
        [6, 11, 0.09498, 0.19890, 0.0, 1.0],
        [6, 12, 0.12291, 0.25581, 0.0, 1.0],
        [6, 13, 0.06615, 0.13027, 0.0, 1.0],
        [7, 8, 0.0, 0.17615, 0.0, 1.0],
        [7, 9, 0.0, 0.11001, 0.0, 1.0],
        [9, 10, 0.03181, 0.08450, 0.0, 1.0],
        [9, 14, 0.12711, 0.27038, 0.0, 1.0],
        [10, 11, 0.08205, 0.19207, 0.0, 1.0],
        [12, 13, 0.22092, 0.19988, 0.0, 1.0],
        [13, 14, 0.17093, 0.34802, 0.0, 1.0],
    ],
    dtype=float,
)

SBASE = 100.0


def ieee14_model() -> tuple[list[Hat], list[str], np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Tap'lı hatları yaklaşık π modeli ile Ybus'a gömer (off-nominal tap)."""
    n = 14
    tip_map = {1: PQ, 2: PV, 3: SLACK}
    tip = [tip_map[int(BUS[i, 4])] for i in range(n)]
    p = np.zeros(n)
    q = np.zeros(n)
    v0 = np.ones(n)
    for i in range(n):
        p[i] -= BUS[i, 1] / SBASE
        q[i] -= BUS[i, 2] / SBASE
        v0[i] = BUS[i, 3]
    for g in GEN:
        bi = int(g[0]) - 1
        p[bi] += g[1] / SBASE
        # PV/slack için Q başlangıç tahmini; NR Q'yu serbest bırakır
        if tip[bi] == PQ:
            q[bi] += g[2] / SBASE
        v0[bi] = g[3]

    # Bara 9 şönt kapasitör (MATPOWER Bs=19 Mvar → +0.19 pu @ V=1)
    q[8] += 0.19

    hatlar: list[Hat] = []
    y_extra = np.zeros((n, n), dtype=complex)
    for br in BRANCH:
        i, j = int(br[0]) - 1, int(br[1]) - 1
        r, x, b, tap = br[2], br[3], br[4], br[5]
        if abs(tap - 1.0) < 1e-9:
            hatlar.append(Hat(i, j, r, x, b))
        else:
            # Off-nominal tap: from-side tap a, y = 1/(r+jx)
            y = 1 / complex(r, x) if (r or x) else 0j
            a = tap
            y_extra[i, i] += y / (a * a) + 1j * b / 2
            y_extra[j, j] += y + 1j * b / 2
            y_extra[i, j] -= y / a
            y_extra[j, i] -= y / a
    return hatlar, tip, p, q, v0, y_extra


def coz_nr():
    hatlar, tip, p, q, v0, y_extra = ieee14_model()  # type: ignore[misc]
    y_bus = ybus_kur(14, hatlar) + y_extra
    # Slack P bilinmiyor; GEN'deki Pg başlangıç tahminidir, NR slack P'yi serbest bırakır
    # PV baralarda P sabit, V sabit
    sonuc = nr_coz(y_bus, tip, p, q, v0, tol=1e-8, azami_iterasyon=40)
    return sonuc, y_bus


def coz_pandapower():
    import pandapower as pp
    import pandapower.networks as pn

    net = pn.case14()
    pp.runpp(net, algorithm="nr", calculate_voltage_angles=True)
    v = net.res_bus.vm_pu.to_numpy()
    teta = np.deg2rad(net.res_bus.va_degree.to_numpy())
    return v, teta, net


def main() -> None:
    sonuc, _ = coz_nr()
    print("=== Kendi NR (IEEE 14) ===")
    print(f"iterasyon: {sonuc.iterasyon}")
    print(f"artıklar: {[f'{a:.2e}' for a in sonuc.artiklar]}")
    print("bara | V(pu)  | açı(°)  | P(pu)   | Q(pu)")
    for i in range(14):
        print(
            f"{i+1:4d} | {sonuc.v[i]:6.4f} | {np.degrees(sonuc.teta[i]):7.3f} | "
            f"{sonuc.s.real[i]:7.4f} | {sonuc.s.imag[i]:7.4f}"
        )

    out = {
        "kaynak": "numpy-nr",
        "iterasyon": sonuc.iterasyon,
        "artiklar": sonuc.artiklar,
        "v": sonuc.v.tolist(),
        "teta_deg": np.degrees(sonuc.teta).tolist(),
        "p": sonuc.s.real.tolist(),
        "q": sonuc.s.imag.tolist(),
    }

    try:
        v_pp, teta_pp, _ = coz_pandapower()
        dv = np.abs(sonuc.v - v_pp)
        da = np.abs(np.degrees(sonuc.teta - teta_pp))
        print("\n=== pandapower karşılaştırması ===")
        print(f"max |ΔV|  = {dv.max():.4e} pu")
        print(f"max |Δθ|  = {da.max():.4e} derece")
        print("bara | V_NR   | V_pp   | ΔV      | θ_NR    | θ_pp    | Δθ")
        for i in range(14):
            print(
                f"{i+1:4d} | {sonuc.v[i]:6.4f} | {v_pp[i]:6.4f} | {dv[i]:.2e} | "
                f"{np.degrees(sonuc.teta[i]):7.3f} | {np.degrees(teta_pp[i]):7.3f} | {da[i]:.2e}"
            )
        out["pandapower"] = {
            "v": v_pp.tolist(),
            "teta_deg": np.degrees(teta_pp).tolist(),
            "max_dv": float(dv.max()),
            "max_dtheta_deg": float(da.max()),
        }
        if dv.max() > 5e-3 or da.max() > 0.5:
            print("\nUyarı: sapma beklenenden büyük (tap modeli / Q şönt farkı olabilir).")
        else:
            print("\nDoğrulama OK: NR ile pandapower uyumlu.")
    except ImportError:
        print("\npandapower kurulu değil → yalnız kendi NR çalıştı.")
        print("Kurulum: pip install pandapower")

    hedef = Path(__file__).with_name("ieee14_sonuc.json")
    hedef.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\nSonuç yazıldı: {hedef.name}")


if __name__ == "__main__":
    main()
