"""Proof-of-concept ('register interest') versions of pilot.html and index.html, for approval.
Run: python3 mocks/poc/make_poc.py"""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..')

def sub(s, old, new, n=1):
    assert s.count(old) == n, (old[:60], s.count(old)); return s.replace(old, new)

BAR_CSS = """<style>
.launch-bar{background:var(--forest);color:var(--cream);font-size:.92rem;padding:11px 0;text-align:center}
.launch-bar b{color:var(--butter);font-weight:700}
.launch-bar a{color:var(--butter)}
.member .portrait span.cred{font-size:1rem;letter-spacing:.1em}
</style>"""

def common(s, bar):
    s = s.replace('href="assets/', 'href="../../assets/').replace('src="assets/', 'src="../../assets/')
    s = sub(s, '</head>', BAR_CSS + '\n</head>')
    s = sub(s, '<header class="header">', f'<div class="launch-bar">{bar}</div>\n<header class="header">')
    return s

# ---------------- pilot page ----------------
s = open(os.path.join(ROOT, 'pilot.html')).read()
s = common(s, '<b>Launching in Vienna in 2027.</b> We\'re not taking on work yet: register your interest and be among the first 10. <a href="#apply">Register ↗</a>')
s = sub(s, '<span>Pilot programme</span><span>10 places</span>', '<span>Launching 2027</span><span>10 places</span>')
s = sub(s, "We're choosing 10 restaurants, hotels and wellness &amp; beauty businesses (practices, salons, hairdressers, spas) to receive our Discovery Pack at no cost. Tell us about one real problem that costs you time every week. We pick the cases where AI or automation can make the clearest difference, spend a day with your team and give you a clear plan: which tools fix which problem, and what they cost.",
 "We're preparing to launch ImplementAI in Vienna in 2027. When we start, 10 restaurants, hotels and wellness &amp; beauty businesses (practices, salons, hairdressers, spas) will receive our Discovery Pack at no cost. Register your interest now and tell us about one real problem that costs you time every week. We'll pick the cases where AI or automation can make the clearest difference, spend a day with your team and give you a clear plan: which tools fix which problem, and what they cost.")
s = sub(s, '<span>free Discovery Packs,<br>chosen by real use case</span>', '<span>free Discovery Packs<br>when we launch</span>')
s = sub(s, '<strong>You describe a real pain</strong>', '<strong>You register a real pain</strong>')
s = sub(s, '<strong>We analyse it with you, free</strong>', '<strong>At launch, we analyse it with you, free</strong>')
s = sub(s, '<span class="tag">What the 10 get</span>', '<span class="tag">What the first 10 will get</span>')
s = sub(s, 'Normally <s>€1,490</s>, free for pilot clients', 'Planned price <s>€1,490</s>, free for the first 10')
s = s.replace('Describe your use case <span class="dot">↗</span>', 'Register your interest <span class="dot">↗</span>')
s = sub(s, '<span class="eyebrow"><b>02</b> Apply</span>', '<span class="eyebrow"><b>02</b> Register</span>')
s = sub(s, "You can describe up to two problems. We read every application ourselves and reply to everyone, whether or not you're selected.",
 "You can describe up to two problems. Registering is free and doesn't commit you to anything. We read every registration ourselves and get back to everyone before we launch.")
s = sub(s, """        <div><span class="av" style="background:var(--terra)">DS</span><span><b>Daniel Sheccoury</b>MSc Oxford · AI implementation</span></div>
        <div><span class="av" style="background:var(--olive)">TS</span><span><b>Dr. Tibor Sekera</b>PhD Physics · Data science</span></div>
        <div><span class="av" style="background:var(--forest)">JL</span><span><b>Jean Christophe Loeb</b>Senior Data Scientist · Agentic AI</span></div>""",
"""        <div><span class="av" style="background:var(--terra)">i.</span><span><b>The engineer</b>MSc, University of Oxford · AI integration and training</span></div>
        <div><span class="av" style="background:var(--olive)">ii.</span><span><b>The physicist</b>PhD Physics · Data science</span></div>
        <div><span class="av" style="background:var(--forest)">iii.</span><span><b>The agent builder</b>Senior Data Scientist · Agentic AI</span></div>""")
s = sub(s, """      <fieldset>
        <legend>A second pain (optional)</legend>""", """      <fieldset>
        <legend>After the free analysis</legend>
        <div><label for="pw">Would you consider paying us to set up the recommended tools and train your team (from €3,900)?</label><select id="pw" name="pay_intent" required><option value="">Choose…</option><option>Yes, if the plan makes sense</option><option>Maybe, it depends on the cost</option><option>No, the analysis is what I need</option></select><div class="hint">An honest answer helps us plan. It doesn't commit you to anything.</div></div>
      </fieldset>

      <fieldset>
        <legend>A second pain (optional)</legend>""")
