# -*- coding: utf-8 -*-
"""All site copy, English and Turkish. Edit text here, then run build.py."""

SITE = "https://aitradeai.net"
CAL = "https://calendar.app.google/qvtHpnCi4qVszRdK8"
WA_NUMBER = "905334755284"
LINKEDIN = "https://linkedin.com/in/hakanaydin55/"
LINKEDIN_CO = "https://www.linkedin.com/company/aitradeai/"
EMAIL = "hakan.aydin@aitradeai.net"

# Search engine verification (meta tag values). Empty = not added.
GSC_VERIFY = ""   # Google Search Console: content value of google-site-verification
BING_VERIFY = "F9897FD44A7FC3706BDF0ED05C5F26AD"  # Bing Webmaster Tools: content value of msvalidate.01
# Cloudflare Web Analytics token (cookieless). Empty = no analytics script.
CF_BEACON = "206d4b174c34470281ed475f3bb0363f"

T = {
"en": {
  "wa_text": "Hi, I'd like to talk about a free check-up.",
  "nav": {"how": "How it works", "results": "Results", "about": "About", "contact": "Contact", "cta": "Free check-up", "menu": "Open menu", "lang_label": "Language"},
  "footer": {"copy": "© 2026 AI Trade · Istanbul, Türkiye", "contact": "Contact", "privacy": "Privacy & KVKK", "li": "LinkedIn"},
  "fab": "Let's talk",
  "home": {
    "title": "AI Trade — E-commerce profitability consulting",
    "desc": "We find where your e-commerce operation loses money and time, fix what matters most and hand the working system to your team in eight weeks. Free check-up.",
    "eyebrow": "AI-powered e-commerce profit partner",
    "h1": "Less waste.<br>More profit.",
    "lead": "We find where your e-commerce operation loses money and time, fix what matters most, and hand the working system to your team.", "lead_weeks": "In eight weeks.",
    "cta": "Request a free check-up", "ghost": "Estimate your losses ›",
    "panel_kicker": "Contribution profit · weekly", "panel_title": "Before and after the project", "panel_tag": "Example view",
    "chart_aria": "Example chart: weekly contribution profit stays flat before the fixes go live, then rises above the baseline",
    "chart_base": "Baseline", "chart_live": "Fixes live", "chart_w1": "Week 1", "chart_w8": "Week 8",
    "rows": [("Ads on out-of-stock products", "Stopped"), ("Duplicate shipping fees", "Recovered"), ("Weekly sales report", "Automated")],
    "steps": [("Find.", "Where money and time leak."), ("Fix.", "The two or three that matter most."), ("Teach.", "Your team, on real work."), ("Hand over.", "A system you own and run.")],
    "leak_h": "Profit rarely disappears all at once.",
    "leak_p": "It leaks at every step of an order's journey. We find each leak, then close it.",
    "nodes": [("Ads", "Can you see how much of your ad spend turns into profit?", "Spend on loss-makers paused"),
              ("Order", "Campaigns grow revenue. Do they grow profit too?", "Repriced or stopped"),
              ("Shipping", "Do you know what each shipping invoice really charges you?", "Right carrier, every invoice checked"),
              ("Returns", "Do the same return reasons come back every month?", "Root cause fixed"),
              ("Manual work", "Does your team rebuild the same report every week?", "Automated")],
    "leak_q": "Sound familiar?", "leak_a": "The free check-up finds it ›", "leak_c": "Or estimate it in a minute ›",
    "how_h": "A fixed eight-week project with a clear finish line.", "how_p": "It starts with a free check-up. If the numbers justify it, we begin.",
    "plan": [("Before · free", "Check-up", "A short conversation and a few summary figures."),
             ("Weeks 1–2", "Diagnose", "Data, processes and people. A baseline and a list of losses."),
             ("Weeks 3–4", "Pilot", "Two or three fixes, approved by leadership. The first one goes live."),
             ("Weeks 5–7", "Implement", "AI, automation and CRM in place. Results tracked every week."),
             ("Week 8", "Hand over", "Before and after, training, an internal owner, documentation.")],
    "m_h": "We measure profit, not just sales.", "m_p": "Revenue alone is not success. Every gain is reported on its own, and never counted twice.",
    "metrics": [("Profit", "contribution, not sales"), ("Cash", "costs removed, money recovered"), ("Time", "hours released, not counted as cash"), ("Forecast", "kept apart, assumptions shown")],
    "cases_note": "From our team's work · client names kept confidential", "swipe": " · swipe ›",
    "cases": [("6", "x", "orders in five months", "Omnichannel retail platform, MENA. Also 5x revenue, 4x ROAS."),
              ("750", "+", "suppliers managed", "Cross-border operation across 4 marketplaces and 3 regions."),
              ("50", "", "stores in scope", "AI transformation advisory for a retail brand. Ongoing.")],
    "w_k": "Selected work", "w_h": "Work we have led", "w_p": "Three engagements, told the same way. Client names are kept confidential.",
    "work": [
      {"k": "Omnichannel retail platform · MENA · 5 months",
       "h": "6x orders while acquisition cost fell 80%",
       "ctx": "An e-commerce and retail platform with a website, a mobile app and stores.",
       "brief": "Grow orders and revenue across acquisition, retention and lifetime value without letting acquisition costs run away.",
       "built": "Unit-economics model and customer segmentation, attribution and campaign-efficiency framework, martech for search, mobile attribution and CRM automation, a redesigned site and app.",
       "res": [("6x", "orders"), ("5x", "revenue"), ("−80%", "acquisition cost"), ("4x", "ROAS")]},
      {"k": "Global consumer-brand manufacturer · Türkiye · 2 months",
       "h": "More digital revenue and lower campaign costs in two months",
       "ctx": "A global manufacturer selling through 50 own stores, marketplaces and its online store.",
       "brief": "Raise returns on digital advertising and improve the profitability of campaigns within a short engagement.",
       "built": "Monthly digital-ad optimisation of budget and creatives, campaign-product and shipping-cost optimisation, and the groundwork for demand forecasting and AI content.",
       "res": [("+40%", "revenue, digital channels"), ("20%", "saved on campaign-product and shipping costs")]},
      {"k": "Cross-border commerce · advisory · 2022–2024",
       "h": "From Turkish suppliers to CIS and GCC marketplaces, without holding stock",
       "ctx": "A cross-border retail e-commerce operation selling fashion, beauty and FMCG on the leading marketplaces in each region.",
       "brief": "Sell on overseas marketplaces from Turkish supply without tying up cash in inventory.",
       "built": "A Türkiye-based sourcing network and a stock-free flow-through model: goods are bought and shipped as orders arrive, with pricing, campaign and marketplace optimisation on top.",
       "res": [("$2M", "monthly revenue within the first year"), ("750+", "suppliers"), ("2", "regions")]}],
    "brief_l": "Brief", "built_l": "What was built", "res_l": "Results", "prev": "Previous case", "next": "Next case", "case_l": "Case",
    "ex_cta": "Find your own leaks in a free check-up ›",
    "p_h": "The people you meet do the work.", "p_p": "Small senior team, hands-on from day one to handover.",
    "principles": [("Senior only", "Senior people on every project.", "Every project is run by practitioners with 15+ years in marketplaces and retail. Nothing is passed down the line."),
                   ("Hands-on", "We build it with you.", "Not a report and a goodbye. We work inside the project, with your team, until it runs."),
                   ("Ownership", "We answer for the result.", "An agreed baseline, weekly tracking, and a before-and-after you can check yourself."),
                   ("Shared experience", "What we know stays with you.", "Your team learns on real work. Training and documentation are part of every project.")],
    "p_foot": "Experience across Turkey, Europe, the CIS and MENA · marketplaces, brands and manufacturers",
    "c_h": "Know where you stand before you commit.", "c_p": "Start with the check-up. The call comes after, once we have seen your numbers.",
    "cards": [("2 minutes", "Request a free check-up", "A few questions about your business. Then you pick a time for a 30-minute call.", "Start the check-up"),
              ("Quick question", "Message on WhatsApp", "Write to us directly. We reply within working hours.", "Open WhatsApp")],
    "c_mobile": ("Request a free check-up", "WhatsApp"),
  },
  "cu": {
    "title": "Free e-commerce check-up — AI Trade",
    "desc": "A 30-minute call and a few summary figures. Find out where your e-commerce profit leaks and whether a project is worth it. No commitment.",
    "eyebrow": "Free check-up", "h1": "Find out where your profit leaks.", "lead": "A 30-minute call and a few summary figures. No commitment.",
    "fit": "<strong>We help most</strong> companies with 1,000+ monthly orders, where leadership takes part. Smaller? You can still apply; if it is not a fit, we will tell you plainly.", "gets_k": "You get", "gets": ["Where your biggest losses are", "A rough size of the opportunity", "An honest view on whether a project is worth it"],
    "steplabel": "Step {n} of {t}", "multi_hint": "Select all that apply.", "next_btn": "Continue", "time": "About 2 minutes",
    "qs": [("channel", "Where do you sell?", ["Our own website", "Local marketplaces", "International marketplaces"], "multi"),
           ("orders", "Monthly orders", ["Under 1,000", "1,000–5,000", "5,000–20,000", "20,000+"]),
           ("concern", "Biggest concern right now", ["Campaign and product profitability", "Advertising efficiency", "Returns, cancellations, stock", "Manual work and reporting", "Not sure yet"]),
           ("timing", "When would you like to start?", ["This month", "Within 1–3 months", "Just exploring"]),
           ("role", "Your role", ["Owner / General manager", "E-commerce manager", "Marketing", "Other"])],
    "c_h": "Where should we reply?", "f_name": "Full name", "f_email": "Work email", "f_company": "Company", "f_phone": "Phone (optional)",
    "f_note": "Anything we should know? (optional)", "f_note_ph": "e.g. a recent drop in margin, a campaign that worries you",
    "e_name": "Please enter your name", "e_email": "Please use your company email (Gmail, Hotmail and similar are not accepted)", "f_web": "Company website or store link", "e_web": "Please add your website or store link", "e_company": "Please enter your company",
    "consent": "I agree that my details are used to respond to this request, as described in the <a href=\"{privacy}\">privacy notice</a>.",
    "submit": "Send request", "send_err": "Couldn't send. Please try again or message us on WhatsApp.",
    "d_h": "Thanks. We'll reply within one business day.", "d_p": "Want to skip the wait? Pick a time for the 30-minute call now.",
    "d_btn": "Pick a time", "d_sum": "Your answers", "restart": "Start again", "back": "‹ Back",
    "alt": "Question before you start? <a href=\"{wa}\">Message us on WhatsApp</a>",
    "founder": "Your check-up is led by our founder Hakan Aydın, 15+ years running e-commerce at n11 and eBay. <a href=\"{li}\">LinkedIn ›</a>",
    "r_k": "What you receive", "r_h": "A one-page assessment in plain language", "r_p": "This is what a check-up summary looks like. The company is fictional and the figures are blurred.",
    "r": {"tag": "Sample", "title": "Check-up summary", "for": "Prepared for Example Brand Ltd.",
          "profile": [("Channels", "Own store + 2 marketplaces", False), ("Monthly orders", "≈ 8,000", False), ("Monthly ad spend", "₺ 640,000", True)],
          "leaks_h": "Top three leaks", "cols": ("Leak", "Evidence", "Est. monthly impact", "Priority"),
          "rows": [("Discount campaigns below contribution margin", "14 products sold at negative contribution in the last 90 days", "₺ 185,000", "High"),
                   ("Ad spend on low-stock products", "9% of spend went to items with under 3 days of stock", "₺ 57,000", "High"),
                   ("Manual weekly reporting", "About 11 hours a week across two people", "11 h / week", "Medium")],
          "view_h": "Our view", "view": "A project is likely to pay for itself. Recommended focus: leaks 1 and 2.",
          "next_h": "Next step", "next": "A fixed-scope proposal for an eight-week project.", "hidden": "figure hidden in sample"},
    "a_h": "What we look at",
    "areas": [("Profitability", "Which products or channels pull profit down."), ("Ads and CRM", "Where budget is wasted, how repeat buying is tracked."),
              ("Operations", "Which recurring tasks eat the most time."), ("Returns and stock", "Which losses could be prevented."),
              ("Readiness", "Who decides, and whether the data is reachable.")],
    "notes": ["Summary figures are enough. Your data is used only for the check-up.", "We can sign an NDA before you share any data."],
    "faq_h": "Questions",
    "faq": [("Is it really free?", "Yes. No fee and no obligation. If a project does not make economic sense, we will say so."),
            ("What data do you need?", "Summary figures for the last three months: revenue, margin, ad spend, returns. No system access at this stage."),
            ("What happens after?", "You receive a short written assessment. If there is a clear opportunity, we propose a fixed-scope project.")],
  },
  "privacy": {
    "title": "Privacy & KVKK notice — AI Trade",
    "desc": "How AI Trade handles the personal data you share through this website.",
    "draft": "",
    "h1": "Privacy & KVKK notice",
    "body": [
      ("Who we are", "AI Trade is a sole proprietorship run by Hakan Aydın in Istanbul, Türkiye, acting as data controller under the Turkish Personal Data Protection Law No. 6698 (KVKK). Address: Cevizli Mah. Zühal Cad. A Ticari Blok Apt. No:46/50, Maltepe/İstanbul. Contact: hakan.aydin@aitradeai.net."),
      ("What we collect", "When you request a check-up: your name, work email, company, phone (optional), your note (optional) and your answers to the form questions. When you book a call, Google Calendar collects the details you enter there."),
      ("Why we use it", "Only to reply to your request, arrange the call and prepare the check-up. We do not sell your data or use it for advertising."),
      ("Legal basis", "Taking steps at your request before a possible contract, and our legitimate interest in responding to business enquiries (KVKK Article 5/2 (c) and (f))."),
      ("Where it is stored", "Form answers are stored in our Google Workspace account (Google Sheets and Gmail). Google may process this data on servers outside Türkiye. Fonts are served from this website. This site sets no cookies. We use Cloudflare Web Analytics, which counts page visits without cookies and without identifying individual visitors."),
      ("How long we keep it", "Up to two years after our last contact, unless a business relationship requires longer."),
      ("Your rights", "Under KVKK Article 11 you can ask what data we hold, request correction or deletion, and object to processing. Write to hakan.aydin@aitradeai.net.")],
  },
},
"tr": {
  "wa_text": "Merhaba, ücretsiz check-up hakkında konuşmak istiyorum.",
  "nav": {"how": "Nasıl çalışıyoruz", "results": "Sonuçlar", "about": "Hakkımızda", "contact": "İletişim", "cta": "Ücretsiz check-up", "menu": "Menüyü aç", "lang_label": "Dil"},
  "footer": {"copy": "© 2026 AI Trade · İstanbul, Türkiye", "contact": "İletişim", "privacy": "Gizlilik ve KVKK", "li": "LinkedIn"},
  "fab": "Konuşalım",
  "home": {
    "title": "AI Trade — E-ticaret kârlılık danışmanlığı",
    "desc": "E-ticaretinizde para ve zaman kaybını buluyor, en önemlisini çözüyor, çalışan sistemi sekiz haftada ekibinize devrediyoruz. Ücretsiz check-up.",
    "eyebrow": "AI destekli e-ticaret kâr ortağınız",
    "h1": "Daha az kayıp.<br>Daha fazla kâr.",
    "lead": "E-ticaret operasyonunuzun nerede para ve zaman kaybettiğini buluyor, en önemlisini çözüyor ve çalışan sistemi ekibinize devrediyoruz.", "lead_weeks": "Sekiz haftada.",
    "cta": "Ücretsiz check-up isteyin", "ghost": "Kaybınızı kabaca hesaplayın ›",
    "panel_kicker": "Katkı kârı · haftalık", "panel_title": "Proje öncesi ve sonrası", "panel_tag": "Örnek görünüm",
    "chart_aria": "Örnek grafik: haftalık katkı kârı çözümler devreye girene kadar yatay seyrediyor, sonra başlangıç seviyesinin üzerine çıkıyor",
    "chart_base": "Başlangıç", "chart_live": "Çözümler devrede", "chart_w1": "1. hafta", "chart_w8": "8. hafta",
    "rows": [("Stoksuz ürün reklamları", "Durduruldu"), ("Mükerrer kargo ücretleri", "Geri alındı"), ("Haftalık satış raporu", "Otomatik")],
    "steps": [("Bul.", "Para ve zamanın kaçtığı yerleri."), ("Çöz.", "En çok önemli olan iki üç sorunu."), ("Öğret.", "Ekibinize, gerçek iş üzerinde."), ("Devret.", "Sahip olduğunuz, yürüttüğünüz bir sistem.")],
    "leak_h": "Kâr nadiren bir anda kaybolur.",
    "leak_p": "Bir siparişin yolculuğunun her adımında sızar. Her sızıntıyı bulup kapatıyoruz.",
    "nodes": [("Reklam", "Reklam harcamasının ne kadarı kâra dönüyor, net görebiliyor musunuz?", "Zarar ettiren harcama durduruldu"),
              ("Sipariş", "Kampanyalar ciroyu büyütüyor. Peki kârı da büyütüyor mu?", "Yeniden fiyatlandı ya da durduruldu"),
              ("Kargo", "Kargo faturalarında tam olarak neye ödeme yaptığınızı biliyor musunuz?", "Doğru firma, her fatura kontrol edildi"),
              ("İade", "Aynı nedenle gelen iadeler her ay tekrar ediyor mu?", "Kök neden çözüldü"),
              ("Manuel iş", "Ekibiniz her hafta aynı raporu yeniden mi hazırlıyor?", "Otomatikleşti")],
    "leak_q": "Tanıdık geliyor mu?", "leak_a": "Ücretsiz check-up bulur ›", "leak_c": "Ya da bir dakikada hesaplayın ›",
    "how_h": "Net bir bitişi olan, sekiz haftalık sabit kapsamlı bir proje.", "how_p": "Ücretsiz check-up ile başlar. Rakamlar gerekçelendirirse işe koyuluruz.",
    "plan": [("Önce · ücretsiz", "Check-up", "Kısa bir görüşme ve birkaç özet rakam."),
             ("1–2. hafta", "Teşhis", "Veri, süreç ve ekip. Başlangıç ölçümü ve kayıp listesi."),
             ("3–4. hafta", "Pilot", "Yönetimin onayladığı iki üç çözüm. İlki devreye girer."),
             ("5–7. hafta", "Uygulama", "AI, otomasyon ve CRM kurulur. Sonuçlar her hafta izlenir."),
             ("8. hafta", "Devir", "Önce-sonra karşılaştırması, eğitim, iç sorumlu, dokümantasyon.")],
    "m_h": "Sadece satışı değil, kârı ölçüyoruz.", "m_p": "Tek başına ciro artışı başarı değildir. Her kazanç ayrı raporlanır, hiçbiri iki kez sayılmaz.",
    "metrics": [("Kâr", "ciro değil, katkı kârı"), ("Nakit", "kaldırılan maliyet, geri alınan para"), ("Zaman", "kazanılan saat, nakit sayılmaz"), ("Tahmin", "ayrı tutulur, varsayımlar açık")],
    "cases_note": "Ekibimizin çalışmalarından · müşteri adları gizli", "swipe": " · kaydırın ›",
    "cases": [("6", "x", "beş ayda sipariş", "Çok kanallı perakende platformu, MENA. Ayrıca 5x gelir, 4x ROAS."),
              ("750", "+", "yönetilen tedarikçi", "Sınır ötesi operasyon, 4 pazar yeri ve 3 bölge."),
              ("50", "", "mağaza kapsamda", "Bir perakende markası için AI dönüşüm danışmanlığı. Devam ediyor.")],
    "w_k": "Seçili işler", "w_h": "Yürüttüğümüz işler", "w_p": "Üç proje, aynı formatta. Müşteri adları gizli tutulur.",
    "work": [
      {"k": "Çok kanallı perakende platformu · MENA · 5 ay",
       "h": "Edinme maliyeti %80 düşerken 6 kat sipariş",
       "ctx": "Web sitesi, mobil uygulama ve mağazaları olan bir e-ticaret ve perakende platformu.",
       "brief": "Edinme, elde tutma ve yaşam boyu değer boyunca sipariş ve ciroyu büyütmek; bunu edinme maliyetini kontrol altında tutarak yapmak.",
       "built": "Birim ekonomisi modeli ve müşteri segmentasyonu, atıf ve kampanya verimliliği çerçevesi, arama, mobil atıf ve CRM otomasyonu için martech, yenilenen site ve uygulama.",
       "res": [("6x", "sipariş"), ("5x", "ciro"), ("−%80", "edinme maliyeti"), ("4x", "ROAS")]},
      {"k": "Global tüketici markası üreticisi · Türkiye · 2 ay",
       "h": "İki ayda daha fazla dijital ciro, daha düşük kampanya maliyeti",
       "ctx": "50 mağaza, pazar yerleri ve kendi online mağazası üzerinden satış yapan global bir üretici.",
       "brief": "Kısa bir projede dijital reklam getirisini artırmak ve kampanyaların kârlılığını iyileştirmek.",
       "built": "Bütçe ve kreatif bazında aylık dijital reklam optimizasyonu, kampanyalı ürün ve kargo maliyeti optimizasyonu, talep tahmini ve AI içerik için altyapı hazırlığı.",
       "res": [("+%40", "ciro, dijital kanallar"), ("%20", "kampanyalı ürün ve kargo maliyetinde tasarruf")]},
      {"k": "Sınır ötesi ticaret · danışmanlık · 2022–2024",
       "h": "Türk tedarikçilerden BDT ve Körfez pazar yerlerine, stok tutmadan",
       "ctx": "Moda, güzellik ve hızlı tüketim ürünlerini her bölgenin önde gelen pazar yerlerinde satan bir sınır ötesi perakende operasyonu.",
       "brief": "Stoka nakit bağlamadan, Türkiye'deki tedarikle yurt dışı pazar yerlerinde satış yapmak.",
       "built": "Türkiye merkezli tedarik ağı ve stoksuz flow-through modeli: ürün sipariş geldikçe alınıp gönderiliyor; üstünde fiyat, kampanya ve pazar yeri optimizasyonu.",
       "res": [("2M $", "ilk yıl içinde aylık ciro"), ("750+", "tedarikçi"), ("2", "bölge")]}],
    "brief_l": "Hedef", "built_l": "Kurulanlar", "res_l": "Sonuçlar", "prev": "Önceki vaka", "next": "Sonraki vaka", "case_l": "Vaka",
    "ex_cta": "Kendi sızıntılarınızı ücretsiz check-up'ta bulun ›",
    "p_h": "Tanıştığınız kişiler işi yapar.", "p_p": "Küçük, kıdemli bir ekip; ilk günden devire kadar işin içinde.",
    "principles": [("Yalnızca kıdemli", "Her projede kıdemli ekip.", "Her proje pazar yeri ve perakendede 15+ yıllık deneyime sahip kişilerce yürütülür. İş alt kademeye devredilmez."),
                   ("Uygulamada", "Sizinle birlikte kuruyoruz.", "Rapor verip ayrılmıyoruz. Sistem çalışana kadar ekibinizle projenin içindeyiz."),
                   ("Sahiplik", "Sonucun hesabını veriyoruz.", "Mutabık kalınan başlangıç ölçümü, haftalık takip ve kendiniz kontrol edebileceğiniz bir önce-sonra."),
                   ("Deneyim paylaşımı", "Bildiklerimiz sizde kalır.", "Ekibiniz gerçek iş üzerinde öğrenir. Eğitim ve dokümantasyon her projeye dahildir.")],
    "p_foot": "Türkiye, Avrupa, BDT ve MENA'da deneyim · pazar yerleri, markalar ve üreticiler",
    "c_h": "Karar vermeden önce nerede durduğunuzu bilin.", "c_p": "Check-up ile başlayın. Görüşme, rakamlarınızı gördükten sonra gelir.",
    "cards": [("2 dakika", "Ücretsiz check-up isteyin", "İşletmeniz hakkında birkaç soru. Ardından 30 dakikalık görüşme için saat seçersiniz.", "Check-up'a başla"),
              ("Kısa bir soru", "WhatsApp'tan yazın", "Doğrudan yazın, mesai saatlerinde yanıtlıyoruz.", "WhatsApp'ı aç")],
    "c_mobile": ("Ücretsiz check-up isteyin", "WhatsApp"),
  },
  "cu": {
    "title": "Ücretsiz e-ticaret check-up — AI Trade",
    "desc": "30 dakikalık bir görüşme ve birkaç özet rakam. E-ticaret kârınızın nereden sızdığını ve bir projenin değip değmeyeceğini öğrenin. Taahhüt yok.",
    "eyebrow": "Ücretsiz check-up", "h1": "Kârınızın nereden sızdığını öğrenin.", "lead": "30 dakikalık bir görüşme ve birkaç özet rakam. Taahhüt yok.",
    "fit": "<strong>En çok fayda sağladığımız firmalar:</strong> aylık 1.000+ siparişi olan ve yönetimin sürece dahil olduğu firmalar. Daha küçükseniz de yazabilirsiniz; uygun değilse açıkça söyleriz.", "gets_k": "Neler alırsınız", "gets": ["En büyük kayıplarınızın nerede olduğu", "Fırsatın kabaca büyüklüğü", "Bir projenin değip değmeyeceğine dair dürüst bir görüş"],
    "steplabel": "Adım {n} / {t}", "multi_hint": "Birden fazla seçebilirsiniz.", "next_btn": "Devam", "time": "Yaklaşık 2 dakika",
    "qs": [("channel", "Nerede satıyorsunuz?", ["Kendi web sitemiz", "Yurt içi pazar yerleri", "Yurt dışı pazar yerleri"], "multi"),
           ("orders", "Aylık sipariş sayısı", ["1.000'in altı", "1.000–5.000", "5.000–20.000", "20.000+"]),
           ("concern", "Şu anki en büyük sorun", ["Kampanya ve ürün kârlılığı", "Reklam verimliliği", "İade, iptal ve stok", "Manuel iş ve raporlama", "Henüz emin değilim"]),
           ("timing", "Ne zaman başlamayı düşünüyorsunuz?", ["Bu ay", "1–3 ay içinde", "Sadece araştırıyorum"]),
           ("role", "Rolünüz", ["Şirket sahibi / Genel müdür", "E-ticaret müdürü", "Pazarlama", "Diğer"])],
    "c_h": "Size nereden dönelim?", "f_name": "Ad soyad", "f_email": "İş e-postası", "f_company": "Şirket", "f_phone": "Telefon (isteğe bağlı)",
    "f_note": "Bilmemiz gereken bir şey var mı? (isteğe bağlı)", "f_note_ph": "ör. son dönemde düşen marj, sizi endişelendiren bir kampanya",
    "e_name": "Lütfen adınızı yazın", "e_email": "Lütfen şirket e-postanızı yazın (Gmail, Hotmail vb. kabul edilmiyor)", "f_web": "Şirket web sitesi ya da mağaza linki", "e_web": "Lütfen web sitesi ya da mağaza linkinizi ekleyin", "e_company": "Lütfen şirket adını yazın",
    "consent": "Bilgilerimin bu talebe yanıt vermek için, <a href=\"{privacy}\">aydınlatma metninde</a> açıklandığı şekilde kullanılmasını kabul ediyorum.",
    "submit": "Talebi gönder", "send_err": "Gönderilemedi. Lütfen tekrar deneyin ya da WhatsApp'tan yazın.",
    "d_h": "Teşekkürler. Bir iş günü içinde dönüyoruz.", "d_p": "Beklemek istemiyor musunuz? 30 dakikalık görüşme için şimdi saat seçin.",
    "d_btn": "Saat seçin", "d_sum": "Cevaplarınız", "restart": "Baştan başla", "back": "‹ Geri",
    "alt": "Başlamadan önce sorunuz mu var? <a href=\"{wa}\">WhatsApp'tan yazın</a>",
    "founder": "Check-up'ınızı, n11 ve eBay'de 15+ yıl e-ticaret yönetmiş kurucumuz Hakan Aydın yürütür. <a href=\"{li}\">LinkedIn ›</a>",
    "r_k": "Neler alırsınız", "r_h": "Sade dille yazılmış tek sayfalık bir değerlendirme", "r_p": "Bir check-up özeti böyle görünür. Şirket kurgusaldır, rakamlar bulanıklaştırılmıştır.",
    "r": {"tag": "Örnek", "title": "Check-up özeti", "for": "Örnek Marka A.Ş. için hazırlanmıştır",
          "profile": [("Satış kanalları", "Kendi mağaza + 2 pazar yeri", False), ("Aylık sipariş", "≈ 8.000", False), ("Aylık reklam harcaması", "₺ 640.000", True)],
          "leaks_h": "En büyük üç sızıntı", "cols": ("Sızıntı", "Bulgu", "Tahmini aylık etki", "Öncelik"),
          "rows": [("Katkı marjının altında satan indirim kampanyaları", "Son 90 günde 14 ürün negatif katkıyla satıldı", "₺ 185.000", "Yüksek"),
                   ("Stoğu azalan ürünlere reklam harcaması", "Harcamanın %9'u stoğu 3 günden az olan ürünlere gitti", "₺ 57.000", "Yüksek"),
                   ("Manuel haftalık raporlama", "İki kişide haftada yaklaşık 11 saat", "Haftada 11 saat", "Orta")],
          "view_h": "Görüşümüz", "view": "Bir projenin kendini amorti etmesi muhtemel. Önerilen odak: 1 ve 2 numaralı sızıntılar.",
          "next_h": "Sonraki adım", "next": "Sekiz haftalık, kapsamı belli sabit ücretli bir proje teklifi.", "hidden": "örnekte gizlenen rakam"},
    "a_h": "Neye bakıyoruz",
    "areas": [("Kârlılık", "Hangi ürün ya da kanal kârı aşağı çekiyor."), ("Reklam ve CRM", "Bütçe nerede boşa gidiyor, tekrar alım nasıl izleniyor."),
              ("Operasyon", "Hangi tekrarlayan işler en çok zamanı alıyor."), ("İade ve stok", "Hangi kayıplar önlenebilir."),
              ("Hazırlık", "Kararı kim veriyor, verilere ulaşılabiliyor mu.")],
    "notes": ["Özet rakamlar yeterli. Verileriniz yalnızca check-up için kullanılır.", "Veri paylaşmadan önce gizlilik sözleşmesi (NDA) imzalayabiliriz."],
    "faq_h": "Sorular",
    "faq": [("Gerçekten ücretsiz mi?", "Evet. Ücret ve yükümlülük yok. Bir proje ekonomik olarak anlamlı değilse bunu açıkça söyleriz."),
            ("Hangi verilere ihtiyacınız var?", "Son üç ayın özet rakamları: ciro, marj, reklam harcaması, iadeler. Bu aşamada sistem erişimi gerekmez."),
            ("Sonrasında ne oluyor?", "Kısa bir yazılı değerlendirme alırsınız. Net bir fırsat varsa, kapsamı belli sabit ücretli bir proje öneririz.")],
  },
  "privacy": {
    "title": "Gizlilik ve KVKK aydınlatma metni — AI Trade",
    "desc": "AI Trade'in bu site üzerinden paylaştığınız kişisel verileri nasıl işlediği.",
    "draft": "",
    "h1": "Gizlilik ve KVKK aydınlatma metni",
    "body": [
      ("Veri sorumlusu", "AI Trade, İstanbul'da Hakan Aydın tarafından yürütülen bir şahıs işletmesidir ve 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) kapsamında veri sorumlusudur. Adres: Cevizli Mah. Zühal Cad. A Ticari Blok Apt. No:46/50, Maltepe/İstanbul. İletişim: hakan.aydin@aitradeai.net."),
      ("Hangi verileri topluyoruz", "Check-up talebinde: adınız, iş e-postanız, şirketiniz, telefonunuz (isteğe bağlı), notunuz (isteğe bağlı) ve form sorularına verdiğiniz cevaplar. Görüşme ayarladığınızda, oraya girdiğiniz bilgileri Google Takvim toplar."),
      ("Neden kullanıyoruz", "Yalnızca talebinize yanıt vermek, görüşmeyi ayarlamak ve check-up'ı hazırlamak için. Verilerinizi satmıyor, reklam amacıyla kullanmıyoruz."),
      ("Hukuki sebep", "Bir sözleşmenin kurulmasından önce talebiniz üzerine adım atılması ve iş taleplerine yanıt vermekteki meşru menfaatimiz (KVKK m. 5/2 (c) ve (f))."),
      ("Nerede saklanıyor", "Form cevapları Google Workspace hesabımızda (Google Sheets ve Gmail) saklanır. Google bu verileri Türkiye dışındaki sunucularda işleyebilir. Yazı tipleri bu siteden yüklenir. Bu site çerez kullanmaz. Ziyaretleri çerezsiz ve ziyaretçileri tek tek tanımlamadan sayan Cloudflare Web Analytics kullanılır."),
      ("Ne kadar süre saklıyoruz", "Bir iş ilişkisi daha uzun süre gerektirmedikçe, son iletişimimizden sonra en fazla iki yıl."),
      ("Haklarınız", "KVKK m. 11 kapsamında hangi verilerinizi tuttuğumuzu sorabilir, düzeltilmesini ya da silinmesini isteyebilir ve işlemeye itiraz edebilirsiniz. hakan.aydin@aitradeai.net adresine yazmanız yeterli.")],
  },
},
}

