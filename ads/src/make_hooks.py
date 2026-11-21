"""Five hook ads for the register-interest campaign (approved from ads/mocks/hooks), EN + DE, feed + story.
Reuses the styles of make_ads.py. Run: python3 make_hooks.py && node render.js $PWD/html-hooks $PWD/../images/hooks"""
import pathlib, json
HERE = pathlib.Path(__file__).parent
src = (HERE / "make_ads.py").read_text()
ns = {"__file__": str(HERE / "make_ads.py")}
exec(src[:src.index("jobs = []")].replace('OUT.mkdir(parents=True, exist_ok=True)', ''), ns)
head, brand, SIZES = ns["head"], ns["brand"], ns["SIZES"]
OUT = HERE / "html-hooks"; OUT.mkdir(exist_ok=True)
IMG = HERE.parent / "images" / "hooks"; IMG.mkdir(exist_ok=True)

EXTRA = """<style>
.note{font-size:22px;color:var(--ink2);margin-top:22px;line-height:1.4}
.a .note{color:rgba(245,240,231,.6)}
.hours{font-family:Newsreader,serif;line-height:.8;color:var(--terra);letter-spacing:-.05em}
.hours small{font-size:.4em;font-style:italic;margin-left:10px}
.nod{display:flex;flex-direction:column;gap:16px}
.nod span{font-weight:600;background:var(--paper);border:2px solid var(--sand);border-radius:24px;padding:20px 28px}
.nod span:before{content:"✓";display:inline-grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--butter);margin-right:18px;font-weight:800;font-size:26px}
.perks{display:flex;flex-direction:column;gap:14px;margin-top:40px}
.perks span{font-size:34px;font-weight:600;color:var(--cream)}
.perks span:before{content:"✦ ";color:var(--butter)}
.seats{display:flex;gap:14px;margin-top:40px}
.seats i{width:66px;height:66px;border-radius:33px 33px 10px 10px;border:3px solid var(--butter)}
.clock{border-radius:50%;background:conic-gradient(var(--butter) 0 25%, var(--sand) 25% 100%);position:relative}
.clock:after{content:"";position:absolute;inset:40px;border-radius:50%;background:var(--cream)}
.three{display:flex;gap:18px;align-items:flex-end}
.three i{width:76px;height:170px;border-radius:60px 60px 18px 18px;background:var(--sand)}
.three i.on{background:var(--terra)}
</style>"""

T = {
 "en": dict(cta="Register interest", where="Vienna · from 2027",
   h1_big="10<small>h</small>", h1="A week on paperwork. <i>How much could a tool take over?</i>",
   h1_sub="10 Vienna businesses get a free analysis when we launch in 2027.",
   h1_note="Restaurants and hotels: about 10 hours a week on bureaucracy (WKO survey of 600 businesses, 2024).",
   h2="Sound <i>familiar?</i>", h2_items=["The phone rings mid-service", "No-shows, again", "The rota takes all evening", "Same questions on WhatsApp all day"],
   h2_sub="If you nodded, tell us. 10 businesses get it analysed free when we launch.",
   h3="Less time at the desk. <i>More time for clients.</i>",
   h3_sub="We find the admin a tool can take off your plate. Free for the first 10 Vienna businesses when we launch in 2027.",
   h4_kicker="FOUNDING CLIENTS · VIENNA 2027", h4="Only <i>10</i> founding places.",
   h4_perks=["Free AI analysis (planned €1,490)", "First in line when we start", "Founding-client rate afterwards"],
   h4_note="Registration takes 2 minutes. No obligation.", h4_cta="Claim a place",
   h5="<i>3 in 10</i> Austrian businesses already use AI.",
   h5_sub="Start with the right tools, not the hype. 10 businesses get a free analysis when we launch in 2027.",
   h5_note="Businesses with 10+ staff, 2025 (Statistik Austria)."),
 "de": dict(cta="Interesse anmelden", where="Wien · ab 2027",
   h1_big="10<small>h</small>", h1="pro Woche für Papierkram. <i>Wie viel davon kann ein Tool übernehmen?</i>",
   h1_sub="10 Wiener Betriebe erhalten zum Start 2027 eine Gratis-Analyse.",
   h1_note="Gastronomie und Hotellerie: rund 10 Stunden pro Woche für Bürokratie (WKO-Umfrage unter 600 Betrieben, 2024).",
   h2="Kommt Ihnen das <i>bekannt vor?</i>", h2_items=["Das Telefon läutet mitten im Service", "Schon wieder No-Shows", "Der Dienstplan kostet den ganzen Abend", "Den ganzen Tag dieselben WhatsApp-Fragen"],
   h2_sub="Dann erzählen Sie es uns. 10 Betriebe bekommen es zum Start gratis analysiert.",
   h3="Weniger Zeit am Schreibtisch. <i>Mehr Zeit für Ihre Kund:innen.</i>",
   h3_sub="Wir finden die Büroarbeit, die ein Tool Ihnen abnehmen kann. Gratis für die ersten 10 Wiener Betriebe zum Start 2027.",
   h4_kicker="GRÜNDUNGSKUND:INNEN · WIEN 2027", h4="Nur <i>10</i> Gründungs&shy;plätze.",
   h4_perks=["Gratis-KI-Analyse (geplant € 1.490)", "Als Erste an der Reihe", "Gründungskund:innen-Tarif danach"],
   h4_note="Anmeldung in 2 Minuten. Ohne Verpflichtung.", h4_cta="Platz sichern",
   h5="<i>3 von 10</i> Betrieben in Österreich nutzen bereits KI.",
   h5_sub="Starten Sie mit den richtigen Tools, nicht mit dem Hype. 10 Betriebe erhalten zum Start 2027 eine Gratis-Analyse.",
   h5_note="Unternehmen ab 10 Beschäftigten, 2025 (Statistik Austria)."),
}

