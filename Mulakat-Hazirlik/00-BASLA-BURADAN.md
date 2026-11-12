# Başla buradan

Bu klasör, TÜBİTAK MAM araştırmacı mülakatına hazırlanmak içindir. Bu sayfa üç şeyi anlatır: ilan neyi istiyor, mülakat neyi ölçecek ve klasörler hangi sırayla çalışılır.

Kısaltmalar:

- **TÜBİTAK:** Türkiye Bilimsel ve Teknolojik Araştırma Kurumu.
- **MAM:** Marmara Araştırma Merkezi. TÜBİTAK'ın araştırma merkezlerinden biridir.

## İlan künyesi

| Alan | Değer |
| --- | --- |
| İlan | **TBTK.MAM.A.2026-2.02** (ilan kodu TBTK.MAM.A.2026-2) |
| Pozisyon | Ar-Ge Personeli / Araştırmacı, proje personeli, en az 3 yıl |
| Yer | Ankara |
| Birim | TÜBİTAK MAM Enerji Teknolojileri Başkan Yardımcılığı, **Güç Sistemleri Araştırma Grubu** |
| İşin cümlesi | Elektrik **iletim ve dağıtım** şebekeleri için **analiz** ve **yazılım** |

İlan kodundaki **TBTK**, TÜBİTAK'ın kısaltmasıdır. **Ar-Ge**, araştırma ve geliştirme demektir.

İşin cümlesi iki parçalıdır ve ikisi birlikte istenir:

- **İletim ve dağıtım:** elektriğin santralden yüksek gerilimle taşınması (iletim) ve şehir içinde tüketiciye ulaştırılması (dağıtım).
- **Analiz ve yazılım:** şebekenin davranışını hesaplamak ve bu hesabı çalışan bir programa dönüştürmek.

## Kaynaklar

Bu klasör, ilandaki her maddeyi ve grubun kamuoyuna açıkladığı işleri mülakatta anlatılabilir hale getirir.

| Bilgi türü | Kaynak |
| --- | --- |
| Rakamlar | TEİAŞ 2025 faaliyet raporu |
| Rakamlar | TEİAŞ “Sayılarla Elektrik İletimi” sayfası (Eylül–Ekim 2026) |
| Kurallar | Elektrik Şebeke Yönetmeliği |
| Ürün tanımları | MAM'ın kendi sayfaları |

**TEİAŞ:** Türkiye Elektrik İletim A.Ş. Türkiye'nin iletim şebekesini işleten devlet şirketidir. Grubun ana müşterisidir.

## Mülakatın omurgası

Panel büyük ihtimalle şunu ölçecek:

- Bir iletim veya dağıtım problemini fizikten kurup sayısal yönteme dökebiliyor musun?
- Sonucu işletme kararına çevirebiliyor musun?
- Bunu çalışan bir yazılıma bağlayabiliyor musun?

> Sade anlatım: Panel üç halkalı bir zincir arar. Fizik → hesap → karar → yazılım. Halkalardan biri eksikse cevap havada kalır.

Dört katman, ilandaki tercih sebeplerinin tamamını karşılar:

1. **Şebeke fiziği:** temeller, iletim, dağıtım, kısa devre, koruma, topraklama.
2. **Analiz:** yük akışı, güvenlik (N-1), kararlılık, durum kestirimi.
3. **Karar:** ekonomik işletme, planlama, optimizasyon, yenilenebilir entegrasyon.
4. **Yazılım:** Python, MATLAB, Java, JavaScript, analiz paketleri, veri modeli, dijital ikiz, web servis.

İki terim açıklaması:

- **N-1:** şebekedeki herhangi tek bir eleman (bir hat, bir trafo, bir santral) devre dışı kaldığında sistemin hâlâ güvenli çalışması ölçütü.
- **Dijital ikiz:** gerçek şebekenin ölçümlerle sürekli güncellenen bilgisayar modeli.

Yanına üç davranış ölçütü gelir:

- araştırmaya istek,
- analitik problem çözme,
- koordinasyon ve planlama.

