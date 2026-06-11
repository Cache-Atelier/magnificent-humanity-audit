# Audit Workflow

This file describes the procedural backbone of a *Magnifica Humanitas* audit: the reading passes, the evidence log, and the motion from observation to finding. Load this file before beginning a real audit. The discipline matters more than the framework — the framework only works if the audit reads patiently, records evidence, and writes findings only when confidence is high.

## What the audit is and is not

**The audit is** a structured reading of a system's functional behavior against the seven principles of Catholic Social Doctrine as articulated in *Magnifica Humanitas*. It produces bug-report-style findings, each citing specific paragraphs of the encyclical as authority, with confidence scoring and concrete remediation steps.

**The audit is not** a value judgment on the system's authors, a political statement, a comparison to other systems, or an attempt to "win" against the platform. It is closer in genre to a security audit: precise, evidence-grounded, focused on the specific behaviors that produce specific concerns.

## Inputs

The agent should establish, before reading anything else, what evidence base the audit will draw from. Common cases:

- **Full source code access.** The user has shared a repository. Run the seven passes against the codebase.
- **Partial code access.** The user has shared specific files, screenshots of code, or a description. Work from what is available; note in the report where evidence was limited.
- **Product description only.** The user has described a platform, app, or system without code access. Work from product documentation, public APIs, the user's account of use, and what can be observed. Findings will lean on behavioral evidence rather than code locations; that is fine — the encyclical's principles are about functional behavior, not implementation detail. Concrete tactics when source is unavailable:
  - Observe notification timing, content, and frequency directly
  - Read the platform's own documentation about how recommendations, feeds, or matching work
  - Read transparency reports, regulatory filings, and prior independent research
  - Test the system as a user and note what it does to attention, choice, and inner state
  - Ask the user-of-the-audit what their lived experience of the system has been
  
  Findings derived this way are valid. Cite the evidence honestly ("observable behavior" rather than "code at file:line"), and let the confidence score reflect the evidence's strength.
- **Mixed evidence.** Most real audits are this. Combine sources; weight code evidence higher when both code and behavior are available.

The agent should also establish, before starting, what the user wants from the audit:
- A full audit covering all seven principles, or a focused audit on specific concerns?
- Long-form report or condensed?
- Are there sections of the system the user wants explicitly in or out of scope?

If any of this is genuinely unclear and would significantly change the audit, the agent asks one or two clarifying questions before starting. The default if there is no ambiguity: full audit, full report, all principles in scope.

## Phase 1 — Survey

Before doing principle-by-principle reading, build a model of the system.

**Read in this order:**

1. **README and top-level documentation.** What does the system describe itself as? What does it claim to do? What is its stated audience and purpose?
2. **Package manifests and dependencies.** `package.json`, `requirements.txt`, `Gemfile`, `pubspec.yaml`, `go.mod`, etc. Dependencies often predict findings. Look for: analytics SDKs (Mixpanel, Amplitude, Segment), session replay tools (FullStory, LogRocket, Hotjar), ad networks (especially behavioral targeting), A/B testing frameworks, attention-tracking, behavioral retention services, telemetry libraries.
3. **Configuration defaults.** `config/`, `settings.py`, environment variables. What does the system default to? What is opt-in vs. opt-out?
4. **The top-level route, controller, or entry-point structure.** What are the system's surfaces? What does it offer the user? What does it ask of the user?
5. **The user data model.** What does the system store about each user? What fields? What relationships? What derived data, scores, or profiles?

This pass takes 10–20% of the audit's reading time. Its output is a mental model: *I now know what this system is.* Without this model, the principle-by-principle passes will be ungrounded.

**A note on marketing copy.** The encyclical's §9 is operationally important here: "technology is never neutral, because it takes on the characteristics of those who devise, finance, regulate and use it." But that includes the characteristics the system functionally has, not the characteristics it claims. Marketing copy is not evidence. Stated values are not evidence. What the code does is evidence.

## Phase 2 — Read against the principles

The bulk of the audit. Walk the nine loci listed in `loci/`. For each functional behavior identified, ask of each principle whether the behavior honors, violates, or is silent. Maintain an evidence log throughout.

