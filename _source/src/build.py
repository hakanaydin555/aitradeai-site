# -*- coding: utf-8 -*-
"""Builds the static site into ../dist. Run: python3 build.py"""
import os, shutil, html, urllib.parse, json, datetime
import kaynaklar as KB
from content import T, SITE, CAL, WA_NUMBER, LINKEDIN, LINKEDIN_CO, EMAIL, GSC_VERIFY, BING_VERIFY, CF_BEACON

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "dist")

PAGES = {  # key: (en path, tr path, canonical en, canonical tr)
    "home": ("index.html", "tr/index.html", "/", "/tr/"),
    "cu": ("check-up.html", "tr/check-up.html", "/check-up", "/tr/check-up"),
    "privacy": ("privacy.html", "tr/privacy.html", "/privacy", "/tr/privacy"),
}

e = html.escape
CHECK = '<svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10.5l4 4 8-9" fill="none" stroke="#F59E0B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
WA_ICON = '<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1.1 2.7.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3z"/></svg>'
CHAT = '<svg width="18" height="18" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 15.5l-1 3 3.4-1.6A8 8 0 1 0 4 15.5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'


def wa(lang):
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, urllib.parse.quote(T[lang]["wa_text"]))


def rel(lang, target_lang, key):
    """Relative link from a page in `lang` to page `key` in `target_lang`."""
    # Clean URLs (match canonicals) so Google doesn't crawl *.html duplicates.
    path = PAGES[key][2 if target_lang == "en" else 3].lstrip("/")
    prefix = "../" if lang == "tr" else ""
    return (prefix + path) or "./"


ORG_ID = SITE + "/#org"