# --- Profit-leak estimator and example AI workflows (v5) ---
T["en"]["home"].update({
    "calc_k": "Estimate", "calc_h": "What could this be worth for you?",
    "calc_p": "Enter a few rough monthly figures. You get a cautious estimate, not a promise. The check-up replaces it with real numbers.",
    "calc_cur": "Currency", "calc_cur_default": "$",
    "calc_f": [("rev", "Monthly revenue", "250,000", "money", ""),
               ("ads", "Monthly ad spend", "20,000", "money", ""),
               ("disc", "Share of sales on discount", "35", "pct", ""),
               ("ret", "Return and cancellation rate", "8", "pct", ""),
               ("logi", "Shipping and fulfilment cost, as a share of revenue", "10", "pct", "Carrier, packaging, warehouse handling"),
               ("hrs", "Team hours a week on repetitive manual work", "40", "hrs", "Reports, data entry, stock and price updates, routine customer replies")],
    "calc_lines": [("camp", "Campaigns"), ("ad", "Ads"), ("logi", "Shipping and fulfilment"), ("rets", "Returns")],
    "calc_total": "Estimated profit gain per year", "calc_range": "Cautious range", "calc_plus": "+ Also",
    "calc_hours": "{h} hours", "calc_week": "/ week", "calc_back": "back to the team",
    "calc_days": "≈ {d} working days", "calc_fte": "{f} full-time staff", "calc_fte_hours": 40,
    "calc_time_p": "Time that goes back to analysis, customers and growth.",
    "calc_note": "Time is shown separately and is not added to the profit figure.",
    "calc_how": "How is this calculated?",
    "calc_method": ["The headline figure is the middle of a cautious range: <range>. Team time is shown separately and is not added to it.",
                    "Campaigns: 1.5–4% of discounted revenue. Part of discounted sales usually lands below contribution margin; fixing campaign rules recovers some of it.",
                    "Ads: 5–12% of ad spend. Typical waste is spend on low-stock or low-margin products and overlapping audiences.",
                    "Returns: 10–20% of returns are preventable, and each return costs roughly 15% of its order value.",
                    "Shipping and fulfilment: 5–10% of that cost, through carrier choice by size and region, packaging, free-shipping thresholds and avoiding duplicate shipments.",
                    "Time: 40–60% of repetitive manual work can be automated. Full-time equivalent uses a 40-hour week and an 8-hour working day.",
                    "These ratios come from our project experience. They are deliberately cautious and will differ for your business."],
    "calc_cta": "Check these numbers with a free check-up", "calc_carry": "Your figures will be added to the request.",
    "fl_k": "Example workflows", "fl_h": "What the AI actually does.",
    "fl_p": "Systems like these run inside your existing tools and work for your team. Built and handed over during the eight weeks.",
    "fl_tag": "Example workflow", "swipe": "Swipe ›",
    "flows": [
        {"t": "stock", "h": "Low stock pauses the ad", "p": "When a product drops below three days of stock, its ads pause and the team gets a message.",
         "prod": "Product A", "stock": "Stock", "d1": "12 days", "d2": "2 days", "ad": "Ads", "on": "Running", "off": "Paused",
         "toast": "Team notified: ads for Product A paused, 2 days of stock left"},
        {"t": "alert", "h": "A sudden drop raises an alarm", "p": "If conversion, orders or ad costs move sharply, the right person hears about it within minutes, not at month end.",
         "chip": "Conversion rate · today", "alert": "Alarm: conversion down 40% in the last 2 hours", "alert2": "Check the payment step · sent to e-mail and WhatsApp"},
        {"t": "report", "h": "Monday 08:00, the report is ready", "p": "Contribution profit by channel, product and campaign is calculated every week and lands in your inbox.",
         "clock": "Mon 08:00", "mail": "Weekly profit report", "mail2": "Contribution profit · channels · products"},
        {"t": "camp", "h": "Loss-making campaigns get flagged", "p": "Products selling below contribution margin are flagged before the campaign ends, with a suggested fix.",
         "rows": [("Product A", "20% off", "+$5.20"), ("Product B", "35% off", "−$4.10"), ("Product C", "15% off", "+$2.40")],
         "fix": "Suggestion: cut the discount to 20%"},
        {"t": "carrier", "h": "The right carrier for each parcel", "p": "Each order goes to the carrier with the best price that still meets the delivery promise, by size and region.",
         "order": "Order #4821 · 3 kg · Region 2", "rows": [("Carrier A", "$9.20", "2 days"), ("Carrier B", "$7.80", "2 days"), ("Carrier C", "$7.10", "4 days")],
         "pick": "Selected"},
        {"t": "returns", "h": "Return reasons, read and grouped", "p": "AI reads return notes and reviews, groups the reasons by product and suggests what to fix on the page.",
         "rows": [("Runs small", 46), ("Colour differs", 22), ("Arrived damaged", 12)], "fix": "Suggestion: add a size chart to the product page"},
        {"t": "reply", "h": "Reply drafts for routine questions", "p": "For questions like order status, AI drafts the answer from the order data. A team member approves it in one click.",
         "q": "Where is my order?", "a": "Your parcel left the warehouse today and should arrive tomorrow. Tracking: TR-48210.", "btn": "Approve and send"},
        {"t": "more", "tag": "Beyond these", "h": "And other places it fits", "p": "Every check-up starts with where your time and money go, then picks the workflows that pay back first.",
         "tags": ["Competitor price tracking", "Stock transfers between stores", "Product content", "CRM segments", "Marketplace listing checks", "Supplier orders"]},
    ],
})
T["en"]["cu"].update({"calc_in": "Your estimate from the calculator is attached to this request."})
T["tr"]["home"].update({
    "calc_k": "Tahmin", "calc_h": "Sizin için ne kadar edebilir?",
    "calc_p": "Birkaç kaba aylık rakam girin. Söz değil, temkinli bir tahmin görürsünüz. Check-up bunu gerçek rakamlarla netleştirir.",
    "calc_cur": "Para birimi", "calc_cur_default": "₺",
    "calc_f": [("rev", "Aylık ciro", "5.000.000", "money", ""),
               ("ads", "Aylık reklam harcaması", "400.000", "money", ""),
               ("disc", "İndirimli satışların payı", "35", "pct", ""),
               ("ret", "İade ve iptal oranı", "8", "pct", ""),
               ("logi", "Kargo ve elleçleme maliyetinin ciroya oranı", "8", "pct", "Kargo, paketleme, depo elleçleme"),
               ("hrs", "Ekibin tekrarlayan manuel işlere haftada ayırdığı saat", "40", "hrs", "Raporlar, veri girişi, stok ve fiyat güncellemeleri, rutin müşteri yanıtları")],
    "calc_lines": [("camp", "Kampanyalar"), ("ad", "Reklam"), ("logi", "Kargo ve elleçleme"), ("rets", "İadeler")],
    "calc_total": "Tahmini yıllık kâr kazancı", "calc_range": "Temkinli aralık", "calc_plus": "+ Ayrıca",
    "calc_hours": "{h} saat", "calc_week": "/ hafta", "calc_back": "ekibe geri döner",
    "calc_days": "≈ {d} iş günü", "calc_fte": "{f} tam zamanlı kişi", "calc_fte_hours": 45,
    "calc_time_p": "Bu zaman analize, müşteriye ve büyümeye döner.",
    "calc_note": "Zaman ayrı gösterilir, kâr rakamına eklenmez.",
    "calc_how": "Hesap nasıl yapılıyor?",
    "calc_method": ["Büyük rakam, temkinli bir aralığın ortasıdır: <range>. Ekip zamanı ayrı gösterilir, kâra eklenmez.",
                    "Kampanyalar: indirimli cironun %1,5–4'ü. İndirimli satışların bir kısmı genelde katkı marjının altında kalır; kampanya kurallarını düzeltmek bunun bir kısmını geri kazandırır.",
                    "Reklam: reklam harcamasının %5–12'si. Tipik kayıp, stoğu azalan ya da marjı düşük ürünlere ve çakışan kitlelere giden harcamadır.",
                    "İadeler: iadelerin %10–20'si önlenebilir; her iadenin maliyeti sipariş tutarının yaklaşık %15'i kadardır.",
                    "Kargo ve elleçleme: bu maliyetin %5–10'u; desi ve bölgeye göre kargo firması seçimi, paketleme, ücretsiz kargo eşiği ve mükerrer gönderimlerin önlenmesiyle.",
                    "Zaman: tekrarlayan manuel işin %40–60'ı otomatikleştirilebilir. Tam zamanlı eşdeğer haftalık 45 saat, iş günü 9 saat üzerinden hesaplanır.",
                    "Oranlar proje deneyimimize dayanır, bilerek temkinli tutulmuştur ve sizin işinizde farklı çıkacaktır."],
    "calc_cta": "Bu rakamları ücretsiz check-up ile netleştirin", "calc_carry": "Girdiğiniz rakamlar talebinize eklenir.",
    "fl_k": "Örnek iş akışları", "fl_h": "Yapay zekâ burada ne yapıyor?",
    "fl_p": "Bu tür sistemler mevcut araçlarınızın içinde, ekibiniz için çalışır. Sekiz hafta içinde kurulur ve ekibe devredilir.",
    "fl_tag": "Örnek iş akışı", "swipe": "Kaydırın ›",
    "flows": [
        {"t": "stock", "h": "Stok azalınca reklam durur", "p": "Stoğu üç günün altına düşen ürünün reklamı kendiliğinden duraklar, ekibe mesaj gider.",
         "prod": "Ürün A", "stock": "Stok", "d1": "12 gün", "d2": "2 gün", "ad": "Reklam", "on": "Açık", "off": "Duraklatıldı",
         "toast": "Ekibe bildirim: Ürün A reklamı durduruldu, 2 günlük stok kaldı"},
        {"t": "alert", "h": "Ani düşüşte alarm çalar", "p": "Dönüşüm, sipariş ya da reklam maliyeti sert değişirse doğru kişi ay sonunu beklemeden, dakikalar içinde haberdar olur.",
         "chip": "Dönüşüm oranı · bugün", "alert": "Alarm: dönüşüm son 2 saatte %40 düştü", "alert2": "Ödeme adımı kontrol edilmeli · e-posta ve WhatsApp'a gönderildi"},
        {"t": "report", "h": "Pazartesi 08:00, rapor hazır", "p": "Kanal, ürün ve kampanya bazında katkı kârı her hafta hesaplanır ve gelen kutunuza düşer.",
         "clock": "Pzt 08:00", "mail": "Haftalık kâr raporu", "mail2": "Katkı kârı · kanallar · ürünler"},
        {"t": "camp", "h": "Zarar eden kampanya işaretlenir", "p": "Katkı marjının altında satan ürünler kampanya bitmeden işaretlenir, bir düzeltme önerisiyle birlikte.",
         "rows": [("Ürün A", "%20 indirim", "+₺46"), ("Ürün B", "%35 indirim", "−₺38"), ("Ürün C", "%15 indirim", "+₺21")],
         "fix": "Öneri: indirimi %20'ye çek"},
        {"t": "carrier", "h": "Her pakete doğru kargo", "p": "Her sipariş, desi ve bölgeye göre teslim sözünü tutan en uygun fiyatlı kargo firmasına otomatik atanır.",
         "order": "Sipariş #4821 · 3 desi · İzmir", "rows": [("Kargo A", "₺92", "2 gün"), ("Kargo B", "₺78", "2 gün"), ("Kargo C", "₺71", "4 gün")],
         "pick": "Seçildi"},
        {"t": "returns", "h": "İade nedenleri okunur, gruplanır", "p": "Yapay zekâ iade notlarını ve yorumları okur, nedenleri ürün bazında gruplar ve sayfada neyin düzeltileceğini önerir.",
         "rows": [("Kalıbı küçük", 46), ("Renk farklı", 22), ("Hasarlı geldi", 12)], "pct_first": True, "fix": "Öneri: ürün sayfasına beden tablosu ekle"},
        {"t": "reply", "h": "Rutin sorulara yanıt taslağı", "p": "Sipariş durumu gibi sorulara yapay zekâ sipariş verisinden yanıt taslağı hazırlar. Ekipten biri tek tıkla onaylar.",
         "q": "Siparişim nerede?", "a": "Paketiniz bugün depodan çıktı, yarın teslim edilmesi bekleniyor. Takip: TR-48210.", "btn": "Onayla ve gönder"},
        {"t": "more", "tag": "Diğer alanlar", "h": "Ve uygulanabileceği diğer alanlar", "p": "Her check-up, zamanınızın ve paranızın nereye gittiğiyle başlar; önce en hızlı geri dönen iş akışları seçilir.",
         "tags": ["Rakip fiyat takibi", "Mağazalar arası stok transferi", "Ürün içerikleri", "CRM segmentleri", "Pazar yeri ilan kontrolleri", "Tedarikçi siparişleri"]},
    ],
})
T["tr"]["cu"].update({"calc_in": "Hesaplayıcıdaki tahmininiz bu talebe eklenecek."})

