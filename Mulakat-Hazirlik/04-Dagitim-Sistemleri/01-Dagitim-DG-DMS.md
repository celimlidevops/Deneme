# Dağıtım — mülakat kartları

**Bu ne? → Panelde söyle → Unutma.** Hesap yok.

---

## 1. Dağıtım ile iletim farkı

**Bu ne?**

| | İletim | Dağıtım |
| --- | --- | --- |
| Yapı | Örgülü (çok yol) | Çoğunlukla **radyal** (tek yol) |
| Gerilim | 400 / 154 kV | OG (ör. 34,5 kV), AG (0,4 kV) |
| R / X | X baskın | R daha görünür |
| Fazlar | Dengeli varsayım sık | Dengesizlik sık |

**Fider:** trafo merkezinden çıkan bir dağıtım hattı / besleme kolu.

**Panelde söyle:**  
> Dağıtım radyaldir, R yüksektir, fazlar dengesiz olabilir. İletim formülünü olduğu gibi taşımak yanlış olur.

---

## 2. Gerilim neden düşer / yükselir?

**Bu ne?**  
Fider boyunca yük çekildikçe gerilim genelde **düşer**.  
Çatı güneşi öğlen fazla basarsa, özellikle uçlara yakınsa gerilim **yükselebilir** (ters akış + R etkisi).

Araçlar (ucuzdan pahalıya fikir): kademe, kondansatör, iletken büyütme, evirici volt-var, yeni trafo/fider.

**Panelde söyle:**  
> Dağıtımda aktif güç de gerilimi oynatır. Öğlen yükselmeyi çoğu zaman reaktif “üretmek” değil, eviricinin reaktif tüketmesi veya aktif sınırlama çözer.

---

## 3. Dağıtık üretim (DG) bağlantı soruları

**Bu ne?**  
Çatı güneşi / küçük santral fidere bağlanacak. Standart sorular:

1. Gerilim limitini bozar mı?  
2. Hat/trafo ısınır mı?  
3. Koruma hâlâ doğru görür mü?  
4. Ters akış var mı, trafo/röle buna hazır mı?  
5. Ada tehlikesi var mı?

**Panelde söyle:**  
> Bağlantı çalışması tek MW sayısı değildir; gerilim, termik, koruma ve ters akış birlikte bakılır.

---

## 4. Barındırma kapasitesi

**Bu ne?**  
Bir noktaya / fidere, limitler bozulmadan **ne kadar üretim** bağlanabilir?

En küçük limit geçerlidir (gerilim, ısınma, koruma, ters akış…).  
Trafo yanı ile fider ucu **aynı MW değildir**.  
En zor saat genelde: **az yük + çok üretim** (öğlen, bahar).

**Panelde söyle:**  
> Barındırma kapasitesi konuma ve saate bağlıdır; tek rakam her yere yapıştırılmaz.

---

## 5. Ada ve tekrar kapama

**Bu ne?**  
Şebeke kesildiğinde küçük üretim “kendi adasını” canlı tutmaya çalışırsa tehlikelidir (bakım ekibi, gerilim/frekans kontrolden çıkar).

Evirici şebeke gidince **açılmalıdır**.  
Otomatik tekrar kapama (OTK) ile zamanlama çakışırsa sorun çıkar — koruma koordinasyonu konusu.

**Panelde söyle:**  
> Ada çalışmasına izin vermem; evirici anti-islanding ile çıkar, OTK ile koordinasyon şarttır.

---

## 6. Dağıtım şirketi yazılımları (isim yeter)

| Kısaltma | Ne işe yarar |
| --- | --- |
| GIS | Harita / şebeke coğrafyası |
| SCADA | Canlı izleme ve kumanda |
| DMS | Dağıtım yönetim sistemi (analiz + işletme) |
| OMS | Kesinti yönetimi |
| AMI | Akıllı sayaç altyapısı |

**Panelde söyle:**  
> DMS işletme beynidir; OMS kesintiyi yönetir; AMI ölçü getirir; GIS topolojiyi taşır.

---

## 7. Kayıp iki tür

- **Teknik:** tel ısınması (fizik).  
- **Ticari:** kaçak, ölçüm hatası, kayıt hatası.

İkisini karıştırmadan konuş.

---

## 90 saniye

> “Dağıtım radyaldir, R görünür, dengesizlik normaldir. DG’de gerilim, ısınma, koruma ve ters akışa bakarım. Barındırma kapasitesi yere ve saate bağlıdır. Ada yasaktır. DMS–OMS–AMI katmanları ayrı işler görür.”
