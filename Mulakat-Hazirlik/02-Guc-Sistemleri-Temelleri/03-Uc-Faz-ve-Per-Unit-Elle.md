# Üç faz ve per-unit — “bu ne?”

[01’deki](01-Guc-Birim-Sistem-Modeller.md) 5 ve 6 numaralı kartlar. Hesap yok.

## Neden üç faz?

Tek tel yerine üç tel, aralarında kaymalı üç dalga:

- Aynı malzemeyle daha çok güç taşır.
- Büyük motorlar kendi kendine döner.
- Dengeliyken üç akım birbirini dengeler.

**Dengeli** demek: üç faz benzer yük çekiyor. O zaman bir fazı çözmek yeter; diğerleri kopyadır. Haritada üç teli tek çizgiyle göstermek (**tek hat şeması**) bu yüzdendir.

Dengesiz arıza veya tek fazlı ev yükü olunca bu kolaylık bozulur.

## “400 kV” ne demek?

İki anlam karışmasın:

| Söz | Anlam |
| --- | --- |
| Hat gerilimi | İki faz teli arası — “400 kV” budur |
| Faz gerilimi | Bir faz ile nötr arası — daha küçük |

**Panel cümlesi:** “400 kV hat gerilimidir, iki faz arasıdır.”

## Yıldız ve üçgen (çok kısa)

Trafo sargıları iki türlü bağlanır:

- **Yıldız:** ortada ortak nokta (nötr) olabilir; nötr topraklanabilir.
- **Üçgen:** uç uca kapalı halka; nötr yoktur.

Hangisinin seçildiği, toprak arızasında akımın yolunu değiştirir (ayrıntı [06](06-Yuk-Modelleri-ve-Trafo-Gruplari.md)).

## Per-unit ne işe yarar?

Şebeke bir yandan 400.000 volt, bir yandan 230 volt. Aynı tabloya koyunca insan ve bilgisayar boğulur.

**Per-unit** = “her şeyi kendi normaline böl.”

Sonuç:

- Sağlıklı gerilim hep **1 civarı** görünür.
- 0,95 = biraz düşük, 1,05 = biraz yüksek — hemen anlaşılır.
- Trafo oranı doğru seçilince “kaybolur”; model sadeleşir.

**Benzetme:** Farklı okulların notlarını hep 100 üzerinden yazmak.

**Trafo plakası uyarısı:** Etiketindeki yüzde, o cihazın kendi boyutuna göredir. Büyük sistem hesabına koymadan önce sistemin diline çevirmek gerekir. Çevirmezsen kısa devre sonucu yanlış çıkar.

**Panel cümlesi:** “Per-unit farklı gerilimleri aynı dile getirir; trafo plakasını sistem bazına çevirmeden matrise sokmam.”

## 90 saniye

> “Üç faz daha verimli taşır; dengeliyken bir faz yeter, tek hat şeması budur. 400 kV iki faz arasıdır. Per-unit farklı gerilim dünyalarını aynı ölçeğe getirir; trafo etiketini sistem diline çeviririm.”
