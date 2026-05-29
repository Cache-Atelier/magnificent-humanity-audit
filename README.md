# Magnificent Humanity Audit

A skill that teaches your agent to find anthropological bugs (Babel bugs?) in software systems using the principles of Catholic Social Doctrine as laid out by Pope Leo XIV in his encyclical *Magnifica Humanitas*. This skill analyzes a codebase for patterns that violate these principles, signaling a defect in the software's implicit account of the human person and our shared anthropology. The skill names the bug, cites the encyclical paragraph that grounds the claim, gives a confidence score, and proposes remediation.

From §90 of the encyclical:

>We are called to reflect on the great “construction sites” of our era and ask: What are we building? As technological development rapidly transforms languages, relationships, institutions and forms of power, we believers must and can choose which projects to work on and in what manner, so as to safeguard and value the grandeur of humanity that has been given to us as a gift. This is a choice not only for our future but also for our present, since artificial intelligence and other emerging technologies are already part of our daily lives.

**Full Encyclical:** https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html


## How to use

Install the skill (see [Install](#install)), then ask your agent to audit something — a codebase, a product, or a behavioral account of using a system. The skill triggers on requests like:

- "Find the anthropological bugs in this codebase"
- "Find the Babel bugs in this codebase"
- "Audit this app against Catholic Social Doctrine"
- "Run a *Magnifica Humanitas* audit on this platform"
- "Is this system respecting human dignity?"
- "Ethics / values audit of this app"

You don't have to speak Catholic vocabulary; the framework is Catholic, but the diagnostic value travels. The agent returns a structured report with paragraph-cited findings, confidence scores, and remediation steps.


## What this skill is and isn't

The skill isn't a substitute for moral judgment, a guarantee of comprehensiveness, or a way to score political points against a platform. It doesn't impute bad faith. Every finding is treated as an opportunity for reform.

The framework is Catholic, and the audit doesn't pretend otherwise. Diagnostic findings can travel to readers who don't share the tradition (the labels and remediation steps work regardless), but the evaluative authority does not claim to be neutral. *Magnifica Humanitas* is cited because the encyclical is the authority. Readers outside the Catholic framework can still engage the findings on their own terms.


## Audience

Built with these readers in mind:

- Developers who want to check their own systems against an explicit moral framework
- Catholic institutions deciding whether to adopt a tool
- Journalists investigating how a platform actually behaves
- Parents and schools weighing a children's product
- Researchers studying platform ethics
- Anyone watching the way digital systems shape the persons who use them

The audit works on full source, partial source, product documentation alone, or a behavioral account of using the system. The encyclical's principles are about functional behavior, so the evidence base can be whatever the auditor has.


**Author:** [Cache Atelier](https://cacheatelier.work)
**License:** [MIT](LICENSE)
**Encyclical:** https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html
**Skill spec:** [AgentSkills](https://agentskills.io/specification) (works with any AgentSkills-compliant agent, including Claude Code, OpenCode, Hermes, and others)

## Install

*The best way to install is to simply give your agent the current url, but all standard skill pathways are also supported:*

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

### Claude Cowork and other hosted Claude environments

Download `magnificent-humanity-audit.skill` from the [latest release](https://github.com/Cache-Atelier/magnificent-humanity-audit/releases/latest) and drop it into your workspace's skill installer.

## Repo structure

The repo is the skill: flat AgentSkills layout, `SKILL.md` at root.

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
