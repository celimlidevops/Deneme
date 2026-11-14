# Kısıt ve katsayılar — “bu ne?”

İsimler korkutucu; fikirler basit. Hesap yok.

## Kısıt nedir?

Ucuz santral çalışıyor ama aradaki hat **dolu**. Güç yüke ulaşamıyor. Sistem daha pahalı santrali çalıştırmak zorunda kalabilir.

Buna **iletim kısıtı** denir. Çözüm: üretimi kaydırmak (**yeniden dağıtım**) veya uzun vadede hat/trafo eklemek.

**Panelde söyle:**  
> Kısıt, fiziğin ekonomiyi sınırlamasıdır. Yazılımda önce hangi hattın dolduğunu, sonra hangi üretimi kaydırınca rahatladığını gösterirsin.

## PTDF — “bu üretim şu hatta ne kadar görünür?”

**Bu ne?**  
Bir yerde üretimi 1 birim artırırsan, belirli bir hatta akış **ne kadar** değişir?

Kısaca: **güç transferinin hatlara dağılım katsayısı**.

Ne işe yarar? Binlerce senaryoyu hızlı elemek, “hangi hat dolacak?” diye bakmak.

## LODF — “şu hat açılırsa diğerleri ne kadar dolar?”

**Bu ne?**  
Bir hat açılınca (arıza / bakım), komşu hatlara akış **nasıl kayar?**

Kısaca: **hat açılma dağılım katsayısı**. N-1 taramasını hızlandırır.

**Panelde söyle:**  
> PTDF transferin nereye gittiğini, LODF bir hat düşünce yükün nereye kaydığını kabaca gösterir. İnce gerilim kararı için AC doğrulama gerekir.

## NTC / ATC — sınır ötesi kapasite

**Bu ne?**  
İki bölge / iki ülke arasında **ne kadar güç transferine izin var?**

- Kabaca “toplam transfer kapasitesi” ailesi (NTC gibi isimler)
- “Hâlâ boşta ne kadar var?” (ATC gibi isimler)

Panelde isim ezberi değil, fikir önemli: **sınır hatları + güvenlik (N-1) + gerilim** birlikte kapasiteyi belirler.

## Unutma

Bu katsayılar çoğu zaman **basitleştirilmiş** (DC benzeri) dünyadan gelir. Gerilim ve reaktif işin içine girince tam AC yük akışıyla doğrula.

## 90 saniye

> “Kısıt, ucuz gücün hatta takılmasıdır. PTDF transferin hatlara payını, LODF hat açılınca kaymayı hızlı gösterir. Sınır kapasitesi N-1 ve gerilimle sınırlıdır; elekten geçen senaryoyu AC ile doğrularım.”
