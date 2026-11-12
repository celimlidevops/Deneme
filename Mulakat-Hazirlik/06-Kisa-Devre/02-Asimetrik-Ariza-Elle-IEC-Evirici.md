# Asimetrik arıza

Bu sayfa üç şeyi anlatır: dengesiz arızanın simetrik bileşenlerle elle çözümü, IEC 60909 hesabı ve evirici katkısı. IEC, International Electrotechnical Commission (Uluslararası Elektroteknik Komisyonu) demektir.

## Simetrik bileşenler neden var

Üç faz kısa devrede sistem dengeli kalır; tek fazı çözersin.

Arızaların büyük çoğunluğu ise tek faz-topraktır ve dengesizdir. Dengesiz üç fazlı devreyi doğrudan çözmek, birbirine bağlı üç denklem demektir.

Fortescue'nun fikri: dengesiz herhangi bir üç faz kümesi, üç **dengeli** kümenin toplamı olarak yazılabilir.

| Dizi | Dönüş | Ne zaman oluşur |
| --- | --- | --- |
| **Doğru dizi (1)** | Normal dönüş yönü, a-b-c | Sağlıklı şebekenin kendisi. |
| **Ters dizi (2)** | Ters dönüş, a-c-b | Yalnızca dengesizlik varsa oluşur. |
| **Sıfır dizi (0)** | Üç faz aynı açıda | Yalnızca toprak yolu varsa akar. |

Aşağıdaki denklemler, dizi gerilimlerinden faz gerilimlerine geri dönüşü verir. `a`, fazörü 120° döndüren işleçtir:

```
V_a = V_0 + V_1 + V_2
V_b = V_0 + a² V_1 + a V_2             a = 1∠120°
V_c = V_0 + a V_1 + a² V_2
```

> Sade anlatım: Yazılımcı gözüyle bu bir baz değişimidir. Faz koordinatlarında birbirine bağlı olan üç denklem, dizi koordinatlarında **birbirinden bağımsız** üç devreye ayrılır. Köşegenleştirme. Her dizi devresini tek fazlı devre gibi çözer, sonra geri dönersin.

Her dizinin kendi empedansı vardır: `Z_1`, `Z_2`, `Z_0`.

Yalnızca doğru dizi devresinde gerilim kaynağı bulunur. Çünkü generatörler dengeli gerilim üretir.

## Dört arıza, dört bağlantı

Arıza türü, üç dizi devresinin arıza noktasında nasıl bağlanacağını belirler.

| Arıza | Dizi devreleri | Akım |
| --- | --- | --- |
| Üç faz | Yalnız doğru dizi | `I = E / Z_1` |
| Faz-toprak | Üçü **seri** | `I_0 = I_1 = I_2 = E / (Z_1 + Z_2 + Z_0)`, `I_f = 3 I_0` |
| Faz-faz | Doğru ve ters **paralel** (sıfır yok) | `I_1 = E / (Z_1 + Z_2)`, `I_f = √3 I_1` |
| İki faz-toprak | Doğru, (ters ∥ sıfır) ile seri | `I_1 = E / (Z_1 + Z_2 ∥ Z_0)` |

Tabloda `E` arıza öncesi gerilim, `∥` paralel bağlantıdır.

Arıza empedansı `Z_f` varsa faz-toprak formülünün paydasına `3 Z_f` eklenir.

## Elle örnek

### Veriler

- 154 kV bara.
- Arıza noktasından görülen Thevenin empedansları (100 MVA baz): `Z_1 = Z_2 = j0,2`, `Z_0 = j0,1` pu.
- Arıza öncesi gerilim 1,0 pu.

pu (per unit, birim değer), büyüklüğün baz değere oranıdır. MVA megavoltamper, kV kilovolttur. `j`, empedansın saf reaktif (endüktif) olduğunu gösterir.

Baz akım, pu sonuçları ampere çevirmek için gerekir:

```
I_baz = 100 MVA / (√3 × 154 kV) = 374,9 A
```

### 1. Üç faz

Yalnız doğru dizi devresi çalışır. Gerilimi doğru dizi empedansına bölüp baz akımla çarparak ampere geçeriz:

```
I = 1 / 0,2 = 5,00 pu = 1875 A
```

### 2. Faz-toprak

