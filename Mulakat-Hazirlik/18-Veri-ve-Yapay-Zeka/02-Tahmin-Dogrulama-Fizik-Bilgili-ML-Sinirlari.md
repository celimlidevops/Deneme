# Tahmin doğrulaması ve ML sınırları

Bu sayfanın tam konusu: tahmin doğrulaması, fizik bilgili modeller, güç sistemlerinde makine öğrenmesinin (ML, machine learning) sınırları.

Bu sayfada şunları öğreneceksin:

- yük ve üretim tahmininin ufuklara göre nasıl ayrıldığı,
- zaman serisinde doğrulamanın nasıl yapıldığı ve sızıntının nasıl önlendiği,
- hata ölçütlerinin elle nasıl hesaplandığı,
- fizik bilgisini modele sokmanın altı yolu,
- makine öğrenmesinin güç sisteminde nerede durması gerektiği.

## İki tuzak

Bu konuda iki tuzak var:

1. **Fazla hevesli görünmek:** "her şeyi yapay zekâyla çözerim."
2. **Fazla şüpheci görünmek.**

MAM'ın (TÜBİTAK Marmara Araştırma Merkezi) YTBS (Yük Tevzi Bilgi Sistemi) tanımında "yapay zekâ destekli güvenlik analizi ve tahmin" geçer; grup bu araçları kullanıyor.

> Sade anlatım: Panelin duymak istediği, **nerede işe yaradığını ve nerede yaramadığını** bilen biri.

## Yük ve üretim tahmini

### Ufuklar

Tahmin ufku, ne kadar ileriyi tahmin ettiğindir. Her ufkun kullanıldığı karar ve baskın girdisi farklıdır:

| Ufuk | Kullanım | Baskın girdi |
| --- | --- | --- |
| Çok kısa (dakika–saat) | Gerçek zamanlı dengeleme, AGC, kısıt | Son ölçümler, gökyüzü görüntüsü, uydu |
| Kısa (saat–birkaç gün) | Gün öncesi piyasa, ünite tahsisi, güvenlik analizi | Sayısal hava tahmini, takvim |
| Orta (hafta–ay) | Bakım, yakıt, hidrolik planlama | Mevsim, iklim normalleri |
| Uzun (yıl–on yıl) | Yatırım planlaması | Ekonomi, nüfus, teknoloji benimseme |

AGC (Automatic Generation Control, otomatik üretim kontrolü), frekansı ve bölgeler arası akışı korumak için santral çıkışlarını otomatik ayarlayan kontroldür.

### Neyi tahmin ediyoruz

| Büyüklük | Özelliği |
| --- | --- |
| **Yük** | Güçlü günlük, haftalık ve yıllık örüntü; sıcaklığa doğrusal olmayan bağımlılık (ısıtma ve soğutma); tatiller ve özel günler |
| **Rüzgâr** | Rüzgâr hızının küpüyle gider; güç eğrisi doğrusal değildir; hava tahmininin hatası baskındır |
| **Güneş** | Büyük kısmı belirlenimlidir (güneşin konumu, açık gökyüzü modeli); belirsiz olan buluttur |
| **Net yük** | Yük eksi sayaç arkası üretim. Sistem işletmecisinin asıl gördüğü budur |

"Sayaç arkası üretim", çatı güneşi gibi tüketicinin kendi tarafında olan ve şebekeye görünmeyen üretimdir.

### Olasılıksal tahmin

Tek bir sayı yerine dağılım verilebilir. **Olasılıksal tahmin** yüzdelikler veya aralık verir.

Yedek boyutlandırma ve stokastik eniyileme (`13/02`, bkz. [02-DCOPF-LMP-Gevsetme-Stokastik-Araclar.md](../13-Optimizasyon/02-DCOPF-LMP-Gevsetme-Stokastik-Araclar.md)) bunu ister. Stokastik eniyileme, belirsizliği senaryolarla hesaba katan optimizasyondur.

## Doğrulama yöntemi

