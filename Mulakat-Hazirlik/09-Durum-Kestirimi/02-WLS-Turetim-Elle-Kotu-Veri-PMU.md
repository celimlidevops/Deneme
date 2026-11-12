# WLS türetimi ve elle örnekler

Bu sayfa WLS (Weighted Least Squares, ağırlıklı en küçük kareler) türetimini, elle örnekleri, kötü veri testini, gözlenebilirliği ve PMU'yu (Phasor Measurement Unit, fazör ölçüm birimi) anlatır.

## Durum kestirimi ne iş yapar

SCADA'dan (Supervisory Control and Data Acquisition, uzaktan izleme ve veri toplama sistemi) gelen ölçümlerin dört kusuru vardır:

- gürültülüdür,
- eksiktir,
- bazen yanlıştır,
- aynı anda alınmamıştır.

Ham ölçümle yük akışı ya da güvenlik analizi koşulmaz. Çünkü ölçümler birbiriyle bile tutmaz: bir baraya giren ve çıkan güçlerin toplamı sıfır etmez.

Durum kestirimi, fazlalık ölçümü kullanarak şebeke denklemleriyle **tutarlı**, en olası durumu bulur.

Durum, bütün bara gerilimlerinin büyüklüğü ve açısıdır. Bunları bilirsen her akışı hesaplarsın.

> **Sade anlatım:** Yazılımcı gözüyle durum kestirimi, fizik kısıtlı, ağırlıklı, doğrusal olmayan bir regresyondur.

Yük akışından farkı:

| | Yük akışı | Durum kestirimi |
| --- | --- | --- |
| Denklem sayısı | Bilinmeyene eşittir | Bilinmeyenden fazladır |
| Veriye bakış | Veri doğru kabul edilir | Hiçbir veri doğru kabul edilmez |

Enerji yönetim sistemindeki (EMS, Energy Management System) zincir:

```
SCADA → topoloji işleyici → durum kestirimi → güvenlik analizi, optimal güç akışı, operatör ekranı
```

Kestirim bozulursa arkasındaki her şey bozulur.

## Model

Ölçümü, durumu ve hatayı birbirine bağlayan denklem:

```
z = h(x) + e
```

| Sembol | Anlamı |
| --- | --- |
| `z` | Ölçüm vektörü (`m` adet): akışlar, enjeksiyonlar, gerilim büyüklükleri |
| `x` | Durum vektörü (`n = 2N − 1` adet): `N` gerilim büyüklüğü, `N − 1` açı |
| `h(x)` | Durumu ölçüme bağlayan şebeke denklemleri |
| `e` | Ölçüm hatası; sıfır ortalamalı, `σ_i` standart sapmalı, bağımsız kabul edilir |

`N` bara sayısıdır. Açı sayısı `N − 1`'dir, çünkü bir bara referans alınır.

**Fazlalık oranı** `m / n`'dir, yani ölçüm sayısının durum sayısına oranı. Pratikte 1,5–3 arasında olması istenir.

## WLS türetimi

Amaç: ölçüm ile model arasındaki farkın, **güvenilirliğe göre ağırlıklandırılmış** kareler toplamını en aza indirmek.

Aşağıdaki satır amaç fonksiyonunu önce toplam, sonra matris biçiminde yazar:

```
J(x) = Σ (z_i − h_i(x))² / σ_i²  =  (z − h(x))ᵀ W (z − h(x))          W = R⁻¹ = diag(1/σ_i²)
```

- `R`: ölçüm hata kovaryans matrisi, köşegeni `σ_i²`.
- `W`: ağırlık matrisi, köşegeni `1/σ_i²`.

Ağırlık neden `1/σ²`: hassas ölçüme çok, kaba ölçüme az güvenilir. Hatalar Gauss dağılımlıysa bu, en büyük olabilirlik kestirimidir (gözlenen veriyi en olası kılan durumu seçer).

**Adım 1.** En küçük noktada türev sıfırdır. Bu adım, minimumun koşulunu yazar.

```
∂J/∂x = −2 Hᵀ W (z − h(x)) = 0          H = ∂h/∂x   (ölçüm Jacobian'ı, m × n)
```

