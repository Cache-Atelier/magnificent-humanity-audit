# Audit Report Template — Markdown

This template defines the **Markdown** rendering of an audit. It is the *secondary* artifact (for sharing or LLM upload); the default is the styled HTML in `templates/report.html`. Both render the **same structured object**, defined in `templates/findings-schema.md` — field names are authoritative there; this file defines layout only. The two renderings must carry identical content.

Follow the structure precisely. The load-bearing rules: **code evidence is fenced code blocks**, **encyclical citations are blockquotes**, **findings are numbered in reading order and never grouped under principles** — the findings × principles table carries the cross-relations.

---

# An anthropological audit of [system_name]

This reads the system against the seven principles of Catholic social doctrine set out in the encyclical *Magnifica Humanitas*, asking what its workings imply about the human person.

**Date:** [YYYY-MM-DD]
**Scope:** [what was audited]
**Evidence:** [Source code / Partial code / Product documentation / Behavioral account / Mixed evidence]
**Repository:** [repo_url — omit this line if null]

---

## Synthesis

**[Toward Babel / Toward the rebuilt Jerusalem / Between Babel and Jerusalem]** — [N] findings · of 7 principles: [X] violated, [Y] strained

[200–400 words. Not a summary; a judgment. Names the principles most centrally violated and strained. Answers §85's litmus question in evidence-grounded form, and frames the whole through the §7–10 / §90 image. Weighs the case the findings build; introduces no new findings.]

*(The verdict tag is `synthesis.verdict_image`; the stat line is computed from the data — findings counted, principles by aggregate verdict. Findings carry no verdict counts of their own.)*

---

## The findings, by principle

One row per finding, one column per principle. `●` = violates that principle · `◐` = strains it · `·` = not engaged.

| # | Anthropological bug | Dig | C.G. | U.D. | Sub | Sol | S.J. | I.D. | conf |
|---|---|---|---|---|---|---|---|---|---|
| 01 | [title, linked to the finding below] | ◐ | ◐ | · | · | · | · | ● | 88 |
| 02 | … | ● | · | · | ◐ | · | ● | · | 86 |

Column key — Dig: The dignity of the human person §48–58 · C.G.: The common good §59–64 · U.D.: The universal destination of goods §65–67 · Sub: Subsidiarity §68–72 · Sol: Solidarity §73–76 · S.J.: Social justice §77–81 · I.D.: Integral human development §82–85.

**By principle:** [for each of the seven, in encyclical order: `Name — violated / strained / —` with `verdict_summary` in brief where it earns its line. Principles no finding engages render unmarked (`—`); "honors" is never displayed as a rating.]

---

## The findings, in detail

Findings appear **once each**, in reading order: findings carrying any *violates* relation first, then the rest, ties broken by descending confidence. Number them `01`..`NN` in that order; the stable ids (`F1`…) appear nowhere in the rendered text.

### 01. [title] — confidence [80–100]

*Engages:* violates [principle name(s)] · strains [principle name(s)] *(from `principle_relations`, primary first; omit either clause if empty)*

**Code evidence:**

```[language]
[snippet]
```
`Location: [file:line / flow]`

[Repeat the fenced block + Location line for each `code_evidence[]` entry. Omit the whole block if the array is empty — e.g. a purely behavioral finding.]

**Behavior:** [factual account of what the system does — the defensible basis.]

**From *Magnifica Humanitas*:**

> §N "[verbatim quote ≤25 words]"
> — [gloss]

[Repeat the blockquote for each `citations[]` entry. If a citation has no verbatim quote, render `> §N — [gloss]` without quotation marks.]

**Violation:** [the moral reading: how the behavior contradicts the cited paragraphs — named per principle, matching the relations above.]

**Resembles:** [label] — [gloss]   *(omit this line entirely if `resembles` is null)*

**Remediation:**
- [tactical fix 1]
- [tactical fix 2]
- [tactical fix 3]

**Structural note:** [when the fix is non-local — business model, org telos, regulation. Omit the line if null/empty.]

---

[Next finding: `### 02. …` — one flat list, no per-principle sections.]

---

## What the system does well

[Renders `mitigations[]`. Each: a credited honoring behavior, named honestly. Omit this whole section if the array is empty.]

- **[title]** ([principle]) — [note]

---

## Dropped and consolidated

[Renders `dropped[]` — transparency about what was merged or fell below threshold. Omit if empty. Translate `merged_into:F1` to "merged into finding 01" using the display ordinals.]

- **[title]** — conf [NN / —] — [below threshold / merged into finding 01 / charitable reading / out of scope]

---

## Limits of this audit

[Renders `scope_limits[]`. Where the evidence was partial, where assumptions were made, where decisive consumers were out of repo. Be honest about the audit's limits. Omit if empty.]

---

## Methodology note

This audit was conducted using the [Magnificent Humanity Audit](https://github.com/Cache-Atelier/magnificent-humanity-audit/releases/latest) agent skill made by [Cache Atelier](https://cacheatelier.work), applying the seven principles of Catholic Social Doctrine as articulated in Pope Leo XIV's encyclical *Magnifica Humanitas* (15 May 2026). Findings are reported only at confidence ≥80. The encyclical is at https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html.

---

# Notes on using this template

## Formatting

- Headings: `#` title, `##` major sections, `###` findings (`### 01. [title] — confidence NN`). There are **no per-principle heading sections** — the table carries the by-principle view.
- **Code evidence renders as fenced code blocks** with a language tag, each followed by its `Location:` line. **Citations render as blockquotes** under a "From *Magnifica Humanitas*" lead-in, with the verbatim `§N "quote"` and a `— gloss` line. This is the point of the structured fields; do not flatten them back into prose.
- Confidence is an integer 80–100 in the finding heading. Never include findings below 80.
- Verbatim encyclical quotes are **≤25 words**, copied exactly from the paragraph's note in `paragraphs/`. Paraphrase otherwise and cite the paragraph.
- Cite as "*Magnifica Humanitas* §X" (or "§X" inside a finding where the context is established). Ranges use an en-dash: "§170–172".
- In finding **titles**, prefer spaced en-dashes (" – ") over em-dashes.
- **Inline code:** identifiers, paths, functions, flags, and field names in prose are wrapped in backticks (`` `device_id` ``, `` `ranking_scorer.rs:125-173` ``) — in every prose field, per `findings-schema.md`. No other inline markup (no bold/italic) in prose fields.

## Vocabulary

- A finding **violates** or **strains** a principle — always *in relation to* a principle, never in the abstract. A finding has no standalone verdict; do not write "this finding: violates."
- The data key `tension` always renders as **"strains/strained"**. The phrase "in tension" does not appear in a rendered report.
- "Honors" is never displayed as a rating — a bug-finding audit awards no honors. A principle no finding engages is simply unmarked.

## Tone

- Diagnostic, not moralizing. Name what is, with evidence. Frank but not antagonistic (§14).
- Assume good faith of the developers; the technocratic paradigm is structural. Most engineers operate within it without intending it.
- Don't hedge in a way that undermines a stated confidence. A 90-confidence finding is written directly.

## What each field carries

- **Behavior** is factual — defensible against "that's not what the code does."
- **Citations** ground the moral reading; precision of the paragraph is the source of the finding's force. A verbatim ≤25-word quote beats a paraphrase.
- **Violation** is the moral reading that ties behavior to the cited paragraphs, principle by principle.
- **Resembles** is optional; use a diagnostic label only when it adds clarity. Most findings will be technocratic-paradigm; some warrant transhumanism or posthumanism; some none.
- **Remediation** is tactical and implementable. **Structural note** names when tactical fixes are insufficient — honest about scope, not an escape from the finding.

## Length

A typical full audit produces **4–12 findings after consolidation** (`workflow.md`, Phase 3b). More than ~12 is usually either insufficient consolidation or a system in tension across many surfaces — say which in the synthesis. Each finding is typically 150–350 words across its fields; some shorter when the evidence is direct, some longer when the structural note needs development. The synthesis is 200–400 words: it weighs the findings, it does not restate them.
