"""Mock-ups: five hook ideas for the register-interest ads (English feed, 1080x1350).
Reuses the styles of ads/src/make_ads.py. Run: python3 make_hooks.py && node ../../src/render.js $PWD/html $PWD"""
import pathlib, json
HERE = pathlib.Path(__file__).parent
src = (HERE.parents[1] / "src" / "make_ads.py").read_text()
ns = {"__file__": str(HERE.parents[1] / "src" / "make_ads.py")}
exec(src[:src.index("jobs = []")].replace('OUT.mkdir(parents=True, exist_ok=True)', ''), ns)
head, brand = ns["head"], ns["brand"]
OUT = HERE / "html"; OUT.mkdir(exist_ok=True)
EXTRA = """<style>
.note{font-size:22px;color:var(--ink2);margin-top:22px}
.a .note{color:rgba(245,240,231,.6)}
.hours{font-family:Newsreader,serif;font-size:300px;line-height:.8;color:var(--terra);letter-spacing:-.05em}
.hours small{font-size:120px;font-style:italic;margin-left:10px}
.nod{display:flex;flex-direction:column;gap:16px}
.nod span{font-size:36px;font-weight:600;background:var(--paper);border:2px solid var(--sand);border-radius:24px;padding:20px 28px}
.nod span:before{content:"✓";display:inline-grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--butter);margin-right:18px;font-weight:800;font-size:26px}
.perks{display:flex;flex-direction:column;gap:14px;margin-top:40px}
.perks span{font-size:34px;font-weight:600;color:var(--cream)}
.perks span:before{content:"✦ ";color:var(--butter)}
.seats{display:flex;gap:14px;margin-top:40px}
.seats i{width:66px;height:66px;border-radius:33px 33px 10px 10px;border:3px solid var(--butter)}
.clock{width:330px;height:330px;border-radius:50%;background:conic-gradient(var(--butter) 0 25%, var(--sand) 25% 100%);position:relative}
.clock:after{content:"";position:absolute;inset:40px;border-radius:50%;background:var(--cream)}
.clock b{position:absolute;inset:0;display:grid;place-items:center;z-index:1;font-family:Newsreader,serif;font-style:italic;font-weight:400;font-size:76px;color:var(--forest)}
.three{display:flex;gap:18px;align-items:flex-end}
.three i{width:76px;height:170px;border-radius:60px 60px 18px 18px;background:var(--sand)}
.three i.on{background:var(--terra)}
</style>"""
FOOT = '<div class="foot"><span class="cta">Register interest →</span><span class="langs">Vienna · from 2027</span></div>'
H = {
"1-ten-hours": ('', f'''{brand()}<div class="mid">
<div class="hours">10<small>h</small></div>
<h1 style="font-size:84px;margin-top:40px">A week on paperwork. <i>How much could a tool take off you?</i></h1>
<p class="sub" style="margin-top:30px">10 Vienna businesses get a free analysis when we launch in 2027.</p>
<p class="note">Restaurants and hotels: about 10 hours a week on bureaucracy (WKO survey of 600 businesses, 2024).</p></div>{FOOT}'''),
"2-sound-familiar": ('', f'''{brand()}<div class="mid">
<h1 style="font-size:104px">Sound <i>familiar?</i></h1>
<div class="nod" style="margin-top:44px"><span>The phone rings mid-service</span><span>No-shows, again</span><span>The rota takes all evening</span><span>Same questions on WhatsApp all day</span></div>
<p class="sub" style="margin-top:40px">If you nodded, tell us. 10 businesses get it analysed free when we launch.</p></div>{FOOT}'''),
"3-friday-back": ('', f'''{brand()}<div class="mid">
<div style="display:flex;gap:44px;align-items:center"><div class="clock"><b>Fri</b></div>
<h1 style="font-size:88px;flex:1">What would you do with <i>Friday afternoon</i> back?</h1></div>
<p class="sub" style="margin-top:50px">We find the hours AI can hand back to you and your team. Free for the first 10 Vienna businesses at our 2027 launch.</p></div>{FOOT}'''),
"4-founding-places": ('a', f'''<div class="ring"></div>{brand(True)}<div class="mid">
<div class="kicker">FOUNDING CLIENTS · VIENNA 2027</div>
<h1 style="font-size:104px;margin-top:34px">Only <i>10</i> founding places.</h1>
<div class="seats"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
<div class="perks"><span>Free AI analysis (planned €1,490)</span><span>First in line when we start</span><span>Founding-client rate afterwards</span></div>
<p class="note" style="font-size:26px">Registration takes 10 minutes. No obligation.</p></div>
<div class="foot"><span class="cta">Claim a place →</span><span class="langs">Vienna · from 2027</span></div>'''),
"5-three-in-ten": ('', f'''{brand()}<div class="mid">
<div class="three"><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
<h1 style="font-size:92px;margin-top:44px"><i>3 in 10</i> Austrian businesses already use AI.</h1>
<p class="sub" style="margin-top:30px">Start with the right tools, not the hype. 10 businesses get a free analysis when we launch in 2027.</p>
<p class="note">Businesses with 10+ staff, 2025 (Statistik Austria).</p></div>{FOOT}'''),
}
V3 = {
 "3a-evenings": "Get your <i>evenings</i> back.",
 "3b-desk": "Less time at the desk. <i>More time for guests.</i>",
 "3c-laptop": "Close the laptop. <i>Open the doors.</i>",
 "3d-first-guest": "Admin done <i>before the first guest arrives.</i>",
}
SUB3 = "We find the admin a tool can take off your plate. Free for the first 10 Vienna businesses when we launch in 2027."
for k, h in V3.items():
    H[k] = ('', f'''{brand()}<div class="mid">
<div class="clock" style="width:260px;height:260px"></div>
<h1 style="font-size:112px;margin-top:56px">{h}</h1>
<p class="sub" style="margin-top:40px">{SUB3}</p></div>{FOOT}''')
jobs = []
for name, (cls, body) in H.items():
    (OUT / f"{name}.html").write_text(head(1080, 1350, False) + EXTRA + f'<div class="frame {cls}">{body}</div></body></html>')
    jobs.append({"name": name, "w": 1080, "h": 1350})
json.dump(jobs, open(OUT / "jobs.json", "w"))
print(len(jobs), "hooks")
