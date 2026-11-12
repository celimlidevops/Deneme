# Koruma ve topraklama

Bu sayfa korumanın genel çerçevesini anlatır. Önce iyi bir korumanın dört niteliğini, sonra röle ailelerini, koordinasyonu, eviricinin (inverter) korumaya etkisini ve en sonda topraklamayı göreceksin. Sayılı ve elle hesaplı derin anlatım `02-Koordinasyon-CTI-Mesafe-Evirici.md` dosyasındadır.

> **Sade anlatım:** Koruma, şebekenin sigortasıdır ama akıllı bir sigortadır. Bir yerde kısa devre olunca yalnız o parçayı, olabildiğince çabuk ve doğru yerden keser. Topraklama ise o arıza akımını toprağa, çevredeki insanı çarpmadan akıtmanın yoludur.

## Dört nitelik

Bir koruma sistemi dört ölçütle değerlendirilir:

| Nitelik | Ne ister | Ek not |
| --- | --- | --- |
| **Seçicilik** | Yalnız arızalı eleman ayrılsın. | Sağlam kısımlar enerjili kalır. |
| **Hız** | Arıza süresi kısa olsun. | Kararlılık ve hasar, süreyi kısaltır. Geçici hal CCT'si (Critical Clearing Time, kritik temizleme süresi) koruma süresinin üstündedir. |
| **Duyarlılık** | En küçük makul arızayı görsün. | Asgari kısa devre burada kullanılır. |
| **Güvenilirlik** | Çalışması gereken yerde çalışsın (dependability), çalışmaması gereken yerde suskun kalsın (security). | İkisi ters yöndedir. Çok hassas röle yanlış açar. |

Hız satırını açalım: arıza ne kadar uzun sürerse ekipman o kadar hasar görür ve generatörler senkronizmadan o kadar kolay kopar. CCT, arızanın sistem kararsız olmadan en geç ne zaman temizlenmesi gerektiğidir. Koruma bu süreden önce işini bitirmelidir.

Güvenilirlik satırını açalım: "her arızada mutlaka aç" (dependability) ile "arıza yokken asla açma" (security) birbirini çeker. Röleyi çok hassas yaparsan birinciyi kazanır, ikinciyi kaybedersin.

### Yedek koruma ve kesici arıza koruması

Yedek koruma, birincil röle veya kesici arızalanırsa devreye girer. Yedek daha yavaş ve daha geniş bölgeli olmak zorundadır. Yavaş olmalıdır ki önce asıl korumaya fırsat tanısın. Geniş olmalıdır ki asıl korumanın bölgesini de kapsasın.

Kesici arıza koruması (CBF, Circuit Breaker Failure), açma emri gittiği halde akım kesilmezse komşu kesicileri açar.

## Röle aileleri

Röle, ölçü trafoları üzerinden akımı ve gerilimi izleyen, arıza görünce kesiciye açma emri veren cihazdır. Başlıca aileler aşağıdadır.

### Aşırı akım

Akım, ayarlanmış eşiği geçince röle zaman saymaya başlar: `I > I_pickup` ise zaman sayar. `I_pickup`, rölenin "uyandığı" (çalışmaya başladığı) akım değeridir.

| Tür | Davranış |
| --- | --- |
| Sabit zaman | Kademelidir: eşik aşılınca hep aynı gecikmeyle açar. |
| Ters zaman | Akım büyüdükçe hızlanır; sigortayla koordinasyonu kolaydır. |
| Yönlü aşırı akım | Akımın yönüne de bakar; halka ve çift beslemede şarttır. |

Dağıtım fiderinin (dağıtım hattının) klasik aracı budur. Üretim katkısı arttıkça pickup ve zaman eğrisi yeniden çizilir, çünkü arıza akımları değişir.

### Mesafe

Mesafe rölesi, ölçtüğü gerilimi ölçtüğü akıma böler. Görülen empedans `Z = V/I` hattın empedansına bölününce mesafe olur. Hattın empedansı boyuyla orantılı olduğu için bu oran arızanın ne kadar uzakta olduğunu verir.

Tipik bölge uygulaması aşağıdadır. Sayılar şirket standardına göre kayar. Mülakatta tipik değer söyle ve "TEİAŞ (Türkiye Elektrik İletim A.Ş.) ayar değeri standarttır" diye kes.

| Bölge | Erişim ve gecikme | Neden |
| --- | --- | --- |
| Bölge 1 | Hat empedansının yaklaşık %80'i, gecikmesiz. | %100 yapılmaması, ölçü hatasının bir sonraki barayı içine almasını önler. |
| Bölge 2 | Hattın tamamı artı bir sonraki en kısa hattın bir kısmı, yaklaşık 0,3–0,5 s. | Karşı uç yedeği. |
| Bölge 3 | Daha geniş yedek, daha uzun gecikme. | Yük istilası (load encroachment) riski taşır. |

