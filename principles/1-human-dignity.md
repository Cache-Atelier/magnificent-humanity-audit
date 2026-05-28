# Principle 1: The Dignity of the Human Person

> "The human person always remains 'the way for the Church' and the heart of every authentic path of integral human development." — *Magnifica Humanitas* §50

## What the encyclical teaches

Human dignity, in the encyclical's articulation, is **infinite, inalienable, and prior to capacity** (§48–58). It is not earned. It does not depend on a person's abilities, wealth, position in life, or right or wrong choices made (§50). It is grounded in the person being created in the image of the Triune God — willed and loved into existence by God as an expression of his unfailing love.

The encyclical distinguishes four dimensions of dignity (§52):

- **Moral dignity** — how a person directs choices and actions
- **Social dignity** — living conditions and the concrete respect received from society
- **Existential dignity** — how a person perceives their own worth
- **Ontological dignity** — the deepest level, belonging to every human being simply by virtue of existing, having been willed by God

The first three can be enhanced or diminished; ontological dignity cannot. Per *Dignitas Infinita*, cited in §53: "Every human person possesses an infinite dignity, inalienably grounded in his or her very being, which prevails in and beyond every circumstance, state, or situation the person may ever encounter."

**The ideology the encyclical names as "particularly insidious"** (§51): the notion that every person must earn or justify their own worth, with greater value attributed to those who are more efficient or effective. This is named explicitly. A system whose functional behavior implements this ideology — whether by grading users on productivity, by treating non-productive users as marginal, or by routing capacities and attention to those who produce more — is in direct contradiction to the principle.

The encyclical extends dignity into rights (§54–55): human rights are not external additions to the person but expressions of intrinsic dignity. They are universal and inalienable. The right to life from conception to natural end is foundational and is named as the first right.

## What honoring this principle looks like in software

A system that honors human dignity:

- Treats every user as worth the same care, regardless of revenue, engagement, or "value" to the platform
- Does not grade, rank, or differentially route capacity based on user productivity, status, or wealth
- Provides the same quality of recourse, error handling, and support to all users
- Does not require users to perform productivity for the system in order to receive its benefits
- Does not treat vulnerable users (children, elderly, disabled, low-resource) as edge cases handled later
- Provides clear pathways for users to be heard when something goes wrong — humans, not just bots
- Respects user choices that the system's metrics would prefer the user not make ("done for today," "leave," "delete")
- Does not collapse the person into a profile, score, or behavioral signature

## What violating this principle looks like

A system that violates human dignity:

- Implements differential treatment by user "tier" in ways that affect basic functionality, not just optional features
- Routes lower-paying or less-engaged users to inferior support channels (bot-only, longer waits, less recourse)
- Optimizes for "high-value users" in ways that degrade the experience of others
- Grades, scores, or surfaces public "trust" or "reputation" scores that follow the user
- Implements consequential decisions (account suspension, content removal, eligibility) without human review
- Treats minors, the elderly, or users with disabilities as edge cases with degraded experiences
- Has no path for a person to challenge an automated decision and reach a human
- Encodes assumptions about "worthy" users in fraud-detection, anti-abuse, or moderation systems
- Surveils users in ways that reduce them to behavioral profiles for prediction and influence

The encyclical names a sharper case in §103: "Entrusting an algorithm in practice with the power to select who is worthy or not, without anyone bearing responsibility for that judgment, is to hand over the task of redefining the boundaries of human possibilities."

## Code-level signatures

Where to look in a codebase for evidence on this principle:

- **User model and tier system.** How are users segmented? What does a "tier" or "plan" entitle the user to, and what does it deny? Are denied users denied conveniences, or denied basic dignity (slower help, fewer rights of recourse, worse error messages)?
- **Authorization and feature-gating code.** What features are gated by payment, by engagement metrics, by retention status, by "trust" scores? Are any of these dignity-essential (account deletion, data export, ability to reach support)?
- **Support routing.** Is human review available to all users, or only paying ones? Does the appeals process exist in code?
- **Account suspension and content moderation.** Are these decisions made by algorithm alone? Is there a documented appeal path? Is the appeal also algorithmic?
- **Onboarding screens.** What does the system require of the user as a condition of use? What does it withhold? Per §51: does the system functionally require users to earn or justify their worth before being granted access to its goods?
- **Edge-case handling.** Search the codebase for terms like "fraud," "abuse," "spam," "trust score," "risk score." How are these computed? What do they cause? Who reviews them?
- **Marketing copy vs. functional reality.** Does the product page promise things the code does not deliver to all users?

## Common remediations

When the audit identifies a violation of human dignity, remediation typically takes one of these forms:

- **Equalize basic dignity guarantees across tiers.** Whatever a paying user gets in terms of basic recourse, deletion, export, and human review must also be available to non-paying users. Differential features can be in optional functionality; differential dignity cannot.
- **Add human review paths for consequential decisions.** Any decision that suspends an account, removes content the user values, denies access to a service, or significantly reduces user reach must have a documented appeal path that reaches a human within bounded time.
- **Remove productivity-grading.** Score-based segmentation that drives capacity or attention routing should be replaced with equal-access defaults. Anti-abuse systems can be reactive rather than predictive-classificatory.
- **Audit fraud/abuse systems.** Run a sample of users flagged by these systems through human review. Identify false-positive demographics. Adjust thresholds and review processes.
- **Make recourse legible.** If an appeal path exists in policy but not in product surface, fix the product surface. A right that the user cannot find or invoke is not a right.

When the issue is non-local — typically because the entire business model depends on differential treatment — note that the remediation requires a structural change, not just a code-level patch.

## Typical diagnostic labels

When a finding violates the principle of human dignity, the diagnostic label that most often applies is **technocratic-paradigm** — the ideology in which efficiency, control, and profit dictate what matters and what can be discarded. When the violation specifically takes the form of grading or optimizing the user, **transhumanism** or **posthumanism** may apply (see `diagnostic-labels/`).

## Connections to other principles

A violation of dignity is almost always also a violation of social justice (§77–81), since dignity violations typically fall hardest on the most vulnerable. The connection to the universal destination of goods is also frequent: when a system concentrates dignity-essential goods (recourse, support, voice) in the hands of a paying few, both principles are violated simultaneously.

## Key encyclical paragraphs to cite

- **§48–50** for the foundational claim
- **§51** for the ideology the encyclical explicitly names as insidious (productivity-grading)
- **§52–53** for the four dimensions and the *Dignitas Infinita* citation
- **§55** for human rights as expressions of dignity
- **§103** for the algorithmic-judgment-without-responsibility specific case
