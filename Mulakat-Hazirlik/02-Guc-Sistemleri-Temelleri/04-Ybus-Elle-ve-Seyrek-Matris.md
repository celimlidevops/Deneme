# Ybus — “bu ne?”

[01’deki](01-Guc-Birim-Sistem-Modeller.md) 7 numaralı kart. Hesap yok; mantık var.

## Ybus nedir?

Şebekeyi bilgisayarda tutmanın yolu.

- **Bara** = düğüm (hatların buluştuğu nokta)
- **Hat** = iki düğümü bağlayan yol
- **Ybus** = “kim kime bağlı?” tablosu (matris)

Bu tablo şunu söyler: baralara giren akımlar ile baraların gerilimleri birbirine nasıl bağlı.

Kısaca: **şebekenin bağlantı haritası**.

Yük akışı, kısa devre, durum kestirimi hep aynı haritayı kullanır.

## Tablo nasıl doldurulur? (fikir yeter)

İki kural:

1. **İki bara arasında hat varsa** o iki baranın kesişiminde bir sayı vardır (bağlantının “eksi” hali).
2. **Bir baranın kendi kutusunda** o baraya değen her şeyin toplamı vardır.

Toprağa bağlı ekstra parçalar (şönt) yalnız o baranın kendi kutusuna yazılır.

**Hata kontrolü (kolay):** ekstra şönt yoksa bir satırdaki sayıların toplamı sıfır çıkar. Tutmuyorsa yazım hatası vardır.

## “Seyrek” ne demek?

Gerçek şebekede bir bara birkaç komşuya bağlıdır, hepsine değil. Tablonun çoğu kutusu boştur.

Bu yüzden:

- Bütün tabloyu ters çevirmek (tersini almak) kötü fikirdir — boşluklar dolar, bellek şişer.
- Boşlukları koruyan çözüm yöntemleri kullanılır.

**Panel cümlesi:** “Ybus seyrektir; tersini almam, seyrek çözerim.”

## Hat açılırsa ne olur?

O hatta ait dört kutu değişir: iki ucun kendi kutuları ve aralarındaki iki kesişim. Bütün Türkiye haritasını baştan çizmek zorunda değilsin; sadece o bağlantıyı güncellersin.

## Yazılım köprüsü (tek cümle)

Python’da seyrek matris araçları vardır (`scipy.sparse`). Örnek kod `14-Programlama/ornekler` altındadır — şimdi açmana gerek yok; “biliyorum, seyrek çözerim” demen yeter.

## 90 saniye

> “Ybus şebekenin kim-kime-bağlı tablosudur. Köşegen dışı bağlantıyı, köşegen o baraya değenleri tutar. Çoğu kutu boştur; tersini almam, seyrek çözerim.”
