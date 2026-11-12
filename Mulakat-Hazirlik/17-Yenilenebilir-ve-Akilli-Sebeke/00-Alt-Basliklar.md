# 17 — Yenilenebilir, depolama, akıllı şebeke

Bu klasör, güneş ve rüzgâr gibi yenilenebilir kaynakların şebekeye nasıl bağlandığını, bataryaların ne işe yaradığını ve "akıllı şebeke" denince gerçekte neyin kastedildiğini anlatır. Aşağıdaki liste klasörün içindekiler tablosudur. Her maddenin yanında o başlıkta ne öğreneceğin bir cümleyle yazıyor.

Konular iki sayfaya dağılmış durumda:

- [01-Evirici-Depolama-Sebeke-Kodu.md](01-Evirici-Depolama-Sebeke-Kodu.md): evirici türleri, enerji ve kapasite kavramları, depolama, akıllı şebeke, güç kalitesi, model seçimi.
- [02-Sebeke-Kodu-Lisanssiz-Uretim-Depolama.md](02-Sebeke-Kodu-Lisanssiz-Uretim-Depolama.md): şebeke kodunun dört temel gereksinimi, lisanssız üretim ve mahsuplaşma, depolamanın kullanım alanları, elle hesap örnekleri.

## Alt başlıklar

1. **Kaynak türleri ve şebekeye bağlanma biçimi:** güneş ve rüzgârın şebekeye doğrudan değil, bir güç elektroniği cihazı (evirici) üzerinden bağlandığını ve bunun neden önemli olduğunu öğreneceksin.
2. **Şebeke takip ve şebeke oluşturan evirici:** şebekeyi izleyen evirici ile kendisi gerilim ve frekans kuran evirici arasındaki farkı ve bu farkın kararlılığa etkisini öğreneceksin.
3. **Arıza katkısı ve arıza boyunca kalma (fault ride through):** eviricinin arızada ne kadar akım verdiğini ve gerilim çökünce neden hemen ayrılmaması gerektiğini öğreneceksin.
4. **Gerilim ve frekans desteği, LFSM:** eviricinin reaktif güçle gerilimi, aktif güçle frekansı nasıl desteklediğini ve LFSM'nin (Limited Frequency Sensitive Mode, Sınırlı Frekans Duyarlı Mod) eşiklerini öğreneceksin.
5. **Rampa, kısıntı, kapasite faktörü, ELCC:** yenilenebilir üretimin yıl boyunca ve puant saatinde ne kadar işe yaradığını ölçen kavramları, ELCC (Effective Load Carrying Capability, Etkin Yük Taşıma Kapasitesi) dahil, öğreneceksin.
6. **Barındırma kapasitesi ve bağlantı:** bir fiderin hiçbir sınırı bozmadan ne kadar üretim kaldırabileceğini ve bu sınırı ucuzdan pahalıya nasıl artıracağını öğreneceksin.
7. **Depolama: enerji, güç, süre, hizmetler:** bir bataryayı tanımlayan dört sayıyı ve bataryanın hangi hizmetlere hangi zaman ölçeğinde satılabileceğini öğreneceksin.
8. **Talep tarafı ve elektrikli araç:** tüketicinin yükünü kaydırmasının ve araç şarjının şebekeyi nasıl etkilediğini öğreneceksin.
9. **Akıllı şebeke bileşenleri:** akıllı şebekenin ölçüm, kumanda, iletişim, yazılım ve müşteri katmanlarını abartısız bir listeyle öğreneceksin.
10. **Mikro şebeke ve ada:** bilerek planlanmış ada çalışması ile kazara oluşan ada arasındaki farkı öğreneceksin.
11. **Güç kalitesi: harmonik, fliker, dengesizlik:** gerilim dalga biçimini bozan üç sorunun nereden geldiğini ve yönetmelikteki dengesizlik sınırlarını öğreneceksin.
12. **Şebeke yönetmeliği yükümlülükleri:** rüzgâr ve güneş santrallerinden yönetmeliğin ne istediğini ve bu koşulların Türkiye'de nerede yazdığını öğreneceksin.
13. **Düşük atalet senaryosu:** dönen jeneratörler azalıp eviriciler arttıkça frekansın neden daha hızlı değiştiğini öğreneceksin.
14. **Modelleme: statik, RMS, EMT hangisi:** hangi soruda statik yük akışı, hangisinde RMS (Root Mean Square, etkin değer tabanlı fazör benzetimi), hangisinde EMT (Electromagnetic Transient, elektromanyetik geçici hal benzetimi) kullanılacağını öğreneceksin.
