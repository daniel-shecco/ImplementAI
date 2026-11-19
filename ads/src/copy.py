"""Ad copy for the pilot programme. Run to regenerate ../AD-COPY.md with character counts checked."""
import pathlib
LIM = {"headline": 40, "description": 30, "hook": 125}
C = {
"English": {
 "primary": [
  ("Offer", "We're giving 10 Vienna restaurants, hotels and wellness & beauty businesses our AI Starter package free (normally €3,900).",
   "Tell us one real problem that costs you time every week: missed booking calls, no-shows, rotas, endless emails. We pick the 10 strongest use cases, set up the right tools and train your team until it runs without us.\n\nApply in 10 minutes. No AI knowledge needed."),
  ("Pain", "40 booking calls a week during dinner service, and a quarter go unanswered. That's the kind of problem we want to hear about.",
   "Describe your biggest daily headache. We'll choose 10 businesses and solve it with them for free: setup, training and 30 days of help.\n\nWe read every application ourselves, and everyone gets a reply."),
  ("No risk", "Curious about AI but not sure where to start? Start with one problem, and let us solve it for free.",
   "In our pilot programme we set up ready-made tools such as Microsoft Copilot or a booking chatbot for 10 businesses, train the team and step back. Every tool stays in your name. No subscription.\n\nWe work in English, German, French and Slovak."),
 ],
 "headline": ["10 free AI Starter packs", "Your first AI project, on us", "Tell us your biggest daily headache",
              "Free AI setup for 10 Vienna businesses", "Less admin. More time for guests."],
 "description": ["Worth €3,900. Free for 10.", "Apply in 10 minutes", "Setup, training, 30 days help",
                 "No AI knowledge needed", "English · Deutsch · FR · SK"],
 "cta": "Apply Now",
},
"German": {
 "primary": [
  ("Angebot", "Wir schenken 10 Wiener Restaurants, Hotels und Betrieben aus Wellness & Beauty unser KI-Starter-Paket (regulär € 3.900).",
   "Erzählen Sie uns ein echtes Problem, das Sie jede Woche Zeit kostet: verpasste Reservierungsanrufe, No-Shows, Dienstpläne, endlose E-Mails. Wir wählen die 10 stärksten Anwendungsfälle, richten die passenden Tools ein und schulen Ihr Team, bis alles ohne uns läuft.\n\nBewerbung in 10 Minuten. Kein KI-Wissen nötig."),
  ("Problem", "40 Reservierungsanrufe pro Woche im Abendservice, ein Viertel bleibt unbeantwortet. Genau solche Probleme suchen wir.",
   "Beschreiben Sie Ihr größtes Alltagsproblem. Wir wählen 10 Betriebe aus und lösen es gemeinsam mit ihnen, kostenlos: Einrichtung, Schulung und 30 Tage Unterstützung.\n\nWir lesen jede Bewerbung selbst und antworten allen."),
  ("Ohne Risiko", "Neugierig auf KI, aber unsicher, wo Sie anfangen sollen? Beginnen Sie mit einem Problem, wir lösen es gratis.",
   "Im Pilotprogramm richten wir für 10 Betriebe fertige Tools wie Microsoft Copilot oder einen Reservierungs-Chatbot ein, schulen das Team und ziehen uns zurück. Alle Tools laufen auf Ihren Namen. Kein Abo.\n\nWir arbeiten auf Deutsch, Englisch, Französisch und Slowakisch."),
 ],
 "headline": ["10 gratis KI-Starter-Pakete", "Ihr erstes KI-Projekt, auf uns", "Ihr Alltagsproblem, gratis gelöst",
              "Gratis KI-Einrichtung für 10 Betriebe", "Weniger Papierkram, mehr Zeit für Gäste"],
 "description": ["Wert € 3.900, gratis für 10", "Bewerbung in 10 Minuten", "Einrichtung, Schulung, Support",
                 "Kein KI-Wissen nötig", "Deutsch · English · FR · SK"],
 "cta": "Jetzt bewerben (Apply Now)",
},
}
problems = []
out = ["# Facebook / Instagram ads: pilot programme", "",
       "Offer: free Starter package (normally €3,900) for 10 selected businesses. Landing page: `pilot.html` / `de/pilot.html`.", "",
       "Character counts are checked by `ads/src/copy.py`. Limits: headline ≤ 40, description ≤ 30, first part of primary text ≤ 125 (shown before \"See more\").", ""]
for lang, c in C.items():
    out += [f"## {lang}", "", "### Primary text (3 variants)", ""]
    for name, hook, body in c["primary"]:
        n = len(hook)
        if n > LIM["hook"]: problems.append(f"{lang} hook '{name}' {n}")
        out += [f"**{name}** (opening line: {n} characters)", "", "```", hook, "", body, "```", ""]
    for kind in ("headline", "description"):
        out += [f"### {kind.capitalize()}s", "", "| # | Text | Characters |", "|---|---|---|"]
        for i, h in enumerate(c[kind], 1):
            if len(h) > LIM[kind]: problems.append(f"{lang} {kind} '{h}' {len(h)}")
            out.append(f"| {i} | {h} | {len(h)} |")
        out.append("")
    out += [f"**Button:** {c['cta']}", ""]
out += ["## Images (`ads/images/`)", "",
        "| Concept | Feed 4:5 (1080×1350) | Stories/Reels 9:16 (1080×1920) |", "|---|---|---|"]
for lang in ("en", "de"):
    for cn, label in (("offer", "Offer: big 10"), ("pain", "Pain: real use case"), ("industries", "Industries: three arches")):
        out.append(f"| {label} ({lang.upper()}) | `{lang}-{cn}-feed.png` | `{lang}-{cn}-story.png` |")
out += ["", "Stories images keep text out of the top 250 px and bottom 360 px, which the Stories interface covers.", "",
"## Suggested setup", "",
"- **Objective:** Leads. Use an Instant Form (lead form inside Facebook), because the website is not online yet. Switch to the landing page later.",
"- **Instant Form type:** \"Higher intent\" (adds a review step, so fewer but better applications).",
"- **Custom questions** (same as the pilot page): business name; industry (Gastronomy / Hospitality / Wellness & Beauty); team size; software used today; *What's the problem?*; *How often does it happen?*; *Who deals with it?*; *What does it cost you?*",
"- **Location:** Vienna + about 20 km. **Languages:** create the German ads for German speakers and the English ads for everyone else.",
"- **Audience:** start broad (Advantage+ audience) with age 25–65; the creatives and questions filter for business owners.",
"- **Placements:** Facebook and Instagram feeds (4:5) and Stories/Reels (9:16).",
"- **Test:** run the 3 concepts side by side for 7–10 days at a small daily budget, then keep the best one.",
"", "## Before launch", "",
"- A Facebook Page and a Meta Business account for ImplementAI.",
"- A **privacy policy URL**: Instant Forms require one. The website's privacy page is still a placeholder.",
"- Decide the deadline and whether the offer is Vienna-only, and add both to the pilot page.",
"- Plan capacity: 10 free Starter packs are about 640 team hours by our estimate.",
]
pathlib.Path(__file__).parent.parent.joinpath("AD-COPY.md").write_text("\n".join(out) + "\n")
print("problems:", problems or "none")