İlk satır, üç dizi devresi seri olduğu için ortak dizi akımını bulur:

```
I_0 = 1 / (0,2 + 0,2 + 0,1) = 2,00 pu
```

İkinci satır, faz akımının dizi akımının üç katı olduğunu kullanır ve ampere çevirir:

```
I_f = 3 × 2,00 = 6,00 pu = 2249 A
```

Faz-toprak akımı üç faz akımından **büyük** çıktı.

- Neden: `Z_0 < Z_1`.
- Nerede olur: yıldız noktası doğrudan topraklı büyük trafoların yakınında.
- Sonuç: kesici seçerken yalnızca üç faz akımına bakmak bu yüzden yetmez.

#### Sağlam fazın gerilimi

İlk satır, her dizi devresinde kaynak geriliminden empedans üzerindeki düşümü çıkararak dizi gerilimlerini bulur. Ters ve sıfır dizide kaynak olmadığı için yalnızca düşüm kalır.

İkinci satır, dizi gerilimlerini toplayıp arızalı fazın geriliminin sıfır olduğunu doğrular.

Üçüncü satır, dönüşüm denklemiyle sağlam b fazının gerilimini hesaplar:

```
V_1 = 1 − 0,2 × 2 = 0,6        V_2 = −0,2 × 2 = −0,4        V_0 = −0,1 × 2 = −0,2
V_a = −0,2 + 0,6 − 0,4 = 0                        (arızalı faz, beklenen)
V_b = V_0 + a² V_1 + a V_2 = −0,3 − j0,866   →   |V_b| = 0,917 pu
```

Sağlam faz gerilimi düştü.

`Z_0` büyük olsaydı (yüksek empedanslı topraklama) sağlam faz gerilimi yükselirdi. Yalıtılmış sistemde hat gerilimine (1,73 pu) kadar çıkardı.

Topraklama türü, arıza akımı ile aşırı gerilim arasındaki takastır.

| Topraklama | Arıza akımı | Sağlam faz gerilimi |
| --- | --- | --- |
| Doğrudan (küçük `Z_0`) | Büyük | Düşer |
| Yüksek empedanslı / yalıtılmış (büyük `Z_0`) | Küçük | Yükselir, 1,73 pu'ya kadar |

### 3. Faz-faz

İlk satır, doğru ve ters dizi paralel bağlı olduğu için doğru dizi akımını bulur. Sıfır dizi devreye girmez:

```
I_1 = 1 / (0,2 + 0,2) = 2,50 pu
```

İkinci satır, faz akımını `√3` katsayısıyla bulur ve ampere çevirir:

```
I_f = √3 × 2,50 = 4,33 pu = 1623 A
```

`Z_1 = Z_2` iken faz-faz akımı, üç faz akımının `√3/2 = 0,866` katıdır. Akılda tutmaya değer.

### 4. İki faz-toprak

Her satırın işlevi:

1. Ters ve sıfır dizinin paralel eşdeğerini bulur.
2. Doğru dizi akımını, doğru dizi empedansı ile bu paralel eşdeğerin seri toplamından bulur.
3. Doğru dizi akımını akım bölücüyle ters diziye paylaştırır.
4. Aynı akım bölücüyle sıfır dizi payını bulur.
5. Toprağa akan akımı sıfır dizi akımının üç katı olarak bulur ve ampere çevirir.
6. Arızalı fazlardan birinin akımını verir.

```
Z_2 ∥ Z_0 = (0,2 × 0,1) / 0,3 = 0,0667
I_1 = 1 / (0,2 + 0,0667) = 3,75 pu
I_2 = −3,75 × 0,1 / 0,3 = −1,25 pu
I_0 = −3,75 × 0,2 / 0,3 = −2,50 pu
Toprak akımı = 3 × 2,50 = 7,50 pu = 2812 A
Arızalı faz akımı = 5,73 pu
```

### Özet

| Arıza | pu | A |
| --- | --- | --- |
| Üç faz | 5,00 | 1875 |
| Faz-toprak | 6,00 | 2249 |
| Faz-faz | 4,33 | 1623 |
| İki faz-toprak (toprak akımı) | 7,50 | 2812 |

Sayıların tamamı `14-Programlama/ornekler/elle_ornekler.py` ile doğrulanmıştır.

## IEC 60909 ve c katsayısı

