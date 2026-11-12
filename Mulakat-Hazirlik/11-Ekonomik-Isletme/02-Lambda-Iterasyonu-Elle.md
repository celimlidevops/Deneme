# Lambda iterasyonu, elle

Bu sayfa ekonomik dağıtımı (ED, Economic Dispatch) anlatır: eşit artımsal maliyet ilkesi ve lambda iterasyonu, elle çözülmüş örneklerle.

## Problem

Devrede olan santraller arasında toplam yükü, toplam yakıt maliyeti en az olacak şekilde paylaştır.

Aşağıdaki blok problemin matematiksel yazımıdır: birinci satır amaç (toplam maliyeti küçült), ikinci satır güç dengesi, üçüncü satır her ünitenin üretim sınırıdır.

```
en küçük   Σ C_i(P_i)
öyle ki    Σ P_i = P_yük (+ kayıp)
           P_i,min ≤ P_i ≤ P_i,max
```

Hangi santralin devrede olacağı ayrı bir problemdir: ünite tahsisi (UC, Unit Commitment). Ekonomik dağıtım, devredekilerin **ne kadar** üreteceğini bulur.

### Maliyet eğrisi ve artımsal maliyet

Maliyet eğrisi çoğunlukla ikinci derecedendir: `C(P) = a P² + b P + c`.

Bu yazımda harfler şöyledir:

- `a`: karesel katsayı; eğrinin ne kadar dik büküldüğünü belirler.
- `b`: doğrusal katsayı.
- `c`: sabit maliyet.

Not: `01-ED-UC-OPF-Piyasa.md` aynı eğriyi `a_i + b_i P_i + c_i P_i²` diye yazar; orada `a` sabit, `c` karesel katsayıdır. Bu sayfada harflerin görevi terstir.

Maliyetin türevi **artımsal maliyettir** (IC, Incremental Cost): bir sonraki megavat-saatin maliyeti.

Aşağıdaki blok artımsal maliyeti yazar; birimi TL/MWh'tir.

```
IC(P) = dC/dP = 2a P + b          (TL/MWh)
```

## Eşit artımsal maliyet ilkesi

En ucuz noktada, sınırına dayanmamış bütün üniteler **aynı artımsal maliyette** çalışır. Bu ortak değere `λ` (lambda) denir.

> **Sade anlatım:** İki ünitenin artımsal maliyeti farklıysa, pahalı olandan 1 MW alıp ucuz olana verirsin ve toplam maliyet düşer. Bunu, fark kalmayana kadar sürdürürsün. Fark kalmadığında bütün serbest üniteler aynı λ'dadır.

### Matematiği

1. Lagrange işlevi kurulur: `L = Σ C_i(P_i) + λ (P_yük − Σ P_i)`. Bu, güç dengesi kısıtını λ çarpanıyla amaca ekler.
2. `∂L/∂P_i = 0` koşulu yazılır. Bu, her ünite için en iyi noktayı arar.
3. Sonuç `dC_i/dP_i = λ` olur. Yani her ünitenin artımsal maliyeti λ'ya eşittir.

`λ`, güç dengesi kısıtının **gölge fiyatıdır**: yük 1 MW artarsa toplam maliyet `λ` kadar artar. Piyasadaki marjinal fiyatın kökeni budur.

## Lambda iterasyonu

Lambda iterasyonu, doğru λ'yı deneme-düzeltme ile bulan yöntemdir.

1. Bir `λ` tahmin et.
2. Her ünite için `P_i = (λ − b_i) / (2 a_i)` hesapla. Sınırı aşıyorsa sınıra sabitle.
3. `Σ P_i` yükten küçükse `λ`'yı artır, büyükse azalt.
4. Fark tolerans içine girene kadar tekrarla.

İkinci adımdaki formül, `2a_i P_i + b_i = λ` denkleminin `P_i` için çözülmüş halidir.

Toplam üretim `λ` ile tekdüze (monoton) arttığı için ikiye bölme veya doğrusal ara değerleme her zaman yakınsar.

## Elle örnek 1: kayıpsız

İki ünite var, yük 100 MW.

Aşağıdaki blok iki ünitenin maliyet eğrisini (solda) ve artımsal maliyetini (sağda) verir.

```
C_1 = 0,02 P_1² + 4 P_1          IC_1 = 0,04 P_1 + 4
C_2 = 0,03 P_2² + 3 P_2          IC_2 = 0,06 P_2 + 3
```

**Tahmin 1, `λ = 5`.**

Bu adım ilk kaba tahminle her ünitenin üretimini bulur ve toplamı yükle karşılaştırır.

```
P_1 = (5 − 4) / 0,04 = 25,00
P_2 = (5 − 3) / 0,06 = 33,33
Toplam = 58,33 MW   →   100'den az, λ'yı artır
```

**Tahmin 2, `λ = 7`.**

Bu adım λ'yı artırıp toplamın yükün üstüne çıktığını görür; böylece doğru λ'nın 5 ile 7 arasında olduğu anlaşılır.

```
P_1 = 75,00       P_2 = 66,67
Toplam = 141,67 MW   →   fazla, λ'yı azalt
```

