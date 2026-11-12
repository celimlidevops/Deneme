# Dağıtım sistemi

Bu sayfa dağıtım şebekesinin iletimden nerede ayrıldığını anlatır. Sonra gerilim düşümünü, kaybı, dağıtık üretimin bağlantı sorularını, korumayı, dağıtım şirketinin yazılım sistemlerini ve planlamayı sırayla açar.

**Dağıtım**, elektriği trafo merkezinden evlere ve işyerlerine daha düşük gerilimle ulaştıran yerel şebekedir. **İletim** ise elektriği santrallerden şehirlere yüksek gerilimle taşıyan ana şebekedir. Bu sayfadaki her şey bu iki şebekenin farkına dayanır.

## Sayfa haritası

1. **İletimden ayrılan yer:** radyal işletme, R/X oranı, dengesizlik ve ölçek.
2. **Gerilim ve kayıp:** gerilim düşümü formülü, regülasyon araçları, teknik ve ticari kayıp, çeşitlilik.
3. **Dağıtık üretim:** bağlantı çalışmasının standart soruları ve barındırma kapasitesi.
4. **Koruma ve otomasyon:** aşırı akım kademelemesi, OTK, FLISR, SAIDI ve SAIFI.
5. **Sistemler:** GIS, SCADA, DMS, AMI ve kimlik eşleme sorunu.
6. **Planlama:** dağıtım planlama kararları ve dağıtım durum kestirimi.
7. **90 saniye:** mülakatta söyleyeceğin kısa metin.
8. **Kendini yokla:** sorular ve cevaplar.

## 1. İletimden ayrılan yer

### Radyal işletme

Dağıtım çoğunlukla **radyal** işletilir. Radyal, ağaç dalları gibi demektir: her yük kaynağa tek bir yoldan bağlıdır.

Şebekede halka varsa bile bir yerde **açık nokta** bırakılır. Yani halkadaki bir anahtar açık tutulur. Bunun iki sebebi vardır:

- arıza bölgesi küçük kalsın,
- koruma basit kalsın.

Sonuçları:

- Tek besleme yolu vardır.
- Ters akış yokken gerilim kaynaktan uca doğru düşer.
- **Kısa devre gücü** uçta zayıftır. Kısa devre gücü, bir noktada arıza olduğunda şebekenin oraya basabileceği güçtür; şebekenin o noktadaki "sağlamlığını" gösterir.

### R/X oranı yüksek

**R** hattın direnci, **X** reaktansıdır. Reaktans, alternatif akımda bobin etkisinden doğan, enerjiyi harcamayan ama akımı zorlaştıran büyüklüktür. **R/X**, bu ikisinin oranıdır.

Dağıtımda R/X iletimden yüksektir. Özellikle AG (alçak gerilim) kabloda R, X'ten büyük olabilir.

O zaman **aktif güç** (gerçekten iş yapan güç, P) de gerilimi değiştirir. İletimde gerilimi daha çok **reaktif güç** (iş yapmayan ama gerilimi ayakta tutan güç, Q) belirler; dağıtımda bu kural zayıflar.

Örnek: çatı güneşinin öğlen gerilimi yükseltmesi, reaktiften çok aktif güç enjeksiyonudur. Bu yüzden "Daha fazla kapasitör basalım" cevabı bu problemi büyütebilir. Kapasitör reaktif güç üretir ve gerilimi daha da yükseltir.

> **Sade anlatım:** İletimde gerilimi reaktif güç oynatır. Dağıtımda direnç büyük olduğu için aktif güç de oynatır. Güneşin yükselttiği gerilimi kapasitörle düzeltmeye çalışmak, ateşe odun atmaktır.

### Fazlar eşit yüklenmez

Üç fazlı şebekede ideal olan, üç fazın eşit yüklenmesidir. Dağıtımda bu olmaz. Sebepler:

- kırsal fider (uzun, az müşterili hat),
- tek fazlı müşteri,
- bitişik iki fazda kaynak (iki faz arasına bağlanan tek bir yük, örneğin kaynak makinesi).

