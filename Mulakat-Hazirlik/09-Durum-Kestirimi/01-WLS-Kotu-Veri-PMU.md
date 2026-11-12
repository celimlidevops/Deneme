# Durum kestirimi

## Neden var

SCADA (Supervisory Control and Data Acquisition, uzaktan izleme ve veri toplama sistemi) şebekede üç tür büyüklük ölçer:

- bara gerilimleri,
- hat akışları,
- bara enjeksiyonları (baraya giren ya da çıkan net güç).

Bu ölçümlerin dört kusuru vardır:

| Kusur | Anlamı |
| --- | --- |
| Gürültü | Her ölçüm gerçek değerin biraz sapmış hâlidir |
| Eksiklik | Bazı noktalarda ölçüm cihazı yoktur |
| Bozukluk | Bir kısım ölçü tamamen yanlıştır |
| Senkron eksikliği | Zaman damgaları tam olarak aynı ana ait değildir |

Yük akışı ise üretimin ve yükün doğru bilindiğini varsayar. İşletmede ne ölçüm kusursuzdur ne de üretim ve yük tam bilinir.

Durum kestirimi bu boşluğu doldurur. Fazla ve gürültülü ölçümden şebekenin **en olası gerilim profilini** çıkarır. Güvenlik analizi bundan sonra bu profil üzerinde koşar.

EMS (Energy Management System, enerji yönetim sistemi) zincirinin ortasındaki halka budur:

```
topoloji işlemcisi → durum kestirimi → kötü veri → yük akışı ve N-1
```

Topoloji işlemcisi, kesici ve ayırıcı durumlarından şebekenin o anki bağlantı şemasını kurar. N-1, herhangi bir tek elemanın devre dışı kalması durumunda şebekenin güvenli kalıp kalmadığını sınayan analizdir.

> **Sade anlatım:** Ölçümler birbirini tutmaz. Durum kestirimi, fizik kurallarına uyan ve ölçümlere en yakın düşen tek bir "şebeke fotoğrafı" çizer.

## Durum vektörü ve ölçüm modeli

Durum vektörü, şebekenin bütün bara gerilim açıları ve büyüklükleridir:

```
x = [θ₂ … θn, V₁ … Vn]
```

- `θ`: bara gerilim açısı
- `V`: bara gerilim büyüklüğü
- `θ₁` yoktur, çünkü bir açının referansı sabitlenir. Açılar ancak birbirine göre anlamlıdır.

Ölçüm modeli, her ölçümü durumun bir fonksiyonu artı hata olarak yazar:

```
z = h(x) + e
```

- `z`: ölçüm vektörü
- `h`: ölçüm fonksiyonu; durumu ölçüme çevirir
- `e`: ölçüm hatası

Ölçüm türüne göre `h` şöyle davranır:

| Ölçüm | h(x) ne olur |
| --- | --- |
| Güç akışı | Yük akışı denklemlerinin aynısıdır |
| Gerilim | Doğrudan `V`'dir |
| Akım | Daha da doğrusal değildir; kötü veri testini zorlaştırır |

## Ağırlıklar

`e`'nin varyansı ölçümün kalitesini gösterir. Varyans küçükse ölçüm hassastır.

```
W = R⁻¹       R köşegen,  köşegen elemanları σ² (varyans)
```

- `R`: ölçüm hatalarının kovaryans matrisi. Hatalar bağımsız kabul edildiği için köşegendir.
- `W`: ağırlık matrisi; `R`'nin tersidir.
- Sonuç: iyi sayaca büyük ağırlık verilir.

Tipik `σ` (standart sapma), ölçünün tam skala değerinin yüzdesi olarak verilir. Gerilim ölçümünün σ'sı güç ölçümününkinden daha dar olabilir.

Ağırlığı "hepsi 1" yapmak bir hatadır. Bozuk sayacı sağlam sayaçla eşitler.

## WLS

WLS (Weighted Least Squares, ağırlıklı en küçük kareler), ölçüm ile model arasındaki farkın ağırlıklı kareler toplamını en aza indirir. Aşağıdaki ifade bu amaç fonksiyonudur:

```
J(x) = [z - h(x)]ᵀ W [z - h(x)]
```

