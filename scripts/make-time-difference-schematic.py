"""Schematic thumbnail: three period classifications combined by majority vote.

Nothing here is data. The patchwork is generated from seeded noise purely so the
tiles read as land-cover maps at card size; the point it makes is structural -
three maps of one place, one combined map, and a layer marking where they differ.
"""
import numpy as np

N = 14                      # cells per tile edge
PALETTE = {1: "#006400",    # Forest
           2: "#baad19",    # Bareland
           3: "#e3e519",    # Open Land
           4: "#46ff00"}    # Shrubland
INK, MUTED, LINE, ACCENT = "#23282d", "#5c666f", "#c9d0d4", "#17627a"
DISAGREE = "#c2185b"

rng = np.random.default_rng(11)

def smooth(a, k=3):
    """Box-blur so classes form patches rather than salt and pepper."""
    out = np.zeros_like(a, dtype=float)
    pad = np.pad(a.astype(float), k // 2, mode="edge")
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            out[i, j] = pad[i:i + k, j:j + k].mean()
    return out

# Base map: four classes laid out as coherent patches.
field = smooth(rng.random((N, N)), 5)
field = (field - field.min()) / np.ptp(field)
base = np.digitize(field, [0.34, 0.52, 0.70]) + 1     # -> 1..4

def vary(base, frac, seed):
    """Flip a fraction of cells to a neighbouring class, as a later period would."""
    r = np.random.default_rng(seed)
    out = base.copy()
    flip = r.random(base.shape) < frac
    shift = r.choice([-1, 1], size=base.shape)
    out[flip] = np.clip(out[flip] + shift[flip], 1, 4)
    return out

p1 = base
p2 = vary(base, 0.14, 202)
p3 = vary(base, 0.22, 303)

stack = np.stack([p1, p2, p3])
mode = np.zeros_like(base)
for i in range(N):
    for j in range(N):
        vals, counts = np.unique(stack[:, i, j], return_counts=True)
        mode[i, j] = vals[np.argmax(counts)]
agree = (stack == mode).sum(axis=0)        # 3 = all agree, 2 = one dissents, 1 = all differ

W, H = 1200, 675
out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">' % (W, H, W, H)]
out.append('<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H))
FONT = "font-family=\"system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif\""

def tile(x, y, size, grid, mark=None, flat=None):
    """Draw one map tile. `flat` paints a single background colour instead of classes."""
    cell = size / N
    out.append('<g>')
    for i in range(N):
        for j in range(N):
            fill = flat if flat else PALETTE[int(grid[i, j])]
            if mark is not None and mark[i, j]:
                fill = DISAGREE
            out.append('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="%s"/>'
                       % (x + j * cell, y + i * cell, cell + 0.4, cell + 0.4, fill))
    out.append('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="none" stroke="%s" stroke-width="2"/>'
               % (x, y, size, size, INK))
    out.append('</g>')

def label(cx, y, text, size=26, fill=INK, weight="600"):
    out.append('<text x="%.1f" y="%.1f" text-anchor="middle" %s font-size="%d" font-weight="%s" fill="%s">%s</text>'
               % (cx, y, FONT, size, weight, fill, text))

CY = 316                      # vertical centre of the tile row
S, GAP = 190, 16
xs = [40, 40 + S + GAP, 40 + 2 * (S + GAP)]
TY = CY - S / 2
for x, g, name in zip(xs, [p1, p2, p3], ["Jan \u2013 Apr", "May \u2013 Aug", "Sep \u2013 Dec"]):
    tile(x, TY, S, g)
    label(x + S / 2, TY - 20, name, 24, MUTED, "500")
left_cx = (xs[0] + xs[2] + S) / 2
label(left_cx, TY + S + 46, "three four-month periods, one classifier", 26)

ax0, ax1 = 650, 718
out.append('<path d="M%d %.1f L%d %.1f" stroke="%s" stroke-width="5" fill="none"/>' % (ax0, CY, ax1 - 14, CY, ACCENT))
out.append('<path d="M%d %.1f l-18 -11 l0 22 z" fill="%s"/>' % (ax1, CY, ACCENT))

BS, BX = 236, 730
BY = CY - BS / 2
tile(BX, BY, BS, mode)
label(BX + BS / 2, BY - 20, "majority vote", 24, MUTED, "500")

# Top-aligned with the majority tile so both captions sit on one baseline.
DS, DX = 150, 990
tile(DX, BY, DS, mode, mark=(agree < 3), flat="#e8ecee")
label(DX + DS / 2, BY - 20, "disagreement", 24, MUTED, "500")

label((BX + DX + DS) / 2, TY + S + 46, "one combined map", 26)

out.append('<text x="40" y="520" %s font-size="22" fill="%s">Schematic, not data</text>' % (FONT, MUTED))
out.append('</svg>')
open("/tmp/thumb/thumb.svg", "w", encoding="utf-8").write("\n".join(out))
print("disagreeing cells", int((agree < 3).sum()), "of", N * N)