Zaman serisinde doğrulama, sıradan makine öğrenmesinden farklıdır. En sık yapılan hatalar buradadır ve hepsi sonucu **olduğundan iyi** gösterir.

### 1. Rastgele bölme yapılmaz

Veriyi karıştırıp %80 eğitim, %20 sınama ayırırsan, model sınama gününün hem dününü hem yarınını görmüş olur.

Zaman serisinde komşu örnekler ilişkilidir; bu bir sızıntıdır. Sızıntı, modelin gerçek kullanımda bilemeyeceği bilgiyi eğitimde görmesidir.

Doğrusu: **zamana göre böl.** Eğitim geçmişte, sınama gelecekte.

### 2. Kayan başlangıçlı doğrulama

Tek bir bölme tek bir mevsimi sınar. Bunun yerine eğitim penceresi her adımda bir ay büyütülür ve bir sonraki ay sınanır. Aşağıdaki şema bu sırayı gösterir:

```
Eğitim: [Oca–Haz]              →  Sınama: Tem
Eğitim: [Oca–Tem]              →  Sınama: Ağu
Eğitim: [Oca–Ağu]              →  Sınama: Eyl
...
```

- Her adımda model yeniden eğitilir ve bir sonraki dönemi tahmin eder.
- Gerçek işletmedeki kullanımın benzetimidir.
- En az bir tam yılı kapsamalıdır; yaz ve kış hataları farklıdır.

### 3. Sızıntı denetimi

Sızıntının beş tipik türü:

| Sızıntı | Örnek |
| --- | --- |
| Gerçekleşen hava verisi kullanmak | İşletmede elinde yalnız hava **tahmini** olur. Gerçekleşen sıcaklıkla eğitilen modelin hatası sahada iki katına çıkar |
| Tahmin anında bilinmeyen girdi | Yarının yükünü tahmin ederken yarının gerçekleşen üretimini kullanmak |
| Ölçekleme sızıntısı | Normalleştirme katsayılarını bütün veriden hesaplamak |
| Hedef sızıntısı | Hedefin gecikmeli hali, gecikme tahmin ufkundan kısaysa |
| Veri düzeltme sızıntısı | Sonradan düzeltilmiş sayaç verisiyle eğitmek; işletmede ham veri gelir |

Kural: her girdi için sor, "tahmini yaptığım anda bu değeri gerçekten biliyor muyum?"

### 4. Kıyas modeli

Bir modelin hatası tek başına anlamsızdır. Karşılaştırılacak basit modeller:

| Kıyas modeli | Varsayımı | Nerede güçlü |
| --- | --- | --- |
| **Kalıcılık** | "Bir sonraki değer şimdiki değerdir." | Çok kısa ufukta yenmesi zordur |
| **Mevsimsel kalıcılık** | "Yarın bu saat, geçen hafta aynı gün aynı saat gibidir." | Yük için güçlü |
| **İklim ortalaması** | O saat ve mevsim için tarihsel ortalama | — |

**Beceri puanı** = `1 − hata_model / hata_kıyas`

- Sıfırsa model kıyastan iyi değil.
- Eksiyse daha kötü.

### 5. Ölçütler

Formüllerde `e` hatadır (tahmin − gerçek), `ort` ortalamadır.

| Ölçüt | Açılımı | Formül | Not |
| --- | --- | --- | --- |
| MAE | Mean Absolute Error, ortalama mutlak hata | `ort(|e|)` | Anlaşılır; MW (megavat) cinsinden |
| RMSE | Root Mean Square Error, karekök ortalama kare hata | `√ort(e²)` | Büyük hataları cezalandırır. Yedek, büyük hataya göre boyutlandığı için sistem işletmecisi için anlamlıdır |
| MAPE | Mean Absolute Percentage Error, ortalama mutlak yüzde hata | `ort(|e| / |gerçek|)` | Gerçek değer sıfıra yaklaşınca patlar. Güneş ve rüzgârda kullanılmaz |
| NMAE | Normalized MAE, normalleştirilmiş ortalama mutlak hata | `MAE / kurulu güç` | Santraller ve bölgeler arası karşılaştırma. Yenilenebilirde standart |
| Yanlılık | — | `ort(e)` | Sistematik fazla veya eksik tahmin |
| Pinball kaybı, CRPS | CRPS: Continuous Ranked Probability Score, sürekli sıralı olasılık puanı | — | Olasılıksal tahmin için |