### The seven recommended reading passes

Each pass focuses on one principle. The passes can be done in any order; the order below is the one *Magnifica Humanitas* uses. A full audit does all seven; a focused audit may do a subset.

1. **Dignity pass.** Read the system asking: how does it differentiate among users? Are dignity-essential goods (recourse, support, ability to be heard, basic functionality) gated by anything other than the user being a human? Use `principles/1-human-dignity.md`.

2. **Common-good pass.** Read the system asking: what aggregate effect does this system have? What does it measure at the community level? Use `principles/2-common-good.md`.

3. **Universal-destination-of-goods pass.** Read the system asking: who owns the data, the algorithms, the platform capacity? Is what should be common treated as private? Use `principles/3-universal-destination-of-goods.md`.

4. **Subsidiarity pass.** Read the system asking: who makes decisions about the user, and how accountable is that decision-making? Where does the platform act as if it were the highest authority on questions that should belong elsewhere? Use `principles/4-subsidiarity.md`.

5. **Solidarity pass.** Read the system asking: how does the system treat the bonds the user inhabits? Does it support them or exploit them? Does it consider future generations and populations beyond its current beneficiaries? Use `principles/5-solidarity.md`.

6. **Social-justice pass.** Read the system asking: who bears the costs and who reaps the benefits? Are vulnerable populations protected or exploited? Does algorithmic decision-making produce disparate harm? Use `principles/6-social-justice.md`.

7. **Integral-human-development pass.** Read the system asking the encyclical's litmus question from §85: does this help individuals and peoples become more humane and fraternal, while respecting our common home and future generations? Use `principles/7-integral-human-development.md`.

### Using the loci

The `loci/` directory contains nine files (plus an optional warfare appendix) describing where in code or product to look. They are organized by area of the system rather than by principle, because the principles cut across areas. The recommended pattern:

- During a principle pass, refer to the loci that are most relevant to that principle. The dignity pass touches loci 1, 2, 4, 7, 8 most heavily. The common-good pass touches loci 4, 5, 6 most heavily. And so on.
- Each locus file lists the principles it most often engages, so the agent can read the loci either by principle or by area.

### The evidence log

Maintain an evidence log throughout reading. The format is a markdown file in the working directory. Each entry has:

```
## [Brief observation]
Location: [file:line / feature / flow]
Behavior: [what the system does]
Principle(s) potentially engaged: [list]
Code/quote candidates: [snippet(s) worth quoting + the paragraph number(s) whose verbatim text fits]
Evidence strength: [strong / moderate / partial]
Notes: [anything that affects interpretation]
```

The `Code/quote candidates` line pre-stages the structured finding: capturing the snippet and the paragraph number at observation time makes the later `code_evidence[]` and `citations[]` fields cheap to fill, and a reminder to pull the **verbatim** quote from that paragraph's note in `paragraphs/`.

The evidence log is not the report. It is a scratchpad. Many entries in the log will not become findings — some because the evidence is too partial, some because on reflection the principle doesn't quite apply, some because the behavior is more defensible than first appeared. The discipline is: record observations as they appear, weigh them later.

The motion from log to finding is the next phase.

## Phase 3 — Write findings

From the evidence log, identify the entries that meet the bar for inclusion. The bar:

- **Confidence ≥ 80.** If you are not confident the violation is real, do not include the finding. Use the confidence scale in `SKILL.md`.
- **Location is specific.** A file, function, route, flow, screen, behavior, or documented mechanic — not "the system in general."
- **The principle is cited with paragraph.** Not "human dignity" but "*Magnifica Humanitas* §51." When in doubt about which paragraph, consult `encyclical-reference.md`.
- **Remediation is concrete.** What can be changed? Tactical first; structural note where applicable.
- **The finding survives a charitable reading.** Could a reasonable defender of the system explain this away? If yes, drop the confidence score or drop the finding entirely.

