# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

**Optimizasyon**, kurallara uyarak en ucuz veya en iyi seçimi bulmaktır. Üç parçası vardır: neyi seçeceğin (karar), neyi küçülteceğin (amaç), hangi sınıra uyacağın (kısıt). Mülakatta önce “bu hangi sınıf” denir, sonra çözümün gerçek şebekede çalışıp çalışmadığı sorulur.

**Dışbükey** problem tek çukurlu bir kâsedir. Top nereden bırakılırsa bırakılsın aynı dibe iner. Bulunan iyi, genel iyidir. **AC optimal güç akışı** çok çukurludur. Çözücü bir çukura iner; en derin çukur o olmayabilir. Bunu “kesin en iyi” diye satma.

Amaç ve kısıtlar düz çizgiyse problem **doğrusal program**dır. DC optimal güç akışı bu ailedendir: hızlıdır, gerilim ve kayıp ayrıntısını taşımaz. Aç-kapa gibi evet-hayır karar eklenirse **karışık tamsayılı** problem olur. Ünite tahsisi budur. Santral kararını 0,6 bulup 1’e yuvarlamak yanlıştır; açmak minimum üretim ve yakıt getirir. Trafo kademesi ise çoğu zaman gevşetilip yuvarlanabilir, çünkü komşu kademeler birbirine yakındır.

Bir kısıtın **gölge fiyatı**, o sınırı bir birim gevşetirsem ne kazanırım sorusunun cevabıdır. Sınır rahatsa fiyat sıfırdır. Hat dolmuşsa fiyat, o hatta bir MW daha taşımanın değeridir. Hatlar boşken elektrik her barada benzer fiyata gider. Bir hat dolunca ucuz güç bazı baralara ulaşamaz ve oradaki fiyat yükselir. Buna düğüm fiyatı, **LMP** denir.

Sezgisel yöntemler (genetik, parçacık sürüsü) türevin olmadığı veya çok engebeli problemde denenebilir. Dışbükey ve standart şebeke probleminde hazır çözücüden daha zayıf bir iddiadır. Maliyet ile güvenilirlik çelişirse tek sayı yerine **Pareto** cephesi gösterilir: birini iyileştirince diğeri bozulan seçenekler.

Çözücü yanlış modeli de mutlu mutlu çözer. Birim karışıklığı uyarı vermez, yanlış plan verir. “Uygun çözüm yok” derse kısıtlar birlikte imkânsızdır. “Sınırsız” derse amaç, maliyetsiz büyüyen bir değişkene bağlıdır. Ulusal problem parçalanır: ünite kararı ayrı, şebeke ayrı, senaryolar ayrı çözülüp bağlanır. Buna ayrıştırma denir.

## Mülakatta hızlı tuzak savar notlar

- **Sınıf önce:** Doğrusal, tamsayılı veya doğrusal olmayan demeden çözücü adı sayma.
- **AC optimal güç akışı:** Yerel iyi bulur. “En iyi budur” garantisi verme.
- **Gölge fiyat:** Rahat kısıtta sıfırdır. Dolu hattın bir MW’ının değeridir.
- **Yuvarlama:** Kademe yuvarlanabilir. Ünite aç-kapa yuvarlanamaz.
- **Çözücü:** Hata vermemesi modelin doğru olduğunu göstermez. Birim ve kısıt ayrıca kontrol edilir.
