# Yenilenebilir, depolama, akıllı şebeke

## Bu konu neden önemli

2025 sonunda kurulu güç artışının büyük kısmı güneş ve rüzgârdır. Kurulu güç, santrallerin etiketinde yazan en yüksek üretim gücünün toplamıdır.

Bu yüzden grubun entegrasyon, uyumluluk, depolama ve akıllı şebeke maddeleri ilanın gövdesindedir. Yani bunlar ilanda kenar süs değil, ana iş tanımının parçasıdır.

“Yenilenebilir iyidir” bir analiz cümlesi değildir. Mülakatta senden beklenen, bu kaynakların şebekeye nasıl davrandığını sayı ve mekanizmayla anlatmandır.

## Evirici

Evirici (inverter), güneş panelinin ya da rüzgâr türbininin ürettiği elektriği şebekenin alternatif akımına (AC, Alternating Current) çeviren güç elektroniği cihazıdır. Güneş ve rüzgâr şebekeye klasik jeneratör gibi doğrudan değil, bu cihaz üzerinden bağlanır.

### Şebekeyi takip eden evirici

Çoğu güneş ve rüzgâr, şebekeyi takip eden (grid-following) eviriciyle bağlanır. Bu evirici şöyle çalışır:

1. Fazörü şebekeden kilitler. Fazör, gerilimin genliğini ve açısını gösteren vektördür. Evirici bu açıyı şebekeden okur ve ona uyar.
2. Akımı bu referansa göre basar. Yani gerilimi kendisi kurmaz; var olan gerilime akım enjekte eder.

Bunun iki sonucu vardır:

- **Doğal atalet yoktur.** Atalet, dönen jeneratör kütlesinin frekans değişimine direnmesidir. Evirici dönen bir kütle taşımadığı için bunu kendiliğinden vermez.
- **Doğal arıza akımı yoktur.** Arıza akımı kontrolcüyle sınırlanır. Çoğu üründe yaklaşık 1,1–1,5 kat nominal civarındadır. Nominal, cihazın anma (etiket) akımıdır.

Dikkat: üretici belgesine bakılmadan arıza akımı için sayı söylenmez.

### Şebeke oluşturan evirici

Şebeke oluşturan (grid-forming) kontrol, gerilim ve frekans kaynağı gibi davranır. Yani şebekeyi takip etmez; gerilimi ve frekansı kendisi kurar.

Şu üç konunun kapısı burasıdır:

- **Ada:** şebekenin bir parçasının ana şebekeden ayrılıp kendi başına beslenmesi.
- **Zayıf şebeke:** kısa devre gücü düşük, gerilimi kolay oynayan şebeke.
- **Sentetik atalet:** eviricinin kontrol yazılımıyla atalete benzer tepki vermesi.

Kontrol modu değişince kararlılık modeli de değişir. “Bütün eviriciler aynıdır” yanlış cevaptır. Önce kontrol modunu sor.

### Arıza boyunca kalma (FRT)

FRT (Fault Ride Through), arıza boyunca bağlı kalma demektir.

Gerilim çökünce hemen ayrılmak, arızayı üretim kaybına çevirir. Kısa süren bir hat arızası, birçok santralin aynı anda ayrılmasıyla büyük bir güç açığına dönüşür.

Yönetmelik, belirli bir gerilim-süre eğrisinin altında bağlı kalmayı ve toparlanmayı ister.

> **Mülakatta şöyle söyle:** Eğrinin sayılarını ezberlemek yerine “FRT eğrisi ve üretici modeli olmadan dinamik çalışma kapanmaz” de. Sayı sorulursa güncel şebeke yönetmeliği ekinin o tarihteki haline bak.

### Reaktif destek

Reaktif güç, gerilimi ayakta tutan güç bileşenidir. Evirici bunu iki durumda verir:

| Durum | Ne verir |
| --- | --- |
| Normal işletme | Güç faktörü bandı içinde reaktif güç |
| Arıza | Ek reaktif akım |

Dağıtımda iki yaygın kontrol vardır:

| Kontrol | Ne yapar |
| --- | --- |
| Volt-var | Gerilime göre reaktif güç ayarlar; dağıtımda gerilim yükselmesini keser |
| Volt-watt | Gerilim çok yükselirse aktif gücü kısar |

İkisi çatışırsa hangisinin önce geleceği ayar meselesidir.

### Frekans desteği: LFSM

LFSM (Limited Frequency Sensitive Mode), sınırlı frekans duyarlı moddur. Frekans belirli eşikleri aşınca santral aktif gücünü değiştirir.

LFSM eşikleri 49,8 ve 50,2 Hz’dir (Hz: hertz, saniyedeki salınım sayısı; Türkiye şebekesinin anma frekansı 50 Hz).

Primer hizmet sözleşmesi olan santral ile sadece bu yükümlülüğü olan santral aynı rezervi vermez. Primer hizmet, frekans sapmasına saniyeler içinde sürekli tepki veren frekans kontrolüdür; LFSM ise yalnızca eşik aşılınca devreye girer.

## Enerji ve kapasite

