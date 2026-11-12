# Salınım denklemi ve eşit alan ölçütü: çiz, anlat, elle çöz

Panel tahtaya çizmeni isteyebilir. Bu sayfayı kâğıda üç kez çizmeden mülakata girme.

## Fiziksel resim

Senkron generatör, türbinin döndürdüğü büyük bir kütledir. Üzerinde iki tork yarışır:

| Güç | Nereden gelir | Hızı |
| --- | --- | --- |
| **Mekanik güç `P_m`** | Türbinden | Buhar veya su vanası yavaştır; arıza süresince sabit kabul edilir |
| **Elektriksel güç `P_e`** | Şebekeye verilen güç | Şebeke koşullarına anında tepki verir |

İkisinin farkı rotorun ne yapacağını belirler:

- İkisi eşitse rotor sabit hızla döner.
- `P_m > P_e` ise rotor hızlanır.
- `P_m < P_e` ise yavaşlar.

Bu, Newton'un ikinci yasasının dönen kütle için yazılmış halidir.

```
(2H / ω_0) × d²δ/dt² = P_m − P_e          (pu)
```

`pu` (per unit, birim değer), büyüklüklerin bir baz değere bölünmüş halidir.

- `δ`: rotor açısı. Rotorun, şebekeyle eşzamanlı dönen referansa göre ne kadar önde olduğu.
- `H`: atalet sabiti, saniye. Anma hızında depolanan kinetik enerjinin anma gücüne oranı. "Bu makine, depoladığı enerjiyle anma gücünü kaç saniye verebilir." Tipik 2–9 s.
- `ω_0 = 2π × 50 = 314 rad/s`.

### Güç–açı eğrisi

Elektriksel güç, tek makine–sonsuz bara modelinde şöyle yazılır. Sonsuz bara, gerilimi ve frekansı hiç değişmeyen dev şebekedir.

```
P_e = (E V / X) sin δ = P_max sin δ
```

- `E`: generatörün iç gerilimi.
- `V`: sonsuz bara gerilimi.
- `X`: aradaki reaktans.

Güç açının **sinüsüyle** gider. Açı 90°'yi geçince daha fazla açı daha az güç demektir. Kararsızlığın kaynağı bu eğridir.

> **Sade anlatım:** Yazılımcı için benzetme: yaylı bir sarkaç. `P_e` geri çağıran kuvvettir; ama yay doğrusal değildir ve belli bir açıdan sonra gevşer.

## Eşit alan ölçütü

Eşit alan ölçütü, diferansiyel denklemi çözmeden kararlılığı söylemenin yoludur. Yalnızca tek makine–sonsuz bara (veya iki makine) için geçerlidir.

Fikir enerji dengesidir:

- Rotor hızlanırken kinetik enerji kazanır.
- Yavaşlarken geri verir.
- Kazandığı enerjinin tamamını, geri dönüşsüz noktaya varmadan geri verebiliyorsa kararlıdır.

`P–δ` düzleminde enerji, **alan**dır.

### Çizim

