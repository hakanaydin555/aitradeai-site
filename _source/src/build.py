# -*- coding: utf-8 -*-
"""Builds the static site into ../dist. Run: python3 build.py"""
import os, shutil, html, urllib.parse
from content import T, SITE, CAL, WA_NUMBER, LINKEDIN

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "dist")

PAGES = {  # key: (en path, tr path, canonical en, canonical tr)
    "home": ("index.html", "tr/index.html", "/", "/tr/"),
    "cu": ("check-up.html", "tr/check-up.html", "/check-up", "/tr/check-up"),
    "privacy": ("privacy.html", "tr/privacy.html", "/privacy", "/tr/privacy"),
}

e = html.escape
CHECK = '<svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10.5l4 4 8-9" fill="none" stroke="#F59E0B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHAT = '<svg width="18" height="18" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 15.5l-1 3 3.4-1.6A8 8 0 1 0 4 15.5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'


def wa(lang):
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, urllib.parse.quote(T[lang]["wa_text"]))


def rel(lang, target_lang, key):
    """Relative link from a page in `lang` to page `key` in `target_lang`."""
    path = PAGES[key][0 if target_lang == "en" else 1]
    prefix = "../" if lang == "tr" else ""
    return prefix + path


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
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'tr_TR'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0E1A2B">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@500;600;700;800&amp;family=Source+Sans+3:wght@400;600&amp;display=swap" rel="stylesheet">
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
<a class="brand" href="{rel(lang, lang, 'home')}">AI Trade</a>
<nav class="nav" aria-label="Main">
<a class="navlink" href="{home}#how">{n['how']}</a>
<a class="navlink" href="{home}#measure">{n['results']}</a>
<a class="navlink" href="{home}#about">{n['about']}</a>
<a class="navlink" href="{home}#contact">{n['contact']}</a>
<div class="lang" role="group" aria-label="{n['lang_label']}">
<a href="{l_en}" hreflang="en" lang="en" data-setlang="en" aria-current="{'true' if lang == 'en' else 'false'}">EN</a>
<a href="{l_tr}" hreflang="tr" lang="tr" data-setlang="tr" aria-current="{'true' if lang == 'tr' else 'false'}">TR</a>
</div>
<a class="btn btn-amber" href="{rel(lang, lang, 'cu')}">{n['cta']}</a>
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
</nav>
</div>
</footer>
<a class="fab" href="{home}#contact">{CHAT}<span>{T[lang]['fab']}</span></a>
</body>
</html>
"""


def home(lang):
    h = T[lang]["home"]
    out = [head(lang, "home", h), '<div class="dark">', header(lang, "home", True)]
    rows = "".join(f'<div><span>{e(a)}</span><span class="st s{i+1}">{e(b)}</span></div>' for i, (a, b) in enumerate(h["rows"]))
    out.append(f"""<section class="hero" id="top">
