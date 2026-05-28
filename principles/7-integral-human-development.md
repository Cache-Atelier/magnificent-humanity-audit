# Principle 7: Integral Human Development

> "Technological innovations, including artificial intelligence, are not neutral, for they can either foster participation and justice or exacerbate inequality, control and exclusion. For this reason, they must be evaluated by asking a crucial question: Do they truly help individuals and peoples to become more humane and fraternal, while respecting our common home and future generations?" — *Magnifica Humanitas* §85

## What the encyclical teaches

Integral human development is the encyclical's **integrating framework** — the principle through which the other six are translated into a concrete way of evaluating human, social, and technological reality. Per Paul VI in *Populorum Progressio*, cited in §82, development is authentic only when it is "integral": fostering "the development of each person and of the whole person." Every dimension of existence, all peoples, and future generations.

Per §83, development is not truly human when:
- It places accumulation of wealth at the center rather than persons
- It concerns only individuals and not peoples
- It increases consumption for some while shifting costs and burdens onto others
- It relegates entire regions to subordinate roles, preventing them from realizing their full potential

Development is integral when it is not limited to the economic sphere but **promotes quality of life in spiritual, cultural, moral, and relational dimensions**, while respecting our common home, the diversity of peoples, and their ways of life (§83).

In §84, the encyclical brings integral ecology into the framework. Development is just only when it integrates justice toward people and care for the common home. True progress is not what increases the wellbeing of some by degrading ecosystems, shifting costs onto disadvantaged communities, or compromising the living conditions of those who follow.

**§85 contains the encyclical's litmus question** — the question that every audit ultimately answers:

> "Do they truly help individuals and peoples to become more humane and fraternal, while respecting our common home and future generations?"

This question is repeated in different form in §129, where John Paul II's question from *Redemptor Hominis* is invoked at the climax of Chapter 3: does AI "make human life on earth 'more human' in every aspect of that life? Does it make it more worthy of man?"

These are the questions an audit's synthesis must answer. Findings are evidence; the synthesis weighs the evidence against these questions.

The encyclical's vision of integral development is also a vision of **what must not be lost** (§112–114). Even as technological power grows, what must not be lost is:
- The capacity to recognize the other as a face, not merely a function (§114)
- The ability to care for one another, which is "a fundamental dimension of our humanity, one that is learned and mastered through lived experience"
- The recognition that humanity flourishes not despite limitations but often through them (§118)
- The integration of suffering rather than its denial (§120)
- The interplay between freedom and grace that allows persons to change (§128)

A system that systematically erodes any of these — that makes care harder, that hides faces behind functions, that promises to eliminate suffering by eliminating depth, that classifies and optimizes what already exists rather than allowing change — fails integral human development.

## What honoring this principle looks like in software

A system that honors integral human development:

- Treats users as persons in their fullness — spiritual, cultural, moral, relational beings — not as profiles or behavioral signatures
- Supports the formation of capacities that flourish over time (attention, patience, judgment, relationship) rather than the displacement of those capacities by quick interaction
- Does not promise to eliminate the friction that personal growth requires
- Respects the user's freedom to change, including changes the system's models did not predict
- Considers all dimensions of impact: not only individual user satisfaction but cultural, ecological, relational consequences
- Includes future generations in its design — the children who will inherit the platform's effects, the populations not yet served
- Treats environmental impact (energy, water, materials) as part of the design space, not as externality
- Recognizes the limits of its own competence and refuses to colonize domains where it does not belong (intimate care, moral discernment, friendship)
- Distinguishes between augmenting human capacity and replacing it; chooses augmenting where the choice matters

## What violating this principle looks like

A system that violates integral human development:

- Reduces the person to a behavioral profile and operates exclusively on that reduction
- Erodes capacities (attention, patience, judgment) through design choices that reward speed over depth
- Treats user growth, change, and conversion as edge cases the model handles poorly
- Optimizes a single dimension (engagement, revenue, retention) without considering aggregate effect on the person, the community, the culture, the environment
- Externalizes the costs of its operation onto populations and generations not in its current beneficiary set
- Substitutes for human relationships, capacities, or formation processes rather than supporting them
- Treats the human as something to be optimized — per §117, "If the human being is treated as something to be perfected or surpassed, it becomes easier to accept that some lives are less useful, less desirable or less worthy"
- Promises a frictionless life as if frictionlessness were the same as flourishing
- Operates with the implicit anthropology that the encyclical names in §112: "When efficiency becomes the ultimate measure of value, human beings are tempted to see themselves as a project to be optimized rather than as persons called to relationship and communion"

Per §150, the encyclical names a specific case: AI that forces workers to adapt to the speed and demands of machines rather than the reverse. This deskills, surveils, and erodes the worker's sense of agency. The same pattern — humans adapting to the machine rather than vice versa — appears across many software contexts and is a direct violation of integral development.

## Code-level signatures

Where to look in a codebase for evidence on this principle:

