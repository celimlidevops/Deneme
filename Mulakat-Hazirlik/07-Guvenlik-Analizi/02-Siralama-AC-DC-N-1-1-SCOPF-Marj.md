# Sıralama, N-1-1, SCOPF, marj

Bu sayfa güvenlik analizinin hesap tarafını anlatır. Başlık konularının tamamı şunlardır: beklenmeyen durum sıralaması, AC ve DC N-1, N-1-1, SCOPF, güvenlik marjı.

Kısaltmalar:

- **AC** (alternatif akım) yük akışı: gerilim genliği, açı, aktif ve reaktif gücü birlikte çözen tam, doğrusal olmayan model.
- **DC** yük akışı: yalnız aktif güç ve açıyı kullanan doğrusal yaklaşım.
- **LODF** (Line Outage Distribution Factor, hat açma dağılım katsayısı): bir hat açılınca akışının diğer hatlara hangi oranla dağıldığını veren katsayı.
- **SCOPF** (Security-Constrained Optimal Power Flow): güvenlik kısıtlı optimal güç akışı.
- **SIPS** (System Integrity Protection Scheme): sistem bütünlüğü koruma şeması, yani özel koruma sistemi.
- **pu** (per unit, birim değer): büyüklüğün seçilmiş bir taban değere oranı.

## Problem

Güvenlik analizi şunu sorar: şu anki işletme noktasında herhangi bir eleman devre dışı kalırsa sistem sınırlar içinde kalır mı?

Zorluk ölçektir:

- Türkiye ölçeğinde binlerce hat ve trafo vardır.
- Operatör bu cevabı birkaç dakikada bir, taze durum kestirimiyle isteyecektir.
- Hepsini tam AC yük akışıyla çözmek pahalıdır.
- Çoğu arıza da zararsızdır.

Çözüm üç kademelidir. Aşağıdaki akış, vakaların her kademede nasıl azaldığını gösterir: ucuz yöntem herkese, pahalı yöntem yalnız kritik olanlara uygulanır.

```
Bütün arızalar  →  hızlı tarama (DC, LODF)  →  sıralama  →  kritik olanlara AC yük akışı  →  en kritiklere dinamik benzetim
```

## Performans indeksi ile sıralama

Her arıza için tek bir sayı üretilir; büyük olan önce incelenir. Aşağıdaki iki formül, biri hat akışları biri bara gerilimleri için bu sayıyı hesaplar.

```
PI_akış    = Σ  w_l (P_l / P_l,sınır)^(2n)
PI_gerilim = Σ  w_i (|V_i − V_i,nom| / ΔV_sınır)^(2n)
```

| Sembol | Anlamı |
| --- | --- |
| `PI` | Performans indeksi |
| `w_l`, `w_i` | Hat veya baranın önem ağırlığı |
| `P_l / P_l,sınır` | Hattın yüklenme oranı |
| `|V_i − V_i,nom| / ΔV_sınır` | Gerilimin nominalden sapmasının izin verilen sapmaya oranı |
| `n` | Üstel |

`n = 1` hesabı kolaydır ama **maskeleme** yapar: çok sayıda orta yüklü hat, tek bir aşırı yüklü hattan daha yüksek puan alabilir. `n` büyüdükçe indeks, en kötü elemana odaklanır.

> **Sade anlatım:** Oran 1'den küçükse yüksek kuvvet onu sıfıra yaklaştırır, 1'den büyükse şişirir. Böylece büyük üs, limiti aşan hattı öne iter.

### Elle örnek

**Adım 1 — Şebekeyi kur.** Bu adım, hesabın hangi şebeke ve hangi sınırlarla yapılacağını belirler.

`03` klasöründeki üç baralı şebeke kullanılır. Sınırlar: hat 1–2 için 0,5; hat 1–3 ve 2–3 için 0,6 pu.

**Adım 2 — Her arıza için kalan akışları ve yüklenmeyi yaz.** Bu adım, her hat açıldığında geri kalan hatların ne kadar yüklendiğini gösterir. Yüklenme, akışın sınıra bölünmesidir.

Arıza sonrası akışlar (DC):

