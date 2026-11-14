# Gerilim ve reaktif — “bu ne?”

[01’deki](01-Guc-Birim-Sistem-Modeller.md) 2 ve 8 numaralı kartlar. Hesap yok.

## İki sağlık göstergesi

| Göstergе | Nerede aynı? | Ne anlatır? |
| --- | --- | --- |
| Frekans | Bütün ülkede | Üretim–tüketim dengesi (aktif güç) |
| Gerilim | Mahalle mahalle | O bölgede reaktif yeterli mi? |

Frekans düştüyse ülke genelinde üretim yetmiyor olabilir.  
Gerilim düştüyse **o bölgede** reaktif eksiktir; Ankara’daki santral İzmir’in mahallesini tek başına kurtaramayabilir.

## Neden “yerinde üretilir”?

Reaktif güç uzun yolda zayıflar. Uzaktan göndermek zor ve verimsizdir. Bu yüzden kondansatör / STATCOM yükün yakınına konur.

**Benzetme:** Soğuk bir odanın ısısını uzak bir kaloriferle değil, odadaki radyatörle tutarsın.

## Kim ne yapar?

| Araç | Basitçe |
| --- | --- |
| Kondansatör | Ucuz reaktif kaynağı. Gerilim düşünce kendi gücü de zayıflar. |
| Reaktör | Tersine: fazla gerilimi / fazla reaktifi emer (özellikle gece boş hatlarda). |
| STATCOM | Hızlı, zor anda da işe yarar. MAM’ın milli ürünü bu aileden. |
| Trafo kademesi (OLTC) | Gerilimi ayarlar ama reaktif **üretmez**; sorunu öteye kaydırabilir. |
| Generatör uyarma | Santralin kendi barasını tutar. |

**Panelde sık soru:** “Kapasitör mü STATCOM mu?”

> Sürekli ve ucuz ihtiyaçta kondansatör; hızlı / zor / zayıf şebekede STATCOM. Çoğu yerde ikisi birlikte: tabanı kondansatör, dinamik payı STATCOM.

## İletim ile dağıtım farkı (tek fikir)

- Büyük iletim hatlarında gerilimi asıl oynatan reaktif taraftır.
- Ev / alçak gerilim tarafında direnç büyüdüğü için **aktif güç de** gerilimi oynatır. Çatı güneşinin öğlen gerilim yükseltmesi buradan gelir.

## Gece gerilim neden yükselir?

Hat boşken kendi “kapasite” davranışı baskın gelir; uçta gerilim şişebilir. Bu yüzden gece reaktörler devreye alınır.

## 90 saniye

> “Frekans ülke sağlığıdır, gerilim mahalle sağlığıdır. Reaktif uzaktan gelmez, yerinde üretilir. Kondansatör ucuz ama zayıfken düşer; STATCOM hızlıdır. Kademe reaktif üretmez.”
