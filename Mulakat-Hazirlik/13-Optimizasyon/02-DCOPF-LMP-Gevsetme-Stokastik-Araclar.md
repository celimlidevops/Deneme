# DC-OPF, LMP ve Gevşetmeler

Bu sayfanın konuları sırasıyla şunlardır:

- DC-OPF (Direct Current Optimal Power Flow, doğru akım yaklaşımlı optimal güç akışı)
- Gölge fiyat ve LMP (Locational Marginal Price, bölgesel marjinal fiyat)
- Dışbükey gevşetmeler
- Belirsizlik altında eniyileme
- Meta-sezgiseller
- Araçlar

## Neden dışbükeylik bu kadar önemli

Dışbükey problemde yerel en iyi, genel en iyidir ve çözücü bunu **kanıtlar**.

Dışbükey olmayan problemde çözücü bir nokta bulur. Ama daha iyisinin olup olmadığını söyleyemez.

AC (alternatif akım) optimal güç akışı dışbükey değildir. Sebebi şudur: güç denklemleri gerilimlerin çarpımını ve açıların sinüsünü içerir. Çarpım ve sinüs, kâse biçimli değil, dalgalı bir uygun bölge üretir.

Bu yüzden üç yol vardır:

| Yol | Ne yapar | Bedeli |
| --- | --- | --- |
| Yerel çözücü (iç nokta) | AC-OPF'yi olduğu gibi çözer | Genel en iyi garantisi yok; başlangıca duyarlı |
| Doğrusallaştırma (DC-OPF) | Fiziği basitleştirir | Gerilim ve reaktif yok; sonuç AC'de uygulanamayabilir |
| Dışbükey gevşetme (SOCP, SDP) | Uygun bölgeyi dışbükey bir kümeyle sarar | Çözüm fiziksel olmayabilir; ama alt sınır verir |

Tablodaki kısaltmalar: SOCP (Second-Order Cone Programming, ikinci dereceden konik programlama) ve SDP (Semidefinite Programming, yarı kesin programlama).

> **Sade anlatım:** Ya gerçek fiziği çözüp "en iyi bu mu" sorusunu cevapsız bırakırsın, ya fiziği basitleştirip hızlı ama yaklaşık bir sonuç alırsın, ya da problemi geniş bir kılıfla sarıp "en iyi bundan daha iyi olamaz" diyen bir alt sınır elde edersin.

## DC-OPF: doğrusal program biçimi

DC-OPF, AC güç akışının basitleştirilmiş halidir. Varsayımları:

- Gerilimler 1,0 pu'dur (per unit, birim değer).
- Açı farkları küçüktür.
- Direnç ve reaktif güç ihmal edilir.

Modelde PTDF (Power Transfer Distribution Factor, güç aktarım dağılım katsayısı) kullanılır. PTDF_l,k, bara k'ya 1 MW (megavat) enjekte edilince hat l'nin akışının ne kadar değiştiğini söyler.

Aşağıdaki blok modelin tamamıdır. İlk satır üretim maliyetini en aza indirir. İkinci satır üretimin yüke eşit olmasını ister; çarpanı λ'dır. Üçüncü satır her hattın akışını sınırında tutar; çarpanı μ_l'dir. Son satır her üretecin alt ve üst sınırıdır.

```
en küçük   Σ c_i g_i
öyle ki    Σ g_i = Σ d_i                                   (güç dengesi)             ← λ
           −F_l ≤ Σ_k PTDF_l,k (g_k − d_k) ≤ F_l           (hat sınırları)           ← μ_l
           g_i,min ≤ g_i ≤ g_i,max
```

Semboller:

| Sembol | Anlamı |
| --- | --- |
| c_i | Üreteç i'nin birim maliyeti |
| g_i | Üreteç i'nin üretimi |
| d_i | Bara i'deki yük |
| F_l | Hat l'nin taşıma sınırı |