| Arıza | Kalan hat akışları | Yüklenme |
| --- | --- | --- |
| 1–3 açık | 1–2: 0,30 ve 2–3: 0,80 | %60 ve **%133** |
| 1–2 açık | 1–3: 0,30 ve 2–3: 0,50 | %50 ve %83 |
| 2–3 açık | 1–2: 0,50 ve 1–3: 0,80 | %100 ve **%133** |

**Adım 3 — `n = 1` ile indeksi hesapla.** Bu adım, her yüklenme oranının karesini alıp toplar ve arızaya tek bir puan verir (ağırlıklar 1 alınmıştır).

`n = 1` ile:

```
1–3 açık:  0,60² + 1,333² = 0,36 + 1,78 = 2,14
1–2 açık:  0,50² + 0,833² = 0,25 + 0,69 = 0,94
2–3 açık:  1,00² + 1,333² = 1,00 + 1,78 = 2,78
```

**Adım 4 — Sırala.** Bu adım, puanı en büyük arızayı incelenecekler listesinin başına koyar.

Sıra: 2–3, sonra 1–3, sonra 1–2.

**Adım 5 — Üssü büyüt ve karşılaştır.** Bu adım, yüksek üssün ihlalli ve ihlalsiz vakaları ne kadar net ayırdığını gösterir.

`n = 5` ile değerler 18,8; 17,8 ve 0,16 olur. İhlal olan ile olmayan arasındaki fark 3 kattan 100 kata çıktı; ayrım netleşti.

**Adım 6 — Sonucu yorumla.** Bu adım, sayının arkasındaki işletme veya planlama sorununu okur.

İkinci ders: bara 3'ün 0,8'lik yükü, her biri 0,6 taşıyabilen iki hatla besleniyor. Birini kaybedince diğeri yetmez. Bu, **üretimi yeniden dağıtarak çözülemez**, çünkü bara 3'e başka yol yoktur.

Geriye üç seçenek kalır:

- Yük atma
- Bara 3'te yerel üretim
- Üçüncü bir hat

Bu bir işletme değil **planlama** sorunudur.

## DC ile AC N-1

İki model birbirinin rakibi değil, tamamlayıcısıdır. DC eler, AC doğrular.

| | DC tarama | AC doğrulama |
| --- | --- | --- |
| Model | `P = B θ`, doğrusal | Tam doğrusal olmayan yük akışı |
| Hız | Çok hızlı; LODF ile çözüm bile gerekmez | Her arıza için yineleme |
| Görür | Aktif güç akışı, ısıl aşırı yük | Isıl, gerilim, reaktif sınır |
| Görmez | Gerilim, reaktif güç, kayıp | Dinamik davranış |
| Hata | İletimde akışta tipik olarak birkaç yüzde; ağır yükte ve yüksek R/X'te artar | Model ve veri kadar doğru |
| Yakınsama | Her zaman çözer | Yakınsamayabilir; bu da bir bulgudur |

`P = B θ` formülünde `P` bara aktif güçleri, `B` susseptans matrisi, `θ` bara açılarıdır. R/X, hattın direncinin reaktansına oranıdır.

Kurallar:

- DC taramada sınıra yakın çıkan (örneğin %90 üstü) her vakayı AC'ye gönder. DC'nin hata payı kadar tampon bırak.
- Gerilim sorunu olduğu bilinen bölgeleri DC sonucuna bakmadan AC ile çöz.
- AC yakınsamazsa vakayı atma. Gerilim çökmesi adayıdır ve listenin başına yazılır.
- Arıza sonrası otomatik tepkileri modelle:
  - generatör reaktif sınırları,
  - kademe değiştirici,
  - özel koruma sistemi,
  - salınım barası yerine üretimin governor (hız regülatörü) payına göre dağıtılması.

## N-1-1 ve N-2

| Ölçüt | Tanım | Örnek veya kural |
| --- | --- | --- |
| **N-1** | Tek eleman kaybı | Türkiye şebeke yönetmeliğinin planlama ölçütü (nükleer bağlantı noktasında N-2) |
| **N-2** | İki elemanın **aynı anda** kaybı | Ortak direkteki çift devre hat, bara arızası, kesici arızası gibi ortak nedenli olaylar |
| **N-1-1** | Bir eleman kaybedilir, operatör sistemi **yeniden ayarlar** (30 dakika gibi bir sürede), sonra ikinci eleman kaybedilir | Bakım sırasında ikinci arıza |