Yük istilası şudur: ağır yük, bölge 3'ün içine empedans olarak girebilir. Yani arıza olmadığı halde yükün empedansı röleye arıza gibi görünür. Yük blinder'ı (yük körleyicisi) bunu keser.

**Güç salınımı.** Güç salınımı, empedansın röle düzleminde daire çizmesidir. Generatörler birbirine göre salındıkça röle değişen bir empedans görür. Salınım bloğu, kararlı salınımda açmayı engeller, gerçek arızada bırakır.

Yanlış bölge 3 açması zincirleme arızanın klasik tetiğidir. SIPS'in (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması) var olma nedenlerinden biri, rölelerin yerel doğruyu yapıp sistemi bölmesidir. Her röle kendi açısından haklıdır ama toplam sonuç sistemin parçalanması olabilir.

### Diferansiyel

Diferansiyel koruma, koruma bölgesine giren ve çıkan akımın farkına bakar. Sağlam durumda giren akım çıkan akıma eşittir. Fark varsa akım bölgenin içinde bir yere kaçıyordur, yani arıza içeridedir. Uygulandığı yerler: hat, trafo, bara.

Yanılma kaynakları ve çareleri:

| Sorun | Ne olur | Çare |
| --- | --- | --- |
| Haberleşme gecikmesi ve CT (Current Transformer, akım trafosu) doyması | Dış akımı (bölge dışındaki arızayı) iç arıza gibi taklit eder. | Tutma (restraint) eğrisi, dış arızada yanlış açmayı keser. |
| Trafo mıknatıslanma akımı (inrush) | Trafo enerjilenirken yalnız bir sargıdan akım akar, fark varmış gibi görünür. | Trafo diferansiyeli ikinci harmonik tutması kullanır. |

Bara diferansiyeli, bara arızasını N-1'in (bir elemanın devre dışı kaldığı durumun) ağır halinden hızla çıkarır.

### Frekans ve gerilim

| Koruma | Ne yapar |
| --- | --- |
| Düşük frekans | Yük atma |
| Yüksek frekans | Üretim kısıntısı |
| RoCoF (Rate of Change of Frequency, frekansın değişim hızı) | Ada veya kayıp şebeke tespiti |
| Düşük gerilim | Yük atma |

Eşikler sistem koruma planındadır, fider rölesinin keyfi değildir. Yani bu değerleri tek bir fiderin mühendisi değil, bütün sistemi planlayan kurum belirler.

Düşük atalette RoCoF büyür. Atalet, dönen kütlelerin frekans değişimine direncidir; evirici ağırlıklı şebekede azalır. Dağıtık üretim RoCoF ile kendini ayırırsa üretim tam da ihtiyaç anında gider.

## Koordinasyon

Koordinasyon, arka arkaya dizilmiş koruma cihazlarının doğru sırayla açmasını sağlamaktır.

Zaman-akım eğrisi üst üste bindirilir. Aşağıdaki cihaz (arızaya yakın olan) yukarıdakinden, tüm arıza akımı aralığında bir zaman marjı (çoğunlukla 0,2–0,3 s artı kesici süresi) kadar önce açar.

Sigorta eğrisi, röle eğrisi ve OTK (otomatik tekrar kapama) sayısı aynı grafiğe çizilir. Yazılım (ETAP, PowerFactory protection, CYMTCC) eğriyi çizer; mühendis marjı ve istisnayı okur.

### Otomatik tekrar kapama (OTK)

Hatlardaki arızaların bir kısmı geçicidir (örneğin hatta değen dal). OTK, kesici açtıktan sonra hattı kendiliğinden yeniden kapatır. Sırası:

1. Ölü zaman (hattın enerjisiz beklediği süre).
2. Kapama.
3. Varsa ikinci deneme.
4. Sonra kilit (arıza kalıcı sayılır, kesici açık kalır).

Dağıtık üretim ölü zamanda adayı söndürmelidir. Söndürmezse kesici, şebekeyle senkron olmayan bir adayı yeniden bağlar. Senkron olmayan kapama, mekanik moment üretir.

### Haberleşmeli hat koruması

Haberleşmeli hat koruması bölge 1'i hattın yüzde 100'üne çıkarmak için kullanılır. İki uçtaki röle birbirine haber gönderir:

- **İzinli şema:** karşı uç da arızayı görüyorsa izin ver.
- **Blokaj şeması:** karşı uç arızayı görmüyorsa (arıza dışarıdaysa) blokaj.

