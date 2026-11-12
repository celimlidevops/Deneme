# Teknik sorular ve kısa cevaplar

Bu sayfa, teknik mülakatta sık gelen soruların sesli söylenecek cevaplarını toplar. Sorular konu başlıklarına göre gruplanmıştır.

Nasıl kullanılır:

- Her cevabı 60–90 saniyede söyle.
- “Derinleşirlerse” satırı ikinci tur içindir. Panel aynı konuda ikinci bir soru sorarsa onu kullanırsın.
- Cevabın içinde geçen kısaltmalar, ilk geçtikleri yerde parantez içinde açılmıştır. Sesli cevapta kısaltmayı söylemen yeterlidir; açılımı senin anlaman içindir.

## Temel

**Aktif ve reaktif güç işletmede neyi bozar?**

Aktif güç (P, gerçekten iş yapan güç) dengesi açıyı ve frekansı belirler. Reaktif güç (Q, alanlar arasında gidip gelen güç) dengesi gerilimi belirler.

İletimde X (reaktans) baskın olduğu için bu ayrışır: P açıya, Q gerilime bağlı kalır.

Dağıtımda R (direnç) büyüyünce aktif güç de gerilimi kaydırır. Çatı güneşi öğlen gerilimi böyle yükseltir: öğlen üretilen aktif güç, R üzerinden gerilimi yukarı iter.

Derinleşirlerse: `P = V_s V_r / X sin δ`. Burada `V_s` gönderen uç gerilimi, `V_r` alan uç gerilimi, `δ` iki uç arasındaki açı farkıdır. Küçük açıda `Q` gerilim farkıyla gider. Dağıtımda `ΔV ≈ (PR + QX) / V` olur; formülde PR terimi, dağıtımda P'nin de gerilim düşümüne katıldığını gösterir.

**Per-unit neden?**

Per-unit (pu, birim değer), her büyüklüğü seçilmiş bir taban (baz) değere bölerek boyutsuz yazma yöntemidir.

Neden kullanılır:

- Farklı gerilim bölgeleri aynı matriste buluşsun diye.
- Trafo oranı baz seçimine gömülsün diye. Doğru baz seçilince trafo, devrede oran olarak ayrıca görünmez.

Kural: tek S baz (tüm sistem için bir güç tabanı), bölge başına V baz (her gerilim bölgesi için ayrı gerilim tabanı).

Empedans `Z_pu = Z * S_baz / V_baz²` ile taşınır. Trafo plaka değeri çevrilmeden Ybus’a (bara admitans matrisi) girmez; önce sistem bazına dönüştürülür.

**Tek faz-toprak arızada diziler nasıl bağlanır?**

Simetrili bileşenler yönteminde dengesiz arıza; artı (pozitif), eksi (negatif) ve sıfır dizi devrelerine ayrılır.

Tek faz-toprak arızada artı, eksi ve sıfır dizi devreleri arıza noktasında seri bağlanır.

Akım: `3 V / (Z1+Z2+Z0+3Zf)`. Burada Z1, Z2, Z0 sırasıyla artı, eksi ve sıfır dizi empedansı; Zf arıza empedansıdır.

Sıfır diziyi trafo grubu (sargıların yıldız/üçgen bağlanışı) ve topraklama belirler. Üçgen sargı sıfır diziyi geçirmez.

**Hattın kapasitesi neden tek sayı değil?**

Bir hattın taşıyabileceği gücü üç ayrı sınır belirler:

| Sınır | Neye bakar |
| --- | --- |
| Termik sınır | İletken sıcaklığı |
| Gerilim sınırı | Gerilim profili |
| Kararlılık sınırı | Açı ve salınım |

Kısa hat termiğe, uzun hat kararlılığa takılır. Yüzde yükün hangi limite göre olduğunu söylerim.

## İletim ve dağıtım

**Türkiye iletim gerilimleri ve planlama bandı?**

Nominal (anma) gerilimler 400, 154 ve 66 kV'tur.

Arıza öncesi planlama bandı:

| Nominal | Planlama bandı |
| --- | --- |
| 400 kV | 370–420 kV |
| 154 kV | 146–162 kV; kısıtlı bölgede 140–170 kV kabulü |
| 66 kV | 62–70 kV |

Normal işletme bandı daha geniştir:

| Nominal | Normal işletme bandı |
| --- | --- |
| 400 kV | 340–420 kV |
| 154 kV | 140–170 kV |

