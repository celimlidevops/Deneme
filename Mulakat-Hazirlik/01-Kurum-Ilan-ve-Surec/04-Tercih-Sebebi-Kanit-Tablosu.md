# Tercih sebebi ve kanıt

İlanda on tercih sebebi var. **Tercih sebebi**, zorunlu olmayan ama adayı öne çıkaran özelliktir.

Panel her birine karşılık senden bir kanıt arar. Bu sayfa, her madde için ne söyleyeceğini **önceden** yazman içindir.

## Önce dürüst durum tespiti

Bu tablo bir şablondur. Güçlü ve boş sütunlarını kendi özgeçmişinle doldur. Yıl, unvan ve proje adı buraya hazır yazılmaz.

Bu profil bazı maddelerde güçlü, bazılarında boştur. Boş maddeyi dolu göstermeye çalışmak mülakatta en hızlı puan kaybettiren şeydir, çünkü panel alanın içindendir ve tek bir takip sorusu yeter.

Strateji üç cümledir:

1. Güçlü olduğun maddeleri (yazılım, öğrenme, koordinasyon) somut kanıtla söyle.
2. Boş maddeleri açıkça boş söyle ve ne yaptığını göster: bu klasördeki çalışma, sıfırdan yazdığın yük akışı kodu, elle çözdüğün örnekler.
3. Aradaki köprüyü kur: üretim yazılımı disiplinini analiz yazılımına taşımak.

> Sade anlatım: Eksiğini saklama, eksiğin üstüne ne koyduğunu göster. Panel alan bilgisini öğretebilir; dürüstlüğü ve öğrenme hızını öğretemez.

## Tecrübe beyanı uyarısı

İlanın üçüncü özel koşulu: "İşin tanımında belirtilen alanlarda en az 3 yıl mesleki tecrübe."

İşin tanımı: elektrik iletim ve dağıtım şebekeleri için **analiz ve yazılım geliştirme**. Dipnot ayrıca tecrübe yılını "belirtilen alanlarda tam süreli çalışılan süre" diye tanımlar.

Bunun üç sonucu var:

- Kariyer sistemine girdiğin beyan, SGK hizmet dökümü ve onaylı çalışma belgesiyle karşılaştırılır. İlanın g maddesi, hatalı bilginin başvuruyu geçersiz kıldığını yazar.
- Yazılım geliştirme tecrübenin bu tanıma sayılıp sayılmayacağı **kurumun kararıdır**. Benim ya da senin yorumun değildir.
- Mülakatta "Bu üç yılın hangisi şebekeyle ilgili?" sorusu gelebilir. Cevabın belgeyle aynı olmalı.

**SGK:** Sosyal Güvenlik Kurumu. **SGK hizmet dökümü**, hangi işyerinde hangi tarihler arasında sigortalı çalıştığını gösteren resmî belgedir.

### Yapılacak iş

SGK dökümündeki her işyeri için bir satır yaz:

| Tarih aralığı | Unvan | Yaptığın iş | Enerji veya şebekeyle ilişkisi |
| --- | --- | --- | --- |
| | | | **var / dolaylı / yok** |

- "Dolaylı" yazdıysan ilişkiyi bir cümleyle anlat.
- "Yok" yazdıysan mülakatta da "yok" de.
- Emin değilsen mülakattan önce İnsan Kaynakları'na sor: `mam.ik@tubitak.gov.tr`.

### Hazır cevap iskeleti

Köşeli parantezli kısım yalnızca şebekeyle doğrudan ilgili bir işin varsa söylenir.

> Mülakatta şöyle söyle: "Tecrübem yazılım geliştirme tarafında. [Şebekeyle doğrudan ilgili iş varsa: şu projede şu kadar süre şunu yaptım.] Güç sistemi analizinde iş tecrübem yok; lisans derslerim var ve son haftalarda yük akışını, durum kestirimini ve ekonomik dağıtımı sıfırdan kodlayıp elle çözülmüş örneklerle doğruladım. Getirdiğim şey, analiz kodunu test edilebilir ve servis edilebilir hale getirme disiplini."

