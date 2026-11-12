"""Üç baralık doğrusal (DC) durum kestirimi ve bir kötü veri.

Aynı şebeke: x12=0.1, x13=0.2, x23=0.25.
Gerçek durum θ2=1.3/110, θ3=-9.2/110, θ1=0.

Ölçümler hat akışları ve P2 enjeksiyonu. Temiz sette kestirim
gerçek açıyı bulur. P23 bozulunca en büyük normalize artık ona işaret eder.
"""

from __future__ import annotations

import numpy as np


def kestir(
    h: np.ndarray,
    z: np.ndarray,
    sigma: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, float]:
    w = np.diag(1.0 / sigma**2)
    g = h.T @ w @ h
    x = np.linalg.solve(g, h.T @ w @ z)
    r = z - h @ x
    # Artık kovaryansının köşegeni: Ω = R - H G^{-1} Hᵀ
    omega = sigma**2 - np.sum((h @ np.linalg.inv(g)) * h, axis=1)
    if np.any(omega < -1e-10):
        raise ValueError("artık varyansı negatif, model hatalı")
    omega = np.clip(omega, 1e-14, None)
    r_n = np.abs(r) / np.sqrt(omega)
    j = float(r.T @ w @ r)
    return x, r_n, j


def _model() -> tuple[np.ndarray, np.ndarray]:
    # Sütunlar: θ2, θ3
    # P12 = -10 θ2
    # P13 = -5 θ3
    # P23 = 4 θ2 - 4 θ3
    # P2  = 14 θ2 - 4 θ3
    h = np.array(
        [
            [-10.0, 0.0],
            [0.0, -5.0],
            [4.0, -4.0],
            [14.0, -4.0],
        ]
    )
    teta = np.array([1.3 / 110, -9.2 / 110])
    return h, teta


def _ornek() -> None:
    h, teta = _model()
    z = h @ teta
    sigma = np.array([0.01, 0.01, 0.01, 0.02])
    x, r_n, j = kestir(h, z, sigma)
    if not np.allclose(x, teta, atol=1e-9):
        raise SystemExit(f"temiz kestirim sapması: {x}")
    if j > 1e-8 or np.max(r_n) > 1e-6:
        raise SystemExit("temiz sette artık kalmamalı")

    z_bozuk = z.copy()
    z_bozuk[2] += 0.25
    _, r_n_bozuk, j_bozuk = kestir(h, z_bozuk, sigma)
    suclu = int(np.argmax(r_n_bozuk))
    if suclu != 2:
        raise SystemExit(f"kötü veri P23 olmalı, işaret edilen {suclu}")
    if not (r_n_bozuk[2] > 3 and j_bozuk > 20):
        raise SystemExit("kötü veri eşiği oluşmadı")

    adlar = ["P12", "P13", "P23", "P2"]
    print("Durum kestirimi doğrulandı")
    print(f"  temiz açı: {x}")
    print(f"  bozuk J: {j_bozuk:.1f}")
    for ad, deger in zip(adlar, r_n_bozuk):
        print(f"  normalize artık {ad}: {deger:.2f}")
    print(f"  işaret edilen ölçüm: {adlar[suclu]}")


if __name__ == "__main__":
    _ornek()
