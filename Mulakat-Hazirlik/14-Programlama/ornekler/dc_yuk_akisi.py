"""Üç baralık DC yük akışı.

Bara 1 salınım barası, açısı 0. Enjeksiyon üretimde pozitif.
x12 = 0.1, x13 = 0.2, x23 = 0.25 pu.
P2 = 0.5 pu, P3 = -0.8 pu.

Elle sonuç:
  θ2 =  0.01181818 rad
  θ3 = -0.08363636 rad
  P1 =  0.3 pu
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def dc_yuk_akisi(
    x: dict[tuple[int, int], float],
    p_enjeksiyon: dict[int, float],
    slack: int = 1,
) -> tuple[NDArray[np.floating], float]:
    baralar = sorted({b for hat in x for b in hat} | set(p_enjeksiyon) | {slack})
    if slack not in baralar:
        raise ValueError("salınım barası şebekede yok")

    bilinmeyen = [b for b in baralar if b != slack]
    indeks = {b: i for i, b in enumerate(bilinmeyen)}
    b_mat = np.zeros((len(bilinmeyen), len(bilinmeyen)))

    for (i, j), x_ij in x.items():
        if x_ij <= 0:
            raise ValueError("reaktans pozitif olmalı")
        b_ij = 1.0 / x_ij
        for a, c, isaret in ((i, j, -1.0), (j, i, -1.0)):
            if a != slack and c != slack:
                b_mat[indeks[a], indeks[c]] += isaret * b_ij
        for a in (i, j):
            if a != slack:
                b_mat[indeks[a], indeks[a]] += b_ij

    p = np.array([p_enjeksiyon.get(b, 0.0) for b in bilinmeyen])
    try:
        teta_bilinmeyen = np.linalg.solve(b_mat, p)
    except np.linalg.LinAlgError as hata:
        raise ValueError("şebeke ada içeriyor veya reaktans hatalı") from hata

    teta = {slack: 0.0}
    teta.update(zip(bilinmeyen, teta_bilinmeyen))

    p_slack = 0.0
    for (i, j), x_ij in x.items():
        if i == slack or j == slack:
            p_slack += (teta[slack] - teta[i if j == slack else j]) / x_ij

    sirali = np.array([teta[b] for b in baralar])
    return sirali, float(p_slack)


def hat_akisi(
    x: dict[tuple[int, int], float],
    teta: dict[int, float],
) -> dict[tuple[int, int], float]:
    return {hat: (teta[i] - teta[j]) / x_ij for hat, (i, j, x_ij) in (
        (k, (*k, v)) for k, v in x.items()
    )}


def _ornek() -> None:
    x = {(1, 2): 0.1, (1, 3): 0.2, (2, 3): 0.25}
    p = {2: 0.5, 3: -0.8}
    teta, p1 = dc_yuk_akisi(x, p)
    beklenen = np.array([0.0, 1.3 / 110, -9.2 / 110])
    if not np.allclose(teta, beklenen, atol=1e-9):
        raise SystemExit(f"açı beklenenden saptı: {teta}")
    if not np.isclose(p1, 0.3, atol=1e-9):
        raise SystemExit(f"salınım barası gücü 0.3 olmalı, gelen {p1}")

    akis = hat_akisi(x, {1: teta[0], 2: teta[1], 3: teta[2]})
    # Bara 2 dengesi: -P12 + P23 = 0.5
    denge2 = -akis[(1, 2)] + akis[(2, 3)]
    denge3 = -akis[(1, 3)] - akis[(2, 3)]
    if not np.isclose(denge2, 0.5) or not np.isclose(denge3, -0.8):
        raise SystemExit("hat akışları bara dengesini tutmuyor")

    print("DC yük akışı doğrulandı")
    print(f"  açılar rad: {teta}")
    print(f"  P1 pu: {p1:.4f}")
    for hat, p_hat in akis.items():
        print(f"  P{hat[0]}{hat[1]} pu: {p_hat:.4f}")


if __name__ == "__main__":
    _ornek()
