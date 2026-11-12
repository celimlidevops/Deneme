# Planlama

Bu sayfa, elektrik sisteminin yıllar sonrası için nasıl planlandığını anlatır. Talep tahmininden başlar, üretim ve iletimin birlikte düşünülmesine, güvenilirlik göstergelerine, fayda/maliyet hesabına, bağlantı çalışmasına, esnekliğe ve en sonda planın yazılıma dökülmesine gider.

Önce temel farkı koyalım:

- **İşletme**, bugünü limit içinde tutar.
- **Planlama**, yıllar sonra da tutacak şebekeyi ve üretimi seçer.

İkisi aynı **yük akışı** motorunu kullanır. Yük akışı, belli bir üretim ve tüketim durumunda hangi hattan ne kadar güç aktığını ve baralardaki gerilimleri hesaplayan temel analizdir. Planlamada değişen şey motor değil, belirsizlik ve yatırım kararıdır.

Bu konu doğrudan başvurduğun grubun işidir. Grubun ilk iş paketi "fayda/maliyet ve risk/etki eksenli yatırım planlaması" ve "master plan, enterkonneksiyon"dur. **Master plan**, bir şebekenin uzun dönemli yatırım yol haritasıdır. **Enterkonneksiyon**, ülkeler arası şebeke bağlantısıdır.

## Sayfa haritası

1. **Talep:** planlama tahmininin neyi içerdiği, neden senaryo gerektiği, net yük.
2. **Üretim ve iletim birlikte:** iki planın neden ayrı optimize edilmemesi gerektiği, iletim ve dağıtım adayları.
3. **Güvenilirlik:** LOLE, LOLP, EENS, ELCC; iletimde N-1 ve risk/etki; dağıtımda SAIDI, SAIFI, CAIDI.
4. **Fayda ve maliyet:** kalemler, iskonto oranı, duyarlılık.
5. **Bağlantı çalışması:** yeni santral veya büyük yük için sekiz adımlık paket.
6. **Esneklik:** yenilenebilir arttıkça neden hat yetmez.
7. **Yazılım:** planlama çalışmasını tekrarlanabilir yapmak.
8. **90 saniye:** mülakatta söyleyeceğin kısa metin.
9. **Kendini yokla:** sorular ve cevaplar.

## 1. Talep

### Kısa dönem ile planlama tahmini

**Kısa dönem tahmin** saatten haftaya kadar olan işletme tahminidir. O konu `18` klasöründe anlatılıyor.

**Planlama tahmini** ise yıllıktır. Şunları içerir:

| Tahmin edilen büyüklük | Birim veya not |
|---|---|
| Enerji | TWh (terawatt-saat), yıl boyunca tüketilen toplam |
| Puant | MW (megavat), yılın en yüksek anlık tüketimi |
| Puantın saati | Puantın günün hangi saatinde olduğu |
| Bölge dağılımı | Tüketimin ülkenin neresinde olduğu |
| Net yük | Çatı güneşi düşülmüş yük |

### Hata nerede?

Planlamada hata, nokta tahminde değil senaryodadır. **Nokta tahmin**, tek bir sayı vermek demektir ("2035'te puant şu kadar MW").

Tek bir "resmi talep" ile hat inşa etmek tehlikelidir. Talep sapınca **atıl varlık** üretir: yapılmış ama kullanılmayan hat veya trafo.

Bu yüzden en az şu senaryolar gerekir:

- düşük talep,
- orta talep,
- yüksek talep,
- elektrifikasyon senaryosu (elektrikli araç, ısı pompası).

**Elektrifikasyon**, daha önce petrol veya gazla yapılan işlerin elektriğe geçmesidir.

### Net yük ve puantın kayması

```
Net yük = talep − rüzgâr − güneş
```

Bu formül, şebekenin diğer santrallerle karşılaması gereken kısmı verir.

Güneş arttıkça puant artık akşama, güneş batımına kayabilir. "Yıllık puant yaz öğleni" alışkanlığı, güneş payı yüksek bölgede bozulur. Çünkü öğlen saatlerinde güneş tüketimin bir kısmını zaten karşılıyor.