# --- v6: hero notification feed, merged team + measurement section ---
T["en"]["home"].update({
    "feed_k": "After the project · a day for your team", "feed_h": "The system watches for you", "feed_tag": "Example view",
    "feed": [("rep", "Mon 08:00", "Weekly profit report is ready", "Contribution profit +6% on last week"),
             ("ad", "08:12", "Ads for Product A paused", "Stock down to 2 days · $160 a day of spend saved"),
             ("ship", "09:40", "Duplicate shipping fee found", "October invoice · $210 refund request ready"),
             ("camp", "11:05", "Campaign B is below margin", "−$4.10 per order · suggestion: cut the discount to 20%")],
    "t_k": "Team and measurement", "t_h": "The people who do the work measure the result.",
    "t_p": "A small senior team, with you from day one to handover. Every gain is measured on its own and never counted twice.",
    "t_team": "Team",
    "t_pr": [("Senior only", "15+ years in marketplaces and retail on every project. Nothing is passed down the line."),
             ("We build it with you", "Not a report and a goodbye. We stay inside your team until the system runs."),
             ("What we know stays with you", "Your team learns on real work. Training and documentation are part of every project.")],
    "t_name": "Hakan Aydın", "t_role": "Founder · 15+ years running e-commerce at n11 and eBay",
    "t_tags": ["E-commerce growth", "E-export", "Marketplaces", "AI and automation"],
    "t_regions": "Türkiye · Europe · CIS · MENA",
    "t_meas": "Measurement · every week",
    "sc_h": "Weekly results card", "sc_tag": "Example view", "sc_week": "Week {n} of 8",
    "sc_rows": [("Contribution profit", "+$9.2K", "against the agreed baseline, not revenue"),
                ("Cash recovered", "$2.1K", "duplicate shipping fees refunded"),
                ("Team time", "18 h / week", "counted on its own, never turned into cash")],
    "sc_foot": "In your inbox every Monday · the baseline is agreed together",
})
T["tr"]["home"].update({
    "feed_k": "Proje sonrası · ekibinizin bir günü", "feed_h": "Sistem sizin yerinize izliyor", "feed_tag": "Örnek görünüm",
    "feed": [("rep", "Pzt 08:00", "Haftalık kâr raporu hazır", "Katkı kârı geçen haftaya göre +%6"),
             ("ad", "08:12", "Ürün A reklamı durduruldu", "Stok 2 güne düştü · günlük ₺3.200 harcama korundu"),
             ("ship", "09:40", "Mükerrer kargo ücreti bulundu", "Ekim faturası · ₺4.120 iade talebi hazır"),
             ("camp", "11:05", "Kampanya B marjın altında", "Sipariş başına −₺38 · öneri: indirimi %20'ye çek")],
    "t_k": "Ekip ve ölçüm", "t_h": "İşi yapan ekip, sonucu da ölçer.",
    "t_p": "Küçük ve kıdemli bir ekip; ilk günden devire kadar sizinle. Her kazanç ayrı ölçülür, hiçbiri iki kez sayılmaz.",
    "t_team": "Ekip",
    "t_pr": [("Yalnızca kıdemli", "Her projede pazar yeri ve perakendede 15+ yıllık deneyim. İş alt kademeye devredilmez."),
             ("Sizinle birlikte kurarız", "Rapor verip gitmeyiz; sistem çalışana kadar ekibinizin içindeyiz."),
             ("Bilgi sizde kalır", "Ekibiniz gerçek iş üzerinde öğrenir; eğitim ve dokümantasyon projeye dahildir.")],
    "t_name": "Hakan Aydın", "t_role": "Kurucu · n11 ve eBay'de 15+ yıl e-ticaret yönetimi",
    "t_tags": ["E-ticaret büyümesi", "E-ihracat", "Pazar yerleri", "AI ve otomasyon"],
    "t_regions": "Türkiye · Avrupa · BDT · MENA",
    "t_meas": "Ölçüm · her hafta",
    "sc_h": "Haftalık sonuç kartı", "sc_tag": "Örnek görünüm", "sc_week": "Hafta {n} / 8",
    "sc_rows": [("Katkı kârı", "+₺184 bin", "birlikte belirlenen başlangıca göre, ciro değil"),
                ("Geri alınan nakit", "₺42 bin", "iade edilen mükerrer kargo ücretleri"),
                ("Ekip zamanı", "18 saat / hafta", "ayrı sayılır, nakde çevrilmez")],
    "sc_foot": "Her pazartesi gelen kutunuzda · başlangıç değeri birlikte belirlenir",
})

