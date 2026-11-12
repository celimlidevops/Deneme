# 05 — Yük akışı

Bu bölüm yük akışını baştan kurar. Aşağıdaki her madde bir alt başlıktır. Yanındaki cümle, o konuda ne öğreneceğini söyler. Konular üç sayfaya dağılmıştır: `01-NR-FDLF-DC-Dagitim.md` genel çerçeve, `02-NR-Elle-Jacobian-Q-Limit.md` elle Newton-Raphson, `03-Uc-Faz-Dengesiz-ve-Olasiliksal.md` dağıtım ve belirsizlik.

1. **Problemin tanımı: verilen üretim ve yükten gerilim ve akı** — Elinde hangi bilgiler olduğunu ve yük akışının hangi bilinmeyenleri bulduğunu öğreneceksin.
2. **Bara tipleri: PQ, PV, slack, izolasyon** — Her bara tipinde (PQ: P ve Q bilinen yük barası, PV: P ve gerilim büyüklüğü bilinen üretim barası, slack: referans/salınım barası) neyin verilip neyin arandığını öğreneceksin.
3. **Ybus kurulumu** — Bara admitans matrisini (Ybus) hat ve şönt değerlerinden nasıl yazacağını öğreneceksin.
4. **Güç denklemleri, polar form** — Her baradaki P ve Q'yu gerilim büyüklüğü ve açıyla veren denklemleri öğreneceksin.
5. **Gauss-Seidel: neden zayıf kaldığı** — Eski yinelemeli yöntemin büyük sistemde neden tercih edilmediğini öğreneceksin.
6. **Newton-Raphson ve Jacobian blokları** — NR (Newton-Raphson) yönteminin Jacobian matrisinin H, N, M, L bloklarıyla nasıl adım attığını öğreneceksin.
7. **Ayrık hızlı yük akışı (fast decoupled)** — FDLF'nin (Fast Decoupled Load Flow, ayrık hızlı yük akışı) neyi atarak hız kazandığını ve nerede yanıldığını öğreneceksin.
8. **DC yük akışı ve ne zaman meşru olduğu** — Doğrusallaştırılmış aktif güç modelinin varsayımlarını ve kör noktasını öğreneceksin.
9. **Kontrol: kademe, şönt, Q limiti, PV'den PQ'ya düşme** — Trafo kademesi, şönt ve reaktif sınırının çözüme nasıl girdiğini öğreneceksin.
10. **Iraksama: ağır yük, kötü başlangıç, ada, veri hatası** — Yük akışı yakınsamadığında nedeni nasıl ayırt edeceğini öğreneceksin.
11. **Dağıtım yük akışı: geri-ileri süpürme** — Radyal fiderin neden ayrı bir yöntemle çözüldüğünü ve süpürmenin adımlarını öğreneceksin.
12. **Üç faz dengesiz yük akışı** — Fazların neden ayrı ama bağlı modellendiğini ve dengesizliğin kayba etkisini öğreneceksin.
13. **Devam güç akışı ve PV eğrisine köprü** — Yükü adım adım artırıp gerilim çökmesi noktasına (burun) nasıl yaklaşıldığını öğreneceksin.
14. **Hassasiyet ve dağıtım faktörleri (PTDF, LODF)** — PTDF (Power Transfer Distribution Factor, güç transfer dağıtım faktörü) ve LODF (Line Outage Distribution Factor, hat açılma dağıtım faktörü) ile hızlı tarama yapmayı öğreneceksin.
15. **Büyük sistemde seyrek matris ve performans** — Binlerce baralı şebekenin neden seyrek çözücüyle hızlı çözüldüğünü öğreneceksin.
16. **Sonuçların işletme diline çevrilmesi** — Çıktıdaki sayıları işletmecinin soracağı sorulara nasıl çevireceğini öğreneceksin.
