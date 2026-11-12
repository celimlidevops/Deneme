# MAM grubu, YTBS, SIPS ve Türkiye şebekesi

Bu sayfa üç şeyi anlatır. Önce başvurduğun grubu tanıtır: MAM'ın (TÜBİTAK Marmara Araştırma Merkezi) Güç Sistemleri Araştırma Grubu. Sonra bu grubun iki ana ürününü açıklar. Son olarak Türkiye elektrik sisteminin kurumlarını, kurallarını ve büyüklüklerini verir.

Güç sistemlerini unuttuysan sorun değil. Her terim ilk geçtiği yerde açılıyor. Önce tek bir kelimeyle başlıyoruz, çünkü sayfanın yarısı ona dayanıyor.

## Sayfa haritası

1. **"Nominal" ne demek?** Sayfadaki bütün sayıları okumak için gereken anahtar kelime ve birkaç birim.
2. **Güç Sistemleri Araştırma Grubu:** grup ne yapar, hangi alanlarda çalışır.
3. **YTBS:** grubun enerji yönetim platformu.
4. **SIPS:** grubun akıllı koruma sistemi ve klasik röleden farkı.
5. **STATCOM:** MAM'ın bir başka ürünü ve seninle ilişkisi.
6. **Türkiye sisteminin kurumları:** TEİAŞ, EPİAŞ, EPDK, dağıtım, üretim.
7. **Şebeke yönetmeliğinden sınırlar:** gerilim, planlama, N-1, frekans, rezervler, PSS.
8. **Büyüklükler:** kurulu güç, puant, tüketim, hat uzunluğu, trafo sayıları.
9. **Enterkonneksiyon:** Türkiye'nin komşu ülkelerle bağlantısı.
10. **Kendi tecrübeni bağlama:** üç dakikalık girişin sırası.
11. **90 saniye:** mülakatta söyleyeceğin kısa metin.
12. **Kendini yokla:** sorular ve cevaplar.

## 1. Önce bir kelime: "nominal"

**Nominal**, bir şeyin etiket değeridir. Tasarım değeri de denir. Ekipman bu değere göre tasarlanır, sistem bu değerle anılır. Ama o anda ölçtüğün değer değildir.

İki örnek:

- Bir hat "400 kV hat" diye anılır. 400 kV onun nominal gerilimidir. O an voltmetreye baktığında 389 kV görebilirsin. Hat yine 400 kV hattır; sadece o anki gerilim 389 kV'dir.
- Türkiye şebekesinin nominal frekansı 50 Hz'dir. O an ölçülen frekans 49,9 Hz olabilir. Şebeke yine "50 Hz şebeke"dir.

Yönetmelik bu yüzden hep iki şey verir: nominal değer ve onun etrafında izin verilen bant. Aşağıda "400 kV: 370–420 kV" gibi satırlar göreceksin. Birincisi etiket, ikincisi gerçek değerin durması gereken aralıktır.

> **Sade anlatım:** Nominal, şişenin üstündeki "1 litre" yazısıdır. İçinde o an ne kadar su olduğu ayrı bir sorudur.

### Birimler, kısa hatırlatma

| Birim | Ne ölçer | Not |
|---|---|---|
| kV (kilovolt) | Gerilim | 1 kV = 1.000 V |
| V (volt) | Gerilim | Evdeki priz alçak gerilimdir |
| Hz (hertz) | Frekans; alternatif akımın saniyede kaç kez yön değiştirme döngüsü yaptığı | Türkiye'de nominal 50 Hz |
| mHz (milihertz) | Frekansın binde biri | **200 mHz = 0,2 Hz.** 200 Hz değil! |
| MW (megavat) | Güç, yani o anki üretim veya tüketim hızı | 1 MW = 1.000 kW |
| MVA (megavoltamper) | Trafo gibi ekipmanın taşıyabileceği görünür güç | Trafo büyüklüğü böyle verilir |
| TWh (terawatt-saat) | Bir süre boyunca tüketilen toplam enerji | Yıllık tüketim böyle verilir |

200 mHz'e özellikle dikkat et. "Mili" binde bir demektir. 200 mHz, frekansın 50,0 Hz'den 49,8 Hz'e düşmesi kadar küçük bir değişimdir.

## 2. Güç Sistemleri Araştırma Grubu

### Grup ne yapar?

MAM'ın kendi sayfasındaki tanım şu alanları sayar: elektrik iletim ve dağıtım sistemleri, yenilenebilir entegrasyon, güç sistemleri güvenliği, optimizasyon, simülasyon ve veri analitiği.

Biraz açalım. **İletim**, elektriği santrallerden şehirlere yüksek gerilimle taşıyan ana şebekedir. **Dağıtım**, bu elektriği daha düşük gerilimle evlere ve işyerlerine ulaştıran yerel şebekedir. **Yenilenebilir entegrasyon**, güneş ve rüzgâr gibi kaynakların şebekeye sorunsuz bağlanmasıdır.

