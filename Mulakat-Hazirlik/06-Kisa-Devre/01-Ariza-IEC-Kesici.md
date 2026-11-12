# Kısa devre analizi

## Ne için yapılır

Kısa devre yük akışı değildir. Yük akışı normal işletmeyi hesaplar. Kısa devre ise arıza anını hesaplar.

Amaç, arıza anında akımın ve gerilimin ekipmanı, kesiciyi ve röleyi nasıl zorladığını görmektir.

> Sade anlatım: Bir hatta iletken toprağa ya da başka bir faza değdiğinde çok büyük bir akım akar. Kısa devre hesabı, “bu akım ne kadar büyük olur ve ekipmanım buna dayanır mı, rölem bunu fark eder mi?” sorusunu cevaplar.

Kısa devre hesabının beslediği kararlar:

- Kesici kesme akımı ve tepe dayanımı
- Bara, iletken, topraklama ve termik dayanım
- Röle görme (pick-up, rölenin çalışmaya başladığı akım eşiği) ve koordinasyon
- Yeni santral veya evirici bağlanınca kısa devre gücünün artması
- Zayıf barada korumanın arızayı görememesi

### “En büyük akım üç fazdır” ezberi

Üç faz metalik arıza (araya direnç girmeyen arıza) en büyük dengeli akımı verir sanılır. Oysa tek faz-toprak arızası, sıfır dizi empedansı küçükse ve topraklama katıysa üç fazdan büyük olabilir.

“En büyüğü üç fazdır” ezberi yanlıştır. Her iki hesabı da koştur.

### Olasılık sırası

| Arıza türü | Ne sıklıkta |
| --- | --- |
| Tek faz-toprak | En sık |
| İki faz | Daha seyrek |
| Üç faz | Daha seyrek |

Koruma her türü görmelidir. Planlama iki ayrı ölçü kullanır:

- Ekipmanı en büyük akıma göre seçer.
- Röle hassasiyetini en küçük makul arızaya göre seçer.

## Thevenin ve Zbus

Thevenin eşdeğeri, bütün şebekeyi arıza noktasından bakınca tek bir gerilim kaynağı ve tek bir seri empedansa indirir.

Arıza noktasına doğru Thevenin empedansı, o noktadan bakılan Zbus köşegenidir. Zbus, bara empedans matrisidir. Ybus ise bara admitans matrisidir.

Zbus, Ybus’un tersidir. Pratikte ters alınmaz. Bunun yerine dal ekleme veya seyrek çarpanlarla (seyrek matris ayrıştırması) çalışılır.

### Üç faz metalik arıza

Aşağıdaki formül, arıza öncesi gerilimi Thevenin empedansına bölerek arıza akımını verir:

```
I_f = V_pre / Z_th
```

Ön arıza gerilimi (V_pre) 1 pu alınabilir. pu (per unit, birim değer), büyüklüğün seçilen baz değere oranıdır.

IEC (International Electrotechnical Commission, Uluslararası Elektroteknik Komisyonu) bu gerilimi gerilim katsayısıyla (c) büyütür veya küçültür:

- Azami hesapta cmax
- Asgari hesapta cmin

Türkiye pratiğinde ekipman seçimi IEC 60909’a dayanır.

> Mülakatta şöyle söyle: “ANSI mi IEC mi?” sorusuna “ekipman ve kesici için IEC 60909, dinamik katkı için zaman tanım bölgesi veya makine modeli” diye cevap ver.

ANSI, American National Standards Institute (Amerikan Ulusal Standartlar Enstitüsü) demektir.

### Dengesiz arıza

Dengesiz arızada artı, eksi ve sıfır Zbus ayrıdır. Bunlar doğru (artı), ters (eksi) ve sıfır dizi devrelerinin empedans matrisleridir.

Arıza noktasında dizi devrelerinin nasıl bağlanacağını gösteren kural `02` klasöründeki tablodur.

Tek faz-toprak arıza akımı, üç dizi empedansının ve arıza direncinin toplamından bulunur:

```
I_f = 3 V_pre / (Z1 + Z2 + Z0 + 3 Z_f)
```

| Sembol | Anlamı |
| --- | --- |
| Z1 | Doğru (artı) dizi Thevenin empedansı |
| Z2 | Ters (eksi) dizi Thevenin empedansı |
| Z0 | Sıfır dizi Thevenin empedansı |
| Z_f | Ark ve direk topraklama direnci |

Z0’ı yanlış girmek bu akımı en çok bozan hatadır.

### Trafo bağlantı grubu ve sıfır dizi

Trafo bağlantı grubu (Yyn, Dyn, YNd) sıfır diziyi geçirip geçirmemeyi belirler.

Dyn11 gibi bir dağıtım trafosu, AG (alçak gerilim) tarafındaki toprak arızasının OG (orta gerilim) sıfır dizisine geçişini sınırlar.

Grubu boş bırakılmış model, AG arızasını iletime taşır. Yani gerçekte olmayan bir sıfır dizi akımı iletim tarafında görünür.

## Zaman

Senkron makine arıza akımı zamanla sönümlenir. Her evreyi farklı bir reaktans belirler:

| Evre | Reaktans | Ne olur |
| --- | --- | --- |
| İlk çevrimler | Alt geçici reaktans X''d | En büyük AC (alternatif akım) |
| Ardından | Geçici X'd | Akım azalır |
| Sürekli hal | Senkron reaktans Xs | Uyarma tavanı belirler |

### DC bileşen ve tepe akım

DC (doğru akım) bileşen, arıza anındaki akı sürekliliğinden gelir. Bobindeki akı bir anda değişemediği için akım dalgası bir yana kayar.

Bu bileşen X/R zaman sabitiyle söner. X/R, reaktansın dirence oranıdır.

- Tepe akım AC tepesinin üzerine biner.
- Kesicinin tepe dayanımı bu yüzden AC etkin değerinden büyüktür.
- Yüksek X/R (büyük generatör barası, trafo yanı) DC’yi uzatır; kesici asimetrisi artar.
- IEC’nin κ tepe faktörü X/R’den gelir.

### Diğer kaynaklar

| Kaynak | Arıza katkısı |
| --- | --- |
| Asenkron motor | İlk anda kaynak gibi katkı verir, hızla söner. |
| Statik yük | Katkı vermez. |
| Evirici | Akım limitine kadar katkı verir. Kontrolü arızayı “beslemeye devam” diye tasarlanmamışsa hızla keser. |
| Şebeke oluşturan (grid-forming) evirici | Bu davranışı değiştirir; klasik IEC generatör eğrisi ona uymaz. |

Yeni santral çalışmasında grid-forming davranışını ayrıca söyle.

## Azami ve asgari

İki hesap iki farklı soruyu cevaplar.

| | Azami kısa devre | Asgari kısa devre |
| --- | --- | --- |
| Soru | Ekipman ve kesici dayanır mı? | Röle görüyor mu? |
| Makineler | Tüm makineler devrede | Zayıf üretim |
| Gerilim katsayısı | cmax | cmin |
| Arıza direnci | Düşük | Dirençli arıza |
| Şebeke / topoloji | Şebeke güçlü | Hat sonu, bakım topolojisi |

Dağıtık üretim hat ucundaki kısa devreyi bazen büyütür. Bazen de evirici sınırından dolayı korumanın beklediği kadar büyütmez.

“Arıza akımı arttı, röle daha kolay görür” her zaman doğru değildir; yön ve süre değişir.

### Bara kısa devre gücü

Bara kısa devre gücü, baranın arızaya ne kadar güç basabildiğini gösterir:

```
S_sc = √3 V I_sc
```

| | Büyük S_sc (sert şebeke) | Küçük S_sc (zayıf şebeke) |
| --- | --- | --- |
| Gerilim | Gerilim çökmesi küçük | Gerilim hassas |
| Ekipman | Ekipman pahalı | — |
| Harmonik | Harmonik yayılımı kolay | — |
| Evirici | — | Evirici kararlılığı zor |
| Koruma | — | Koruma görme zayıf |

Bağlantı görüşlerinde her iki uç da sınırdır. Yenilenebilir santral “çok zayıf baraya” ve “aşırı sert baraya” ayrı takılır.

## Arıza yeri

Hat uçlarındaki akım veya empedans, arıza noktasını mesafeye çevirir.

- Çift uç yöntemi tek uçtan daha iyidir. Ara yük ve karşılıklı besleme tek ucu kaydırır.
- PMU (Phasor Measurement Unit, fazör ölçüm birimi) ile iki uç fazörü senkron ise mesafe hesabı klasik empedans rölesinden daha temizdir.
- SIPS (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması) ve geniş alan izleme bu veriyi sistem düzeyinde kullanır. Röle ise kendi bölgesinde kullanır.

## Yazılım kontrol listesi

Kısa devre yazılımında sonuca güvenmeden önce şunları sor:

- Artı, eksi, sıfır dizi ayrı mı?
- Trafo grubu ve nötr topraklama direnci girilmiş mi?
- Şönt ve hat kapasitesi kısa devrede hangi standarda göre ihmal ediliyor?
- Generatör X'' mu Xd mu? Sürekli hal reaktansıyla kesici seçilmez.
- Ön arıza yükü ihmal mi, tam yük mü? IEC belirli bir yöntemi dayatır; karışık kullanma.
- Paralel yollar ve kuplaj kesicisi topolojiyle uyumlu mu?
- Sonuç kA (kiloamper), pu ve MVA (megavoltamper) aynı bazda mı?

Aşağıdaki konuşma metni bu sayfanın özünü toplar: azami/asgari ayrımı, dizi empedansları, X/R, evirici ve IEC 60909.

## 90 saniye

> “Kısa devreyi ekipman için azami, röle için asgari koştururum. Üç faz Thevenin Z1, tek faz-toprak Z1+Z2+Z0. En büyük akım her zaman üç faz değildir. Generatör katkısı X'' ile başlar, X/R tepeyi belirler. Evirici, senkron makine gibi katkı vermez. IEC 60909 gerilim katsayısı ve empedans düzeltmesiyle kesici seçilir. Sıfır dizi ve trafo grubu boşsa sonuç çöptür.”
