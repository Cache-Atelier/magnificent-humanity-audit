# Principle 5: Solidarity

> "Like the natural environment, the 'digital ecosystem' can be preserved or exploited, shared or monopolized." — *Magnifica Humanitas* §76

## What the encyclical teaches

Solidarity is **the conscious recognition that the future of each individual is connected to the future of all** (§73–74). Per Pope Francis, cited in §73, "no one is saved alone." Solidarity is more than the empirical fact of interdependence; it is the choice to take responsibility for the bonds we already inhabit.

The encyclical articulates solidarity as both principle and virtue (§75). As a principle, it expresses the objective order of relationships among individuals, groups, and peoples. As a virtue, it requires "a firm and persevering determination" to strive for the common good, with particular attention to those most in need. Per Francis quoted in §75, solidarity is "a way of making history" that creates communities rather than masses of individuals.

The encyclical explicitly applies solidarity to digital consumption and technology use (§75): solidarity requires "a willingness to challenge habits and privileges — including those related to digital consumption and the use of technology — when they prevent others from living with dignity."

The decisive application for the audit is in **§76**: "Like the natural environment, the 'digital ecosystem' can be preserved or exploited, shared or monopolized. Solidarity demands that decisions regarding data, algorithms, platforms and artificial intelligence take into account not only the immediate benefit for a few, but also the impact on all peoples and on future generations."

This is the encyclical's environmental analogy made explicit: just as integral ecology rejects the framing of the natural environment as an externality to economic decisions, integral solidarity rejects the framing of the digital ecosystem as an externality to platform decisions. The platform that optimizes for itself, treating the impact on the broader information ecosystem, on future generations of users, and on the communities not yet served as not its concern, violates solidarity directly.

Solidarity is linked tightly to subsidiarity (§73). When subsidiarity is not linked to solidarity, it becomes merely the protection of particular interests. When solidarity is not supported by subsidiarity, it degenerates into welfare that does not foster responsibility. The two must travel together.

In §73, solidarity is also linked to authentic participation: it is expressed when each person, individually and collectively, takes part in the life of the community by staying informed, engaging with others, making their voice heard, and contributing to public decisions — "assuming real responsibility so that the common good is achieved through shared decision-making."

The encyclical also names the global dimension: in §76, "responsibility extends to digital and information infrastructure." This includes future generations and peoples not yet beneficiaries of the technology.

## What honoring this principle looks like in software

A system that honors solidarity:

