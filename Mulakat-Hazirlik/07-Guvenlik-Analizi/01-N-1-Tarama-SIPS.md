# Güvenlik analizi

Bu sayfa güvenlik analizinin temelini anlatır. Önce üç kelimeyi ayırır. Sonra N-1 kuralını, binlerce arızanın nasıl tarandığını, arızaya karşı iki müdahale türünü, zincirleme arızayı ve SIPS'i işler. Son olarak sonucun operatöre nasıl raporlandığını gösterir.

## Kelimeler

Mülakatta en sık karışan üç kelime vardır. Her biri farklı bir soruya cevap verir.

| Kelime | Ne sorar? | Zaman ölçeği | Örnek ölçüt |
| --- | --- | --- | --- |
| Güvenilirlik | Enerji uzun dönemde kesintisiz ve yeterli olacak mı? | Uzun dönem (yıllar) | LOLE, EENS, SAIDI |
| Güvenlik (security) | Şu anki işletme anında makul bir arıza olsa sistem limitler içinde kalır mı? | Belirli bir işletme anı | N-1 |
| Kararlılık | Bozucu etkiden sonra sistem yeni bir dengeye oturur mu? | Bozucu etkiden sonraki saniyeler | Açı, gerilim, frekans kararlılığı |

Kısaltmalar:

- **LOLE** (Loss of Load Expectation, yük kaybı beklentisi): yükün karşılanamayacağı beklenen süre.
- **EENS** (Expected Energy Not Supplied, beklenen karşılanmayan enerji): verilemeyecek enerji miktarının beklentisi.
- **SAIDI** (System Average Interruption Duration Index, sistem ortalama kesinti süresi indeksi): müşteri başına ortalama kesinti süresi.

Güvenilirlik bu ailedendir. Güvenlik ise bir işletme anına bakar; N-1 onun işletme kuralıdır.

Kararlılık açı, gerilim veya frekans olarak bozulabilir. Bir durum termik olarak N-1 güvenli olup dinamik olarak kararsız olabilir. Yani termik hesap “sorun yok” dese bile salınım başlayabilir.

> **Sade anlatım:** Güvenilirlik “uzun vadede ışık hep yanar mı?”, güvenlik “şimdi bir hat koparsa limitler aşılır mı?”, kararlılık “sarsıntıdan sonra sistem yerine oturur mu?” sorusudur.

> **Mülakatta şöyle söyle:** Üç kelimeyi aynı cümlede “sağlam” diye birleştirme.

## N-1

N-1, “sistemden bir eleman eksilince de çalışabilmeli” kuralıdır. Eksilen eleman bir iletim elemanıdır: hat, trafo, büyük üretim ünitesi, bara kesiti, bazen büyük yük.

Bu eleman devre dışıyken şu altı koşul sağlanmalıdır:

- Kalan hat ve trafolar termik limitin altında
- Gerilimler işletme bandında
- Frekans bandında
- Kararlılık bozulmuyor
- Kullanıcı kaybedilmiyor
- Sistem adalara bölünmüyor

Bu liste Elektrik Şebeke Yönetmeliği'nin planlama ve işletme diliyle uyumludur. Yönetmeliğe göre iki ek hüküm vardır:

- Planlama yükü puantın %5 üzeridir. Puant, yılın en yüksek tüketim anıdır.
- Nükleer bağlantıda N-2 aranır.

### N-1-1, N-2 ve ortak mod

| Durum | Ne olur? | Neden önemli? |
| --- | --- | --- |
| N-1-1 | Bir eleman bakımdayken ikinci eleman arızalanır. | Yaz bakımı ile yaz puantı çakışırsa asıl risk budur. |
| N-2 | İki eleman aynı anda devre dışı kalır. | Ortak nedenli olaylar bu sınıfa girer. |
| Ortak mod | Ortak direkte çift devre, ortak koridor, ortak kesici arızası. | Bağımsız iki arıza değildir; olasılığı iki bağımsız arızadan yüksektir. |

> **Sade anlatım:** Aynı direği paylaşan iki hat, iki ayrı şanssızlık değildir. Direk düşerse ikisi birden gider.