N-1-1'in N-2'den farkı aradaki ayardır. İlk arızadan sonra sistem N-1 güvenli değildir; operatörün işi onu yeniden N-1 güvenli hale getirmektir.

Bakım planlaması da aynı mantıktır: bir hat bakıma alındığında kalan sistem N-1 sağlamalıdır.

Vaka sayısı hızla büyür:

- `n` eleman için N-1 `n` vakadır.
- N-2 yaklaşık `n²/2` vakadır. 5.000 eleman için 12,5 milyon.

Hepsi çözülmez; ortak nedenli ve ağır sonuçlu çiftler seçilir.

## SCOPF: güvenlik kısıtlı optimal güç akışı

OPF (Optimal Power Flow, optimal güç akışı), en ucuz üretimi şebeke sınırları içinde bulur. SCOPF, buna "her N-1 durumunda da sınırlar korunmalı" koşulunu ekler.

Aşağıdaki problem, baz durum maliyetini en küçüklerken her arıza durumunda da denklemlerin ve sınırların sağlanmasını ister.

```
en küçük  maliyet(u_0)
öyle ki   baz durum denklemleri ve sınırları        g_0(x_0, u_0) = 0,  h_0 ≤ 0
          her k arızası için                        g_k(x_k, u_k) = 0,  h_k ≤ 0
          |u_k − u_0| ≤ Δu_k                        (arıza sonrası yapılabilecek ayar)
```

| Sembol | Anlamı |
| --- | --- |
| `u_0` | Baz durumdaki kontrol değişkenleri (üretim, kademe vb.) |
| `x_0`, `x_k` | Baz ve k. arıza durumundaki durum değişkenleri (gerilim, açı) |
| `g` | Yük akışı denklemleri |
| `h` | Sınırlar (akış, gerilim) |
| `Δu_k` | Arızadan sonra kontrolde izin verilen değişim |

İki tür:

- **Önleyici (preventive):** `Δu = 0`. Baz durum öyle seçilir ki arızadan sonra **hiçbir şey yapmadan** sınırlar korunur. Pahalı, basit, güvenli.
- **Düzeltici (corrective):** arızadan sonra kısa sürede yapılabilecek ayarlara izin verir (hızlı yeniden dağıtım, faz kaydırıcı, özel koruma sistemi). Daha ucuz; ama o ayarın gerçekten zamanında yapılacağına güvenir. Hatların kısa süreli aşırı yük dayanımı bu zamanı verir.

### Boyut sorunu

Her arıza, değişkenlerin bir kopyasını ekler. Bin arıza, bin katı büyük problem demektir.

Pratik çözüm, arızaların çoğunun bağlayıcı olmamasına dayanır:

1. Önce arızasız çöz.
2. İhlal üreten arızaları bul.
3. Yalnız onları ekle.
4. Tekrar çöz.

Bu yönteme kısıt üretimi denir; Benders ayrıştırması da bu ailedendir.

### SIPS ile bağ

SIPS düzeltici bir eylemdir. Sistemi, önleyici ölçütün izin verdiğinden daha yüklü ve daha ucuz işletmeyi mümkün kılar. Karşılığında SIPS'in güvenilirliği sistemin güvenliğinin parçası olur.

## Güvenlik marjı

"Güvenli" evet-hayır değil, mesafedir. Dört marj vardır:

| Marj | Tanım | Örnek |
| --- | --- | --- |
| Isıl | `(sınır − arıza sonrası akış) / sınır` | Sınır 0,6; akış 0,5 → %17 |
| Gerilim kararlılığı | Çökme noktasına kadar artırılabilecek yük (MW) | P–V eğrisinin burnuna uzaklık |
| Geçici hal | Kritik temizleme süresi − koruma temizleme süresi | 302 ms − 150 ms = 152 ms |
| Frekans | Kalan yedek, en büyük ünite kaybına göre | Atalet ve primer yedek |

