"""Generate Facebook/Instagram ad creatives as HTML, then render them to PNG with render.js.
Run: python3 make_ads.py && node render.js
"""
import json, pathlib
OUT = pathlib.Path(__file__).parent / "html"; OUT.mkdir(exist_ok=True)
SIZES = {"feed": (1080, 1350), "story": (1080, 1920)}

T = {
 "en": dict(
   kicker="PILOT PROGRAMME · 10 PLACES",
   a_h="Your first AI project. <i>On us.</i>",
   a_sub="10 restaurants, hotels and wellness &amp; beauty businesses get our Starter package free.",
   a_worth="Normally €3,900", a_free="Free for 10",
   b_q="“40 booking calls a week during service. A quarter go unanswered.”",
   b_h="Tell us your biggest daily headache. <i>We solve 10 for free.</i>",
   b_sub="Describe a real problem. We set up the AI tools and train your team.",
   c_h="Less admin. <i>More time for guests.</i>",
   c_sub="Free AI Starter package for 10 businesses: setup, training and 30 days of help.",
   arches=("Dine","Stay","Care"), labels=("Gastronomy","Hospitality","Wellness &amp; Beauty"),
   cta="Apply now", lang="EN · DE · FR · SK", brand_line="Vienna"),
 "de": dict(
   kicker="PILOTPROGRAMM · 10 PLÄTZE",
   a_h="Ihr erstes KI-Projekt. <i>Auf uns.</i>",
   a_sub="10 Restaurants, Hotels und Betriebe aus Wellness &amp; Beauty erhalten unser Starter-Paket gratis.",
   a_worth="Regulär € 3.900", a_free="Gratis für 10",
   b_q="„40 Reservierungsanrufe pro Woche im Service. Ein Viertel bleibt unbeantwortet.“",
   b_h="Erzählen Sie uns Ihr größtes Alltagsproblem. <i>Wir lösen 10 gratis.</i>",
   b_sub="Beschreiben Sie ein echtes Problem. Wir richten die KI-Tools ein und schulen Ihr Team.",
   c_h="Weniger Papierkram. <i>Mehr Zeit für Gäste.</i>",
   c_sub="Gratis KI-Starter-Paket für 10 Betriebe: Einrichtung, Schulung und 30 Tage Unterstützung.",
   arches=("Essen","Wohnen","Pflege"), labels=("Gastronomie","Hotellerie","Wellness &amp; Beauty"),
   cta="Jetzt bewerben", lang="DE · EN · FR · SK", brand_line="Wien"),
}

CSS = """
:root{--cream:#F5F0E7;--paper:#FBF8F2;--ink:#1E1C17;--ink2:#5C564B;--terra:#C4623F;--olive:#6B7442;--forest:#1F3B33;--butter:#F0D690;--sand:#E9DFCD}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{font-family:Manrope,sans-serif;color:var(--ink);background:var(--cream);-webkit-font-smoothing:antialiased}
.frame{position:relative;width:100%%;height:100%%;padding:%(pad)s;display:flex;flex-direction:column}
.mid{margin:auto 0;padding:28px 0}
h1{font-family:Newsreader,serif;font-weight:400;letter-spacing:-.03em;line-height:1.02}
h1 i{color:var(--terra)}
.kicker{font-weight:800;font-size:26px;letter-spacing:.14em}
.brand{display:flex;align-items:center;gap:16px;font-family:Newsreader,serif;font-size:44px;letter-spacing:-.02em}
.brand i{color:var(--terra)}
.mark{width:46px;height:46px;border-radius:23px 23px 7px 7px;background:var(--terra);position:relative}
.mark:after{content:"";position:absolute;left:14px;right:14px;bottom:0;height:20px;border-radius:9px 9px 0 0;background:var(--cream)}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:center}
.cta{background:var(--terra);color:#fff;font-weight:800;font-size:34px;padding:26px 46px;border-radius:999px}
.langs{font-weight:700;font-size:24px;letter-spacing:.08em;color:var(--ink2)}
.sub{font-size:38px;line-height:1.4;color:var(--ink2)}
/* A: offer */
.a{background:var(--forest);color:var(--cream)}
.a .kicker{color:var(--butter)} .a h1 i{color:var(--butter)} .a .sub{color:rgba(245,240,231,.82)}
.a .brand{color:var(--cream)} .a .mark:after{background:var(--forest)} .a .langs{color:rgba(245,240,231,.7)}
.a .big{font-family:Newsreader,serif;font-size:%(bign)dpx;line-height:.8;color:var(--terra);letter-spacing:-.05em}
.a .pill{white-space:nowrap;flex-shrink:0;display:inline-flex;gap:18px;align-items:center;background:var(--cream);color:var(--ink);border-radius:999px;padding:18px 30px;font-size:30px;font-weight:700}
.a .pill s{color:var(--ink2);font-weight:500}
.a .pill b{color:var(--terra)}
.a .cta{background:var(--butter);color:var(--ink)}
.ring{position:absolute;right:-220px;top:-160px;width:700px;height:700px;border-radius:50%%;border:2px solid rgba(245,240,231,.15)}
/* B: pain */
.qcard{background:var(--paper);border:2px solid var(--sand);border-radius:40px;padding:48px 52px;box-shadow:0 40px 80px -40px rgba(30,28,23,.35)}
.qcard .lbl{font-size:22px;font-weight:800;letter-spacing:.14em;color:var(--olive);margin-bottom:18px}
.qcard q{font-family:Newsreader,serif;font-size:%(qsize)dpx;line-height:1.22;quotes:none;display:block}
.tagrow{display:flex;gap:14px;flex-wrap:wrap}
.tag{font-size:24px;font-weight:700;padding:12px 22px;border-radius:999px;background:var(--paper);border:2px solid var(--sand)}
.tag.on{background:var(--butter);border-color:var(--butter)}
/* C: arches */
.arches{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;align-items:end}
.arch{border-radius:999px 999px 26px 26px;color:#fff;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;padding:30px 12px;position:relative;overflow:hidden}
.arch:before{content:"";position:absolute;inset:0;opacity:.14;background-image:radial-gradient(circle at 1.5px 1.5px,#fff 1.5px,transparent 0);background-size:20px 20px}
.arch .g{position:absolute;top:22%%;left:0;right:0;text-align:center;font-family:Newsreader,serif;font-style:italic;font-size:%(gsize)dpx}
.arch .l{position:relative;font-size:21px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;text-align:center}
.arch:nth-child(1){background:var(--terra);height:%(a1)dpx}.arch:nth-child(2){background:var(--olive);height:%(a2)dpx}.arch:nth-child(3){background:var(--forest);height:%(a3)dpx}
.free{display:inline-block;background:var(--forest);color:var(--butter);font-weight:800;font-size:26px;letter-spacing:.1em;padding:14px 24px;border-radius:14px}
"""

