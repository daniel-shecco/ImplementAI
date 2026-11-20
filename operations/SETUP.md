# Applications: how it works and how to set it up

## How it works

```
Website form (pilot, Quick-Check, contact)
   └─► Apps Script web app ─► Google Sheet "ImplementAI – Pilot applications"
                                 ├─ pilot ─► tab Applicants
                                 └─ other ─► tab Enquiries
                              └─► confirmation email, straight away (English or German)

Facebook/Instagram ad ─► website pilot page ─► Sheet automatically (hook from the link)

Instant form (optional) ─► download from Meta Leads Center once a day ─► paste into Applicants (Status "New")
                                 └─► confirmation email within 10 minutes (the script checks every 10 minutes)

Team ─► scores and sets the status in the Sheet ─► menu "ImplementAI › Create email draft" ─► Gmail draft ─► check and send
```

- Sheet: https://docs.google.com/spreadsheets/d/1rBI76hgVDs0AlgDZo-9r6d9259FILZjBvhjEaBE-X7A/edit
- Script: `operations/apps-script/Code.gs` and `operations/apps-script/Templates.gs`
- Email texts: `operations/email-templates.md` (edit them in `operations/src/make_templates.py`, then run `python3 operations/src/make_templates.py`)
- Website: `assets/site.js` sends the forms to the script. Until the script's address is filled in there, forms fall back to opening the visitor's email app.

## One-time setup (about 20 minutes)

Do this with the Google account that should send the emails. Ideally that is the account of your business address (for example a Google Workspace account for `hello@…`). Until then, your own account works and replies can still go to the business address (`REPLY_TO`).

1. **Open the Sheet** and choose **Extensions › Apps Script**.
2. **Paste the code.** Replace the contents of `Code.gs` with `operations/apps-script/Code.gs`. Click **+ › Script**, name it `Templates`, and paste `operations/apps-script/Templates.gs`. Save.
3. **Fill in the settings** at the top of `Code.gs`:
   - `REPLY_TO`: the business email address (to follow).
   - `SELECTION_DATE_EN` / `SELECTION_DATE_DE`: the date you will choose the 10, for example `15 December` / `15. Dezember`.
   - `BOOKING_LINK` (optional): a booking page for the 30-minute calls. Without it, the email asks applicants to reply with times.
   - `NOTIFY_TEAM` (optional): your three addresses, separated by commas, for a short notice per new application.
4. **Turn on automatic confirmations:** choose the function `setup` and click **Run**. Google asks for permission (Sheets and Gmail). Because this is your own script, Google shows "unverified app": click **Advanced › Go to … (unsafe)** and allow.
5. **Test it:** run `testWebsiteApplication`. A test row appears in Applicants and you receive the confirmation email. Delete the test row afterwards.
6. **Publish the web app:** **Deploy › New deployment › Web app**. Execute as: **Me**. Who has access: **Anyone**. Deploy and copy the URL ending in `/exec`.
7. **Connect the website:** paste the URL into `FORM_ENDPOINT` in `assets/site.js` (or send it to Claude), then run `python3 build.py`.
8. **Reload the Sheet.** The **ImplementAI** menu appears next to Help.
9. **Delete the two example rows** (row 2 in Applicants and in Enquiries) before the first real application.

Sending limits: about 100 emails a day from a free Gmail account, 1,500 from Google Workspace. That is plenty for the pilot.

## Facebook lead form

Run the ads with a lead form (Objective: Leads, Instant Form), so people can apply inside Facebook. Settings:

