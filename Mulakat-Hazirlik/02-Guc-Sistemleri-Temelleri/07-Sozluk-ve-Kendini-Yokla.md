# Sözlük ve kendini yokla

## Bu klasörü hangi sırayla oku

Dosyalar numara sırasıyla değil, aşağıdaki sırayla okunur. Her satır, o dosyada ne öğreneceğini söyler.

1. `02-Sifirdan-AC-Devre-ve-Fazor` — fazör, empedans, aktif ve reaktif güç
2. `03-Uc-Faz-ve-Per-Unit-Elle` — hat ve faz gerilimi, birim sistem
3. `04-Ybus-Elle-ve-Seyrek-Matris` — şebekenin matrisi
4. `05-Reaktif-Guc-Kompanzasyon-Gerilim` — gerilim neden yereldir
5. `06-Yuk-Modelleri-ve-Trafo-Gruplari` — yük ve sıfır bileşen yolu
6. `01-Guc-Birim-Sistem-Modeller` — hepsinin yoğun özeti, en son

İlk beş dosyadaki elle örnekleri kâğıtta kendin çöz. Sayın tutmuyorsa `14-Programlama/ornekler/elle_ornekler.py` aynı örnekleri hesaplar.

## Sözlük

Panel bir terimi İngilizce söyleyebilir. Türkçesini ve bir cümlelik anlamını bil.

| Türkçe | İngilizce | Bir cümle |
| --- | --- | --- |
| Bara | Bus | Şebekede elemanların bağlandığı düğüm |
| Fider | Feeder | Trafo merkezinden çıkan dağıtım hattı |
| Trafo merkezi (TM) | Substation | Gerilimin değiştiği ve hatların buluştuğu tesis |
| Kesici | Circuit breaker | Yük ve arıza akımını kesebilen anahtar |
| Ayırıcı | Disconnector | Akım yokken açılan, görünür ayırma sağlayan anahtar |
| Kademe değiştirici | Tap changer (OLTC, On-Load Tap Changer) | Trafonun sarım oranını yük altında değiştirir |
| Yük akışı | Power flow, load flow | Verilen üretim ve yükte gerilim ve akışları bulur |
| Salınım barası | Slack, swing bus | Açı referansı; kaybı ve dengesizliği üstlenir |
| Kısa devre | Short circuit, fault | Fazların birbirine veya toprağa istenmeyen teması |
| Beklenmeyen durum | Contingency | Bir elemanın plansız devre dışı kalması |
| Güvenlik analizi | Security analysis | Arıza sonrası limitlerin korunup korunmadığı |
| Kararlılık | Stability | Bozucudan sonra yeni dengeye oturabilme |
| Durum kestirimi | State estimation | Gürültülü ölçümden en olası gerilim ve açıyı bulma |
| Atalet | Inertia | Dönen kütlelerin frekans değişimine direnci |
| Hız eğimi | Droop | Frekans sapmasına karşı güç tepkisinin oranı |
| Puant | Peak load | En yüksek anlık talep |
| Kurulu güç | Installed capacity | Santrallerin anma güçleri toplamı |
| Yedek | Reserve | Arıza ve sapma için boşta tutulan kapasite |
| Kısıt | Congestion | Hattın, ucuz üretimi taşımaya yetmemesi |
| Yeniden dağıtım | Redispatch | Kısıtı çözmek için üretimin yerini değiştirme |
| Ekonomik dağıtım | Economic dispatch | Devredeki ünitelerin en ucuz yük paylaşımı |
| Ünite tahsisi | Unit commitment | Hangi ünitenin ne zaman devrede olacağı |
| Optimal güç akışı | Optimal power flow (OPF) | Şebeke limitleriyle birlikte en ucuz işletme |
| Evirici | Inverter | Doğru akımı şebeke frekansında alternatif akıma çevirir |
| Dağıtık üretim | Distributed generation | Dağıtım şebekesine bağlı küçük üretim |
| Barındırma kapasitesi | Hosting capacity | Limit bozulmadan bağlanabilecek üretim |
| Fazör ölçüm birimi | PMU (Phasor Measurement Unit) | Zaman damgalı gerilim ve akım fazörü ölçer |
| Arıza boyunca kalma | Fault ride through | Gerilim çökünce santralin ayrılmaması |
| Yük atma | Load shedding | Sistemi kurtarmak için tüketimin kesilmesi |
| Kısıntı | Curtailment | Üretimin bilerek kesilmesi |
| Simetrik bileşenler | Symmetrical components | Dengesiz üç fazı üç dengeli diziye ayırma |
| Koruma koordinasyonu | Protection coordination | Arızaya en yakın rölenin önce açmasını sağlama |

## Kendini yokla

Cevaba bakmadan yaz. On sorudan sekizi tutmadan `03` klasörüne geçme.

1. 230 V etkin gerilimin tepe değeri kaçtır?
2. 154 kV hat gerilimine karşılık faz gerilimi kaçtır?
3. 50 MW, güç faktörü 0,9. Görünür güç ve reaktif güç?
4. `Z = 3 + j4 Ω` için büyüklük ve açı?
5. 154 kV ve 100 MVA için empedans bazı?
6. 25 MVA, %8 empedanslı trafo 100 MVA bazında kaç pu eder?
7. `z = j0,2` hattın admitansı ve Ybus'taki köşegen dışı elemanı?
8. Gerilim 0,9 pu'ya düşerse sabit empedans yükü yüzde kaç azalır?
9. Dyn11 trafonun alçak gerilim toprak arızası yüksek tarafta sıfır bileşen akımı üretir mi?
10. Kondansatör gerilimi %10 düşerse ürettiği reaktif yüzde kaç düşer?

Cevaplar. Her cevabın yanında hangi kuralı kullandığı yazılıdır.

1. `230 × √2 = 325 V` — tepe değer, etkin değerin √2 katıdır.
2. `154 / √3 = 88,9 kV` — faz gerilimi, hat geriliminin √3'e bölümüdür.
3. `S = 50 / 0,9 = 55,6 MVA`, `Q = 50 × tan(25,84°) = 24,2 Mvar` — önce görünür güç, sonra güç faktörü açısının tanjantıyla reaktif güç.
4. `|Z| = 5 Ω`, açı `arctan(4/3) = 53,1°` — büyüklük `√(R² + X²)`, açı `arctan(X/R)`.
5. `154² / 100 = 237,2 Ω` — `Z_baz = V_baz² / S_baz`.
6. `0,08 × 100 / 25 = 0,32 pu` — baz değiştirme; gerilim bazı aynı olduğu için yalnız güç oranı çarpılır.
7. `y = −j5`, köşegen dışı `+j5` — `1/(jx) = −j/x`, köşegen dışı admitansın eksilisidir.
8. `0,9² = 0,81`, yani %19 azalır — sabit empedans yükünde güç gerilimin karesiyle gider.
9. Hayır. Üçgen sargı sıfır bileşeni yüksek tarafa geçirmez — sıfır bileşen yolu kuralı.
10. `0,9² = 0,81`, yani %19 düşer — kondansatör reaktifi `Q = V² / X_c`.