Maliyet doğrusal veya parçalı doğrusal ise bu bir doğrusal programdır, yani LP'dir (Linear Programming).

LP olmasının dört faydası vardır:

- Milisaniyelerde çözülür.
- Her zaman genel en iyiyi verir.
- Her kısıtın gölge fiyatını bedavaya üretir.
- Piyasa eşleştirme ve güvenlik kısıtlı dağıtım yazılımlarının temelidir.

## Gölge fiyat ve LMP

**Gölge fiyat** (ikil değişken): Bir kısıtın sağ tarafı bir birim gevşetilirse amaç işlevi ne kadar iyileşir, onu söyler. Bağlamayan kısıtın gölge fiyatı sıfırdır.

**Bölgesel marjinal fiyat (LMP):** Belirli bir barada yük 1 MW artarsa toplam maliyet ne kadar artar, onu söyler.

LMP'nin üç bileşeni vardır. Aşağıdaki blokta ilk satır bileşenleri toplar. İkinci satır kısıt bileşeninin nasıl hesaplandığını gösterir: her hattın gölge fiyatı, o baranın o hat üzerindeki PTDF'siyle çarpılır ve eksi işaretle toplanır.

```
LMP_k = λ (enerji)  +  kısıt bileşeni  +  kayıp bileşeni
kısıt bileşeni = −Σ_l μ_l × PTDF_l,k
```

Kısıt yoksa ve kayıp ihmal edilirse bütün baralarda LMP aynıdır ve `λ`'ya eşittir. Bir hat dolunca fiyatlar ayrışır.

> **Sade anlatım:** Hatlar boşken elektrik her yere aynı fiyata gider. Bir hat dolunca bazı baralara ucuz elektrik ulaşamaz ve oradaki fiyat yükselir.

### Elle örnek

**Şebeke kurulumu.** Bu adım, hesapta kullanılacak bütün verileri bir araya getirir.

`03` klasöründeki üç baralı şebeke kullanılır:

| Bara | İçerik |
| --- | --- |
| Bara 1 | G1 üreteci, 10 TL/MWh (megavatsaat başına Türk lirası). Referans bara |
| Bara 2 | G2 üreteci, 30 TL/MWh |
| Bara 3 | 150 MW yük |

Üreteçlerin kapasitesi 200 MW'tır.

**Hat akışı formülü.** Bu adım, hat 1–3'ün akışını yalnızca g_2 cinsinden yazarak sınırla karşılaştırılabilir hale getirir.

Hat 1–3'ün PTDF değerleri: bara 2 için −0,1818, bara 3 için −0,6364. Referans bara (bara 1) için PTDF sıfırdır, bu yüzden g_1 formüle girmez.

```
Hat 1–3 akışı = −0,1818 × g_2 − 0,6364 × (−150) = 95,45 − 0,1818 g_2
```

**Kısıtsız durum.** Bu adım, hat sınırı yokken ulaşılacak en ucuz çözümü ve buna karşılık gelen akışı bulur.

Ucuz olan hepsini üretir: `g_1 = 150`, `g_2 = 0`.

- Maliyet 1.500 TL/saat.
- Hat 1–3 akışı 95,5 MW.
- Bütün baralarda fiyat 10 TL/MWh.

**Hat 1–3 sınırı 80 MW.** Bu adım, sınır eklenince pahalı üretecin en az ne kadar çalışması gerektiğini ve yeni maliyeti bulur.

Aşağıda ilk satır akış sınırını g_2 için çözer. İkinci satır güç dengesinden g_1'i bulur. Üçüncü satır toplam maliyeti hesaplar.

```
95,45 − 0,1818 g_2 ≤ 80   →   g_2 ≥ 85
g_2 = 85,  g_1 = 65
Maliyet = 65 × 10 + 85 × 30 = 3.200 TL/saat
```

**Kısıt maliyeti.** Bu adım, hat sınırının sisteme toplam bedelini gösterir: 3.200 − 1.500.

