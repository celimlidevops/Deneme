# Python, MATLAB, Java, JavaScript

Bu sayfa, ilandaki dört programlama dilinin güç sistemi analiz işinde nerede durduğunu anlatır. Her dil için mülakatta bilmen gerekenleri ve iyi alışkanlıkları verir. Sonunda sayısal hesap ve test tuzaklarını, örnek kodları nasıl çalıştıracağını ve 90 saniyelik konuşma metnini bulursun.

## Sayfa haritası

1. **Dört dil, dört katman:** hangi dil hangi işe yarar, ekibin ürün yığını ne.
2. **Python:** bilimsel kütüphaneler, pandapower, iyi alışkanlıklar.
3. **MATLAB:** MATPOWER, Simulink ve prototipten ürüne mesafe.
4. **Java:** büyük EMS'lerde neden yaygın, analiz modülünü servise koymak.
5. **JavaScript:** operatör arayüzünde araştırmacının bilmesi gerekenler.
6. **Sayısal iş ve test:** bellek, tekil matris, birim, test, Git.
7. **Mülakatta kod sorusu ve örnekler:** cevap sırası ve örnek betikler.
8. **90 saniye:** mülakatta söyleyeceğin kısa metin.
9. **Kendini yokla:** sorular ve cevaplar.

## 1. Dört dil, dört katman

İlandaki diller: Java, Python, JavaScript, MATLAB ve "vb.". Bu dört dil dört katmandır, dört ayrı meslek değildir. Yani aynı hesap fikirden ekrana giderken farklı dillerden geçer.

| Dil | Bu işte yeri |
| --- | --- |
| Python | Analiz betiği, optimizasyon modeli, veri temizleme, makine öğrenmesi, pandapower |
| MATLAB | Algoritma prototipi, Simulink dinamik model, MATPOWER, üniversite çalışması |
| Java | Uzun ömürlü sunucu, enerji yönetim modülü, web servis, kurumsal ürün |
| JavaScript | Operatör ve planlamacı arayüzü, grafik, coğrafi gösterim |

### Ekibin ürün yığını

Aynı dönemde yayımlanan aday araştırmacı ilanı, ekibin ürün yığınını daha açık yazar:

- Java,
- JavaScript,
- ilişkisel veri tabanı,
- REST/SOAP,
- Git,
- Maven,
- Jenkins veya GitLab CI.

Terimler:

- **Ürün yığını:** bir yazılım ürününü oluşturan dil, araç ve altyapıların toplamı.
- **REST** (Representational State Transfer): web üzerinden veri alışverişinin yaygın, hafif yolu. Genelde JSON (JavaScript Object Notation, metin tabanlı veri biçimi) taşır.
- **SOAP** (Simple Object Access Protocol, Basit Nesne Erişim Protokolü): daha eski, XML (Extensible Markup Language, işaretleme dili) tabanlı web servis protokolü.
- **Git:** kodun sürümlerini tutan sürüm yönetim aracı.
- **Maven:** Java projesinin bağımlılıklarını ve derlemesini yöneten araç.
- **Jenkins / GitLab CI:** her kod değişikliğinde testleri otomatik çalıştıran araçlar. **CI** (Continuous Integration), sürekli entegrasyon demektir.

Senin kadron analiz araştırmacısıdır. Yine de algoritmayı bu yığına teslim edemeyen kişi ürün döngüsünün dışında kalır.

> **Sade anlatım:** Sen hesabı bulan kişisin. Ama hesabın ürüne girmesi için onu ekibin kullandığı dile ve araçlara uygun biçimde teslim edebilmen gerekir.

## 2. Python

### Bilimsel yığın

| Kütüphane | Ne işe yarar |
| --- | --- |
| NumPy | Dizi (sayı vektörü ve matrisi) |
| SciPy | Seyrek doğrusal cebir ve optimizasyon |
| pandas | Tablo |
| matplotlib | Çizim |

Şebeke için iki yol var:

- **pandapower:** PowerFactory'ye benzer veri modeli kullanır, arka planda PYPOWER çalışır. PYPOWER, MATPOWER'ın Python'a aktarılmış hâlidir.
- **Doğrudan SciPy seyrek matris:** hesabı kendin kurarsın.

**Seyrek matris**, elemanlarının çoğu sıfır olan matristir. Şebekede her bara yalnızca birkaç komşusuna bağlıdır. Bu yüzden şebeke matrisleri seyrektir. Seyrek matris yalnızca sıfır olmayanları saklar.

