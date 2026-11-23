# Özet

Formül yok. Mülakattan hemen önce bunu oku; sesli, kendi cümlenle söyle.

**Dağıtım**, elektriği mahalleye ve eve indiren kısımdır. Çoğu fider (dağıtım hattı) tek kaynaktan beslenir; buna radyal denir. Hat açılınca arkası enerjisiz kalır. İletimden farkı burada başlar: mahallede direnç daha görünür, bu yüzden aktif güç de gerilimi oynatır. Çatı güneşi öğlen gücü geri basarsa gerilim yükselir; akşam yük artınca gerilim düşer.

Yeni üretimi bağlarken üç şeye bakılır: gerilim sınırı, hattın ve trafonun ısınması, korumanın hâlâ doğru yeri açması. **Barındırma kapasitesi**, hiçbir sınırı bozmadan o fidere sığan üretim miktarıdır. Yetmezse önce ucuz önlem (kademe, reaktif ayar, faz dengesi), sonra pahalı önlem (hat veya trafo yenileme) düşünülür.

Gerilimi yerinde tutmak için **Volt/VAR** kontrolü kullanılır: kademe değiştirici, kondansatör ve eviricinin reaktif gücü. Kesinti sonrası sağlam kısımları başka beslemeye almak **yeniden yapılandırma**dır; radyal yapı bozulmadan anahtarlar çevrilir. Müşterinin gördüğü kalite, kesintinin ne kadar sürdüğü ve ne sıklıkta olduğuyla ölçülür (SAIDI süre, SAIFI sıklık).

**DMS** (Distribution Management System, dağıtım yönetim sistemi) şebekeyi işleten yazılımdır. Akıllı sayaç (**AMI**) müşteri ucundan ölçüm getirir ama her noktayı görmez; dağıtım durum kestirimi bu yüzden iletimdeki kadar bol ölçüme güvenemez, tahminle (pseudo ölçüm) boşluk doldurur. **DERMS** dağıtık üretimi ve depolamayı topluca yönetir. Elektrikli araç, akşam aynı saatte şarj olursa trafoyu ve gerilimi zorlar; kaydırmak ile yeni trafo kurmak ayrı kararlardır.

## Mülakatta hızlı tuzak savar notlar

- **Radyal:** Tek yol açılınca arkası kararır. İletimdeki “akım komşuya kaçar” cümlesi burada varsayılan değildir.
- **Güneş:** Yalnız enerji değildir. Öğlen gerilimi yükseltir, koruma akımının yönünü değiştirebilir.
- **Barındırma:** İsim plakasındaki güç değil, sınırı bozmayan güçtür.
- **Sayaç:** Her barayı görmez. Dağıtım kestirimi ölçüm azlığında tahmine yaslanır; bunu açık söyle.
- **Kesinti yazılımı ile gerilim yazılımı:** Biri müşteri dakikasını, diğeri elektrik sınırını yönetir. Aynı ekran değillerdir.
