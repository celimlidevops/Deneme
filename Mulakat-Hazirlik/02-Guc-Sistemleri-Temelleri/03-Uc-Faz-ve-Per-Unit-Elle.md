# Üç faz ve birim sistem, elle

## Üç faz neden var

Üç iletkende, aralarında 120° olan üç sinüs taşınır. Üç yararı vardır:

1. Aynı iletken miktarıyla daha çok güç.
2. Toplamı sabit olan (titreşimsiz) anlık güç.
3. Motorda kendiliğinden dönen manyetik alan.

Dengeli sistemde üç faz akımının toplamı sıfırdır. Bu yüzden dönüş iletkenine gerek kalmaz.

İki gerilim vardır ve karıştırılması en sık yapılan hatadır:

| Gerilim | Nerede ölçülür |
| --- | --- |
| Faz gerilimi | Bir faz ile nötr arası |
| Hat gerilimi | İki faz arası. `V_hat = √3 × V_faz` |

"400 kV hat" derken hat gerilimi söylenir. Faz gerilimi `400 / √3 = 230,9 kV`'tur. Evdeki 400/230 V da aynı ilişkidir.

Bağlantı türleri:

| Bağlantı | Yapı | Sargı hangi gerilimi görür |
| --- | --- | --- |
| Yıldız (Y) | Üç sargının bir ucu ortak noktada (nötr) birleşir. Nötr topraklanabilir | Faz gerilimi |
| Üçgen (Δ) | Sargılar uç uca kapanır, nötr yoktur | Hat gerilimi |

Üç faz güç, hat büyüklükleriyle aşağıdaki gibi yazılır. `cos φ` güç faktörüdür.

```
S = √3 × V_hat × I_hat
P = √3 × V_hat × I_hat × cos φ
```

Dengeli sistemde üç fazı ayrı ayrı çözmeyiz. Bir fazı çözeriz, diğer ikisi 120° kaymış kopyasıdır. Tek hat şeması bu varsayımın çizimidir.

Varsayım iki yerde bozulur: dengesiz arızada ve dağıtımın tek fazlı yüklerinde. Orada simetrik bileşenler veya üç faz model gerekir.

## Elle örnek 1: akım ve reaktif güç

400 kV'ta 300 MW, güç faktörü 0,95 geri.

1. `S = 300 / 0,95 = 315,8 MVA`. Bu adım, aktif gücü güç faktörüne bölerek görünür gücü bulur.
2. `I = 315,8 MVA / (√3 × 400 kV) = 455,8 A`. Bu adım, üç faz güç formülünden hat akımını çeker.
3. `Q = 300 × tan(arccos 0,95) = 300 × 0,3287 = 98,6 Mvar`. Bu adım, güç faktörünün açısını bulup tanjantıyla reaktif gücü hesaplar.

Aynı güç 154 kV'ta 1184 A ister. Gerilim katının neden var olduğu bu sayıdadır.

## Birim sistem (per-unit)

Şebekede 400 kV ile 0,4 kV yan yanadır. Gerçek birimle çalışırsan iki sorun çıkar:

- Her trafoda oran çarpmak zorunda kalırsın.
- Sayılar altı basamak farklı olur.

Birim sistem (per-unit, pu) her büyüklüğü bir baza böler:

```
değer_pu = gerçek değer / baz değer
```

> Sade anlatım: yazılımcı gözüyle bu bir normalizasyondur.

Üç kazancı vardır:

1. Trafo oranları kaybolur.
2. Sağlıklı gerilim hep 1,0 civarındadır. 0,93 gördüğünde sorun olduğunu hemen anlarsın.
3. Sayısal çözücü iyi koşullu matrisle çalışır.

İki baz seçilir, diğerleri türetilir. Aşağıdaki blokta ilk iki satır seçilen, son iki satır türetilen bazlardır.

```
S_baz    : bütün sistem için tek değer (alışkanlık 100 MVA)
V_baz    : her gerilim bölgesinin nominal hat gerilimi
I_baz    = S_baz / (√3 × V_baz)
Z_baz    = V_baz² / S_baz
```

## Elle örnek 2: bazlar ve çevirme

154 kV bölgesi, 100 MVA baz.

