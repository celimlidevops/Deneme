# Yük modelleri, trafo bağlantı grupları, sıfır bileşen yolu

## Yük modelleri

Yük akışında yükü "100 MW" diye yazarız. Gerçekte yükün çektiği güç gerilime bağlıdır. Üç saf davranış vardır:

| Model | Güç nasıl değişir | Örnek cihaz |
| --- | --- | --- |
| Sabit empedans (Z) | `P ∝ V²` | Rezistanslı ısıtıcı, akkor lamba |
| Sabit akım (I) | `P ∝ V` | Bazı aydınlatma ve elektronik |
| Sabit güç (P) | `P` sabit | Motor sürücüleri, güç elektroniği, şarj cihazı |

Gerçek yük bunların karışımıdır. ZIP modeli (Z, I ve P harflerinden gelir) üçünü ağırlıklandırır.

Aşağıdaki blokta `P₀` nominal güç, `V₀` nominal gerilim, `a_z`, `a_i`, `a_p` üç davranışın payıdır. Paylar toplamı 1'dir.

```
P = P₀ [ a_z (V/V₀)² + a_i (V/V₀) + a_p ]      a_z + a_i + a_p = 1
```

Reaktif güç için ayrı katsayılar vardır.

Üstel model aynı şeyi tek üsle yazar: `P = P₀ (V/V₀)^α`.

| `α` | Karşılığı |
| --- | --- |
| 2 | Sabit empedans |
| 1 | Sabit akım |
| 0 | Sabit güç |

### Elle örnek

Nominalde 100 MW çeken yük, gerilim 0,95 pu'ya düşünce:

- Sabit empedans: `100 × 0,95² = 90,25 MW`. Bu satır, gücü gerilimin karesiyle ölçekler.
- Sabit akım: `100 × 0,95 = 95,00 MW`. Bu satır, gücü gerilimle doğrusal ölçekler.
- Sabit güç: `100 MW`. Bu satır, gerilim ne olursa olsun gücü sabit tutar.

Sabit güç yükü, gerilim düşünce akımını **artırır** (`I = P/V`). Bu, gerilimi daha da düşürür. Sabit empedans yükü ise kendiliğinden hafifler ve sisteme yardım eder.

### Neden önemli

- Gerilim kararlılığında sabit güç varsayımı kötümser, sabit empedans iyimser sonuç verir. Hangisini kullandığını söylemeden "sistem çöker" veya "çökmez" denmez.
- Modern yük (evirici, sürücü, LED, şarj) sabit güce kayıyor. Şebeke eskisine göre daha az "kendiliğinden toparlanıyor".
- Motor yükü ayrıca dinamiktir: gerilim düşünce yavaşlar, durma noktasına gelirse nominalin birkaç katı reaktif çeker. Arıza sonrası gerilimin geç toparlanmasının nedeni budur.
- Yük frekansa da bağlıdır: frekans %1 düşünce yük yaklaşık %1–2 azalır. Buna yük sönümü denir ve frekans kararlılığına yardım eder.
- CVR (Conservation Voltage Reduction, gerilimi bilinçli düşürerek tüketimi azaltma), yükün sabit empedans payı kadar çalışır.

Planlama yük akışında varsayılan sabit güçtür. Dinamik çalışmada ZIP veya motor modeli şarttır.

## Trafo bağlantı grupları

Trafonun iki sargısı yıldız (Y) veya üçgen (D) bağlanabilir. Plakadaki gösterim şöyle okunur:

| İşaret | Anlamı |
| --- | --- |
| Büyük harf | Yüksek gerilim sargısı |
| Küçük harf | Alçak gerilim sargısı |
| `N` veya `n` | Nötrün dışarı çıkarıldığı |
| Sondaki sayı | Saat açısı. Her saat 30°'dir |

Yaygın gruplar:

- **Dyn11:** yüksek taraf üçgen, alçak taraf nötrü çıkarılmış yıldız, alçak taraf 30° ileride. Dağıtım trafosunun standart grubudur.
- **YNd11:** santral yükseltici trafolarında yaygın.
- **YNyn0:** iletim ototrafolarında, çoğunlukla üçgen bağlı üçüncü (tersiyer) sargıyla.

Saat açısı neden önemli: iki trafo paralel çalışacaksa aynı saat grubunda olmalıdır. Farklı grupta iki sekonder arasında sürekli gerilim farkı ve büyük dolaşım akımı oluşur.

