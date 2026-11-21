"""Five ad copies built on Brendan Kane's Hook Point principles. Run: python3 hookpoint_copy.py -> ../HOOKPOINT-COPY.md"""
import pathlib
LIM = {"open": 125, "headline": 40, "desc": 30}
ADS = [
 dict(n=1, name="Flipped expectation", principle="Curiosity by flipping an expectation (Kane's \"WARNING! Safety Is Dangerous\" pattern), and it leads with what sets you apart: vendor-neutral, observe first.",
  visual="Big serif text on cream, nothing else: “Don't buy AI.” Small line below: “…until someone has found the problem worth fixing.”",
  en=dict(open="Don't buy AI. Not until someone has spent a day in your business and found the one problem worth fixing.",
          body="That's what we do. We watch how your restaurant, hotel or salon really runs, find the task that eats the most time, and give you a plan: which tool fixes it, and what it costs.\n\nWhen we launch in 2027, the first 10 Vienna businesses get this free (planned price €1,490). Register in 10 minutes. No obligation.",
          head="Don't buy AI. Yet.", desc="Free for the first 10"),
  de=dict(open="Kaufen Sie keine KI. Nicht bevor jemand einen Tag in Ihrem Betrieb war und das eine Problem gefunden hat, das sich lohnt.",
          body="Genau das machen wir. Wir sehen uns an, wie Ihr Restaurant, Hotel oder Salon wirklich läuft, finden die Aufgabe, die am meisten Zeit frisst, und geben Ihnen einen Plan: welches Tool sie löst und was es kostet.\n\nZum Start 2027 ist das für die ersten 10 Wiener Betriebe gratis (geplanter Preis € 1.490). Anmeldung in 10 Minuten, ohne Verpflichtung.",
          head="Kaufen Sie keine KI. Noch nicht.", desc="Gratis für die ersten 10")),
 dict(n=2, name="Say their problem better than they can", principle="Describe the pain so precisely that the reader feels understood (\"connects to the audience's needs or pain points and hints at a solution\").",
  visual="Phone screen at night, clock showing 23:40, a stack of unread booking requests, reviews and supplier emails. Text: “Your second shift starts at closing time.”",
  en=dict(open="23:40. Service is over. You're still answering booking requests, replying to reviews and ordering stock.",
          body="That second shift is the part a tool can take over. Tell us about it: when we launch in 2027, we analyse the 10 strongest cases free, with a day on-site and a written plan of which tools fix it and what they cost.\n\nFor restaurants, hotels and wellness & beauty businesses in Vienna. Register in 10 minutes.",
          head="Your second shift starts at closing", desc="Free analysis for 10"),
  de=dict(open="23:40 Uhr. Der Service ist vorbei. Sie beantworten noch Reservierungen, Bewertungen und bestellen Ware nach.",
          body="Diese zweite Schicht kann ein Tool übernehmen. Erzählen Sie uns davon: Zum Start 2027 analysieren wir die 10 stärksten Fälle gratis, mit einem Tag vor Ort und einem schriftlichen Plan, welche Tools helfen und was sie kosten.\n\nFür Gastronomie, Hotellerie sowie Wellness & Beauty in Wien. Anmeldung in 10 Minuten.",
          head="Ihre zweite Schicht beginnt um 23 Uhr", desc="Gratis-Analyse für 10")),
 dict(n=3, name="Insight with a number", principle="An eye-opening fact from a credible source (\"insight\" hook; data-driven hooks resonate most), followed straight by the question it raises.",
  visual="Huge “10h” in terracotta, under it a week bar with 10 hours shaded. Small source line: WKO survey 2024.",
  en=dict(open="Restaurants and hotels spend about 10 hours a week on paperwork (WKO survey, 2024). Which of those hours could go?",
          body="We find out, free, for 10 Vienna businesses when we launch in 2027: one day on-site, a list of the tasks a tool can take over, the tools to do it and their costs.\n\nNo AI knowledge needed. Register in 10 minutes, no obligation.",
          head="Which of your 10 admin hours can go?", desc="Free for the first 10"),
  de=dict(open="Gastronomie und Hotellerie: rund 10 Stunden pro Woche für Papierkram (WKO-Umfrage 2024). Welche davon können weg?",
          body="Das finden wir heraus, gratis für 10 Wiener Betriebe zum Start 2027: ein Tag vor Ort, eine Liste der Aufgaben, die ein Tool übernehmen kann, die passenden Tools und ihre Kosten.\n\nKein KI-Wissen nötig. Anmeldung in 10 Minuten, ohne Verpflichtung.",
          head="Welche Ihrer 10 Bürostunden können weg?", desc="Gratis für die ersten 10")),
 dict(n=4, name="One clear promise", principle="Clear, concise, instantly understandable, like \"No Late Fees\": the whole offer in a few words, and it delivers exactly what it says.",
  visual="Three large words stacked on dark green, each with a small icon: “One day. One problem. One plan.” Butter-yellow “Free for 10” stamp.",
  en=dict(open="One day. One problem. One plan. Free for 10 Vienna restaurants, hotels and wellness & beauty businesses.",
          body="We spend a day in your business, find the task that costs you the most time, and hand you a written plan: the AI tools that fix it, what they cost and how much time you could save. You keep the plan.\n\nLaunching in 2027 (planned price €1,490). Register now to be one of the first 10.",
          head="One day. One problem. One plan.", desc="Free for the first 10"),
  de=dict(open="Ein Tag. Ein Problem. Ein Plan. Gratis für 10 Wiener Restaurants, Hotels und Betriebe aus Wellness & Beauty.",
          body="Wir verbringen einen Tag in Ihrem Betrieb, finden die Aufgabe, die Sie am meisten Zeit kostet, und geben Ihnen einen schriftlichen Plan: die KI-Tools, die sie lösen, ihre Kosten und die mögliche Zeitersparnis. Der Plan gehört Ihnen.\n\nStart 2027 (geplanter Preis € 1.490). Jetzt anmelden und einer der ersten 10 sein.",
          head="Ein Tag. Ein Problem. Ein Plan.", desc="Gratis für die ersten 10")),
 dict(n=5, name="Familiar meets unexpected (personality)", principle="Blends the familiar with the unexpected, using the team as the hook (\"personality\" hook): a joke set-up people recognise, with a real, specific offer as the punchline.",
  visual="The three team photos in their coloured arches, standing in front of a restaurant counter or salon chair. Text: “…walk into your restaurant.”",
  en=dict(open="An Oxford engineer, a physicist and a data scientist walk into your restaurant. No joke: they want to fix your admin.",
          body="We're Daniel, Tibor and Jean Christophe. When we launch in 2027, we'll spend a day each with 10 Vienna restaurants, hotels and salons, find what eats your time, and show you which tools fix it and what they cost. Free for those 10.\n\nRegister in 10 minutes. We speak English, German, French and Slovak.",
          head="No joke: a free AI plan for 10", desc="Vienna · from 2027"),
  de=dict(open="Ein Oxford-Ingenieur, ein Physiker und ein Data Scientist kommen in Ihr Restaurant. Kein Witz: Sie wollen Ihnen Arbeit abnehmen.",
          body="Wir sind Daniel, Tibor und Jean Christophe. Zum Start 2027 verbringen wir je einen Tag mit 10 Wiener Restaurants, Hotels und Salons, finden heraus, was Ihre Zeit frisst, und zeigen Ihnen, welche Tools helfen und was sie kosten. Gratis für diese 10.\n\nAnmeldung in 10 Minuten. Wir sprechen Deutsch, Englisch, Französisch und Slowakisch.",
          head="Kein Witz: ein Gratis-KI-Plan für 10", desc="Wien · ab 2027")),
]
problems = []
out = ["# Five ads built on Hook Point (Brendan Kane)", "",
 "Generated by `ads/src/hookpoint_copy.py`. Character limits checked: opening line ≤ 125 (shown before \"See more\"), headline ≤ 40, description ≤ 30.", "",
 "**Principles used** (from Kane's interview with the National Association of Realtors, April 2026, and a summary of *Hook Point*): the first three seconds decide; the hook only has to earn the next 5–10 seconds, not sell; be clear, concise and instantly understandable; spark curiosity without confusing, often by flipping an expectation; describe the audience's pain and hint at the solution; blend the familiar with the unexpected; a hook sets an expectation and delivers it (otherwise it is clickbait); judge hooks by leads, not attention; test, because no hook is known to work before it is tested.", "",
 "**Button for all:** Sign up (DE: Registrieren). **Link:** the pilot page with `utm_content=hook6` … `hook10` (one per copy, so the Sheet shows which one works).", ""]
for a in ADS:
    out += [f"## {a['n']}. {a['name']}", "", f"*Why it should stop the scroll:* {a['principle']}", "", f"*Image idea (first 3 seconds):* {a['visual']}", ""]
    for lang in ("en", "de"):
        c = a[lang]
        for k, lim in (("open", "open"), ("head", "headline"), ("desc", "desc")):
            if len(c[k]) > LIM[lim]: problems.append(f"{a['n']} {lang} {k} {len(c[k])}")
        out += [f"**{'English' if lang == 'en' else 'German'}**", "", "Primary text:", "```", c["open"], "", c["body"], "```",
                f"- Headline: {c['head']} ({len(c['head'])})", f"- Description: {c['desc']}", f"- Opening line: {len(c['open'])} characters", ""]
pathlib.Path(__file__).parent.parent.joinpath("HOOKPOINT-COPY.md").write_text("\n".join(out))
print("problems:", problems or "none")
