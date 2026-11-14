# Mülakat kartları — sıfırdan

Her kart üç satır: **Bu ne?** → **Panelde söyle** → **Unutma**.

Hesap yok. Anlamadığın kelime için [07 sözlük](07-Sozluk-ve-Kendini-Yokla.md).

---

## 1. Aktif güç, reaktif güç, görünür güç

**Bu ne?**

Şebeke iki şey taşır:

- **Aktif güç (P):** gerçekten iş yapan kısım. Lamba yanar, motor döner. Birimi MW.
- **Reaktif güç (Q):** iş yapmaz ama motor ve trafonun manyetik alanı için gerekir. Birimi Mvar. “Yararsız trafik” gibi: yolu doldurur.
- **Görünür güç (S):** ikisinin toplamı. Trafo ve hat buna göre seçilir. Birimi MVA.

**Panelde söyle:**

> Aktif güç iş yapar; dengesi bozulursa frekans sarsılır. Reaktif güç iş yapmaz ama akımı şişirir; dengesi bozulursa gerilim sarsılır. Cihazlar ısındığı için S’ye (MVA) göre boyutlanır.

**Unutma:** Reaktif güç “kayıp” değildir. Kayıp, onun şişirdiği akımın ısıya dönüşmesidir.

---

## 2. Frekans ve gerilim

**Bu ne?**

- **Frekans (50 Hz):** bütün Türkiye’de aynıdır. “Üretim ile tüketim dengede mi?” sorusunun cevabıdır. Üretim azsa frekans düşer.
- **Gerilim:** mahalle mahalle farklıdır. “Bu bölgede reaktif güç yeterli mi?” sorusunun cevabıdır.

**Panelde söyle:**

> Frekans sistemin aktif güç sağlığıdır, her yerde aynıdır. Gerilim yereldir; reaktif eksikse o bölgede düşer, uzaktaki santral bunu kolay kurtaramaz.

**Unutma:** Frekans = ülke. Gerilim = mahalle.

---

## 3. Neden yüksek gerilim?

**Bu ne?**

Aynı gücü yüksek gerilimle taşırsan akım küçülür. Akım küçülünce tel daha az ısınır, kayıp azalır. Bu yüzden iletim 400 kV gibi yüksek değerlerdedir. Trafo gerilimi yükseltip düşürür; trafo yalnızca alternatif akımda (AC) çalışır.

**Panelde söyle:**

> Yüksek gerilim, aynı enerjiyi küçük akımla taşıyıp kaybı düşürmek içindir. Trafo yüzünden iletim AC’dir.

---

## 4. Fazör (çok basit)

**Bu ne?**

Prizdeki elektrik saniyede 50 kez salınan bir dalgadır. Her dalgayı iki sayıyla anlatırız: **ne kadar büyük** ve **ne kadar önde/geride** (açı). Bu ikiliye **fazör** denir.

Açı tek başına anlamsızdır; bir barayı “sıfır” kabul ederiz (slack / salınım barası). Diğerleri ona göre söylenir.

**Panelde söyle:**

> Frekans ortak olduğu için gerilim ve akımı büyüklük ve açıdan oluşan fazörle anlatırım. Referans baranın açısı sıfırdır. Fazör sakin, sürekli hali anlatır; arıza anının milisaniyeleri için yetmez.

---

## 5. Üç faz ve “400 kV”

**Bu ne?**

Evde çoğu zaman tek faz vardır. İletimde **üç tel** (üç faz) vardır; aralarında 120 derece kayma vardır. Daha verimli taşır, motoru kendi kendine döndürür.

“400 kV” denince **iki tel arası** gerilim kastedilir (hat gerilimi). Bir tel ile nötr arası daha küçüktür (faz gerilimi).

**Panelde söyle:**

> 400 kV hat gerilimidir, iki faz arasıdır. Dengeli sistemde üç fazın birini çözerim; tek hat şeması budur.

**Unutma:** 400 kV ≠ faz gerilimi.

---

## 6. Per-unit (birim sistem)

**Bu ne?**

Şebekede hem 400.000 volt hem 230 volt vardır. Aynı hesaba koyunca rakamlar deli gibi büyür/küçülür. **Per-unit**, her sayıyı “normal kabul ettiğimiz değere” bölmektir. Sağlıklı gerilim hep **1 civarı** görünür. 0,9 görürsen “düşük” demektir.

Trafo etiketindeki yüzde, o trafonun kendi dünyasına göredir. Büyük sistem hesabına koymadan önce sistemin diline çevrilir.

**Panelde söyle:**