Kısıt maliyeti saatte 1.700 TL.

**Hattın gölge fiyatı.** Bu adım, hat sınırını 1 MW gevşetmenin kaç TL kazandırdığını bulur; bu sayı μ'dür.

Sınır 81 MW olsaydı: `g_2 ≥ 79,5`. Yani 5,5 MW pahalı üretim ucuzuyla yer değiştirir. Her MW'ta kazanç 30 − 10 = 20 TL'dir.

```
μ = 5,5 × (30 − 10) = 110 TL/MW·saat
```

Hattın kapasitesini 1 MW artırmanın saatlik değeri 110 TL'dir. İletim yatırımının fayda hesabı bu sayıdan başlar (`12/02`).

**Bara 3'ün LMP'si.** Bu adım, bara 3'te 1 MW ek yükün toplam maliyeti ne kadar artırdığını doğrudan hesaplar.

Bara 3'te yük 1 MW artsın. Hat sınırda kaldığı için akış değişmemeli.

Aşağıda ilk satır, akışın sabit kalması için G2'nin ne kadar artması gerektiğini bulur. İkinci satır, güç dengesinden G1'in ne kadar değişeceğini bulur. Üçüncü satır, bu iki değişikliğin maliyetini toplar.

```
Akış değişimi = −0,1818 Δg_2 + 0,6364 = 0   →   Δg_2 = +3,5 MW
Güç dengesi:    Δg_1 + Δg_2 = 1               →   Δg_1 = −2,5 MW
Maliyet değişimi = 3,5 × 30 − 2,5 × 10 = 80 TL
```

**LMP_3 = 80 TL/MWh.** Sistemdeki en pahalı santral 30 TL/MWh iken bara 3'teki fiyat 80 çıktı.

Neden: bara 3'e 1 MW daha göndermek için pahalı santrali 3,5 MW artırıp ucuz santrali 2,5 MW **azaltmak** gerekiyor. Elektrik istediğin yoldan akmaz; akışı yeniden biçimlendirmenin bedeli fiyata yansır.

> **Sade anlatım:** Bara 3'e 1 MW yollamak için 1 MW üretmek yetmiyor. Hattı aşmamak için ucuz santrali kısıp pahalıyı fazlasıyla artırmak gerekiyor. Bu "dolambaçlı yol"un bedeli 80 TL ediyor.

**Formülle kontrol.** Bu adım, aynı fiyatları LMP formülüyle (λ + μ × PTDF büyüklüğü) bularak doğrudan hesabı doğrular.

Aşağıda her satır bir baranın fiyatıdır. Bara 1 referans olduğu için kısıt bileşeni sıfırdır. Bara 2 ve 3'e, 110'luk gölge fiyat ile o baranın PTDF büyüklüğünün çarpımı eklenir.

```
LMP_1 = 10                                    (referans, marjinal ünite G1)
LMP_2 = 10 + 110 × 0,1818 = 30                (G2 de marjinal; kendi maliyeti)
LMP_3 = 10 + 110 × 0,6364 = 80
```

**Kısıt rantı.** Bu adım, yükün ödediği para ile üreticilerin aldığı para arasındaki farkın nereden geldiğini gösterir.

| Kalem | Hesap | Tutar |
| --- | --- | --- |
| Yükün ödediği | `150 × 80` | 12.000 |
| Üreticilerin aldığı | `65 × 10 + 85 × 30` | 3.200 |
| Fark | `μ × sınır = 110 × 80` | 8.800 TL |

Bu para iletim işletmecisinde birikir. İletim hakkı sahiplerine dağıtılır veya tarifeyi düşürür.

**Doğrulama.** Bütün sayılar `elle_ornekler.py` içinde `scipy.optimize.linprog` (HiGHS) ile doğrulanmıştır.

**Türkiye bağlamı.** Türkiye'de piyasa tek bölgelidir, LMP uygulanmaz (`11/03`). Ama aynı hesap, kısıt talimatlarının maliyetini ve iletim yatırımının değerini bulmak için kullanılır.

