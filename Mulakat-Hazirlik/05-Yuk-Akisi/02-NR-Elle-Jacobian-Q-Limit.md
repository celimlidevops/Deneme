# Newton-Raphson elle

Bu sayfa Newton-Raphson (NR) yük akışını elle çözmeyi, Jacobian yapısını, yakınsamayı ve Q limitini anlatır.

## Problem neden doğrusal değil

Şebeke denklemi `I = Y V` doğrusaldır. Ama bize akım değil **güç** verilir: yük 50 MW çeker, santral 200 MW üretir.

Güç, gerilim ile akımın çarpımıdır. Yani gerilimin karesini ve açıların sinüsünü içerir. Bu yüzden kapalı çözüm yoktur, yineleme gerekir.

> Sade anlatım: Akım verilseydi tek bir matris denklemiyle biterdi. Güç verildiği için tahmin et, düzelt, tekrar et yapmak zorundasın.

Her bara için dört büyüklük vardır: `P`, `Q`, `|V|`, `θ`. İkisi verilir, ikisi bulunur.

| Bara tipi | Verilen | Bulunan | Fiziksel karşılığı |
| --- | --- | --- | --- |
| PQ (yük) | P, Q | V, θ | Tüketim; ayrıca reaktif sınırına dayanmış santral |
| PV (üretim) | P, V | Q, θ | Gerilimini AVR (Automatic Voltage Regulator, otomatik gerilim regülatörü) ile tutan santral |
| Salınım (slack) | V, θ = 0 | P, Q | Açı referansı; kaybı ve dengesizliği üstlenir |

Salınım barası neden şart:

- Kayıplar çözümden önce bilinmez. Bu yüzden bütün üretimleri önceden belirleyemezsin. Bir bara farkı kapatır.
- Açılar görelidir. Biri sıfır seçilmezse denklem takımı tekildir.

## Denklemler

Bara `i` için hesaplanan güç aşağıdaki gibidir. Bu iki denklem, tahmin edilen gerilim ve açılarla baraya giren gücü hesaplar:

```
P_i = V_i Σ V_k (G_ik cos θ_ik + B_ik sin θ_ik)
Q_i = V_i Σ V_k (G_ik sin θ_ik − B_ik cos θ_ik)          θ_ik = θ_i − θ_k
```

Artık (mismatch), verilen ile hesaplanan arasındaki farktır:

- `ΔP = P_verilen − P_hesaplanan`
- `ΔQ = Q_verilen − Q_hesaplanan`

Newton adımı, artığı sıfırlayacak düzeltmeyi doğrusal yaklaşımla bulur. Aşağıdaki matris denklemi, artığı açı ve gerilim düzeltmesine çevirir:

```
[ ΔP ]   [ H  N ] [ Δθ ]          H = ∂P/∂θ    N = ∂P/∂V
[ ΔQ ] = [ M  L ] [ ΔV ]          M = ∂Q/∂θ    L = ∂Q/∂V
```

Bilinmeyen sayısı:

- PV ve PQ baraların açıları,
- yalnız PQ baraların gerilimleri.

`n` baralı, `g` üretim baralı sistemde Jacobian boyutu `(2n − g − 1)`'dir (salınım dahil `g`).

## Jacobian'ın yapısı

Köşegen elemanlar aşağıdadır. Ezberleme, türet. Her biri, baranın kendi gücünün kendi açısına veya gerilimine göre türevidir:

```
H_ii = −Q_i − B_ii V_i²        N_ii = P_i / V_i + G_ii V_i
M_ii =  P_i − G_ii V_i²        L_ii = Q_i / V_i − B_ii V_i
```

Köşegen dışı elemanlar yalnızca `Y_ik ≠ 0` ise sıfırdan farklıdır. Yani **Jacobian, Ybus ile aynı seyreklik desenine sahiptir.** Büyük sistemlerin çözülebilmesinin nedeni budur.

### Bloklardan basit modellere

İletimde `X ≫ R` ve açı farkları küçüktür. O zaman `N` ve `M` blokları `H` ve `L`'ye göre küçük kalır: aktif güç açıya, reaktif güç gerilime bağlıdır.

| Model | Ne yapar |
| --- | --- |
| Tam Newton | Dört bloğu da kullanır |
| Hızlı ayrık yöntem (FDLF, Fast Decoupled Load Flow) | `N` ve `M` bloklarını atar, kalanları sabit matrislerle değiştirir |
| DC yük akışı | Bir adım daha ileri gider: yalnızca `P = B θ` kalır |

## Elle örnek: iki bara, iki tur

Bu örnek, Newton'un bir turda ne yaptığını sayılarla gösterir.

**Veri.** Bara 1 salınım, `V = 1,0∠0`. Bara 2 yük: `P = 0,5`, `Q = 0,2` pu (per unit, birim değer) çekiyor. Hat `x = 0,1` pu, direnç yok.

