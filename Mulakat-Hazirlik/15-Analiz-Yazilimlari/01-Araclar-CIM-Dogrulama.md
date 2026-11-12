# Analiz yazılımları ve veri modelleri

Araç bilmek, düğme bilmek değildir. Aracın hangi varsayımla çözdüğünü ve modelin komşu araca nasıl bozulduğunu anlatabilmektir.

> **Sade anlatım:** Bir programın menüsünü ezberlemek yetmez. Programın arka planda neyi basitleştirdiğini bilmen gerekir. Bir de aynı şebekeyi başka bir programa taşıdığında nerelerin bozulduğunu bilmen gerekir.

Bu sayfa dört parçadan oluşur:

1. Araçlar ve her birinin güçlü ve sınırlı olduğu yer.
2. Hangi mühendislik sorusunun hangi araca gittiği.
3. Veri modeli: model alışverişi neden kırılır, CIM ve CGMES nedir.
4. Doğrulama ve betik: aracın verdiği sayıya nasıl güvenilir, iş nasıl otomatikleşir.

## Araçlar

Önce tablodaki kısaltmaları açalım:

| Kısaltma | Açılımı | Anlamı |
| --- | --- | --- |
| RMS | Root Mean Square (etkin değer) | Dinamik benzetimde dalga şekli yerine fazörün genliği ve açısı izlenir. Saniyeler ölçeğindeki olaylar içindir. |
| EMT | Electromagnetic Transient (elektromanyetik geçici hal) | Gerilim ve akımın anlık dalga şekli izlenir. Milisaniye ve altı olaylar içindir. |
| API | Application Programming Interface (uygulama programlama arayüzü) | Programı arayüz yerine kodla sürmeyi sağlar. |
| PSS/E | Power System Simulator for Engineering | Siemens'in iletim analiz paketi. |
| ETAP | Electrical Transient Analyzer Program | Endüstriyel şebeke analiz paketi. |
| EMS | Energy Management System (enerji yönetim sistemi) | İşletmede canlı veriyle çalışan kontrol merkezi yazılımı. |
| OPF | Optimal Power Flow (optimal güç akışı) | Maliyet gibi bir hedefi en iyileyen yük akışı. |
| MATPOWER | MATLAB tabanlı güç sistemi paketi | Yük akışı ve OPF için akademik araç. |

Aşağıdaki tablo her aracın güçlü olduğu yeri ve sınırını gösterir:

| Araç | Güçlü olduğu yer | Sınırı |
| --- | --- | --- |
| DIgSILENT PowerFactory | İletim ve dağıtım, dinamik, koruma, RMS/EMT, Python API | Lisans, büyük vaka dosyası disiplini |
| Siemens PSS/E | İletim planlama, dinamik, ham veri dosyası yaygın | Dağıtım dengesiz modeli asıl işi değil |
| PSCAD / EMTP-RV | Milisaniye, evirici kontrolü, yalıtım, ferrorezonans | Şebekenin tamamı değil, kritik kesit |
| ETAP | Endüstriyel şebeke, kısa devre, koruma koordinasyonu | Ulusal iletim EMS’i değil |
| PowerWorld | Eğitim, görsel yük akışı, duyarlılık | Büyük dinamik çalışma için değil |
| MATLAB + MATPOWER / Simulink | Algoritma, kontrol, makale | Ürün sunucusu değil |
| pandapower | Python ile yük akışı, OPF, zaman serisi | Üretici dinamik kütüphanesi sınırlı |
| OpenDSS | Dağıtım, dengesiz, zaman serisi | İletim dinamik analizi değil |
| GridLAB-D | Dağıtım, ev yükü, birlikte simülasyon | Öğrenme eşiği |
| CYME | Dağıtım şirketi planlaması | Ekosisteme bağlı |
| Gerçek zamanlı simülatör | Röle ve kontrolör kapalı çevrim | Pahalı, model sadeleştirilir |

Tablodaki bazı terimler ilk kez öğrenen biri için açıklama ister:

- **Ferrorezonans:** Trafonun doymaya giren demir çekirdeği ile kablo veya kesici kapasitansı arasında oluşan, yüksek ve düzensiz aşırı gerilim olayıdır.
- **Kritik kesit:** EMT araçları şebekenin tamamını değil, incelenen olaya yakın küçük bir bölümü ayrıntılı modeller.
- **Dengesiz model:** Dağıtımda üç faz eşit yüklenmez. Bu yüzden her faz ayrı çözülür.
- **Kapalı çevrim:** Gerçek röle veya kontrolör, simülatöre bağlanır. Simülatör ona sinyal verir, o da simülatöre karar döndürür.

Hangisini kullandıysan onu derin anlat. Kullanmadığını “biliyorum” deme.

Şu cümle yeter: “PowerFactory’de şunu koştum, PSS/E ham verisini şu yüzden içeri aldım, doğrulamayı şu barada yaptım”.

Hiçbiri yoksa pandapower ile küçük bir N-1'i mülakattan önce kendi elinle koşmuş ol. N-1, şebekeden tek bir elemanın (bir hat, bir trafo veya bir üreteç) çıktığı durumda sistemin sınırlar içinde kalıp kalmadığını sınamaktır.

