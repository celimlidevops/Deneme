# Sıfırdan: alternatif akım, fazör, güç

Bu sayfa, elektrikle yıllardır uğraşmamış bir yazılımcı için yazıldı. Diğer bütün klasörler buradaki altı fikre dayanır.

Burayı tahtada anlatabiliyorsan gerisi formül değil, uygulama olur.

## 1. Neden alternatif akım ve neden yüksek gerilim

Güç, gerilim ile akımın çarpımıdır. Aynı gücü yüksek gerilimde taşırsan akım düşer.

Hat kaybı akımın karesiyle gider: `P_kayıp = 3 I² R`. Buradaki 3, üç fazın her birindeki kaybın toplanmasıdır.

Gerilimi kolayca yükseltip düşüren cihaz trafodur. Trafo yalnızca alternatif akımda (AC) çalışır. İletimin 400 kV olmasının nedeni budur.

### Elle: 100 MW'ı faz başına direnci 10 Ω olan bir hattan taşı

Adım 1, 154 kV'ta:

- Akım `100 MW / (√3 × 154 kV) = 375 A`. Bu adım, üç faz güç formülünden hat akımını bulur.
- Kayıp `3 × 375² × 10 = 4,2 MW`, yani %4,2. Bu adım, akımın karesini direnç ve faz sayısıyla çarpıp kaybı bulur.

Adım 2, 400 kV'ta:

- Akım 144 A. Aynı formül, yalnızca gerilim değişti.
- Kayıp 0,63 MW, yani %0,6. Aynı kayıp formülü, küçük akımla.

Adım 3, karşılaştırma:

- Gerilim 2,6 kat arttı, kayıp 6,75 kat düştü.
- Oran, gerilim oranının karesidir. Bu adım, kaybın gerilimin karesiyle ters orantılı olduğunu gösterir.

## 2. Sinüs ve etkin değer

Şebeke gerilimi saniyede 50 kez salınan bir sinüstür: `v(t) = V_tepe sin(ωt + φ)`.

| Büyüklük | Değer |
| --- | --- |
| Frekans | 50 Hz |
| Periyot | 20 ms |
| Açısal hız | `ω = 2π × 50 = 314 rad/s` |

Mühendis tepe değeri değil etkin değeri (RMS, Root Mean Square) söyler. Etkin değer, aynı ısıyı üreten doğru akım eşdeğeridir: `V_etkin = V_tepe / √2`.

Prizdeki 230 V etkin değerdir; tepe 325 V'tur. Bu notlardaki bütün kV ve A değerleri etkin değerdir.

## 3. Fazör: sinüsü iki sayıyla anlatmak

Frekans herkes için aynıysa (50 Hz), bir sinüsü ayırt eden iki şey kalır: büyüklüğü ve açısı. Fazör bu ikiliyi tek bir karmaşık sayıda tutar: `V = |V| ∠φ = |V| (cos φ + j sin φ)`.

> Sade anlatım: zaman ekseni olan bir sinyali, iki alanlı sabit bir yapıya indirgiyoruz. Karşılığında türev ve integral, karmaşık sayı çarpma ve bölmesine dönüşüyor.

Güç sistemi analizinin tamamı bu sadeleştirmenin üstünde durur.

`j`, mühendislikte `i` yerine kullanılır, çünkü `i` akımdır.

Açı mutlak değildir. Bir bara referans seçilir (açısı 0), diğerleri ona göre söylenir. Yük akışındaki salınım barası bu referanstır.

## 4. Üç eleman: direnç, bobin, kondansatör

| Eleman | Empedans | Akım ile gerilim | Nerede karşına çıkar |
| --- | --- | --- | --- |
| Direnç R | `R` | Aynı fazda | İletken kaybı |
| Bobin L | `jωL = jX_L` | Akım 90° geride | Hat, trafo, motor |
| Kondansatör C | `1/(jωC) = -jX_C` | Akım 90° önde | Hat kapasitesi, kablo, kompanzasyon |

Empedans `Z = R + jX` karmaşık dirençtir. Ohm yasası aynen geçerlidir: `V = Z I`.

Admitans empedansın tersidir: `Y = 1/Z = G + jB`. `G` iletkenlik, `B` süseptanstır.

Şebeke matrisi (Ybus, bara admitans matrisi) admitansla kurulur, çünkü paralel elemanlar admitansta toplanır.

Örnek: 31,83 mH bobin 50 Hz'te `X = 314 × 0,03183 = 10 Ω` eder. Bu hesap, `X_L = ωL` formülüne açısal hızı ve henry cinsinden endüktansı koyar.

## 5. Güç: aktif, reaktif, görünür

Gerilim ile akım aynı fazda değilse, çarpımlarının bir kısmı iş yapar, bir kısmı kaynak ile alan arasında gidip gelir.