**Ybus elemanları.** Hat admitansı `1/(j0,1)` olduğu için:

`B_22 = −10`, `B_21 = +10`, `G = 0`.

**Bara 2 güç denklemleri.** Genel denklemlere bu değerler konunca bara 2 için şu kalır:

```
P_2 = 10 V_2 sin θ_2
Q_2 = 10 V_2² − 10 V_2 cos θ_2
```

**Başlangıç (düz başlatma):** `V_2 = 1,0`, `θ_2 = 0`. Bu, sağlıklı şebekede çözüme yakın bir ilk tahmindir.

### Tur 1

Aşağıdaki bloğun adımları:

1. İlk satır, başlangıç tahminiyle bara 2'nin gücünü hesaplar.
2. İkinci satır artığı bulur. Yük çektiği için verilen güç eksi işaretlidir.
3. Orta iki satır Jacobian'ın dört elemanını köşegen formüllerinden hesaplar.
4. Son iki satır düzeltmeyi bulur ve tahmini günceller. N ve M sıfır olduğu için her denklem ayrı bölmeyle çözülür.

```
P_2 = 0,   Q_2 = 0
ΔP = −0,5 − 0 = −0,5         ΔQ = −0,2 − 0 = −0,2

H = −Q_2 − B_22 V² = 0 + 10 = 10        N = P_2/V + G V = 0
M =  P_2 − G V²    = 0                  L = Q_2/V − B_22 V = 10

Δθ = −0,5 / 10 = −0,05 rad      ΔV = −0,2 / 10 = −0,02
θ_2 = −0,05 rad                 V_2 = 0,98
```

### Tur 2

Aşağıdaki bloğun adımları:

1. İlk iki satır, yeni tahminle gücü yeniden hesaplar.
2. Üçüncü satır kalan artığı verir. Artık şimdiden çok küçülmüştür.
3. `J` yeni noktada hesaplanmış Jacobian'dır. Artık N ve M sıfır değil, bu yüzden 2×2 sistem birlikte çözülür.
4. Son iki satır düzeltmeyi ve güncel tahmini verir.

```
P_2 = 10 × 0,98 × sin(−0,05)             = −0,48980
Q_2 = 10 × 0,98² − 10 × 0,98 × cos(0,05) = −0,18375
ΔP = −0,01020        ΔQ = −0,01625

J = [  9,7878  −0,4998 ]
    [ −0,4898   9,6125 ]

Δθ = −0,001132       ΔV = −0,001748
θ_2 = −0,051132 rad  V_2 = 0,978252
```

### Tur 3

Artıklar `−0,00002` ve `−0,00004`. Bu tur sonucun artık değişmediğini doğrular.

Sonuç `θ_2 = −0,051134 rad` (−2,93°), `V_2 = 0,978248`.

Bu küçük örneğin kapalı çözümü vardır ve aynı sayıyı verir: `V_2 = 0,978248`.

### Yakınsamayı okumak

Artığın gidişine bak: 0,5 → 0,016 → 0,00004.

Her turda hata yaklaşık **karesi** kadar küçülür. Newton'un ayırt edici özelliği budur (ikinci dereceden yakınsama). Üç-beş turda yakınsamayan bir vaka, hasta bir vakadır.

### Üç baralı örnek

Üç baralı örneğin (PV baralı, dirençli) çıktısı `nr_yuk_akisi.py` ile:

- 5 turda artık `7,9e-1 → 4,0e-2 → 3,1e-4 → 2,1e-8 → 4,4e-16`,
- `V_3 = 0,9515`,
- kayıp 0,019 pu,
- salınım barası 0,319 pu üretir.

## Q limiti: PV barası PQ olur

PV barası, gerilimini sabit tutmak için ne kadar reaktif gerekiyorsa onu üretir. Ama generatörün sınırı vardır. Yük akışı bunu şöyle uygular:

1. Yakınsadıktan sonra her PV barasının `Q`'sunu hesapla. Bu adım, santralden istenen reaktifi gösterir.
2. `Q > Q_max` ise barayı PQ yap, `Q = Q_max` olarak sabitle, gerilimi serbest bırak. Bu adım fiziksel sınırı modele yazar.
3. Yeniden çöz. Bu adım, sınırlı reaktifle oluşan yeni gerilimleri bulur.
4. Bara PQ iken gerilimi ayar değerinin üstüne çıkarsa (sınır artık bağlamıyorsa) PV'ye geri al. Bu adım gereksiz yere PQ'da kalmayı önler.

Üç baralı örnekte bara 2 gerilimini 1,02'de tutmak için 0,3995 pu reaktif üretiyor. Sınır 0,10 pu olarak verilince:

| | Sınırsız | `Q_max = 0,10` |
| --- | --- | --- |
| Bara 2 tipi | PV | PQ |
| Bara 2 gerilimi | 1,0200 | 0,9959 |
| Bara 3 gerilimi | 0,9515 | 0,9399 |
| Bara 2 reaktif üretimi | 0,3995 | 0,1000 |
| Salınım barası reaktifi | −0,0046 | +0,2939 |

