# 09 — Durum kestirimi

Bu klasör, enerji yönetim sisteminin (EMS, Energy Management System) ölçümden "şebekenin şu anki hâli"ni çıkaran halkasını anlatır. Aşağıdaki her madde, bu sayfada ne öğreneceğini bir cümleyle söyler.

1. **Neden SCADA ham değeri yetmez** — SCADA (Supervisory Control and Data Acquisition, uzaktan izleme ve kontrol sistemi) ölçümünün neden gürültülü, eksik ve birbiriyle çelişkili olduğunu öğreneceksin.
2. **Durum vektörü: açı ve gerilim** — Şebekenin "durumu" denince hangi bilinmeyenlerin kastedildiğini ve neden bir açının referans alındığını öğreneceksin.
3. **Ölçüm türleri: P, Q, V, I, kademe, fazör** — Aktif güç (P), reaktif güç (Q), gerilim (V), akım (I), trafo kademesi ve fazör ölçümünün kestirime nasıl girdiğini öğreneceksin.
4. **Ölçüm modeli z = h(x) + e** — Ölçümü, durumu ve hatayı birbirine bağlayan temel denklemi öğreneceksin.
5. **Ağırlıklar ve standart sapma** — Her ölçüme neden `1/σ²` kadar güvenildiğini öğreneceksin.
6. **Ağırlıklı en küçük kareler (WLS)** — WLS (Weighted Least Squares) amaç fonksiyonunu ve adım adım türetimini öğreneceksin.
7. **Kazanç matrisi ve normal denklemler** — `G = HᵀWH` matrisinin ne taşıdığını ve her iterasyonda hangi denklemin çözüldüğünü öğreneceksin.
8. **Gözlenebilirlik ve kritik ölçüm** — Ölçümlerin durumu tek anlamlı belirleyip belirlemediğini nasıl test edeceğini ve hangi ölçümün "kritik" sayıldığını öğreneceksin.
9. **Pseudo-ölçüm** — Ölçüm yetmeyen yere tahmin değerini nasıl ve hangi ağırlıkla koyacağını öğreneceksin.
10. **Kötü veri: ki-kare, normalize artık, en büyük normalize artık testi** — Bozuk ölçümün önce varlığını, sonra yerini nasıl bulacağını elle hesapla öğreneceksin.
11. **Kaldıraç noktası ve ölçüm hatasının yayılması** — Bir ölçümün çözümü aşırı etkilediği durumu ve bir hatanın komşu artıklara nasıl bulaştığını öğreneceksin.
12. **Topoloji hatası ve parametre hatası** — Yanlış kesici durumu ve yanlış hat parametresinin neden ölçüm atarak düzelmediğini öğreneceksin.
13. **PMU ile lineer kestirim ve hibrit kestirim** — PMU (Phasor Measurement Unit, fazör ölçüm birimi) ile modelin neden doğrusal olduğunu ve SCADA ile nasıl birleştirildiğini öğreneceksin.
14. **İzleme hızı: klasik SE dakikalar, WAMS alt saniye** — Klasik durum kestirimi (SE, State Estimation) ile WAMS (Wide Area Monitoring System, geniş alan izleme sistemi) arasındaki hız farkını öğreneceksin.
15. **Dağıtım durum kestirimi** — Dağıtım şebekesinde ölçüm azlığı yüzünden kestirimin neden bir tahmin problemine dönüştüğünü öğreneceksin.
16. **Tahmin destekli kestirim** — Bir sonraki durumu önceden öngörüp ölçüm gelince düzeltmenin ne kazandırdığını öğreneceksin.
17. **Kestirim çıktısının güvenlik analizine bağlanması** — Kestirim sonucunun hangi kalite koşuluyla N-1 analizine verileceğini öğreneceksin.
18. **Yazılımda sayısal sorunlar: referans açı, ağırlık koşullandırma** — Kazanç matrisini tekil ya da kötü koşullu yapan yazılım hatalarını ve çarelerini öğreneceksin.