def foot(t, cta=None):
    return f'<div class="foot"><span class="cta">{cta or t["cta"]} →</span><span class="langs">{t["where"]}</span></div>'

def ads(t, st, de):
    k = 1.12 if st else 1.0           # story: a little larger
    f = lambda n: int(n * k)
    return {
"1-ten-hours": ('', f'''{brand()}<div class="mid">
<div class="hours" style="font-size:{f(300)}px">{t["h1_big"]}</div>
<h1 style="font-size:{f(78 if de else 84)}px;margin-top:40px">{t["h1"]}</h1>
<p class="sub" style="margin-top:30px">{t["h1_sub"]}</p>
<p class="note">{t["h1_note"]}</p></div>{foot(t)}'''),
"2-sound-familiar": ('', f'''{brand()}<div class="mid">
<h1 style="font-size:{f(92 if de else 104)}px">{t["h2"]}</h1>
<div class="nod" style="margin-top:44px">{"".join(f'<span style="font-size:{f(34 if de else 36)}px">{x}</span>' for x in t["h2_items"])}</div>
<p class="sub" style="margin-top:40px">{t["h2_sub"]}</p></div>{foot(t)}'''),
"3-more-time-for-clients": ('', f'''{brand()}<div class="mid">
<div class="clock" style="width:{f(260)}px;height:{f(260)}px"></div>
<h1 style="font-size:{f(100 if de else 112)}px;margin-top:56px">{t["h3"]}</h1>
<p class="sub" style="margin-top:40px">{t["h3_sub"]}</p></div>{foot(t)}'''),
"4-founding-places": ('a', f'''<div class="ring"></div>{brand(True)}<div class="mid">
<div class="kicker">{t["h4_kicker"]}</div>
<h1 style="font-size:{f(98 if de else 104)}px;margin-top:34px">{t["h4"]}</h1>
<div class="seats">{"<i></i>" * 10}</div>
<div class="perks">{"".join(f"<span>{x}</span>" for x in t["h4_perks"])}</div>
<p class="note" style="font-size:26px">{t["h4_note"]}</p></div>{foot(t, t["h4_cta"])}'''),
"5-three-in-ten": ('', f'''{brand()}<div class="mid">
<div class="three">{'<i class="on"></i>' * 3}{"<i></i>" * 7}</div>
<h1 style="font-size:{f(86 if de else 92)}px;margin-top:44px">{t["h5"]}</h1>
<p class="sub" style="margin-top:30px">{t["h5_sub"]}</p>
<p class="note">{t["h5_note"]}</p></div>{foot(t)}'''),
    }

jobs = []
for lang, t in T.items():
    for fmt, (w, h) in SIZES.items():
        for name, (cls, body) in ads(t, fmt == "story", lang == "de").items():
            n = f"{lang}-{name}-{fmt}"
            (OUT / f"{n}.html").write_text(head(w, h, fmt == "story") + EXTRA + f'<div class="frame {cls}">{body}</div></body></html>')
            jobs.append({"name": n, "w": w, "h": h})
json.dump(jobs, open(OUT / "jobs.json", "w"))
print(len(jobs), "hook ads")
