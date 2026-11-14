# 21 — 14 günlük çalışma planı

Bu sayfa, mülakata kadar bütün klasörleri iki haftada bir kez dolaşmanı sağlayan günlük plandır.

## Planı nasıl kullanırsın

Mülakat tarihi belli değilse bu plan iki haftada bir tur atar. Tur bitince baştan başlarsın.

Tarih erkense bazı günleri öne çek. Öne çekilecek günler şunlar:

- 1. gün (kurum ve sistem)
- 4. gün (yük akışı)
- 7. gün (kararlılık)
- 8. gün (durum kestirimi)
- 9. gün (ekonomi, planlama, optimizasyon)
- 20. gün

Not: Plan 14 gündür. Asıl notta “20. gün” yazıyor. Bu büyük olasılıkla 20 numaralı soru bankası klasörünü (13. ve 14. günler) kastediyor.

Her akşam ilgili 90 saniye kutusunu ayakta, sesli söyle. “90 saniye kutusu”, her ders sayfasının sonundaki kısa sözlü anlatım bölümüdür.

> Sade anlatım: Okumak bilmek değildir. Bir konuyu ancak sesli, notsuz anlatabiliyorsan biliyorsun demektir.

## Günlük süre

Günde iki blok yeter:

| Blok | Süre | Ne yaparsın |
| --- | --- | --- |
| Teknik | 70 dakika | Klasörü okur, formülü ve kavramı çalışırsın |
| Sesli anlatım veya kod | 25 dakika | 90 saniye kutusunu söyler ya da örnek kodu çalıştırırsın |

Blok uzadıkça formül ezberi artar, anlatım düşer. Bu yüzden blokları uzatma.

## On dört günün klasör eşlemesi

Tablo her gün için iki şey söyler. “Klasör” sütunu o gün çalışacağın klasör numaralarını verir. “Akşam çıktısı” sütunu akşam elinde olması gereken somut sonucu verir.

Önce plandaki kısaltmaları açalım:

| Kısaltma | Açılımı | Kısa anlamı |
| --- | --- | --- |
| YTBS | Yük Tevzi Bilgi Sistemi | Grubun TEİAŞ için geliştirdiği enerji yönetim platformu |
| SIPS | System Integrity Protection Scheme (Akıllı Koruma Sistemi) | Büyük arızada sistemi otomatik koruyan özel koruma şeması |
| NR | Newton-Raphson | Yük akışını yinelemeli çözen sayısal yöntem |
| DC | Doğru akım (direct current) yaklaşımı | Yük akışının doğrusallaştırılmış, hızlı ama kaba hali |
| N-1 | Bir eleman kaybı ölçütü | Herhangi bir hat veya ünite düşünce sistemin ayakta kalması koşulu |
| ED | Economic Dispatch (ekonomik dağıtım) | Çalışan üniteler arasında yükü en ucuza paylaştırma |
| UC | Unit Commitment (ünite devreye alma) | Hangi ünitenin hangi saatte çalışacağına karar verme |
| OPF | Optimal Power Flow (optimal güç akışı) | Şebeke kısıtlarını da içeren maliyet optimizasyonu |
| SCOPF | Security-Constrained OPF (güvenlik kısıtlı OPF) | N-1 durumlarını da kısıt olarak ekleyen OPF |
| EMS | Energy Management System (enerji yönetim sistemi) | Kontrol merkezindeki ölçüm, kestirim, analiz ve kontrol zinciri |
| STAR | Situation, Task, Action, Result (durum, görev, eylem, sonuç) | Davranışsal sorulara hikâye anlatma kalıbı |

Şimdi günlük plan:

| Gün | Klasör | Akşam çıktısı |
| --- | --- | --- |
| 1 | 01 kurum, YTBS, SIPS, Türkiye sistemi | Üç dakikalık “nereye başvurdum” |
| 2 | 02 temeller — 01 mülakat kartları + 07 yoklama | 12 kartı sesli söyle; test.html?sayfa=02-00 |
| 3 | 03 iletim + 04 dağıtım — 01 kartları | test.html?sayfa=03-00 ve 04-00; farkı 5 cümlede söyle |
| 4 | 05 yük akışı — 01 kartları (formülsüz) | Bara tipleri + DC’nin ne zaman yetmediği; test.html?sayfa=05-00 |
| 5 | 06 kısa devre — 01 kartları | Arıza türleri + kesici/IEC; test.html?sayfa=06-00 |
| 6 | 07 güvenlik | N-1 tarama katmanlarını sırayla çiz |
| 7 | 08 kararlılık | Açı, gerilim, frekans için birer örnek olay |
| 8 | 09 durum kestirimi + `wls_durum_kestirimi.py` | Kötü veriyi artıkla göster |
| 9 | 11 ekonomi, 12 planlama, 13 optimizasyon + `ekonomik_dagitim.py` | ED, UC, OPF, SCOPF’i dört cümlede ayır |
| 10 | 14 ve 15 programlama ve araçlar | Kullandığın aracı dürüstçe, kullanmadığını iddiasız anlat |
| 11 | 16 mimari, 17 yenilenebilir | EMS zincirini kutularla çiz |
| 12 | 18 veri ve yapay zekâ, 19 davranışsal | İki STAR hikâyesi yaz |
| 13 | 20 soru bankası, yarısını sesli | Takıldığın soruyu klasöre geri götür |
| 14 | 20 kalan yarısı, formül kartı, İngilizce üç cevap | Kendini tanıt, 3 dakika, notsuz |

Tablodaki birkaç ifadenin anlamı:

- **Tek faz-toprak eşdeğeri:** Bir fazın toprağa kısa devre olduğu arızada pozitif, negatif ve sıfır bileşen devrelerinin nasıl bağlandığını gösteren çizim.
- **DC’nin kör noktası:** DC yük akışının gerilim genliğini ve reaktif gücü hesaba katmaması.
- **Azami ve asgari hesap:** Kısa devre akımının en büyük (cihaz seçimi için) ve en küçük (korumanın algılaması için) değerini ayrı hesaplamak.
- **Artık:** Ölçülen değer ile kestirilen değer arasındaki fark. Kötü veri, artığı büyük çıkan ölçümdür.
- **WLS:** `wls_durum_kestirimi.py` adındaki WLS, Weighted Least Squares (ağırlıklı en küçük kareler) yöntemidir.

Örnek Python dosyaları [14-Programlama/ornekler](../14-Programlama/ornekler/) klasöründedir:

| Gün | Dosya |
| --- | --- |
| 4 | [dc_yuk_akisi.py](../14-Programlama/ornekler/dc_yuk_akisi.py) |
| 8 | [wls_durum_kestirimi.py](../14-Programlama/ornekler/wls_durum_kestirimi.py) |
| 9 | [ekonomik_dagitim.py](../14-Programlama/ornekler/ekonomik_dagitim.py) |

Klasörlerin içindekiler sayfaları:

