# İletim — mülakat kartları

Her kart: **Bu ne?** → **Panelde söyle** → **Unutma**. Hesap yok.

---

## 1. İletim nedir?

**Bu ne?**  
Santrallerden şehirlerin kapısına kadar elektriği taşıyan **yüksek gerilim omurgası**. Dağıtım ise şehir içinde evlere götüren kısımdır.

Türkiye’de kabaca **36 kV üstü** iletim sayılır.

**Panelde söyle:**  
> İletim uzun mesafe yüksek gerilim taşımasıdır; dağıtım son kullanıcıya yerel dağıtımdır. İkisi birlikte ilanın “iletim ve dağıtım” cümlesidir.

---

## 2. Türkiye gerilim kademeleri

**Bu ne?**

| kV | Ne işe yarar |
| --- | --- |
| 400 | Uzun mesafe, büyük santral çıkışı — omurga |
| 154 | Bölge iletimi, büyük tüketim noktaları |
| 66 | Küçük, kalan bir katman; omurga değil ama “yok” sayılmaz |

**Panelde söyle:**  
> Nominal kademeler 400, 154 ve 66 kV. 400 omurga, 154 bölge iletimi.

**Unutma:** 220 kV Türkiye iç omurgası değildir; bazı sınır hatlarında karşı ülkenin gerilimi olabilir.

---

## 3. Örgülü şebeke ve N-1

**Bu ne?**  
İletimde bir noktaya **birden çok yoldan** güç gelebilir (örgü). Bir hat açılınca güç çoğu zaman kaybolmaz, başka yollara kayar.

**N-1:** herhangi **tek** bir eleman (hat, trafo, santral) düşse sistem hâlâ güvenli kalsın.

**Panelde söyle:**  
> İletim örgüldür; dağıtımdaki “hep tek yoldan akar” sezgisi burada yanlış. Analiz N-1’siz eksiktir.

---

## 4. Trafo merkezi (çok kısa)

**Bu ne?**  
Hatların, trafoların, kesicilerin buluştuğu tesis. İçinde: bara, kesici, ayırıcı, ölçü trafosu, koruma, bazen reaktör/kapasitör.

Bara düzeni (tek bara, çift bara…) bakım ve arıza esnekliğini belirler. Yazılım çoğu zaman barayı tek düğüm görür; gerçek hayatta kesici topolojisi daha incedir.

**Panelde söyle:**  
> Modeldeki bara ile sahadaki kesici düzeni aynı şey değildir; topoloji işlemcisi kesici konumundan model üretir.

---

## 5. Reaktör, kapasitör, kademe

**Bu ne?**

| Cihaz | Ne yapar |
| --- | --- |
| Şönt reaktör | Gece / boş hatta gerilimi **aşağı** çeker |
| Şönt kapasitör | Ağır yükte gerilimi **yukarı** destekler |
| OLTC (kademe) | Trafonun yavaş gerilim ayarı; reaktif **üretmez** |

**Panelde söyle:**  
> Hafif yükte Ferranti ile gerilim şişebilir → reaktör. Ağır yükte destek → kapasitör. Hızlı çökmede kademe yetişmez; STATCOM/uyarma yetişir.

---

## 6. FACTS (ne ailesi?)

**Bu ne?**  
Güç elektroniğiyle **gerilimi veya hat akışını hızlı** ayarlayan cihaz ailesi.

| İhtiyaç | Cihaz (isim yeter) |
| --- | --- |
| Gerilim / dinamik reaktif | SVC veya **STATCOM** |
| Hat akışını kaydırmak | Seri cihaz (TCSC / SSSC) |
| Hem P hem Q | UPFC |

**Panelde söyle:**  
> FACTS’i soruna göre seçerim: gerilimde STATCOM/SVC, akışta seri cihaz. Zayıf gerilimde STATCOM, SVC’den daha iyi destek tutar. MAM’ın milli STATCOM’u bu ailedendir.

**Unutma:** Statik “sabit Q kaynağı” modeli dinamik kararı anlatmaz; kontrol modeli gerekir.

---

## 7. HVDC ve enterkonneksiyon

**Bu ne?**  
**HVDC** = yüksek gerilim **doğru akım** bağlantısı. Uzun kablo, uzun mesafe veya **senkron olmayan** iki sistemi bağlamak için.

**Back-to-back:** iki AC sistemi aynı tesiste kısa bir DC halkayla bağlamak.

**Türkiye:**  
- Avrupa (ENTSO-E) ile Yunanistan–Bulgaristan üzerinden **senkron** (aynı frekans, tek ada gibi).  
- Gürcistan tarafı tipik olarak back-to-back HVDC — aynı senkron ada değil.

**Panelde söyle:**  
> Senkron bağlanınca frekans ve rezerv paylaşılır. HVDC ile asenkron bağlanır; frekanslar ayrı kalabilir.

---

## 8. Kayıp, kısıt, planlama

**Bu ne?**  
- **Kayıp:** hattın ısınmasıyla kaybolan enerji.  
- **Kısıt:** ucuz üretim var ama hat dolu; yüke ulaşamıyor.  
- **Yeniden dağıtım:** kısıtı çözmek için üretimin yerini değiştirmek (çoğu zaman daha pahalı).  
- **Master plan:** yıllarca ileriye hangi hat/trafo gerekir diye senaryolar koşmak.

**Panelde söyle:**  
> Kısıt fizik + ekonomi kesişimidir: en ucuz MW her zaman akamaz. Çözüm yeniden dağıtım veya yeni hat olabilir.

---

## 90 saniye

> “İletim 400 ve 154 kV omurgasıdır, örgüldür, N-1 şarttır. Gerilimi reaktör/kapasitör/kademe ve FACTS tutar; dinamikte STATCOM öne çıkar. Avrupa ile senkronuz; bazı komşular HVDC ile bağlanır. Kısıt, ucuz gücün hatta takılmasıdır.”
