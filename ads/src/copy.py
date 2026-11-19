"""Ad copy for the pilot programme. Run to regenerate ../AD-COPY.md with character counts checked."""
import pathlib
LIM = {"headline": 40, "description": 30, "hook": 125}
C = {
"English": {
 "primary": [
  ("Offer", "We're giving 10 Vienna restaurants, hotels and wellness & beauty businesses our AI Discovery Pack free (normally €1,490).",
   "Tell us one real problem that costs you time every week: missed booking calls, no-shows, rotas, endless emails. We pick the 10 strongest use cases and spend a day on-site with each. You get a written plan: your biggest time drains, the AI tools that fix them, what they cost and how much time you could save.\n\nApply in 10 minutes. No AI knowledge needed, no obligation afterwards."),
  ("Pain", "40 booking calls a week during dinner service, and a quarter go unanswered. That's the kind of problem we want to hear about.",
   "Describe your biggest daily headache. The 10 strongest use cases get our Discovery Pack free (normally €1,490): a day on-site, a map of your biggest pains, the right AI tools with their costs, and a walkthrough of the plan.\n\nWe read every application ourselves, and everyone gets a reply."),
  ("No risk", "Curious about AI but not sure where to start? Find out for free what it could do for your business.",
   "With our free Discovery Pack (normally €1,490) we spend a day in your business, then show you which ready-made tools, such as Microsoft Copilot or a booking chatbot, would fix your biggest problems and what they cost. The report is yours, with no obligation.\n\nWe work in English, German, French and Slovak."),
 ],
 "headline": ["10 free AI Discovery Packs", "Your AI plan, on us", "Tell us your biggest daily headache",
              "Free Discovery Pack for 10 businesses", "Less admin. More time for guests."],
 "description": ["Worth €1,490. Free for 10.", "Apply in 10 minutes", "A day on-site + written plan",
                 "No obligation afterwards", "English · Deutsch · FR · SK"],
 "cta": "Apply Now",
},
"German": {
 "primary": [
  ("Angebot", "Wir schenken 10 Wiener Restaurants, Hotels und Betrieben aus Wellness & Beauty unser KI-Analyse-Paket (regulär € 1.490).",
   "Erzählen Sie uns ein echtes Problem, das Sie jede Woche Zeit kostet: verpasste Reservierungsanrufe, No-Shows, Dienstpläne, endlose E-Mails. Wir wählen die 10 stärksten Anwendungsfälle und verbringen mit jedem Betrieb einen Tag vor Ort. Sie erhalten einen schriftlichen Plan: Ihre größten Zeitfresser, die passenden KI-Tools, ihre Kosten und die mögliche Zeitersparnis.\n\nBewerbung in 10 Minuten. Kein KI-Wissen nötig, danach keine Verpflichtung."),
  ("Problem", "40 Reservierungsanrufe pro Woche im Abendservice, ein Viertel bleibt unbeantwortet. Genau solche Probleme suchen wir.",
   "Beschreiben Sie Ihr größtes Alltagsproblem. Die 10 stärksten Anwendungsfälle erhalten unser Analyse-Paket gratis (regulär € 1.490): ein Tag vor Ort, eine Übersicht Ihrer größten Baustellen, die passenden KI-Tools mit Kosten und eine Besprechung des Plans.\n\nWir lesen jede Bewerbung selbst und antworten allen."),
  ("Ohne Risiko", "Neugierig auf KI, aber unsicher, wo Sie anfangen sollen? Finden Sie gratis heraus, was sie Ihrem Betrieb bringt.",
   "Mit unserem Gratis-Analyse-Paket (regulär € 1.490) verbringen wir einen Tag in Ihrem Betrieb und zeigen Ihnen dann, welche fertigen Tools, etwa Microsoft Copilot oder ein Reservierungs-Chatbot, Ihre größten Probleme lösen und was sie kosten. Der Bericht gehört Ihnen, ohne Verpflichtung.\n\nWir arbeiten auf Deutsch, Englisch, Französisch und Slowakisch."),
 ],
 "headline": ["10 gratis KI-Analyse-Pakete", "Ihr KI-Plan, auf uns", "Ihr Alltagsproblem, gratis analysiert",
              "Gratis Analyse-Paket für 10 Betriebe", "Weniger Papierkram, mehr Zeit für Gäste"],
 "description": ["Wert € 1.490, gratis für 10", "Bewerbung in 10 Minuten", "Ein Tag vor Ort + Plan",
                 "Danach keine Verpflichtung", "Deutsch · English · FR · SK"],
 "cta": "Jetzt bewerben (Apply Now)",
},
}
problems = []
out = ["# Facebook / Instagram ads: pilot programme", "",
       "Offer: free Discovery Pack (German: Analyse-Paket), normally €1,490: a day on-site, map of the biggest pains, recommended AI tools with licence costs, time-saving estimate, written report and walkthrough. For 10 selected businesses. Landing page: `pilot.html` / `de/pilot.html`.", "",
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
"- **Objective:** Leads with an Instant Form (lead form inside Facebook). Form settings, the connection to the applications Sheet and the follow-up process: `operations/SETUP.md`.",
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
"- Plan capacity: 10 free Discovery Packs are about 180 team hours by our estimate (about 60 hours each).",
]
pathlib.Path(__file__).parent.parent.joinpath("AD-COPY.md").write_text("\n".join(out) + "\n")
print("problems:", problems or "none")