Grupta üç faaliyet biçimi birlikte yürür:

- uygulamalı Ar-Ge,
- ürün,
- danışmanlık.

### İş paketleri

Grubun yazdığı iş paketleri, ilandaki tercih sebeplerinin açık hali gibidir. Yani ilan "şunu bilen tercih edilir" derken aslında bu işleri kastediyor:

- Fayda/maliyet ve risk/etki eksenli yatırım planlaması
- Yenilenebilir enerji ve depolama entegrasyonu
- Şebeke işletimi için karar destek algoritmaları
- Gerçek zamanlı modelleme ve dijital ikiz
- Bilgi sistemi ve yazılım

### Çalışma alanlarının tam listesi

1. İletim ve dağıtım için gelişmiş dinamik ve statik analiz, master plan, enterkonneksiyon analizi
2. Yenilenebilirin şebeke entegrasyonu ve uyumluluk
3. Akıllı şebeke teknolojilerinin tümleştirilmesi
4. Fizibilite ve fayda/maliyet
5. Piyasa ile şebekeyi birlikte ele alan enerji ekonomisi
6. Koruma-koordinasyon ve özel koruma sistemleri
7. Topraklama analizi ve tasarımı
8. Şebeke ekipmanının teknik yeterlilik ve performans değerlendirmesi
9. Gerçek zamanlı modelleme ve benzetim
10. Elektrik şebekesi bilgi sistemleri ve yazılımları
11. Büyük veri, derin öğrenme ve optimizasyon destekli iletim işletme ve planlama araçları

Birkaç terim:

- **Statik analiz:** şebekenin belli bir andaki dengeli halini hesaplar. "Bu yükte hangi hat ne kadar dolu, gerilimler ne?" sorusu.
- **Dinamik analiz:** bir arızadan sonra saniyeler içinde neler olduğunu zaman içinde izler. "Jeneratörler birlikte dönmeye devam ediyor mu?" sorusu.
- **Enterkonneksiyon:** ülkeler arası şebeke bağlantısı. Bölüm 9'da ayrıca anlatılıyor.
- **Benzetim:** simülasyonun Türkçesi.

### Uygulama alanı ve Avrupa bağlantısı

Grubun işi dört kapıdan dışarı çıkar:

- Ar-Ge projesi,
- enerji sektörüne ürün,
- iletim ve dağıtım kuruluşlarına danışmanlık,
- kamu ve özel sektör için karar destek.

Grup, EERA (European Energy Research Alliance, Avrupa Enerji Araştırma İttifakı) Smart Grids ve Hydropower üyesidir. Smart Grids akıllı şebekeler, Hydropower hidroelektrik demektir.

> **Mülakatta şöyle söyle:** Bunu "Avrupa araştırma işbirliğini takip ediyoruz" diye bir cümlede kullan. Üyelik listesini ezberleme.

İletişim ve kurum bilgisi mülakatta adres okumak için değildir.

> **Mülakatta şöyle söyle:** "Gebze'deki genel MAM ile Ankara'daki enerji yazılım grubunu ayırıyorum." Bu kadarı yeter.

## 3. YTBS

### Ne olduğu

YTBS, **Yük Tevzi Bilgi Sistemi**'dir. İngilizce adı Load Dispatch Information System. "Yük tevzi", elektriğin üretim ve tüketim arasında dağıtılıp dengelenmesi demektir.

YTBS bir enerji yönetim platformudur. Şu üç özelliği aklında tut:

- TEİAŞ (Türkiye Elektrik İletim A.Ş., ülkenin iletim şebekesini işleten kurum) tarafından lisanslanmıştır.
- THS 9 seviyesindedir.
- Geliştiren birim bu gruptur.

**THS**, Teknoloji Hazırlık Seviyesi demektir. Bir teknolojinin fikirden gerçek kullanıma ne kadar ilerlediğini 1'den 9'a kadar basamaklarla ölçen bir ölçektir. 1 en erken aşamadır: temel fikir. **9 en üst basamaktır**: ürünün gerçek işletme ortamında çalışarak kanıtlandığı anlamına gelir. Yani "THS 9" demek, "bu ürün laboratuvarda değil, sahada, gerçek kullanımda" iddiasıdır.

### MAM'ın saydığı yetenekler

- Şebekenin yaşayan dijital ikizi: senaryo ve analiz
- Yapay zekâ destekli güvenlik analizi, yük ve yenilenebilir üretim tahmini, işletme planlaması
- En düşük maliyet ve yüksek güvenilirlik için enerji optimizasyonu
- Merkezi veri tabanı; SCADA/EMS ile web servisleri üzerinden veri alışverişi

Son maddedeki kısaltmalar:

