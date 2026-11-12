# Kendi projelerinden köprü

Bu sayfa bir **şablondur**. Proje adı, rol ve mimari buraya yazılmaz. Kartları kendi işinle doldurursun.

Boşlukları doldurmadan mülakata girme. Doldurduktan sonra bu sayfa senin en güçlü sayfan olur.

Sayfa beş adımdan oluşur:

| Adım | Ne yapacaksın |
| --- | --- |
| 1 | Her proje için kimlik kartı doldur |
| 2 | Veri akışı, ölçekleme ve güvenlikte birer mimari karar seç |
| 3 | Ad hakkındaki tahmini ve uyarıyı oku |
| 4 | İki dakikalık anlatımı sesli çalış |
| 5 | Gelecek zor soruların cevabını yaz |

## Neden önemli

Panelin karşısında iki tür aday olacak:

- Güç sistemini bilen ama üretim yazılımı geliştirmemiş olanlar.
- İkincisi: üretim yazılımı geliştirmiş, güç sistemini sonradan öğrenen.

İlanın cümlesi "analiz **ve yazılım geliştirme**"dir. YTBS (Yük Tevzi Bilgi Sistemi), on binlerce web servis isteği ve binlerce kullanıcıyla çalışan bir üretim sistemidir (`01/03`). Senin kanıtın, böyle bir sistemin kararlarını vermiş olmandır.

Ama kural şu: **benzetme kur, eşitlik kurma.**

> **Mülakatta şöyle söyle:** "Eski projemde yaptığım, durum kestirimiyle aynı şey" deme. "Şu kararı verdim; şebeke yazılımında aynı sorunun karşılığı şudur" de.

## Adım 1: her proje için kimlik kartı

Her proje için ayrı doldur. Yalnız gerçeği yaz. Hatırlamadığın sayıyı mertebe olarak ver (örneğin "binler düzeyinde").

Aşağıdaki kart, panelin projen hakkında soracağı temel bilgileri tek yerde toplar. Satırları tek tek doldur.

```
Proje adı            :
Tek cümleyle ne      :
Kullanıcısı kim      :
Dönem                : ____ – ____
Senin rolün          : (geliştirici / teknik lider / mimar / ...)
Ekip büyüklüğü       :
Sorumlu olduğun kısım:
Teknoloji yığını     : dil, çerçeve, veri tabanı, kuyruk, bulut
Ölçek                : kullanıcı sayısı, istek/saniye, veri hacmi, belge sayısı
Üretimde mi          : evet / hayır; ne zamandan beri
Enerji veya şebekeyle ilişkisi : var / dolaylı / yok   (dürüstçe)
SGK dökümünde hangi işyeri ve dönem altında görünüyor :
```

Son iki satır, `01/04` dosyasındaki tecrübe beyanı uyarısıyla doğrudan ilgilidir. SGK (Sosyal Güvenlik Kurumu) dökümü, tecrübe süresinin resmî kanıtıdır.

## Adım 2: üç mimari karar

İlan maddeleri ve panelin ilgisi açısından en değerli üç eksen şunlardır: **veri akışı, ölçekleme, güvenlik**. Her biri için bir karar seç ve aşağıdaki dört satırı doldur.

Bu dört satırlık kalıp, bir kararı "ne, neye karşı, neden, sonuç" sırasıyla anlatmana yarar.

```
Karar      : Ne seçtin?
Alternatif : Neyi eledin?
Gerekçe    : Neden? (ölçüm, kısıt, maliyet)
Sonuç      : Ne oldu? Sayıyla. Bugün olsa aynısını yapar mıydın?
```

### Veri akışı

Kendine sor:

