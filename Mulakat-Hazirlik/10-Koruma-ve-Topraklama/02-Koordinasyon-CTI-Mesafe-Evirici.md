# Röle koordinasyonu

Bu sayfanın konuları: zaman-akım eğrileri, CTI, mesafe bölgeleri, evirici ağırlıklı şebeke. CTI (Coordination Time Interval), Türkçesiyle koordinasyon zaman aralığıdır: yedek rölenin asıl röleden ne kadar geç açması gerektiğini söyler. Konular dört elle hesaplı örnekle anlatılır.

> **Sade anlatım:** Bir hatta arka arkaya birkaç röle dizilidir. Arıza olunca arızaya en yakın röle önce açmalı, arkadakiler biraz bekleyip "o açtı mı?" diye bakmalıdır. Koordinasyon, bu bekleme sürelerini ve eşiklerini doğru ayarlama işidir.

## Korumanın dört ölçütü

| Ölçüt | Ne ister |
| --- | --- |
| **Seçicilik** | Yalnız arızalı kısım ayrılmalı; arızaya en yakın kesici açmalı. |
| **Hız** | Ekipman hasarı ve kararlılık için hızlı açmalı (`08` klasörü: kritik temizleme süresi). |
| **Duyarlılık** | En küçük arıza akımını bile görmeli. |
| **Güvenilirlik** | Gerektiğinde açmalı (bağımlılık), gerekmediğinde açmamalı (emniyet). |

Bu dördü birbiriyle çatışır. Örneğin çok duyarlı bir röle, arıza olmayan durumda da açabilir. Koordinasyon, aralarındaki dengeyi kurma işidir.

**Yazılımcı benzetmesi: zaman aşımı zinciri.** Çağrı zincirinde en içteki servisin zaman aşımı en kısa, dıştakilerin giderek uzun olmalıdır; yoksa iç servis yanıt veremeden dış katman bütün isteği düşürür. Radyal fiderde röleler aynı mantıkla sıralanır. Radyal fider, tek yönden beslenen, dallanarak yüke giden hattır.

## Ters zamanlı aşırı akım rölesi

Akım ne kadar büyükse o kadar hızlı açar. Bu davranışın standart eğrileri IEC 60255'te (IEC: International Electrotechnical Commission, Uluslararası Elektroteknik Komisyonu) tanımlıdır.

Aşağıdaki formül, rölenin açma süresini arıza akımına göre verir. `M`, arıza akımının ayar akımına oranıdır (ayarın kaç katı akım aktığı).

```
t = TMS × k / (M^α − 1)          M = I_arıza / I_ayar
```

`k` ve `α` sabitleri eğri tipine göre değişir:

| Eğri | `k` | `α` | Kullanım |
| --- | --- | --- | --- |
| Standart ters (SI, Standard Inverse) | 0,14 | 0,02 | Genel |
| Çok ters (VI, Very Inverse) | 13,5 | 1 | Arıza akımı mesafeyle hızlı düşüyorsa |
| Aşırı ters (EI, Extremely Inverse) | 80 | 2 | Sigortalarla koordinasyon, soğuk yük alma |

`α` büyüdükçe eğri dikleşir: büyük akımda çok hızlı, küçük akımda çok yavaş açar.

### İki ayar

- **Akım ayarı `I_ayar`:** rölenin çalışmaya başladığı akım. En büyük yük akımının üstünde, en küçük arıza akımının altında olmalı. Böylece normal yükte açmaz, en zayıf arızayı da görür.
- **Zaman çarpanı `TMS` (Time Multiplier Setting):** eğriyi zaman ekseninde aşağı yukarı kaydırır. Eğrinin şeklini değil, ne kadar geç açtığını değiştirir.

Ek olarak **ani eleman:** akım çok büyükse gecikmesiz açar. Yalnız kendi bölgesindeki arızada o akıma ulaşılacak şekilde ayarlanır. Böylece komşu bölgedeki arızada gecikmesiz açıp seçiciliği bozmaz.

## Koordinasyon zaman aralığı (CTI)

