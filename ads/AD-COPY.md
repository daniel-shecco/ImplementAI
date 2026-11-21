# Facebook / Instagram ads: pilot programme

Interest test before the launch in 2027: people register interest; nothing is sold or delivered yet. Offer at launch: free Discovery Pack (German: Analyse-Paket), planned price €1,490: a day on-site, map of the biggest pains, recommended AI tools with licence costs, time-saving estimate, written report and walkthrough. For the first 10 selected businesses. Landing page: `pilot.html` / `de/pilot.html`.

Character counts are checked by `ads/src/copy.py`. Limits: headline ≤ 40, description ≤ 30, first part of primary text ≤ 125 (shown before "See more").

## English

### Primary text (3 variants)

**Offer** (opening line: 116 characters)

```
Launching in Vienna in 2027: 10 restaurants, hotels and wellness & beauty businesses get our AI Discovery Pack free.

Register your interest now and tell us one real problem that costs you time every week: missed booking calls, no-shows, rotas, endless emails. When we launch, we pick the 10 strongest use cases and spend a day on-site with each. You get a written plan: your biggest time drains, the AI tools that fix them, what they cost and how much time you could save.

Registering takes 2 minutes. No AI knowledge needed, no obligation. Planned price €1,490, free for the first 10.
```

**Pain** (opening line: 125 characters)

```
40 booking calls a week during dinner service, and a quarter go unanswered. That's the kind of problem we want to hear about.

Describe your biggest daily headache. When we launch in 2027, the 10 strongest use cases get our Discovery Pack free (planned price €1,490): a day on-site, a map of your biggest pains, the right AI tools with their costs, and a walkthrough of the plan.

We read every registration ourselves, and everyone gets a reply.
```

**No risk** (opening line: 99 characters)

```
Curious about AI but not sure where to start? Find out for free what it could do for your business.

When we launch in 2027, our Discovery Pack (planned price €1,490) is free for the first 10 businesses. We spend a day in your business, then show you which ready-made tools, such as Microsoft Copilot or a booking chatbot, would fix your biggest problems and what they cost. The report is yours, with no obligation.

Register your interest now. We work in English, German, French and Slovak.
```

### Headlines

| # | Text | Characters |
|---|---|---|
| 1 | 10 free AI Discovery Packs | 26 |
| 2 | Your AI plan, on us | 19 |
| 3 | Tell us your biggest daily headache | 35 |
| 4 | Launching 2027: 10 free places | 30 |
| 5 | Less admin. More time for guests. | 33 |

### Descriptions

| # | Text | Characters |
|---|---|---|
| 1 | Planned €1,490. Free for 10. | 28 |
| 2 | Register in 2 minutes | 21 |
| 3 | A day on-site + written plan | 28 |
| 4 | No obligation | 13 |
| 5 | English · Deutsch · FR · SK | 27 |

**Button:** Sign Up (Meta has no "Register interest" button; the image and landing page say it)

## German

### Primary text (3 variants)

**Angebot** (opening line: 117 characters)

```
Start in Wien 2027: 10 Restaurants, Hotels und Betriebe aus Wellness & Beauty erhalten unser KI-Analyse-Paket gratis.

Melden Sie jetzt Ihr Interesse an und erzählen Sie uns ein echtes Problem, das Sie jede Woche Zeit kostet: verpasste Reservierungsanrufe, No-Shows, Dienstpläne, endlose E-Mails. Zum Start wählen wir die 10 stärksten Anwendungsfälle und verbringen mit jedem Betrieb einen Tag vor Ort. Sie erhalten einen schriftlichen Plan: Ihre größten Zeitfresser, die passenden KI-Tools, ihre Kosten und die mögliche Zeitersparnis.

Anmeldung in 2 Minuten. Kein KI-Wissen nötig, keine Verpflichtung. Geplanter Preis € 1.490, für die ersten 10 gratis.
```

**Problem** (opening line: 117 characters)

```
40 Reservierungsanrufe pro Woche im Abendservice, ein Viertel bleibt unbeantwortet. Genau solche Probleme suchen wir.

Beschreiben Sie Ihr größtes Alltagsproblem. Zum Start 2027 erhalten die 10 stärksten Anwendungsfälle unser Analyse-Paket gratis (geplanter Preis € 1.490): ein Tag vor Ort, eine Übersicht Ihrer größten Baustellen, die passenden KI-Tools mit Kosten und eine Besprechung des Plans.

Wir lesen jede Anmeldung selbst und antworten allen.
```

**Ohne Risiko** (opening line: 112 characters)

```
Neugierig auf KI, aber unsicher, wo Sie anfangen sollen? Finden Sie gratis heraus, was sie Ihrem Betrieb bringt.

Zum Start 2027 ist unser Analyse-Paket (geplanter Preis € 1.490) für die ersten 10 Betriebe gratis. Wir verbringen einen Tag in Ihrem Betrieb und zeigen Ihnen dann, welche fertigen Tools, etwa Microsoft Copilot oder ein Reservierungs-Chatbot, Ihre größten Probleme lösen und was sie kosten. Der Bericht gehört Ihnen, ohne Verpflichtung.

Melden Sie jetzt Ihr Interesse an. Wir arbeiten auf Deutsch, Englisch, Französisch und Slowakisch.
```

### Headlines

