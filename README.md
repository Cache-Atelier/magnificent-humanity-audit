# Magnificent Humanity Audit

> A skill for finding **anthropological bugs** in software — defects in the implicit account of the human person that a system's functional behavior enacts.

An [AgentSkills](https://agentskills.io)-compliant skill for auditing digital systems against the seven principles of Catholic Social Doctrine as articulated in Pope Leo XIV's encyclical *Magnifica Humanitas* (15 May 2026), *On Safeguarding the Human Person in the Time of Artificial Intelligence*.

An *anthropological bug* is a security bug's analogue in the moral register: a correctness defect, but against an account of the human person rather than against a threat model. The skill names them, cites the encyclical paragraph that grounds the citation, scores confidence (0–100, threshold 80), and proposes concrete remediation. The structure mirrors familiar code-review patterns; the encyclical functions as the cited authority that findings are checked against.

**Author:** Cache Atelier
**License:** [MIT](LICENSE)
**Encyclical:** https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html
**Skill spec:** [AgentSkills](https://agentskills.io/specification) — works with any agent that implements the spec, including Claude Code, Hermes, and others.

## Install

### With the AgentSkills CLI (any AgentSkills-compatible agent)

```bash
npx skills add git@github.com:cache-atelier/magnificent-humanity-audit.git
```

Or via HTTPS:

```bash
npx skills add https://github.com/cache-atelier/magnificent-humanity-audit
```

### Manual install

Clone this repo into your agent's skills directory. The agent's entry point is `SKILL.md`; the agent will load the rest on demand.

- **Claude Code:** `~/.claude/skills/magnificent-humanity-audit/`
- **Codex CLI:** `~/.codex/skills/magnificent-humanity-audit/`
- **OpenCode:** `~/.opencode/skills/magnificent-humanity-audit/`
- **Hermes:** the equivalent skills path for your installation

```bash
git clone https://github.com/cache-atelier/magnificent-humanity-audit.git ~/.claude/skills/magnificent-humanity-audit
```

### Pack your own `.skill` file

If your agent (or an offline workflow) needs a single-file `.skill` package, pack the repo from its parent directory so the archive contains a top-level folder named after the skill:

```bash
cd ..
zip -r magnificent-humanity-audit.skill magnificent-humanity-audit \
  -x "magnificent-humanity-audit/.git/*" \
  -x "*.DS_Store"
```

### Validate

Using the official AgentSkills reference validator:

```bash
pip install -e git+https://github.com/agentskills/agentskills.git#subdirectory=skills-ref
skills-ref validate /path/to/magnificent-humanity-audit
```

## Audience

The audit is appropriate for:

- Developers wanting to check their own systems against an explicit moral framework
- Catholic institutions evaluating digital tools for use
- Journalists investigating platform behavior
- Parents and schools assessing children's products
- Researchers studying platform ethics
- Anyone concerned with how digital systems form the persons who use them

## Triggering

The skill triggers on requests like:

- "Find the anthropological bugs in this codebase"
- "Audit this codebase against Catholic Social Doctrine"
- "Run a *Magnifica Humanitas* audit on this app"
- "Is this system respecting human dignity?"
- "Catholic social teaching audit"
- "Ethics audit / values report on this platform"

It works equally well with full source code access, partial code, product documentation only, or a user's behavioral account of using the system. The encyclical's principles concern functional behavior; the evidence base can be whatever the auditor has.

## What this skill is and is not

**The skill is** a structured reading of a system's functional behavior for anthropological bugs — measured against an explicit, magisterial moral framework. Its findings are evidence-grounded, paragraph-cited, and concretely actionable. Its authority comes from the encyclical, not from the skill itself. It is closer in genre to a security audit than to a manifesto: same diagnostic posture, same confidence-thresholded findings, same orientation toward remediation rather than denunciation. The threat model is different — the audit reads against a flourishing model of the human person rather than against an attacker — but the discipline is the same.

**The skill is not** a substitute for moral judgment, a guarantee of comprehensiveness, or a tool for political attack on systems. It does not impute bad faith. It treats every finding as an opportunity for reform.

The skill is explicitly Catholic in its framework. Diagnostic findings can travel to non-Catholic readers (the diagnostic labels and remediation steps work regardless of tradition); the evaluative authority does not pretend to be neutral. *Magnifica Humanitas* is the cited authority because the encyclical is the authority. Readers who do not share the Catholic framework can still engage the findings; the audit does not require their assent to its grounding.

## A note on posture

Per *Magnifica Humanitas* §14, the encyclical's posture is one of "a clarity that sheds light and a frankness that unlocks new possibilities. We cannot condone naïve enthusiasms, nor fuel unfounded fears." The audit aims for this posture — toward, in the encyclical's central image, the rebuilt Jerusalem rather than the Tower of Babel.

## The encyclical

*Magnifica Humanitas* was promulgated on the 135th anniversary of *Rerum Novarum*. It is the magisterium's most extensive treatment of artificial intelligence, the digital revolution, and Catholic Social Doctrine in the technological age. The encyclical applies the seven principles of Catholic Social Doctrine to the new conditions of the digital age and offers a positive vision — the "civilization of love" — against the technocratic paradigm and against the underlying narratives of transhumanism and posthumanism.

This skill exists to translate the encyclical's analysis into operational practice — to make the framework directly applicable to the work of building, evaluating, and reforming the digital systems that increasingly shape contemporary life.

## Repo structure

The repo is the skill — flat AgentSkills layout, `SKILL.md` at root.

```
magnificent-humanity-audit/        # repo root = AgentSkills payload
├── README.md                      # this file
├── SKILL.md                       # agent entry: frontmatter + methodology
├── LICENSE                        # MIT
├── encyclical-reference.md        # paragraph-by-paragraph map
├── workflow.md                    # procedural discipline
├── figures-cited.md               # who Pope Leo XIV cites
├── principles/                    # the seven principles
├── loci/                          # nine areas of evidence (+ warfare appendix)
├── diagnostic-labels/             # technocratic-paradigm, transhumanism, posthumanism
└── templates/
    └── report.md                  # output template
```

## Contributing

Issues and pull requests welcome. The skill's content is constrained by the encyclical: findings, principles, loci, and diagnostic labels follow the encyclical's own vocabulary and paragraph structure. Contributions that sharpen precision, correct citations, or improve the auditor's reading discipline are especially welcome.
