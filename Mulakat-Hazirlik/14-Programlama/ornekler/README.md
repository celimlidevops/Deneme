# Örnekler

Bu klasör, mülakat notlarındaki hesapların çalışan halidir. Notlarda elle yapılan hesaplar burada Python betiği olarak yeniden yapılır.

Üç özelliği var:

- **Dış veri yok.** Her betik kendi küçük şebekesini içinde tanımlar. İnternetten veya başka dosyadan veri çekmez.
- **Kendi sonucunu denetler.** Her betik, bulduğu sayıyı beklenen değerle karşılaştırır.
- **Sapınca hata verir.** Sayı saparsa betik sessizce devam etmez, hata verir.

## Nasıl çalıştırılır

Aşağıdaki komutlar şu sırayla iş görür:

1. `pip install -r requirements.txt` gerekli kütüphaneleri `requirements.txt` dosyasındaki listeye göre kurar.
2. Sonraki satırlar her betiği tek tek çalıştırır.
3. `test_ornekler.py` satırındaki `#` sonrası bir yorumdur: testler `pytest -q` komutuyla da koşturulabilir. pytest, Python'un test çalıştırma aracıdır; `-q` (quiet) çıktıyı kısa tutar.

```
pip install -r requirements.txt
python nr_canli_kodlama.py
python nr_yuk_akisi.py
python ieee14_nr_karsilastir.py
python elle_ornekler.py
python test_ornekler.py        # veya: pytest -q
python dc_yuk_akisi.py
python wls_durum_kestirimi.py
python ekonomik_dagitim.py
```

Görsel laboratuvar (tarayıcı): `Mulakat-Hazirlik/Lab-Ac.bat` veya `lab/index.html`.

## Dosyalar

Tablodaki "İlgili not" sütunu, betiğin hangi not dosyasına ait olduğunu gösterir. `14/02` gibi bir yazım "14 numaralı klasörün 02 numaralı dosyası" demektir.

| Dosya | Ne yapar | İlgili not |
| --- | --- | --- |
| `nr_canli_kodlama.py` | Seyrek Ybus ve Newton-Raphson, 59 satır. Canlı kodlamada yazılacak sürüm | `14/02` |
| `nr_yuk_akisi.py` | Tam sürüm: açık formüllü ve vektörel Jacobian, Q limitinde PV→PQ, yakınsama hatası | `05/02` |
| `ieee14_nr_karsilastir.py` | IEEE 14 NumPy NR + pandapower `case14` karşılaştırması; `ieee14_sonuc.json` yazar | `14/02`, `15/02` |
| `test_ornekler.py` | 7 test: analitik çözüm, güç dengesi, Jacobian eşitliği, Q limiti, çözümsüz vaka, girdi denetimi | `14/02` |
| `elle_ornekler.py` | 02–13 klasörlerindeki bütün elle örneklerin sayısal doğrulaması | Her klasörün `02` dosyası |
| `dc_yuk_akisi.py` | Üç barada DC yük akışı | `05/01` |
| `wls_durum_kestirimi.py` | Dört ölçümle açı kestirimi; bozuk ölçümü normalize artıkla bulur | `09/01` |
| `ekonomik_dagitim.py` | Eşit λ çözümü ve üretim sınırı | `11/01` |

### Tablodaki terimler

İlk kez görüyorsan bu terimler tabloyu okumayı kolaylaştırır:

| Terim | Anlamı |
| --- | --- |
| Ybus | Bara admitans matrisi. Hangi baranın hangisine hangi admitansla bağlı olduğunu tutar |
| Seyrek | Matrisin yalnız sıfır olmayan elemanlarının saklanması |
| Newton-Raphson | Doğrusal olmayan yük akışı denklemlerini yinelemeli çözen yöntem |
| Jacobian | Güç denklemlerinin açıya ve gerilime göre türevlerinden oluşan matris |
| Açık formüllü ve vektörel Jacobian | Aynı matrisin iki yazımı: biri eleman eleman formülle, biri dizi işlemleriyle |
| Q limiti, PV→PQ | Bir PV barası (aktif gücü P ve gerilimi V sabit tutulan bara, genelde üretici) reaktif güç (Q) sınırına ulaşınca PQ barasına (P ve Q'su verilen bara, genelde yük) çevrilir |
| Yakınsama hatası | Hesap belirlenen tur sayısında çözüme ulaşmazsa fırlatılan hata |
| Çözümsüz vaka | Yükün şebekenin taşıyabileceğinden fazla olduğu, yük akışının çözümü olmayan durum |
| DC yük akışı | DC (Direct Current, doğru akım) yaklaşımı: AC denklemlerinin doğrusallaştırılmış, hızlı hali |
| WLS | Weighted Least Squares, ağırlıklı en küçük kareler. Ölçümlerden şebeke durumunu kestirir |
| Normalize artık | Ölçümle kestirim arasındaki farkın, o farkın beklenen saçılımına bölünmüş hali. Büyük çıkan ölçüm bozuk sayılır |
| Eşit λ | Ekonomik dağıtımda bütün üreticilerin artımlı maliyetinin (bir MW daha üretmenin maliyeti) eşit olduğu çözüm. λ (lambda) bu ortak maliyettir |

## Son çalıştırma

Son çalıştırma: Python 3.14, NumPy 2.3, SciPy 1.17. Yedi test geçti.

## pandapower doğrulama

`ieee14_nr_karsilastir.py` kendi NR ile `pandapower.networks.case14()` sonucunu karşılaştırır.
Bu makinede son koşu: max |ΔV| ≈ 2e-3 pu, max |Δθ| ≈ 0.02°. Tap modeli / bara 9 şöntü milipuanlık fark bırakabilir — beklenen model farkı.

Bu karşılaştırma neden önemli: kendi yazdığın kodun sonucunu bağımsız bir referans araçla doğrulamış olursun.
