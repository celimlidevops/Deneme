# Ekonomik işletme

Bu sayfa, ekonomik işletmenin dört ana problemini sırayla anlatır:

| Kısaltma | Açılımı | Türkçesi | Sorduğu soru |
| --- | --- | --- | --- |
| ED | Economic Dispatch | Ekonomik dağıtım | Devredeki üniteler yükü nasıl paylaşsın? |
| UC | Unit Commitment | Ünite tahsisi | Hangi ünite, hangi saatte devrede olsun? |
| OPF | Optimal Power Flow | Optimal güç akışı | Şebeke sınırlarıyla birlikte üretim ne olsun? |
| SCOPF | Security-Constrained Optimal Power Flow | Güvenlik kısıtlı optimal güç akışı | N-1 arızalarından sonra da sınırlar korunsun mu? |

Sonra rezervi, Türkiye piyasasını ve bir optimizasyon sonucunun sahada uygulanabilir olup olmadığını nasıl sınayacağını anlatır.

## Eşit artan maliyet

Termik ünitenin yakıt maliyeti çoğunlukla ikinci dereceden (karesel) bir fonksiyonla yaklaştırılır.

Aşağıdaki blok iki şey yazar: birinci satır ünitenin saatlik maliyetini, ikinci satır bu maliyetin türevini, yani artan maliyeti verir.

```
C_i(P_i) = a_i + b_i P_i + c_i P_i²
dC_i/dP_i = b_i + 2 c_i P_i
```

Terimler:

- `C_i`: i. ünitenin maliyeti.
- `P_i`: i. ünitenin ürettiği aktif güç (MW).
- `a_i`: sabit terim; ünite çalıştığı sürece üretimden bağımsız ödenen maliyet.
- `b_i`, `c_i`: maliyetin üretimle doğrusal ve karesel artışını belirleyen katsayılar.
- `dC_i/dP_i`: artan maliyet; bir MW daha üretmenin maliyeti.

Kayıpsız ve limitsiz bir sistemde optimum, her ünitenin artan maliyetinin eşitlenmesidir. Bu ortak değere λ (lambda) denir. λ, sistemin bir MW daha istemesinin fiyatıdır.

> **Sade anlatım:** İki ünitenin "bir MW daha" maliyeti farklıysa, pahalıdan alıp ucuza vermek toplam faturayı düşürür. Bu alışveriş, iki maliyet eşitlenince biter. Eşitlendikleri değer λ'dır.

Aşağıdaki blok optimum koşulunu yazar: birinci satır "her ünitenin artan maliyeti λ'ya eşit", ikinci satır "toplam üretim yüke eşit" der.

```
b_i + 2 c_i P_i = λ
Σ P_i = P_yük
```

Pmin ve Pmax (ünitenin alt ve üst üretim sınırı) varsa problem eşitsizlik içerir. Limitine dayanmış ünitenin λ'sı, serbest ünitelerin λ'sına eşit olmak zorunda değildir.

Lagrange çarpanı limitte eşitsizlik olarak kalır. Bu koşullara KKT (Karush-Kuhn-Tucker) koşulları denir. Bunu `13` klasöründeki dille aynı söyle.

### Kayıp varsa: ceza faktörü

Kayıp varsa her ünitenin artan maliyeti bir ceza faktörüyle çarpılır.

Aşağıdaki blokta birinci satır ceza faktörünün tanımıdır, ikinci satır kayıplı durumdaki optimum koşuludur.

```
L_i = 1 / (1 - ∂P_kayıp/∂P_i)
(dC_i/dP_i) * L_i = λ
```

- `L_i`: i. ünitenin ceza faktörü.
- `∂P_kayıp/∂P_i`: i. ünite 1 MW artınca toplam kaybın ne kadar arttığı (artan kayıp).

Yükün uzağındaki üretim kaybı artırıyorsa L_i > 1 olur. O üretim, gerçekte olduğundan daha pahalıymış gibi değerlendirilir.

Bu, "reaktif ve aktif yerinde kalsın" (güç tüketildiği yere yakın üretilsin) ilkesinin ekonomik halidir.

## Ünite tahsisi

Ekonomik dağıtım, zaten devrede olan üniteler arasında yükü paylaşır. Ünite tahsisi ise kimin devrede olacağına karar verir. Karar ikilidir: açık veya kapalı.

Ünite tahsisinin kısıtları:

- Güç dengesi ve yedek
- Pmin, Pmax, rampa (ünitenin çıkışını dakikada en fazla ne kadar değiştirebileceği)
- En az açık kalma, en az kapalı kalma süresi
- İlk yol alma maliyeti ve ısınma
- Hidro için suyun günlük enerji bütçesi, rezervuar
- Emisyon veya yakıt kotası, varsa

Problemin boyutları:

| Özellik | Değer |
| --- | --- |
| Ufuk | 24 veya 36 saat |
| Zaman adımı | 15 veya 60 dakika |
| Model türü | MILP (Mixed-Integer Linear Programming, karışık tam sayılı doğrusal programlama) |
| Çözüm yöntemi | Lagrange gevşetmesi veya modern MILP çözücüleri (dal-kesme, branch-and-cut) |

İkili değişken çoktur; bu yüzden özel çözüm yöntemleri gerekir. Sonuç, gün öncesi planın iskeletidir.

Rampa ihmal edilirse plan kâğıtta ucuz, sahada uygulanamaz olur.

### Yenilenebilir ünite tahsisine nasıl girer

Yenilenebilir "negatif yük" gibi yükten düşülürse problem sadeleşir. Ama tahmin sapması yedeğe kalır.

Daha doğru kurulum, yenilenebiliri senaryolu veya ihtiyat paylı yazmaktır.

Kısıntı (curtailment, yenilenebilir üretimin bilerek azaltılması) bir karar değişkenidir. Sıfır kısıntı her zaman en ekonomik veya en güvenli çözüm değildir.

## OPF

Ekonomik dağıtım şebekeyi tek bir bara (tek düğüm) sanır. OPF (optimal güç akışı) ise yük akışı denklemlerini ve şebeke limitlerini problemin içine alır.

Aşağıdaki blok OPF'nin genel yazımıdır: ilk satır amaç fonksiyonu, "kısıt:" altındaki satırlar uyulması gereken koşullardır.

```
min  Σ C_i(P_i)     veya kayıp, veya kısıntı
kısıt:
  güç dengesi (AC veya DC)
  Pmin ≤ P ≤ Pmax
  Qmin ≤ Q ≤ Qmax
  Vmin ≤ V ≤ Vmax
  |S_hat| ≤ Smax
  kademe ve şönt, ayrık veya sürekli gevşetilmiş
```

Satırların anlamı:

- Amaç: toplam maliyet, veya kayıp, veya kısıntı en aza indirilir.
- Güç dengesi: AC (tam alternatif akım) veya DC (doğru akım yaklaşımı) yük akışı denklemleri.
- `P`, `Q`: aktif ve reaktif üretim sınırları.
- `V`: bara gerilim sınırları.
- `|S_hat|`: hattan geçen görünür güç; hattın taşıma sınırı `Smax`'ı aşmamalı.
- Kademe ve şönt: transformatör kademesi ve şönt kompanzasyon; gerçekte ayrık (basamaklı) değerlerdir, ya öyle ya da sürekli değişkene gevşetilerek modellenir.

AC-OPF ile DC-OPF farkı:

| Özellik | AC-OPF | DC-OPF |
| --- | --- | --- |
| Matematik | Lineer değil, dışbükey değil | Lineer veya karesel |
| Çözüm | Yerel minimumu vardır | Hızlıdır, piyasa motorlarında kullanılır |
| Gördükleri | Gerilim ve kayıp dahil | Gerilimi ve kaybı görmez |

İşletme yazılımı çoğu zaman şöyle çalışır:

1. DC-OPF ile fiyat ve MW üretir.
2. AC ile fizibiliteyi (fiziksel olarak uygulanabilirliği) kontrol eder.
3. İhlal varsa kısıt ekleyip tekrar çözer.

### Güvenlik kısıtlı OPF

Güvenlik kısıtlı OPF (SCOPF), baz duruma ek olarak seçilmiş N-1 kısıtlarını taşır. N-1, tek bir elemanın (hat, transformatör, ünite) devre dışı kaldığı durumdur.

| Tür | Ne yapar | Maliyet ve zorluk |
| --- | --- | --- |
| Önleyici SCOPF | Tek bir üretim planını tüm arızalara dayanıklı kılar | Daha pahalı |
| Düzelticili SCOPF | Arıza sonrası ikinci bir kontrol hareketine izin verir | Daha ucuz, modellemesi daha zor |

