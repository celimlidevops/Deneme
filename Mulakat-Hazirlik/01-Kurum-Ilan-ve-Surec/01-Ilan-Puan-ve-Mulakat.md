# İlan, puan ve mülakat süreci

Bu sayfa başvurduğun ilanı baştan sona anlatır. Önce ilanın kimliğini verir: kod, yer, kontenjan, tarih. Sonra kısa iş tanımının aslında hangi işleri kastettiğini açar. Ardından zorunlu koşulları, mülakata kimin çağrılacağını belirleyen puan formülünü ve mülakat elemesini anlatır. En sonda belge ve beyan riskini ve mülakatta söyleyeceğin kısa metni verir.

İlanda geçen kurum adı **MAM**, TÜBİTAK Marmara Araştırma Merkezi'dir. Başvurduğun grup, MAM'ın Ankara'daki Güç Sistemleri Araştırma Grubu'dur.

## Sayfa haritası

1. **Kimlik:** ilanın kodu, görev yeri, kontenjanı, son başvuru tarihi ve grubun iletişim bilgisi.
2. **İş tanımının çözümü:** tek cümlelik iş tanımından çıkan dört iş parçası.
3. **Zorunlu koşullar:** bölüm, yaş, tecrübe, İngilizce ve genel şartlar.
4. **Puan formülü:** mülakata çağrılma sırasını belirleyen hesap, tecrübe terimi ve özel koşul ek puanı.
5. **Mülakat elemesi:** kaç kişinin çağrıldığı, baraj, asil ve yedek.
6. **Mülakat öncesi değerlendirme:** envanter, teknik test ve ekibin yazılım yığını.
7. **Beyan:** istenen belgeler ve tutarlılık riski.
8. **Mülakatta 90 saniye:** mülakatta söyleyeceğin kısa metin.

## 1. Kimlik

İlanın temel bilgileri aşağıda. **Referans kodu**, aynı ilan içindeki belirli kadroyu gösteren alt koddur; başvuru bu koda yapılır.

| Alan | Değer |
| --- | --- |
| Unvan | Araştırmacı (Ar-Ge personeli) |
| İlan kodu | TBTK.MAM.A.2026-2 |
| Referans | TBTK.MAM.A.2026-2.02 |
| İş yeri | MAM |
| Görev yeri | Ankara |
| Statü | Proje personeli |
| Tecrübe | 3 yıl ve daha fazlası |
| Kontenjan | 3 |
| Son başvuru | 05.10.2026, 17:00 |
| Başvuru | Yalnızca kariyer.tubitak.gov.tr |
| Aynı dönem kuralı | TBTK ile başlayan, son başvurusu aynı tarih olan ilanlardan en fazla 2 |

Son satırı açalım. Kodu "TBTK" ile başlayan ve son başvuru tarihi aynı olan ilanlardan en fazla ikisine başvurabilirsin.

**Proje personeli** statüsü, kadronun belirli projelere bağlı olarak açıldığını anlatır.

### Görev yeri ve iletişim

Görev yerinin Ankara olması önemlidir. Bu, Gebze'deki genel MAM adresinden ayrıdır.

| Bilgi | Değer |
| --- | --- |
| Birim adı | Enerji Teknolojileri Başkan Yardımcılığı, Ankara |
| Grubun iletişim telefonu | 0312 210 18 30 |
| E-posta | `mam.byet-gsag@tubitak.gov.tr` |

## 2. İş tanımının çözümü

İlandaki iş tanımı kısadır ve bilinçli olarak geniştir:

> Güç sistemleri araştırma alanında yürütülen projelerde, elektrik iletim ve dağıtım şebekeleri için analiz ve yazılım geliştirme.

İki terim:

- **İletim:** elektriği santrallerden şehirlere yüksek gerilimle taşıyan ana şebeke.
- **Dağıtım:** bu elektriği daha düşük gerilimle evlere ve işyerlerine ulaştıran yerel şebeke.

