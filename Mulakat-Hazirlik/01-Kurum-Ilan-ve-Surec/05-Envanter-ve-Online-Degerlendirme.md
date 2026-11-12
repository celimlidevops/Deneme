# Envanter ve online değerlendirme

Mülakattan önce bir ön değerlendirme gelebilir. Bu sayfa, ilanın bu konuda ne dediğini, neyi demediğini ve üç olası biçime nasıl hazırlanacağını anlatır.

Terimler:

- **Envanter:** kişilik ve yetkinlik anketi. Doğru cevabı yoktur.
- **Online değerlendirme:** internet üzerinden yapılan test; yetenek testi veya teknik sınav olabilir.

## İlan ne diyor

Başvuru süreci, (f) maddesi:

"Mülakata çağrılacak adaylar, mülakat öncesi uygulama olarak envanter/teknik değerlendirmeye ve/veya online değerlendirme araçları kullanılarak değerlendirmeye tabi tutulabileceklerdir."

Kesin olan budur. "Tutulabilecekler" yazar; yapılacağı kesin değildir.

İlanda **yazmayanlar**:

- hangi aracın kullanılacağı,
- kaç soru olacağı,
- sonucun mülakat puanına nasıl yansıyacağı.

Çağrı e-postası geldiğinde orada yazanı esas al ve belirsizse İnsan Kaynakları'na sor.

### İlandan bilinen diğer süreç bilgileri

| Konu | İlandaki bilgi |
| --- | --- |
| Kaç aday çağrılır | Formül puanına göre sıralamada kontenjanın 10 katı aday çağrılır: 3 kişilik kadro için yaklaşık 30 aday |
| Kim sıralanır | Mülakatta 100 üzerinden 70 ve üzeri alanlar sıralanır |
| Kaç kişi seçilir | 3 asil, en fazla 3 yedek |
| Duyuru nerede | `mam.tubitak.gov.tr` ve `tubitak.gov.tr` |

**Formül puanı**, ilanda tanımlanan formülle hesaplanan ve mülakata kimin çağrılacağını belirleyen ön sıralama puanıdır. **MAM**, TÜBİTAK Marmara Araştırma Merkezi'dir; **TÜBİTAK**, Türkiye Bilimsel ve Teknolojik Araştırma Kurumu'dur.

Kariyer sistemindeki e-posta adresini ve istenmeyen posta klasörünü her gün kontrol et.

## Üç olası biçim ve hazırlığı

Biçim ilanda yazmadığı için üçüne de hazırlanılır. Hangisinin geleceği bilinmiyor.

| Biçim | Neyi ölçer | Senin için risk |
| --- | --- | --- |
| Kişilik ve yetkinlik envanteri | Tutarlılık | Rol yapmak |
| Genel yetenek testi | Sayısal, sözel, şekil akıl yürütme | Süre baskısı |
| Teknik değerlendirme veya kodlama | Alan bilgisi veya kod | Güç sistemi soruları |

### 1. Kişilik ve yetkinlik envanteri

Doğru cevabı yoktur. Ölçtüğü şey tutarlılıktır: aynı özellik farklı cümlelerle birkaç kez sorulur.

- Olduğun gibi işaretle. "İdeal aday" profilini oynamak, tekrar eden sorularda çelişki üretir.
- Her maddeye uç cevap verme. "Her zaman" ve "asla" çok sayıda olunca profil güvenilmez görünür.
- Fazla düşünme. İlk tepki çoğunlukla en tutarlı olandır.
- Mülakatta envanter sonucu önlerinde olabilir. "Tek başına çalışmayı tercih ederim" işaretleyip mülakatta "tam bir takım oyuncusuyum" dersen bu fark sorulur.

### 2. Genel yetenek testi

Sayısal, sözel ve şekil akıl yürütme. Süre baskısı ana zorluktur.

- Takıldığın soruyu geç. Bu testlerde her sorunun değeri çoğu zaman eşittir.
- Yüzde, oran, tablo ve grafik okuma ile sayı dizilerinden birer deneme çöz. Amaç bilgi değil tempo.
- Yanlışın puan götürüp götürmediğini yönergeden oku. Götürmüyorsa boş bırakma.

### 3. Teknik değerlendirme veya kodlama

Senin profilinde iki yöne gidebilir.

#### Kodlama

Burada rahatsın. Risk, soruyu güç sistemi bağlamında sormalarıdır:

- "Bu admitans matrisini kur."
- "Bu ölçümlerden en küçük kareler çözümünü bul."

Terimler:

- **Admitans matrisi (Ybus):** şebekedeki baraların birbirine hangi iletkenlikle bağlı olduğunu tutan matris. Yük akışının girdisidir.
- **En küçük kareler:** ölçümlerle modelin farkının karelerini en aza indiren çözüm. Durum kestiriminin temelidir.

Hazırlık: `14-Programlama/ornekler/nr_yuk_akisi.py` içindeki `ybus_kur` ve `nr_coz` işlevlerini bakmadan yeniden yaz. Ayrıntı `14/02` dosyasında.

- `ybus_kur`: admitans matrisini kuran işlev.
- `nr_coz`: yük akışını Newton-Raphson (NR) yöntemiyle çözen işlev. NR, sonucu adım adım düzelterek yaklaşan yinelemeli yöntemdir.

#### Güç sistemi çoktan seçmeli

Zayıf tarafın. Hazırlık: `20-Soru-Bankasi` ve `21-Calisma-Plani/Mini-Sinavlar`.

Hesap sorularında üç refleks:

1. **Birimi yaz.** kV mı V mu, MW mı pu mu, hat gerilimi mi faz gerilimi mi.
2. **Mertebe kontrolü yap.** 154 kV'ta 100 MVA yaklaşık 375 A eder. Sonucun 37 kA çıktıysa √3 veya bin katı kaçmıştır.
3. **Seçenekleri ele.** Dört seçenekten ikisi çoğunlukla √3 veya kare hatasının sonucudur.

Birimler:

| Birim | Anlamı |
| --- | --- |
| V, kV | Volt, kilovolt (1000 volt) |
| MW | Megavat; aktif güç |
| MVA | Megavolt-amper; görünür güç |
| A, kA | Amper, kiloamper (1000 amper) |
| pu | Per unit, birim değer. Büyüklüğün seçilen bir baz değere oranı |

**Hat gerilimi** iki faz arasındaki gerilimdir. **Faz gerilimi** bir fazla nötr arasındaki gerilimdir. Aralarında √3 kat fark vardır; çoğu hata buradan çıkar.

Mertebe kontrolündeki 375 A şöyle bulunur:

1. Üç fazlı görünür güç formülü: akım = görünür güç / (√3 × hat gerilimi). Bu adım hangi formülün kullanılacağını belirler.
2. Değerleri koy: 100.000.000 VA / (√3 × 154.000 V). Bu adım birimleri temel birime (VA ve V) çevirir; kV–MVA karışıklığını önler.
3. Payda: √3 × 154.000 ≈ 266.700. Bu adım √3'ü unutmadığını garantiler.
4. Sonuç: 100.000.000 / 266.700 ≈ 375 A. Bu, cevabın olması gereken mertebedir; kA mertebesinde bir sonuç bir şeyin kaçtığını gösterir.

## Teknik hazırlık

- Sabit internet, şarjlı bilgisayar, yedek olarak telefon bağlantısı.
- Kamera ve mikrofon istenebilir. Önceden dene.
- Tarayıcı sekmesi değiştirmenin kaydedildiği araçlar vardır. Yönergede izin verilmeyen hiçbir şeyi açma.
- Sessiz oda, kâğıt, kalem, izin veriliyorsa hesap makinesi.
- Bağlantı koparsa: ekran görüntüsü al, saati yaz, aynı gün İnsan Kaynakları'na e-posta at.

## Yaygın yanlış

- **"Envanteri geçmek için hazırlanılır."** Envanter geçilmez, tutarlı doldurulur.
- **"Online test önemsizdir, asıl mülakat."** Otuz adayın arasından sıyrılmak için kullanılan ilk veri olabilir.
- **"Teknik testte yazılım sorulur, hazırım."** İlanın alanı güç sistemidir. Zayıf tarafından sorulacağını varsay.
- **"Süre yeter."** Bu testler bilerek yetmeyecek şekilde tasarlanır.

Aşağıdaki konuşma metni dört parçalıdır: ilanın ne dediği ve ne demediği, envanter, yetenek testi, teknik test.

## 90 saniye

"İlan, mülakattan önce envanter veya online değerlendirme yapılabileceğini söylüyor; biçimini söylemiyor. Üç ihtimale hazırlandım. Envanteri olduğum gibi ve tutarlı doldururum. Genel yetenek testinde tempoyu korur, takıldığımı geçerim. Teknik testte birimi yazar, mertebeyi kontrol eder, seçenek elerim. Kodlama gelirse admitans matrisini ve Newton-Raphson döngüsünü bakmadan yazabiliyorum."

## Bu sayfayı dene

Çoktan seçmeli. Bilemediğin soru tarayıcıda saklanır ve doğru bilinene kadar yeniden sorulur.

[Bu sayfanın sorularına geç](test.html?sayfa=01-05)