**Dengeli yük akışı** üç fazı eşit varsayarak tek faz çözer. Bu varsayım gerilim ihlalini gizler, çünkü en çok yüklü fazın gerilimi ortalamada kaybolur.

Dağıtım yazılımı **üç faz, dört tel** düşünebilmelidir: üç faz iletkeni artı nötr. OpenDSS (Open Distribution System Simulator, açık kaynak dağıtım sistemi simülatörü) ve benzeri araçlar bu yüzden iletim paketlerinden ayrı anılır.

### Ölçek

Ölçek de farklıdır:

| | İletim | Dağıtım |
|---|---|---|
| Model büyüklüğü | Binlerce bara zor bir modeldir | On binlerce düğüm normaldir |
| Veri kalitesi | Görece tam | Eksik sayaç ve hatalı GIS normaldir |

**Bara** (veya düğüm), hatların, trafoların ve yüklerin birleştiği bağlantı noktasıdır. **GIS** (Geographic Information System, Coğrafi Bilgi Sistemi), şebekenin harita üzerindeki kaydıdır; Bölüm 5'te tekrar geçiyor.

Algoritma "veri tam" varsayarsa sahada susar.

## 2. Gerilim ve kayıp

### Gerilim düşümü

Radyal fiderde yaklaşık gerilim düşümü şu formülle verilir. **Fider**, trafo merkezinden çıkan tek bir dağıtım hattıdır.

Formülde P aktif güç, Q reaktif güç, R direnç, X reaktans, V gerilimdir:

```
ΔV ≈ (P R + Q X) / V
```

Formül, Bölüm 1'deki fikri gösterir: R büyükse PR terimi de büyür, yani aktif güç gerilimi belirgin biçimde değiştirir.

### Regülasyon araçları

**Regülasyon**, gerilimi izin verilen bantta tutmaktır. Araçlar ucuzdan pahalıya düşünülür:

1. İletken kesiti ve faz dengeleme
2. Hat başı gerilim ayarı, OLTC (On-Load Tap Changer, yük altında kademe değiştirici: trafonun sarım oranını enerji kesmeden değiştiren düzenek)
3. Hat regülatörü (seri regülasyon trafosu)
4. Şönt kapasitör, sabit veya anahtarlamalı (**şönt**: hatta seri değil, hat ile toprak arasına paralel bağlı)
5. Dağıtık üretimin reaktif modu (volt-var, volt-watt)
6. Depolama ve talep kaydırma
7. Yeni çıkış fideri veya yeni trafo merkezi

Beşinci maddedeki modlar:

- **Volt-var:** evirici, gerilime bakarak reaktif güç üretir veya tüketir.
- **Volt-watt:** evirici, gerilim çok yükselince aktif gücünü kısar.

**Evirici** (inverter), güneş panelinin doğru akımını şebekenin alternatif akımına çeviren güç elektroniği cihazıdır.

### Teknik kayıp ve ticari kayıp

Kayıp iki parçadır:

| Tür | İçeriği | Nasıl bulunur |
|---|---|---|
| **Teknik kayıp** | I²R (akımın karesi çarpı direnç; iletkendeki ısınma), trafo bakır ve boşta demir kaybı, korona, bağlantı direnci | Yük akışıyla hesaplanır |
| **Ticari kayıp** | Kaçak ve ölçüm hatası | Enerji bilançosu ile teknik kayıp arasındaki farktan tahmin edilir; bu bir veri problemidir |

Terimler:

- **Bakır kaybı:** trafo sargılarındaki, yükle artan ısınma kaybı.
- **Boşta demir kaybı:** trafo enerjili olduğu sürece, yük olmasa da çekirdekte oluşan kayıp.
- **Korona:** yüksek gerilimde iletken çevresindeki havanın iyonlaşmasıyla oluşan kayıp.
- **Enerji bilançosu:** fidere giren enerji ile faturalanan enerji arasındaki fark.

İkisi aynı projeyle çözülmez. Teknik kaybı mühendislik düşürür; ticari kaybı veri analizi bulur.