# --- v7: measurement as 4th principle, founder card in contact ---
T["en"]["home"]["t_pr"] = T["en"]["home"]["t_pr"] + [("Every gain measured on its own", "Profit, cash and time are reported separately and never counted twice. The baseline is agreed with you.")]
T["tr"]["home"]["t_pr"] = T["tr"]["home"]["t_pr"] + [("Her kazanç ayrı ölçülür", "Kâr, nakit ve zaman ayrı raporlanır, hiçbiri iki kez sayılmaz. Başlangıç değeri sizinle birlikte belirlenir.")]
T["en"]["home"].update({"t_p": "A small senior team, with you from day one to handover.", "who_k": "Who you will talk to", "li_co": "Follow AI Trade on LinkedIn ›"})
T["tr"]["home"].update({"t_p": "Küçük ve kıdemli bir ekip; ilk günden devire kadar sizinle.", "who_k": "Görüşmeyi kim yapıyor", "li_co": "AI Trade'i LinkedIn'de takip edin ›"})

# --- v8: consulting-first framing ---
T["en"]["home"].update({
    "feed_k": "Designed around your business", "feed_h": "What we can build after the check-up",
    "fl_k": "Example solutions", "fl_h": "Not an off-the-shelf tool. Designed around your business.",
    "fl_p": "First we find where the loss is. Then we build the right system inside the tools you already use and hand it to your team. These are examples of what can be built for different businesses.",
    "fl_tag": "Example solution",
    "how_note": "We do not sell software, licences or subscriptions. We work with the tools you already have, and if a new one is needed, we help you choose the right one.",
})
T["tr"]["home"].update({
    "feed_k": "İşinize göre tasarlanır", "feed_h": "Check-up sonrası kurulabilecekler",
    "fl_k": "Örnek çözümler", "fl_h": "Hazır araç değil, işinize göre tasarım.",
    "fl_p": "Önce kaybın nerede olduğunu buluruz. Sonra o soruna uygun sistemi mevcut araçlarınızın içinde kurar, ekibinize devrederiz. Aşağıdakiler farklı işletmelerde kurulabilecek çözümlere örnek.",
    "fl_tag": "Örnek çözüm",
    "how_note": "Yazılım, lisans ya da abonelik satmıyoruz. Mevcut araçlarınızla çalışırız; yeni bir araç gerekirse doğru olanı seçmenize yardım ederiz.",
})
T["en"]["home"]["li_me"] = "Hakan's profile ›"
T["tr"]["home"]["li_me"] = "Hakan'ın profili ›"

