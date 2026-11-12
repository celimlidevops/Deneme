# Türkiye elektrik piyasası

Bu sayfa Türkiye elektrik piyasasının ana parçalarını kaynak etiketleriyle anlatır. Sayfada sık geçen kısaltmalar:

| Kısaltma | Açılımı | Kısaca |
| --- | --- | --- |
| GÖP | Gün Öncesi Piyasası | Ertesi günün saatlik enerji ticareti |
| GİP | Gün İçi Piyasası | Teslimata yakın düzeltme ticareti |
| DGP | Dengeleme Güç Piyasası | Gerçek zamanlı denge, TEİAŞ talimatları |
| PTF | Piyasa Takas Fiyatı | GÖP'te oluşan saatlik fiyat |
| SMF | Sistem Marjinal Fiyatı | DGP'de oluşan fiyat |
| EPİAŞ | Enerji Piyasaları İşletme A.Ş. | Piyasa işletmecisi |
| EPDK | Enerji Piyasası Düzenleme Kurumu | Düzenleyici |
| TEİAŞ | Türkiye Elektrik İletim A.Ş. | Sistem ve iletim işletmecisi |
| DUY | Elektrik Piyasası Dengeleme ve Uzlaştırma Yönetmeliği | Dengeleme ve uzlaştırma kuralları |

## Kaynak etiketleri

Sayfadaki bilgiler güvenilirliğine göre üç etiket taşır:

| Etiket | Anlamı | Mülakatta |
| --- | --- | --- |
| **Doğrulandı** | EPİAŞ veya EPDK'nın kendi sayfasında Kasım 2026'da okundu. | Rahatça söyle. |
| **İkincil** | Resmî olmayan kaynak veya genel sektör bilgisi. | "Bildiğim kadarıyla" de. |
| **Doğrula** | Hafızadan yazıldı. | Mülakattan önce resmî kaynaktan kontrol et. |

Mülakattan önce bakılacak yerler:

- EPİAŞ Şeffaflık Platformu (güncel PTF ve SMF)
- EPİAŞ piyasa sayfaları
- EPDK Kurul Kararları
- Elektrik Piyasası Dengeleme ve Uzlaştırma Yönetmeliği (DUY)

## Kim ne yapar

| Kurum | Görev |
| --- | --- |
| EPDK | Düzenler: lisans, tarife, yönetmelik, fiyat sınırları |
| EPİAŞ | Piyasa işletmecisi: gün öncesi, gün içi, vadeli piyasalar ve uzlaştırma |
| TEİAŞ | Sistem işletmecisi: dengeleme güç piyasası, yan hizmetler, iletim |
| Dağıtım şirketleri | Dağıtım şebekesi işletmesi |
| Görevli tedarik şirketleri ve tedarikçiler | Perakende satış |

Bu ayrım mülakatta işe yarar.

> **Mülakatta şöyle söyle:** EPİAŞ **ticareti**, TEİAŞ **fiziği** yönetir.

## Zaman çizgisi

Aşağıdaki blok, elektriğin teslimattan ne kadar önce hangi piyasada işlem gördüğünü sırayla gösterir.

```
Yıllar–aylar önce     İkili anlaşmalar, vadeli piyasalar
Bir gün önce          GÖP   →  saatlik PTF
Gün içinde            GİP   →  sürekli ticaret, teslimata 1 saat kalana kadar
Gerçek zaman          DGP   →  TEİAŞ talimatları, SMF
Sonrası               Uzlaştırma: dengesizlikler fiyatlanır
```

## Gün Öncesi Piyasası (GÖP)

GÖP, ertesi günün her saati için alış ve satış tekliflerinin toplandığı ve tek fiyatla eşleştirildiği piyasadır.

### Fiyat bölgesi ve PTF

- Türkiye **tek fiyat bölgesidir**: bütün ülke için saatlik tek fiyat oluşur. Şebeke kısıtı eşleştirmede dikkate alınmaz. (İkincil; yapısal olarak yıllardır böyledir.)
- Çıkan fiyat **PTF**'dir: Piyasa Takas Fiyatı. Arz ve talep eğrilerinin kesiştiği fiyattır.
- Kabul edilen bütün teklifler aynı fiyattan uzlaştırılır. Buna marjinal fiyatlama denir.

### Fiyat sınırları

- **Doğrulandı:** asgari fiyat 0, azami fiyat **4.500 TL/MWh**. Bu değer 4 Nisan 2026'dan itibaren geçerlidir; dayanağı EPDK'nın 2 Nisan 2026 tarihli ve 14459 sayılı Kurul Kararı'dır.
- Asgari fiyat sıfır olduğu için Türkiye'de **negatif fiyat oluşmaz**.

Önceki azami değerler:

| Tarih | Azami fiyat (TL/MWh) |
| --- | --- |
| Haziran 2024 | 3.000 |
| Nisan 2025 | 3.400 |
| 4 Nisan 2026'dan itibaren | 4.500 |

Azami fiyat sık güncellenir. Mülakatta rakam söylerken tarihini de söyle.

> **Mülakatta şöyle söyle:** "Nisan 2026 kararıyla 4.500 lira."

### Teklif süreci

- **İkincil:** teklifler 12.30'a kadar verilir, sonuçlar 14.00 civarında kesinleşir. Saatleri doğrula.
- Teklif türleri: saatlik, blok ve esnek teklifler. (İkincil.)

### Elle örnek 1: liyakat sırası ve PTF

Liyakat sırası (merit order), satış tekliflerinin ucuzdan pahalıya dizilmesidir. Talebi karşılayan son (en pahalı kabul edilen) teklif fiyatı belirler.

**Adım 1: teklifleri sırala ve birikimli miktarı yaz.** Bu adım, her fiyat düzeyine kadar toplam ne kadar arz olduğunu gösterir.

Bir saat için satış teklifleri (fiyata göre sıralı):

| Kaynak | Miktar | Fiyat (TL/MWh) | Birikimli |
| --- | --- | --- | --- |
| Akarsu, rüzgâr | 1000 MW | 0 | 1000 |
| Linyit | 800 MW | 1500 | 1800 |
| Doğal gaz | 600 MW | 2500 | 2400 |
| Eski doğal gaz | 400 MW | 4000 | 2800 |

Talep 2100 MW ve fiyattan bağımsız.

**Adım 2: talebin birikimli eğride nereye düştüğünü bul.** Bu adım, marjinal teklifi ve dolayısıyla PTF'yi belirler.

```
2100 MW, birikimli 1800 ile 2400 arasına düşer   →   marjinal teklif: doğal gaz
PTF = 2500 TL/MWh
```

Rüzgâr ve linyit de 2500'den uzlaştırılır. Eski doğal gaz santrali çalışmaz.

**Adım 3: sıfır fiyatlı yeni arz ekle ve sırayı yeniden kur.** Bu adım, yenilenebilirin fiyatı nasıl değiştirdiğini gösterir.

Şimdi aynı saate 400 MW güneş, sıfır fiyatla giriyor. Birikimli miktarlar 400 MW kayar: 1400, 2200, 2800, 3200.

**Adım 4: talebin yeni yerini bul.** Bu adım, yeni marjinal teklifi ve yeni PTF'yi verir.

```
2100 MW, 1400 ile 2200 arasına düşer   →   marjinal teklif: linyit
PTF = 1500 TL/MWh
```

400 MW güneş, fiyatı 1000 TL/MWh düşürdü. Buna **liyakat sırası etkisi** denir.

Cem Şahin'in 2021 makalesi (`01/03`) yenilenebilirin Türkiye elektrik piyasalarındaki gelişimini ele alır. Özetini okurken bu etkiye nasıl değindiğine bak.

## Gün İçi Piyasası (GİP)

GÖP kapandıktan sonra tahminler değişir: rüzgâr farklı eser, bir santral arızalanır. Katılımcılar pozisyonlarını GİP'te düzeltir.

- **Doğrulandı:** GİP **sürekli ticaret** yöntemiyle çalışır. Teklifler eşleştikçe işlem gerçekleşir; tek fiyat yoktur.
- **Doğrulandı:** ertesi günün kontratları bir önceki gün 18.00'de açılır.
- **Doğrulandı:** **kapı kapanışı teslimattan 1 saat öncedir.** (Kapı kapanışı, o saat için artık işlem yapılamayan andır.)
- **Doğrulandı:** kontratlar saatliktir.
- Fiyat sınırlarının GÖP sınırlarıyla ilişkisi için güncel kurala bak. (Doğrula.)

GİP'in şebeke açısından anlamı: yenilenebilir tahmin hatasının büyük kısmı burada, piyasa katılımcıları arasında kapanır. Kapanmayan kısım gerçek zamanda TEİAŞ'a kalır.

## Dengeleme Güç Piyasası (DGP)

Gerçek zamanda üretim ile tüketim eşit olmak zorundadır. Aradaki farkı TEİAŞ Milli Yük Tevzi Merkezi (MYTM) kapatır.

- Santraller, 15 dakika içinde yerine getirebilecekleri yük alma ve yük atma tekliflerini verir.
- Talimatlar fiyat sırasına göre verilir; oluşan fiyat **SMF**'dir: Sistem Marjinal Fiyatı.
- **Doğrulandı:** DGP'de de asgari 0, azami 4.500 TL/MWh sınırı geçerlidir (aynı Kurul Kararı).

