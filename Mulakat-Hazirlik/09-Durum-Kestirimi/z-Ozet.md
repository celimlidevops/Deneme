# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

**Durum kestirimi**, gürültülü, eksik, bozuk veya zamanı kaymış SCADA (Supervisory Control and Data Acquisition, uzaktan izleme ve veri toplama) ölçümlerinden, şebeke denklemleriyle tutarlı en olası gerilim büyüklüğü ve açı profilini çıkaran adımdır. Yük akışı üretimin ve yükün doğru bilindiğini varsayar. İşletmede ikisi de tam bilinmez. Kestirim bu boşluğu doldurur. Güvenlik analizi ancak bu profilin üstünde koşar.

Çözüm **WLS** (Weighted Least Squares, ağırlıklı en küçük kareler) ile yapılır. Amaç, ölçüm ile kestirim arasındaki farkların, ölçümün güvenilirliğine göre ağırlıklandırılmış karelerini mümkün olduğunca küçültmektir. İyi sayaca büyük ağırlık verilir. Herkese eşit ağırlık vermek, bozuk sayacı sağlam sayaçla bir tutmaktır.

Amaç fonksiyonunun değişiminin sıfır olduğu yer aranır. Ölçüm denklemleri doğrusal olmadığı için mevcut tahminin etrafında düzleştirilir ve her turda doğrusal bir sistem çözülür. Bu sistemin katsayı tablosuna **kazanç matrisi** denir: ölçümün duruma duyarlılığı ile ağırlıkların birleşimi. Bu tablo tekil değilse ve ölçümler ağın yapısını kurabiliyorsa sistem **gözlenebilirdir**. Yani durum, ölçümlerden tek anlamlı biçimde çıkar.

Kötü veri önce **ki-kare** testi ile aranır: toplam hata belirlenen eşiği aşıyor mu. Sonra **normalize artık** ile en büyük şüpheli bulunur. Her ölçümün kalan hatası, kendi artık sapmasına bölünür; böylece farklı sayaçlar kıyaslanır. Her seferinde yalnızca tek bir ölçüm çıkarılır ve kestirim yeniden çalıştırılır. Büyük artıkların hepsini aynı anda atmak yanlıştır. Bozuk ölçüm çözümü kendine çeker, sağlam komşuların artığını da şişirir. Buna **bulaşma** denir. Sağlam veri de dışarı atılabilir.

Bir durumu yalnızca tek ölçüm görüyorsa o ölçüm **kritiktir**. Hatalıdır ama artık testinde gizlenir. İki ölçüm aynı bilgiyi taşıyorsa **kritik çift** oluşur. Bozulma fark edilir, hangisinin hatalı olduğu tek başına ayırt edilemez. Ölçüm yetmeyen yere, düşük ağırlıkla tahmin değer konur. Buna pseudo ölçüm denir. Yanlış kesici durumu veya yanlış hat parametresi ise ölçüm atarak düzelmez; topoloji ve parametre ayrı şüphedir.

**PMU** (Phasor Measurement Unit, GPS uydu saatiyle eşzamanlı fazör ölçen cihaz) saniyede onlarca kez açı ve gerilim ölçer. Dikdörtgen koordinatlarda model doğrusal hale gelir; yineleme gerekmez, tek adımda çözülür. Bu hız, SIPS (sistem bütünlüğü koruma şeması) gibi hızlı izleme ve koruma uygulamalarını besler. Klasik kestirim dakikalar mertebesindedir. Geniş alan izleme ise saniyenin altındadır. Normal denklemler, ağırlıklar birbirinden çok farklıysa sayıyı kötü koşullar. Pratikte QR ayrışımı veya Hachtel yöntemi gibi daha kararlı çözümler tercih edilir.

Kestirim yakınsamazsa eski sonucu yeniymiş gibi gösterme. Son geçerli kestirimi zaman damgasıyla, yakınsamama sebebini ve bundan etkilenen alt uygulamaları operatöre açıkça söyle.

## Mülakatta hızlı tuzak savar notlar

- **Kritik ölçüm ve kritik çift:** Tek ölçüm hatayı gizler. İki ölçüm arızayı sezdirir ama suçluyu ayırt ettirmez.
- **Kötü veri:** Her seferinde tek ölçüm çıkar. Hepsini birden silmek sağlam veriyi de götürür.
- **Topoloji:** Yanlış kesici veya yanlış hat parametresi, ölçüm atarak düzelmez.
- **PMU:** Modeli doğrusal yapar ve hızlı uygulamayı besler. Klasik SCADA kestiriminin yerini “her şeyi çözer” diye anlatma.
- **Yakınsamama:** Eski veriyi yeni diye sunma. Zaman damgası, sebep ve etkilenen uygulama açıkça yazılır.