- **The metric the system optimizes.** Read the analytics setup, the A/B test infrastructure, the OKRs documented in the codebase. What is the system actually optimizing? Is it engagement, time-on-app, conversion? Is anything tracked at the level of "did this help the user become a fuller person"? Is anything tracked at the level of community, culture, or environment?
- **Onboarding flow.** What does the system assume the user wants from it? Is the user invited to grow, or invited to consume? Does the onboarding presume the user is a deficit to be filled, or a person with capacities to be supported?
- **Default behaviors.** Defaults that maximize engagement vs. defaults that respect the user's stated intent. Defaults are revealed anthropology.
- **Notification and re-engagement systems.** Per §170, when business models "thrive on human weakness," the person is treated as a means. Look for variable-reward notification timing, FOMO triggers, social-pressure cues.
- **AI integration points.** Where does the system use AI? Is it augmenting user capacity (helping them do what they're trying to do) or substituting for it (doing it for them in a way that erodes the capacity)? Per §140, "the speed and ease with which answers or summaries can be obtained risk extinguishing the desire to ask questions."
- **Children's and adolescents' features.** Per §141–142, the encyclical takes children's design extremely seriously. Look for age gates that are real vs. theatrical, content filters that work vs. that gesture, controls available to parents and schools.
- **Worker-facing features.** Per §150, look for surveillance, pacing pressure, machine-driven workflow constraints, automated performance scoring.
- **Environmental and infrastructure cost.** Per §101 and §173, look at what the system consumes. Energy, water, rare earths, labor in the supply chain.
- **The system's posture toward user departure.** When a user wants to leave, what does the system do? Does it support graceful exit, or does it engage retention dark patterns?

## Common remediations

Because integral human development is the integrating principle, remediations here usually require integrating multiple specific changes. Typical patterns:

- **Re-anchor optimization to user-stated goods.** The single most important change. Replace engagement-time and retention metrics as primary optimization targets with goals the user has actually stated. Measure success by task completion, by the user reporting they accomplished what they came to do.
- **Build "done for today" surfaces.** Per the encyclical's framing in §140, teach the system to support disengagement when the user has finished. A platform that knows when to let go is a platform that honors integral development.
- **Audit AI integrations for substitution vs. augmentation.** For each AI feature, ask: does this help the user develop a capacity, or does it replace the capacity? Where it replaces, consider whether the replacement is appropriate (some replacements are good — physical hazards, repetitive low-value labor) or whether it's eroding a capacity that the user benefits from having (writing, thinking, deliberating).
- **Protect children's development.** Implement real, not theatrical, protections for minors. Age gating that works. Content filtering that filters. Tools for parents and schools that actually grant control. Defaults that prioritize developmental safety over engagement metrics.
- **Treat worker dignity as a design constraint.** For systems used by workers, refuse to deploy patterns that surveil, pace-pressure, or deskill. Design tools that support workers' agency rather than displacing it.
- **Account for resource footprint honestly.** Document the system's energy, water, and material costs. Reduce them where possible. Where reduction is not possible without redesign, acknowledge the cost.
- **Refuse to colonize domains the system doesn't belong in.** Per §100, AI that simulates relationship for the lonely is a violation. Per §198, AI that takes lethal-force decisions in warfare is a violation. Each system has its own list of domains where it should be augmenting, not substituting; the list belongs in design documentation.

When the issue is non-local — when the system's existence depends on a model the encyclical names as violating integral development — the structural note is unavoidable: the audit will conclude that the system's foundational design needs rethinking, not just its features.

## The synthesis question

Every audit's synthesis is structured by integral human development. The question the audit answers, in its final paragraph, is the encyclical's litmus question from §85:

> Does this system truly help individuals and peoples become more humane and fraternal, while respecting our common home and future generations?

Or, in the form of John Paul II's question repeated in §129:

> Does this system make human life on earth "more human" in every aspect of that life? Does it make it more worthy of man?

Or, in the encyclical's central image (§9, §129):

> Is this system being built toward Babel or toward the rebuilt Jerusalem?

The synthesis answers in evidence-grounded terms, drawing on the findings already produced. The synthesis is not a fresh assertion but a weighing of what the audit has already established.

## Typical diagnostic labels

When a system fails integral human development, the diagnostic labels that apply depend on the mechanism. **Technocratic-paradigm** when the system reduces everything to measurable efficiency and treats the human as object of optimization. **Transhumanism** when the system frames human limitations (attention, memory, patience) as defects to be corrected by technology. **Posthumanism** when the system envisions human-machine hybridization or the displacement of distinctly human capacities as progress. All three are named in the encyclical (§92–93, §115–117).

## Connections to other principles

Integral human development integrates all six other principles. Per §82, this principle indicates "the practical ways in which the noble principles — dignity, the common good, the universal destination of goods, subsidiarity, solidarity and social justice — are implemented in real life." A finding under integral human development is rarely isolated; it almost always engages multiple principles at once. The audit's synthesis is where they come together.

## Key encyclical paragraphs to cite

- **§82–83** for the foundational claim about integrality
- **§84** for the integration with ecology and care for the common home
- **§85** for the *litmus question* — **the most-cited paragraph** for any audit's synthesis
- **§112–114** for what must not be lost (capacity for relationship, care, the face of the other)
- **§117** when the violation is specifically about treating the human as object of optimization
- **§129** for John Paul II's question, repeated as the climax of Chapter 3
- **§150** when the violation is specifically about workers adapting to machines
- **§170** when the violation involves business models that thrive on human weakness
