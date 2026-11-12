# Davranışsal ve araştırma

İlanın son tercih sebepleri teknik değildir ve eler. Bu sebepler şunlardır:

- araştırmaya istek,
- analitik düşünme,
- problem analizi,
- çözüm geliştirme,
- koordinasyon,
- organizasyon,
- planlama,
- yeni teknolojiyi öğrenme,
- lisansüstü motivasyon.

Teknik soruyu doğru bilip bu maddelerde dağınık görünmek puanı 70’in altına itebilir. Yani teknik bilgi tek başına yetmez; bu sayfa, bu maddelerde nasıl toplu ve kanıtlı görüneceğini anlatır.

> Sade anlatım: Panel yalnızca "biliyor mu?" diye bakmaz. "Bu kişi araştırmacı gibi düşünüyor, planlı çalışıyor, öğrenebiliyor mu?" diye de bakar. Bu sorulara somut örnekle cevap vermen gerekir.

## Araştırmacı duruşu

Danışmanlık işi “dosyayı teslim ettim” ile biter. Araştırma grubunda ise dosya, tekrar koşulan bir araca ve bir iddiaya dönüşür.

Buradaki iddia ölçülüdür. Ölçülü iddia şu parçaları içerir:

| Parça | Ne demek |
|---|---|
| Varsayım | Hesabı hangi kabullerle kurdun |
| Veri | Hangi veriyle çalıştın |
| Limit | Yöntemin sınırı ne |
| Sonuç | Ne buldun |
| Sonucun bozulduğu yer | Hangi durumda sonuç artık geçerli değil |

Literatürü taradığını, bir yöntemi neden seçtiğini ve neden elediğini söylemen araştırma refleksidir. Panel bunu duymak ister.

| Zayıf ifade | Güçlü ifade |
|---|---|
| “Makale okurum.” | “Şu problemi şu yöntemle kurdum, şu yüzden sezgiseli eledim, şu vakada doğruladım.” |

Güçlü ifadede problem, yöntem, elenen seçenek ve doğrulama vakası vardır. Zayıf ifadede hiçbiri yoktur.

### Lisansüstü sorusu

Lisansüstü sorusu bir motivasyon sorusudur. Kapı açıksa, yani gerçekten lisansüstü yapmak istiyorsan, aşağıdaki problemlerden birini seç:

- güvenlik kısıtlı işletme,
- durum kestirimi,
- yenilenebilirle azalan atalet,
- dağıtım barındırma kapasitesi (hosting capacity: şebekenin gerilim ve akım sınırlarını aşmadan kabul edebileceği dağıtık üretim miktarı).

Seçtiğin problem için üç soruya cevap hazırla:

1. Neden o problem ülke sisteminde büyüyor?
2. MAM’da (TÜBİTAK Marmara Araştırma Merkezi) hangi ürüne değer?
3. Senin üç yılın ona nasıl bağlanıyor?

Yapılmaması gerekenler ve yerine söylenebilecekler:

- “Doktora yapmak istiyorum çünkü CV (özgeçmiş)” deme.
- Yapmayacaksan yalan söyleme.
- Bunun yerine şu yeter: “ürün içindeki yöntemi yayınlanabilir hale getirmek istiyorum, lisansüstü bunun disiplini”.

İlanda “yapmış olmak veya motivasyon” birlikte yazar. İkisi de kabuldür, sahtesi değildir.

### Yeni teknoloji

Son öğrendiğin şeyi somut söyle. Örnek iskelet:

> Mülakatta şöyle söyle: “Dağıtım dengesiz yük akışı için OpenDSS’i şu iş için öğrendim, şu dokümandan gittim, küçük fiderde doğruladım, asıl modele taşıdım.”

OpenDSS, dağıtım şebekesi analizi için kullanılan açık kaynaklı bir simülasyon aracıdır. Fider, dağıtım merkezinden tüketicilere giden hat demektir.

Öğrenme yöntemin dört adımdır:

1. birincil kaynak,
2. küçük örnek,
3. elde doğrulama,
4. sonra ölçek.

Panel, araç adını değil bu döngüyü dinler.

## STAR

STAR, İngilizce Situation (Durum), Task (Görev), Action (Eylem), Result (Sonuç) kelimelerinin baş harfleridir. Bir projeyi bu dört parçayla anlatma yöntemidir.

Her proje için dört cümle hazırla. Dört proje yeter:

- analiz,
- yazılım,
- zor veri,
- birlikte çalışılan.

Dört parçanın her birinde ne söyleyeceğin:

- **Durum:** şebeke, yıl, senin rolün. Bir cümle.
- **Görev:** karar neydi, süre neydi.
- **Eylem:** senin yaptığın hesap, kod, kontrol. “Ekip yaptı” içinden kendi fiilini ayır.
- **Sonuç:** sayı, karar değişikliği, hâlâ kullanılıyor mu. Sonuç yoksa ne öğrenildi.

Sayı uydurma. Hatırlamıyorsan mertebe söyle ve “raporda net değer var” de. Panelden biri alanı biliyorsa uydurma sayı hemen düşer.

### Analitik anlatımın kalıbı

Bir problemi analitik anlatmak için beş adımı sırayla kullan. Her adımın yanında ne işe yaradığı ve örneği var.

