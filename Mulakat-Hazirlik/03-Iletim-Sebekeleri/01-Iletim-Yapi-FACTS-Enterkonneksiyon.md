# İletim şebekesi

Bu sayfa, Türkiye iletim şebekesinin yapısını, gerilimi ve güç akışını yöneten cihazları, komşu ülkelere bağlanma çalışmasını ve uzun vadeli planlamayı anlatır.

## Yapı

### Gerilim kademeleri

Türkiye'de 36 kV'nin üstü iletim sayılır. Nominal kademeler 400, 154 ve 66 kV'dir.

| Kademe | Görevi |
| --- | --- |
| 400 kV | Uzun mesafe taşıma ve büyük santral çıkışı |
| 154 kV | Bölge iletimi ve büyük tüketim noktaları |
| 66 kV | Dar bir kalıntı katman. 2025 sonunda 18 transformatörle temsil edilir. Analizde "yok" sayılmaz ama omurga değildir |
| 220 kV | Türkiye iç şebekesinde kullanılan bir kademe değildir. Bazı sınır hatlarında karşı ülkenin gerilimidir |

### Örgülü yapı

İletim **örgüldür** (meshed). Yani bir noktaya birden çok yoldan güç gelebilir. Bir hat açılınca güç kaybolmaz, başka yollara itilir.

Bu yüzden iletim analizi N-1 olmadan eksiktir. N-1, "herhangi bir elemanın tek başına devre dışı kalması" durumudur. Dağıtımdaki radyal "güç hep aşağı akar" sezgisi iletimde yanlıştır.

### Trafo merkezi

Tipik bir trafo merkezinde şunlar bulunur:

- Hat fiderleri (merkeze giren ve çıkan hat bağlantıları)
- Güç trafoları
- Bara (ekipmanların bağlandığı ortak iletken)
- Kesici, ayırıcı, toprak bıçağı
- Ölçü trafoları
- Parafudr (aşırı gerilim tutucu)
- Reaktör veya kapasitör
- Koruma ve kontrol panoları
- Haberleşme: kuranportör (hat üzerinden sinyal taşıma) ve fiber

### Bara düzenleri

Bara düzeni güvenilirliği belirler:

| Düzen | Özelliği |
| --- | --- |
| Tek bara | Ucuzdur. Bara arızası bütün merkezi karartır |
| Çift bara | Transfer imkânı ve bakım esnekliği verir |
| Kesici ve yarım (breaker-and-a-half) | Her iki hat için iki kesici yolu vardır. 400 kV'ta sık tercih edilir |
| Halka | Orta sayıda fider için uygundur |

### Yazılımdaki bara modeli

Yazılım modeli barayı çoğu zaman tek bir düğüm olarak görür. Koruma ve bakım çalışmasında ise gerçek bara-kesici topolojisi gerekir.

Düğüm-kesici modeli ile bara-hat modeli aynı şey değildir. Durum kestirimi ve SCADA (merkezi izleme ve kumanda sistemi) topoloji işlemcisi bu ikisinin arasında durur. Topoloji işlemcisi, kesici konumlarından bara-hat modelini üretir.

## Hat ve trafo işletmesi

### Hat verisi

Hat verisi R (direnç), X (reaktans), B (şönt süseptans) ve limitten ibaret değildir:

- Limit mevsimseldir.
- Sehim (iletkenin sarkması) sıcaklıkla artar. Yere ve nesnelere yaklaşım mesafesi limiti kısıtlar.
- İletken tipi termik eğriyi değiştirir. İletkenler A, C, H gibi harflerle ve kuş türü adlarıyla anılır.
- Çift devre bir direkteyse ortak mod arızası N-1'i N-2'ye çevirebilir. Yani tek olay iki devreyi birlikte düşürür. Planlamada ortak koridor riski bu yüzden sorulur.

### Reaktör ve kapasitör

| Cihaz | Ne yapar | Bedeli |
| --- | --- | --- |
| Şönt reaktör | Hafif yükte 400 kV gerilimini aşağı çeker | — |
| Şönt kapasitör | Ağır yükte gerilimi yukarı çeker ve kaybı azaltır | — |
| Seri kapasitör | Hattın elektriksel boyunu kısaltır, açı kararlılığı marjını açar | Alt senkron rezonans riski doğurur |

