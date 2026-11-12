# Yazılım, davranışsal sorular ve formül kartı

Bu sayfada dört parça var:

1. Yazılım soruları ve kısa cevapları.
2. Davranışsal sorular (kişilik, deneyim, motivasyon) ve cevap iskeletleri.
3. Panele senin sorabileceğin sorular.
4. Formül kartı, rakam kartı ve birim refleks listesi: mülakattan hemen önce göz gezdirmek için.

## Yazılım soruları

**Python’da büyük Ybus neden yavaşlar?**

Ybus (bara admitans matrisi), şebekedeki baraların birbirine bağlantısını tutan matristir. Çoğu elemanı sıfırdır; buna seyrek matris denir.

Yavaşlığın nedeni yoğun matris kurulmasıdır. Yoğun matris, sıfırları da tek tek bellekte tutar. On bin barada yoğun Ybus gigabayt bellek, yoğun LU (alt-üst üçgen çarpanlara ayırma) ise dakikalar demektir.

Çözüm:

- `scipy.sparse` ile matrisi seyrek tutarım.
- Profilde (kodun hangi kısmının ne kadar sürdüğünü ölçerek) asıl sürenin çözücüde mi, Python döngüsünde mi olduğuna bakarım.

**Yük akışı servisi ıraksarsa API ne döner?**

API (Application Programming Interface, uygulama programlama arayüzü), başka programların servisi çağırdığı arayüzdür.

Boş 200 (HTTP "başarılı" kodu) ve sessiz liste dönmem. Şunları döndürürüm:

- Kalite bayrağı.
- Neden: ada, iterasyon veya limit.
- Son iterasyonun artığı.

Çağıran N-1 modülü, o bayrakla gelen sonucu operatöre “kesin” diye basmaz.

**REST ile SOAP?**

İkisi de servisler arası haberleşme biçimidir:

| Yer | Tercih |
| --- | --- |
| Yeni modüller arasında | REST (Representational State Transfer) ve JSON (JavaScript Object Notation, metin tabanlı veri biçimi) |
| Eski EMS (Energy Management System, enerji yönetim sistemi) entegrasyonunda | SOAP (Simple Object Access Protocol) ve WSDL (Web Services Description Language, servisin tanım dosyası) |

YTBS’nin (Yük Tevzi Bilgi Sistemi) SCADA (Supervisory Control and Data Acquisition, uzaktan izleme ve veri toplama) tarafı web servistir.

Ağır hesap, istek zaman aşımında değil, kuyrukta koşar. Yani uzun süren hesap, isteği bekletmeden ayrı bir iş kuyruğuna verilir.

**Java’da paralel N-1 neden bozulur?**

