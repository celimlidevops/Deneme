# Güç ve fazör — “bu ne?”

[01’deki](01-Guc-Birim-Sistem-Modeller.md) 1, 3 ve 4 numaralı kartların açılmış hali. Hesap yok.

## Elektrik ne taşır?

Düşün: bir boru hattı.

| İsim | Ne işe yarar | Günlük benzetme |
| --- | --- | --- |
| Aktif güç P | Gerçek iş | Musluktan akan, işe yarayan su |
| Reaktif güç Q | Motor/trafo için gerekli “destek” | Boruyu doldurup boşaltan, ama evde kullanılmayan su |
| Görünür güç S | İkisinin birlikte hattı ne kadar doldurduğu | Borunun toplam doluluk hali |

Q iş yapmaz diye “önemsiz” değildir. Hattı doldurur → hat ve trafo daha çabuk dolmuş sayılır → ısınır, gerilim düşer.

**Panel cümlesi:** “Aktif iş yapar; reaktif hattı doldurur; cihaz S’ye göre seçilir.”

## Neden yüksek gerilim?

Aynı gücü yüksek gerilimle taşı → akım küçülür → tel daha az ısınır.

Bu yüzden şehirler arası hatlar çok yüksek gerilimdedir. Şehre gelince trafo düşürür.

## Fazör ne demek?

Elektrik düz bir çizgi değil; sürekli salınan bir dalga (saniyede 50 kez).

Her dalgayı iki kelimeyle anlatırız:

1. Ne kadar güçlü? (büyüklük)
2. Diğerine göre önde mi geride mi? (açı)

Bu ikiliye **fazör** denir. Yazılımda karmaşık sayı gibi tutulur; sen mülakatta “büyüklük ve açı” demen yeter.

Açı için bir başlangıç noktası seçilir (slack barası = 0). Haritada “kuzeyi sıfır alıyorum” demek gibi.

**Ne zaman yetmez?** Arıza olur olmaz ilk milisaniyelerde. Orada daha ince zaman modeli gerekir; “fazör yetmez” demen yeter.

## Üç küçük eleman (isim bilmen yeter)

| Eleman | Ne yapar | Şebekede nerede |
| --- | --- | --- |
| Direnç | Isı / kayıp | Telin kendisi |
| Bobin | Akımı geciktirir | Hat, trafo, motor |
| Kondansatör | Akımı öne çeker | Kompanzasyon, kablo |

İletim hatlarında bobin etkisi genelde dirençten büyüktür. Ev seviyesinde direnç daha görünür hale gelir.

## 90 saniye

> “Şebeke salınan bir dalgadır; büyüklük ve açı ile anlatırım, buna fazör derim. Aktif güç iş yapar, reaktif güç hattı doldurur ama iş yapmaz. Yüksek gerilim kaybı azaltmak içindir.”