Bu klasörün kardeşi `14/ornekler` hesap içindir. pandapower kurulumu lisanssızdır.

## Hangi soru nereye

Aracı ürün adına göre değil, sorunun türüne göre seçersin. Liste şöyle:

| Soru | Gittiği araç veya yöntem |
| --- | --- |
| Günlük termik ve gerilim | AC yük akışı, planlama aracı veya EMS. |
| Binlerce N-1 | DC elek + AC doğrulama, betik. |
| Koruma eğrisi | Koruma modülü, kısa devre ile birlikte. |
| Açı kararlılığı | RMS dinamik. |
| Evirici kontrolü, TRV, ferrorezonans | EMT. |
| Dağıtım gerilim, çatı güneş yılı | OpenDSS veya pandapower zaman serisi, üç faz gerekebilir. |
| Kapalı çevrim röle testi | Gerçek zamanlı simülatör + ikincil enjeksiyon. |

Tablodaki terimler:

- **AC yük akışı:** AC (Alternating Current, alternatif akım) yük akışı gerilim genliğini, açıyı ve reaktif gücü tam hesaplar.
- **DC elek:** DC (Direct Current, doğru akım) yük akışı yaklaşık ve hızlıdır. Yalnız aktif güç ve açıyı hesaplar. Binlerce N-1 vakasını hızlıca eler. Şüpheli çıkanlar sonra AC ile doğrulanır.
- **Termik:** Hattın veya trafonun akım yüzünden ısınma sınırıdır.
- **TRV:** Transient Recovery Voltage (geçici toparlanma gerilimi). Kesici akımı kestikten hemen sonra kontakları arasında oluşan gerilimdir.
- **Çatı güneş yılı:** Çatı güneş panellerinin bir yıl boyunca saat saat etkisinin izlenmesidir.
- **İkincil enjeksiyon:** Röleye, gerçek akım ve gerilim trafosu yerine, test cihazından ikincil devre düzeyinde sinyal vermektir.

Aynı vakanın RMS ve EMT sonucu milisaniyede ayrışır. Ayrışınca hangisinin ihmalinin devrede olduğunu söyle: şebeke frekansı modeli RMS’te cebirseldir, EMT’de diferansiyeldir.

> **Sade anlatım:** RMS aracı şebekeyi her an "sabit frekansta sinüs" sayar ve hat ile trafoyu cebirsel denklemle çözer. Bu yüzden çok hızlı olayları göremez. EMT aracı hat ve trafoyu diferansiyel denklemle çözer ve dalga şeklini anbean izler. İki sonuç ilk milisaniyelerde farklıysa sebep genelde bu ihmaldir.

## Veri modeli

Bir şebeke modeli bir araçtan ötekine taşınır. Buna model alışverişi denir. Bu taşımada model sık sık bozulur.

Kırılan alışverişin alışılmış nedenleri:

| Neden | Ne bozulur |
| --- | --- |
| Baz güç 100 MVA burada, 1000 orada | MVA (megavoltamper) cinsinden baz farklıysa per-unit (birim değer) empedanslar yanlış ölçeklenir. |
| Kademe oranının hangi sargıya yazıldığı | Trafo kademesi yanlış tarafa uygulanırsa gerilim ters yönde kayar. |
| Trafo grubu ve saat açısı | Sargı bağlantısının getirdiği faz kayması kaybolabilir. |
| Hatın şönt B’sinin tamamı mı yarısı mı | Hattın şönt suseptansı (B) toplam mı yazılır, her uca yarısı mı, araçtan araca değişir. |
| İşaret: yük negatif mi pozitif mi | Yük üretim gibi görünebilir. |
| Slack’in kim olduğu | Slack (salınım barası), kayıpları ve dengesizliği karşılayan referans baradır. Farklı seçilirse akışlar değişir. |
| Limitin nominal mi mevsimsel mi | Aynı hat bir araçta yüklü, ötekinde aşırı yüklü görünebilir. |
| Dinamik modelin (AVR, PSS, governor) ayrı kütüphanede kalması | AVR (Automatic Voltage Regulator, otomatik gerilim regülatörü), PSS (Power System Stabilizer, güç sistemi kararlılık sağlayıcısı) ve governor (hız regülatörü) modelleri taşınmayabilir. |
| Koordinat ve bara adının GIS ile uyuşmaması | GIS (Geographic Information System, coğrafi bilgi sistemi) ile model eşleşmez. |

### Dosya biçimleri ve CIM

PSS/E `.raw` iletim değiş tokuşunun eski ortak dilidir.

Avrupa planlama verisi UCTE DEF ve bugün CGMES ile yürür. UCTE, Avrupa'nın eski iletim koordinasyon birliğidir (Union for the Co-ordination of Transmission of Electricity). DEF onun veri değişim biçimidir (Data Exchange Format).

CIM (IEC 61970/61968) şebekeyi UML sınıflarıyla anlatır: ekipman, topoloji, durum.

