# Yük akışı

Yük akışı, güç sisteminin statik fotoğrafıdır. Şebekenin belli bir andaki hâlini tek bir çözümle gösterir.

Başka hesapların çoğu bunun etrafında döner:

- güvenlik taraması,
- OPF (Optimal Power Flow, optimal güç akışı),
- planlama,
- durum kestirimi.

“Analiz yazdım” diyorsan bu hesabı tahtada kurabilmen gerekir.

> Sade anlatım: Üretimi ve tüketimi biliyorsun. Yük akışı, bu durumda her baradaki gerilimin ne olacağını ve hatlardan ne kadar güç geçeceğini hesaplar.

## Problem

Bu bölüm, hesaba neyle girdiğini ve neyle çıktığını ayırır.

| | Ne? |
| --- | --- |
| Bilinenler | Şebeke admitansı; yüklerin P'si ve Q'su; gerilim kontrollü baraların P ve \|V\| değeri; bir referans baranın açısı ve gerilimi |
| Bilinmeyenler | Her baranın gerilim büyüklüğü ve açısı; sonra hat akışları, kayıp, üretim reaktifi |

Burada P aktif güç, Q reaktif güç, |V| gerilim büyüklüğü, θ gerilim açısıdır.

Güç dengesi her barada aşağıdaki denklemle yazılır. İlk satır baraya giren aktif gücü, ikinci satır reaktif gücü verir. G ve B, admitansın gerçel ve sanal kısımlarıdır.

```
P_i = V_i Σ_k V_k (G_ik cos θ_ik + B_ik sin θ_ik)
Q_i = V_i Σ_k V_k (G_ik sin θ_ik - B_ik cos θ_ik)
θ_ik = θ_i - θ_k
```

### Ybus

Ybus, bara admitans matrisidir. Akımı gerilime bağlar: `I = Y V`.

- Köşegen dışı eleman: `Y_ik = -y_ik`. Yani iki bara arasındaki seri admitansın eksi işaretlisi.
- Köşegen eleman: o baraya bağlı seri admitansların toplamı artı şönt.

Kademeli trafoda off-nominal oran (nominal dışı dönüştürme oranı) köşegeni bozar. “Sadece hat y’sini yazdım” yetmez.

## Bara tipleri

Her barada dört büyüklük vardır: P, Q, V, θ. Bara tipi, bunlardan hangisinin verildiğini söyler.

| Tip | Bilinen | Bilinmeyen | Fiziksel karşılık |
| --- | --- | --- | --- |
| PQ / yük | P, Q | V, θ | Yük, reaktif limiti dolmuş üretim |
| PV / gerilim kontrollü | P, V | Q, θ | Uyarma kontrollü senkron, STATCOM (Static Synchronous Compensator, statik senkron kompanzatör) yaklaşık |
| Slack / salınım | V, θ | P, Q | Açı referansı ve kayıp dahil güç dengesi |
| İzole | — | — | Enerjisiz ada, hesap ayrı yapılır |

### Slack

Slack bir santral değildir. Kayıpları ve dengesizliği üstlenen matematiksel kaptır.

- Büyük modelde slack’i zayıf bir baraya koymak açıyı ve kaybı çarpıtır.
- Pratikte güçlü bir üretim barası seçilir.
- Birden fazla ada varsa her adaya bir slack gerekir.
- Tek slack ile ıraksama çoğu zaman topoloji hatasıdır.

### PV barasından PQ'ya

PV bara Q limitine çarpınca PQ’ya döner. Bu dönüşüm yapılmazsa gerilim “mükemmel” görünür, reaktif ise fiziksel olarak imkânsız çıkar.

İyi bir yük akışı Q limitini iterasyon içinde denetler. Limit kalkınca barayı tekrar PV yapabilir.

## Newton-Raphson

Denklemler lineer değildir. NR (Newton-Raphson), artık vektörünü Jacobian ile çözer. Artık, verilen güç ile hesaplanan güç arasındaki farktır. Jacobian, gücün açıya ve gerilime göre türevlerinden oluşan matristir.

