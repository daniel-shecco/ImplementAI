"""Single source for the pilot-programme emails.
Writes ../email-templates.md (to read and copy) and ../apps-script/Templates.gs (used by the script).
Placeholders: {{Name}} {{Business}} {{Problem}} {{SelectionWhen}} {{BookingSentence}} {{DiscoveryDate}} {{Signature}}
Run: python3 make_templates.py
"""
import json, pathlib
OUT = pathlib.Path(__file__).parent.parent

T = {
"pilot_confirmation": {
  "when": "Sent automatically when a pilot application arrives (status New → Confirmation sent).",
  "EN": ("Your application to the ImplementAI pilot programme",
"""Hello {{Name}},

Thank you for applying for one of our 10 free Discovery Packs. We have received your application for {{Business}}.

What happens next:
1. We read every application ourselves and reply within 2 working days.
2. If your use case is a good fit, we invite you to a 30-minute call to understand the problem better.
3. We choose the 10 businesses {{SelectionWhen}} and let every applicant know.

The problem you described:
"{{Problem}}"

If you would like to add anything, such as numbers or a second example, simply reply to this email.

{{Signature}}"""),
  "DE": ("Ihre Bewerbung für das ImplementAI-Pilotprogramm",
"""Guten Tag {{Name}},

danke für Ihre Bewerbung um eines unserer 10 kostenlosen Analyse-Pakete. Wir haben Ihre Bewerbung für {{Business}} erhalten.

So geht es weiter:
1. Wir lesen jede Bewerbung selbst und melden uns innerhalb von 2 Werktagen.
2. Wenn Ihr Anwendungsfall gut passt, laden wir Sie zu einem 30-minütigen Gespräch ein, um das Problem besser zu verstehen.
3. Wir wählen die 10 Betriebe {{SelectionWhen}} aus und informieren alle Bewerber:innen.

Das Problem, das Sie beschrieben haben:
„{{Problem}}“

Wenn Sie etwas ergänzen möchten, etwa Zahlen oder ein zweites Beispiel, antworten Sie einfach auf diese E-Mail.

{{Signature}}"""),
},
"pilot_more_info": {
  "when": "Draft for status Needs more info: the description is too vague to score.",
  "EN": ("A quick question about your application",
"""Hello {{Name}},

Thank you for your application for {{Business}}. To assess it fairly, we need a little more detail:

- How often does the problem happen, per day or per week?
- Roughly how much time or money does it cost you?
- Which software or tools do you use for it today?

A few lines are enough. Just reply to this email.

{{Signature}}"""),
  "DE": ("Eine kurze Frage zu Ihrer Bewerbung",
"""Guten Tag {{Name}},

danke für Ihre Bewerbung für {{Business}}. Damit wir sie fair beurteilen können, brauchen wir noch ein paar Details:

- Wie oft tritt das Problem auf, pro Tag oder pro Woche?
- Wie viel Zeit oder Geld kostet es Sie ungefähr?
- Welche Software oder Tools verwenden Sie dafür heute?

Ein paar Zeilen genügen. Antworten Sie einfach auf diese E-Mail.

{{Signature}}"""),
},
"pilot_shortlisted": {
  "when": "Draft for status Shortlisted: invite to a 30-minute call.",
  "EN": ("Your application is on our shortlist",
"""Hello {{Name}},

Good news: your application for {{Business}} is on our shortlist for the pilot programme.

Before we make the final choice, we would like to talk with you for 30 minutes, by video or in person in Vienna. We will ask about the problem you described, how your day runs and which tools you use today.

{{BookingSentence}}

{{Signature}}"""),
  "DE": ("Ihre Bewerbung ist in der engeren Auswahl",
"""Guten Tag {{Name}},

gute Nachrichten: Ihre Bewerbung für {{Business}} ist in der engeren Auswahl für unser Pilotprogramm.

Bevor wir endgültig entscheiden, möchten wir 30 Minuten mit Ihnen sprechen, per Video oder persönlich in Wien. Wir fragen nach dem Problem, das Sie beschrieben haben, nach Ihrem Arbeitsalltag und nach den Tools, die Sie heute verwenden.

{{BookingSentence}}

{{Signature}}"""),
},
"pilot_selected": {
  "when": "Draft for status Selected: the business is one of the 10.",
  "EN": ("You're one of our 10 pilot businesses",
"""Hello {{Name}},

We are happy to tell you that {{Business}} is one of the 10 businesses in our pilot programme. Your Discovery Pack is free of charge and comes with no obligation.

What happens now:
1. The on-site day: one of us spends a normal working day with your team, including a busy period. Please suggest two or three dates in the next few weeks.
2. The report: within 5 working days you receive a written plan with your biggest time drains, the AI tools that fix them, their licence costs and the time you could save.
3. The walkthrough: we go through the report together in a one-hour meeting.

To prepare, please name one contact person for the day and think of rough numbers for the problem you described (for example calls per week or hours spent).

We do not need any personal data of your guests, clients or patients for the analysis.

{{Signature}}"""),
  "DE": ("Sie sind einer unserer 10 Pilotbetriebe",
"""Guten Tag {{Name}},

wir freuen uns, Ihnen mitzuteilen, dass {{Business}} einer der 10 Betriebe in unserem Pilotprogramm ist. Ihr Analyse-Paket ist kostenlos und ohne Verpflichtung.

So geht es weiter:
1. Der Tag vor Ort: Eine:r von uns verbringt einen normalen Arbeitstag mit Ihrem Team, inklusive einer Stoßzeit. Bitte schlagen Sie zwei oder drei Termine in den nächsten Wochen vor.
2. Der Bericht: Innerhalb von 5 Werktagen erhalten Sie einen schriftlichen Plan mit Ihren größten Zeitfressern, den passenden KI-Tools, deren Lizenzkosten und der möglichen Zeitersparnis.
3. Die Besprechung: Wir gehen den Bericht in einem einstündigen Termin gemeinsam durch.

Zur Vorbereitung nennen Sie uns bitte eine Ansprechperson für den Tag und überlegen Sie grobe Zahlen zu Ihrem Problem (zum Beispiel Anrufe pro Woche oder aufgewendete Stunden).

Für die Analyse brauchen wir keine personenbezogenen Daten Ihrer Gäste, Kund:innen oder Patient:innen.

{{Signature}}"""),
},
"pilot_not_selected": {
  "when": "Draft for status Not selected.",
  "EN": ("Your application to the ImplementAI pilot programme",
"""Hello {{Name}},

Thank you for applying with {{Business}} and for taking the time to describe your problem.

We received many good applications and could only choose 10. This time your business is not among them. We chose a mix of industries and problems that ready-made AI tools can solve within a few weeks.

If you would still like to explore AI for your business, you can book a free one-hour Quick-Check with us at any time. Just reply to this email.

{{Signature}}"""),
  "DE": ("Ihre Bewerbung für das ImplementAI-Pilotprogramm",
"""Guten Tag {{Name}},

danke, dass Sie sich mit {{Business}} beworben und Ihr Problem so genau beschrieben haben.

Wir haben viele gute Bewerbungen erhalten und konnten nur 10 auswählen. Diesmal ist Ihr Betrieb nicht dabei. Wir haben eine Mischung aus Branchen und Problemen gewählt, die fertige KI-Tools innerhalb weniger Wochen lösen können.

Wenn Sie KI für Ihren Betrieb trotzdem ausloten möchten, können Sie jederzeit einen kostenlosen einstündigen Quick-Check mit uns vereinbaren. Antworten Sie einfach auf diese E-Mail.

{{Signature}}"""),
},
"discovery_prep": {
  "when": "Draft for status Discovery booked: confirms the on-site day (uses the Next step date).",
  "EN": ("Your Discovery day on {{DiscoveryDate}}",
"""Hello {{Name}},

We are looking forward to visiting {{Business}} on {{DiscoveryDate}}.

How the day runs:
- A 15-minute start with you and your contact person
- We observe the day, including a busy period, and talk briefly with your team
- A 15-minute wrap-up with first impressions

Please have ready, if possible:
- A list of the software you use (booking, POS, calendar, email, messaging)
- Rough numbers for the problem you described

We do not need any personal data of your guests, clients or patients, and we are happy to sign a confidentiality agreement.

{{Signature}}"""),
  "DE": ("Ihr Analyse-Tag am {{DiscoveryDate}}",
"""Guten Tag {{Name}},

wir freuen uns auf unseren Besuch bei {{Business}} am {{DiscoveryDate}}.

So läuft der Tag ab:
- 15 Minuten Start mit Ihnen und Ihrer Ansprechperson
- Wir beobachten den Tag, inklusive einer Stoßzeit, und sprechen kurz mit Ihrem Team
- 15 Minuten Abschluss mit ersten Eindrücken

Bitte halten Sie nach Möglichkeit bereit:
- Eine Liste der Software, die Sie verwenden (Reservierung, Kassa, Kalender, E-Mail, Messaging)
- Grobe Zahlen zu dem Problem, das Sie beschrieben haben

Wir brauchen keine personenbezogenen Daten Ihrer Gäste, Kund:innen oder Patient:innen und unterschreiben gerne eine Vertraulichkeitsvereinbarung.

{{Signature}}"""),
},
"enquiry_confirmation": {
  "when": "Sent automatically for Quick-Check and contact requests (Enquiries tab).",
  "EN": ("Thanks for getting in touch with ImplementAI",
"""Hello {{Name}},

Thank you for your message. We have received it and will reply within one working day with a few times for a free one-hour Quick-Check, in person in Vienna or by video.

If you would like to add anything in the meantime, simply reply to this email.

{{Signature}}"""),
  "DE": ("Danke für Ihre Nachricht an ImplementAI",
"""Guten Tag {{Name}},

danke für Ihre Nachricht. Wir haben sie erhalten und melden uns innerhalb eines Werktags mit Terminvorschlägen für einen kostenlosen einstündigen Quick-Check, persönlich in Wien oder per Video.

Wenn Sie in der Zwischenzeit etwas ergänzen möchten, antworten Sie einfach auf diese E-Mail.

{{Signature}}"""),
},
}

