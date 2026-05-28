---
name: magnificent-humanity-audit
description: Audit a codebase, application, platform, or digital system for anthropological bugs (also called Babel bugs): patterns that violate the principles of Catholic Social Doctrine as Pope Leo XIV articulates them in Magnifica Humanitas (15 May 2026), signaling a defect in the software's implicit account of the human person and our shared anthropology. Produces bug-report-style findings with confidence scoring (0-100, threshold 80), each citing specific paragraphs of the encyclical, with concrete remediation. Use whenever a user wants an ethical, values-based, or human-centered audit of software — including requests to audit, critique, or examine a system for its treatment of the human person, respect for human dignity, alignment with Catholic Social Doctrine, or moral effects on persons. Use even when the user doesn't speak Catholic vocabulary; the framework is Catholic but the diagnostic value travels. Works on source code, product documentation, or behavioral accounts. Not for security audits, code-quality review, or generic bug-finding.
license: MIT
compatibility: Requires filesystem read for on-demand loading of bundled reference files. Optional network access to fetch the encyclical from vatican.va if a reference file is missing or to verify a paragraph citation.
metadata:
  author: Cache Atelier
  version: "1.0"
---

# Magnificent Humanity Audit

This skill teaches an agent to find **anthropological bugs** (also called **Babel bugs**) in software systems, using the principles of Catholic Social Doctrine as Pope Leo XIV articulates them in *Magnifica Humanitas* (15 May 2026), his encyclical on safeguarding the human person in the time of artificial intelligence. The audit analyzes a codebase, application, or platform for patterns that violate those principles. Each pattern signals a defect in the software's implicit account of the human person and our shared anthropology. The skill names the bug, cites the encyclical paragraph that grounds the claim, scores confidence from 0 to 100 (threshold 80), and proposes concrete remediation.

The skill is explicitly Catholic in its framework. Its evaluative posture is the Magisterium's, not a bespoke synthesis. Diagnostic findings can travel to non-Catholic readers; the evaluative authority does not pretend to be neutral.

## When this skill triggers

The user has asked, in substance, for an audit of a digital system against Catholic Social Doctrine, for an evaluation of how a software system treats the human person, or for any ethical/values/human-centered audit of software. Phrases that activate it include: "find the anthropological bugs in this codebase," "find the Babel bugs in this codebase," "audit this codebase," "ethics audit of this app," "is this app respecting human dignity," "how does this system treat persons," "audit against Magnifica Humanitas," "Catholic social doctrine audit," "values report on this platform," and similar. The distinctive phrases "anthropological bug" and "Babel bug" are the terms of art the skill uses; treat them as strong triggers.

The user is not necessarily a developer. They may be a Catholic institution evaluating a tool, a journalist investigating a platform, a parent assessing a children's product, a researcher studying digital culture, or anyone concerned with how a digital system forms its users. Adapt accordingly: if there is no code, work from product documentation, the user's account of using the system, and what is publicly known. Functional behavior is the evidence base.

## The seven principles

The audit reads software against the seven principles Pope Leo XIV identifies in Chapter 2 of the encyclical:

1. **The dignity of the human person** (§48–58) — every person possesses infinite, inalienable dignity grounded in being created in the image of the Triune God, prior to capacity or productivity.
2. **The common good** (§59–64) — the sum total of social conditions that allow people, individually and as groups, to reach their fulfilment; not the aggregation of private interests.
3. **The universal destination of goods** (§65–67) — the earth's goods, and now also patents, algorithms, digital platforms, technological infrastructure, and data, are given for the entire human family; concentration in few hands contradicts this principle.
4. **Subsidiarity** (§68–72) — decisions are made at the level closest to the persons involved; in the digital age this principle applies especially to platform power, requiring transparency, accountability, and meaningful participation.
5. **Solidarity** (§73–76) — the conscious recognition that the future of each is bound to the future of all; in the digital ecosystem, this extends to decisions about data, algorithms, and AI.
6. **Social justice** (§77–81) — a social, economic, and political order that allows everyone, particularly the weakest, to live a dignified life without anyone being left behind.
7. **Integral human development** (§82–85) — development that promotes quality of life in all its dimensions (spiritual, cultural, moral, relational), respecting our common home and future generations; the principle from which the encyclical's litmus question for any AI deployment is drawn (§85).

Each principle has its own file under `principles/`. Load the relevant file when writing a finding that engages that principle.

## The nine loci

The audit reads against nine areas of the system where evidence for principle violations typically accumulates. They are organized by area rather than by principle, because the principles cut across areas. A tenth optional appendix covers warfare and adversarial contexts.