Planlama modeli net yükün **rampasını** da taşımalıdır. Rampa, net yükün kısa sürede ne kadar hızlı yükseldiği veya düştüğüdür (örneğin güneş batarken). Sadece yıllık maksimum yetmez.

> **Sade anlatım:** Öğlen güneş bol olduğu için diğer santrallere az iş düşer. Akşam güneş bir anda çekilince diğer santrallerin çok kısa sürede devreye girmesi gerekir. Planlama bu hızlı yükselişi de görmelidir.

## 2. Üretim ve iletim birlikte

### Neden birlikte?

- **Üretim planı** enerji yetmezliğini çözer.
- **İletim planı** o enerjinin yerine ulaşmasını çözer.

İkisi ayrı optimize edilirse ucuz santral kısıtlı koridora yığılır. **Koridor**, iki bölge arasındaki hat grubudur; **kısıtlı** koridor, kapasitesi dolmak üzere olan koridordur.

Birlikte düşünmenin pratik hali bir döngüdür:

1. Üretim senaryosunu sabitle.
2. İletimi N-1'e göre tasarla. **N-1**, şebekedeki herhangi bir elemanın (hat, trafo, jeneratör) tek başına devre dışı kalmasında da limitlerin sağlanmasıdır.
3. Olmazsa üretimin yerini veya kısıntı maliyetini değiştir. **Kısıntı**, üretilebilecek enerjinin şebeke taşıyamadığı için kesilmesidir.
4. Tekrarla.

### İletim adayları

Bir iletim sorununu çözebilecek yatırım türleri:

- yeni hat,
- yeni trafo,
- kesit veya iletken değişimi (hattın telini daha kalın veya daha iyi iletkenle değiştirmek),
- reaktör/kapasitör (gerilimi düşüren veya yükselten reaktif güç ekipmanı),
- FACTS (Flexible AC Transmission Systems, Esnek Alternatif Akım İletim Sistemleri; güç elektroniğiyle akışı ve gerilimi kontrol eden cihazlar),
- gerilim katı yükseltme (154'ten 400'e, yani 154 kV'lik bölgeyi 400 kV'ye taşımak),
- bölge bara düzeni (trafo merkezindeki baraların bağlanış şeklini değiştirmek).

### Adaylar nasıl elenir ve sıralanır?

Her aday için master plan senaryo seti (`03` dosyası) koşulur.

- **Elenecek aday:** hiçbir senaryoda ihlali çözmeyendir.
- **Kalan adaylar:** fayda/maliyet ve risk ile sıralanır.

### Dağıtım adayları

Dağıtım adayı daha yereldir:

- fider (dağıtım trafo merkezinden çıkan tek bir besleme hattı),
- trafo,
- yeni TM (trafo merkezi),
- gerilim seviyesi.

**Barındırma kapasitesi** haritası, bir dağıtım noktasına limit ihlali olmadan ne kadar üretim bağlanabileceğini gösterir. Bu harita, nereye üretim bağlanacağını planlamanın önüne koyar.

## 3. Güvenilirlik

### Yeterlilik ve dört gösterge

**Yeterlilik** (adequacy) şu soruyu sorar: üretim, talebi olasılık olarak karşılıyor mu?

| Gösterge | Açılımı | Ne ölçer |
|---|---|---|
| **LOLE** | Loss of Load Expectation, Beklenen Yük Kaybı Süresi | Beklenen yük kaybı saati; yıl başına saat |
| **LOLP** | Loss of Load Probability, Yük Kaybı Olasılığı | Yükün karşılanamama olasılığı |
| **EENS** | Expected Energy Not Served, Beklenen Verilemeyen Enerji | Karşılanamayan enerji, MWh/yıl. Paraya çevrilebilir |
| **ELCC** | Effective Load Carrying Capability, Etkin Yük Taşıma Kapasitesi | Bir santralin güvenilir kapasite katkısı |

