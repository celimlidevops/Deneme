# Newton-Raphson'ı sıfırdan yazmak

Bu sayfa beş konuyu anlatır: canlı kodlama, seyrek çözücü, sayısal kararlılık, test ve CI (Continuous Integration, sürekli entegrasyon). Hepsi tek bir işin etrafında döner: yük akışını Newton-Raphson (NR) yöntemiyle sıfırdan yazmak.

**Yük akışı**, şebekedeki her baranın gerilim genliğini ve açısını, verilen üretim ve yüke göre hesaplamaktır. **Bara**, hatların, trafoların, üreticilerin ve yüklerin birleştiği düğümdür. **Newton-Raphson**, doğrusal olmayan denklemleri, her turda doğrusal bir yaklaşım çözerek adım adım çözen yöntemdir.

## Bu neden senin kartın

Bu senin en güçlü kartın.

Panelde güç sistemi bilgisi senden fazla olan çok aday olacak. Ama yük akışını test edilebilir, okunur ve hatasını söyleyen bir kod olarak yazabilen az aday olacak.

Bu sayfanın hedefi: 20 dakikada, bakmadan, konuşarak yazmak.

## Dosyalar

Dosyalar `14-Programlama/ornekler` klasöründe:

| Dosya | Ne |
| --- | --- |
| `nr_canli_kodlama.py` | 59 satır, çekirdeği 35. Canlı kodlamada yazacağın sürüm: seyrek Ybus + Newton |
| `nr_yuk_akisi.py` | Tam sürüm: açık ve vektörel Jacobian, Q limiti, hata sınıfı |
| `test_ornekler.py` | 7 test |
| `elle_ornekler.py` | Notlardaki bütün elle örneklerin sayısal doğrulaması |

Tablodaki terimler:

- **Ybus:** bara admitans matrisi. Hangi baranın hangisine hangi admitansla (empedansın tersi) bağlı olduğunu tutar.
- **Seyrek:** matrisin yalnız sıfır olmayan elemanlarını saklamak. Şebekede her bara yalnız birkaç komşusuna bağlı olduğu için matrislerin çoğu sıfırdır.
- **Jacobian:** güç denklemlerinin açıya ve gerilime göre türevlerinden oluşan matris. Newton'un her adımı bu matrisle çözülür.
- **Açık ve vektörel Jacobian:** aynı matrisin iki yazımı. Açık olan eleman eleman formülle, vektörel olan dizi işlemleriyle kurulur.
- **Q limiti:** üreticinin verebileceği reaktif gücün (Q) sınırı.
- **Hata sınıfı:** yakınsama olmadığında fırlatılan özel hata türü.

Hepsi bu makinede çalıştırıldı (Python 3.14, NumPy 2.3, SciPy 1.17); 7 test geçiyor.

## Yazmadan önce söyleyeceklerin

Canlı kodlamada ilk iki dakika kod yazma. Sözleşmeyi söyle.

**Sözleşme**, kodun hangi varsayımlarla çalıştığının açık listesidir: birimler, işaretler, indisler, girdiler. Yanlış varsayımı kodun ortasında fark etmek pahalıdır.

> **Mülakatta şöyle söyle:**
>
> 1. "Her şey per-unit, açılar radyan."
> 2. "Enjeksiyon üretimde pozitif, yükte negatif."
> 3. "Bara indisleri sıfırdan başlıyor."
> 4. "Bir salınım barası var; PV ve PQ listelerinde yok."
> 5. "Önce Ybus, sonra güç artığı, sonra Jacobian, sonra çözüm ve güncelleme. Sonunda iki baralı analitik örnekle sınarım."

Bu cümlelerdeki terimler:

| Terim | Anlamı |
| --- | --- |
| Per-unit (pu) | Birim değer. Her büyüklük seçilmiş bir baz değere bölünür |
| Radyan | Açı birimi. 180 derece = π radyan |
| Enjeksiyon | Bir baradan şebekeye verilen net güç (üretim eksi yük) |
| Salınım barası | Gerilim genliği ve açısı sabit tutulan referans bara. Kayıpları o karşılar |
| PV barası | Aktif gücü (P) ve gerilim genliği (V) verilen bara; genelde üretici |
| PQ barası | Aktif (P) ve reaktif (Q) gücü verilen bara; genelde yük |
| Güç artığı | Verilen güç ile o anki gerilimlerden hesaplanan güç arasındaki fark |
| Analitik örnek | Kapalı formülle elde çözülebilen, sonucu kesin bilinen örnek |

## İskelet: altı adım

Aşağıdaki blok, kodun tamamının sözle planıdır. Canlı kodlamada bunu önce yorum satırı olarak yazarsın, sonra her satırın altını doldurursun.

Adımların görevi:

1. **Ybus kur:** şebekenin bağlantı ve admitans bilgisini tek matrise koyar.
2. **Hesaplanan güç:** o anki gerilimlerle her baranın gücünü bulur.
3. **Artık:** verilen güçle hesaplanan güç arasındaki farkı alır.
4. **Durma ölçütü:** fark yeterince küçükse çözüm bulunmuştur.
5. **Doğrusal çözüm:** Jacobian ile düzeltme miktarını (Δx) bulur.
6. **Güncelleme:** açıları (θ) ve gerilimleri (V) düzeltir, tekrar 2. adıma döner.

```
1. Ybus kur
2. S = V · conj(Ybus · V)                      hesaplanan güç
3. artık = [P_verilen − P_hesap ; Q_verilen − Q_hesap]
4. |artık| < tolerans ise bitir
5. J · Δx = artık çöz
6. θ ve V'yi güncelle, 2'ye dön
```

`conj` karmaşık eşleniktir (sanal kısmın işaretini çevirir). `J` Jacobian'dır.

## Kod

Aşağıdaki blok `nr_canli_kodlama.py`'nin çekirdeğidir. İki fonksiyon var:

- `ybus(n, hatlar)`: hat listesinden seyrek Ybus matrisini kurar.
- `yuk_akisi(...)`: Newton döngüsünü koşar. Yakınsarsa gerilimleri, açıları ve tur sayısını döndürür; yakınsamazsa hata fırlatır.

İçe aktarılan araçlar:

- `coo_matrix`: COO (Coordinate, koordinat) biçiminde seyrek matris. Her eleman (satır, sütun, değer) üçlüsüyle verilir.
- `diags`: köşegen matris kurar.
- `bmat`: seyrek blokları tek bir seyrek matriste birleştirir.
- `spsolve`: seyrek doğrusal sistemi çözer.

`nr_canli_kodlama.py`'nin çekirdeği:

```python
import numpy as np
from scipy.sparse import bmat, coo_matrix, diags
from scipy.sparse.linalg import spsolve


def ybus(n, hatlar):
    """hatlar: (i, j, r, x) listesi. Aynı hücreye düşen girdileri COO kendisi toplar."""
    i, j, r, x = (np.array(sutun) for sutun in zip(*hatlar))
    y = 1 / (r + 1j * x)
    satir, sutun = np.r_[i, j, i, j], np.r_[i, j, j, i]
    return coo_matrix((np.r_[y, y, -y, -y], (satir, sutun)), shape=(n, n)).tocsc()


def yuk_akisi(y, p, q, pv, pq, v0, tol=1e-8, azami=20):
    """p, q: net enjeksiyon. pv, pq: bara indisleri; salınım barası ikisinde de yok."""
    v, teta = v0.astype(float).copy(), np.zeros(len(v0))
    pvpq = np.r_[pv, pq].astype(int)
    for tur in range(azami):
        vc = v * np.exp(1j * teta)
        akim = y @ vc
        s = vc * np.conj(akim)
        artik = np.r_[p[pvpq] - s.real[pvpq], q[pq] - s.imag[pq]]
        if np.max(np.abs(artik)) < tol:
            return v, teta, tur

        ds_dteta = (1j * diags(vc) @ (diags(akim) - y @ diags(vc)).conj()).tocsr()
        ds_dv = (diags(vc) @ (y @ diags(vc / v)).conj() + diags(akim.conj() * vc / v)).tocsr()
        jac = bmat(
            [
                [ds_dteta.real[pvpq][:, pvpq], ds_dv.real[pvpq][:, pq]],
                [ds_dteta.imag[pq][:, pvpq], ds_dv.imag[pq][:, pq]],
            ],
            format="csc",
        )
        dx = spsolve(jac, artik)
        teta[pvpq] += dx[: len(pvpq)]
        v[pq] += dx[len(pvpq) :]
    raise RuntimeError(f"{azami} turda yakınsamadı, son artık {np.max(np.abs(artik)):.2e}")
```