<div class="wrap">
<div class="hero-copy">
<p class="eyebrow">{h['eyebrow']}</p>
<h1 class="rise">{h['h1']}</h1>
<p class="lead rise d2">{e(h['lead'])} <span class="weeks">{e(h['lead_weeks'])}</span></p>
<div class="hero-ctas rise d3">
<a class="btn btn-amber" href="{rel(lang, lang, 'cu')}">{e(h['cta'])}</a>
<a class="ghost" href="#how">{e(h['ghost'])}</a>
</div>
</div>
<div class="panel anim">
<div class="panel-head">
<div><p class="panel-kicker">{e(h['panel_kicker'])}</p><p class="panel-title">{e(h['panel_title'])}</p></div>
<span class="tag">{e(h['panel_tag'])}</span>
</div>
<svg viewBox="0 0 400 170" role="img" aria-label="{e(h['chart_aria'])}">
<line x1="0" y1="140" x2="400" y2="140" stroke="rgba(255,255,255,0.12)"/>
<line x1="0" y1="95" x2="400" y2="95" stroke="rgba(255,255,255,0.06)"/>
<line x1="0" y1="50" x2="400" y2="50" stroke="rgba(255,255,255,0.06)"/>
<line class="fadein" x1="0" y1="112" x2="400" y2="112" stroke="#8FA0B5" stroke-width="1.5" stroke-dasharray="5 5"/>
<text class="fadein" x="4" y="106" fill="#8FA0B5" font-size="11" font-family="Geist, sans-serif">{e(h['chart_base'])}</text>
<line class="fixmark" x1="170" y1="20" x2="170" y2="150" stroke="rgba(246,185,122,0.5)"/>
<text class="fixmark" x="176" y="30" fill="#F6B97A" font-size="11" font-family="Geist, sans-serif">{e(h['chart_live'])}</text>
<polyline class="draw" pathLength="1" points="0,116 34,110 68,118 102,113 136,117 170,112 204,98 238,86 272,74 306,66 340,58 374,52 400,48" fill="none" stroke="#F59E0B" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
<circle class="popdot" cx="396" cy="48" r="4" fill="#F59E0B"/>
<text x="2" y="164" fill="#8FA0B5" font-size="11" font-family="Geist, sans-serif">{e(h['chart_w1'])}</text>
<text x="398" y="164" text-anchor="end" fill="#8FA0B5" font-size="11" font-family="Geist, sans-serif">{e(h['chart_w8'])}</text>
</svg>
<div class="panel-rows">{rows}</div>
</div>
</div>
</section>
""")
    out.append('</div>\n<main>\n')

    nodes = "".join(f'<li class="node n{i+1}"><span class="dot" aria-hidden="true">{i+1}</span><span class="txt"><span class="nt">{e(a)}</span><span class="nl">{e(b)}</span><span class="nf">{e(c)}</span></span></li>' for i, (a, b, c) in enumerate(h["nodes"]))
    out.append(f"""<section class="section grey" id="leaks">
<div class="wrap">
<div class="sec-head reveal"><h2>{e(h['leak_h'])}</h2><p>{e(h['leak_p'])}</p></div>
<div class="leakmap">
<div class="leakline" aria-hidden="true"></div>
<ol class="nodes">{nodes}</ol>
</div>
<div class="leak-cta"><p>{e(h['leak_q'])}</p><a href="{rel(lang, lang, 'cu')}">{e(h['leak_a'])}</a></div>
</div>
</section>
""")
    plan = "".join(f'<div class="prow"><p class="w">{e(w)}</p><p class="t">{e(t)}</p><p class="d">{e(d)}</p></div>' for w, t, d in h["plan"])
    out.append(f"""<section class="section" id="how">
<div class="wrap">
<div class="sec-head reveal"><h2>{e(h['how_h'])}</h2><p>{e(h['how_p'])}</p></div>
<div class="plist stagger">{plan}</div>
<div class="example reveal">
<p class="ex-k">{e(h['ex_k'])}</p>
<h3>{e(h['ex_h'])}</h3>
<p class="ex-ctx">{e(h['ex_ctx'])}</p>
<div class="ex-cols">{"".join(f'<div><p class="ex-t">{e(t)}</p><p>{e(d)}</p></div>' for t, d in h['ex_cols'])}<div><p class="ex-t">{e(h['ex_res_h'])}</p><div class="ex-stats">{"".join(f'<div><p class="ex-n">{e(n)}</p><p class="ex-l">{e(l)}</p></div>' for n, l in h['ex_res'])}</div></div></div>
<a class="link" href="{rel(lang, lang, 'cu')}">{e(h['ex_cta'])}</a>
</div>
</div>
</section>
""")
    metrics = "".join(f'<div><p class="k">{e(k)}</p><p class="v">{e(v)}</p></div>' for k, v in h["metrics"])
    cases = "".join(f'<div class="case"><p class="big"><span data-count="{n}" data-suffix="{s}">{n}{s}</span></p><p class="what">{e(w)}</p><p class="ctx">{e(c)}</p></div>' for n, s, w, c in h["cases"])
    out.append(f"""<section class="section dark" id="measure">
<div class="wrap">
<div class="sec-head reveal"><h2>{e(h['m_h'])}</h2><p>{e(h['m_p'])}</p></div>
<div class="measure-grid stagger">{metrics}</div>
<div class="cases">
<p class="cases-note">{e(h['cases_note'])}<span class="swipe-hint">{e(h['swipe'])}</span></p>
<div class="case-track stagger">{cases}</div>
<div class="case-dots" aria-hidden="true"><span class="on"></span><span></span><span></span></div>
</div>
</div>
</section>
""")
    pr = "".join(f'<div class="principle"><p class="k">{e(k)}</p><h3>{e(t)}</h3><p>{e(d)}</p></div>' for k, t, d in h["principles"])
    out.append(f"""<section class="section" id="about">
