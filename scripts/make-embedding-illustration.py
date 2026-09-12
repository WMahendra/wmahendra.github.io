"""
Original stylised illustration in the visual language of a learned-embedding
false-colour composite, over a drowned-valley (ria) coastline.

Everything is generated procedurally from noise: the coastline, the tidal
channels and all three colour fields. No real imagery, no embedding data and
no existing figure is used or traced.

Run with:  python scripts/make-embedding-illustration.py
Output:    images/s2-alphaearth-embedding-illustration.jpg (1200x675)
"""
import pathlib

import numpy as np
from scipy.ndimage import gaussian_filter, distance_transform_edt
from PIL import Image, ImageFilter

W, H = 1600, 900


def fbm(octaves=8, sigma0=110.0, persistence=0.56, seed=0):
    """Multi-scale noise: white noise blurred at halving radii, summed.

    Blurring full-resolution noise (rather than upsampling a small grid) is
    what keeps genuine pixel-scale detail in the finest octaves, which is the
    texture that makes a composite read as imagery instead of watercolour.
    """
    r = np.random.default_rng(seed)
    out = np.zeros((H, W))
    amp, total, sigma = 1.0, 0.0, sigma0
    for _ in range(octaves):
        layer = gaussian_filter(r.standard_normal((H, W)), max(sigma, 0.7))
        layer = (layer - layer.mean()) / (layer.std() + 1e-9)
        out += amp * layer
        total += amp
        amp *= persistence
        sigma /= 2.0
    out /= total
    return (out - out.min()) / (np.ptp(out) + 1e-9)


def norm(a):
    return (a - a.min()) / (np.ptp(a) + 1e-9)


def stretch(ch, lo=3.0, hi=97.0, gamma=1.12):
    p1, p2 = np.percentile(ch, [lo, hi])
    return np.clip((ch - p1) / (p2 - p1 + 1e-9), 0, 1) ** gamma


# ------------------------------------------------------ coastline / relief ---
yy, xx = np.mgrid[0:H, 0:W]

# Gentle rise inland, warped so the shore never reads as a straight line.
warp = fbm(octaves=5, sigma0=150, seed=7)
base_slope = norm(0.75 * norm(xx) + 0.22 * norm(yy) + 0.55 * (warp - 0.5))

relief = fbm(octaves=8, sigma0=95, persistence=0.58, seed=11)

# Ridged noise inverts to a branching network; subtracting it carves valleys.
# Flooding those valleys is what produces a dendritic, estuarine coast.
net = fbm(octaves=7, sigma0=120, persistence=0.54, seed=29)
valleys = 1.0 - np.abs(net - 0.5) * 2.0
valleys = norm(valleys) ** 2.2

elevation = norm(0.92 * base_slope + 0.30 * relief - 0.26 * valleys)
elevation = gaussian_filter(elevation, 2.2)

SEA = 0.400
land = elevation > SEA
# Drop speckle so the coast reads as one landmass with inlets, not an archipelago.
from scipy.ndimage import binary_opening, binary_closing, label
land = binary_closing(binary_opening(land, np.ones((7, 7))), np.ones((5, 5)))
lab, n = label(land)
if n:
    sizes = np.bincount(lab.ravel())
    sizes[0] = 0
    land = np.isin(lab, np.where(sizes > 4000)[0])

# Narrow tidal creeks reaching further inland than the flooded valleys.
creeks = (valleys > 0.945) & land & (distance_transform_edt(land) < 120)
creeks = gaussian_filter(creeks.astype(float), 0.9) > 0.30
water = (~land) | creeks

# ---------------------------------------------------------- colour fields ---
# Three decorrelated fields stand in for three axes of an embedding space,
# plus a fine field that carries pixel-scale grain into every channel.
f1 = fbm(octaves=9, sigma0=44, persistence=0.62, seed=101)
f2 = fbm(octaves=9, sigma0=30, persistence=0.60, seed=202)
f3 = fbm(octaves=9, sigma0=60, persistence=0.62, seed=303)
grain = fbm(octaves=3, sigma0=3.2, persistence=0.5, seed=404)

