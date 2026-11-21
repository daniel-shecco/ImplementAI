"""Mock-ups: images for the five Hook Point copies (ads/HOOKPOINT-COPY.md), English feed 1080x1350.
Run: python3 make.py && node ../../src/render.js $PWD/html $PWD"""
import pathlib, json, base64
HERE = pathlib.Path(__file__).parent; ROOT = HERE.parents[2]
src = (ROOT / "ads/src/make_ads.py").read_text()
ns = {"__file__": str(ROOT / "ads/src/make_ads.py")}
exec(src[:src.index("jobs = []")].replace('OUT.mkdir(parents=True, exist_ok=True)', ''), ns)
head, brand = ns["head"], ns["brand"]
OUT = HERE / "html"; OUT.mkdir(exist_ok=True)
img = lambda n: base64.b64encode((ROOT / f"assets/img/team/{n}.jpg").read_bytes()).decode()
EXTRA = """<style>
.note{font-size:22px;color:var(--ink2);margin-top:20px}
.night{background:#14181c;color:#F5F0E7}
.notif{background:rgba(245,240,231,.1);border:1px solid rgba(245,240,231,.16);border-radius:26px;padding:20px 26px;display:flex;gap:18px;align-items:center;font-size:28px}
.notif b{display:block;font-size:22px;letter-spacing:.06em;color:#F0D690;text-transform:uppercase;margin-bottom:4px}
.notif i{font-style:normal;width:56px;height:56px;border-radius:16px;display:grid;place-items:center;font-size:30px;flex:none}
.clock{font-family:Newsreader,serif;font-size:210px;line-height:.9;letter-spacing:-.04em}
.week{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}
.week div{height:150px;border-radius:16px;background:var(--sand);position:relative;overflow:hidden}
.week div:after{content:"";position:absolute;left:0;right:0;bottom:0;height:var(--h);background:var(--terra)}
.week span{display:block;text-align:center;font-weight:800;font-size:20px;color:var(--ink2);margin-top:10px;letter-spacing:.08em}
.trio{display:flex;flex-direction:column;gap:22px}
.trio div{display:flex;align-items:center;gap:30px;font-family:Newsreader,serif;font-size:104px;line-height:1;color:var(--cream)}
.trio div em{font-style:italic;color:var(--butter)}
.trio b{width:86px;height:86px;border-radius:43px 43px 14px 14px;background:var(--terra);flex:none}
.trio div:nth-child(2) b{background:var(--olive)} .trio div:nth-child(3) b{background:var(--butter)}
.stamp{display:inline-block;background:var(--butter);color:var(--ink);font-weight:800;font-size:30px;padding:16px 28px;border-radius:999px;transform:rotate(-3deg)}
.team{display:flex;gap:20px;align-items:flex-end}
.team div{flex:1;border-radius:999px 999px 18px 18px;padding:10px}
.team div span{display:block;width:100%;height:100%;border-radius:999px 999px 12px 12px;background-size:cover;background-position:center 20%}
</style>"""
FOOT = '<div class="foot"><span class="cta">Sign up →</span><span class="langs">Vienna · from 2027</span></div>'
A = {
"1-dont-buy-ai": ('', f'''{brand()}<div class="mid">
<h1 style="font-size:190px;line-height:.95">Don't buy <i>AI.</i></h1>
<p class="sub" style="margin-top:44px;font-size:44px">…until someone has spent a day in your business and found the problem worth fixing.</p>
<p class="sub" style="margin-top:36px;font-size:30px">Free for the first 10 Vienna businesses.</p></div>{FOOT}'''),
"2-second-shift": ('night', f'''{brand(True)}<div class="mid">
<div class="clock">23:40</div>
<div style="display:flex;flex-direction:column;gap:14px;margin-top:40px">
<div class="notif"><i style="background:#25D366">✆</i><div><b>WhatsApp · 3 new</b>Table for 6 on Saturday?</div></div>
<div class="notif"><i style="background:#4285F4">★</i><div><b>New review</b>“Waited 20 minutes for the bill…”</div></div>
<div class="notif"><i style="background:#C4623F">✉</i><div><b>Supplier</b>Order deadline tomorrow 07:00</div></div></div>
<h1 style="font-size:84px;margin-top:46px;color:#F5F0E7">Your second shift starts <i style="color:#F0D690">at closing time.</i></h1></div>
<div class="foot"><span class="cta" style="background:#F0D690;color:#1E1C17">Sign up →</span><span class="langs" style="color:rgba(245,240,231,.7)">Free analysis for 10</span></div>'''),
"3-ten-hours": ('', f'''{brand()}<div class="mid">
<div style="font-family:Newsreader,serif;font-size:300px;line-height:.8;color:var(--terra);letter-spacing:-.05em">10<span style="font-size:120px;font-style:italic">h</span></div>
<h1 style="font-size:76px;margin-top:30px">a week on paperwork. <i>Which hours could go?</i></h1>
<div class="week" style="margin-top:44px">{"".join(f'<div style="--h:{h}%"></div>' for h in (40,30,50,20,60))}</div>
<div class="week" style="margin-top:0">{"".join(f'<span>{d}</span>' for d in ("MON","TUE","WED","THU","FRI"))}</div>
<p class="note">Restaurants and hotels, WKO survey of 600 businesses, 2024.</p></div>{FOOT}'''),
"4-one-day-one-plan": ('a', f'''<div class="ring"></div>{brand(True)}<div class="mid">
<div class="trio"><div><b></b>One day.</div><div><b></b>One problem.</div><div><b></b><em>One plan.</em></div></div>
<div style="margin-top:56px"><span class="stamp">Free for the first 10</span></div>
<p class="sub" style="margin-top:40px">Restaurants, hotels, wellness &amp; beauty in Vienna. Launching 2027.</p></div>
<div class="foot"><span class="cta">Sign up →</span><span class="langs">Vienna · from 2027</span></div>'''),
"5-walk-into": ('', f'''{brand()}<div class="mid">
<div class="team" style="height:420px">{"".join(f'<div style="background:var(--{c});height:{h}%"><span style="background-image:url(data:image/jpeg;base64,{img(n)})"></span></div>' for n,c,h in (("daniel","terra",92),("tibor","olive",100),("jean-christophe","forest",88)))}</div>
<p class="sub" style="margin-top:30px;font-size:30px;font-weight:700;color:var(--ink)">An Oxford engineer, a physicist and a data scientist…</p>
<h1 style="font-size:104px;margin-top:14px">…walk into <i>your restaurant.</i></h1>
<p class="sub" style="margin-top:28px;font-size:34px">No joke: a free AI plan for 10 Vienna businesses.</p></div>{FOOT}'''),
}
jobs = []
for name, (cls, body) in A.items():
    (OUT / f"{name}.html").write_text(head(1080, 1350, False) + EXTRA + f'<div class="frame {cls}">{body}</div></body></html>')
    jobs.append({"name": name, "w": 1080, "h": 1350})
json.dump(jobs, open(OUT / "jobs.json", "w")); print(len(jobs))