- Veri sisteme nereden giriyor, hangi biçimde, ne sıklıkta?
- Girdi bozuk, eksik veya gecikmeli gelirse ne oluyor? Sessizce mi yutuluyor, reddediliyor mu, karantinaya mı alınıyor?
- İşleme eşzamanlı mı, kuyrukla mı? Neden?
- Aynı girdi iki kez gelirse sonuç değişiyor mu (eşgüçlülük)?
- Bir sonucun hangi girdiden ve hangi kod sürümünden üretildiğini geriye doğru izleyebiliyor musun?
- Şema değiştiğinde eski veriye ne oluyor?

Eşgüçlülük, aynı işlemi bir kez veya birçok kez yapmanın aynı sonucu vermesidir.

Şebeke yazılımındaki karşılıkları:

| Senin sorunun | Şebeke yazılımındaki karşılığı |
| --- | --- |
| Bozuk veya eksik girdi | Kalite bayrağı kötü olan ölçüm; durum kestiriminde kötü veri (`09/02`) |
| Gecikmeli, sırasız veri | SCADA taramasının eşzamansızlığı; geç gelen sayaç verisi |
| Kuyruk ve eşzamansız işleme | 30 saniye süren güvenlik analizinin istekten ayrılması |
| Eşgüçlülük | Aynı model + aynı senaryo = aynı sonuç; önbellek anahtarı |
| Veri soy izi | Sonucun hangi model, ölçüm ve algoritma sürümüyle üretildiği |
| Şema evrimi | CIM sürümleri; model değişince eski senaryoların geçerliliği |
| Doğrulama katmanı | Topoloji denetimi, ada tespiti, birim ve baz denetimi |

Tablodaki kısaltmalar: SCADA (Supervisory Control and Data Acquisition, denetleyici kontrol ve veri toplama) sahadan ölçüm toplayan sistemdir. CIM (Common Information Model, ortak bilgi modeli) şebeke modelinin ortak sınıf yapısıdır.

### Ölçekleme

Kendine sor:

- Darboğaz neredeydi? Nasıl **ölçtün**?
- Yatay mı dikey mi ölçekledin? Durum nerede tutuluyor?
- En pahalı işlem neydi; önbelleğe aldın mı, ön hesapladın mı, paralelleştirdin mi?
- Yük ani arttığında sistem nasıl davranıyor: yavaşlıyor mu, reddediyor mu, çöküyor mu?
- Ölçeklemeden önce ve sonra hangi sayı değişti?

Yatay ölçekleme makine sayısını artırmak, dikey ölçekleme tek makineyi güçlendirmektir.

Şebeke yazılımındaki karşılıkları:

| Senin sorunun | Şebeke yazılımındaki karşılığı |
| --- | --- |
| Bağımsız işleri paralelleştirme | Binlerce N-1 vakası birbirinden bağımsızdır (`07/02`) |
| Pahalı hesabı ön hesaplama | PTDF ve LODF: duyarlılık bir kez hesaplanır, binlerce kez kullanılır (`03/03`) |
| Önbellek | Matris çarpanlarının yeniden kullanımı; topoloji değişmediyse simgesel ayrışma |
| Kademeli işleme (ucuz filtre, pahalı doğrulama) | DC tarama → AC doğrulama → dinamik benzetim |
| Geri basınç ve öncelik | Operatörün anlık isteği, toplu gece çalışmasının önüne geçer |
| Ölçmeden eniyileme yapmamak | Sürenin kurulumda mı çözücüde mi geçtiğini profille görmek (`14/02`) |

Tablodaki kısaltmalar ve terimler:

- **N-1:** şebekeden tek bir elemanın (hat, trafo, ünite) düşürüldüğü arıza senaryosu.
- **PTDF** (Power Transfer Distribution Factor, güç aktarım dağılım çarpanı): bir baradaki güç değişiminin hat akışlarına nasıl dağıldığını gösterir.
- **LODF** (Line Outage Distribution Factor, hat açılması dağılım çarpanı): bir hat açılınca akışının diğer hatlara nasıl dağıldığını gösterir.
- **DC / AC:** DC (doğru akım) yaklaşımı hızlı ve kaba yük akışıdır; AC (alternatif akım) yük akışı tam ve yavaştır.
- **Geri basınç:** sistem doluyken yeni işi yavaşlatma veya reddetme mekanizması.