## Dışbükey gevşetmeler

Fikir: Dışbükey olmayan uygun bölgeyi içine alan dışbükey bir küme üzerinde çöz.

Bunun üç sonucu vardır:

- Gevşetilmiş problemin sonucu, gerçek problemin en iyisi için **alt sınırdır**.
- Gevşetilmiş çözüm aynı zamanda özgün kısıtları sağlıyorsa gevşetme **sıkıdır** (exact). Genel en iyi bulunmuştur ve kanıtlıdır.
- Sağlamıyorsa çözüm fiziksel değildir. Yine de yerel çözücünün bulduğu noktanın ne kadar iyi olduğunu ölçmek için kullanılır (en iyilik aralığı).

> **Sade anlatım:** Garip biçimli bir bölgeyi bir balonla sararsın. Balonun içindeki en iyi nokta, gerçek bölgedeki en iyiden daha kötü olamaz. Bu en iyi nokta gerçek bölgenin içine düşerse şanslısın: gerçek cevabı bulmuşsundur.

### SOCP: ikinci dereceden konik gevşetme

Radyal (ağaç biçimli, döngüsüz) şebekeler için dal akış modeli kullanılır.

Değişkenler gerilimin ve akımın **karesi**dir: `v_i = |V_i|²`, `ℓ_ij = |I_ij|²`. Açılar modelden düşer.

Aşağıdaki üç satır dal akış modelidir. İlk satır güç dengesidir. İkinci satır gerilim düşümüdür. Üçüncü satır gücü, gerilimi ve akımı birbirine bağlar; problemin dışbükey olmayan tek parçası budur. Burada P etkin güç, Q reaktif güç, r direnç, x reaktanstır.

```
P_ij − r_ij ℓ_ij − Σ P_jk = p_j                              doğrusal
v_j = v_i − 2 (r_ij P_ij + x_ij Q_ij) + (r_ij² + x_ij²) ℓ_ij    doğrusal
ℓ_ij v_i = P_ij² + Q_ij²                                     DIŞBÜKEY DEĞİL
```

Tek sorunlu satır sonuncusudur. Eşitlik, eşitsizliğe gevşetilir. Aşağıdaki kısıt bir koni tanımlar ve dışbükeydir:

```
ℓ_ij v_i ≥ P_ij² + Q_ij²          ikinci dereceden koni kısıtı
```

**Neden çoğu zaman işe yarar:** Amaç kaybı veya maliyeti en aza indiriyorsa çözücü `ℓ`'yi (akımı, dolayısıyla kaybı) gereksiz yere büyütmek istemez. Bu yüzden eşitsizlik kendiliğinden eşitlikle sağlanır.

Radyal şebekede ve hafif koşullar altında (ters akış ve gerilim üst sınırı bağlamıyorsa) gevşetme sıkıdır.

**Kullanım alanları:**

- Dağıtımda volt/VAR (gerilim ve reaktif güç) kontrolü.
- Yeniden yapılandırma (ikili değişkenlerle karışık tam sayılı SOCP).
- Barındırma kapasitesi (şebekenin ne kadar dağıtık üretim kaldırabileceği).

Ticari çözücülerle büyük ölçekte çözülür.

**Sıkılığın bozulduğu yer:** Yüksek güneş üretimiyle ters akış ve gerilim üst sınırının bağladığı durum. Yani tam da ilgilendiğimiz durum. Sonuç her zaman denetlenir.

### SDP: yarı kesin gevşetme

Gözlü (iletim) şebeke için kullanılır. Gözlü şebekede döngüler vardır.

`W = V Vᴴ` matrisi tanımlanır. Burada V gerilim vektörü, Vᴴ onun eşlenik devriğidir. Güç denklemleri gerilimde ikinci dereceden, `W`'de ise **doğrusaldır**.

