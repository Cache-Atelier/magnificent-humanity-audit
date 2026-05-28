# Audit Report Template

This template defines the structure of the audit's output. Follow it precisely. The precision is part of the audit's authority.

---

# *Magnifica Humanitas* Audit: [System Name]

**Date:** [YYYY-MM-DD]
**Scope:** [What was audited — a repository, a specific feature set, a product as a whole, a behavioral account]
**Evidence base:** [Source code / partial code / product documentation / behavioral account / mixed]
**Principles in scope:** [All seven / specific subset, with reason]

---

## Synthesis

[200–400 words. Not a summary; a judgment. Names the principles most centrally honored and violated. Answers the encyclical's litmus question from §85: does this system truly help individuals and peoples become more humane and fraternal, while respecting our common home and future generations? Frames the answer through the central image of §7–10 and §90: toward Babel or toward the rebuilt Jerusalem? The synthesis does not introduce new findings; it weighs the case the findings have built.]

---

## Findings

Found [N] anthropological bugs (confidence ≥80):

### 1. [Brief description of the finding] — confidence [80-100]

**Location:** [file:line / feature / flow / behavior — be specific]

**Behavior:** [What the system functionally does. The factual basis of the finding. Two to four sentences.]

**Violation:** [How the behavior contradicts the principle. Cite the principle by name and the specific paragraphs of *Magnifica Humanitas*. Where helpful, quote a phrase of fifteen words or fewer. Three to six sentences.]

**Resembles:** [diagnostic label if applicable: technocratic-paradigm, transhumanism, or posthumanism. With a brief gloss explaining the application. Optional — not every finding will warrant a label.]

**Remediation:**
- [Tactical fix 1 — specific, actionable]
- [Tactical fix 2 — specific, actionable]
- [Tactical fix 3 — specific, actionable]

**Structural note:** [Optional. When the remediation requires changes beyond the engineering team's scope — business model, organizational strategy, regulatory environment — name this honestly. The finding stands; the structural note acknowledges the dependency.]

---

### 2. [Next finding]

[Same structure.]

---

[Continue for each finding. Findings are numbered consecutively. Each is self-contained — the reader can engage one finding without reading the others.]

---

## Out of scope and acknowledged trade-offs

[Where the evidence was partial, where the user noted prior trade-offs the audit accepted, where assumptions were made. Be honest about the audit's limitations. This section can be brief.]

---

## Methodology note

[1–2 sentences naming that this audit was conducted using the Magnificent Humanity Audit skill, applying the seven principles of Catholic Social Doctrine as articulated in Pope Leo XIV's encyclical *Magnifica Humanitas* of 15 May 2026. Provide the encyclical URL for readers who want to consult the source.]

---

# Notes on using this template

## Formatting

- Use markdown headings as shown above (`#`, `##`, `###`). The hierarchy matters for legibility.
- Findings are numbered. Number them in the order they appear; the order is editorial — typically grouped by principle or by severity-of-evidence, not chronological by audit pass.
- Confidence scores are integers from 80 to 100. Do not include findings below 80.
- Cite the encyclical as "*Magnifica Humanitas* §X" with italics where formatting permits.
- Quote directly only when the exact wording matters. Quotes stay under 15 words. Paraphrase otherwise.

## Tone

- Diagnostic, not moralizing. The audit names what is, with evidence.
- Frank but not antagonistic. Per §14 of the encyclical, "a clarity that sheds light and a frankness that unlocks new possibilities."
- The audit assumes good faith on the part of the developers. The technocratic paradigm is structural; most engineers operate within it without intending it.
- Avoid hedging that undermines confidence claims. If the audit reports a 90-confidence finding, the language should be direct.

## What to include in each section

**Behavior** is factual. What does the code do? What does the system do? This section should be defensible against the response "that's not actually what the code does."

**Violation** is the moral reading. Why does this behavior contradict the principle? Cite specific paragraphs. The strength of the violation section depends on the precision of the citation. Vague gestures to "human dignity" are weak; "*Magnifica Humanitas* §51, which names as 'particularly insidious' the ideology that persons must earn their worth," is strong.

**Resembles** is optional. Use a diagnostic label only when it adds clarity. Most findings will use technocratic-paradigm. Some will warrant transhumanism or posthumanism. Some will warrant no label.

**Remediation** is tactical. What specifically can be changed? Code-level, product-level, process-level changes. Each item should be implementable. "Improve the recommendation algorithm" is too vague; "Add a community-health signal to the ranking model, weighted to penalize content scored high on conflict-prediction" is actionable.

**Structural note** acknowledges when tactical fixes are insufficient. If a finding is fully explained by a business model the engineering team cannot change, the structural note says so. This is honest about scope, not an escape from naming the violation.

## Length

A typical full audit produces 4–12 findings in this format. Audits with more than 15 findings are usually either insufficiently filtered (lower the confidence threshold higher) or evidence of a system in serious tension with the principles across many surfaces (which is itself worth saying explicitly in the synthesis).

Each finding is typically 200–400 words. Some are shorter when the evidence is direct and the violation is clean. Some are longer when the behavior is complex or the structural note requires development.

The synthesis is 200–400 words. Resist the temptation to make it longer. Its job is to weigh the findings, not to restate them.
