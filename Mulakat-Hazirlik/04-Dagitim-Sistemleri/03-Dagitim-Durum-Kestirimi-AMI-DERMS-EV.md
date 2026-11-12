# Durum kestirimi, AMI, DERMS, EV

Bu sayfa dört konuyu anlatır: dağıtımda durum kestiriminin neden zor olduğu, AMI (gelişmiş sayaç altyapısı), DERMS (dağıtık enerji kaynakları yönetim sistemi) ve EV (elektrikli araç) şarjının şebekeye etkisi.

Durum kestirimi, eldeki ölçümlerden şebekenin o anki gerilim ve açılarını en olası şekilde tahmin etmektir.

## Dağıtımda durum kestirimi neden zor

İletimde durum kestirimi olgun bir üründür (`09` klasörü). Aynı yöntemi dağıtıma taşıyınca beş şey bozulur:

| İletimdeki varsayım | Dağıtımdaki gerçek | Sonuç |
| --- | --- | --- |
| Ölçüm, bilinmeyenden fazladır | Fider başında birkaç ölçüm, gerisi ölçümsüz | Sistem gözlenemez; açığı **sözde ölçüm** kapatır |
| Üç faz dengelidir | Tek fazlı yükler, dengesiz hatlar | Üç faz model gerekir, bilinmeyen sayısı üçe katlanır |
| `X ≫ R` | `R ≈ X` | P–θ ve Q–V ayrışması tutmaz, hızlı ayrık yöntem çalışmaz |
| Topoloji bilinir | Anahtar konumu ve müşterinin hangi faza bağlı olduğu belirsizdir | Model hatası ölçüm hatasından büyük olabilir |
| Ölçümler eşzamanlıdır | SCADA saniyelik, sayaç 15 dakikalık ve gecikmeli | Zaman hizalama gerekir |

Tablodaki terimler:

- **Gözlenebilirlik:** Eldeki ölçümlerin bütün bilinmeyenleri çözmeye yetmesi.
- **P–θ ve Q–V ayrışması:** İletimde aktif gücün (P) çoğunlukla açıya (θ), reaktif gücün (Q) çoğunlukla gerilime (V) bağlı olması. Hızlı ayrık yöntem bu ayrışmaya dayanır.
- **SCADA:** Merkezi izleme ve kumanda sistemi.

### Sözde ölçüm

**Sözde ölçüm (pseudo-measurement):** Ölçülmeyen yük için tahmin kullanmaktır.

Kaynakları:

- Sayaç geçmişi
- Trafo anma gücüne göre paylaştırma
- Yük profili

Belirsizliği büyüktür (%20–50). Bu yüzden ağırlığı küçük verilir. Kestirimin kalitesi doğrudan sözde ölçümün kalitesine bağlıdır.

### Durum değişkeni

Durum değişkeni seçimi de değişir:

- İletimde bara gerilimi ve açısı kullanılır.
- Radyal dağıtımda **dal akımı** tabanlı kestirim daha iyi koşullu ve daha hızlıdır.

> **Sade anlatım:** Yazılımcı gözüyle iletim kestirimi, fazla belirlenmiş ve temiz veriyle yapılan bir regresyondur. Dağıtım kestirimi ise eksik veriyle, güçlü önsel bilgiyle ve hatalı şemayla yapılan bir çıkarımdır.

### Elle örnek: ağırlığın etkisi

Durum: Bir fider kesimindeki akış için iki bilgi var.

- SCADA ölçümü 2,00 MW (σ = 0,02)
- Sayaç profilinden sözde ölçüm 2,60 MW (σ = 0,50)

σ (sigma), bilginin standart sapmasıdır; ne kadar belirsiz olduğunu gösterir.

Aşağıdaki ilk satır, her bilgiye belirsizliğinin karesinin tersi kadar ağırlık verir. İkinci satır, iki değerin bu ağırlıklarla ortalamasını alır.

```
ağırlık = 1/σ²:   2500   ve   4
kestirim = (2500 × 2,00 + 4 × 2,60) / 2504 = 2,001 MW
```

Sonuç: Sözde ölçüm sonucu neredeyse hiç oynatmadı. Ölçümün olduğu yerde belirleyici olan ölçümdür. Sözde ölçüm yalnızca ölçümün olmadığı yerde sistemi çözülebilir kılar.

