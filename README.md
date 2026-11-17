# ImplementAI website

Static website for an AI implementation consultancy serving SMEs in gastronomy, hospitality and private health & beauty clinics.

- `index.html` — main company website (industries, services, process, packages, team, FAQ, contact)
- `landing.html` — conversion landing page for the free 30-minute "AI Quick-Check"
- `assets/styles.css`, `assets/main.js` — shared styles and scripts

No build step: open `index.html` in a browser, or deploy the folder to any static host (GitHub Pages, Netlify, Vercel).

## Before going live
- Replace placeholders: `[Your Name]` (team card initials "YN" too), `hello@implementai.example` (in both HTML files and `assets/main.js`).
- Add Imprint and Privacy policy pages (required in DE/AT/CH).
- Forms currently open the visitor's email app. To collect submissions directly, add `data-endpoint="https://formspree.io/f/…"` (or similar) to each `<form>`.
- Review the indicative prices and target metrics.