# Patchiness: thresholded fields give parcel-like blocks, as land cover does.
patch = (gaussian_filter((f1 > 0.52).astype(float), 1.1) * 0.9
         + gaussian_filter((f2 > 0.58).astype(float), 0.8) * 0.8
         + gaussian_filter((f3 > 0.47).astype(float), 1.6) * 0.6)
patch = norm(patch)

# Channel mixing chosen so no pure primary dominates: each output channel
# draws on more than one field, which yields the olive / magenta / teal family
# typical of an embedding composite rather than red-green-blue poster colours.
R = norm(0.34 * f2 + 0.30 * (1 - f1) + 0.18 * patch + 0.30 * f3 + 0.26 * grain)
G = norm(0.60 * f1 + 0.40 * f3 + 0.22 * (1 - f2) + 0.18 * patch + 0.26 * grain)
B = norm(0.46 * f3 + 0.42 * (1 - f2) + 0.28 * f1 + 0.22 * patch + 0.26 * grain)

R, G, B = stretch(R), stretch(G), stretch(B)

# Modest chroma lift only: over-saturating is what made the first attempt look
# like poster paint instead of a stretched composite.
mean = (R + G + B) / 3.0
SAT = 1.34
R = np.clip(mean + (R - mean) * SAT, 0, 1)
G = np.clip(mean + (G - mean) * SAT, 0, 1)
B = np.clip(mean + (B - mean) * SAT, 0, 1)

# Dendritic drainage: the same valley network that shapes the coast is darkened
# into the land, which is the vein-like texture a real composite shows.
shade = 1.0 - 0.42 * norm(gaussian_filter(valleys, 1.2))
R, G, B = R * shade, G * shade, B * shade

# Hue nudged off pure red towards the olive / magenta / teal family.
R2 = 0.86 * R + 0.14 * G
G2 = 0.10 * R + 0.90 * G
B2 = 0.06 * R + 0.94 * B
R, G, B = R2, G2, B2

# Land mid-toned so the water stays the brightest, most readable element.
R = 0.08 + 0.70 * R
G = 0.08 + 0.70 * G
B = 0.08 + 0.70 * B

# ------------------------------------------------------------------ water ---
# The raw distance transform has a medial-axis skeleton that shows through as
# polygon edges once it is used as a colour ramp, so it is smoothed first.
depth = gaussian_filter(distance_transform_edt(~land), 22.0)
depth = np.clip(depth / 190.0, 0, 1) ** 0.8
ripple = gaussian_filter(fbm(octaves=4, sigma0=14, seed=55), 2.5)

wR = 0.06 + 0.34 * (1 - depth) + 0.07 * ripple
wG = 0.34 + 0.40 * (1 - depth) + 0.08 * ripple
wB = 0.42 + 0.36 * (1 - depth) + 0.08 * ripple

R = np.where(water, wR, R)
G = np.where(water, wG, G)
B = np.where(water, wB, B)

# Pale intertidal halo: the shoreline detail that carries at thumbnail size.
pad = np.pad(land, 1, constant_values=True)          # treat outside as land
dist_in = distance_transform_edt(pad)[1:-1, 1:-1]     # so no false shore at the frame
halo = (dist_in > 0) & (dist_in < 4)
k = np.clip(1.0 - dist_in / 4.0, 0, 1)
R = np.where(halo, np.clip(R + 0.26 * k, 0, 1), R)
G = np.where(halo, np.clip(G + 0.24 * k, 0, 1), G)
B = np.where(halo, np.clip(B + 0.22 * k, 0, 1), B)

img = np.clip(np.dstack([R, G, B]), 0, 1)
out = Image.fromarray((img * 255).astype(np.uint8), "RGB")
out = out.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
# Trim the frame: the distance transforms and the unsharp mask both leave a
# faint seam on the outermost pixels.
out = out.crop((8, 8, W - 8, H - 8))

# Written next to the site assets so re-running reproduces the committed file.
here = pathlib.Path(__file__).resolve().parent.parent
card = out.resize((1200, 675), Image.LANCZOS)
card.save(here / "images" / "s2-alphaearth-embedding-illustration.jpg",
          quality=82, optimize=True, progressive=True)
print("land fraction %.2f" % land.mean(), "| card", card.size)
