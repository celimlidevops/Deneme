# Genişleme, LOLE/EENS ve TEİAŞ projeksiyonları

Bu sayfa dört şeyi anlatır:

1. Genişleme planlamasının bir optimizasyon problemi olarak nasıl kurulduğu.
2. Güvenilirliğin iki göstergesi olan LOLE ve EENS'in elle nasıl hesaplandığı.
3. Bir iletim yatırımının fayda/maliyetinin elle nasıl hesaplandığı.
4. TEİAŞ'ın (Türkiye Elektrik İletim Anonim Şirketi) yayımladığı talep projeksiyonlarında neyin doğrulanmış olduğu.

Kısaltmalar:

| Kısaltma | Açılımı | Türkçesi |
| --- | --- | --- |
| LOLP | Loss of Load Probability | Yük Kaybı Olasılığı |
| LOLE | Loss of Load Expectation | Beklenen Yük Kaybı Süresi |
| EENS | Expected Energy Not Served | Beklenen Verilemeyen Enerji |
| EUE | Expected Unserved Energy | Beklenen Karşılanamayan Enerji (EENS'in diğer adı) |
| FOR | Forced Outage Rate | Zorunlu Devre Dışı Kalma Oranı |
| VOLL | Value of Lost Load | Verilemeyen Enerjinin (Kayıp Yükün) Değeri |
| ELCC | Effective Load Carrying Capability | Etkin Yük Taşıma Kapasitesi (kapasite değeri) |
| N-1 | — | Herhangi tek bir eleman (hat, trafo, ünite) kaybında sistemin limit içinde kalması kuralı |
| DC / AC model | Direct Current / Alternating Current | Doğru akım (basitleştirilmiş, doğrusal) / alternatif akım (tam) şebeke modeli |

## Planlama zinciri

Aşağıdaki şema, planlamanın talep tahmininden yatırım programına kadar hangi sırayla ilerlediğini gösterir.

```
Talep tahmini  →  Üretim genişleme (ne kadar, ne tür, ne zaman)
               →  İletim genişleme (hangi hat, hangi trafo)
               →  Doğrulama: yük akışı, N-1, kısa devre, kararlılık
               →  Fayda-maliyet  →  yatırım programı
```

Zincirin halkaları:

| Halka | Ne yapar |
| --- | --- |
| Talep tahmini | Yıllar sonra ne kadar ve nerede tüketim olacağını tahmin eder |
| Üretim genişleme | Ne kadar, ne tür ve ne zaman santral gerektiğine karar verir |
| İletim genişleme | Hangi hat ve hangi trafonun yapılacağına karar verir |
| Doğrulama | Seçilen planı yük akışı, N-1, kısa devre ve kararlılık analizleriyle sınar |
| Fayda-maliyet | Planın parasal olarak değip değmediğine bakar ve yatırım programını çıkarır |

İşletme ile planlama farklı sorular sorar:

- İşletme: "elimdeki şebekeyle bugün ne yaparım"
- Planlama: "on yıl sonra yeterli olması için bugün neye karar vermeliyim"

Hat inşası 5–10 yıl sürer; yanlış karar pahalıdır ve geri alınmaz.

## Genişleme planlaması bir optimizasyon problemidir

Optimizasyon problemi, bazı kısıtları sağlarken bir maliyeti en küçük yapan çözümü arar. Aşağıdaki blok, genişleme planlamasının amaç fonksiyonunu ("en küçük") ve kısıtlarını ("öyle ki") yazar.

```
en küçük   yatırım maliyeti + işletme maliyeti + verilemeyen enerji maliyeti
öyle ki    her senaryo ve her saat için güç dengesi
           hat ve trafo sınırları (yalnız kurulmuşsa kullanılabilir)
           N-1 güvenliği
           güvenilirlik ölçütü (LOLE ≤ hedef)
           politika hedefleri (yenilenebilir payı, emisyon)
```

Bloğun satırları:

- **Amaç:** yatırım, işletme ve verilemeyen enerji maliyetlerinin toplamını en küçük yapmak. Çok az yatırım yapılırsa verilemeyen enerji maliyeti büyür; çok fazla yatırım yapılırsa yatırım maliyeti büyür. Optimum ikisinin dengesidir.
- **Güç dengesi:** her senaryoda ve her saatte üretim tüketime eşit olmalı.
- **Hat ve trafo sınırları:** bir hat veya trafo yalnız kurulmuşsa kullanılabilir ve kapasitesini aşamaz.
- **N-1 güvenliği:** tek eleman kaybında da limitler sağlanmalı.
- **Güvenilirlik ölçütü:** LOLE hedefin altında kalmalı.
- **Politika hedefleri:** yenilenebilir payı ve emisyon sınırları sağlanmalı.

### Neden karışık tam sayılı?

Karar değişkenleri ikilidir: "bu hattı kur veya kurma". Yani değişken 0 ya da 1 olur, arası olmaz. Bu yüzden problem karışık tam sayılıdır: bazı değişkenler tam sayı (kur/kurma), bazıları sürekli (akış, üretim miktarı).

Şebeke denklemleri çoğunlukla DC modelle yazılır. DC model, gerilim büyüklüklerini sabit kabul edip yalnızca aktif güç akışını doğrusal denklemlerle hesaplayan basitleştirmedir. Aday çözümler sonra AC yük akışı, kısa devre ve kararlılıkla doğrulanır.

### Zorluğu

| Zorluk | Açıklama | Nasıl yönetilir |
| --- | --- | --- |
| **Belirsizlik** | talep, yakıt fiyatı, yenilenebilirin nereye kurulacağı, politika | Tek tahmin yerine senaryolar kullanılır; iyi plan, senaryoların çoğunda kabul edilebilir olan plandır. |
| **Boyut** | yüzlerce aday, binlerce saat, onlarca senaryo | Temsilî günler ve ayrıştırma yöntemleri kullanılır. |
| **Tavuk-yumurta** | santral, hattın olduğu yere gelmek ister; hat, santralin olduğu yere yapılır | Bağlanabilir kapasite ilanı bu döngüyü yönetmenin aracıdır. |

Temsilî gün, yılın 8760 saatinin hepsi yerine yılı iyi temsil eden birkaç tipik günün hesaplanmasıdır. Ayrıştırma, büyük problemi daha küçük alt problemlere bölüp sırayla çözmektir.

## Yeterlilik ile güvenlik

Güvenilirliğin iki yüzü:

| Yüz | Sorduğu soru | Nasıl ölçülür |
| --- | --- | --- |
| **Yeterlilik (adequacy)** | talebi karşılayacak kadar kaynak var mı? | Olasılıksal ölçülür: LOLE, EENS. |
| **Güvenlik (security)** | ani bir arızaya dayanabiliyor mu? | Deterministik ölçülür: N-1. |

Olasılıksal, "ne kadar ihtimalle" diye bakmaktır. Deterministik, ihtimale bakmadan "şu arıza olursa sistem dayanmalı" diye kesin kural koymaktır.

İkisi ayrı sorudur. Kâğıt üstünde bol kapasitesi olan sistem, tek bir hat kaybında çökebilir.

> **Sade anlatım:** Yeterlilik "dolapta yeterince yemek var mı" sorusudur. Güvenlik "tencere elinden düşerse akşam yemeği yine çıkar mı" sorusudur. Biri evetse öbürü otomatik evet olmaz.

## LOLE ve EENS

| Endeks | Tanım | Birim |
| --- | --- | --- |
| LOLP | Belirli bir anda talebin karşılanamama olasılığı | — |
| LOLE | Yılda talebin karşılanamadığı beklenen süre | saat/yıl veya gün/yıl |
| EENS (EUE) | Yılda verilemeyen beklenen enerji | MWh/yıl |

LOLE sıklığı, EENS büyüklüğü söyler. Yılda 3 saatlik LOLE, 10 MW'lık açık da olabilir 5000 MW'lık açık da.

### Hedef değerler

Uluslararası tipik hedefler:

| Bölge | Tipik hedef |
| --- | --- |
| Kuzey Amerika | 10 yılda 1 gün (0,1 gün/yıl) |
| Avrupa | birçok ülkede yılda 3 saat civarı |
| Türkiye | resmî hedef değerini **doğrulamadım**; rakam söyleme |

### Hesabın iki girdisi

Hesap iki tablonun birleşimidir:

1. **Kapasite kayıp olasılık tablosu:** her ünitenin zorunlu devre dışı kalma oranı (FOR) ile, kaç MW'ın hangi olasılıkla devre dışı olacağı.
2. **Yük süre eğrisi:** yükün yılın hangi oranında hangi seviyede olduğu.

Zorunlu devre dışı kalma oranı (FOR), bir ünitenin plansız arıza nedeniyle çalışamaz durumda olduğu zamanın oranıdır. Yük süre eğrisi, yılın saatlerindeki yükleri büyükten küçüğe sıralayıp çizilen eğridir.

> **Sade anlatım:** Birinci tablo "elimde hangi olasılıkla kaç MW santral hazır" sorusunu, ikinci tablo "yılın ne kadarında ne kadar tüketim var" sorusunu cevaplar. Hazır santral tüketimden azsa o an yük kaybı olur. İki tabloyu birleştirince yük kaybının olasılığı, süresi ve enerjisi çıkar.

## Elle örnek

Üç adet 100 MW ünite, her birinin zorunlu devre dışı kalma oranı %5. Üniteler bağımsız.

"Bağımsız" demek, bir ünitenin arızalanmasının diğerinin arızalanma olasılığını değiştirmemesidir. Bu varsayım sayesinde olasılıklar çarpılabilir.

### Adım 1, kapasite kayıp tablosu (binom dağılımı)

Bu adım, 0, 1, 2 veya 3 ünitenin aynı anda devre dışı olma olasılığını ve o durumda kalan kullanılabilir kapasiteyi hesaplar. Binom dağılımı, her biri aynı olasılıkla "arızalı/sağlam" olan bağımsız denemelerde kaç tanesinin arızalı çıkacağının olasılığını verir. Çarpandaki 3, üç üniteden hangisinin (veya hangi ikisinin) arızalı olduğunun 3 farklı şekilde seçilebilmesinden gelir.

| Devre dışı ünite | Kullanılabilir | Olasılık |
| --- | --- | --- |
| 0 | 300 MW | `0,95³ = 0,857375` |
| 1 | 200 MW | `3 × 0,05 × 0,95² = 0,135375` |
| 2 | 100 MW | `3 × 0,05² × 0,95 = 0,007125` |
| 3 | 0 MW | `0,05³ = 0,000125` |

Toplam 1,000000. Kontrol tuttu.

Bu kontrol, tüm durumların olasılıkları toplamının 1 olması gerektiğini sınar; tutması tablonun eksiksiz ve doğru olduğunu gösterir.

### Adım 2, yük modeli

Bu adım, yük süre eğrisini iki basamaklı basit bir modele indirir: yılın %20'sinde 250 MW (puant), %80'inde 150 MW.

Puant, yılın en yüksek tüketim seviyesidir.

### Adım 3, puant saatleri (250 MW)

Bu adım, puant saatlerinde yük kaybı olasılığını ve ortalama açığı hesaplar.

Kullanılabilir kapasite 250'nin altındaysa yük kaybı var: 1, 2 veya 3 ünite devre dışı.

Aşağıdaki blok önce bu üç durumun olasılıklarını toplar, sonra her durumun açığını (250 − kullanılabilir kapasite: 50, 150, 250 MW) kendi olasılığıyla çarpıp toplar.

```
Olasılık       = 0,135375 + 0,007125 + 0,000125 = 0,142625
Beklenen açık  = 0,135375 × 50 + 0,007125 × 150 + 0,000125 × 250 = 7,869 MW
```

- **Olasılık satırı:** puant saatinde yük kaybı yaşanma olasılığını verir.
- **Beklenen açık satırı:** puant saatinde ortalama kaç MW eksik kaldığını verir. Açıklar: 1 ünite devre dışıyken 250 − 200 = 50 MW, 2 ünite devre dışıyken 250 − 100 = 150 MW, 3 ünite devre dışıyken 250 − 0 = 250 MW.

### Adım 4, diğer saatler (150 MW)

Bu adım, puant dışı saatlerde aynı hesabı yapar.

Yük kaybı için 2 veya 3 ünite devre dışı olmalı. Tek ünite devre dışıyken 200 MW kalır, bu da 150 MW'ı karşılar.

Aşağıdaki blok iki durumun olasılığını toplar ve açıkları (150 − 100 = 50 MW, 150 − 0 = 150 MW) olasılıklarıyla ağırlıklandırır.

```
Olasılık       = 0,007125 + 0,000125 = 0,007250
Beklenen açık  = 0,007125 × 50 + 0,000125 × 150 = 0,375 MW
```

- **Olasılık satırı:** puant dışı saatte yük kaybı olasılığını verir.
- **Beklenen açık satırı:** puant dışı saatte ortalama kaç MW eksik kaldığını verir.

### Adım 5, birleştir

Bu adım, iki yük seviyesinin sonuçlarını yılın içindeki payları (%20 ve %80) ile ağırlıklandırıp yıllık göstergeleri çıkarır. 8760, bir yıldaki saat sayısıdır (365 × 24).

```
LOLP = 0,20 × 0,142625 + 0,80 × 0,007250 = 0,034325
LOLE = 0,034325 × 8760 = 300,7 saat/yıl
EENS = 8760 × (0,20 × 7,869 + 0,80 × 0,375) = 8760 × 1,874 = 16.414 MWh/yıl
```

- **LOLP satırı:** rastgele seçilen bir saatte yük kaybı olma olasılığını verir.
- **LOLE satırı:** bu olasılığı yılın saat sayısıyla çarparak yılda beklenen yük kaybı saatini verir.
- **EENS satırı:** saat başına ortalama açığı (MW) yılın saat sayısıyla çarparak yılda verilemeyen beklenen enerjiyi (MWh) verir.

### Yorum

Kurulu güç 300 MW, puant 250 MW: yedek marjı %20. Yedek marjı, kurulu gücün puantı yüzde kaç aştığıdır: (300 − 250) / 250 = %20.

Kâğıt üstünde rahat görünür. Ama LOLE 300 saat; hedefin yüz katı.

Neden: tek bir ünite sistemin üçte biridir ve herhangi birinin devre dışı olma olasılığı %14'tür. Bu %14, Adım 3'teki 0,142625 değeridir.

**Yedek marjı tek başına güvenilirliği söylemez; ünite büyüklüğü ve sayısı belirleyicidir.**

> **Mülakatta şöyle söyle:** "Yedek marjı tek başına güvenilirliği söylemez; ünite büyüklüğü ve sayısı belirleyicidir. Üç yüz megavatlık örnekte yüzde yirmi yedek marjına rağmen LOLE üç yüz saat çıktı."

### Dördüncü ünite eklenirse

Aynı yöntem, `elle_ornekler.py` mantığıyla hesaplandı. Yani dördüncü bir 100 MW ünite (%5 FOR) eklenip Adım 1–5 tekrarlandı.

| | 3 ünite | 4 ünite |
| --- | --- | --- |
| LOLP | 0,0343 | 0,0032 |
| LOLE | 300,7 saat/yıl | 27,9 saat/yıl |
| EENS | 16.414 MWh/yıl | 1.486 MWh/yıl |

Bir ünite, verilemeyen enerjiyi on birde birine indirdi.

### Yatırım kararı

Bu adım, güvenilirlik artışını paraya çevirip yatırım maliyetiyle kıyaslar.

Verilemeyen enerjinin değeri (VOLL) 100.000 TL/MWh varsayılırsa (varsayım), dördüncü ünitenin yıllık güvenilirlik faydası `(16.414 − 1.486) × 100.000 ≈ 1,49 milyar TL`'dir.

Bu formül, dördüncü ünitenin azalttığı verilemeyen enerjiyi (MWh/yıl) her MWh'nin değeriyle çarpar.

Ünitenin yıllıklandırılmış maliyeti bunun altındaysa yatırım yapılır. Yıllıklandırılmış maliyet, toplam yatırım maliyetinin ömür boyunca eşit yıllık taksitlere çevrilmiş halidir.

Yeterlilik planlamasının özü bu karşılaştırmadır.

## Yenilenebilirin yeterliliğe katkısı

Güneş ve rüzgâr kurulu güçleri kadar güvenilirlik sağlamaz.

Ölçüsü **kapasite değeri** (ELCC): bu santrali ekleyince, LOLE'yi değiştirmeden ne kadar ek yük karşılanabilir?

- Akşam puantlı bir sistemde güneşin kapasite değeri düşüktür; pay arttıkça daha da düşer (puant, güneşin olmadığı saatlere kayar).
- Depolamanın kapasite değeri süresine bağlıdır.
- Hesap için kronolojik benzetim gerekir; yukarıdaki basit tablo yöntemi depolamayı ve korelasyonu göremez. Pratikte ardışık Monte Carlo kullanılır.

Terimler:

- **Kronolojik benzetim:** yılı saat saat, sırasıyla simüle etmek. Depolamanın şarj durumu bir önceki saate bağlı olduğu için sıranın korunması gerekir.
- **Korelasyon:** örneğin bütün güneş santrallerinin aynı anda (akşam) üretimi bırakması; basit tablo yöntemi üniteleri bağımsız kabul ettiği için bunu göremez.
- **Ardışık Monte Carlo:** rastgele arıza ve hava durumu dizileriyle yılı çok kez, saat sırasıyla simüle edip sonuçların ortalamasını almak.

> **Sade anlatım:** 1000 MW güneş eklemek, akşam puantında neredeyse hiç işe yaramıyorsa, güvenilirlik açısından 1000 MW değil çok daha az sayılır. ELCC bu "gerçekten güvenilebilen" kısmı ölçer.

## İletim yatırımının fayda-maliyeti

### Elle örnek

`13` klasöründeki örnekte hat 1–3'ün kısıtı, üretim maliyetini saatte 1.500'den 3.200 TL'ye çıkarıyordu: kısıt maliyeti 1.700 TL/saat. Bu kısıt yılda 2.000 saat bağlıyor olsun.

Kısıt maliyeti, hat kapasitesi yetmediği için ucuz santral yerine pahalı santralin çalıştırılmasından doğan ek maliyettir: 3.200 − 1.500 = 1.700 TL/saat. "Bağlıyor" demek, hattın o saatlerde kapasite sınırına dayanmasıdır.

**Adım 1, yıllık fayda.** Aşağıdaki satır, saatlik kısıt maliyetini kısıtın bağladığı saat sayısıyla çarparak kısıt kaldırılırsa yılda kazanılacak tutarı verir.

```
Yıllık kısıt maliyeti = 1.700 × 2.000 = 3,40 milyon TL
```

Kısıtı kaldıran yatırım 25 milyon TL, ömür 30 yıl, iskonto oranı %10.

İskonto oranı, gelecekteki parayı bugünkü değere çevirmek için kullanılan orandır.

**Adım 2, yatırımı yıllığa çevir.** Aşağıdaki blok, sermaye geri kazanım faktörüyle 25 milyon TL'lik yatırımı 30 yıl boyunca ödenecek eşit yıllık tutara çevirir. Formülde r iskonto oranı (0,10), n ömürdür (30 yıl); (1,10)³⁰ = 17,449 olduğu için payda 17,449 − 1 = 16,449 olur.

```
Sermaye geri kazanım faktörü = r (1+r)ⁿ / ((1+r)ⁿ − 1) = 0,10 × 17,449 / 16,449 = 0,1061
Yıllık maliyet = 25 × 0,1061 = 2,65 milyon TL
```

- **Birinci satır:** her 1 TL yatırımın yıllık eşdeğerini (0,1061 TL) verir.
- **İkinci satır:** bu faktörü yatırım tutarıyla çarparak yıllık maliyeti verir.

**Adım 3, karşılaştır.** Bu adım, yıllık faydayı yıllık maliyetle kıyaslar.

Fayda (3,40) maliyetten (2,65) büyük; oran 1,28. Yatırım yapılır.

**Adım 4, duyarlılık.** Bu adım, varsayım değişince kararın değişip değişmediğine bakar.

İskonto oranı %15 olsaydı yıllık maliyet 3,81 milyon TL'ye çıkar ve yatırım yapılmazdı. Sonuç varsayıma duyarlıdır; bu yüzden duyarlılık analizi raporun parçasıdır.

| | İskonto %10 | İskonto %15 |
| --- | --- | --- |
| Yıllık fayda | 3,40 milyon TL | 3,40 milyon TL |
| Yıllık maliyet | 2,65 milyon TL | 3,81 milyon TL |
| Karar | yatırım yapılır | yatırım yapılmaz |

Grubun iş paketlerinden biri "fayda/maliyet ve risk/etki eksenli yatırım planlaması"dır (`01/02`).

## TEİAŞ projeksiyonları (kaynaklı)

Projeksiyon, geleceğe dönük tahmindir. Bu bölümde neyin doğrulandığı, neyin doğrulanmadığı ayrı ayrı işaretlidir.

### Doğrulanan rapor listesi

**Doğrulandı** (TEİAŞ "İlgili Raporlar" sayfası, Kasım 2026): sayfada şu raporlar listelenir:

- 2026–2035 Talep Tahmin Raporu (ve önceki yıllar: 2025–2034, 2024–2033)
- Bağlanabilir Bölgesel Üretim Tesisi Kapasite Raporu 2024–2028 ve 2029–2033
- Kısa Devre Akımları (2025)

### Doğrulanan 2032 puant tahmini

**Doğrulandı** (2023–2032 Talep Tahmin Raporu):

| 2032 puant tahmini | MW |
| --- | --- |
| Düşük senaryo | 71.409 |
| Baz senaryo | 77.718 |
| Yüksek senaryo | 86.596 |

Yöntem: dağıtım şirketlerinin ve organize sanayi bölgelerinin tahminleri **trafo merkezi bazında** toplanır; düşük, baz ve yüksek olmak üzere üç senaryo üretilir.

### Doğrulanmayan bilgi

**İkincil, doğrulanmadı:** 2026–2035 raporunun baz senaryosunda yıllık ortalama talep artışının %3,7 civarında olduğu ikincil bir kaynakta geçiyor. Raporun kendisinden okumadım. Mülakattan önce raporu aç, 2035 baz puantını ve artış oranını not et.

**Kullanma:** 2035 için tek bir enerji ve puant rakamı veren internet özetleri farklı kurumların farklı yıllardaki senaryolarını karıştırıyor. Kaynağını raporun sayfasında görmediğin rakamı söyleme.

### Karşılaştırma için gerçekleşmeler

Doğrulanmış gerçekleşmeler (`01/02`):

| Gösterge | Değer |
| --- | --- |
| 2025 ani puantı | 60.414 MW |
| 2025 sonu kurulu güç | 122.518,6 MW |

Üretim tarafı: uzun dönemli üretim kapasite projeksiyonu ve Türkiye Ulusal Enerji Planı ayrı belgelerdir. Güncel hedef rakamlarını **doğrulamadım**.

### Mülakat için anlamı

Trafo merkezi bazında tahmin, **mekânsal** tahmindir; planlama yük akışının girdisidir. Mekânsal tahmin, tüketimin yalnız ne kadar olacağını değil, şebekenin hangi noktasında olacağını da söyler. Yük akışı da tam olarak bu nokta bazlı yüke ihtiyaç duyar.

Şebeke yönetmeliği planlama çalışmalarında puantın %5 üzerinin kullanılmasını ister (`01/02`).

> **Mülakatta şöyle söyle:** "TEİAŞ talep tahminini trafo merkezi bazında, üç senaryolu yayımlıyor."

## Yaygın yanlış

| Yanlış inanç | Neden yanlış |
| --- | --- |
| **"Kurulu güç puantın iki katıysa arz güvenliği tamamdır."** | Güneş gece, rüzgâr durgun havada, hidrolik kurak yılda yoktur. Kapasite değeri sorulur. |
| **"Yedek marjı %20 ise sistem güvenilirdir."** | Elle örnekte %20 marjla LOLE 300 saat çıktı. |
| **"LOLE düşükse kesinti küçüktür."** | LOLE süreyi söyler, büyüklüğü EENS söyler. |
| **"N-1 sağlanıyorsa yeterlilik de vardır."** | Biri arıza dayanımı, diğeri kaynak yeterliliğidir. |
| **"Planlama tek tahminle yapılır."** | Senaryolarla yapılır; tek tahmin neredeyse kesinlikle yanlış çıkar. |
| **"En ucuz plan en iyi plandır."** | Belirsizlik altında pişmanlığı en az olan plan aranır. |

Pişmanlık, seçilen planın, gerçekleşen senaryo için en iyi olabilecek plana göre ne kadar daha kötü sonuç verdiğidir. Pişmanlığı en az plan, hangi senaryo gerçekleşirse gerçekleşsin çok kötü duruma düşmeyen plandır.

## Panel takip sorusu

Panel, ana cevaptan sonra derine inen bu soruları sorabilir.

**Soru 1:** "İletim planında N-1'i optimizasyona nasıl sokarsın?"

> **Mülakatta şöyle söyle:** Her aday şebeke için her arıza durumunda akış kısıtı yazmak problemi patlatır. Önce arızasız çözer, çıkan planı N-1 ile denetler, ihlal eden arızaları kısıt olarak ekler, yeniden çözerim.

Bu yöntemin mantığı: arızaların çoğu zaten sorun çıkarmaz; yalnız sorun çıkaranları probleme eklemek, problemi küçük tutar.

**Soru 2:** "Talep tahmininde elektrikli araç ve ısı pompası nasıl girer?"

> **Mülakatta şöyle söyle:** Geçmişe dayalı ekonometrik model bunları göremez, çünkü geçmişte yoklar. Aşağıdan yukarı, teknoloji benimseme senaryolarıyla ayrıca eklenir; yalnız enerjiyi değil puantın saatini ve yerini de değiştirirler.

Ekonometrik model, geçmiş tüketimi ekonomik büyüme, nüfus ve fiyat gibi değişkenlerle ilişkilendiren istatistiksel modeldir. Aşağıdan yukarı tahmin, araç sayısı ve şarj alışkanlığı gibi alt kalemlerden toplam talebi kurmaktır.

## 90 saniye öncesi: konuşmanın iskeleti

Aşağıdaki konuşma, sayfanın ana fikirlerini sırayla söyler:

1. Planlama karışık tam sayılı bir eniyileme problemidir ve senaryolarla çözülür.
2. Güvenilirliğin iki yüzü: olasılıksal yeterlilik ve deterministik güvenlik (N-1).
3. LOLE ve EENS hesabı: kapasite kayıp tablosu + yük süre eğrisi.
4. Elle örnek: %20 yedek marjına rağmen LOLE 300 saat.
5. Yatırım kararı: kazanılan güvenilirlik veya azalan kısıt maliyeti ile yıllıklandırılmış maliyetin kıyası.
6. TEİAŞ: trafo merkezi bazında, üç senaryolu talep tahmini.

## 90 saniye

"Planlama, talep tahmininden başlayıp üretim ve iletim yatırımına giden, karışık tam sayılı bir eniyileme problemidir ve belirsizlik yüzünden senaryolarla çözülür. Güvenilirliğin iki yüzü vardır: yeterlilik olasılıksaldır, güvenlik ise N-1 gibi deterministik bir ölçüttür. Yeterliliği LOLE ve EENS ile ölçerim: ünitelerin devre dışı kalma olasılıklarından kapasite kayıp tablosunu kurar, yük süre eğrisiyle birleştiririm. Üç yüz megavatlık örnekte yüzde yirmi yedek marjına rağmen LOLE üç yüz saat çıktı, çünkü üniteler büyüktü. Yatırım kararını, kazanılan güvenilirliğin veya azalan kısıt maliyetinin yıllıklandırılmış yatırım maliyetiyle karşılaştırmasına bağlarım. TEİAŞ talep tahminini trafo merkezi bazında, üç senaryolu yayımlıyor."
