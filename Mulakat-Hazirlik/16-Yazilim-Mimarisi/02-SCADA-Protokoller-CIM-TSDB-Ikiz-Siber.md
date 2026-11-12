# SCADA, protokoller, CIM, zaman serisi, ikiz, siber güvenlik

Bu sayfa şu konuları sırayla anlatır: SCADA/EMS veri akışı, haberleşme protokolleri, CIM (ortak bilgi modeli), zaman serisi veri tabanı, dijital ikiz ve siber güvenlik.

Bu klasör senin sahana en yakın olanıdır. Kavramların çoğunu başka adlarla zaten biliyorsun. Burada yapılacak iş, bu kavramların enerji sektöründeki adlarını ve kısıtlarını öğrenmek.

## Veri akışı: sahadan operatöre

Bir ölçüm, sahadaki trafodan çıkıp operatör ekranına ve kurumsal sistemlere kadar birkaç katmandan geçer. Aşağıdaki şema bu yolu yukarıdan aşağıya gösterir.

Şemada geçen kısaltmalar (ilk kez burada geçiyorlar):

| Kısaltma | Açılımı | Ne iş yapar |
| --- | --- | --- |
| **SCADA** | Supervisory Control and Data Acquisition, denetleyici kontrol ve veri toplama | Ölçer, gösterir, kumanda eder, alarm verir. Analiz yapmaz |
| **EMS** | Energy Management System, enerji yönetim sistemi | SCADA + iletim analiz uygulamaları |
| **DMS / ADMS** | Distribution Management System / Advanced DMS, dağıtım yönetim sistemi / gelişmiş dağıtım yönetim sistemi | EMS'nin dağıtım karşılığı |
| **RTU** | Remote Terminal Unit, uzak uç birimi | Sahadaki sinyalleri toplar, merkeze taşır |
| **IED** | Intelligent Electronic Device, akıllı elektronik cihaz | Sayısal röle, ölçü cihazı, kontrolör |
| **IEC** | International Electrotechnical Commission, Uluslararası Elektroteknik Komisyonu | Standartları yayımlayan kurum; numaralar onun standartlarıdır |
| **DNP3** | Distributed Network Protocol 3, dağıtık ağ protokolü | Merkez ile kontrol merkezi arası protokol |
| **FEP** | Front-End Processor, ön uç sunucusu | Kontrol merkezinde sahadan gelen haberleşmeyi karşılar |
| **OPF** | Optimal Power Flow, optimal güç akışı | En ucuz üretimi şebeke sınırları içinde bulur |
| **AGC** | Automatic Generation Control, otomatik üretim kontrolü | Frekansı ve alışverişi düzenler |
| **ICCP** | Inter-Control Center Communications Protocol, kontrol merkezleri arası haberleşme protokolü | Kontrol merkezlerini birbirine bağlar |
| **YTBS** | Yük Tevzi Bilgi Sistemi | Grubun enerji yönetim platformu |

"Historian", ölçümleri zaman sırasıyla saklayan arşiv yazılımıdır.

```
Akım ve gerilim trafosu
   ↓  analog / örneklenmiş değer
Koruma rölesi, ölçü cihazı (IED), RTU                    ← trafo merkezi
   ↓  IEC 61850 (merkez içi)
Merkez ağ geçidi
   ↓  IEC 60870-5-104 veya DNP3 (geniş alan ağı)
Kontrol merkezi ön uç sunucusu (FEP)                     ← yük tevzi merkezi
   ↓
SCADA gerçek zamanlı veri tabanı  →  arşiv (historian)
   ↓
EMS uygulamaları:  topoloji işleyici → durum kestirimi → güvenlik analizi → OPF, AGC
   ↓                                                         ↓
Operatör ekranı                                   ICCP ile diğer kontrol merkezleri
   ↓
Kurumsal katman: web servisleri, raporlama, piyasa sistemleri        ← YTBS'nin durduğu yer
```

Şemanın katmanları adım adım:

1. Akım ve gerilim trafosu, yüksek değerleri ölçülebilir seviyeye indirir; çıktısı analog veya örneklenmiş değerdir.
2. Trafo merkezinde koruma rölesi, ölçü cihazı (IED) ve RTU bu değerleri alır.
3. Trafo merkezi içinde haberleşme IEC 61850 ile olur.
4. Merkez ağ geçidi, veriyi geniş alan ağı üzerinden IEC 60870-5-104 veya DNP3 ile yük tevzi merkezine gönderir.
5. Kontrol merkezindeki ön uç sunucusu (FEP) veriyi karşılar.
6. Veri SCADA gerçek zamanlı veri tabanına yazılır ve arşive (historian) aktarılır.
7. EMS uygulamaları sırayla çalışır: topoloji işleyici → durum kestirimi → güvenlik analizi → OPF, AGC.
8. Sonuç operatör ekranına gelir; ICCP ile diğer kontrol merkezlerine de gider.
9. En üstte kurumsal katman vardır: web servisleri, raporlama, piyasa sistemleri. YTBS'nin durduğu yer burasıdır.

### Zaman ölçekleri

Her verinin yenilenme hızı farklıdır. Yazılım tasarımını bu zaman ölçekleri belirler.

| Veri | Yenilenme | Kullanım |
| --- | --- | --- |
| Koruma (GOOSE, örneklenmiş değer) | Milisaniye | Açma, kilitleme |
| PMU | 20–40 ms (saniyede 25–50) | Geniş alan izleme, SIPS |
| SCADA taraması | 2–10 s | Operatör ekranı, durum kestirimi |
| AGC çevrimi | 2–4 s | Frekans ve alışveriş kontrolü |
| Durum kestirimi, güvenlik analizi | 1–5 dakika | Karar destek |
| Sayaç | 15 dakika – 1 saat, gecikmeli | Uzlaştırma, tahmin |

Tablodaki yeni kısaltmalar:

- **GOOSE** (Generic Object Oriented Substation Event, genel nesne yönelimli trafo merkezi olayı): IEC 61850'nin hızlı olay mesajı. Aşağıda ayrıntısı var.
- **PMU** (Phasor Measurement Unit, fazör ölçüm birimi): gerilim ve akımın genliğini ve açısını eşzamanlı zaman damgasıyla ölçen cihaz.
- **SIPS** (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması): geniş alan ölçümüyle sistem düzeyinde koruma eylemi yapan şema.

### YTBS sahayla nasıl konuşur

MAM (TÜBİTAK Marmara Araştırma Merkezi) sayfasındaki YTBS tanımı "SCADA/EMS ile web servisleri üzerinden veri alışverişi" der.

Yani YTBS büyük ihtimalle protokol düzeyinde sahayla konuşmaz. SCADA'nın sağladığı veriyi servis olarak alır. İç mimarisini bilmiyorum.

## Protokoller

Protokol, iki sistemin veriyi hangi kurallarla taşıyacağını belirler. Enerji sektöründe yaygın olanlar:

| Protokol | Nerede | Model | Özellik |
| --- | --- | --- | --- |
| **IEC 61850** | Trafo merkezi içi | Nesne modeli + üç servis | Aşağıda |
| **IEC 60870-5-104** | Merkez ↔ kontrol merkezi | TCP/IP üstünde telekontrol (kapı 2404) | Avrupa ve Türkiye'de yaygın; zaman damgalı, olay tabanlı iletim. `101` seri hat sürümüdür |
| **DNP3** | Merkez ↔ kontrol merkezi | Seri ve TCP (kapı 20000) | Kuzey Amerika'da yaygın; olay tamponu, zaman damgası, güvenli kimlik doğrulama eklentisi |
| **Modbus** | Cihaz düzeyi: evirici, sayaç, PLC | Ana–uydu yoklama; yazmaçlar (kapı 502) | En basit ve en yaygın. Zaman damgası yok, veri modeli yok, güvenlik yok |
| **ICCP / TASE.2** (IEC 60870-6) | Kontrol merkezi ↔ kontrol merkezi | Nesne tabanlı veri alışverişi | TSO–TSO, TSO–DSO, TSO–santral |
| **IEEE C37.118** | PMU ↔ fazör veri toplayıcı | Akış | Eşzamanlı fazör verisi |
| **OPC UA** | Endüstriyel birlikte çalışabilirlik | İstemci-sunucu, yayınla-abone ol | Bilgi modeli ve yerleşik güvenlik |

