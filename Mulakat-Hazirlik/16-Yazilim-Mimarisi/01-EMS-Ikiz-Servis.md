# EMS zinciri ve dijital ikiz

Bu sayfa, şebeke hesabının bir yazılım ürününe nasıl dönüştüğünü anlatır. Önce hesap halkalarının sırasını, sonra dijital ikizi, veri ve servis katmanını, arayüzü, güvenliği ve sürümü göreceksin. En sonda senin bu yapıda nerede duracağın var.

## Zincir

EMS (Energy Management System, enerji yönetim sistemi), iletim şebekesinin hesaplarını yapan yazılım katmanıdır. Klasik bir enerji yönetim sistemi işi şu halkalara bölüp sıraya dizer:

| Sıra | Halka | Ne yapar |
| --- | --- | --- |
| 1 | Veri edinme | SCADA analog ve durum bilgisi, sayaç, PMU, hava, piyasa programı toplanır |
| 2 | Veri doğrulama ve zaman hizalama | Gelen veri denetlenir ve aynı zaman anına oturtulur |
| 3 | Topoloji işlemcisi | Kesici durumundan enerjili adaları ve bara modelini kurar |
| 4 | Durum kestirimi ve kötü veri | Ölçümlerden şebekenin en olası durumu bulunur, hatalı ölçüm ayıklanır |
| 5 | Baz durum yük akışı | Arızasız temel durumdaki güç akışları hesaplanır |
| 6 | Güvenlik analizi | Arıza senaryolarında sınır ihlali olup olmadığı taranır |
| 7 | Kararlılık ve atalet gibi seçilmiş dinamik hesaplar | Zamana bağlı davranışın seçilmiş parçaları hesaplanır |
| 8 | Tahmin | Yük, rüzgâr, güneş tahmini |
| 9 | Optimizasyon ve gerilim planı | En uygun üretim ve gerilim ayarları aranır |
| 10 | Operatör arayüzü, kayıt, komşu sistemlere servis | Sonuç gösterilir, kaydedilir ve başka sistemlere verilir |

Tablodaki kısaltmalar:

- **SCADA** (Supervisory Control and Data Acquisition, denetleyici kontrol ve veri toplama): sahadan ölçüm toplayan ve uzaktan kumanda veren sistem. "Analog" ölçülen sayı (akım, gerilim, güç), "durum" ise açık/kapalı bilgisidir (kesici konumu gibi).
- **PMU** (Phasor Measurement Unit, fazör ölçüm birimi): gerilim ve akımın genliğini ve açısını uydu saatine bağlı zaman damgasıyla ölçen cihaz.

> **Sade anlatım:** Zincir bir fabrika bandı gibidir. Her halka bir öncekinin çıktısını alır, kendi işini yapar, bir sonrakine verir. Bir halka bozuk veri verirse arkadaki bütün halkalar yanlış hesaplar.

### YTBS bu zincirin neresinde

YTBS (Yük Tevzi Bilgi Sistemi), grubun enerji yönetim platformudur. YTBS'nin kamuoyuna açık tanımı, bu zincirin ürünleşmiş halidir. Tanımda geçen parçalar:

- model
- veri
- güvenlik
- tahmin
- optimizasyon
- dijital ikiz
- SCADA/EMS ile web servis

30'dan fazla modül, aynı zincirin parçalarıdır.

> **Mülakatta şöyle söyle:** "Hepsini ben yazarım" deme. "Hangi halkada durduğumu ve komşu halkanın sözleşmesini bilirim" de.

Buradaki "sözleşme", bir halkanın komşusundan hangi veriyi hangi biçimde aldığı ve hangi biçimde verdiğidir.

### Çevrimdışı ve çevrimiçi çalışma

İki çalışma türü vardır:

| | Çevrimdışı çalışma | Çevrimiçi çalışma |
| --- | --- | --- |
| Amaç | Planlama ve eğitim | Bu saatin kestirilmiş durumu |
| Örnek | Yarının bakımı, beş yıl sonraki hat, bir eğitim senaryosu | Şu anki şebeke |
| Model | Yayımlanmış bir sürüm | Topolojisi dakikada değişir |

