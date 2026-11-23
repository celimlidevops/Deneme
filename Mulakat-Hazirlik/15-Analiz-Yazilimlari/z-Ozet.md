# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

Aracın menüsünü ezberlemek yetmez. Aracın neyi basitleştirdiğini ve modeli başka araca taşıyınca nerede bozulduğunu bilmek gerekir.

Üç zaman vardır. **Planlama aracı** (PowerFactory, PSS/E gibi) canlı şebekeye bağlı değildir; gelecek senaryoyu çözer. **İşletme aracı**, enerji yönetim sistemi gibi, o anki ölçümle çalışır. **Elektromanyetik geçici hal aracı** (PSCAD, EMTP) milisaniyedeki dalga şeklini görür. Fazör tabanlı araç her anı “sabit frekansta sinüs” sayar; güç elektroniğinin iç olayını göstermez. İki aracın ilk milisaniyeleri uyuşmuyorsa sebep çoğu zaman bu ihmaldir.

Hangi soru hangi araca gider: hat ısınması ve gerilim için yük akışı, binlerce arıza için hızlı tarama, saniyelik salınım için dinamik model, koruma koordinasyonu için kısa devre ve röle eğrisi, evirici arızası için elektromanyetik geçici hal. Açık kaynakta pandapower ve MATPOWER yük akışı ve optimal güç akışı, OpenDSS ve GridLAB-D dağıtım, PyPSA planlama ve enerji sistemi içindir. Ticari aracı kullanmadıysan bunu açık söyle, aynı hesabı hangi yoldan yaptığını göster, nasıl öğreneceğini ekle.

Model taşınınca baz güç, trafo kademesi, trafo grubu, işaret yönü ve sıfır dizi sessizce bozulur. Dosyalar da ayrıdır: şebeke modeli, arıza listesi, dinamik model ve koruma ayarı tek dosyada durmak zorunda değildir. **CIM** (Common Information Model, ortak bilgi modeli) şebekeyi anlatan ortak sözlüktür. **CGMES**, Avrupa’nın bu sözlükten seçtiği değişim kuralıdır. Türkiye Avrupa modeliyle konuşacaksa bu profile bakılır.

Türkiye şebeke modeli kamu malı değildir. Mülakatta kurum verisini, gizli tek hattı ve müşteri yükünü anlatma. Doğrulama ise anlatılır: aynı baz, seçilmiş hat akışları, gerilim ve bir kısa devre noktası iki araçta karşılaştırılır. Betik önce senin makinede koşar, sonra başkasının çağırdığı servise ve saklanan sonuca dönüşür. Buna ürünleşme denir.

## Mülakatta hızlı tuzak savar notlar

- **Menü değil varsayım:** Araç neyi sinüs sayıyor, neyi ihmal ediyor, onu söyle.
- **Kullanmadım:** Açık söyle, eşdeğer yolu göster, öğrenme planını ekle. Uydurma ekran anlatma.
- **Taşıma:** Baz, kademe, trafo grubu ve işaret. “Dosyayı açtım, oldu” deme.
- **CIM:** Ortak sözlüktür. Her aracın kendi dosyasının yerine geçtiğini iddia etme; profil ve sürüm gerekir.
- **Gizli model:** Türkiye şebekesinin ham verisini mülakatta dökme.
