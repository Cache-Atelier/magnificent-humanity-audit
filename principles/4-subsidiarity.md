# Principle 4: Subsidiarity

> "The principle of subsidiarity applies especially in the context of the digital revolution. Here, the highest level is not the State, but rather major economic and technological actors that exercise *de facto* power over the conditions of everyday life." — *Magnifica Humanitas* §71

## What the encyclical teaches

Subsidiarity is the principle that **the role of individuals, families, local communities, and intermediary organizations should not be supplanted by higher-level authorities** (§68). Higher-level institutions must recognize, protect, and promote the freedom and creativity of lower-level entities, coordinating their contributions rather than absorbing them.

The principle has its modern formulation in Pius XI's *Quadragesimo Anno* (1931) and is a cornerstone of Catholic Social Doctrine. *Magnifica Humanitas* gives it a sharp new application: in the digital age, the "highest level" is no longer the State but **major economic and technological actors** — platforms — that exercise de facto power over the conditions of everyday life (§71).

The encyclical's claim in §71 is operationally direct: subsidiarity in the digital age requires that platform processes "not be imposed from above in an opaque and unilateral manner, but instead be directed toward the common good with transparency, accountability and meaningful forms of participation (including independent checks, transparency regarding algorithms, equitable access to data and avenues for recourse)."

This is a programmatic statement. The encyclical names four specific operational requirements:
- **Independent checks** on platform decisions
- **Transparency regarding algorithms** that shape what users see and how they are treated
- **Equitable access to data** rather than monopolization
- **Avenues for recourse** when platform decisions affect users

In §72 the encyclical extends this to the international level: "We cannot allow a handful of actors to dictate these processes on their own; instead, we must build forms of cooperation that respect the various levels of the global community and make them jointly responsible for the common good."

Subsidiarity is not state non-intervention. Per §69–70, public intervention is necessary precisely to enable all social actors to fulfill their mission without being stifled. Subsidiarity does not justify either platform unaccountability or state absorption of community life. It requires both: lower-level entities flourish; higher-level entities support them without replacing them.

## What honoring this principle looks like in software

A system that honors subsidiarity:

- Publishes the rules by which its algorithms operate, in language users can understand
- Allows users meaningful customization of how the algorithm treats them (turn ranking off, see chronological feed, exclude content categories)
- Treats intermediary institutions — schools, parishes, families, civic groups, professional associations — as legitimate participants in the platform's governance, not as objects of platform action
- Provides documented appeal paths for any consequential decision the platform makes about a user
- Makes platform data accessible to independent researchers, regulators, journalists in ways that allow meaningful oversight
- Does not preempt decisions that should be made closer to the persons involved
- Respects the user's authority over their own data, account, and presence on the platform
- Cooperates with international standards for transparency, portability, and accountability rather than circumventing them

## What violating this principle looks like

A system that violates subsidiarity:

- Operates ranking, recommendation, and visibility algorithms whose logic is undisclosed
- Provides no meaningful way for users to opt out of algorithmic curation
- Makes consequential decisions (account suspension, content removal, demonetization, deboosting) with no appeal path or with appeal paths that are themselves automated
- Treats requests for transparency from regulators, researchers, or journalists as adversarial
- Pre-empts decisions that should belong to families, schools, or local communities — for example, by deciding what content is appropriate for minors, what political content reaches whom, what voices get amplified
- Aggregates power that exceeds any meaningful accountability mechanism
- Designs its API and infrastructure so that intermediary institutions cannot build their own tools to manage what their members see
- Treats users as recipients of decisions made elsewhere rather than as participants in the decisions that affect them

The encyclical's framing in §70 is precise: subsidiarity requires "decisions are made at the closest level possible to the persons involved, thereby fostering community life and avoiding people being presented with decisions that have already been taken." A platform that presents users with decisions already taken — what they will see, what is allowed, what is rewarded, what is suppressed — violates this directly.

## Code-level signatures

Where to look in a codebase for evidence on this principle:

