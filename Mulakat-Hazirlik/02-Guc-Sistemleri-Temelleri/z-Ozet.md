# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

Elektrikte iki güç vardır. **Aktif güç** iş yapar: motoru döndürür, lambayı yakar. **Reaktif güç** hattı ve manyetik alanı doldurur; iş yapmaz ama gerilimin ayakta kalması için gerekir. Ülke dengesi **frekansa** bakarak anlaşılır; herkes aynı hızda döner. Mahalle dengesi **gerilime** bakarak anlaşılır; gerilim yerelde üretilen ve tüketilen reaktife bağlıdır, uzaktan taşınması zordur.

Uzak taşıma yüksek gerilimle yapılır. Aynı güç, gerilim yükselince daha küçük akımla gider; hat ısınması ve kayıp azalır. Trafolar bu yüzden santral çıkışında yükseltir, şehre inerken düşürür.

Bilgisayar şebekeyi bir bağlantı tablosuyla tutar. Buna **Ybus** denir. Çoğu kutu boştur, çünkü her bara her baraya bağlı değildir. Bu yüzden bütün tabloyu ters çevirmek yerine boşlukları koruyan seyrek çözüm kullanılır.

Farklı gerilim seviyelerini aynı dilde kıyaslamak için **per-unit** (birim değer) kullanılır. Her büyüklük, kendi bazına bölünür; trafo oranı denklemden kaybolur ve şebeke tek ölçekte yazılır.

Toprak arızasında akımın yolu, trafonun nasıl bağlandığına bağlıdır. Yıldız noktası toprağa bağlı değilse toprak arıza akımı kapanmaz veya çok küçük kalır. Koruma da bu yüzden “arıza var mı”yı trafo bağlantısına bakmadan söyleyemez. Yük, gerilim düşünce her zaman aynı güçte kalmaz; bazı yükler gerilimle birlikte azalır, bazıları kendini toparlamaya çalışır. Bu varsayım gerilim çökmesi hesabını değiştirir.

## Mülakatta hızlı tuzak savar notlar

- **Aktif ve reaktif:** Biri iş, biri gerilim desteğidir. Reaktif yakında üretilir.
- **Frekans ve gerilim:** Frekans ülkenin ortak nabzı, gerilim mahallenin tansiyonudur.
- **Ybus:** Bağlantı tablosudur. Çoğu göz boştur; tersini almak yerine seyrek çözülür.
- **Toprak arızası:** Akımın yolu trafo bağlantısına bağlıdır. Bağlantıyı sormadan “akım şöyle olur” deme.
- **Yük:** Gerilim düşünce yükün ne yapacağı bir varsayımdır. Varsayımı söylemeden sonucu kesinleştirme.