Bu tek cümleden dört iş parçası çıkar:

| İş parçası | İçinde ne var |
| --- | --- |
| Modeli kurmak | Bara, hat, trafo, üretim, yük, koruma |
| Analizi koşmak | Yük akışı, kısa devre, güvenlik, kararlılık, durum kestirimi, ekonomik işletme, planlama |
| Sonucu karara çevirmek | Limit ihlali, yatırım, işletme talimatı, koruma ayarı |
| Bunu başkasının kullanacağı yazılıma koymak | Algoritma, veri, servis, arayüz, test |

Tablodaki birkaç terim:

- **Bara:** şebeke modelinde hatların, trafoların ve yüklerin birleştiği bağlantı düğümü.
- **Yük akışı:** belli bir üretim ve tüketim durumunda her hattan ne kadar güç geçtiğini ve baraların gerilimini hesaplayan temel analiz.
- **Kısa devre:** arıza anında akan akımın hesabı.
- **Durum kestirimi:** sahadan gelen, hatalı olabilecek ölçümlerden şebekenin en olası gerçek durumunu bulmak.
- **Limit ihlali:** bir büyüklüğün izin verilen sınırı aşması.

### İki yaygın tuzak

İlan **hem iletim hem dağıtım** yazar. Yalnızca 400 kV anlatıp 34,5 kV'yi boş bırakmak ilanın yarısını kaçırır. 400 kV iletimin, 34,5 kV ise dağıtımın tipik gerilimidir.

Aynı şekilde yalnızca fizik anlatıp kod tarafını "öğrenirim" diye geçiştirmek, ilanın "yazılım projelerinde aktif çalışmış olmak" maddesine çarpar.

> **Sade anlatım:** İlan "analiz" ve "yazılım" kelimelerini yan yana koyuyor. İkisinden birini boş bırakırsan, cevabının yarısı eksik kalır.

## 3. Zorunlu koşullar

Bu koşulların hepsi sağlanmazsa başvuru geçersizdir.

| Koşul | Ayrıntı |
| --- | --- |
| Bölüm | Elektrik veya Elektrik-Elektronik Mühendisliği, en az 4 yıllık lisans |
| Doğum tarihi | 01.01.1991 ve sonrası |
| Tecrübe | İş tanımındaki alanda en az 3 tam yıl. Bu süreden az başvuru geçersizdir. Doktora, istihdam edileceği alanda 4 yıl tecrübeye sayılır. |
| Askerlik | Erkek adayda son başvuru itibarıyla askerlik bitmiş, muaf veya tecilli |
| Genel şartlar | Kamu haklarından yasaklı olmamak, görevini sürekli engelleyecek hastalık bulunmamak, ilanda sayılan adli şartlar |

**Tecilli**, askerliği yasal olarak ertelenmiş demektir.

### İngilizce

Aşağıdaki sınavlardan birinde verilen puan veya düzey yeterlidir. Bu puanlarda **geçerlilik süresi aranmaz**; yani eski tarihli bir sonuç da kabul edilir.

| Sınav | Gereken |
| --- | --- |
| YDS, YÖKDİL, KPDS veya ÜDS | 70 |
| TOEFL iBT | 84 |
| TOEFL CBT | 221 |
| TOEFL PBT | 561 |
| FCE | C |
| CAE | B |
| CPE | C |

Kısaltmalar:

- **YDS:** Yabancı Dil Bilgisi Seviye Tespit Sınavı.
- **YÖKDİL:** Yükseköğretim Kurumları Yabancı Dil Sınavı.
- **KPDS:** Kamu Personeli Yabancı Dil Bilgisi Seviye Tespit Sınavı (eski sınav).
- **ÜDS:** Üniversitelerarası Kurul Yabancı Dil Sınavı (eski sınav).
- **TOEFL** (Test of English as a Foreign Language): uluslararası İngilizce sınavı. **iBT** internet tabanlı, **CBT** bilgisayar tabanlı, **PBT** kâğıt tabanlı sürümdür.
- **FCE, CAE, CPE:** Cambridge sınavları. Sırasıyla First Certificate in English, Certificate in Advanced English, Certificate of Proficiency in English.