### NMAE %2 nasıl yorumlanır

MAM'ın güneş tahmin projesi ulusal ölçekte **NMAE %2** bildirir (`01/03`, bkz. [03-Guncel-Projeler-Yayinlar-Urunler.md](../01-Kurum-Ilan-ve-Surec/03-Guncel-Projeler-Yayinlar-Urunler.md)).

Bu sayıyı yorumlarken iki şey sor:

1. Hangi ufuk için?
2. Hangi toplama düzeyinde?

Ulusal toplam hata, tek santral hatasından çok küçüktür. Çünkü santrallerin hataları kısmen bağımsızdır ve toplanınca birbirini götürür. Buna **mekânsal düzgünleşme** denir.

### Elle örnek

Dört saat, kurulu güç 200 MW. Önce her saat için hata bulunur (hata = tahmin − gerçek):

| Saat | Gerçek | Tahmin | Hata |
| --- | --- | --- | --- |
| 1 | 50 | 60 | +10 |
| 2 | 120 | 110 | −10 |
| 3 | 160 | 150 | −10 |
| 4 | 90 | 110 | +20 |

Aşağıdaki blokta her satır bir ölçütü hesaplar. Adımların amacı:

1. **MAE:** hataların işaretini atıp ortalamasını alır; "ortalama kaç MW yanıldım" sorusunu cevaplar.
2. **RMSE:** hataların karesini alıp ortalar, sonra karekök alır; büyük hatayı (20 MW) daha çok cezalandırır.
3. **NMAE:** MAE'yi kurulu güce böler; farklı büyüklükteki santralleri karşılaştırılabilir yapar.
4. **MAPE:** her saatin hatasını o saatin gerçek değerine böler, sonra ortalar; küçük üretimli saatlerin etkisini gösterir.
5. **Yanlılık:** hataları işaretiyle ortalar; model sistematik olarak fazla mı eksik mi tahmin ediyor, onu gösterir.

```
MAE  = (10 + 10 + 10 + 20) / 4 = 12,5 MW
RMSE = √((100 + 100 + 100 + 400) / 4) = √175 = 13,2 MW
NMAE = 12,5 / 200 = %6,25
MAPE = (10/50 + 10/120 + 10/160 + 20/90) / 4 = %14,2
Yanlılık = (10 − 10 − 10 + 20) / 4 = +2,5 MW
```

Sonucun yorumu:

- Aynı tahmin, ölçüte göre %6 veya %14 hatalı.
- MAPE büyük çıktı, çünkü küçük üretimli saat (50 MW) orantısız ağırlık aldı.
- Ölçütü söylemeden "hata şu kadar" denmez.

**Kıyas:** kalıcılık modeli. Her saat için tahmin, bir önceki saatin gerçeğidir; ilk saatten önceki değer 40 MW.

Aşağıdaki blokta adımların amacı:

1. **Kalıcılık tahminleri:** her saate bir önceki saatin gerçek değerini yazar (40, 50, 120, 160); hatalar bu tahminle gerçek arasındaki farktır.
2. **MAE_kalıcılık:** bu hataların ortalamasıdır; basit modelin ne kadar yanıldığını gösterir.
3. **Beceri:** modelimizin MAE'sini kıyas MAE'siyle karşılaştırır; modelin basit yönteme göre ne kadar iyi olduğunu tek sayıda söyler.

```
Kalıcılık tahminleri: 40, 50, 120, 160     hatalar: 10, 70, 40, 70
MAE_kalıcılık = 47,5 MW
Beceri = 1 − 12,5 / 47,5 = 0,74
```

