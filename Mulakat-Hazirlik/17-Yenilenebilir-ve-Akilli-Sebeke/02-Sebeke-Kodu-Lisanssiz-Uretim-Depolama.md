# Şebeke kodu, lisanssız üretim, depolama

Bu sayfa üç konuyu anlatır: eviricili santrallerden şebeke kodunun ne istediği, lisanssız üretimin ve mahsuplaşmanın şebekeye etkisi, depolamanın hangi işlerde kullanıldığı.

## Etiketlerin anlamı

Sayfadaki bilgilerin ne kadar güvenilir olduğunu şu etiketler gösterir:

| Etiket | Anlamı |
| --- | --- |
| **Doğrulandı** | Resmî kaynakta Kasım 2026'da okundu |
| **İkincil** | Resmî olmayan kaynak veya genel bilgi |
| **Genel** | Uluslararası tipik uygulama; Türkiye'nin değeri değildir |
| **Doğrula** | Mülakattan önce resmî metne bak |

## Şebeke kodu neden var

Senkron generatör, şebekeye fiziği gereği destek olur:

- **Atalet verir:** dönen kütlesi frekansın ani değişmesine direnir.
- **Arızada büyük akım basar:** koruma röleleri bu akımı görüp arızayı ayırır.
- **Gerilimi uyartımla tutar:** uyartım, rotor sargısına verilen akımdır; bununla gerilim ayarlanır.

Evirici bunların hiçbirini kendiliğinden yapmaz; **ne programlanırsa onu yapar**. Evirici, güneş veya rüzgârın ürettiği elektriği şebekeye uygun alternatif akıma çeviren güç elektroniği cihazıdır.

Şebeke kodu, bu programın asgari içeriğini belirleyen kurallar bütünüdür.

### Tarihsel ders

Evirici tabanlı üretim azken kural "arıza olursa hemen ayrıl" idi.

Pay büyüyünce bu kural tehlikeli oldu. Zincir şöyle işler:

1. Bir iletim arızası gerilimi geniş bir bölgede düşürür.
2. Binlerce megavat aynı anda ayrılır.
3. Arıza bir frekans olayına dönüşür; üretim aniden kaybolduğu için frekans düşer.

Bugünkü kural tersidir: **bağlı kal ve destek ol.**

### Türkiye'deki ve Avrupa'daki kaynak

Türkiye'de kaynak: Elektrik Şebeke Yönetmeliği.

**Doğrulandı:** rüzgâr ve güneş santrallerinin bağlantı koşulları yönetmeliğin **Ek-18**'indedir.

Avrupa'daki karşılığı ENTSO-E'nin (European Network of Transmission System Operators for Electricity, Avrupa İletim Sistemi İşletmecileri Ağı) üreticiler için bağlantı kodu (RfG, Requirements for Generators) ve onun ulusal uygulamalarıdır.

## Dört temel gereksinim

### 1. Arıza boyunca bağlı kalma (FRT, LVRT)

FRT (Fault Ride Through), arıza boyunca bağlı kalmadır. LVRT (Low Voltage Ride Through), düşük gerilimde bağlı kalmadır; FRT'nin gerilim çökmesine ait halidir.

Santral, bağlantı noktasındaki gerilim belirli bir **gerilim–zaman eğrisinin** üstünde kaldığı sürece şebekeden ayrılmamalıdır.

Aşağıdaki çizim eğrinin biçimini gösterir. Arıza anında gerilim düşer, arıza temizlenince basamak basamak toparlanır. Eğrinin üstündeki her noktada santral bağlı kalmak zorundadır.

```
Gerilim
1,0 ┤━━━━━━┓                         ┏━━━━━━━━━━
    │      ┃                    ┏━━━━┛
    │      ┃               ┏━━━━┛         Eğrinin üstü: BAĞLI KAL
    │      ┃          ┏━━━━┛
    │      ┗━━━━━━━━━━┛                   Eğrinin altı: ayrılabilir
0   ┼──────┴──────────┴─────────────────────── zaman
          arıza    arıza temizlendi
```

Üç parçası vardır:

