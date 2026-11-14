#!/usr/bin/env python3
"""Bakes the name wordmark into an SVG (glyphs converted to outlines).

A one-off asset generator, not part of the nightly refresh: the name does not
change, so the SVGs are committed and served as-is. GitHub strips `style`
attributes and web fonts from READMEs, which is why the name has to be an image
rather than styled text.

The viewBox is fitted to the real ink bounds, so ascenders and descenders are
never clipped.

Needs fonttools:  pip install fonttools
Run from the repo root:  python scripts/make_wordmark.py
"""
from pathlib import Path

from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

TEXT = "Aditya Sharma"
FONT = Path(r"C:\Windows\Fonts\seguili.ttf")   # Segoe UI Light
CAP_HEIGHT = 34        # rendered cap height in px
TRACKING = 0.5         # extra px between glyphs
PAD = 4                # transparent margin around the ink
ASSETS = Path(__file__).resolve().parent.parent / "assets"

# Same ink colours as the contribution graph, so both widgets sit at one weight.
THEMES = {"light": "#1f2328", "dark": "#e6edf3"}


def ntos(v):
    return f"{v:.1f}"


def layout():
    """Return (path data, ink bounds) for TEXT, with y pointing down."""
    font = TTFont(FONT)
    upem = font["head"].unitsPerEm
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    cap = getattr(font["OS/2"], "sCapHeight", int(upem * 0.7)) or int(upem * 0.7)
    scale = CAP_HEIGHT / cap

    x, parts = 0.0, []
    bounds = None
    for ch in TEXT:
        name = cmap.get(ord(ch))
        if name is None:
            x += upem * 0.3 * scale
            continue
        tr = Transform().translate(x, 0).scale(scale, -scale)

        pen = SVGPathPen(glyphs, ntos=ntos)
        glyphs[name].draw(TransformPen(pen, tr))
        if pen.getCommands():
            parts.append(pen.getCommands())

        bp = BoundsPen(glyphs)
        glyphs[name].draw(TransformPen(bp, tr))
        if bp.bounds:
            b = bp.bounds
            bounds = b if bounds is None else (min(bounds[0], b[0]), min(bounds[1], b[1]),
                                               max(bounds[2], b[2]), max(bounds[3], b[3]))
        x += glyphs[name].width * scale + TRACKING

    return " ".join(parts), bounds


def svg(fill):
    d, (x0, y0, x1, y1) = layout()
    width = (x1 - x0) + PAD * 2
    height = (y1 - y0) + PAD * 2
    tx, ty = PAD - x0, PAD - y0
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" '
        f'viewBox="0 0 {width:.0f} {height:.0f}" role="img" aria-label="{TEXT}">'
        f'<path transform="translate({tx:.1f},{ty:.1f})" d="{d}" fill="{fill}"/></svg>'
    )


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    for theme, fill in THEMES.items():
        out = ASSETS / f"name-{theme}.svg"
        out.write_text(svg(fill), encoding="utf-8")
        print(f"wrote {out.name} ({len(out.read_text(encoding='utf-8'))} bytes)")