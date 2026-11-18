#!/usr/bin/env python3
"""Bundle each page into a single self-contained HTML file in standalone/.

CSS, JS and images are inlined, and links between the home and landing page are rewritten
so the bundled files still link to each other. Fonts load from Google Fonts.
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
    ("index.html",      "implementai-website.html",    {"landing.html": "implementai-landing.html",
                                                        "de/index.html": "implementai-website-de.html",
                                                        "de/landing.html": "implementai-landing-de.html",
                                                        "pilot.html": "implementai-pilot.html"}),
    ("landing.html",    "implementai-landing.html",    {"index.html": "implementai-website.html",
                                                        "de/index.html": "implementai-website-de.html",
                                                        "de/landing.html": "implementai-landing-de.html"}),
    ("de/index.html",   "implementai-website-de.html", {"landing.html": "implementai-landing-de.html",
                                                        "pilot.html": "implementai-pilot-de.html",
                                                        "../index.html": "implementai-website.html",
                                                        "../landing.html": "implementai-landing.html"}),
    ("de/landing.html", "implementai-landing-de.html", {"index.html": "implementai-website-de.html",
                                                        "../index.html": "implementai-website.html",
                                                        "../landing.html": "implementai-landing.html"}),
    ("pilot.html",      "implementai-pilot.html",      {"index.html": "implementai-website.html",
                                                        "de/pilot.html": "implementai-pilot-de.html"}),
    ("de/pilot.html",   "implementai-pilot-de.html",   {"index.html": "implementai-website-de.html",
                                                        "../pilot.html": "implementai-pilot.html"}),
    ("designs/midnight/index.html",   "midnight-website.html", {"landing.html": "midnight-landing.html"}),
    ("designs/midnight/landing.html", "midnight-landing.html", {"index.html": "midnight-website.html"}),
    ("designs/classic/index.html",    "classic-website.html",  {"landing.html": "classic-landing.html"}),
    ("designs/classic/landing.html",  "classic-landing.html",  {"index.html": "classic-website.html"}),
]

def bundle(src: Path, links: dict) -> str:
    html = src.read_text()
    base = src.parent

    def css(m):
        return "<style>\n" + (base / m.group(1)).read_text() + "\n</style>"
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