### Güvenlik

Kendine sor:

- Kimlik doğrulama ve yetkilendirme nasıl? Roller neler?
- Hassas veri neydi? Nerede şifreli, kim erişebiliyor, erişim kaydı tutuluyor mu?
- Kiracılar veya müşteriler birbirinin verisinden nasıl yalıtılıyor?
- Dışarıdan gelen dosya veya girdi nasıl doğrulanıyor?
- Sırlar nerede duruyor?
- Bir güvenlik olayı veya denetim yaşadın mı? Ne değişti?
- (Yapay zekâ bileşeni varsa) Model dışarı veri sızdırabilir mi? Girdiyle yönlendirilebilir mi? Çıktısı doğrulanmadan bir eyleme dönüşüyor mu?

Şebeke yazılımındaki karşılıkları:

| Senin sorunun | Şebeke yazılımındaki karşılığı |
| --- | --- |
| Rol tabanlı erişim | Kim senaryo koşar, kim modele yazar, kim yalnız görür |
| Hassas veri | Ulusal şebeke modeli, kısa devre güçleri, kritik merkezler; santrallerin ticari verisi |
| Denetim izi | Kim, ne zaman, hangi model sürümüyle hangi hesabı koştu |
| Güvenilmeyen girdi | Dışarıdan gelen CIM dosyası, sistem kullanıcısından gelen veri |
| Ağ yalıtımı | Analiz servisi kontrol ağına yazamaz; veri tek yönlü (`16/02`) |
| Model çıktısının doğrulanmadan eyleme dönüşmemesi | Yapay zekâ tahmini operatöre öneridir; fizik tabanlı denetimden geçer (`18/02`) |

## Adım 3: işin cinsinden köprü kur, addan tahmin yürütme

Proje adından ne iş yaptığını çıkarma. Aşağıdaki köprüler yalnızca belge veya yapay zekâ işi yaptıysan kullanılır. Değilse atla.

| Belge işleme sisteminde | Şebeke analizinde |
| --- | --- |
| Modelin emin olmadığı çıktıyı insana yönlendirmek | Güvenlik açısından kritik kararda insan onayı |
| Çıkarılan alanı kurallarla doğrulamak (toplam = kalemlerin toplamı) | Öğrenen modelin çıktısını fizikle denetlemek (güç dengesi, sınırlar) |
| Eğitimde görülmemiş belge türünde başarımın düşmesi | Dağılım dışı işletme koşulu: hiç görülmemiş topoloji, aşırı hava |
| Doğruluğu örneklemle sürekli izlemek | Tahmin hatasını ve model kaymasını izlemek |
| Modelin neden o sonucu verdiğini açıklayabilmek | Operatörün öneriye güvenebilmesi için gerekçe |

**Uyarı.** Bu projelerin enerji veya şebekeyle ilişkisi yoksa mülakatta da yok de. "Şebeke yazılımına benzer bir sistem" deme. Panel alanın içindendir ve tek soruyla ayırır.

> **Mülakatta şöyle söyle:** "Alanı farklıydı; taşıdığım şey mimari kararlar."

## Adım 4: iki dakikalık anlatım

Kartı ve kararları doldurduktan sonra her proje için aşağıdaki iskeleti sesli söyle ve süre tut. Köşeli parantezler, senin dolduracağın yerlerdir.

> **Mülakatta şöyle söyle:** "[Proje], [kullanıcı] için [tek cümle]. Ben [rol] olarak [sorumluluk] kısmından sorumluydum. Ölçeği [sayı]. En zor karar [karar] idi: [alternatif] yerine [seçim] yaptım, çünkü [gerekçe]. Sonuç [sayı]. Enerji alanında bir proje değildi. Ama aynı soru sizin sistemlerinizde de var: [karşılık]. Örneğin [bu klasörden somut bir örnek]."