Üç baralı örnekte 4 turda yakınsar: `V = [1,0  1,02  0,9515]`.

Yani 1. bara (salınım) 1,0 pu, 2. bara 1,02 pu, 3. bara 0,9515 pu gerilimde kalır.

### Satır satır neyi savunacaksın

Panel her satırın nedenini sorabilir. Hazır cevaplar:

- **`ybus`, COO biçimi.** Her hat dört girdi üretir: iki köşegen (`+y`), iki köşegen dışı (`−y`). COO aynı hücreye düşen değerleri toplar; köşegeni elle biriktirmek gerekmez. Kurarken COO, çözerken CSC (Compressed Sparse Column, sıkıştırılmış seyrek sütun).
- **`s = vc * conj(y @ vc)`.** `S = V I*` ve `I = Y V`. Bütün güç denklemleri bu tek satırdır. Burada `S` karmaşık güç, `I` akım, `I*` akımın eşleniğidir.
- **Artık vektörü.** Önce PV ve PQ baraların aktif gücü, sonra yalnız PQ baraların reaktif gücü. Bilinmeyenlerin sırası da aynıdır: açılar, sonra gerilimler. PV barasının gerilimi zaten verildiği için onun reaktif gücü denkleme girmez.
- **Jacobian.** Karmaşık gücün açıya ve gerilime göre türevi matris biçiminde yazılır; gerçek kısım `∂P`, sanal kısım `∂Q` bloklarını verir. `bmat` blokları seyrek olarak birleştirir. Türetimi hatırlamıyorsan söyle ve `nr_yuk_akisi.py`'deki açık formüllü (`H`, `N`, `M`, `L`) sürümü yaz; ikisinin aynı matrisi verdiğini bir test doğruluyor.
- **`spsolve`.** Matrisin tersini almıyorum; seyrek LU ile çözüyorum. LU ayrışması, matrisi bir alt üçgen (L, lower) ve bir üst üçgen (U, upper) matrisin çarpımına ayırır; sistem bu iki üçgenle hızlıca çözülür.
- **Son satır.** Yakınsamadıysa sessizce sonuç dönmüyorum; son artığı söyleyen bir hata fırlatıyorum.

`H`, `N`, `M`, `L` Jacobian'ın dört bloğudur: sırasıyla P'nin açıya, P'nin gerilime, Q'nun açıya ve Q'nun gerilime göre türevleri.

### Jacobian'ı unutursan

Panik yapma. Üç seçenek var, tercih sırasıyla:

1. **Açık formüller** (`05/02` dosyası): köşegen `H_ii = −Q_i − B_ii V_i²` ve diğerleri. Çift döngüyle yaz, "bunu sonra vektörleştiririm" de. Burada `B_ii`, Ybus'un köşegen elemanının sanal kısmıdır (süseptans).
2. **Sayısal türev:** her bilinmeyeni `1e-6` oynat, artığın değişimini ölç. Yavaş ama doğru; "doğrulama için kullanırım, üretimde analitik olanı" de.
3. **DC yük akışına düş:** `P = B θ`, tek doğrusal çözüm. "Zamanım kalırsa AC'ye genişletirim" de. DC (Direct Current, doğru akım) yük akışı, AC (Alternating Current, alternatif akım) denklemlerinin doğrusallaştırılmış yaklaşımıdır; gerilimleri 1 pu kabul edip yalnız açıları çözer.

Hangisini seçtiğini ve nedenini söylemek, formülü ezberden yazmaktan değerlidir.

## Seyrek çözücüler

