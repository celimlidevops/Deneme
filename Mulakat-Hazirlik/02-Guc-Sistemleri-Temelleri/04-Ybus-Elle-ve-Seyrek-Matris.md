# Ybus matrisi: elle kurulum ve seyrek yapı

Ybus (bara admitans matrisi), şebekenin kendisidir. Yük akışı, kısa devre, durum kestirimi ve güvenlik analizi aynı matrisi kullanır.

Mülakatta "üç baralı bir şebekenin Ybus'unu yaz" sorusu, temel bilgisini ölçmenin en kısa yoludur.

## Tanım

Her bara için Kirchhoff akım yasası yazılır: baraya giren akım, o baradan hatlara çıkan akımların toplamıdır. Bunu bütün baralar için matrisle yazınca tek denklem çıkar:

```
I = Y V
```

| Sembol | Anlamı |
| --- | --- |
| `I` | Bara enjeksiyon akımları (baraya dışarıdan verilen akım) |
| `V` | Bara gerilimleri |
| `Y` | Bara admitans matrisi |

Kurulum iki kuraldan ibarettir:

- **Köşegen dışı:** `Y_ik = −y_ik`. İki bara arasındaki hattın admitansının eksilisi. Hat yoksa sıfır.
- **Köşegen:** `Y_ii`, o baraya bağlı bütün admitansların toplamı. Hatlar, hat şöntleri, kapasitör, reaktör dahil.

Önce empedansı admitansa çevirirsin: `y = 1/z`. Saf reaktans için `1/(jx) = −j/x`.

## Elle örnek: üç bara

Hatlar (direnç ihmal): `z12 = j0,10`, `z13 = j0,20`, `z23 = j0,25` pu.

Adım 1, admitanslar. Bu adım, her hattın empedansını `1/(jx) = −j/x` kuralıyla admitansa çevirir.

```
y12 = 1/(j0,10) = −j10
y13 = 1/(j0,20) = −j5
y23 = 1/(j0,25) = −j4
```

Adım 2, köşegen dışı (eksilisi). Bu adım, iki bara arasındaki admitansın işaretini çevirip matrisin simetrik iki hücresine yazar.

```
Y12 = Y21 = +j10
Y13 = Y31 = +j5
Y23 = Y32 = +j4
```

Adım 3, köşegen (bağlı olanların toplamı). Bu adım, her baraya dokunan bütün hat admitanslarını toplar.

```
Y11 = y12 + y13 = −j15
Y22 = y12 + y23 = −j14
Y33 = y13 + y23 = −j9
```

Sonuç. Bu blok, üç adımın çıktısını tek matriste birleştirir.

```
        [ −j15   j10    j5  ]
Ybus =  [  j10  −j14    j4  ]
        [  j5    j4    −j9  ]
```

Kontrol: şönt eleman yoksa her satırın toplamı sıfırdır. −15 + 10 + 5 = 0. Tuttu.

Bu kontrol, elle kurulumda hata yakalamanın en hızlı yoludur.

## Dirençli hat ve şönt

Gerçek hatta direnç vardır: `z = 0,02 + j0,10`.

Aşağıdaki blok bu hattın admitansını hesaplar. Ortadaki adım, pay ve paydayı eşlenikle çarpıp paydayı gerçek sayı yapar.

```
y = 1/(0,02 + j0,10) = (0,02 − j0,10) / (0,02² + 0,10²) = 1,923 − j9,615
```

Eşlenikle çarpıp paydayı gerçek yaparsın. Gerçek kısım iletkenlik `G`, sanal kısım süseptans `B`'dir. `Y = G + jB`.

Hattın kapasitesi π modelinde iki uca yarı yarıya şönt olarak konur:

- Toplam şönt `jb` ise her iki uçtaki baranın köşegenine `jb/2` eklenir.
- Köşegen dışına eklenmez.
- O zaman satır toplamı artık sıfır olmaz; kalan değer baranın toprağa şöntüdür.

Kademeli trafoda (oran `t`), seri admitans `y` ise:

| Hücre | Değer |
| --- | --- |
| Kademe tarafındaki köşegen | `y/t²` |
| Diğer köşegen | `y` |
| Köşegen dışları | `−y/t` |

Kademe 1,0 iken sıradan bir hatla aynıdır.

## Seyrek matris