- **SCADA** (Supervisory Control and Data Acquisition, Denetleyici Kontrol ve Veri Toplama): sahadaki ölçümleri toplayan ve uzaktan kumanda veren sistem.
- **EMS** (Energy Management System, Enerji Yönetim Sistemi): bu ölçümler üzerinde şebeke hesaplarını yapan yazılım katmanı.

**Güvenlik analizi**, "şu hat veya şu jeneratör aniden devre dışı kalırsa ne olur?" sorusunu önceden hesaplamaktır.

### TEİAŞ duyurularında geçen modüller

TEİAŞ eğitim duyurularında ayrıca adı geçen modüller:

- yük tahmini,
- gerilim planlaması,
- arz güvenilirliği,
- sistem ataleti hesabı,
- geçici hal kararlılığı.

İki terim açıklaması:

- **Atalet:** şebekede dönen büyük jeneratörlerin kütlesi, frekansın ani değişmesine direnç gösterir. Bu dirence atalet denir. Güneş ve rüzgâr arttıkça bu direnç azalabilir; bu yüzden hesaplanır.
- **Geçici hal kararlılığı:** büyük bir arızadan hemen sonraki ilk saniyelerde jeneratörlerin birbiriyle uyumlu dönmeye devam edip etmediği.

### Ölçek hissi

Faz 3 duyurusunda verilen ölçek:

| Büyüklük | Değer | Kaynak |
|---|---|---|
| Enerji yönetim modülü | 30'dan fazla | TEİAŞ YTBS Faz 3 duyurusu |
| Arıza simülasyonu | 4000'den fazla | TEİAŞ YTBS Faz 3 duyurusu |
| Web servis çağrısı | On binlerce | TEİAŞ YTBS Faz 3 duyurusu |
| Kullanım | Çok kullanıcılı, yoğun ziyaret edilen sistem | TEİAŞ YTBS Faz 3 duyurusu |

Rakamı övünmek için değil, "hesap performansının ve veri modelinin işin parçası olduğunu" anlatmak için bil.

### YTBS, SCADA'nın yerine geçmez

YTBS bir SCADA'nın yerine geçtiğini iddia eden bir kutu değildir. İş bölümü şöyle:

- **SCADA** ölçer ve kumanda eder.
- **YTBS** ölçümü modele bağlar, analizi ve kararı üretir, sonucu operatöre ve diğer sistemlere servis eder.

Dijital ikiz burada pazarlama sözü değildir. Aynı şebekenin, ölçümle güncellenen, üzerinde senaryo koşulabilen hesap kopyasıdır.

> **Sade anlatım:** SCADA şebekenin gözü ve elidir. YTBS, gözün gördüğünü bir haritaya işleyip "şimdi ne olur, ne yapmalı" diye düşünen beyindir.

## 4. SIPS

### Ne olduğu

SIPS, **System Integrity Protection Scheme**'in kısaltmasıdır. Türkçe adı **Akıllı Koruma Sistemi**. Kelime kelime "sistem bütünlüğü koruma düzeni" demektir.

Bu da grubun ürünüdür. O da THS 9 ve TEİAŞ lisanslıdır.

### Nasıl çalışır

SIPS, geniş alan ölçümüyle şebekenin anlık bütünlüğünü izler. Bu ölçümlerin başında PMU fazörleri gelir.

- **PMU** (Phasor Measurement Unit, Fazör Ölçüm Birimi): gerilim ve akımı hem büyüklüğü hem açısıyla, çok hassas zaman damgasıyla ölçen cihaz.
- **Fazör:** bu "büyüklük + açı" ölçümünün adı. Farklı yerlerdeki PMU'lar aynı saate bağlı olduğu için şebekenin uzak noktaları aynı anda karşılaştırılabilir.

Büyük bir arızada SIPS, önceden tanımlanmış eylemleri otomatik tetikler. Örnek: jeneratör atma veya yük atma. **Atmak**, bir jeneratörü ya da bir yük grubunu bilerek şebekeden ayırmak demektir.

Amaç zincirleme çökmeyi durdurmaktır. Yani bir arızanın başka arızaları tetikleyip yayılmasını engellemek.

Ürün tanımında ayrıca şunlar da vardır:

- web arayüzü,
- olay kaydı,
- modüler büyüme.

### SIPS ile klasik röle korumasını ayır

- **Röle**, kendi koruma bölgesindeki ekipmanı arızadan korur. Örneğin tek bir hattı veya tek bir trafoyu.
- **SIPS**, sistem bütünlüğünü korumak için geniş alan verisiyle sistem düzeyinde eylem alır.

İkisi aynı "koruma" kelimesinin iki katmanıdır. İlanda hem koruma hem güvenlik hem kararlılık geçtiği için bu ayrım sorulabilir.

> **Sade anlatım:** Röle, tek bir evin sigortasıdır. SIPS, mahallenin tamamı karanlığa gömülmesin diye bazı sokakların elektriğini bilerek kesen merkezdir.

## 5. STATCOM