Büyük matriste `numpy.linalg` yoğun çözücü kullanma. `scipy.sparse.linalg` kullan. **Yoğun çözücü**, matrisin bütün elemanlarını, sıfırlar dahil, saklayıp işler.

### İyi alışkanlıklar

- **Birim:** güç, gerilim ve açı aynı birimde olsun. Fonksiyonun başında pu'ya çevir, sonunda MW'ye dön. **pu** (per-unit, birim değer), her büyüklüğün seçilmiş bir baz değere oranıdır.
- **İşaret sözleşmesi:** gücün hangi yönde pozitif sayıldığını modülün doc'una (açıklama metnine) yaz.
- **Rastgele tohum:** tohumu sabitle, tahmin kodunda özellikle. **Tohum**, rastgele sayı üretecinin başlangıç değeridir; sabitlenince sonuç her seferinde aynı çıkar.
- **Elde doğrulanmış test:** her hesap için küçük bir elde doğrulanmış şebeke testi yaz. Üç baralık sistem altın değerdir.
- **Vektörize et:** Python döngüsüyle her hat için Jacobian doldurmak binlerce barada yavaşlar. Önce doğru, sonra profil. **Vektörize etmek**, döngü yerine bütün diziyi tek işlemle hesaplamaktır. **Profil almak**, kodun zamanını nerede harcadığını ölçmektir.

**Bara**, şebeke modelinde hatların, trafoların ve yüklerin birleştiği düğümdür. **Jacobian**, yük akışı denklemlerinin bilinmeyenlere göre türevlerinden oluşan matristir.

### pandapower'ı nasıl anlatırsın

> **Mülakatta şöyle söyle:** "Şebekeyi eleman tablolarıyla kurarım, AC yük akışı ve N-1 koşarım, sonucu DataFrame olarak alırım. Özel algoritma gerekirse iç Ybus'u seyrek matris olarak çekip kendi NR'ımı yazarım."

Cümledeki terimler:

- **AC yük akışı:** alternatif akım şebekesinde gerilimleri ve hat akışlarını tam, doğrusal olmayan denklemlerle hesaplamak.
- **N-1:** şebekedeki elemanlardan biri devre dışı kaldığında sistemin hâlâ limitler içinde kalıp kalmadığını sınamak.
- **DataFrame:** pandas'ın tablo nesnesi.
- **Ybus:** bara admitans matrisi; hangi baranın hangisine hangi admitansla bağlı olduğunu tutar.
- **NR:** Newton-Raphson, yük akışını yinelemeli çözen yöntem.

Bu cümle, paketi kullanan ile motoru anlayan kişiyi ayırır.

## 3. MATLAB

**MATPOWER**, yük akışı ve OPF'in referans akademik aracıdır. **OPF** (Optimal Power Flow, optimal güç akışı), limitlere uyarak en düşük maliyetli işletme noktasını bulan hesaptır.

Bilmen gereken adlar:

| Ad | Ne |
| --- | --- |
| `runpf` | Yük akışını çalıştırır |
| `runopf` | OPF'i çalıştırır |
| `mpc.bus` | İç modelde bara tablosu |
| `mpc.branch` | İç modelde dal (hat, trafo) tablosu |
| `mpc.gen` | İç modelde üreteç tablosu |

Yeni bir yöntemi önce MATPOWER vakasında göstermek, hakem ve ekip için ortak dildir. **Vaka**, belli bir şebekenin hazır model dosyasıdır.

**Simulink**, AVR-PSS ve evirici kontrolünün blok modelidir.

- **AVR** (Automatic Voltage Regulator, Otomatik Gerilim Regülatörü): jeneratörün çıkış gerilimini ayarlayan kontrolör.
- **PSS** (Power System Stabilizer, Güç Sistemi Dengeleyicisi): salınımları sönümleyen ek kontrol.
- **Evirici:** doğru akımı alternatif akıma çeviren güç elektroniği cihazı; güneş ve batarya bağlantısında kullanılır.

Üretime Simulink gömülmez; gömülen, orada doğrulanmış denklem ve kazançtır. **Kazanç**, kontrolördeki ayar katsayısıdır.

"MATLAB'da çalıştı" ile "üründe çalışıyor" arasındaki mesafe test ve dildir.

> **Sade anlatım:** MATLAB bir laboratuvar tezgâhıdır. Fikri orada denersin. Ürüne giden şey tezgâhın kendisi değil, orada kanıtladığın formüldür.

## 4. Java

Büyük EMS'ler (Energy Management System, Enerji Yönetim Sistemi) uzun süre ayakta kalan, çok kullanıcılı, servisleşmiş sistemlerdir. Java bu sınıfta yaygındır. Üç nedeni var:

- statik tip (değişkenin türü derleme anında bellidir, hata erken yakalanır),
- olgun servis çerçeveleri,
- uzun destek.

### Analiz modülünü servise koymak

Araştırmacıdan beklenen, bir analiz modülünü şu yüzeye koyabilmektir:

- **Girdi ve çıktı nesneleri nettir** (bara sonucu, ihlal listesi).
- **Katmanlar karışmaz:** hesap, veri tabanı ve arayüz aynı sınıfta karışmaz.
- **İstisna yutulmaz:** ıraksayan yük akışı bir istisna veya kalite bayrağıdır, sessiz boş liste değildir. **İstisna**, programın hatayı bildirme yoludur. **Iraksamak**, yinelemeli hesabın bir sonuca yaklaşmaması demektir.
- **Koleksiyon ve eşzamanlılık:** aynı servise paralel N-1 işi düşer. Paylaşılan değişebilir liste yarış üretir. İş parçacığı başına ayrı vaka kopyası güvenli başlangıçtır.

**Yarış** (race condition), iki iş parçacığının aynı veriyi aynı anda değiştirip sonucu bozmasıdır. **İş parçacığı** (thread), program içinde paralel çalışan iş koludur.

> **Sade anlatım:** Aynı defteri iki kişi aynı anda silip yazarsa defter bozulur. Her kişiye kendi fotokopisini verirsen sorun çıkmaz.

### Sözdizimi mülakatında yeterli olanlar

- sınıf ve arayüz,
- `List`/`Map`,
- istisna,
- basit bir döngü,
- bir birim testin ne iddia ettiği.

Spring ve Maven'i "bağımlılığı ve servisi yöneten araçlar" diye bil. Çerçeve içi ezberi, analiz sorusunun önüne geçirme.

## 5. JavaScript

YTBS (Yük Tevzi Bilgi Sistemi) ve SIPS'te (System Integrity Protection Scheme, Akıllı Koruma Sistemi) operatör web arayüzü vardır. Araştırmacı piksel yarıştırmaz; şunları bilir:

- **Çizim yükü:** tarayıcı binlerce barayı her mouse hareketinde baştan çizmez. Çözümler: tuval veya WebGL, kümeleme, görünür alan. **Tuval** (canvas), tarayıcıda piksel düzeyinde hızlı çizim alanıdır. **WebGL**, tarayıcıda ekran kartıyla çizim yapan arayüzdür. **Kümeleme**, uzaktan bakınca yakın noktaları tek simgede toplamaktır. **Görünür alan**, yalnız ekranda görünen kısmı çizmektir.
- **Zaman serisi:** frekans ve yük tahmini gibi zaman serileri ayrı grafiktir. Eksen birimi yazılır.
- **Hesabın yeri:** hesap tarayıcıda değil sunucuda koşar. Arayüz sonucu ve işin durumunu gösterir.
- **Web servis:** REST JSON taşır. SOAP, eski SCADA/EMS entegrasyonunda hâlâ kapıdadır. İkisi de "web servis" maddesinin içindedir. **SCADA** (Supervisory Control and Data Acquisition, Denetleyici Kontrol ve Veri Toplama), sahadaki ölçümleri toplayan ve uzaktan kumanda veren sistemdir.

**TypeScript**, JavaScript'e tip ekleyen dildir. Büyük arayüzde daha az tip hatası demektir. Zorunlu ilan maddesi değildir.

## 6. Sayısal iş ve test

### Sayısal tuzaklar

- **Bellek:** seyrek matrisin yoğun kopyasını almak bellek patlatır. 10 bin bara Ybus'u seyrek tutulursa megabayt, yoğun tutulursa gigabayttır.
- **Tekil Jacobian:** Jacobian tekile yakınsa çözücü uyarı verir. Uyarıyı `except: pass` ile yutma. **Tekil matris**, tersi alınamayan matristir; denklem sistemi tek çözüm vermez. `except: pass`, Python'da hatayı yakalayıp hiçbir şey yapmadan geçmek demektir.
- **Açı birimi:** açı radyan mıdır derece mi? Çizimde derece, denklemde radyan.

### Test

Şu durumların testi olmalı:

- elde çözülmüş 3 bara,
- bilinen kötü veri,
- bilinen N-1 ihlali,
- ıraksayan vaka,
- boş ölçüm listesi.

Altın değerleri dosyada sabitle. **Altın değer**, doğruluğu bilinen ve test tarafından beklenen sonuçtur.

### Git