VARS = {
 "Signature": {"EN": "Kind regards,\nDaniel, Tibor and Jean Christoph\nImplementAI · Vienna",
               "DE": "Freundliche Grüße\nDaniel, Tibor und Jean Christoph\nImplementAI · Wien"},
}

# Markdown for people
md = ["# Email templates: pilot programme and enquiries", "",
      "Generated from `operations/src/make_templates.py`; edit the texts there and run it again, so the script and this file stay the same.", "",
      "**Placeholders** are filled in by the script:", "",
      "| Placeholder | Filled with |", "|---|---|",
      "| `{{Name}}`, `{{Business}}`, `{{Problem}}` | The applicant's answers |",
      "| `{{SelectionWhen}}` | \"by &lt;selection date&gt;\" from the script settings, or \"in the coming weeks\" if no date is set |",
      "| `{{BookingSentence}}` | A booking link from the settings, or a request to reply with two or three times |",
      "| `{{DiscoveryDate}}` | The Next step date of the row |",
      "| `{{Signature}}` | The team signature below |", ""]
md += ["**Signature (EN)**", "```", VARS["Signature"]["EN"], "```", "**Signature (DE)**", "```", VARS["Signature"]["DE"], "```", ""]
for i, (key, t) in enumerate(T.items(), 1):
    md += [f"## {i}. `{key}`", "", f"*{t['when']}*", ""]
    for lang in ("EN", "DE"):
        subj, body = t[lang]
        md += [f"**{ 'English' if lang=='EN' else 'German' }: subject** {subj}", "", "```", body, "```", ""]
(OUT / "email-templates.md").write_text("\n".join(md))

# Apps Script file
gs = ("// Generated by operations/src/make_templates.py. Edit the texts there, run it, and paste this file again.\n"
      "var TEMPLATES = " + json.dumps({k: {l: {"subject": v[l][0], "body": v[l][1]} for l in ("EN", "DE")} for k, v in T.items()}, ensure_ascii=False, indent=1) + ";\n"
      "var TEMPLATE_VARS = " + json.dumps(VARS, ensure_ascii=False, indent=1) + ";\n")
(OUT / "apps-script" / "Templates.gs").write_text(gs)
print("ok", len(T), "templates")