STATCOM, Static Synchronous Compensator'ın kısaltmasıdır: **statik senkron kompanzatör**. MAM'ın milli STATCOM ürünü, güç elektroniği tabanlı reaktif kompanzasyondur.

**Reaktif güç**, iş yapmayan ama gerilimi ayakta tutmak için gereken güç bileşenidir. **Kompanzasyon**, bu ihtiyacı yerinde karşılamaktır. STATCOM bunu hızlı tepki veren güç elektroniğiyle yapar.

STATCOM için anlatılan konular:

- gerilim regülasyonu,
- geçici ve dinamik kararlılık,
- güç kalitesi.

İlan metni STATCOM tasarımı istemez. Mülakatta "grubun güç elektroniği kartı basan ekip olduğunu" varsayma.

> **Mülakatta şöyle söyle:** "STATCOM gibi hızlı reaktif kaynaklar, gerilim kararlılığı ve dinamik analizde modellenmesi gereken cihazlardır; analiz yazılımı bunları hem statik hem dinamik olarak temsil edebilmelidir."

## 6. Türkiye sisteminin kurumları

| Kurum | Açılımı | Görevi |
|---|---|---|
| **TEİAŞ** | Türkiye Elektrik İletim A.Ş. | İletim sistem işletmecisi. 400, 154 ve 66 kV. Milli Yük Tevzi Merkezi arz-talep dengesini, enterkonneksiyonu ve bölge yük tevzi merkezlerinin koordinasyonunu yürütür. Dengeleme Güç Piyasası'nı işletir. AGC burada çalışır. |
| **EPİAŞ** | Enerji Piyasaları İşletme A.Ş. | Gün öncesi ve gün içi piyasayı işleten piyasa operatörü. Şebeke fiziği ile fiyatı burada birbirine değer. |
| **EPDK** | Enerji Piyasası Düzenleme Kurumu | Lisans, tarife, yönetmelik. Elektrik Şebeke Yönetmeliği bu ilanın "milli kriter" kaynağıdır. |
| **Dağıtım** | — | 21 dağıtım şirketi. CIGRE 2026 Türkiye özetinde tüketici sayısı 2025 sonu için yaklaşık 51,9 milyon. |
| **Üretim** | — | Lisanslı ve lisanssız. Analiz modeli her ikisini de görmek zorundadır; YTBS istatistik sayfası da ikisini birlikte topladığını yazar. |

Tablodaki kısaltmalar:

- **AGC** (Automatic Generation Control, Otomatik Üretim Kontrolü): santrallerin üretimini otomatik olarak artırıp azaltarak frekansı hedefte tutan sistem. Bölüm 7'de rezervlerle birlikte tekrar geçiyor.
- **CIGRE** (Conseil International des Grands Réseaux Électriques, Uluslararası Büyük Elektrik Sistemleri Konseyi): güç sistemleri alanında uluslararası mesleki ve teknik kuruluş.
- **Dengeleme Güç Piyasası:** gerçek zamanda üretim ile tüketim arasındaki farkı kapatmak için santrallere talimat verilen piyasa.
- **Gün öncesi / gün içi piyasa:** elektriğin bir gün önceden ve aynı gün içinde alınıp satıldığı piyasalar.

### MYTM

**MYTM**, Milli Yük Tevzi Merkezi'dir. TEİAŞ'ın şebekeyi gerçek zamanda yöneten merkezidir. Tanımını yönetmelik diliyle bil. MYTM:

- üretimi, iletimi ve tüketimi güvenli, kaliteli ve ekonomik işletir;
- gerçek zamanlı dengeyi sağlar;
- dengeleme piyasasını işletir;
- uluslararası hatları koordine eder.

## 7. Şebeke yönetmeliğinden ezberlenecek sınırlar

Bu bölümün kaynağı Elektrik Şebeke Yönetmeliği'dir. Bölüm 1'deki "nominal" anlatımını burada kullanacaksın.

### Gerilim

Nominal iletim gerilimleri: **400 kV, 154 kV, 66 kV**. Bunlar hatların etiket değerleridir. Gerçek gerilim aşağıdaki bantlarda kalmalıdır.

Yönetmelik iki farklı bant verir:

- **Arıza öncesi planlama gerilimleri:** şebekeyi planlarken, henüz hiçbir arıza yokken hedeflenen dar aralık.
- **Normal işletme:** günlük işletmede izin verilen daha geniş aralık.

| Nominal | Arıza öncesi planlama | Normal işletme | Kaynak |
|---|---|---|---|
| 400 kV | 370–420 kV | 340–420 kV | Elektrik Şebeke Yönetmeliği |
| 154 kV | 146–162 kV; iletim kısıtı olan bölgede planlama kabulü 140–170 kV | 140–170 kV | Elektrik Şebeke Yönetmeliği |
| 66 kV | 62–70 kV | 66 kV ve altı iletim: ±%10 | Elektrik Şebeke Yönetmeliği |