İş parçacıkları (thread'ler) aynı vaka nesnesini değiştirirse yarış (race condition) olur: sonuç, hangi iş parçacığının önce yazdığına bağlı hale gelir.

Çözüm:

- Her işe kopya veya değişmez (immutable) girdi veririm.
- Sonuçlar ihlal tablosuna kimlikleriyle yazılır.

**Test setin nedir?**

Test setim şu vakalardan oluşur:

1. Elde çözülmüş üç bara.
2. Bilinen bir N-1 ihlali.
3. Bilinen bir kötü ölçüm.
4. Bilerek ıraksayan vaka.
5. Boş veri.

Altın değer (doğru olduğu bilinen beklenen sonuç) dosyada kilitlidir.

Ulusal modeli teste ham koyamam; sentetik veya maskelenmiş vaka kullanırım.

**MATLAB prototipi nasıl ürüne iner?**

Sıra şöyledir:

1. Denklem ve kazanç doğrulanır.
2. Birim ve işaret sözleşmesi yazılır.
3. Python veya Java’da aynı üç barada aynı sayı üretilir.
4. Ancak ondan sonra servise girer.

Simulink diyagramı sunucuya gömülmez.

**Modeli Git’e koyar mısın?**

Git, kod sürüm kontrol aracıdır.

| Git'e girer | Git'e girmez |
| --- | --- |
| Kod | Gizli şebeke, parola, ticari üretim ve müşteri verisi |

Büyük vaka için sürüm notu ve erişim kuralı tutulur. Model sürümü, algoritma sürümü ve limit sürümü ayrıdır.

## Davranışsal sorular

**Kendini tanıt.**

[`19` dosyasındaki](../19-Davranissal/00-Alt-Basliklar.md) iskeleti kullan. İskeletin soruları:

- Üç yılda hangi şebeke, hangi analiz, hangi araç?
- Hangi karar değişti?
- Yazılımda ne tekrarlanabilir oldu?
- MAM’daki (TÜBİTAK Marmara Araştırma Merkezi) hangi halkaya bağlanıyor?

**Zor bir analiz hatası.**

STAR kalıbıyla anlat: Situation (durum), Task (görev), Action (eylem), Result (sonuç).

Örnek iskelet:

1. Sonuç beklenenden uzaktı.
2. Baz veya işaret hipotezi kurdum.
3. İki araçta aynı barayı karşılaştırdım.
4. Kademe sargısının ters girildiğini buldum.
5. Modeli kilitledim.
6. Raporu düzelttim.

Kendi hikâyen yoksa bu örneği kendi hayatın gibi anlatma.

**Yetişmeyen teslim.**

Kapsamı önden kestim: önce güvenlik için zorunlu senaryo, sonra duyarlılık.

Bunu tek başıma sessizce yapmadım; hangi senaryonun ertelendiğini yazdım. Kaliteyi “idare eder” diye düşürmedim.

**Bilmediğin bir araç.**

Öğrenme döngüm:

1. Küçük resmi örnek.
2. Elde doğrulama.
3. Sonra gerçek vaka.
4. Fark varsa baz ve işarete bakma.

Öğrendiğin son aracı bu döngüyle anlat.

**Ekipte anlaşmazlık.**

Koruma süresi ile kararlılık CCT’si (Critical Clearing Time, kritik temizleme süresi) çatışırsa, sayıyı aynı vakada yan yana koyarım.

Karar, kimin sesi yüksekse değil, hangi limitin yönetmelikte bağlayıcı olduğuna göre verilir.

**Neden MAM, neden bu grup?**

Ülke iletiminin işletme yazılımı burada üretilmiş; YTBS ve SIPS (System Integrity Protection Scheme, sistem bütünlüğü koruma şeması) sahada.

Ben analiz ile kodun birleştiği yerde çalışıyorum. Danışmanlık dosyası değil, tekrar koşulan araç istiyorum.

**Lisansüstü?**

Cevabın dört parçası:

1. Bir cümlelik problem.
2. Neden Türkiye sisteminde büyüyor.
3. Hangi modüle değer.
4. Senin tecrüben nasıl bağlanıyor.

Yapmayacaksan söyleme. Motivasyon, ilanda “yapmış olmak” ile eşdeğer kabul edilir; sahte kayıt kabul edilmez.

**Online envanter?**

Online envanter, süreçteki çevrimiçi kişilik değerlendirmesidir (ayrıntısı: [Envanter ve online değerlendirme](../01-Kurum-Ilan-ve-Surec/05-Envanter-ve-Online-Degerlendirme.md)).

- Tutarlı işaretle.
- Her maddeye “her zaman” deme.
- Araştırmacı profili: analitik, planlı, öğrenmeye açık.
- Kahraman yönetici profili bu kadroyla çelişir.

## Panele sor

Mülakat sonunda "sizin sorunuz var mı?" denirse sorabileceğin üç soru:

- İşe başlayan araştırmacı ilk yıl hangi halkada duruyor: model, kestirim, güvenlik, tahmin, optimizasyon?
- İletim işletmesi ile dağıtım veya planlama işinin önümüzdeki yıldaki ağırlığı nedir?
- Lisansüstü ve proje teslimi takvimde nasıl ayrılıyor?

## Formül kartı

Aşağıdaki kod bloğu, notlardaki temel formüllerin tek yerde toplanmış halidir. Satır grupları sırasıyla şunlardır:

| Grup | Ne anlatır |
| --- | --- |
| `S`, `Z_pu`, `Z_yeni` | Kompleks güç, per-unit (birim değer) dönüşümü ve baz değiştirme |
| `P`, `ΔV` | İki bara arası aktif güç aktarımı ve dağıtımda gerilim düşümü |
| `I_3faz`, `I_faz-toprak` | Üç faz ve tek faz-toprak kısa devre akımı |
| `NR`, `DC` | Newton-Raphson yük akışı adımı ve DC yük akışı |
| `J`, `G`, `r_N,i` | Durum kestirimi: WLS (ağırlıklı en küçük kareler) amacı, kazanç matrisi, normalize artık |
| Salınım denklemi, `RoCoF` | Rotor açısı dinamiği ve frekans değişim hızı (Rate of Change of Frequency) |
| `dC_i/dP_i = λ` | Ekonomik dağıtım: kayıpsız ve kayıplı eşit artan maliyet koşulu |
| `ζ` | Bir salınım modunun sönüm oranı (σ özdeğerin gerçek kısmı, ω sanal kısmı) |

```
S = P + jQ
Z_pu = Z_ohm * S_baz / V_baz²
Z_yeni = Z_eski * (S_yeni/S_eski) * (V_eski/V_yeni)²

P = (Vs Vr / X) sin δ
ΔV ≈ (P R + Q X) / V

I_3faz = V / Z1
I_faz-toprak = 3 V / (Z1 + Z2 + Z0 + 3 Zf)

NR:  [ΔP; ΔQ] = [H N; M L] [Δθ; ΔV/V]
DC:  P = B θ ,  B_ik = -1/x_ik

J = (z - h)ᵀ W (z - h) ,  W = R⁻¹
G = Hᵀ W H
r_N,i = |r_i| / sqrt(Ω_ii)

(2H/ω0) d²δ/dt² = Pm - Pe
RoCoF ≈ (ΔP / S_sys) * f0 / (2 H_sys)

dC_i/dP_i = λ          kayıpsız
(dC_i/dP_i) / (1 - ∂Pkayıp/∂P_i) = λ

ζ = -σ / sqrt(σ² + ω²)
```

## Rakam kartı (tarihiyle söyle)

Bu rakamları söylerken yanındaki tarihi de söyle; rakamlar zamanla değişir.

| Konu | Değer |
| --- | --- |
| Kurulu güç, 2025 sonu | 122.518,6 MW |
| Ani puant (en yüksek anlık yük), 2025 | 60.414 MW |
| Kurulu güç, Eylül 2026 sonu | 127.355,2 MW |
| Hat uzunluğu, Ekim 2026 sonu | 77.863 km |
| Frekans hedef bandı | 49,8–50,2 Hz |
| Uç tasarım frekansları | 47,5 ve 51,5 Hz |
| Primer frekans kontrolü tanımı | 200 mHz, 30 s |
| Tersiyer kontrol | 15 dk |
| PSS (Power System Stabilizer, güç sistemi dengeleyicisi) şartı | 75 MW ve üzeri ünite veya 300 MW ve üzeri konvansiyonel santral, 0–5 Hz |
| Planlama | Puant + %5, N-1, nükleer bağlantıda N-2 |
| Mülakat | Baraj 70. Kontenjan 3. Çağrı yaklaşık 10 kat |

## Birim refleks listesi

Hesapta en sık yapılan birim hataları ve doğru alışkanlık:

| Büyüklük | Kural |
| --- | --- |
| Açı | Denklemde radyan, ekranda derece |
| Güç | Ya hep pu ya hep MW |
| Gerilim | pu ile kV aynı tabloda toplanmaz |
| Zaman | Milisaniye ile saniye karışmaz; RoCoF birimi Hz/s |
| Atalet H | Birimi saniye; sistem bazı ile makine bazı karışmaz |