<div>
<svg viewBox="0 0 500 290" width="100%" style="max-width:560px" role="img" aria-label="Eşit alan ölçütü: güç-açı eğrisi, hızlanma alanı A1 ve yavaşlama alanı A2">
<rect x="112.4" y="168" width="146.2" height="72" fill="#d9534f" fill-opacity="0.35"/>
<path d="M258.6,168.0 L258.6,60.0 L267.9,60.3 L277.2,61.6 L286.5,63.9 L295.9,67.1 L305.2,71.2 L314.5,76.2 L323.8,82.1 L333.1,88.9 L342.4,96.4 L351.7,104.7 L361.0,113.8 L370.4,123.5 L379.7,133.8 L389.0,144.7 L398.3,156.1 L407.6,168.0 Z" fill="#0f6e56" fill-opacity="0.35"/>
<g fill="none" stroke="currentColor" stroke-width="1.2">
<path d="M60,30 L60,240 L480,240"/>
<path d="M60,168 L480,168" stroke-dasharray="5 4"/>
<path d="M112.4,168 L112.4,240 M258.6,60 L258.6,240 M407.6,168 L407.6,240" stroke-dasharray="2 3"/>
<path stroke-width="2" d="M60.0,240.0 L70.0,225.9 L80.0,211.8 L90.0,198.0 L100.0,184.4 L110.0,171.1 L120.0,158.3 L130.0,146.0 L140.0,134.2 L150.0,123.1 L160.0,112.7 L170.0,103.1 L180.0,94.4 L190.0,86.5 L200.0,79.6 L210.0,73.7 L220.0,68.8 L230.0,65.0 L240.0,62.2 L250.0,60.6 L260.0,60.0 L270.0,60.6 L280.0,62.2 L290.0,65.0 L300.0,68.8 L310.0,73.7 L320.0,79.6 L330.0,86.5 L340.0,94.4 L350.0,103.1 L360.0,112.7 L370.0,123.1 L380.0,134.2 L390.0,146.0 L400.0,158.3 L410.0,171.1 L420.0,184.4 L430.0,198.0 L440.0,211.8 L450.0,225.9 L460.0,240.0"/>
</g>
<g fill="currentColor" font-size="13" font-family="Segoe UI, sans-serif">
<text x="44" y="34" text-anchor="end">P</text>
<text x="484" y="256">δ</text>
<text x="54" y="172" text-anchor="end">P_m</text>
<text x="54" y="64" text-anchor="end">P_max</text>
<text x="112" y="258" text-anchor="middle">δ₀</text>
<text x="258" y="258" text-anchor="middle">δ_c</text>
<text x="408" y="258" text-anchor="middle">π − δ₀</text>
<text x="185" y="210" text-anchor="middle" font-weight="600">A₁ hızlanma</text>
<text x="318" y="135" text-anchor="middle" font-weight="600">A₂ yavaşlama</text>
<text x="150" y="80" text-anchor="middle">P_max sin δ</text>
<text x="185" y="278" text-anchor="middle" font-size="11">arıza sürüyor, P_e = 0</text>
<text x="335" y="278" text-anchor="middle" font-size="11">arıza temizlendi</text>
</g>
</svg>
</div>

Tahtada sırayla çiz:

1. Eksenler.
2. Sinüs eğrisi.
3. Yatay `P_m` çizgisi.
4. Üç dikey çizgi (`δ_0`, `δ_c`, `π − δ_0`).
5. Sonra iki alanı tara.

### Olayların sırası

1. **Arıza öncesi:** `P_m` yatay çizgisi sinüs eğrisini `δ_0`'da keser. Denge noktası.
2. **Arıza anı:** generatör çıkışında üç faz kısa devre. Gerilim çöker, `P_e = 0` olur. Rotor `P_m` ile hızlanır. Açı `δ_0`'dan `δ_c`'ye kayar. `P_m` çizgisinin altındaki dikdörtgen **hızlanma alanı `A_1`**'dir.
3. **Arıza temizlendi:** `δ_c` açısında kesici açar, `P_e` sinüs eğrisine geri sıçrar. Artık `P_e > P_m`, rotor yavaşlar. Ama hızı hâlâ eşzamanlı hızın üstündedir; açı artmaya devam eder. Eğri ile `P_m` çizgisi arasındaki alan **yavaşlama alanı `A_2`**'dir.
4. **Karar:** `δ_max = π − δ_0`'a varmadan `A_2 = A_1` olursa rotor durur ve geri döner: **kararlı**. `δ_max`'ı geçerse `P_e` yeniden `P_m`'in altına düşer, rotor tekrar hızlanır ve geri dönemez: **senkronizmden çıkar**.

Kritik temizleme açısı `δ_kr`, kullanılabilir bütün yavaşlama alanının hızlanma alanına tam eşit olduğu açıdır.

### Türetim (üç satır)

Bu üç satır, iki alanı formülle yazıp eşitler ve kritik açıyı çeker.

- İlk satır: arıza sırasında `P_e = 0` olduğu için hızlanma alanı basit bir dikdörtgendir.
- İkinci satır: yavaşlama alanı, eğri ile `P_m` arasındaki integraldir.
- Üçüncü satır: iki alan eşitlenince `δ_c` yerine sınır değer `δ_kr` gelir.