Bölüm 1'deki örneğe dön: 400 kV hattın o an 389 kV olması, hem planlama bandının (370–420 kV) hem normal işletme bandının (340–420 kV) içindedir.

**İletim kısıtı**, bir bölgede hatların taşıyabileceğinden fazla güç aktarılmak istenmesi durumudur.

### Diğer gerilim seviyeleri

| Seviye | Değerler | Kaynak |
|---|---|---|
| İletim sistemi içindeki dağıtım ve iç ihtiyaç seviyeleri | 34,5 kV, 33 kV, 31,5 kV, 15,8 kV, 10,5 kV, 6,3 kV | Elektrik Şebeke Yönetmeliği |
| Alçak gerilim | 400/230 V | Elektrik Şebeke Yönetmeliği |

**İç ihtiyaç**, bir santralin veya trafo merkezinin kendi çalışması için kullandığı elektriktir.

### Planlama yükü ve planlama kriteri

**Puant**, bir dönemdeki en yüksek tüketim anıdır.

**Planlama yükü:** ilgili planlama yılında puantın **%5 üzeri**. Yani şebeke, beklenen en yüksek tüketimin yüzde 5 fazlasını taşıyacak şekilde planlanır.

**Planlama kriteri:** normal koşullarda santraller azami üretimi aktarabilmeli.

**N-1** ve **N-2** şunu anlatır: şebekede N tane eleman (hat, trafo, jeneratör) varsa, N-1 bunlardan birinin devre dışı kaldığı, N-2 ikisinin birden devre dışı kaldığı durumdur. N-1 durumunda şu şartlar sağlanmalıdır:

- gerilim ve frekans limit içinde,
- hatlar termik limitin altında,
- hiçbir kullanıcı kaybedilmemeli,
- kararlılık bozulmamalı,
- sistem adalara bölünmemeli.

Nükleer bağlantı noktasında kriter **N-2**'dir.

Terimler:

- **Termik limit:** hattın aşırı ısınmadan taşıyabileceği en yüksek akım.
- **Adalara bölünmek:** şebekenin birbirinden kopmuş, ayrı ayrı çalışan parçalara ayrılması.

### Frekans

Nominal frekans 50 Hz'dir. Bölüm 1'deki örnekte olduğu gibi, o an 49,9 Hz ölçmek bu bandın içindedir.

**LFSM** (Limited Frequency Sensitive Mode, Sınırlı Frekans Duyarlı Mod): frekans belli bir eşiği aştığında santralin üretimini otomatik olarak değiştirdiği çalışma modu. Düşük modda frekans düşünce, yüksek modda frekans yükselince devreye girer.

| Büyüklük | Değer | Kaynak |
|---|---|---|
| Nominal frekans | 50 Hz | Elektrik Şebeke Yönetmeliği |
| TEİAŞ'ın normal kontrol bandı | **49,8–50,2 Hz** | Elektrik Şebeke Yönetmeliği |
| LFSM düşük mod eşiği | 49,8 Hz | Elektrik Şebeke Yönetmeliği |
| LFSM yüksek mod eşiği | 50,2 Hz | Elektrik Şebeke Yönetmeliği |
| Kararsız işletmede tasarımın gördüğü uçlar | 47,5 Hz ve 51,5 Hz | Elektrik Şebeke Yönetmeliği |

Üretim tesisleri bu uçlarda yönetmelikteki asgari süreler kadar bağlı kalacak şekilde tasarlanır. Yani frekans 47,5 Hz'e ya da 51,5 Hz'e kadar savrulsa bile santral hemen şebekeden kopmamalıdır.

### Rezervler: frekans nasıl geri getirilir?

Tüketim aniden artar veya bir santral düşerse frekans düşer. Bunu toparlamak için üç kademe vardır. Hızlıdan yavaşa:

| Kademe | Ne yapar | Zaman ölçeği | Kaynak |
|---|---|---|---|
| Primer rezerv | 200 mHz'lik basamak frekans değişiminde verilebilecek azami güç değişimi | En geç 30 saniye | Elektrik Şebeke Yönetmeliği |
| Sekonder kontrol | AGC ile frekansı 50 Hz'e ve sınır programını hedefine çeker | Dakikalar mertebesinde | Elektrik Şebeke Yönetmeliği |
| Tersiyer | Dengeleme piyasasında talimat | 15 dakikalık talimat | Elektrik Şebeke Yönetmeliği |

Tekrar hatırlat: **200 mHz = 0,2 Hz**. Yani primer rezerv tanımı, frekansın bir anda 0,2 Hz değişmesi durumunu esas alır.

**Basamak değişim**, kademeli değil, tek seferde ani değişim demektir. **Sınır programı**, ülkeler arası hatlardan planlanan güç alışverişidir.

> **Sade anlatım:** Primer rezerv refleks gibidir; düşünmeden, saniyeler içinde tepki verir. Sekonder kontrol dakikalar içinde frekansı tam hedefe oturtur. Tersiyer ise piyasa üzerinden yeni santral talimatıyla yükü devralır.