Model, kalıcılığa göre hatayı %74 azaltıyor.

### 6. Hatanın koşullu dökümü

Ortalama hata saklar. Hatayı ayrı ayrı raporla:

- saate göre,
- mevsime göre,
- hava tipine göre (açık, parçalı bulutlu, kapalı),
- rampa olaylarında (üretimin veya yükün kısa sürede hızla değiştiği anlarda),
- tatillerde,
- en büyük %1'lik hatalarda.

Sistem işletmecisini ilgilendiren ortalama gün değil, en kötü gündür.

### 7. Sahada izleme

Model devreye alındıktan sonra bozulur. Nedenleri:

- yeni santraller kurulur,
- tüketim alışkanlığı değişir,
- ölçüm cihazı değişir.

Yapılacaklar:

- Hata sürekli izlenir; eşik aşılınca model yeniden eğitilir.
- Model, verisi ve hata geçmişi sürümlenir.

## Fizik bilgili modeller

Saf veri odaklı model, fiziği veriden yeniden öğrenmek zorundadır. Az veriyle ve görmediği koşulda bunu yapamaz.

Fizik bilgisini modele sokmanın altı yolu, basitten karmaşığa:

| Yol | Nasıl | Örnek |
| --- | --- | --- |
| 1. Fiziksel öznitelik | Ham veri yerine fiziksel anlamı olan girdi | Güneş için açık gökyüzü endeksi; rüzgâr için güç eğrisi çıktısı |
| 2. Artık modelleme (melez) | Fizik modeli tahmin eder; öğrenen model onun **hatasını** öğrenir | Hava modeli + güç eğrisi → sapmayı düzelten model |
| 3. Kayıp işlevinde fizik | Fizik denklemlerini ihlal eden çıktıya ceza | Yük akışı vekil modelinde güç dengesi artığı |
| 4. Katı kısıt ve izdüşüm | Çıktıyı uygun bölgeye geri düşür | Tahmin edilen üretimi sınırlar içine kırp; OPF tahminini uygun noktaya düzelt |
| 5. Yapıda fizik | Modelin mimarisi şebekeyi yansıtır | Şebeke topolojisi üzerinde çizge sinir ağı |
| 6. Öğren, sonra doğrula | Öğrenen model önerir veya eler; fizik çözücü kesin sonucu verir | Arıza taramasında sınıflandırıcı + AC yük akışı |

Tablodaki terimler:

- **OPF** (Optimal Power Flow, optimal güç akışı): şebeke kısıtları altında en ucuz üretim dağılımını bulan hesap.
- **AC yük akışı** (alternatif akım yük akışı): gerilim ve reaktif gücü de içeren tam yük akışı.
- **Vekil model:** pahalı bir hesabın (burada yük akışının) yaklaşık ve hızlı taklidi.
- **Kayıp işlevi:** modelin eğitimde küçültmeye çalıştığı hata ölçüsü.

### Hangi yollar en değerli

Pratikte en çok değer üretenler 1, 2 ve 6'dır. Üçü de aynı ilkeye dayanır:

> Sade anlatım: **Bildiğini öğrenme; bilmediğini öğren.**

**Artık modellemenin üstünlüğü:** öğrenen model başarısız olsa bile (dağılım dışı girdi) fizik modeli makul bir tahmin vermeye devam eder. Buna zarif bozulma denir.

**Altıncı yol** güvenlik analizinde tipiktir:

- Binlerce arıza vakasını bir sınıflandırıcı hızla tarar.
- Şüpheli bulduklarını fizik tabanlı çözücü doğrular.

Sınıflandırıcı yanılırsa iki tür bedel vardır:

| Hata türü | Ne olur | Tehlikesi |
| --- | --- | --- |
| Yanlış alarm | Bir vaka gereksiz yere çözülür | Yalnız hesap zamanı |
| Yanlış güven | Bir vaka kaçırılır | Tehlikelidir |

İkincisi tehlikeli olduğu için eşik buna göre tutucu seçilir.