Seyrek doğrusal sistem (`A x = b`) için ihtiyaca göre farklı araç seçilir:

| İhtiyaç | SciPy aracı | Not |
| --- | --- | --- |
| Tek seferlik çözüm | `spsolve(A, b)` | Arkada SuperLU (veya kuruluysa UMFPACK) |
| Aynı matris, çok sağ taraf | `lu = splu(A)` sonra `lu.solve(b)` | Çarpanlara ayırma bir kez; N-1 taraması, hızlı ayrık yük akışı, PTDF |
| Simetrik pozitif tanımlı | Cholesky (`scikit-sparse`, CHOLMOD) | DC model `B` matrisi, durum kestirimi kazanç matrisi |
| Çok büyük, ön koşullu | `gmres`, `bicgstab`, `cg` | Yinelemeli; güç sistemi matrislerinde iyi ön koşullayıcı şart |

Tablodaki adlar:

| Ad | Anlamı |
| --- | --- |
| SuperLU, UMFPACK | Seyrek LU ayrışması yapan hazır kütüphaneler. UMFPACK: Unsymmetric MultiFrontal Package |
| Sağ taraf | `A x = b` denklemindeki `b` vektörü |
| N-1 taraması | Şebekedeki elemanların her birini tek tek devre dışı bırakıp sonucu inceleme |
| Hızlı ayrık yük akışı | Fast decoupled load flow; P-açı ve Q-gerilim denklemlerini ayırıp sabit matrislerle çözen hızlı yöntem |
| PTDF | Power Transfer Distribution Factor, güç aktarım dağılım katsayısı. Bir baradan diğerine aktarılan gücün her hatta ne kadar akış yarattığını verir |
| Simetrik pozitif tanımlı | Kendi devriğine eşit ve bütün özdeğerleri pozitif matris. Cholesky ayrışmasına uygundur |
| Cholesky, CHOLMOD | Cholesky, simetrik pozitif tanımlı matrisi `L Lᵀ` olarak ayırır. CHOLMOD bunun seyrek kütüphanesidir; `scikit-sparse` ile Python'dan kullanılır |
| Kazanç matrisi | Durum kestiriminde (WLS: Weighted Least Squares, ağırlıklı en küçük kareler) çözülen normal denklem matrisi |
| `gmres`, `bicgstab`, `cg` | Yinelemeli çözücüler: GMRES (Generalized Minimal Residual), BiCGSTAB (Biconjugate Gradient Stabilized), CG (Conjugate Gradient, eşlenik gradyan) |
| Ön koşullayıcı | Sistemi yinelemeli çözücünün daha hızlı yakınsayacağı hale getiren yardımcı matris |

### Bilmen gereken kavramlar

- **Dolgu (fill-in):** çarpanlara ayırırken sıfır olan yerler dolar. Satır ve sütun sıralaması (AMD, COLAMD) dolguyu azaltır. Güç sistemi matrisleri için KLU bu işi en iyi yapan çözücüdür. AMD: Approximate Minimum Degree; COLAMD: Column Approximate Minimum Degree; ikisi de dolguyu azaltan sıralama yöntemidir. KLU, devre ve güç sistemi gibi çok seyrek matrisler için yazılmış seyrek LU çözücüsüdür.
- **Simgesel ve sayısal ayrışma:** seyreklik deseni değişmiyorsa sıralama ve bellek planı (simgesel kısım) bir kez yapılır; her turda yalnız sayılar yenilenir. Newton turlarında desen aynıdır. **Seyreklik deseni**, sıfır olmayan elemanların yerleridir.
- **Düşük ranklı güncelleme:** bir hat açılınca matris dört elemanda değişir. Baştan çarpanlara ayırmak yerine Sherman-Morrison-Woodbury ile mevcut çarpanlar kullanılır. LODF bunun kapalı biçimidir. LODF (Line Outage Distribution Factor, hat açılma dağılım katsayısı), bir hat açılınca akışının diğer hatlara nasıl dağıldığını verir.
- **Biçim dönüşümü:** COO kurmak için, CSR satır dilimlemek ve matris-vektör çarpımı için, CSC sütun dilimlemek ve doğrudan çözücüler için. CSR: Compressed Sparse Row, sıkıştırılmış seyrek satır.

