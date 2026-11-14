# Dengesiz arıza ve evirici — “bu ne?”

[01](01-Ariza-IEC-Kesici.md) sonrası. Elle sayı yok.

## Simetrik bileşenler (hatırlatma)

Dengesiz üç fazı üç dengeli “hikâyeye” ayırırız:

| Dizi | Basitçe |
| --- | --- |
| Artı | Normal dönen şebeke |
| Eksi | Ters dönen etki |
| Sıfır | Üç faz aynı yönde; toprak/nötr yolu ister |

## Arıza → dizi nasıl bağlanır?

| Arıza | Bağlantı fikri |
| --- | --- |
| Üç faz dengeli | Yalnız artı |
| Tek faz-toprak | Artı + eksi + sıfır **seri** |
| İki faz | Artı ile eksi birlikte (sıfır yok) |
| İki faz-toprak | Üçü birden, biraz farklı düzen |

**Panelde söyle:**  
> Tek faz-toprakta üç dizi seri bağlanır. Sıfır diziyi trafo grubu ve topraklama belirler.

## Trafo grubu / sıfır dizi

Üçgen, sıfır dizi akımını **diğer tarafa geçirmez**.  
Topraklı yıldız yol verir.  
Yazılımda tek faz akımı sıfırsa: çoğu zaman Z0 / nötr / grup yanlış.

(Ayrıntı `02` temeller klasöründe Dyn11 kartında.)

## Evirici (güneş / batarya) katkısı

**Bu ne?**  
Senkron makine büyük kısa süreli akım verebilir.  
Evirici ise **kontrollü ve sınırlıdır**; “klasik makine” gibi modellemek yanlış sonuç verir.

Dağıtımda bu yüzden:

- Röle beklediği akımı görmeyebilir (körlenme),  
- veya yanlış yönde etkilenebilir.

**Panelde söyle:**  
> Evirici katkısını senkron makine gibi şişirmem; standart / üretici sınırına ve kontrolüne bakarım.

## Motor katkısı

Büyük motorlar arızanın ilk anında biraz akım ekler, çabuk söner. İhmal her zaman doğru değildir; endüstriyel şebekede sorulur.

## 90 saniye

> “Dengesiz arızada simetrik bileşen kullanırım; tek faz-toprak üç diziyi seri bağlar. Sıfır dizi trafo ve topraklamaya bağlıdır. Evirici katkısı sınırlı ve kontrollüdür; klasik makine formülü yetmez.”