Planlama yükü puantın (en yüksek yükün) yüzde 5 üzeridir.

**ENTSO-E bağlantısı neyi değiştirir?**

ENTSO-E (European Network of Transmission System Operators for Electricity), Avrupa iletim sistemi işletmecilerinin birliğidir.

Türkiye, Yunanistan ve Bulgaristan üzerinden Kıta Avrupası ile senkron çalışır. Senkron demek, aynı frekansta, tek bir sistem gibi dönmek demektir.

Bunun sonuçları:

- Frekans ve primer rezerv paylaşılır.
- Bölgeler arası salınım PSS (Power System Stabilizer, güç sistemi dengeleyicisi) ile sönümlenir.

Gürcistan tarafı back-to-back HVDC’dir (High Voltage Direct Current, yüksek gerilim doğru akım; iki ucu aynı tesiste olan doğru akım bağlantısı). Aynı senkron ada değildir.

**FACTS cihazını nasıl seçersin?**

FACTS (Flexible AC Transmission Systems), güç elektroniğiyle akışı ve gerilimi denetleyen esnek alternatif akım iletim cihazlarıdır. Seçim, çözülecek soruna göre yapılır:

| İhtiyaç | Cihaz |
| --- | --- |
| Gerilim ve dinamik reaktif | SVC (Static Var Compensator, statik reaktif güç kompanzatörü) veya STATCOM (Static Synchronous Compensator, statik senkron kompanzatör) |
| Hat akışını kaydırmak | Seri cihaz: TCSC (Thyristor Controlled Series Capacitor, tristör kontrollü seri kondansatör) veya SSSC (Static Synchronous Series Compensator, statik senkron seri kompanzatör) |
| P ve Q birlikte | UPFC (Unified Power Flow Controller, birleşik güç akışı denetleyicisi) |

Zayıf gerilimde STATCOM, ürettiği reaktifi daha iyi tutar.

Milisaniye kontrol için EMT (ElectroMagnetic Transient, elektromanyetik geçici) veya RMS (Root Mean Square, etkin değer) kontrol modeli gerekir. Statik PV modeli (cihazı sabit P ve gerilimli bara gibi gösteren model) yetmez.

**Dağıtım yük akışı iletimden neden ayrılır?**

Dağıtım şebekesinin dört özelliği farklıdır:

- Radyaldir (ağaç yapısında, tek yönden beslenir).
- R/X oranı yüksektir.
- Dengesizdir (fazlar eşit yüklü değildir).
- Ölçü eksiktir.

Bu yüzden geri-ileri süpürme veya üç faz model gerekir. Dengeli DC (doğru akım yaklaşımlı) tarama fider ucu gerilimini gizler.

**Barındırma kapasitesi nedir?**

Barındırma kapasitesi, limitler bozulmadan o düğüme bağlanabilecek üretimdir.

Gerilim, termik, koruma ve ters akış ayrı kapasite verir; en küçüğü geçerlidir.

Trafo yanı ile fider ucu aynı MW’yi taşımaz. En kötü saat, minimum yük ve maksimum üretimin aynı anda olduğu saattir.

## Yük akışı

**Bara tipleri?**

| Tip | Bilinen | Bilinmeyen |
| --- | --- | --- |
| PQ | Güç (P ve Q) | Gerilim ve açı |
| PV | P ve gerilim | Q ve açı |
| Slack (salınım barası) | Gerilim ve açı | Kayıp ve dengeyi toplar |

Slack bir santral değildir; hesabın denge noktasıdır.

PV bara, Q limitine çarpınca PQ olur. Bu dönüşüm yoksa gerilim sahte düzelir.

**Newton-Raphson’da Jacobian ne işe yarar?**

Jacobian, güç artığını (hesaplanan ile istenen güç arasındaki farkı) gerilim düzeltmesine çeviren türev matrisidir.

Bloklar H N M L'dir: P ve Q’nun açıya ve gerilime türevleri.

Seyrek lineer sistem çözülür, yoğun ters alınmaz. İletimde 3–6 iterasyon tipiktir.

Iraksamanın olası nedenleri: ada, veri hatası, kontrol salınımı veya burun noktası (gerilim çökmesinin eşiği).

**DC yük akışı nerede meşru, nerede değil?**

DC yük akışı varsayımları: açı küçük, gerilim yaklaşık 1 pu, kayıp ve reaktif ihmal.