### PSS

**PSS** (Power System Stabilizer, Güç Sistemi Dengeleyicisi): jeneratörün uyarma sistemine eklenen, salınımları sönümleyen kontrol devresi.

| Şart | Değer | Kaynak |
|---|---|---|
| PSS aranan üniteler | 75 MW ve üzeri konvansiyonel ünite veya 300 MW ve üzeri konvansiyonel santral üniteleri | Elektrik Şebeke Yönetmeliği |
| Söndürülecek salınımlar | 0–5 Hz elektromekanik salınımlar ve bölgeler arası salınım | Elektrik Şebeke Yönetmeliği |

Terimler:

- **Konvansiyonel:** geleneksel, dönen jeneratörlü santral (termik, hidro gibi).
- **Elektromekanik salınım:** jeneratörlerin dönüş hızının birbirine göre ileri geri sallanması.
- **Söndürmek (sönümlemek):** bu sallanmayı giderek küçültüp yok etmek.

## 8. Büyüklükler (kaynağıyla söyle)

| Büyüklük | Değer | Kaynak |
|---|---|---|
| 2025 sonu kurulu güç | **122.518,6 MW** (artışın büyük kısmı güneş ve rüzgâr) | TEİAŞ 2025 faaliyet raporu |
| 2025 ani puant | **60.414 MW** (Temmuz 2025) | Ayrıca kaynak yazılmamış (2025 verileri bloğunda) |
| 2025 tüketim | Yaklaşık **360,9 TWh** | Raporda geçici değer |
| Eylül 2026 sonu kurulu güç | **127.355,2 MW** | TEİAŞ sayılarla elektrik iletimi |
| Ekim 2026 sonu enerji iletim hattı devre uzunluğu | **77.863 km** | TEİAŞ sayılarla elektrik iletimi |
| 2025 sonu transformatör merkezi ölçeği, 400 kV | 450 transformatör | Ayrıca kaynak yazılmamış |
| 2025 sonu transformatör merkezi ölçeği, 154 kV | 1.756 transformatör | Ayrıca kaynak yazılmamış |
| 2025 sonu transformatör merkezi ölçeği, 66 kV | 18 transformatör | Ayrıca kaynak yazılmamış |
| 2025 sonu toplam kurulu trafo gücü | Yaklaşık 237.700 MVA | Ayrıca kaynak yazılmamış |
| Dağıtım şirketi sayısı | 21 | Bölüm 6 |
| 2025 sonu tüketici sayısı | Yaklaşık 51,9 milyon | CIGRE 2026 Türkiye özeti |

Terimler:

- **Kurulu güç:** bütün santrallerin etiket kapasitelerinin toplamı. Yani hepsi aynı anda tam çalışsa ulaşılacak üretim. Bu da bir tür nominal değerdir.
- **Ani puant:** yıl içinde ölçülen en yüksek anlık tüketim.
- **Devre uzunluğu:** hatların toplam uzunluğu; aynı direk üzerinde iki devre varsa ikisi ayrı sayılır.

### Rakamı yorumla

Kurulu güç puantın iki katına yakındır. Bunun anlamı "sistem bol" değildir. Güneş ve rüzgâr aynı anda puantta değildir; iletim kısıtı, atalet ve gerilim yerel kalır.

> **Sade anlatım:** Kurulu güç etiket değeridir. Güneş gece üretmez, rüzgâr her zaman esmez. Üstelik bir bölgede üretilen elektrik, hat kapasitesi yetmezse başka bölgeye taşınamaz.

> **Mülakatta şöyle söyle:** Bu cümle, rakamı ezberlediğini değil, yorumladığını gösterir.

## 9. Enterkonneksiyon

### Senkron bağlantı

**Senkron** çalışmak, iki şebekenin aynı frekansta, birlikte dönen tek bir sistem gibi çalışması demektir.

Türkiye, Kıta Avrupası senkron bölgesi ile Yunanistan ve Bulgaristan 400 kV hatları üzerinden paralel çalışır. Bu bölge, **ENTSO-E**'nin (European Network of Transmission System Operators for Electricity, Avrupa Elektrik İletim Sistemi İşletmecileri Ağı) senkron bölgesidir.

| Olay | Yıl |
|---|---|
| Deneme paralel işletme başladı | 2010 |
| Kalıcı senkron bağlantı tesis edildi | 2015 |

### Doğu ve kuzeydoğu bağlantıları

Doğu ve kuzeydoğu bağlantıları (Gürcistan, Ermenistan, İran) aynı senkron adanın parçası gibi anlatılmaz.

- **Gürcistan** tarafında back-to-back HVDC vardır.
- **İran ve Ermenistan** hatları ayrı işletme rejimidir.

