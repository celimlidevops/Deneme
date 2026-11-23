# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

**İletim**, elektriği santralden şehrin girişine taşıyan büyük yoldur. **Dağıtım** mahalle sokağıdır. Türkiye’de bu büyük yollar esas olarak 400 kV ve 154 kV’dur. İletimde bir baraya çoğu zaman birden çok yoldan gidilir; ağ örgülüdür. Bu yüzden bir hat açılınca akım komşu hatlara dağılır. Dağıtımda ise çoğu zaman tek yol vardır; o yol açılınca arkası kararır.

Planlamanın omurgası **N-1**’dir: tek bir eleman devre dışıyken kullanıcı kaybı ve ada oluşmamalı, gerilim ve hat sınırları içinde kalınmalıdır. Aynı direği paylaşan iki hat iki ayrı şanssızlık değildir; direk düşünce ikisi birden gider, buna ortak mod denir.

Akışın nereye gideceğini kabaca **PTDF** (Power Transfer Distribution Factor, güç aktarım dağılım katsayısı) söyler: bir baradan diğerine eklenen gücün hangi hatta yüzde kaç düşeceği. Bir hat açılınca kalan hatlara binen ek yükü **LODF** (Line Outage Distribution Factor, hat devre dışı dağılım katsayısı) söyler. İki ülke veya iki bölge arasında fiilen taşınabilecek tavan **NTC** (Net Transfer Capacity, net aktarım kapasitesi), bunun o an kullanılmayan kısmı **ATC** (Available Transfer Capacity, kullanılabilir aktarım kapasitesi) olur. Katsayı hızlı tarama içindir; sınırda kalan vakayı tam yük akışı doğrular.

Gerilim ve akış her zaman yeni hatla düzelmez. **FACTS** (esnek alternatif akım iletim cihazları) ve özellikle **STATCOM** (statik senkron kompanzatör) reaktif gücü hızlı basıp çekerek gerilimi tutar. Enterkonneksiyonda senkron hat frekansı paylaşır; doğru akım bağlantısı gücü ayarlar, frekansı geçirmez.

## Mülakatta hızlı tuzak savar notlar

- **İletim ve dağıtım:** Biri örgülü otoyol, diğeri çoğunlukla tek sokaktır. Aynı koruma ve aynı akış mantığı ikisine uymaz.
- **N-1:** “Yedek var” demek yetmez. Açıklama sonrası gerilim, ısınma ve ada kontrol edilir.
- **PTDF ve LODF:** Biri ek gücün dağılımı, diğeri hat açılınca kalan hatlara binen paydır.
- **NTC ve ATC:** Biri tavan, diğeri o an boş kalan paydır.
- **FACTS:** Her sorunun cevabı yeni hat değildir. Gerilim bazen hızlı reaktif cihazla tutulur.
