# ImplementAI website

Website for an AI implementation consultancy serving SMEs in gastronomy, hospitality and private health & beauty clinics.

## Live site (Atelier design)
- `index.html` — main website (English)
- `landing.html` — landing page for the free one-hour "AI Quick-Check" (English)
- `pilot.html` — pilot programme: free Starter pack for 10 selected businesses, with a use-case application form
- `de/index.html`, `de/landing.html`, `de/pilot.html` — German (Austrian) versions; every page has an EN/DE switch
- `assets/style.css`, `assets/site.js`, `assets/img/` (when added) — styles, behaviour, images

No build step: deploy the repository root to any static host (GitHub Pages, Netlify, Vercel).

## Standalone single-file HTML
`standalone/` contains every page bundled into one self-contained `.html` file (CSS, JS and images inlined; links between website and landing page rewritten). Regenerate after edits:

```
python3 build.py
```

- `implementai-website.html`, `implementai-landing.html` — the chosen Atelier design (English)
- `implementai-website-de.html`, `implementai-landing-de.html` — German versions
- `implementai-pilot.html`, `implementai-pilot-de.html` — pilot programme page (English, German)
- `midnight-*.html`, `classic-*.html` — alternative design directions (sources in `designs/`)

## Before going live
- Replace `hello@implementai.example` (in the English and German pages and `assets/site.js`).
- Add team photos: put them in `assets/img/` and add `<img src="assets/img/name.jpg" alt="…">` inside each `.portrait` (add class `has-photo`); styles are ready.
- Add Imprint and Privacy policy pages (required in DE/AT/CH).
- Forms currently open the visitor's email app. To collect submissions directly, add `data-endpoint="https://formspree.io/f/…"` (or similar) to each `<form>`.
- Review the indicative prices and target metrics.

## Applications and emails
`operations/` holds the application workflow: the Google Sheet tracker, the Apps Script that receives the website forms and sends confirmations (`operations/apps-script/`), the email templates (`operations/email-templates.md`) and the setup guide (`operations/SETUP.md`).