- Dal (branch) aç, küçük iş yap, mesajda nedeni yaz.
- Büyük `.pfd` veya vaka dosyası için sürüm notu tut. `.pfd`, PowerFactory'nin proje dosyası uzantısıdır.
- Gizli şebeke verisini depoya koyma.

## 7. Mülakatta kod sorusu ve örnekler

Mülakatta kod sorusu gelirse şu sırayı izle:

1. **Önce sözleşmeyi söyle:** girdi, çıktı, birim, başarısızlık.
2. **Sonra en küçük doğru çözümü yaz.**
3. **Sonra iyileştir:** seyrek veya vektör diye.

Üç barayı zihinden koşamıyorsan ulusal modeli konuşma.

### Örnek betikler

Örnekler bu klasörün `ornekler` altındadır. Aşağıdaki komutlar önce NumPy ve SciPy'ı kurar, sonra üç örneği sırayla çalıştırır: DC yük akışı, WLS (Weighted Least Squares, ağırlıklı en küçük kareler) durum kestirimi ve ekonomik dağıtım.

```
pip install numpy scipy
python dc_yuk_akisi.py
python wls_durum_kestirimi.py
python ekonomik_dagitim.py
```

- **DC yük akışı:** AC denklemlerinin doğrusallaştırılmış, hızlı yaklaşımı.
- **Durum kestirimi:** hatalı ve eksik ölçümlerden şebekenin en olası gerilim ve açılarını bulmak.
- **Ekonomik dağıtım:** yükü santraller arasında en düşük maliyetle paylaştırmak.

### 90 saniyelik metin için not

Aşağıdaki metin sayfanın sözlü özetidir. İçindeki terimler yukarıda açıldı: Ybus (Bölüm 2), ıraksama (Bölüm 4), WLS (Bölüm 7). Metnin ana fikri: her dili kendi katmanında düşünürsün, büyük matrisi seyrek tutarsın, her hesabı test edersin ve hatayı saklamazsın.

## 90 saniye

“Python’da algoritmayı ve veriyi, MATLAB’da prototipi, Java’da servis haline gelmiş hesap motorunu, JavaScript’te operatörün göreceği sonucu düşünürüm. Büyük matrisi seyrek tutarım. Her yeni hesabın üç baralık bir testi olur. Iraksama ve kötü veri bir bayraktır, boş sonuç değildir. Paket kullanırım ama Ybus ve WLS’yi kendim de yazarım.”

## Kendini yokla

Önce cevabı kapat, kendin söyle, sonra kontrol et.

1. **Dört dilin bu işteki yeri nedir?**
   Python analiz betiği, optimizasyon, veri, makine öğrenmesi, pandapower. MATLAB prototip, Simulink, MATPOWER. Java uzun ömürlü sunucu, enerji yönetim modülü, web servis. JavaScript operatör arayüzü, grafik, coğrafi gösterim.

2. **Aday araştırmacı ilanı ekibin ürün yığınını nasıl yazar?**
   Java, JavaScript, ilişkisel veri tabanı, REST/SOAP, Git, Maven, Jenkins veya GitLab CI.

3. **Büyük matriste hangi çözücüyü kullanırsın?**
   `numpy.linalg` yoğun çözücüyü değil, `scipy.sparse.linalg`'ı.

4. **10 bin baralı Ybus seyrek ve yoğun tutulunca bellek ne olur?**
   Seyrek tutulursa megabayt, yoğun tutulursa gigabayt.

5. **Iraksayan yük akışı Java servisinde nasıl dönmeli?**
   Bir istisna veya kalite bayrağı olarak; sessiz boş liste olarak değil.

6. **Paralel N-1 işinde yarışı nasıl önlersin?**
   Paylaşılan değişebilir liste kullanmam; iş parçacığı başına ayrı vaka kopyası güvenli başlangıçtır.

7. **Simulink'te geliştirilen kontrol ürüne nasıl girer?**
   Simulink gömülmez; orada doğrulanmış denklem ve kazanç gömülür.

8. **Açı radyan mı, derece mi?**
   Çizimde derece, denklemde radyan.

9. **Hangi testler olmalı?**
   Elde çözülmüş 3 bara, bilinen kötü veri, bilinen N-1 ihlali, ıraksayan vaka, boş ölçüm listesi. Altın değerler dosyada sabit.

10. **Kod sorusuna nasıl başlarsın?**
    Sözleşmeyi söylerim: girdi, çıktı, birim, başarısızlık. Sonra en küçük doğru çözüm, sonra seyrek veya vektör iyileştirmesi.
