# Ekipman yeterliliği

Grubun çalışma listesinde ayrı bir madde var: şebeke ekipmanının teknik yeterliliği ve performans değerlendirmesi.

Bu yeni bir analiz türü değildir. Yük akışı, kısa devre ve geçici hal sonuçlarını ekipmanın dayanım verisiyle karşılaştırmaktır. Soru şudur: şebeke bu cihazı ne kadar zorluyor, cihaz ne kadarına dayanıyor?

> **Sade anlatım:** Asansörün kapısında taşıyabileceği kişi sayısı yazar. Yeterlilik çalışması, en kalabalık saatte asansöre kaç kişinin bindiğini sayıp o yazıyla karşılaştırmaktır.

## Ne karşılaştırılır

| Ekipman | Karşılaştırılan büyüklükler | Not |
| --- | --- | --- |
| Kesici | Kesme akımı, tepe dayanımı, X/R oranı veya DC zaman sabiti, geçici toparlanma gerilimi (TRV) | Kısa devre hesabı azami duruma göre yapılır. TRV, şüpheli barada EMT (elektromanyetik geçici hal) benzetimiyle bakılır |
| Trafo | Sürekli ve acil yüklenme, kademe çalışma aralığı, kısa devre dayanımı, kayıp (boşta ve yükte), paralel çalışma koşulları (gerilim, sargı grubu, empedans) | — |
| Hat iletkeni | Termik sınır, sehim ve yaklaşım, mevsimsel kapasite | Dinamik hat kapasitesi, hava ölçümüyle statik limiti gevşetir. Koruma ve gerilim limiti ayrıca durur |
| Ölçü trafosu | Doyma, koruma sınıfı mı ölçü sınıfı mı, polarite | Durum kestirimindeki ölçek hatası ve diferansiyel korumadaki doyma buradan gelir |
| Reaktör, kapasitör, parafudr | Sürekli gerilim, geçici aşırı gerilim, enerji emme | — |
| Röle | Görme (arızayı algılama), zaman, haberleşme kaybında yedek | Performans, koordinasyon eğrisi ve olay kaydıyla değerlendirilir |

Terimler:

- **X/R oranı:** Reaktansın dirence oranı. Büyükse arıza akımındaki DC bileşen yavaş söner ve kesiciyi daha çok zorlar.
- **TRV (geçici toparlanma gerilimi):** Kesici akımı kestikten hemen sonra kontakları arasında beliren gerilim. Kesici buna dayanamazsa ark yeniden tutuşur.
- **Doyma:** Ölçü trafosunun çekirdeği büyük akımda dolar ve çıkışı gerçek akımı izlemez.

## Değerlendirmenin sırası

1. Şebeke çalışmasından zorlayan büyüklüğü al: azami akım, azami ve asgari gerilim, arıza süresi, frekans ucu.
2. Ekipmanın etiket ve tip deney değerini aynı birime çevir.
3. Marjın hangi senaryoda eridiğini yaz. Tek bir "uygundur" tüm topolojileri kapsamaz. Bakım topolojisi ve N-1 (tek eleman devre dışı) ayrı bakılır.
4. Yetmezse seçenekler şunlardır: ekipman değişimi, şebeke güçlendirme, işletme kısıtı, koruma süresini kısaltma. Süre kısalınca topraklamadaki dokunma gerilimi de rahatlar. Yani iki iş birbirine bağlıdır.

Tip deneyi laboratuvarın işidir. Araştırmacının işi, sahadaki zorlamanın o deneyin kapsadığı aralıkta olup olmadığını hesabıyla göstermektir.

> **Mülakatta şöyle söyle:** "Deney kapsamıyorsa 'deney var, sorun yok' denmez."

Aşağıdaki metin, ekipman yeterliliği sorulduğunda 90 saniyede söyleyeceğin özettir.

## 90 saniye

"Ekipman yeterliliği, analiz sonucunu etiket değeriyle karşılaştırmaktır. Kesicide azami kısa devre ve tepe, trafoda yüklenme ve kısa devre dayanımı, hatta sehimli termik sınır, ölçü trafosunda doyma. Karşılaştırma azami, asgari ve bakım topolojisinde ayrı yapılır. Yetmeyen yerde ekipman, şebeke veya koruma süresi birlikte düşünülür."
