# Yük ve trafo — “bu ne?”

[01’deki](01-Guc-Birim-Sistem-Modeller.md) 9 ve 10 numaralı kartlar. Hesap yok.

## Yük “sabit” midir?

Programda “100 MW” yazarız. Gerçek hayatta gerilim düşünce cihazlar farklı tepki verir:

| Tip | Gerilim düşünce ne olur? | Örnek |
| --- | --- | --- |
| Kolay yük | Güç de düşer | Isıtıcı |
| Orta | Biraz düşer | Bazı aydınlatmalar |
| Zor yük | Güç aynı kalsın ister, akım artar | Şarj, sürücü, birçok elektronik |

**Zor yük** gerilim düşükken daha çok akım çekerek durumu kötüleştirebilir. Bu yüzden kararlılık çalışmasında “hangi yük varsayımını yaptım?” demek şarttır.

Üç tipin karışımına pratikte **ZIP** denir. İsmi ezberlemek şart değil; “karışım model” demen yeter.

**Panel cümlesi:** “Sabit güç varsayımı kötümserdir; gerilim düşünce akım artar. Ölçüm yoksa iki uç bakıp farkı söylerim.”

## Trafo plakasındaki Dyn11 ne?

İki harf + bir sayı:

- İlk harf (büyük): yüksek gerilim tarafı nasıl bağlı — **D** = üçgen
- Sonraki harf (küçük): alçak taraf — **y** = yıldız, **n** = nötr dışarıda
- Sayı: iki taraf arasındaki açı kayması (saat dilimi gibi; 11 → 30 derece)

**Dyn11** dağıtım trafolarında çok yaygındır.

Paralel çalışacak iki trafonun aynı “saat grubunda” olması gerekir; değilse aralarında boşuna akım dolaşır.

## Toprak arızasında yol neden önemli?

Bir faz toprağa değince özel bir akım akar. Bu akımın **dönüş yolu** ister: nötr / toprak.

Kural (tek cümle):

> Toprak yolu akımı, topraklı yıldız noktasından akar. Üçgen taraf onu diğer tarafa geçirmez.

Bu yüzden Dyn11’de:

- Ev / alçak tarafta faz-toprak arızası → orada görünür, koruma açabilir.
- Orta gerilim tarafındaki toprak rölesi aynı arızayı **görmeyebilir**.

Bu bir hata değil; bağlantının bilinen etkisidir. Her gerilim seviyesinin koruması kendi içinde düşünülür.

**Yazılımda tek faz akımı sıfır çıkıyorsa:** çoğu zaman “toprak yolu” modelde kapalıdır — yanlış bağlantı grubu, eksik nötr toprağı veya boş veri.

## 90 saniye

> “Yük gerilim düşünce hep aynı davranmaz; sabit güç en zorudur. Dyn11 yüksek taraf üçgen, alçak taraf nötrlü yıldızdır. Toprak arızası yolu yalnız topraklı yıldızdan akar; üçgen diğer tarafa geçirmez.”