Isıl örneğin adımı: `(0,6 − 0,5) / 0,6` hesaplanır; bu, hattın sınırına kadar kalan payı oran olarak verir.

Geçici hal örneğinin adımı: kritik temizleme süresinden (302 ms) korumanın arızayı gerçekte temizlediği süre (150 ms) çıkarılır; kalan 152 ms, korumanın gecikebileceği zaman payıdır.

Marj neden bırakılır?

- Tahmin hatası
- Model hatası
- Ölçüm hatası
- Zaman gecikmesi

Marj fazlaysa şebeke boşa çalışır, azsa risk büyür. Olasılıksal güvenlik değerlendirmesi, marjı sabit bir yüzde yerine arıza olasılığı ve sonucuyla tartar.

### Operatör durumları

| Durum | Anlamı |
| --- | --- |
| **Normal** | N-1 güvenli |
| **Alarm** | Sınırlar içinde ama N-1 güvenli değil |
| **Acil** | Sınır ihlali var |
| **Çöküş** | Sistem parçalanmış veya kararmış |
| **Toparlanma** | Sistem yeniden kuruluyor |

Güvenlik analizinin işi, sistemi alarm durumuna girmeden önce uyarmaktır.

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"N-1, bir santral kaybı demektir."** | Hat, trafo, generatör, bara, kompanzatör: herhangi bir tek eleman. |
| **"DC taramada ihlal yoksa sistem güvenlidir."** | DC gerilimi görmez. |
| **"AC yakınsamadıysa vaka bozuktur, atlarım."** | En tehlikeli vaka o olabilir. |
| **"N-1-1 ile N-2 aynıdır."** | Arada operatörün ayarı vardır. |
| **"Her ihlal yeniden dağıtımla çözülür."** | Elle örnekteki gibi, yük tek koridordan besleniyorsa çözülmez. |
| **"Performans indeksi yüksekse ihlal vardır."** | `n = 1` ile ihlalsiz bir vaka, ihlalli bir vakanın üstüne çıkabilir. |

## Panel takip sorusu

**"Beş bin arızayı beş dakikada nasıl koşarsın?"**

> **Mülakatta şöyle söyle:** LODF ile doğrusal tarama, sınıra yakın olanlara AC; AC vakaları bağımsızdır, paralel koşarım; hepsi aynı baz çözümden başlar; baz matrisin çarpanlarını tek hat çıkarma için düşük ranklı güncellemeyle yeniden kullanırım.

Düşük ranklı güncelleme, tek bir hat çıkınca matrisi baştan ayrıştırmak yerine eski ayrıştırmayı küçük bir düzeltmeyle yeniden kullanmaktır.

**"Önleyici mi düzeltici mi?"**

> **Mülakatta şöyle söyle:** Düzeltici eylem hızlı, otomatik ve güvenilirse düzeltici daha ekonomiktir. Eylem operatöre bağlıysa veya süre yetmiyorsa önleyici. Gerçek sistemde ikisi karışıktır.

Aşağıdaki konuşma metni sayfanın sözlü özetidir. İçinde “doğrusal model” DC yük akışını, “hat açma katsayıları” LODF'yi, “güvenlik kısıtlı optimal güç akışı” SCOPF'yi anlatır.

## 90 saniye

> **Mülakatta şöyle söyle:** "Güvenlik analizinde bütün tek eleman kayıplarını üç kademede tararım. Önce doğrusal modelle ve hat açma katsayılarıyla hızlı tarama yapar, performans indeksiyle sıralarım; indeksin üssünü yüksek tutarım ki orta yüklü çok hat tek bir ağır ihlali maskelemesin. Sınıra yakın vakaları AC yük akışıyla doğrularım, çünkü doğrusal model gerilimi görmez; yakınsamayan vaka da bir bulgudur. Güvenlik kısıtlı optimal güç akışı bu denetimi üretim planına gömer: önleyici olan arızadan sonra hiçbir şey yapmadan, düzeltici olan hızlı bir eylemle sınırı korur. Sonucu marj olarak raporlarım."
