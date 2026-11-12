# Kararlılık

## Kararlılık ne demek

Bir çalışma noktası yük akışında vardır. Yük akışı, sistemin "şu an hangi gerilim ve açılarda durduğunu" verir.

Kararlılık başka bir sorudur: sistem itilince o noktanın yakınında veya yeni bir noktada kalabilir mi?

| İttirmenin büyüklüğü | Örnek | Gereken model |
| --- | --- | --- |
| Küçük | Yük artışı, anahtarlama | Doğrusal model yeter |
| Büyük | Kısa devre, hat açma, büyük ünite kaybı | Zaman tanım bölgesi gerekir |

> **Sade anlatım:** Yük akışı topun tepede durduğunu söyler. Kararlılık, topa dokununca geri gelip gelmediğini sorar.

## Üç aile, üç fizik

Kararlılık tek bir konu değildir. Her aile farklı bir dengeyi korur ve farklı sürede bozulur.

| Aile | Denge | Tipik süre | Belirti |
| --- | --- | --- | --- |
| Rotor açısı | Mekanik güç = elektriksel güç | 1–10 s, küçük sinyal daha da izlenir | Açılar ayrılır veya salınır |
| Gerilim | Reaktif denge | 1–10 s kısa, dakikalar uzun | Gerilim çöker, kademe yetişemez |
| Frekans | Sistem güç dengesi | Ani RoCoF, sonra saniyeler ve dakikalar | Frekans 47,5–51,5 penceresine gider |

RoCoF (Rate of Change of Frequency), frekansın değişim hızıdır; birimi Hz/s.

## Açı: salınım denklemi

Rotor açısı kararlılığı, generatör rotorunun şebekeyle eşzamanlı kalıp kalmadığını sorar. Temel denklem, dönen kütle için yazılmış Newton yasasıdır.

```
(2H / ω0) d²δ/dt² = Pm - Pe - D Δω
H saniye, δ elektrik radyan, ω0 senkron hız
```

Terimler:

- `Pm`: türbinden gelen mekanik güç.
- `Pe`: şebekeye verilen elektriksel güç.
- `D Δω`: hız sapmasıyla orantılı sönüm terimi.
- `δ`: rotor açısı.

### Atalet sabiti H

H, nominal güç bazında saniyedir.

- Büyük turbo gruplarda tipik 3–7 s'dir.
- Hidroda daha düşüktür. Atalet küçüktür sanılır ama su kütlesi ayrı değerlendirilir.
- Sistem H'ı, makinelerin H'larının baz güce göre ağırlıklı toplamıdır.
- Evirici takip (grid-following, şebeke izleyen) modunda doğal H katmaz.
- Şebeke oluşturan (grid-forming) kontrol sentetik atalet verebilir. Bu bir kontrol parametresidir, fiziksel volan değildir.

### Tek makine sonsuz bara ve eşit alan

Tek makine sonsuz bara, bir generatörün gerilimi ve frekansı sabit dev bir şebekeye bağlı olduğu basit modeldir. Olaylar şu sırayla gelişir:

1. Arıza sırasında `Pe` düşer, `δ` hızlanır.
2. Arıza temizlenince `Pe`, `Pm`'in üstüne çıkar ve makineyi yavaşlatır.
3. Eşit alan: hızlanma alanı, yavaşlama alanından küçükse açı yakalanır.

Kritik temizleme açısı bu eşitliğin sınırıdır. Süre, açının o değere kaç milisaniyede geldiğidir.

Koruma ne kadar gecikirse geçici hal o kadar zorlaşır. "Röle hızlı olsun" isteğinin kararlılık gerekçesi budur. Ayrıntılı çizim ve elle çözüm `02` dosyasındadır.

### Çok makineli sistem

Çok makineli sistemde eşit alan sezgi olarak kalır. Gerçek hesap şunların diferansiyel denklemlerinin sayısal integralidir:

- makinelerin dinamik modeli,
- AVR (Automatic Voltage Regulator, otomatik gerilim regülatörü),
- hız regülatörü,
- şebeke.

Tipik adım milisaniye, tipik pencere 5–20 s'dir. Çıktı üç soruya cevap verir:

- Rotor açıları birbirinden ayrılıyor mu?
- Gerilim toparlanıyor mu?
- Koruma istenmeyen açma yapar mı?

### Kritik temizleme süresi (CCT)

Kritik temizleme süresi (CCT, Critical Clearing Time), o arıza için kararlılığın döndüğü en uzun kısa devre süresidir.

CCT koruma süresinin altındaysa üç yol vardır:

- Koruma hızlanır.
- Şebeke güçlendirilir: seri kompanzasyon, üretim kaydırma, yeni hat.
- SIPS (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması) eylemi tanımlanır.