1. **Bağlı kal:** gerilim sıfıra yakın düşse bile birkaç yüz milisaniye.
2. **Arıza sırasında reaktif akım ver:** gerilimi desteklemek ve korumanın arızayı görebilmesi için.
3. **Arıza sonrası aktif gücü hızla geri getir:** frekansı korumak için.

Yüksek gerilimde bağlı kalma (HVRT, High Voltage Ride Through) da aynı mantıkla tanımlanır.

**Doğrula:** Türkiye Ek-18'deki eğrinin köşe noktalarını (gerilim ve süre değerleri) ve istenen reaktif akım katsayısını doğrulamadım. **Mülakatta rakam söyleme.**

> **Mülakatta şöyle söyle:** "Eğrinin biçimini ve mantığını biliyorum; Ek-18'deki sayıları yönetmelikten okurum."

#### Elle örnek: arızada reaktif akım (Genel)

Birçok Avrupa kodunda kural şöyledir: gerilimdeki her %1 düşüş için anma akımının %2'si kadar ek reaktif akım (`k = 2`).

pu (per unit, birim değer), bir büyüklüğün anma değerine oranıdır. 1,0 pu gerilim anma gerilimi, 0,5 pu ise yarısı demektir.

Hesabın adımları:

- **Birinci satır:** gerilimin anma değerinden ne kadar düştüğünü (ΔV) bulur. 1,0 pu'dan 0,5 pu'ya inince düşüş 0,5'tir.
- **İkinci satır:** bu düşüşü `k` katsayısıyla çarparak istenen reaktif akımı bulur. Sonuç anma akımının tamamıdır.

```
Gerilim 0,5 pu'ya düştü   →   ΔV = 0,5
I_reaktif = k × ΔV = 2 × 0,5 = 1,0 pu
```

Sonuç: eviricinin bütün akım kapasitesi reaktif akıma ayrılır; aktif güç geçici olarak sıfıra iner.

Neden? Akım sınırı 1,0–1,2 pu olduğu için ikisini birden veremez (`06/02`).

### 2. Reaktif güç ve gerilim desteği

Reaktif güç (Q), gerilimi ayakta tutan güç bileşenidir. Birimi Mvar'dır (megavolt-amper reaktif). Aktif güç (P) ise işe dönüşen güçtür.

Kontrol kipleri:

| Kip | Davranış | Kullanım |
| --- | --- | --- |
| Sabit güç faktörü | `Q = P × tan φ` | En basit; gerilime tepkisiz |
| Sabit Q | Verilen Mvar | İşletmeci talimatıyla |
| **Volt-var** `Q(V)` | Gerilim düşükse üret, yüksekse tüket; ortada ölü bant | Yerel gerilim desteği |
| Gerilim kontrolü | Bağlantı noktası gerilimini ayar değerinde tut (eğimli) | Büyük santraller, iletim |
| Volt-watt `P(V)` | Gerilim çok yüksekse aktif gücü kıs | Son çare; dağıtımda |

Tablodaki `φ`, gerilim ile akım arasındaki açıdır. Güç faktörü bu açının kosinüsüdür (cos φ).

#### Volt-var eğrisi

Aşağıdaki çizim volt-var kipini gösterir:

- Gerilim düşükse (soldaki bölge) evirici reaktif güç üretir (kapasitif davranış) ve gerilimi yükseltir.
- Gerilim ortadaki ölü bantta ise hiçbir şey yapmaz.
- Gerilim yüksekse (sağdaki bölge) reaktif güç tüketir (endüktif davranış) ve gerilimi düşürür.

```
 Q
 + ┤━━━━━━┓  üret (kapasitif)
   │       ╲
 0 ┤        ━━━━━━━━        ölü bant
   │                ╲
 − ┤                 ┗━━━━━━  tüket (endüktif)
   └──┴────┴────────┴────┴───── V
     0,92  0,98    1,02  1,08          (örnek noktalar; ayar işletmeciye aittir)
```

#### Elle örnek: eviricinin reaktif kapasitesi

Evirici görünür güce göre sınırlıdır: `P² + Q² ≤ S²`.

Görünür güç (S), birimi MVA (megavolt-amper) olan, aktif ve reaktif gücün vektörel toplamıdır. Eviricinin akım sınırı aslında S'yi sınırlar.