Each finding is authored as a structured `Finding` object — its fields are defined in `templates/findings-schema.md`. Code evidence and encyclical citations are **discrete fields** (`code_evidence[]`, `citations[]`), not sentences buried in prose; `templates/report.md` shows the layout they render into. Pull each citation's verbatim quote (≤25 words) from the cited paragraph's note in `paragraphs/`. The format is precise; do not improvise.

### What to filter out

Apply these filter rules:

- **Pre-existing patterns the codebase has flagged as deliberate.** Comments, design docs, ADRs that name the choice and reason for it. If the system's authors have acknowledged a trade-off and explained it, that does not automatically excuse the violation, but it changes how the finding should be framed (and may reduce confidence).
- **Pedantic nitpicks.** Findings that depend on tiny interpretive choices rather than the system's actual functional behavior.
- **Findings that depend on assumptions about future use.** "If this system were later combined with X, then Y would be a violation." Audit what is, not what might be.
- **Findings already accounted for elsewhere.** Don't restate the same violation under multiple principles unless the principles genuinely engage different aspects.
- **Findings that confuse the system with the broader culture.** If the violation is fully attributable to the broader internet, the user's choices, or another actor, name that honestly and either drop the finding or reframe it to capture only what the system contributes.

### A worked example

Consider a hypothetical finding from an evidence log entry:

> ## Notification system uses variable-reward timing
> Location: `services/notifications/scheduler.ts:142-180`
> Behavior: Notification dispatch timing is partially randomized within configurable windows, with timing weights derived from a model that predicts user re-engagement probability.
> Principle(s) potentially engaged: integral human development (§170 on attention economy), solidarity (§76 on exploiting digital weakness), human dignity (§51 if users are treated as means)
> Evidence strength: strong — the model and the timing logic are both clearly present in code
> Notes: This is widespread industry practice. The fact that it's common does not change whether it violates the principle.

Moving this to a structured `Finding` (per `templates/findings-schema.md`):

```
{
  id: "F1",
  title: "Notifications are timed by a model that predicts user re-engagement, with variable-reward windows",
  confidence: 90,
  primary_principle: "integral_development",
  principle_relations: [
    { principle: "integral_development", relation: "violates" },
    { principle: "solidarity",           relation: "tension" },
    { principle: "dignity",              relation: "tension" }
  ],
  code_evidence: [
    { location: "services/notifications/scheduler.ts:142-180", language: "typescript",
      snippet: "const weights = reengagementModel.predict(user, candidateTimes);\nconst dispatchAt = sample(candidateTimes, weights); // randomized within window" }
  ],
  behavior: "Notification dispatch timing is partially randomized within configurable windows; the
    weights are derived from a model that predicts the user's likelihood of returning to the
    platform given a send time. The pattern is recognizable as variable-reward conditioning.",
  citations: [
    { paragraph: "§170",
      quote: "When business models thrive on human weakness, the person is treated as a means rather than as an end",
      gloss: "The scheduler operates on the user's attentional vulnerability to maximize the system's metric of return." }
  ],
  violation: "This violates integral human development. The notification model functions exactly as
    §170 describes: it optimizes the user's likelihood of return, not any good the user sought.
    The user's stated reasons for being on the platform play no role in the scheduling.",
  resembles: { label: "technocratic-paradigm",
    gloss: "the user's attention is treated as a resource to be optimally extracted; the user is the object of optimization, not its beneficiary." },
  remediation: [
    "Replace the re-engagement-prediction model with a scheduler that respects user-stated timing preferences",
    "Default users out of non-essential notifications; require explicit opt-in per category",
    "Remove variable-window randomization; deliver at predictable, user-chosen times",
    "Track user-reported satisfaction with notifications and treat decreases as failures even when re-engagement rises"
  ],
  structural_note: "Likely non-local: if platform revenue scales with attention extracted, the
    engineering fix is incomplete without a revenue model that does not depend on attention
    extraction (cf. §95 on platform-power concentration)."
}
```

