# Optimizasyon

## İlan ne istiyor

İlan, optimizasyon tekniklerini programlama dilleriyle aynı maddede ister. Yani optimizasyonu kâğıt üstünde değil, kod yazarak uygulayabilmen beklenir.

Beklenen seviye üç adımdır:

1. Problemi doğru sınıfa koy.
2. Çöz.
3. Sonucu fizikle kontrol et.

Çözücü markası ezberi yetmez. "Gurobi kullanırım" demek, problemin neden o çözücüye uygun olduğunu açıklamanın yerini tutmaz.

> **Sade anlatım:** Optimizasyon, kurallara uyarak en ucuz (veya en iyi) seçimi bulmaktır. Mülakatta önce "bu ne tür bir problem" sorusunu cevaplaman, sonra çözümün gerçek şebekede çalışıp çalışmadığını kontrol etmen beklenir.

## Sınıflar

Optimizasyon problemleri, amaç fonksiyonunun ve kısıtların biçimine göre sınıflara ayrılır. Sınıf, hangi çözücüyü kullanacağını ve sonuca ne kadar güvenebileceğini belirler.

Önce kısaltmalar:

| Kısaltma | Açılımı | Türkçesi |
| --- | --- | --- |
| LP | Linear Programming | Doğrusal programlama |
| QP | Quadratic Programming | Karesel programlama |
| MILP | Mixed-Integer Linear Programming | Karışık tamsayılı doğrusal programlama |
| NLP | Nonlinear Programming | Doğrusal olmayan programlama |
| MINLP | Mixed-Integer Nonlinear Programming | Karışık tamsayılı doğrusal olmayan programlama |
| SDP | Semidefinite Programming | Yarı kesin programlama |
| SOCP | Second-Order Cone Programming | İkinci dereceden konik programlama |
| DC-OPF | Direct Current Optimal Power Flow | Doğru akım yaklaşımlı optimal güç akışı |
| AC-OPF | Alternating Current Optimal Power Flow | Alternatif akımlı (tam fizikli) optimal güç akışı |

Şimdi sınıflar ve güç sistemindeki karşılıkları:

| Sınıf | Ne zaman | Güç sistemi örneği |
| --- | --- | --- |
| LP | Amaç ve kısıt lineer | DC-OPF, ekonomik dağıtımın parçalı lineer hali |
| QP | Karesel amaç, lineer kısıt | Kayıplı ekonomik dağıtım |
| MILP | LP + ikili/tamsayı | Ünite tahsisi, hat anahtarlama, kademe |
| NLP | Sürekli, lineer olmayan | AC-OPF |
| MINLP | NLP + tamsayı | Kademeli AC-OPF. Zordur, çoğu zaman gevşetilir |
| SDP / SOCP | Dışbükey gevşeme | AC-OPF araştırması. İşletme motorunda hâlâ nadir |

Tablodaki birkaç terimi açalım:

- **İkili değişken:** Yalnızca 0 veya 1 alabilen değişkendir. Örneğin bir santralin kapalı (0) veya açık (1) olması.
- **Ünite tahsisi:** Hangi santralin hangi saatte devrede olacağına karar vermektir.
- **Kademe:** Trafonun gerilim oranını adım adım değiştiren ayar noktasıdır.
- **Gevşetmek:** Zor bir kısıtı daha kolay bir kısıtla değiştirip problemi çözülebilir hale getirmektir.

### Dışbükeylik

Dışbükey (konveks) problemde yerel minimum, küresel minimumdur. Yani çözücünün bulduğu "dip" noktası, bütün problemin en dip noktasıdır.

AC-OPF dışbükey değildir. Bu yüzden "Çözücü bir sayı verdi, optimumdur" denmez.

AC-OPF sonucuna güvenmek için üç kontrol gerekir:

| Kontrol | Ne işe yarar |
| --- | --- |
| Farklı başlangıç | Çözücü farklı noktalardan başlayınca aynı sonuca varıyor mu, bakılır |
| DC gevşeme alt sınırı | Bulunan maliyetin, olabilecek en iyi maliyete ne kadar yakın olduğu görülür |
| AC yük akışı kontrolü | Sonucun gerçek fizikle (gerilim, reaktif güç) tutarlı olup olmadığı denetlenir |

> **Sade anlatım:** Dışbükey problem tek çukurlu bir kâse gibidir; topu nereden bırakırsan bırak aynı dibe yuvarlanır. AC-OPF ise çok çukurlu bir arazidir; top bir çukura düşer ama en derin çukur o olmayabilir.

## KKT

KKT, Karush-Kuhn-Tucker koşullarının kısaltmasıdır. Bir noktanın en iyi nokta olabilmesi için sağlaması gereken matematiksel koşullardır.

### Eşitlik kısıtı

Problem şudur: `min f(x), g(x)=0`. Yani `g(x)=0` kuralına uyarak `f(x)`'i en küçük yap.