### Bara arızası

Bara arızası N-1'in ağır halidir. Bara, birçok hattın ve trafonun bağlandığı ortak iletkendir; o giderse bağlı her şey etkilenir.

Kesici ve yarım düzen (breaker-and-a-half), bara arızasında kaybı sınırlamak için vardır. Model barayı tek düğüm görüyorsa bu arızayı temsil edemez.

## Tarama

Türkiye iletiminde eleman sayısı binlerle ölçülür. Her biri için tam AC (alternatif akım, tam doğrusal olmayan) analiz artı dinamik simülasyon, işletme döngüsüne sığmaz.

YTBS (Yük Tevzi Bilgi Sistemi, MAM'ın enerji yönetim platformu) duyurusundaki “4000'den fazla arıza simülasyonu” bu işin endüstriyel ölçeğidir. MAM, TÜBİTAK Marmara Araştırma Merkezi'dir.

Çözüm, işi katmanlara bölmektir. Her katman bir öncekinin elediği vakalarla uğraşır:

1. **Liste.** Topoloji, bakım, fırtına koridoru, daha önce ihlal üretmiş elemanlar. Her hattı kör taramak ile akıllı listelemek yazılım tasarımıdır.
2. **DC elek.** DC (doğru akım yaklaşımı, yalnız aktif güç ve açı kullanan doğrusal model) ile hesaplanır. LODF (Line Outage Distribution Factor, hat açma dağılım katsayısı) ile açılma sonrası akış bulunur. Termik ihlali hızlı eler. Gerilimi görmez.
3. **Sıralama.** İhlal miktarı, ihlal sayısı ve ağırlık (400 kV hat, santral çıkışı) birlikte değerlendirilir.
4. **AC doğrulama.** Elekten geçenler Newton-Raphson ile çözülür. Burada Q (reaktif güç) limiti, kademe ve gerilim görülür.
5. **Dinamik seçki.** Büyük üretim kaybı, zayıf koridor, daha önce salınım görülen kesitler için zaman tanım bölgesi veya hızlı kararlılık metriği kullanılır. Her N-1 için 10 saniyelik dinamik koşmak işletme aracında ancak seçilerek yapılır. YTBS'nin geçici hal modülü bu seçkinin ürün tarafıdır.

### Performans indeksi

Sıralama adımında klasik ölçüt performans indeksidir (PI). Her arızaya tek bir sayı verir; büyük olan önce incelenir.

```
PI = Σ (S_i / S_i,max)^(2n)
```

- `S_i`: arıza sonrası i. hattın akışı.
- `S_i,max`: o hattın limiti.
- `n`: üstel. Yüksek n, limite yakın hatları öne çıkarır.

Elle örnek ve üssün etkisi `02` sayfasındadır.

## Önleyici ve düzeltici

Arızaya iki zamanda hazırlanabilirsin: arızadan önce veya arızadan sonra.

| | Önleyici kontrol | Düzeltici kontrol |
| --- | --- | --- |
| Ne zaman | Arıza olmadan | Arızadan sonra |
| Ne yapar | Çalışma noktasını güvenli bölgeye çeker | İhlali sonradan giderir |
| Araçlar | Üretimi kaydır, trafo kademesini değiştir, şönt al, kısıtlı hatta akışı azalt | Üretim kaydırma, yük atma, şema (SIPS), gerilim cihazı |
| Maliyet | Arıza olmadan da ödenir | Daha ucuz işletilir, çünkü her arıza olmaz |
| Şart | — | Eylemin yetişeceği süre ve güvenilirlik kanıtlanmalıdır |

Yönetmelik ve işletme prosedürü, hangi ihlalin düzelticiye bırakılacağını söyler.

Termik limitin kısa süreli acil değeri ile sürekli değeri farklıdır. 15 dakikalık acil limit, operatöre düzeltici süre tanır. Hat bu süre boyunca biraz fazla yük taşıyabilir; operatör de bu arada müdahale eder.

### SCOPF

SCOPF (Security-Constrained Optimal Power Flow, güvenlik kısıtlı optimal güç akışı), önleyici kaydırmayı ekonomik amaçla birlikte çözer.

- **Amaç fonksiyonu:** üretim maliyeti veya kayıp.
- **Kısıtlar:** hem baz durum hem seçilmiş N-1.

Tam N-1 kısıt kümesi çok büyüktür. Pratik çözüm, önce ihlal adaylarını bulup sadece onları kısıta almaktır (contingency filtering, arıza süzme). Ayrıntı `11` ve `13` içindedir.

## Zincirleme ve SIPS

Zincirleme arıza şöyle ilerler:

1. Bir hat açılır.
2. Akış komşuya yüklenir.
3. Komşu da açar.
4. Ada oluşur.
5. Frekans çöker.

2000'lerin büyük kararmaları bu desendedir. Koruma kendi ekipmanını kurtarırken sistemi parçalayabilir.

SIPS (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması) bu döngüyü geniş alan ölçümüyle görür. Sonra daha küçük ve kontrollü bir kayıp verir: seçilmiş üretim veya yük atılır, sistemin geri kalanı kalır.

> **Sade anlatım:** SIPS, yangının yayılmasını beklemek yerine bir odayı bilerek kapatan itfaiyecidir. Küçük bir kayıp, büyük kararmayı önler.

### SIPS tasarım soruları

- Hangi koridor, hangi ölçüm, hangi eşik?
- Eylem yük atma mı, üretim kısıntısı mı, ada kontrolü mü?
- Yanlış tetik ve kaçırılmış tetik maliyeti nedir?
- Haberleşme gecikmesi eylemi anlamsız kılıyor mu? Kararlılık eylemi yüz milisaniye–birkaç saniye penceresindedir. Dakikalık SCADA (Supervisory Control and Data Acquisition, denetleyici kontrol ve veri toplama) bu pencereye yetişmez. PMU (Phasor Measurement Unit, fazör ölçüm birimi) ve yerel şema yetişir.
- Eylem sonrası sistem N-1'e geri dönebiliyor mu?

MAM SIPS sayfası tam olarak bu katmanı anlatır: PMU sınıfı senkron veri, otomatik eylem, kayıt, operatör arayüzü.

## Belirsizlik

Tek bir yük akışı “güvenli” diyebilir. Ama şu üç şey bu sonucu bozar:

- Yük tahmin hatası
- Rüzgâr sapması
- Plansız devre dışı kalma

İşletme aracı en azından yakın senaryoları koşar:

- Tahmin üst bandı
- En büyük yenilenebilir sapması
- Planlı bakım

Stokastik güvenlik, her N-1'e bir olasılık bağlar. Ürün tarafında bunun sade hali, “kritik senaryo seti”dir.

> **Mülakatta şöyle söyle:** Stokastik optimizasyon anlatıp ürünü unutma; önce senaryo setini söyle.

## Rapor

Operatörün okuyacağı çıktı Jacobian değildir. Jacobian, Newton-Raphson'un iç matrisidir; operatöre bir şey söylemez. Rapor şunları içermelidir:

- İhlal eden eleman, yüzde, limit türü (sürekli, acil)
- Hangi arıza bu ihlali doğurdu
- Önerilen düzeltici: hangi santral, hangi yönde, kaç MW
- Gerilim için hangi bara, hangi şönt veya kademe
- Eylemin yeni ihlal doğurup doğurmadığı (düzeltici sonrası tekrar tarama)

Aşağıdaki konuşma metni sayfanın sözlü özetidir. İçindeki kısaltmalar yukarıda açıldı: N-1, DC, AC, SIPS, YTBS.

## 90 saniye

> **Mülakatta şöyle söyle:** “Güvenlik, arıza olduktan sonra limitlerin içinde kalmaktır. Türkiye kriteri N-1'de termik, gerilim, frekans, kararlılık, kullanıcı ve ada. Taramayı DC elek artı AC doğrulama artı seçilmiş dinamik diye katmanlarım. Önleyici kontrol arızadan önce maliyeti öder, düzeltici sonra öder. Zincirlemeyi SIPS, geniş alan ölçümüyle küçük ve kontrollü bir kayba çevirir. YTBS'deki güvenlik ve arıza simülasyonu bu zincirdir.”