Fiber veya kuranportör (enerji hattı üzerinden taşıyıcı frekanslı haberleşme) giderse şema yedek bölgeye düşer. Haberleşme arızası korumasız bırakmamalıdır.

## Evirici

Güneş ve rüzgâr santralleri şebekeye evirici (inverter) üzerinden bağlanır. Eviricinin arıza davranışı senkron generatöre benzemez:

- Kısa devre katkısı küçüktür, kontrol edilir, negatif dizi davranışı üreticiye göre değişir.
- Mesafe rölesi zayıf beslemede ve evirici kontrolünde yanlış mesafe görebilir.
- Yön, polarizasyon gerilimi çökünce bozulur. Polarizasyon gerilimi, yön elemanının akımı karşılaştırdığı referans gerilimdir.
- Şebeke oluşturan evirici arıza akımını bilinçli büyütürse koordinasyon yeniden yapılır.

Koruma çalışması "kısa devre dosyasını bir kez koştum" ile kapanmaz; kontrol modu senaryosu da koşulur. Çünkü eviricinin arıza akımı donanımdan çok kontrol yazılımına bağlıdır.

## Topraklama

Topraklama biçimi, yani trafonun nötr noktasının toprağa nasıl bağlandığı, hem can güvenliğini hem sıfır dizi akımını belirler. Sıfır dizi akımı, toprak arızasında toprak üzerinden dönen akımdır.

| Biçim | Davranış |
| --- | --- |
| Doğrudan topraklı | Büyük toprak arıza akımı, kolay algı, yüksek dokunma gerilimi riski. İletim trafolarının Y tarafı çoğunlukla böyledir. |
| Direnç üzerinden | Akım sınırlı, ark daha kolay söner, algı için hassas röle gerekir. |
| Rezonans (Peterson) | Bobin kapasitif akımı söndürür, dağıtımda geçici arızayı yaşatmadan temizleyebilir. |
| İzole | Akım kapasitiftir, küçük şebekede kalır, gerilim yükselmeleri izlenir. |

### Trafo merkezi topraklaması

Trafo merkezi topraklaması, arıza akımını toprağa güvenli yayar. Hesabın parçaları:

- Topraklama ağı direnci.
- Toprak özdirenci (Wenner ölçümü ile; dört elektrotlu standart ölçüm yöntemi).
- Adım gerilimi: yürüyen birinin iki ayağı arasına binen gerilim.
- Dokunma gerilimi: topraklı bir metale dokunan birinin eli ile ayağı arasına binen gerilim.
- Toprak potansiyel yükselmesi (GPR, Ground Potential Rise).

IEEE 80 çerçeve standarttır. İzin verilen dokunma gerilimi arıza temizleme süresine bağlıdır; koruma yavaşsa izin verilen gerilim düşer. İnsan vücudu kısa süreli akıma daha fazla dayanır, bu yüzden süre uzadıkça sınır sıkılaşır. Bu yüzden koruma süresi ile topraklama tasarımı aynı projenin iki sayfasıdır.

### Yazılımda topraklama

Yazılımda topraklama ağı, iletim yük akışının içinde çözülmez. Ayrı bir elektrot modelidir. Grubun çalışma alanları listesinde ayrı madde olarak durur.

Mülakatta şu cümle yeter:

> **Mülakatta şöyle söyle:** "Kısa devre akımını alırım, temizleme süresine göre adım ve dokunma gerilimini IEEE 80 ile kontrol ederim, aşım varsa iletken sıklaştırırım veya yüzeye yüksek özdirençli kaplama koyarım."

Elektrot elektrot mesh çizmeyi iddia etme, yapmadıysan.

### Sıfır dizi bağlantısı

Sıfır dizi empedansı, guard teli (hattın üstündeki koruma teli), kule ayağı ve nötr topraklama direncinden gelir. Koruma ayarı ile topraklama modeli birbirini besler: toprak arıza rölesinin göreceği akım, topraklama modelinden çıkan sıfır dizi empedansına bağlıdır.

## 90 saniye

“Koruma seçici, hızlı, duyarlı ve güvenilir olmalı; yedek daha yavaş ve daha geniş. İletimde mesafe bölgeleri ve salınım bloğu, dağıtımda ters zaman ve OTK, kritik elemanda diferansiyel. Evirici kısa devreyi senkron makine gibi beslemez. SIPS yerel rölenin üstünde sistem bütünlüğü katmanıdır. Topraklama biçimi sıfır dizi akımını belirler; adım ve dokunma gerilimi arıza süresiyle birlikte IEEE 80’e bakılır.”