Aşağıdaki iki koşul birlikte `W`'nin gerçekten bir gerilim vektöründen geldiğini garanti eder. İlki dışbükeydir ve tutulur. İkincisi dışbükey değildir ve atılır; gevşetme budur.

```
W ⪰ 0            (yarı kesin pozitif)       dışbükey
rank(W) = 1      (W gerçekten V Vᴴ biçiminde)   DIŞBÜKEY DEĞİL  →  atılır
```

Çözümün rankı 1 çıkarsa gevşetme sıkıdır ve gerilimler `W`'den geri elde edilir. Birçok standart test sisteminde sıkı çıktığı gösterilmiştir; her zaman değil.

**Sorunu ölçektir:** `W`, `n × n` boyutundadır. Binlerce baralı sistemde doğrudan çözülemez. Seyrekliği kullanan ayrıştırma (kordal genişletme) gerekir.

Bu yüzden SDP araştırmada ve en iyilik aralığını ölçmede kullanılır, gerçek zamanlı işletmede değil.

### SOCP ile SDP karşılaştırması

| Özellik | SDP | SOCP |
| --- | --- | --- |
| Sıkılık | SOCP'den sıkıdır | Daha gevşek |
| Hız | Daha yavaş | Daha hızlıdır |
| Radyal şebekede | İkisi eşdeğerdir | İkisi eşdeğerdir |

## Belirsizlik altında eniyileme

Rüzgâr, güneş ve yük tahminle bilinir. Karar (hangi ünite devrede, ne kadar yedek) belirsizlik çözülmeden verilir.

Dört yaklaşım vardır:

| Yaklaşım | Belirsizliği nasıl görür | Neyi eniyiler | Zayıflığı |
| --- | --- | --- | --- |
| Deterministik + yedek | Tek tahmin, üstüne sabit pay | Tahmin senaryosunun maliyeti | Pay keyfidir |
| Stokastik | Olasılıklı senaryolar | **Beklenen** maliyet | Dağılımı bilmek gerekir; senaryo sayısıyla büyür |
| Dayanıklı (robust) | Belirsizlik kümesi (aralık) | **En kötü durum** maliyeti | Tutucudur |
| Şans kısıtlı | Dağılım | Maliyet; kısıt en az `1 − ε` olasılıkla sağlanır | Dağılım varsayımı |

İki aşamalı yapı hepsinde ortaktır:

| Aşama | Ne zaman | Örnek kararlar |
| --- | --- | --- |
| Birinci aşama | **Şimdi**, belirsizlik çözülmeden | Ünite tahsisi, yedek |
| İkinci aşama | Belirsizlik çözüldükten **sonra** | Dağıtım, yük atma |

### Elle örnek: ne kadar yedek tutmalı

**Veriler.** Bu adım, karşılaştırılacak maliyetleri ve olasılıkları tanımlar.

- Yedek tutmanın maliyeti 20 TL/MW.
- Yedek yetmezse verilemeyen gücün cezası 200 TL/MW.

Rüzgâr tahmin hatasından doğan açık için üç senaryo:

| Senaryo | Açık | Olasılık |
| --- | --- | --- |
| Tahmin tuttu | 0 MW | 0,60 |
| Orta sapma | 50 MW | 0,35 |
| Büyük sapma | 150 MW | 0,05 |

**Üç seçeneğin maliyeti.** Bu adım, her yedek miktarı için yedek bedeli ile beklenen ceza bedelini toplar.

Aşağıda her satırın ilk terimi yedek tutma bedelidir (MW × 20). Sonraki terimler, yedeğin yetmediği senaryolarda olasılık × eksik MW × 200 cezasıdır.

```
Yedek 0:    maliyet = 0 + 0,35 × 50 × 200 + 0,05 × 150 × 200 = 3.500 + 1.500 = 5.000
Yedek 50:   maliyet = 50 × 20 + 0,05 × (150 − 50) × 200     = 1.000 + 1.000 = 2.000
Yedek 150:  maliyet = 150 × 20 + 0                           = 3.000
```