1. `Z_baz = 154² / 100 = 237,16 Ω`. Bu adım, bu gerilim bölgesinde 1 pu empedansın kaç ohm ettiğini bulur.
2. `I_baz = 100 MVA / (√3 × 154 kV) = 374,9 A`. Bu adım, bu bölgede 1 pu akımın kaç amper ettiğini bulur.
3. Reaktansı 20 Ω olan hat: `20 / 237,16 = 0,0843 pu`. Bu adım, ohm değerini empedans bazına bölerek pu'ya çevirir.
4. Hattan 0,8 pu akım geçiyorsa: `0,8 × 374,9 = 300 A`. Bu adım, pu akımı akım bazıyla çarparak tekrar ampere döndürür.

Aynı 20 Ω, 400 kV bölgesinde `Z_baz = 1600 Ω` olduğundan 0,0125 pu eder. Aynı ohm, yüksek gerilimde elektriksel olarak çok daha kısadır.

## Elle örnek 3: baz değiştirme

Trafo plakası: 50 MVA, kısa devre empedansı %10. Bu değer trafonun **kendi** bazındadır. Sistem bazı 100 MVA ise aşağıdaki formülle çevrilir.

Blokta ilk satır genel formül, ikinci satır sayıların yerine konmuş halidir.

```
Z_yeni = Z_eski × (S_yeni / S_eski) × (V_eski / V_yeni)²
       = 0,10 × (100 / 50) × 1 = 0,20 pu
```

Adımların anlamı:

1. `Z_eski = 0,10`. Plakadaki %10, pu olarak 0,10'dur.
2. `S_yeni / S_eski = 100 / 50`. Bu çarpan, güç bazı büyüdükçe pu empedansın da büyüdüğünü hesaba katar.
3. `(V_eski / V_yeni)² = 1`. Gerilim bazı değişmediği için ikinci çarpan 1'dir.
4. Sonuç `0,20 pu`.

Küçük trafo, büyük bazda daha büyük empedans görünür. Bu çevirme yapılmadan matrise giren trafo, kısa devre hesabını iki kat şaşırtır.

## Yaygın yanlış

- **"400 kV faz gerilimidir."** Hayır, hat gerilimidir. Faz gerilimi 231 kV.
- **"Üç faz güç, 3 × V × I'dır."** Hat büyüklükleriyle `√3 × V × I`, faz büyüklükleriyle `3 × V_faz × I_faz`. İkisi aynı sonucu verir; karıştırınca √3 kat hata çıkar.
- **"Per-unit yüzde demektir."** Yakındır ama aynı değil: 1,0 pu = %100. Trafo plakası yüzde yazar, matris pu ister.
- **"Plaka empedansı sistem bazındadır."** Hayır, cihazın kendi anma gücündedir. Her zaman çevrilir.
- **"Per-unit'te güç tek faz gücüdür."** Hayır. `S_baz` üç faz toplamıdır.

## Panel takip sorusu

"İki farklı gerilim bölgesini per-unit nasıl birleştirir?"

> Mülakatta şöyle söyle: "Her bölgenin gerilim bazı trafonun anma oranıyla seçilir; o zaman ideal trafo per-unit'te 1:1 olur ve devreden düşer. Kademe nominalden farklıysa bu fark, modelde off-nominal oran olarak kalır."

"Baz gücü 100 yerine 1000 MVA seçsem sonuç değişir mi?"

> Mülakatta şöyle söyle: "Fiziksel sonuç değişmez, per-unit sayılar ölçeklenir. İki ayrı yazılımın sonucu tutmuyorsa ilk baktığım yer baz farkıdır."

Aşağıdaki metin, bu sayfanın tamamını mülakatta 90 saniyede anlatmak içindir.

## 90 saniye

> "Üç faz, 120 derece arayla üç sinüstür; dengeliyken tek fazını çözer, tek hat şemasıyla gösteririm. Hat gerilimi faz geriliminin kök üç katıdır ve 400 kV dediğimizde hat gerilimini söyleriz. Güç kök üç çarpı hat gerilimi çarpı akımdır. Farklı gerilim katlarını tek matriste toplamak için birim sistem kullanırım: tek güç bazı, bölge başına gerilim bazı, empedans bazı gerilimin karesi bölü güç. Trafo plakası kendi bazındadır, sisteme girmeden çeviririm."