Cümledeki üç teknik terim:

- **Yük akışı:** şebekedeki her baranın gerilimini ve her hattan geçen gücü hesaplamak.
- **Durum kestirimi:** gürültülü ölçümlerden şebekenin en olası gerilim ve açı değerlerini bulmak.
- **Ekonomik dağıtım:** talebi santraller arasında en düşük maliyetle paylaştırmak.

## Tablo

"Kanıtın" sütununu kendin doldur. Köşeli parantez içindekiler örnek kalıptır; senin gerçeğin değilse silinir.

| # | İlan maddesi | Dürüst durum | Kanıtın (sen doldur) | Açığı nasıl kapatıyorsun |
| --- | --- | --- | --- | --- |
| 1 | Elektrik enerjisi ve şebekeleri alanında geliştirilen yazılım projelerinde aktif çalışmış olmak | Büyük ihtimalle **boş veya dolaylı** | [Varsa: proje, rol, süre. Yoksa: "Enerji alanında yazılım projem olmadı."] | `14-Programlama/ornekler`: sıfırdan Newton-Raphson, WLS, ekonomik dağıtım, 7 test |
| 2 | Güç Sistemleri Analizi ve Güç Dağıtım Sistemleri dersleri | Transkripte bağlı | [Ders adı, dönem, not] | `02`, `04`, `05` klasörleri |
| 3 | Güvenlik ve kararlılık analizleri, durum kestirimi çalışması | **Boş** | ["İş olarak yapmadım."] | `07`, `08`, `09` elle örnekler; `wls_durum_kestirimi.py` |
| 4 | Optimizasyon teknikleri ve programlama (Java, Python, JavaScript, MATLAB) | **Güçlü** (programlama), optimizasyon değişken | [Dil, yıl, üretimdeki proje] | `13` klasörü; `linprog` ile DC-OPF örneği |
| 5 | Dağıtım, koruma, kararlılık, ekonomik işletme, planlama dersleri | Transkripte bağlı | [Ders adı, not. Almadıysan: "almadım"] | `04`, `08`, `10`, `11`, `12` |
| 6 | Güç sistemleri analiz yazılımları ile çalışma | Büyük ihtimalle **boş** | ["PowerFactory ve PSS/E kullanmadım."] | pandapower ile aynı iş akışı: `15/02` |
| 7 | Lisansüstü çalışma veya motivasyon | Motivasyon | [Hangi problem, neden] | `19/02` |
| 8 | Yeni uygulama geliştirme teknolojilerini öğrenme motivasyonu | **Güçlü** | [Son öğrendiğin teknoloji, nasıl öğrendin, nereye uyguladın] | — |
| 9 | Araştırmaya istek, analitik düşünme, problem çözme | **Güçlü olabilir** | [Kök nedenini bulduğun bir üretim hatası: belirti, hipotez, test, sonuç] | — |
| 10 | Koordinasyon, organizasyon, planlama | **Güçlü** (teknik liderlik) | [Ekip büyüklüğü, teslim, bağımlılık yönetimi] | `19/02` araştırma ortamına çeviri |

### Tablodaki terimler

| Terim | Anlamı |
| --- | --- |
| Newton-Raphson | Yük akışını yinelemeli olarak çözen yöntem |
| WLS | Weighted Least Squares, ağırlıklı en küçük kareler. Durum kestiriminin temel yöntemi |
| `wls_durum_kestirimi.py` | `14-Programlama/ornekler` altındaki WLS örnek betiği |
| DC-OPF | DC Optimal Power Flow. Yalnızca aktif gücü hesaplayan doğrusal yaklaşık modelle optimal güç akışı |
| `linprog` | Python SciPy kütüphanesindeki doğrusal programlama çözücüsü |
| PowerFactory | DIgSILENT firmasının güç sistemi analiz yazılımı |
| PSS/E | Power System Simulator for Engineering. Siemens'in iletim analiz yazılımı |
| pandapower | Açık kaynaklı Python güç sistemi analiz kütüphanesi |
| `15/02`, `19/02` | `15` ve `19` klasörlerindeki `02` numaralı dosya |

