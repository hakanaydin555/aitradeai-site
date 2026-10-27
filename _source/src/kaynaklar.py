# -*- coding: utf-8 -*-
"""Turkish answer pages (/tr/kaynaklar/). Body uses a tiny line format rendered in build.py:
## h2 · = formula · > note · - bullet · 1. numbered · | table row (first row = header) · **Lead:** text · plain = paragraph
"""

UPDATED = "2026-10-27"
UPDATED_TR = "27 Ekim 2026"

INDEX = {
    "title": "Kaynaklar: e-ticaret kârlılığı rehberleri — AI Trade",
    "desc": "Kampanya kârı, stok, iptal, iade, kargo ve rapor otomasyonu için hesap örnekleri ve kontrol listeleri.",
    "h1": "Kaynaklar",
    "lead": "E-ticarette para ve zamanın en sık kaybolduğu yerler için kısa rehberler: her biri bir soruya net cevap, bir hesap örneği ve bir kontrol listesi içerir.",
}

PAGES = [
{
"slug": "kampanya-karliligi",
"title": "Kampanya kârlı mı? Katkı kârı hesabı — AI Trade",
"desc": "%20 indirim sipariş başına kârı %78 azaltabilir. Komisyon, kargo, reklam ve iade dahil katkı kârını ve gereken ek satışı hesaplayın.",
"card": "Kampanya kârlı mı?",
"q": "%20 indirim kârı ne kadar etkiler?",
"h1": "Pazar yerinde kampanya kârlı mı? Katkı kârı nasıl hesaplanır?",
"answer": "Bir kampanyanın kârlı olup olmadığını brüt marj değil, **sipariş başına katkı kârı** gösterir: satış fiyatından ürün maliyeti, pazar yeri komisyonu, kargo, reklam ve iade payı düşüldükten sonra kalan tutar. Aşağıdaki örnekte %20 indirim, sipariş başına katkı kârını 180 TL'den 40 TL'ye indiriyor; aynı toplam kâr için 4,5 kat sipariş gerekiyor.",
"body": """## Katkı kârı formülü nedir?
= Katkı kârı = Satış fiyatı − Ürün maliyeti − Komisyon − Kargo − Reklam − İade payı − Diğer değişken giderler (paketleme, ödeme/hizmet bedeli)
Komisyon ve reklam genelde satış fiyatının yüzdesidir; indirimle birlikte azalır. Ürün maliyeti, kargo ve iade payı ise sabit kalır. Bu yüzden indirim, kârı fiyattan çok daha hızlı eritir.
## Örnek: %20 indirim kârı ne kadar etkiler?
> Örnek rakamlar, TL, KDV hariç. Kendi kategorinizin komisyon oranını satıcı panelinizden alın.
| Kalem | Kampanyasız | %20 indirimli
| Satış fiyatı | 1.000 | 800
| Ürün maliyeti | −420 | −420
| Komisyon (%20) | −200 | −160
| Kargo | −75 | −75
| Reklam (%10) | −100 | −80
| İade payı | −25 | −25
| **Katkı kârı** | **180** | **40**
Fiyat %20 düştü, sipariş başına katkı kârı %78 düştü.
## Kampanya için kaç kat satış gerekir?
= Gereken sipariş çarpanı = Kampanyasız katkı kârı ÷ Kampanyalı katkı kârı
Örnekte 180 ÷ 40 = 4,5. Kampanya sipariş sayısını 4,5 kattan fazla artırmıyorsa, ciro artsa bile toplam kâr azalır. Katkı kârı sıfırın altına iniyorsa kampanya her siparişte zarar ettirir; sipariş artışı zararı büyütür.
## En fazla ne kadar indirim yapılabilir?
Başabaş indirimi, katkı kârını sıfıra indiren fiyattır. Örnekte değişken yüzdeler (komisyon %20 + reklam %10) fiyatın %30'u, sabit kalemler 520 TL. Başabaş fiyatı = 520 ÷ (1 − 0,30) ≈ 743 TL, yani yaklaşık %26 indirim. Bu noktada kâr sıfırdır; gerçekçi bir kampanya bunun epey üstünde kalmalı.
## Kampanyadan önce hangi sorular sorulmalı?
- İndirimden sonra sipariş başına katkı kârı ne olacak?
- Aynı toplam kâr için kaç kat sipariş gerekiyor ve bu gerçekçi mi?
- Kampanya süresince yeterli stok var mı?
- Ücretsiz kargo eşiği, indirimli fiyatta hâlâ kâr bırakıyor mu?
- Kampanya kaldırıldıktan sonra satış normale dönüyor mu, yoksa müşteri indirimi mi bekliyor?""",
"faq": [
("Brüt marj ile katkı kârı arasındaki fark nedir?", "Brüt marj yalnızca ürün maliyetini düşer. Katkı kârı komisyon, kargo, reklam ve iade gibi siparişe bağlı tüm giderleri de düşer; kampanya kararı için doğru ölçü budur."),
("Komisyon oranını nereden bulurum?", "Pazar yerinin satıcı panelinde, kategori bazında yer alır. Oranlar dönem dönem değiştiği için hesaplamada her zaman güncel paneli kullanın."),
("Kampanya zarar ettiriyorsa neden yapılır?", "Stok eritmek, yeni müşteri kazanmak ya da listelemede görünür kalmak için bilinçli olarak yapılabilir. Önemli olan zararın tutarını önceden bilmek ve karşılığında ne alındığını ölçmektir."),
("Bu hesabı tüm ürünler için nasıl yaparım?", "Ürün, kanal ve kampanya bazında katkı kârı tablosu kurulur ve her kampanya sonrası güncellenir. Ücretsiz check-up'ta bu tabloyu sizin verinizle birlikte çıkarıyoruz."),
],
"related": ["iade-ve-kargo-maliyeti", "rapor-otomasyonu"],
"cta": "Kampanyalarınızın hangisinin gerçekten kâr getirdiğini birlikte çıkaralım.",
},
{
"slug": "stoksuz-urune-reklam",
"title": "Stokta olmayan ürüne reklam: kaybı bulun — AI Trade",
"desc": "Stok bittiği halde reklamı süren ürünler bütçeyi sessizce eritir. 30 dakikada kaybı bulmanın adımları ve otomatik durdurma kuralı.",
"card": "Stokta olmayan ürüne reklam",
"q": "Stok bitince reklam neden durmalı?",
"h1": "Stokta olmayan ürüne reklam harcaması nasıl bulunur ve durdurulur?",
"answer": "Stokta olmayan ürüne harcanan reklam bütçesini bulmak için son 30 günün ürün bazında reklam harcamasını, aynı günlerin stok durumuyla eşleştirin: stok sıfırken harcanan tutar boşa giden bütçedir. Kalıcı çözüm, stok sıfıra indiğinde reklamı otomatik durduran bir kuraldır.",
"body": """## Bu kayıp neden fark edilmez?
Reklam paneli harcamayı ve tıklamayı gösterir, stok durumunu göstermez. Stok ekibi ile reklam ekibi farklı ekranlara bakar; ürün tükendiğinde kimse reklamı kapatmayı kendi işi olarak görmez. Sonuç: tıklama gelir, satış gelmez ve reklam algoritması o ürünün "dönüşmediğini" öğrenir.
## Hangi durumlarda olur?
- **Ürün katalogları seyrek güncelleniyorsa:** katalog reklamları stok durumunu katalogdaki alandan okur. Katalog günde bir ya da daha seyrek güncelleniyorsa, tükenen ürün saatlerce reklamda kalır.
- **Tek ürüne giden reklamlarda:** katalog dışı, belirli bir ürün sayfasına yönlendiren reklamlar stoktan habersizdir; elle kapatılana kadar sürer.
- **Varyantlı ürünlerde:** çok satan beden ya da renk biter, ürün sayfası açık kalır; ziyaretçi aradığını bulamaz.
- **Birden çok kanalda aynı stok satılıyorsa:** pazar yerinde tükenen stok, kendi sitenizin reklamında hâlâ var görünür.
## 30 dakikalık kontrol nasıl yapılır?
1. Reklam panelinden son 30 günün **ürün ya da reklam bazında günlük harcamasını** indirin.
1. Aynı 30 gün için ürün bazında **günlük stok durumunu** çıkarın (stok ya da sipariş yönetim sisteminden).
1. Ürün kodu ve tarihle iki tabloyu eşleştirin.
1. Stok sıfır ya da kritik seviyedeyken yapılan harcamayı toplayın. Bu tutarın toplam reklam harcamasına oranı sizin kayıp oranınızdır.
1. Kaybı en yüksek 10 ürünü listeleyin; çoğu zaman kaybın büyük kısmı birkaç çok satan üründe toplanır.
## Örnek hesap
> Örnek rakamlar.
Aylık reklam harcaması 200.000 TL; eşleştirmede stok sıfırken harcanan tutar 14.000 TL çıkıyor. Bütçenin %7'si satış getiremeyecek tıklamalara gitmiş; yıllık karşılığı yaklaşık 168.000 TL. Bu tutar tasarruf olarak sayılır; aynı bütçe stoklu ürünlere kaydırılırsa ek satış ayrıca hesaplanır, ikisi üst üste konmaz.
## Kalıcı çözüm nedir?
- **Katalog güncelleme sıklığını artırın:** stok değiştiğinde ya da en az birkaç saatte bir.
- **Otomatik kural kurun:** stok belirli bir eşiğin altına inince reklamı ya da ürünü reklam setinden çıkarın; stok gelince geri açın.
- **Eşik stok kullanın, sıfır değil:** son birkaç adet satılırken gelen tıklamalar da çoğunlukla boşa gider.
- **Günlük uyarı kurun:** "stok kritik + reklam aktif" olan ürünlerin listesi her sabah ilgili kişiye gitsin.""",
"faq": [
("Katalog reklamları tükenen ürünü kendiliğinden durdurmaz mı?", "Katalogdaki stok bilgisi güncel olduğu sürece genellikle durdurur. Sorun, kataloğun stoktan geç güncellenmesi ve katalog dışı reklamlardır."),
("Kayıp oranı ne kadar olursa sorun sayılır?", "Sabit bir eşik yok; ama bütçenin birkaç yüzdesi bile yıllıkta büyük bir tutardır. Asıl gösterge, kayıp oranının ay ay düşüp düşmediğidir."),
("Bu kontrolü her ay elle mi yapmalıyım?", "İlk sefer elle yapılır; sonra stok ve reklam verisini her gün eşleştiren otomatik bir rapor kurulur."),
],
"related": ["stok-kaynakli-iptal", "rapor-otomasyonu"],
"cta": "Reklam ve stok verinizi birlikte eşleştirip kaybı çıkaralım.",
},
{
"slug": "stok-kaynakli-iptal",
"title": "Stok kaynaklı iptalin gerçek maliyeti — AI Trade",
"desc": "Stok kaynaklı bir iptal üç kez ödetir: kaybedilen kâr, boşa giden reklam ve düşen mağaza puanı. Maliyeti hesaplayın, oranı düşürün.",
"card": "Stok kaynaklı iptalin maliyeti",
"q": "Bir iptal kaç kez ödetir?",
"h1": "Stok kaynaklı iptal e-ticarette gerçekte kaça mal olur?",
"answer": "Satıcının stok bulunamadığı için iptal ettiği bir sipariş üç kez ödetir: siparişin getireceği katkı kârı kaybolur, o siparişi getiren reklam harcaması boşa gider ve pazar yerindeki satıcı puanı düşer. Üçüncüsü en az ölçülen ama en pahalı olabilecek kalemdir, çünkü görünürlüğü ve gelecekteki tüm satışları etkiler.",
"body": """## Pazar yerleri stok kaynaklı iptali nasıl değerlendirir?
Pazar yerleri satıcının operasyon performansını puanlar. Örneğin Trendyol'da satıcı puanı haftalık hesaplanır ve "Tedarik Edememe Oranı", stok ya da tedarik nedeniyle satıcı tarafından iptal edilen siparişleri sayar; müşteri kaynaklı iptaller bu orana girmez. Yüksek puan, ürün sıralamasını ve görünürlüğü olumlu etkiler. Kesin kurallar ve eşikler için her zaman güncel satıcı panelini esas alın.
## Stok kaynaklı iptalin maliyeti nasıl hesaplanır?
= İptal maliyeti (aylık) = İptal sayısı × (Kaybedilen katkı kârı + Sipariş başına reklam maliyeti + İşlem maliyeti)
> Örnek rakamlar: aylık 2.000 sipariş, stok kaynaklı iptal oranı %3, yani 60 iptal.
| Kalem | Sipariş başına | Aylık (60 iptal) | Türü
| Kaybedilen katkı kârı | 180 TL | 10.800 TL | Kaybedilen kâr
| Boşa giden reklam | 100 TL | 6.000 TL | Nakit kayıp
| İşlem (müşteri hizmetleri, iptal) | 15 TL | 900 TL | Ekip zamanı
| Puan ve görünürlük etkisi | ölçülmesi zor | — | Gelecekteki satış
Ölçülebilir kısım ayda yaklaşık 17.700 TL. Kaybedilen kâr ile nakit kayıp ayrı tutulur; aynı kayıp iki kez sayılmaz.
## Stok kaynaklı iptaller neden olur?
- **Gecikmeli stok aktarımı:** depo ile pazar yeri arasındaki stok entegrasyonu saatte bir ya da daha seyrek çalışıyor.
- **Aynı stok birden çok kanalda:** son adet aynı anda iki kanalda satılıyor.
- **Tedarikçi süreleri güncel değil:** sistemde "stokta" görünen ürün aslında tedarikçide.
- **Sistem stoku ile raf stoku farklı:** sayım farkları, hasarlı ya da yanlış yerdeki ürünler.
- **Kampanya ve stok planlaması ayrı yapılıyor:** kampanya talebi artırıyor, stok buna göre hazırlanmıyor.
## Nasıl azaltılır?
- **Haftalık ölçün:** stok kaynaklı iptal oranını kanal kanal, ürün ürün takip edin.
- **Güvenlik stoku bırakın:** çok kanallı satışta son 1–2 adedi pazar yerlerine açmayın.
- **Entegrasyon sıklığını artırın:** stok değişikliği dakikalar içinde tüm kanallara gitsin.
- **Kampanya öncesi stok kontrolü:** kampanyalı ürünlerin tahmini talebiyle stok karşılaştırılsın.
- **Talep tahmini kullanın:** hızlı tükenen ürünler için yeniden sipariş noktası otomatik hesaplansın.""",
"faq": [
("Müşterinin iptal ettiği siparişler de bu hesaba girer mi?", "Hayır. Bu sayfa satıcının stok ya da tedarik nedeniyle iptal ettiği siparişleri kapsar; müşteri kaynaklı iptaller ayrı izlenir."),
("Kaç iptal oranı kabul edilebilir?", "Pazar yerleri ve kategoriler farklı eşikler uygular; güncel eşiği satıcı panelinden kontrol edin. Hedef, oranı sıfıra mümkün olduğunca yaklaştırmaktır."),
("En hızlı sonuç veren adım hangisi?", "Çoğu zaman çok kanallı satışta güvenlik stoku ve stok aktarım sıklığı. İkisi de birkaç gün içinde uygulanabilir."),
],
"related": ["stoksuz-urune-reklam", "iade-ve-kargo-maliyeti"],
"cta": "İptal kaynaklarınızı kanal kanal çıkaralım.",
},
{
"slug": "iade-ve-kargo-maliyeti",
"title": "İade ve kargo maliyeti nasıl düşürülür? — AI Trade",
"desc": "Bir iade, kaybı iki yönlü kargo, işleme ve satılamayan ürünle büyütür. İade başına maliyeti hesaplayın, kargo faturasındaki farkları bulun.",
"card": "İade ve kargo maliyeti",
"q": "İade sipariş başına ne kadara mal olur?",
"h1": "E-ticarette iade ve kargo maliyeti nasıl hesaplanır ve düşürülür?",
"answer": "Bir iadenin maliyeti yalnızca geri ödenen tutar değildir: gidiş kargosu geri gelmez, dönüş kargosu ödenir, ürün kontrol edilip yeniden paketlenir ve bir kısmı bir daha satılamaz. Aşağıdaki örnekte iade başına maliyet yaklaşık 212 TL. Kargo tarafında ise en sık kayıp, faturadaki desi farkları ve kârı silen ücretsiz kargo eşikleridir.",
"body": """## İade başına maliyet nasıl hesaplanır?
= İade maliyeti = Gidiş kargosu + Dönüş kargosu + İşleme ve paketleme + (Ürün maliyeti × Satılamayan oranı)
Komisyonun iadede geri alınıp alınmadığı pazar yerine ve sözleşmeye göre değişir; kendi durumunuza göre ekleyin.
> Örnek rakamlar, TL, KDV hariç. Aylık 2.000 sipariş, iade oranı %8, yani 160 iade.
| Kalem | İade başına
| Gidiş kargosu | 75
| Dönüş kargosu | 75
| İşleme ve yeniden paketleme | 20
| Satılamayan ürün (420 TL × %10) | 42
| **Toplam** | **212**
Aylık maliyet 160 × 212 = 33.920 TL. İade oranını %8'den %6'ya indirmek, ayda yaklaşık 8.500 TL nakit tasarruf demektir.
## İade oranı nasıl düşürülür?
- **İade nedenlerini ürün bazında sınıflandırın:** beden, renk, hasar, yanlış ürün, beklentiyi karşılamama.
- **En çok iade alan 20 ürüne odaklanın:** çoğu zaman iadelerin büyük kısmı az sayıda üründen gelir.
- **Ürün sayfasını düzeltin:** ölçü tablosu, gerçek renk görselleri, müşteri sorularından çıkan açıklamalar.
- **Paketleme ve kontrol:** hasarlı ve yanlış ürün iadeleri depo sürecinden gelir; pazar yerlerinde satıcı puanını da etkiler.
- **Tekrar iade eden müşterileri izleyin:** kural dışı ya da tekrarlayan iadeleri ayrı raporlayın.
## Kargo faturasında nelere bakılmalı?
- **Desi farkları:** sistemdeki ürün ölçüsü ile faturadaki desi aynı mı? Küçük farklar binlerce gönderide büyür.
- **Ücretsiz kargo eşiği:** eşiğin hemen üstündeki sepetlerde kargo, siparişin katkı kârını siliyor mu?
- **Kampanyalı ürünlerde kargo:** indirimli fiyatta kargo maliyeti oransal olarak büyür.
- **Anlaşma ve fiili tarife:** faturadaki birim fiyatlar, sözleşmedeki tarifeyle aynı mı?
Bu kontroller otomasyona çok uygundur: kargo faturası her ay elle değil, her gün sipariş verisiyle otomatik eşleştirilebilir. Bir projede kampanyalı ürün ve kargo maliyetlerini yeniden düzenleyerek bu kalemlerde %20 tasarruf sağladık.""",
"faq": [
("İade oranı kaç olmalı?", "Kategoriye göre çok değişir; moda ile elektronik aynı değildir. Kendi oranınızı kategori ve ürün bazında izleyip ay ay düşürmek, genel bir ortalamayla kıyaslamaktan daha faydalıdır."),
("İade maliyeti katkı kârı hesabına nasıl girer?", "Sipariş başına \"iade payı\" olarak: iade oranı × iade başına maliyet. Örnekte %8 × 212 TL ≈ 17 TL."),
("Kargo faturasını kontrol etmek için hangi veri gerekir?", "Kargo firmasının gönderi bazında faturası ve sipariş sisteminizdeki ürün ölçüleri ile sipariş kayıtları."),
],
"related": ["kampanya-karliligi", "stok-kaynakli-iptal"],
"cta": "İade ve kargo kayıplarınızı ürün bazında çıkaralım.",
},
{
"slug": "rapor-otomasyonu",
"title": "E-ticarette hangi raporlar otomatikleşmeli? — AI Trade",
"desc": "Pazar yeri panellerinden veri indirip birleştirmek haftada saatler alır. E-ticaret ekibinde otomatikleşmesi gereken 6 rapor ve başlama sırası.",
"card": "Hangi raporlar otomatikleşmeli?",
"q": "Ekip haftada kaç saati rapora veriyor?",
"h1": "E-ticaret ekibinde hangi raporlar otomatikleşmeli?",
"answer": "Otomatikleşmesi gereken raporlar, her hafta aynı adımlarla tekrar eden ve bir kararı tetikleyen raporlardır: günlük satış-stok-reklam özeti, kampanya katkı kârı, \"stok kritik + reklam aktif\" uyarısı, iade nedenleri, kargo faturası eşleştirmesi ve pazar yeri hakediş mutabakatı. Haftada 5 saat süren bir rapor, bir kişi için yılda yaklaşık 250 saat demektir.",
"body": """## Ekibiniz rapora gerçekte ne kadar zaman veriyor?
Bir hafta boyunca şunu yazın: hangi rapor, kim hazırlıyor, kaç dakika sürüyor, hangi panellerden veri indiriliyor ve rapor hangi karar için kullanılıyor. Çoğu ekipte asıl zaman analize değil, veriyi indirip birleştirmeye ve düzeltmeye gidiyor.
## Hangi 6 rapor otomatikleşmeli?
| Rapor | Ne gösterir | Hangi kararı tetikler | Sıklık
| Satış-stok-reklam özeti | Kanal ve ürün bazında dünün satışı, stoku, reklam harcaması | Günün öncelikleri | Her sabah
| Kampanya katkı kârı | Kampanya ve ürün bazında sipariş başına kâr | Kampanyayı sürdür, değiştir, durdur | Kampanya boyunca günlük
| Stok kritik + reklam aktif | Stoku eşiğin altında olup reklamı süren ürünler | Reklamı durdur ya da stok getir | Günlük uyarı
| İade nedenleri | Ürün ve neden bazında iade oranı | Ürün sayfası, paketleme, tedarikçi | Haftalık
| Kargo faturası eşleştirme | Desi ve tarife farkları | Kargo firmasından düzeltme talebi | Haftalık
| Pazar yeri hakediş mutabakatı | Beklenen ve yatan tutar farkı | Eksik ödeme ya da kesinti itirazı | Her hakedişte
## Nasıl başlanır?
1. **Envanter çıkarın:** tüm düzenli raporları, süresini ve kullanıldığı kararı listeleyin.
1. **Öncelik verin:** en çok zaman alan ve en pahalı kararı tetikleyen 2–3 raporla başlayın.
1. **Veri kaynaklarını bağlayın:** pazar yeri, reklam, stok ve kargo verisi tek bir yerde günlük toplansın.
1. **Eşik ve uyarı tanımlayın:** rapor okunmasa bile kritik durum ilgili kişiye ulaşsın.
1. **Sahip atayın:** her raporun bir iç sahibi olsun; otomasyon bozulduğunda kim fark edecek belli olsun.
## Ne otomatikleşmemeli?
Tek seferlik analizler, strateji kararları ve müşteri ya da tedarikçi görüşmeleri. Otomasyonun amacı kişiyi işten çıkarmak değil; rapor hazırlayan kişinin rapor okuyan ve karar veren kişiye dönüşmesidir.
## Faydası nasıl ölçülür?
Kazanılan ekip saati ayrı, raporun yakaladığı kayıp ayrı ölçülür. Örneğin "stok kritik + reklam aktif" uyarısının faydası, kazanılan saat değil, durdurulan boşa reklam harcamasıdır. İkisi toplanırken aynı fayda iki kez sayılmaz.""",
"faq": [
("Rapor otomasyonu için yazılım ekibi gerekir mi?", "Çoğu zaman gerekmez. Pazar yeri ve reklam platformlarının veri bağlantıları, tablo araçları ve AI destekli otomasyon araçlarıyla küçük ekipler de kurabilir. Asıl iş, hangi raporun hangi kararı tetikleyeceğini doğru tanımlamaktır."),
("AI raporlamada nerede işe yarar?", "Verileri özetlemede, anormal değişiklikleri işaretlemede ve \"bu hafta neden düştü?\" gibi sorulara ilk taslak cevabı üretmede. Karar yine ekibindir."),
("Kurulum ne kadar sürer?", "Kapsama göre değişir. İlk 2–3 rapor genellikle birkaç hafta içinde kurulup ekibe devredilebilir."),
],
"related": ["kampanya-karliligi", "stoksuz-urune-reklam"],
"cta": "Ekibinizin rapora verdiği saatleri ve otomatikleşecek ilk 3 raporu birlikte çıkaralım.",
},
]
