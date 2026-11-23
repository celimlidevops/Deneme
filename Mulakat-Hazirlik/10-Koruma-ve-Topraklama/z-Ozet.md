# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

**Koruma**, arızayı önlemez. Kısa devre veya arıza anında şebekenin yalnızca arızalı kısmını, mümkün olan en kısa sürede ve doğru yerden ayırarak hasarı ve sistem kararsızlığını önler. Dört ölçütle değerlendirilir. **Seçicilik**, yalnız arızalı elemanı ayırmaktır. **Hız**, kritik temizleme süresinden önce açarak ekipmanı ve senkronizmayı korumaktır. **Duyarlılık**, en küçük makul arızayı bile görebilmektir. **Güvenilirlik**, gerektiğinde açmak ile gereksiz açmamak arasındaki dengedir. Çok hassas röle yanlış açar.

**Yedek koruma**, asıl koruma aksayınca devreye girer. Önce asıl korumaya fırsat tanımak için daha yavaş, asıl bölgeyi de kapsamak için daha geniş olur. Kesici açma emri aldığı halde akımı kesemezse, kesici arıza koruması komşu kesicileri açar. Röle şebekeyi doğrudan değil, akım ve gerilim trafoları üzerinden görür. Trafo doyunca röle yanılabilir.

Dağıtımda öne çıkan araç **aşırı akım** rölesidir. Ayarlanan eşik aşılınca sabit zamanlı veya ters zamanlı eğriye göre açar. Ters zaman, akım büyüdükçe hızlanır ve sigortayla koordinasyonu kolaylaştırır. Halka ve çift beslemede akımın yönüne de bakılır. **OTK** (otomatik tekrar kapama), geçici arızada ölü zaman sonrası hattı yeniden enerjilendirir. Dağıtık üretim varsa, tekrar kapamadan önce adanın söndürülmesi gerekir; yoksa iki kaynak birbirine rastgele bağlanır.

**Koordinasyon**, arka arkaya dizilen rölelerin sıralı açmasıdır. Arkadaki röle, öndekine **CTI** (koordinasyon zaman aralığı) kadar gecikme payı bırakır. Asıl ve yedek röle eğrileri, en büyük arıza akımında bile çakışmamalıdır. Çakışırsa ikisi birden veya yanlış olan önce açar.

İletimde **mesafe koruması** kullanılır. Gerilimin akıma oranı empedansı verir; hat empedansı boyla orantılı olduğu için arıza uzaklığı kestirilir. TEİAŞ ayar standartlarında birinci bölge yaklaşık yüzde seksen ve gecikmesizdir. Yüzde yüz yapılırsa ölçü ve model hatası, komşu hattaki arızayı da içine alır ve gereksiz açma olur. İkinci ve üçüncü bölgeler daha geniş ve kademeli gecikmelidir. **Ara besleme**, başka kaynaktan araya giren akımın empedansı olduğundan büyük göstermesidir; röle arızaya yetişemez. **Yük taşması**, ağır yükün empedansının üçüncü bölgeye girip yanlış açmaya yol açmasıdır. Güç salınımı da empedansı bölge içinde dolaştırabilir; salınım bloğu kararlı salınımda açmayı tutar, gerçek arızada bırakır.

Kritik elemanlarda **diferansiyel koruma** kullanılır. Bir bölgeye giren ve çıkan akımın farkına bakar. İç arızada fark büyür, dış arızada fark sıfır kalmalıdır. Trafo devreye girerken mıknatıslanma akımı fark gibi görünür; ikinci harmonik tutması bunu yanlış açmadan ayırır. Dış arızada ölçü trafosu doyunca sahte fark oluşmasın diye tutma eğrisi kullanılır. Hattın iki ucu haberleşirse bütün hat gecikmesiz korunabilir.

Sistem genelinde **SIPS** (sistem bütünlüğü koruma şeması) devreye girer. Röle tek ekipmanı korur. SIPS, yerel olarak doğru açmaların sistemi bölmesini engellemek için kontrollü kayıp verir.

**Evirici**, güneş ve rüzgârı şebekeye bağlayan güç elektroniği arayüzüdür. Arıza akımını senkron generatör gibi büyütmez, kontrol yazılımıyla sınırlar. Aşırı akım eşiği arızayı hiç göremeyebilir. Mesafe rölesi de zayıf ve kontrol güdümlü akımda şaşırır. Haberleşmeli veya diferansiyel koruma ve **EMT** (elektromanyetik geçici hal) incelemesi önem kazanır. Yalnızca tek bir kısa devre koşusu yetmez; kontrol modları da görülmelidir.

**Topraklama**, nötrün bağlanma biçimi ve trafo merkezi topraklama ağıdır. Sıfır dizi akımını ve can güvenliğini belirler. Doğrudan, direnç üzerinden, rezonans veya izole nötr, toprak arıza akımının büyüklüğünü değiştirir; koruma ayarı da bununla değişir. **Adım gerilimi** iki ayak arası, **dokunma gerilimi** el ile ayak arasıdır. İkisi de **IEEE 80** kapsamında arıza temizleme süresine göre denetlenir. Koruma süresi uzadıkça izin verilen dokunma gerilimi sınırı sıkılaşır.

Hesap veya kestirim yakınsamazsa, ya da kritik bir durum varsa, eski veriyi yeniymiş gibi sunma. Sebebi ve etkilenen uygulamayı operatöre açıkça söyle.

## Mülakatta hızlı tuzak savar notlar

- **Koruma arızayı önlemez:** Arızalı bölgeyi izole eder. Süre uzadıkça IEEE 80 dokunma gerilimi sınırı sıkılaşır.
- **Birinci bölge yüzde seksen civarıdır:** Yüzde yüz yapılırsa ölçü hatası komşu hatta gereksiz açtırır.
- **Yedek:** Daha yavaş ve daha geniş olur. Hızlı olursa asıl korumadan önce açar.
- **Evirici:** Arıza akımı sınırlı ve kontrol güdümlüdür. Klasik eşik arızayı görmeyebilir. Tek kısa devre koşusu yetmez.
- **Ara besleme ve yük taşması:** Biri eksik erişim, diğeri yanlış açmadır. İkisi de “empedans” diye aynı cümlede birleştirilmez.
- **Yakınsamama:** Eski veriyi yeni diye sunma. Sebep ve etkilenen uygulama açıkça söylenir.
