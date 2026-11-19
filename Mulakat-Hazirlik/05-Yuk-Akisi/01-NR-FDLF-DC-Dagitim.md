# Yük akışı — çok basit kartlar

---

## 1. Bu analiz ne sorar?

**Ne demek?**  
Biliyoruz: hangi santral ne üretiyor, hangi yer ne tüketiyor, hatlar nasıl bağlı.  
Arıyoruz: her noktada gerilim nasıl, hatlar ne kadar dolu, kayıp ne kadar.

**Benzetme:**  
Trafikte arabalar (güç) belli. Hangi yollar tıkanır, nerede baskı oluşur?

**Mülakatta:**  
> Yük akışı, verilen üretim ve yükte gerilim ve hat akışlarını bulur.

---

## 2. Nokta (bara) tipleri

Her noktada her şeyi bilemeyiz.

| Tip | Basitçe | Kim |
| --- | --- | --- |
| PQ | Gücü biliyoruz, gerilimi arıyoruz | Yük |
| PV | Üretimi ve gerilimi tutuyoruz | Santral |
| Slack | Referans nokta; dengeyi tamamlar | Hesap başlangıcı |

**Mülakatta:**  
> Slack sihirli santral değildir; hesabın referansıdır. Santral reaktif sınırına gelince gerilim tutamaz.

---

## 3. Bilgisayar nasıl çözer?

1. Bir tahmin koyar.  
2. Sonuca ne kadar uzak bakır.  
3. Düzeltir.  
4. Yeterince iyi olana kadar tekrarlar.

Buna pratikte **Newton-Raphson** denir. Formül ezberleme.  
“Tahmini düzelte düzelte giderim” demen yeter.

**Mülakatta:**  
> İletimde standart yöntem Newton-Raphson’dur. Seyrek çözerim.

---

## 4. Hızlı kaba bakış (DC)

Bazen sadece “hangi hat ısınır?” diye kabaca bakılır.  
Gerilim ve reaktif işi bu kaba bakışta yoktur.

**Mülakatta:**  
> DC yük akışı hızlı termik elek içindir. Gerilim kararı için yetmez; sonra ayrıntılı kontrol yaparım.

---

## 5. Çözüm tutmazsa (ıraksama)

Önce şunlara bak:

1. Şebeke kopuk mu?  
2. Veri yanlış mı?  
3. Kontroller gidip geliyor mu?

**Mülakatta:**  
> Iraksayınca ilk iş çözücü değiştirmek değil; ada, veri ve limitlere bakarım.

---

## 6. Dağıtımda fark

Mahalle şebekesi tek yoldan ve dengesiz olabilir.  
İletim yöntemi olduğu gibi taşınmaz.

**Mülakatta:**  
> Dağıtımda ayrı yöntem veya üç faz model gerekir.

---

## 7. Sonucu nasıl anlatırsın?

Ham sayı yetmez.

- Nerede gerilim bozuk?  
- Hangi hat dolu?  
- Ne yapılmalı?

**Mülakatta:**  
> Sonucu limit ihlali ve müdahale diline çeviririm.

---

## Sesli özet

> Yük akışı: üretim-yük belli → gerilim ve hat doluluğu bulunur. PQ yük, PV santral, slack referanstır. Bilgisayar tahmini düzeltir. Kaba bakış gerilim kararı vermez. Sonuç ‘ne yapmalı’ diline çevrilir.