1. **Problemi ölçülebilir yaz.** Belirsiz şikâyeti sayıya ve koşula çevirir. “Gerilim bozuk” değil, “fider ucu 1,05 pu üstüne çıkıyor, öğlen, ters akış var.” (pu, per unit: değerin anma değerine oranı; 1,05 pu, anma geriliminin yüzde 5 üstü demektir.)
2. **Hipotez.** Olası nedeni açıkça söyler. “Aktif güç, R baskın hatta gerilimi yükseltiyor.” (R, hattın direnci; R baskın hat, direncin reaktansa göre büyük olduğu hattır.)
3. **Ayırıcı test.** Hipotezi diğer açıklamalardan ayırır. “Aynı P, daha kısa fiderde olmuyorsa mesafe hipotezi güçlenir.” (P, aktif güç.)
4. **Müdahale.** Çözüm seçeneklerini ve bedelini koyar. Kademe, volt-watt, iletken, kısıntı. Yan etki.
5. **Doğrulama.** Çözümün gerçekten işe yaradığını gösterir. Ölçüm veya ikinci araç.

### Koordinasyon

Koordinasyonu anlatırken üç şeyi gösterebildiğini anlat:

- bir işi parçalara bölebildiğini,
- bağımlılığı söyleyebildiğini,
- başkasının verisini tarihli isteyebildiğini.

| Kanıtsız | Kanıt |
|---|---|
| “Herkesle iyi anlaşırım.” | “Koruma ayarı için kısa devre sonucunu salı günü kilitledim, çarşamba röle çalışması ona göre yürüdü, veri değişince sürümü yükselttim.” |

İlandaki planlama maddesi tam olarak budur.

## Bilmediğin soru

Sessiz kalma ve uydurma. Şu sırayı izle:

> Mülakatta şöyle söyle: “Bu kurumu sahada uygulamadım. İlk ilkem şu olurdu: … Bunu doğrulamak için şu veriye bakarım. Eksik kalan yer … ”

Bu kalıbın parçaları:

1. Bilmediğini açıkça söyle.
2. İlk ilkeden akıl yürüt.
3. Neyle doğrulayacağını söyle.
4. Eksik kalan yeri belirt.

Bilmediğini bu kalıpla söylemek, analitik maddeye puan yazar. Yarım formülü yarım yazmak puan kırar.

## İngilizce

İlan İngilizce şart koşar. Panel bir soruyu İngilizce sorabilir.

Her teknik klasördeki 90 saniye kutusunun İngilizcesini bir kez kur. Ezber paragraf okuma. Şu iskelet yeter:

> Mülakatta şöyle söyle: “The question is about security analysis. N-1 means the system stays within thermal, voltage and stability limits after a single outage. I screen with a DC method and confirm the critical cases with AC power flow. Preventive actions cost money before the fault. Corrective actions, including a SIPS, act after it.”

İskeletteki kısaltmalar:

| Kısaltma | Açılımı |
|---|---|
| N-1 | Tek bir elemanın (hat, trafo, ünite) devreden çıkması durumu |
| DC | Direct Current; burada DC yük akışı, yani hızlı ve doğrusal yaklaşık yöntem |
| AC | Alternating Current; burada tam AC yük akışı, yani ayrıntılı doğrulama hesabı |
| SIPS | System Integrity Protection Scheme, sistem bütünlüğü koruma şeması |

Kelime dağarcığı:

| İngilizce | Türkçe karşılığı |
|---|---|
| power flow | yük akışı |
| contingency | olası arıza durumu |
| state estimation | durum kestirimi |
| bad data | hatalı ölçüm verisi |
| inertia | atalet |
| reserve | yedek |
| hosting capacity | barındırma kapasitesi |
| unit commitment | ünite tahsisi |
| optimal power flow | optimal güç akışı |
| ride-through | arızada devrede kalma |
| digital twin | dijital ikiz |

Bu listeyi `20` formül kartının arkasına yaz.

## Sorulacak sorular

Soruları sona sakla, üç tane sor, ilan metnini tekrar sorma.

- Önümüzdeki yıl, iletim işletme aracı ile dağıtım veya planlama işinin hangisi daha ağır?
- Yeni araştırmacı analiz motorunda mı, model ve veri kalitesinde mi, yoksa tahmin ve optimizasyon modülünde mi işe başlıyor?
- Lisansüstü ile proje teslimi aynı dönemde nasıl dengeleniyor?

## Anlatma

Mülakatta şunları anlatma:

- gerçek TEİAŞ (Türkiye Elektrik İletim A.Ş.) bara adı,
- müşteri yükü,
- gizli kısıt,
- önceki işyerinin kodu,
- kişi dedikodusu,
- “şu araç kötüdür” yarışı.

Yöntemi anlat, veriyi anlatma.

## Envanter

Kişilik envanteri doğru veya yanlış aramaz, tutarlılık arar. Aşırı uç işaretleme (her şeye “her zaman”) profili bozar.

İş tanımındaki özellikler:

- analitik,
- planlı,
- öğrenmeye açık,
- koordineli.

Sahte bir “liderlik kahramanı” profili, araştırmacı kadrosuyla çelişir. Dürüst ve tutarlı işaretle.

Teknik online sınavda süre, formül kartındaki kısa maddelerden gelir. Birim yaz, seçeneği ele.

Aşağıdaki metin kendini tanıtma konuşmasının iskeletidir. Boşlukları (…) mülakattan önceki gün kendi işinle doldur. YTBS (Yük Tevzi Bilgi Sistemi), grubun enerji yönetim platformudur. Bu metni ezberleme, iskeleti ezberle.

## 90 saniye (kendini tanıt)

“Ben … mühendisim. Son üç yılda … şebekesinde … analizini … aracıyla yaptım. Somut sonuç … oldu. Yazılım tarafında bunu … ile tekrarlanabilir hale getirdim. Sizin gruptaki karşılığı, aynı hesabın YTBS gibi bir işletme veya planlama aracında yaşaması. Başlamak istediğim yer … çünkü sahada o problemi gördüm.”