Arkadaki (yedek) röle, öndeki (asıl) röleden en az CTI kadar geç açmalıdır. Bu süre, asıl rölenin ve kesicinin işini bitirmesine yetmelidir. İçinde ne var:

| Bileşen | Tipik |
| --- | --- |
| Kesici açma süresi | 50–100 ms |
| Rölenin aşma süresi (elektromekanikte) | 0–50 ms |
| Röle ve akım trafosu zaman hatası | 50–100 ms |
| Güvenlik payı | 50–100 ms |
| **Toplam** | **0,2–0,4 s** |

Aşma süresi (overshoot), elektromekanik rölede akım kesildikten sonra diskin ataletle bir süre daha dönmesidir.

| Röle tipi | Kullanılan CTI |
| --- | --- |
| Sayısal röle | 0,2–0,3 s |
| Elektromekanik röle | 0,3–0,4 s |

**Bedeli:** her kademe 0,3 s ekler. Beş kademeli bir fiderde kaynağa en yakın röle, arıza akımının en büyük olduğu yerde, en geç açan röledir. Ters zamanlı eğri bu sorunu hafifletir; ani eleman ve haberleşmeli koruma çözer.

## Elle örnek 1: iki rölenin koordinasyonu

**Durum:** Radyal fider: kaynak → röle A → röle B → yük. B'nin hemen ötesinde arıza, arıza akımı 2000 A. İkisi de standart ters eğri (`k = 0,14`, `α = 0,02`).

### Röle B (asıl)

Ayarlar: `I_ayar = 200 A`, `TMS = 0,10`.

Aşağıdaki blok B'nin açma süresini üç adımda hesaplar:

1. `M = 2000 / 200 = 10` satırı, arıza akımının B'nin ayarının kaç katı olduğunu bulur.
2. `10^0,02 = 1,0471` satırı, formüldeki `M^α` terimini hesaplar.
3. Son satır bu değerleri formüle koyar: önce `0,14 / (1,0471 − 1)` bölümü (2,971) bulunur, sonra `TMS = 0,10` ile çarpılarak B'nin açma süresi elde edilir.

```
M = 2000 / 200 = 10
10^0,02 = 1,0471
t_B = 0,10 × 0,14 / (1,0471 − 1) = 0,10 × 2,971 = 0,297 s
```

### Röle A (yedek)

Ayarlar: `I_ayar = 400 A`. CTI = 0,3 s isteniyor. Bilinmeyen, A'nın `TMS` değeridir.

Aşağıdaki blok A'nın gereken `TMS` değerini beş adımda bulur:

1. "Gereken süre" satırı, B'nin süresine CTI'yı ekleyerek A'nın en erken ne zaman açabileceğini bulur.
2. `M = 2000 / 400 = 5` satırı, aynı arıza akımının A'nın ayarının kaç katı olduğunu bulur.
3. `5^0,02 = 1,0327` satırı, A için `M^α` terimini hesaplar.
4. "TMS = 1 iken süre" satırı, eğrinin çarpansız (TMS = 1) halinde A'nın ne kadar sürede açacağını bulur.
5. "Gereken TMS" satırı, istenen süreyi çarpansız süreye bölerek TMS'yi bulur; çünkü süre TMS ile doğru orantılıdır.

```
Gereken süre: t_A = 0,297 + 0,300 = 0,597 s
M = 2000 / 400 = 5
5^0,02 = 1,0327
TMS = 1 iken süre = 0,14 / 0,0327 = 4,280 s
Gereken TMS = 0,597 / 4,280 = 0,1395
```

**Seçim:** `TMS = 0,14`. Hesaplanan 0,1395 bir üst ayar adımına yuvarlanır, çünkü aşağı yuvarlamak aralığı CTI'nın altına düşürür. Röle A 0,599 s'de açar; aralık 0,302 s. Koşul sağlandı.

### Kontrol edilmesi gerekenler

