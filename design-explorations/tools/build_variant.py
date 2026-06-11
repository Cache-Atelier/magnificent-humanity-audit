#!/usr/bin/env python3
"""Inject the shared sample report into a template. Usage: build_variant.py <template> <out> [data.json]"""
import json, sys, re, os
tpl, out = sys.argv[1], sys.argv[2]
data_path = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_report.json")
report = json.load(open(data_path, encoding="utf-8"))
html = open(tpl, encoding="utf-8").read()
sentinel = "/* @@REPORT_DATA@@ */"
if sentinel not in html:
    print("ERROR: sentinel not found in", tpl); sys.exit(2)
payload = json.dumps(report, ensure_ascii=False, indent=2).replace("</", "<\\/")
res = html.replace(sentinel, payload)
open(out, "w", encoding="utf-8").write(res)
m = re.search(r'<script type="application/json" id="report-data">(.*?)</script>', res, re.S)
parsed = json.loads(m.group(1).strip().replace("<\\/", "</"))
print("OK", out, "| principles:", len(parsed["principles"]), "| bytes:", len(res))
