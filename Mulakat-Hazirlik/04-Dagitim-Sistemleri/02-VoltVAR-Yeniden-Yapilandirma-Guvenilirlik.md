# Volt/VAR, yeniden yapılandırma, güvenilirlik

Bu sayfa dört konuyu anlatır: dağıtımda gerilimi ve reaktif gücü birlikte ayarlayan Volt/VAR optimizasyonu, açık noktaları değiştirerek şebekeyi yeniden yapılandırma, kayıp azaltma ve kesinti süresini ile sıklığını ölçen güvenilirlik endeksleri.

## Volt/VAR optimizasyonu

Dağıtım şirketi, fider boyunca her müşterinin gerilimini izin verilen bant içinde tutmak zorundadır. Fider, trafo merkezinden çıkan tek bir dağıtım hattıdır.

Şirketin elinde üç ayar vardır:

| Cihaz | Ne yapar | Kısıtı |
| --- | --- | --- |
| Yük altında kademe değiştirici (OLTC), hat regülatörü | Gerilimi bütün fider için kaydırır | Ayrık kademe, mekanik aşınma, günde sınırlı işlem |
| Kapasitör bankası | Reaktif üretir, gerilimi yükseltir, kaybı düşürür | Aç-kapa, hafif yükte aşırı gerilim |
| Evirici reaktif gücü | Hem üretir hem tüketir, hızlı ve sürekli | MVA sınırı; reaktif verirken aktif güçten yiyebilir |

Evirici, güneş panelinin doğru akımını şebekenin alternatif akımına çeviren güç elektroniği cihazıdır. MVA sınırı, eviricinin toplam (aktif ve reaktif birlikte) güç kapasitesidir.

### Problem tanımı

Volt/VAR optimizasyonu (VVO), bu üç cihazı birlikte ayarlayan problemdir.

| Parça | İçeriği |
| --- | --- |
| Amaç | Kayıp en az, gerilim sapması en az, kademe işlemi en az. Bazen de CVR (gerilim düşürerek tasarruf): gerilimi bandın alt yarısında tutarak tüketimi azaltmak |
| Kısıt | Her barada gerilim bandı, hat ve trafo akım sınırı, cihaz sınırları |
| Değişken | Kademe konumu (tam sayı), kapasitör durumu (0/1), evirici reaktifi (sürekli) |

Matematik sınıfı: karışık tam sayılı doğrusal olmayan problem. Yani bazı değişkenler tam sayı, bazıları süreklidir ve denklemler doğrusal değildir.

Pratikte iki yol izlenir:

- **Kural tabanlı yerel kontrol:** Her cihaz kendi gerilimine bakar.
- **Merkezi optimizasyon:** DMS (dağıtım yönetim sistemi) veya ADMS (gelişmiş dağıtım yönetim sistemi) içinde, dakikalar mertebesinde çözülür.

### Zaman ölçeği

Zaman ölçeği ayrımı önemlidir:

- Kademe ve kapasitör yavaştır, saatlik planlanır.
- Evirici hızlıdır, bulut geçişine saniyeler içinde tepki verir.

İkisi aynı gerilimi düzeltmeye çalışırsa birbirini kovalar. Buna avlanma denir.

Çözüm: Yavaş cihaza ölü bant ve gecikme, hızlı cihaza eğim verilir. Ölü bant, cihazın tepki vermediği küçük gerilim aralığıdır. Eğim, eviricinin gerilim sapmasıyla orantılı tepki vermesidir.

> **Sade anlatım:** Aynı odada iki kişi termostatı ayarlıyorsa oda hiç dengeye gelmez. Biri yavaş ve sabırlı, diğeri hızlı ama ölçülü davranırsa sorun çözülür.

### Elle örnek: evirici neden reaktif **tüketir**

Durum: Öğlen, fider sonunda güneş 2 MW üretiyor, yük 0,5 MW. Net 1,5 MW geriye akıyor. Fider `R = 2 Ω`, `X = 2 Ω`, 34,5 kV.

**Adım 1.** Bu adım, eviricinin reaktif desteği yokken gerilim değişimini bulur. Geriye akan güç negatif P olarak formüle girer:

```
ΔV ≈ (P R + Q X) / V = (−1,5 × 2 + 0) / 34,5 = −0,087 kV
```

Eksi işaret, gerilimin fider sonunda **yükseldiğini** söyler: +%0,25. Küçük görünür. Alçak gerilim tarafında ve uzun kırsal fiderde aynı etki birkaç yüzdeye çıkar.

