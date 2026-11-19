# Temeller — çok basit kartlar

Her kartta üç şey var:

1. **Ne demek?** (günlük dil)
2. **Nasıl aklında kalsın?** (benzetme)
3. **Mülakatta ne söyle?** (tek kısa paragraf)

---

## 1. Güç nedir? (P, Q, S)

**Ne demek?**

Elektrik hattından iki şey geçer:

- **Aktif güç (P):** gerçekten iş yapan kısım. Lamba yanar, motor döner.
- **Reaktif güç (Q):** iş yapmaz. Ama motor ve trafo çalışsın diye gerekir. Hattı boşuna doldurur.
- **Görünür güç (S):** ikisinin birlikte hattı ne kadar doldurduğu. Trafo büyüklüğü buna göre seçilir.

**Nasıl aklında kalsın?**

Su borusu düşün:

- P = musluktan çıkan, işe yarayan su
- Q = borunun içinde gidip gelen, evde kullanılmayan su
- S = borunun toplam doluluğu

**Mülakatta ne söyle?**

> Aktif güç iş yapar. Reaktif güç iş yapmaz ama hattı doldurur ve gerilimi etkiler. Cihazlar ısındığı için görünen toplam güce (S) göre seçilir.

---

## 2. Frekans ve gerilim

**Ne demek?**

- **Frekans:** elektriğin saniyede kaç kez salındığı. Türkiye’de 50. Bütün ülkede aynıdır.
- **Gerilim:** elektriğin “itme gücü”. Mahalleden mahalleye değişebilir.

Üretim yetmezse frekans düşer.  
Bir bölgede destek yetmezse o bölgenin gerilimi düşer.

**Nasıl aklında kalsın?**

- Frekans = bütün ülkenin nabzı
- Gerilim = o mahallenin tansiyonu

**Mülakatta ne söyle?**

> Frekans ülke genelinde üretim-tüketim dengesini gösterir. Gerilim yerlidir; bir mahallede sorun varsa uzaktaki santral her zaman kurtaramaz.

---

## 3. Neden teller çok yüksek gerilimde?

**Ne demek?**

Aynı enerjiyi yüksek gerilimle taşırsan akım küçülür.  
Akım küçülünce tel daha az ısınır. Kayıp azalır.

Bu yüzden şehirler arası hatlar çok yüksek gerilimdedir.  
Şehre gelince **trafo** gerilimi düşürür.

**Nasıl aklında kalsın?**

Aynı suyu ince hortumla yüksek basınçta taşımak gibi: akış (akım) azalır, kayıp azalır.

**Mülakatta ne söyle?**

> Yüksek gerilim, kaybı azaltmak için kullanılır. Trafo gerilimi yükseltir ve düşürür.

---

## 4. Fazör (çok kısa)

**Ne demek?**

Evdeki elektrik düz çizgi değil; sürekli salınan bir dalgadır.  
Bir dalgayı anlatmak için iki bilgi yeter:

1. Ne kadar büyük?
2. Diğerine göre önde mi, geride mi?

Bu ikiliye **fazör** denir.

**Nasıl aklında kalsın?**

Bir ok: boyu = büyüklük, yönü = açı.

**Mülakatta ne söyle?**

> Şebeke salınan bir dalgadır. Büyüklük ve açı ile anlatırım; buna fazör derim.

---

## 5. Üç faz ve “400 kV”

**Ne demek?**

Büyük şebekede üç tel vardır. Üçü birden çalışır. Buna **üç faz** denir.

“400 kV” denince **iki tel arası** gerilim kastedilir.

**Nasıl aklında kalsın?**

Üç şeritli yol: daha çok taşıma kapasitesi.

**Mülakatta ne söyle?**

> İletimde üç faz kullanılır. 400 kV, iki faz arası hat gerilimidir.

---

## 6. Per-unit (birim sistem)

**Ne demek?**

Şebekede hem çok büyük gerilim (400.000 V) hem küçük gerilim (230 V) vardır.  
Aynı hesaba koyunca rakamlar karmaşık olur.

Per-unit: her sayıyı “normale” bölmek.  
Sağlıklı gerilim hep **1 civarı** görünür.

**Nasıl aklında kalsın?**

Farklı okulların notunu hep 100 üzerinden yazmak.

**Mülakatta ne söyle?**

> Per-unit farklı gerilimleri aynı dile çevirir. Sağlıklı gerilim yaklaşık 1’dir.

---

## 7. Ybus (şebeke tablosu)

**Ne demek?**

Şebeke: noktalar (bara) + teller (hat).  
Bilgisayarda bunu bir tabloya yazarız. Bu tabloya **Ybus** denir.

“Kim kime bağlı?” sorusunun cevabıdır.

**Nasıl aklında kalsın?**

Şehir haritasındaki yolların listesi.

**Mülakatta ne söyle?**

> Ybus şebekenin bağlantı tablosudur. Çoğu kutu boştur; tersini almak yerine seyrek çözerim.

---

## 8. Reaktif neden yakında üretilir?

**Ne demek?**

Reaktif güç uzun yolda zayıflar.  
Uzaktan göndermek zor. Bu yüzden ihtiyacın olduğu yere yakın üretilir.

- **Kondansatör:** ucuz destek
- **STATCOM:** hızlı ve güçlü destek (MAM’ın ürünü bu aileden)
- **Kademe:** trafonun ayarıdır; yeni güç üretmez, gerilimi kaydırır

**Nasıl aklında kalsın?**

Soğuk odayı uzak kaloriferle değil, odadaki radyatörle ısıtırsın.

**Mülakatta ne söyle?**

> Reaktif güç yerinde üretilir. Kondansatör ucuzdur, STATCOM hızlıdır. Kademe reaktif üretmez.

---

## 9. Yük gerilim düşünce ne yapar?

**Ne demek?**

Bazı cihazlar gerilim düşünce daha az çeker (kolay).  
Bazıları aynı gücü zorla çeker, akımı artırır (zor).

**Nasıl aklında kalsın?**

Kolay yük = yavaşlayan musluk.  
Zor yük = “ben aynı suyu isterim” deyip musluğu daha çok açmak.

**Mülakatta ne söyle?**

> Sabit güç yükü gerilim düşünce akımını artırır. Bu yüzden kararlılıkta en zor varsayımdır.

---

## 10. Trafo bağlantısı ve toprak arızası

**Ne demek?**

Trafo sargıları yıldız veya üçgen bağlanır.  
Dağıtımda çok görülen isim: **Dyn11**.

Bir tel toprağa değince akan özel akımın yolu, bu bağlantıya bağlıdır.  
Üçgen taraf bu yolu diğer tarafa geçirmez.

**Nasıl aklında kalsın?**

Kapı bazı odalara açılır, bazılarına açılmaz.

**Mülakatta ne söyle?**

> Toprak arızası yolu topraklı yıldızdan akar. Üçgen diğer tarafa geçirmez. Dyn11 dağıtımda yaygındır.

---

## Sesli özet (1 dakika)

> Elektrikte iş yapan güç aktif, hattı dolduran reaktif güçtür. Frekans ülke nabzı, gerilim mahalle tansiyonudur. Uzak taşıma yüksek gerilimle yapılır. Per-unit farklı gerilimleri aynı dile çevirir. Ybus bağlantı tablosudur. Reaktif yakında üretilir. Yükün gerilim düşünce davranışı varsayıma bağlıdır. Toprak arızasının yolu trafo bağlantısına bağlıdır.