## Küçük sinyal

Küçük sinyal analizi, sistemi hafifçe dürtünce salınımın sönüp sönmediğini sorar.

Çalışma noktası etrafında doğrusallaştır: `Δx' = A Δx`. A'nın özdeğerleri λ = σ ± jω.

- σ < 0 sönümlü.
- Sönüm oranı ζ = -σ / √(σ²+ω²). Yüzde 5 altı zayıf sayılır; işletmeciler bölgeler arası modda daha yüksek sönüm ister.
- Frekans f = ω / 2π.

### Mod türleri

| Mod | Frekans | Ne salınır |
| --- | --- | --- |
| Yerel mod | 0,7–2 Hz civarı | Bir santral ile sistemin geri kalanı |
| Bölgeler arası mod | 0,1–0,8 Hz | İki bölge birbirine karşı |
| Kontrol modu | — | AVR veya PSS'ten gelir |

### PSS

PSS (Power System Stabilizer), güç sistemi dengeleyicisidir.

- Yönetmelik, büyük konvansiyonel ünitelerde 0–5 Hz salınımı ve ENTSO-E (Avrupa iletim sistemi işletmecileri ağı) ile gelen bölgeler arası salınımı söndüren PSS ister.
- PSS, hız veya güç sapmasını alıp AVR referansına sönümleyici bir sinyal ekler.
- Kötü ayarlanmış PSS sönümü azaltır.

"PSS koyalım, bitti" deme. Kazanç ve faz kompanzasyonu çalışma noktasına bağlıdır.

## Gerilim

### PV eğrisi

PV eğrisi, bir baradaki aktif güç (P) arttıkça gerilimin (V) nasıl değiştiğini çizer.

- Yükü artırırsın.
- Burun noktasında dV/dP sonsuza gider, Jacobian tekilleşir.
- Alt yarı kararsızdır.

Jacobian, yük akışında kullanılan türev matrisidir; tekilleşmesi çözümün kaybolması demektir.

İşletme burnun üst yarısında, gerilimi yüksek tarafta kalır. Marj, buruna kalan MW veya yüzde yüktür.

### QV eğrisi

QV eğrisi bir barada ne kadar reaktif (Q) enjeksiyonla gerilimin tutulduğunu gösterir. Eğrinin dibi, o baranın reaktif açığıdır.

### Modal analiz

Modal analiz, Jacobian'ın Q–V alt matrisinin küçük özdeğerlerini bulur.

| Kavram | Ne söyler |
| --- | --- |
| Küçük özdeğer | Zayıf mod |
| Sağ özvektör | Hangi baraların o moda girdiği |
| Sol özvektör veya katılım faktörü | Hangi baraya reaktif konursa modun düzeleceği |

"Kapasitörü her yere koyalım" yerine katılım faktörü yüksek baraya koymak planlama cevabıdır.

### Uzun dönem gerilim çökmesi

Çöküş adım adım ilerler:

1. Hat açılır.
2. Gerilim düşer.
3. Motor yükü toparlar.
4. OLTC (On-Load Tap Changer, yük altında kademe değiştirici) gerilimi geri kaldırmaya çalışırken iletimden daha çok reaktif çeker.
5. Şöntler yetmez.
6. Saniyeler-dakikalar içinde çöküş.

Kısa devre simülasyonu 5 saniyede bunu görmez. Yük toparlanması ve kademe modeli gerekir.

Dağıtık üretim volt-var'ı (gerilime göre reaktif güç ayarı) bu sürece yardım veya köstek olabilir.

## Frekans

### RoCoF formülü

Ani açık `ΔP` için, kayıplar ve regülatör henüz yokken frekansın ilk düşme hızı:

```
RoCoF ≈ (ΔP / S_sys) * f0 / (2 H_sys)
```

- `S_sys`: sistemin baz gücü.
- `H_sys`: sistem ataleti.
- `f0`: nominal frekans.

H_sys düşünce aynı ünite kaybı daha dik frekans eğimi verir. RoCoF röleleri jeneratörü veya dağıtık üretimi gereksiz açabilir, olay büyür.

### Türkiye bağlantısı

Düşük atalet, Türkiye'de güneş ve rüzgâr payı arttıkça YTBS'nin "sistem ataleti hesabı" modülünün gerekçesidir. YTBS (Yük Tevzi Bilgi Sistemi), grubun enerji yönetim platformudur (ayrıntısı `01-Kurum-Ilan-ve-Surec` bölümünde).

Atalet hesabı, devredeki senkron makinelerin H ve S değerlerinin envanteridir. Eviricilerin sentetik katkısı ancak kontrol modu biliniyorsa eklenir.

