"""Build ImplementAI logo SVGs with the wordmark converted to outlines (no font needed to display).
Usage: python3 make_logo.py <dir with Newsreader.ttf and NewsreaderItalic.ttf>
"""
import sys, pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONTS = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(__file__).parent.parent
INK, TERRA, CREAM, FOREST, BUTTER = "#1E1C17", "#C4623F", "#F5F0E7", "#1F3B33", "#F0D690"

def text_path(fontfile, text, x0, baseline, size, tracking=0.0):
    f = TTFont(fontfile); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm
    s = size / upm; pen = SVGPathPen(gs); x = x0
    for ch in text:
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (s, 0, 0, -s, x, baseline))
        gs[g].draw(tp)
        x += gs[g].width * s + tracking * size
    return pen.getCommands(), x

# Mark: arch with a doorway cut-out and a four-point spark inside the doorway (100 x 112 units)
def mark(x, y, h, arch=TERRA, spark=TERRA):
    k = h / 112.0
    def P(px, py): return f"{x + px * k:.2f},{y + py * k:.2f}"
    r = 50 * k; ri = 20 * k
    outer = f"M{P(0,112)} V{y+50*k:.2f} A{r:.2f},{r:.2f} 0 0 1 {P(100,50)} V{y+112*k:.2f} Z"
    door = f"M{P(30,112)} V{y+66*k:.2f} A{ri:.2f},{ri:.2f} 0 0 1 {P(70,66)} V{y+112*k:.2f} Z"
    cx, cy, a, b = 50, 78, 11, 3.2   # spark centre, arm length, waist
    sp = (f"M{P(cx,cy-a)} Q{P(cx+b,cy-b)} {P(cx+a,cy)} Q{P(cx+b,cy+b)} {P(cx,cy+a)} "
          f"Q{P(cx-b,cy+b)} {P(cx-a,cy)} Q{P(cx-b,cy-b)} {P(cx,cy-a)} Z")
    return (f'<path fill="{arch}" fill-rule="evenodd" d="{outer} {door}"/>'
            f'<path fill="{spark}" d="{sp}"/>')

def wordmark(x, baseline, size, ink, accent):
    p1, x1 = text_path(FONTS / "Newsreader.ttf", "Implement", x, baseline, size, -0.01)
    p2, x2 = text_path(FONTS / "NewsreaderItalic.ttf", "AI", x1 + size * 0.11, baseline, size, 0.01)
    return f'<path fill="{ink}" d="{p1}"/><path fill="{accent}" d="{p2}"/>', x2

def svg(w, h, body, bg=None, title="ImplementAI"):
    rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" '
            f'role="img" aria-label="{title}"><title>{title}</title>{rect}{body}</svg>\n')

files = {}
# Horizontal lockups
for name, ink, acc, bg, spark in (("logo-horizontal", INK, TERRA, None, TERRA),
                                   ("logo-horizontal-dark", CREAM, BUTTER, FOREST, BUTTER)):
    size = 100; mh = 96
    wm, xend = wordmark(118, 88, size, ink, acc)
    W = xend + 12; H = 112
    files[name + ".svg"] = svg(W, H, mark(0, 4, mh, TERRA, spark) + wm, bg)
# Stacked lockup
wm, xend = wordmark(0, 0, 100, INK, TERRA)
ww = xend
wm, xend = wordmark(0, 300, 100, INK, TERRA)
W = ww + 40; cx = (W - 0) / 2
files["logo-stacked.svg"] = svg(W, 340, mark(cx - 80, 20, 180) +
                                 wordmark((W - ww) / 2, 318, 100, INK, TERRA)[0])
# Mark only (transparent), app icons and favicon
files["logo-mark.svg"] = svg(100, 112, mark(0, 0, 112))
files["icon-cream.svg"] = svg(512, 512, mark(256 - 240 * 100 / 112 / 2, 136, 240), CREAM)
files["icon-forest.svg"] = svg(512, 512, mark(256 - 240 * 100 / 112 / 2, 136, 240, TERRA, BUTTER), FOREST)
files["favicon.svg"] = svg(64, 64, mark(32 - 54 * 100 / 112 / 2, 5, 54))
for n, s in files.items():
    (OUT / n).write_text(s)
print("\n".join(files))