Aşağıdaki sistem, artığı (sol taraf) açı ve gerilim düzeltmesine (sağdaki vektör) bağlar:

```
[ ΔP ]   [ H  N ] [ Δθ ]
[ ΔQ ] = [ M  L ] [ ΔV/V ]
```

Bloklar:

| Blok | Anlamı |
| --- | --- |
| H | ∂P/∂θ |
| N | ∂P/∂V |
| M | ∂Q/∂θ |
| L | ∂Q/∂V |

Hangi satırlar düşer:

- Slack satır ve sütunları düşer.
- PV barada Q denklemi ve ΔV bilinmeyeni düşer.

### Başlangıç

- Düz (flat) profil çoğu iletim sisteminde yeter: açılar 0, gerilimler 1 pu (per unit, birim değer).
- Ağır yüklü veya dağıtım sisteminde önceki çözümün sıcak başlangıcı daha iyidir.

### Hız ve maliyet

NR yerel kuadratik yakınsar. Güç sisteminde çoğunlukla 3–6 iterasyon yeter.

Her iterasyon Jacobian’ı yeniden kurar ve seyrek lineer sistem çözer. Büyük şebekede maliyet buradadır.

Yoğun matris tersi almak yanlıştır. Seyrek LU (alt-üst üçgen ayrışım) veya KLU sınıfı çözücüler kullanılır.

### Iraksama

Iraksamanın anlamı “çözücü bozuk” olmak zorunda değildir:

- **Çözüm yoktur:** gerilim çökmesi sınırının ötesi, ada, veri hatası (hat empedansı sıfır, paralel hat iki kez).
- **Başlangıç kötüdür:** başlangıç çekim havzasının dışındadır.
- **Kontroller salınıyordur:** kademe, şönt, Q limiti birbirini kovalıyordur. Kontrolleri dondurup önce kontrolsüz çözmek teşhistir.
- **Çok küçük empedans vardır:** bara kuplajı Jacobian’ı hasta eder. Küçük empedanslı kuplaj yerine bara birleştirme daha sağlıklıdır.

## Ayrık hızlı yük akışı

İletimde P–θ ve Q–V zayıf bağlaşır. Yani aktif güç çoğunlukla açıya, reaktif güç çoğunlukla gerilime bağlıdır.

FDLF (Fast Decoupled Load Flow, ayrık hızlı yük akışı) bu yüzden iki ayrı denklem çözer. B’ ve B’’ sabit matrislerdir; her turda yeniden kurulmazlar:

```
B' Δθ = ΔP / V
B'' ΔV = ΔQ / V
```

| Artı | Eksi |
| --- | --- |
| Jacobian her tur kurulmaz, hız kazanılır | Dağıtımda yalan söyler veya ıraksar |
| R/X (direnç/reaktans oranı) küçükken doğruluk iyidir | Ağır yüklü, gerilimi çökmüş sistemde yalan söyler veya ıraksar |

“Her yerde FDLF kullanırım” yanlış cevaptır. İletim tarama motorunda makul, dağıtım fiderinde NR veya süpürme daha doğrudur.

## DC yük akışı

DC yük akışı, AC (alternatif akım) şebekenin doğrusallaştırılmış aktif güç modelidir. Varsayımları:

- açılar küçük,
- gerilimler 1 pu,
- direnç ve şönt ihmal.

Bu varsayımlarla güç denklemi tek bir lineer bağıntıya iner. x hat reaktansıdır:

```
P = B θ ,   B_ik = -1/x_ik
```

| Kaybettiğin | Kazandığın |
| --- | --- |
| Kayıp yoktur | Lineerdir |
| Reaktif yoktur | Binlerce beklenmeyen durum saniyede taranır |
| Gerilim yoktur | PTDF ve LODF bu modelden gelir |

PTDF (güç transfer dağıtım faktörü) ve LODF (hat açılma dağıtım faktörü) bu lineer modelden gelir.