| Meşru | Meşru değil |
| --- | --- |
| Termik N-1 eleği | Gerilim ihlali |
| PTDF (Power Transfer Distribution Factor, güç aktarım dağılım çarpanı) | Dağıtım |
| | Ağır yük |

Elekten geçen durum AC (alternatif akım, tam) yük akışıyla doğrulanır.

**Yük akışı ıraksadı, ilk bakacağın üç şey?**

1. Ada ve kesici topolojisi.
2. Sıfır empedans veya yanlış baz.
3. Q limiti ve kademe salınımı.

Veri sağlamsa yükü ölçekleyip burun noktasına bakılır. Çözücüyü değiştirmek ilk adım değildir.

## Kısa devre

**En büyük arıza her zaman üç faz mıdır?**

Hayır. Katı topraklı şebekede tek faz-toprak arıza, Z0 küçükse üç fazı geçebilir.

Ekipman için azami, röle için asgari hesabı ayrı koşarım. IEC 60909 (International Electrotechnical Commission'ın kısa devre hesap standardı) gerilim katsayısı kullanır.

**X'', X' ve Xd neden karışmaz?**

Senkron makinenin üç reaktansı üç ayrı zaman dilimine aittir:

| Reaktans | Adı | Nerede kullanılır |
| --- | --- | --- |
| X'' | Alt geçici reaktans | Kesici ve ilk tepe |
| X' | Geçici reaktans | Kararlılık modeli |
| Xd | Senkron reaktans | Sürekli hal |

X/R oranı, DC bileşenin sönümünü ve tepe çarpanını belirler.

**Evirici kısa devreye ne katkı verir?**

Takip eden evirici (şebekeyi izleyerek akım basan evirici), akımını kontrolle sınırlar. Senkron makinenin katları gibi beslemez.

Koruma görme ve yön bundan bozulur. Şebeke oluşturan kontrol (gerilimi kendisi kuran evirici) ayrı senaryodur. Üretici modeli olmadan sayı vermem.

## Güvenlik

**N-1’i yönetmelik diline yakın söyle.**

N-1, tek bir elemanın devre dışı kalmasına karşı güvenlik ölçütüdür. Tek eleman devre dışıyken:

- termik limit aşılmaz,
- gerilim ve frekans bandında kalır,
- kararlılık bozulmaz,
- kullanıcı kaybedilmez,
- sistem adalara bölünmez.

Nükleer bağlantıda N-2 aranır. Ortak direkte çift devre bağımsız iki arıza değildir.

**Güvenlik ile kararlılık?**

Güvenlik, arıza sonrası limit içinde kalmaktır. Kararlılık, yeni dengeye oturmaktır.

Termik olarak güvenli bir durum, açı olarak kararsız olabilir. İkisi ayrı hesaptır, aynı işletme kararında buluşur.

**Binlerce arızayı nasıl tararsın?**

Katmanlı bir eleme yaparım:

1. Aday liste.
2. DC ve LODF (Line Outage Distribution Factor, hat açma dağılım çarpanı) eleği.
3. Performans indeksiyle sıra.
4. Şüphelide AC.
5. Büyük üretim ve zayıf koridorda dinamik.

YTBS (Yük Tevzi Bilgi Sistemi) ölçeğindeki arıza simülasyonu bu katmandır. Her arızaya EMT koşmam.

**Önleyici ve düzeltici?**

| Tür | Ne yapar |
| --- | --- |
| Önleyici | Arızadan önce üretimi kaydırır, maliyeti hemen öder |
| Düzeltici | Arızadan sonra kaydırır veya yük atar |

SIPS (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması) düzeltici ve otomatiktir. Acil termik limit, operatöre süre tanır.

## Kararlılık

**Salınım denklemi ne söyler?**

`(2H/ω0) δ'' = Pm - Pe`. Burada H atalet sabiti, ω0 nominal açısal hız, δ'' rotor açısının ikinci türevi, Pm mekanik güç, Pe elektriksel güçtür.

Açık güç (Pm ile Pe arasındaki fark) açıyı hızlandırır.

Eşit alan ölçütü: hızlanma alanı yavaşlama alanından küçükse açı yakalanır. Kritik temizleme süresi koruma süresinden büyük olmalıdır.

**PSS neyi söndürür?**

Küçük sinyal salınımını söndürür.

PSS, hız veya güç sapmasını AVR (Automatic Voltage Regulator, otomatik gerilim regülatörü) referansına ekler.

- Yerel mod yaklaşık 1 Hz'dir.
- Bölgeler arası mod daha yavaştır.

Yönetmelik, büyük konvansiyonel ünitelerde 0–5 Hz ve ENTSO-E bölgeler arası mod için PSS arar. Kötü kazanç sönümü azaltır.

**Gerilim neden dakikalar sonra çöker?**

Zincir şöyle işler:

1. Hat açılır.
2. Gerilim düşer.
3. Yük toparlar.
4. OLTC (On-Load Tap Changer, yük altında kademe değiştirici) gerilimi kaldırmak için iletimden daha çok reaktif çeker.

Beş saniyelik kısa devre simülasyonu bunu görmez. PV eğrisinin (güç–gerilim eğrisi) burnu statik marjdır.

**RoCoF ve atalet?**

RoCoF (Rate of Change of Frequency), frekansın değişim hızıdır.

`RoCoF ≈ (ΔP/S) f0 / (2H)`. Burada ΔP kaybedilen güç, S sistem gücü, f0 nominal frekans, H atalet sabitidir.

H düşünce aynı ünite kaybı daha dik frekans düşüşü yapar. Takip eden evirici doğal H katmaz.

YTBS atalet hesabı bu envanterdir. Düşük frekans rölesi son çaredir; kademeleri TEİAŞ (Türkiye Elektrik İletim A.Ş.) yıllık belirler.

**Primer, sekonder, tersiyer?**

| Kontrol | Nasıl çalışır | Süre / eşik |
| --- | --- | --- |
| Primer | Hız regülatörü | 200 mHz tanımında 30 saniye |
| Sekonder | AGC (Automatic Generation Control, otomatik üretim kontrolü); frekansı 50 Hz’e ve sınır programına çeker | Normal bant 49,8–50,2 Hz |
| Tersiyer | Dengeleme piyasasında | 15 dakika |

LFSM (Limited Frequency Sensitive Mode, sınırlı frekans duyarlı mod) eşikleri 49,8 ve 50,2 Hz’dir.

## Durum kestirimi

**SCADA yetmez mi?**

SCADA (Supervisory Control and Data Acquisition, uzaktan izleme ve veri toplama) ölçüsü gürültülü, eksik ve bazen bozuktur. Yük akışı ise gücün doğru bilindiğini varsayar.

Durum kestirimi, fazla ölçüden en olası gerilim ve açıyı çıkarır. Güvenlik analizi ancak sağlam kestirime koşar.

**WLS’yi yaz.**

WLS (Weighted Least Squares), ağırlıklı en küçük kareler yöntemidir. Denklemler:

- Amaç fonksiyonu: `J = (z-h)ᵀ W (z-h)`, `W = R⁻¹`. Burada z ölçüm vektörü, h(x) ölçümlerin durumdan hesaplanan değeri, R ölçüm hata kovaryansıdır.
- Kazanç matrisi ve adım: `G = Hᵀ W H`, `G Δx = Hᵀ W (z-h)`. H ölçüm Jacobian'ıdır.

G tekilse sistem gözlenemez. Referans açı sabitlenmezse de G tekil olur. Pseudo-ölçüm (tahminle doldurulan sahte ölçüm) ağırlığı düşük tutulur.

**Kötü veriyi nasıl bulursun?**

1. Tespit: J, serbestlik derecesi m−n olan ki-kare eşiğini aşarsa sette kötü veri vardır (m ölçüm sayısı, n durum sayısı).
2. Yer bulma: normalize artığı en büyük olan ölçü işaret edilir.

Sınırları:

- Kritik ölçüde test kördür.
- Kaldıraç noktasında artık küçük kalabilir.
- Topoloji hatası ölçü atarak düzelmez.

**PMU neyi değiştirir?**

PMU (Phasor Measurement Unit, fazör ölçüm birimi), senkron fazör ölçer. Bu, durumu lineer ve hızlı tahmin ettirir.

SCADA ile hibrit kullanılır. Dakikalık SCADA, SIPS’in yüz milisaniye penceresine yetişmez.

## Koruma ve topraklama

**Dört nitelik?**

1. Seçicilik.
2. Hız.
3. Duyarlılık.
4. Güvenilirlik.

Güvenilirliğin iki yüzü vardır: gerektiğinde çalışma ve gerekmediğinde susma. Yedek koruma daha yavaş ve daha geniş bölgededir.

**Mesafe bölgelerini tipik değerle, ayar iddiası olmadan söyle.**

| Bölge | Kapsam | Gecikme |
| --- | --- | --- |
| Bölge 1 | Hattın yaklaşık yüzde 80’i | Gecikmesiz |
| Bölge 2 | Hattın tamamı ve karşı ucun bir kısmı | Birkaç yüz milisaniye |
| Bölge 3 | Geniş yedek | — |

Yük istilası ve güç salınımı yanlış açmayı bölge 3’te doğurur. Salınım bloğu, kararlı salınımda açmayı keser. Gerçek ayar şirket standardındadır.

**Diferansiyel neden ayrı?**

Diferansiyel koruma, bölgeye giren ve çıkan akımın farkına bakar. Bu, seçiciliği süreden bağımsız yapar.

CT (Current Transformer, akım trafosu) doyması ve trafo inrush'ı (enerjilendirme anındaki ani mıknatıslanma akımı) yanlış fark üretir. Tutma ve ikinci harmonik bunun içindir.

**Topraklama neden korumayla birlikte?**

Topraklama biçimi, toprak arıza akımını yani sıfır diziyi belirler.

Adım ve dokunma gerilimi arıza temizleme süresine bağlıdır. IEEE 80 (Institute of Electrical and Electronics Engineers'ın trafo merkezi topraklama standardı), süreyi ve toprak özdirencini birlikte kullanır.

Yavaş koruma, izin verilen dokunma gerilimini düşürür.

## Ekonomi ve planlama

**Eşit λ?**

Kayıpsız sistemde optimum, devredeki ünitelerin artan yakıt maliyetinin (bir MW daha üretmenin maliyetinin) eşitlenmesidir. Bu ortak değere λ (lambda) denir.

Limitteki ünite eşitliğin dışındadır.

Kayıp varsa ceza faktörü `1/(1-∂Pkayıp/∂P)` ile çarpılır.

**Ekonomik dağıtım, ünite tahsisi, OPF?**

| Problem | Ne yapar |
| --- | --- |
| Ekonomik dağıtım | Devredeki MW’yi paylaşır |
| Ünite tahsisi | Kimin açık olacağıdır; ikili değişkendir; rampa ve en az açık süre vardır |
| OPF (Optimal Power Flow, optimal güç akışı) | Şebeke limitini ekler |
| SCOPF (Security Constrained OPF, güvenlik kısıtlı OPF) | Bir de N-1 ekler |

**Piyasa ile fizik nerede ayrılır?**

- Gün öncesi ve gün içi piyasa EPİAŞ’tadır (Enerji Piyasaları İşletme A.Ş.).
- Dengeleme, AGC ve kısıt talimatı TEİAŞ’tadır.

Program şebekeye sığmazsa yeniden dağıtım yapılır, ardından N-1 tekrar bakılır.

**LOLE ile N-1?**

LOLE (Loss of Load Expectation), üretim yeterliliğinin beklenen yük kaybı süresidir. N-1 ise iletimin deterministik güvenlik kuralıdır. İkisi aynı göstergenin iki adı değildir.

ELCC (Effective Load Carrying Capability, etkin yük taşıma kapasitesi), rüzgârın isim plakasının tamamını kapasite saymaz.

**Fayda/maliyette gizleme.**

İskonto, talep ve kısıntı fiyatı değişince sıralama değişiyor mu, ona bakarım.

Ada riskini iç verim oranının içine saklamam. Düşük olasılıklı ülkeyi bölen koridoru, sık ama yerel arızayla aynı kefeye koyarım.

## Optimizasyon

**AC-OPF neden “çözdüm” demez?**

AC-OPF (tam AC modelli optimal güç akışı) dışbükey değildir; yerel çözüm vardır.

Yük akışıyla fizibiliteyi, mümkünse bir alt sınırla kaliteyi kontrol ederim. Kademe yuvarlanır, ünite yuvarlanmaz.

**Gölge fiyat?**

Gölge fiyat, bir kısıtın Lagrange çarpanıdır:

- Güç dengesinin çarpanı, o baradaki bir MW’nin fiyatıdır.
- Hat limitinin çarpanı, sıkışıklık maliyetidir.
- Boş kısıtın çarpanı sıfırdır.

**Büyük N-1 optimizasyonu?**

1. Önce baz durumu çöz.
2. İhlal eden arızayı kısıt olarak ekle.
3. Tekrarla.

Benders ayrıştırması aynı fikrin ayrıştırılmış halidir. Tüm arızayı baştan koymak bellek yer.

## Ürün, yazılım, yenilenebilir, veri

**YTBS’yi bir cümleyle.**

TEİAŞ’ın kullandığı, şebekenin ölçümle güncellenen modelinde güvenlik, tahmin ve optimizasyon koşan, SCADA ile web servisle konuşan dijital ikiz platformu. THS 9.

THS, Teknoloji Hazırlık Seviyesi demektir; 9 en üst basamaktır ve ürünün gerçek işletmede kanıtlandığını söyler.

**SIPS ile röle?**

Röle ekipmanı korur.

SIPS, PMU sınıfı geniş alan verisiyle sistem bütünlüğü için üretim veya yük atar. Zincirleme açmayı küçük ve kontrollü kayba çevirmek içindir.

**Dijital ikiz kumanda eder mi?**

Hayır. Senaryo ve karar desteği üretir.

Kumanda yetkisi ve prosedür SCADA tarafında kalır. Kalite bayrağı bozuksa sonuç otomasyona bağlanmaz.

**CIM neden her şeyi çözmez?**

CIM (Common Information Model, ortak bilgi modeli), şebeke verisinin standart veri modelidir.

- Ekipman, topoloji ve analog ayrı profillerdir.
- CGMES (Common Grid Model Exchange Standard, ortak şebeke modeli alışveriş standardı), Avrupa iletim alışverişinin profilidir.
- Koruma çoğu zaman ayrı kalır.

Baz, kademe ve işaret bozulmasını sayı ve seçilmiş akışla doğrularım.

**Öğrenen model kararlılıkta ne yapar?**

Aday arızayı eler ve sıralar. İhlal fizikle doğrulanır.

Yük atma eşiği onaysız değişmez. Yeni hat modeli eskidir: şebekeye yeni hat eklenince, eski veriyle eğitilmiş model artık güncel değildir. Veri azsa derin ağ kurmam.

**Düşük atalette ilk üç önlem?**

1. Atalet envanteri ve RoCoF izleme.
2. Primer ve hızlı frekans desteği olan kaynak veya depolama.
3. RoCoF rölelerinin yanlış açmasını gözden geçirmek.

Sentetik atalet, şebeke oluşturan kontrolün bir ayarıdır. Fiziksel H ile aynı sınıfta söylemem, katkı olarak söylerim.

## İngilizce kısa tur

Bu bölümde cevaplar İngilizce söylenir. Altlarındaki Türkçe not, cevabın ne dediğini anlaman içindir.

**What is state estimation?**

It finds the most likely bus voltages and angles from redundant, noisy measurements by weighted least squares. Bad data is detected with the chi-square test and located with the normalized residual. Contingency analysis runs on that estimate only if the quality flag is healthy.

Türkçe not: Durum kestirimi, fazla ve gürültülü ölçülerden ağırlıklı en küçük kareler ile en olası bara gerilim ve açılarını bulur. Kötü veri ki-kare testiyle tespit edilir, normalize artıkla yeri bulunur. Arıza analizi bu kestirim üzerinde yalnızca kalite bayrağı sağlamsa koşar.

**What does N-1 mean in Turkey?**

After a single outage, thermal, voltage and frequency limits hold, the system stays stable, no customer is lost and the system does not split into islands. The planning case is five percent above peak. Nuclear connection points are planned for N-2.

Türkçe not: Tek bir eleman kaybından sonra termik, gerilim ve frekans limitleri korunur, sistem kararlı kalır, kullanıcı kaybedilmez ve sistem adalara bölünmez. Planlama vakası puantın yüzde 5 üzeridir. Nükleer bağlantı noktaları N-2'ye göre planlanır.

**Why can a DC power flow not replace an AC power flow?**

It ignores voltage, reactive power and losses. It is a fast thermal screen. Critical cases are confirmed with an AC solution, including generator reactive limits.

Türkçe not: DC yük akışı gerilimi, reaktif gücü ve kayıpları yok sayar. Hızlı bir termik elektir. Kritik vakalar, generatör reaktif limitleri dahil AC çözümle doğrulanır.