# --- v8b: tighter consulting copy ---
T["en"]["home"].update({
    "feed_k": "Example · designed for each business", "feed_h": "Built for you after the check‑up", "feed_tag": "",
    "fl_h": "Built for your business, not off the shelf.",
    "fl_p": "We find the loss first, then build the fix inside the tools you already use. A few examples:",
    "how_pts": ["No software to buy", "Works with your current tools", "Yours after handover"],
})
T["tr"]["home"].update({
    "feed_k": "Örnek · her işletmeye özel tasarlanır", "feed_h": "Check‑up sonrası, size özel", "feed_tag": "",
    "fl_h": "Hazır paket değil, işinize göre kurulur.",
    "fl_p": "Önce kaybı buluruz, sonra çözümü kullandığınız araçların içinde kurarız. Birkaç örnek:",
    "how_pts": ["Yazılım satmıyoruz", "Mevcut araçlarınızla çalışırız", "Devirden sonra sistem sizin"],
})
T["en"]["home"].update({"how_pts": ["No software to buy", "Tools chosen to fit the problem", "Yours after handover"],
    "fl_p": "We find the loss first, then build the right fix for it, with AI where it helps, and hand it to your team. A few examples:"})
T["tr"]["home"].update({"how_pts": ["Yazılım satmıyoruz", "Araçları sorununuza göre seçeriz", "Devirden sonra sistem sizin"],
    "fl_p": "Önce kaybı buluruz, sonra ona uygun çözümü, gereken yerde yapay zekâyla kurar ve ekibinize devrederiz. Birkaç örnek:"})

