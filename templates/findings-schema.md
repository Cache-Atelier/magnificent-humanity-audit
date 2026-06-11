# Findings schema — the structured audit object

This file is the **single source of truth** for the shape of an audit's output. Both renderers consume it:

- `templates/report.html` — the **default** artifact (styled, self-contained: matrix index + one flat severity-ordered findings list).
- `templates/report.md` — the **secondary** share/LLM copy (same content, Markdown).

The agent's job is to assemble **one structured object** (the `report` below) and then render it to both forms. The two renderers must never disagree about field names or meaning; if a field is added or renamed, change it here first.

The format is described as annotated pseudo-JSON. It is a contract, not a literal file the agent must emit verbatim — but every field named here must be populated (or explicitly null/empty) so the renderers can rely on it.

---

## The `report` object

```
report = {
  meta: {
    system_name:          string,          // e.g. "X 'For You' Feed Algorithm"
    date:                 "YYYY-MM-DD",
    scope:                string,           // what was audited
    evidence_base:        "source_code" | "partial_code" | "product_docs" | "behavioral_account" | "mixed",
    repo_url:             string | null,    // omitted from render if null
    principles_in_scope:  "all" | [ <principle key>, ... ]
  },

  synthesis: {
    verdict_image:        "babel" | "rebuilt_jerusalem" | "contested",   // the overarching §9/§90 judgment
    text:                 string            // 200–400 words; a judgment, not a summary
  },

  // Exactly the seven principles, in encyclical order, ALWAYS all seven present.
  principles: [
    {
      key:               <principle key>,   // see "Principle keys" below
      name:              string,            // canonical display name
      paragraph_range:   string,            // e.g. "§48–58"
      verdict:           "honors" | "tension" | "violates",   // derived; see "Verdict derivation"
      verdict_summary:   string,            // one line; why this verdict
      findings:          [ Finding, ... ]   // only findings whose primary_principle == key; may be empty
    },
    ... // 7 total
  ],

  mitigations: [                            // what the system does WELL / safeguards credited — may be empty
    { title: string, principle_key: <principle key>, note: string }
  ],

  dropped: [                                // transparency: consolidated-away or sub-threshold — may be empty
    {
      title:      string,
      confidence: int | null,
      reason:     "below_threshold" | "merged_into:<finding id>" | "charitable_reading" | "out_of_scope"
    }
  ],

  scope_limits: [ string, ... ]             // evidence gaps, out-of-scope areas, assumptions — may be empty
}
```

## The `Finding` object

```
Finding = {
  id:                   string,             // stable, e.g. "F1"; used in anchors (#f-F1) and by dropped[].reason.
                                            // NEVER shown raw to the reader — display uses ordinals (see below)
  title:                string,             // one-line description of the bug
  confidence:           int,                // 80–100 only (findings below 80 are never included)
  primary_principle:    <principle key>,    // the finding's home bucket (must equal principle_relations[0].principle)

  // THE RELATION MODEL — the load-bearing field. A bug has NO standalone verdict;
  // it only violates or strains *in relation to a principle*. List every principle
  // the finding engages, primary FIRST, each with its relation:
  principle_relations: [
    { principle: <principle key>, relation: "violates" | "tension" }
  ],
  // (legacy: if principle_relations is absent the renderers fall back to
  //  primary_principle + secondary_principles with relation "tension"; new
  //  audits must always emit principle_relations.)

  code_evidence: [                          // DISCRETE — renders as fenced code blocks / <pre>; may be empty
    {
      location: string,                     // "file:line", route, flow, or "observable behavior: ..."
      language: string,                     // "rust" | "python" | "javascript" | ... | "text" (behavioral)
      snippet:  string                      // the quoted code, or a short behavioral description if language=="text"
    }
  ],

  behavior:             string,             // factual: what the system does. The defensible factual basis.

  citations: [                              // DISCRETE — renders as blockquotes with a §-chip; >= 1 required
    {
      paragraph: string,                    // e.g. "§170" or a range "§170–172"
      quote:     string,                    // VERBATIM, <= 25 words; or "" if only a paraphrase is available
      gloss:     string                     // one line connecting the paragraph to this behavior
    }
  ],

  violation:            string,             // the moral reading: how the behavior contradicts the principle(s)
  resembles:            { label: "technocratic-paradigm" | "transhumanism" | "posthumanism", gloss: string } | null,
  remediation:          [ string, ... ],    // 2–4 concrete tactical steps
  structural_note:      string | null       // when the fix is non-local (business model, org telos, regulation)
}
```