İkisi aynı hesap motorunu kullanabilir, aynı veriyi kullanamaz. Çevrimiçi modelin topolojisi dakikada değişir. Çevrimdışı model ise yayımlanmış, sabit bir sürümdür.

İkisi karışırsa ne olur: operatör, bakımda olan hattı ayakta görür.

## Dijital ikiz

Bu işte dijital ikiz, şebekenin üç boyutlu resmi değildir. Dijital ikiz, ölçümle güncellenen ve üzerinde senaryo koşulan bir hesap modelidir.

İkizden beklenenler:

- Şu anki durum, kestirim kalitesiyle birlikte
- "Şu hat açılırsa" sorusunun dakikalar değil saniyeler içinde cevabı
- Yarının tahmini üzerinde aynı soru
- Eğitimde gerçek sistemi bozmadan oynama

### İkiz ile kumanda ayrımı

İkiz, sahayı kumanda eden SCADA'nın yerine geçmez. Kumanda yetkisi, prosedür ve yetki matrisi ayrıdır. Yetki matrisi, hangi rolün hangi işlemi yapabileceğini gösteren tablodur.

Analiz ekranındaki "önerilen üretim" bir talimat olmaz. Ancak operatör ve piyasa kuralı onu talimat yaptığında talimata dönüşür.

> **Mülakatta şöyle söyle:** Bu ayrımı söylemen, kritik altyapıda çalıştığını gösterir.

## Veri ve servis

### İki tür veri

| Veri | Ne tutar | Nerede |
| --- | --- | --- |
| Şebeke kimliği | Bara, ekipman, bağlantı, limitin sürümü | İlişkisel veri tabanı |
| Zaman serisi | Ölçüm, tahmin | Ya aynı tabanda ya da zaman serisi için ayrılmış bir depoda |

İkisi aynı indeksle zorlanırsa sorgu yavaşlar. Çünkü şebeke kimliği kimlik üzerinden, zaman serisi ise zaman aralığı üzerinden sorgulanır.

Anahtar nokta: ekipman kimliği zaman içinde değişir. Ekipman kimliği, ölçüm kimliğiyle karıştırılmaz.

### Servis yüzeyi

Servis yüzeyi, sistemin dışarıya açtığı kapılardır. Üç parça var:

- **REST/JSON:** REST (Representational State Transfer, temsili durum aktarımı) ile JSON (JavaScript Object Notation, metin tabanlı veri biçimi), yeni modüller arasında rahat bir sözleşmedir. Dört öğesi vardır: kaynak, fiil, durum kodu, sayfalama.
- **SOAP:** SOAP (Simple Object Access Protocol, basit nesne erişim protokolü), eski EMS ve kurumsal entegrasyonda yaşar. Sözleşmesi WSDL (Web Services Description Language, web servis tanım dili) dosyasıdır. WSDL sözleşmesi kırılmadan alan eklenir.
- **YTBS'nin SCADA/EMS ile web servisi:** bu kapıdır.

### 85 bin istek ve kuyruk

85 bin istek ölçeği, ağır hesabı senkron olarak, yani isteğin içinde koşturmamayı gerektirir. Akış şöyledir:

1. İstek işi kuyruğa bırakır.
2. Hesap kuyrukta koşar.
3. Sonuç hazır olunca alınır.

Neden: ağır N-1 hesabı, HTTP (HyperText Transfer Protocol, web istek protokolü) zaman aşımının içinde bitmez. N-1, şebekeden tek bir elemanın (hat, trafo, ünite) düşürüldüğü arıza senaryosudur.

### İş kuyruğu

İş kuyruğu şöyle çalışır:

- Her arıza bir iştir.
- İşçiler, vaka kopyası üzerinde çözer.
- Sonuçlar ihlal tablosuna yazılır.

Paylaşılan tek vaka nesnesini on iş parçacığı değiştirirse sonuç rastgeledir. Bu yüzden kopya veya değişmez girdi şarttır.

