# PTDF, LODF, NTC/ATC ve kısıt

Bu sayfa, iletim güvenlik analizinde kullanılan iki duyarlılık katsayısını (PTDF ve LODF), sınır ötesi kapasite kavramlarını (TTC, TRM, NTC, AAC, ATC) ve Türkiye'de iletim kısıtının nasıl oluşup yönetildiğini anlatır.

## Neden bu iki katsayı

Güvenlik analizi "şu hat açılırsa ne olur" sorusunu binlerce kez sorar. Her biri için yük akışını baştan çözmek pahalıdır.

DC yaklaşımında şebeke doğrusaldır. DC yaklaşımı; gerilimleri 1 pu, hat direncini sıfır ve açı farklarını küçük kabul edip yalnız aktif gücü hesaplayan sade modeldir. Doğrusal sistemde her sorunun cevabı önceden hesaplanmış bir katsayıdır.

> **Sade anlatım:** Yazılımcı gözüyle bu, pahalı bir işlevin sonucunu önceden hesaplayıp tabloya koymaktır.

- **PTDF** (güç transfer dağıtım katsayısı): Bir baraya 1 MW enjekte edip referans baradan çekersem, bu 1 MW'ın ne kadarı hangi hattan geçer?
- **LODF** (hat açma dağıtım katsayısı): Bir hat açılırsa, üzerindeki akışın ne kadarı diğer hatlara biner?

Aşağıdaki üç satır, katsayıların formülüdür. İlki PTDF'yi reaktans matrisinden, ikincisi LODF'yi PTDF'den hesaplar. Üçüncüsü, hat açılınca yeni akışı eski akışlardan bulur.

```
PTDF_(ij),k = (X_ik − X_jk) / x_ij           X = B⁻¹ (referans bara satır ve sütunu sıfır)
LODF_(l),k  = PTDF_l(k hattının uçları arası transfer) / (1 − PTDF_k(aynı transfer))
Yeni akış_l = Eski akış_l + LODF_(l),k × Eski akış_k
```

Semboller:

| Sembol | Anlamı |
| --- | --- |
| `i`, `j` | Hattın iki ucundaki baralar |
| `k` | Enjeksiyonun yapıldığı bara (PTDF'de) veya açılan hat (LODF'de) |
| `l` | Etkisine bakılan hat |
| `x_ij` | i–j hattının reaktansı |
| `B` | Bara süseptans matrisi |
| `X` | `B`'nin tersi |

## Elle örnek

`05` klasöründeki üç baralı şebeke kullanılır:

- Hat reaktansları: `x12 = 0,10`, `x13 = 0,20`, `x23 = 0,25` pu (birim değer).
- Bara 1 referans.
- Bara 2 üretim +0,5, bara 3 yük −0,8.

**Adım 1, B matrisi (referans bara çıkarılmış).** Bu adım şebekenin bağlantı ve reaktans bilgisini tek bir matrise koyar. Köşegen, baraya bağlı hatların `1/x` toplamıdır. Köşegen dışı, iki bara arasındaki hattın `−1/x` değeridir.

```
B = [ 1/0,1 + 1/0,25    −1/0,25        ]  =  [ 14   −4 ]
    [ −1/0,25           1/0,2 + 1/0,25 ]     [ −4    9 ]
```

**Adım 2, tersi.** Bu adım, enjeksiyondan bara açısına geçen `X` matrisini bulur. 2×2 matrisin tersi için önce determinant hesaplanır: `14 × 9 − 16 = 110`.

```
X = (1/110) [ 9   4 ]  =  [ 0,0818  0,0364 ]
            [ 4  14 ]     [ 0,0364  0,1273 ]
```

**Adım 3, PTDF.** Bu adım, her baraya yapılan 1 birim enjeksiyonun her hatta ne kadar akış yarattığını formülle hesaplar. Bara 1 referans olduğu için `X_1k = 0`.

| Hat | Bara 2'ye enjeksiyon | Bara 3'e enjeksiyon |
| --- | --- | --- |
| 1–2 | `(0 − 0,0818)/0,1 = −0,8182` | `(0 − 0,0364)/0,1 = −0,3636` |
| 1–3 | `(0 − 0,0364)/0,2 = −0,1818` | `(0 − 0,1273)/0,2 = −0,6364` |
| 2–3 | `(0,0818 − 0,0364)/0,25 = +0,1818` | `(0,0364 − 0,1273)/0,25 = −0,3636` |

