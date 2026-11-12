# Büyüklükler, birim sistem ve modeller

Bu sayfa klasörün yoğun özetidir. İlk kez okuyorsan önce `02`–`06` dosyalarını oku, bu sayfaya en son gel. Burada her konu kısa tutulmuş ama hiçbir olgu atlanmamıştır.

## Güç

Gerilim ve akım sinüs biçimindeyse (sinüzoidal durum), onları fazörle, yani büyüklük ve açıdan oluşan karmaşık sayıyla anlatmak yeter.

Anlık güç iki parçaya ayrılır:

- **Ortalama kısım:** iş yapan, zamanla değişmeyen kısım.
- **Salınım kısmı:** frekansın iki katında gidip gelen kısım.

Üç faz dengeli sistemde üç fazın salınımları birbirini götürür. Toplam anlık güç sabittir. Bu yüzden iletim planlaması etkin değerle (RMS, aynı ısıyı üreten doğru akım eşdeğeri) yürür.

Aşağıdaki blok, gücün temel formüllerini toplar. `S` görünür güç, `P` aktif güç, `Q` reaktif güç, `V_f` ve `I_f` faz büyüklükleri, `V_L` ve `I_L` hat büyüklükleridir. `*` karmaşık eşlenik demektir. `pf` güç faktörüdür (power factor).

```
S = P + jQ = 3 V_f I_f* = √3 V_L I_L*
|S| = √(P² + Q²)
pf = P / |S| = cos φ
Q > 0  endüktif (akım geride)
```

İşaret sözleşmesini her yazılımda kontrol et. Bazı paketler yükü pozitif çeker, bazıları enjeksiyonu (baraya verilen gücü) pozitif sayar.

> Mülakatta şöyle söyle: "İşaret sözleşmesini baştan sabitlerim." Bu cümle hata ayıkladığını gösterir.

Güç faktörünü düzeltmek, aynı aktif güç için akımı düşürür. Hat kaybı ve gerilim düşümü farklı şeylere bağlıdır:

| Büyüklük | Neye bağlı |
| --- | --- |
| Hat kaybı | `I²R`, yani akımın karesi ve direnç |
| Gerilim düşümü | Hem `R` hem `X` (reaktans) |

Hangi parametrenin baskın olduğu gerilim seviyesine göre değişir:

| Seviye | Baskın parametre |
| --- | --- |
| İletim | `X` baskın |
| Dağıtım OG (orta gerilim) | `R` ve `X` birlikte |
| Dağıtım AG (alçak gerilim) | `R` baskınlaşır |

> Mülakatta şöyle söyle: "İletim formülünü dağıtıma neden taşımam?" sorusunun cevabı bu tek cümledir: iletimde X baskın, AG'de R baskındır.

## Fazör ve referans

Gerilim açısı bağıl bir büyüklüktür. Tek başına anlamı yoktur, bir referansa göre söylenir.

- Slack (salınım) baranın açısı referanstır, yani 0 kabul edilir.
- Aktif güç, gerilim açısı yüksek olan baradan düşük olan baraya akar.
- Mutlak zaman bilgisi ancak PMU (Phasor Measurement Unit, fazör ölçüm birimi) ile gelir.
- Klasik SCADA (Supervisory Control and Data Acquisition, uzaktan izleme ve kontrol sistemi) faz açısını doğrudan ölçmez. Açıyı durum kestirimi hesaplar.

## Birim sistem

Büyük şebekede 400 kV ile 0,4 kV aynı matriste buluşur. Per-unit (birim değer, pu) her büyüklüğü bir baz değere bölerek bunu ölçekler. Ayrıca trafo sargılarının dönüştürme oranını yutar, böylece admitans matrisi sadeleşir.

Aşağıdaki blok dört temel büyüklüğün pu tanımını ve iki türetilmiş bazı verir. `I_baz` ve `Z_baz`, seçilen `S_baz` ve `V_baz`'dan hesaplanır.

```
S_pu = S_gercek / S_baz
V_pu = V_gercek / V_baz
I_pu = I_gercek / I_baz ,   I_baz = S_baz / (√3 V_baz)
Z_pu = Z_gercek / Z_baz ,   Z_baz = V_baz² / S_baz
```

Kurallar:

- Sistemde tek `S_baz` seçilir. 100 MVA alışkanlıktır; paket ne kullanıyorsa onu söyle.
- Her gerilim bölgesinin kendi `V_baz`'ı vardır. Nominal gerilim çoğunlukla baz alınır.
- `Z_pu` yeni baza `Z_yeni = Z_eski * (S_yeni/S_eski) * (V_eski/V_yeni)²` ile taşınır.
- Trafo kaçak reaktansı kendi plaka bazında verilir. Sistem bazına çevrilmeden Ybus'a (bara admitans matrisi) girmez.
- Kademe, off-nominal oran (nominalden farklı dönüştürme oranı) `t` olarak π modeline girer. Admitans `y/t²`, `y/t` şeklinde iki yana dağılır. Faz kaydırıcıda `t` karmaşık olur.
- Per-unit güç üç faz toplamıdır. Tek faz formülüyle üç faz gücünü karıştırmak klasik hatadır.