**LOLE hedefi hakkında:** Klasik hedef birçok sistemde 0,1 gün/yıl mertebesinde konuşulur. Türkiye hedefi sorulursa güncel kapasite mekanizması ve TEİAŞ (Türkiye Elektrik İletim A.Ş.) / EPDK (Enerji Piyasası Düzenleme Kurumu) belgesine bak. Ezber rakamı piyasaya mal etme.

**ELCC hakkında:**

- Rüzgârın kurulu gücünün tamamı ELCC değildir.
- Güneşin akşam puantına katkısı düşüktür.
- Kapasite hesabında isim plakasını (etiket kapasitesini) toplamak yanlıştır.
- 122 GW kurulu güç ile 60 GW puant yan yana dururken aradaki farkın bir kısmı tam olarak budur.

> **Sade anlatım:** 10 MW'lık bir güneş santrali, akşam puantında neredeyse hiç üretmiyorsa, puantı karşılama açısından 10 MW değil, çok daha az sayılır. ELCC bu "gerçekten güvenilebilen" kısmı ölçer.

### İletim güvenilirliği: N-1 ve risk/etki

İletim güvenilirliği N-1 **deterministik** kriterle yürür. Deterministik, olasılığa bakmadan "her tek arıza için sağlanmalı" diyen kural demektir.

**Olasılıklı iletim planlaması** ise şu çarpımla çalışır:

```
risk = arıza oranı × sonuç
```

Bu, grubun "risk/etki" eksenidir.

**Etki** şunlarla ölçülür:

- kesilen MW,
- kesintinin süresi,
- kritik yük (hastane gibi kesilmemesi gereken tüketim).

Önemli nokta: düşük olasılıklı ama ülkeyi bölen bir koridor, sık ama yerel bir arızadan önce gelebilir. Sıralamayı sadece olasılığa göre yapmak büyük olayı gizler.

### Dağıtım: SAIDI, SAIFI, CAIDI

Dağıtımda bu göstergeler müşteri gözündeki karşılıktır.

| Gösterge | Açılımı | Ne anlatır |
|---|---|---|
| **SAIDI** | System Average Interruption Duration Index, Sistem Ortalama Kesinti Süresi Endeksi | Müşteri başına ortalama toplam kesinti süresi |
| **SAIFI** | System Average Interruption Frequency Index, Sistem Ortalama Kesinti Sıklığı Endeksi | Müşteri başına ortalama kesinti sayısı |
| **CAIDI** | Customer Average Interruption Duration Index, Müşteri Ortalama Kesinti Süresi Endeksi | Ortalama kesinti süresi |

```
CAIDI = SAIDI / SAIFI
```

Toplam süreyi kesinti sayısına bölünce, bir kesintinin ortalama ne kadar sürdüğü çıkar.

Planlı ve plansız kesintiler ayrı tutulur.

## 4. Fayda ve maliyet

### Kalemler

| Maliyet | Fayda |
|---|---|
| Yatırım | Ertelenen başka yatırım |
| Kayıp | Kayıp düşüşü |
| Bakım | Kısıntı azalışı |
| Kamulaştırma | Kesinti azalışı |
| Kısıntı | Piyasa sıkışıklığının azalması |
| Güvenilirlik bedeli: EENS × birim kesinti maliyeti | |

**Kayıp**, hatlarda ısıya dönüşüp kaybolan enerjidir. **Piyasa sıkışıklığı**, hat kapasitesi yetmediği için ucuz elektriğin istenen yere taşınamamasıdır.

Paraya çevrilemeyen fayda (ada riski, güvenlik) ayrı satırda kalır. **İç verim oranının** içine saklanmaz. İç verim oranı, yatırımın getirisini tek bir yüzdeyle özetleyen ölçüdür. **Ada riski**, şebekenin birbirinden kopmuş parçalara bölünme riskidir.

### İskonto ve duyarlılık

