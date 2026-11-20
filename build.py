#!/usr/bin/env python3
"""Bundle each page into a single self-contained HTML file in standalone/.

CSS, JS and images are inlined, and links between the home and landing page are rewritten
so the bundled files still link to each other. Fonts (assets/fonts) are inlined as data URIs.
Run: python3 build.py
"""
import base64
import mimetypes
import re
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "standalone"

# (source page, output name, {original href -> bundled href})
PAGES = [
    ("index.html",      "implementai-website.html",    {"imprint.html": "implementai-imprint.html", "privacy.html": "implementai-privacy.html",
                                                        "landing.html": "implementai-landing.html",
                                                        "de/index.html": "implementai-website-de.html",
                                                        "de/landing.html": "implementai-landing-de.html",
                                                        "pilot.html": "implementai-pilot.html"}),
    ("landing.html",    "implementai-landing.html",    {"imprint.html": "implementai-imprint.html", "privacy.html": "implementai-privacy.html",
                                                        "index.html": "implementai-website.html",
                                                        "de/index.html": "implementai-website-de.html",
                                                        "de/landing.html": "implementai-landing-de.html"}),
    ("de/index.html",   "implementai-website-de.html", {"impressum.html": "implementai-impressum.html", "datenschutz.html": "implementai-datenschutz.html",
                                                        "landing.html": "implementai-landing-de.html",
                                                        "pilot.html": "implementai-pilot-de.html",
                                                        "../index.html": "implementai-website.html",
                                                        "../landing.html": "implementai-landing.html"}),
    ("de/landing.html", "implementai-landing-de.html", {"impressum.html": "implementai-impressum.html", "datenschutz.html": "implementai-datenschutz.html",
                                                        "index.html": "implementai-website-de.html",
                                                        "../index.html": "implementai-website.html",
                                                        "../landing.html": "implementai-landing.html"}),
    ("pilot.html",      "implementai-pilot.html",      {"imprint.html": "implementai-imprint.html", "privacy.html": "implementai-privacy.html",
                                                        "index.html": "implementai-website.html",
                                                        "de/pilot.html": "implementai-pilot-de.html"}),
    ("de/pilot.html",   "implementai-pilot-de.html",   {"impressum.html": "implementai-impressum.html", "datenschutz.html": "implementai-datenschutz.html",
                                                        "index.html": "implementai-website-de.html",
                                                        "../pilot.html": "implementai-pilot.html"}),
    ("imprint.html",    "implementai-imprint.html",    {"imprint.html": "implementai-imprint.html", "index.html": "implementai-website.html", "privacy.html": "implementai-privacy.html",
                                                        "de/impressum.html": "implementai-impressum.html", "de/datenschutz.html": "implementai-datenschutz.html"}),
    ("privacy.html",    "implementai-privacy.html",    {"privacy.html": "implementai-privacy.html", "index.html": "implementai-website.html", "imprint.html": "implementai-imprint.html",
                                                        "de/impressum.html": "implementai-impressum.html", "de/datenschutz.html": "implementai-datenschutz.html"}),
    ("de/impressum.html",   "implementai-impressum.html",   {"impressum.html": "implementai-impressum.html", "index.html": "implementai-website-de.html", "datenschutz.html": "implementai-datenschutz.html",
                                                        "../imprint.html": "implementai-imprint.html", "../privacy.html": "implementai-privacy.html"}),
    ("de/datenschutz.html", "implementai-datenschutz.html", {"datenschutz.html": "implementai-datenschutz.html", "index.html": "implementai-website-de.html", "impressum.html": "implementai-impressum.html",
                                                        "../imprint.html": "implementai-imprint.html", "../privacy.html": "implementai-privacy.html"}),
    ("designs/midnight/index.html",   "midnight-website.html", {"landing.html": "midnight-landing.html"}),
    ("designs/midnight/landing.html", "midnight-landing.html", {"index.html": "midnight-website.html"}),
    ("designs/classic/index.html",    "classic-website.html",  {"landing.html": "classic-landing.html"}),
    ("designs/classic/landing.html",  "classic-landing.html",  {"index.html": "classic-website.html"}),
]

def bundle(src: Path, links: dict) -> str:
    html = src.read_text()
    base = src.parent

    def css(m):
        f = base / m.group(1)
        text = re.sub(r"url\((fonts/[^)]+\.woff2)\)",
                      lambda u: "url(data:font/woff2;base64," + base64.b64encode((f.parent / u.group(1)).read_bytes()).decode() + ")", f.read_text())
        return "<style>\n" + text + "\n</style>"
    def js(m):
        return "<script>\n" + (base / m.group(1)).read_text() + "\n</script>"

    html = re.sub(r'<link rel="stylesheet" href="(?!https?:)([^"]+)">', css, html)
    html = re.sub(r'<script src="(?!https?:)([^"]+)"></script>', js, html)
    def img(m):
        f = base / m.group(1)
        mime = mimetypes.guess_type(f.name)[0] or "application/octet-stream"
        return f'src="data:{mime};base64,{base64.b64encode(f.read_bytes()).decode()}"'

    html = re.sub(r'src="(?!https?:|data:)([^"]+\.(?:jpe?g|png|webp|gif|svg))"', img, html)
    html = re.sub(r'<link rel="alternate"[^>]*>\n?', '', html)  # hreflang hints only make sense on a hosted site
    for old, new in links.items():
        html = html.replace(f'href="{old}', f'href="{new}')
    return html

OUT.mkdir(exist_ok=True)
for src, name, links in PAGES:
    (OUT / name).write_text(bundle(ROOT / src, links))
    print("built", OUT / name)

# ---------------- Public website for GitHub Pages ----------------
# Only these pages and the assets they use go into docs/, which GitHub Pages publishes
# (Settings > Pages > Deploy from a branch > /docs). Designs, mock-ups, ads and notes stay out.
import shutil
SITE = ROOT / "docs"
PUBLIC = ["index.html", "landing.html", "pilot.html", "imprint.html", "privacy.html",
          "de/index.html", "de/landing.html", "de/pilot.html", "de/impressum.html", "de/datenschutz.html"]
if SITE.exists():
    shutil.rmtree(SITE)
for page in PUBLIC:
    (SITE / page).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / page, SITE / page)
shutil.copytree(ROOT / "assets", SITE / "assets")
(SITE / ".nojekyll").write_text("")   # serve files as they are, without Jekyll processing
print("site", SITE, len(PUBLIC), "pages")