s = sub(s, 'I agree that my details are used to assess this application. No newsletter, no spam.', 'I agree that my details are stored to contact me about the launch and the free Discovery Pack. No newsletter, no spam.')
s = sub(s, 'Send my application <span class="dot">↗</span>', 'Register my interest <span class="dot">↗</span>')
s = sub(s, "Thank you! We've received your application and sent you a confirmation email. We reply to every application within 2 working days.", "Thank you! We've received your registration and sent you a confirmation email. We'll be in touch before we launch.")
s = sub(s, '<h3>What we ask in return</h3>', '<h3>What we\'ll ask in return</h3>')
s = sub(s, '<h2>How we <i>choose</i> the 10.</h2>', '<h2>How we\'ll <i>choose</i> the 10.</h2>')
s = sub(s, '<span class="when">10 minutes</span><h3>You apply</h3><p>Describe one or two real problems using the form above.</p>', '<span class="when">Now, 10 minutes</span><h3>You register</h3><p>Describe one or two real problems using the form above.</p>')
s = sub(s, '<span class="when">30 minutes</span><h3>Short call</h3><p>For shortlisted applicants: a call to understand the problem better.</p>', '<span class="when">Before launch</span><h3>Short call</h3><p>For the most promising registrations: a 30-minute call to understand the problem better.</p>')
s = sub(s, '<span class="when">Then</span><h3>We start</h3><p>The 10 selected businesses are notified and we plan the on-site day together.</p>', '<span class="when">At launch, 2027</span><h3>We start</h3><p>The 10 selected businesses are notified and we plan the on-site day together.</p>')
s = sub(s, '<h2>Before you <i>apply</i>.</h2>', '<h2>Before you <i>register</i>.</h2>')
s = sub(s, "<details open><summary>Is it really free?</summary><p>Yes. The Discovery Pack normally costs €1,490; pilot clients pay nothing, and there's no obligation afterwards.</p></details>",
 "<details open><summary>When do you start?</summary><p>We're preparing to launch in Vienna in 2027 and are not taking on work yet. Registering now puts you first in line for the 10 free places. We'll contact you before we start.</p></details>\n      <details><summary>Is it really free?</summary><p>Yes. The Discovery Pack will cost €1,490; the first 10 businesses pay nothing, and there's no obligation afterwards.</p></details>")
s = sub(s, "<p>We're a new consultancy. We want real results from real businesses to show future clients, and honest feedback to improve how we work.</p>",
 "<p>We're three AI and data specialists preparing to start a consultancy. Before we launch, we want to understand which problems matter most to businesses like yours, and the first 10 projects will become our first case studies.</p>")
s = sub(s, "<details><summary>What if I'm not selected?</summary><p>We reply to everyone. If your problem is a good fit for AI, you can still book a free one-hour Quick-Check with us.</p></details>",
 "<details><summary>What if I'm not selected?</summary><p>We reply to everyone. If your problem is a good fit for AI, you'll be able to book a free one-hour Quick-Check once we've launched.</p></details>\n      <details><summary>Who is behind ImplementAI?</summary><p>An engineer with an MSc from the University of Oxford, a PhD physicist and a senior data scientist specialised in AI agents, based in Vienna. You'll meet us in person on the call and on the on-site day.</p></details>")
s = sub(s, "<p>We only use your application to assess it.", "<p>We only use your registration to contact you about the launch and to choose the 10. If we don't launch, we delete it.")
s = sub(s, '<a href="#">Imprint</a> · <a href="#">Privacy</a>', '<a href="../legal/imprint.html">Imprint</a> · <a href="../legal/privacy.html">Privacy</a>')
s = sub(s, 'Apply for a free Discovery Pack ↗', 'Register for a free Discovery Pack ↗')
s = sub(s, '<a href="#apply" class="btn btn-dark" style="padding:12px 20px">Apply now</a>', '<a href="#apply" class="btn btn-dark" style="padding:12px 20px">Register interest</a>')
open(os.path.join(HERE, 'pilot-interest.html'), 'w').write(s)

# ---------------- main page ----------------
s = open(os.path.join(ROOT, 'index.html')).read()
s = s.replace('href="assets/', 'href="../../assets/').replace('src="assets/', 'src="../../assets/')
s = sub(s, '<div class="announce">Now booking: free one-hour AI Quick-Checks for restaurants, hotels, wellness &amp; beauty — <a href="landing.html">reserve a slot →</a></div>',
        '<div class="announce">Launching in Vienna in 2027 — we\'re not taking on work yet. <a href="pilot-interest.html">Register your interest for one of 10 free Discovery Packs →</a></div>')
for i, (ini, name, role) in enumerate([('DS', 'Daniel Sheccoury', 'AI Implementation Consultant · MSc, University of Oxford'),
                                        ('TS', 'Dr. Tibor Sekera', 'Data Scientist · PhD in Physics'),
                                        ('JL', 'Jean Christophe Loeb', 'Senior Data Scientist · Agentic AI')]):
    new_name = ['The engineer', 'The physicist', 'The agent builder'][i]
    s = sub(s, f'<div class="portrait"><span>{ini}</span><em class="ph">Photo placeholder</em></div>\n        <h3>{name}</h3>',
            f'<div class="portrait"><span>{["MSc", "PhD", "AI"][i]}</span></div>\n        <h3>{new_name}</h3>')
s = sub(s, '<p class="reveal d1">Start with a free hour, then go one step at a time', '<p class="reveal d1">Planned prices from our launch in 2027. Start with a free hour, then go one step at a time')
s = sub(s, '<a href="#">Imprint</a>', '<a href="../legal/imprint.html">Imprint</a>')
s = sub(s, '<a href="#">Privacy</a>', '<a href="../legal/privacy.html">Privacy</a>')
open(os.path.join(HERE, 'index-anon.html'), 'w').write(s)
print('ok')