**Adım 2.** Bu adım, evirici 1 Mvar reaktif tükettiğinde (`Q = +1`) gerilimin ne kadar düzeldiğini gösterir:

```
ΔV = (−1,5 × 2 + 1 × 2) / 34,5 = −0,029 kV
```

**Sonuç.** Yükselme üçte birine indi. Bedeli: fiderden fazladan 1 Mvar aktı, kayıp arttı. Volt/VAR optimizasyonunun özü bu takastır.

## Şebekenin yeniden yapılandırılması

Dağıtım şebekesi halka olarak kurulur, **radyal** işletilir. Radyal, her yükün kaynağa tek yoldan bağlı olması demektir.

Halkayı açık tutan anahtara **normalde açık nokta** denir. Yeniden yapılandırma, hangi anahtarın açık olacağını yeniden seçmektir.

### Neden yapılır

1. Kaybı azaltmak ve yükü dengelemek.
2. Arızadan sonra sağlam kısmı başka fiderden beslemek (FLISR: arızayı bul, ayır, yeniden enerjilendir).
3. Bakım için bir kesimi boşaltmak.
4. Dağıtık üretimin barındırma kapasitesini artırmak. Barındırma kapasitesi, fidere limitler bozulmadan bağlanabilecek üretimdir.

### Kısıtlar

- Şebeke radyal kalmalı: her yük tek yoldan beslenmeli, halka kalmamalı.
- Kimse enerjisiz kalmamalı.
- Gerilim ve akım sınırları korunmalı.
- Koruma koordinasyonu bozulmamalı.

### Yazılımcı gözüyle

Bu, bir çizgede **kapsayan ağaç** seçme problemidir. Kapsayan ağaç, bütün düğümlere ulaşan ama hiç döngü içermeyen kenar kümesidir.

`n` anahtar için `2ⁿ` durum vardır; kombinatoryal olarak patlar.

Yöntemler:

- **Dal değiştirme sezgiseli:** Bir anahtarı kapat, oluşan halkada en az akım taşıyan yeri aç.
- **Karışık tam sayılı konik program.**
- **Meta-sezgiseller.**

### Elle örnek: yük dengeleme kaybı düşürür

Durum: Aynı trafo merkezinden çıkan iki fider var. Her birinin direnci faz başına 1 Ω.

**Önce.** Bu satır dengesiz durumdaki üç fazlı kaybı hesaplar. Biri 300 A, diğeri 100 A taşıyor:

`3 × (300² + 100²) × 1 = 300 kW`

**Sonra.** Bu satır, açık nokta kaydırılıp iki fider de 200 A taşıyınca kaybı hesaplar:

`3 × 2 × 200² = 240 kW`

**Sonuç.** Toplam akım aynı kaldı, kayıp %20 düştü. Neden: kayıp akımın karesiyle gider. Kareler toplamı, dağılım eşitken en küçüktür.

## Kayıp azaltma

Kayıp iki türdür:

| Tür | İçeriği | Nasıl ele alınır |
| --- | --- | --- |
| **Teknik kayıp** | İletkende `I²R`, trafoda demir (yükten bağımsız) ve bakır (yüke bağlı) kaybı | Mühendislik önlemleriyle azaltılır |
| **Teknik olmayan kayıp** | Kaçak kullanım, sayaç ve faturalama hatası | Mühendislik değil tespit problemidir; sayaç verisi analitiği burada devreye girer |

Teknik kaybı azaltma yolları, ucuzdan pahalıya:

1. Yeniden yapılandırma
2. Faz dengeleme
3. Reaktif kompanzasyon
4. Gerilim seviyesini yükseltme
5. İletken kesitini büyütme
6. Trafoyu yüke yaklaştırma
7. Verimli trafo

## Güvenilirlik endeksleri

| Endeks | Açılımı | Formül | Anlam |
| --- | --- | --- | --- |
| SAIFI | Sistem ortalama kesinti sıklığı endeksi | Kesintiden etkilenen müşteri sayısı toplamı / toplam müşteri | Ortalama müşteri yılda kaç kez kesinti yaşar |
| SAIDI | Sistem ortalama kesinti süresi endeksi | Müşteri kesinti süreleri toplamı / toplam müşteri | Ortalama müşteri yılda kaç dakika enerjisiz kalır |
| CAIDI | Müşteri ortalama kesinti süresi endeksi | SAIDI / SAIFI | Bir kesinti ortalama kaç dakika sürer |
| ENS | Verilemeyen enerji | Kesilen güç × süre | Verilemeyen enerji |