def schema(lang, key, page, canon):
    """JSON-LD structured data. Only states what the visible page also says."""
    org = {
        "@type": "Organization", "@id": ORG_ID, "name": "AI Trade", "url": SITE + "/",
        "email": EMAIL, "description": T["en"]["home"]["desc"],
        "address": {"@type": "PostalAddress", "addressLocality": "Istanbul", "addressCountry": "TR"},
        "areaServed": [{"@type": "Country", "name": "Türkiye"}, "MENA", "CIS"],
        "knowsAbout": ["E-commerce profitability", "Marketplace operations", "Performance marketing", "CRM",
                       "Demand forecasting", "Pricing and promotions", "AI automation", "Cross-border e-commerce"],
        "founder": {"@type": "Person", "name": "Hakan Aydın", "sameAs": [LINKEDIN]},
        "sameAs": [LINKEDIN_CO],
    }
    site = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "AI Trade",
            "inLanguage": ["en", "tr"], "publisher": {"@id": ORG_ID}}
    webpage = {"@type": "WebPage", "@id": canon + "#page", "url": canon, "name": page["title"],
               "description": page["desc"], "inLanguage": lang, "isPartOf": {"@id": SITE + "/#website"},
               "about": {"@id": ORG_ID}}
    graph = [org, site, webpage]
    if key == "home":
        graph.append({"@type": "FAQPage", "@id": canon + "#faq", "inLanguage": lang, "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in T[lang]["home"]["sss"]]})
    if key == "cu":
        c = T[lang]["cu"]
        graph.append({"@type": "Service", "@id": canon + "#service", "name": c["h1"], "description": page["desc"],
                      "serviceType": "E-commerce profitability check-up", "provider": {"@id": ORG_ID},
                      "areaServed": "TR", "url": canon,
                      "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "url": canon}})
        graph.append({"@type": "FAQPage", "@id": canon + "#faq", "inLanguage": lang, "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]})
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    return '<script type="application/ld+json">' + data.replace("</", "<\\/") + "</script>"


def verify_tags():
    out = ""
    if GSC_VERIFY:
        out += '<meta name="google-site-verification" content="%s">\n' % e(GSC_VERIFY)
    if BING_VERIFY:
        out += '<meta name="msvalidate.01" content="%s">\n' % e(BING_VERIFY)
    if CF_BEACON:
        out += ('<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" '
                'data-cf-beacon=\'{"token": "%s"}\'></script>\n' % e(CF_BEACON))
    return out


def head(lang, key, page):
    en_c, tr_c = SITE + PAGES[key][2], SITE + PAGES[key][3]
    canon = en_c if lang == "en" else tr_c
    prefix = "../" if lang == "tr" else ""
    og = SITE + "/assets/og-%s.png" % lang
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(page['title'])}</title>
<meta name="description" content="{e(page['desc'])}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{en_c}">
<link rel="alternate" hreflang="tr" href="{tr_c}">
<link rel="alternate" hreflang="x-default" href="{en_c}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AI Trade">
<meta property="og:title" content="{e(page['title'])}">
<meta property="og:description" content="{e(page['desc'])}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(page['title'])}">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'tr_TR'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(page['title'])}">
<meta name="twitter:description" content="{e(page['desc'])}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
{verify_tags()}{schema(lang, key, page, canon)}
<meta name="theme-color" content="#0E1A2B">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{prefix}assets/libre-franklin.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="{prefix}assets/source-sans-3.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="{prefix}assets/style.css">
<script src="{prefix}assets/config.js"></script>
<script src="{prefix}assets/main.js" defer></script>
</head>
<body class="hero-light">
"""


def header(lang, key, on_home):
    n = T[lang]["nav"]
    home = "" if on_home else rel(lang, lang, "home")
    other = "tr" if lang == "en" else "en"
    l_en = rel(lang, "en", key)
    l_tr = rel(lang, "tr", key)
    return f"""<header class="site-header">
<div class="wrap">
<a class="brand" href="{rel(lang, lang, 'home')}" aria-label="AI Trade"><span class="brand-a">A</span>I Trade</a>
<nav class="nav" aria-label="Main">
<a class="navlink" href="{home}#how">{n['how']}</a>
<a class="navlink" href="{home}#work">{n['results']}</a>
<a class="navlink" href="{home}#about">{n['about']}</a>
<a class="navlink" href="{home}#contact">{n['contact']}</a>
<div class="lang" role="group" aria-label="{n['lang_label']}">
<a href="{l_en}" hreflang="en" lang="en" data-setlang="en" aria-current="{'true' if lang == 'en' else 'false'}">EN</a>
<a href="{l_tr}" hreflang="tr" lang="tr" data-setlang="tr" aria-current="{'true' if lang == 'tr' else 'false'}">TR</a>
</div>
<a class="btn btn-amber" href="{rel(lang, lang, 'cu')}"><span class="lg">{n['cta']}</span><span class="sm">{n['cta_s']}</span></a>
<button class="menu-btn" type="button" aria-label="{n['menu']}" aria-expanded="false"><svg width="22" height="22" viewBox="0 0 22 22" aria-hidden="true"><path d="M3 7h16M3 15h16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>
</nav>
</div>
</header>
"""


def footer(lang, on_home):
    f = T[lang]["footer"]
    home = "" if on_home else rel(lang, lang, "home")
    return f"""<footer class="site-footer">
<div class="wrap">
<p>{f['copy']}</p>
<nav aria-label="Footer">
<a href="{home}#contact">{f['contact']}</a>
<a href="{rel(lang, lang, 'privacy')}">{f['privacy']}</a>
{'<a href="%skaynaklar/">%s</a>' % ("" if on_home else "../tr/", f['kb']) if lang == "tr" else ""}
<a href="{LINKEDIN_CO}" target="_blank" rel="noopener">{f['li']}</a>
</nav>
</div>
</footer>
<a class="fab" href="{e(wa(lang))}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_ICON}</a>
</body>
</html>
"""



LEAK_ICONS = [
    '<svg viewBox="0 0 24 24"><path d="M4 10v4h3l6 4V6L7 10H4z M16.5 9a4 4 0 0 1 0 6 M19 6.5a7.5 7.5 0 0 1 0 11" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>',
    '<svg viewBox="0 0 24 24"><path d="M3 4h2.5l2.2 10.5h10.6L20.5 7H7 M9 19.5a1 1 0 1 0 0 .01 M17 19.5a1 1 0 1 0 0 .01" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>',
    '<svg viewBox="0 0 24 24"><path d="M4 7.5 12 4l8 3.5v9L12 20l-8-3.5z M4 7.5 12 11l8-3.5 M12 11v9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
    '<svg viewBox="0 0 24 24"><path d="M9 7H5V3 M5.5 7A8 8 0 1 1 4 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>',
    '<svg viewBox="0 0 24 24"><path d="M12 7v5l3 2 M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>',
]


def home(lang):
    h = T[lang]["home"]
    out = [head(lang, "home", h), '<div class="dark">', header(lang, "home", True)]
    out.append(f"""<section class="hero" id="top">
<div class="wrap">
<div class="hero-copy">
<p class="eyebrow">{h['eyebrow']}</p>
<h1 class="rise">{h['h1']}</h1>
<p class="lead rise d2">{e(h['lead'])} <span class="wk">{e(h['lead_weeks'])}</span></p>
<div class="hero-ctas rise d3">
<a class="btn btn-amber" href="{rel(lang, lang, 'cu')}">{e(h['btn_cu'])}</a>
<a class="btn btn-est" href="#estimate">{e(h['btn_est'])}</a>
</div>
</div>
{feed_panel(h)}
</div>
</section>
""")
    out.append('</div>\n<main>\n')

    nodes = "".join(f'<li class="node n{i+1}"><span class="dot" aria-hidden="true">{LEAK_ICONS[i]}</span><span class="txt"><span class="nt">{e(a)}</span><span class="nl">{e(b)}</span><span class="nf">{e(c)}</span></span></li>' for i, (a, b, c) in enumerate(h["nodes"]))
    out.append(f"""<section class="section grey" id="leaks">
<div class="wrap">
<div class="sec-head reveal"><p class="ex-k">{e(h['leak_k'])}</p><h2>{e(h['leak_h'])}</h2><p>{e(h['leak_p'])}</p></div>
<div class="leakmap">
<div class="leakline" aria-hidden="true"></div>
<ol class="nodes">{nodes}</ol>
</div>
<div class="leak-cta2"><p>{e(h['leak_q'])}</p><div class="btn-row"><a class="btn btn-amber" href="{rel(lang, lang, 'cu')}">{e(h['btn_cu'])}</a><a class="btn btn-est" href="#estimate">{e(h['btn_est'])}</a></div></div>
</div>
</section>
""")
    plan = "".join(f'<div class="prow"><p class="w">{e(w)}</p><p class="t">{e(t)}</p><p class="d">{e(d)}</p></div>' for w, t, d in h["plan"])
    how_html = (f"""<section class="section" id="how">
<div class="wrap">
<div class="sec-head reveal"><p class="ex-k">{e(h['how_k'])}</p><h2>{e(h['how_h'])}</h2><p>{e(h['how_p'])}</p></div>
{steps(h)}
<ul class="how-pts reveal">{"".join(f"<li>{e(x)}</li>" for x in h['how_pts'])}</ul>
</div>
</section>
""")
    out.append(how_html)
    out.append(flows_section(h))
    metrics = "".join(f'<div><p class="k">{e(k)}</p><p class="v">{e(v)}</p></div>' for k, v in h["metrics"])
    cases = "".join(f'<div class="case"><p class="big"><span data-count="{n}" data-suffix="{s}">{n}{s}</span></p><p class="what">{e(w)}</p><p class="ctx">{e(c)}</p></div>' for n, s, w, c in h["cases"])
    cards = []
    for i, w in enumerate(h["work"]):
        stats = "".join(f'<div><p class="wn">{e(n)}</p><p class="wl">{e(l)}</p></div>' for n, l in w["res"])
        tags = "".join(f"<span>{e(t)}</span>" for t in w["tags"])
        cards.append(f'''<article class="work-card wc2" aria-label="{e(h['case_l'])} {i + 1}">
<p class="ex-k">{e(w['k'])}</p>
<div class="wstats">{stats}</div>
<h3>{e(w['h'])}</h3>
<p class="wt wdid">{e(h['did_l'])}</p><p class="wtags">{tags}</p>
<details class="wmore"><summary>{e(h['more_l'])}</summary><p class="wtags wtags-m">{tags}</p><p>{e(w['ctx'])}</p><p>{e(w['brief'])}</p><p>{e(w['built'])}</p></details>
</article>''')
    dots = "".join(f'<button type="button" aria-label="{e(h["case_l"])} {i + 1}"{" aria-current=\"true\"" if i == 0 else ""}></button>' for i in range(len(h["work"])))
    out.append(f"""<section class="section dark results" id="work">
<div class="wrap">
<div class="sec-head reveal"><p class="ex-k">{e(h['w_k'])}</p><h2>{e(h['w_h'])}</h2><p>{e(h['w_p'])}</p></div>
<div class="work-grid stagger">{"".join(cards)}</div>
<div class="btn-row two more-cta"><a class="btn btn-amber" href="{rel(lang, lang, 'cu')}">{e(h['btn_cu'])}</a><a class="btn btn-est" href="#estimate">{e(h['btn_est'])}</a></div>
</div>
</section>
""")
    out.append(calc_section(lang, h))
    c = h["cards"]
    links = [rel(lang, lang, "cu"), wa(lang)]
    cls = ["btn btn-amber", "btn btn-wa"]
    ext = ["", 'target="_blank" rel="noopener"']
    cards = "".join(f'<div class="ccard"><p class="k">{e(k)}</p><h3>{e(t)}</h3><p>{e(d)}</p><a class="{cls[i]}" href="{e(links[i])}" {ext[i]}>{WA_ICON if i else ""}{e(b)}</a></div>' for i, (k, t, d, b) in enumerate(c))
    m = h["c_mobile"]
    out.append(f"""<section class="section" id="contact">
<div class="wrap">
<div class="sec-head reveal"><p class="ex-k">{e(h['c_k'])}</p><h2>{e(h['c_h'])}</h2><p>{e(h['c_p'])}</p></div>
<div class="cbox">
<div class="btn-row two"><a class="btn btn-amber" href="{rel(lang, lang, 'cu')}">{e(h['btn_cu'])}</a><a class="btn btn-est" href="#estimate">{e(h['btn_est'])}</a></div>
{team_block(lang, h)}
</div>
</div>
</section>
{sss_section(lang, h)}
</main>
""")
    out.append(footer(lang, True))
    return "".join(out)




ICONS = {
    "rep": '<svg viewBox="0 0 20 20"><path d="M4 16V9M10 16V5M16 16v-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/></svg>',
    "ad": '<svg viewBox="0 0 20 20"><rect x="6" y="5" width="2.6" height="10" rx="1" fill="currentColor"/><rect x="11.4" y="5" width="2.6" height="10" rx="1" fill="currentColor"/></svg>',
    "ship": '<svg viewBox="0 0 20 20"><path d="M3 6.5 10 3l7 3.5v7L10 17l-7-3.5z M3 6.5 10 10l7-3.5 M10 10v7" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    "camp": '<svg viewBox="0 0 20 20"><path d="M10 4v7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><circle cx="10" cy="15" r="1.4" fill="currentColor"/></svg>',
}


def feed_panel(h):
    items = "".join(f'<li class="fd fd-{k}" style="--i:{i}"><span class="fd-ic">{ICONS[k]}</span><span class="fd-tx"><b>{e(t)}</b><small>{e(d)}</small></span><time>{e(tm)}</time></li>' for i, (k, tm, t, d) in enumerate(h["feed"]))
    return f"""<div class="panel anim feedp">
<div class="panel-head"><div><p class="panel-kicker">{e(h['feed_k'])}</p><p class="panel-title">{e(h['feed_h'])}</p></div>{f'<span class="tag">{e(h["feed_tag"])}</span>' if h['feed_tag'] else ''}</div>
<ul class="feed" aria-label="{e(h['feed_h'])}">{items}</ul>
</div>"""



def who_card(lang, h):
    tags = "".join(f"<span>{e(x)}</span>" for x in h["t_tags"])
    return f"""<div class="who reveal">
<div class="who-top"><img src="{'../' if lang == 'tr' else ''}assets/hakan.jpg" width="64" height="64" alt="{e(h['t_name'])}" loading="lazy">
<div><p class="who-k">{e(h['who_k'])}</p><p class="who-n">{e(h['t_name'])} <a class="li-ic" href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn: {e(h['t_name'])}">in</a></p><p class="who-r">{e(h['t_role'])}</p></div></div>
<p class="who-t">{tags}</p>
<div class="who-f"><span class="who-g">{e(h['t_regions'])}</span><span class="who-l"><a href="{LINKEDIN_CO}" target="_blank" rel="noopener">{e(h['li_co'])}</a></span></div>
</div>"""



def team_block(lang, h):
    tick = '<svg viewBox="0 0 20 20"><path d="M5 10.5l3.2 3.2L15 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    pr = "".join(f'<li><i>{tick}</i><span><b>{e(t)}</b> {e(d)}</span></li>' for t, d in h["t_pr"])
    return f"""<div class="teamc" id="about">
<p class="team-k">{e(h['t_h'])}</p>
<ul class="tlist">{pr}</ul>
<a class="btn btn-wa cwa" href="{e(wa(lang))}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a>
{who_card(lang, h)}
</div>"""


def team_section(lang, h):
    tick = '<svg viewBox="0 0 20 20"><path d="M5 10.5l3.2 3.2L15 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    pr = "".join(f'<div class="tp"><i>{tick}</i><div><b>{e(t)}</b><span>{e(d)}</span></div></div>' for t, d in h["t_pr"])
    return f"""<section class="section" id="about">
<div class="wrap">
<div class="sec-head reveal"><p class="ex-k">{e(h['t_k'])}</p><h2>{e(h['t_h'])}</h2><p>{e(h['t_p'])}</p></div>
<div class="team1 stagger">{pr}</div>
</div>
</section>
"""



PHASE_COLORS = ["#0E1A2B", "#FCD9A0", "#F8BC5E", "#F59E0B", "#B45309"]
PHASE_WEEKS = [None, (1, 2), (3, 4), (5, 7), (8, 8)]


def timeline(h):
    plan = h["plan"]
    cells = []
    for wk in range(1, 9):
        ph = next(i for i in range(1, 5) if PHASE_WEEKS[i][0] <= wk <= PHASE_WEEKS[i][1])
        cells.append(f'<span class="tl-c" style="--c:{PHASE_COLORS[ph]};--d:{(wk - 1) * .12:.2f}s"><b>{wk}</b></span>')
    rows = "".join(f'<li style="--c:{PHASE_COLORS[i]}"><span class="tl-sw"></span><div><p class="tl-t">{e(t)} <span>{e(w)}</span></p><p class="tl-d">{e(d)}</p></div></li>' for i, (w, t, d) in enumerate(plan))
    return f"""<div class="tl reveal">
<div class="tl-top"><span class="tl-pre" style="--c:{PHASE_COLORS[0]}">{e(plan[0][1])}</span><span class="tl-arr" aria-hidden="true"></span><div class="tl-bar" aria-hidden="true">{''.join(cells)}</div></div>
<ol class="tl-list">{rows}</ol>
</div>"""



def steps(h):
    rows = "".join(f'<li><span class="st-w">{e(w)}</span><div><p class="st-t">{e(t)}</p><p class="st-d">{e(d)}</p></div></li>' for w, t, d in h["plan"])
    return f'<ol class="steps2 stagger">{rows}</ol>'


def calc_section(lang, h):
    curs = ["$", "€", "£", "₺"] if lang == "en" else ["₺", "$", "€"]
    opts = "".join(f'<label><input type="radio" name="cur" value="{c}"{" checked" if c == h["calc_cur_default"] else ""}><span>{c}</span></label>' for c in curs)
    RNG = {"disc": (0, 80, 1), "ret": (0, 40, 0.5), "logi": (0, 30, 0.5), "hrs": (0, 200, 5)}
    money, sliders = [], []
    for key, label, val, kind, hint in h["calc_f"]:
        if kind == "money":
            money.append(f'<label class="cx-field"><span class="cx-l">{e(label)}</span><span class="cx-in"><span class="cx-pre" data-cur>{e(h["calc_cur_default"])}</span><input type="text" inputmode="numeric" name="{key}" value="{e(val)}" data-kind="money" autocomplete="off"></span></label>')
        else:
            lo, hi, st = RNG[key]
            unit = "%" if kind == "pct" else ""
            ttl = f' title="{e(hint)}"' if hint else ""
            sliders.append(f'<label class="cx-sl"{ttl}><span class="cx-slh"><span class="cx-l">{e(label)}</span><b>{unit if lang == "tr" else ""}<span data-val="{key}">{e(val)}</span>{unit if lang != "tr" else ""}</b></span><input type="range" name="{key}" min="{lo}" max="{hi}" step="{st}" value="{e(val)}" data-kind="{kind}"></label>')
    fields = ['<div class="cx-money">' + "".join(money) + '</div>'] + sliders
    cols = ["#F59E0B", "#F6B97A", "#8FA0B5", "#4B5B70"]
    bar = "".join(f'<i data-seg="{k}" style="background:{cols[i]}"></i>' for i, (k, t) in enumerate(h["calc_lines"]))
    leg = "".join(f'<div><span><em style="background:{cols[i]}"></em>{e(t)}</span><b data-out="{k}">–</b></div>' for i, (k, t) in enumerate(h["calc_lines"]))
    method = "".join("<li>" + e(m).replace("&lt;range&gt;", '<span data-out="range">–</span>') + "</li>" for m in h["calc_method"])
    return f"""<section class="section grey" id="estimate">
<div class="wrap">
<div class="sec-head reveal"><p class="ex-k">{e(h['calc_k'])}</p><h2>{e(h['calc_h'])}</h2><p>{e(h['calc_p'])}</p></div>
<div class="calc reveal" data-calc data-lang="{lang}" data-cu="{rel(lang, lang, 'cu')}" data-fte="{h['calc_fte_hours']}" data-t-days="{e(h['calc_days'])}" data-t-fte="{e(h['calc_fte'])}" data-t-hours="{e(h['calc_hours'])}">
<div class="cx-inputs">
<div class="cx-cur2"><span class="cx-l">{e(h['calc_cur'])}</span><span class="cx-seg">{opts}</span></div>
{''.join(fields)}
<button type="button" class="btn btn-est cx-go">{e(h['calc_go'])}</button>
</div>
<div class="cx-out pre" aria-live="polite">
<p class="cx-preh">{e(h['calc_pre'])}</p>
<p class="cx-k">{e(h['calc_total'])}</p>
<p class="cx-total" data-out="total">–</p>
<div class="cx-bar" aria-hidden="true">{bar}</div>
<div class="cx-leg">{leg}</div>
<p class="cx-plus">{e(h['calc_plus'])}</p>
<p class="cx-tv"><span data-out="time">–</span> <span class="u">{e(h['calc_week'])}</span></p>
<p class="cx-eq">{e(h['calc_back'])} · <span data-out="eq">–</span></p>
<a class="btn btn-amber cx-cta" href="{rel(lang, lang, 'cu')}">{e(h['calc_cta'])}</a>
</div>
</div>
<details class="cx-how"><summary>{e(h['calc_how'])}</summary><ul>{method}</ul></details>
</div>
</section>
"""


_I = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{}</svg>'
MORE_ICONS = [_I.format(p) for p in [
    '<path d="M3 12V4h8l10 10-8 8L3 12z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    '<path d="M7 7h12l-3-3M17 17H5l3 3"/>',
    '<path d="M4 20h4L19 9l-4-4L4 16v4zM13.5 6.5l4 4"/>',
    '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5.5a3 3 0 0 1 0 5.5M18 14.5c2 .8 3 2.7 3 5.5"/>',
    '<rect x="5" y="3.5" width="14" height="17" rx="2"/><path d="M9 3.5h6v3H9zM9 13l2 2 4-4"/>',
    '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7M7 19a2 2 0 1 0 0-.01M17 19a2 2 0 1 0 0-.01"/>',
    '<path d="M3 20h18M5 16l4-5 4 3 6-8"/>',
    '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
]]


def flow_viz(f):
    t = f["t"]
    if t == "stock":
        return f"""<div class="fviz fv1">
<div class="fv-row"><span class="fv-name">{e(f['prod'])}</span><span class="fv-swap"><b class="a">{e(f['stock'])}: {e(f['d1'])}</b><b class="b bad">{e(f['stock'])}: {e(f['d2'])}</b></span></div>
<div class="fv-row"><span class="fv-name">{e(f['ad'])}</span><span class="fv-tg"><i></i></span><span class="fv-swap r"><b class="a ok">{e(f['on'])}</b><b class="b">{e(f['off'])}</b></span></div>
<div class="fv-toast">{e(f['toast'])}</div></div>"""
    if t == "alert":
        return f"""<div class="fviz fv-al">
<span class="fv-clock">{e(f['chip'])}</span>
<svg viewBox="0 0 300 70" class="fv-line"><polyline class="ok" pathLength="1" points="0,30 30,26 60,32 90,24 120,28 150,22 180,26 210,24" /><polyline class="drop" pathLength="1" points="210,24 240,46 270,58 300,60" /></svg>
<div class="fv-alarm"><b>{e(f['alert'])}</b><small>{e(f['alert2'])}</small></div></div>"""
    if t == "report":
        bars = "".join(f'<i style="--h:{v}%;--d:{i * .08:.2f}s"></i>' for i, v in enumerate([38, 52, 46, 70, 64, 86]))
        return f"""<div class="fviz fv2">
<span class="fv-clock">{e(f['clock'])}</span>
<div class="fv-mail"><span class="fv-ic"></span><span><b>{e(f['mail'])}</b><small>{e(f['mail2'])}</small></span></div>
<div class="fv-bars">{bars}</div></div>"""
    if t == "camp":
        rows = "".join(f'<div class="fv-tr{" hit" if i == 1 else ""}"><span>{e(a)}</span><span>{e(b)}</span><b>{e(c)}</b></div>' for i, (a, b, c) in enumerate(f["rows"]))
        return f'<div class="fviz fv3">{rows}<div class="fv-fix">{e(f["fix"])}</div></div>'
    if t == "carrier":
        rows = "".join(f'<div class="fv-tr fv-cr{" pick" if i == 1 else ""}{" slow" if i == 2 else ""}"><span>{e(a)}</span><span>{e(c)}</span><b>{e(b)}</b><em>{e(f["pick"])}</em></div>' for i, (a, b, c) in enumerate(f["rows"]))
        return f'<div class="fviz fv-ca"><span class="fv-clock">{e(f["order"])}</span>{rows}</div>'
    if t == "returns":
        rows = "".join(f'<div class="fv-rr"><span>{e(a)}</span><span class="fv-rb"><i style="--w:{v * 2}%;--d:{i * .12:.2f}s"></i></span><b>{("%" + str(v)) if f.get("pct_first") else (str(v) + "%")}</b></div>' for i, (a, v) in enumerate(f["rows"]))
        return f'<div class="fviz fv-re">{rows}<div class="fv-fix">{e(f["fix"])}</div></div>'
    if t == "reply":
        return f"""<div class="fviz fv-rp">
<div class="fv-q">{e(f['q'])}</div>
<div class="fv-a"><span class="fv-dots"><i></i><i></i><i></i></span><span class="fv-at">{e(f['a'])}</span></div>
<div class="fv-ok">{e(f['btn'])}</div></div>"""
    tags = "".join(f'<span><i>{MORE_ICONS[k]}</i>{e(x)}</span>' for k, x in enumerate(f["tags"]))
    return f'<div class="fviz fv-mo"><div class="fv-emo">{tags}</div></div>'


def flows_section(h):
    def card(f):
        if f["t"] == "more":
            items = "".join(f'<li><i>{MORE_ICONS[k]}</i>{e(x)}</li>' for k, x in enumerate(f["tags"]))
            return f'<article class="flow flow-more flow-top"><h3>{e(f["n"])}</h3><ul class="more-list">{items}</ul></article>'
        return f'<article class="flow flow-top"><h3>{e(f["n"])}</h3><div class="fviz-wrap" aria-hidden="true">{flow_viz(f)}</div><p class="fl-line">{e(f["h"])}.</p><div class="fl-alt"><ul>{"".join(f"<li>{e(x)}</li>" for x in f["alt"])}</ul></div></article>'
    cards = "".join(card(f) for f in h["flows"])
    dots = "".join(f'<button type="button" aria-label="{i + 1}"{" aria-current=\"true\"" if i == 0 else ""}></button>' for i in range(len(h["flows"])))
    return f"""<section class="section grey" id="flows">
<div class="wrap">
<div class="sec-head reveal"><p class="ex-k">{e(h['fl_k'])}</p><h2>{e(h['fl_h'])}</h2><p>{e(h['fl_p'])}</p></div>
<div class="work flows-car" data-carousel>
<p class="swipe" aria-hidden="true">{e(h['swipe'])}</p>
<div class="work-track flows stagger" tabindex="0">{cards}</div>
<div class="work-nav">
<div class="work-dots">{dots}</div>
<div class="work-arrows"><button type="button" class="work-prev" aria-label="{e(h['prev'])}">‹</button><button type="button" class="work-next" aria-label="{e(h['next'])}">›</button></div>
</div>
</div>
</div>
</section>
"""

_A = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{}</svg>'
AREA_ICONS = [_A.format(p) for p in [
    '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    '<path d="M4 10v4h3l6 4V6L7 10H4zM16.5 9a4 4 0 0 1 0 6"/>',
    '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M2 12h3M19 12h3M4.9 19.1 7 17M17 7l2.1-2.1"/>',
    '<path d="M9 7H5V3M5.5 7A8 8 0 1 1 4 12"/>',
    '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 11l2 2 4-4"/>',
]]
NOTE_ICONS = [_A.format('<path d="M4 20h16M7 16V9M12 16V5M17 16v-4"/>'), _A.format('<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>')]


def checkup(lang):
    c = T[lang]["cu"]
    privacy = rel(lang, lang, "privacy")
    out = [head(lang, "cu", c), '<div class="dark">', header(lang, "cu", False)]
    gets = "".join(f"<div>{CHECK}<span>{e(g)}</span></div>" for g in c["gets"])
    qsteps = []
    for i, (key, q, opts, *kind) in enumerate(c["qs"]):
        multi = "multi" in kind
        buttons = "".join(f'<button type="button" class="opt" aria-pressed="false" data-i="{j}">{e(o)}</button>' for j, o in enumerate(opts))
        hint = f'<p class="multi-hint">{e(c["multi_hint"])}</p>' if multi else ""
        nxt = f'<button type="button" class="btn btn-amber multi-next" disabled>{e(c["next_btn"])}</button>' if multi else ""
        qsteps.append(f'<div data-step="{i}" data-key="{key}" data-q="{e(q)}"{" data-multi" if multi else ""}{" hidden" if i else ""}><h2>{e(q)}</h2>{hint}<div class="opts{" multi" if multi else ""}" style="margin-top:18px">{buttons}</div>{nxt}</div>')
    alt = c["alt"].format(cal=CAL, wa=e(wa(lang)))
    founder = c["founder"].format(li=LINKEDIN)
    out.append(f"""<section class="cu">
<div class="wrap">
<div class="cu-copy">
<p class="eyebrow">{e(c['eyebrow'])}</p>
<h1>{e(c['h1'])}</h1>
<p class="lead">{e(c['lead'])}</p>
<p class="fit">{c['fit']}</p>
<div class="gets"><p class="k">{e(c['gets_k'])}</p>{gets}</div>
</div>
<div class="cu-form-col">
<p class="cu-calc">{e(c['calc_in'])}</p>
<form class="formcard" id="checkup" novalidate>
<div class="progress-wrap">
<div class="progress-meta"><span data-steplabel="{e(c['steplabel'])}">{e(c['steplabel'].replace('{n}', '1').replace('{t}', str(len(c['qs']) + 1)))}</span><span>{e(c['time'])}</span></div>
<div class="progress"><span></span></div>
</div>
{''.join(qsteps)}
<div data-step="{len(c['qs'])}" hidden>
<h2>{e(c['c_h'])}</h2>
<div style="display:flex;flex-direction:column;gap:14px;margin-top:16px">
<div class="field"><label for="f-name">{e(c['f_name'])}</label><input id="f-name" name="name" type="text" autocomplete="name" required><span class="err">{e(c['e_name'])}</span></div>
<div class="field"><label for="f-email">{e(c['f_email'])}</label><input id="f-email" name="email" type="email" autocomplete="email" required><span class="err">{e(c['e_email'])}</span></div>
<div class="row2">
<div class="field"><label for="f-company">{e(c['f_company'])}</label><input id="f-company" name="company" type="text" autocomplete="organization" required><span class="err">{e(c['e_company'])}</span></div>
<div class="field"><label for="f-phone">{e(c['f_phone'])}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
</div>
<div class="field"><label for="f-website">{e(c['f_web'])}</label><input id="f-website" name="website" type="text" inputmode="url" autocomplete="url" placeholder="example.com" required><span class="err">{e(c['e_web'])}</span></div>
<div class="field"><label for="f-note">{e(c['f_note'])}</label><textarea id="f-note" name="note" rows="3" placeholder="{e(c['f_note_ph'])}"></textarea></div>
<div style="position:absolute;left:-9999px" aria-hidden="true"><label for="f-web">Website</label><input id="f-web" name="website2" type="text" tabindex="-1" autocomplete="off"></div>
<label class="consent"><input type="checkbox" name="consent"><span>{c['consent'].format(privacy=privacy)}</span></label>
<p class="form-error" role="alert">{e(c['send_err'])}</p>
<button class="btn btn-amber" type="submit" style="width:100%">{e(c['submit'])}</button>
</div>
</div>
<div data-step="{len(c['qs']) + 1}" hidden>
<svg class="done-icon" viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="21" fill="#FFF4E0"/><path d="M13 22.5l6 6 12-13" fill="none" stroke="#B45309" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
<h2 style="margin-top:16px" role="status">{e(c['d_h'])}</h2>
<p style="font-size:16px;color:var(--muted);margin:10px 0 18px">{e(c['d_p'])}</p>
<a class="btn btn-amber" href="{CAL}" target="_blank" rel="noopener" style="width:100%">{e(c['d_btn'])}</a>
<div class="next-steps"><strong>{e(c['next_h'])}</strong><ol>{"".join(f"<li>{e(x)}</li>" for x in c['next'])}</ol></div>
<div class="summary" style="margin-top:18px"><strong>{e(c['d_sum'])}</strong><div class="summary-list"></div></div>
<p class="est-try">{e(c['est_try'])} <a class="btn btn-est" href="{rel(lang, lang, 'home')}#estimate">{e(c['est_btn'])}</a></p>
<button type="button" class="back restart" style="color:var(--amber-text);font-weight:600">{e(c['restart'])}</button>
</div>
<button type="button" class="back" hidden>{e(c['back'])}</button>
</form>
<p class="form-alt">{alt}</p>
<p class="founder"><img src="{'../' if lang == 'tr' else ''}assets/hakan.jpg" width="40" height="40" alt="" loading="lazy">{founder}</p>
</div>
</div>
</section>
</div>
<main>
""")
    areas = "".join(f'<div class="area"><span class="area-ic">{AREA_ICONS[i]}</span><h3>{e(a)}</h3><p>{e(b)}</p></div>' for i, (a, b) in enumerate(c["areas"]))
    nd = c.get("nda")
    pre = "../" if lang == "tr" else ""
    nl = [e(n) for n in c["notes"]]
    if nd:
        nl[1] = f'{e(nd[0])}<a href="{pre}assets/{nd[3]}" download>{e(nd[1])}</a>{e(nd[2])}'
    notes = "".join(f'<p><span class="note-ic">{NOTE_ICONS[i % 2]}</span>{n}</p>' for i, n in enumerate(nl))
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in c["faq"])
    r = c["r"]
    prof = "".join(f'<div><p class="rk">{e(k)}</p><p class="rv">' + (f'<span class="blur" aria-hidden="true">{e(v)}</span><span class="sr-only">{e(r["hidden"])}</span>' if b else e(v)) + '</p></div>' for k, v, b in r["profile"])
    rrows = "".join(f'<tr><td><span class="rn">{i+1}</span>{e(a)}</td><td>{e(b)}</td><td><span class="blur" aria-hidden="true">{e(x)}</span><span class="sr-only">{e(r["hidden"])}</span></td><td><span class="prio p{0 if p in ("High", "Yüksek") else 1}">{e(p)}</span></td></tr>' for i, (a, b, x, p) in enumerate(r["rows"]))
    out.append(f"""<section class="section grey" id="sample">
<div class="wrap">
<div class="sec-head reveal"><p class="ex-k">{e(c['r_k'])}</p><h2>{e(c['r_h'])}</h2><p>{e(c['r_p'])}</p></div>
<article class="report reveal" aria-label="{e(r['title'])}">
<header class="r-head"><div><p class="r-title">{e(r['title'])}</p><p class="r-for">{e(r['for'])}</p></div><span class="tag">{e(r['tag'])}</span></header>
<div class="r-prof">{prof}</div>
<p class="r-sub">{e(r['leaks_h'])}</p>
<div class="r-table"><table><thead><tr>{"".join(f'<th>{e(x)}</th>' for x in r['cols'])}</tr></thead><tbody>{rrows}</tbody></table></div>
<div class="r-foot"><div><p class="r-sub">{e(r['view_h'])}</p><p>{e(r['view'])}</p></div><div><p class="r-sub">{e(r['next_h'])}</p><p>{e(r['next'])}</p></div></div>
</article>
</div>
</section>
""")
    out.append(f"""<section class="section">
<div class="wrap">
<div class="sec-head reveal"><p class="ex-k">{e(c['a_k'])}</p><h2>{e(c['a_h'])}</h2><p>{e(c['a_p'])}</p></div>
<div class="areas2 stagger">{areas}</div>
<div class="notes">{notes}</div>
</div>
</section>
<section class="section grey" id="faq">
<div class="wrap"><div class="faq"><h2>{e(c['faq_h'])}</h2>{faq}</div></div>
</section>
</main>
""")
    out.append(footer(lang, False))
    return "".join(out)


def privacy(lang):
    p = T[lang]["privacy"]
    out = [head(lang, "privacy", p), '<div class="dark">', header(lang, "privacy", False), "</div>\n<main>"]
    body = "".join(f"<h2>{e(h)}</h2><p>{e(t)}</p>" for h, t in p["body"])
    draft = f'<p class="draft">{e(p["draft"])}</p>' if p["draft"] else ""
    out.append(f'<article class="legal">{draft}<h1>{e(p["h1"])}</h1>{body}</article>\n</main>\n')
    out.append(footer(lang, False))
    return "".join(out)


def llms_txt():
    """Plain summary for AI assistants and crawlers (llms.txt convention)."""
    en, tr = T["en"], T["tr"]
    plan = "\n".join("- %s (%s): %s" % (t, w, d) for w, t, d in en["home"]["plan"])
    kb_lines = "\n".join("- [%s](%s/tr/kaynaklar/%s): %s" % (p["h1"], SITE, p["slug"], p["desc"]) for p in KB.PAGES)
    return f"""# AI Trade

> {en['home']['desc']}

AI Trade is an e-commerce profitability and AI automation consultancy based in Istanbul, Türkiye. It works with mid-sized e-commerce companies, brands and manufacturers' e-commerce teams in Türkiye and abroad. Founder: Hakan Aydın ({LINKEDIN}). LinkedIn: {LINKEDIN_CO}

How a project works:
{plan}

Results are measured as contribution profit, cash savings and team hours, not revenue alone.

## Pages
- [Home (English)]({SITE}/): what we do, how it works, anonymised results
- [Free check-up (English)]({SITE}/check-up): short form and call to find profit leaks
- [Ana sayfa (Türkçe)]({SITE}/tr/): {tr['home']['desc']}
- [Ücretsiz check-up (Türkçe)]({SITE}/tr/check-up)
- [Privacy & KVKK]({SITE}/privacy)

## Kaynaklar (Turkish guides)
- [Kaynaklar]({SITE}/tr/kaynaklar/): {KB.INDEX['desc']}
{kb_lines}

## Contact
- Email: {EMAIL}
- Check-up request: {SITE}/check-up
"""



def sss_section(lang, h):
    items = "".join(f'<details class="sss-i"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in h["sss"])
    more = ""
    if h.get("sss_more_l"):
        more = f'<p class="sss-more">{e(h["sss_more"])} <a href="kaynaklar/">{e(h["sss_more_l"])} →</a></p>'
    return f"""<section class="section grey" id="faq">
<div class="wrap sss">
<div class="sec-head reveal"><p class="ex-k">{e(h['sss_k'])}</p><h2>{e(h['sss_h'])}</h2></div>
<div class="sss-list">{items}</div>
{more}
</div>
</section>"""


# ---------- Kaynaklar (TR answer pages) ----------
import re as _re


def _inline(t):
    t = e(t)
    return _re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)


def kb_body(src):
    out, mode, rows = [], None, []

    def flush():
        nonlocal mode, rows
        if mode == "ul":
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in rows) + "</ul>")
        elif mode == "ol":
            out.append("<ol>" + "".join(f"<li>{x}</li>" for x in rows) + "</ol>")
        elif mode == "table":
            hd, *bd = rows
            th = "".join(f"<th>{c}</th>" for c in hd)
            tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in bd)
            out.append(f'<div class="kb-table"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
        mode, rows = None, []

    for line in src.split("\n"):
        line = line.rstrip()
        if not line:
            continue
        kind = "ul" if line.startswith("- ") else "ol" if line.startswith("1. ") else "table" if line.startswith("| ") else None
        if kind != mode:
            flush()
        if kind == "ul":
            mode = "ul"; rows.append(_inline(line[2:]))
        elif kind == "ol":
            mode = "ol"; rows.append(_inline(line[3:]))
        elif kind == "table":
            mode = "table"; rows.append([_inline(c.strip()) for c in line[2:].split("|")])
        elif line.startswith("## "):
            out.append(f"<h2>{_inline(line[3:])}</h2>")
        elif line.startswith("= "):
            out.append(f'<p class="kb-formula">{_inline(line[2:])}</p>')
        elif line.startswith("> "):
            out.append(f'<p class="kb-note">{_inline(line[2:])}</p>')
        else:
            out.append(f"<p>{_inline(line)}</p>")
    flush()
    return "".join(out)


def kb_head(title, desc, canon, graph):
    og = SITE + "/assets/og-tr.png"
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="AI Trade">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="tr_TR">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
{verify_tags()}<script type="application/ld+json">{data}</script>
<meta name="theme-color" content="#0E1A2B">
<link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="../../assets/libre-franklin.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="../../assets/source-sans-3.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="../../assets/style.css">
<script src="../../assets/config.js"></script>
<script src="../../assets/main.js" defer></script>
</head>
<body class="hero-light kb-page">
"""


def _deep(html_):
    """TR header/footer markup is written for /tr/x; kaynak pages sit one level deeper."""
    return html_.replace('href="../', 'href="../../')


def _crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


KB_BASE = SITE + "/tr/kaynaklar/"


def kb_page(p):
    by = {x["slug"]: x for x in KB.PAGES}
    canon = KB_BASE + p["slug"]
    org = {"@type": "Organization", "@id": ORG_ID, "name": "AI Trade", "url": SITE + "/"}
    graph = [
        org,
        {"@type": "Article", "@id": canon + "#article", "headline": p["h1"], "description": p["desc"], "inLanguage": "tr",
         "datePublished": KB.UPDATED, "dateModified": KB.UPDATED, "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID},
         "mainEntityOfPage": canon, "image": SITE + "/assets/og-tr.png"},
        {"@type": "FAQPage", "@id": canon + "#faq", "inLanguage": "tr", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
        _crumbs([("Ana sayfa", SITE + "/tr/"), ("Kaynaklar", KB_BASE), (p["card"], canon)]),
    ]
    faq = "".join(f'<details class="sss-i"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in p["faq"])
    rel_ = "".join(f'<li><a href="{r}">{e(by[r]["card"])}</a><span>{e(by[r]["q"])}</span></li>' for r in p["related"])
    hdr = _deep('<div class="dark">' + header("tr", "home", False) + "</div>")
    body = f"""<main class="kb">
<div class="wrap kb-wrap">
<nav class="kb-crumb" aria-label="Konum"><a href="../">Ana sayfa</a><span>›</span><a href="./">Kaynaklar</a></nav>
<article>
<h1>{e(p['h1'])}</h1>
<p class="kb-meta">Hazırlayan: AI Trade · Son güncelleme: <time datetime="{KB.UPDATED}">{KB.UPDATED_TR}</time></p>
<p class="kb-answer">{_inline(p['answer'])}</p>
{kb_body(p['body'])}
<h2>Sık sorulanlar</h2>
<div class="sss-list">{faq}</div>
</article>
<aside class="kb-cta"><p>{e(p['cta'])}</p><a class="btn btn-amber" href="../check-up">Ücretsiz check-up</a></aside>
<section class="kb-rel"><h2>İlgili rehberler</h2><ul>{rel_}</ul></section>
</div>
</main>
"""
    return kb_head(p["title"], p["desc"], canon, graph) + hdr + body + _deep(footer("tr", False))


def kb_index():
    i = KB.INDEX
    graph = [
        {"@type": "Organization", "@id": ORG_ID, "name": "AI Trade", "url": SITE + "/"},
        {"@type": "CollectionPage", "@id": KB_BASE + "#page", "url": KB_BASE, "name": i["title"], "description": i["desc"],
         "inLanguage": "tr", "publisher": {"@id": ORG_ID},
         "hasPart": [{"@type": "Article", "headline": p["h1"], "url": KB_BASE + p["slug"]} for p in KB.PAGES]},
        _crumbs([("Ana sayfa", SITE + "/tr/"), ("Kaynaklar", KB_BASE)]),
    ]
    cards = "".join(f'<a class="kb-card" href="{p["slug"]}"><span class="kb-n">{n + 1:02d}</span><h2>{e(p["card"])}</h2><p>{e(p["q"])}</p><span class="kb-go">Oku →</span></a>' for n, p in enumerate(KB.PAGES))
    hdr = _deep('<div class="dark">' + header("tr", "home", False) + "</div>")
    body = f"""<main class="kb">
<div class="wrap kb-wrap kb-wide">
<nav class="kb-crumb" aria-label="Konum"><a href="../">Ana sayfa</a></nav>
<h1>{e(i['h1'])}</h1>
<p class="kb-lead">{e(i['lead'])}</p>
<div class="kb-grid">{cards}</div>
<aside class="kb-cta"><p>Kendi rakamlarınızla görmek isterseniz, kayıpları birlikte çıkaralım.</p><a class="btn btn-amber" href="../check-up">Ücretsiz check-up</a></aside>
</div>
</main>
"""
    return kb_head(i["title"], i["desc"], KB_BASE, graph) + hdr + body + _deep(footer("tr", False))


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "tr"))
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(OUT, "assets"))
    for lang in ("en", "tr"):
        for key, fn in (("home", home), ("cu", checkup), ("privacy", privacy)):
            path = PAGES[key][0 if lang == "en" else 1]
            with open(os.path.join(OUT, path), "w", encoding="utf-8") as f:
                f.write(fn(lang))
    os.makedirs(os.path.join(OUT, "tr", "kaynaklar"))
    with open(os.path.join(OUT, "tr", "kaynaklar", "index.html"), "w", encoding="utf-8") as f:
        f.write(kb_index())
    for p in KB.PAGES:
        with open(os.path.join(OUT, "tr", "kaynaklar", p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(kb_page(p))
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write("aitradeai.net")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE)
    today = datetime.date.today().isoformat()
    urls = []
    for key in PAGES:
        en_c, tr_c = SITE + PAGES[key][2], SITE + PAGES[key][3]
        alts = ('<xhtml:link rel="alternate" hreflang="en" href="%s"/><xhtml:link rel="alternate" hreflang="tr" href="%s"/>'
                '<xhtml:link rel="alternate" hreflang="x-default" href="%s"/>') % (en_c, tr_c, en_c)
        for loc in (en_c, tr_c):
            urls.append("<url><loc>%s</loc><lastmod>%s</lastmod>%s</url>" % (loc, today, alts))
    for u in [KB_BASE] + [KB_BASE + p["slug"] for p in KB.PAGES]:
        urls.append("<url><loc>%s</loc><lastmod>%s</lastmod></url>" % (u, KB.UPDATED))
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n%s\n</urlset>\n' % "\n".join(urls))
    with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms_txt())
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found — AI Trade</title><meta name="robots" content="noindex"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/style.css"></head><body class="hero-light"><header class="site-header"><div class="wrap"><a class="brand" href="/"><span class="brand-a">A</span>I Trade</a></div></header><main class="nf-main"><div class="wrap"><p class="eyebrow">404</p><h1>Page not found.</h1><p class="lead">Bu sayfa bulunamadı.</p><div class="btn-row"><a class="btn btn-amber" href="/">AI Trade</a><a class="btn btn-est" href="/tr/">Türkçe</a></div></div></main></body></html>')
    print("built", OUT)


if __name__ == "__main__":
    main()