Gerçek şebekede bir bara ortalama 2–4 komşuya bağlıdır.

On bin baralı sistemde:

- Matrisin 100 milyon hücresi vardır.
- Sıfırdan farklı olan yaklaşık 40 bin tanesidir.
- Doluluk on binde dörttür.

Yazılım sonucu:

- Yoğun (dense) saklarsan 100 milyon karmaşık sayı, yaklaşık 1,6 GB eder. Seyrek saklarsan bir megabaytın altındadır.
- Yoğun çarpanlara ayırma `n³` ile, seyrek çözücü yaklaşık `n` ile büyür. Fark, saatler ile milisaniyeler arasıdır.
- Biçimler: kurarken koordinat listesi (COO, Coordinate), çözerken sıkıştırılmış satır veya sütun (CSR, Compressed Sparse Row; CSC, Compressed Sparse Column).
- Matrisin tersi alınmaz. Tersi yoğundur, yani seyrekliği yok eder. Bunun yerine LU çarpanları (alt üçgen L ve üst üçgen U matrisleri) saklanır ve her sağ taraf için ileri-geri yerine koyma yapılır.
- Çarpanlara ayırırken yeni sıfır olmayanlar oluşur (fill-in). Satır ve sütunları akıllı sıralamak (minimum derece, AMD, Approximate Minimum Degree) bunu azaltır.
- Güç sistemi için özel olarak yazılmış çözücü KLU'dur.

Python karşılığı:

- Matrisi tutmak için `scipy.sparse.csr_matrix`.
- Çözmek için `scipy.sparse.linalg.spsolve`.
- Çarpanları saklamak için `splu`.

`14-Programlama/ornekler/nr_yuk_akisi.py` çözümü `spsolve` ile yapar.

Ybus ayrıca simetriktir (faz kaydırıcı trafo yoksa).

Zbus (bara empedans matrisi), Ybus'un tersidir. Yoğundur ve kısa devre hesabında yalnızca gereken sütunu hesaplanır.

## Yaygın yanlış

- **"Köşegen dışı elemanlar pozitif admitanstır."** Hayır, eksilisidir. İşaret hatası en sık yapılan hatadır.
- **"Hat şöntü köşegen dışına da girer."** Hayır, yalnız köşegene.
- **"Ybus'un tersini alıp gerilimi bulurum."** Küçük örnekte olur, gerçek sistemde bellek ve süre patlar. Çarpanlara ayır, yerine koy.
- **"İki bara arasında bağlantı yoksa küçük bir değer yazarım."** Sıfır yazılır. Tersine, kesiciyi çok küçük empedansla modellemek matrisi sayısal olarak hasta eder; iki barayı birleştirmek doğrusudur.
- **"Ybus topolojiden bağımsızdır."** Bir kesici açıldığında değişir. N-1 analizinde (her seferinde bir elemanın devre dışı kaldığı senaryolar) her arıza için baştan kurmak yerine düşük ranklı güncelleme veya LODF (Line Outage Distribution Factor, hat açılma dağılım katsayısı) kullanılır.

## Panel takip sorusu

"Bir hat devre dışı kalırsa Ybus'ta ne değişir?"

> Mülakatta şöyle söyle: "Dört eleman. İki köşegenden `y` çıkar, iki köşegen dışı sıfırlanır. Bütün matrisi yeniden çarpanlara ayırmadan düşük ranklı güncelleme yapılabilir."

"Satır toplamı ne zaman sıfır olmaz?"

> Mülakatta şöyle söyle: "Toprağa şönt varsa: hat kapasitesi, kapasitör, reaktör, nominalden farklı kademe."

Aşağıdaki metin, bu sayfanın tamamını mülakatta 90 saniyede anlatmak içindir.

## 90 saniye

> "Ybus, akım eşittir admitans çarpı gerilim denkleminin matrisidir. Köşegen dışına iki bara arasındaki admitansın eksilisini, köşegene o baraya bağlı bütün admitansların toplamını yazarım; şöntler yalnız köşegene girer. Şönt yoksa satır toplamı sıfırdır, bu benim hata kontrolümdür. Matris seyrektir, çünkü bir bara birkaç komşuya bağlıdır. Tersini almam; seyrek LU çarpanlarını saklar, her çözümde yerine koyma yaparım."