```
A_1 = P_m (δ_c − δ_0)
A_2 = ∫[δ_c → δ_max] (P_max sin δ − P_m) dδ = P_max (cos δ_c − cos δ_max) − P_m (δ_max − δ_c)

A_1 = A_2   →   cos δ_kr = (P_m / P_max)(δ_max − δ_0) + cos δ_max
```

`δ_max = π − δ_0` ve `P_m / P_max = sin δ_0` yerine konursa formül yalnızca başlangıç açısına bağlı kalır:

```
cos δ_kr = (π − 2δ_0) sin δ_0 − cos δ_0
```

### Açıdan süreye

Kritik açı tek başına yetmez; korumacı milisaniye ister. Açıyı süreye çevirmek için hareket denklemi kullanılır.

Arıza sırasında `P_e = 0` olduğu için ivme sabittir. Sabit ivmeli hareket: `δ(t) = δ_0 + (ω_0 P_m / 4H) t²`. Buradan `t` çekilir:

```
t_kr = √[ 4H (δ_kr − δ_0) / (ω_0 P_m) ]
```

## Elle örnek

Veriler: `P_m = 0,8 pu`, `P_max = 2,0 pu`, `H = 5 s`, 50 Hz. Arıza süresince `P_e = 0`; temizlenince şebeke eski haline döner.

**Adım 1, başlangıç açısı.** Arıza öncesi denge `P_m = P_max sin δ_0` olduğundan buradan `δ_0` bulunur; dönüşsüz açı `δ_max` da ondan çıkar.

```
sin δ_0 = 0,8 / 2,0 = 0,4   →   δ_0 = 0,4115 rad (23,58°)
cos δ_0 = 0,9165
δ_max = π − 0,4115 = 2,730 rad (156,42°)
```

**Adım 2, kritik açı.** `δ_0` değerleri kapalı formüle konur; bu, kesicinin en geç hangi açıda açması gerektiğini verir.

```
cos δ_kr = (3,1416 − 2 × 0,4115) × 0,4 − 0,9165 = 0,9274 − 0,9165 = 0,0109
δ_kr = 1,560 rad (89,4°)
```

**Adım 3, kritik süre.** Kritik açı, sabit ivmeli hareket formülüyle milisaniyeye çevrilir.

```
t_kr = √[ 4 × 5 × (1,560 − 0,4115) / (314,16 × 0,8) ] = √(22,97 / 251,3) = 0,302 s
```

**Sonuç: 302 ms.** Koruma arızayı 100–150 ms'de temizliyorsa marj 150 ms'nin üstündedir.

**Doğrulama.** `elle_ornekler.py` aynı denklemi zaman tanım bölgesinde Runge-Kutta ile çözer.

- 297 ms'de temizlenince rotor geri döner.
- 307 ms'de senkronizmden çıkar.

Eşit alan sonucu ile benzetim tutuyor.

**Adım 4, duyarlılık.** Aynı formül farklı girdilerle tekrar çalıştırılır; bu, hangi parametrenin kritik süreyi ne kadar oynattığını gösterir.

| Değişiklik | `t_kr` | Yorum |
| --- | --- | --- |
| Baz durum | 302 ms | |
| Atalet yarıya iner (`H = 2,5`) | 214 ms | `t_kr`, `√H` ile orantılı |
| Yükleme artar (`P_m = 1,2`) | 180 ms | Hem alan küçülür hem ivme büyür |
| Arıza sonrası hat kaybı (`P_max` düşer) | Daha kısa | Yavaşlama alanı küçülür |

## Kararlılığı iyileştiren önlemler

Hepsi çizimde okunur: ya `A_1` küçülür ya `A_2` büyür.

| Önlem | Çizimdeki etkisi |
| --- | --- |
| Hızlı koruma ve kesici | `δ_c` küçülür, `A_1` küçülür |
| Hızlı tekrar kapama, tek kutup açma | Arıza sonrası eğri yüksek kalır |
| Paralel hat, seri kompanzasyon | `X` düşer, `P_max` yükselir |
| Hızlı uyartım | `E` artar, eğri yükselir |
| Hızlı vana kapama, frenleme direnci | `P_m` düşer veya `P_e` yapay artar |
| Daha düşük ön yükleme | `δ_0` küçülür, marj büyür |