**HVDC** (High Voltage Direct Current, Yüksek Gerilim Doğru Akım): elektriği alternatif akım yerine doğru akımla aktaran bağlantı. **Back-to-back HVDC**, alternatif akımı doğru akıma çevirip aynı istasyonda hemen tekrar alternatif akıma çeviren düzenektir. Böylece iki taraf frekanslarını birbirinden bağımsız tutarak güç alışverişi yapabilir.

Dikkat: bu sayfa Gürcistan'daki back-to-back HVDC'yi belirli bir hatta bağlamıyor. Mülakatta sen de bağlama.

### Hat çiftleri

Faaliyet raporundaki isimler:

| Hat | Komşu ülke | Gerilim | Kaynak |
|---|---|---|---|
| Hamitabat–Maritsa | Bulgaristan | 400 kV | TEİAŞ faaliyet raporu |
| Babaeski–Nea Santa | Yunanistan | 400 kV | TEİAŞ faaliyet raporu |
| Borçka–Ahıska | Gürcistan | 400 kV | TEİAŞ faaliyet raporu |
| Hopa–Batum | (Gürcistan, Batum) | 220 kV | TEİAŞ faaliyet raporu |
| Kars–Gümrü | (Ermenistan, Gümrü) | 220 kV | TEİAŞ faaliyet raporu |
| Doğubeyazıt–Bazargan | (İran, Bazargan) | 154 kV | TEİAŞ faaliyet raporu |

Parantezli ülke adları, karşı uçtaki şehrin bulunduğu ülkeyi okumana yardım içindir; raporda hat adıyla birlikte geçen ülke yalnızca ilk üç hatta yazılıdır.

Hat adlarını ve gerilimlerini bil. Transfer kapasitesini ezberleme, çünkü mevsimsel ve anlaşmaya bağlıdır.

> **Mülakatta şöyle söyle:** Güncel MW değeri sorulursa "TEİAŞ enterkonneksiyon ve kapasite tahsis verisinden bakarım" de.

### Senkron ile HVDC farkı

Enterkonneksiyon analizi grubun çalışma alanıdır. İki bağlantı türü farklı sorular doğurur:

- **Senkron alan:** frekans, primer rezerv paylaşımı, bölgeler arası salınım ve N-1'de komşu sisteme etki.
- **HVDC bağlantı:** frekansı paylaşmaz, güç ayar noktasıyla kontrol edilir.

**Güç ayar noktası**, bağlantıdan ne kadar güç aktarılacağının operatör tarafından belirlenen değeridir.

> **Sade anlatım:** Senkron bağlantıda iki ülke aynı ipe bağlı iki koşucu gibidir; biri yavaşlarsa diğeri hisseder. HVDC'de aradaki bir vana gibidir; geçen miktar ayarlanır, frekans geçmez.

## 10. Kendi tecrübeni bağlama

Üç dakikalık giriş için şu sıra yeter:

1. Kim olduğun ve 3 yılın hangi şebekede, hangi analizde, hangi yazılımda geçtiği.
2. O işte kullandığın model büyüklüğü: bara sayısı, gerilim, araç (PowerFactory, PSS/E, MATLAB, Python).
3. Çıktının kararı nasıl değiştirdiği: bir hat, bir trafo, bir ayar, bir yatırım.
4. Grubun işine köprü.

**Bara**, şebeke modelindeki bağlantı düğümüdür; hatların, trafoların ve yüklerin birleştiği nokta. Bara sayısı modelin büyüklüğünü anlatır.

Dördüncü adım için iki hazır köprü cümlesi:

> **Mülakatta şöyle söyle:** "Aynı hesabı operatörün her gün kullanacağı servise taşımak istiyorum."
>
> veya: "Planlama çalışmasını tekrarlanabilir bir araca bağlamak istiyorum."

Somut olmayan "güç sistemlerine ilgiliyim" cümlesi bu panelde zayıftır. Model, varsayım, limit ve sonuç söyle.

### 90 saniyelik metin için not

Aşağıdaki metin sayfanın kısa sözlü özetidir. İçindeki kısaltmalar yukarıda açıldı: YTBS (Bölüm 3), SIPS ve PMU (Bölüm 4), SCADA (Bölüm 3), ENTSO-E (Bölüm 9), N-1 (Bölüm 7).

İki noktayı söylemeden önce kontrol et:

- Metin "400 ve 154 kV'de ENTSO-E ile senkron" diyor. Bölüm 9 ise senkron bağlantıyı Yunanistan ve Bulgaristan **400 kV** hatlarıyla anlatıyor. İfadeyi bu farkı bilerek kullan.
- Metindeki "Dağıtım ... 36 kV ve altı" sınırı bu sayfanın başka bir bölümünde geçmiyor. Kullanmadan önce yönetmelikten teyit et.

## 90 saniye