**Sonuçların yorumu.** Bu adım, her yaklaşımın hangi seçeneği seçeceğini gösterir.

| Karar | Yedek | Gerekçe |
| --- | --- | --- |
| **Stokastik karar** | 50 MW | Beklenen maliyet en düşük (2.000) |
| **Dayanıklı karar** | 150 MW | Hiçbir senaryoda açık yok; bedeli 1.000 TL fazla |
| **Yedeksiz** | 0 MW | En pahalısı |

**Marjinal mantık.** Bu adım, sonucu tek tek MW düzeyinde gerekçelendirir.

Kural: Bir MW daha yedek tutmak, "o MW'a ihtiyaç duyulma olasılığı × ceza" yedek maliyetinden büyükse değer.

- İlk 50 MW için ihtiyaç olasılığı 0,35 + 0,05 = 0,40'tır: `0,40 × 200 = 80 > 20`. Değer.
- Sonraki 100 MW için ihtiyaç olasılığı yalnızca 0,05'tir: `0,05 × 200 = 10 < 20`. Değmez.

**Hangisi doğru?** Cezanın gerçekten 200 mü yoksa sistem çökmesi mi olduğuna bağlı.

Sonucu geri alınamaz olan durumlarda dayanıklı yaklaşım veya riske duyarlı ölçütler kullanılır. Bunlara örnek CVaR'dır (Conditional Value at Risk, koşullu riske maruz değer). CVaR, en kötü senaryoların ortalama maliyetine bakar.

## Meta-sezgiseller: genetik algoritma, parçacık sürüsü

Türevsiz, popülasyon tabanlı arama yöntemleridir. Aynı anda çok sayıda aday çözümü dener ve iyi olanları geliştirir.

Güç sistemi literatüründe çok yaygındır. Mülakatta ölçülü konuş.

**Mantıklı olduğu yer:**

- Amaç işlevi kara kutudur: her değerlendirme bir benzetim çalıştırır. Örnekler: dinamik benzetimle PSS (Power System Stabilizer, güç sistemi dengeleyicisi) ayarı, koruma koordinasyonu.
- Problem ayrık, dışbükey değil ve iyi bir matematiksel formülasyonu yok.
- Çok amaçlı; tek çözüm değil Pareto cephesi isteniyor.
- Çevrim dışı planlama; "yeterince iyi" çözüm yetiyor, süre sorun değil.

**Mantıksız olduğu yer:**

- Problem LP, QP (Quadratic Programming, karesel programlama), MILP (Mixed-Integer Linear Programming, karışık tamsayılı doğrusal programlama) veya SOCP olarak yazılabiliyorsa. Örnekler: ekonomik dağıtım, DC-OPF, ünite tahsisi. Kesin çözücü hem daha hızlıdır hem en iyiliği kanıtlar.
- Gerçek zamanlı işletme. Sonuç her çalıştırmada farklı çıkar (rastlantısaldır), süre garantisi yoktur.
- Çözümün ne kadar iyi olduğunu söylemen gerekiyorsa. Meta-sezgisel alt sınır ve en iyilik aralığı vermez.
- Çok sayıda eşitlik kısıtı varsa. Kısıtlar ceza terimiyle sağlanır; ceza katsayısını ayarlamak ayrı bir problemdir.
- Gölge fiyata ihtiyaç varsa.

Hazır cümle:

> **Mülakatta şöyle söyle:** "Önce problemi dışbükey veya karışık tam sayılı biçimde yazmaya çalışırım. Yazamıyorsam ve amaç bir benzetimin çıktısıysa meta-sezgisel kullanırım; sonucu bir alt sınırla veya basit bir sezgiselle kıyaslarım."

## Araçlar

Araçlar iki gruba ayrılır: modelleme dilleri ve çözücüler.