| Talimat | Anlamı | Ne zaman |
| --- | --- | --- |
| **YAL (yük alma)** | Üretimi artırma talimatı | Sistemde enerji açığı varsa |
| **YAT (yük atma)** | Üretimi azaltma talimatı | Sistemde enerji fazlası varsa |

### Yön kuralı

Yön kuralı ikincil bilgidir ama mantığı sağlamdır. Aşağıdaki blok, sistemin açık veya fazla vermesine göre hangi talimatın verildiğini ve SMF'nin PTF'ye göre nereye düştüğünü gösterir.

```
Sistem açık verdi   →  YAL talimatları  →  SMF ≥ PTF
Sistem fazla verdi  →  YAT talimatları  →  SMF ≤ PTF
```

### Talimat etiketleri

**İkincil; doğrula.** Talimatlar veriliş nedenine göre etiketlenir:

| Etiket | Veriliş nedeni |
| --- | --- |
| 0 | Enerji dengesi |
| 1 | **İletim kısıtı** |
| 2 | Yan hizmet (yedek oluşturma) |

SMF'yi yalnızca 0 etiketli talimatlar belirler.

### Bu ayrım neden önemli

Bu ayrım, ilan açısından en önemli noktadır.

1. GÖP şebekeyi görmediği için, piyasanın ürettiği program fiziksel olarak taşınamayabilir.
2. TEİAŞ kısıtı 1 etiketli talimatlarla çözer: kısıtın bir tarafında üretimi düşürür, diğer tarafında artırır.
3. Bunun maliyeti vardır. Hangi talimatın verileceğini bulmak bir **güvenlik kısıtlı yeniden dağıtım** problemidir.
4. YTBS'nin (Yük Tevzi Bilgi Sistemi) analiz modülleri bu kararın arkasındaki hesaptır.

## Dengesizlik uzlaştırması

Her katılımcının programı ile gerçekleşeni arasındaki fark dengesizliktir ve cezalı fiyatlanır.