- Takes responsibility for the bonds users form on the platform, not just for the platform's own metrics
- Considers second-order effects on communities, populations, and generations not directly using the platform
- Does not exploit users' isolation; actively supports user agency in maintaining bonds outside the platform
- Treats the platform's success as conditional on the ecosystem's health, not as extractable from it
- Provides users with what they need to participate in the platform's decisions about itself — feedback channels that produce response, governance structures with user voice
- Considers the burden the platform imposes on future generations (data accumulation, environmental cost, behavioral patterns that shape children's development)
- Cooperates with other systems, institutions, and platforms rather than competing for closed dominance
- Recognizes that some users are more vulnerable and that the system's design should accommodate that

## What violating this principle looks like

A system that violates solidarity:

- Treats interdependence as an extractive opportunity rather than a moral bond
- Optimizes for individual user engagement in ways that fracture the broader bonds the user inhabits
- Exploits user isolation, loneliness, or vulnerability for engagement (the encyclical names this specifically — see §100 on AI simulating relationship and §170 on attention-economy mechanics that "thrive on human weakness")
- Externalizes costs onto the broader ecosystem (environmental, social, attentional, civic) as if they were not the platform's concern
- Decides about the user without the user; decides about communities without the communities
- Treats future generations as externalities — children's developmental trajectories, the long-term effects of algorithmic curation on civic discourse, the data that will outlive everyone who consented to its collection
- Refuses to cooperate with other platforms or institutions because cooperation does not maximize the platform's individual position
- Competes in ways that hurt users — for example, by deliberately breaking interoperability, by making it costly to leave, by treating departures as losses to be prevented rather than rights to be honored

Per §100, the encyclical names a specific case: AI that simulates relationship for users who are isolated. "The danger is not so much that a person may believe they are communicating with another person, but rather that they may gradually lose the very desire to form genuine human connections." A system designed to be the user's substitute for human community, rather than support for it, violates solidarity at the deepest level.

## Code-level signatures

Where to look in a codebase for evidence on this principle:

- **Engagement loops and retention systems.** What does the platform do when a user starts to leave? Variable-reward notifications? Win-back campaigns? Social-pressure cues ("your friends are posting without you")? These mechanisms exploit the bonds the user inhabits rather than supporting them.
- **AI-companionship features.** Does the system simulate friendship, romance, support, or care? Under what conditions are these surfaced to lonely or vulnerable users? Per §100, the encyclical names this as a specific risk.
- **Interoperability and migration.** Can the user leave with their bonds intact — exporting their social graph, their conversation history, their relationships? Or does leaving mean losing what they built?
- **Cross-platform behavior.** Does the system actively degrade other systems? Block APIs, refuse standard protocols, route around interoperability requirements?
- **Children's design.** Are features designed for minors actually safe for minors, or are they versions of the adult product with cosmetic adjustments? Per §141–142, the encyclical takes this seriously.
- **Environmental and resource footprint.** What is the energy and water consumption? Where do the rare earths come from? Per §101, the encyclical names this as a real concern that solidarity must address.
- **Decision-making infrastructure.** Are users informed of decisions that affect them? Do they have any voice? Does the platform have a feedback mechanism that actually shapes platform behavior, or only one that records complaints?

## Common remediations

When the audit identifies a violation of solidarity:

- **Replace exploitative engagement with supportive engagement.** Retention systems that exploit weakness should be replaced with systems that genuinely serve the user. Notifications driven by behavioral hooks (variable rewards, FOMO, social pressure) should be replaced with notifications driven by stated user goals.
- **Stop simulating relationship with vulnerable users.** AI companionship features, especially those targeted at or used by lonely, isolated, or grieving users, should be reconsidered. At minimum, surface honestly that the user is interacting with a system, and direct them toward human connection where possible.
- **Support migration with dignity.** Make it easy to leave. Export complete data, including social graph and conversation history. Cooperate with portability standards. Treat a user's departure as their right, not the system's loss.
- **Cooperate with other platforms and institutions.** Adopt standard protocols. Open APIs to legitimate third-party tools. Support the institutions — schools, parishes, families, professional associations — that mediate users' lives.
- **Measure and reduce the resource footprint.** Document energy and water consumption. Source materials responsibly. Account for these costs honestly in product decisions.
- **Add user voice in platform decisions.** Establish governance structures — user councils, content moderation review boards, formal feedback that produces response — that give users meaningful participation in platform decisions.
- **Consider future generations.** Audit how the platform's design will affect children, future users, and the patterns of communication and bond-formation those generations will inherit.

When the issue is non-local — when the platform's economics depend on user isolation and platform closure — the structural note is that the remediation requires reckoning with the business model itself, not just the product features.

## Typical diagnostic labels

Violations of solidarity most often manifest as **technocratic-paradigm** when the platform's logic treats the broader ecosystem as externality. When the specific pattern is the platform substituting for human relationships rather than supporting them, the encyclical's own framing in §100 — AI as simulated companionship — is the diagnostic vocabulary. When the violation involves treating future generations or distant populations as externalities, the §178 framing of digital colonialism applies.

## Connections to other principles

Solidarity is the principle that integrates many of the others. Its connection to subsidiarity (§73) is foundational: the two must travel together. Its connection to the universal destination of goods is direct (§76 frames the digital ecosystem analogously to the natural environment). Its connection to social justice is constant: solidarity is the disposition out of which social justice is built. And its connection to integral human development (Principle 7) is structural: development is not integral unless it embraces all peoples and all generations.

## Key encyclical paragraphs to cite

- **§73–74** for the foundational definition and "no one is saved alone"
- **§75** for solidarity as principle and virtue, and for the explicit application to digital consumption
- **§76** for the "digital ecosystem" analogy with the natural environment — **the most-cited paragraph for ecosystem-impact findings**
- **§100** when the specific pattern is AI simulating relationship for vulnerable users
- **§178** when the violation has the structural pattern of digital colonialism