- CIM, Common Information Model (ortak bilgi modeli) demektir.
- IEC, International Electrotechnical Commission (Uluslararası Elektroteknik Komisyonu) demektir. IEC 61970 iletim ve EMS tarafını, IEC 61968 dağıtım tarafını kapsar.
- UML, Unified Modeling Language (birleşik modelleme dili) demektir. Nesneleri sınıf ve ilişki olarak tanımlar.

CGMES, CIM’in Avrupa profilidir. CGMES, Common Grid Model Exchange Standard (ortak şebeke modeli değişim standardı) demektir. ENTSO-E model paylaşımı buna dayanır. ENTSO-E, European Network of Transmission System Operators for Electricity (Avrupa elektrik iletim sistemi işletmecileri ağı) demektir.

Türkiye enterkonneksiyon çalışması Avrupa modeliyle konuşacaksa bu profil kapıdır.

> **Sade anlatım:** CIM, şebekeyi anlatan ortak bir sözlüktür. CGMES, Avrupa'nın bu sözlükten seçtiği ve herkesin uyduğu kurallar setidir. Türkiye Avrupa şebekesiyle model paylaşacaksa bu kurallara uymak zorundadır.

### CIM her şeyi tek dosyada çözmez

CIM'de bilgi parçalara ayrılır. Her parçaya profil denir:

| Profil | İçerik |
| --- | --- |
| Ekipman | Hat, trafo, üreteç gibi fiziksel elemanlar. |
| Durum (kesici) | Kesici açık mı kapalı mı. |
| Analog değer | Ölçülen akım, gerilim, güç. |
| Diyagram | Şemanın çizim bilgisi. |

Durum kestirimi “ekipman dosyası” ile çalışmaz; topoloji ve analog ister. Durum kestirimi, ölçümlerden şebekenin en olası anlık durumunu hesaplayan EMS işlevidir.

Koruma modeli CIM’de zayıftır, çoğu zaman ayrı kalır.

Bunu bilmek, “CIM’e aktardık, bitti” cümlesini düzeltir.

## Doğrulama

Yeni araca geçmiş bir model için asgari kontrol altı adımdır. Her adımın ne işe yaradığı yanında yazıyor:

1. **Bara, hat, trafo sayısı.** Taşımada eleman kaybolmuş ya da çoğalmış mı, bunu yakalar.
2. **Toplam üretim, yük, kayıp.** Sistemin genel güç dengesi eski araçla aynı mı, bunu gösterir.
3. **Seçilmiş 10 hattın akışı, eski araçla.** Empedans, kademe ve topoloji hatalarını hat düzeyinde yakalar.
4. **Seçilmiş 10 gerilim.** Kademe, reaktif kaynak ve şönt hatalarını bara düzeyinde yakalar.
5. **Bir kısa devre barası, üç faz ve tek faz-toprak.** Sıfır bileşen ve topraklama verisinin doğru taşındığını sınar.
6. **Slack gücü makul mü.** Slack çok büyük güç veriyor ya da çekiyorsa bir yerde yük, üretim veya işaret hatası vardır.

Fark varsa önce baz, işaret ve kademe. “Yeni araç daha doğrudur” kolay kaçıştır. Fark açıklanmadan rapor çıkmaz.

### Türkiye modeli ve gizlilik

Türkiye modeli kamu malı değildir. Mülakatta gerçek bara adı, gerçek kısıt veya müşteri verisi konuşulmaz.

Mülakatta konuşulanlar:

- Yöntem
- Büyüklük mertebesi
- Senin rolün

Örnek veri olarak IEEE 14, 39, 118 veya küçük sentetik dağıtım fideri kullan. IEEE (Institute of Electrical and Electronics Engineers) test sistemleri herkese açık standart örnek şebekelerdir. Sayı, sistemdeki bara sayısını gösterir.

Akademik vakada yöntemi anlatmak giz ihlali değildir.

## Betik

Arayüzden elle 40 senaryo koşmak hata üretir.

PowerFactory Python, PSS/E Python veya pandapower ile şu dört adımı betiğe yaptırırsın:

1. Senaryo tablosunu oku.
2. Çöz.
3. İhlalleri yaz.
4. Sürümü etiketle.

Ürünleşme, bu betiğin bir servise ve veri tabanına taşınmasıdır. `16` klasörü o taşımayı anlatır.

> **Sade anlatım:** Önce bilgisayarında çalışan bir betik yazarsın. Sonra bu betik, başkalarının da çağırabildiği bir servise dönüşür ve sonuçlar bir veri tabanında saklanır. Buna ürünleşme denir.

Aşağıdaki konuşma, bu sayfanın tamamını mülakatta tek nefeste anlatman içindir. İçinde araç seçimi, model taşıma, doğrulama, CGMES ve betik var.

## 90 saniye

“Aracı soruya göre seçerim: planlama AC ve dinamik için PowerFactory veya PSS/E, milisaniye için EMT, dağıtım dengesiz için OpenDSS veya pandapower, algoritma için MATPOWER. Model taşırken baz, kademe, trafo grubu ve işaret bozulur; sayı ve seçilmiş akışla doğrularım. Avrupa ile model CGMES profilidir. Elle senaryo yerine betik, betiğin ürün hali servistir.”