| Araç | Ne | Ne zaman |
| --- | --- | --- |
| **Pyomo** | Python'da cebirsel modelleme dili. Modeli yazarsın, çözücüye o çevirir | Büyük, yapılandırılmış modeller; LP'den doğrusal olmayana her sınıf; çözücü değiştirme özgürlüğü |
| **CVXPY** | Dışbükey eniyileme için modelleme dili. Dışbükeyliği **kurallarla denetler** | SOCP ve SDP gevşetmeleri, hızlı prototip. Dışbükey olmayan modeli reddeder; bu bir özelliktir |
| **Gurobi** | Ticari çözücü: LP, QP, MILP, SOCP | En hızlılardan; akademik lisansı ücretsiz. Ürüne gömmek lisans ister |
| **HiGHS** | Açık kaynak çözücü: LP, MILP, QP | Lisans engeli yok; `scipy.optimize.linprog` ve `milp`'in arkasındaki çözücü |
| **Ipopt** | Açık kaynak iç nokta çözücü: doğrusal olmayan | AC-OPF için standart yerel çözücü |
| MOSEK, CPLEX, SCIP | Konik, MILP | MOSEK konik problemlerde güçlü; SCIP açık kaynak |
| PowerModels.jl | Julia'da OPF formülasyonları kütüphanesi | AC, DC, SOCP, SDP biçimlerini aynı veriyle karşılaştırmak |

Modelleme dili ile çözücü ayrı şeylerdir:

- Pyomo ve CVXPY problemi **tarif eder**.
- Gurobi, HiGHS ve Ipopt **çözer**.

Yazılım mimarisinde bu ayrım, çözücüyü değiştirebilmeni sağlar.

### SciPy ile DC-OPF

Yukarıdaki DC-OPF, SciPy ile çözülmüştür (çalıştırılıp doğrulandı; tamamı `elle_ornekler.py` içinde).

Kod şunları yapar:

- `c`: iki üretecin birim maliyetlerini (10 ve 30 TL/MWh) verir.
- `A_ub` ve `b_ub`: hat 1–3 akış sınırını yazar. Yükün sabit katkısı sağ tarafa taşınmıştır.
- `A_eq` ve `b_eq`: üretimin 150 MW yüke eşit olmasını ister.
- `bounds`: her üreteci 0–200 MW arasında tutar.
- `method="highs"`: HiGHS çözücüsünü seçer.
- Son üç satır: üretimi ve maliyeti, hat kısıtının gölge fiyatını ve güç dengesinin gölge fiyatını yazdırır.

```python
from scipy.optimize import linprog

sonuc = linprog(
    c=[10, 30],                          # TL/MWh
    A_ub=[[0, -0.181818]],               # hat 1-3 akışı, g2'ye duyarlılık
    b_ub=[80 - 0.636364 * 150],          # sınır eksi yükün katkısı
    A_eq=[[1, 1]], b_eq=[150],           # güç dengesi
    bounds=[(0, 200), (0, 200)],
    method="highs",
)
print(sonuc.x, sonuc.fun)                # [65. 85.] 3200.0  (yuvarlanmış)
print(sonuc.ineqlin.marginals)           # [-110.]  hat kısıtı: sınır 1 MW artarsa maliyet 110 düşer
print(sonuc.eqlin.marginals)             # [10.]    güç dengesi: referans baradaki enerji fiyatı λ
```

**İşarete dikkat:** SciPy, kısıtın sağ tarafı bir birim artınca amacın ne kadar **değiştiğini** verir. Hat sınırını gevşetmek maliyeti düşürdüğü için değer eksidir.

Çözücüler arasında işaret sözleşmesi farklıdır. İlk kullanımda küçük bir örnekle denetle.

**Dürüstlük notu:** Bu makinede Pyomo, CVXPY ve Gurobi kurulu değil. Onlarla yazılmış örnek kod koymadım, çünkü çalıştırıp doğrulayamadım.