**İskonto oranı**, gelecekteki paranın bugünkü değerini hesaplarken kullanılan orandır. Yüksek iskonto, uzak gelecekteki faydayı küçültür. Bu yüzden iskonto oranı uzun hattı cezalandırır.

Ömrü 40 yıl olan hattı 10 yıllık pencerede ucuz santralla kıyaslamak yöntemi bozar.

**Duyarlılık analizi** şu soruyu sorar: iskonto, talep, yakıt, kısıntı fiyatı değişince sıralama değişiyor mu? Değişmiyorsa karar **gürbüzdür** (varsayımlar değişse de sağlam kalır).

## 5. Bağlantı çalışması

Yeni santral veya büyük yük için tipik paket:

1. Bağlantı noktası alternatifleri
2. Yük akışı, yaz-kış, tam üretim ve kısmi
3. N-1 ve ortak mod
4. Kısa devre azami (ekipman) ve asgari (koruma)
5. Gerilim ve reaktif
6. Gerekirse geçici hal ve küçük sinyal
7. Koruma koordinasyonu
8. Şebeke güçlendirme bedeli ve kim öder

Birkaç terim:

- **Ortak mod:** iki elemanın aynı sebeple birlikte devre dışı kalması (örneğin aynı direği paylaşan iki devre).
- **Kısa devre azami / asgari:** en büyük kısa devre akımı ekipmanın dayanıp dayanamayacağını, en küçük kısa devre akımı korumanın arızayı görüp göremeyeceğini belirler.
- **Reaktif:** iş yapmayan ama gerilimi ayakta tutmak için gereken güç bileşeni.
- **Geçici hal:** büyük bir arızadan hemen sonraki ilk saniyelerde jeneratörlerin uyumlu dönmeye devam edip etmediği.
- **Küçük sinyal:** küçük bozulmalarda oluşan salınımların sönüp sönmediği.
- **Koruma koordinasyonu:** rölelerin doğru sırayla ve doğru sürede açması.

### Enterkonneksiyon ve HVDC

Enterkonneksiyon çalışması aynı pakete şunları ekler:

- frekans paylaşımı,
- NTC (Net Transfer Capacity, Net Transfer Kapasitesi; iki ülke arasında güvenle aktarılabilecek güç),
- bölgeler arası salınım.

**HVDC** (High Voltage Direct Current, Yüksek Gerilim Doğru Akım) ise güç kontrol modunu ekler.

## 6. Esneklik

Yenilenebilir arttıkça "yeterince hat" yetmez. **Esneklik**, sistemin üretim ve tüketimdeki hızlı değişimlere ayak uydurabilmesidir.

Esneklik kaynakları:

- depolama,
- talep kaydırma (tüketimi başka saate kaydırmak),
- hızlı termik,
- hidro,
- kısıntı,
- dış ticaret,
- sektörel bağlama (ısı, hidrojen) ileride.

Plan, esnekliği **MW ve süre** olarak ister. Bunlar ayrı ihtiyaçlardır:

| İhtiyaç | Ne demek |
|---|---|
| 15 dakikalık rampa | Kısa sürede hızlı artış veya azalış |
| 4 saatlik enerji | Saatlerce sürecek açığı kapatmak |
| Anlık atalet | Dönen kütlenin frekansın ani değişimine direnci |

Depolamayı sadece enerji arbitrajı diye modellemek, şebeke hizmetini kaçırır. **Enerji arbitrajı**, ucuzken depolayıp pahalıyken satmaktır.

## 7. Yazılım

Planlama çalışması kişiye bağlı bir PowerFactory dosyası olarak kalırsa tekrar edilemez. **PowerFactory**, güç sistemi analiz yazılımıdır.

Tekrarlanabilir iş şunlardan oluşur:

- versiyonlu şebeke modeli,
- senaryo tablosu,
- betik (Python API; API = Application Programming Interface, Uygulama Programlama Arayüzü),
- sonuç veri tabanı,
- aynı limit kontrolü.

Grubun ürün refleksi budur. Danışmanlık projesi de, sonunda TEİAŞ veya dağıtım şirketinin kendi koşacağı araca yaklaştığı ölçüde değerlidir.