# --- v9: shorter case cards ---
for _w, _t in zip(T["en"]["home"]["work"], [["Unit-economics model", "Attribution and campaign efficiency", "CRM automation", "Site and app redesign"],
                                             ["Monthly ad optimisation", "Campaign-product costs", "Shipping costs"],
                                             ["Supplier network", "Stock-free flow-through", "Marketplace optimisation"]]):
    _w["tags"] = _t
for _w, _t in zip(T["tr"]["home"]["work"], [["Birim ekonomisi modeli", "Atıf ve kampanya verimliliği", "CRM otomasyonu", "Site ve uygulama yenileme"],
                                             ["Aylık reklam optimizasyonu", "Kampanyalı ürün maliyeti", "Kargo maliyeti"],
                                             ["Tedarik ağı", "Stoksuz flow-through", "Pazar yeri optimizasyonu"]]):
    _w["tags"] = _t
T["en"]["home"].update({"did_l": "What we did", "more_l": "Details"})
T["tr"]["home"].update({"did_l": "Ne yaptık", "more_l": "Detaylar"})

for _l, _new in (("tr", {"ads": "Aylık reklam", "logi": "Kargo ve elleçleme payı", "hrs": "Haftalık manuel iş (ekip, saat)"}), ("en", {"ads": "Monthly ad spend", "logi": "Shipping and fulfilment share", "hrs": "Manual work per week (team hours)"})):
    T[_l]["home"]["calc_f"] = [(k, _new.get(k, lab), v, kind, hint) for k, lab, v, kind, hint in T[_l]["home"]["calc_f"]]