**Adım 2.** `h(x)` doğrusal değildir; çevresinde doğrusallaştır. Bu adım, denklemi çözülebilir bir doğrusal biçime getirir.

```
h(x + Δx) ≈ h(x) + H Δx
```

**Adım 3.** Yerine koy. Bu adım, doğrusallaştırılmış `h`'yi Adım 1'deki koşula yerleştirir ve `Δx`'i yalnız bırakır.

```
Hᵀ W (z − h(x) − H Δx) = 0
(Hᵀ W H) Δx = Hᵀ W (z − h(x))
```

**Adım 4.** Tanımla ve yinele. Bu adım, sol taraftaki matrise isim verir ve çözümü bir döngüye çevirir.

```
G = Hᵀ W H                      kazanç matrisi (n × n, simetrik, seyrek)
G Δx = Hᵀ W r                   normal denklemler,   r = z − h(x)
x ← x + Δx                      |Δx| küçülene kadar
```

Üç matrisi ayır:

| Matris | Boyut | Ne taşır |
| --- | --- | --- |
| `H` | `m × n` | Fizik: hangi ölçüm hangi duruma ne kadar duyarlı |
| `W` | `m × m`, köşegen | Güven: her ölçümün hassasiyeti |
| `G` | `n × n` | İkisinin birleşimi. Tersi, kestirimin kovaryansıdır. Tekilse sistem gözlenemez |

**Sayısal not:** `G`, `H`'nin koşul sayısının karesini taşır. Koşul sayısı, bir matrisin sayısal hatayı ne kadar büyüttüğünün ölçüsüdür.

Çok farklı ağırlıklar (sanal ölçümler, sıfır enjeksiyonlar) `G`'yi kötü koşullu yapar. Çözüm iki yoldan biridir:

- normal denklemler yerine QR ayrışımı,
- sıfır enjeksiyonları eşitlik kısıtı olarak yazmak.

## Elle örnek 1: iki ölçüm, bir durum

**Kurulum.** İki bara, hat `x = 0,1` pu, DC model. Bara 1 referans (`θ_1 = 0`). Tek bilinmeyen `θ_2`.

- pu (per unit, birim değer): büyüklüğün seçilen bir taban değere oranı.
- DC model: kayıpsız, gerilimleri 1 pu kabul eden, yalnız açılarla çalışan basit akış modeli.

Aynı hattın akışı iki ayrı cihazla ölçülmüş:

```
z_1 = 1,02 pu    σ_1 = 0,01       (hassas)
z_2 = 0,98 pu    σ_2 = 0,02       (kaba)
```

Model: `P_12 = (θ_1 − θ_2) / x = −10 θ_2`. Doğrusal olduğu için tek adımda çözülür.

**Hesap.** Aşağıdaki blok sırasıyla şunları yapar:

1. `H` satırlarını yazar: her iki ölçüm de `θ_2`'ye −10 duyarlıdır.
2. `W`'yi yazar: `1/0,01² = 10.000` ve `1/0,02² = 2.500`.
3. `G = HᵀWH`'yi hesaplar.
4. Sağ taraf `HᵀWz`'yi hesaplar.
5. `θ_2`'yi bölmeyle bulur.
6. Bulunan açıdan akışı geri hesaplar.

```
H = [ −10 ]        W = [ 10.000     0  ]
    [ −10 ]            [    0    2.500 ]

G     = Hᵀ W H = 100 × 10.000 + 100 × 2.500 = 1.250.000
Hᵀ W z = −10 × 10.000 × 1,02 − 10 × 2.500 × 0,98 = −126.500

θ_2 = −126.500 / 1.250.000 = −0,1012 rad
P̂   = −10 × (−0,1012) = 1,012 pu
```

**Yorum.** Kestirim 1,012; iki ölçümün düz ortalaması 1,000 olurdu. Hassas ölçümün ağırlığı dört kat fazla olduğu için sonuç ona yakın.

Bu örnekte WLS, **ağırlıklı ortalamadan** başka bir şey değildir: `(10.000 × 1,02 + 2.500 × 0,98) / 12.500 = 1,012`.

