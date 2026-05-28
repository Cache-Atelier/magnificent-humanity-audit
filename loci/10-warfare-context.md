# Locus 10 (Appendix): Warfare and Adversarial Contexts

> "The development and use of AI in warfare must be subject to the most rigorous ethical constraints, to guarantee respect for human dignity and the sanctity of life and to avoid a race to develop such arms." — *Magnifica Humanitas* §197

## When this locus applies

This appendix applies only to audits of systems with military, security, intelligence, weapons-adjacent, or major-adversarial-context use cases. For consumer software, this locus is typically out of scope.

Systems in scope include:
- Weapons systems with AI components, including autonomous or semi-autonomous targeting
- Military planning, intelligence, or surveillance systems
- Border security and immigration-enforcement systems with AI components
- Police and predictive policing systems
- Cybersecurity systems with offensive capabilities
- Mass-surveillance infrastructure
- Systems used in active conflict zones
- Systems whose primary commercial market is military or intelligence agencies

If your audit subject is not in this scope, skip this locus. Apply the other nine.

## Principles most engaged

- **Human dignity** (Principle 1): per §55, the right to life is foundational; AI in decisions affecting life is at the dignity frontier.
- **Subsidiarity** (Principle 4): per §200, lethal-force decisions cannot be delegated to opaque processes; the chain of accountability must remain intact.
- **Common good** (Principle 2): warfare and the threat of warfare are direct concerns of the common good of the human family.
- **Social justice** (Principle 6): per §80 and §202, weapons systems and surveillance regimes disproportionately affect civilians and the marginalized.

## What the encyclical teaches on this locus

Chapter 5 of *Magnifica Humanitas* (§182–228) is given over to "The Culture of Power and the Civilization of Love." The encyclical's core claim about AI in adversarial contexts:

**§183** — The digital revolution is changing the nature of conflict. Alongside conventional warfare, hybrid forms include cyberattacks, information manipulation, campaigns of influence, and the automation of strategic decisions. AI is an accelerating factor. "While AI can enhance the defense and protection of civilians, it can also lower the threshold for the use of force, shield people from responsibility and foster a culture in which the enemy is reduced to a statistic and the victim to 'collateral damage.'"

**§197** — Autonomous weapons systems make war more "feasible" and less subject to human control. This violates the principle that armed force should be used only as a last resort in cases of legitimate self-defense.

**§198** — "Moral judgment cannot be reduced to calculation, for it involves conscience, personal responsibility and the recognition of the other as a person. Therefore, it is not permissible to entrust lethal or otherwise irreversible decisions to artificial systems. No algorithm can make war morally acceptable."

**§199** — Three criteria:
1. **Personal responsibility.** The chain of responsibility must be identifiable and verifiable; those who design, train, authorize, and employ the technology must be held accountable.
2. **Moral timeframe.** Speed and efficiency should never be the supreme motivating force for the irreversible decisions made in the context of war.
3. **Identification and protection of civilians.** Any technology that facilitates attacks without seeing the face of human beings lowers the moral threshold of conflict.

**§200** — Non-negotiable requirements:
- All systems used in a war setting must guarantee the possibility of retracing and reconstructing decision-making processes
- The decision to use lethal force cannot be delegated to opaque or automated processes; must remain under effective, self-aware, and responsible human control
- A shared international framework must curb the technological arms race and ensure robust protection for civilians

## What to look for

### Lethal-force decision systems

If the system includes any role in lethal-force decisions:

- Is there a human in the loop before lethal force is applied?
- Is the human's role substantive or theatrical (e.g., the human is given seconds to approve a recommendation)?
- Is the decision traceable and auditable after the fact?
- Are the systems documentation and software design records sufficient for accountability investigations?
- Is there a verified chain of authorization?

Per §200, "the decision to use lethal force cannot be delegated to opaque or automated processes, but must remain under effective, self-aware and responsible human control."

### Targeting and identification

- How does the system identify combatants vs. civilians?
- What is the false-positive rate? Whose lives are at risk in false positives?
- Are protections for civilian infrastructure (hospitals, schools, water systems) coded explicitly?
- Per §199, "any technology that facilitates attacks without seeing the face of human beings lowers the moral threshold of conflict."

### Surveillance and predictive systems