<div class="wrap">
<div class="sec-head reveal"><h2>{e(h['p_h'])}</h2><p>{e(h['p_p'])}</p></div>
<div class="principles stagger">{pr}</div>
<p class="principles-foot">{e(h['p_foot'])}</p>
</div>
</section>
""")
    c = h["cards"]
    links = [rel(lang, lang, "cu"), wa(lang)]
    cls = ["btn btn-amber", "btn btn-dark"]
    ext = ["", 'target="_blank" rel="noopener"']
    cards = "".join(f'<div class="ccard"><p class="k">{e(k)}</p><h3>{e(t)}</h3><p>{e(d)}</p><a class="{cls[i]}" href="{e(links[i])}" {ext[i]}>{e(b)}</a></div>' for i, (k, t, d, b) in enumerate(c))
    m = h["c_mobile"]
    out.append(f"""<section class="section grey" id="contact">
<div class="wrap">
<div class="sec-head reveal"><h2>{e(h['c_h'])}</h2><p>{e(h['c_p'])}</p></div>
<div class="contact-grid stagger">{cards}</div>
<div class="contact-mobile stagger">
<a class="btn btn-amber" href="{rel(lang, lang, 'cu')}">{e(m[0])}</a>
<a class="btn btn-line" href="{e(wa(lang))}" target="_blank" rel="noopener">{e(m[1])}</a>
</div>
</div>
</section>
</main>
""")
    out.append(footer(lang, True))
    return "".join(out)


def checkup(lang):
    c = T[lang]["cu"]
    privacy = rel(lang, lang, "privacy")
    out = [head(lang, "cu", c), '<div class="dark">', header(lang, "cu", False)]
    gets = "".join(f"<div>{CHECK}<span>{e(g)}</span></div>" for g in c["gets"])
    qsteps = []
    for i, (key, q, opts) in enumerate(c["qs"]):
        buttons = "".join(f'<button type="button" class="opt" aria-pressed="false" data-i="{j}">{e(o)}</button>' for j, o in enumerate(opts))
        qsteps.append(f'<div data-step="{i}" data-key="{key}" data-q="{e(q)}"{" hidden" if i else ""}><h2>{e(q)}</h2><div class="opts" style="margin-top:18px">{buttons}</div></div>')
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
<div class="summary" style="margin-top:18px"><strong>{e(c['d_sum'])}</strong><div class="summary-list"></div></div>
<button type="button" class="back restart" style="color:var(--amber-text);font-weight:600">{e(c['restart'])}</button>
</div>
<button type="button" class="back" hidden>{e(c['back'])}</button>
</form>
<p class="form-alt">{alt}</p>
<p class="founder">{founder}</p>
</div>
</div>
</section>
</div>
<main>
""")
    areas = "".join(f'<div><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in c["areas"])
    notes = "".join(f"<p>{e(n)}</p>" for n in c["notes"])
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
<h2 class="h2-left">{e(c['a_h'])}</h2>
<div class="areas stagger">{areas}</div>
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
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write("aitradeai.net")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE)
    urls = []
    for key in PAGES:
        for i in (2, 3):
            urls.append("<url><loc>%s%s</loc></url>" % (SITE, PAGES[key][i]))
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % "".join(urls))
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found — AI Trade</title><link rel="stylesheet" href="/assets/style.css"></head><body><div class="dark" style="min-height:100vh;display:flex;align-items:center"><div class="wrap" style="display:flex;flex-direction:column;gap:20px;padding-top:80px;padding-bottom:80px"><p class="eyebrow">404</p><h1 style="font-size:48px;letter-spacing:-.03em">Page not found.</h1><p style="color:#C9D1DC">Bu sayfa bulunamadı.</p><p><a class="btn btn-amber" href="/">AI Trade home</a></p></div></div></body></html>')
    print("built", OUT)


if __name__ == "__main__":
    main()