## AMI: gelişmiş sayaç altyapısı

AMI; akıllı sayaç, haberleşme ağı, veri toplayıcı ve sayaç veri yönetim sistemi (MDMS) bütünüdür.

### Ne verir

- 15 dakikalık veya saatlik tüketim ve üretim
- Gerilim
- Kesinti ve geri gelme bildirimi ("son nefes" mesajı: sayacın enerji giderken gönderdiği son mesaj)
- Uzaktan açma-kapama

### Analiz için değeri

- Kestirim için sözde ölçüm kaynağı
- Yük profili ve tahmin
- Teknik olmayan kayıp tespiti: trafo ölçümü ile altındaki sayaçların toplamı tutmuyorsa
- Topoloji ve faz tespiti: aynı faza bağlı sayaçların gerilimleri birlikte hareket eder
- Kesinti yerinin hızlı bulunması

### Sınırları

- Veri gecikmelidir. Çoğu sistem günde bir kez toplu aktarır.
- Gerçek zamanlı kontrol için uygun değildir.
- Veri hacmi büyüktür.
- Kişisel veridir (KVKK, Kişisel Verilerin Korunması Kanunu).

Türkiye'deki güncel akıllı sayaç yaygınlaştırma takvimini ve oranını **doğrulamadım**.

> **Mülakatta şöyle söyle:** Akıllı sayaç yaygınlığı için rakam verme.

## DERMS: dağıtık enerji kaynakları yönetim sistemi

DERMS; çatı güneşi, batarya, şarj istasyonu ve esnek yük gibi binlerce küçük kaynağı izleyen, tahmin eden ve yöneten yazılımdır.

### Kardeş sistemlerden ayrımı

| Sistem | Sorumluluğu |
| --- | --- |
| SCADA | Ölçer, kumanda eder |
| DMS / ADMS (dağıtım yönetim sistemi / gelişmiş DMS) | Şebekeyi yönetir: yük akışı, kestirim, FLISR (arıza tespiti, izolasyon, hizmet iadesi), volt/VAR |
| DERMS | Şebekeye bağlı kaynakları yönetir: toplar, sınır koyar, ayar noktası gönderir |
| Sanal santral (VPP) | Kaynakları **piyasa** için toplar; şebeke kısıtını bilmek zorunda değildir |

### Tipik işlevleri

- Kayıt ve görünürlük
- Üretim ve esneklik tahmini
- Toplama
- Kısıt yönetimi: dinamik işletme zarfı. Bu, her bağlantı noktasına o an izin verilen en büyük ithalat ve ihracattır.
- Volt/VAR desteği

### Standartlar

- Haberleşme standartları: IEEE 2030.5, OpenADR, SunSpec Modbus, IEC 61850-7-420.
- Evirici davranışı IEEE 1547-2018 ile tanımlanır.

### Bu ilanla bağı

TEİAŞ'ın (Türkiye Elektrik İletim A.Ş.) güneş tahmin projesi 34 binden fazla santrali kapsar (`01/03`).

- İletim operatörü için bu kaynakların toplam davranışı önemlidir.
- Dağıtım için tek tek davranışı önemlidir.

İkisi arasındaki veri alışverişi (TSO–DSO koordinasyonu, yani iletim ve dağıtım sistemi operatörlerinin koordinasyonu) açık bir araştırma alanıdır.

## Elektrikli araç şarjı

Şebeke açısından üç etki vardır:

1. **Eşzamanlılık.** Akşam eve dönüş, evsel puantla çakışır. Trafo ve alçak gerilim kablosu ısıl sınıra dayanır.
2. **Gerilim düşümü ve dengesizlik.** Tek fazlı ev şarjı faz dengesini bozar.
3. **Hızlı şarj.** 150–350 kW'lık istasyon, orta gerilimde küçük bir sanayi tesisi gibidir; ani yüklenir.

### Elle örnek: trafo ne zaman dolar

Durum: 400 kVA dağıtım trafosu, 100 hane. Akşam puantında hane başına 2 kW, güç faktörü 0,95.

**Adım 1.** Bu adım, mevcut yükü kVA'ya çevirip trafonun ne kadar dolu olduğunu bulur. Ardından boş kalan kapasiteyi hesaplar:

```
Mevcut yük = 100 × 2 / 0,95 = 210,5 kVA      (%53)
Kalan      = 400 − 210,5    = 189,5 kVA
```

**Adım 2.** Bu adım, boş kapasiteye aynı anda kaç aracın sığacağını bulur. Ev tipi şarj 7,4 kW'tır (tek faz, 32 A). Güç faktörü 1 kabul edilir:

```
Aynı anda şarj edebilecek araç ≈ 189,5 / 7,4 ≈ 25
```

**Adım 3.** Bu adım, 40 aracın aynı anda takıldığı kötü senaryoyu hesaplar. Yüz hanenin 40'ında araç varsa ve hepsi 19.00'da takarsa `40 × 7,4 = 296 kW` ister. Toplam `200 + 296 = 496 kW` ve 65,7 kvar, yani 500 kVA eder. Trafo %125 yüklenir.

**Sonuç.** Aynı 40 araç gece boyunca sıraya konursa sorun yoktur. Çözüm bakır değil, zamanlama.

### Araçlar

| Araç | Ne yapar |
| --- | --- |
| **Akıllı şarj (V1G)** | Şarjın zamanını ve gücünü kaydırır. Tarife, sinyal veya doğrudan kontrol ile |
| **Araçtan şebekeye (V2G)** | Bataryadan şebekeye geri verir. Teknik olarak mümkündür; batarya ömrü, sayaç ve mevzuat engelleri vardır |
| **Planlama** | Eşzamanlılık katsayısı kullanılır. Yüz aracın hepsi aynı anda tam güçte şarj etmez; katsayı ölçümle belirlenir |

Dikkat: Herkesi aynı ucuz saate yönlendiren basit tarife, puantı yok etmez; **yeni bir puant** yaratır (geri tepme etkisi). Başlangıç saatini dağıtmak gerekir.

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"İletimdeki kestirim kodunu dağıtıma kurarım."** | Gözlenebilirlik, denge ve R/X varsayımlarının üçü de tutmaz. |
| **"Akıllı sayaç gerçek zamanlı ölçümdür."** | Çoğu kurulumda saatler gecikmeli toplu veridir. |
| **"DERMS ile sanal santral aynıdır."** | Biri şebeke kısıtını, diğeri piyasa gelirini optimize eder; çatışabilirler. |
| **"Elektrikli araç sorunu enerji sorunudur."** | Yıllık enerji payı küçüktür. Sorun eşzamanlı güç ve yereldir. |
| **"Sözde ölçüm ölçüm gibidir."** | Büyük varyanslı tahmindir; ağırlığı buna göre verilmezse kestirimi bozar. |

## Panel takip sorusu

"Dağıtımda gözlenebilirliği nasıl artırırsın?"

> **Mülakatta şöyle söyle:** "Önce mevcut veriyi kullanırım: sayaç verisinden sözde ölçüm, trafo ölçümleri. Sonra kestirim varyansını en çok düşürecek noktalara ölçüm yerleştiririm; bu bir optimal sensör yerleşimi problemidir."

"Topoloji hatasını ölçüm hatasından nasıl ayırırsın?"

> **Mülakatta şöyle söyle:** "Ölçüm hatası tek bir artığı büyütür. Topoloji hatası, yanlış modellenen anahtarın çevresindeki birçok artığı birlikte büyütür."

Artık, ölçülen değer ile kestirimin o ölçüm için öngördüğü değer arasındaki farktır.

Aşağıdaki metin, bu konu sorulduğunda 90 saniyede söyleyeceğin özettir.

## 90 saniye

"Dağıtımda durum kestirimi iletimdekinden zordur, çünkü ölçüm azdır, şebeke dengesizdir, direnç reaktansa yakındır ve topoloji belirsizdir. Eksik ölçümü sayaç geçmişinden üretilen sözde ölçümle kapatır, belirsizliği büyük olduğu için ağırlığını küçük veririm. Akıllı sayaç altyapısı bu verinin kaynağıdır ama gerçek zamanlı değildir. DERMS, binlerce küçük kaynağı şebeke kısıtı içinde yönetir; sanal santral ise piyasa için toplar. Elektrikli araçta sorun enerji değil eşzamanlı güçtür; ilk çözüm şarjı zamana yaymaktır."