| # | Text | Characters |
|---|---|---|
| 1 | 10 gratis KI-Analyse-Pakete | 27 |
| 2 | Ihr KI-Plan, auf uns | 20 |
| 3 | Ihr Alltagsproblem, gratis analysiert | 37 |
| 4 | Start 2027: 10 Gratis-Plätze | 28 |
| 5 | Weniger Papierkram, mehr Zeit für Gäste | 39 |

### Descriptions

| # | Text | Characters |
|---|---|---|
| 1 | Geplant € 1.490, gratis für 10 | 30 |
| 2 | Anmeldung in 2 Minuten | 22 |
| 3 | Ein Tag vor Ort + Plan | 22 |
| 4 | Ohne Verpflichtung | 18 |
| 5 | Deutsch · English · FR · SK | 27 |

**Button:** Registrieren (Sign Up)

## Hook ads (`ads/images/hooks/`)

Five hooks to test against each other. Pair each image with its opening line; the rest of the primary text can be any variant above.

### English

| Hook | Opening line | Characters |
|---|---|---|
| 1 Ten hours | Restaurants and hotels spend about 10 hours a week on paperwork (WKO survey, 2024). How much could a tool take over? | 116 |
| 2 Sound familiar | The phone rings mid-service, no-shows again, the rota takes all evening? Tell us. 10 businesses get it analysed free. | 117 |
| 3 More time for clients | Less time at the desk, more time for clients. We find the admin a tool can take off your plate, free for 10 businesses. | 119 |
| 4 Founding places | Only 10 founding places in Vienna: a free AI analysis (planned €1,490), first in line when we launch in 2027. | 109 |
| 5 Three in ten | 3 in 10 Austrian businesses already use AI (Statistik Austria, 2025). Start with the right tools, not the hype. | 111 |

### German

| Hook | Opening line | Characters |
|---|---|---|
| 1 Zehn Stunden | Gastronomie und Hotellerie: rund 10 Stunden pro Woche für Papierkram (WKO-Umfrage 2024). Wie viel kann ein Tool übernehmen? | 123 |
| 2 Bekannt | Das Telefon läutet mitten im Service, schon wieder No-Shows? Erzählen Sie es uns. 10 Betriebe bekommen es gratis analysiert. | 124 |
| 3 Mehr Zeit | Weniger Zeit am Schreibtisch, mehr Zeit für Ihre Kund:innen. Wir finden, was ein Tool Ihnen abnimmt, gratis für 10 Betriebe. | 124 |
| 4 Gründungsplätze | Nur 10 Gründungsplätze in Wien: Gratis-KI-Analyse (geplant € 1.490), als Erste an der Reihe zum Start 2027. | 107 |
| 5 Drei von zehn | 3 von 10 Betrieben in Österreich nutzen bereits KI (Statistik Austria, 2025). Starten Sie mit den richtigen Tools. | 114 |

Files: `{en,de}-{1-ten-hours,2-sound-familiar,3-more-time-for-clients,4-founding-places,5-three-in-ten}-{feed,story}.png`.

**Links:** give each hook ad its own link, ending in `utm_content=hook1` … `hook5`, for example `pilot.html?utm_source=facebook&utm_medium=paid&utm_campaign=pilot&utm_content=hook3` (German: `de/pilot.html?...`). The Sheet then shows registrations, founding benefits and strong leads per hook (Overview tab).

## Images (`ads/images/`)

| Concept | Feed 4:5 (1080×1350) | Stories/Reels 9:16 (1080×1920) |
|---|---|---|
| Offer: big 10 (EN) | `en-offer-feed.png` | `en-offer-story.png` |
| Pain: real use case (EN) | `en-pain-feed.png` | `en-pain-story.png` |
| Industries: three arches (EN) | `en-industries-feed.png` | `en-industries-story.png` |
| Offer: big 10 (DE) | `de-offer-feed.png` | `de-offer-story.png` |
| Pain: real use case (DE) | `de-pain-feed.png` | `de-pain-story.png` |
| Industries: three arches (DE) | `de-industries-feed.png` | `de-industries-story.png` |

Stories images keep text out of the top 250 px and bottom 360 px, which the Stories interface covers.

## Suggested setup

- **Objective:** Leads or Traffic, with the website pilot page as destination (each hook with its own link). Registrations then go straight into the Sheet; no Zapier or Make needed. An Instant Form is optional; its leads are downloaded from Meta Leads Center by hand. Details: `operations/SETUP.md`.
- **Instant Form type:** "Higher intent" (adds a review step, so fewer but better registrations).
- **Custom questions** (same as the pilot page): business name; industry (Gastronomy / Hospitality / Wellness & Beauty); team size; software used today; *What's the problem?*; *How often does it happen?*; *Who deals with it?*; *What does it cost you?*; *When would you like this problem solved?*; *Reserve my founding-client benefits* (Yes / No)
- **Location:** Vienna + about 20 km. **Languages:** create the German ads for German speakers and the English ads for everyone else.
- **Audience:** start broad (Advantage+ audience) with age 25–65; the creatives and questions filter for business owners.
- **Placements:** Facebook and Instagram feeds (4:5) and Stories/Reels (9:16).
- **Test:** run the 3 concepts side by side for 7–10 days at a small daily budget, then keep the best one.

## Before launch

- A Facebook Page and a Meta Business account for ImplementAI.
- A **privacy policy URL**: Instant Forms require one. Use the site's privacy page once the website is online and its placeholders (address, hosting provider) are filled in.
- Agree the go / no-go target with the team before the ads start (Overview tab of the Sheet).
- Do not deliver any Discovery or Quick-Check before the business and trade licence are registered.