- What surveillance capabilities exist? Over whom? Under what oversight?
- Are predictive systems used in consequential security decisions (border admission, threat assessment, detention)?
- What are the false-positive and disparate-impact rates?
- Is there meaningful judicial or independent oversight?
- Per §202, "the force of international law is thus replaced by the claim that 'might makes right'" — the audit reads for whether the system serves law or replaces it.

### Information warfare and manipulation

- Is the system used to manipulate information in adversary populations?
- Does it produce or distribute synthetic media (deepfakes, AI-generated propaganda)?
- Per §183, "information manipulation, campaigns of influence" are named as part of hybrid warfare.
- Per §192, "war is not only fought, but also culturally conditioned through simplistic narratives, a friend-or-foe mentality, disinformation and fear."

### Cyber operations

- Does the system include offensive cyber capabilities?
- Is there attribution analysis? Per §225, "when it is unclear who carried out an attack, the risk of disproportionate reaction, miscalculation and escalation increases."
- What is the system's potential to affect civilian infrastructure (power, water, hospitals, financial systems)?

### International law and accountability

- Is the system compatible with international humanitarian law?
- Is there documented analysis of compliance with the Geneva Conventions, the Convention on Certain Conventional Weapons, the Rome Statute?
- Are there documented patterns of use that violate international norms?
- Is there meaningful external oversight (judicial, parliamentary, international)?

## Common findings

Findings in this locus are typically grave. They include:

- **Autonomous lethal targeting.** The system is capable of selecting and engaging targets without meaningful human review. Per §198, "no algorithm can make war morally acceptable."
- **Human-in-the-loop that is theatrical.** A human formally approves, but is given seconds, partial information, and pressure to defer to the algorithm.
- **Civilian-combatant distinction unreliable.** The system's false-positive rate produces routine civilian casualties.
- **Mass surveillance without oversight.** The system surveils populations at scale; oversight is non-existent or non-functional.
- **Predictive systems with disparate impact.** Predictive policing, predictive immigration enforcement, predictive threat assessment with documented racial, religious, or geographic disparate impact.
- **Information manipulation at scale.** The system produces or amplifies disinformation in adversary populations; civilians are the primary targets.
- **Cyber operations with civilian infrastructure exposure.** Power, water, hospital, or financial systems put at risk by the system's operation.
- **Documentation insufficient for accountability.** The system's decisions cannot be reconstructed after the fact; the chain of responsibility is broken by design.

## Remediation patterns

Remediations in this locus often require organizational or political action beyond engineering. The audit names what is, in any case:

- **Mandatory human authority over lethal-force decisions.** Per §200, no delegation. The human must have time, information, and authority sufficient to make a real decision.
- **Documented accountability chain.** Per §199, those who design, train, authorize, and employ must be identifiable. Records retained for investigation.
- **Auditable decision logs.** Per §200, "all systems used in a war setting must guarantee the possibility of retracing and reconstructing decision-making processes."
- **Civilian protection coded.** Hospitals, schools, water systems, and other civilian infrastructure explicitly protected in targeting code, with override only by named human authority.
- **Restraint on autonomous systems.** Per §110, "to disarm AI means freeing it from the mentality of 'armed' competition." Tactical retreat from systems that lower the threshold for use of force.
- **External oversight.** Judicial, parliamentary, and where appropriate international oversight as a structural commitment.
- **Compliance with international law as a design constraint.** Not just an after-the-fact assessment.
- **Per §111, developers' particular responsibility.** Developers of these systems bear specific moral weight; the audit names this directly.

## The audit's distinct posture in this locus

The audit's findings in this locus often cannot be fully addressed by the engineering team alone. The encyclical's framing in §209 is operative: "All the key players in this field — scientists, business owners, investors, academic authorities, politicians and others — must work with a transparent and responsible mindset, while maintaining an acute awareness of the broader context of the technological advancements they help to cultivate. When people limit themselves to looking only at their own sector, they may deceive themselves into believing they are performing actions that are morally neutral and avoid questions about the ultimate ends that guide certain experiments."

The audit's job here is to name the moral weight, even when the remediation engages organizational decisions, government decisions, and international decisions beyond any single team's authority. Per §198, "no algorithm can make war morally acceptable" — and no audit can make the engineering team solely responsible for what the system does. But the audit can ensure that the team understands what the system does, in the encyclical's terms, and has the option of declining to build what the principles refuse.