## Makine öğrenmesinin sınırları

### 1. Dağılım dışı girdi

Öğrenen model, eğitim verisinin kapsadığı bölgede ara değer bulur. Dışına çıkınca çıktısı keyfidir ve **bunu haber vermez**; aynı güvenle yanlış cevap verir.

Güç sisteminde dağılım dışı durumlar tam da önemli olanlardır:

- **Topoloji değişimi.** Bir hat bakıma alındı; eğitim verisinde bu yapılandırma yok.
- **Aşırı hava.** Rekor sıcaklık, fırtına; tanım gereği geçmişte az.
- **Yapısal değişim.** Çatı güneşi beş yılda on katına çıktı; geçmiş yük verisi bugünü temsil etmiyor.
- **Nadir olaylar.** Sistem çökmesi, kademeli arıza.

Önlemler:

- Girdinin eğitim dağılımına uzaklığını ölç ve uzaksa uyar.
- Modelin kararsız kaldığında çekilmesine izin ver.
- Fizik tabanlı yedek yöntem bulundur.
- Topolojiyi girdi olarak ver.

### 2. Nadir olay ve sınıf dengesizliği

Güvenli işletme olağandır; arıza ve kararsızlık nadirdir. Bu yüzden veride "güvenli" sınıfı çok, "güvensiz" sınıfı azdır. Buna sınıf dengesizliği denir.

**Elle örnek.** 1000 arıza vakası; 10'u gerçekten güvensiz.

Terimler:

- **Doğruluk:** bütün vakalardan kaçını doğru bildiğin.
- **Yakalama (duyarlılık):** gerçekten güvensiz olanlardan kaçını yakaladığın.
- **Kesinlik:** "güvensiz" dediklerinden kaçının gerçekten güvensiz olduğu.

**Model A** hepsine "güvenli" diyor. Aşağıdaki hesapta ilk adım doğruluğu bulur (990 güvenli vakayı doğru bildi), ikinci adım yakalamayı bulur (10 güvensiz vakadan hiçbirini yakalamadı):

```
Doğruluk = 990 / 1000 = %99          Yakalama (duyarlılık) = 0 / 10 = %0
```

**Model B**, 10 güvensiz vakanın 9'unu yakalıyor ve 50 yanlış alarm veriyor. Aşağıdaki hesabın adımları:

1. **Doğruluk:** doğru bilinen güvenli vakalar (990 − 50 = 940) ile yakalanan güvensiz vakalar (9) toplanır, bütün vakalara bölünür; modelin genel isabetini verir.
2. **Yakalama:** yakalanan 9 güvensiz vaka, toplam 10 güvensiz vakaya bölünür; kaçırma oranını gösterir.
3. **Kesinlik:** yakalanan 9 vaka, "güvensiz" denen bütün vakalara (9 + 50) bölünür; alarmların ne kadarının gerçek olduğunu gösterir.

```
Doğruluk = (940 + 9) / 1000 = %94,9
Yakalama = 9 / 10 = %90
Kesinlik = 9 / (9 + 50) = %15
```

Yorum:

- B'nin doğruluğu daha düşük, kesinliği kötü; ama işe yarayan odur.
- 59 vaka AC ile doğrulanır; 1000 yerine 59, yani 17 kat az hesap.
- Ama **bir güvensiz vaka kaçtı**. Güvenlik uygulamasında bu kabul edilmez.
- Eşik, yakalama %100'e yaklaşana kadar gevşetilir ve yanlış alarm artışına razı olunur.

Ders:

- Doğruluk yanıltır.
- Yakalama, kesinlik ve hataların maliyeti ayrı raporlanır.
- Yanlış güvenin maliyeti, yanlış alarmın maliyetinden kat kat büyüktür.

Nadir olay verisi çoğunlukla **benzetimle** üretilir. Bu, modelin ancak benzetim kadar doğru olabileceği anlamına gelir.

### 3. Açıklanabilirlik

Operatör, gerekçesini anlamadığı bir öneriyle santral durdurmaz, yük atmaz. Ve haklıdır: sorumluluk ondadır.