**Artıklar.** Aşağıdaki blok her ölçümün kestirimden farkını alır, sonra bu farkların ağırlıklı kareler toplamı `J`'yi hesaplar:

```
r_1 = 1,02 − 1,012 = +0,008
r_2 = 0,98 − 1,012 = −0,032
J   = 0,008² × 10.000 + 0,032² × 2.500 = 0,64 + 2,56 = 3,20
```

## Kötü veri: tespit

Ölçümler yalnızca gürültü içeriyorsa `J`, serbestlik derecesi `m − n` olan ki-kare dağılımına uyar. `J` eşiği aşıyorsa içeride gürültüden fazlası vardır.

Örnekte serbestlik derecesi `m − n = 2 − 1 = 1`. %95 güven için ki-kare eşiği 3,84.

Aşağıdaki satır, hesaplanan `J`'yi eşikle karşılaştırır:

```
J = 3,20 < 3,84   →   kötü veri şüphesi yok
```

Sık kullanılan eşikler (%95):

| Serbestlik derecesi | Eşik |
| --- | --- |
| 1 | 3,84 |
| 2 | 5,99 |
| 3 | 7,81 |
| 10 | 18,31 |

## Kötü veri: teşhis (en büyük normalize artık)

Ki-kare "bir sorun var" der, hangisi olduğunu söylemez.

Ham artığa bakmak da yanıltır. Kötü ölçüm kestirimi kendine çeker, kendi artığını küçültür ve komşularının artığını büyütür. Buna **bulaşma** denir.

Çare: her artık kendi standart sapmasına bölünür. İlk satır artık kovaryansını, ikinci satır normalize artığı verir:

```
Ω = R − H G⁻¹ Hᵀ              artık kovaryansı
r_N,i = |r_i| / √Ω_ii          normalize artık
```

Kural: en büyük `r_N` 3,0'ı aşıyorsa o ölçüm kötüdür. Çıkar, yeniden kestir, tekrarla.

**Hesap.** Örnekte `H G⁻¹ Hᵀ` matrisinin bütün elemanları `100 / 1.250.000 = 0,00008`.

Aşağıdaki blok her ölçüm için şunu yapar: `R`'nin köşegeninden (`0,01² = 0,0001` ve `0,02² = 0,0004`) 0,00008'i çıkarıp `Ω_ii`'yi bulur, sonra ham artığı `√Ω_ii`'ye böler:

```
Ω_11 = 0,0001 − 0,00008 = 0,00002       r_N,1 = 0,008 / 0,00447 = 1,79
Ω_22 = 0,0004 − 0,00008 = 0,00032       r_N,2 = 0,032 / 0,01789 = 1,79
```

İkisi de 3'ün altında.

Ama asıl ders başka: **iki normalize artık birbirine eşit.** Bir durumu yalnızca iki ölçüm gözlüyorsa hangisinin yanlış olduğu ayırt edilemez. Biri bozulsa ikisinin normalize artığı birlikte büyür.

Buna **kritik çift** denir. Tespit edilir, teşhis edilemez. Teşhis için en az üç ölçüm gerekir.

## Elle örnek 2: üçüncü ölçüm ve kaba hata

Aynı hatta üçüncü bir ölçüm ekleniyor ve bozuk: `z_3 = 1,20`, `σ_3 = 0,02`. Üçüncü ölçümün ağırlığı `1/0,02² = 2.500`'dür.

Aşağıdaki blok sırasıyla şunları yapar:

1. Yeni `G`'yi üç ağırlığın toplamıyla kurar.
2. Akışı üç ölçümün ağırlıklı ortalaması olarak kestirir.
3. Artıkları ve `J`'yi hesaplar, `J`'yi 2 serbestlik derecesinin eşiğiyle karşılaştırır (`m − n = 3 − 1 = 2`).
4. Normalize artıkları hesaplar ve en büyüğünü seçer.

```
G = 100 × (10.000 + 2.500 + 2.500) = 1.500.000
P̂ = (10.000 × 1,02 + 2.500 × 0,98 + 2.500 × 1,20) / 15.000 = 1,0433

r = [ −0,0233   −0,0633   +0,1567 ]
J = 76,8        eşik (2 serbestlik derecesi) = 5,99     →   kötü veri VAR

r_N = [ 4,04    3,47    8,58 ]                          →   en büyük: üçüncü ölçüm
```