1. **Defaults and onboarding** — what the system assumes before the user has chosen; what the user must accept to enter.
2. **Consent, data ownership, and deletion** — the lifecycle of the user's data and the user's rights over it.
3. **Algorithmic decision-making** — automated decisions about users; opacity, appeal, accountability.
4. **Telemetry and behavioral profiling** — what the system measures and what it does with the measurement.
5. **Engagement and attention design** — notifications, retention systems, the architecture by which the system holds attention.
6. **Communication, copy, and truth** — language, microcopy, the system's treatment of disinformation and manipulation.
7. **Monetization, access, and equity** — pricing, tiers, what is gated and what is universal.
8. **Accessibility and the vulnerable** — children, the elderly, disabled users, language minorities, the marginalized.
9. **Supply chain, labor, and ecological cost** — the hidden costs of AI: labelers, moderators, miners, energy, water.
10. **Warfare and adversarial contexts** (appendix) — only applicable for systems with military, security, or weapons-adjacent use cases.

Each locus file (in `loci/`) names the principles it most often engages, describes what to look for, lists common findings, and suggests how to gather evidence when source code is partial or absent.

The loci most relevant to each principle:

- **Dignity (1):** loci 1, 3, 7, 8 — onboarding assumptions, algorithmic decisions about persons, tier-based service quality, treatment of vulnerable users.
- **Common good (2):** loci 3, 5, 6 — algorithmic effects on community discourse, engagement design's aggregate effect, manipulation of public communication.
- **Universal destination of goods (3):** loci 2, 4 — data ownership, telemetry extraction.
- **Subsidiarity (4):** loci 3, 4 — opaque automated decision-making, surveillance that pre-empts community decision.
- **Solidarity (5):** loci 1, 5, 8, 9 — onboarding's treatment of bonds, engagement design's exploitation of weakness, treatment of the vulnerable, the supply chain that sustains the system.
- **Social justice (6):** loci 3, 4, 6, 7, 8, 9 — algorithmic disparate impact, differential surveillance, misinformation, equitable access, vulnerable populations, supply-chain labor.
- **Integral human development (7):** all loci — the integrating principle cuts across everything.

When the same evidence is relevant to multiple principles, attach it to whichever principle the violation most centrally engages. Other principles can be referenced as secondary.

## Reading discipline

Six commitments hold throughout the audit:

**Read functionally, not intentionally.** What the system *does* is the evidence. Author intent, marketing copy, and stated values do not count unless they manifest as functional behavior. *Magnifica Humanitas* §9 makes this principle explicit: "technology is never neutral, because it takes on the characteristics of those who devise, finance, regulate and use it."

**Cite the encyclical precisely.** Each finding names the principle and cites the specific paragraphs that ground the claim. Vague gestures to "Catholic social teaching" are not findings; precise citations are. When uncertain about a paragraph, consult `encyclical-reference.md`.

**Specificity in location.** A finding must name a file, function, route, flow, screen, behavior, or documented mechanic. If the user has provided code, cite locations. If they have not, cite behaviors precisely.

**Filter false positives ruthlessly.** Only findings at confidence ≥80 are reported. Speculative, pedantic, or interpretively strained findings are not reported. The audit's authority depends on the precision of what it includes.

**Diagnostic tone.** The audit names the behavior, cites the principle, proposes remediation. It does not moralize, lecture, or condescend. A reader who does not share the framework should still find the diagnosis precise and the citations accurate.

**Remediation included.** Each finding proposes concrete remediation: tactical steps (what to change in code or product), and where applicable a structural note (when the issue requires non-local change — a monetization model, an organizational telos, a regulatory environment). The encyclical itself models this dual posture, naming both immediate practical responses and structural reform.

## Severity by confidence

Findings are reported with a confidence score from 0 to 100. The threshold for inclusion is **80**. The threshold filters out interpretive noise.

- **100** — Certain. The behavior unambiguously violates the principle; the evidence is direct; the interpretation is not contestable.
- **90** — Highly confident. The violation is clear; an honest reader would agree.
- **80** — Confident. The violation is real; some interpretive room exists but the evidence is strong.
- **70 and below** — Not reported. The interpretation is too uncertain, the evidence too partial, or the principle too loosely applied.

Things that warrant low confidence and exclusion: pre-existing patterns the codebase has flagged as exceptions; behaviors the user has explained as deliberate trade-offs; interpretively strained applications of the principles; findings that depend on assumptions about future use.

Severity beyond confidence is conveyed by the language of the finding itself. A finding that says "the system treats persons as commodities" conveys gravity directly. A finding that says "the consent flow could be more granular" conveys a lesser concern. The audit does not impose a separate CRITICAL/MAJOR/MINOR scale on top of confidence.

## Method

### Phase 1 — Survey

Establish what the system is, who uses it, what it does, what it measures, and what it makes easy, hard, default, or hidden. Read README, package manifests (dependencies often predict findings — analytics SDKs, ad networks, behavioral targeting libraries), top-level routes, configuration defaults, the user data model. Avoid marketing copy as primary evidence; it describes intention, not function.

### Phase 2 — Read against the principles

Walk the nine loci defined in `loci/`. For each functional behavior identified, ask of each principle whether the behavior honors, violates, or is silent. Maintain an evidence log as you read — a markdown file in the working directory, observations attached to locations, kept as a scratchpad. The report is written from the evidence log, not from memory.