> **Mülakatta şöyle söyle:** "Çalışmayı betiğe bağladım, modeli kilitledim, sonucu tabloda karşılaştırdım." Bu cümle, analiz ile yazılımı birleştirir.

### 90 saniyelik metin için not

Aşağıdaki metin sayfanın sözlü özetidir. İçindeki kısaltmalar yukarıda açıldı: N-1 (Bölüm 2), ELCC ve EENS (Bölüm 3). "Puantın yüzde 5 üzerinde" ifadesi, şebeke yönetmeliğinin planlama yükü kuralıdır: planlama, beklenen en yüksek tüketimin yüzde 5 fazlasıyla yapılır.

## 90 saniye

"Planlama, puantın yüzde 5 üzerinde N-1 ile yılları seçer. Kurulu gücü toplamak yeterlilik değildir; ELCC ve EENS bakılır. İletimde master plan senaryoları, aday yatırımı eler. Sıralama fayda, maliyet ve düşük olasılıklı büyük risktir. Yenilenebilirde net yük rampası ve esneklik süresi gerekir. Çalışmayı betik ve kilitli model ile tekrarlanabilir bırakırım."

## Kendini yokla

Önce cevabı kapat, kendin söyle, sonra kontrol et.

1. **Planlama tahmini neleri içerir?**
   Enerji (TWh), puant (MW), puantın saati, bölge dağılımı, çatı güneşi düşülmüş net yük.

2. **Neden tek "resmi talep" ile plan yapılmaz?**
   Talep sapınca atıl varlık üretir. En az düşük, orta, yüksek talep ve elektrifikasyon (araç, ısı pompası) senaryosu gerekir.

3. **Net yük nedir ve güneş arttıkça puanta ne olur?**
   Net yük = talep − rüzgâr − güneş. Puant akşam güneş batımına kayabilir; model net yükün rampasını da taşımalıdır.

4. **Üretim ve iletim ayrı optimize edilirse ne olur?**
   Ucuz santral kısıtlı koridora yığılır.

5. **Hangi iletim adayı elenir?**
   Hiçbir senaryoda ihlali çözmeyen. Kalanlar fayda/maliyet ve risk ile sıralanır.

6. **ELCC neden önemli? Kurulu güç ile puant örneği?**
   Santralin güvenilir kapasite katkısını verir; isim plakasını toplamak yanlıştır. 122 GW kurulu güç ile 60 GW puant arasındaki farkın bir kısmı budur.

7. **LOLE hedefi sorulursa ne dersin?**
   Klasik hedef birçok sistemde 0,1 gün/yıl mertebesinde konuşulur; Türkiye için güncel kapasite mekanizmasına ve TEİAŞ/EPDK belgesine bakarım.

8. **Risk sıralamasını sadece olasılığa göre yapmak neden yanlış?**
   Düşük olasılıklı ama ülkeyi bölen koridor, sık ama yerel arızadan önce gelebilir; sadece olasılık büyük olayı gizler.

9. **CAIDI nasıl hesaplanır?**
   CAIDI = SAIDI/SAIFI; ortalama kesinti süresi.

10. **Güvenilirlik bedeli nasıl hesaplanır, paraya çevrilemeyen fayda nereye yazılır?**
    EENS × birim kesinti maliyeti. Paraya çevrilemeyen fayda ayrı satırda kalır, iç verim oranına saklanmaz.

11. **Bağlantı çalışmasının sekiz adımı nedir?**
    Bağlantı noktası alternatifleri; yük akışı (yaz-kış, tam ve kısmi üretim); N-1 ve ortak mod; kısa devre azami ve asgari; gerilim ve reaktif; gerekirse geçici hal ve küçük sinyal; koruma koordinasyonu; güçlendirme bedeli ve kim öder.

12. **Esneklik hangi boyutlarda istenir?**
    MW ve süre: 15 dakikalık rampa, 4 saatlik enerji, anlık atalet ayrı ayrı.
