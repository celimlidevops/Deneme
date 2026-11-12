"""İki üniteli ekonomik dağıtım.

C1 = 0.02 P1² + 4 P1
C2 = 0.03 P2² + 3 P2
P1 + P2 = 100 MW

Limitsiz eşit λ: P1 = P2 = 50 MW, λ = 6.
P1 ≤ 40 olunca P1 = 40, P2 = 60, λ = 6.6 (P2'nin artan maliyeti).
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


def artan_maliyet(p: np.ndarray) -> np.ndarray:
    return np.array([0.04 * p[0] + 4.0, 0.06 * p[1] + 3.0])


def maliyet(p: np.ndarray) -> float:
    return float(0.02 * p[0] ** 2 + 4 * p[0] + 0.03 * p[1] ** 2 + 3 * p[1])


def dagit(p_min: np.ndarray, p_max: np.ndarray, talep: float) -> np.ndarray:
    def amaç(p: np.ndarray) -> float:
        return maliyet(p)

    kisit = {"type": "eq", "fun": lambda p: p[0] + p[1] - talep}
    sinir = list(zip(p_min, p_max))
    sonuc = minimize(
        amaç,
        x0=np.array([talep / 2, talep / 2]),
        method="SLSQP",
        bounds=sinir,
        constraints=kisit,
    )
    if not sonuc.success:
        raise RuntimeError(sonuc.message)
    return sonuc.x


def _ornek() -> None:
    serbest = dagit(np.array([0.0, 0.0]), np.array([100.0, 100.0]), 100.0)
    if not np.allclose(serbest, [50.0, 50.0], atol=1e-6):
        raise SystemExit(f"limitsiz paylaşım 50-50 olmalı: {serbest}")
    if not np.allclose(artan_maliyet(serbest), [6.0, 6.0], atol=1e-6):
        raise SystemExit("λ eşitlenmedi")

    limitli = dagit(np.array([0.0, 0.0]), np.array([40.0, 100.0]), 100.0)
    if not np.allclose(limitli, [40.0, 60.0], atol=1e-6):
        raise SystemExit(f"limitli paylaşım 40-60 olmalı: {limitli}")
    lam = artan_maliyet(limitli)
    if lam[0] >= lam[1]:
        raise SystemExit("limitteki ünitenin artan maliyeti, serbest üniteden küçük kalmalı")

    print("Ekonomik dağıtım doğrulandı")
    print(f"  limitsiz MW: {serbest}, λ: {artan_maliyet(serbest)[0]:.2f}")
    print(f"  P1 max 40 MW: {limitli}, artan maliyet: {lam}")


if __name__ == "__main__":
    _ornek()