Alt senkron rezonans, seri kapasitörlü hattın generatör miliyle şebeke frekansının altındaki bir frekansta salınım alışverişine girmesidir. Yönetmelik alt senkron rezonansı ayrıca tanımlar.

> **Mülakatta şöyle söyle:** "Seri kompanzasyon bedava kapasite değildir."

### OLTC ve gerilim kontrol hiyerarşisi

OLTC (yük altında kademe değiştirici), 400/154 ve 154/OG (orta gerilim) trafolarında günlük gerilim aracının başıdır. Kademe değişimi ayrık ve yavaştır.

Hızlı bir gerilim çökmesinde kademe yetişmez. STATCOM, SVC veya senkron makine uyarımı yetişir.

Gerilim kontrol hiyerarşisi zaman ölçeğine göre üç kattır:

| Zaman ölçeği | Araç |
| --- | --- |
| Milisaniye | Uyarma ve FACTS |
| Saniye–dakika | Kademe ve şönt anahtarlama |
| Saat | Planlama |

## FACTS ve HVDC

FACTS (esnek AC iletim sistemleri), güç elektroniğiyle gerilimi veya hat akışını hızla ayarlayan cihaz ailesidir. HVDC ise yüksek gerilim doğru akım bağlantısıdır.

| Cihaz | Açılımı | Ne enjekte eder veya değiştirir | Tipik iş |
| --- | --- | --- | --- |
| SVC | Statik VAR kompanzatörü | Tristörlü reaktif, kademeli-sürekli | Gerilim, dinamik destek |
| STATCOM | Statik senkron kompanzatör | Gerilim kaynaklı evirici, reaktif | Zayıf gerilimde SVC'den daha iyi destek, simetrik kapasitif-endüktif |
| TCSC | Tristör kontrollü seri kapasitör | Hattın seri reaktansı | Güç akışı, sönüm |
| SSSC | Statik senkron seri kompanzatör | Hatta seri gerilim | Güç akışı |
| UPFC | Birleşik güç akış kontrolörü | Seri + şönt | P ve Q birlikte |
| HVDC LCC / VSC | Hat komütasyonlu / gerilim kaynaklı dönüştürücü | Doğru akım koridoru | Uzun mesafe, kablo, asenkron bağlama |
| Back-to-back | Sırt sırta HVDC | Kısa DC ara halka | İki senkron olmayan AC sistem |

### STATCOM'un zayıf şebekedeki üstünlüğü

SVC'nin üretebildiği reaktif güç gerilimle düşer. STATCOM ise akımı daha geniş bir aralıkta tutar. Bu yüzden gerilim düştüğünde STATCOM daha çok destek verir.

MAM'ın (TÜBİTAK Marmara Araştırma Merkezi) milli STATCOM'u bu ailedendir.

Modelleme tarafında iki ayrı model gerekir:

- Statik hal için PV (aktif güç ve gerilim sabit), PQ (aktif ve reaktif güç sabit) veya reaktif limitli bir kaynak.
- Dinamik hal için kontrol çevrimli bir kaynak.

Kontrol modeli yoksa kararlılık çalışması ancak "reaktif destek varmış" kadar doğru olur.

### HVDC

HVDC, AC açı kararlılığına AC hat gibi girmez. Çünkü üzerinden geçen güç açı farkıyla değil, ayar noktasıyla kontrol edilir.

- VSC-HVDC gerilim ve frekans desteği de verebilir.
- Klasik LCC daha çok bir güç koridorudur.

Gürcistan bağlantısını AC enterkonneksiyon gibi anlatma.

## Enterkonneksiyon çalışması

Enterkonneksiyon, komşu ülke şebekesine bağlanmaktır. Grubun açıkça yazdığı iştir. Tipik soru seti:

- Bağlantı AC mi, HVDC mi? Senkron ada büyüyor mu?
- N-1'de sınır hattı düşerse frekans sapması ve açı salınımı ne olur?
- İthalat, yerli üretim ve atalet nasıl değişir? İthalat artınca sistem ataleti düşebilir, çünkü sınırın ötesindeki atalet elektriksel olarak uzaktır.
- Bölgeler arası salınım modu (0,1–0,8 Hz tipik bant) sönümleniyor mu? PSS (güç sistemi kararlı kılıcısı) ayarı bu yüzden ENTSO-E (Avrupa iletim sistemi operatörleri ağı) bağlantısıyla birlikte yönetmelikte anılır.
- NTC (net transfer kapasitesi), güvenilirlik marjı düşüldükten sonra kalan ticarî kapasitedir. Termik limit tek başına NTC değildir.
- Koruma: sınır hattında mesafe rölesi, güç salınımı blokajı, ada koruması.

## Kayıp ve kısıt

### Kayıp

İletim kaybı kabaca yüzde birkaçtır. Dağıtım kaybı daha büyüktür ve orada teknik kayıp ile kaçak ayrı raporlanır.

Kayıp I²R'dir, yani akımın karesiyle büyür. Bu yüzden iki şey kaybı düşürür:

- Gerilimi yüksek tutmak (aynı güç için daha az akım).
- Reaktifin uzun yol gezmesini engellemek.

Reaktif yerinde üretilir. Bu ilke hem planlamanın hem OPF'nin (optimal güç akışı) cümlesidir.

### Kısıt

İletim kısıtı, ucuz üretimin yükün olduğu bölgeye akamamasıdır. Piyasa bunu bölge fiyatı veya yeniden dağıtımla fiyatlar.

Türkiye uygulamasında kısıt yönetimi TEİAŞ (Türkiye Elektrik İletim A.Ş.) işletme talimatı ve dengeleme mekanizmasıyla yürür.

Fizik tarafı: kısıtlı hatta akışı azaltmak için bir tarafta üretimi kısar, diğer tarafta artırırsın. Bu, güvenlik kısıtlı ekonomik dağıtımdır.

## Master plan senaryoları

İletim planı tek bir pik yük durumu koşmaz. En az şu aileler gerekir:

- Kış puant, yaz puant, bahar minimum (Ferranti etkisi ve reaktör ihtiyacı için)
- Yüksek yenilenebilir, düşük atalet
- Büyük santral devrede / devre dışı
- Sınır ithalatı ve ihracatı
- N-1 ve seçilmiş ortak mod N-2
- 5–10 yıllık yük ve üretim senaryosu, puantın %5 üzeri planlama yükü

Ferranti etkisi: hafif yüklü uzun hatta veya kabloda, hattın kendi kapasitesi yüzünden uçtaki gerilimin baştakinden yüksek çıkmasıdır.

Her senaryoda şunlara bakılır:

- Yük akışı
- Kısa devre: bara kısa devre gücünün koruma ve ekipman için alt ve üst sınırı
- Gerilim
- Seçilmiş olaylarda kararlılık

Master plan, bu taramayı yatırım adaylarına ve fayda/maliyet sırasına bağlar. Grubun "risk/etki eksenli planlama" dediği yer burasıdır.

## Yazılıma nasıl girer

Bir iletim modeli en az şunları taşır:

- Bara numarası ve gerilim bazı
- Hat ve trafo parametreleri
- Kademe sınırları
- Üretim Pmin/Pmax/Qmin/Qmax
- Yük P-Q
- Limitler
- Topoloji (kesici durumu)
- Kontrol modu: PV, PQ, slack (salınım barası), kademe kontrol

Eksik Q limiti "gerilim sorunu yok" yalanı üretir. Çünkü makine uyarması sınırsız sanılır.

> **Sade anlatım:** Generatöre "en fazla şu kadar reaktif verebilirsin" demezsen, model gerilimi her yerde tutturur ve sorun hiç görünmez.

Aşağıdaki metin, iletim konusu sorulduğunda 90 saniyede söyleyeceğin özettir.

## 90 saniye

"Türkiye iletimi 400 ve 154 kV örgü, 66 kV dar bir katman. Güç açıyla, reaktif yerinde yönetilir. Kapasite termik, gerilim ve kararlılık diye üçe ayrılır. FACTS ve kademe farklı zaman ölçeklerinde gerilime yardım eder. ENTSO-E bağlantısı senkron adayı büyütür; doğudaki HVDC ve radyal hatlar aynı adaya eklenmez. Planlama puantın yüzde 5 üzerinde, N-1'de kullanıcı kaybı ve ada oluşumu olmadan yapılır."