**Bulaşmaya dikkat.** Sağlam olan birinci ve ikinci ölçümün normalize artıkları da 3'ü aştı. Hepsini birden atmak yanlıştır.

Yalnız **en büyüğü** çıkarılır ve yeniden kestirilir. Sonuç 1,012'ye döner, `J = 3,20` olur, test geçer.

Sayılar `elle_ornekler.py` ve ek bir hesapla doğrulanmıştır.

## Gözlenebilirlik

Eldeki ölçümlerle bütün durum değişkenleri tek anlamlı bulunabiliyorsa sistem **gözlenebilirdir**.

| Ölçüt | Koşul |
| --- | --- |
| Sayısal | `G` tekil değilse (`H`'nin rankı `n` ise) |
| Topolojik | Ölçümler, bütün baraları kapsayan bir ağaç oluşturabiliyorsa |

`m ≥ n` gerekir ama yetmez. Ölçümlerin hepsi şebekenin bir köşesinde toplanmışsa öbür köşe gözlenemez.

Gözlenemeyen kısım için:

1. sistemi gözlenebilir adalara böl,
2. eksik kısmı **sözde ölçümle** (tahmin, geçmiş veri) tamamla,
3. sözde ölçümün ağırlığını küçük ver.

**Kritik ölçüm:** çıkarılırsa sistemi gözlenemez yapan ölçüm. Artığı her zaman sıfırdır, çünkü kestirim onu birebir karşılar. Bu yüzden hatası **tespit edilemez**.

Ölçüm yerleşimi planlanırken kritik ölçüm bırakılmamaya çalışılır.

## PMU ve doğrusal kestirim

| | Klasik SCADA | PMU |
| --- | --- | --- |
| Ne ölçer | Güç ve gerilim büyüklüğü | GPS saatiyle eşzamanlanmış **gerilim ve akım fazörü**: büyüklük ve açı |
| Durumla ilişki | Doğrusal değil; yineleme gerekir | Dikdörtgen koordinatta doğrusal |
| Hız | Tarama birkaç saniyede bir | Saniyede 25–50 ölçüm (50 Hz sistemde) |
| Eşzamanlılık | Ölçümler eşzamanlı değildir | GPS ile eşzamanlı |

Zaman doğruluğu neden önemli: 1 mikrosaniyelik zaman hatası 50 Hz'te 0,018° açı hatasıdır.

**Doğrusallık nereden gelir.** Durumu dikdörtgen koordinatlarda (gerilimin gerçek ve sanal kısmı) yazarsan iki şey olur:

- gerilim fazörü ölçümü durumun kendisidir,
- akım fazörü ölçümü `I = Y V` ile durumun **doğrusal** işlevidir (`Y`: şebekenin admitans matrisi).

Bu durumda model ve çözüm şöyledir. İlk satır doğrusal ölçüm modelini, ikinci satır iterasyonsuz çözümü verir:

```
z = H x + e          H sabit
x̂ = (Hᵀ W H)⁻¹ Hᵀ W z          tek adım, yineleme yok
```

Sonuçları:

- yakınsama sorunu yoktur,
- `G`'nin çarpanları bir kez hesaplanıp saklanır,
- kestirim saniyede onlarca kez koşabilir.

### Elle örnek 3

`05` klasöründeki iki baralı örnek. Bara 1'deki PMU şunları ölçüyor: `V_1 = 1,0∠0°` ve hat akımı `I_12 = 0,5 − j0,2303` pu.

Aşağıdaki blok iki adım yapar. İlk satır, hattaki gerilim düşümünü (`j x I_12`) bara 1 geriliminden çıkararak `V_2`'yi bulur. İkinci satır, bu karmaşık sayıyı büyüklük ve açıya çevirir:

```
V_2 = V_1 − j x I_12 = 1,0 − j0,1 × (0,5 − j0,2303) = 0,97697 − j0,05
|V_2| = 0,9782       açı = −2,93°
```

Newton-Raphson'ın üç turda bulduğu sonuç, tek satır karmaşık sayı aritmetiğiyle geldi.

Ayrıca bara 2'de ölçüm cihazı yokken durumu bulundu: bir PMU, akım ölçtüğü her hattın karşı ucunu da gözlenebilir kılar.

**Pratik gerçek:** her baraya PMU konmaz. Uygulamada **hibrit** kestirim kullanılır: SCADA ölçümleriyle klasik kestirim, PMU ölçümleriyle iyileştirme.

PMU'nun ek değerleri:

- doğrudan açı ölçümü,
- dinamikleri görmek (salınım, RoCoF — Rate of Change of Frequency, frekansın değişim hızı),
- geniş alan koruma.

SIPS'in (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması) veri kaynağı budur.

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"Durum kestirimi ölçümleri filtreler."** | Yumuşatmaz; şebeke denklemlerine uyan en olası durumu bulur. |
| **"Ölçüm sayısı bilinmeyenden fazlaysa sistem gözlenebilirdir."** | Dağılım da önemlidir. |
| **"En büyük ham artık kötü ölçümdür."** | Normalize artığa bakılır; ham artık bulaşmadan etkilenir ve ölçüm türleri arasında karşılaştırılamaz. |
| **"Eşiği aşan bütün ölçümleri atarım."** | Yalnız en büyüğü, sonra yeniden kestirim. |
| **"Kritik ölçümdeki hata yakalanır."** | Artığı hep sıfırdır; yakalanamaz. |
| **"Ağırlık, ölçümün önemidir."** | Hassasiyetidir: `1/σ²`. |
| **"Kötü veri her zaman ölçüm hatasıdır."** | Topoloji hatası (kesici konumu yanlış) ve parametre hatası (hat empedansı yanlış) da aynı belirtiyi verir; ama artıklar tek ölçümde değil bir bölgede büyür. |
| **"PMU varsa SCADA'ya gerek yok."** | Kapsama yetmez; hibrit çalışılır. |

## Panel takip sorusu

**"Birbirini doğrulayan iki kötü ölçüm olursa?"**

> **Mülakatta şöyle söyle:** Etkileşen ve uyumlu çoklu kötü veri, en büyük normalize artık testini yanıltabilir; sağlam ölçüm suçlanır. Çareler: hipotez testi ile teşhis, dayanıklı kestiriciler (en küçük mutlak değer), ve daha fazla fazlalık.

**"Kestirim yakınsamazsa operatöre ne gösterirsin?"**

> **Mülakatta şöyle söyle:** Eski sonucu taze gibi göstermem. Son geçerli çözümü zaman damgasıyla, yakınsamama nedenini (topoloji değişimi, gözlenemeyen ada, kaba hata) ve hangi alt uygulamaların durduğunu gösteririm.

**"Normal denklemler neden sorun çıkarır?"**

> **Mülakatta şöyle söyle:** `G = HᵀWH` koşul sayısını kareler. Ağırlıklar arasında milyon kat fark varsa çarpanlara ayırma sayısal olarak bozulur. QR veya Hachtel yöntemi kullanılır.

Hachtel yöntemi, normal denklemleri kurmadan ölçüm ve kısıt denklemlerini birlikte genişletilmiş bir matrisle çözer; böylece koşul sayısının karesi alınmaz.

## 90 saniye

"Durum kestirimi, gürültülü ve fazlalıklı ölçümlerden şebeke denklemleriyle tutarlı en olası gerilim ve açıları bulur. Ağırlıklı en küçük karelerde her artığı ölçümün varyansına böler, toplamı en aza indiririm. Türevi sıfıra eşitleyip doğrusallaştırınca normal denklemler çıkar: kazanç matrisi H devrik W H'dir ve tekilse sistem gözlenemez. Kötü veriyi önce ki-kare testiyle tespit eder, sonra en büyük normalize artıkla teşhis eder, o ölçümü çıkarıp yeniden kestiririm. Bir durumu tek ölçüm gözlüyorsa hatası yakalanamaz, iki ölçüm gözlüyorsa tespit edilir ama teşhis edilemez. PMU fazör ölçtüğü için dikdörtgen koordinatlarda model doğrusaldır ve çözüm tek adımdır."