| Biçim | Ne için |
| --- | --- |
| COO | Kurmak |
| CSR | Satır dilimlemek ve matris-vektör çarpımı |
| CSC | Sütun dilimlemek ve doğrudan çözücüler |

> **Sade anlatım:** Simgesel ayrışma, bir rafın hangi gözüne ne konacağını planlamaktır. Desen değişmiyorsa planı bir kez yaparsın. Her turda yalnız gözlerin içini yenilersin.

### Dürüst not

`nr_yuk_akisi.py` Ybus'u ve Jacobian'ı okunurluk için **yoğun** kurup sonra seyreğe çevirir. **Yoğun** kurmak, bütün elemanları, sıfırlar dahil, bellekte tutmaktır.

Üç bara için sorun değil; on bin bara için yanlış.

`nr_canli_kodlama.py` baştan sona seyrektir.

Mülakatta bu farkı sen söyle.

## Sayısal kararlılık

Bu tablo, yük akışı kodunda sayısal olarak ne bozulabileceğini, nedenini ve önlemini verir.

| Sorun | Nedeni | Önlem |
| --- | --- | --- |
| Tekil veya neredeyse tekil Jacobian | Gerilim çökme noktası; ada; salınım barası yok | Bağlı bileşen denetimi; koşul sayısını izle |
| Kötü koşullanma | Çok küçük empedans (kesici, bara bağlantısı) yanında uzun hat | Sıfır empedanslı dalları bara birleştirerek modelden çıkar |
| Iraksama | Kötü başlangıç, ağır yük | Önceki çözümden veya DC çözümünden başla; adım küçült |
| PV–PQ salınımı | Reaktif sınırda gidip gelen bara | Histerezis; tur sayısı sınırı |
| Yanlış yakınsama | Düşük gerilimli ikinci çözüm | Sonuç gerilimlerini makullük için denetle (0,8–1,2 pu) |
| Yuvarlama | Farklı ölçekte büyüklükler | Per-unit zaten ölçekler; MW ve pu karıştırma |

Tablodaki terimler:

- **Tekil matris:** tersi alınamayan matris. Denklem sisteminin tek çözümü yoktur.
- **Ada:** şebekenin geri kalanından kopmuş bara grubu.
- **Koşul sayısı:** matrisin girdideki küçük hatayı ne kadar büyüttüğünü gösteren sayı. Büyükse matris kötü koşulludur.
- **Iraksama:** yinelemenin bir çözüme yaklaşmaması.
- **Histerezis:** geçiş için gidiş ve dönüşte farklı eşik kullanmak; bara iki tür arasında sürekli gidip gelmez.
- **MW:** megavat.

### Yakınsama ölçütü

Yakınsama ölçütü: artığın en büyük mutlak değeri (sonsuz norm), örneğin `1e-8` pu.

100 MVA (megavoltamper) bazda bu 1 W'tır. Hesabın adımları:

1. `1e-8` pu × 100 MVA = `1e-8` × 100 000 000 VA. Bu adım, pu değeri baz güçle çarpıp gerçek birime çevirir.
2. Sonuç 1 VA, yani güç artığı için 1 W mertebesidir. Bu adım, toleransın fiziksel olarak ne kadar küçük olduğunu gösterir.

Pratikte `1e-4`–`1e-6` yeter.

Göreli değil mutlak tolerans kullanılır, çünkü güç artığının fiziksel anlamı vardır.

### Kayan nokta

**Kayan nokta**, bilgisayarın ondalıklı sayıları sınırlı basamakla saklama biçimidir. Bu yüzden küçük yuvarlama farkları oluşur.

- Eşitliği `==` ile sınama; `np.isclose` veya `math.isclose` kullan.
- Açıları derece olarak saklama.
- `float32` kullanma. (`float32` yaklaşık 7 anlamlı basamak tutar; yük akışı için yetmez.)

## Test