Bu problem NR (Newton-Raphson, doğrusal olmayan denklemi ardışık doğrusallaştırarak çözen yöntem) ile çözülür.

`H = ∂h/∂x` Jacobian'dır. Dikkat: bu, yük akışı Jacobian'ı değil, **ölçüm Jacobian'ıdır**. Satırları ölçümler, sütunları durum değişkenleridir.

Her iterasyonda aşağıdaki iki satır kurulur ve çözülür. İlki kazanç matrisini tanımlar, ikincisi durum düzeltmesi `Δx`'i verir:

```
G = Hᵀ W H
G Δx = Hᵀ W [z - h(x)]
```

`G` kazanç matrisidir. Gözlenebilir sistemde tekil değildir.

Çözüm, artıklar (ölçüm ile kestirilen değer arasındaki farklar) ölçüm gürültüsüyle uyumlu olana kadar iterasyonla sürer.

Lineer ölçümde, yani yalnız PMU gerilim ve akım fazörü varsa, tek adım yeter. Aşağıdaki formül kestirimi iterasyonsuz verir:

```
x̂ = (Hᵀ W H)⁻¹ Hᵀ W z
```

PMU (Phasor Measurement Unit, fazör ölçüm birimi) gerilim fazörü durumu doğrudan görür. Akım fazörü, dikdörtgen koordinatta (gerçek ve sanal kısım) lineer yazılabilir. Bu yüzden geniş alan kestirimi klasiğinden daha hızlıdır.

## Gözlenebilirlik

Ölçümler durumu tek türlü belirliyorsa sistem **gözlenebilirdir**.

İki pratik test vardır:

| Test | Koşul |
| --- | --- |
| Sayısal | `G` tam rank |
| Topolojik | Her adada bir gerilim ölçümü ve yeterli akış ölçümüyle bütün baraları kapsayan bir ağaç kurulabiliyor |

**Kritik ölçüm:** o ölçüm kalkarsa gözlenebilirlik biter.

Kritik ölçünün hatası artık testinde gizlenir. Sebep: hesap o ölçüme birebir uymaya mecburdur, artığı sıfır çıkar.

**Kritik ölçüm çifti** de benzerdir: iki ölçüm birlikte kritiktir, birinin hatası ikisine eşit dağılır.

Ölçüm yerleşim planı, kritik ölçüm bırakmamaya çalışır.

### Pseudo-ölçüm

Ölçüm yetmezse **pseudo-ölçüm** (sözde ölçüm) konur. Örnekler:

- yük tahmini,
- bir önceki kestirim,
- tipik güç faktörü.

Ağırlığı gerçek ölçüden küçük tutulur.

Pseudo-ölçümün iki yüzü vardır. Çözümü kurtarır, çünkü gözlenebilirliği sağlar. Aynı anda çözümü kendine çeker, çünkü bir tahmin olduğu hâlde denkleme girer.

Dağıtımda pseudo-ölçüm çoğunluktadır. Bu yüzden dağıtım kestirimi "ölçüm" kadar "tahmin" problemidir. AMI (Advanced Metering Infrastructure, akıllı sayaç altyapısı) bu oranı düzeltir.

## Kötü veri

Artık, ölçüm ile kestirimden hesaplanan değer arasındaki farktır:

```
r = z - h(x̂)
```

**Tespit (ki-kare):** Sağlam modelde `J(x̂)` yaklaşık ki-kare dağılıdır. Serbestlik derecesi `m - n`'dir (ölçüm sayısı eksi durum sayısı). `J` eşiğin üstündeyse sette kötü veri vardır.

**Teşhis (normalize artık):** Hangi ölçüm olduğunu bulmak için her artık kendi standart sapmasına bölünür. İlk satır artık kovaryansını, ikinci satır normalize artığı verir:

```
Ω = R - H G⁻¹ Hᵀ     (artık kovaryansı, W = R⁻¹ ise bu form)
r_N,i = |r_i| / √Ω_ii
```

Kural şöyle işler:

1. En büyük normalize artık eşikten (çoğunlukla 3) büyükse o ölçüm şüpheli çıkar.
2. Ağırlığı düşürülür veya atılır.
3. Kestirim tekrarlanır.

Bir turda bir ölçüm atmak güvenlidir. Birden fazla atmak iyiyi de götürebilir.