**Tahmin 3, doğrusal ara değerleme.**

Bu adım iki tahmin arasında düz çizgi çekip yükün 100 MW olduğu λ'yı okur, sonra üretimleri yeniden hesaplar.

```
λ = 5 + (7 − 5) × (100 − 58,33) / (141,67 − 58,33) = 5 + 2 × 0,5 = 6
P_1 = (6 − 4) / 0,04 = 50,00
P_2 = (6 − 3) / 0,06 = 50,00
Toplam = 100,00 MW   ✓
```

**Sonuç:** `λ = 6 TL/MWh`, `P_1 = P_2 = 50 MW`.

Toplam maliyet, iki ünitenin maliyet eğrisine 50 MW konarak bulunur: `0,02 × 2500 + 200 + 0,03 × 2500 + 150 = 475 TL/saat`.

### Kapalı çözümle kontrol

İkinci dereceden maliyette kapalı (doğrudan formülle) çözüm de vardır; kontrol için kullanılır.

Aşağıdaki blok λ'yı tek formülle hesaplar: paydaki `Σ b_i / 2a_i` = 100 + 50, paydadaki `Σ 1/2a_i` = 25 + 16,67.

```
λ = (P_yük + Σ b_i / 2a_i) / Σ (1 / 2a_i) = (100 + 100 + 50) / (25 + 16,67) = 6,00
```

Dikkat: ünite 2'nin sabit terimi daha ucuz (3'e karşı 4; burada kastedilen `b` katsayısı, yani artımsal maliyetin sıfır üretimdeki değeri) ama eğimi daha dik. "Ucuz olan hepsini üretsin" yanlıştır; önemli olan ortalama değil **marjinal** maliyettir.

## Elle örnek 2: üretim sınırı

Ünite 1'in üst sınırı 40 MW olsun. Sınırsız çözüm 50 MW istiyordu; yani sınır bağlıyor.

Aşağıdaki blok adım adım şunu yapar:

1. Ünite 1'i sınırına sabitler (40 MW).
2. Kalan yükü ünite 2'ye verir (60 MW).
3. λ'yı sınırda olmayan ünite 2'nin artımsal maliyetinden okur.
4. Ünite 1'in artımsal maliyetini hesaplayıp λ ile karşılaştırır.

```
P_1 = 40 (sabit)
P_2 = 100 − 40 = 60
λ = IC_2(60) = 0,06 × 60 + 3 = 6,60
IC_1(40) = 0,04 × 40 + 4 = 5,60   <   λ
```

Üst sınırına dayanmış ünitenin artımsal maliyeti `λ`'nın **altında** kalır: daha fazla üretmek isterdi ama üretemiyor. Alt sınırına dayanmış ünitede tersi olur. `λ`'yı sınırda olmayan (marjinal) ünite belirler.

Maliyet: `0,02 × 1600 + 160 + 0,03 × 3600 + 180 = 480 TL/saat`. Sınırın bedeli 5 TL/saat (480 − 475).

## Elle örnek 3: iletim kaybı

Ünite 1 yükten uzakta; ürettiği gücün bir kısmı hatta kayboluyor: `P_kayıp = 0,0005 P_1²`. Ünite 2 yükün yanında, kaybı yok.

Güç dengesi artık `P_1 + P_2 = 100 + P_kayıp` olur. Optimum koşulu da değişir.

Aşağıdaki blok kayıplı koşulu ve ceza faktörünün tanımını yazar.

```
IC_i × L_i = λ          L_i = 1 / (1 − ∂P_kayıp / ∂P_i)          ceza faktörü
```

Ceza faktörü: uzaktaki ünitenin 1 MW'ı yüke 1 MW olarak ulaşmaz; ünitenin etkin maliyeti o oranda artar.

Aşağıdaki blok bu örnekteki artımsal kaybı ve iki ünitenin ceza faktörünü hesaplar.

```
∂P_kayıp / ∂P_1 = 0,001 P_1        L_1 = 1 / (1 − 0,001 P_1)        L_2 = 1
```

Koşul: `(0,04 P_1 + 4) / (1 − 0,001 P_1) = 0,06 P_2 + 3`, ve `P_2 = 100 − P_1 + 0,0005 P_1²`.

Bu, tek bilinmeyenli doğrusal olmayan bir denklemdir.

### Elle iki tur deneme