### Çeşitlilik

**Çeşitlilik**, yüklerin aynı anda en yüksek değerini çekmemesidir. Yüz dairenin aynı anda **puant** (en yüksek tüketim) çekmemesi, trafo boyutunu kurtarır.

Elektrikli araç ve elektrikli ısıtma çeşitliliği azaltır, çünkü insanlar bunları benzer saatlerde kullanır.

Eski **çakışma katsayısıyla** (aynı anda devrede olan yük oranı) yeni yükü boyutlamak, fideri sessizce doldurur.

> **Sade anlatım:** Her ev kendi en yüksek tüketimine çıkabilir, ama hepsi aynı anda çıkmaz; trafo bu yüzden bütün evlerin en yüksek değerlerinin toplamı kadar büyük olmak zorunda kalmaz. Herkes akşam aynı saatte arabasını takınca bu rahatlık biter.

## 3. Dağıtık üretim

**Dağıtık üretim** (DG, Distributed Generation), dağıtım şebekesine bağlanan küçük üretimdir: çatı güneşi, küçük rüzgâr, batarya gibi.

### Bağlantı çalışmasının standart soruları

| Soru | Ne kontrol edilir |
|---|---|
| **Ters akış var mı?** | Üst trafo ve röle ters gücü görüyor mu? |
| **Gerilim yükselmesi limitin içinde mi?** | En kötü durum: minimum yük, maksimum üretim. |
| **Kademe kontrolü avlanıyor mu?** | Güneş bir bulutla düşünce OLTC peşinden gidiyor mu? |
| **Kısa devre katkısı artıyor mu?** | Evirici katkısı senkron makine gibi 6–10 kat değildir; çoğunlukla 1,1–1,5 kat nominal akım civarında sınırlanır ve hızla kesilir. Koruma "eski kısa devre gücü" ile koordineli kalmayabilir. |
| **Ada** | Şebeke gidince evirici adayı canlı tutmamalı. |
| **Güç kalitesi** | Harmonik, DC enjeksiyon, fliker, dengesizlik. Şebeke yönetmeliği ve dağıtım bağlantı kriterleri bu başlıkları sayar. |

Tablodaki terimler:

- **Ters akış:** üretim yerel yükten fazla olunca gücün kaynağa, yani trafo merkezine doğru geri akması.
- **Avlanma:** kademe değiştiricinin gerilim inip çıktıkça sürekli kademe değiştirmesi; cihazı aşındırır.
- **Senkron makine:** klasik santral jeneratörü. Kısa devrede nominal akımının 6–10 katını basabilir.
- **Nominal akım:** cihazın etiket akımı.
- **Ada:** şebekeden kopmuş ama içindeki üretim sayesinde enerjili kalan küçük şebeke parçası.
- **DC enjeksiyon:** eviricinin şebekeye istemeden doğru akım bileşeni vermesi.
- **Fliker:** gerilimdeki hızlı dalgalanmanın lambalarda gözle görülen titremesi.

### Ada koruması ile OTK'nın çakışması

**Anti-islanding** (ada önleme), eviricinin şebeke gidince adayı fark edip kapanmasıdır. Yöntemleri: aktif frekans kaydırma, gerilim-frekans penceresi.

- **Aktif frekans kaydırma:** evirici frekansı bilerek hafifçe iter; şebeke varsa bu itme tutmaz, yoksa frekans kayar ve evirici adayı anlar.
- **Gerilim-frekans penceresi:** gerilim veya frekans belirli bir aralığın dışına çıkınca evirici kapanır.

Anti-islanding ile **otomatik tekrar kapama** (OTK) çakışır. OTK, arızadan sonra kesiciyi kısa bir süre sonra otomatik olarak yeniden kapatan işlevdir.

Kapama ölü devreye olmazsa, senkron olmayan iki kaynağı üst üste bindirir. Yani ada hâlâ canlıysa ve frekansı şebekeyle aynı değilse, kesici kapandığı an iki farklı fazdaki gerilim çarpışır.

### Barındırma kapasitesi

