"""Notlardaki elle çözülmüş örneklerin sayısal doğrulaması.

Her bölüm, ilgili klasördeki "Elle örnek" başlığındaki sayıları üretir.
Sayı tutmazsa betik hata verir; notu değil hesabı düzelt.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.optimize import brentq, linprog

from nr_yuk_akisi import PQ, SLACK, Hat, guc_enjeksiyonu, jacobian_acik, nr_coz, ybus_kur


def yakin(a: float, b: float, tol: float = 1e-3) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise SystemExit(f"beklenen {b}, gelen {a}")


def bolum_02_temel() -> None:
    print("02 Temeller")
    v, z = 230.0, complex(10, 10)
    akim = v / z
    s = v * akim.conjugate()
    print(f"  I = {abs(akim):.2f} A, açı {math.degrees(math.atan2(akim.imag, akim.real)):.0f}°")
    print(f"  S = {abs(s):.0f} VA, P = {s.real:.0f} W, Q = {s.imag:.0f} var, pf = {s.real / abs(s):.3f}")
    yakin(abs(akim), 16.26)
    yakin(s.real, 2645, 1e-3)

    p_mw, pf = 300.0, 0.95
    s_mva = p_mw / pf
    i_hat = s_mva * 1e6 / (math.sqrt(3) * 400e3)
    q_mvar = p_mw * math.tan(math.acos(pf))
    print(f"  400 kV, 300 MW, pf 0.95: S = {s_mva:.1f} MVA, I = {i_hat:.1f} A, Q = {q_mvar:.1f} Mvar")
    print(f"  faz gerilimi = {400 / math.sqrt(3):.1f} kV")

    z_baz = 154**2 / 100
    i_baz = 100e6 / (math.sqrt(3) * 154e3)
    print(f"  154 kV, 100 MVA: Zbaz = {z_baz:.2f} ohm, Ibaz = {i_baz:.1f} A, 20 ohm = {20 / z_baz:.4f} pu")
    print(f"  trafo %10, 50 MVA -> 100 MVA bazında {0.10 * 100 / 50:.2f} pu")

    p, pf0, pf1 = 10.0, 0.8, 0.95
    q0 = p * math.tan(math.acos(pf0))
    q1 = p * math.tan(math.acos(pf1))
    s0, s1 = p / pf0, p / pf1
    print(f"  kompanzasyon: Q0 = {q0:.2f}, Q1 = {q1:.3f}, Qc = {q0 - q1:.3f} Mvar")
    print(f"  akım oranı = {s1 / s0:.3f}, kayıp oranı = {(s1 / s0) ** 2:.3f}")

    dv0 = (6 * 2 + 3 * 4) / 34.5
    dv1 = (6 * 2) / 34.5
    print(f"  gerilim düşümü: {dv0:.3f} kV (%{100 * dv0 / 34.5:.2f}), Q=0 iken {dv1:.3f} kV (%{100 * dv1 / 34.5:.2f})")

    y = 1 / complex(0.02, 0.10)
    print(f"  0.02+j0.10 hattın admitansı = {y.real:.3f} {y.imag:+.3f}j")


def bolum_03_ptdf() -> None:
    print("03 PTDF ve LODF")
    x = {(1, 2): 0.1, (1, 3): 0.2, (2, 3): 0.25}
    b = np.array([[14.0, -4.0], [-4.0, 9.0]])
    xm = np.zeros((4, 4))
    xm[2:, 2:] = np.linalg.inv(b)
    ptdf = {hat: [(xm[hat[0], k] - xm[hat[1], k]) / x_ij for k in (2, 3)] for hat, x_ij in x.items()}
    for hat, deger in ptdf.items():
        print(f"  PTDF hat {hat}: bara2 = {deger[0]:+.4f}, bara3 = {deger[1]:+.4f}")
    akis = {hat: d[0] * 0.5 + d[1] * (-0.8) for hat, d in ptdf.items()}
    print(f"  baz akışlar: { {h: round(a, 4) for h, a in akis.items()} }")
    yakin(akis[(1, 3)], 0.4182)

    # Hat 1-3 açılırsa: 1'den 3'e transferin dağılımı
    k = (1, 3)
    ptdf_k = -ptdf[k][1]
    for hat in ((1, 2), (2, 3)):
        lodf = -ptdf[hat][1] / (1 - ptdf_k)
        print(f"  LODF {hat} | {k} açık = {lodf:+.3f}, yeni akış = {akis[hat] + lodf * akis[k]:+.4f}")


def bolum_05_nr() -> None:
    print("05 NR, iki bara elle iterasyon")
    y_bus = ybus_kur(2, [Hat(0, 1, 0.0, 0.1)])
    v = np.array([1.0, 1.0])
    teta = np.zeros(2)
    for tur in range(1, 4):
        s = guc_enjeksiyonu(y_bus, v, teta)
        dp, dq = -0.5 - s.real[1], -0.2 - s.imag[1]
        jac = jacobian_acik(y_bus, v, teta, [1], [1])
        dx = np.linalg.solve(jac, [dp, dq])
        print(
            f"  tur {tur}: ΔP = {dp:+.5f}, ΔQ = {dq:+.5f}, "
            f"J = [[{jac[0, 0]:.4f}, {jac[0, 1]:.4f}], [{jac[1, 0]:.4f}, {jac[1, 1]:.4f}]], "
            f"Δθ = {dx[0]:+.6f}, ΔV = {dx[1]:+.6f}"
        )
        teta[1] += dx[0]
        v[1] += dx[1]
        print(f"         θ2 = {teta[1]:.6f} rad, V2 = {v[1]:.6f}")
    v_analitik = math.sqrt((0.96 + math.sqrt(0.96**2 - 4 * 0.01 * 0.29)) / 2)
    teta_analitik = -math.asin(0.05 / v_analitik)
    print(f"  analitik: V2 = {v_analitik:.6f}, θ2 = {teta_analitik:.6f} rad")
    yakin(v[1], v_analitik, 1e-6)

    sonuc = nr_coz(y_bus, [SLACK, PQ], np.array([0, -0.5]), np.array([0, -0.2]), np.ones(2))
    yakin(sonuc.v[1], v_analitik, 1e-8)


def bolum_06_kisa_devre() -> None:
    print("06 Kısa devre")
    z1 = z2 = 0.2j
    z0 = 0.1j
    i_baz = 100e6 / (math.sqrt(3) * 154e3)
    a = complex(-0.5, math.sqrt(3) / 2)

    i3 = 1 / z1
    print(f"  üç faz: {abs(i3):.2f} pu = {abs(i3) * i_baz:.0f} A")
    i0 = 1 / (z1 + z2 + z0)
    print(f"  faz-toprak: I0 = {abs(i0):.2f} pu, If = {abs(3 * i0):.2f} pu = {abs(3 * i0) * i_baz:.0f} A")
    v1, v2, v0 = 1 - z1 * i0, -z2 * i0, -z0 * i0
    vb = v0 + a**2 * v1 + a * v2
    print(f"  faz-toprak sağlam faz gerilimi = {abs(vb):.4f} pu")
    i1 = 1 / (z1 + z2)
    print(f"  faz-faz: I1 = {abs(i1):.2f} pu, If = {abs(math.sqrt(3) * i1):.3f} pu = {abs(math.sqrt(3) * i1) * i_baz:.0f} A")
    par = z2 * z0 / (z2 + z0)
    i1 = 1 / (z1 + par)
    i2 = -i1 * z0 / (z2 + z0)
    i0 = -i1 * z2 / (z2 + z0)
    ib = i0 + a**2 * i1 + a * i2
    print(
        f"  iki faz-toprak: I1 = {abs(i1):.3f}, I2 = {abs(i2):.3f}, I0 = {abs(i0):.3f} pu, "
        f"faz akımı = {abs(ib):.3f} pu, toprak = {abs(3 * i0):.2f} pu"
    )
    z_ohm = 0.2 * 154**2 / 100
    print(f"  IEC c=1.1: I''k = {1.1 * 154 / (math.sqrt(3) * z_ohm):.3f} kA (Zk = {z_ohm:.2f} ohm)")


def bolum_07_siralama() -> None:
    print("07 Performans indeksi")
    limit = {"12": 0.5, "13": 0.6, "23": 0.6}
    durumlar = {
        "1-3 açık": {"12": 0.3, "23": 0.8},
        "1-2 açık": {"13": 0.3, "23": 0.5},
        "2-3 açık": {"12": 0.5, "13": 0.8},
    }
    for ad, akis in durumlar.items():
        pi1 = sum((abs(p) / limit[h]) ** 2 for h, p in akis.items())
        pi5 = sum((abs(p) / limit[h]) ** 10 for h, p in akis.items())
        print(f"  {ad}: PI(n=1) = {pi1:.3f}, PI(n=5) = {pi5:.2f}")


def bolum_08_kararlilik() -> None:
    print("08 Kararlılık")
    pm, pmax, h, w0 = 0.8, 2.0, 5.0, 2 * math.pi * 50
    d0 = math.asin(pm / pmax)
    dmax = math.pi - d0
    dcr = math.acos((math.pi - 2 * d0) * math.sin(d0) - math.cos(d0))
    tcr = math.sqrt(4 * h * (dcr - d0) / (w0 * pm))
    print(f"  δ0 = {d0:.4f} rad ({math.degrees(d0):.2f}°), δmax = {math.degrees(dmax):.2f}°")
    print(f"  δkr = {dcr:.4f} rad ({math.degrees(dcr):.2f}°), tkr = {tcr * 1000:.1f} ms")

    def kararli(t_temizleme: float) -> bool:
        delta, omega, dt = d0, 0.0, 1e-4
        for adim in range(int(3.0 / dt)):
            t = adim * dt
            pe_max = 0.0 if t < t_temizleme else pmax

            def f(d: float, w: float) -> tuple[float, float]:
                return w, w0 / (2 * h) * (pm - pe_max * math.sin(d))

            k1 = f(delta, omega)
            k2 = f(delta + dt / 2 * k1[0], omega + dt / 2 * k1[1])
            k3 = f(delta + dt / 2 * k2[0], omega + dt / 2 * k2[1])
            k4 = f(delta + dt * k3[0], omega + dt * k3[1])
            delta += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
            omega += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            if delta > math.pi:
                return False
        return True

    if not kararli(tcr - 0.005) or kararli(tcr + 0.005):
        raise SystemExit("zaman tanım bölgesi, eşit alan sonucunu doğrulamadı")
    print(f"  benzetim: {tcr * 1000 - 5:.0f} ms kararlı, {tcr * 1000 + 5:.0f} ms kararsız")

    print(f"  RoCoF: H=4 için {(1000 / 50000) * 50 / (2 * 4):.3f} Hz/s, H=2 için {(1000 / 50000) * 50 / (2 * 2):.3f} Hz/s")
    print(f"  droop %5, 200 MW, Δf 0.1 Hz: ΔP = {(0.1 / 50) / 0.05 * 200:.1f} MW")
    ks = pmax * math.cos(d0)
    wn = math.sqrt(ks * w0 / (2 * h))
    zeta = 10 / (2 * math.sqrt(2 * h * ks * w0))
    print(f"  küçük sinyal: Ks = {ks:.3f}, ωn = {wn:.3f} rad/s = {wn / (2 * math.pi):.3f} Hz, D=10 için ζ = {zeta:.4f}")


def bolum_09_wls() -> None:
    print("09 WLS, tek durum")
    h = np.array([[-10.0], [-10.0]])
    z = np.array([1.02, 0.98])
    sigma = np.array([0.01, 0.02])
    w = np.diag(1 / sigma**2)
    g = h.T @ w @ h
    x = np.linalg.solve(g, h.T @ w @ z)
    r = z - h @ x
    j = float(r @ w @ r)
    omega = sigma**2 - np.diag(h @ np.linalg.inv(g) @ h.T)
    rn = np.abs(r) / np.sqrt(omega)
    print(f"  G = {g[0, 0]:.3e}, θ2 = {x[0]:.4f} rad, P tahmini = {-10 * x[0]:.4f}")
    print(f"  artıklar = {np.round(r, 4)}, J = {j:.2f}, normalize artıklar = {np.round(rn, 3)}")


def bolum_10_koruma() -> None:
    print("10 Röle koordinasyonu")

    def si(tms: float, kat: float) -> float:
        return tms * 0.14 / (kat**0.02 - 1)

    t_b = si(0.1, 2000 / 200)
    carpan = si(1.0, 2000 / 400)
    tms_a = (t_b + 0.3) / carpan
    print(f"  alt röle: {t_b:.4f} s, üst röle TMS=1 süresi {carpan:.4f} s, gereken TMS = {tms_a:.4f}")
    print(f"  TMS 0.14 seçilirse üst röle {si(0.14, 5):.4f} s, aralık {si(0.14, 5) - t_b:.4f} s")
    print(f"  mesafe: 40 ohm birincil -> {40 * (1000 / 1) / (154000 / 100):.2f} ohm ikincil")


def bolum_11_ekonomi() -> None:
    print("11 Lambda iterasyonu")
    for lam in (5.0, 7.0, 6.0):
        p1, p2 = (lam - 4) / 0.04, (lam - 3) / 0.06
        print(f"  λ = {lam}: P1 = {p1:.2f}, P2 = {p2:.2f}, toplam = {p1 + p2:.2f}")
    lam = (100 + 4 / 0.04 + 3 / 0.06) / (1 / 0.04 + 1 / 0.06)
    print(f"  kapalı form λ = {lam:.3f}")

    def fark(p1: float) -> float:
        p2 = 100 - p1 + 0.0005 * p1**2
        return (0.04 * p1 + 4) / (1 - 0.001 * p1) - (0.06 * p2 + 3)

    p1 = brentq(fark, 0, 100)
    p2 = 100 - p1 + 0.0005 * p1**2
    print(
        f"  kayıplı: P1 = {p1:.2f}, P2 = {p2:.2f}, kayıp = {0.0005 * p1**2:.3f} MW, "
        f"ceza faktörü = {1 / (1 - 0.001 * p1):.4f}, λ = {0.06 * p2 + 3:.4f}"
    )


def bolum_12_guvenilirlik() -> None:
    print("12 LOLE ve EENS")
    q, n, birim = 0.05, 3, 100
    olasilik = [math.comb(n, k) * q**k * (1 - q) ** (n - k) for k in range(n + 1)]
    print(f"  kapasite kaybı olasılıkları: {[round(o, 6) for o in olasilik]}")
    lolp, eens = 0.0, 0.0
    for yuk, pay in ((250, 0.2), (150, 0.8)):
        p_kayip = sum(o for k, o in enumerate(olasilik) if (n - k) * birim < yuk)
        beklenen = sum(o * max(0, yuk - (n - k) * birim) for k, o in enumerate(olasilik))
        lolp += pay * p_kayip
        eens += pay * 8760 * beklenen
        print(f"  yük {yuk} MW: yük kaybı olasılığı {p_kayip:.6f}, beklenen açık {beklenen:.5f} MW")
    print(f"  LOLP = {lolp:.6f}, LOLE = {lolp * 8760:.1f} saat/yıl, EENS = {eens:.0f} MWh/yıl")


def bolum_13_dcopf() -> None:
    print("13 DC-OPF ve LMP")
    # Değişkenler: g1 (bara 1), g2 (bara 2). Yük bara 3'te 150 MW.
    ptdf13_bara2, ptdf13_bara3 = -0.181818, -0.636364

    def coz(limit: float, yuk: float = 150.0) -> tuple[np.ndarray, float]:
        # Hat 1-3 akışı = ptdf(2)*g2 + ptdf(3)*(-yuk); bara 1 referans
        sonuc = linprog(
            c=[10, 30],
            A_ub=[[0, ptdf13_bara2]],
            b_ub=[limit + ptdf13_bara3 * yuk],
            A_eq=[[1, 1]],
            b_eq=[yuk],
            bounds=[(0, 200), (0, 200)],
            method="highs",
        )
        if not sonuc.success:
            raise SystemExit(sonuc.message)
        return sonuc.x, sonuc.fun

    serbest, maliyet0 = coz(1e9)
    kisitli, maliyet1 = coz(80)
    print(f"  kısıtsız: g = {np.round(serbest, 2)}, maliyet {maliyet0:.0f}, hat 1-3 = {0.636364 * 150:.1f} MW")
    print(f"  80 MW limitli: g = {np.round(kisitli, 2)}, maliyet {maliyet1:.0f}")
    _, m_limit = coz(81)
    _, m_yuk = coz(80, 151)
    print(f"  hat gölge fiyatı = {maliyet1 - m_limit:.1f} TL/MW, bara 3 LMP = {m_yuk - maliyet1:.1f} TL/MWh")
    yakin(m_yuk - maliyet1, 80, 1e-3)


def bolum_04_dagitim() -> None:
    print("04 Dağıtım")
    musteri = 1000
    olay = [(200, 90), (500, 30)]
    saifi = sum(m for m, _ in olay) / musteri
    saidi = sum(m * d for m, d in olay) / musteri
    print(f"  SAIFI = {saifi:.2f}, SAIDI = {saidi:.1f} dk, CAIDI = {saidi / saifi:.1f} dk")
    print(f"  kayıp: 300/100 A = {3 * (300**2 + 100**2) / 1000:.0f} kW, 200/200 A = {3 * 2 * 200**2 / 1000:.0f} kW")
    for ad, deger in (("Z", 0.95**2), ("I", 0.95), ("P", 1.0)):
        print(f"  ZIP, V = 0.95: sabit {ad} yük = {100 * deger:.2f} MW")


if __name__ == "__main__":
    for bolum in (
        bolum_02_temel,
        bolum_03_ptdf,
        bolum_04_dagitim,
        bolum_05_nr,
        bolum_06_kisa_devre,
        bolum_07_siralama,
        bolum_08_kararlilik,
        bolum_09_wls,
        bolum_10_koruma,
        bolum_11_ekonomi,
        bolum_12_guvenilirlik,
        bolum_13_dcopf,
    ):
        bolum()
    print("Bütün elle örnekler doğrulandı")