### Reaktif OPF

Reaktif OPF ayrı koşulabilir:

- Amaç: kayıp veya gerilim sapması.
- Karar değişkenleri: kademe, şönt, generatör Q (reaktif güç).

Aktif üretim piyasa tarafından kilitliyse geriye gerilim planlaması kalır. YTBS (Yük Tevzi Bilgi Sistemi) eğitim duyurusundaki "gerilim planlaması" bu ailedendir.

## Rezerv ve piyasa

Rezerv, henüz gerçekleşmemiş bir arıza için boşta tutulan kapasitedir.

Bedavadır sanılır, değildir. Ucuz üniteyi tam yüklemeyip pahalı üniteyi boşta tutmak günlük bir maliyettir.

| Rezerv | Görevi |
| --- | --- |
| Primer | Frekans sapmasına saniyeler içinde tepki; sözleşmeli |
| Sekonder | AGC (Automatic Generation Control, otomatik üretim kontrolü) |
| Tersiyer | 15 dakikalık dengeleme talimatı |

### Türkiye piyasası

| Mekanizma | Ne yapar | Kim işletir |
| --- | --- | --- |
| Gün öncesi piyasa | Bir sonraki günün saatlik enerji fiyatını kurar | EPİAŞ (Enerji Piyasaları İşletme A.Ş.) |
| Gün içi piyasa | Teslimata yakın düzeltme | EPİAŞ |
| Dengeleme Güç Piyasası ve sistem işletme talimatı | Gerçek zamanlı denge | TEİAŞ (Türkiye Elektrik İletim A.Ş.) / MYTM (Milli Yük Tevzi Merkezi) |
| YEKDEM (Yenilenebilir Enerji Kaynakları Destekleme Mekanizması) | Yenilenebilir destek mekanizması | — |

YEKDEM, üretim tahminini ve kısıntı tartışmasını etkiler. Ama bir yük akışı denklemi değildir.

Piyasa fiyatı ile fizik kısıtı çelişirse fizik kazanır. Aradaki fark, yeniden dağıtım maliyeti olarak ortaya çıkar.

### Kısıt yönetimi

Gün öncesi sonuç şebekeye sığmıyorsa TEİAŞ bir bölgede yük aldırır, başka bir bölgede yük attırır.

- İki talimatın fiyat farkı, kısıtın maliyetidir.
- Analiz yazılımı, bu talimatın limitleri çözdüğünü ve yeni bir N-1 sorunu doğurmadığını göstermelidir.

### Hidro farklıdır

Hidro, termikten farklıdır: bugünkü suyun yarınki değeri vardır.

- Sadece bu saatin λ'sına bakmak barajı boşaltır.
- Zincirleme santral (aynı nehir üzerinde arka arkaya santraller) su gecikmesini de modele koyar.
- Pompalı depolama hem yük hem üretimdir.

## Uygulanabilirlik

Bir optimizasyon "%2 daha ucuz" dediğinde şunları sor:

- AC yük akışı çözüyor mu, yoksa DC mi?
- N-1 dahil mi?
- Rampa ve kişilerin sahada uygulayacağı adım var mı?
- Tam sayı karar (kademe, kesici, ünite) gevşetilip unutulmuş mu?
- Tahmin saparsa plan devriliyor mu?

YTBS'nin "en düşük maliyet ve en yüksek güvenilirlik" cümlesi tam olarak bu çok amaçlı yapıdır.

Tek amaçlı en ucuz plan, güvenilirliği satmış olabilir. Güvenilirliği ağırlık veya kısıt olarak yazmak bir mühendislik tercihidir; tercihi gizlemek olmaz.

`ornekler/ekonomik_dagitim.py` iki üniteli eşit λ çözümünü analitik ve çözücüyle yan yana koyar.

## 90 saniye

“Ekonomik dağıtım, artan maliyetleri eşitleyerek devredeki üniteleri paylaşır; kayıp varsa ceza faktörü biner. Ünite tahsisi kimin açık olacağıdır, MILP’dir, rampa ve en az açık süre vardır. OPF buna şebeke limitini ekler. SCOPF bir de N-1 ekler. Türkiye’de enerji fiyatı EPİAŞ’ta, dengeleme ve kısıt talimatı TEİAŞ’ta oluşur. Fizik sığmıyorsa yeniden dağıtım yapılır ve yeni durum tekrar taranır.”
