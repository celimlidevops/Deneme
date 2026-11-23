# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

Yük akışı topun tepede durduğunu söyler. **Kararlılık**, topa dokununca geri gelip gelmediğini sorar. Üç aile vardır. **Açı kararlılığı**, generatörlerin birbirine göre senkron kalıp kalmadığıdır. **Gerilim kararlılığı**, yük artınca gerilimin toparlanıp toparlanmadığıdır. **Frekans kararlılığı**, üretim-tüketim dengesizliği sonrası frekansın kabul edilebilir yerde kalıp kalmadığıdır.

Küçük bir salınımda sistem doğrusallaştırılır; özdeğerin sönüp sönmediğine bakılır. Buna küçük sinyal denir. Büyük bir arızada (kısa devre, hat açması) bu yetmez; zaman içinde adım adım çözülür. Rotor, atalet yüzünden hemen hız değiştirmez. Arıza sürerken elektriksel güç düşer, mekanik güç devam eder, rotor hızlanır. Arıza **kritik temizleme süresi**nden önce açılmazsa makine senkrondan kopar. Tek makineye indirgenmiş basit resimde bunu alan karşılaştırmasıyla görmek mümkündür; gerçek sistemde süre, zaman tanım bölgesi çalışmasıyla bulunur. Koruma bu süreden önce işini bitirmelidir.

Gerilimde güç-gerilim eğrisinin burnu, daha fazla yükün taşınamadığı noktadır. Buruna yaklaştıkça az bir yük artışı büyük gerilim düşümü yapar. Yük altında kademe değiştirici gerilimi kurtarmaya çalışırken yükü geri çağırır ve çöküşü hızlandırabilir. **PSS** (Power System Stabilizer, güç sistemi kararlı kılıcısı) gerilim regülatörünün üzerine binip salınımı söndürür. Hız regülatörü ise frekans içindir; PSS’nin yerine geçmez.

Frekans kontrolü katmanlıdır. Primer saniyeler, sekonder dakikalar, tersiyer piyasa talimatıdır. Güneş ve rüzgâr döner kütle getirmediği için **atalet** düşer. Frekans daha hızlı değişir; buna **RoCoF** (Rate of Change of Frequency, frekans değişim hızı) denir. Çok düşerse **UFLS** (düşük frekansta yük atma) bilinçli kesinti yapar. **Şebeke izleyen evirici** gerilim ve frekansı dışarıdan alır; referans yoksa şaşırır. **Şebeke kuran evirici** gerilim ve frekansı kendisi üretir, diğerleriyle eğim kuralıyla uzlaşır.

Hangi model: yıllık plan için kaba statik bakış, saniyelik salınım için fazör tabanlı dinamik model, milisaniyelik güç elektroniği için elektromanyetik geçici hal. Kısa olay, daha ayrıntılı ve daha yavaş model ister.

## Mülakatta hızlı tuzak savar notlar

- **Yük akışı kararlılık değildir:** Biri denge noktası, diğeri itilince geri gelme.
- **PSS ve hız regülatörü:** Biri salınımı söndürür, diğeri frekansı tutar.
- **Kademe değiştirici:** Gerilimi düzeltirken gerilim çökmesini kötüleştirebilir.
- **Atalet:** Kurulu güç değil, döner kütle ve şebeke kuran kontrol frekansı yavaşlatır.
- **Model:** Eviricinin iç anahtarlamasını fazör modeli göstermez. Milisaniye sorusu elektromanyetik geçici hal ister.