**Doğrula** (hafızadan; DUY'un güncel metnine bak). Aşağıdaki blok iki yöndeki dengesizliğin hangi fiyattan ödendiğini gösterir.

```
Pozitif dengesizlik (fazla üretim / eksik tüketim):  min(PTF, SMF) × 0,97 üzerinden ödeme ALIR
Negatif dengesizlik (eksik üretim / fazla tüketim):  max(PTF, SMF) × 1,03 üzerinden ödeme YAPAR
```

Katsayılar değişmiş olabilir. Mantık değişmez: dengesizlik her iki yönde de piyasada işlem yapmaktan **kötü** fiyatlanır. Böylece katılımcı iyi tahmin yapmaya ve GİP'te pozisyon kapatmaya özenir.

> **Sade anlatım:** Fazla üretirsen fazlanı ucuz olan fiyatın biraz altından satarsın. Eksik üretirsen eksiğini pahalı olan fiyatın biraz üstünden alırsın. İki durumda da tahmini tutturmak daha kârlıdır.

### Elle örnek 2: tahmin hatasının maliyeti

Bir rüzgâr santrali GÖP'te bir saat için 100 MWh sattı; 80 MWh üretti. PTF 2500, SMF 3200 TL/MWh (sistem açık). Yukarıdaki katsayılar kullanılır.

Aşağıdaki blokta her satır bir adımdır:

1. **GÖP geliri:** satılan miktar PTF ile çarpılır; santralin piyasadan aldığı paradır.
2. **Negatif dengesizlik:** eksik kalan 20 MWh, PTF ile SMF'nin büyüğü (3200) ve 1,03 ile çarpılır; santralin ödediği cezadır.
3. **Net:** gelirden ceza düşülür.

```
GÖP geliri           = 100 × 2500 = 250.000 TL
Negatif dengesizlik  = 20 MWh × max(2500, 3200) × 1,03 = 20 × 3296 = 65.920 TL (öder)
Net                  = 184.080 TL
```

**Karşılaştırma adımı:** doğru tahminle 80 MWh satsaydı 200.000 TL kazanırdı. Bu adım, hatanın gerçek bedelini ortaya çıkarır.

- Tahmin hatasının bedeli 15.920 TL.
- Yani eksik kalan megavat-saat başına 796 TL.

Güneş ve rüzgâr tahmin projelerinin (RİTM, TEİAŞ güneş tahmini) ekonomik gerekçesi bu sayıdadır. RİTM, rüzgâr üretimi izleme ve tahmin sistemidir. Sistem tarafındaki gerekçe ise yedek ihtiyacıdır.

## Diğer mekanizmalar

Her biri bir cümleyle; hepsi ikincil.

| Mekanizma | Açıklama |
| --- | --- |
| **İkili anlaşmalar** | Taraflar arasında serbestçe yapılır, EPİAŞ'a bildirilir. Hacmin önemli kısmı buradadır. |
| **Vadeli Elektrik Piyasası (VEP)** | EPİAŞ'ın işlettiği, fiziksel teslimatlı vadeli piyasa. |
| **YEKDEM** (Yenilenebilir Enerji Kaynakları Destekleme Mekanizması) | Sabit fiyat garantisi. Eski santraller dolar bazlı, yenileri TL bazlı ve güncellemeli. |
| **YEKA** (Yenilenebilir Enerji Kaynak Alanı) | Yenilenebilir enerji kaynak alanı yarışmaları. |
| **Yan hizmetler** | Primer ve sekonder frekans kontrol kapasitesi TEİAŞ tarafından ihaleyle tedarik edilir. |
| **Kapasite mekanizması** | Arz güvenliği için bazı santrallere kapasite ödemesi. |
| **Lisanssız üretim** | Mayıs 2026'dan itibaren saatlik mahsuplaşma (`17/02`). |

## Piyasa ile şebekenin buluştuğu yerler

1. **Kısıt yönetimi:** tek bölgeli piyasa + fiziksel kısıt = yeniden dağıtım (1 etiketli talimat).
2. **Yedek boyutlandırma:** tahmin hatası ve en büyük ünite kaybı kadar yedek.
3. **Atalet ve gerilim:** piyasa bunları fiyatlamaz. Sistem işletmecisi bazı senkron santralleri piyasa dışı gerekçeyle devrede tutar.
4. **Enterkonneksiyon kapasitesi:** sınır kapasitesi ihaleyle tahsis edilir (`03/03`: NTC ve ATC, yani net transfer kapasitesi ve kullanılabilir transfer kapasitesi).

"Grubun çalışma alanlarından biri piyasa ile şebekeyi birlikte ele alan enerji ekonomisi" (`01/02`). Yukarıdaki dört madde bunun somut halidir.

## Yaygın yanlış

| Yanlış | Doğrusu |
| --- | --- |
| **"PTF ile SMF aynı şeydir."** | PTF gün öncesi piyasasının, SMF gerçek zamanlı dengelemenin fiyatıdır. |
| **"EPİAŞ dengelemeyi yapar."** | Dengeleme güç piyasasını TEİAŞ işletir; EPİAŞ uzlaştırır. |
| **"GÖP şebeke kısıtını dikkate alır."** | Tek bölgedir; kısıt sonradan çözülür. |
| **"Türkiye'de de negatif fiyat oluşuyor."** | Asgari fiyat sıfırdır. |
| **"GİP de GÖP gibi tek fiyatlıdır."** | Sürekli ticarettir; her eşleşmenin kendi fiyatı vardır. |
| **"Azami fiyat sabittir."** | Haziran 2024'ten bu yana üç ayrı değer aldı (3.000, 3.400, 4.500). Tarihiyle söyle. |
| **"Yenilenebilir fiyatı düşürür, o halde sistem maliyeti de düşer."** | Enerji fiyatı düşer; dengeleme, yedek ve şebeke maliyeti artabilir. |

## Panel takip sorusu

**"Türkiye bölgesel veya noktasal fiyata geçse ne değişir?"**

> **Mülakatta şöyle söyle:** Kısıt, gün öncesi fiyatına yansır; kısıtlı bölgede fiyat yükselir, yeniden dağıtım ihtiyacı azalır, yatırım sinyali yerelleşir. Bedeli: piyasa derinliği azalır, bölgesel piyasa gücü riski doğar, hesaplama ve mevzuat ağırlaşır. Bugünkü yapı tek bölgedir.

**"1 etiketli talimat hacmini nasıl azaltırsın?"**

> **Mülakatta şöyle söyle:** Kısa vadede daha iyi kısıt tahmini ve topoloji önlemleri; orta vadede dinamik hat kapasitesi ve depolama; uzun vadede iletim yatırımı. Hangisinin değeceğini fayda-maliyet analizi söyler.

## 90 saniye

"Türkiye'de enerji önce gün öncesi piyasasında, saatlik ve ülke çapında tek fiyatla satılır; bu fiyat piyasa takas fiyatıdır. Tahmin değiştikçe katılımcılar gün içi piyasasında sürekli ticaretle, teslimata bir saat kalana kadar pozisyon düzeltir. Gerçek zamanda kalan farkı TEİAŞ dengeleme güç piyasasında yük alma ve yük atma talimatlarıyla kapatır; buradan sistem marjinal fiyatı çıkar. Dengesizlik iki yönde de cezalı fiyatlanır. Gün öncesi piyasası şebekeyi görmediği için iletim kısıtı ayrı etiketli talimatlarla çözülür; analiz yazılımının piyasayla buluştuğu yer burasıdır. Fiyat üst sınırı Nisan 2026 kararıyla megavat-saat başına dört bin beş yüz liradır."