Analiz kodunda test, "sonuç neye göre doğru?" sorusunun cevabıdır.

Katmanlar ve bu depodaki karşılıkları:

| Tür | Örnek (bu depoda) |
| --- | --- |
| Analitik doğrulama | İki baralı sistemin kapalı çözümü: `test_iki_bara_analitik_cozum` |
| Fiziksel değişmez | Üretim − yük = kayıp: `test_guc_dengesi_kayba_esit` |
| Çapraz doğrulama | İki ayrı Jacobian aynı matrisi veriyor: `test_iki_jacobian_ayni` |
| Davranış | Q sınırında PV → PQ: `test_q_limiti_pv_barayi_pq_yapar` |
| Olumsuz yol | Çözümsüz yükte hata fırlatılıyor: `test_cozumsuz_yuk_sessiz_kalmaz` |
| Girdi doğrulama | Sıfır empedans reddediliyor: `test_sifir_empedans_reddedilir` |

Her türün ne sınadığı:

- **Analitik doğrulama:** kodun sonucunu, elle kesin çözülen bir örnekle karşılaştırır.
- **Fiziksel değişmez:** fizik yasasının (güç dengesi) her durumda tuttuğunu sınar.
- **Çapraz doğrulama:** aynı şeyi iki farklı yolla hesaplayıp sonuçları karşılaştırır.
- **Davranış:** belli bir koşulda kodun beklenen kararı verdiğini sınar.
- **Olumsuz yol:** kodun başarısız olması gereken yerde gerçekten hata verdiğini sınar.
- **Girdi doğrulama:** anlamsız girdinin baştan reddedildiğini sınar.

### Bu depoda olmayan ama söylemen gerekenler

- **Referans araçla karşılaştırma:** aynı vakayı pandapower veya MATPOWER ile çöz, gerilimleri tolerans içinde karşılaştır. IEEE (Institute of Electrical and Electronics Engineers) 14, 30, 118 baralı test sistemleri bunun için vardır.
- **Altın değer (regresyon) testi:** bilinen bir vakanın sonucu dosyada saklanır; kod değişince sonuç değişirse test düşer. Değişim bilinçliyse dosya gözden geçirilerek güncellenir.
- **Özellik tabanlı test:** rastgele üretilen bağlı şebekelerde değişmezleri sına: güç dengesi, Ybus simetrisi, şöntsüz şebekede satır toplamı sıfır. **Şönt**, baradan toprağa bağlı eleman demektir (kondansatör, reaktör, hat şarj kapasitesi).
- **Performans testi:** büyük vakada süre ve bellek eşiği. Karmaşıklık gerilemesini yakalar. Yani bir değişiklik kodu fark edilmeden yavaşlatırsa test düşer.

Gerçek şebeke modeli teste konmaz; gizlidir ve büyüktür. Sentetik veya maskelenmiş vaka kullanılır.

## CI

CI (Continuous Integration, sürekli entegrasyon), her itmede otomatik çalışan boru hattıdır. **İtme** (push), kodu ortak depoya göndermektir. **Boru hattı**, sırayla çalışan otomatik adımlar dizisidir.

Analiz yazılımında asgari adımlar:

1. biçim ve statik denetim,
2. testler,
3. elle örneklerin doğrulaması.

**Statik denetim**, kodu çalıştırmadan okuyup hata ve stil sorunu arayan denetimdir.

### Örnek GitLab CI dosyası

Örnek GitLab CI dosyası (bu makinede çalıştırılmadı; betiklerin kendisi çalıştırıldı).

Bu dosya ne yapar:

- `image`: işlerin `python:3.12-slim` kapsayıcısında koşacağını söyler.
- `stages`: iki aşama tanımlar: önce `denetim`, sonra `test`.
- `before_script`: her işten önce gerekli paketleri, `pytest`'i ve `ruff`'ı kurar. `ruff`, Python için biçim ve statik denetim aracıdır.
- `denetim` işi: `ruff check` ile hata arar, `ruff format --check` ile biçimin doğru olup olmadığına bakar.
- `test` işi: örnek klasörüne girer, `pytest -q` ile testleri koşar, `python elle_ornekler.py` ile elle örnekleri doğrular.

