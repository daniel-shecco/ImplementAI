"""Build the ImplementAI "Spark i" logo files with outlined lettering.
Usage: python3 make_logo.py <folder containing Manrope.ttf (ExtraBold)>
"""
import sys, pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT = pathlib.Path(sys.argv[1]) / "Manrope.ttf"; OUT = pathlib.Path(__file__).parent.parent
INK, TERRA, CREAM, FOREST, BUTTER = "#1E1C17", "#C4623F", "#F5F0E7", "#1F3B33", "#F0D690"
f = TTFont(FONT); gs = f.getGlyphSet(); cmap = f.getBestCmap(); UPM = f["head"].unitsPerEm
TRACK = -0.045 * UPM

def spark(cx, cy, size, fill):
    """Four-point spark centred at (cx, cy), total width/height = size (SVG coordinates)."""
    a, b = size / 2, size * 0.067
    pts = (f"M{cx:.1f},{cy-a:.1f} Q{cx+b:.1f},{cy-b:.1f} {cx+a:.1f},{cy:.1f} Q{cx+b:.1f},{cy+b:.1f} {cx:.1f},{cy+a:.1f} "
           f"Q{cx-b:.1f},{cy+b:.1f} {cx-a:.1f},{cy:.1f} Q{cx-b:.1f},{cy-b:.1f} {cx:.1f},{cy-a:.1f} Z")
    return f'<path fill="{fill}" d="{pts}"/>'

def wordmark(ink, accent, spark_fill, scale=0.05, x0=4, base=None):
    """'ımplement' + 'ai' at scale (px per font unit); returns svg body, width, height."""
    asc = 1700  # room above x-height for the spark
    base = asc * scale if base is None else base
    parts, x = {"ink": SVGPathPen(gs), "acc": SVGPathPen(gs)}, x0
    spark_svg = ""
    for i, ch in enumerate("ımplementai"):
        g = cmap[ord(ch)]; pen = parts["acc"] if i >= 9 else parts["ink"]
        gs[g].draw(TransformPen(pen, (scale, 0, 0, -scale, x, base)))
        if i == 0:  # spark replaces the dot of the i (dotless-i stem spans x 160-432)
            spark_svg = spark(x + 296 * scale, base - 1370 * scale, 600 * scale, spark_fill)
        x += (gs[g].width + TRACK) * scale
    body = (f'<path fill="{ink}" d="{parts["ink"].getCommands()}"/>'
            f'<path fill="{accent}" d="{parts["acc"].getCommands()}"/>' + spark_svg)
    descent = 420 * scale
    return body, x - TRACK * scale + 4, base + descent

def svg(w, h, body, bg=None, rx=0):
    rect = f'<rect width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" width="{w:.0f}" height="{h:.0f}" '
            f'role="img" aria-label="ImplementAI"><title>ImplementAI</title>{rect}{body}</svg>\n')

files = {}
b, w, h = wordmark(INK, TERRA, TERRA);          files["logo.svg"] = svg(w, h, b)
b, w, h = wordmark(CREAM, BUTTER, BUTTER);      files["logo-dark.svg"] = svg(w, h, b)
pad = 60
b, w, h = wordmark(CREAM, BUTTER, BUTTER, x0=pad, base=1700 * 0.05 + pad)
files["logo-on-green.svg"] = svg(w + pad, h + pad, b, FOREST)
files["spark.svg"] = svg(100, 100, spark(50, 50, 100, TERRA))
files["profile-picture.svg"] = svg(1080, 1080, spark(540, 540, 520, BUTTER), FOREST)
files["favicon.svg"] = svg(64, 64, spark(32, 32, 38, BUTTER), FOREST, rx=14)
for n, s in files.items(): (OUT / n).write_text(s)
print(" ".join(files))