> Per-unit farklı gerilim seviyelerini aynı dile çevirir. Trafo plakası kendi bazındadır; sistem matrisine girmeden çeviririm.

**Benzetme:** Herkesin notunu 100 üzerinden yazmak gibi.

---

## 7. Ybus (şebeke haritası)

**Bu ne?**

Şebeke baralar (düğümler) ve hatlardan (bağlantılar) oluşur. Bilgisayarda bunu bir tabloya (matris) yazarız: **Ybus**.

- İki bara bağlıysa tabloda ikisinin kesişiminde bir sayı vardır.
- Bir bara hangi hatlara bağlıysa kendi kutusunda onların toplamı vardır.

Bu tablo çok büyük ama çoğu kutu boştur (seyrek). Tersini almak yerine akıllıca çözeriz.

**Panelde söyle:**

> Ybus şebekenin bağlantı haritasıdır: akım = Ybus × gerilim. Çoğu eleman sıfırdır; tersini almam, seyrek çözerim.

---

## 8. Reaktif güç neden yerinde üretilir?

**Bu ne?**

Reaktif güç uzun yolda “erir”. Uzaktaki büyük santral, senin mahallendeki gerilimi kurtaramayabilir. Bu yüzden kondansatör, STATCOM gibi cihazlar **yükün yanında** konur.

- **Kondansatör:** ucuz, yavaş, gerilim düşünce kendi gücü de düşer.
- **STATCOM:** pahalıya yakın, çok hızlı, zor anda da işe yarar. MAM’ın milli ürünü bu aileden.
- **Kademe (OLTC):** trafonun ayarıdır; reaktif **üretmez**, gerilimi bir taraftan diğerine kaydırır.

**Panelde söyle:**

> Reaktif uzun hatta taşınamaz; tüketildiği yerde üretilir. Kondansatör ucuz ama gerilim düşünce zayıflar; STATCOM dinamik payı alır. Kademe reaktif üretmez.

---

## 9. Yük nasıl davranır?

**Bu ne?**

“100 MW yük” yazmak kolaydır. Gerçekte gerilim düşünce bazı cihazlar daha az çeker, bazıları aynı gücü zorla çeker ve akımı artırır.

- Isıtıcı gibi → gerilim düşünce güç düşer (kolay).
- Bilgisayar, şarj, sürücü gibi → güç aynı kalsın ister, akım artar (zor).

Kararlılık çalışmasında “hangi varsayımı yaptım?” demeden “sistem çöker” denmez.

**Panelde söyle:**

> Sabit güç yükü gerilim düşünce akımını artırır; en zor varsayımdır. Ölçüm yoksa iyimser ve kötümser iki uç bakıp farkı söylerim.

---

## 10. Trafo bağlantısı ve toprak arızası

**Bu ne?**

Trafo sargıları **yıldız** veya **üçgen** bağlanır. Dağıtımda çok görülen **Dyn11**: yüksek taraf üçgen, alçak taraf yıldız (nötr dışarıda).

Bir faz toprağa değince akan “toprak yolu” akımı, bu bağlantıya bağlıdır. Üçgen taraf, bu özel akımı diğer tarafa geçirmez. Bu yüzden ev tarafındaki toprak arızası, orta gerilim toprak rölesinde görünmeyebilir — bilinçli bir ayırmadır.

**Panelde söyle:**

> Sıfır dizi (toprak yolu) akımı yalnız topraklı yıldızdan akar; üçgen diğer tarafa geçirmez. Dyn11 dağıtımın klasik bağlantısıdır. Yazılımda tek faz akımı sıfırsa çoğu zaman sıfır dizi yolu yanlış girilmiştir.

---

## Bonus: hat ne kadar taşır?

Tek sayı yoktur. Üç ayrı tavan vardır:

1. **Tel ısınmasın** (termik)
2. **Gerilim bozulmasın**
3. **Sistem salınıp kopmasın** (kararlılık)

Kısa hat çoğunlukla ısınmaya, uzun hat kararlılığa takılır.

---

## 90 saniye (sesli oku)

> “Aktif güç iş yapar ve frekansı etkiler; reaktif güç iş yapmaz ama gerilimi etkiler. Frekans her yerde aynıdır, gerilim yerlidir. Yüksek gerilim kaybı düşürmek içindir. Per-unit farklı gerilimleri aynı dile çevirir. Ybus şebekenin bilgisayar haritasıdır. Reaktif yakında üretilir; kondansatör ucuz, STATCOM hızlıdır. Yükün gerilim düşünce nasıl davrandığı varsayıma bağlıdır. Toprak arızasının yolu trafo yıldız-üçgen bağlantısına bağlıdır.”