```yaml
image: python:3.12-slim

stages: [denetim, test]

before_script:
  - pip install -r 14-Programlama/ornekler/requirements.txt pytest ruff

denetim:
  stage: denetim
  script:
    - ruff check 14-Programlama/ornekler
    - ruff format --check 14-Programlama/ornekler

test:
  stage: test
  script:
    - cd 14-Programlama/ornekler
    - pytest -q
    - python elle_ornekler.py
```

Kurumun hangi CI aracını kullandığını bilmiyorum.

> **Mülakatta şöyle söyle:** "Analiz modüllerinde regresyon testini hangi vakalarla koşuyorsunuz?"

Bu, panele sorabileceğin bir sorudur.

### Analiz yazılımına özgü üç kural

1. **Model, algoritma ve sınır değerleri ayrı sürümlenir.** Sonuç değiştiyse hangisinin değiştiği bilinmelidir.
2. **Sonuç yinelenebilir olmalıdır.** Rastgelelik varsa tohum sabitlenir ve kaydedilir. **Tohum**, rastgele sayı üretecinin başlangıç değeridir.
3. **Sayısal sonuç değişikliği gözden geçirme ister.** Bir yeniden düzenleme, sonucu beşinci basamakta değiştiriyorsa bu bir bulgudur.

## Canlı kodlama provası

Kronometreyle, üç kez:

| Dakika | İş |
| --- | --- |
| 0–2 | Sözleşmeyi söyle; iskeleti yorum satırı olarak yaz |
| 2–6 | `ybus` |
| 6–9 | Güç hesabı ve artık |
| 9–15 | Jacobian ve çözüm |
| 15–18 | Güncelleme, döngü, hata |
| 18–20 | İki baralı test: `x = 0,1`, yük `0,5 + j0,2` → `V_2 = 0,97825` |

### İki baralı testin elle hesabı

Son satırdaki test, kodu kesin bir sonuçla sınamak içindir. Sistem şöyle: 1. bara salınım barası, gerilimi 1 pu. İki bara arasında yalnız reaktans var, `x = 0,1` pu. 2. barada yük `0,5 + j0,2` pu, yani P = 0,5 ve Q = 0,2.

Bu sistemin kapalı (formülle bulunan) çözümü vardır. Yük barası gerilimi V için denklem:

`V⁴ + (2·Q·x − V₁²)·V² + x²·(P² + Q²) = 0`

Adımlar:

1. `2·Q·x − V₁² = 2·0,2·0,1 − 1 = 0,04 − 1 = −0,96`. Bu adım, denklemin V² teriminin katsayısını bulur.
2. `x²·(P² + Q²) = 0,01·(0,25 + 0,04) = 0,01·0,29 = 0,0029`. Bu adım, denklemin sabit terimini bulur.
3. Denklem `V⁴ − 0,96·V² + 0,0029 = 0` olur. Bu adım, V²'ye göre ikinci dereceden bir denklem elde eder.
4. `V² = (0,96 + √(0,96² − 4·0,0029)) / 2 = (0,96 + √0,91) / 2 ≈ (0,96 + 0,95394) / 2 ≈ 0,95697`. Bu adım, iki kökten büyük olanı (işletmedeki yüksek gerilimli çözümü) seçer.
5. `V = √0,95697 ≈ 0,97825`. Bu adım, testin beklediği `V_2 = 0,97825` değerini verir.

Kodun bulduğu `V_2` bu sayıyla tolerans içinde eşleşirse kod doğrudur.

### Konuşarak yaz

Yazarken konuş. Sessiz yazan aday, yanlış yola girdiğinde yardım alamaz.

## Yaygın yanlış