Tablodaki kısaltmalar:

- **TCP/IP** (Transmission Control Protocol / Internet Protocol): internetin temel taşıma protokolleri. "Kapı" (port), bir sunucuda servisin dinlediği numaradır.
- **PLC** (Programmable Logic Controller, programlanabilir mantık denetleyicisi): endüstriyel kontrol cihazı.
- **TASE.2** (Telecontrol Application Service Element 2): ICCP'nin standart adı.
- **TSO** (Transmission System Operator, iletim sistemi işletmecisi) ve **DSO** (Distribution System Operator, dağıtım sistemi işletmecisi).
- **IEEE** (Institute of Electrical and Electronics Engineers, Elektrik ve Elektronik Mühendisleri Enstitüsü): C37.118 onun standardıdır.
- **OPC UA** (Open Platform Communications Unified Architecture, açık platform haberleşmesi birleşik mimarisi): endüstriyel birlikte çalışabilirlik standardı.

Tablodaki diğer terimler:

- **Telekontrol:** uzaktan izleme ve kumanda.
- **Ana–uydu yoklama:** ana cihaz sırayla sorar, uydu cihaz cevap verir.
- **Yazmaç:** cihazın numaralı veri hücresi.
- **Yayınla-abone ol:** gönderen veriyi yayınlar, isteyen abone olup alır.

### IEC 61850 biraz daha ayrıntılı

Diğer protokoller "veri nasıl taşınır" sorusuna cevap verir. IEC 61850 önce "veri **nedir**" sorusuna cevap verir: cihazdan bağımsız, standart adlı bir nesne modeli sunar.

**Mantıksal düğüm**, bir işlevin standart adıdır. Örnekler:

| Ad | Anlamı |
| --- | --- |
| `XCBR` | Kesici |
| `MMXU` | Ölçüm |
| `PTOC` | Zamanlı aşırı akım koruması |
| `PDIS` | Mesafe koruması |

Adresleme hiyerarşiktir: `MerkezA/Fider3/XCBR1.Pos.stVal` → kesicinin konumu. Bu adres, merkezden fidere, fiderden kesiciye, kesiciden konum verisine iner.

Yazılımcı için fark şudur: Modbus "40001 numaralı yazmaç" der ve anlamını bir Excel tablosundan öğrenirsin. IEC 61850 ise tip tanımlı, kendini tarif eden bir şema sunar.

> **Sade anlatım:** Modbus sana numaralı kutular verir, hangi kutuda ne olduğunu ayrı bir listeden bulursun. IEC 61850 kutunun üstüne ne olduğunu yazar.

#### Üç haberleşme servisi