> **Sade anlatım:** On kişi aynı kâğıda aynı anda yazarsa kâğıtta ne kalacağı belli olmaz. Herkese kendi fotokopisini verirsin.

### Kalite bayrağı

Kalite bayrağı, sonucun yanında "bu sayıya ne kadar güvenebilirim" bilgisini taşır. Bayrak türleri:

- kestirim kötü
- topoloji şüpheli
- ölçüm eski
- çözüm ıraksak (hesap yakınsamadı)

Bayrak varsa:

- Ekranda sonuç kırmızı görünür.
- Otomasyon o sonucu "uygula"ya çevirmez.

Operatör güveni, her sayının yanında nedenini görmekle oluşur. Siyah kutu skoru güven oluşturmaz.

## Arayüz

Operatörün sorusu "Jacobian kaç?" değildir. Jacobian, yük akışı çözücüsünün içinde kullanılan türev matrisidir; operatörü ilgilendirmez.

Ekranda olması gerekenler:

- Coğrafya veya tek hat şeması üzerinde ihlal
- İhlali doğuran arıza
- Önerilen eylem ve eylemin yan etkisi
- Tahmin bandı
- Son tazeleme zamanı ve veri yaşı

Araştırmacı ekranı tasarlamayabilir. Ama ekranın hangi sayıyı hangi birimle istediğini bilmek zorundadır. Birim hatası bu katmanda sahaya çıkar.

## Güvenlik ve sürüm

### Güvenlik

Şebeke modeli ve gerçek zaman ölçümü hassastır. Depoya şunlar konmaz:

- parola
- üretime ait ticari veri
- kişisel müşteri verisi

Erişim rollere göre verilir. Ayrı roller:

| Rol | Yetki |
| --- | --- |
| Analiz gören | Sonucu görür |
| Modeli yayımlayan | Model sürümünü yayına alır |
| Kumanda eden | Sahaya komut verir |

Denetim kaydı, kimin hangi senaryoyu koştuğunu tutar.

Bu bir siber güvenlik uzmanlığı iddiası değildir. Ürün ekibinin asgari hijyenidir.

### Sürüm

Üç şey ayrı sürüm numarası taşır:

- model sürümü
- algoritma sürümü
- limit sürümü

"Geçen ay bu hat ihlalliydi" iddiası, ancak o ayın modeliyle tekrar koşulursa doğrudur.

Test ortamı üretim verisinin birebir kopyası olmak zorunda değildir. Sentetik veya maskelenmiş veri, algoritma testi için yeter. Üretim ortamında deneme koşusu olmaz.

### İzleme

İzlenen metrikler:

- Servis ayakta mı?
- Kuyruk büyüyor mu?
- Son kestirim kaç saniye sürdü?
- Kaç kötü veri atıldı?

Araştırmacı bu metrikleri, algoritması yavaşladığında okuyabilmelidir.

## Senin yerin

Tipik katkı, zincirin bir halkasındaki yöntemi iyileştirip o halkanın sözleşmesini bozmamaktır.

Örnek: geçici hal taramasını hızlandıran bir metrik.

- Aynı ihlal JSON şemasına yazar.
- Kalite bayrağını doldurur.
- Üç baralık ve bir büyük sentetik vakayla test edilir.
- Çevrimiçi süre bütçesine sığar.

Mülakatta kendi projenden buna en yakın köprüyü seç.

Aşağıdaki konuşmada geçen kısaltmalar yukarıda açıldı: EMS, SCADA, N-1.

## 90 saniye

“EMS sırası ölçüm, topoloji, kestirim, yük akışı, N-1, tahmin ve optimizasyondur. Dijital ikiz bu modelin ölçümle yaşayan, senaryo koşulan halidir; kumanda yetkisi SCADA’da kalır. Ağır hesap istek içinde değil kuyrukta koşar. Sonuç kalite bayrağıyla çıkar. Model, algoritma ve limit ayrı sürüm taşır. Ben halkadaki hesabın sözleşmesini ve testini sahiplenirim.”