# --- v10: section labels, results section ---
T["en"]["home"].update({"leak_k": "The problem", "how_k": "How we work", "w_k": "Results", "c_k": "Contact"})
T["tr"]["home"].update({"leak_k": "Sorun", "how_k": "Yöntem", "w_k": "Sonuçlar", "c_k": "İletişim"})
T["en"]["home"]["w_p"] = "Three engagements we have led. Client names are kept confidential."
T["tr"]["home"]["w_p"] = "Yürüttüğümüz üç proje. Müşteri adları gizli tutulur."

# --- v11 ---
T["en"]["home"].update({"calc_go": "Calculate", "calc_pre": "Enter your figures and tap Calculate"})
T["tr"]["home"].update({"calc_go": "Hesapla", "calc_pre": "Rakamlarınızı girin, Hesapla'ya basın"})
_EMO = ["🏷️", "🔁", "✍️", "👥", "🛒", "📦"]
for _l in ("en", "tr"):
    for _f in T[_l]["home"]["flows"]:
        if _f["t"] == "more":
            _f["emo"] = _EMO

T["en"]["home"].update({"tl_wk": "Week", "weeks_badge": "8 weeks"})
T["tr"]["home"].update({"tl_wk": "Hafta", "weeks_badge": "8 hafta"})

# --- v13: hero facts, clean method list ---
T["en"]["home"]["facts"] = [("8", "weeks", "a clear finish line"), ("Free", "", "check-up first"), ("Yours", "", "after handover")]
T["tr"]["home"]["facts"] = [("8", "hafta", "net bir bitiş"), ("Ücretsiz", "", "önce check-up"), ("Sizin", "", "devirden sonra")]
for _l, _a, _b in (("tr", "Mağazalar arası stok transferi", "Mağazalar arası transfer"), ("en", "Stock transfers between stores", "Store-to-store transfers")):
    for _f in T[_l]["home"]["flows"]:
        if _f["t"] == "more":
            _f["tags"] = [_b if x == _a else x for x in _f["tags"]]

# --- v15: short button labels ---
T["en"]["home"].update({"cta_s": "Free check-up", "ghost_s": "Estimate your loss", "leak_btn1": "Free check-up", "leak_btn2": "Estimate it"})
T["tr"]["home"].update({"cta_s": "Ücretsiz check-up", "ghost_s": "Kaybı hesapla", "leak_btn1": "Ücretsiz check-up", "leak_btn2": "Hesaplayın"})

# --- v16: one check-up button, one estimator button ---
for _l, _cu, _est, _wk in (("en", "Free check-up", "Estimate your loss", "In just eight weeks."), ("tr", "Ücretsiz check-up", "Kaybı hesapla", "Sadece sekiz haftada.")):
    _h = T[_l]["home"]
    _h.update({"btn_cu": _cu, "btn_est": _est, "lead_weeks": _wk, "calc_cta": _cu, "c_mobile": (_cu, "WhatsApp")})
    _h["cards"] = [(k, t, d, _cu if i == 0 else b) for i, (k, t, d, b) in enumerate(_h["cards"])]
    for _f in _h["flows"]:
        if _f["t"] == "more":
            _f["tags"] = _f["tags"] + (["Demand forecasting", "Abandoned-cart flows"] if _l == "en" else ["Talep tahmini", "Sepet terk akışları"])

