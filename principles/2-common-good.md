# Principle 2: The Common Good

> "The whole is greater than the sum of its parts... the mere sum of individual interests is not capable of generating a better world for the whole human family." — *Magnifica Humanitas* §61

## What the encyclical teaches

The common good is **the social expression of the dignity recognized in every person** (§59). It cannot be reduced to a list of conditions or institutions. It is not the sum of individual benefits, nor the intersection of particular interests. Per the Second Vatican Council quoted in §60: "the sum total of social conditions which allow people, either as groups or as individuals, to reach their fulfillment more fully and more easily."

The encyclical insists in §61 that the common good is a "plus" — a greater good belonging to everyone that emerges from interaction and mutual influence, that cannot be explained by adding up individual goods. This matters operationally: a system that delivers individual benefits to each user can still fail the common good if the aggregate effect on the community, the platform's ecosystem, or the broader culture is degrading.

The common good is not a private optimization. It requires "a slow and arduous effort calling for a desire for integration and a willingness to achieve this through the growth of a peaceful and multifaceted culture of encounter" (§62). When politics — and by extension product design — abandons a long-term perspective and reduces itself to short-term calculations or sterile polarizations, "the language of the common good loses credibility, and, at the same time, social inequalities and divisions grow" (§63).

The common good takes a global dimension (§64): the right of peoples to exist, preserve their identity, and contribute their unique qualities. Any attempt to eliminate or subjugate a nation is "gravely immoral and therefore unacceptable."

In §132–134, the encyclical applies the common good to truth itself: truth is a common good, not the property of those with power or influence. A system that degrades the truth of public communication — through disinformation amplification, manipulation, or algorithmic incentive of conflict — is a system that destroys a common good.

## What honoring the common good looks like in software

A system that honors the common good:

- Considers second-order and aggregate effects, not just individual user benefit
- Has explicit, measured commitments to community-level outcomes, not just individual KPIs
- Maintains the conditions under which honest exchange and trust can grow on the platform
- Does not optimize for engagement at the cost of the platform's overall health
- Distinguishes between user-stated goods (what the user came to do) and system-extracted goods (what the system gets from the user) and does not collapse them
- Considers the impact on the broader ecosystem (other platforms, the public sphere, the civic conversation)
- Recognizes that a healthy commons requires forbearance from extracting maximum value
- Treats truth and accurate communication as something the system actively maintains, not just a side effect

## What violating the common good looks like

A system that violates the common good:

- Optimizes individual engagement metrics in ways that produce a degraded aggregate (polarization, addiction, decline of trust)
- Defines "value" entirely in terms of individual session metrics, with no measurement of community health
- Allows algorithmic amplification of falsehoods or inflammatory content because such content engages
- Permits dynamics in which the most aggressive, manipulative, or attention-seeking users determine what others see
- Treats other platforms or the broader information ecosystem as externalities to extract from
- Concentrates the conditions of communication (who can be seen, who can be heard, what spreads) in opaque ways that serve the platform's revenue rather than the conversation's quality
- Generates "social inequalities and divisions" as a byproduct of monetizable engagement

The encyclical specifically applies this to truth (§132): "Tools that could foster dialogue and participation are often used to construct distorted narratives and blur the boundaries between truth and falsehood, mixing facts with opinions." When public discourse is corrupted by a platform's design choices, the common good is directly damaged.

## Code-level signatures

Where to look in a codebase for evidence on this principle:

- **Recommendation and ranking algorithms.** What signals do they optimize? Are second-order effects on community discourse measured anywhere? Is there a "downrank inflammatory" signal or only "uprank engaging"?
- **Engagement metrics in the analytics codebase.** Look for what is tracked at the individual level (sessions, time-on-app, conversions) vs. what is tracked at the community level (health, trust, conversation quality). The asymmetry is often striking.
- **Content moderation policies in code.** What is removed? What is left up despite obvious harm? What is left up *because* it engages?
- **A/B test infrastructure.** What are the success metrics? Are they exclusively individual-engagement-based? Is a test that increases engagement but decreases stated user satisfaction allowed to ship?
- **Notification systems.** Do they exist to serve user goals or to recapture user attention? See `loci/05-engagement-and-attention-design.md`.
- **Cross-platform behavior.** Does the system actively degrade the experience of leaving (slow exports, partial APIs, deliberately broken interoperability)? Healthy commons require open exit; closed ecosystems extract from the broader commons.
- **Data sharing and platform openness.** Are third-party researchers able to study the platform's effects? Or is the data closed in ways that make community-level study impossible?

## Common remediations

When the audit identifies a violation of the common good:

- **Add community-health metrics alongside engagement metrics.** Whatever the platform measures at the individual level, measure something analogous at the community level: trust over time, perceived conversation quality, user-reported satisfaction with what they see, share of users reporting they "feel worse after using" — and treat these as constraints on engagement optimization.
- **Require multi-metric pass for A/B tests.** A test that increases engagement but decreases user-reported well-being or community-health metrics should not ship. The bar should be "improves the individual experience without degrading the aggregate."
- **Audit recommendation signals for inflammatory amplification.** Look explicitly for content classes that engage *because* they distress, polarize, or shock, and dampen their distribution even when they perform on engagement.
- **Open up the data for independent study.** When researchers cannot study a platform's aggregate effects, the platform cannot honestly claim to serve the common good. Restricted-access data partnerships with academic institutions are a starting point.
- **Slow down where the common good is at stake.** Per §106, "calling for prudence, rigorous evaluation and even, at times, a slower pace in adopting AI does not mean opposing progress; instead, it is an exercise of responsible care for the human family."

When the issue is non-local — typically because individual engagement is the only metric tied to revenue — the structural fix involves changing what the business is measured by, not just what the algorithm optimizes.

## Typical diagnostic labels

Violations of the common good often manifest as **technocratic-paradigm** when the system reduces everything to measurable efficiency. When the specific mechanism is platform optimization that erodes shared truth or shared trust, the violation can also be described as a Babel pattern from the encyclical's own framing (§7, §10).

## Connections to other principles

The common good is the principle through which the other six are integrated. Per §46, the principles "be considered collectively, so that it becomes clear how they relate to and complement each other." A finding that violates the common good will often also touch subsidiarity (the platform has accumulated unaccountable power), the universal destination of goods (the platform's data and reach are concentrated), and social justice (the costs of the violation fall hardest on the vulnerable).

## Key encyclical paragraphs to cite

- **§59–60** for the foundational definition
- **§61** for the "plus" claim — the common good is more than the sum of individual goods
- **§62** for the "culture of encounter" requirement
- **§63** for the warning about short-term calculations
- **§132–134** when the violation is specifically about truth as common good
