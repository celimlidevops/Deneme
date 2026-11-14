# Newton-Raphson — fikir (formülsüz)

[01](01-NR-FDLF-DC-Dagitim.md) kart 3’ün açılmış hali. Elle matris yok.

## NR ne yapar?

1. Gerilimlere bir **tahmin** koy.  
2. Bu tahminle her barada P ve Q’yu hesapla.  
3. İstenen P/Q ile farka bak (**artık**).  
4. Farkı küçültecek düzeltmeyi bul, gerilimleri güncelle.  
5. Fark yeterince küçük olana kadar tekrarla.

**Jacobian** = “P/Q farkı, gerilim/açıyı nasıl oynatmalı?” sorusunun türev tablosu.  
İsimini bilmen yeter; mülakatta satır satır yazman beklenmez (yaz derlerse “seyrek lineer sistem çözerim, tersini almam” de).

**Panelde söyle:**  
> NR, güç artığını gerilim düzeltmesine çeviren yinelemeli çözücüdür. Matris seyrektir; yoğun ters alınmaz. İletimde birkaç iterasyon tipiktir.

## Q limiti neden kritik?

PV baraya “gerilimi tut” denir ama makinenin verebileceği reaktif **sınırlıdır**.  
Sınıra çarpınca artık gerilimi tutamaz → tip **PQ’ya düşer**.

Bu dönüşüm yoksa ekranda gerilim düzgün, sahada değil.

## Kademe ve şönt

Çözümün içinde anahtarlanan / kademe değiştiren kontroller varsa salınım olabilir. Iraksama bazen “fizik imkânsız” değil, “kontrol gidip geliyor”dur.

## 90 saniye

> “NR tahmin-düzeltme döngüsüdür; Jacobian düzeltmenin yönünü verir. Seyrek çözerim. PV Q limitine çarpınca PQ olur; aksi halde gerilim sahte kalır.”