| Servis | Taşıma | Süre | Kullanım |
| --- | --- | --- | --- |
| MMS | TCP/IP, istemci-sunucu | Yüzlerce ms | İzleme, kumanda, raporlama |
| GOOSE | Doğrudan Ethernet, çoklu yayın, yayınla-abone ol | < 4 ms | Açma, kilitleme; bakır kablonun yerini alır |
| Örneklenmiş değerler (SV) | Doğrudan Ethernet | Periyot başına 80 örnek (50 Hz'te saniyede 4000) | Akım ve gerilim dalga biçimi; proses barası |

- **MMS** (Manufacturing Message Specification, üretim mesaj belirtimi): istemci-sunucu tarzı mesajlaşma.
- **SV** (Sampled Values, örneklenmiş değerler): ham dalga biçimi örnekleri. 50 Hz'te bir periyot 20 ms'dir; periyot başına 80 örnek, saniyede 50 × 80 = 4000 örnek eder.
- **Çoklu yayın:** bir mesajın aynı anda birçok alıcıya gitmesi.
- **Proses barası:** sahadaki ölçü trafosu ile röle arasındaki sayısal ağ.

#### Yapılandırma dili

Yapılandırma dili SCL (Substation Configuration Language, trafo merkezi yapılandırma dili), XML (Extensible Markup Language, genişletilebilir işaretleme dili) tabanlıdır. Üç ayrı dosya türü vardır:

- cihaz yeteneği
- merkez tasarımı
- cihaza yüklenen ayar

## CIM: ortak bilgi modeli

Her yazılım şebekeyi kendi biçiminde tutarsa, `n` sistem arasında `n²` dönüştürücü gerekir. CIM (Common Information Model, ortak bilgi modeli), şebeke için ortak bir sınıf modelidir. Herkes ortak modele çevirince dönüştürücü sayısı azalır.

| Standart | Kapsam |
| --- | --- |
| IEC 61970 | İletim, EMS: şebeke elemanları, topoloji, ölçüm |
| IEC 61968 | Dağıtım: varlık, iş emri, sayaç, müşteri |
| IEC 62325 | Piyasa |
| **CGMES** | ENTSO-E'nin CIM profili; iletim işletmecileri arası model değişimi |

- **CGMES** (Common Grid Model Exchange Standard, ortak şebeke modeli değişim standardı).
- **ENTSO-E** (European Network of Transmission System Operators for Electricity, Avrupa elektrik iletim sistemi işletmecileri ağı).

Model UML (Unified Modeling Language, birleşik modelleme dili) ile tanımlanır. RDF/XML (Resource Description Framework, kaynak tanımlama çerçevesi; XML biçiminde) olarak serileştirilir. Her nesnenin kalıcı bir kimliği vardır: mRID (master resource identifier, ana kaynak kimliği).

### Çekirdek kavram: çizge

Yazılımcı için CIM'in çekirdeği bir **çizgedir**. Aşağıdaki satır üç kavramın nasıl bağlandığını gösterir: iletken eleman bir uca, uç bir bağlantı düğümüne bağlanır.

```
İletken eleman (hat, trafo, kesici)  ──  Uç (Terminal)  ──  Bağlantı düğümü (ConnectivityNode)
```

### İki model düzeyi ve topoloji işleme

İki model düzeyi vardır. Aralarındaki dönüşümün adı **topoloji işleme**dir.

| Model | Ne içerir | Kim kullanır |
| --- | --- | --- |
| **Düğüm-kesici modeli** | Her kesici ve ayırıcı ayrı ayrı vardır | SCADA ve işletme |
| **Bara-dal modeli** | Kapalı anahtarlarla birbirine bağlı düğümler tek bir baraya indirgenir | Yük akışı |

Topoloji işleyici, anahtar konumlarına bakıp bağlı bileşenleri bulan bir çizge algoritmasıdır. Kullanılan yöntemler birleştir-bul veya genişlik öncelikli aramadır.

Bir kesici konumu yanlış gelirse bara sayısı değişir ve durum kestirimi bozulur.

### CGMES profilleri

CGMES modeli profillere bölünür:

| Profil | İçerik | Değişme sıklığı |
| --- | --- | --- |
| EQ | Ekipman: ne var, nasıl bağlı | Nadiren |
| SSH | Sürekli hal varsayımı: yük, üretim, anahtar ve kademe konumu | Her senaryo |
| TP | Topoloji: hesaplanan baralar | Her senaryo |
| SV | Durum değişkenleri: yük akışı sonucu | Her çözüm |
| DL, GL | Şema yerleşimi, coğrafi konum | Nadiren |
| DY | Dinamik modeller | Nadiren |

Profil adlarının açılımı: EQ (Equipment), SSH (Steady State Hypothesis), TP (Topology), SV (State Variables), DL (Diagram Layout), GL (Geographical Location), DY (Dynamics).

Bu ayrım iyi bir tasarım örneğidir: yavaş değişen yapı ile hızlı değişen durum ayrı tutulur.

### Gerçekte zor olan

- Üreticilerin CIM yorumları farklıdır.
- Uzantılar yaygındır.
- Dosyalar büyüktür.
- Modelin doğrulanması (referans bütünlüğü, eksik parametre) işin çoğunu oluşturur.

## Zaman serisi veri tabanı

Ölçüm verisinin özellikleri:

- yazma ağırlıklı
- zaman sıralı
- nadiren güncellenen
- zaman aralığıyla sorgulanan

İlişkisel satır deposu bu tür veri için verimsizdir.

| Araç | Not |
| --- | --- |
| PI System (AVEVA) | Enerji sektöründe fiilî standart arşiv |
| TimescaleDB | PostgreSQL uzantısı; SQL ve ilişkisel veriyle birleştirme |
| InfluxDB | Açık kaynak, etiket tabanlı |
| ClickHouse, Parquet dosyaları | Analitik ve toplu işleme |

SQL (Structured Query Language), ilişkisel veri tabanının sorgu dilidir.

### Kavramlar

- **Etiket (tag) + zaman damgası + değer + kalite.** Bir ölçüm kaydı bu dört parçadan oluşur. Kalite bayrağı (iyi, şüpheli, eski, elle girilmiş) verinin parçasıdır. Kalite bayrağını atan analiz, donmuş bir ölçümü taze sanar.
- **Sıkıştırma:** ölü bant ve salınan kapı gibi kayıplı yöntemler değişmeyen değeri yazmaz. Ölü bant, belli bir eşikten küçük değişimi yok sayar. Bir de sütun bazlı kayıpsız sıkıştırma vardır.
- **Alt örnekleme ve saklama:** ham veri kısa süre, dakikalık ve saatlik özetler uzun süre tutulur.
- **Geç gelen ve sırasız veri:** haberleşme kesilir, cihaz tamponunu sonradan boşaltır.
- **Zaman:** her şey UTC (Coordinated Universal Time, eşgüdümlü evrensel zaman) olarak saklanır. Olay zamanı (cihaz saati) ile alım zamanı (sunucu saati) ayrı tutulur. Yaz saati ve artık saniye hataları klasiktir.

### Elle örnek: boyutlandırma

Senaryo: 20.000 ölçüm noktası, 2 saniyede bir tarama.

Hesabın adımları ve ne işe yaradıkları:

1. **Saniyede örnek:** nokta sayısını tarama süresine bölerek veri tabanına saniyede kaç yazma geleceğini buluruz.
2. **Günde örnek:** saniyelik sayıyı bir gündeki 86.400 saniyeyle çarparak günlük satır sayısını buluruz.
3. **Ham boyut:** günlük örnek sayısını örnek başına 16 baytla çarparak sıkıştırmasız disk ihtiyacını buluruz; yıla çevirince uzun dönem depolama ölçeği çıkar.
4. **Sıkıştırma:** 10 kat sıkıştırma varsayımıyla gerçekçi günlük disk ihtiyacını buluruz.

```
Saniyede örnek = 20.000 / 2 = 10.000
Günde örnek    = 10.000 × 86.400 = 864 milyon
Ham boyut      = 864 milyon × 16 bayt ≈ 13,8 GB/gün  ≈ 5 TB/yıl
10 kat sıkıştırmayla ≈ 1,4 GB/gün
```

**PMU eklenirse:** 100 PMU × 20 kanal × saniyede 50 örnek = saniyede 100.000 örnek. Bu, SCADA'nın saniyedeki 10.000 örneğinin on katıdır. Bu adım, PMU'nun yazma yükünü SCADA ile karşılaştırmaya yarar. Bu ölçekte yazma hızı ve sıkıştırma bir tasarım kararına dönüşür.

MAM'ın TEKİS-C projesi 20.678 yüksek gerilim ölçüm noktasından söz eder (`01/03`). Bu örnek o mertebededir.

## Dijital ikiz

Üç düzeyi birbirinden ayır:

| Düzey | Veri akışı |
| --- | --- |
| Dijital model | Elle güncellenen çevrim dışı model. Planlama çalışması |
| Dijital gölge | Gerçek sistemden modele otomatik akış. Durum kestirimiyle güncellenen model |
| Dijital ikiz | İki yönlü: model kararı gerçek sisteme geri gider (operatör aracılığıyla veya otomatik) |

> **Sade anlatım:** Model, elle çizilmiş bir harita. Gölge, kendiliğinden güncellenen bir harita. İkiz, haritaya bakıp yolu da değiştirebildiğin sistem.

### Şebeke dijital ikizinin katmanları

1. **Yapısal model:** CIM; ekipman, parametre, bağlantı.
2. **Canlı durum:** SCADA ve PMU ölçümü → topoloji işleyici → durum kestirimi.
3. **Hesap motoru:** yük akışı, kısa devre, güvenlik, kararlılık.
4. **Senaryo:** "şu hat açılırsa", "yarın rüzgâr şöyle olursa". Canlı durumdan dallanan kopyalar.
5. **Doğrulama döngüsü:** model tahmini ile ölçüm karşılaştırılır; fark, parametre veya topoloji hatasını gösterir.

### Yazılım açısından zor olanlar

- Modelin sürümlenmesi: dün neydi, yarın ne olacak.
- Senaryoların yalıtılması: operatörün "ne olursa" denemesi canlı durumu bozmamalı.
- Hesapların tutarlı bir anlık görüntü üzerinde koşması.
- Sonucun hangi model ve veri sürümüyle üretildiğinin izlenebilmesi.

MAM sayfası YTBS'yi "şebekenin yaşayan dijital ikizi" diye tanımlar.

## Siber güvenlik temelleri

### Bilişim ile işletme teknolojisi farkı

IT (Information Technology, kurumsal bilişim) ofis ve iş sistemleridir. OT (Operational Technology, işletme teknolojisi) fiziksel süreci izleyen ve kumanda eden sistemlerdir.

| | Kurumsal bilişim (IT) | İşletme teknolojisi (OT) |
| --- | --- | --- |
| Öncelik | Gizlilik, bütünlük, erişilebilirlik | **Erişilebilirlik** ve güvenlik (can, ekipman), bütünlük, gizlilik |
| Yama | Haftalık | Planlı duruşta; yıllar sürebilir |
| Ömür | 3–5 yıl | 15–30 yıl |
| Gecikme toleransı | Saniyeler | Milisaniyeler |
| Hata sonucu | Veri kaybı | Fiziksel hasar, kesinti |

Sonuç: "şüpheli durumda sistemi kapat" refleksi OT'de yanlıştır. Antivirüs taraması bir koruma rölesini geciktiremez.

### Yapı

- **Bölgeler ve kanallar** (IEC 62443): ağ, güvenlik düzeyine göre bölgelere ayrılır. Bölgeler arası her akış tanımlı bir kanaldan geçer.
- **Katmanlı model** (Purdue): saha cihazları → kontrol → merkez gözetim → işletme → **arındırılmış bölge (DMZ)** → kurumsal ağ → internet. DMZ (Demilitarized Zone), iki ağ arasında tampon görevi gören ara bölgedir. Kurumsal ağdan kontrol ağına doğrudan bağlantı olmaz.
- **Tek yönlü geçit (veri diyotu):** veri kontrol ağından dışarı akar, içeri fiziksel olarak akamaz.
- **IEC 62351:** güç sistemi protokollerinin güvenliği. İçerdikleri: TLS (Transport Layer Security, aktarım katmanı güvenliği), kimlik doğrulama, GOOSE imzalama, rol tabanlı erişim.

Protokollerin çoğu güvenlik düşünülmeden tasarlandı. Modbus ve klasik IEC 104 kimlik doğrulamaz: ağa erişen, komut gönderir.

### Bilinen olaylar

2015 ve 2016'da Ukrayna'da dağıtım ve iletim saldırıları oldu. İkincisinde kullanılan zararlı yazılım, IEC 104 ve IEC 61850 ile doğrudan konuşup kesici açtı.

Ders: saldırgan, protokolü ve prosesi bilen biridir.

### Türkiye

EPDK'nın (Enerji Piyasası Düzenleme Kurumu) enerji sektöründeki endüstriyel kontrol sistemleri için bir bilişim güvenliği yönetmeliği vardır (2017). Güncel adını ve kapsamını **doğrulamadım**.

> **Mülakatta şöyle söyle:** Ad verme. "EPDK'nın bu alandaki düzenlemesi" de.

Sayaç verisi kişisel veridir; KVKK (Kişisel Verilerin Korunması Kanunu) kapsamına girer.

### Analiz yazılımına özgü tehdit: sahte veri enjeksiyonu

Durum kestirimi kötü veriyi artıklardan yakalar (`09/02`). Artık, ölçüm ile kestirimin ölçüme karşılık gelen değeri arasındaki farktır.

Şebeke modelini bilen saldırgan, ölçümleri **modelle tutarlı** biçimde değiştirirse artıklar değişmez.

Saldırı vektörü `a = H c` biçimindeyse kestirim `c` kadar kayar, artık aynı kalır. Burada `H` ölçüm matrisi (durumu ölçüme bağlayan katsayılar), `c` saldırganın durumda yaratmak istediği kayma, `a` ölçümlere eklenen saldırı vektörüdür.

> **Sade anlatım:** Kötü veri testi "ölçümler birbiriyle tutarlı mı" diye bakar. Saldırgan bütün ölçümleri aynı yalanla tutarlı biçimde değiştirirse test bir şey görmez.

**Elle örnek.** `09/02`'deki iki ölçüm: `z = [1,02  0,98]`, `H = [−10  −10]`. Saldırgan durumu `c = 0,01 rad` kaydırmak istiyor: `a = H c = [−0,1  −0,1]`.

Adımların ne işe yaradığı:

1. **Saldırı vektörü:** `a = H c` her ölçüm için −10 × 0,01 = −0,1 verir; bu, ölçümlere eklenecek modelle tutarlı değişikliktir.
2. **Yeni ölçümler:** her ölçüme −0,1 eklenir; 1,02 → 0,92 ve 0,98 → 0,88 olur. Bu adım saldırganın sisteme gönderdiği sahte değerleri gösterir.
3. **Kestirim:** iki ölçümün 10.000 ve 2.500 ağırlıklı ortalaması (ağırlıklar toplamı 12.500) alınır; sonuç 0,912 çıkar, önceki 1,012'den tam 0,1 aşağıdadır. Bu adım kestirimin saldırganın istediği kadar kaydığını gösterir.
4. **Artıklar:** her ölçümden kestirim çıkarılır; +0,008 ve −0,032 çıkar, saldırıdan öncekiyle aynıdır. Bu adım kötü veri testinin neden bir şey görmediğini gösterir.
5. **J:** artıklardan hesaplanan kötü veri test istatistiği (ağırlıklı artık karelerinin toplamı) 3,20 çıkar, öncekiyle aynıdır. Bu adım alarmın neden çalmadığını gösterir.

```
Yeni ölçümler:  z' = [0,92  0,88]
Kestirim:       (10.000 × 0,92 + 2.500 × 0,88) / 12.500 = 0,912      (önce 1,012)
Artıklar:       0,92 − 0,912 = +0,008      0,88 − 0,912 = −0,032    (aynı)
J = 3,20                                                              (aynı)
```

Sonuç: operatör hattan 0,1 pu daha az güç aktığını görür; kötü veri testi hiçbir şey söylemez. pu (per unit, birim değer), büyüklüğün baz değere oranıdır.

**Savunma:**

- Bazı ölçümleri kriptografik olarak korumak. Saldırganın `H c` kurması için bütün ilgili ölçümlere erişmesi gerekir; birkaçı korunursa tutarlı saldırı kurulamaz.
- PMU gibi bağımsız kaynaklarla çapraz denetim.
- Zaman içinde tutarlılık denetimi.
- Model bilgisini gizli tutmak.

### Yazılımcının sorumluluğu

Burada kendi tecrübenden konuşabilirsin:

| Konu | Ne yapılır |
| --- | --- |
| Girdi doğrulama | Dışarıdan gelen her model ve ölçüm dosyası güvenilmezdir. Şema doğrulama, aralık denetimi, boyut sınırı |
| Kimlik doğrulama ve yetkilendirme | Kim hangi senaryoyu koşabilir, kim sonucu görebilir, kim modele yazabilir. En az yetki |
| Denetim izi | Kim, ne zaman, hangi model sürümüyle, hangi hesabı koştu |
| Sırlar | Parola ve anahtar kodda ve depoda durmaz |
| Bağımlılıklar | Sürüm sabitleme, zafiyet taraması, yazılım malzeme listesi |
| Ağ | Analiz servisi kontrol ağına yazamaz; veri tek yönlü gelir |
| Hata davranışı | Servis çökerse operatör eski veriyi taze sanmamalı |

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"SCADA analiz yapar."** | Ölçer ve kumanda eder. Analiz EMS uygulamalarındadır |
| **"IEC 61850 bir haberleşme protokolüdür."** | Önce bir veri modelidir; üç ayrı haberleşme servisi içerir |
| **"IEC 104 ve DNP3 aynı işi yapar, biri seçilir."** | Aynı işi yaparlar; hangisinin kullanılacağını bölge ve mevcut altyapı belirler |
| **"CIM bir dosya biçimidir."** | Bir bilgi modelidir; RDF/XML serileştirmelerinden biridir |
| **"Kontrol ağı internete bağlı değil, o halde güvenli."** | Ukrayna saldırıları kurumsal ağdan sıçradı. Taşınabilir bellek, bakım dizüstü bilgisayarı ve uzaktan erişim de yoldur |
| **"Şifrelersek güvenli olur."** | OT'de öncelik erişilebilirlik ve bütünlüktür; şifreleme gecikme ekler ve izlemeyi zorlaştırır. Önce kimlik doğrulama ve bölümleme |
| **"Dijital ikiz üç boyutlu görselleştirmedir."** | Ölçümle güncellenen ve üzerinde senaryo koşulabilen hesap modelidir |
| **"Kalite bayrağı ayrıntıdır."** | Donmuş bir ölçümü taze sanan durum kestirimi, sessizce yanlış sonuç üretir |

## Panel takip sorusu

Panelin bu konuda sorabileceği üç soru ve cevapları.

**Soru 1:** "SCADA verisi 5 saniye, PMU verisi 20 ms. İkisini aynı kestirimde nasıl kullanırsın?"

> **Mülakatta şöyle söyle:** Zaman damgasına göre hizalarım; SCADA taramasının anına en yakın PMU örneğini veya o pencerenin ortalamasını alırım. PMU'ya ölçüm doğruluğuna göre daha yüksek ağırlık veririm. SCADA ölçümlerinin kendi içinde eşzamanlı olmadığını varyansa yansıtırım.

**Soru 2:** "Web servisiniz günde 85.000 istek alıyor ve hesap 30 saniye sürüyor. Nasıl tasarlarsın?"

> **Mülakatta şöyle söyle:** İsteği kabul edip iş kimliği dönerim; hesap kuyrukta, işçilerde koşar; sonuç sorgulanır veya bildirilir. Aynı girdiyle gelen istekleri önbellekten karşılarım; anahtar, model sürümü + senaryo özetidir. İşçiler durumsuzdur, yatay ölçeklenir. Sonuç, üretildiği model sürümüyle saklanır.

"Durumsuz" işçi, kendi içinde kalıcı bilgi tutmayan işçidir; bu yüzden sayısı artırılarak yatay ölçeklenebilir.

**Soru 3:** "Operatörün 'ne olursa' senaryosu canlı modeli bozmasın. Nasıl?"

> **Mülakatta şöyle söyle:** Senaryo, canlı durumun değişmez bir anlık görüntüsünden dallanır; değişiklikler fark olarak tutulur. Yazarken kopyala mantığı.

"Yazarken kopyala", veriyi ancak değiştirileceği an kopyalamak demektir; değişmeyen kısım paylaşılır.

Aşağıdaki konuşmada geçen kısaltmalar yukarıda açıldı: IEC 61850, IEC 104 (IEC 60870-5-104), DNP3, SCADA, CIM, IEC 61970, 61968.

## 90 saniye

"Veri sahadan şöyle akar: ölçü trafosundan röleye ve uzak uç birimine, trafo merkezi içinde IEC 61850 ile, merkezden kontrol merkezine IEC 104 veya DNP3 ile, oradan SCADA veri tabanına ve enerji yönetim uygulamalarına. SCADA ölçer ve kumanda eder; analiz ayrı katmandır. Şebeke modeli için ortak dil CIM'dir: iletimde IEC 61970, dağıtımda 61968; düğüm-kesici modelinden bara-dal modeline geçiş topoloji işlemedir. Ölçümler kalite bayrağıyla birlikte zaman serisi veri tabanında tutulur. Dijital ikiz, bu modelin ölçümle güncellenen ve üzerinde senaryo koşulan halidir. Güvenlikte öncelik erişilebilirliktir; ağ bölgelere ayrılır, analiz servisi kontrol ağına yazamaz."
