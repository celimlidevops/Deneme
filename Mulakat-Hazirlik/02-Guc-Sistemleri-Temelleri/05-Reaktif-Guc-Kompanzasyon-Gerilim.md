# Reaktif güç kontrolü, kompanzasyon, gerilim regülasyonu

## Ana fikir

Frekans ve gerilim farklı şeyleri gösterir:

| Büyüklük | Kapsam | Neyin göstergesi |
| --- | --- | --- |
| Frekans | Bütün sistemde aynı | Aktif güç dengesi |
| Gerilim | **Yerel** | Reaktif güç dengesi |

Bir bölgede reaktif güç eksikse o bölgenin gerilimi düşer. Uzaktaki bir santral bunu düzeltemez, çünkü reaktif güç uzun hatta taşınırken hattın kendi reaktansında tüketilir.

Bu yüzden kural: **reaktif güç, tüketildiği yerde üretilir.**

Kim üretir, kim tüketir:

| Tüketen | Üreten |
| --- | --- |
| Motorlar, trafolar | Senkron generatör (aşırı uyarılı) |
| Ağır yüklü hat (I²X) | Şönt kapasitör |
| Şönt reaktör | Hafif yüklü hat ve kablo (kapasitesi) |
| Düşük uyarılı generatör | STATCOM, SVC, senkron kompanzatör |

Tablodaki kısaltmalar: STATCOM (Static Synchronous Compensator, statik senkron kompanzatör, güç elektroniğiyle reaktif üreten veya çeken cihaz), SVC (Static Var Compensator, tristörle anahtarlanan kapasitör ve reaktör grubu).

Aynı hat, yüke göre iki rol oynar:

- Ağır yükte reaktif tüketir, gerilim düşer.
- Hafif yükte kendi kapasitesi baskın gelir, reaktif üretir, alıcı uç gerilimi yükselir (Ferranti etkisi).

Gece 400 kV hatlarda şönt reaktörün devreye alınmasının nedeni budur.

## Gerilim düşümü formülü

Kısa bir hat için yaklaşık gerilim düşümü aşağıdadır. `P` aktif güç, `Q` reaktif güç, `R` direnç, `X` reaktans, `V` gerilimdir.

```
ΔV ≈ (P R + Q X) / V
```

İletimde `X` dirençten çok büyüktür, bu yüzden gerilimi belirleyen `Q`'dur. Dağıtımda `R` büyüktür, `P` de gerilimi oynatır.

## Elle örnek 1: gerilim düşümü

34,5 kV fider, `R = 2 Ω`, `X = 4 Ω`. Yük 6 MW ve 3 Mvar.

Adım 1, kompanzasyonsuz durum. Bu adım, formüle hem aktif hem reaktif katkıyı koyar ve sonucu nominal gerilime bölerek yüzdeye çevirir.

```
ΔV = (6 × 2 + 3 × 4) / 34,5 = 24 / 34,5 = 0,696 kV   → %2,02
```

Adım 2, yük kendi reaktifini yerinde üretirse (`Q = 0`). Bu adım, reaktif terimi sıfırlayıp yalnızca aktif gücün etkisini bırakır.

```
ΔV = (6 × 2) / 34,5 = 0,348 kV   → %1,01
```

Gerilim düşümü yarıya indi. Kondansatörün işi budur.

## Elle örnek 2: kompanzasyon hesabı

10 MW yük, güç faktörü 0,80 geri. Hedef 0,95.

1. Mevcut reaktif: `Q₀ = 10 × tan(arccos 0,80) = 10 × 0,75 = 7,50 Mvar`. Bu adım, şu anki güç faktörü açısından yükün çektiği reaktifi bulur.
2. Hedef reaktif: `Q₁ = 10 × tan(arccos 0,95) = 10 × 0,3287 = 3,29 Mvar`. Bu adım, hedef güç faktöründe şebekeden çekilmesine izin verilen reaktifi bulur.
3. Gereken kondansatör: `Q_c = 7,50 − 3,29 = 4,21 Mvar`. Bu adım, aradaki farkı kondansatörün yerinde üretmesi gereken miktar olarak alır.
4. Görünür güç 12,5 MVA'dan 10,53 MVA'ya iner. Akım oranı 0,842. Bu adım, aynı gerilimde akımın görünür güçle orantılı düştüğünü gösterir.
5. Kayıp akımın karesiyle gider: `0,842² = 0,709`. **Kayıp %29 azalır.** Bu adım, akım oranının karesini alarak kayıp oranına geçer.

Aktif güç değişmedi. Değişen, hattın taşıdığı gereksiz akımdır.

## Araçlar ve zaman ölçekleri

| Araç | Tepki | Özellik |
| --- | --- | --- |
| Generatör uyarması (AVR) | Milisaniye–saniye | Sürekli, sınırı makinenin ısıl eğrisi |
| STATCOM | Milisaniye | Hem üretir hem tüketir. Gerilim düşse de akımını korur |
| SVC | Onlarca milisaniye | Ürettiği reaktif, gerilimin karesiyle düşer |
| Şönt kapasitör, reaktör | Saniye–dakika | Kademeli, ucuz. Kapasitör tam ihtiyaç anında zayıflar |
| Yük altında kademe değiştirici (OLTC) | Onlarca saniye | Reaktif üretmez, gerilimi bir taraftan diğerine kaydırır |
| Evirici (volt-var) | Milisaniye | Güneş ve depolama, MVA sınırı içinde |