1. Koordinasyon **en büyük** arıza akımında yapılır, çünkü ters zamanlı eğriler orada birbirine en yakındır. Aynı tip eğride, büyük akımda tutan aralık küçük akımda da tutar.
2. A'nın akım ayarı, B'ninkinden büyük olmalı (400 > 200). Yoksa küçük akımlarda eğriler kesişir.
3. A, B'nin bölge sonundaki **en küçük** arızayı da görebilmeli (yedek koruma duyarlılığı).
4. A'nın ayarı en büyük yük akımının üstünde kalmalı.

## Mesafe koruması

İletimde aşırı akım yetmez. Üç neden vardır:

- Şebeke gözlüdür (birçok döngü içerir).
- Akım iki yönden gelir.
- Arıza akımı üretim durumuna göre değişir.

Mesafe rölesi gerilimi akıma böler ve **empedans** ölçer: `Z = V / I`. Hattın empedansı uzunluğuyla orantılı olduğundan ölçülen empedans arızaya uzaklığı verir ve kaynak gücünden büyük ölçüde bağımsızdır.

| Bölge | Erişim | Gecikme | Amaç |
| --- | --- | --- | --- |
| 1 | Hattın %80–85'i | Gecikmesiz | Asıl koruma |
| 2 | Hattın tamamı + komşu en kısa hattın %20–50'si | 0,3–0,5 s | Hattın kalan kısmı ve karşı bara |
| 3 | Komşu hattın tamamını kapsayacak kadar | 0,8–1,5 s | Uzak yedek |

**Neden %80:** ölçü trafosu hataları, hat empedans verisindeki belirsizlik ve röle hatası toplamda %10–15'e varır. %100 ayarlansa röle, komşu hattın başındaki arızayı kendi hattında sanıp gecikmesiz açabilir (aşırı erişim). Seçicilik bozulur.

Kalan %15–20'deki arıza 2. bölgede gecikmeli temizlenir. Bunu hızlandırmak için iki uç haberleşir (izinli veya bloklamalı şemalar) ya da hat diferansiyel koruması kullanılır.

### Elle örnek 2: ikincil empedans

Röle, ölçü trafolarının ikincil tarafını görür. Yani röleye şebekenin gerçek akımı ve gerilimi değil, küçültülmüş kopyası gelir. Ayar da bu küçültülmüş tarafta yapılır.

**Durum:** 154 kV hat, birincil empedans 40 Ω. Akım trafosu (AT) 1000/1 A, gerilim trafosu (GT) 154.000/100 V.

Aşağıdaki satır, birincil empedansı rölenin gördüğü ikincil empedansa çevirir. AT oranı 1000/1 = 1000, GT oranı 154.000/100 = 1540'tır. Empedans gerilim bölü akım olduğu için AT oranı pay, GT oranı paydaya gelir.

```
Z_ikincil = Z_birincil × (AT oranı / GT oranı) = 40 × (1000 / 1540) = 25,97 Ω
```

Sonraki adım bölge 1 ayarını bulur: ikincil hat empedansı %80 ile çarpılır.

1. bölge ayarı: `0,8 × 25,97 = 20,8 Ω` ikincil.

### Elle örnek 3: ara besleme (infeed)

Ara besleme, röle ile arıza arasındaki bir baraya başka bir kaynaktan da akım girmesidir.

**Durum:** Röle A'nın hattı 40 Ω. Karşı baradan sonra komşu hatta, 10 Ω ileride arıza var. Karşı baraya başka bir kaynaktan da A'nınkine eşit akım giriyor.

Aşağıdaki blok iki empedansı karşılaştırır:

1. "Gerçek empedans" satırı, röleden arızaya kadar olan fiziksel empedansı toplar.
2. "Görülen empedans" satırı, komşu hattaki gerilim düşümünü iki akımın birlikte oluşturduğunu hesaba katar. Röle yalnız kendi akımını (`I_A`) ölçtüğü için komşu hattın 10 Ω'u `(1 + I_diğer / I_A)` katsayısıyla büyümüş görünür. Akımlar eşit olduğundan katsayı 2'dir.