“Grup Ankara’da, TEİAŞ için YTBS ve SIPS’i üretmiş. YTBS dijital ikiz, güvenlik analizi, tahmin, optimizasyon ve SCADA’ya web servis tarafı. SIPS, PMU ile geniş alan izleyip sistem bütünlüğü için otomatik eylem alıyor. Türkiye 400 ve 154 kV’de ENTSO-E ile senkron, normal frekans bandı 49,8–50,2 Hz, planlama kriteri puantın yüzde 5 üzerinde N-1. Dağıtım 21 şirkette, 36 kV ve altı. Benim anlatacağım tecrübe de analiz sonucunu yazılıma ve işletme kararına bağlayan taraf.”

## Kendini yokla

Önce cevabı kapat, kendin söyle, sonra kontrol et.

1. **"Nominal" ne demek? Örnek ver.**
   Etiket, yani tasarım değeri; o an ölçülen değer değil. 400 kV hat o an 389 kV olabilir; 50 Hz şebeke o an 49,9 Hz olabilir.

2. **200 mHz kaç Hz'dir?**
   0,2 Hz. 200 Hz değil.

3. **THS 9 ne anlatır?**
   Teknoloji Hazırlık Seviyesi'nin en üst basamağı; ürünün gerçek işletmede kanıtlandığı iddiası. YTBS ve SIPS THS 9'dur.

4. **YTBS ile SCADA arasındaki fark nedir?**
   SCADA ölçer ve kumanda eder. YTBS ölçümü modele bağlar, analizi ve kararı üretir, sonucu operatöre ve diğer sistemlere servis eder.

5. **SIPS ile klasik röle arasındaki fark nedir?**
   Röle kendi koruma bölgesindeki ekipmanı korur. SIPS geniş alan verisiyle (özellikle PMU fazörleri) sistem bütünlüğü için sistem düzeyinde eylem alır; örneğin jeneratör veya yük atma. Amaç zincirleme çökmeyi durdurmak.

6. **400 kV için arıza öncesi planlama ve normal işletme bantları nedir?**
   Planlama 370–420 kV, normal işletme 340–420 kV.

7. **154 kV için planlama bandı nedir? İletim kısıtı olan bölgede ne değişir?**
   146–162 kV; iletim kısıtı olan bölgede planlama kabulü 140–170 kV.

8. **Planlama yükü nedir?**
   İlgili planlama yılında puantın %5 üzeri.

9. **N-1 durumunda hangi şartlar sağlanmalı? Nükleer bağlantı noktasında kriter nedir?**
   Gerilim ve frekans limit içinde, hatlar termik limitin altında, kullanıcı kaybı yok, kararlılık bozulmuyor, sistem adalara bölünmüyor. Nükleerde N-2.

10. **TEİAŞ'ın normal frekans bandı ve kararsız işletmede tasarımın gördüğü uçlar nedir?**
    Normal bant 49,8–50,2 Hz. Uçlar 47,5 Hz ve 51,5 Hz.

11. **Primer, sekonder ve tersiyer kontrolün zaman ölçekleri nedir?**
    Primer: 200 mHz basamak değişimde en geç 30 saniye. Sekonder: AGC ile dakikalar mertebesinde. Tersiyer: dengeleme piyasasında 15 dakikalık talimat.

12. **PSS hangi ünitelerde aranır?**
    75 MW ve üzeri konvansiyonel ünite veya 300 MW ve üzeri konvansiyonel santral ünitelerinde; 0–5 Hz elektromekanik ve bölgeler arası salınımlar için.

13. **2025 sonu kurulu güç ve 2025 ani puant kaç? Bu iki rakamı nasıl yorumlarsın?**
    122.518,6 MW ve 60.414 MW (Temmuz 2025). Kurulu güç puantın iki katına yakın, ama bu "sistem bol" demek değil: güneş ve rüzgâr aynı anda puantta değil; iletim kısıtı, atalet ve gerilim yerel kalır.

14. **Türkiye ENTSO-E ile ne zaman ve hangi hatlarla senkron oldu?**
    Deneme paralel işletme 2010, kalıcı senkron bağlantı 2015. Yunanistan ve Bulgaristan 400 kV hatları üzerinden: Babaeski–Nea Santa ve Hamitabat–Maritsa.

15. **Senkron bağlantı ile HVDC bağlantı arasındaki fark nedir?**
    Senkron alanda frekans, primer rezerv paylaşımı, bölgeler arası salınım ve N-1'de komşuya etki konuşulur. HVDC frekansı paylaşmaz, güç ayar noktasıyla kontrol edilir.

16. **Transfer kapasitesi sorulursa ne dersin?**
    "TEİAŞ enterkonneksiyon ve kapasite tahsis verisinden bakarım." Çünkü kapasite mevsimsel ve anlaşmaya bağlıdır.

## Bu sayfayı dene

Soruyu gör, cevabını yaz, sonra aç. Bilemediğin soru tekrar gelir.

[Bu sayfanın sorularına geç](test.html?sayfa=01-02)