---

## Principle keys

The seven, in encyclical order. `key` is the stable identifier; `name` and `paragraph_range` are the canonical display values.

| key | name | paragraph_range |
|---|---|---|
| `dignity` | The dignity of the human person | §48–58 |
| `common_good` | The common good | §59–64 |
| `universal_destination` | The universal destination of goods | §65–67 |
| `subsidiarity` | Subsidiarity | §68–72 |
| `solidarity` | Solidarity | §73–76 |
| `social_justice` | Social justice | §77–81 |
| `integral_development` | Integral human development | §82–85 |

---

## Verdict derivation

A principle's `verdict` is **derived from the relations of every finding that engages it** (via `principle_relations`, regardless of which principle is the finding's home bucket), so the scorecard is auditable rather than a free editorial label:

- **`violates`** — at least one finding carries a `"violates"` relation to this principle.
- **`tension`** — findings engage the principle, but none with a `"violates"` relation.
- **`honors`** — no finding engages the principle at all.

The judgment lives in the relations themselves: when assembling a finding, decide **per principle** whether the behavior *contradicts* it (`violates`) or *strains* it (`tension`) — that decision, not a confidence threshold, drives the verdict. A **one-notch manual override** of a derived verdict is permitted, but only with the reason stated in `verdict_summary`. Never leave a verdict empty — a principle with no engaging findings is `honors` (the audit found no violation; not necessarily positive evidence).

`synthesis.verdict_image` is the overarching judgment and is set independently of the per-principle verdicts: `babel` (the system is built toward Babel), `rebuilt_jerusalem` (toward the rebuilt Jerusalem), or `contested` (genuinely between). It answers §85/§129 for the system as a whole.

---

## Display vocabulary and ordinals

The data keys above are stable; the **renderers translate them for the reader**:

- `tension` displays as **"strains"** (a finding *strains* a principle; a principle is *strained*). The phrase "in tension" never appears in a rendered report.
- `honors` is **never displayed as a rating**. A bug-finding audit awards no honors; a principle no finding engages simply renders unmarked (no dot, no chip). The `honors` key exists so the derivation is total.
- **A finding displays no standalone verdict** — only its per-principle relations (the matrix row; the rail's dotted ENGAGES list). Asking whether a bug "violates" *in general* is a category error the report's structure refuses.
- **Ordinals:** findings display as `01`..`NN` in the report's reading order — findings carrying any `"violates"` relation first, then the rest, ties broken by descending `confidence`. The stable `id` (`F1`) survives only in anchors (`#f-F1`) and machine references; any rendered cross-reference (e.g. a `dropped[].reason` of `merged_into:F1`) is translated to "finding 01".

---

## Inline code in prose

In every prose field (`behavior`, `violation`, `synthesis.text`, glosses, remediation steps, `structural_note`, `meta.scope`, mitigation notes, `scope_limits`), wrap identifiers, file paths, function names, flags, and field names in **backticks** — `` `ranking_scorer.rs:125-173` ``, `` `device_id` ``. Both renderers set these as inline code (mono, sized to the prose, on the code surface tint in HTML; standard backticks in Markdown). Never leave a code identifier bare in serif prose, and never backtick ordinary words for emphasis — prose fields carry no other markup (no bold/italic).

---

## Verbatim discipline

`citations[].quote` must be **copied verbatim** from the encyclical and **≤ 25 words**. Load the paragraph's note in [`../paragraphs/`](../paragraphs/) (linked from `encyclical-reference.md`) and quote from it, so the words are exact. If only a paraphrase is available, set `quote: ""` and rely on `paragraph` + `gloss` — **never fabricate or reconstruct a quote.** The audit's authority depends on quote fidelity. Longer passages are summarized in `gloss`, not quoted.

---

## Rendering contract

Both renderers map the structured object the same way; this fixes the HTML/MD correspondence so they cannot drift.

| Object field | HTML (`report.html`) | Markdown (`report.md`) |
|---|---|---|
| `meta` | masthead: "An anthropological audit of" overline, system name, dek, **labeled** meta block (date / scope / evidence / repository) | title block with the same labeled lines |
| `synthesis` | italic "Synthesis" header; below the rule: the verdict pill (`verdict_image` → "Toward Babel" / "Toward the rebuilt Jerusalem" / "Between Babel and Jerusalem") + a data-computed stat line ("N findings · of 7 principles: X violated, Y strained"), then the prose | `## Synthesis` with the verdict tag + the same stat line, then prose |
| `principles[]` × findings | **"The findings, by principle" matrix**: one row per finding (✴ + ordinal + linked title + confidence), one slanted-name column per principle with its aggregate verdict dot at the column foot; relation dots at the intersections (red = violates, gold = strains, faint mote = not engaged); legend below | a findings × principles table (rows = findings, columns = principle short names, cells `●` violates / `◐` strains / `·` not engaged, plus a confidence column) + the same legend |
| `principle.verdict` | aggregate dot at the column foot: violates → `--violates` red, tension → `--tension` gold, honors → **no dot** | a one-line per-principle aggregate under the table; `honors` principles listed unmarked |
| `Finding` body | ONE flat list, reading order = ordinal order, no per-principle sections; each card: sticky rail (✴ permalink + ordinal + dotted ENGAGES list of principle names + confidence), mono title, prose, evidence, citations, remedies, note; ⁂ asterism between findings | `## The findings, in detail` — `### 01. [title] — confidence NN` per finding with an *Engages:* line naming each principle + relation |
| `Finding.principle_relations` | matrix-row dots + the rail's ENGAGES list (relation expressed by dot color; names only, no relation text) | `*Engages:* violates Social justice · strains Dignity, Subsidiarity` |
| `Finding.code_evidence[]` | `<figure>` with a `file:line` caption bar (+ language tag + copy affordance) and a syntax-highlighted `<pre><code>` | fenced code block ```` ```lang ```` with a `Location:` line |
| `Finding.citations[]` | under a small "From *Magnifica Humanitas*" label: the §-ref hung in the gutter, the verbatim quote in italic serif, the gloss beneath | `> §N "quote"` blockquote, then `> — gloss` |
| `Finding.behavior` / `.violation` | the card's running prose (factual account, then the moral reading) | **Behavior:** / **Violation:** paragraphs |
| `Finding.resembles` | small tag with gloss; omitted if null | `Resembles: {label} — {gloss}`; omitted if null |
| `Finding.remediation[]` | ✦ bullet list | `- ` bullet list under **Remediation** |
| `Finding.structural_note` | italic left-bordered aside; omitted if null/"" | **Structural note:** paragraph; omitted if null/"" |
| `mitigations[]` | "What the system does well" closing section (✓ bullets) | `## What the system does well` list |
| `dropped[]` | "Dropped and consolidated" list with mono metadata (`conf NN · reason …`); `merged_into:F1` → "merged into finding 01" (linked) | same list, same translation |
| `scope_limits[]` | "Limits of this audit" muted list | `## Out of scope and acknowledged limits` list |
| navigation | persistent left mini-nav (synth / index / 01..NN / notes) on wide viewports; footer wayfinding line | the heading hierarchy carries navigation |
| footer | "This audit was conducted using the *Magnificent Humanity Audit* agent skill made by Cache Atelier." — skill name → the GitHub release, Cache Atelier → cacheatelier.work (new-tab) | `## Methodology note` with the same attribution + links |

Empty arrays and null optionals **omit** their block entirely (no empty headings). A principle no finding engages still gets its matrix column (unmarked) and its line in the Markdown aggregate; `verdict_summary` is carried in the data (and shown in the Markdown aggregate line) even where the HTML matrix does not surface it.

The HTML renderer receives the object **injected verbatim** in place of the `/* @@REPORT_DATA@@ */` sentinel inside `<script type="application/json" id="report-data">` (escape `</` as `<\/`). Everything in the report is computed from the object at render time — the template contains no audit-specific content.

---

## A note on length and consolidation

A finished report typically carries **4–12 findings after consolidation** (see `workflow.md`, Phase 3b). Because the loci are organized by area, the same behavior surfaces under several passes; pre-consolidation overlap is expected and not a defect. If more than ~12 consolidated findings remain, that breadth is itself a signal to name in `synthesis.text`. Each finding is self-contained — a reader can engage one without the others.
