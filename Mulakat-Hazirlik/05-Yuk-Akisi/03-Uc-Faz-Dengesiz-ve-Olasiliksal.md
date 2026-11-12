# Dengesiz ve olasılıksal yük akışı

Bu sayfa iki konuyu anlatır: dağıtımda fazların neden ayrı modellendiği (dengesiz üç fazlı yük akışı) ve belirsiz girdilerle nasıl hesap yapıldığı (olasılıksal yük akışı).

## Dengesiz üç fazlı yük akışı

İletimde üç faz dengeli kabul edilir ve tek faz çözülür. Dağıtımda bu varsayım tutmaz:

- Evler ve çatı güneşleri tek fazlıdır; fazlara eşit dağılmaz.
- Hatlar çaprazlanmaz; fazlar arası karşılıklı empedans eşit değildir.
- Tek ve iki fazlı kol hatlar vardır.
- Nötr iletkeni akım taşır.

Sonuç: her bara üç gerilim, her hat `3 × 3` empedans matrisi ile temsil edilir.

Aşağıdaki denklem, hattın uç gerilimini baş gerilimden empedans matrisi ile akımın çarpımını çıkararak bulur:

```
[ V_a ]         [ V_a ]       [ Z_aa  Z_ab  Z_ac ] [ I_a ]
[ V_b ]       = [ V_b ]     − [ Z_ba  Z_bb  Z_bc ] [ I_b ]
[ V_c ] uç      [ V_c ] baş   [ Z_ca  Z_cb  Z_cc ] [ I_c ]
```

Köşegen dışı elemanlar fazlar arası manyetik kuplajdır. Bir fazdaki akım, diğer fazın gerilimini de düşürür.

> Sade anlatım: Üç faz aynı direğin üstünde yan yana gider. Birinden geçen akım, komşusunun gerilimini de etkiler. Bu yüzden fazları birbirinden bağımsız çözemezsin.

### Yöntemler

| Yöntem | Nasıl çalışır | Nerede |
| --- | --- | --- |
| **İleri-geri süpürme** | Geri süpürmede uçtan kaynağa akımlar toplanır, ileri süpürmede kaynaktan uca gerilim düşümleri hesaplanır. Matris çarpanlara ayırmaz; R/X (direnç/reaktans oranı) yüksekliğinden etkilenmez. | Radyal şebeke |
| **Akım enjeksiyonu / sabit nokta** | OpenDSS'in yaklaşımı: her elemanın admitans matrisi kurulur, doğrusal olmayan yük akım kaynağına çevrilir, yinelenir. | Halkalı şebekeyi de çözer |
| **Üç faz Newton** | Newton-Raphson'un üç fazlı hâli. | Genel ama Jacobian üç kat büyür |

### Dengesizliğin ölçüsü

Gerilim dengesizlik faktörü, ters dizi geriliminin doğru dizi gerilimine oranıdır (`V_2 / V_1`).

- Doğru dizi, dengeli üç fazın normal bileşenidir.
- Ters dizi, dengesizlikten doğan ters dönen bileşendir.

Tipik sınır %2 civarındadır. Dengesizlik motorları ısıtır, nötr akımını ve kaybı artırır.

### Elle örnek: dengesizliğin kayba etkisi

Bu örnek, aynı toplam akımın dengesiz dağılınca neden daha fazla kayıp yaptığını gösterir.

**Veri.** Dört telli alçak gerilim hattı, faz ve nötr direnci 0,1 Ω. Toplam yük 300 A.

**Dengeli durum.** Her faz 100 A. Nötr akımı sıfır. Kayıp, üç fazın `I² R` toplamıdır:

```
Kayıp = 3 × 100² × 0,1 = 3,0 kW
```

**Dengesiz durum.** Fazlar 200, 50 ve 50 A (aynı güç faktörü).

Aşağıdaki bloğun adımları:

1. İlk satır nötr akımını bulur. Nötr akımı, üç fazörün toplamıdır. 120° kaymış iki 50 A'lık fazörün gerçel kısmı −25'er A'dır, sanal kısımları birbirini götürür.
2. İkinci satır kaybı hesaplar: önce üç faz iletkenindeki `I² R`, sonra nötr iletkenindeki `I² R`.

```
I_n = 200∠0° + 50∠−120° + 50∠120° = 200 − 25 − 25 = 150 A
Kayıp = (200² + 50² + 50²) × 0,1 + 150² × 0,1 = 4,5 + 2,25 = 6,75 kW
```

**Sonuç.** Aynı toplam akım, **2,25 kat** kayıp (6,75 / 3,0).

- Tek faz eşdeğeriyle çalışan bir yazılım bu farkı göremez.
- 200 A taşıyan fazın gerilim düşümü diğerlerinden kat kat büyüktür.
- İlk bant dışına çıkan o fazdaki müşteridir.

## Olasılıksal yük akışı

Klasik yük akışı tek bir senaryo çözer: "yük 100 MW, rüzgâr 40 MW". Gerçekte ikisi de belirsizdir.

Olasılıksal yük akışı girdiyi dağılım olarak alır, çıktıyı da dağılım olarak verir: "bu hattın aşırı yüklenme olasılığı %3".

> Sade anlatım: Tek bir yarını değil, binlerce olası yarını çözersin. Sonra "kaçında hat aşırı yüklendi" diye sayarsın.

### Monte Carlo

Yazılımcı için en doğal yöntemdir:

1. Belirsiz girdiler için dağılım tanımla (yük, rüzgâr, güneş; aralarındaki korelasyonla birlikte).
2. Dağılımlardan bir örnek çek.
3. Deterministik yük akışını çöz.
4. Sonucu kaydet.
5. `N` kez tekrarla; histogram, ortalama, yüzdelik ve ihlal olasılığını çıkar.