T["en"]["home"]["btn_est"] = "Loss estimator"
T["tr"]["home"]["btn_est"] = "Zarar hesaplayıcı"

# --- v19 ---
T["en"]["nav"]["cta_s"] = "Check-up"
T["tr"]["nav"]["cta_s"] = "Check-up"
T["en"]["home"].update({"how_h": "Eight weeks, a clear finish line.", "c_h": "See where you stand first."})
T["tr"]["home"].update({"how_h": "Sekiz hafta, net bir bitiş.", "c_h": "Önce nerede durduğunuzu görün."})
T["en"]["cu"].update({"next_h": "What happens next", "next": ["We reply within one business day.", "A 30-minute call on your numbers.", "A one-page assessment, with an honest view."], "est_try": "Meanwhile, try the loss estimator", "est_btn": "Loss estimator"})
T["tr"]["cu"].update({"next_h": "Sonraki adımlar", "next": ["Bir iş günü içinde dönüş yaparız.", "Rakamlarınız üzerine 30 dakikalık görüşme.", "Dürüst bir görüşle tek sayfalık değerlendirme."], "est_try": "Bu arada zarar hesaplayıcıyı deneyin", "est_btn": "Zarar hesaplayıcı"})

T["en"]["cu"].update({"a_k": "Check-up scope", "a_p": "Five areas, one short conversation. We only ask for summary figures."})
T["tr"]["cu"].update({"a_k": "Check-up kapsamı", "a_p": "Beş alan, tek kısa görüşme. Sadece özet rakamlar istiyoruz."})

# --- v21: short card names on top; one-line text under the visual ---
_FN = {
    "tr": {"stock": "Stok koruma", "alert": "Anlık alarm", "report": "Haftalık kâr raporu", "camp": "Kampanya kontrolü",
           "carrier": "Kargo seçimi", "returns": "İade analizi", "reply": "Müşteri yanıtları", "more": "Diğer alanlar"},
    "en": {"stock": "Stock guard", "alert": "Instant alerts", "report": "Weekly profit report", "camp": "Campaign check",
           "carrier": "Carrier selection", "returns": "Returns analysis", "reply": "Customer replies", "more": "Other areas"},
}
for _l in ("en", "tr"):
    for _f in T[_l]["home"]["flows"]:
        _f["n"] = _FN[_l][_f["t"]]

# --- v22: related ideas under each card ---
_ALT = {
    "tr": {"stock": ["Fiyat, rakip fiyatına göre güncellenir", "Tükenen ürün yerine benzeri öne çıkar", "Tedarikçiye otomatik sipariş taslağı"],
           "alert": ["Pazar yeri puanı düşünce uyarı", "Ödeme hatası artınca uyarı", "Kargo gecikmesi büyüyünce uyarı"],
           "report": ["Günlük nakit ve tahsilat özeti", "Pazar yeri komisyon kontrolü", "Yönetime aylık kâr sunumu"],
           "camp": ["İndirim öncesi kâr simülasyonu", "Kupon kötüye kullanımı tespiti", "Kârsız reklam kelimelerinin ayıklanması"],
           "carrier": ["Kargo faturası kontrolü", "Hatalı desi tespiti", "Teslimat sözü sayfada gösterilir"],
           "returns": ["Ürün sayfası metni yeniden yazılır", "Beden önerisi", "Yorumlardan ürün fikri çıkarılır"],
           "reply": ["Pazar yeri sorularına yanıt taslağı", "Yorum yanıtları", "Toptan teklif taslakları"]},
    "en": {"stock": ["Prices follow competitor prices", "A similar product steps in when one sells out", "Draft purchase orders to suppliers"],
           "alert": ["Alert when marketplace rating drops", "Alert when payment errors rise", "Alert when delivery delays grow"],
           "report": ["Daily cash and collections summary", "Marketplace commission checks", "Monthly profit pack for management"],
           "camp": ["Profit simulation before a discount", "Coupon abuse detection", "Cutting unprofitable ad keywords"],
           "carrier": ["Carrier invoice checks", "Wrong parcel size detection", "Delivery promise shown on the page"],
           "returns": ["Product page copy rewritten", "Size recommendations", "Product ideas from reviews"],
           "reply": ["Draft replies to marketplace questions", "Review replies", "Wholesale quote drafts"]},
}
for _l in ("en", "tr"):
    T[_l]["home"]["fl_alt"] = "Benzer örnekler" if _l == "tr" else "Similar ideas"
    for _f in T[_l]["home"]["flows"]:
        _f["alt"] = _ALT[_l].get(_f["t"], [])

# --- v23: short FAQ on home ---
T["tr"]["home"].update({"sss_k": "SSS", "sss_h": "Kısa cevaplar.", "sss_more": "Daha fazlası için", "sss_more_l": "Kaynaklar", "sss": [
    ("Check-up gerçekten ücretsiz mi?", "Evet. Ücret ve yükümlülük yok. Bir proje sizin için ekonomik olarak anlamlı değilse bunu açıkça söyleriz."),
    ("Proje ne kadar sürer, ücret nasıl belirlenir?", "Proje sekiz hafta sürer. Ücret check-up'tan sonra kapsama göre belirlenir ve işe başlamadan önce yazılı olarak netleşir."),
    ("Hangi verileri paylaşmamız gerekiyor?", "Check-up için son üç ayın özet rakamları yeter; sistem erişimi gerekmez. İsterseniz veri paylaşımından önce gizlilik sözleşmesi (NDA) imzalarız."),
    ("Yeni yazılım almamız gerekiyor mu?", "Gerekmeyebilir. Yazılım satmıyoruz; önce mevcut araçlarınızla çalışırız. Yeni bir araç gerekirse sorununuza göre birlikte seçer, maliyetini önceden gösteririz."),
    ("Proje bitince ne oluyor?", "Kurulan sistem, nasıl kullanılacağı ve ekip eğitimiyle birlikte size devredilir; sistem sizin olur. Devirden sonraki ilk ay sonuçları birlikte izleriz; daha uzun destek isterseniz ayrıca planlarız."),
]})
T["en"]["home"].update({"sss_k": "FAQ", "sss_h": "Short answers.", "sss_more": "", "sss_more_l": "", "sss": [
    ("Is the check-up really free?", "Yes. No fee and no obligation. If a project doesn't make economic sense for you, we say so plainly."),
    ("How long is a project, and how is the fee set?", "A project runs for eight weeks. The fee is set after the check-up, based on scope, and agreed in writing before work starts."),
    ("What data do we need to share?", "For the check-up, summary figures for the last three months are enough; no system access needed. We can sign an NDA before you share any data."),
    ("Do we need to buy new software?", "Probably not. We don't sell software; we start with the tools you already use. If a new tool is needed, we choose it together for your problem and show the cost up front."),
    ("What happens when the project ends?", "The system we built is handed to your team with documentation and training; it is yours. We track the results with you for the first month after handover; longer support can be planned separately."),
]})
T["tr"]["footer"]["kb"] = "Kaynaklar"

# --- v24: downloadable NDA on check-up ---
T["tr"]["cu"]["nda"] = ("Veri paylaşmadan önce gizlilik sözleşmesi imzalayabiliriz: ", "standart NDA'mızı indirin", ", imzalayıp hakan.aydin@aitradeai.net adresine gönderin.", "nda-tr.pdf")
T["en"]["cu"]["nda"] = ("We can sign an NDA before you share any data: ", "download our standard NDA", ", sign it and send it to hakan.aydin@aitradeai.net.", "nda-en.pdf")

# --- v25: hero fit line, softer email rule ---
T["tr"]["home"]["fit"] = "Aylık 1.000+ siparişli e-ticaret ekipleri için · Ücretsiz · Taahhüt yok"
T["en"]["home"]["fit"] = "For e-commerce teams with 1,000+ orders a month · Free · No commitment"
T["tr"]["cu"]["e_email"] = "Lütfen geçerli bir e-posta adresi yazın"
T["en"]["cu"]["e_email"] = "Please enter a valid email address"

# --- v26: fit line without threshold; calculator in nav ---
T["tr"]["home"]["fit"] = "Büyüyen e-ticaret ekipleri için · Ücretsiz · Taahhüt yok"
T["en"]["home"]["fit"] = "For growing e-commerce teams · Free · No commitment"
T["tr"]["nav"]["calc"] = "Zarar hesaplayıcı"
T["en"]["nav"]["calc"] = "Loss estimator"
