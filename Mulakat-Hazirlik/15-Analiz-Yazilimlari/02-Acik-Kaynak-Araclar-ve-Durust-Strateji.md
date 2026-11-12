# Açık kaynak araçlar ve dürüst strateji

Bu sayfanın tam başlığı: Açık kaynak araçlar ve "ticari yazılım kullanmadım" demenin doğru yolu.

İlandaki madde: "Güç sistemleri analiz yazılımları ile çalışma yapmış olmak."

Büyük ihtimalle PowerFactory, PSS/E gibi ticari paketleri kullanmadın. PSS/E, Siemens'in Power System Simulator for Engineering paketidir.

Bu sayfanın iki işi var:

1. Açık kaynak araçları tanıtmak.
2. Bu eksiği mülakatta dürüstçe, puan kaybını en aza indirerek söylemeni sağlamak.

## Beş açık kaynak araç: hangisi ne için

Tablodan önce birkaç kısaltma:

- **OPF:** Optimal Power Flow (optimal güç akışı). Maliyet gibi bir hedefi en iyileyen yük akışıdır.
- **IEC 60909:** IEC (International Electrotechnical Commission, Uluslararası Elektroteknik Komisyonu) kısa devre akımı hesap standardıdır.
- **Durum kestirimi:** Hatalı ve eksik ölçümlerden şebekenin en olası durumunu hesaplamaktır.
- **pandas:** Python'un tablo işleme kütüphanesidir.
- **`mpc`:** MATPOWER case, yani MATPOWER'ın vaka yapısıdır.
- **Octave:** MATLAB'ın ücretsiz, büyük ölçüde uyumlu karşılığıdır.

| Araç | Dil | Güçlü olduğu yer | Zayıf olduğu yer |
| --- | --- | --- | --- |
| **pandapower** | Python | Dengeli yük akışı, IEC 60909 kısa devre, OPF, durum kestirimi; tablo (pandas) tabanlı veri modeli; hazır eleman kütüphanesi | Dinamik benzetim yok; dengesiz analiz sınırlı |
| **MATPOWER** | MATLAB / Octave | Yük akışı ve OPF için akademik referans; IEEE test vakaları; `mpc` vaka biçimi fiilî standart | Yalnız sürekli hal; MATLAB bağımlılığı |
| **OpenDSS** | Kendi betik dili; Python arayüzleri | **Dağıtım**: dengesiz çok fazlı yük akışı, zaman serisi (yıllık 8760 saat), dağıtık üretim, harmonik | İletim için tasarlanmadı; veri modeli betik tabanlı |
| **PyPSA** | Python | **Planlama ve enerji sistemi**: çok dönemli doğrusal OPF, yatırım eniyilemesi, depolama, sektör birleştirme | Ayrıntılı şebeke analizi (kısa devre, koruma) yok |
| **GridLAB-D** | Kendi model dili | Dağıtım + **son kullanıcı**: ev, cihaz, termostat düzeyinde ajan tabanlı zaman benzetimi; talep tepkisi | Öğrenmesi zor; iletim yok |

Tablodaki bazı terimler:

- **IEEE test vakaları:** IEEE (Institute of Electrical and Electronics Engineers) tarafından yayımlanan, herkesin kullandığı örnek şebekelerdir.
- **8760 saat:** Bir yıldaki saat sayısıdır (365 × 24).
- **Sektör birleştirme:** Elektrik, ısı ve ulaşım gibi enerji sektörlerinin aynı modelde birlikte ele alınmasıdır.
- **Ajan tabanlı:** Her ev veya cihaz kendi kuralıyla davranan ayrı bir nesne olarak benzetilir.
- **Talep tepkisi:** Tüketicinin fiyata veya sinyale göre tüketimini kaydırmasıdır.

Seçim kuralı, tek cümleyle:

| İhtiyaç | Araç |
| --- | --- |
| İletimde yük akışı, kısa devre, hızlı prototip | **pandapower** |
| Bir OPF yöntemini literatürle kıyaslamak | **MATPOWER** (Julia'da PowerModels.jl) |
| Dağıtım fideri, çatı güneşi, barındırma kapasitesi, dengesizlik | **OpenDSS** |
| On yıllık yatırım planı, yenilenebilir ve depolama senaryosu | **PyPSA** |
| Akıllı sayaç, talep tepkisi, cihaz düzeyinde davranış | **GridLAB-D** |

Barındırma kapasitesi, bir dağıtım fiderinin sınır aşmadan kabul edebileceği en fazla dağıtık üretim miktarıdır.

### Dinamik benzetim için açık kaynak

Dinamik benzetim (geçici hal kararlılığı) için açık kaynak seçenekler daha azdır:

| Araç | Dil veya kaynak |
| --- | --- |
| ANDES | Python |
| PowerSimulations ve PowerSimulationsDynamics | Julia |
| Dynawo | RTE |

RTE, Réseau de Transport d'Électricité, yani Fransa'nın iletim sistemi işletmecisidir.

Sorulursa adlarını bilmen yeter.

## Ticari paketler: ne olduklarını bil

| Paket | Üretici | Tipik kullanım |
| --- | --- | --- |
| PowerFactory | DIgSILENT | Avrupa ve Türkiye'de yaygın; iletim, dağıtım, dinamik, koruma tek pakette |
| PSS/E | Siemens | İletim planlaması ve dinamik; Kuzey Amerika'da standart |
| ETAP | ETAP | Endüstriyel tesis, koruma koordinasyonu, ark parlaması |
| PSCAD, EMTP | Manitoba Hydro, EMTP Alliance | Elektromanyetik geçici hal; evirici, HVDC, yıldırım |
| NEPLAN, CYME, Synergi | — | Dağıtım planlaması |
| PLEXOS | Energy Exemplar | Piyasa ve üretim planlama benzetimi |

Tablodaki terimler:

- **EMTP:** Electromagnetic Transients Program (elektromanyetik geçici hal programı).
- **HVDC:** High Voltage Direct Current (yüksek gerilim doğru akım) iletimidir.
- **Ark parlaması:** Kısa devrede havada oluşan arkın açığa çıkardığı tehlikeli ısı ve ışık enerjisidir.

### Fark algoritmada değil

Ticari paketlerin açık kaynaktan farkı algoritma değildir; algoritmalar aynı ders kitaplarındandır.

Fark şu beş şeydedir:

1. Doğrulanmış eleman modelleri (röle, evirici, uyartım sistemi kütüphaneleri).
2. Büyük model yönetimi.
3. Grafik arayüz.
4. Şebeke işletmecilerinin veri biçimleriyle uyum.
5. Üreticinin sorumluluğu.

TEİAŞ'ın (Türkiye Elektrik İletim A.Ş.) ve MAM'ın (TÜBİTAK Marmara Araştırma Merkezi) hangi paketleri kullandığını **doğrulamadım**. Mülakatta varsayma; sor.

## Dürüst strateji

### Söylenmeyecekler

| Söylenmeyecek cümle | Neden |
| --- | --- |
| "PowerFactory'ye biraz baktım." | Takip sorusu: "Hangi modülüne? Kısa devre yöntemini nereden seçiyorsun?" Cevap veremezsin. |
| "Aynı şey zaten, hızlı öğrenirim." | Küçümseyici ve kanıtsız. |
| "Üniversitede görmüştük." | Hatırlamıyorsan söyleme. |
| Sessizce geçiştirmek. | İlanda madde olarak yazıyor; sorulacak. |

### Söylenecek olan: üç parçalı cevap

1. **Açık gerçek.** "PowerFactory ve PSS/E kullanmadım."
2. **Eşdeğer iş akışı.** "Ama bu araçların yaptığı işi adım adım biliyorum, çünkü aynısını kodla yaptım."
3. **Öğrenme planı ve soru.** "İlk haftada şunu yaparım. Siz hangisini kullanıyorsunuz?"

> **Sade anlatım:** Önce eksiğini açıkça kabul edersin. Sonra o aracın yaptığı işi başka yoldan yaptığını gösterirsin. En sonda nasıl öğreneceğini söyler ve karşı tarafa soru sorarsın.

### Eşdeğer iş akışı: bunu anlatabilmelisin

Her analiz paketi aynı altı adımı izler. Sen bu adımları açık kaynakla ve kendi kodunla yaptın.

Tablodaki kısaltmalar:

- **CIM:** Common Information Model (ortak bilgi modeli), şebeke modeli değişim standardı.
- **PSS-E dosyası:** PSS/E'nin ham veri dosyası.
- **DPL:** DIgSILENT Programming Language, PowerFactory'nin kendi betik dili.
- **IDEV:** PSS/E'de komutları sırayla koşturan toplu komut dosyası.
- **Newton-Raphson:** Doğrusal olmayan yük akışı denklemlerini adım adım çözen yöntem.

| Adım | Ticari pakette | Senin yaptığın / yapacağın |
| --- | --- | --- |
| 1. Model kur | Tek hat şeması çiz, eleman verisi gir veya CIM/PSS-E dosyası içe aktar | Bara, hat, trafo, yük, üreteç tablolarını kodla kur (`nr_yuk_akisi.py`: `Hat` veri sınıfı) |
| 2. Veriyi doğrula | Topoloji denetimi, ada raporu, birim ve baz uyarıları | Bağlı bileşen denetimi, satır toplamı denetimi, sıfır empedans reddi (testte var) |
| 3. Baz durumu çöz | Yük akışı; yakınsama raporu | Newton-Raphson; artık geçmişi (`Sonuc.artiklar`) |
| 4. Senaryo koş | Çalışma vakaları, değişkenler, betikle toplu koşu (DPL, Python API, IDEV) | Döngü içinde parametre değiştir, sonuçları tabloya topla |
| 5. Sınırları denetle | Gerilim ve yüklenme raporu, renkli şema | İhlal tablosu: eleman, değer, sınır, yüzde |
| 6. Raporla ve yinele | Rapor şablonu, sürüm | Kod + veri + sonuç birlikte sürümlü; test ile sabitlenmiş |

API, Application Programming Interface (uygulama programlama arayüzü) demektir. Ada raporu, şebekenin birbirinden kopuk parçalara (adalara) bölünüp bölünmediğini gösterir.

Söyleyeceğin cümle:

> "PowerFactory ve PSS/E kullanmadım; bunu açıkça söyleyeyim. Yaptığım şey şu: yük akışını Newton-Raphson ile sıfırdan yazdım, kapalı çözümü olan bir örnekle ve güç dengesiyle doğruladım, reaktif sınırda bara tipinin değişmesini ve yakınsamayan vakayı test ettim. Yani bu araçların yük akışı düğmesinin arkasında ne olduğunu biliyorum; bilmediğim şey arayüzleri, veri biçimleri ve eleman kütüphaneleri. Onları öğrenme yolum belli: küçük bir vakayı araçta kurar, kendi kodumla aynı sonucu verdiğini görür, sonra gerçek modele geçerim. Grubunuzda hangi paket kullanılıyor?"

Bu cevap maddeyi "var" yapmaz. Ama üç şeyi kanıtlar:

1. Dürüstlük.
2. Yöntemi anlama.
3. Öğrenme biçimi.

İkisi (araştırma ve öğrenme motivasyonu) ilanın ayrı maddeleridir.

### Bu cevabı daha güçlü yapmak için: bir akşamlık iş

Şu an "pandapower kullandım" diyemezsin; bu makinede kurulu değil ve denemedin. Mülakattan önce şunu yap, sonra **gerçekten** söyleyebilirsin. Her adımın amacı yanında yazıyor:

1. `pip install pandapower` (Python 3.14 ile kurulmazsa 3.12'lik bir sanal ortam aç).
   Amacı: aracı kendi makinende çalışır hale getirmek.
2. `nr_yuk_akisi.py`'deki üç baralı şebekeyi pandapower'da kur: `create_empty_network`, `create_bus`, `create_line_from_parameters`, `create_ext_grid`, `create_gen`, `create_load`, sonra `runpp`.
   Amacı: sonucunu bildiğin bir şebekeyi yeni araçta yeniden kurmak. `runpp`, pandapower'ın yük akışını koşturan işlevidir.
3. `net.res_bus` içindeki gerilimleri kendi sonucunla karşılaştır: beklenen `V_3 ≈ 0,9515 pu`.
   Amacı: iki çözücünün aynı sayıyı verdiğini görmek. pu, per-unit (birim değer) demektir.
4. Tutmazsa nedenini bul. Büyük ihtimalle birim çevirmesidir: pandapower hattı ohm/km ve kV ile, yükü MW ile ister; senin kodun per-unit. Bu ayıklama, mülakatta anlatacağın en iyi hikâyedir.
   Amacı: araçlar arası farkın kaynağını bulmayı kendi elinle yaşamak.
5. `runpp` yerine `pandapower.shortcircuit.calc_sc` ile kısa devreyi de dene.
   Amacı: yük akışının yanında kısa devre hesabını da araçta görmüş olmak.

Bu sayfaya pandapower kodu koymadım, çünkü çalıştırıp doğrulayamadım. İşlev adları pandapower belgelerindendir; kurduğunda güncel belgeden imzalarını kontrol et.

Yaptıktan sonra cümlen şuna döner:

> "Ticari paket kullanmadım. pandapower ile üç baralı bir vakayı kurup kendi yazdığım çözücüyle karşılaştırdım; ilk denemede tutmadı, nedeni baz çevirmesiydi."

## Ortak veri biçimleri

Araçlar arası geçiş, yazılım işinin büyük kısmıdır.

| Biçim | Ne |
| --- | --- |
| CIM / CGMES (IEC 61970, 61968) | Şebeke işletmecileri arası standart model değişimi; XML/RDF (`16/02`) |
| PSS/E RAW ve DYR | Fiilî endüstri standardı metin biçimi: sürekli hal ve dinamik veri |
| MATPOWER `mpc` | Akademik vaka biçimi |
| IEEE Common Data Format | Eski test vakaları |
| OpenDSS `.dss` | Dağıtım modelleri |

Tablodaki kısaltmalar:

- **CGMES:** Common Grid Model Exchange Standard (ortak şebeke modeli değişim standardı), CIM'in Avrupa profilidir.
- **XML/RDF:** XML (Extensible Markup Language, genişletilebilir işaretleme dili) ve RDF (Resource Description Framework, kaynak tanımlama çerçevesi). CIM dosyaları bu biçimde yazılır.
- **RAW ve DYR:** RAW sürekli hal (yük akışı) verisini, DYR dinamik model verisini taşır.

### Dönüştürmede sorun çıkan yerler

| Sorun yeri | Açıklama |
| --- | --- |
| Per-unit bazları | Baz güç veya baz gerilim araçtan araca farklı olabilir. |
| Trafo kademe tarafı ve oranı | Kademe hangi sargıya yazılmış, oran nasıl tanımlanmış. |
| Hat şöntünün iki uca paylaşımı | Şönt suseptans toplam mı, her uca yarısı mı. |
| Üç sargılı trafonun yıldız eşdeğeri | Üç sargılı trafo, ortada sanal bir baralı üç kola çevrilir; araçlar bunu farklı yapabilir. |
| Anahtar ve bara ayrıntısı | Bara-kesici modeli ile bara-dal modeli. |

Bara-kesici modeli her kesiciyi ve ayırıcıyı ayrı gösterir. Bara-dal modeli bunları toplayıp yalnız elektriksel baraları ve dalları bırakır.

## Yaygın yanlış

| Yanlış inanç | Doğrusu |
| --- | --- |
| **"Açık kaynak araç oyuncaktır."** | pandapower ve OpenDSS sektörde ve şebeke işletmecilerinde kullanılır. Eksikleri dinamik modeller ve doğrulanmış kütüphanelerdir. |
| **"Ticari paket doğru sonuç verir."** | Girdiği veri kadar doğru sonuç verir. İki paket aynı modelde farklı sonuç verebilir: varsayılan ayarlar, kademe ve yük modeli farkı. |
| **"Aracı bilmek analizi bilmektir."** | Düğmeye basmak ile sonucun neden öyle çıktığını söylemek ayrı şeylerdir. Panel ikincisini ölçer. |
| **"Kullanmadığımı söylersem elenirim."** | Kullandığını söyleyip takip sorusunda takılırsan elenirsin. |
| **"OpenDSS ile iletim, pandapower ile dengesiz dağıtım yaparım."** | Aracın tasarım amacının dışına çıkmak mümkündür ama verimsizdir. |

## Panel takip sorusu

### Soru 1

"İki araç aynı vakada farklı sonuç verdi. Ne yaparsın?"

Cevap: en küçük farkı üreten vakaya inerim. Sırayla bakarım:

1. Baz güç ve gerilim
2. Trafo kademe konumu ve tarafı
3. Hat şöntü
4. Yük modeli (sabit güç mü)
5. Üreteç reaktif sınırları
6. Salınım barası
7. Yakınsama toleransı

Tek bir hat ve tek bir yükle başlayıp eleman ekleyerek farkın nerede doğduğunu bulurum.

> **Mülakatta şöyle söyle:** "En küçük farkı üreten vakaya inerim. Baz güç ve gerilim, trafo kademe konumu ve tarafı, hat şöntü, yük modeli, üreteç reaktif sınırları, salınım barası ve yakınsama toleransına sırayla bakarım. Tek bir hat ve tek bir yükle başlayıp eleman ekleyerek farkın nerede doğduğunu bulurum."

### Soru 2

"Kendi çözücünü yazmak yerine neden hazır aracı kullanmadın?"

Cevap: öğrenmek için yazdım. Üretimde hazır ve doğrulanmış çözücüyü kullanırım; kendi kodum onu anlamak ve sonucunu sınamak içindir.

Aşağıdaki konuşma bu sayfanın tamamını kapsar: dürüst kabul, beş açık kaynak aracın işi, altı adımlı ortak iş akışı ve öğrenme yöntemi.

## 90 saniye

"Ticari analiz paketlerini kullanmadım; bunu açık söylüyorum. Açık kaynak tarafını tanıyorum: pandapower iletimde yük akışı ve kısa devre için, OpenDSS dengesiz dağıtım ve zaman serisi için, PyPSA yatırım planlaması için, MATPOWER optimal güç akışında akademik referans olarak, GridLAB-D son kullanıcı davranışı için kullanılır. Bütün paketler aynı iş akışını izler: model kur, veriyi doğrula, baz durumu çöz, senaryo koş, sınırları denetle, raporla. Bu akışı kendi yazdığım yük akışı koduyla ve testleriyle uyguladım. Yeni bir aracı küçük bir vakayı kurup bildiğim sonuçla karşılaştırarak öğrenirim."