Lisansüstü motivasyonu da ayrıca sorulur.

## Nasıl çalışılır

Her teknik klasörde `00-Alt-Basliklar.md` dosyası o konunun tam listesidir. Diğer dosyalar bu başlıkları anlatır.

Dosyanın sonundaki **90 saniye** kutusunu sesli söyle. Takılırsan o kutu, mülakatta kullanacağın iskelettir.

Çalışma sırası:

1. `01` kurum, ilan, Türkiye sistemi, YTBS, SIPS. Bunları bilmeden teknik cevap havada kalır.
2. `02` → `06` fizik ve klasik analiz.
3. `07` → `12` güvenlik, kararlılık, kestirim, koruma, ekonomi, planlama. İlanın göbeği burası.
4. `13` → `16` optimizasyon ve yazılım. `14-Programlama/ornekler` altındaki üç betiği kendi makinede çalıştır.
5. `17` ve `18` yenilenebilir, depolama, tahmin, yapay zekâ.
6. `19` anlatım. `20` soru bankasını kart gibi çevir. `21` takvim.

İlk adımdaki iki kısaltma:

- **YTBS:** Yük Tevzi Bilgi Sistemi. MAM'ın TEİAŞ için geliştirdiği enerji yönetim platformudur.
- **SIPS:** System Integrity Protection Scheme, yani sistem bütünlüğünü koruma şeması. Büyük bir arızada şebekenin çökmesini önleyen özel koruma sistemidir.

## Online sınav

Online teknik sınav veya envanter, mülakattan önce gelebilir. İlan bunu açıkça yazar.

Soru bankasındaki kısa cevaplar ve `ornekler` klasörü bu sınav içindir. Ayrıntı `01-Kurum-Ilan-ve-Surec/05-Envanter-ve-Online-Degerlendirme.md` dosyasındadır.

## Klasör haritası

| Klasör | Ne işe yarar |
| --- | --- |
| 01 Kurum, ilan, süreç | Nereye başvurduğunu ve Türkiye sistemini kendi cümlelerinle anlatmak |
| 02 Temeller | Fazör, birim sistem, dizi bileşenleri, P–δ ve Q–V |
| 03 İletim | 400/154/66 kV, hat, trafo, FACTS, enterkonneksiyon |
| 04 Dağıtım | Radyal şebeke, dağıtık üretim, barındırma kapasitesi, DMS |
| 05 Yük akışı | NR, ayrık hızlı, DC, dağıtım yük akışı |
| 06 Kısa devre | Simetrik bileşenler, IEC 60909, kesici |
| 07 Güvenlik | N-1, beklenmeyen durum taraması, düzeltici kontrol, SIPS |
| 08 Kararlılık | Açı, gerilim, frekans; atalet, AGC, PSS |
| 09 Durum kestirimi | WLS, gözlenebilirlik, kötü veri, PMU |
| 10 Koruma ve topraklama | Seçicilik, mesafe, diferansiyel, koordinasyon |
| 11 Ekonomik işletme | Ekonomik dağıtım, ünite tahsisi, OPF, piyasa |
| 12 Planlama | Talep tahmini, master plan, güvenilirlik, fizibilite |
| 13 Optimizasyon | LP, MILP, KKT, şebeke formülasyonları |
| 14 Programlama | Python, MATLAB, Java, JavaScript ve çalışan örnekler |
| 15 Analiz yazılımları | PowerFactory, PSS/E, ETAP, pandapower, CIM/CGMES |
| 16 Yazılım mimarisi | EMS zinciri, dijital ikiz, servis, veri tabanı |
| 17 Yenilenebilir ve akıllı şebeke | Evirici tabanlı kaynak, depolama, şebeke kodu |
| 18 Veri ve yapay zekâ | Yük ve RES tahmini, karar destek, model sınırı |
| 19 Davranışsal | Araştırma, STAR, lisansüstü, sorulacak sorular |
| 20 Soru bankası | Teknik, yazılım ve formül kartı |
| 21 Çalışma planı | 14 günlük yoğun takvim |