Mülakat türevi, adım adım:

1. 400 kV'ta 100 MVA bazda `Z_baz = V²/S = 1600 ohm`. Bu adım, o gerilim bölgesinde "1 pu empedans" kaç ohm eder onu bulur.
2. 10 ohm'luk bir hat `10/1600 = 0,00625 pu`'dur, yani çok kısadır. Bu adım ohm değerini baza bölerek elektriksel uzunluğu gösterir.
3. Aynı ohm, 34,5 kV'ta çok daha büyük pu olur. Çünkü `Z_baz` gerilimin karesiyle küçülür.

> Mülakatta şöyle söyle: "400 kV'ta 100 MVA bazda Z_baz = V²/S = 1600 ohm. 10 ohm'luk bir hat 10/1600 = 0,00625 pu'dur, yani çok kısadır. Aynı ohm, 34,5 kV'ta çok daha büyük pu olur."

Bu örnek, kısa devre gücünün gerilimle neden patladığını da anlatır.

## Tek hat ve şebeke elemanları

Tek hat şeması, üç fazın simetrik olduğunu varsayar ve üç fazı tek çizgiyle gösterir. Üzerindeki her elemanın bir admitansı veya bir eşdeğer devresi vardır.

### Hat

Hat modeli uzunluğa göre seçilir:

| Hat | Model |
| --- | --- |
| Kısa | Kapasite ihmal edilir, yalnız seri `Z` |
| Orta | Nominal π: seri `Z`, iki uca yarı yarıya şönt `B/2` |
| Uzun | Dağıtılmış parametre, ABCD parametreleri veya hiperbolik fonksiyonlar |

- 150 km üstü pratikte uzun sayılır.
- 400 kV'ta Ferranti etkisi (açık uçta gerilim yükselmesi) π modeliyle bile görünür.
- Sürşarj empedansı (karakteristik empedans) `Zc = √(z/y)`'dir.
- Doğal güç (SIL, Surge Impedance Loading) `SIL ≈ V²/Zc`'dir.
- Hattı SIL altında işletmek kapasitif, üstünde endüktif davranış üretir.
- 400 kV havai hatta SIL kabaca birkaç yüz MW mertebesindedir.

> Mülakatta şöyle söyle: "Rakamı hat verisinden hesaplarım, ezberlemem."

### Trafo

Trafo modelinin parçaları:

- Seri kaçak empedansı.
- Kademe.
- İsteğe bağlı kaydırma açısı.
- İsteğe bağlı mıknatıslanma kolu.

Mıknatıslanma kolu yük akışında çoğu zaman ihmal edilir. Kısa devrede ve ferrorezonansta (demir çekirdek ile kapasitenin doğrusal olmayan rezonansı) ihmal edilmez.

Üç sargılı trafo üç bara ve bir yıldız noktasıyla modellenir.

OLTC (On-Load Tap Changer, yük altında kademe değiştirici) gerilimi kademe adımıyla tutar. Adım çoğunlukla %1–1,25'tir. Dinamik ve günlük işletmede kademe değişimi ayrı bir kontrol döngüsüdür. Kademe sınırına dayanmış trafo, gerilim sorununu "daha fazla kademe" ile çözemez.

### Senkron makine

Senkron makinede üç farklı reaktans üç farklı hesaba girer:

| Durum | Kullanılan model |
| --- | --- |
| Sürekli hal | İç gerilim ve senkron reaktans: `E = V + j X_s I` |
| Açı kararlılığı | Geçici reaktans ve atalet |
| Kısa devrenin ilk çevrimleri | Alt geçici reaktans `X''` akımı belirler |

Üç reaktansı karıştırmak hem kararlılık hem kesici hesabını bozar.

### Yük

- Sabit P-Q, planlama ve iletim yük akışının varsayılanıdır.
- Gerçek yük, gerilim düşünce gücünü azaltır.
- ZIP modeli (Z: sabit empedans, I: sabit akım, P: sabit güç karışımı) `P = P0 (a_z V² + a_i V + a_p)` şeklindedir.
- Gerilim kararlılığında sabit güç kötümser, sabit empedans iyimser sonuç verir. Hangi varsayımı kullandığını söylemeden "sistem çöker" deme.
- Motor yükü ek olarak frekansa ve yeniden yol alma akımına duyarlıdır.

## Simetrik bileşenler

Dengesiz arıza ve dengesiz yükte üç fazı faz faz yazmak zordur. Simetrik bileşenler, üç fazı üç ayrık, dengeli diziye böler. Bu dönüşüm Fortescue dönüşümüdür.

