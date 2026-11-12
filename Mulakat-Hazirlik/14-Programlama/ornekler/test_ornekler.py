"""Yük akışı testleri. `pytest` ile ya da doğrudan `python test_ornekler.py` ile çalışır.

Her test bir iddiadır: analitik çözüm, güç dengesi, iki Jacobian'ın eşitliği,
Q limitinde bara tipinin değişmesi, çözümsüz durumda hatanın sessiz kalmaması.
"""

from __future__ import annotations

import math

import numpy as np

from nr_yuk_akisi import (
    PQ,
    PV,
    SLACK,
    Hat,
    YakinsamaHatasi,
    hat_kaybi,
    jacobian_acik,
    jacobian_matris,
    nr_coz,
    ornek_sebeke,
    ybus_kur,
)


def test_iki_bara_analitik_cozum() -> None:
    y_bus = ybus_kur(2, [Hat(0, 1, 0.0, 0.1)])
    sonuc = nr_coz(y_bus, [SLACK, PQ], np.array([0, -0.5]), np.array([0, -0.2]), np.ones(2))
    v = math.sqrt((0.96 + math.sqrt(0.96**2 - 4 * 0.01 * 0.29)) / 2)
    assert math.isclose(sonuc.v[1], v, abs_tol=1e-9)
    assert math.isclose(sonuc.teta[1], -math.asin(0.05 / v), abs_tol=1e-9)


def test_guc_dengesi_kayba_esit() -> None:
    hatlar, tip, p, q, v0 = ornek_sebeke()
    sonuc = nr_coz(ybus_kur(3, hatlar), tip, p, q, v0)
    assert math.isclose(sonuc.s.real.sum(), hat_kaybi(hatlar, sonuc.v, sonuc.teta), abs_tol=1e-8)
    assert math.isclose(sonuc.v[1], 1.02, abs_tol=1e-12), "PV barada gerilim sabit kalmalı"


def test_iki_jacobian_ayni() -> None:
    hatlar, *_ = ornek_sebeke()
    y_bus = ybus_kur(3, hatlar)
    v = np.array([1.0, 1.02, 0.97])
    teta = np.array([0.0, 0.03, -0.08])
    acik = jacobian_acik(y_bus, v, teta, [1, 2], [2])
    matris = jacobian_matris(y_bus, v, teta, [1, 2], [2])
    assert np.allclose(acik, matris, atol=1e-12)


def test_q_limiti_pv_barayi_pq_yapar() -> None:
    hatlar, tip, p, q, v0 = ornek_sebeke()
    sonuc = nr_coz(ybus_kur(3, hatlar), tip, p, q, v0, q_max=np.array([9.0, 0.10, 9.0]))
    assert sonuc.tip[1] == PQ
    assert math.isclose(sonuc.s.imag[1], 0.10, abs_tol=1e-8)
    assert sonuc.v[1] < 1.02, "reaktif sınırlanınca gerilim ayar değerinin altına düşer"


def test_limit_bol_ise_bara_pv_kalir() -> None:
    hatlar, tip, p, q, v0 = ornek_sebeke()
    sonuc = nr_coz(ybus_kur(3, hatlar), tip, p, q, v0, q_max=np.array([9.0, 9.0, 9.0]))
    assert sonuc.tip[1] == PV


def test_cozumsuz_yuk_sessiz_kalmaz() -> None:
    # x = 0.1 hatta aktarılabilecek azami güç yaklaşık 5 pu; 8 pu'nun çözümü yok.
    y_bus = ybus_kur(2, [Hat(0, 1, 0.0, 0.1)])
    try:
        nr_coz(y_bus, [SLACK, PQ], np.array([0, -8.0]), np.array([0, -2.0]), np.ones(2))
    except YakinsamaHatasi as hata:
        assert hata.artiklar, "teşhis için artık geçmişi dönmeli"
    else:
        raise AssertionError("çözümsüz durumda hata bekleniyordu")


def test_sifir_empedans_reddedilir() -> None:
    try:
        ybus_kur(2, [Hat(0, 1, 0.0, 0.0)])
    except ValueError:
        return
    raise AssertionError("sıfır empedans kabul edilmemeli")


if __name__ == "__main__":
    testler = [(ad, f) for ad, f in sorted(globals().items()) if ad.startswith("test_")]
    for ad, f in testler:
        f()
        print(f"gecti  {ad}")
    print(f"{len(testler)} test gecti")