- **Algorithm documentation.** Is there any? In code comments, in developer docs, in user-facing help? The absence of documented logic is itself evidence.
- **Ranking and recommendation code.** What signals does it use? Are users informed of these signals? Can they adjust their weighting?
- **User-controllable preferences.** Search the settings UI and the underlying code for what is configurable. Often the platform exposes cosmetic preferences (theme, notification frequency) but not structural preferences (what gets recommended, what gets ranked, what gets seen first).
- **Appeal and recourse infrastructure.** Search the code and policy documents for "appeal," "dispute," "recourse," "review." If these exist only in policy and not in product, the right is fictitious.
- **Moderation pipelines.** Are decisions made by algorithm? By human? By human with algorithmic recommendation? Is the human empowered to overrule? Is the appeal path also algorithmic?
- **API and developer access.** Can a third-party tool, with the user's permission, manage the user's experience? Can a school or parish build tools for its members? Or is access tightly controlled by platform business logic?
- **Researcher access programs.** Does one exist? What does it permit? What is excluded from view?
- **Transparency reports.** Are they published? What do they include? What do they omit?

## Common remediations

When the audit identifies a violation of subsidiarity:

- **Document the algorithm in plain language.** Publish what the ranking signals are, in approximate weight, in a form users can actually read. Per §71, "transparency regarding algorithms" is one of the four specific requirements.
- **Add structural user controls.** Beyond cosmetic preferences, add user controls over the structural variables: what types of content the algorithm surfaces, what signals it weights, whether ranking is on at all, whether suggested content appears.
- **Build an appeal path that reaches a human.** Any consequential decision must have a path of appeal that ends with a human within a bounded time. The appeal path must be visible from the affected user's surface (not buried three menus deep) and must produce a documented outcome.
- **Open data access to legitimate researchers.** Per §71, "equitable access to data" is a subsidiarity requirement. Restricted-access programs for academic researchers, regulators, and accredited journalists are the starting point. Public datasets where privacy permits.
- **Cooperate with intermediary institutions.** Provide tools, APIs, and data access for the legitimate institutions that mediate between individuals and platforms — schools, parishes, family safety organizations, professional associations.
- **Accept regulatory oversight.** Per §71–72 and §106, "robust legal frameworks, independent oversight, informed users and a political system that does not abdicate its responsibility are required." Resistance to oversight is itself a finding.

When the issue is non-local — when the platform's market position depends on opacity and the absence of recourse — the structural note is that the remediation requires regulatory and possibly antitrust action, not just product change.

## Typical diagnostic labels

Violations of subsidiarity most often manifest as **technocratic-paradigm**, where opaque algorithmic decision-making replaces human judgment and accountability. The encyclical's specific framing of platform power as the new "highest level" exercising de facto authority over everyday life is the diagnostic frame.

## Connections to other principles

Subsidiarity is intimately linked to solidarity (§73): per §73, "when subsidiarity is not linked to solidarity, it ends up becoming merely the protection of particular interests; when solidarity is not supported by subsidiarity, it degenerates into a form of welfare that does not foster responsibility." A finding that violates subsidiarity will frequently also violate solidarity (the system's design isolates users from the intermediary institutions that could support them) and human dignity (decisions are taken about persons rather than by persons).

The connection to the universal destination of goods is also tight: §67 names platforms and data as goods of common destination, and §71 then says they must be governed with subsidiarity-shaped accountability. The two principles work together against the same pattern: digital wealth concentrated in a few hands and exercised without accountability.

## Key encyclical paragraphs to cite

- **§68–69** for the foundational principle
- **§70** for "decisions made at the closest level" and "avoiding people being presented with decisions already taken"
- **§71** for the *direct application to the digital revolution* — **the most-cited paragraph for platform-power findings**, with the four operational requirements (independent checks, algorithmic transparency, equitable data access, recourse)
- **§72** for the international cooperation point
- **§102–105** when the finding is specifically about algorithmic decision-making without accountability
