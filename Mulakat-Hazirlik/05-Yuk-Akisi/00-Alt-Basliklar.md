# 05 — Yük akışı

**Yük akışı** = “şu an üretim ve yük böyleyse, her baranın gerilimi ve her hattın akışı ne?” sorusunun cevabı.

Hesap yok, Jacobian yok. Amaç: problemi ve yöntem isimlerini düz cümleyle anlatmak.

## Nasıl kullan

1. [01](01-NR-FDLF-DC-Dagitim.md) — ana kartlar  
2. Takılınca → [02](02-NR-Elle-Jacobian-Q-Limit.md), [03](03-Uc-Faz-Dengesiz-ve-Olasiliksal.md)  
3. [Soruları dene](test.html?sayfa=05-00)

## Sayfalar

| Sayfa | Konu |
| --- | --- |
| [01 Kartlar](01-NR-FDLF-DC-Dagitim.md) | Problem, bara tipleri, yöntemler |
| [02 NR fikri](02-NR-Elle-Jacobian-Q-Limit.md) | Newton-Raphson ne yapar (formülsüz) |
| [03 Dağıtım / belirsizlik](03-Uc-Faz-Dengesiz-ve-Olasiliksal.md) | Üç faz, olasılık — fikir |

## Panelde 8 düz cümle

1. Yük akışı verilen P/Q’dan gerilim ve hat akışını bulur.
2. PQ yük, PV üretim (gerilim tutulan), slack referans + denge.
3. Newton-Raphson iletimde standart çözücüdür.
4. DC yük akışı yalnız aktif güç / açı için kaba elektir; gerilim işi değildir.
5. Iraksayınca önce ada, veri, Q limiti bakılır — çözücü değiştirmek ilk adım değildir.
6. Dağıtımda geri-ileri süpürme veya üç faz model gerekir.
7. Sonuç işletme diline çevrilir: limit aşımı, nerede müdahale.
8. PV bara Q limitine çarpınca PQ’ya düşer; yoksa gerilim sahte düzelir.