Tablodaki kısaltmalar: AVR (Automatic Voltage Regulator, otomatik gerilim regülatörü), OLTC (On-Load Tap Changer). Volt-var, eviricinin gerilime göre reaktif güç ayarlaması demektir.

İki inceliği bil.

**Kondansatör gerilim düşünce zayıflar.** Ürettiği reaktif `Q = V² / X_c`'dir. Gerilim %10 düşerse üretimi %19 düşer (`0,9² = 0,81`). Yani en çok gerektiği anda en az verir. STATCOM bu yüzden gerilim çökmesinde üstündür. MAM'ın (TÜBİTAK Marmara Araştırma Merkezi) milli STATCOM ürünü bu ailedendir.

**Kademe değiştirici reaktif güç üretmez.** Yük tarafının gerilimini yükseltirken iletim tarafından daha çok reaktif çeker. Reaktif açık varken kademe ile gerilim kurtarmaya çalışmak iletimi daha da zorlar. Uzun dönem gerilim çökmesinin mekanizması budur (`08` klasörü).

## Gerilim kontrol hiyerarşisi

| Katman | Ne yapar | Zaman |
| --- | --- | --- |
| Birincil | Generatör AVR'si ve STATCOM, kendi barasını tutar | Saniyenin altı |
| İkincil | Bir bölgenin pilot barasının gerilimini, o bölgedeki reaktif kaynakları koordine ederek tutar | Dakika |
| Üçüncül | Bütün sistem için gerilim ayar noktalarını kaybı en aza indirecek şekilde seçer. Bu, reaktif optimal güç akışıdır | — |

YTBS'nin (Yük Tevzi Bilgi Sistemi) "gerilim planlaması" modülü üçüncül katmandır.

Generatörün ne kadar reaktif verebileceğini yetenek eğrisi (capability curve) belirler. Eğriyi üç sınır çizer:

1. Armatür akımı.
2. Uyarma akımı.
3. Düşük uyarma kararlılık sınırı.

Aktif güç arttıkça verebileceği reaktif azalır. Yük akışındaki `Qmin` ve `Qmax` bu eğriden gelir.

## Yaygın yanlış

- **"Gerilim düşükse kademeyi yükseltirim, sorun biter."** Kademe reaktif üretmez, sorunu iletime taşır.
- **"Kondansatör ne kadar çoksa o kadar iyi."** Aşırı kompanzasyon hafif yükte gerilimi yükseltir, kapasitif güç faktörü cezası doğurur ve harmoniklerle rezonansa girebilir.
- **"Reaktif güç santralden de gönderilir."** Uzun hatta taşınamaz; hattın reaktansında harcanır ve kayıp yaratır.
- **"Çatı güneşi gerilimi reaktiften yükseltir."** Dağıtımda R büyük olduğu için asıl neden aktif güç enjeksiyonudur. Çözüm de çoğu zaman eviricinin reaktif **tüketmesidir**.
- **"Güç faktörünü 1,00 yapmak hedeftir."** Ekonomik hedef çoğunlukla 0,95–0,98'dir; son yüzde için gereken kondansatör orantısız büyür.

## Panel takip sorusu

"Aynı Mvar'ı kapasitörle mi STATCOM'la mı verirsin?"

> Mülakatta şöyle söyle: "Sürekli hal ve ucuzluk için kapasitör; arıza sonrası toparlanma ve zayıf şebeke için STATCOM. Çoğu merkezde ikisi birlikte kullanılır: taban yükü kapasitör, dinamik payı STATCOM alır."

"Gerilim 1,05 pu'nun üstüne çıkıyor, ne yaparsın?"

> Mülakatta şöyle söyle: "Önce nedenini ayırırım. Hafif yükte hat kapasitesi ise reaktör alırım veya kapasitörü çıkarırım. Dağıtımda ters akış ise evirici volt-var, kademe düşürme, gerekirse aktif güç sınırlama."

Aşağıdaki metin, bu sayfanın tamamını mülakatta 90 saniyede anlatmak içindir.

## 90 saniye

> "Frekans sistemin aktif güç dengesini, gerilim ise bölgenin reaktif güç dengesini gösterir. Reaktif güç uzun hatta taşınamaz, bu yüzden tüketildiği yerde üretilir. Gerilim düşümü yaklaşık PR artı QX bölü V'dir; iletimde Q, dağıtımda P de belirleyicidir. Kompanzasyon aktif gücü değiştirmez, akımı ve kaybı düşürür. Kapasitör ucuzdur ama gerilim düşünce zayıflar; STATCOM hızlıdır ve akımını korur. Kademe değiştirici reaktif üretmez, yalnızca gerilimi kaydırır."