| No | Klasör |
| --- | --- |
| 01 | [Kurum, ilan ve süreç](../01-Kurum-Ilan-ve-Surec/00-Alt-Basliklar.md) |
| 02 | [Güç sistemleri temelleri](../02-Guc-Sistemleri-Temelleri/00-Alt-Basliklar.md) |
| 03 | [İletim şebekeleri](../03-Iletim-Sebekeleri/00-Alt-Basliklar.md) |
| 04 | [Dağıtım sistemleri](../04-Dagitim-Sistemleri/00-Alt-Basliklar.md) |
| 05 | [Yük akışı](../05-Yuk-Akisi/00-Alt-Basliklar.md) |
| 06 | [Kısa devre](../06-Kisa-Devre/00-Alt-Basliklar.md) |
| 07 | [Güvenlik analizi](../07-Guvenlik-Analizi/00-Alt-Basliklar.md) |
| 08 | [Kararlılık](../08-Kararlilik/00-Alt-Basliklar.md) |
| 09 | [Durum kestirimi](../09-Durum-Kestirimi/00-Alt-Basliklar.md) |
| 10 | [Koruma ve topraklama](../10-Koruma-ve-Topraklama/00-Alt-Basliklar.md) |
| 11 | [Ekonomik işletme](../11-Ekonomik-Isletme/00-Alt-Basliklar.md) |
| 12 | [Planlama](../12-Planlama/00-Alt-Basliklar.md) |
| 13 | [Optimizasyon](../13-Optimizasyon/00-Alt-Basliklar.md) |
| 14 | [Programlama](../14-Programlama/00-Alt-Basliklar.md) |
| 15 | [Analiz yazılımları](../15-Analiz-Yazilimlari/00-Alt-Basliklar.md) |
| 16 | [Yazılım mimarisi](../16-Yazilim-Mimarisi/00-Alt-Basliklar.md) |
| 17 | [Yenilenebilir ve akıllı şebeke](../17-Yenilenebilir-ve-Akilli-Sebeke/00-Alt-Basliklar.md) |
| 18 | [Veri ve yapay zekâ](../18-Veri-ve-Yapay-Zeka/00-Alt-Basliklar.md) |
| 19 | [Davranışsal](../19-Davranissal/00-Alt-Basliklar.md) |
| 20 | [Soru bankası](../20-Soru-Bankasi/00-Alt-Basliklar.md) |

## Her günün aynı kapanışı

Her günü aynı şekilde bitir. Dört satır yaz ve hepsini tek bir dosyaya ekle. Böylece iki hafta sonunda kendi zayıf noktalarının listesi oluşur.

- Bugün tahtada türevini yapabildiğim formül
- Hâlâ karıştırdığım iki terim
- Kendi işimden bağlayabildiğim bir örnek
- Yarın ilk bakacağım sayfa

## Karıştırılan kavram çiftleri

Bu ilanda karıştırılan çiftler şunlar olur:

| No | Birinci kavram | İkinci kavram |
| --- | --- | --- |
| 1 | Güvenlik | Kararlılık |
| 2 | Ekonomik dağıtım | OPF |
| 3 | Kestirim | Yük akışı |
| 4 | SIPS | Röle |
| 5 | Kurulu güç | Puant |
| 6 | Takip eden evirici | Şebeke oluşturan evirici |
| 7 | Önleyici kontrol | Düzeltici kontrol |

Terimlerin kısa anlamı:

- **Puant:** Sistemin belli bir dönemde gördüğü en yüksek tüketim (yük).
- **Kurulu güç:** Sistemdeki santrallerin toplam etiket gücü.
- **Takip eden evirici (grid-following):** Şebekenin gerilim ve frekansını izleyip ona göre akım basan evirici.
- **Şebeke oluşturan evirici (grid-forming):** Gerilim ve frekansı kendisi kuran evirici.
- **Önleyici kontrol:** Arıza olmadan önce işletme noktasını değiştirmek.
- **Düzeltici kontrol:** Arıza olduktan sonra müdahale etmek.

Bu çiftleri 14. gün yan yana söyleyemiyorsan o klasörü tekrar aç.

## Mülakattan bir gün önce

Bu gün için kurallar:

1. Yeni konu açma.
2. Formül kartını bir kez oku.
3. Kendi üç STAR hikâyeni ve üç sorunu yaz. “Üç soru”, mülakatın sonunda kurula soracağın sorulardır.
4. Rakamların tarihini kontrol et. Kurulu güç ayda değişir. Karttaki aydan yenisini ezberleme.
5. Gerçek bara adı ve müşteri verisi yok. Örneklerde bunları kullanma.

> Sade anlatım: Uyku, karttan daha çok puan getirir.