Her satır bir `P_1` dener. Kaybı, `P_2`'yi, koşulun sol tarafını (ünite 1'in cezalı artımsal maliyeti) ve sağ tarafını (ünite 2'nin artımsal maliyeti) hesaplar. Hangi taraf büyükse `P_1` ona göre düzeltilir.

- Birinci tur (`P_1 = 50`): sol büyük çıkar; ünite 1 fazla pahalı, üretimi azaltılmalı.
- İkinci tur (`P_1 = 47`): sağ büyük çıkar; bu kez ünite 2 pahalı, `P_1` artırılmalı. Kök 47 ile 50 arasındadır.

```
P_1 = 50:   kayıp = 1,25   P_2 = 51,25   sol = 6,00 / 0,950 = 6,316   sağ = 6,075   →  sol büyük, P_1'i azalt
P_1 = 47:   kayıp = 1,10   P_2 = 54,10   sol = 5,88 / 0,953 = 6,170   sağ = 6,246   →  sağ büyük, P_1'i artır
```

### Sayısal çözüm

Aşağıdaki blok `elle_ornekler.py` dosyasının kök bulma ile verdiği sonuçtur.

```
P_1 = 47,72 MW      P_2 = 53,42 MW      kayıp = 1,14 MW
L_1 = 1,050         λ = 6,205 TL/MWh
```

Kayıpsız çözüme göre uzaktaki ünite 2,3 MW az, yakındaki 3,4 MW çok üretiyor. `λ` 6,00'dan 6,21'e çıktı: kayıp da üretilmek zorunda.

Gerçek sistemde kayıp `B` katsayıları (kaybı üretimlerin karesel fonksiyonu olarak veren katsayılar) ile veya doğrudan optimal güç akışıyla hesaplanır.

Ceza faktörü fikri, bölgesel marjinal fiyatın **kayıp bileşeninin** kökenidir (`13` klasörü).

## Ekonomik dağıtım, zincirin neresinde

| Problem | Soru | Ufuk | Matematik |
| --- | --- | --- | --- |
| Ünite tahsisi (UC) | Hangi ünite, ne zaman devrede | Gün öncesi | Karışık tam sayılı |
| Ekonomik dağıtım (ED) | Devredekiler ne kadar üretsin | 5–15 dakika | Dışbükey, tek kısıt |
| Optimal güç akışı (OPF, Optimal Power Flow) | Şebeke sınırlarıyla birlikte ne kadar | 5–15 dakika | Doğrusal olmayan |
| Güvenlik kısıtlı OPF | N-1 sonrası da sınırlar korunsun | 5–15 dakika | Çok büyük |

Ekonomik dağıtım şebekeyi görmez. Hat dolarsa çözümü uygulanamaz. O zaman OPF gerekir ve tek bir `λ` yerine her bara için ayrı fiyat çıkar.

Piyasa bağlantısı: serbest piyasada santraller maliyet eğrisi yerine **teklif** verir. Piyasa işletmecisi aynı eniyilemeyi teklifler üzerinden yapar. Takas fiyatı, kabul edilen son teklifin fiyatıdır; yani `λ`.

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"En ucuz santral tam kapasite çalışır, sonra ikincisi."** | Bu, sabit marjinal maliyetli (doğrusal) teklifler için doğrudur: liyakat sırası. Maliyet eğrisi ikinci derecedense ünite yüklendikçe pahalılaşır ve yük paylaşılır. |
| **"λ ortalama maliyettir."** | Marjinal maliyettir. |
| **"Sınıra dayanan ünite de λ'da çalışır."** | Üst sınırdaki ünitenin artımsal maliyeti `λ`'nın altındadır. |
| **"Sabit maliyet `c` dağıtımı etkiler."** | Türevde kaybolur; ekonomik dağıtımı değil ünite tahsisini etkiler. |
| **"Kayıp sonradan eklenir."** | Kayıp, hangi ünitenin daha değerli olduğunu değiştirir; eniyilemenin içindedir. |
| **"Ekonomik dağıtımın sonucu uygulanabilirdir."** | Şebeke sınırlarını bilmez. |

## Panel takip sorusu

**"Maliyet eğrisi dışbükey değilse?"**

> **Mülakatta şöyle söyle:** Vana noktası etkisi veya yasak çalışma bölgeleri varsa eşit artımsal maliyet koşulu yeterli olmaz, yerel en küçük noktalar oluşur. Parçalı doğrusallaştırıp karışık tam sayılı programla çözerim; küçük boyutta dinamik programlama da olur.

**"Rampa kısıtı nasıl girer?"**

> **Mülakatta şöyle söyle:** Ünitenin bir sonraki dönemdeki sınırları, şimdiki çıkışı ± rampa hızı olur. Dönemler birbirine bağlanır; problem dinamik ekonomik dağıtıma döner.

**"Yenilenebilirin marjinal maliyeti sıfırsa ne olur?"**

> **Mülakatta şöyle söyle:** Liyakat sırasının başına girer, pahalı üniteleri dışarı iter ve takas fiyatını düşürür. Ama esneklik, yedek ve atalet ihtiyacı ayrı kısıtlar olarak geri gelir.

## 90 saniye

"Ekonomik dağıtım, devredeki ünitelerin yükü en az maliyetle paylaşmasıdır. En iyi noktada sınırına dayanmamış bütün üniteler aynı artımsal maliyette çalışır; bu ortak değer lambda'dır ve yükün bir megavat artmasının maliyetidir. Lambda iterasyonunda bir değer tahmin eder, her ünitenin üretimini hesaplar, toplam yükten azsa lambda'yı artırırım. Üst sınırına dayanan ünite lambda'nın altında kalır. Kayıp varsa her ünitenin artımsal maliyetini ceza faktörüyle çarparım; yükten uzaktaki ünite daha pahalı görünür. Şebeke sınırı devreye girerse optimal güç akışına geçerim ve tek fiyat yerine bara fiyatları çıkar."