```
Gerçek empedans   = 40 + 10 = 50 Ω
Görülen empedans  = 40 + (1 + I_diğer / I_A) × 10 = 40 + 2 × 10 = 60 Ω
```

Röle arızayı olduğundan **uzakta** görür (eksik erişim). 2. ve 3. bölge ayarları bu etki hesaba katılarak yapılır. Ara besleme kaynağı devre dışıysa erişim uzar; iki durum da kontrol edilir.

### Elle örnek 4: yük taşması

Yük taşması (load encroachment), arıza olmadığı halde ağır yükün empedansının röle bölgesine girmesidir.

**Durum:** 154 kV hat, 300 MVA yük taşıyor.

Aşağıdaki satır, yükün röleye görünen empedansını hesaplar. Gerilimin karesi (kV cinsinden) görünür güce (MVA cinsinden) bölünür; sonuç doğrudan ohm çıkar.

```
Z_yük = V² / S = 154² / 300 = 79 Ω
```

3. bölge uzun erişimle ayarlanmışsa (örneğin 80 Ω), ağır yük empedansı bölgenin içine girebilir. Röle arıza olmadığı halde açar, yük komşu hatlara biner, onlar da açar. Büyük sistem çökmelerinde tekrar tekrar görülen mekanizmadır.

Çare:

- Yük taşması engeli (açıya göre kör bölge). Yük empedansının açısı küçük, arıza empedansının açısı büyüktür; engel bu farka bakar.
- 3. bölge erişiminin sınırlanması.

## Diğer koruma türleri (bir cümle)

| Koruma | Ne yapar |
| --- | --- |
| **Diferansiyel** | Giren ve çıkan akımı karşılaştırır. Trafo, bara, generatör, kısa hat. Kesin seçicidir; yedek koruma sağlamaz. |
| **Yönlü aşırı akım** | Halka ve paralel fiderlerde akımın yönüne bakar. |
| **Toprak arıza koruması** | Artık akımı (`3 I_0`) ölçer; faz korumasından çok daha duyarlı ayarlanır. `I_0` sıfır dizi akımıdır. |
| **Düşük frekans yük atma** | Frekans kademeli eşiklerin altına inince yük keser. |
| **Kesici arıza koruması** | Kesici açmazsa çevredeki kesicileri açtırır. |

## Evirici ağırlıklı şebekede zorluklar

Güneş ve rüzgâr santralleri şebekeye evirici (inverter) üzerinden bağlanır. Fiziksel neden `06/02` dosyasında: evirici arıza akımını anma değerinin yaklaşık 1,0–1,2 katında sınırlar ve açısını kontrol belirler. Senkron generatör ise anma akımının birkaç katı arıza akımı verir; klasik korumalar buna göre tasarlanmıştır.

| Koruma | Sorun |
| --- | --- |
| Aşırı akım | Arıza akımı yük akımına yakın; ayar aralığı kalmaz |
| Mesafe | Akım sınırlı ve kontrollü; ölçülen empedans kayar, erişim hatası |
| Yön ve faz seçimi | Ters dizi akımı bastırılmışsa yön elemanı yanılır |
| Salınım engelleme | Evirici dinamiği klasik güç salınımına benzemez |
| Ada tespiti | RoCoF (Rate of Change of Frequency, frekansın değişim hızı) ve vektör sıçraması röleleri sistem olayında topluca açabilir |
| Dağıtım | Çift yönlü akış; körleme, yanlış açma, tekrar kapamada eşzamansız kapama |

### Elle kontrol

`06/02`'deki örnekte 50 MVA evirici santrali 225 A arıza akımı veriyordu; anma akımı 187 A. Aşırı akım ayarı yükün 1,25 katına (234 A) konursa röle **kendi arızasını göremez**.

Adım adım:

1. Anma akımı 187 A'dır; bu santralin normal en büyük akımıdır.
2. Ayar, yükün 1,25 katına konur: 187 × 1,25 ≈ 234 A. Bu, normal yükte açmamak için konan eşiktir.
3. Arıza akımı 225 A'dır; bu, 234 A'lık eşiğin altında kalır. Röle eşiği hiç aşılmadığı için arızayı görmez.

