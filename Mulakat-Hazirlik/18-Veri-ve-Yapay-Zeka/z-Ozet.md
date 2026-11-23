# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

Tahmin, ufka göre başka kararı besler. Saniyeler ve dakikalar dengelemeyi, saatler gün içi piyasayı, günler ünite tahsisini, yıllar planlamayı ilgilendirir. Yükü takvim, hava ve özel gün belirler. Rüzgâr ve güneşte önce hava, sonra santralin güç eğrisi gelir. Tek santralin hatası bölge toplamından büyüktür; hatalar birbirini bir ölçüde götürür.

Sistem işletmecisinin gördüğü şey brüt yük değil **net yüktür**: tüketim eksi yenilenebilir üretim. Güneş akşam çekilince net yük hızla yükselir. Bu rampayı ortalama hatadan ayrı izle.

Hata ölçütü yedek boyutunu besler. Ortalama mutlak hata tipik sapmayı, büyük sapmalara daha çok kızan ölçüt kuyruğu anlatır. Yüzde hata, küçük bazda şişer; onu tek skor diye kullanma. Hata bandı kadar yedek tutulmazsa dengeleme yetişmez. Fazla yedek de para yakar.

Öğrenen model güvenlik taramasında eleme yapabilir: binlerce arızadan şüphelileri öne alır. Karar, limit aşımı ve kararlılık için fizik motoruna kalır. Model “kararlı” der, fizik demezse fizik yazılır. Açıklamasız öneriyi operatör uygulamaz. Gerekçe, hangi özelliğin sonucu çektiği ve hangi koşulda güvenilmeyeceği şeklinde söylenir.

Zaman serisinde veriyi rastgele karıştırma. Yarının havasını bugünün eğitimine sızdırmak, testi şişirir. Buna **zaman sızıntısı** denir. Eğitim, doğrulama ve test zamana göre ayrılır. Yeni hat, yeni santral veya yeni tüketim alışkanlığı modeli eskidir. Performans izlenir, eşik düşünce model yenilenir. Başarısız olursa son geçerli fizik hesabı veya son iyi tahmin, zaman damgasıyla ekranda kalır. Sessizce eski sayı “taze” gösterilmez.

Fizik ile öğrenen model arasında seçim, verinin boyuna ve kararın kritikliğine bağlıdır. Az veri ve can güvenliği varsa fizik. Çok veri ve eleme hızı varsa öğrenen model, arkada fizik doğrulamasıyla.

## Mülakatta hızlı tuzak savar notlar

- **Net yük:** Tüketim eksi yenilenebilir. Rampa, günlük ortalama hatadan ayrı bir olaydır.
- **Öğrenen model karar vermez:** Eleme ve öneri yapar. Limit ve kararlılık fizikte kalır.
- **Zaman sızıntısı:** Geleceği eğitimin içine karıştırma. Bölme zamana göredir.
- **Operatör:** Gerekçesiz skoru uygulamaz. Ne zaman güvenilmeyeceğini de söyle.
- **Eskime ve çökme:** Model bozulunca veya servis düşünce eski sayıyı yeni diye sunma.
