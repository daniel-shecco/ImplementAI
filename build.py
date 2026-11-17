#!/usr/bin/env python3
"""Bundle each page into a single self-contained HTML file in standalone/.

CSS and JS are inlined, and links between the home and landing page are rewritten
so the bundled files still link to each other. Fonts load from Google Fonts.
Run: python3 build.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "standalone"

# (source page, output name, {original href -> bundled href})
PAGES = [
    ("designs/midnight/index.html",   "midnight-website.html", {"landing.html": "midnight-landing.html"}),
    ("designs/midnight/landing.html", "midnight-landing.html", {"index.html": "midnight-website.html"}),
    ("designs/atelier/index.html",    "atelier-website.html",  {"landing.html": "atelier-landing.html"}),
    ("designs/atelier/landing.html",  "atelier-landing.html",  {"index.html": "atelier-website.html"}),
    ("index.html",                    "classic-website.html",  {"landing.html": "classic-landing.html"}),
    ("landing.html",                  "classic-landing.html",  {"index.html": "classic-website.html"}),
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
    for old, new in links.items():
        html = html.replace(f'href="{old}', f'href="{new}')
    return html

OUT.mkdir(exist_ok=True)
for src, name, links in PAGES:
    (OUT / name).write_text(bundle(ROOT / src, links))
    print("built", OUT / name)
