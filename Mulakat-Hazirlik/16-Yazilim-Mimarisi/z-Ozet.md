# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

Şebeke yazılımı bir banttır. Ölçüm sahadan gelir, topoloji kurulur, durum kestirilir, kötü veri ayıklanır, yük akışı ve güvenlik analizi koşar, sonuç operatöre gider. Bir halka bozuk veri verirse arkadaki bütün halkalar yanlış hesaplar.

**SCADA** ölçer ve kumanda eder. **EMS** (enerji yönetim sistemi) o ölçümle hesap yapar; analiz modülü kesiciye doğrudan kumanda etmez. **Topoloji işlemcisi**, kesici ve ayırıcı konumundan o anki adaları ve bara modelini kurar. Yanlış kesici bilgisi, sonraki bütün hesapları yanlış şebekeye oturtur.

**Dijital ikiz** üç boyutlu resim değildir. Ölçümle güncellenen, üzerinde senaryo koşulan hesap modelidir. Çevrimdışı planlama modeli ile “şu an” modeli karışırsa operatör geleceğin senaryosunu bugünün gerçeği sanır. İkisinin sürümü ve zaman damgası ayrı durur.

Şebeke kimliği (bara, hat, limit) ile ölçüm zaman serisi ayrı tutulur. Biri yavaş değişen model, diğeri hızla akan sayıdır. Ağır iş, kullanıcının tıklamasının içinde koşmaz. Binlerce arıza bir **kuyruğa** girer; servis “hesap bitti” deyince sonucu yazar. Her sonucun yanında kalite bayrağı vardır: kestirim yakınsadı mı, veri bayat mı, hangi uygulama etkilendi. Bayrak yoksa operatör eski veya bozuk sayıyı taze sanır.

Yeni sistemler çoğu zaman REST, eski kurum sistemleri SOAP ile konuşur. İkisini de “web servis” diye geçiştirme. Model, algoritma ve limit sürümleri ayrıdır; algoritmayı değiştirince şebeke modeli değişmiş sayılmaz. Erişim role göredir, yapılan işlem kayıtlıdır, sırlar kodun içine yazılmaz.

Siber tarafta kötü veri testi “ölçümler birbiriyle tutarlı mı” diye bakar. Saldırgan bütün ölçümleri aynı yalanla tutarlı değiştirirse artık testi tek başına görmez. Bunu sınır olarak söyle.

Kendi yazılım tecrübeni bu banda bağla: hangi halkayı yazdın, girdi-çıktı sözleşmesi neydi, hata olursa kullanıcı ne gördü.

## Mülakatta hızlı tuzak savar notlar

- **Zincir:** Ölçüm, topoloji, kestirim, akış, güvenlik, ekran. Bir halkayı atlama.
- **İkiz:** Hesap modelidir. Üç boyutlu çizim değildir. Canlı model ile plan modeli karıştırılmaz.
- **Kumanda:** Analiz yazılımı SCADA’nın yerine kesici açmaz. Öneri üretir.
- **Kalite bayrağı:** Yakınsamayan veya bayat sonucu yeni diye gösterme.
- **Tutarlı yalan:** Kötü veri testi, hep birlikte kaydırılmış ölçümü sağlam sanabilir. Bunu bilmediğini söyleme, sınır olarak söyle.