**Barındırma kapasitesi**, seçilen limitler bozulmadan fidere bağlanabilecek üretimdir.

Tek sayı değildir. Her limit ayrı bir kapasite verir:

- gerilim,
- termik,
- koruma,
- ters akış,
- güç kalitesi.

Bunlardan **en küçüğü** ilan edilir. **Termik limit**, iletkenin aşırı ısınmadan taşıyabileceği en yüksek akımdır.

Konum önemlidir. Trafo yanında 5 MW ile fider ucunda 5 MW aynı sonucu vermez. Fider ucu zayıf olduğu için aynı üretim orada gerilimi çok daha fazla yükseltir.

Yazılım işi tam olarak budur: her düğüm için kapasite eğrisi.

## 4. Koruma ve otomasyon

### Radyal fiderde koordinasyon

Radyal fiderde **zaman kademeli aşırı akım** koruması kullanılır: kaynak tarafı daha yavaş, uç daha hızlı açar. Böylece arızaya en yakın cihaz önce açar, fiderin geri kalanı enerjili kalır.

Sigorta, röle ve otomatik tekrar kapama (OTK) birlikte koordinedir.

- OTK geçici arızayı (dal, kuş) kapatır; yani kısa kesintiden sonra hattı geri verir.
- Kalıcı arızada kilitler; yani birkaç denemeden sonra açık kalır.

Dağıtık üretim varsa, OTK'nın **ölü zamanında** (açık kaldığı kısa süre) adanın sönmüş olması gerekir.

### Halka kapanırsa

Halka kapanacaksa yönlü röle veya diferansiyel gerekir. Yönsüz aşırı akım, kapalı halkada seçiciliği kaybeder.

- **Yönlü röle:** akımın hangi yönde aktığına bakarak açar.
- **Diferansiyel koruma:** bir bölgeye giren ve çıkan akımı karşılaştırır; fark varsa arıza içeridedir.
- **Seçicilik:** yalnızca arızalı kısmın açılması.

Kapalı halkada akım iki yönden gelir; yön bilmeyen röle hangi tarafın arızaya yakın olduğunu ayırt edemez.

### FLISR ve OMS

**FLISR** (Fault Location, Isolation and Service Restoration; arıza tespiti, izolasyon, hizmet iadesi), dağıtım otomasyonunun işletme değeridir. Arızayı bulur, ayırır, sağlam kısma enerjiyi geri verir.

**OMS** (Outage Management System, Kesinti Yönetim Sistemi), kesintiyi müşteriye ve regülasyona raporlar.

### SAIDI ve SAIFI

| Endeks | Açılımı | Ne ölçer |
|---|---|---|
| **SAIDI** | System Average Interruption Duration Index, Sistem Ortalama Kesinti Süresi Endeksi | Süre |
| **SAIFI** | System Average Interruption Frequency Index, Sistem Ortalama Kesinti Sıklığı Endeksi | Sıklık |

CIGRE (Conseil International des Grands Réseaux Électriques, Uluslararası Büyük Elektrik Sistemleri Konseyi) 2026 Türkiye özetindeki dağıtım değerleri, planlı kesinti hariç ve dahil olmak üzere ayrı raporlanır.

Rakamı ezberlemekten çok, planlı ile plansızın karıştırılmaması gerekir. **Planlı kesinti**, bakım gibi önceden duyurulan kesintidir.

2025 özetinde geçen değerler:

| | SAIDI | SAIFI |
|---|---|---|
| Planlı dahil | 1,820 | 21,17 |
| Planlı hariç | 1,099 | 17,8 |

Birim dakikadır. Güncel hedef EPDK (Enerji Piyasası Düzenleme Kurumu) kalite göstergesindedir.

Not: SAIDI değerleri kaynakta "1,820" ve "1,099" diye yazılmış ve birimi dakika verilmiş. Türkçede virgül ondalık ayırıcıdır; bu yazımla "1,8 dakika" okunur. İngilizce yazımda ise virgül binlik ayırıcıdır ve "1.820 dakika" anlamına gelir. Kullanmadan önce kaynaktan hangisi olduğunu teyit et.

