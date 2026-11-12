# Düşük atalet, RoCoF, şebeke kuran ve şebeke izleyen evirici, küçük sinyal

## Atalet neden azalıyor

Senkron generatörün rotoru şebekeye **manyetik olarak kilitlidir**. Frekans düşmeye başladığı anda rotor yavaşlar ve kinetik enerjisini kendiliğinden şebekeye verir. Kontrol, ölçüm, gecikme yoktur; fiziktir.

Yenilenebilir kaynaklarda durum farklıdır:

- Güneş paneli dönmez.
- Rüzgâr türbini döner ama evirici onu şebeke frekansından ayırır.
- İkisi de varsayılan haliyle atalet vermez.

Evirici tabanlı üretim senkron santralin yerini aldıkça sistemin toplam kinetik enerjisi düşer.

Sistem ataleti, makinelerin ağırlıklı ortalamasıdır. Formül, her makinenin H'ını kendi gücüyle (S) ağırlıklandırır:

```
H_sistem = Σ (H_i × S_i) / S_sistem          toplam kinetik enerji  E_k = Σ H_i S_i   (MW·s)
```

## RoCoF: frekans değişim hızı

RoCoF (Rate of Change of Frequency), büyük bir santral kaybından sonraki ilk anda, hiçbir kontrol henüz tepki vermeden frekansın düşme hızıdır:

```
RoCoF = df/dt = (ΔP × f_0) / (2 × H_sistem × S_sistem) = (ΔP × f_0) / (2 E_k)
```

- `ΔP`: kaybedilen güç.
- `f_0`: nominal frekans (50 Hz).
- `E_k`: toplam kinetik enerji.

### Elle örnek 1

Sistemde 50.000 MVA (megavolt-amper) senkron kapasite devrede. 1000 MW'lık bir santral aniden çıkıyor.

Aynı kayıp iki farklı atalet için formüle konur; bu, ataletin RoCoF'u nasıl değiştirdiğini gösterir.

```
H = 4 s:   RoCoF = (1000 × 50) / (2 × 4 × 50.000) = 0,125 Hz/s
H = 2 s:   RoCoF = (1000 × 50) / (2 × 2 × 50.000) = 0,250 Hz/s
```

Atalet yarıya inince frekans iki kat hızlı düşer. Primer kontrolün tepki vermesi birkaç saniye sürer; o sürede frekansın ne kadar düşeceğini atalet belirler.

### Elle örnek 2: en az ne kadar atalet gerekir