### Tablodaki kısaltmalar

Her biri ilgili klasörde ayrıntılı anlatılır. Burada yalnızca açılımı var.

| Kısaltma | Açılımı | Kısa anlamı |
| --- | --- | --- |
| P–δ, Q–V | Aktif güç–yük açısı, reaktif güç–gerilim | Aktif güç açıyla, reaktif güç gerilimle ilişkilidir |
| kV | Kilovolt | 1000 volt |
| FACTS | Flexible AC Transmission Systems | Esnek alternatif akım iletim sistemleri; güç elektroniğiyle hat akışını ve gerilimi denetler |
| DMS | Distribution Management System | Dağıtım yönetim sistemi |
| NR | Newton-Raphson | Yük akışında kullanılan yinelemeli çözüm yöntemi |
| DC | Direct current (doğru akım) | Burada “DC yük akışı”: yalnızca aktif gücü hesaplayan doğrusal yaklaşık model |
| IEC 60909 | International Electrotechnical Commission standardı 60909 | Kısa devre akımı hesaplama standardı |
| AGC | Automatic Generation Control | Otomatik üretim kontrolü; frekansı ve bölgeler arası akışı düzeltir |
| PSS | Power System Stabilizer | Güç sistemi kararlı kılıcısı; jeneratördeki salınımları sönümler |
| WLS | Weighted Least Squares | Ağırlıklı en küçük kareler; durum kestiriminin temel yöntemi |
| PMU | Phasor Measurement Unit | Fazör ölçüm birimi; zaman damgalı gerilim ve akım ölçer |
| OPF | Optimal Power Flow | Optimal güç akışı; şebeke kısıtları altında maliyeti en aza indirir |
| LP | Linear Programming | Doğrusal programlama |
| MILP | Mixed-Integer Linear Programming | Karma tamsayılı doğrusal programlama |
| KKT | Karush–Kuhn–Tucker koşulları | Kısıtlı optimizasyonda en iyi noktanın sağlaması gereken koşullar |
| PSS/E | Power System Simulator for Engineering | Siemens'in iletim analiz yazılımı |
| ETAP | Electrical Transient Analyzer Program | Ticari güç sistemi analiz yazılımı |
| CIM/CGMES | Common Information Model / Common Grid Model Exchange Standard | Şebeke modelini kurumlar arasında paylaşmak için veri standardı |
| EMS | Energy Management System | Enerji yönetim sistemi; iletim işletmesinin analiz yazılımı |
| RES | Rüzgâr enerji santrali | — |
| STAR | Situation, Task, Action, Result | Durum, görev, eylem, sonuç; davranışsal soruya cevap kalıbı |

## Bu hazırlıkta bilinçli olarak yapılmayanlar

Bu klasörde şunlar yoktur:

- gizli TEİAŞ modeli,
- gerçek röle ayarı,
- iç yazılım kodu,
- personel bilgisi.

Mülakatta da olmaması gerekir. Ürünleri MAM'ın yayımladığı yeteneklerle anlat; içerideki mimariyi bildiğini iddia etme.

## Ezber rakamlar

Güncel kurulu güç her ay değişir. Ezber rakam söylerken ayını da söyle.

| Rakam | Değer | Tarih |
| --- | --- | --- |
| Kurulu güç | 122.518,6 MW | 2025 sonu |
| Ani puant | 60.414 MW | 2025, Temmuz |
| Kurulu güç | 127.355,2 MW | Eylül 2026 sonu |

Terimler:

- **MW:** megavat, bir milyon vat.
- **Kurulu güç:** ülkedeki bütün santrallerin toplam kapasitesi.
- **Ani puant:** bir yıl içinde herhangi bir anda görülen en yüksek tüketim.

> Mülakatta şöyle söyle: "2025 sonunda kurulu güç 122.518,6 megavattı; Eylül 2026 sonu itibarıyla 127.355,2 megavat. 2025'in ani puantı Temmuz'da 60.414 megavat."
