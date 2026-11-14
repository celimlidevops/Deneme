# Kısa devre — mülakat kartları

**Bu ne? → Panelde söyle → Unutma.** Formül yok.

---

## 1. Neden hesaplanır?

**Bu ne?**  
Yük akışı “normal gün”dür. Kısa devre “bir şey birbirine değdi” anıdır.

Kararlar:

- Kesici bu akımı **kesebilir mi?**  
- Röle **görür mü**, doğru yerde açar mı?  
- Trafo / bara bu zorlamaya **dayanır mı?**  
- Topraklama yeterli mi?

**Panelde söyle:**  
> Kısa devre hesabı ekipman seçimi, koruma ve topraklama içindir; yük akışının yerine geçmez.

---

## 2. Arıza türleri

| Tür | Basitçe |
| --- | --- |
| Üç faz | Üç tel birbirine — dengeli |
| İki faz | İki tel birbirine |
| İki faz-toprak | İki tel + toprak |
| Tek faz-toprak | Bir tel + toprak — **en sık** |

**Unutma:** “En büyük hep üç fazdır” yanlış olabilir. Katı topraklı şebekede tek faz-toprak bazen daha büyük çıkar.

**Panelde söyle:**  
> Ekipman için azami, röle görme için asgari hesabı ayrı düşünürüm. En sık arıza tek faz-topraktır.

---

## 3. Thevenin / Zbus (fikir)

**Bu ne?**  
Arıza noktasına dışarıdan bakınca şebeke tek bir “eşdeğer engel” gibi görünür.  
O engel küçükse akım büyük, büyükse akım küçük.

Bara empedans matrisi (Zbus) bu bakışın tablo halidir — isim yeter.

---

## 4. Zaman: alt geçici / geçici / sürekli

**Bu ne?**  
Senkron makine arızanın **ilk anında** en çok akım verir, sonra azalır.

| Dönem | Ne için düşünülür |
| --- | --- |
| Alt geçici (ilk çevrimler) | En büyük akım, kesici tepe |
| Geçici | Ortası |
| Sürekli | Uzun süre kalan |

**Panelde söyle:**  
> Hangi reaktansı kullandığımı söylemeden arıza akımı konuşmam; ilk çevrim ile sürekli aynı sayı değildir.

---

## 5. Kesici seçimi

**Bu ne?**  
Kesici yalnız “etkin amper”e bakarak seçilmez.  
İlk tepe, doğru akım bileşeni, X/R (şebekenin ne kadar “bobinsi” olduğu) işin içine girer.

**Panelde söyle:**  
> Kesicide kesme kapasitesi ve tepe dayanımı ayrı bakılır; X/R tepeyi şişirir.

---

## 6. IEC 60909

**Bu ne?**  
Kısa devre akımı hesabı için yaygın uluslararası standart.  
Gerilim katsayısı (c) ve empedans düzeltmeleri gibi kuralları vardır.

**Panelde söyle:**  
> Hesabı hangi standarda göre yaptığımı söylerim; IEC 60909 yaygın seçimdir. ANSI/IEEE farklı gelenek — karıştırmam.

---

## 7. Zayıf / sert bara

- **Çok zayıf:** arıza akımı küçük → röle görmeyebilir, gerilim çok düşer.  
- **Çok sert:** arıza akımı çok büyük → kesici / ekipman zorlanır.

İkisi de sorundur; “büyük her zaman iyi” değildir.

---

## 90 saniye

> “Kısa devre ekipman ve koruma içindir. En sık tek faz-toprak; en büyük her zaman üç faz değil. Makine akımı zamanla düşer. Kesicide tepe ve X/R önemli. Standardı söylerim: çoğu zaman IEC 60909.”
