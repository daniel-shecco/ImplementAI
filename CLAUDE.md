# Working process for this project

## Design: mock first, build second
- Before building or changing anything visual (logos, pages, page sections, ads, slides, images), first show a mock-up for approval.
- For open design questions, show several options side by side (for example 3–5 versions) and let Daniel choose.
- Only after a version is approved: build it properly, roll it out to the site, ads, deck etc., and commit.
- Keep mock-ups in `mocks/` (or the relevant folder's `mocks/` subfolder), separate from production files.

## Project basics
- Site: static HTML. Main design is "Atelier" (root `index.html`, `landing.html`, `pilot.html`, German versions in `de/`). Shared styles in `assets/style.css`, behaviour in `assets/site.js`.
- `python3 build.py` bundles every page into self-contained files in `standalone/`.
- Target industries are named "Gastronomy · Hospitality · Wellness & Beauty" (German: "Gastronomie · Hotellerie · Wellness & Beauty").
- The free pilot offer is called "Starter Pack" (German: "Starter-Paket").
- The site is private and not published; do not deploy without explicit approval.
