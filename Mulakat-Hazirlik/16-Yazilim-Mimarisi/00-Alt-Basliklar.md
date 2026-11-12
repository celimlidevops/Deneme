# 16 — Yazılım mimarisi ve dijital ikiz

Bu klasör, şebeke analiz hesabının bir yazılım ürününe nasıl dönüştüğünü anlatır. Ölçüm sahadan gelir, bir modele bağlanır, hesaplanır ve operatöre servis edilir. Aşağıdaki başlıklar bu yolculuğun durakları.

## Klasördeki sayfalar

| Sayfa | İçerik |
| --- | --- |
| [01 — EMS zinciri ve dijital ikiz](01-EMS-Ikiz-Servis.md) | Zincirin halkaları, servis, kuyruk, kalite bayrağı, arayüz, sürüm |
| [02 — SCADA, protokoller, CIM, zaman serisi, dijital ikiz, siber güvenlik](02-SCADA-Protokoller-CIM-TSDB-Ikiz-Siber.md) | Verinin sahadan kontrol merkezine akışı ve bunun güvenliği |
| [03 — Kendi projelerinden köprü](03-Kendi-Projelerinden-Kopru.md) | Kendi yazılım tecrübeni şebeke yazılımına bağlama şablonu |

## Kısaltmalar

- **EMS** (Energy Management System, Enerji Yönetim Sistemi): iletim şebekesinin hesaplarını yapan yazılım katmanı.
- **SCADA** (Supervisory Control and Data Acquisition, Denetleyici Kontrol ve Veri Toplama): sahadan ölçüm toplayan ve uzaktan kumanda veren sistem.
- **REST** (Representational State Transfer, temsili durum aktarımı) ve **SOAP** (Simple Object Access Protocol, basit nesne erişim protokolü): iki web servis tarzı.

## Alt başlıklar

Her maddenin altında o başlıkta ne öğreneceğin tek cümleyle yazılı.

1. **EMS zinciri**
   Bu sayfada ölçümün sahadan operatör ekranına kadar hangi hesap halkalarından geçtiğini sırasıyla öğreneceksin.

2. **Çevrimdışı çalışma ile çevrimiçi çalışma**
   Bu sayfada planlama ve eğitim modeli ile "şu anki" canlı model arasındaki farkı ve ikisi karışırsa ne olduğunu öğreneceksin.

3. **Dijital ikizin bu zincirdeki anlamı**
   Bu sayfada dijital ikizin üç boyutlu bir resim değil, ölçümle güncellenen ve üzerinde senaryo koşulan bir hesap modeli olduğunu öğreneceksin.

4. **Topoloji işlemcisi**
   Bu sayfada kesici durumlarından enerjili adaları ve bara modelini kuran adımı öğreneceksin.

5. **Veri tabanı: zaman serisi ve şebeke modeli**
   Bu sayfada şebeke kimliği ile ölçüm verisinin neden ayrı tutulduğunu öğreneceksin.

6. **Web servis: REST ve SOAP**
   Bu sayfada yeni ve eski sistemlerle konuşan iki servis tarzının nerede kullanıldığını öğreneceksin.

7. **SCADA/EMS entegrasyonu**
   Bu sayfada analiz yazılımının SCADA verisini nasıl aldığını ve neden kumanda etmediğini öğreneceksin.

8. **İş kuyruğu ve binlerce arıza**
   Bu sayfada ağır hesabın neden istek içinde değil, kuyrukta koşturulduğunu öğreneceksin.

9. **Kalite bayrağı ve operatör güveni**
   Bu sayfada her sonucun yanında "bu sayıya ne kadar güvenebilirim" bilgisinin nasıl taşındığını öğreneceksin.

10. **Arayüzde ne gösterilir**
    Bu sayfada operatörün ekranda gerçekten hangi bilgiyi görmek istediğini öğreneceksin.

11. **Test, sürüm, izleme**
    Bu sayfada model, algoritma ve limit sürümlerinin neden ayrı tutulduğunu ve servisin nasıl izlendiğini öğreneceksin.

12. **Güvenlik: kimlik, kayıt, gizli veri**
    Bu sayfada rol tabanlı erişim, denetim kaydı ve sırların korunması gibi asgari güvenlik hijyenini öğreneceksin.

13. **Araştırmacının bu mimaride durduğu yer**
    Bu sayfada bu zincirde senin katkının nerede olacağını ve bunu mülakatta nasıl anlatacağını öğreneceksin.