### Kontrol katmanları (yönetmelikle)

| Katman | Ne yapar | Süre / eşik |
| --- | --- | --- |
| **Primer** | Hız regülatörü | Saniyeler, 200 mHz basamakta 30 s tanımı |
| **Sekonder** | AGC (Automatic Generation Control, otomatik üretim kontrolü), MYTM'den (Milli Yük Tevzi Merkezi) set-point. Frekansı 50 Hz'e ve sınır programını hedefine getirir | Normal kontrol bandı 49,8–50,2 Hz |
| **Tersiyer** | Dengeleme piyasası. Sekonder rezervi serbest bırakır | 15 dakika |
| **UFLS** | Under-Frequency Load Shedding: düşük frekans rölesi ile talep kesmesi | TEİAŞ kademeleri her yıl 31 Ekim'e kadar sonraki yıl için belirler |

Primer kontrolün iki ayarı:

- Droop (hız eğimi), yüzde olarak güç değişimini frekans sapmasına bağlar.
- Ölü bant küçük salınımda aşınmayı keser. Ölü bant büyükse primer geç kalır.

UFLS son çaredir. SIPS'in kontrollü yük atmasından daha kördür. TEİAŞ, Türkiye Elektrik İletim A.Ş.'dir.

### LFSM

LFSM (Limited Frequency Sensitive Mode), sınırlı frekans duyarlı moddur.

- LFSM-U (under) 49,8 Hz altında gücü artırır.
- LFSM-O (over) 50,2 Hz üstünde kısar.

Primer hizmet sözleşmesi olan ünite ile sadece LFSM yükümlü ünite aynı şey değildir.

## Hızlı kestirim

Zaman tanım bölgesi kesin ve yavaştır. İşletmede "bu arıza kararlı mı" sorusu dakikalar süremez. Üç aile yaklaşım vardır:

| Yaklaşım | Not |
| --- | --- |
| Enerji fonksiyonu ve eşdeğer tek makine | Model kısıtı çoktur |
| Önceden hesaplanmış CCT veya kararlılık indeksi tablosu | — |
| Öğrenen model | Arıza öncesi gerilim, açı, üretim ve arıza tanımından kararlı/kararsız sınıfı |

Öğrenen modelde iki seçenek:

- Karar ağacı yorumlanabilir olduğu için operatör aracında anlatması kolaydır.
- Yapay sinir ağı daha esnek, gerekçesi daha opaktır.

YTBS'nin yapay zekâ destekli güvenlik ve geçici hal modülü bu üçüncü ailenin ürünleşmiş halidir.

> **Mülakatta şöyle söyle:** Öğrenen model tarama motorudur, şüpheli durumda fizik tabanlı simülasyon doğrular. Kritik altyapıda tek başına kara kutu karar vermez. Eğitim verisi, görülmemiş topolojiyi kapsamaz; model eskimesi (concept drift) yeniden eğitim ister.

## Hangi model

Her soru aynı modeli istemez. Aşağıdaki tablo hangi sorunun hangi araçla yanıtlanacağını eşler.

| Soru | Model |
| --- | --- |
| Limit aşılır mı | AC yük akışı |
| Açı yakalanır mı | RMS dinamik, 5–20 s |
| Salınım sönüyor mu | Özdeğer veya daha uzun simülasyon |
| Gerilim dakikada çöker mi | Kademe + yük toparlanması |
| Frekans bandı | Sistem frekans modeli, atalet envanteri |
| Milisaniye, evirici kontrolü, ferrorezonans | EMT (elektromanyetik geçici). RMS yetmez |

RMS dinamik model, büyüklükleri efektif değer (fazör) olarak izler. EMT ise anlık dalga şeklini çözer.

- EMT her bara için pahalıdır.
- Hibrit: kritik bölge EMT, geri kalan RMS.
- Gerçek zamanlı simülatör (RTDS, Real Time Digital Simulator sınıfı) kontrolörü kapalı çevrim test eder.

Grubun "gerçek zamanlı modelleme" maddesi bu ihtiyaca bağlanır. Her çalışmayı EMT'de koşarım deme.

## 90 saniye

> “Kararlılığı açı, gerilim ve frekans diye ayırırım. Açıda salınım denklemi ve kritik temizleme süresi, küçük sinyalde özdeğer ve PSS. Gerilimde PV burnu ve kademenin reaktif tüketmesi. Frekansta RoCoF ataletle ters gider; primer 30 saniye, sekonder AGC, tersiyer 15 dakika, normal bant 49,8–50,2. Düşük atalette öğrenen model tarar, fizik simülasyonu doğrular. YTBS’nin atalet ve geçici hal modülü bu yüzden işletme aracıdır.”