Koşullar aşağıdaki iki satırdır. İlk satır, en iyi noktada amacın eğimi ile kısıtın eğiminin λ ile dengelendiğini söyler. İkinci satır, kısıtın sağlandığını söyler.

```
∇f + λ ∇g = 0
g(x) = 0
```

Burada:

- `∇f`: amaç fonksiyonunun gradyanı (eğim vektörü).
- `∇g`: kısıtın gradyanı.
- `λ` (lambda): Lagrange çarpanı.

λ gölge fiyattır. Güç dengesinin λ'sı, o barada bir MW'nin (megavat) fiyatıdır.

Düğüm bazlı fiyatlama, yani LMP (Locational Marginal Price, bölgesel/düğüm marjinal fiyatı), bu çarpandan gelir. LMP'nin üç bileşeni vardır:

| Bileşen | Anlamı |
| --- | --- |
| Enerji | Sistemin genelindeki marjinal üretim maliyeti |
| Kayıp | O baraya güç taşırken hatlarda kaybolan enerjinin bedeli |
| Kısıt | Dolu hatlar yüzünden oluşan sıkışıklık bedeli |

### Eşitsizlik kısıtı

Eşitsizlik `h(x) ≤ 0` için çarpan μ (mü) kullanılır ve μ ≥ 0 olmalıdır.

Ek olarak tamamlayıcı gevşeklik koşulu vardır: `μ h = 0`. Bu çarpım sıfır olduğu için iki durumdan biri doğrudur:

| Durum | μ'nün değeri | Anlamı |
| --- | --- | --- |
| Kısıt boştaysa (h < 0) | μ sıfırdır | Limit zorlamıyor, gevşetmenin değeri yok |
| Kısıt aktifse (h = 0) | μ, o limiti bir birim gevşetmenin değeridir | Limit zorluyor, gevşetmek maliyeti düşürür |

Hat limiti bağlayıcıysa o hattın μ'su sıkışıklık maliyetidir.

> **Sade anlatım:** μ, "bu sınırı biraz açsam ne kazanırım" sorusunun cevabıdır. Sınır zaten rahatsa cevap sıfırdır. Hat dolmuşsa cevap, o hattın bir MW fazla taşımasının sana kazandıracağı paradır.

### Mülakatta nasıl kullanılır

Mülakatta türev ispatı istenirse yukarıdaki iki satırı yaz. Sayfa dolusu teori isteme.

Hemen güç sistemine dön ve şunu söyle:

> **Mülakatta şöyle söyle:** "Hat limitinin gölge fiyatı yeniden dağıtım maliyetidir."

## Nasıl çözülür

Her problem sınıfının kendine uygun çözüm yöntemi vardır.

### LP ve MILP

Yöntemler:

- **Simpleks:** Uygun bölgenin köşeleri arasında dolaşarak en iyi köşeyi bulur.
- **İç nokta:** Uygun bölgenin içinden geçerek en iyiye yaklaşır.
- **Dal-kesme (branch-and-cut):** MILP'de kullanılır. Tamsayı değişkenleri dallara ayırır ve kesme düzlemleriyle arama alanını daraltır.

Modeller için çözücüler: CBC, HiGHS, Gurobi, CPLEX.

| Çözücü | Tür | Not |
| --- | --- | --- |
| CBC (COIN-OR Branch and Cut) | Açık kaynak | İş görür |
| HiGHS | Açık kaynak | İş görür |
| Gurobi | Ticari | Büyük ünite tahsisinde belirgin hızlanır |
| CPLEX | Ticari | Büyük ünite tahsisinde belirgin hızlanır |

Açık kaynakta HiGHS ve CBC iş görür. Büyük ünite tahsisinde ticari çözücü belirgin hızlanır.

Lisans yoksa dürüst bir cevap şudur:

> **Mülakatta şöyle söyle:** "HiGHS ile kurarım, ölçek büyürse ticari çözücüye aynı modeli veririm."