Note what the structure buys: the §170 quote is **verbatim and ≤25 words**, taken from that paragraph's note in `paragraphs/`; `code_evidence` and `citations` are discrete fields, so both the HTML and Markdown renderers show a real code block and a blockquote rather than a wall of prose. The `principle_relations` carry the judgment per principle — the behavior *violates* integral human development and *strains* solidarity and dignity (the finding has no standalone verdict; relations are what the matrix and the rail render). Confidence is 90 because the mechanism is unambiguously present and §170 is direct.

## Phase 3b — Consolidate

Because the loci are organized by area, the same underlying behavior surfaces under several reading passes — the notification scheduler above would also be caught under telemetry and under engagement design. Pre-consolidation overlap is expected; leaving it unmerged is the defect. After verifying findings:

1. **Merge** findings describing the same underlying behavior-and-violation into one — combine their code locations, keep the strongest and most accurate citations — and record each merged-away finding in `dropped[]` with `reason: merged_into:<id>`.
2. **Assign** each survivor its `principle_relations` — the principle it most centrally engages first (this becomes `primary_principle`), then every other principle it engages, judging each relation: `violates` (the behavior contradicts the principle) or `tension` (it strains it — displayed as "strains").
3. **Name the breadth.** 4–12 consolidated findings is typical; more than ~12 is a signal of system-wide tension to state in the synthesis, not a filtering failure to hide.

A locus-organized reading routinely produces roughly twice the findings that survive consolidation — for example, a recent audit yielded 21 verified findings that consolidated to 10. That ratio is the process working.

## Phase 4 — Synthesize

After all findings are written, produce a synthesis at the top of the report. The synthesis:

- Is no more than 250–400 words for a typical audit
- Names the principles most centrally violated and strained
- Answers the encyclical's litmus question from §85 in evidence-grounded form
- Frames the answer through the encyclical's central image (§7–10, §90): toward Babel or toward the rebuilt Jerusalem? — and sets `synthesis.verdict_image` accordingly
- Does not introduce new findings — only weighs what is already in the report

A synthesis is not a summary; it is a judgment. The audit has built the case in the findings. The synthesis says what the case adds up to. (The renderers place a data-computed stat line beside the verdict — findings counted, principles by aggregate verdict — so the synthesis prose never needs to recite counts.)

Then derive the **per-principle verdicts**: for each of the seven principles, set `verdict` (`violates` / `tension` / `honors`) from the findings' `principle_relations` and write a one-line `verdict_summary`, using the derivation rule in `templates/findings-schema.md`. The synthesis is the overarching judgment; the findings × principles matrix makes it concrete principle by principle.

## Phase 5 — Output

Assemble the structured `report` object (per `templates/findings-schema.md`), then render it two ways:

- **Default — the HTML artifact.** Take `templates/report.html`, replace its `@@REPORT_DATA@@` sentinel with the `report` object serialized as JSON, and write the result as a self-contained `.html` file. Escape any `</` sequence in the embedded JSON (so a code snippet containing `</script>` cannot break the page). Write no presentation markup — only the data; the template's own CSS and JS render everything (the synthesis verdict row and stat line, the findings × principles matrix, the reading-order ordinals, the finding cards with their marginalia rails, code highlighting, the themes, navigation, and print styles) from the object at load time.
- **Secondary — the Markdown copy.** Render the same object into the `templates/report.md` layout and save it alongside, for sharing or LLM upload — same content, same vocabulary (violates/strains), same ordinals.

If the user requests a shorter format, condense `behavior` and `remediation` while keeping each finding's principle relations, paragraph citations, confidence, and remediation, plus the findings × principles matrix. Never report findings below confidence 80. The audit's authority depends on the precision of its presentation.

## A note on humility

The encyclical itself is humble about ethical pronouncement: per §23, the Church "does not claim to offer a definitive opinion" on every specific question. The audit should follow this disposition. Where the application of a principle is genuinely contested, say so. Where evidence is partial, lower the confidence score. Where the finding rests on inference, name the inference. The authority comes from precision, not assertion.

The encyclical's posture in §14 is also instructive: avoid "humiliating or antagonistic words, opting rather for a clarity that sheds light and a frankness that unlocks new possibilities. We cannot condone naïve enthusiasms, nor fuel unfounded fears." The audit speaks with clarity, not with heat.
