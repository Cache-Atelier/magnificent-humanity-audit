# Diagnostic Label: posthumanism

## The encyclical's definition

*Magnifica Humanitas* §115–117 introduces transhumanism and posthumanism together, but with a distinction. §116 articulates posthumanism specifically:

> "Posthumanism, especially in its more radical forms, goes further: it challenges anthropocentrism and envisions a hybridization of human beings, machines and the environment, even anticipating a threshold where humanity surpasses itself in a new evolutionary stage."

In §115, the encyclical describes both as "currents of thought that interpret progress as surpassing the human condition." But where transhumanism wants to *enhance* the human, posthumanism wants to *surpass* the human — to envision a future in which the distinctly human is dissolved into something else, whether hybrid, machine, or evolutionary successor.

The encyclical names what it considers most dangerous in this framing in §172:

> "At the root of these problems lies a technocratic and post-humanist mentality that tends to regard the human person as an object to be manipulated or a resource to be optimized, removing all safeguards against the unchecked pursuit of profit. What prevails is efficiency, rather than respect for freedom and human dignity. Some post-humanist currents even go so far as to envision 'second-class' human beings, subordinate to the interests of elites who consider themselves superior."

This last claim is the encyclical's sharpest accusation against posthumanism. Where the framing imagines a post-human future, it tends to imagine some humans more obsolete than others — and to operate, in the meantime, as if those treated as obsolete are already so. The framing creates a "second-class" anthropology that operates politically and economically even before the post-human future arrives.

## What it looks like in software

Posthumanism in software is less common than transhumanism but appears in specific patterns:

- AI systems framed as cognitive partners or successors rather than tools
- Product framings that explicitly or implicitly position AI as the future of work, with the human worker as a transitional figure
- Systems where the human role is engineered out of the workflow as a goal, not a side effect
- Brain-computer interface frameworks, neural-interface products
- "Mind upload" or digital-immortality framings
- AI-companion products framed as alternatives to human relationship, not supplements to it
- Systems whose long-term roadmap explicitly contemplates the obsolescence of distinctly human capacities they currently augment
- Marketing and design materials that treat the human-machine boundary as a problem to be dissolved

The most operationally significant pattern is the one §172 names: the system creates conditions in which some humans are treated as more obsolete than others — typically workers, the elderly, or low-resource populations whose roles the system is positioned to replace.

## When to use this label

Use posthumanism when:

- The system's framing positions AI or machine intelligence as a successor rather than a tool
- The product's roadmap treats the elimination of human roles as the goal
- The system contemplates or implements hybridization of human and machine in domains beyond medical necessity
- The framing treats the human-machine boundary as obsolete or undesirable
- The system creates explicit two-tier anthropologies — some humans more replaceable than others

Posthumanism is the most specific of the three labels. Most findings will not warrant it. Use it when the more specific framing is clearly engaged — not as decoration on findings that are more accurately labeled technocratic-paradigm or transhumanism.

Distinguishing from transhumanism: transhumanism wants to enhance the human; posthumanism wants to surpass the human. A productivity tool that treats distraction as a defect to be optimized is transhumanist. A system that positions AI as the legitimate replacement for human deliberation in some domain is posthumanist.

Distinguishing from technocratic-paradigm: the technocratic paradigm is a logic of optimization applied broadly. Posthumanism is a specific anthropological vision in which the human is surpassed. A finding that engages the broader logic uses technocratic-paradigm; a finding that engages the specific surpassing vision uses posthumanism.

## Example finding

```
7. Customer service architecture treats human escalation as failure mode to be minimized
   
   Location: services/support/escalation-policy.yaml, docs/internal/support-roadmap.md
   Confidence: 88
   
   Behavior: The customer service architecture documents AI-first handling as the design 
   target, with human escalation rate as a key metric to reduce over time. Internal roadmap 
   documents describe "AI handling 100% of tier-1 and tier-2 issues by [date]" as a goal, 
   with human agents repositioned to "training the AI" rather than serving users. The system's 
   internal language treats human handling as legacy.

   Violation: This violates the principle of human dignity. Per Magnifica Humanitas §103, 
   when consequential decisions are entrusted to algorithms "without anyone bearing responsibility 
   for that judgment," we hand over "the task of redefining the boundaries of human possibilities." 
   The roadmap here is to eliminate the human from the chain of responsibility for customer 
   service decisions — a domain where users frequently raise consequential concerns (account 
   suspension, billing errors, lost data, harassment) requiring judgment AI cannot provide. 
   Per §172, the post-humanist mentality "tends to regard the human person as an object to be 
   manipulated or a resource to be optimized." The roadmap operationalizes this — the human 
   user becomes a profile to be served by an algorithm, and the human agent becomes a 
   transitional figure on the way to that algorithm.

   Resembles: posthumanism — the system's roadmap explicitly positions the human role in 
   customer service as transitional, with the goal being elimination rather than augmentation.

   Remediation:
   — Rewrite the roadmap to position AI as augmentation of human agents, not replacement
   — Establish floors for human-reachable support: any consequential decision (account 
     suspension, billing dispute, data loss) reaches a human within bounded time
   — Replace the "escalation rate as failure" framing with "escalation rate as quality" — 
     when users need humans, the system has produced the conditions in which they need them
   — Treat AI handling as triage, not resolution; humans resolve, AI prepares the resolution
   
   Structural note: this finding engages organizational strategy, not just product. The 
   remediation requires leadership commitment to human-in-the-loop as a structural feature, 
   not a vestigial one.
```

## A note on the encyclical's gravity

The encyclical's framing of posthumanism is the sharpest of the three labels. §172 reaches for the language of "second-class human beings" — a serious charge. The audit should use posthumanism only when the structural pattern justifies the gravity. Many AI features that look superficially "post-human" are better described as transhumanist (treating human capacity as defect) or technocratic (applying optimization logic broadly). Posthumanism is reserved for findings where the system genuinely treats the distinctly human as the obstacle to be removed.

When in doubt, prefer the less specific label. The audit's authority rests on precision; over-application of the most serious label undercuts the seriousness of cases that warrant it.
