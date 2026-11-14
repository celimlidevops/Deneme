# Yük akışı — mülakat kartları

**Bu ne? → Panelde söyle → Unutma.** Formül yok.

---

## 1. Problem nedir?

**Bu ne?**  
Elimizde: hangi santral ne kadar üretiyor, hangi yük ne kadar çekiyor, şebeke bağlantısı.  
Aradığımız: her baranın **gerilimi** (ve açısı), her hattın **ne kadar güç taşıdığı**, kayıplar.

**Panelde söyle:**  
> Yük akışı, verilen üretim ve yükte gerilim profili ile hat akışlarını bulan temel analizdir. Güvenlik, ekonomik işletme, planlama hep bunun üstüne oturur.

---

## 2. Bara tipleri

**Bu ne?**  
Her düğümde her şeyi bilemeyiz; bazıları verilir, bazıları bulunur.

| Tip | Ne biliyoruz? | Ne arıyoruz? | Tipik kim |
| --- | --- | --- | --- |
| **PQ** | P ve Q | Gerilim ve açı | Yük |
| **PV** | P ve gerilim büyüklüğü | Q ve açı | Gerilim tutan santral |
| **Slack** | Gerilim ve açı (referans) | Kayıp + dengeyi tamamlayan P/Q | Hesap denge noktası |

**Panelde söyle:**  
> Slack bir “sihirli santral” değil; hesabın referansı ve denge noktasıdır. PV, Q limitine çarpınca PQ’ya düşer — düşmezse gerilim sahte düzelir.

---

## 3. Yöntemler (isim + ne zaman)

| Yöntem | Düz anlatım |
| --- | --- |
| **Newton-Raphson (NR)** | İletimde standart. Tahmini düzeltire düzelte yakınsar. |
| **Ayrık hızlı (FDLF)** | P–açı / Q–gerilim ayrımını kullanarak hızlanır; her yerde doğru değil. |
| **DC yük akışı** | “Gerilim hep 1, kayıp/Q yok” kabullü **sadece aktif akış** kaba modeli. |
| **Geri-ileri süpürme** | Radyal dağıtım fideri için uygun. |

**Panelde söyle:**  
> İletimde NR. Hızlı termik elekte DC. Dağıtımda süpürme veya üç faz. DC ile gerilim kararı vermem.

---

## 4. DC yük akışı — ne zaman evet / hayır?

**Evet (kaba elek):** binlerce N-1’de “hangi hat ısınır?”, PTDF taraması.  
**Hayır:** gerilim ihlali, ağır yük, dağıtım, reaktif karar.

Elekten geçen senaryoyu **tam (AC) yük akışıyla** doğrula.

---

## 5. Iraksadı — ilk üç bakış

1. Ada / kesici topolojisi (şebeke kopuk mu?)  
2. Veri: yanlış baz, sıfır empedans, saçma yük  
3. Kontrol salınımı: Q limiti, kademe gidip geliyor mu?

**Unutma:** İlk iş “başka çözücü dene” değildir.

---

## 6. Sonucu işletmeye çevir

Sayı yetmez. Sor:

- Hangi bara limit dışı?  
- Hangi hat dolu?  
- Kademe / şönt / üretim kaydırma gerekir mi?  
- Bu N-1 sonrası mı, normal mi?

**Panelde söyle:**  
> Çıktıyı limit ihlali ve müdahale diline çeviririm; ham gerilim listesi işletme cevabı değildir.

---

## 90 saniye

> “Yük akışı verilen üretim-yükte gerilim ve akışı bulur. PQ, PV, slack tipleri neyin bilindiğini ayırır. İletimde NR, hızlı termik elekte DC, dağıtımda süpürme. Iraksayınca ada-veri-Q limiti. Sonucu limit ve müdahale diline çeviririm.”