- **Yöntemler:** öznitelik önemi, SHAP (SHapley Additive exPlanations, her girdinin sonuca katkısını ölçen yöntem) değerleri, yerel doğrusal açıklamalar, karar ağacı gibi doğası gereği okunur modeller.
- Güç sisteminde en inandırıcı açıklama fizikseldir: "Şu hat açılırsa şu hat %112 yüklenir" cümlesi, yük akışıyla doğrulanabilir.
- Bu yüzden öğrenen modelin çıktısı çoğunlukla **nihai karar** değil, **neye bakılacağını gösteren işaret** olarak tasarlanır.
- Olay sonrası inceleme ve düzenleyici hesap verebilirlik de açıklama ister.

### 4. Güvenlik açısından kritik kararlar

Kararın hızı ve kritikliği arttıkça öğrenen modelin rolü küçülür:

| Karar | Öğrenen modelin rolü |
| --- | --- |
| Koruma açması (milisaniye) | Yok veya çok sınırlı. Belirlenimli, sınanmış, sertifikalı mantık |
| Otomatik kontrol (AGC, SIPS) | Çevrim dışı ayar ve tasarımda yardımcı; çevrim içinde doğrulanmış kural |
| Operatör karar desteği | Öneri, sıralama, erken uyarı. İnsan onaylar |
| Tahmin | Ana kullanım. Hata, yedekle karşılanır |
| Planlama, tarama | Hızlandırıcı. Sonuç fizikle doğrulanır |

SIPS (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması), büyük bir arızadan sonra seçilmiş üretim veya yükü otomatik atarak sistemi koruyan şemadır.

**Yapısal nedenler:**

- **Garanti yok.** Sinir ağının bütün girdiler için sınır içinde kalacağı genel olarak kanıtlanamaz.
- **Hata asimetrisi.** Tahminde %2 hata yedekle karşılanır. Koruma kararında tek hata, ekipman hasarı veya sistem çökmesidir.
- **Geri besleme.** Model çıktısı sistemi değiştirir; sistem modelin eğitildiği dağılımdan uzaklaşır.
- **Saldırı yüzeyi.** Girdi verisi bozularak model yanıltılabilir (`16/02`: sahte veri enjeksiyonu; bkz. [02-SCADA-Protokoller-CIM-TSDB-Ikiz-Siber.md](../16-Yazilim-Mimarisi/02-SCADA-Protokoller-CIM-TSDB-Ikiz-Siber.md)).

**Mühendislik deseni:**

1. Öğrenen model önerir, fizik tabanlı denetim onaylar.
2. Denetimden geçemeyen öneri atılır; yedek yöntem devreye girer.
3. Önce **gölge kipte** çalıştırılır: öneri üretir, uygulanmaz, sonucu mevcut yöntemle karşılaştırılır.
4. Kademeli devreye alma ve geri dönüş planı.
5. Sürekli izleme: girdi dağılımı, hata, yanlış güven oranı.

### 5. Veri gerçekleri

Tecrübenden konuşabileceğin yer burasıdır:

| Gerçek | Ayrıntı |
| --- | --- |
| Ölçüm verisi kirlidir | Donmuş değerler, boşluklar, birim hataları, saat kaymaları, elle girilmiş değerler |
| Etiket azdır | "Güvensiz durum" etiketi benzetimden gelir |
| Veri gizlidir | Gerçek şebeke verisi dışarı çıkmaz; kıyaslama zordur |
| Sistem durağan değildir | Bugünün şebekesi, eğitim verisinin şebekesi değildir |

Model başarımının büyük kısmı algoritmadan değil veri hattından gelir. Veri hattında çalıştıysan köprün burasıdır.

## Yaygın yanlış