### Neden bir kısayol gerekir

Yukarıdaki hesap arıza öncesi gerilimi 1,0 pu aldı. Gerçekte arıza öncesi gerilim, yük ve kademe konumu bilinmez.

Tam yöntem (süperpozisyon) arıza öncesi yük akışı ister.

IEC 60909 bunun yerine standart bir kısayol tanımlar:

- Arıza noktasına **eşdeğer gerilim kaynağı** `c × U_n / √3` konur.
- Diğer bütün kaynaklar kısa devre edilir.
- Yükler ve hat kapasiteleri ihmal edilir.

Başlangıç simetrik kısa devre akımı, bu eşdeğer kaynağın kısa devre empedansına bölünmesiyle bulunur. `U_n` anma hat gerilimi, `Z_k` kısa devre empedansıdır:

```
I"k = c × U_n / (√3 × Z_k)
```

`c`, bu ihmallerin ve gerilim değişiminin güvenli tarafta kalmasını sağlayan katsayıdır.

| Gerilim | `c_max` (en büyük akım) | `c_min` (en küçük akım) |
| --- | --- | --- |
| Alçak gerilim (1 kV'a kadar) | 1,05 veya 1,10 (gerilim toleransına göre) | 0,95 |
| 1 kV üstü | 1,10 | 1,00 |

### İki hesap, iki amaç

- **En büyük akım (`c_max`):** ekipman dayanımı. Kesicinin kesme kapasitesi, baranın mekanik ve ısıl dayanımı.
- **En küçük akım (`c_min`):** koruma duyarlılığı. Röle en zayıf arızayı da görebilmeli.

### Elle

Aynı bara. İlk adım, pu empedansı baz empedansla (154² / 100 = 237,16 Ω) çarpıp ohm'a çevirir:

```
Z_k = 0,2 pu × 237,16 Ω = 47,43 Ω
```

İkinci adım, 1 kV üstü için `c_max = 1,1` alıp IEC formülünü uygular:

```
I"k = 1,1 × 154 / (√3 × 47,43) = 2,062 kA
```

`c` olmadan 1,875 kA bulmuştuk; fark tam %10'dur.

### Standardın diğer büyüklükleri

| Sembol | Anlamı |
| --- | --- |
| `I"k` | Başlangıç simetrik akımı |
| `i_p` | Tepe akımı: `κ × √2 × I"k`. Doğru akım bileşeni yüzünden ilk tepe daha yüksektir; `κ` R/X oranına bağlıdır. |
| `I_b` | Kesme akımı |
| `I_k` | Sürekli akım |
| `I_th` | Isıl eşdeğer akım |

R/X, direncin reaktansa oranıdır. Standart ayrıca trafo ve generatör empedanslarına düzeltme katsayıları (`K_T`, `K_G`) uygular.

## Evirici tabanlı üretimin arıza katkısı

Senkron generatör, arızada fiziği gereği anma akımının 5–10 katını verir. Manyetik alanındaki enerjiyi boşaltan bir gerilim kaynağıdır.

Evirici ise yarı iletkenlerini korumak için akımını **kontrol yazılımıyla** sınırlar.

| | Senkron generatör | Evirici (güneş, tam dönüştürücülü rüzgâr, batarya) |
| --- | --- | --- |
| Arıza akımı | Anma akımının 5–10 katı | Tipik olarak 1,0–1,2 katı |
| Davranış | Empedans arkasında gerilim kaynağı | Sınırlı akım kaynağı |
| Belirleyen | Makine reaktansları | Kontrol algoritması ve şebeke kodu |
| Ters dizi akımı | Doğal olarak var | Kontrole bağlı; çoğu zaman bastırılır |

### Elle örnek

154 kV'a bağlı 50 MVA santral.

İlk adım, santralin anma akımını bulur; iki kaynağı bu akımın katı olarak karşılaştıracağız:

```
50 MVA / (√3 × 154 kV) = 187,4 A
```

İkinci adım, iki kaynağın arıza akımını anma akımıyla çarparak bulur:

- Senkron, `X"d = 0,2 pu`: `1 / 0,2 = 5 pu` → **937 A**
- Evirici, 1,2 pu sınır: **225 A**

Aynı kurulu güç, dörtte bir arıza akımı.

### Korumaya etkisi

1. **Aşırı akım rölesi.** Arıza akımı yük akımına yaklaşır; röle arızayı yükten ayıramaz. Evirici ağırlıklı adada aşırı akım koruması çalışmayabilir.
2. **Mesafe rölesi.** Akım sınırlı ve açısı kontrolle belirlendiği için ölçülen empedans yanlış çıkar; erişim kısalır veya uzar.
3. **Yön ve faz seçimi.** Ters dizi büyüklüklerine dayanan elemanlar, evirici ters dizi akımı vermediğinde yanlış karar verir.
4. **Düşen kısa devre gücü.** Senkron santraller devreden çıktıkça şebeke zayıflar: gerilim daha çok oynar, evirici kontrolü kararsızlaşabilir. Ölçüsü kısa devre oranıdır (SCR, Short Circuit Ratio).
5. **Dağıtımda körleme ve yanlış açma.** Fider ortasındaki üretim, fider başındaki rölenin gördüğü akımı azaltır (körleme). Ya da komşu fider arızasına katkı vererek sağlam fideri açtırır.

### Çözüm yönleri

- Şebeke kodunun arıza sırasında reaktif (ve ters dizi) akım enjeksiyonu istemesi
- Diferansiyel ve haberleşmeli koruma
- Uyarlamalı ayar
- Senkron kompanzatör
- Şebeke kuran evirici

### Standart tarafı

IEC 60909'un 2016 baskısı tam dönüştürücülü üniteleri akım kaynağı olarak hesaba katar.

Türkiye şebeke yönetmeliğinin arıza sırasında istediği reaktif akım eğrisinin sayılarını **doğrulamadım**; rakam verme (`17/02`).

## Yaygın yanlış

| Yanlış cümle | Doğrusu |
| --- | --- |
| **"En büyük arıza akımı her zaman üç fazdır."** | `Z_0 < Z_1` ise faz-toprak daha büyüktür. Örnekte 6 pu'ya karşı 5 pu. |
| **"Faz-toprak akımı `I_0`'dır."** | `3 I_0`'dır. |
| **"Faz-faz arızada sıfır dizi akar."** | Toprak yolu yoktur, akmaz. |
| **"c katsayısı bir güvenlik payıdır, keyfe göre seçilir."** | Standartta tanımlıdır ve amaca göre (en büyük, en küçük) seçilir. |
| **"Evirici arıza akımına katkı vermez."** | Verir; ama küçük, sınırlı ve kontrolle belirlenen bir akım. |
| **"Kısa devre gücü düşükse şebeke daha güvenlidir."** | Ekipman için evet; gerilim kararlılığı, koruma ve evirici kontrolü için zayıf şebeke demektir. |

## Panel takip sorusu

**"Dizi devrelerini neden seri bağlıyoruz?"**

> Mülakatta şöyle söyle: Faz-toprak arızasının sınır koşulları `I_b = I_c = 0` ve `V_a = 0`'dır. Bunları dizi büyüklüklerine çevirince `I_0 = I_1 = I_2` ve `V_0 + V_1 + V_2 = 0` çıkar; bu, seri bağlantının tanımıdır.

**"Yazılımda faz-toprak akımı sıfır çıkıyor, neden?"**

> Mülakatta şöyle söyle: Sıfır dizi yolu kapalı. Trafo bağlantı grubu, nötr topraklaması veya sıfır dizi empedans verisi eksik.

Aşağıdaki konuşma metni sayfanın özüdür: dizi devreleri, bağlantı kuralı, `Z_0` etkisi, IEC 60909 ve evirici.

## 90 saniye

> "Dengesiz arızayı simetrik bileşenlerle çözerim: sistemi doğru, ters ve sıfır dizi devrelerine ayırırım; bu üç devre birbirinden bağımsızdır. Arıza türü devrelerin bağlantısını belirler: üç fazda yalnız doğru dizi, faz-toprakta üçü seri, faz-fazda doğru ve ters paralel. Sıfır dizi empedansı küçükse faz-toprak akımı üç fazdan büyük çıkar. IEC 60909, arıza noktasına c katsayılı eşdeğer kaynak koyar; en büyük akımla ekipmanı, en küçük akımla korumayı sınarım. Evirici akımını anma değerinin biraz üstünde sınırlar; bu, aşırı akım ve mesafe korumasını zorlar."
