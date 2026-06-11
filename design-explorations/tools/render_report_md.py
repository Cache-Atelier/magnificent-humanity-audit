#!/usr/bin/env python3
"""render_report_md.py <report.json> <out.md>
Deterministic Markdown rendering of the structured report object, following
templates/report.md. Mirrors the HTML renderer's display rules: reading-order
ordinals, violates/strains vocabulary, no standalone finding verdicts."""
import json, re, sys

VERDICT_IMAGE = {"babel": "Toward Babel", "rebuilt_jerusalem": "Toward the rebuilt Jerusalem",
                 "contested": "Between Babel and Jerusalem"}
SHORT = {"dignity": "Dig", "common_good": "C.G.", "universal_destination": "U.D.",
         "subsidiarity": "Sub", "solidarity": "Sol", "social_justice": "S.J.",
         "integral_development": "I.D."}
ORDER = ["dignity", "common_good", "universal_destination", "subsidiarity",
         "solidarity", "social_justice", "integral_development"]

def dedash(s):
    s = re.sub(r"\s*—\s*", " – ", s)  # em-dash -> spaced en-dash (titles only)
    return re.sub(r"\s*--\s*", " – ", s)

def relations(f):
    rels = f.get("principle_relations")
    if rels: return rels
    out = [{"principle": f.get("primary_principle"), "relation": "tension"}]
    out += [{"principle": k, "relation": "tension"} for k in f.get("secondary_principles", [])]
    return out

def rel_to(f, key):
    for r in relations(f):
        if r["principle"] == key: return r["relation"]
    return None