Hesabın adımları:

- **Birinci satır:** evirici 0,9 MW aktif güç üretirken S sınırından geriye kalan reaktif payı bulur.
- **İkinci satır:** evirici tam 1,0 MW ürettiğinde reaktif paya hiç yer kalmadığını gösterir.

```
1 MVA evirici, 0,9 MW üretirken:   Q_max = √(1² − 0,9²) = 0,436 Mvar
Aynı evirici, 1,0 MW üretirken:    Q_max = 0
```

Tam güneşte, yani gerilim yükselmesinin en büyük olduğu anda, reaktif kapasite sıfırdır.

Çözüm: eviriciyi büyük seçmek. Anma gücünde 0,95 güç faktörü isteniyorsa:

- **Sol taraf:** 1 MW aktif gücü 0,95 güç faktörüyle verebilmek için gereken görünür gücü (S) bulur.
- **Sağ taraf:** bu S ile 1 MW üretirken elde kalan reaktif gücü (Q) gösterir.

```
S = P / 0,95 = 1,053 MVA     →     Q = 0,329 Mvar
```

Yani %5,3 büyük evirici. Şebeke kodundaki reaktif güç gereksinimi, doğrudan donanım maliyetidir.

### 3. Frekans tepkisi

**Doğrulandı** (şebeke yönetmeliği, `01/02`):

| Büyüklük | Değer |
| --- | --- |
| Normal kontrol bandı | 49,8–50,2 Hz |
| Sınırlı frekans duyarlılık kipinin (LFSM) eşikleri | 49,8 ve 50,2 Hz |
| Tasarım uçları | 47,5 ve 51,5 Hz |

LFSM, Limited Frequency Sensitive Mode, yani sınırlı frekans duyarlı moddur. Hz (hertz) frekans birimidir; Türkiye şebekesinin anma frekansı 50 Hz'dir.

| Kip | Ne zaman | Davranış |
| --- | --- | --- |
| LFSM-O (yüksek frekans) | `f > 50,2 Hz` | Aktif gücü eğimle azalt. Her santral yapabilir |
| LFSM-U (düşük frekans) | `f < 49,8 Hz` | Aktif gücü artır. Yalnız payı (kısılmış üretim, depolama) olan yapabilir |
| FSM (frekans duyarlı kip) | Sürekli | Primer frekans kontrolüne katılım |

LFSM-O'daki O, Over (üstünde); LFSM-U'daki U, Under (altında) demektir. FSM, Frequency Sensitive Mode'dur.

#### Elle örnek: LFSM-O

100 MW üreten güneş santrali, eğim %5 (örnek değer), frekans 50,5 Hz.

Eğim (droop), frekansın yüzde kaç değişmesiyle gücün tamamen değişeceğini söyler. %5 eğim, frekans %5 değişirse güç %100 değişir demektir.

Hesabın adımları:

- **Birinci satır:** frekansın eşiği ne kadar aştığını bulur. Tepki eşikten itibaren başladığı için 50'den değil 50,2'den çıkarılır.
- **İkinci satır:** bu aşımı önce anma frekansına (`f_n` = 50 Hz) bölerek oransal hale getirir, sonra eğime bölüp santral gücüyle çarpar. Sonuç santralin azaltması gereken güçtür.

```
Δf = 50,5 − 50,2 = 0,3 Hz
ΔP = (Δf / f_n) / eğim × P = (0,3 / 50) / 0,05 × 100 = 12 MW azaltır
```

Ayrıca istenenler:

- Frekans aralıklarında bağlı kalma süreleri.
- RoCoF (Rate of Change of Frequency, frekansın değişim hızı) dayanımı.
- Yüklenme hızı (rampa) sınırı.

### 4. İzlenebilirlik ve kontrol edilebilirlik

- **Doğrulandı:** dağıtım sistemine bağlı 10 MW ve üzeri rüzgâr ve güneş santrallerinin MW ve MVAr verisi, dağıtım şirketinin SCADA sistemi üzerinden TEİAŞ SCADA sistemine aktarılır.
- İşletmecinin aktif güç sınırlama talimatını uygulama yeteneği.
- Tahmin verisi sağlama.