| Setting | Value |
|---|---|
| Form type | Higher intent (adds a review step, fewer but better applications) |
| Intro headline | EN: "Your biggest daily headache, analysed free" · DE: "Ihr größtes Alltagsproblem, kostenlos analysiert" |
| Status line (first line of the intro) | EN: "Launching in Vienna in 2027. Register your interest now." · DE: "Start in Wien 2027. Jetzt Interesse anmelden." |
| Intro text | EN: "When we launch, 10 businesses get our Discovery Pack free (planned price €1,490). Describe one real problem that costs you time every week." · DE: "Zum Start erhalten 10 Betriebe unser Analyse-Paket gratis (geplanter Preis € 1.490). Beschreiben Sie ein echtes Problem, das Sie jede Woche Zeit kostet." |
| Prefilled questions | Full name, Email, Phone (optional) |
| Custom questions | Business name (short answer) · Industry (multiple choice: Gastronomy, Hospitality, Wellness & Beauty, Other) · Team size (multiple choice: 1–10, 11–50, 51–250) · What's the problem? · How often does it happen? · Who deals with it? · What does it cost you? (all short answer) · When would you like this problem solved? (multiple choice: As soon as possible, In the next 3 months, This year, Just curious for now) · Reserve my founding-client benefits: first in line when we start, a free follow-up visit 3 months after the analysis, a founding-client rate for later implementation (multiple choice: Yes, No) |
| Privacy policy | Link to your privacy policy page. **Required by Facebook; the website page is still a placeholder.** |
| Thank-you screen | EN: "Thank you! Check your inbox: we've sent you a confirmation. We'll be in touch before we launch." · DE: "Danke! Wir haben Ihnen eine Bestätigung per E-Mail geschickt und melden uns vor unserem Start." |

Use one form per language (EN and DE), so the confirmation goes out in the right language.

**Getting Facebook applications into the Sheet** (no Zapier or Make):

- **Chosen for the interest test: Traffic ads linking to the website pilot page** (full setup in `ads/CAMPAIGN.md`). Registrations go straight into the Sheet with the hook. If you later add Instant forms: in Meta Business Suite › Leads Center, download the leads as CSV once a day and paste them into Applicants, using the column values below with Status "New". The script sends the confirmation within 10 minutes. Leads stay downloadable in Meta for 90 days.

| Applicants column | Value |
|---|---|
| ID | `FB-` followed by the lead ID |
| Received | Lead created time |
| Source | `Facebook` (fixed) |
| Language | `EN` or `DE` (fixed, per form) |
| Name, Email, Phone | From the lead |
| Business, Industry, Team size | Custom answers |
| Problem, How often, Who deals with it, What it costs | Custom answers |
| Timing, Founding benefits | Custom answers (always store the English wording: As soon as possible / In the next 3 months / This year / Just curious for now, and Yes / No) |
| Hook (ad) | `Hook 1` … `Hook 5`: name each ad after its hook (for example "Hook 3 – More time for clients") and map the ad name, or use one form per hook |
| Status | `New` (fixed) |

When the website is online, link the ads to `pilot.html?utm_source=facebook&utm_medium=paid&utm_campaign=pilot` (German: `de/pilot.html?...`). Website applications from the ads are then marked "Facebook" in the Source column.

Give each hook ad its own link so the Sheet records which ad brought each registration (column Hook, and the "Registrations by hook" table on the Overview): `pilot.html?utm_source=facebook&utm_medium=paid&utm_campaign=pilot&utm_content=hook1` … `hook5`. Compare hooks by strong leads, not by clicks.

## The process

| When | What | Status in the Sheet | Email |
|---|---|---|---|
| Straight away | Confirmation | New › Confirmation sent | Automatic: `pilot_confirmation` |
| Within 2 working days | Pick an owner, score 1–5 per criterion (Scoring guide tab) | Needs more info, Shortlisted or Not selected | Drafts: `pilot_more_info`, `pilot_shortlisted` |
| Within a week of shortlisting | 30-minute call | Call booked | Calendar invitation |
| By the selection date | Choose the 10, mixing the three industries | Selected or Not selected | Drafts: `pilot_selected`, `pilot_not_selected` |
| After selection | Book the on-site day (enter it as Next step date) | Discovery booked | Draft: `discovery_prep` |
| On-site day + 5 working days | Report, then one-hour walkthrough | Discovery done | Ask for feedback and, if agreed, a quote for the case study |

The Overview tab shows places left, applications by status, industry and source, and how many reach the shortlist threshold.

**Interest test (go / no-go).** The Overview also counts urgent registrations (as soon as possible or within 3 months), founding benefits reserved, and strong leads (both). The go target (5 strong leads by default) is an input you can change. Agree on it with the team before the ads start.

## Still open

- **Business email address.** Fill it into `REPLY_TO` in the script and `EMAIL` in `assets/site.js` (used only if sending fails).
- **Privacy policy page.** Required for the Facebook lead form. It should say that form answers are stored in Google Sheets and used only to assess the application, and how long they are kept (suggestion: delete applications that were not selected after 6 months).
- **Selection date**, and optionally a booking link for the calls.