Dengeli yük akışında bu 30° kayma göz ardı edilebilir. Koruma ve dengesiz analizde edilemez.

## Sıfır bileşen yolu

Simetrik bileşenlerde sıfır dizi, üç fazda aynı yönde akan akımdır. Üç faz aynı anda aynı yöne akıyorsa bir dönüş yolu lazımdır: toprak veya nötr.

Kural tek cümledir: **sıfır bileşen akımı, ancak topraklanmış bir yıldız noktası varsa akar. Üçgen sargı onu dışarı vermez, içinde dolaştırır.**

| Bağlantı | Sıfır bileşen davranışı |
| --- | --- |
| YNyn (iki nötr de topraklı) | İki taraf arasında geçer |
| YNd | Yıldız tarafında toprağa yol verir, üçgen tarafına geçmez |
| Dyn | Alçak taraf arızasında yol verir, yüksek tarafa geçmez |
| Yy (nötrler topraksız) | Hiç geçmez |
| Dd | Hiç geçmez |
| Yd (yıldız topraksız) | Hiç geçmez |

Nötr bir empedans `Z_n` üzerinden topraklanmışsa sıfır dizi devresine `3 Z_n` olarak girer. Üç katı olmasının nedeni, nötrden üç fazın sıfır akımının toplamının (`3 I₀`) geçmesidir.

### Elle örnek

34,5 kV fider, Dyn11 dağıtım trafosuyla 0,4 kV'a iniyor. Alçak gerilim tarafında bir faz toprağa değdi.

1. Alçak taraf yıldızdır ve nötrü topraklıdır. Sıfır bileşen akımı akar, arıza akımı büyüktür, sigorta veya şalter açar. Bu adım, arıza tarafında sıfır dizi yolunun açık olduğunu gösterir.
2. Yüksek taraf üçgendir. 34,5 kV tarafındaki toprak rölesi bu arızayı **görmez**. Aynı arıza 34,5 kV'ta faz-faz akımı gibi görünür. Bu adım, üçgen sargının sıfır diziyi diğer tarafa geçirmediğini gösterir.

Sonuç: her gerilim seviyesinin toprak koruması kendi içinde koordine edilir. Bu, Dyn bağlantısının bilinçli bir faydasıdır.

## Yaygın yanlış

- **"Yük sabittir."** Yük akışı varsayımıdır, fizik değildir.
- **"Gerilim düşünce yük hep azalır."** Sabit güç yükü azalmaz, akımı artar.
- **"Üçgen sargı sıfır bileşeni yok eder."** Yok etmez; içinde dolaştırır ve diğer tarafa geçirmez. Yıldız tarafı için düşük empedanslı bir yol oluşturur.
- **"Yıldız bağlantı her zaman sıfır bileşen geçirir."** Yalnızca nötrü topraklıysa.
- **"Saat açısı yalnızca plakada duran bir bilgidir."** Paralel çalışmada ve diferansiyel korumada doğrudan sonuç değiştirir.

## Panel takip sorusu

"Kısa devre yazılımında tek faz-toprak akımı sıfır çıkıyor, neden?"

> Mülakatta şöyle söyle: "Sıfır dizi yolu kapalıdır. Trafo grubu yanlış girilmiştir, nötr topraklaması eksiktir veya sıfır dizi empedansı boş bırakılmıştır."

"Gerilim kararlılığı çalışmasında hangi yük modelini seçersin?"

> Mülakatta şöyle söyle: "Ölçüme dayalı ZIP varsa onu. Yoksa sabit güç ile sabit empedans arasında iki uç senaryo koşar, sonucun hangi varsayıma duyarlı olduğunu raporlarım."

Aşağıdaki metin, bu sayfanın tamamını mülakatta 90 saniyede anlatmak içindir.

## 90 saniye

> "Yük gerilime bağlıdır. Sabit empedans gerilimin karesiyle, sabit akım gerilimle değişir, sabit güç değişmez; ZIP üçünün karışımıdır. Sabit güç yükü gerilim düşünce akımını artırdığı için kararlılıkta en zor olanıdır. Trafoda bağlantı grubu iki şeyi belirler: saat açısı paralel çalışmayı, yıldız ve üçgen sıfır bileşen yolunu. Sıfır bileşen akımı yalnızca topraklı yıldız noktasından akar; üçgen onu diğer tarafa geçirmez. Bu yüzden dağıtımdaki Dyn trafosu, alçak gerilim toprak arızasını orta gerilimden ayırır."