Kısaltmalar:

- **SCADA** (Supervisory Control and Data Acquisition): uzaktan izleme, kumanda ve veri toplama sistemi.
- **TEİAŞ:** Türkiye Elektrik İletim A.Ş., iletim sistemi işletmecisi.
- **MVAr:** megavolt-amper reaktif, reaktif güç birimi (Mvar ile aynı).

Bu madde, TEİAŞ'ın güneş tahmin ve "YTBS–sistem kullanıcıları entegrasyonu" projesinin (`01/03`) mevzuat dayanağıdır. YTBS, Yük Tevzi Bilgi Sistemi'dir (MAM'ın enerji yönetim platformu).

10 MW'ın altındaki on binlerce santral ölçülmez; tahmin edilir.

Diğer başlıklar:

- Güç kalitesi (harmonik, kırpışma)
- Koruma ayarları
- Ada çalışmayı önleme
- Model ve benzetim sunma
- Uygunluk testleri

## Lisanssız üretim

Lisanssız üretim, belirli bir gücün altındaki tesislerin, üretim lisansı almadan ve şirket kurmadan, öncelikle kendi tüketimini karşılamak üzere kurulmasıdır.

Çoğunluğu çatı ve arazi tipi güneştir ve **dağıtım şebekesine** bağlanır.

### Güncel mevzuat

**Doğrulandı** (EPDK duyurusu; EPDK, Enerji Piyasası Düzenleme Kurumu'dur):

- Lisanssız Elektrik Üretim Yönetmeliği'nde 2 Nisan 2026 tarihli ve 33212 sayılı Resmî Gazete ile değişiklik yapıldı.
- **1 Mayıs 2026'dan itibaren saatlik mahsuplaşmaya** geçildi. İşlemler EPİAŞ'ın (Enerji Piyasaları İşletme A.Ş.) Lisanssız Üretim Modülü (LÜM) üzerinden yürür.
- **Mesken abonelerinde aylık mahsuplaşma devam ediyor.**
- İlgili Kurul Kararı: 30 Nisan 2026, 14531 sayılı.

**İkincil** (haber ajansı): 2026 için tahsis edilen lisanssız kapasite yaklaşık 3,5 GW (gigavat); bunun 1.500 MW'ı iletim, yaklaşık 2.000 MW'ı dağıtım seviyesinde.

**Çelişkili, doğrula:** lisanssız tesisin kurulu güç üst sınırı için kaynaklarda hem 1 MW hem 5 MW geçiyor. Tesis türüne ve bağlantı anlaşmasındaki sözleşme gücüne göre farklı kurallar var. Mülakatta tek sayı söyleme; yönetmeliğin güncel metnine bak.

**Doğrulandı:** bağlanabilir kapasite, 6446 sayılı Kanun'un 23. maddesi uyarınca TEİAŞ tarafından bölge bazında (15 bölge) yayımlanır.

### Mahsuplaşma neden önemli

Mahsuplaşma, üretim ile tüketimin hangi zaman aralığında birbirinden düşüleceğidir.

#### Elle örnek

Bir işyeri bir günde şöyle üretip tüketiyor. Net sütunu, üretimden tüketimin çıkarılmasıdır: artı ise şebekeye verir, eksi ise şebekeden çeker.

| Saat | Üretim | Tüketim | Net |
| --- | --- | --- | --- |
| Öğlen | 10 kWh | 2 kWh | +8 (şebekeye verir) |
| Akşam | 0 kWh | 8 kWh | −8 (şebekeden çeker) |
| Gün toplamı | 10 | 10 | 0 |

kWh, kilovat-saat, enerji birimidir.

İki mahsuplaşma türü aynı günü farklı hesaplar:

- **Aylık mahsuplaşma:** dönem sonunda net sıfır. Şebeke bedava batarya gibi kullanılmıştır.
- **Saatlik mahsuplaşma:** öğlen verilen 8 kWh ile akşam çekilen 8 kWh ayrı ayrı, kendi saatlerinin koşullarıyla uzlaştırılır. Net sıfır değildir.

Sonuç: saatlik mahsuplaşma, üretimi tüketildiği saate yaklaştırmayı ödüllendirir: öz tüketim, yük kaydırma, depolama.

| Bakış açısı | Etkisi |
| --- | --- |
| Şebeke | Öğlen ters akışı ve akşam puantı azalır |
| Yatırımcı | Geri ödeme süresi uzar |

> **Sade anlatım:** Aylıkta şebeke senin bedava bataryandı; öğlen fazlanı yazıp akşam geri alıyordun. Saatlikte her saat kendi hesabını kapatır, bu yüzden üretimini o saatte kendin kullanman ya da bir bataryada tutman kârlı hale gelir.

### Dağıtım şebekesine etkileri

| Etki | Mekanizma | Ayrıntı |
| --- | --- | --- |
| Gerilim yükselmesi | Ters aktif güç akışı, R baskın hat | `04/02` elle örnek |
| Ters güç akışı | Üretim yerel yükü aşar; trafo ters yüklenir | Kademe değiştirici ve koruma tek yön varsayar |
| Koruma | Körleme, yanlış açma, tekrar kapamada eşzamansızlık, istenmeyen ada | `10/02` |
| Kısa devre | Evirici katkısı küçük ama sıfır değil; çok sayıda eviricide toplanır | `06/02` |
| Dengesizlik | Tek fazlı çatı sistemleri fazlara eşit dağılmaz | `05/03` |
| Kayıp | Az üretim kaybı düşürür; çok üretim (ters akış) artırır | U biçimli eğri |
| Gözlenebilirlik | Sayaç arkasındaki üretim görülmez; yalnız net yük ölçülür | `04/03` |
| Net yük biçimi | Öğlen çukur, akşam dik rampa ("ördek eğrisi") | Esneklik ihtiyacı |
| Tahmin | Yük tahmini artık yük eksi görülmeyen üretimin tahminidir | `18/02` |
| İletim | Toplamda büyük; trafo merkezlerinden iletime ters akış | Bağlanabilir kapasiteyi tüketir |

Tablodaki bazı terimler:

- **R baskın hat:** direnci (R) reaktansına göre büyük olan dağıtım hattı; burada aktif güç akışı gerilimi doğrudan etkiler.
- **Körleme:** üretim kaynağının arıza akımının bir kısmını karşılaması yüzünden rölenin arızayı görememesi.
- **Tekrar kapama:** arızadan sonra kesicinin hattı otomatik olarak yeniden kapatması.
- **Ördek eğrisi:** öğlen çöken, akşam dikleşen net yük eğrisi; biçimi ördeğe benzer.

**Barındırma kapasitesi:** bir fidere, hiçbir sınır (gerilim, ısıl, koruma, güç kalitesi) bozulmadan bağlanabilecek en büyük üretim. Fider, trafo merkezinden çıkan dağıtım hattıdır.

Tek bir sayı değildir; nereye bağlandığına ve evirici ayarlarına bağlıdır.

Artırma yolları, ucuzdan pahalıya:

1. Evirici volt-var
2. Kademe ayarı
3. Yeniden yapılandırma
4. Dinamik ihracat sınırı
5. Depolama
6. İletken ve trafo yenileme

## Depolama kullanım alanları

Depolama tek bir hizmet değil, bir hizmetler demetidir. Hizmetleri zaman ölçeğine göre ayır:

| Zaman ölçeği | Hizmet | Ne gerektirir |
| --- | --- | --- |
| Milisaniye–saniye | Hızlı frekans tepkisi, sanal atalet, şebeke kurma | Güç (MW), hızlı evirici; az enerji |
| Saniye–dakika | Primer ve sekonder frekans kontrolü | Güç; sık ve sığ çevrim |
| Dakika–saat | Yenilenebilir üretimi düzgünleştirme, rampa desteği, dengesizlik azaltma | Güç ve enerji |
| Saat | Enerji arbitrajı, puant tıraşlama, kısıntıyı azaltma | Enerji (MWh) |
| Saat (yerel) | İletim ve dağıtım yatırımını erteleme, kısıt giderme, gerilim desteği | Doğru **yer** |
| Olay bazlı | Sıfırdan enerjilendirme, yedek güç | Şebeke kuran evirici |

İki boyutu ayır:

- **Güç (MW, megavat):** ne kadar hızlı verebildiği.
- **Enerji (MWh, megavat-saat):** ne kadar süre verebildiği.

100 MW / 200 MWh batarya iki saatliktir (200 / 100 = 2 saat).

### Elle örnek: arbitraj

Arbitraj, ucuz saatte alıp pahalı saatte satmaktır.

Veriler: 100 MWh boşaltabilen batarya, gidiş-dönüş verimi %85. Ucuz saatte 1.000, pahalı saatte 3.000 TL/MWh.

Gidiş-dönüş verimi, şarj edilen enerjinin ne kadarının geri alınabildiğidir. %85, 100 birim yüklersen 85 birim geri alırsın demektir.

Hesabın adımları:

- **Birinci satır:** 100 MWh satabilmek için verim kaybı yüzünden daha fazla enerji almak gerektiğini, yani ne kadar alınacağını bulur.
- **İkinci satır:** bu enerjinin ucuz saatteki fiyatla maliyetini bulur.
- **Üçüncü satır:** boşaltılan 100 MWh'nin pahalı saatteki satış gelirini bulur.
- **Dördüncü satır:** gelirden maliyeti çıkararak bir şarj-boşaltma çevriminin brüt kazancını bulur.

```
100 MWh satmak için alınması gereken enerji = 100 / 0,85 = 117,6 MWh
Alış maliyeti = 117,6 × 1.000 = 117.647 TL
Satış geliri  = 100 × 3.000   = 300.000 TL
Çevrim başına brüt kazanç     = 182.353 TL
```

Başa baş koşulu: `satış fiyatı / alış fiyatı > 1 / 0,85 = 1,18`. Bu oran, verim kaybını tam karşılayan fiyat farkıdır.

Fiyat farkı %18'in altındaysa çevrim zarar eder. Buna batarya yıpranma maliyeti eklenir.

### Depolamanın sınırları

- **Enerji üretmez**, kaydırır; ve kayıpla kaydırır.
- Lityum iyon bataryalar tipik olarak 1–4 saatliktir. Günlerce süren rüzgârsız ve güneşsiz dönemi çözmez; orada pompaj depolamalı hidroelektrik, hidrojen veya esnek termik gerekir.
- Bir megavat aynı anda iki hizmete satılamaz. Hizmetleri üst üste koymak (değer yığma) gelir için şarttır ama şarj durumu yönetimi ister.
- Şebeke açısından **yeri** belirleyicidir: kısıtın yanlış tarafındaki batarya kısıtı çözmez.

### Türkiye

- **İkincil:** 2022'nin sonundan itibaren depolamalı rüzgâr ve güneş santrali ön lisans başvuruları alındı ve büyük bir hacim oluştu. Rakamı doğrulamadım.
- **İkincil, doğrula** (bir hukuk bürosu bülteni): Nisan 2026 tarihli Kurul Kararlarıyla (14482–14484) depolamalı tesisler için yeni kapasite tahsisinin durdurulduğu, önceliğin mevcut santrallere eklenen birleşik (hibrit) kapasiteye verildiği belirtiliyor. EPDK'nın kendi metninden okumadım.

### Analiz yazılımı açısından

Depolama zordur, çünkü dönemleri birbirine bağlar: bu saatteki karar, sonraki saatin şarj durumunu belirler.

Tek dönemli optimal güç akışı, çok dönemli bir probleme döner. Optimal güç akışı, şebeke sınırlarını bozmadan maliyeti en aza indiren üretim dağılımını bulan hesaptır.

## Yaygın yanlış

| Yanlış inanış | Doğrusu |
| --- | --- |
| **"Arızada evirici kendini korumak için ayrılmalı."** | Eski kural. Bugün bağlı kalması ve reaktif akım vermesi istenir. |
| **"Evirici istediği kadar reaktif güç verir."** | Görünür güç sınırı içinde; tam üretimde kapasitesi sıfıra iner. |
| **"Güneş santrali frekans düşünce destek olur."** | Zaten elindekinin tamamını üretiyorsa artıramaz. Yalnızca azaltabilir (yüksek frekansta). |
| **"Lisanssız üretim küçüktür, iletimi etkilemez."** | Toplamı gigavatlar mertebesindedir ve öğlen net yükü belirler. |
| **"Mahsuplaşma bir muhasebe ayrıntısıdır."** | Yatırımcının davranışını, dolayısıyla şebekeye ters akışı belirler. |
| **"Depolama yenilenebilirin bütün sorunlarını çözer."** | Saatlik kaydırmayı çözer; mevsimlik dengeyi ve iletim kısıtını (yanlış yerdeyse) çözmez. |
| **"Batarya kapasitesi megavatla söylenir."** | İki sayı gerekir: MW ve MWh. |
| **"Şebeke kodu evrenseldir."** | Her ülkenin eğrileri ve katsayıları farklıdır. Türkiye'ninkini yönetmelikten oku. |

## Panel takip sorusu

### Gerilim yükselen fider

Soru: "Çatı güneşinin yoğun olduğu bir fiderde gerilim yükseliyor. Sırayla ne yaparsın?"

> **Mülakatta şöyle söyle:** Önce ölçümle doğrularım: hangi saat, hangi faz, fiderin neresi. Sonra ucuzdan pahalıya: evirici volt-var ayarı, trafo kademesi, faz dengeleme, yeniden yapılandırma, ihracat sınırı, depolama, en son iletken değişimi. Her adımın yan etkisini (kayıp, kademe aşınması, üretim kaybı) söylerim.

### Görünmeyen küçük santraller

Soru: "10 MW altındaki santralleri göremiyorsan net yükü nasıl tahmin edersin?"

> **Mülakatta şöyle söyle:** Ölçülen temsilî santrallerden ve uydu veya hava modeli ışınımından bölgesel üretimi kestirir, kurulu güç kaydıyla ölçeklerim. MAM'ın SEERC 2025 bildirisi bu konudadır; yöntemin ayrıntısını bildiriden okumam gerekir.

MAM, TÜBİTAK Marmara Araştırma Merkezi'dir. SEERC, bildirinin sunulduğu bölgesel konferanstır (ayrıntısı `01/03`).

### Depolama ve optimal güç akışı

Soru: "Depolamayı optimal güç akışına nasıl eklersin?"

Cevaptaki denklem, bir sonraki dönemin enerjisini (`E_{t+1}`) bu dönemin enerjisinden (`E_t`) hesaplar. Şarjda verim (`η`) kadar az enerji girer, deşarjda verime bölündüğü için daha fazla enerji çıkar. `Δt` dönem uzunluğudur.

> **Mülakatta şöyle söyle:** Her dönem için şarj ve deşarj gücü ile şarj durumu değişkenleri; `E_{t+1} = E_t + η P_şarj Δt − P_deşarj Δt / η`; şarj durumu ve güç sınırları. Aynı anda şarj ve deşarjı önlemek için ikili değişken veya gevşetme.

Aşağıdaki metin mülakatta 90 saniyede söyleyebileceğin özettir. Metindeki "on sekizinci ek", yukarıdaki Ek-18'dir.

## 90 saniye

"Evirici ne programlanırsa onu yapar; şebeke kodu bu programın asgarisini belirler. Dört temel gereksinim var: arızada gerilim–zaman eğrisinin üstünde bağlı kalmak ve reaktif akım vermek, volt-var gibi kiplerle gerilimi desteklemek, yüksek frekansta aktif gücü eğimle azaltmak ve işletmeci tarafından izlenip kontrol edilebilmek. Türkiye'de rüzgâr ve güneş için bu koşullar şebeke yönetmeliğinin on sekizinci ekindedir; eğri sayılarını ezberden söylemem. Lisanssız üretim dağıtıma bağlanır; gerilim yükselmesi, ters akış, koruma ve gözlenebilirlik sorunları getirir. Mayıs 2026'da mesken dışı aboneler için saatlik mahsuplaşmaya geçildi; bu, öz tüketimi ve depolamayı özendirir. Depolamada gücü ve enerjiyi ayırırım; hizmeti zaman ölçeği ve yer belirler."