Hata, örnek sayısının kareköküyle azalır. σ, çıktının standart sapmasıdır:

```
standart hata = σ / √N
```

Doğruluğu on kat artırmak yüz kat örnek ister.

### Elle örnek: kaç örnek gerekir

**Ortalama için.** Bir hattın akışının standart sapması 20 MW. Ortalamayı ±1 MW (bir standart hata) doğrulukla istiyorum.

Aşağıdaki satır, standart hata formülünü `N` için çözer ve sayıları koyar:

```
N = (σ / hata)² = (20 / 1)² = 400 örnek
```

±0,1 MW için 40.000 örnek gerekir. Hata 10 kat küçülünce örnek sayısı 100 kat büyür.

**Nadir olay için.** Nadir olay daha pahalıdır. Aşırı yüklenme olasılığı `p = 0,01` ise ve bunu %10 göreli hatayla kestirmek istiyorsam:

Aşağıdaki satır, olasılık kestiriminin göreli hata formülüne `p = 0,01` ve göreli hata `0,1` koyar:

```
N ≈ (1 − p) / (p × 0,1²) = 0,99 / (0,01 × 0,01) ≈ 9.900 örnek
```

`p = 0,0001` için yaklaşık bir milyon. Güvenilirlik hesaplarının neden pahalı olduğu bu sayıdadır.

### Hızlandırma

| Yöntem | Nasıl | Artı / eksi |
| --- | --- | --- |
| **Doğrusallaştırma** | DC model veya çalışma noktası çevresinde duyarlılık (PTDF, Power Transfer Distribution Factor, güç transfer dağıtım faktörü). Çıktı, girdilerin doğrusal birleşimidir; dağılım analitik bulunur. | Hızlı, büyük sapmada hatalı |
| **Nokta kestirim yöntemi** | Her belirsiz girdi için iki-üç özenle seçilmiş noktada yük akışı; `2m` veya `2m + 1` çözüm (`m` belirsiz girdi sayısı). | Momentleri verir, kuyrukları iyi vermez |
| **Akıllı örnekleme** | Latin hiperküp, yarı rastgele diziler, önem örneklemesi (nadir olay için). | Aynı doğruluğa daha az örnekle ulaşır |
| **Paralellik** | Örnekler bağımsızdır; iş parçacıklarına veya makinelere doğrudan dağıtılır. | Her işin kendi rastgele sayı tohumu olmalıdır, yoksa sonuç yinelenemez |

### Korelasyon

En sık yapılan modelleme hatası girdileri bağımsız çekmektir. Gerçekte girdiler birlikte hareket eder:

- Aynı bölgedeki rüzgâr santralleri birlikte üretir.
- Sıcak günde her yerde yük birlikte artar.
- Güneş ile öğlen yükü ilişkilidir.

Bağımsız çekim uçları birbirine götürtür ve riski **küçük** gösterir.

Korelasyon modele şu yollarla girer:

- korelasyon matrisi ve Cholesky ayrışımı,
- kopula.

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"Dengesizlik küçük bir düzeltmedir."** | Alçak gerilimde kaybı ikiye katlayabilir ve tek bir fazı bant dışına çıkarabilir. |
| **"Üç fazı ayrı ayrı çözer, toplarım."** | Fazlar manyetik olarak bağlıdır; ayrı çözülemez. |
| **"Simetrik bileşenler dağıtımı da çözer."** | Dizi devrelerinin birbirinden bağımsız olması, hattın simetrik olmasını gerektirir. Çaprazlanmamış dağıtım hattında diziler de bağlıdır; faz koordinatlarında çalışılır. |
| **"Monte Carlo'da bin örnek her şeye yeter."** | Ortalama için yeter, yüzde birlik kuyruk için yetmez. |
| **"Olasılıksal sonuç kesin sonuçtan daha doğrudur."** | Girdi dağılımı yanlışsa çıktı da hassas görünen bir yanlıştır. |

## Panel takip sorusu

Panelin bu konudan sonra sorabileceği iki soru ve cevapları:

> Mülakatta şöyle söyle — "Monte Carlo sonucunun yeterli olduğunu nasıl anlarsın?" Cevap: ilgilendiğim büyüklüğün (ortalama, yüzdelik, ihlal olasılığı) güven aralığını izlerim; aralık kabul sınırının altına inince dururum. Sabit bir örnek sayısıyla durmam.

> Mülakatta şöyle söyle — "On bin yük akışını nasıl hızlandırırsın?" Cevap: topoloji değişmediği için matrisin simgesel çarpanlara ayrılmasını bir kez yaparım, her örneği önceki çözümden başlatırım, örnekleri paralel koşarım. Yetmezse doğrusal modelle tarar, yalnız sınıra yakın örnekleri AC ile çözerim.

AC burada alternatif akım modeli, yani tam doğrusal olmayan yük akışı demektir.

Aşağıdaki metin, bu sayfanın mülakatta yüksek sesle söylenecek özetidir.

## 90 saniye

> Mülakatta şöyle söyle: "Dağıtım şebekesi dengesizdir: tek fazlı yükler, çaprazlanmamış hatlar ve akım taşıyan nötr vardır. Bu yüzden her hattı üçe üç empedans matrisiyle modeller, radyal şebekede ileri-geri süpürmeyle çözerim. Dengesizlik aynı toplam akımda kaybı katlar ve tek bir fazın gerilimini bozar. Belirsizlik için olasılıksal yük akışı kullanırım; en basit hali Monte Carlo'dur: dağılımdan örnek çek, çöz, tekrarla. Hata örnek sayısının kareköküyle azalır, nadir olaylar çok örnek ister ve girdiler arasındaki korelasyonu atlamak riski küçük gösterir."
