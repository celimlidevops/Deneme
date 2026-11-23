# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

Bu kadroda kod, menü ezberi değildir. Bir güç sistemi hesabını doğru, test edilmiş ve başkasının çağırabildiği bir parçaya dönüştürmektir. Katmanlar ayrılır. **Python** hesabı dener ve veriye bakar. **MATLAB** laboratuvar tezgâhıdır; fikir orada kanıtlanır, ürüne tezgâhın kendisi değil kanıtlanan yöntem gider. **Java** büyük enerji yönetim sistemlerinde servisin dilidir. **JavaScript** operatörün gördüğü ekrandır: grafik, harita, uyarı.

Bilimsel Python’da dizi hesabı NumPy, seyrek şebeke matrisi scipy, tablo pandas ile yapılır. Şebeke matrisi seyrektir; çoğu göz boştur. Tam matris gibi saklamak belleği ve süreyi boşa harcar. pandapower veya MATPOWER kullanmak ayıp değildir. Mülakatta “paketi çağırdım” ile “yakınsamazsa bara tipine, adaya ve birime bakarım” arasındaki fark puan getirir.

Canlı kodlamada önce sözleşmeyi söyle: girdi nedir, çıktı nedir, neyin yanlışında dururum. Sonra en küçük doğru çözümü yaz. Newton-Raphson’da her turda duyarlılık tablosu kurulur, düzeltme çözülür, gerilim güncellenir. Desen değişmiyorsa seyrek matrisin “hangi göz dolu” planı bir kez yapılır, her turda yalnız sayılar yenilenir.

Önce doğru ve okunur kod, sonra ölçerek hızlandırma. Erken hız, yanlış sonucu çabuk üretir. Aynı girdi her seferinde aynı sonucu vermelidir: sürüm, veri ve parametre birlikte durur. Birim testi yakınsamayı, bilinen küçük şebekeyi ve birim karışıklığını yakalar. Sürekli entegrasyon, her değişiklikte bu testleri koşturur. İki kişi aynı dosyaya aynı anda yazmasın diye her dal kendi kopyasıdır; bu Git’tir.

Kod sorusunda susmak yerine düşünceyi sesli söyle. Takıldığın yeri “burada seyrek çözücü çağırırım, elimle tersini almam” diye adlandır.

## Mülakatta hızlı tuzak savar notlar

- **Dört dil:** Python dener, MATLAB kanıtlar, Java servis olur, JavaScript gösterir. Hepsinde aynı işi yapıyorum deme.
- **Kütüphane:** Kullanmak serbest. Motoru anlamamak puan kırar.
- **Sıra:** Önce doğru, sonra hızlı. Ölçmeden optimize etme.
- **Seyrek:** Boş gözleri saklama. Her turda deseni baştan kurmak zorunda değilsin.
- **Test:** “Benim makinemde çalıştı” yetmez. Bilinen şebeke, birim ve yakınsamama hali testte durur.
