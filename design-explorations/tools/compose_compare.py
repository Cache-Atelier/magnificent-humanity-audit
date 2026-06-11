#!/usr/bin/env python3
"""compose_compare.py <section> <before.png> <after.png> <out.png>
Side-by-side labeled BEFORE | AFTER composite, dark slate frame."""
import subprocess, sys, struct

def dims(p):
    with open(p, 'rb') as f:
        f.read(16); w, h = struct.unpack('>II', f.read(8))
    return w, h

section, before, after, out = sys.argv[1:5]
BG = '#1C1B1A'; INK = '#CECDC3'; MUT = '#878580'
W = 1080  # each panel width after downscale

tmp_b, tmp_a = '/tmp/_cmp_b.png', '/tmp/_cmp_a.png'
for src, dst in ((before, tmp_b), (after, tmp_a)):
    subprocess.run(['magick', src, '-resize', str(W), dst], check=True)

hb, ha = dims(tmp_b)[1], dims(tmp_a)[1]
H = max(hb, ha)
# pad both to same height (top-aligned), add label bar above each
for dst, label in ((tmp_b, 'BEFORE'), (tmp_a, 'AFTER')):
    subprocess.run(['magick', dst, '-background', BG, '-gravity', 'north', '-extent', f'{W}x{H}', dst], check=True)
    subprocess.run(['magick', '-background', BG, '-fill', INK, '-font', '/System/Library/Fonts/Menlo.ttc', '-pointsize', '30',
                    '-gravity', 'center', f'label:{label}', '-extent', f'{W}x64', dst.replace('.png', '_l.png')], check=True)
    subprocess.run(['magick', dst.replace('.png', '_l.png'), dst, '-append', dst], check=True)

# title bar across the top
subprocess.run(['magick', '-background', BG, '-fill', MUT, '-font', '/System/Library/Fonts/Menlo.ttc', '-pointsize', '26',
                '-gravity', 'west', f'label: {section}', '-extent', f'{W*2+48}x56', '/tmp/_cmp_t.png'], check=True)
# join: title over [before | gutter | after], outer border
subprocess.run(['magick', tmp_b, '-size', f'24x{H+64}', f'xc:{BG}', tmp_a, '+append', '/tmp/_cmp_row.png'], check=True)
subprocess.run(['magick', '/tmp/_cmp_t.png', '/tmp/_cmp_row.png', '-append',
                '-bordercolor', BG, '-border', '24', out], check=True)
print(out, dims(out))