## Çok makineli gerçek sistem

Eşit alan ölçütü öğretir, ürün olmaz. Gerçek sistemde yüzlerce makine, uyartım ve hız regülatörü modelleri, yük dinamiği ve evirici vardır. Orada üç yol kullanılır:

| Yöntem | Ne yapar | Ne zaman |
| --- | --- | --- |
| **Zaman tanım bölgesi benzetimi** | Diferansiyel-cebirsel denklemler adım adım çözülür | Doğru ama yavaş |
| **Doğrudan yöntemler** | Enerji işlevi, genişletilmiş eşit alan (SIME, SIngle Machine Equivalent) | Hızlı tarama için |
| **Makine öğrenmesi ile tarama** | Çok sayıda benzetimden öğrenilmiş sınıflandırıcı | Sonucu benzetimle doğrulanır |

YTBS (Yük Tevzi Bilgi Sistemi) eğitim duyurularında geçici hal kararlılığı modülü adı geçer; yöntemini bilmiyorum.

## Yaygın yanlış

- **"Açı 90°'yi geçerse kararsızdır."** Hayır. 90° sürekli hal sınırıdır. Geçici halde açı 90°'yi geçip geri dönebilir; örnekte kritik temizleme açısı zaten 89°'dir ve rotor ondan sonra da ilerler. Dönüşsüz nokta `π − δ_0`'dır.
- **"Arıza temizlenince rotor hemen durur."** Hızı kalmıştır; açı artmaya devam eder.
- **"Kritik temizleme süresi koruma ayarıdır."** Sistemin özelliğidir. Koruma süresi ondan kısa olmalıdır.
- **"Yüksek atalet her zaman iyidir."** Geçici halde ilk salınımı yavaşlatır, evet. Ama salınım frekansını düşürür ve sönüm ayrıca sağlanmalıdır.
- **"Eşit alan gerçek sistemde uygulanır."** Tek makine eşdeğeri içindir.
- **"H ile M aynıdır."** `M = 2H / ω_0`. Birim farkı sonucu 314 kat şaşırtır.

## Panel takip sorusu

**"Arıza temizlendikten sonra bir hat devre dışı kalırsa çizim nasıl değişir?"**

> **Mülakatta şöyle söyle:** Arıza sonrası eğri, arıza öncesinden alçak olur (`X` büyüdü). Yavaşlama alanı küçülür, yeni denge açısı büyür, `δ_max` küçülür. Kritik süre kısalır.

**"Arıza sırasında `P_e` sıfır değilse?"**

> **Mülakatta şöyle söyle:** Arıza generatörden uzaktaysa bir miktar güç aktarılır; üçüncü, alçak bir eğri çizilir. Hızlanma alanı o eğri ile `P_m` arasındadır. İvme sabit olmadığı için süre kapalı formülle değil sayısal bulunur.

**"Evirici ağırlıklı sistemde bu resim ne olur?"**

> **Mülakatta şöyle söyle:** Eviricinin rotoru ve açısı yoktur; kararlılığını kontrol döngüsü ve faz kilitlemesi belirler. Ama kalan senkron makineler daha düşük toplam ataletle daha hızlı ivmelenir (`03` dosyası).

## 90 saniye

> "Salınım denklemi, rotor için Newton yasasıdır: atalet çarpı açısal ivme, mekanik güç eksi elektriksel güçtür. Elektriksel güç açının sinüsüyle gider. Arızada elektriksel güç düşer, rotor hızlanır; bu, güç–açı düzleminde bir hızlanma alanıdır. Arıza temizlenince elektriksel güç mekanik gücün üstüne çıkar ve rotor yavaşlar; bu da yavaşlama alanıdır. Rotor, dönüşsüz açıya varmadan iki alan eşitlenirse sistem kararlıdır. Alanların tam eşitlendiği temizleme süresi kritik süredir; atalet azaldıkça ve ön yükleme arttıkça kısalır. Örnekte üç yüz iki milisaniye buldum ve benzetimle doğruladım."