Hesabı ve formülleri [`02-VoltVAR-Yeniden-Yapilandirma-Guvenilirlik.md`](02-VoltVAR-Yeniden-Yapilandirma-Guvenilirlik.md) sayfasında bulacaksın.

## 5. Sistemler

Dağıtım şirketinin yazılım sistemleri:

| Sistem | Açılımı | Ne yapar |
|---|---|---|
| **GIS** | Geographic Information System, Coğrafi Bilgi Sistemi | Coğrafi ve elektriksel varlık kaydı. Hatalı GIS, hatalı yük akışı demektir. Faz bağlantısı yanlışsa dengesiz analiz anlamsızdır. |
| **SCADA** | Supervisory Control and Data Acquisition, Denetleyici Kontrol ve Veri Toplama | İzlenen anahtarlar ve gerilimler. Dağıtımda her ayırıcı izlenmez. |
| **DMS** | Distribution Management System, Dağıtım Yönetim Sistemi | Yük akışı, anahtarlama planı, gerilim kontrolü, arıza yeri. |
| **AMI** | Advanced Metering Infrastructure, Gelişmiş Sayaç Altyapısı | Akıllı sayaç. Gerilim ve enerjiyi saatlik veya daha sık getirir. Durum kestiriminin yeni ölçüm kaynağıdır. |

**Ayırıcı**, hattı yüksüzken açıp kapatan, görünür bir açıklık sağlayan anahtardır.

### Kimlik eşleme sorunu

**GIS + AMI + SCADA** aynı barayı farklı isimle tutuyorsa, yazılım projesi ölçümden önce **kimlik eşlemeyle** boğulur. Yani önce "bu üç sistemdeki üç farklı kayıt aynı nokta mı?" sorusu çözülmelidir.

> **Mülakatta şöyle söyle:** Bunu söylemen, "yazılım projesinde çalıştım" cümlesini inandırıcı kılar.

## 6. Planlama

### Dağıtım planlama kararları

Dağıtım planı, iletim **master planından** (uzun vadeli ana plan) daha kısa adımlıdır ve coğrafyaya yapışıktır:

- parsel,
- kanal,
- direk,
- müşteri büyümesi.

Tipik kararlar:

- yeni fider,
- kesit artırımı (daha kalın iletken),
- yeni dağıtım trafosu,
- yeni TM (trafo merkezi) çıkışı,
- iletim bağlantı geriliminin 154 kV mi 34,5 kV mi olacağı.

Elektrikli araç kümelenmesi bir sokağı, bir iletim hattından önce doldurur.

Depolama, hem gerilim hem **puant tıraşlama** (en yüksek tüketim anını bataryadan karşılayıp tepeyi düşürme) için bir fider varlığıdır.

Ama **enerji arbitrajı** (ucuzken şarj edip pahalıyken satmak) ile şebeke hizmeti aynı bataryada çakışabilir. Bu yüzden kontrol önceliği yazılır: hangi durumda hangisi önce gelir, açıkça belirlenir.

### Dağıtım durum kestirimi

**Durum kestirimi**, eldeki ölçümlerden şebekenin o anki gerilim ve açılarını en olası şekilde tahmin etmektir.

Dağıtım durum kestirimi iletim kestiriminin küçüğü değildir:

- Ölçüm azdır.
- **Pseudo-ölçüm** (sözde ölçüm; ölçülmeyen yer için tahminî yük) çoktur.
- Faz bilgisi kirlidir.
- Topoloji (şebekenin bağlantı şekli) belirsizdir.

**Ağırlıklı en küçük kareler** (WLS, Weighted Least Squares) yine kullanılır. Bu yöntem, güvenilir ölçüme büyük, güvensiz ölçüme küçük ağırlık vererek en uygun çözümü bulur.

Asıl mesele iki şeydir: **gözlenebilirlik** (eldeki ölçümlerin şebekeyi çözmeye yetip yetmediği) ve pseudo-ölçümün ağırlığı.