Tabloyu okuma: Bara 2'ye enjekte edilen 1 MW'ın %82'si 1–2 hattından doğrudan, %18'i 2–3 ve 3–1 üzerinden dolanarak referansa gider. Güç en kısa yoldan değil, **empedansla ters orantılı olarak bütün yollardan** akar.

**Adım 4, baz akışlar.** Bu adım, gerçek üretim ve yükü PTDF'lerle çarpıp her hattın normal durumdaki akışını bulur. Akış = PTDF × enjeksiyon:

```
P12 = −0,8182 × 0,5 + (−0,3636) × (−0,8) = −0,1182
P13 = −0,1818 × 0,5 + (−0,6364) × (−0,8) = +0,4182
P23 = +0,1818 × 0,5 + (−0,3636) × (−0,8) = +0,3818
```

Kontrol: Bara 3'e giren `0,4182 + 0,3818 = 0,80`. Bara 3'teki yük 0,8 olduğu için hesap tuttu.

**Adım 5, hat 1–3 açılırsa.** Bu adım, LODF ile açılan hattın akışını kalan hatlara dağıtır ve yeni akışları yük akışı çözmeden bulur. Üç baralı halkada tek alternatif yol 1–2–3'tür. Bu yüzden iki LODF de 1,0'dır:

```
P12 yeni = −0,1182 + 1,0 × 0,4182 = 0,30
P23 yeni =  0,3818 + 1,0 × 0,4182 = 0,80
```

Sağduyu kontrolü: Yük 0,8; bara 2 0,5 üretiyor. Kalan 0,3 referanstan 1–2 üzerinden gelir ve 0,8'in tamamı 2–3'ten geçer. Tuttu.

**Sonuç.** Hat 2–3'ün limiti 0,6 ise bu arıza %133 aşırı yük demektir. Sistem N-1 güvenli değildir. N-1 güvenli, herhangi bir eleman tek başına düştüğünde hiçbir limitin aşılmaması demektir.

## PTDF nerede kullanılır

- N-1 taraması (LODF ile, yük akışı çözmeden)
- Kısıt yönetimi: Hangi santrali 1 MW azaltırsam o hat kaç MW rahatlar?
- Bölgesel fiyatın kısıt bileşeni (`13` klasörü)
- Sınır ötesi kapasite hesabı (akış tabanlı yöntem)

Sınırları:

- Doğrusaldır ve yalnız aktif gücü hesaplar.
- Gerilimi ve reaktif gücü görmez.
- Topoloji değişince yeniden hesaplanır.

## NTC ve ATC

Bu kavramlar, iki bölge arasında ticarete ne kadar kapasite verilebileceğinin hesabıdır. ENTSO-E (Avrupa iletim sistemi operatörleri ağı) tanımları:

| Kısaltma | Açılımı | Anlam |
| --- | --- | --- |
| TTC | Toplam transfer kapasitesi | Güvenlik kriterleri (N-1 dahil) bozulmadan aktarılabilecek en büyük güç |
| TRM | İletim güvenilirlik payı | Frekans regülasyonu sapmaları, acil yardım ve ölçüm belirsizliği için ayrılır |
| NTC | Net transfer kapasitesi | NTC = TTC − TRM |
| AAC | Önceden tahsis edilmiş kapasite | Daha önce kullanıcılara verilmiş kısım |
| ATC | Kullanılabilir transfer kapasitesi | ATC = NTC − AAC |

Elle örnek:

1. TTC 1000 MW, TRM 100 MW ise NTC = 1000 − 100 = 900 MW. Bu adım güvenlik payını düşer.
2. 600 MW önceden tahsis edildiyse ATC = 900 − 600 = 300 MW. Bu adım, satılmış kısmı düşüp piyasaya kalanı bulur.

TTC'yi çoğunlukla hattın ısıl kapasitesi belirlemez. **N-1 sonrası** bir başka elemanın aşırı yüklenmesi, gerilim veya kararlılık sınırı belirler. Bu yüzden iki 1000 MW'lık hattın TTC'si 2000 MW değildir.

## Türkiye'de iletim yapısı ve kısıt

### Yapı

Kaynak: Elektrik Şebeke Yönetmeliği ve TEİAŞ (Türkiye Elektrik İletim A.Ş.) verisi; `01/02` dosyasında kaynaklı.

- 400 kV omurga
- 154 kV bölgesel iletim
- Az sayıda 66 kV
- Avrupa ile Bulgaristan ve Yunanistan üzerinden senkron bağlantı

### Kısıt nerede oluşur