def main(src, dst):
    d = json.load(open(src, encoding="utf-8"))
    meta, syn, principles = d["meta"], d["synthesis"], d["principles"]
    pname = {p["key"]: p["name"] for p in principles}
    prange = {p["key"]: p["paragraph_range"] for p in principles}

    findings = []
    for p in principles:
        for f in p.get("findings", []):
            findings.append(f)
    # reading order: any violates-relation first, then confidence desc
    findings.sort(key=lambda f: (0 if any(r["relation"] == "violates" for r in relations(f)) else 1,
                                 -(f.get("confidence") or 0)))
    ordinals = {f["id"]: f"{i+1:02d}" for i, f in enumerate(findings)}

    def ord_refs(s):
        return re.sub(r"\bF(\d{1,2})\b",
                      lambda m: ("finding " + ordinals["F" + m.group(1)]) if ("F" + m.group(1)) in ordinals else m.group(0), s)

    L = []
    # masthead
    L.append(f"# An anthropological audit of {meta['system_name']}\n")
    L.append("This reads the system against the seven principles of Catholic social doctrine set out in the encyclical *Magnifica Humanitas*, asking what its workings imply about the human person.\n")
    L.append(f"**Date:** {meta['date']}")
    L.append(f"**Scope:** {meta['scope']}")
    ev = {"source_code": "Source code", "partial_code": "Partial code", "product_docs": "Product documentation",
          "behavioral_account": "Behavioral account", "mixed": "Mixed evidence"}.get(meta.get("evidence_base"), meta.get("evidence_base", ""))
    L.append(f"**Evidence:** {ev}")
    if meta.get("repo_url"): L.append(f"**Repository:** {meta['repo_url']}")
    L.append("\n---\n")

    # synthesis + stat line (findings counted; principles by aggregate verdict)
    agg = {"violates": 0, "tension": 0}
    for p in principles:
        if p["verdict"] in agg: agg[p["verdict"]] += 1
    stat = f"{len(findings)} finding" + ("s" if len(findings) != 1 else "")
    pbits = []
    if agg["violates"]: pbits.append(f"{agg['violates']} violated")
    if agg["tension"]: pbits.append(f"{agg['tension']} strained")
    if pbits: stat += f" · of {len(principles)} principles: " + ", ".join(pbits)
    L.append("## Synthesis\n")
    L.append(f"**{VERDICT_IMAGE.get(syn['verdict_image'], syn['verdict_image'])}** — {stat}\n")
    for para in re.split(r"\n{2,}", syn["text"].strip()):
        L.append(para.strip() + "\n")
    L.append("---\n")

    # matrix
    L.append("## The findings, by principle\n")
    L.append("One row per finding, one column per principle. `●` = violates that principle · `◐` = strains it · `·` = not engaged.\n")
    head = "| # | Anthropological bug | " + " | ".join(SHORT[k] for k in ORDER) + " | conf |"
    L.append(head)
    L.append("|" + "---|" * (len(ORDER) + 3))
    for f in findings:
        cells = []
        for k in ORDER:
            r = rel_to(f, k)
            cells.append("●" if r == "violates" else "◐" if r == "tension" else "·")
        conf = f.get("confidence");  conf = str(conf) if conf is not None else "—"
        L.append(f"| {ordinals[f['id']]} | {dedash(f['title'])} | " + " | ".join(cells) + f" | {conf} |")
    L.append("")
    L.append("Column key — " + " · ".join(f"{SHORT[k]}: {pname[k]} {prange[k]}" for k in ORDER) + ".\n")
    bp = []
    for k in ORDER:
        p = next(pp for pp in principles if pp["key"] == k)
        word = {"violates": "violated", "tension": "strained"}.get(p["verdict"], "—")
        line = f"**{p['name']}** — {word}"
        if p.get("verdict_summary"): line += f": {p['verdict_summary']}"
        bp.append(line)
    L.append("**By principle:** " + " ".join(b + "." if not b.endswith(".") else b for b in bp) + "\n")
    L.append("---\n")

    # findings, in detail
    L.append("## The findings, in detail\n")
    for i, f in enumerate(findings):
        L.append(f"### {ordinals[f['id']]}. {dedash(f['title'])} — confidence {f.get('confidence', '—')}\n")
        v = [pname[r["principle"]] for r in relations(f) if r["relation"] == "violates"]
        s = [pname[r["principle"]] for r in relations(f) if r["relation"] == "tension"]
        eng = []
        if v: eng.append("violates " + ", ".join(v))
        if s: eng.append("strains " + ", ".join(s))
        L.append("*Engages:* " + " · ".join(eng) + "\n")
        if f.get("code_evidence"):
            L.append("**Code evidence:**\n")
            for ce in f["code_evidence"]:
                L.append(f"```{ce.get('language', 'text')}")
                L.append(ce.get("snippet", "").rstrip())
                L.append("```")
                L.append(f"`Location: {ce.get('location', '')}`\n")
        if f.get("behavior"): L.append(f"**Behavior:** {f['behavior']}\n")
        if f.get("citations"):
            L.append("**From *Magnifica Humanitas*:**\n")
            for c in f["citations"]:
                if c.get("quote"):
                    L.append(f"> {c['paragraph']} “{c['quote']}”")
                else:
                    L.append(f"> {c['paragraph']}")
                if c.get("gloss"): L.append(f"> — {c['gloss']}")
                L.append("")
        if f.get("violation"): L.append(f"**Violation:** {f['violation']}\n")
        if f.get("resembles"):
            L.append(f"**Resembles:** {f['resembles']['label']} — {f['resembles']['gloss']}\n")
        if f.get("remediation"):
            L.append("**Remediation:**")
            for r in f["remediation"]: L.append(f"- {r}")
            L.append("")
        if f.get("structural_note"): L.append(f"**Structural note:** {f['structural_note']}\n")
        if i < len(findings) - 1: L.append("---\n")
    L.append("---\n")

    # closings
    if d.get("mitigations"):
        L.append("## What the system does well\n")
        for m in d["mitigations"]:
            L.append(f"- **{m['title']}** ({pname.get(m.get('principle_key'), m.get('principle_key', ''))}) — {m['note']}")
        L.append("")
        L.append("---\n")
    if d.get("dropped"):
        L.append("## Dropped and consolidated\n")
        for x in d["dropped"]:
            conf = x.get("confidence"); conf = str(conf) if conf is not None else "—"
            reason = ord_refs(str(x.get("reason", "")).replace("merged_into:", "merged into ").replace("_", " "))
            L.append(f"- **{x['title']}** — conf {conf} — {reason}")
        L.append("")
        L.append("---\n")
    if d.get("scope_limits"):
        L.append("## Limits of this audit\n")
        for x in d["scope_limits"]: L.append(f"- {ord_refs(x)}")
        L.append("")
        L.append("---\n")

    L.append("## Methodology note\n")
    L.append("This audit was conducted using the [Magnificent Humanity Audit](https://github.com/Cache-Atelier/magnificent-humanity-audit/releases/latest) agent skill made by [Cache Atelier](https://cacheatelier.work), applying the seven principles of Catholic Social Doctrine as articulated in Pope Leo XIV's encyclical *Magnifica Humanitas* (15 May 2026). Findings are reported only at confidence ≥80. The encyclical is at https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html.")

    open(dst, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("OK", dst, "| findings:", len(findings), "| order:", " ".join(f["id"] for f in findings))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
