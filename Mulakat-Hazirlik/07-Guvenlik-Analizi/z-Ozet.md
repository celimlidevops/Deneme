# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

Üç kelime karışır. **Güvenilirlik**, uzun vadede ışık yeterince yanıyor mu sorusudur. **Güvenlik**, şu an bir eleman kaybedilirse limitler aşılır mı sorusudur. **Kararlılık**, sarsıntıdan sonra sistem yerine oturur mu sorusudur. Güvenlik analizi ikinci soruyu sistemli sorar.

**N-1**, tek bir elemanın devre dışı kalmasıdır. **N-1-1**, biri gittikten ve operatör müdahale ettikten sonra ikincinin gitmesidir. **N-2**, iki elemanın birlikte gitmesidir. Aynı direkteki iki hat ortak moddur; iki ayrı şans gibi sayılmaz. Türkiye planlamasında N-1 sonrası kullanıcı kaybı ve kontrolsüz ada istenmez.

İhlal üç türlü olur: hat veya trafo ısınır (termik), gerilim bant dışına çıkar, sistem kararlılığını kaybeder. Binlerce arızanın hepsini tam modelle çözmek yavaştır. Önce hızlı ve kaba bir elek (çoğu zaman DC, doğru akım yaklaşımlı bakış) şüphelileri sıralar, sonra tam yük akışı yalnız tehlikeli olanları doğrular. Sıralama, limite yakın veya limiti aşan vakayı öne alır.

Müdahale iki zamanlıdır. **Önleyici** kontrol, arıza olmadan üretimi ve akışı rahatlatır; pahalı ama hazırlıklıdır. **Düzeltici** kontrol, arızadan sonra birkaç dakika içinde aksiyon alır; daha ucuzdur ama operatörün yetişeceği varsayılır. İkisi birlikte güvenlik kısıtlı optimal güç akışına (**SCOPF**) girer: plan hem şimdi hem seçilen arızalar sonrası sınıra uyar.

Tek bir açma, komşu hattı aşırı yükler, o da açar ve sistem adalara bölünür. Buna zincirleme denir. **SIPS** (sistem bütünlüğü koruma şeması) yangının yayılmasını beklemez; küçük ve kontrollü bir kesintiyle büyük kararmayı önler. Operatöre ham liste değil, en kritik vaka, ihlal türü ve önerilen hareket verilir. Yük, rüzgâr ve bakım tahmini kayıksa “güvenli” sonuç da kayar; belirsizliği söyle.

## Mülakatta hızlı tuzak savar notlar

- **Üç kelime:** Güvenilirlik uzun vade, güvenlik şimdiki limit, kararlılık sarsıntıdan sonra toparlanmadır.
- **N-1 ve N-1-1:** İkincisinde arada operatörün iş yapacak zamanı vardır. İkisi aynı liste değildir.
- **Ortak mod:** Aynı direk, aynı koridor. Ayrı ayrı N-1 saymak eksik kalır.
- **Hız:** Önce elek, sonra tam model. Eleği nihai karar diye sunma.
- **SIPS:** Arızayı önlemez. Yayılmayı kontrollü kayıpla keser. Rölenin yerel doğru kararı sistemi bölebilir.