Aşağıdaki resim genel mühendislik bilgisidir. Güncel sayıları **doğrulamadım**:

- Tüketim Marmara ve batıda yoğundur. Büyük hidroelektrik ve linyit kapasitesinin önemli kısmı doğu ve güneydoğudadır. Sistemin tarihsel ana akış yönü doğudan batıyadır.
- Rüzgâr batı kıyısı ve Trakya'da, güneş İç Anadolu ve güneyde yoğunlaşır. Kaynağın iyi olduğu yerde şebeke zayıf, şebekenin güçlü olduğu yerde yük vardır.
- Güneş santralleri öğlen aynı anda üretir. Bir bölgenin trafo merkezi ve hat kapasitesi, o bölgedeki toplam kurulu güce göre değil **eşzamanlı** üretime göre dolar.

### Doğrulanan kurumsal mekanizma

- 6446 sayılı Kanun'un 23. maddesi gereği TEİAŞ, **bağlanabilir kapasiteyi** bölge bazında yayımlar.
- TEİAŞ "İlgili Raporlar" sayfasında "Bağlanabilir Bölgesel Üretim Tesisi Kapasite Raporu 2024-2028 / 2029-2033" yer alır. Kapasite 15 bölge üzerinden verilir.
- Aynı sayfada "Kısa Devre Akımları (2025)" raporu ve talep tahmin raporları bulunur.

Bölge bazındaki MW değerlerini ezbere söyleme.

> **Mülakatta şöyle söyle:** "TEİAŞ'ın bağlanabilir kapasite raporundan bakarım; rapor beş yıllık iki dönem için bölge bazında değer verir."

### Kısıt nasıl yönetilir

- Gün öncesi piyasası Türkiye'yi **tek fiyat bölgesi** olarak eşleştirir. Şebeke kısıtını görmez.
- Kısıt, gerçek zamana yakın dengeleme güç piyasasında TEİAŞ'ın verdiği yük alma ve yük atma talimatlarıyla çözülür.
- Kısıt nedeniyle verilen talimat ayrı etiketlenir (`11/03` dosyası).
- Yenilenebilir üretimin kısılması ve yeni kapasite tahsisinin durması da kısıtın sonuçlarıdır.

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"Elektrik sözleşmedeki yoldan akar."** | Fizik sözleşmeyi bilmez. A'dan B'ye satılan güç, komşu ülkelerin şebekesinden de geçer (döngü akışı). |
| **"PTDF topolojiden bağımsızdır."** | Bir hat açılınca değişir. LODF bunun için vardır. |
| **"PTDF referans baraya bağlıdır, o yüzden güvenilmez."** | Tek tek değerler referansa bağlıdır. İki bara arasındaki transferin PTDF farkı bağlı değildir. |
| **"NTC hattın MVA değeridir."** | Güvenlik kriterinden sonra kalan değerdir. Yöne, mevsime ve topolojiye göre değişir. |
| **"Kurulu güç fazlaysa kısıt olmaz."** | Kısıt enerji değil yer problemidir. |

## Panel takip sorusu

"LODF paydası sıfıra giderse ne olur?"

> **Mülakatta şöyle söyle:** "Açılan hat, iki bölge arasındaki tek bağlantıdır; açılması sistemi adalara böler. LODF tanımsızdır, vaka ayrıca ele alınır."

"DC katsayılarla bulduğun ihlale güvenir misin?"

> **Mülakatta şöyle söyle:** "Tarama için evet, karar için hayır. Sınıra yakın ve gerilim açısından şüpheli vakaları AC yük akışıyla doğrularım."

Aşağıdaki metin, bu konu sorulduğunda 90 saniyede söyleyeceğin özettir.

## 90 saniye

"DC yaklaşımında şebeke doğrusaldır, bu yüzden duyarlılıkları önceden hesaplarım. PTDF, bir baraya enjekte edilen bir megavatın hangi hattan ne kadar geçtiğini; LODF, açılan bir hattın akışının diğer hatlara nasıl dağıldığını verir. Bunlarla binlerce arıza durumunu yük akışı çözmeden tararım, kritik olanları AC ile doğrularım. Sınır ötesi kapasitede toplam transfer kapasitesinden güvenilirlik payını düşünce net kapasite, tahsis edilmişi düşünce kullanılabilir kapasite kalır. Türkiye'de piyasa tek bölgedir; kısıt dengeleme piyasasında talimatla çözülür ve bağlanabilir kapasite bölge bazında yayımlanır."