def head(w, h, story):
    v = dict(w=w, h=h, pad="250px 84px 360px" if story else "76px 84px", bign=380 if story else 300,
             qsize=58 if story else 50, gsize=68 if story else 64,
             a1=420 if story else 400, a2=490 if story else 470, a3=400 if story else 380)
    return ('<!doctype html><html><head><meta charset="utf-8">'
            '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&display=swap" rel="stylesheet">'
            '<style>' + CSS % v + '</style></head><body>')

def brand(): return '<div class="brand"><span class="mark"></span>Implement<i>AI</i></div>'

def ad_a(t, story):
    gap = 70 if story else 40
    return f'''<div class="frame a"><div class="ring"></div>
{brand()}<div class="mid">
<div class="kicker">{t["kicker"]}</div>
<div style="display:flex;align-items:flex-end;gap:36px;margin-top:{gap}px"><div class="big">10</div>
<div class="pill" style="margin-bottom:30px"><s>{t["a_worth"]}</s><b>{t["a_free"]}</b></div></div>
<h1 style="font-size:{108 if story else 92}px;margin-top:{gap}px">{t["a_h"]}</h1>
<p class="sub" style="margin-top:{gap-10}px">{t["a_sub"]}</p></div>
<div class="foot"><span class="cta">{t["cta"]} →</span><span class="langs">{t["brand_line"]} · {t["lang"]}</span></div></div>'''

def ad_b(t, story):
    gap = 64 if story else 40
    labels = "".join(f'<span class="tag{" on" if i==0 else ""}">{l}</span>' for i, l in enumerate(t["labels"]))
    return f'''<div class="frame">
{brand()}<div class="mid">
<div class="qcard"><div class="lbl">{"A REAL USE CASE" if t is T["en"] else "EIN ECHTER ANWENDUNGSFALL"}</div><q>{t["b_q"]}</q></div>
<h1 style="font-size:{96 if story else 84}px;margin-top:{gap}px">{t["b_h"]}</h1>
<p class="sub" style="margin-top:{gap-14}px">{t["b_sub"]}</p>
<div class="tagrow" style="margin-top:{gap-10}px">{labels}</div></div>
<div class="foot"><span class="cta">{t["cta"]} →</span><span class="langs">{t["kicker"].split("·")[1].strip()}</span></div></div>'''

def ad_c(t, story):
    gap = 64 if story else 36
    arches = "".join(f'<div class="arch"><div class="g">{g}</div><div class="l">{l}</div></div>' for g, l in zip(t["arches"], t["labels"]))
    return f'''<div class="frame">
{brand()}<div class="mid">
<h1 style="font-size:{96 if story else 88}px">{t["c_h"]}</h1>
<div style="margin-top:{gap-6}px"><span class="free">{t["kicker"]}</span></div>
<div class="arches" style="margin-top:{gap+6}px">{arches}</div>
<p class="sub" style="margin-top:{gap-6}px">{t["c_sub"]}</p></div>
<div class="foot"><span class="cta">{t["cta"]} →</span><span class="langs">{t["brand_line"]} · {t["lang"]}</span></div></div>'''

jobs = []
for lang, t in T.items():
    for cname, fn in (("offer", ad_a), ("pain", ad_b), ("industries", ad_c)):
        for fmt, (w, h) in SIZES.items():
            name = f"{lang}-{cname}-{fmt}"
            (OUT / f"{name}.html").write_text(head(w, h, fmt == "story") + fn(t, fmt == "story") + "</body></html>")
            jobs.append({"name": name, "w": w, "h": h})
json.dump(jobs, open(OUT / "jobs.json", "w"))
print(len(jobs), "ads")
