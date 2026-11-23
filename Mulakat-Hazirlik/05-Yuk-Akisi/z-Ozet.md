# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

**Yük akışı**, “üretim ve tüketim böyleyse gerilimler ve hatlar ne durumda?” sorusudur. Aranan, her baranın gerilim büyüklüğü ve açısıdır. Hat akışı ve kayıp bundan çıkar. Eldeki veri ile aranan bilinmeyen her barada aynı değildir.

Üç bara tipi vardır. **Yük barası** (PQ): çektiği aktif ve reaktif güç bellidir, gerilim ve açı aranır. **Santral barası** (PV): aktif güç ve gerilim hedefi bellidir, reaktif güç ve açı aranır; reaktif sınır dolunca bu bara yük barasına döner. **Referans bara** (salınım barası): açısı sabitlenir, aktif ve reaktif dengeyi o kapatır. Açı ancak birbirine göre anlamlı olduğu için bir bara referans alınır.

Denklemler doğrusal değildir. **Newton-Raphson** mevcut tahmini, “biraz değiştirirsem ölçülen güç ne kadar değişir” duyarlılığıyla düzeltir. Bu duyarlılık tablosuna **Jacobian** denir. Her turda tahmin güncellenir; düzeltme küçülünce durulur. Yakınsamazsa önce bara tipi, reaktif sınır, ada (kopuk ada), hatalı veri ve kötü başlangıç aranır. Eski sonucu yeniymiş gibi sunmam.

Hızlı bakış için **DC yük akışı** gerilimleri yaklaşık 1 kabul eder, yalnız açıyı ve aktif gücü çözer. Kayıp ve gerilim sorusu sorulamaz; hat doluluğuna kaba bakış içindir. **Hızlı ayrık yük akışı** aktif ve reaktifi kabaca ayırıp tam yöntemden hızlı, DC’den zengin bir orta yol sunar. Dağıtımda direnç büyük olduğu için “aktif güç yalnız açıyı oynatır” varsayımı zayıflar. Üç faz eşit değilse tek faz eşdeğer yetmez. Üretim ve yük belirsizse tek bir çözüm yerine olasılık bandı konuşulur.

Sonuç mühendise “şöyle gerilim” diye değil, operatöre “hangi hat dolu, hangi bara zayıf, ne yapılabilir” diye çevrilir.

## Mülakatta hızlı tuzak savar notlar

- **Yük akışı kestirim değildir:** Üretim ve yük biliniyor kabul edilir. Ölçüm gürültülüyse önce durum kestirimi gelir.
- **PV sınırı:** Reaktif tavan dolunca gerilim hedefi tutulamaz. Bara tipi değişir.
- **DC:** Hızlı aktif akış içindir. Gerilim, kayıp ve reaktif sorusuna cevap değildir.
- **Yakınsamama:** Sessizce son iterasyonu “sonuç” diye verme. Sebebi ve etkilenen hesabı söyle.
- **Dağıtım:** Direnç görünür. İletimdeki aktif-reaktif ayrımı burada kör kullanılmaz.