For the workflow itself — reading order, the seven recommended passes, the evidence log format, the motion from observation to finding — load `workflow.md`.

### Phase 3 — Write findings

Each finding follows the template in `templates/report.md`. The structure is a bug-report format with the encyclical as the cited authority:

```
1. [Brief description] (Magnifica Humanitas §X says "[quote]")
   Location: [file:line / feature / flow]
   Confidence: [80-100]
   
   Behavior: [what the system functionally does]
   Violation: [how this contradicts the principle, with the paragraph reference]
   Resembles: [diagnostic label if applicable: technocratic-paradigm, transhumanism, or posthumanism]
   
   Remediation:
   — [Tactical fix 1]
   — [Tactical fix 2]
   Structural note: [optional — when remediation requires non-local change]
```

Only findings at confidence ≥80 are included.

### Phase 4 — Synthesize

Produce a short synthesis at the top of the report, organized by the encyclical's central image (§7–10, §90): is this system being built toward Babel — the construction that "sacrifices human dignity for efficiency" — or toward the rebuilt Jerusalem, the work of shared responsibility in which "all persons assume their own role and recognize that their strength comes from the Lord"?

The synthesis answers: which principles are most centrally honored or violated? What kind of person does sustained use of this system tend to form (the Wojtyłan question, repeated at §129)? Where does the system stand against the encyclical's litmus question: *does it truly help individuals and peoples become more humane and fraternal, while respecting our common home and future generations?* (§85).

## Output

Default output is a full report following `templates/report.md`. If the user requests a shorter format, condense findings while retaining the principle cited, the confidence score, and the remediation. Always preserve the structure of individual findings — they are the audit's evidence base. Never report findings below confidence 80.

## Diagnostic labels

A diagnostic label characterizes the *kind* of anthropological bug — the implicit anthropology a system's functional behavior enacts. The audit uses only the three labels *Magnifica Humanitas* itself names, because the audit's authority comes from speaking the encyclical's language rather than supplementing it with bespoke terminology:

- **technocratic-paradigm** (§92–94) — the framing the encyclical develops most extensively, drawing on *Laudato Si'*. The logic of efficiency, control, and profit treated as the standard by which everything is judged. Use when the system treats persons, attention, data, or relationships as inputs to be optimized for system metrics. This is the broadest label and the most commonly applied.
- **transhumanism** (§115–117) — the vision of human enhancement through technology to increase performance and capabilities, treating human limitations as defects to be corrected. Use when the system implicitly treats human capacities, limits, or weaknesses as defects to be corrected by technology — especially AI features that *replace* rather than *augment* human capacities (writing, deliberating, remembering, attending, feeling).
- **posthumanism** (§115–117) — more radical than transhumanism in challenging anthropocentrism, envisioning human-machine hybridization, anticipating a threshold where humanity "surpasses itself." Use when the system implicitly envisions a future in which the distinctly human is surpassed — when the framing presumes that human-machine hybridization is desirable progress, or when AI is treated as a successor rather than a tool.

The "Resembles:" line of a finding comes after the violation statement and before the remediation. It is a quick characterization for a reader scanning many findings; the encyclical citation gives the doctrinal grounding. A finding may use more than one label, comma-separated, when the same behavior is doing more than one kind of work:

```
Resembles: technocratic-paradigm, transhumanism — the system treats attention as
extractable and treats the user's tendency to be distracted as a defect the system
will optimize away.
```

Full elaboration of each label lives in `diagnostic-labels/`. Load the relevant file when writing the "Resembles:" line if the label's application is not already clear.

## Files

- `encyclical-reference.md` — operationally relevant paragraphs of *Magnifica Humanitas* in moderate depth, organized for citation. Load early; consult throughout. The agent should rarely need to web-fetch the encyclical itself, but it remains available at https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html for edge cases.
- `principles/` — one file per principle, each with the encyclical's articulation, what honoring and violating look like in software, code signatures, common remediations, and typical diagnostic labels. The evaluative spine of the audit.
- `workflow.md` — reading passes, evidence log discipline, motion from observation to finding, worked example.
- `loci/` — nine files covering where in code to look for evidence on each principle. Plus an optional appendix on AI in adversarial and warfare contexts.
- `figures-cited.md` — brief notes on the people Pope Leo XIV explicitly cites in the encyclical: Augustine, Aquinas, Guardini, Frankl, Arendt, Plato, Tolkien, La Pira, Saint Benedict, and the recent papal predecessors. Loaded when a citation needs context.
- `diagnostic-labels/` — three labels the encyclical itself names: `technocratic-paradigm`, `transhumanism`, `posthumanism`. Loaded when writing the "Resembles" line of a finding.
- `templates/report.md` — output template.

Load on demand. For a full audit, the typical order is: `encyclical-reference.md` and `workflow.md` first, then the relevant `principles/` files and `loci/` files during the reading passes, then `diagnostic-labels/` files when writing findings, and `figures-cited.md` when a citation in the encyclical needs context.