Tabloyu şöyle oku:

- Santral reaktif veremeyince gerilimi tutamadı.
- Yük barası 0,94'e düştü.
- Eksik reaktif uzaktaki salınım barasından geldi.

Gerilim çökmesinin başlangıç mekanizması budur.

## Yakınsama sorunları

Yük akışı yakınsamıyorsa nedeni ya **veri** ya **fizik**tir. Önce veriye bak.

| Belirti | Olası neden | İlk bakılacak yer |
| --- | --- | --- |
| İlk turda devasa artık | Birim veya baz hatası (MW yerine pu, ohm yerine pu) | Girdi ölçekleri |
| Tek bir barada artık küçülmüyor | Ada: baranın şebekeyle bağlantısı yok | Topoloji, bağlı bileşen sayısı |
| Salınıyor, yakınsamıyor | PV–PQ geçişi iki bara arasında gidip geliyor | Geçiş mantığı, histerezis |
| Yavaş yakınsıyor, gerilimler düşük | Sistem gerçekten sınıra yakın | Yük seviyesi, reaktif kaynaklar |
| Hiç yakınsamıyor, yük artınca başladı | Çözüm yok: gerilim çökmesi noktası aşıldı | Yükü kademeli artır (sürekli yük akışı) |
| Sayısal hata, tekil matris | Sıfıra yakın empedans (kesici, kısa bağlantı), salınım barası yok | Küçük empedanslı dallar |

Çareler:

- daha iyi başlangıç (önceki çözüm veya DC çözümü),
- adım küçültme (sönümlü Newton),
- yükü kademeli artırma,
- reaktif sınırları ilk turlarda uygulamama.

Yazılım kuralı: yakınsamayan vaka **sessizce** sonuç dönmemeli. `nr_yuk_akisi.py` bu durumda `YakinsamaHatasi` fırlatır ve artık geçmişini taşır; bunu bir test sabitler.

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"Salınım barası en büyük santraldir."** | Matematiksel bir gerekliliktir. Seçimi sonuçları (özellikle kayıp dağılımını) etkiler; büyük sistemde dağıtılmış salınım kullanılır. |
| **"Yakınsamadıysa tur sayısını artırırım."** | Newton beş turda yakınsamadıysa elli turda da yakınsamaz. Nedenini ara. |
| **"Yakınsadıysa sonuç doğrudur."** | Yanlış veriyle de yakınsar. Ayrıca düşük gerilimli ikinci bir matematiksel çözüm vardır; kötü başlangıç oraya götürebilir. |
| **"PV barası hep PV kalır."** | Reaktif sınırına dayanınca PQ olur. |
| **"Açılar derece girilir."** | Denklemlerde radyan. En sık yapılan kod hatasıdır. |
| **"DC yük akışı doğru akımdır."** | Hayır; alternatif akım şebekesinin doğrusallaştırılmış aktif güç modelidir. |

## Panel takip sorusu

Panelin bu konudan sonra sorabileceği üç soru ve cevapları:

> Mülakatta şöyle söyle — "Jacobian'ı her turda yeniden mi kurarsın?" Cevap: tam Newton'da evet. Maliyeti düşürmek için birkaç tur aynı çarpanları kullanan yöntemler ve hızlı ayrık yöntem vardır; yakınsama hızı düşer, tur maliyeti azalır.

> Mülakatta şöyle söyle — "Düz başlatma neden çoğu zaman çalışır?" Cevap: sağlıklı şebekede gerilimler 1,0'a, açılar birbirine yakındır; başlangıç çözümün çekim bölgesindedir. Ağır yüklü veya bozuk veride çalışmaz.

> Mülakatta şöyle söyle — "Dağıtımda Newton neden zorlanır?" Cevap: R/X oranı yüksek, şebeke radyal, çok kısa ve çok uzun hatlar bir arada; matris kötü koşullu olur. İleri-geri süpürme veya akım enjeksiyonu yöntemi tercih edilir.

Aşağıdaki metin, bu sayfanın mülakatta yüksek sesle söylenecek özetidir.

## 90 saniye

> Mülakatta şöyle söyle: "Yük akışı, verilen üretim ve yük için bara gerilimlerini bulur. Güç gerilimin doğrusal olmayan işlevi olduğu için Newton-Raphson kullanırım: güç artığını hesaplar, Jacobian ile doğrusallaştırır, açı ve gerilim düzeltmesini çözer, tekrarlarım. Jacobian, admitans matrisiyle aynı seyrek yapıdadır ve yakınsama ikinci derecedendir; sağlıklı vaka üç-beş turda biter. Üretim barası reaktif sınırına dayanırsa yük barasına çevirir, yeniden çözerim. Yakınsamayan vakada önce veriye, adaya ve birime, sonra sistemin gerçekten sınırda olup olmadığına bakarım."