| Yanlış cümle | Neden yanlış |
| --- | --- |
| **"Sınama hatam %1; model çok iyi."** | Rastgele bölmeyle mi, gerçekleşen hava verisiyle mi, kıyas modeline göre mi? |
| **"Derin öğrenme her zaman daha iyidir."** | Tablo biçimli tahmin verisinde gradyan artırmalı ağaçlar çoğu zaman eşit veya daha iyidir ve daha az veri ister |
| **"MAPE standarttır."** | Güneş ve rüzgârda sıfıra yakın değerler yüzünden kullanılmaz; NMAE kullanılır |
| **"Model emin değilse düşük olasılık verir."** | Dağılım dışında, yanlışken de emin görünebilir |
| **"Fizik bilgili sinir ağı fiziği garanti eder."** | Kayıp işlevindeki ceza yumuşak kısıttır; ihlali azaltır, sıfırlamaz |
| **"Yapay zekâ yük akışının yerini alır."** | Vekil model yaklaşık ve hızlıdır; taramada kullanılır, kesin sonuç çözücüden gelir |
| **"Daha çok veri her sorunu çözer."** | Nadir olayın verisi yoktur; yapısal değişimden önceki veri yanıltır |
| **"Açıklanabilirlik sonradan eklenen bir özelliktir."** | Operatörün kullanıp kullanmayacağını belirler |

## Panel takip sorusu

### Soru 1

"Güvenlik analizini makine öğrenmesiyle hızlandırmak istiyoruz. Nasıl tasarlarsın?"

> Mülakatta şöyle söyle: Sınıflandırıcıyı eleyici olarak kullanırım, karar verici olarak değil. Girdi: işletme noktası ve topoloji. Çıktı: her arıza için risk puanı. Eşiği, güvensiz vakaları kaçırmayacak kadar tutucu seçerim; eşiği aşanlar AC ile doğrulanır. Eğitim verisini benzetimden, mevcut analiz motoruyla üretirim. Topoloji değişince modelin geçerliliğini denetler, geçerli değilse tam taramaya dönerim. Önce gölge kipte, mevcut sonuçlarla yan yana koşarım.

### Soru 2

"Tahmin modelin geçen hafta iyiydi, bu hafta kötü. Ne yaparsın?"

> Mülakatta şöyle söyle: Önce veriye bakarım: girdi boru hattında değişiklik, donmuş ölçüm, hava tahmini sağlayıcısında değişiklik. Sonra hatanın nerede yoğunlaştığına: saat, bölge, hava tipi. Sonra yapısal değişime: yeni kapasite, tatil, aşırı hava. Modeli yeniden eğitmek son adımdır, ilk değil.

### Soru 3

"Güneş tahmininde NMAE %2 ne demek, iyi mi?"

Hesabın amacı: oranı MW'a çevirip somut büyüklüğü görmek. 23.000 MW × %2 ≈ 460 MW.

> Mülakatta şöyle söyle: Ortalama mutlak hatanın kurulu güce oranı. 23.000 MW için yaklaşık 460 MW ortalama hata. İyi olup olmadığı ufka ve kıyas modeline bağlı; ulusal toplamda mekânsal düzgünleşme hatayı düşürür. Yedek açısından ortalamaya değil en büyük hatalara bakmak gerekir.

## 90 saniye

"Tahminde doğrulamayı zamana göre yaparım: eğitim geçmişte, sınama gelecekte, kayan başlangıçla ve en az bir tam yıl. Sızıntıya dikkat ederim; işletmede elimde gerçekleşen hava değil hava tahmini olur. Hatayı kalıcılık gibi basit bir modele göre ve kurulu güce oranla raporlarım; ortalamanın yanında en kötü günlere bakarım. Fiziği modele katmanın en verimli yolları fiziksel öznitelik, fizik modelinin hatasını öğrenmek ve öğrenen modelin önerisini fizik çözücüyle doğrulamaktır. Makine öğrenmesinin sınırı dağılım dışı durumlardır: topoloji değişimi, aşırı hava, nadir arıza; model burada yanlışken de emin görünür. Bu yüzden güvenlik açısından kritik kararda öğrenen model önerir, fizik tabanlı denetim ve operatör onaylar."