### Maddeler duruma göre gruplanınca

| Grup | Maddeler |
| --- | --- |
| Güçlü | 4 (programlama), 8, 10; 9 güçlü olabilir |
| Boş veya büyük ihtimalle boş | 1, 3, 6 |
| Transkripte bağlı | 2, 5 |
| Motivasyon | 7 |

## Transkript taraması

2 ve 5 numaralı maddeler "ders almış olmak" der. Bu, transkriptinle doğrulanabilir tek tercih sebebidir ve panel transkripti görür.

Transkriptini aç ve şu adlara benzeyen dersleri işaretle:

- Güç Sistemleri Analizi
- Enerji İletimi
- Enerji Dağıtımı
- Elektrik Makineleri
- Yüksek Gerilim Tekniği
- Güç Elektroniği
- Koruma
- Elektrik Tesisleri
- Enerji Ekonomisi
- Kontrol Sistemleri
- Sayısal Yöntemler
- Optimizasyon

Her biri için üç bilgi yaz: dönem, not, hatırladığın tek konu.

Notun düşükse saklama.

> Mülakatta şöyle söyle: "O dönem zayıftım, şimdi şu örneği elle çözebiliyorum." Ve çöz.

## Güçlü maddeni nasıl söylersin

Zayıf: "Yazılımda iyiyim."

Güçlü:

> Mülakatta şöyle söyle: "[Kaç] yıldır üretimde çalışan sistemler geliştiriyorum. [Sistem] için [ölçek] yükte [karar] verdim. Analiz yazılımında bunun karşılığı şu: yük akışı ıraksadığında servis sessizce boş sonuç dönmemeli, nedenini ve son artığı dönmeli. Yazdığım örnekte bunu bir testle sabitledim."

İki terim:

- **Iraksamak:** yinelemeli çözümün bir sonuca yaklaşmayıp uzaklaşması.
- **Artık:** denklemin o adımda ne kadar sağlanmadığını gösteren fark. Sıfıra yaklaşıyorsa çözüm yakınsıyordur.

Bu cümle 1 numaralı maddedeki boşluğu örtmez. Ama 4, 8 ve 9'u kanıtlar ve panele, eksik olan alan bilgisinin üstüne ne koyacağını gösterir.

## Yaygın yanlış

- **"Enerji sektöründeki bir müşteriye yazılım yaptıysam bu şebeke yazılımıdır."** Müşteri enerji şirketi olabilir, yazılım muhasebe yazılımıdır. İkisini ayır ve olduğu gibi söyle.
- **"Boş maddeyi atlarım, sormazlar."** İlanın en üstteki maddesidir. Sorarlar.
- **"Kullanmadığım aracı 'biraz baktım' diye söylerim."** Takip sorusu "hangi modülünü?" olur. `15/02` dosyasındaki dürüst kalıbı kullan.
- **"Liderlik tecrübem her kapıyı açar."** Kadro araştırmacı kadrosudur. Liderliği "teknik karar ve koordinasyon" olarak çevir, "yöneticilik" olarak değil.

Aşağıdaki konuşma bir örnektir, bir özgeçmiş değildir. Kendi güçlü ve boş maddelerini söyle.

## 90 saniye

"İlandaki on maddeye dürüst bakınca üçü bende güçlü: programlama, yeni teknolojiyi öğrenme ve koordinasyon. Üçü boş: şebeke yazılımı projesi, güvenlik ve kestirim çalışması, ticari analiz yazılımı. Boş olanları dolu göstermeyeceğim. Bunun yerine son haftalarda ne yaptığımı gösterebilirim: yük akışını, durum kestirimini ve ekonomik dağıtımı sıfırdan kodladım, elle çözülmüş örneklerle doğruladım ve testlerini yazdım. Getirdiğim katkı, analiz kodunu üretim kalitesine taşıma tecrübesi; öğrenmem gereken de alanın kendisi."

## Bu sayfayı dene

Soruyu gör, cevabını yaz, sonra aç. Bilemediğin soru tekrar gelir.

[Bu sayfanın sorularına geç](test.html?sayfa=01-04)