### Kaldıraç noktası

Normalize artık, **kaldıraç noktasında** şaşırır.

Kaldıraç, o ölçümün çözümü fazla etkilemesidir. Tipik örnek az yedekli bir koldur. Bu durumda ki-kare bozulur ama normalize artık küçük kalır.

Şüphede ölçümün kaldıracına da bakılır. Mülakatta bu ayrımı söylemen, ders notunu aştığını gösterir.

### Kötü verinin kaynakları

Kötü veri üç kaynaktan gelir:

| Kaynak | Örnek |
| --- | --- |
| Ölçüm | Sayaç, polarite, ölçek, takılı kalmış değer |
| Topoloji | Kesici durumu yanlış; hesap, olmayan bir hattı varmış gibi görür |
| Parametre | Yanlış hat uzunluğu, yanlış kademe |

Topoloji hatası ölçüm atılarak düzelmez. Artıklar tek ölçümde değil, bir bölgede sistematik büyür.

Parametre kestirimi ayrı bir problemdir. Hat empedansı şüpheliyse onu da bilinmeyen yapmak istersin. Bu durumda bilinmeyen sayısı artar, gözlenebilirlik daha da zorlaşır.

## Hız ve hibrit

| Kaynak | Hız |
| --- | --- |
| Klasik SE (State Estimation, durum kestirimi) | SCADA turunda saniyeler-dakika çalışır |
| PMU | Saniyede onlarca fazör verir |

**Hibrit kestirim**, SCADA'nın geniş kapsamasını PMU'nun senkron açısıyla birleştirir.

Zaman hizasızlığı bir sorundur: SCADA ölçümü 5 saniye eski, PMU 20 ms eski olabilir. Modelde bu fark ya yok sayılır ya öngörüyle düzeltilir.

**Tahmin destekli kestirim**, bir sonraki durumu yük ve üretim eğiliminden öngörür. Ölçüm gelince düzeltir. Kayıp ölçüm anında pseudo-ölçüm kalitesini yükseltir.

### Güvenlik analizine bağlama

Çıktı güvenlik analizine ancak **kalite damgasıyla** girer. Şunlar "kestirim sağlam" sayılmaz:

- büyük artık,
- çözülmemiş ada,
- limit dışı gerilim.

Sağlam değilse N-1 sonucu operatöre kesinmiş gibi sunulmaz. Yazılımda bunun bayrağı olur.

## Sayısal işler

Yazılımda karşılaşılan sayısal sorunlar ve çareleri:

| Sorun | Sonuç / çare |
| --- | --- |
| Referans açı sabitlenmez | `G` tekildir |
| Ağırlıklar 10⁶ farkla yayılır | `G` hastadır (kötü koşullu). σ tabanını makul aralıkta tut |
| Sıfır empedanslı kuplaj | Durumu iki bara arasında bölüştüremez. Bara birleştir |
| Akım ölçümü mutlak değer | Türevi gerilim sıfır civarında patlar. Dikdörtgen koordinat veya dikkatli başlangıç gerekir |
| Büyük sistem | `G` seyrektir. Yoğun ters yok; seyrek çarpanlara ayırma kullanılır |

`14-Programlama/ornekler/wls_durum_kestirimi.py` üç baralık lineer bir kestirimi ve bir kötü veriyi koşar. Onu çalıştırıp artığın kime işaret ettiğini elle doğrula.

Aşağıdaki konuşma metni, bu sayfanın tamamını 90 saniyeye sığdırır.

> **Mülakatta şöyle söyle:** Önce "neden var" cümlesiyle başla, sonra WLS, gözlenebilirlik, kötü veri ve PMU sırasıyla git.

## 90 saniye

“Durum kestirimi, gürültülü ve fazla ölçüden gerilim ve açıyı bulur. WLS, ölçüm varyansının tersiyle ağırlıklar. Gözlenemeyen yere pseudo-ölçüm koyarım, ağırlığını düşük tutarım. Kötü veriyi ki-kare ile sezer, normalize artık ile yerini bulur, kritik ölçüde bu test körleşir. Topoloji hatası ölçüm atarak düzelmez. Kestirim sağlamsa N-1 ona koşar. PMU lineer ve hızlıdır, SCADA ile hibrit kullanılır.”