Model, çözücüden bağımsız yazılırsa bu geçiş kolaydır. Pyomo ve OR-Tools (Google'ın optimizasyon araçları kütüphanesi) bunu sağlar.

### NLP

Yöntemler: ardışık karesel programlama veya iç nokta. İç nokta için standart çözücü IPOPT'tur (Interior Point OPTimizer, iç nokta eniyileyicisi).

AC-OPF için başlangıç olarak yük akışı çözümü verilir. Böylece çözücü fiziksel olarak anlamlı bir noktadan aramaya başlar.

### Sezgiseller

Türev yoksa son çare sezgiseldir. Genetik algoritma ve parçacık sürüsü, kısıtı ceza fonksiyonuyla tutturmaya çalışır. Yani kısıt ihlal edilirse amaca büyük bir ceza eklenir.

| Kullanılır | Kullanılmaz |
| --- | --- |
| Küçük yerleştirme (kapasitör, DG yeri). DG: Distributed Generation, dağıtık üretim | Ulusal iletim OPF'i |

Ulusal iletim OPF'inde neden kullanılmaz:

- Tekrar üretilemez; her çalıştırmada farklı sonuç çıkabilir.
- Kısıt ihlalini gizleyebilir.

### Ayrık kademe

Trafo kademesi gibi ayrık ama sıralı adımlar için yöntem:

1. Sürekli gevşet (kademeyi her değeri alabilen bir sayı gibi düşün).
2. Çöz.
3. En yakın adıma yuvarla.
4. AC ile kontrol et.

Yuvarlama ihlal doğurursa o kademeyi sabitleyip tekrar çöz.

Ünite ikilisi ise yuvarlanmaz. 0,6 açık diye bir santral yoktur. İkili, MILP'de kalır.

> **Sade anlatım:** Kademe 3,4 çıkarsa 3'e yuvarlamak küçük bir hata yaratır. Santral 0,6 çıkarsa ne 0 ne 1'e yuvarlamak doğru olur; çünkü açmak minimum üretim ve yakıt maliyeti getirir. Bu yüzden santral kararı en baştan tamsayı olarak çözülür.

## Büyük problem

Ulusal modelde N-1 kısıtlarının hepsini baştan koymak bellek ve zaman yer. N-1, "herhangi bir tek eleman (hat, trafo, ünite) arızalansa da sistem güvenli kalmalı" kuralıdır.

Bunun yerine şu döngü kullanılır:

1. Baz OPF çöz.
2. N-1 tara, ihlalleri topla.
3. İhlalleri kısıt diye ekle.
4. Tekrar çöz. Yeni ihlal yoksa dur.

Çoğu arıza zaten sorun çıkarmadığı için, yalnızca gerçekten ihlal yaratanları eklemek problemi küçük tutar.

### Benders ayrıştırması

Benders ayrıştırması aynı fikrin resmidir. Problem iki kata ayrılır:

| Katman | İçerik |
| --- | --- |
| Ana problem | Yatırım veya ünite kararları |
| Alt problem | Her senaryo veya her arızanın fizibilitesi (uygulanabilirliği) |

Alt problemden gelen kesit (cut) ana probleme "bu karar şu arızada olmuyor" der. Ana problem bu bilgiyi yeni kısıt olarak ekler ve tekrar karar verir.

Planlama ufku ve senaryo sayısı artınca ayrıştırma, tek parça NLP'den daha anlatılabilir olur.

### Çok amaç

Tipik iki amaç: maliyet ve EENS (Expected Energy Not Supplied, beklenen karşılanamayan enerji). Biri ucuzluğu, diğeri güvenilirliği ölçer.

- **Ağırlıklı toplam:** İki amacı ağırlıklarla toplayıp tek amaç yapar. Ağırlık politiktir; teknik değil, karar vericinin tercihidir.
- **Pareto cephesi:** Birini bozmadan diğerinin iyileşemediği noktalardır.

Karar vericiye iki üç nokta göstermek, tek "optimum" göstermekten daha dürüsttür.

## Teşhis

Çözücü beklenmedik bir sonuç verdiğinde ne yapacağını bilmek, mülakatta deneyim göstergesidir.

- **Infeasible (uygun çözüm yok):** Kısıtlar çelişiyor. Hangi kısıtın çeliştiğini izolasyonla bul (yedek yetmiyor, hat limiti ile üretimin yeri uyumsuz). Ceza ile yumuşatılmış kısıt, hangi limitin pahalıya kırıldığını gösterir.
- **Unbounded (sınırsız):** Maliyeti düşüren açık bir yön var. Eksik Pmax (en büyük üretim sınırı) veya işaret hatası.
- **Zayıf gevşeme:** MILP alt sınırı ile bulunan tam sayı çözüm çok ayrıksa, ya süre yetmemiştir ya formülasyon gevşektir.
- **Fizik tutmuyor:** DC optimumunu AC yük akışına ver, gerilim ve Q (reaktif güç) limitine bak.

İşaret ve birim, optimizasyonda da yük akışındaki kadar çok hata üretir. MW ile pu'yu (per unit, birim değer) aynı kısıtta toplamak sessizce yanlış plan üretir.

> **Sade anlatım:** Çözücü hata vermez, yanlış modeli de mutlu mutlu çözer. Birim karışıklığı uyarı üretmez; sadece yanlış bir plan çıkar.

### Konuşmanın özeti için hatırlatma

Aşağıdaki 90 saniyelik konuşma bu sayfanın bütün ana fikirlerini sırayla toplar: sınıflandırma, λ ve μ'nün anlamı, AC kontrolü, N-1 döngüsü, kademe ile ünite farkı ve çözücüden bağımsız model.

## 90 saniye

“Problemi önce sınıfa koyarım: paylaşım LP veya QP, ünite tahsisi MILP, AC limit NLP. λ güç dengesinin gölge fiyatıdır, hat limitinin çarpanı sıkışıklıktır. AC-OPF’in yerel çözümünü yük akışıyla kontrol ederim. N-1’i baştan değil, ihlal oldukça eklerim. Kademeyi gevşetip yuvarlarım, üniteyi yuvarlamam. Modeli çözücüden bağımsız kurarım.”
