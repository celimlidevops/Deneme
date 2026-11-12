# Tahmin ve öğrenen modeller

Bu sayfada şunları öğreneceksin: tahminin hangi işletme kararını beslediği, hata ölçütlerinin neden tek başına yetmediği, güvenlik analizinde öğrenen modelin sınırı ve altyapıda neyi anlatman gerektiği.

"Öğrenen model", veriden kalıp çıkaran model demektir (makine öğrenmesi, derin öğrenme). "Fizik motoru" ise yük akışı gibi denklemleri doğrudan çözen hesap yazılımıdır.

## Neden bu konu önemli

Grubun iş tanımındaki madde açıktır: büyük veri, derin öğrenme ve optimizasyon destekli iletim işletme ve planlama araçları.

YTBS (Yük Tevzi Bilgi Sistemi, MAM'ın enerji yönetim platformu; MAM = TÜBİTAK Marmara Araştırma Merkezi) bunu dört yerde kullanır:

- güvenlik,
- yük tahmini,
- yenilenebilir tahmini,
- işletme planı.

TEİAŞ (Türkiye Elektrik İletim A.Ş.) RİTM projesi (rüzgâr üretim izleme ve tahmin projesi) rüzgâr tahminini üç tür modelle kurmayı hedefler: fiziksel, istatistiksel ve hibrit (ikisinin karışımı). Çözünürlük saatliktir, ufuk çok günlüktür.

> Sade anlatım: "Yapay zekâ biliyorum" demek yetmez. Hangi işletme kararını beslediğini söylemen gerekir.

## Tahmin

### Yük tahmini

Yükü belirleyen girdiler:

| Girdi türü | Örnekler |
| --- | --- |
| Takvim | Saat, haftanın günü, tatil, ramazan, sanayi vardiyası |
| Hava | Sıcaklık, nem, rüzgâr |
| Büyük müşteri | Büyük müşterinin üretim planı |

Hangi model nerede güçlü:

- **Doğrusal modeller ve gradyan ağaçlar** (örneğin gradyan boosting; çok sayıda küçük karar ağacının art arda birbirinin hatasını düzelttiği yöntem) saatlik yükte hâlâ güçlü bir bazdır. "Baz", yeni modelin yenmesi gereken basit kıyas modelidir.
- **Derin ağ** (çok katmanlı sinir ağı), çok bölgeli ve hava alanlı (harita biçiminde hava verisi kullanan) problemde işe yarar.

Kural: baz modelini yenmeden derin model anlatma.

### Rüzgâr ve güneş tahmini

Tahmin üç adımda kurulur:

1. Sayısal hava tahmini alınır (hava modelinin rüzgâr hızı, ışınım gibi çıktıları).
2. Güç eğrisiyle güce çevrilir (rüzgâr hızı veya ışınım → MW, megavat).
3. Sahadaki ölçümle düzeltilir.

Santral altı (türbin, invertör) tahmin ile bölge tahmini farklı hatalıdır:

- Bölge hatası daha küçüktür, çünkü santrallerin hataları birbirini iptal eder.
- Yedek, bölge hatasına göre boyutlanır.

Dikkat: kapasite faktörünü tahmin hatası sanma. Kapasite faktörü, santralin ortalamada kurulu gücünün ne kadarını ürettiğidir; tahminin ne kadar yanıldığıyla ilgisi yoktur.

### Ufuklar

Her tahmin ufku farklı bir kararı besler:

| Ufuk | Karar |
| --- | --- |
| Saniye–dakika | Regülasyon, birincil sapma |
| Saat öncesi | Gün içi, dengeleme |
| Gün öncesi | Ünite tahsisi, gün öncesi piyasa |
| Hafta | Bakım, hidro su |
| Yıl | Planlama senaryosu, nokta tahmin değil |

"Ünite tahsisi", hangi santralin hangi saatte devrede olacağına karar vermektir.

### Hata ölçütleri

Kısaltmalar:

- **MAE** (Mean Absolute Error, ortalama mutlak hata)
- **RMSE** (Root Mean Square Error, karekök ortalama kare hata)
- **MAPE** (Mean Absolute Percentage Error, ortalama mutlak yüzde hata)

Yüzde hata (MAPE) iki yerde yanıltır:

- puantta (yükün en yüksek olduğu saatlerde),
- sıfıra yakın güneşte. Güneş gece sıfırken MAPE anlamsızlaşır, çünkü sıfıra bölmeye yaklaşır.

Bu yüzden mutlak MW hatasını da söyle.

Hata bandı (quantile, yüzdelik) tek noktadan değerlidir. Tek nokta tahmin yalnız bir değer söyler; hata bandı ise gerçek değerin büyük olasılıkla düşeceği bir aralık verir. Rezerv, bandın genişliğine göre tutulur.

### Zaman sızıntısı

Zaman sızıntısı, modelin tahmin anında bilemeyeceği bir bilgiyi eğitimde görmesidir. İki tipik hali:

- yarının havasını bugünün modeline "bilgi" diye vermek,
- rastgele bölmeyle geleceği karıştırmak.

Doğru yöntem:

- Test seti son yıl olmalı; karışık satır bölmesi olmamalı.
- Tatil ve fırtına testte ayrı bakılmalı.
- Ortalama hata iyi, en kötü gün kötüyse model işletme aracı olmaz.

Ayrıntılı doğrulama yöntemi için: [02-Tahmin-Dogrulama-Fizik-Bilgili-ML-Sinirlari.md](02-Tahmin-Dogrulama-Fizik-Bilgili-ML-Sinirlari.md).

## Güvenlik ve kararlılık

### Öğrenen model ne yapar

Öğrenen model, binlerce simülasyondan öğrenip "bu arıza büyük ihtimalle kararlı / termik ihlalli" diye eleme yapar. Termik ihlal, hattın ısınma sınırını aşacak kadar yüklenmesidir.

Model seçenekleri:

| Model | Artısı | Eksisi |
| --- | --- | --- |
| Karar ağacı | Eşiği operatöre cümle gibi okunabilir | Daha az doğru olabilir |
| Orman ve gradyan ağaç | Daha doğru olabilir | Okunması zor |
| Sinir ağı | Daha esnek | Gerekçesi daha zor |

Fizik tabanlı özellikler ham SCADA (Supervisory Control and Data Acquisition, uzaktan izleme ve veri toplama sistemi) dökümünden daha iyi geneller. Örnekler:

- açı farkı,
- koridor akışı,
- atalet,
- gerilim marjı.

### Kural: model eler, fizik doğrular

- Öğrenen model eleme ve sıralama yapar.
- İhlal adayı fizik motorunda doğrulanır.
- Kumanda veya yük atma, yalnız öğrenen skorla tetiklenmez.
- SIPS'te (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması) tetik, önceden tanımlanmış ve test edilmiş mantıktır.
- Öğrenen model o mantığın eşiğini önermek için kullanılırsa, değişiklik yine mühendislik onayından geçer.

### Model eskimesi

Eğitim verisi yalnız görülmüş topolojileri (şebekenin hat ve bara bağlantı yapısını) kapsar. Yeni hat girdikten sonra model eskir.

Bunu "concept drift" (kavram kayması, verideki ilişkinin zamanla değişmesi) diye adlandırıp bırakma. Şöyle de:

> Mülakatta şöyle söyle: "Model sürümü, şebeke sürümüne bağlı; büyük topoloji değişiminde yeniden eğitim ve yeniden doğrulama."

### Anomali tespiti ve kötü veri testi

Durum kestirimi, ölçümlerden şebekenin anlık durumunu hesaplayan yöntemdir. İçindeki kötü veri testi, hatalı ölçümü yakalar.

Anomali tespiti bu testin rakibidir, yerine geçeni değildir:

| Yöntem | Neye dayanır | Ne söyler |
| --- | --- | --- |
| Artık testi (kötü veri testi) | Fizik ölçüm fonksiyonuna | Ölçüm fiziğe uymuyor |
| Anomali modeli | Geçmiş veriye | "Bu ölçek alışılmadık"; polarite hatasını kanıtlamaz |

İkisi birlikte, operatöre daha az yanlış alarm vermek için kullanılır.

## Altyapının görünen yüzü

Araştırmacının anlatacağı mimari, platform pazarlaması değildir. Anlatman gerekenler:

- Ölçüm kimliği, zaman damgası, kalite
- Eğitim veri setinin versiyonu
- Özelliklerin şebeke modelinden tekrar üretilebilir olması
- Model dosyasının sürümü ve hangi kodla eğitildiği
- Çevrimiçi süre: tahmin saatlikse saniye yeter; güvenlik elemesi N-1 döngüsüne sığmalı (N-1: herhangi tek bir elemanın kaybında sistemin güvenli kalması ölçütü)
- Başarısızlık: model cevap vermezse fizik motoru veya son sağlam tahmin devreye girer

### Derin öğrenme ne zaman haklı

Derin öğrenme, özelliğin kendisinin öğrenildiği yerde haklıdır. Örnekler: ham hava alanı, çok değişkenli zaman serisi.

On baralık bir fiderde üç yıllık veriyle derin ağ kurmak, ezber ve gürültüdür.

Kural: veri boyu, model kapasitesinden küçükse basit modeli seç.

## 90 saniye

“Tahmini, beslediği kararla anlatırım: gün öncesi ünite tahsisi, saat öncesi dengeleme, saniye mertebesi rezerv. Hata bandı rezervi belirler, MAPE tek başına yetmez. Güvenlikte öğrenen model arızayı eler, fizik doğrular, SIPS eşiği onaysız değişmez. Test seti gelecektedir, karışık satır değildir. Yeni hat, modeli eskidir. Veri azsa derin ağ değil, fizik özellikli basit model kullanırım.”