İskeletin sırası şudur: ne yaptın, rolün ne, ne büyüklükte, en zor karar ne, sonuç ne, alanla ilişkisi ne, şebekedeki karşılığı ne.

Örnek karşılık cümleleri. Gerçeğine uyanı seç:

| Kendi deneyimin | Şebekedeki karşılığı |
| --- | --- |
| Uzun süren işi kuyruğa almak | Binlerce bağımsız arıza vakası |
| Bozuk girdiyi reddetmek | Yakınsamayan yük akışında hata fırlatmak |
| Model çıktısını kuralla doğrulamak | Güç dengesi ve sınırlarla denetim |

> **Mülakatta şöyle söyle:** "Uzun süren işi istekten ayırıp kuyruğa almıştım. Güvenlik analizinde de binlerce arıza vakası bağımsızdır ve aynı desenle koşar."

> **Mülakatta şöyle söyle:** "Bozuk girdiyi sessizce yutmak yerine reddedip nedenini dönüyordum. Yazdığım yük akışı kodu da yakınsamazsa boş sonuç dönmüyor, artık geçmişini taşıyan bir hata fırlatıyor."

> **Mülakatta şöyle söyle:** "Model çıktısını kuralla doğrulamadan sisteme yazmıyordum. Şebekede bunun karşılığı, öğrenen modelin sonucunu güç dengesi ve sınırlarla denetlemek."

## Adım 5: gelecek zor sorular

Her sorunun cevabını önceden yaz. "Cevabın yönü" sütunu, cevabın hangi yöne gitmesi gerektiğini gösterir.

| No | Soru | Cevabın yönü |
| --- | --- | --- |
| 1 | "Bu projelerin güç sistemiyle ne ilgisi var?" | Dürüst cevap ve köprü |
| 2 | "Oradaki hata bir belgeyi yanlış okumaktı. Burada hata bir bölgenin karanlıkta kalması. Bu farkı nasıl yönetirsin?" | Güvenlik açısından kritik yazılım: fizik tabanlı denetim, insan onayı, kademeli devreye alma, geri dönüş planı, gölge modda çalıştırma |
| 3 | "Teknik liderdin. Burada en kıdemsiz araştırmacı olacaksın. Sorun olur mu?" | `19/02` |
| 4 | "Hangi mimari kararından pişmansın?" | Gerçek bir örnek; ne öğrendin |
| 5 | "Ölçek dediğin sayı ne? Nasıl ölçtün?" | Sayı ve ölçüm yöntemi |
| 6 | "Bu sistemi sen mi tasarladın, ekip mi?" | Kendi payını ayır |

İkinci sorudaki "gölge modda çalıştırma", yeni sistemin gerçek veriyle çalışıp sonucunun henüz kullanılmaması, yalnızca eskisiyle karşılaştırılmasıdır.

Aşağıdaki konuşma bir şablondur. Köşeli parantezleri kendi gerçeğinle doldur. Proje adı uydurma.

## 90 saniye

(Şablon. Köşeli parantezleri kendi gerçeğinle doldur.)

"[Kaç] yıldır üretimde çalışan yazılım sistemleri geliştiriyorum; en çok emek verdiğim ikisi [proje: tek cümle] ve [proje: tek cümle]. Enerji alanında projeler değildi. Taşıdığım şey üç tür karar: veri akışında [karar], ölçeklemede [karar], güvenlikte [karar]. Şebeke analiz yazılımında aynı sorular var: bozuk ölçümü sessizce yutmamak, binlerce bağımsız arıza vakasını paralel koşmak, sonucun hangi model sürümünden üretildiğini izlemek. Eksik olan alan bilgisi; onu kapatmak için yük akışını ve durum kestirimini sıfırdan yazıp doğruladım."
