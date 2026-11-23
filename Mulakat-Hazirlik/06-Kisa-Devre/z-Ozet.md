# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

**Kısa devre**, tellerin istemeden birbirine veya toprağa değmesidir. Akım bir anda çok büyür. Bu hesap “şebeke çöker mi” diye değil, kesici bu akımı kesebilir mi, bara ve hat dayanır mı, röle görür mü diye yapılır. Yaygın kural kitabı **IEC 60909**’dur. Amaç gerçek bir anın filmini çekmek değil, ekipman seçimi için standart ve tekrarlanabilir bir akım bulmaktır.

En sık arıza bir fazın toprağa değmesidir. En büyük akım her zaman üç faz kısa devre değildir; toprak yolu ve şebeke kuvvetine göre tek faz toprağa daha büyük olabilir. Bunu söylemek için topraklama ve trafo bağlantısı gerekir.

Senkron generatör ilk anda, iç manyetik alanı henüz çökmeden, çok büyük akım verir. Sonra akım azalır ve sürekli değere oturur. Kesici hem ilk tepeyi taşıyacak hem azalan akımı doğru anda kesecek şekilde seçilir. Kaynağa yakın arıza ile uzak arıza aynı değildir: yakın arızada makine akımı belirgindir, uzak arızada şebeke daha “düz” görünür.

**Evirici** (güneş ve rüzgârın şebeke arayüzü) senkron makine gibi akımı büyütmez. Kontrol yazılımı akımı kabaca anma değerinin biraz üstünde tutar. Bu yüzden klasik “arıza olursa akım on katına çıkar” cümlesi eviricili şebekede yanlıştır. Koruma bu küçük akımı göremeyebilir. Ayrıca eviricinin arıza sırasındaki davranışı moda bağlıdır; tek bir kısa devre koşusu yetmez.

Dengesiz arızada sistem simetrik bileşenlere ayrılır: doğru, ters ve sıfır dizi. Sıfır dizi, toprak yoludur. Trafo yıldız noktası toprağa bağlı değilse sıfır dizi geçmez ve toprak arıza akımı değişir.

## Mülakatta hızlı tuzak savar notlar

- **Amaç:** Kısa devre hesabı koruma ve kesici içindir. Yük akışının yerine geçmez.
- **En büyük akım:** Her zaman üç faz değildir. Topraklama ve trafo grubunu söylemeden “en büyüğü budur” deme.
- **Makine:** İlk an büyük, sonra küçük. Tek sayı hem tepeyi hem sürekli akımı anlatmaz.
- **Evirici:** Akımı sınırlar ve kontrol eder. Klasik eşik arızayı görmeyebilir; kontrol modu da söylenir.
- **Standart:** IEC seçim içindir. Elektromanyetik geçici hal incelemesi ise dalga şeklinin kendisini görmek içindir. İkisi aynı iş değildir.