Aşağıdaki blok, dizi gerilimlerinden (`V0`, `V1`, `V2`) faz gerilimlerine (`Va`, `Vb`, `Vc`) geçişi gösterir. `a`, 120° döndürme operatörüdür.

```
[Va]   [1  1  1] [V0]
[Vb] = [1  a² a] [V1]
[Vc]   [1  a  a²] [V2]

a = e^{j120°} = -1/2 + j√3/2
```

Ters dönüşümde `V1`, `V2`, `V0` aynı matrisin eşleniğiyle, 1/3 çarpanıyla gelir.

| Dizi | Anlamı |
| --- | --- |
| Artı dizi | Normal işletmenin döndüğü şebeke |
| Eksi dizi | Ters yönlü döner alan. Generatör rotorunda ısınır, korumada dengesizlik ölçüsüdür |
| Sıfır dizi | Üç fazda aynı yönlü akım. Dönüş yolu topraktan veya nötrden geçer. Üçgen sargı ve topraklanmamış yıldız sıfır diziyi geçirmez |

Hat ve trafonun artı ve eksi dizi empedansı pratikte yakındır. Sıfır dizi çok farklıdır. Onu toprak dönüşü, kule, guard teli (koruma iletkeni) ve trafo bağlantı grubu belirler. Kısa devre yazılımında "sıfır dizi verisi yok" ise sonuç çöptür.

Arıza yerinde dizi devrelerinin bağlantısı:

| Arıza | Dizi bağlantısı |
| --- | --- |
| Üç faz dengeli | Yalnız artı dizi |
| Tek faz-toprak | Üç dizi seri |
| İki faz | Artı ve eksi paralel, sıfır yok |
| İki faz-toprak | Üçü birden, artıya eksi ve sıfırın paraleli |

Topraklama direnci ve arıza direnci bu eşdeğer devreye seri girer. Dirençli arıza, metalik arızadan daha küçük akım ve daha zor algılanan röle koşulu demektir.

## P–δ ve Q–V

Kısa bir hatta direnç ihmal edilirse iki uç arasındaki güç akışı aşağıdaki gibidir. `V_s` gönderen uç, `V_r` alıcı uç gerilimi, `X` hat reaktansı, `δ` iki uç arasındaki açı farkıdır.

```
P = (V_s V_r / X) sin δ
Q_r ≈ (V_r (V_s cos δ - V_r)) / X
```

Küçük açıda `P` açıyla, `Q` gerilim farkıyla gider. Operatör sezgisi buradan gelir:

- Aktif güç dengesi frekansı ve açıyı belirler.
- Reaktif güç dengesi gerilimi belirler.

Dağıtımda `R` büyükse bu ayrışma bozulur; aktif güç de gerilimi oynatır. Çatı güneşinin AG'de gerilimi yükseltmesinin nedeni budur.

Senkronizasyon gücü, açı biraz değişince gücün ne kadar değiştiğidir: `dP/dδ = (V_s V_r / X) cos δ`.

- Açı 90°'ye geldikçe bu türev sıfıra iner. Sistem açı olarak marjını kaybeder.
- Kararlı hal açı sınırı ile geçici hal sınırı aynı sayı değildir.
- Geçici halde atalet ve arıza temizleme süresi devreye girer.

## Kapasitenin üç sınırı

Bir hattın taşıyabileceği güç üç ayrı nedenle sınırlanır:

1. **Termik:** iletken sıcaklığı, sehim, hızlandırılmış yaşlanma. Mevsim ve rüzgârla değişir. Dinamik hat kapasitesi bu sınırı ölçümle gevşetir.
2. **Gerilim:** özellikle uzun ve zayıf hatlarda, yük artınca alıcı uç çöker veya hafif yükte Ferranti etkisiyle yükselir.
3. **Kararlılık:** açı, gerilim veya bölgeler arası salınım.

Kısa hatlar çoğunlukla termik sınıra, uzun hatlar kararlılık sınırına takılır.

Yazılım "hat yüzde 80 yüklü" diyorsa bunun hangi limite göre yüzde olduğunu sor. Termik yüzde ile kararlılık marjı aynı eksen değildir.

Aşağıdaki metin, bu sayfanın tamamını mülakatta 90 saniyede anlatmak içindir.

## 90 saniye

> “Dengeli işletmede tek hat ve per-unit yeter. Güç aktif ve reaktif diye ayrılır; iletimde P açıyla, Q gerilimle gider, dağıtımda R yüzünden bu ayrışır. Arıza ve dengesizlikte simetrik bileşenlere inerim: tek faz-toprak üç diziyi seri bağlar, sıfır dizi ise trafo bağlantısı ve topraklamayla belirlenir. Hat kapasitesini termik, gerilim ve kararlılık diye üç ayrı limite bölerim.”