Ayrıntı `09` klasöründe ([`../09-Durum-Kestirimi/`](../09-Durum-Kestirimi/00-Alt-Basliklar.md)) ve [`03-Dagitim-Durum-Kestirimi-AMI-DERMS-EV.md`](03-Dagitim-Durum-Kestirimi-AMI-DERMS-EV.md) sayfasında.

### 90 saniyelik metin için not

Aşağıdaki metin sayfanın kısa sözlü özetidir. İçindeki kısaltmalar yukarıda açıldı: R/X (Bölüm 1), OTK (Bölüm 3 ve 4), GIS ve SCADA (Bölüm 5). "PR+QX", Bölüm 2'deki gerilim düşümü formülünün payıdır.

## 90 saniye

“Dağıtım radyal, R/X yüksek ve dengesiz. Gerilim düşümü PR+QX ile gider. Çatı güneşi ters akış ve gerilim yükseltmesi yaratır; barındırma kapasitesi düğüme ve limite göre değişir. Eviricinin kısa devre katkısı senkron makine gibi değildir, OTK ile ada koruması birlikte düşünülür. Yazılım tarafında GIS, SCADA ve sayaç kimliği birleşmeden yük akışı güvenilmez.”

## Kendini yokla

Önce cevabı kapat, kendin söyle, sonra kontrol et.

1. **Dağıtım neden radyal işletilir?**
   Arıza bölgesi küçük kalsın, koruma basit kalsın diye. Halka varsa bile açık nokta bırakılır.

2. **Çatı güneşi gerilimi neden yükseltir, kapasitör neden çözüm değildir?**
   Dağıtımda R/X yüksektir; aktif güç enjeksiyonu gerilimi yükseltir. Kapasitör reaktif üretip problemi büyütebilir.

3. **Radyal fiderde yaklaşık gerilim düşümü formülü nedir?**
   ΔV ≈ (P R + Q X) / V.

4. **Teknik ve ticari kayıp nasıl ayrılır?**
   Teknik kayıp (I²R, trafo bakır ve boşta demir, korona, bağlantı direnci) yük akışıyla hesaplanır. Ticari kayıp (kaçak, ölçüm hatası) enerji bilançosu ile teknik kayıp farkından tahmin edilir.

5. **Eviricinin kısa devre katkısı senkron makineden nasıl farklıdır?**
   Senkron makine 6–10 kat verir. Evirici çoğunlukla 1,1–1,5 kat nominal akım civarında sınırlanır ve hızla kesilir.

6. **Gerilim yükselmesinde en kötü durum nedir?**
   Minimum yük, maksimum üretim.

7. **Barındırma kapasitesi neden tek sayı değildir?**
   Gerilim, termik, koruma, ters akış ve güç kalitesi ayrı kapasite verir; en küçüğü ilan edilir. Konum da önemlidir: trafo yanında 5 MW ile fider ucunda 5 MW aynı değildir.

8. **OTK ile ada koruması neden çakışır?**
   Ada canlı kalırsa, ölü devreye olmayan kapama senkron olmayan iki kaynağı üst üste bindirir. OTK'nın ölü zamanında adanın sönmüş olması gerekir.

9. **Kapalı halkada neden yönsüz aşırı akım yetmez?**
   Seçiciliği kaybeder; yönlü röle veya diferansiyel gerekir.

10. **2025 özetinde SAIDI ve SAIFI değerleri nedir?**
    Planlı dahil SAIDI 1,820 ve SAIFI 21,17; planlı hariç SAIDI 1,099 ve SAIFI 17,8. Birim dakika. Planlı ile plansızı karıştırma.

11. **GIS, SCADA, DMS ve AMI ne yapar?**
    GIS varlık kaydı, SCADA izleme ve kumanda, DMS yük akışı/anahtarlama/gerilim kontrolü/arıza yeri, AMI akıllı sayaç verisi.

12. **Dağıtım durum kestiriminde asıl mesele nedir?**
    Ağırlıklı en küçük kareler yine kullanılır; asıl mesele gözlenebilirlik ve pseudo-ölçümün ağırlığıdır.
