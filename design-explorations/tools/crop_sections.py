#!/usr/bin/env python3
"""crop_sections.py <offsets_json> <full_png_prefix> <out_dir> <tag>
offsets_json: the measured anchor dict (CSS px, width 1100, DPR 2 captures)
full_png_prefix: e.g. .../audit-shots/before  (expects -dark-full.png / -light-full.png)
tag: filename prefix for crops, e.g. before
"""
import json, subprocess, sys, os

offs = json.load(open(sys.argv[1]))
prefix, outdir, tag = sys.argv[2], sys.argv[3], sys.argv[4]
H = offs["H"]; S = 2  # device scale

def sections(o):
    return [
        # name, y_css, h_css
        ("masthead",      0,                    o["sum_cap"] + 40),
        ("synthesis",     o["sum_cap"] - 40,    (o["ratings_key"] - o["sum_cap"]) + 60),
        ("scorecard-top", o["ratings_key"] - 40,(o["sc_group4"] - o["ratings_key"]) + 80),
        ("scorecard-mid", o["sc_group4"] - 40,  (o["finding1"] - o["sc_group4"]) + 40),
        ("finding-card",  o["finding1"] - 20,   (o["finding2"] - o["finding1"]),),
        ("code-citations",o["pre1"] - 40,       (o["finding2"] - o["pre1"]) + 20),
        ("boundary",      o["finding2"] - 80,   700),
        ("closings",      o["movement1"] - 40,  (o["footer"] - o["movement1"]) - 0),
        ("footer",        H - 700,              700),
    ]

LIGHT = {"masthead", "scorecard-top", "finding-card", "footer"}
made = []
for mode in ("dark", "light"):
    src = f"{prefix}-{mode}-full.png"
    for name, y, h in sections(offs):
        if mode == "light" and name not in LIGHT:
            continue
        y = max(0, y); h = min(h, H - y)
        out = os.path.join(outdir, f"{tag}-{name}-{mode}.png")
        subprocess.run(["magick", src, "-crop", f"2200x{h*S}+0+{y*S}", "+repage", out], check=True)
        made.append(out)
for m in made:
    print(m)