İngilizce puanı **aranmayan** üç hal vardır:

1. %100 İngilizce lisans. Alan dışı dersler hariç tutulur ve üniversite bunu onaylamalıdır.
2. Resmi dili İngilizce olan bir ülkede lisans, YL (yüksek lisans) veya doktora.
3. Ya da o ülkede iş tanımındaki alanda en az 3 yıl meslek.

## 4. Puan formülü (bu ilan tecrübelidir)

Bu formül **mülakat notu değildir**. Mülakata kimin çağrılacağını sıralar. İlan "araştırmacı ve tecrübe şartlı" olduğu için aşağıdaki formül kullanılır.

Formüldeki kısaltmalar:

- **GNO:** Genel Not Ortalaması. Burada 4'lük sistemde lisans ortalaman.
- **YKS:** Yükseköğretim Kurumları Sınavı. Üniversiteye yerleştiğin sınavdaki sıralaman kullanılır.

Aşağıdaki blok formülün kendisidir. Dört terimi toplar ve sonucun en az 3,20 olmasını ister.

```
Lisans GNO (4'lük)
+ 5 * (1 / (1 + e^(5 - tecrübe yılı)))
+ 10000 / (YKS yerleştirme sıralaması)
+ özel koşul ek puanı
>= 3,20
```

Terimleri tek tek okuyalım:

| Terim | Ne ölçer |
| --- | --- |
| Lisans GNO (4'lük) | Lisans başarın |
| `5 * (1 / (1 + e^(5 - tecrübe yılı)))` | Tecrübe yılın; tavanı 5 puan |
| `10000 / (YKS yerleştirme sıralaması)` | Sınav sıralaman; sıralama küçüldükçe (yani daha iyi oldukça) puan büyür |
| Özel koşul ek puanı | Alanla ilgili ödül ve dereceler |
| `>= 3,20` | Toplamın geçmesi gereken alt sınır |

### Tecrübe terimi nasıl davranır?

Tecrübe terimi bir **lojistik doygunluktur**. Yani başta yavaş artar, ortada hızlanır, sonra tavana yaklaşıp yatay kalır. Burada `e`, doğal logaritmanın tabanıdır (yaklaşık 2,718).

| Tecrübe yılı | Tecrübe terimi |
| --- | --- |
| 3 | Yaklaşık 0,56 |
| 5 | 2,50 |
| 7 | Yaklaşık 4,41 |
| 10 | Yaklaşık 4,97 |
| Tavan | 5 puan |

5 yılda değer tam 2,50 çıkar, çünkü üs `5 − 5 = 0` olur, `e^0 = 1` olur ve terim `5 × 1/2 = 2,50` olur.

Sonuç: kıdem tek başına GNO'yu ezmez, fakat 3 yıl ile 7 yıl arasında ciddi fark açar.

Kontrol notu: formülü hesap makinesiyle yeniden koşarsan 3 yıl için yaklaşık 0,60 ve 7 yıl için yaklaşık 4,40 bulursun. Tablodaki 0,56 ve 4,41 değerleri bu notun önceki sürümünden aynen korundu; mülakatta kesin sayı söyleyeceksen kendin hesapla.

> **Sade anlatım:** Tecrübe puanı bir doldurma kabı gibidir. İlk yıllarda yavaş dolar, 3 ile 7 yıl arasında hızla dolar, 10 yılda neredeyse ağzına kadar dolmuştur. Kabın hacmi 5 puandır.

### Not ve sıralama dönüşümleri

- **100 üzerinden not**, YÖK'ün (Yükseköğretim Kurulu) 4'lük dönüşüm tablosuyla çevrilir.
- **Yurt dışı mezuniyette** GNO ve sıralama yerine Times Higher Education sıralaması kullanılır. İlk 1000 dışındaki üniversiteden başvuru alınmaz.
- **ÖSYM'siz veya DGS ile gelen adayda**, başladığı yıldaki bölümün en düşük yerleştirme sıralaması kullanılır. ÖSYM, Ölçme, Seçme ve Yerleştirme Merkezi'dir; DGS, Dikey Geçiş Sınavı'dır (ön lisanstan lisansa geçiş sınavı).

### Özel koşul ek puanı

| Kural | Değer |
| --- | --- |
| Ne sayılır | Alanla ilgili ulusal veya uluslararası birincilik, ikincilik, üçüncülük ya da ödül |
| Her biri | 0,3 |
| Tavan | 0,9 |
| Hangi dönem | Ön lisans, lisans veya sonrası sayılır |
| Belge | Belgesiz beyan puan üretmez |

Yani en fazla üç ödül puan getirir: `3 × 0,3 = 0,9`.

## 5. Mülakat elemesi

### Kim çağrılır?

Çağrı kuralı: her referans kodu için en yüksek puandan başlayarak **kontenjanın 10 katı** aday çağrılır.

- Kontenjan 3 kişi olduğu için 30 aday çağrılır.
- Son sıradaki puanı paylaşanlar da çağrılır. Yani 30. adayla aynı puanı alan herkes listeye girer.

### Mülakatta baraj

Mülakat 100 üzerinden **70** barajlıdır.

- Barajı geçenler kendi içinde sıralanır.
- 3 asil, en fazla 3 yedek belirlenir.
- 70 altı alan aday, formül puanı yüksek olsa da elenir.

> **Sade anlatım:** Formül puanı seni yalnızca kapıdan içeri sokar. İçeride herkes sıfırdan başlar ve 70'i geçmek zorundadır.

## 6. Mülakat öncesi değerlendirme

Mülakattan önce envanter, teknik değerlendirme veya online araç gelebilir. **Bu tur da elemedir.**

Gelebilecek biçimler:

- kod,
- kısa analiz sorusu,
- kişilik envanteri.

**Envanter**, kişilik ve yetkinlik özelliklerini ölçen anket tipi testtir. Ayrıntılı hazırlık [05-Envanter-ve-Online-Degerlendirme.md](05-Envanter-ve-Online-Degerlendirme.md) sayfasındadır.

### Ekibin yazılım yığını

Aynı dönemde yayımlanan aday araştırmacı ilanı, ekibin yazılım tarafını gösterir:

| Teknoloji | Ne işe yarar |
| --- | --- |
| Java | Programlama dili |
| JavaScript | Web arayüzü ve programlama dili |
| İlişkisel veri tabanı | Tablolar halinde veri saklama |
| REST/SOAP | Web servis türleri. REST (Representational State Transfer) hafif, SOAP (Simple Object Access Protocol) daha katı kurallı bir servis biçimidir. |
| Git | Sürüm kontrol |
| Maven | Java projelerini derleme ve bağımlılık yönetimi |
| Jenkins | Otomatik derleme ve test (sürekli entegrasyon) |
| GitLab | Git deposu barındırma ve iş akışı platformu |

Senin ilanın bu listeyi zorunlu tutmaz; sen analiz tarafındasın. Yine de aynı ürün ailesine kod yazılacağı için bu yığını tanımak gerekir.

## 7. Beyan

Kariyer sistemindeki **beyan esastır**. Hatalı bilgi veya eksik belge başvuruyu düşürür.

İstenen belgeler:

- transkript,
- diploma,
- YKS sonuç ve yerleştirme belgesi,
- yabancı dil belgesi,
- SGK (Sosyal Güvenlik Kurumu) hizmet dökümü,
- meslek kodu yoksa çalışma belgesi,
- varsa ödül belgesi,
- erkek adayda askerlik belgesi.

**SGK hizmet dökümü**, hangi işyerinde hangi tarihler arasında sigortalı çalıştığını gösteren resmi kayıttır.

Mülakatta tecrübe yılın ile anlattığın projelerin, bu belgelerle aynı hikâyeyi anlatması gerekir. Bu konunun ayrıntısı [04-Tercih-Sebebi-Kanit-Tablosu.md](04-Tercih-Sebebi-Kanit-Tablosu.md) sayfasındaki "Tecrübe beyanı uyarısı" bölümündedir.

### 90 saniyelik metin için not

Aşağıdaki metin bu sayfanın sözlü özetidir. Kısaltmalar:

- **TEİAŞ:** Türkiye Elektrik İletim A.Ş., ülkenin iletim şebekesini işleten kurum.
- **SIPS** (System Integrity Protection Scheme): Akıllı Koruma Sistemi; geniş alan ölçümüyle sistem bütünlüğünü koruyan sistem. Ayrıntısı [02-MAM-YTBS-SIPS-ve-Turkiye-Sistemi.md](02-MAM-YTBS-SIPS-ve-Turkiye-Sistemi.md) sayfasında.
- **Yük Tevzi Bilgi Sistemi** (YTBS): grubun TEİAŞ için geliştirdiği enerji yönetim platformu.

## Mülakatta 90 saniye

“Başvurduğum kadro, Ankara’daki Güç Sistemleri Araştırma Grubu’nda iletim ve dağıtım şebekesi için analiz ve yazılım işi. Grup TEİAŞ’ın kullandığı Yük Tevzi Bilgi Sistemi’ni ve geniş alan ölçümüne dayanan SIPS’i geliştirmiş. Ben de analiz tarafında yük akışı, güvenlik, kararlılık ve durum kestirimini; yazılım tarafında bu hesapların veri modeli, servis ve test ile nasıl ürüne döndüğünü anlatabilirim. Kontenjan 3, baraj 70. Öncesinde online teknik değerlendirme olabileceğini de biliyorum.”

## Kendini yokla

Önce cevabı kapat, kendin söyle, sonra kontrol et.

1. **İlan kodu ve referans kodu nedir?**
   İlan kodu TBTK.MAM.A.2026-2, referans TBTK.MAM.A.2026-2.02.

2. **Görev yeri neresi, son başvuru ne zaman?**
   Ankara. 05.10.2026, saat 17:00.

3. **İş tanımından çıkan dört iş parçası nedir?**
   Modeli kurmak, analizi koşmak, sonucu karara çevirmek, bunu başkasının kullanacağı yazılıma koymak.

4. **Tecrübe şartı nedir? Doktora kaç yıl sayılır?**
   İş tanımındaki alanda en az 3 tam yıl. Doktora, istihdam edileceği alanda 4 yıl tecrübeye sayılır.

5. **YDS ve TOEFL iBT için gereken puan nedir?**
   YDS 70, TOEFL iBT 84. Geçerlilik süresi aranmaz.

6. **Tecrübe teriminin tavanı nedir ve 5 yılda kaç puan verir?**
   Tavan 5 puan. 5 yılda 2,50.

7. **Özel koşul ek puanı nasıl hesaplanır?**
   Her alanla ilgili derece veya ödül 0,3; tavan 0,9; belgesiz beyan puan üretmez.

8. **Mülakata kaç kişi çağrılır, baraj kaçtır?**
   Kontenjanın 10 katı, yani 30 aday; son sıradaki puanı paylaşanlar da çağrılır. Baraj 100 üzerinden 70. 3 asil, en fazla 3 yedek.

9. **Formül puanı yüksek ama mülakattan 65 alan aday ne olur?**
   Elenir. 70 altı, formül puanı yüksek olsa da elenir.

## Bu sayfayı dene

Soruyu gör, cevabını yaz, sonra aç. Bilemediğin soru tekrar gelir.

[Bu sayfanın sorularına geç](test.html?sayfa=01-01)