| Güç | Birim | Anlamı |
| --- | --- | --- |
| Aktif güç P | MW | İş yapan kısım. Motoru döndürür, ısıtır |
| Reaktif güç Q | Mvar | Bobinin manyetik alanı ile kondansatörün elektrik alanını her çeyrek periyotta doldurup boşaltan kısım. Ortalaması sıfırdır, ama akımı gerçektir |
| Görünür güç S | MVA | İkisinin vektör toplamı. Ekipman S'ye göre boyutlanır, çünkü ısınma akıma bağlıdır |

Aşağıdaki blok üç gücün ilişkisini verir. `*` eşlenik demektir.

```
S = V I* = P + jQ        (* eşlenik demektir)
|S| = √(P² + Q²)
güç faktörü = cos φ = P / |S|
```

Reaktif güç neden önemli? İş yapmaz ama hattı doldurur, kayıp üretir ve gerilimi düşürür.

> Sade anlatım: reaktif güç, yararlı yük taşımayan ama bant genişliğini tüketen trafik gibidir.

Reaktif güç tamamen yok edilmez, çünkü motor ve trafo manyetik alan olmadan çalışmaz. Hedef, onu yükün yanında üretip uzun hatta gezdirmemektir.

İşaret sözleşmesi:

- Endüktif yük (motor) reaktif güç **tüketir**. Q pozitif, akım geridedir.
- Kondansatör reaktif güç **üretir**.
- "Geri" ve "ileri" güç faktörü buradan gelir.

## Elle örnek

230 V etkin gerilim, `Z = 10 + j10 Ω` yük.

1. `|Z| = √(10² + 10²) = 14,14 Ω`, açısı 45°. Bu adım, empedansı büyüklük ve açı biçimine çevirir.
2. `I = 230 / 14,14 = 16,26 A`, açısı −45°. Akım geride, yük endüktif. Bu adım, Ohm yasasıyla akımı bulur; açı, empedans açısının eksi işaretlisidir.
3. `|S| = 230 × 16,26 = 3741 VA`. Bu adım, görünür gücü gerilim ve akım büyüklüklerinin çarpımı olarak bulur.
4. `P = 3741 × cos 45° = 2645 W`, `Q = 3741 × sin 45° = 2645 var`. Bu adım, görünür gücü aktif ve reaktif bileşenlerine ayırır.
5. Güç faktörü 0,707 geri. Bu adım, `cos 45°`'yi güç faktörü olarak okur; akım geride olduğu için "geri" denir.

Kontrol: `P = I² R = 16,26² × 10 = 2645 W`. Tuttu. Bu kontrol, aktif gücün yalnızca dirençte harcandığını kullanarak sonucu doğrular.

Yorum: bu yük 2645 W iş yapıyor ama kaynak 3741 VA'lık akım taşıyor. Aradaki fark reaktif güçtür.

## Yaygın yanlış

- **"Reaktif güç kayıp güçtür."** Hayır. Reaktif güç harcanmaz, gidip gelir. Kayıp, onun akımının dirençte ürettiği ısıdır.
- **"Güç faktörü 1 ise akım yoktur."** Hayır. Güç faktörü 1, akımın tamamının iş yaptığını söyler.
- **"Tepe değer ile etkin değer aynı tabloda toplanır."** Hayır. Notlarda ve standartlarda aksi yazmıyorsa her şey etkin değerdir.
- **"Empedans dirençle aynıdır."** Direnç empedansın gerçek kısmıdır. İletim hattında sanal kısım (reaktans) dirençten 5–10 kat büyüktür; analizlerin çoğunda belirleyici olan odur.
- **"j bir birimdir."** Değil. 90° faz kaymasını taşıyan sayıdır: `j² = −1`.

## Panel takip sorusu

"Reaktif güç iş yapmıyorsa neden parasını konuşuyoruz?"

> Mülakatta şöyle söyle: "Akımı büyütür, hat ve trafo kapasitesini tüketir, kayıp ve gerilim düşümü üretir. Bu yüzden yükün yanında kompanze edilir ve dağıtımda reaktif enerji bedeli vardır."

"Fazör neyi varsayar?"

> Mülakatta şöyle söyle: "Tek frekans ve sürekli hal. Arıza anındaki milisaniyelik geçici olaylar ve harmonikler fazörle tam anlatılmaz; orada zaman tanım bölgesi (EMT) gerekir."

EMT, Electromagnetic Transients (elektromanyetik geçici olaylar) demektir; sinyali fazör yerine zamanda adım adım çözer.

Aşağıdaki metin, bu sayfanın tamamını mülakatta 90 saniyede anlatmak içindir.

## 90 saniye

> "Şebeke 50 Hz sinüstür; frekans ortak olduğu için her gerilimi ve akımı büyüklük ve açıdan oluşan bir fazörle, yani karmaşık sayıyla anlatırım. Bobin akımı geriletir, kondansatör ilerletir; ikisi empedansın sanal kısmıdır. Güç ikiye ayrılır: iş yapan aktif güç ve alanları doldurup boşaltan reaktif güç. Reaktif güç harcanmaz ama akım taşıdığı için kapasiteyi doldurur, kayıp ve gerilim düşümü yaratır. Yüksek gerilim, aynı gücü küçük akımla taşıyıp kaybı akımın karesiyle düşürmek içindir."