Mülakatta "Pyomo veya CVXPY ile üretimde model kurdun mu?" diye sorulursa cevabın gerçeği olsun.

## Yaygın yanlış

Aşağıdaki her madde, sık duyulan yanlış bir cümle ve onun düzeltmesidir.

| Yanlış cümle | Doğrusu |
| --- | --- |
| **"DC-OPF'nin çözümü uygulanabilirdir."** | AC'de gerilim ve reaktif sınırları ihlal edebilir. AC yük akışıyla denetlenir. |
| **"LMP en pahalı çalışan santralin fiyatını geçemez."** | Elle örnekte 30'luk santral varken fiyat 80 çıktı. |
| **"Gevşetme her zaman doğru cevabı verir."** | Alt sınır verir. Sıkı olup olmadığı denetlenir. |
| **"Dayanıklı eniyileme her zaman daha güvenlidir, o halde daha iyidir."** | Daha pahalıdır; belirsizlik kümesi kötü seçilirse aşırı tutucu veya yetersiz olur. |
| **"Genetik algoritma genel en iyiyi bulur."** | Garanti etmez ve bulduğunu kanıtlayamaz. |
| **"Çözücü 'optimal' dediyse model doğrudur."** | Yanlış kurulmuş modelin en iyisini bulmuştur. |
| **"Gölge fiyat her aralıkta geçerlidir."** | Yalnızca bağlayan kısıt kümesi değişmediği sürece. |

## Panel takip sorusu

Panel, ana konuşmadan sonra bu soruları sorabilir.

**"Ünite tahsisi neden zor?"**

> **Mülakatta şöyle söyle:** "Aç-kapa kararları ikilidir, asgari çalışma ve durma süreleri dönemleri birbirine bağlar; karışık tam sayılı programdır. Dal-sınır ve kesme düzlemleriyle çözülür; çözücü en iyilik aralığını raporlar ve kabul edilebilir bir aralıkta durdurulur."

**"Çözücü 'uygun çözüm yok' derse ne yaparsın?"**

> **Mülakatta şöyle söyle:** "Hangi kısıtların çeliştiğini bulurum (indirgenemez tutarsız alt küme). Sonra katı kısıtları cezalı esnek kısıtlara çevirir, hangisinin ne kadar ihlal edildiğine bakarım. Operatöre 'çözüm yok' değil 'şu hat şu kadar aşılıyor' denir."

**"Stokastik modelde senaryoları nereden alırsın?"**

> **Mülakatta şöyle söyle:** "Geçmiş tahmin hatalarından. Çok sayıda senaryo üretir, sonra temsil gücünü koruyarak azaltırım. Örneklem dışı senaryolarla çözümün kalitesini sınarım."

### Konuşmanın özeti için hatırlatma

Aşağıdaki 90 saniyelik konuşma bu sayfanın ana fikirlerini sırayla toplar: AC'nin dışbükey olmaması, DC modelin gölge fiyatları, bara fiyatının en pahalı santrali aşabilmesi, gevşetmeyle alt sınır, stokastik ile dayanıklı model farkı ve meta-sezgiselin yeri.

## 90 saniye

"AC optimal güç akışı dışbükey değildir. Hız ve kesinlik gerekince doğrusal DC modelini kullanırım; bu bir doğrusal programdır ve her kısıtın gölge fiyatını verir. Güç dengesinin gölge fiyatı enerji fiyatıdır; dolu bir hattın gölge fiyatı, o hattın bir megavatlık kapasitesinin değeridir. Bara fiyatı, enerji fiyatına hat gölge fiyatı çarpı duyarlılık eklenerek bulunur ve en pahalı santralin fiyatını aşabilir. Daha doğru bir model için konik veya yarı kesin gevşetmeyle alt sınır alır, sıkı olup olmadığını denetlerim. Belirsizlikte stokastik model beklenen maliyeti, dayanıklı model en kötü durumu eniyiler. Meta-sezgiseli yalnızca problem kara kutuysa kullanırım."