Türkiye'de EPDK (Enerji Piyasası Düzenleme Kurumu) aynı kavramları Türkçe kısaltmalarla izler:

- OKSÜRE (ortalama kesinti süresi)
- OKSIK (ortalama kesinti sıklığı)

Güncel hedef değerleri ve tazminat kurallarını **doğrulamadım**.

> **Mülakatta şöyle söyle:** Sorulursa Elektrik Dağıtımı ve Perakende Satışına İlişkin Hizmet Kalitesi Yönetmeliği'ne atıf yap, rakam söyleme.

### Elle örnek

Durum: 1000 müşterili fider, yılda iki kesinti.

- Kesinti A: 200 müşteri, 90 dakika
- Kesinti B: 500 müşteri, 30 dakika

Aşağıdaki üç satırda ilki etkilenen müşterileri toplayıp sıklığı, ikincisi müşteri × dakikayı toplayıp süreyi bulur. Üçüncüsü, ikisini bölerek bir kesintinin ortalama süresini verir.

```
SAIFI = (200 + 500) / 1000 = 0,70 kesinti/müşteri
SAIDI = (200 × 90 + 500 × 30) / 1000 = 33.000 / 1000 = 33 dakika/müşteri
CAIDI = 33 / 0,70 = 47,1 dakika
```

### Yorum

- SAIFI'yi koruma ve ayırma düşürür: daha az müşteri etkilenir.
- SAIDI'yi otomasyon ve yeniden yapılandırma düşürür: enerji daha çabuk geri gelir.
- CAIDI tek başına yanıltıcıdır. Kısa kesintileri otomasyonla ortadan kaldırırsan geriye uzun olanlar kalır ve CAIDI **yükselir**. Oysa hizmet iyileşmiştir.

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"Dağıtım şebekesi halka çalışır."** | Halka kurulur, radyal işletilir. Koruma bu varsayıma göre ayarlıdır. |
| **"Güneş çok üretince gerilim reaktif yüzünden yükselir."** | Dağıtımda R büyüktür; neden aktif güçtür. |
| **"Kapasitör her zaman kaybı düşürür."** | Hafif yükte aşırı kompanzasyon kaybı ve gerilimi artırır. |
| **"CAIDI düştüyse hizmet iyileşmiştir."** | Yukarıdaki gibi ters de olabilir. SAIDI ve SAIFI birlikte okunur. |
| **"Yeniden yapılandırma bir optimizasyon sorusudur, koruma ayrı."** | Besleme yönü değişince kısa devre akımı ve röle koordinasyonu değişir. |

## Panel takip sorusu

"Volt/VAR için amaç fonksiyonun ne olur?"

> **Mülakatta şöyle söyle:** "Kayıp ve gerilim sapmasının ağırlıklı toplamı, artı kademe işlemine ceza. Ağırlıkları işletmecinin önceliği belirler; tek doğru yoktur."

"Yeniden yapılandırmada radyalliği nasıl garanti edersin?"

> **Mülakatta şöyle söyle:** "Kapalı dal sayısı = bara sayısı − besleme noktası sayısı ve şebeke bağlı olmalı. Formülasyonda tek mal akışı veya kapsayan ağaç kısıtlarıyla yazılır."

Tek mal akışı: her yüke kaynaktan sanal bir "mal" gönderilir. Mal her yüke ulaşabiliyorsa şebeke bağlıdır.

Aşağıdaki metin, bu konu sorulduğunda 90 saniyede söyleyeceğin özettir.

## 90 saniye

"Dağıtımda gerilimi üç cihaz yönetir: kademe değiştirici, kapasitör ve eviricinin reaktif gücü. Volt/VAR optimizasyonu bunları kayıp, gerilim sapması ve kademe aşınması arasında dengeleyen karışık tam sayılı bir problemdir; yavaş ve hızlı cihazların birbirini kovalamaması için zaman ölçekleri ayrılır. Yeniden yapılandırma, radyal kalmak şartıyla açık noktaları yeniden seçmektir; kaybı düşürür ve arıza sonrası beslemeyi geri getirir. Hizmet kalitesini SAIFI ile sıklık, SAIDI ile süre olarak ölçerim; CAIDI ikisinin oranıdır ve tek başına yanıltabilir."
