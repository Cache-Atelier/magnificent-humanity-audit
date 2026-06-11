#!/usr/bin/env python3
"""verify_template.py <template.html> — mechanical invariant checks after each build batch.
Exits non-zero on any failure."""
import re, subprocess, sys, tempfile, os

p = sys.argv[1]
s = open(p, encoding="utf-8").read()
fails = []

# 1. sentinel + unfilled guard intact
if "/* @@REPORT_DATA@@ */" not in s: fails.append("MISSING data sentinel /* @@REPORT_DATA@@ */")
if 'id="report-data"' not in s: fails.append('MISSING #report-data script tag')
if 'indexOf("@@REPORT_DATA@@")' not in s: fails.append("MISSING unfilled-template guard")

# 2. functional core present
for token in ["function esc(", "JSON.parse", "RE_C", "RE_PY", "function highlight(", "@media print", "localStorage.getItem('mh-theme')"]:
    if token not in s and token.replace("'", '"') not in s:
        fails.append("MISSING functional token: " + token)

# 3. node --check every <script> block (skip the JSON one)
blocks = re.findall(r"<script(?![^>]*application/json)[^>]*>(.*?)</script>", s, re.S)
if not blocks: fails.append("no JS script blocks found")
for i, b in enumerate(blocks):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(b); tmp = f.name
    r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
    os.unlink(tmp)
    if r.returncode != 0:
        fails.append(f"script block {i} fails node --check:\n{r.stderr[:800]}")

# 4. sample injection succeeds
r = subprocess.run(["python3", os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_variant.py"), p, "/tmp/_verify_render.html"],
                   capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(p)))
if r.returncode != 0: fails.append("sample injection failed: " + (r.stdout + r.stderr)[:400])

if fails:
    print("VERIFY FAIL (" + p + ")"); [print(" -", f) for f in fails]; sys.exit(1)
print("VERIFY OK (" + p + "): sentinel+guard, core tokens, " + str(len(blocks)) + " JS blocks parse, sample injects")