### Çözüm yönleri

- Haberleşmeli ve diferansiyel koruma (akım büyüklüğüne değil farkına bakar).
- Gerilim tabanlı ve yürüyen dalga korumaları.
- Uyarlamalı ayar grupları.
- Şebeke kodunda arıza sırasında reaktif ve ters dizi akım zorunluluğu.
- Senkron kompanzatör.
- Şebeke kuran evirici.

Koruma çalışmasının fazör modeli yerine elektromanyetik geçici hal modeliyle (EMT) ve gerçek röleyle döngüde sınanması gerekir. Fazör modeli yalnız temel frekansı izler; eviricinin hızlı kontrol davranışını göstermez.

**SIPS ile ayrım:** yukarıdakiler **ekipman** korumasıdır. SIPS (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması), ekipman koruması doğru çalıştıktan sonra **sistemin** bütünlüğünü korur.

## Yaygın yanlış

| Yanlış inanç | Doğrusu |
| --- | --- |
| **"Koruma arızayı önler."** | Önlemez; arızalı kısmı ayırır. |
| **"Kaynağa yakın röle hızlı açmalı, akım orada büyük."** | Zaman kademeli şemada en yavaş odur. Ters eğri ve ani eleman bunu hafifletir. |
| **"1. bölgeyi %100 ayarlarsam hattın tamamını korurum."** | Aşırı erişir, komşu hattın arızasında açar. |
| **"CTI küçüldükçe iyidir."** | Kesici süresinden ve hatalardan küçük olursa iki röle birlikte açar. |
| **"Koordinasyon bir kez yapılır."** | Yeni santral, yeni hat veya topoloji değişimi kısa devre akımlarını değiştirir; ayarlar yeniden doğrulanır. |
| **"Mesafe rölesi kaynak gücünden bağımsızdır."** | Ara besleme, arıza direnci ve evirici davranışı ölçümü kaydırır. |

## Panel takip sorusu

**Soru 1:** "Koordinasyonu yazılımla nasıl denetlersin?"

> **Mülakatta şöyle söyle:** Her arıza yeri ve türü için kısa devre hesabından röle akımlarını alır, her asıl–yedek çifti için açma sürelerini hesaplar, CTI'dan küçük olan çiftleri ve hiç açmayan durumları listelerim. Bunu en büyük ve en küçük üretim senaryosunda ve N-1 topolojilerinde tekrarlarım. Aslında bir kısıt denetimidir; ayarın kendisini bulmak ise optimizasyon problemidir.

N-1, herhangi bir elemanın devre dışı kaldığı durumdur.

**Soru 2:** "Arıza direnci mesafe rölesini nasıl etkiler?"

> **Mülakatta şöyle söyle:** Ark ve toprak direnci ölçülen empedansa direnç bileşeni ekler; nokta, karakteristiğin dışına kayabilir. Dörtgen karakteristik direnç yönünde daha geniş erişim sağlar.

Dörtgen (quadrilateral) karakteristik, röle düzleminde dikdörtgene benzer açma bölgesidir; daire biçimli karakteristiğe göre direnç eksenine daha fazla uzanır.

## 90 saniye

"Koruma seçici, hızlı, duyarlı ve güvenilir olmalıdır. Radyal fiderde ters zamanlı aşırı akım röleleri kullanırım: akım ayarı ve zaman çarpanı olmak üzere iki ayarı vardır. Yedek röle, asıl röleden koordinasyon aralığı kadar, tipik olarak sıfır virgül üç saniye geç açar; bu aralık kesici süresini ve hataları kapsar ve en büyük arıza akımında denetlenir. İletimde mesafe rölesi empedans ölçer: birinci bölge hattın yüzde seksenini gecikmesiz, ikinci bölge tamamını ve komşunun başını gecikmeli, üçüncü bölge uzak yedeği korur. Evirici arıza akımını sınırladığı için aşırı akım ve mesafe koruması zorlanır; diferansiyel ve haberleşmeli korumaya kayılır."