Varsayım (Türkiye'nin değeri değil, hesap için): izin verilen en büyük RoCoF 0,5 Hz/s, en büyük tekil kayıp 1000 MW.

Bu kez formül ters çevrilir: RoCoF sınırı verilir, gereken en az kinetik enerji bulunur.

```
E_k,min = (ΔP × f_0) / (2 × RoCoF) = (1000 × 50) / (2 × 0,5) = 50.000 MW·s
```

Sonra kinetik enerji, ortalama atalete bölünerek kapasiteye çevrilir. Devredeki senkron makinelerin ortalama ataleti 4 s ise en az 12.500 MVA senkron kapasite devrede kalmalıdır.

Bu bir **işletme kısıtıdır**: güneşin bol olduğu bir öğlen, ucuz olduğu halde bütün senkron santralleri kapatamazsın.

YTBS (Yük Tevzi Bilgi Sistemi) eğitim duyurularında "sistem ataleti hesabı" adlı bir modül geçer; amacı büyük ihtimalle budur, yöntemini bilmiyorum.

### RoCoF neden tehlikeli

- Generatör şaftlarına mekanik zorlanma.
- RoCoF'a duyarlı ada koruma rölelerinin dağıtık üretimi topluca devreden çıkarması (zincirleme kayıp).
- Düşük frekans yük atma kademelerine primer kontrol yetişemeden ulaşılması.

## Frekans tepkisinin kademeleri

| Kademe | Süre | Kaynak |
| --- | --- | --- |
| Atalet tepkisi | 0–5 s | Dönen kütlelerin kinetik enerjisi; kendiliğinden |
| Hızlı frekans tepkisi | < 1 s | Batarya, evirici; ölçüp tepki verir |
| Primer kontrol | Saniyeler; yönetmelikte 30 s içinde | Hız regülatörü eğimi (droop) |
| Sekonder kontrol (AGC) | Dakikalar | Frekansı 50 Hz'e geri getirir |
| Tersiyer | 15 dakika | Yedekleri yeniler |

AGC (Automatic Generation Control), otomatik üretim kontrolüdür.

Ayrım:

- Atalet düşüşü **yavaşlatır**.
- Primer kontrol düşüşü **durdurur**.
- Sekonder kontrol frekansı **geri getirir**.

### Elle örnek 3: eğim (droop)

200 MW'lık ünite, %5 eğim. Frekans 0,1 Hz düşüyor.

Formül önce frekans sapmasını yüzdeye çevirir, eğime bölerek güç oranını bulur, sonra anma gücüyle çarpıp MW'a çevirir.

```
ΔP = (Δf / f_0) / R × P_anma = (0,1 / 50) / 0,05 × 200 = 8 MW
```

- `R`: eğim (droop), burada 0,05.
- `P_anma`: ünitenin anma gücü.

%5 eğim, frekans %5 (2,5 Hz) değiştiğinde ünitenin çıkışını %100 değiştirmesi demektir.

## Şebeke izleyen ve şebeke kuran evirici

GFL (Grid-Following) şebeke izleyen, GFM (Grid-Forming) şebeke kuran eviricidir.

| | Şebeke izleyen (GFL) | Şebeke kuran (GFM) |
| --- | --- | --- |
| Davranış | Akım kaynağı | Empedans arkasında gerilim kaynağı |
| Eşzamanlama | Faz kilitlemeli döngü (PLL) şebeke gerilimini ölçer ve izler | Kendi gerilim büyüklüğünü ve frekansını üretir |
| Şebekeye ihtiyaç | Güçlü bir gerilim referansı ister | Referansın kendisi olabilir |
| Frekans olayına tepki | Ölçer, sonra tepki verir (gecikmeli) | Anında, fiziğe benzer |
| Zayıf şebeke | PLL kararsızlaşabilir | Daha dayanıklı |
| Sıfırdan enerjilendirme | Yapamaz | Yapabilir |
| Bugünkü yaygınlık | Kurulu eviricilerin neredeyse tamamı | Batarya projelerinde artıyor |

PLL (Phase-Locked Loop), faz kilitlemeli döngüdür.

> **Sade anlatım:** Yazılımcı benzetmesi: şebeke izleyen evirici bir istemcidir; saati sunucudan alır. Sunucu yoksa çalışamaz. Şebeke kuran evirici saati üreten düğümlerden biridir; diğerleriyle uzlaşma kuralı (eğim) üzerinden eşzamanlanır.

Şebeke kuran kontrol yöntemleri:

- Eğim kontrolü.
- Sanal senkron makine (salınım denklemini yazılımda taklit eder).
- Sanal osilatör.

### Sınırı unutma

- Evirici akımı anma değerinin biraz üstünde sınırlıdır.
- Sanal atalet, gerçek bir enerji kaynağı (batarya, DC bara, kısılmış üretim payı) ve akım payı gerektirir.
- Akım sınırına dayanan şebeke kuran evirici, gerilim kaynağı gibi davranmayı bırakır.

"Yazılımla atalet" bedava değildir.

## Küçük sinyal kararlılığı

İki kararlılık sorusu farklı büyüklükte bozucuyu sorar:

- Geçici hal kararlılığı büyük bozucuyu (kısa devre) sorar.
- Küçük sinyal kararlılığı küçük bozucuyu sorar: sistem kendi çalışma noktası çevresinde hafifçe dürtülünce salınım **sönüyor mu, büyüyor mu**?

Yöntem: doğrusal olmayan denklemler çalışma noktası çevresinde doğrusallaştırılır.

```
dΔx/dt = A Δx
```

`A` durum matrisidir. Davranışı özdeğerleri belirler: `λ = σ ± jω`.

| Özdeğer | Anlam |
| --- | --- |
| `σ < 0` | Mod sönüyor: kararlı |
| `σ > 0` | Mod büyüyor: kararsız |
| `ω` | Salınım frekansı, `f = ω / 2π` |
| `ζ = −σ / √(σ² + ω²)` | Sönüm oranı |

Bütün özdeğerlerin gerçek kısmı negatifse sistem küçük sinyal kararlıdır. Ama yeterli değildir: `ζ` de yeterli olmalıdır. Uygulamada %5 civarı bir alt sınır aranır; %3'ün altı zayıf sönümlü sayılır.

### Elektromekanik modlar

| Mod | Ne salınır | Frekans | Not |
| --- | --- | --- | --- |
| **Yerel mod** | Bir santralin sisteme karşı salınımı | Yaklaşık 1–2 Hz | |
| **Bölgeler arası mod** | Bir bölgedeki makinelerin topluca başka bölgeye karşı salınımı | Yaklaşık 0,1–0,8 Hz | Uzun ve zayıf bağlantılarda görülür; Türkiye'nin Avrupa ile senkron bağlantısında izlenen konudur |

### Özvektörler

Özvektörler de bilgi taşır:

- **Sağ özvektör (mod şekli):** hangi makine hangi yönde salınıyor. Bölgeler arası modda iki grup zıt fazdadır.
- **Katılım faktörü:** hangi durum değişkeni bu modu en çok etkiliyor. Sönümleyiciyi (PSS) nereye koyacağını söyler.

Türkiye şebeke yönetmeliği 75 MW ve üzeri konvansiyonel ünitelerde 0–5 Hz aralığındaki elektromekanik salınımları sönümleyecek güç sistemi dengeleyicisi (PSS, Power System Stabilizer) ister (`01/02`).

### Elle örnek 4: tek makinenin modu

`02` dosyasındaki makine: `P_max = 2,0`, `δ_0 = 23,58°`, `H = 5 s`, sönüm katsayısı `D = 10 pu`.

**Doğrusallaştırma.** Sinüs eğrisi çalışma noktasında düz bir çizgiyle değiştirilir: `P_e ≈ P_e0 + K_s Δδ`. Senkronlayıcı güç katsayısı eğrinin eğimidir; yayın sertliği gibi düşün.

```
K_s = P_max cos δ_0 = 2,0 × 0,9165 = 1,833 pu/rad
```

**Denklemi kurmak.** Doğrusallaştırılmış salınım denklemi ikinci dereceden bir sistemdir (kütle-yay-sönümleyici). Her satırın işi:

- İlk satır: kütle (`2H/ω_0`), sönüm (`D/ω_0`) ve yay (`K_s`) terimleriyle hareket denklemi.
- `ω_n` satırı: sönümsüz doğal frekansı yay ve kütleden bulur.
- `ζ` satırı: sönüm oranını hesaplar.
- `λ` satırı: ikisini birleştirip özdeğeri yazar; gerçek kısım sönüm, sanal kısım salınım frekansıdır.

```
(2H/ω_0) Δδ'' + (D/ω_0) Δδ' + K_s Δδ = 0

ω_n = √(K_s ω_0 / 2H) = √(1,833 × 314,16 / 10) = 7,59 rad/s  →  1,21 Hz
ζ   = D / (4 H ω_n) = 10 / (4 × 5 × 7,59) = 0,066
λ   = −ζ ω_n ± j ω_n √(1 − ζ²) = −0,50 ± j7,57
```

**Yorum.** 1,21 Hz'lik yerel mod, %6,6 sönüm. Kabul edilebilir.

**Yükleme etkisi.** Makineyi daha ağır yüklersen:

1. `δ_0` büyür.
2. `cos δ_0` küçülür.
3. `K_s` düşer: yay gevşer, frekans düşer.

`δ_0 = 90°`'de `K_s = 0` olur; geri çağıran kuvvet kalmaz. Sürekli hal kararlılık sınırı budur.

**Uyartımın yan etkisi.** Hızlı ve yüksek kazançlı uyartım sistemi senkronlayıcı torku artırır ama sönümleyici torku **azaltabilir**, hatta negatife çevirebilir. PSS'in var oluş nedeni budur.

## Yaygın yanlış

- **"Atalet frekans düşüşünü durdurur."** Yavaşlatır. Durduran primer kontroldür.
- **"Evirici de atalet sağlar, yazılımla hallolur."** Enerji ve akım payı varsa ve şebeke kuran kontrolle. Varsayılan şebeke izleyen evirici sağlamaz.
- **"Hızlı frekans tepkisi ile atalet aynıdır."** Biri ölçüp tepki verir (gecikmeli), diğeri kendiliğindendir. İlk yüz milisaniyelerde fark eder.
- **"Kurulu güç büyükse atalet de büyüktür."** Atalet devrede olan **senkron** makinelere bağlıdır; güneşli bir öğlen en düşük değerindedir.
- **"Özdeğerlerin gerçek kısmı negatifse iş tamamdır."** Zayıf sönümlü mod, küçük bir işletme değişikliğiyle kararsızlaşır. Sönüm oranına bakılır.
- **"Küçük sinyal analizi büyük arızayı da söyler."** Doğrusaldır; yalnız çalışma noktasının yakınını anlatır.

## Panel takip sorusu

**"Bölgeler arası salınımı gerçek zamanda nasıl izlersin?"**

> **Mülakatta şöyle söyle:** Fazör ölçüm birimleriyle (PMU, Phasor Measurement Unit). İki bölgenin açı farkındaki salınımın frekansını ve sönümünü ölçüm verisinden kestiririm (Prony veya benzeri yöntemler). Model tabanlı özdeğer analizi çevrim dışıdır; ölçüm tabanlısı gerçek zamanlıdır.

**"Evirici oranı arttıkça küçük sinyal resmi nasıl değişir?"**

> **Mülakatta şöyle söyle:** Elektromekanik modlara ek olarak kontrol etkileşimi modları çıkar: PLL, akım kontrolü ve şebeke empedansı arasında, daha yüksek frekanslarda. Klasik fazör modeli bunları görmeyebilir; elektromanyetik geçici hal modeli gerekir.

## 90 saniye

> "Senkron makineler frekans değişimine kinetik enerjileriyle kendiliğinden karşı koyar; evirici tabanlı üretim varsayılan haliyle bunu yapmaz. Bu yüzden yenilenebilir arttıkça atalet düşer ve frekansın ilk düşme hızı, yani RoCoF artar; RoCoF, kayıp gücün iki katı kinetik enerjiye oranıyla orantılıdır. Şebeke izleyen evirici faz kilitlemeyle şebekeyi takip eden bir akım kaynağıdır; şebeke kuran evirici kendi gerilimini ve frekansını üretir, ama enerji ve akım sınırı içinde. Küçük sinyal kararlılığında sistemi doğrusallaştırır, durum matrisinin özdeğerlerine bakarım: gerçek kısım sönümü, sanal kısım frekansı verir. Yerel ve bölgeler arası modların sönüm oranını izlerim."