### Kapasite faktörü ve ELCC

| Kavram | Tanım | Ne anlatır |
| --- | --- | --- |
| Kapasite faktörü | Yıllık enerjinin, tam güçle geçen yıla oranı | Santralin yıl boyunca ortalama ne kadar çalıştığı |
| ELCC (Effective Load Carrying Capability, etkin yük taşıma kapasitesi) | Puant saatine denk gelen güvenilir katkı | Tüketimin en yüksek olduğu saatte santrale ne kadar güvenebileceğin |

Kapasite faktörü rüzgâr ve güneş için birbirinden çok farklıdır ve bölgeye göre değişir.

Öğlen güneşi akşam puantının ELCC’sine az yazar. Puant, tüketimin en yüksek olduğu saattir; akşam puantında güneş batmış olur.

Planlamada isim plakasını (etiket gücünü) toplamak bu yüzden yanlıştır.

### Rampa ve esneklik

Rampa, net yükün hızlı yükselmesi ya da düşmesidir. Net yük, toplam tüketimden yenilenebilir üretimin çıkarılmış halidir.

Güneş batımı ve rüzgâr cephesi, net yükü saat mertebesinde yükseltir.

Esneklik, bu rampayı karşılayacak iki şeydir:

- **MW/dakika:** gücün dakikada ne kadar artırılabildiği (MW: megavat, güç birimi).
- **MWh:** bu artışı ne kadar süre sürdürebilecek enerji (MWh: megavat-saat, enerji birimi).

### Kısıntı

Kısıntı, iletim kısıtı veya asgari üretim (must-run, sistemin güvenliği için çalışmak zorunda olan santraller) yüzünden üretimin bilerek kesilmesidir.

Sıfır kısıntı hedefi, her saatte şebekeyi o üretime göre fazladan inşa etmek demektir. Bu yüzden biraz kısıntı ekonomik olarak normaldir.

Ekonomik kısıntı ile güvenlik kısıntısı ayrı raporlanır.

### Tahmin hatası ve yedek

Tahmin hatası yedek boyutunu belirler. Gün öncesi rüzgâr hatası ile saat öncesi hata aynı rezervi gerektirmez; ufuk kısaldıkça hata küçülür.

YTBS (Yük Tevzi Bilgi Sistemi, MAM’ın enerji yönetim platformu) ve TEİAŞ (Türkiye Elektrik İletim A.Ş.) RİTM hattı (rüzgâr izleme ve tahmin) bu yüzden işletme aracıdır. Ayrıntı `18` içindedir.

## Depolama

Dört sayısı olmadan batarya anlatılmaz:

| Sayı | Birim | Ne söyler |
| --- | --- | --- |
| Güç | MW | Bir anda ne kadar hızlı verebildiği |
| Enerji | MWh | Toplamda ne kadar enerji tuttuğu |
| Süre | saat | Tam güçte kaç saat dayandığı (enerji / güç) |
| Verim | % | Şarj edilen enerjinin ne kadarının geri alındığı |

2 saatlik batarya ile 15 dakikalık batarya farklı hizmettir.

Hizmetler çakışabilir:

- Enerji arbitrajı (ucuz saatte şarj)
- Puant tıraşlama
- Frekans rezervi
- Rampa ve kısıntı emme
- Dağıtımda gerilim ve fider ömrü
- Siyah start ve ada, ancak kontrol ve koruma tasarlanmışsa

Terimler:

- **Arbitraj:** ucuz saatte alıp pahalı saatte satmak.
- **Puant tıraşlama:** en yüksek tüketim anında bataryadan vererek tepeyi kırpmak.
- **Fider:** trafo merkezinden çıkan dağıtım hattı.
- **Siyah start:** tamamen çökmüş şebekeyi dış besleme olmadan yeniden enerjilendirmek.

Aynı MWh iki hizmete aynı anda satılamaz. Optimizasyon, hizmet önceliğini kısıt olarak yazmalıdır.

Pompalı hidro, süreyi saatlerden günlere çıkarır. Yerleşimini coğrafya seçer; batarya gibi her TM’ye (trafo merkezi) konmaz.

## Akıllı şebeke

Abartısız liste:

| Katman | Bileşenler |
| --- | --- |
| Ölçüm | PMU iletimde, AMI dağıtımda, trafo çıkışı sayaçları |
| Kumanda | Uzaktan anahtar, OLTC, kapasitör, evirici ayar noktası |
| İletişim | Fiber, kuranportör, hücresel. Gecikme ve kesinti, koruma şemasının varsayımıdır |
| Yazılım | DMS, OMS, EMS, tahmin, optimizasyon |
| Müşteri | Talep kaydırma, araç şarjı, çatı güneş |

Kısaltmalar:

- **PMU** (Phasor Measurement Unit): fazör ölçüm birimi. Gerilim ve akım fazörünü zaman damgasıyla, saniyede onlarca kez ölçer.
- **AMI** (Advanced Metering Infrastructure): gelişmiş sayaç altyapısı, yani uzaktan okunan akıllı sayaçlar.
- **OLTC** (On-Load Tap Changer): yük altında kademe değiştirici. Trafonun sarım oranını değiştirerek gerilimi ayarlar.
- **Kuranportör:** enerji hattının kendi iletkeni üzerinden haberleşme.
- **DMS** (Distribution Management System): dağıtım yönetim sistemi.
- **OMS** (Outage Management System): kesinti yönetim sistemi.
- **EMS** (Energy Management System): iletimde enerji yönetim sistemi.

Akıllı şebeke yeni bir fizik değildir. Aynı P–δ ve Q–V ilişkisi, daha sık ölçü ve daha küçük kontrol adımıyla işletilir:

- **P–δ:** aktif güç (P) ile iki uç arasındaki gerilim açısı farkı (δ) arasındaki ilişki.
- **Q–V:** reaktif güç (Q) ile gerilim genliği (V) arasındaki ilişki.

Ölçü yoksa “akıllı” algoritma pseudo-ölçüme (gerçek ölçüm yerine tahminle doldurulan değer) yaslanır ve bunu gizlememelidir.

### Mikro şebeke ve ada

| Durum | Ne demek | Ne yapılır |
| --- | --- | --- |
| Mikro şebeke | Bilinçli ada planı | Şebeke oluşturan kaynak, topraklama ve koruma yeniden kurulur |
| Kazara ada | Planlanmamış ayrılma | Anti-islanding (adalanmayı önleme) ile söndürülmesi gerekir |

İkisini aynı kelimeyle anlatma.

Dağıtım rölesi, ada içinde yön değiştiren akışa göre ayarlı değildir. Bu yüzden bilinçli adada koruma yeniden kurulmak zorundadır.

## Güç kalitesi

| Sorun | Nereden gelir |
| --- | --- |
| Harmonik | Evirici anahtarlaması ve doğrusal olmayan yük |
| Fliker | Rüzgâr ve kaynak makinesinin gerilim oynaması |
| Dengesizlik | Tek fazlı bağlanan güneş |

Terimler:

- **Harmonik:** 50 Hz’in tam katlarındaki istenmeyen bileşenler; dalga biçimini bozar.
- **Fliker:** gerilimdeki hızlı, tekrarlı oynamalar; lambada titreme olarak görülür.
- **Dengesizlik:** üç fazın gerilimlerinin eşit olmaması.

Yönetmelikte gerilim dengesizliği için negatif bileşen oranları vardır. Negatif bileşen, dengesizliği ölçen simetrili bileşendir; oranı ne kadar büyükse fazlar o kadar dengesizdir.

Normal işletmede, ölçümün %95’inde:

| Gerilim seviyesi (kV: kilovolt) | Sınır |
| --- | --- |
| 400 kV | %1 |
| 154 kV | %1,5 |
| Altı | %2 mertebesi |

TEİAŞ onayıyla belirli beslemelerde biraz daha yüksek olabilir.

Sayıyı okurken “yüzde 95, 10 dakikalık ortalama” koşulunu düşürme. Anlık bir örneklem ihlal değildir.

## Model seçimi

Soruyu önce süre ölçeğine koy, sonra modeli seç:

| Soru | Model |
| --- | --- |
| Yıllık enerji ve barındırma | Statik yük akışı zaman serisi |
| N-1 termik | AC veya DC elek |
| FRT ve kontrol | RMS, kontrol bloğuyla |
| Adım değişimi, harmonik, ada geçişi | EMT |

Terimler:

- **Barındırma:** bir fiderin sınır bozmadan kaldırabileceği üretim.
- **N-1:** herhangi bir tek elemanın (hat, trafo) devre dışı kaldığı durum. N-1 termik, bu durumda hatların ısıl sınırının aşılıp aşılmadığıdır.
- **AC veya DC elek:** AC tam yük akışı ya da DC (Direct Current) yaklaşık yük akışı.
- **RMS** (Root Mean Square): etkin değer tabanlı fazör benzetimi; saniyeler mertebesindeki elektromekanik olaylar için.
- **EMT** (Electromagnetic Transient): elektromanyetik geçici hal benzetimi; milisaniye altı dalga biçimi olayları için.

Üçünü bir vakada aynı anda koşmak çoğu projede gereksizdir.

> **Sade anlatım:** Yıllık soru için hızlı ve kaba model, saniyelik soru için RMS, milisaniyelik soru için EMT. Ne kadar kısa olay, o kadar ayrıntılı ve yavaş model.

Aşağıdaki metin mülakatta 90 saniyede söyleyebileceğin özettir.

## 90 saniye

“Yenilenebilirde önce eviricinin takip mi oluşturan mı olduğunu sorarım. Takip eden doğal atalet ve büyük arıza akımı vermez; FRT eğrisiyle bağlı kalır. Kurulu güç ile ELCC ayrıdır, net yük rampası planlamanın yeni puantıdır. Depolamada MW, MWh ve hizmet önceliği yazılır. Akıllı şebeke yeni fizik değil, daha sık ölçü ve daha küçük kontrol adımıdır. Kazara ada ile bilinçli mikro şebeke ayrı tasarımdır.”