- **"`np.linalg.inv(J) @ artik` yazarım."** Tersini alma; `solve` veya `spsolve` kullan. Daha hızlı ve sayısal olarak daha sağlamdır.
- **"Ybus'u `np.zeros((n, n))` ile kurarım."** On bin barada 1,6 GB (gigabayt). Küçük örnekte kabul edilir; nedenini söyle.
- **"Açıyı derece tutarım."** `np.exp(1j * teta)` radyan ister.
- **"Yakınsama için tur sayısını artırırım."** Newton'da 20 tur fazlasıyla yeter; yetmiyorsa sorun başka yerdedir.
- **"Test yazmaya vakit yok."** Canlı kodlamada tek bir analitik test, kodun doğru olduğunu **senin** kanıtlamandır.
- **"`python -c` ile denedim, çalışıyor."** Elle deneme test değildir; yinelenemez.
- **"Python yavaştır, yük akışı C++ ile yazılır."** Süre çözücüde (derlenmiş kod) geçer. Python döngüsüyle Jacobian kurarsan yavaşlar; vektörel kurarsan fark küçülür. Önce ölç.

### 1,6 GB nereden geliyor

Bu hesap, yoğun Ybus'un neden büyük şebekede kullanılamayacağını gösterir.

1. On bin barada matris 10 000 × 10 000 = 100 000 000 elemanlıdır. Bu adım, yoğun matrisin eleman sayısını bulur.
2. Ybus karmaşık sayıdır; NumPy'da her karmaşık sayı (`complex128`) 16 bayt tutar. Bu adım, eleman başına belleği verir.
3. 100 000 000 × 16 bayt = 1 600 000 000 bayt ≈ 1,6 GB. Bu adım, toplam belleği bulur.

## Panel takip sorusu

Panelin kodundan sonra sorabileceği üç soru ve cevapları.

**"Bu kodu on bin baraya nasıl taşırsın?"**

> **Mülakatta şöyle söyle:** Ybus ve Jacobian baştan seyrek; Jacobian deseni sabit olduğu için simgesel ayrışmayı bir kez yaparım; başlangıç olarak önceki çözümü kullanırım; profil alır, sürenin kurulumda mı çözümde mi geçtiğine bakarım. Gerekirse KLU'ya geçerim.

**Profil almak**, kodun zamanını nerede harcadığını ölçmektir.

**"Bu işlevi servis haline getirsen arayüzü ne olur?"**

> **Mülakatta şöyle söyle:** Girdi sürümlü bir şebeke modeli kimliği ve senaryo; çıktı gerilimler, akışlar, **yakınsama durumu, tur sayısı, son artık** ve uyarılar. Uzun işler kuyruğa girer. Aynı girdi aynı çıktıyı vermeli; sonuç, model ve algoritma sürümüyle birlikte saklanır.

**"Sonucun doğru olduğuna nasıl güvenirsin?"**

> **Mülakatta şöyle söyle:** Dört katman. Analitik küçük örnek, fiziksel değişmezler, referans araçla karşılaştırma ve gerçek ölçümle karşılaştırma. Yalnızca birincisini ve ikincisini yaptım; üçüncüsü için pandapower kuracağım, dördüncüsü kurum verisi ister.

## 90 saniyelik metin için not

Aşağıdaki metin sayfanın sözlü özetidir. İçindeki terimler yukarıda açıldı: admitans matrisi (Ybus), karmaşık güç, Jacobian, seyrek çözücü, artık, güç dengesi, seyreklik deseni ve çarpanlar. Metindeki altı adım, "İskelet: altı adım" bölümündeki adımlardır.

## 90 saniye

"Yük akışını sıfırdan yazarken altı adım izlerim: admitans matrisini seyrek kurarım, karmaşık gücü gerilim çarpı akımın eşleniği olarak hesaplarım, verilen güçle farkını alırım, Jacobian'ı kurarım, doğrusal sistemi seyrek çözücüyle çözerim, açı ve gerilimi güncellerim. Matrisin tersini almam. Yakınsamayan vakada sessiz sonuç dönmem, son artığı taşıyan bir hata fırlatırım. Doğruluğu kapalı çözümü olan iki baralı örnekle, güç dengesiyle ve iki ayrı Jacobian'ın karşılaştırmasıyla sınarım; bunlar otomatik testtir ve her değişiklikte koşar. Büyük ölçekte seyreklik desenini bir kez çözümler, çarpanları yeniden kullanırım."