Güvenlik taramasının eleği çoğu zaman DC’dir. Elekten geçen ağır durumlar AC ile doğrulanır.

DC sonucu gerilim ihlali söylemez. Bunu unutmak, tarama motorunun kör noktasıdır.

## Dağıtım yük akışı

Radyal fider, kaynaktan uca ağaç gibi dallanan, halka içermeyen hattır. Radyal fiderde geri-ileri süpürme (backward-forward sweep) kullanılır:

1. Uçtan kaynağa akım veya güç topla. Bu adım her hattan geçen yükü bulur.
2. Kaynaktan uca gerilimi güncelle. Bu adım bulunan akımlarla gerilim düşümünü hesaplar.
3. Gerilim ve güç artık bitene kadar tekrarla. Bu adım iki tahminin birbirine oturmasını sağlar.

Ybus-NR ile karşılaştırma:

- Ybus-NR radyal zayıf şebekede de çalışır.
- Süpürme daha az bellek ister ve dengesiz modele daha doğal oturur.
- Kapalı halka varsa süpürme kırılır. Zayıf döngüler için telafi akımı kullanılır veya NR’ye dönülür.

Üç faz dengesiz modelde her hat 3×3 veya 4×4 empedans matrisidir (fazlar ve nötr).

Kariyer paketi “dengeli” kutusunu sessizce işaretli bırakıyorsa sonucu fider ucuna uygulamadan önce bunu söyle.

## Devam gücü akışı

Yükü λ ile ölçekleyip her adımda yük akışı çözmek, PV eğrisini çıkarır. PV eğrisi, yük arttıkça gerilimin nasıl düştüğünü gösteren eğridir.

- Burun noktasında Jacobian tekildir, düz NR ıraksar.
- Devam yöntemi burun noktasını öngör-düzelt ile döner.
- Gerilim kararlılığı marjı “buruna kaç MW var” sorusudur. Ayrıntı `08` içindedir.

Yük akışı ıraksadı diye “kararsız” deme. Önce veri ve ada kontrolü, sonra burun noktası.

## Dağıtım faktörleri

| Faktör | Sorduğu soru |
| --- | --- |
| PTDF | A barasından B barasına 1 MW transfer, her hatta kaç MW ekler? |
| LODF | Bir hat açılırsa akışı diğer hatlara nasıl dağılır? |

İkisi de DC modelin hızlı çocuklarıdır.

N-1 taraması, her seferinde tek bir elemanın devre dışı kaldığı durumları tek tek denemektir. Bunu her seferinde baştan faktörize etmeden yapmak LODF ile mümkündür.

AC doğrulama şarttır. Özellikle gerilim ve Q limiti devreye girince lineer faktör şaşar.

## İşletme dili

Çıktıyı şöyle okursun:

- Gerilimler planlama veya işletme bandında mı?
- Hat ve trafo yükü termik limite göre yüzde kaç?
- Üretim reaktifi limite mi yapışmış?
- Kayıp ve slack gücü makul mü? Slack, modeldeki dengesizliğin aynasıdır.
- Hangi kontrol limitte? Limitteki kontrol, bir sonraki MW’nin daha pahalıya mal olacağı yerdir.

Aşağıdaki metin, bu sayfanın mülakatta yüksek sesle söylenecek özetidir.

## 90 saniye

> Mülakatta şöyle söyle: “Yük akışı, P ve Q bilinen baralardan gerilim ve açıyı bulur. Slack referans ve kayıp kaptır. Newton-Raphson Jacobian’ın H N M L bloklarıyla çözer; Q limiti dolan PV bara PQ olur. İletimde ayrık hızlı ve DC tarama hızlıdır, gerilimi DC görmez. Dağıtımda R büyük olduğu için süpürme veya tam AC, mümkünse üç faz gerekir. Iraksama her zaman çözücü hatası değildir; ada, veri ve burun noktası ayrı ayrı bakılır.”
