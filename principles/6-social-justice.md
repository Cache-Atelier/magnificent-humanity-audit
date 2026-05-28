# Principle 6: Social Justice

> "Justice demands that we prevent the emergence of new forms of exclusion and deprivation of freedoms: individuals and peoples hindered or denied access to basic technologies, communities exposed to invasive surveillance and social groups penalized by opaque algorithms that perpetuate prejudice and discrimination." — *Magnifica Humanitas* §80

## What the encyclical teaches

Social justice is **the capacity of a social, economic, and political order to allow everyone — particularly the weakest — to live a truly dignified life, without leaving anyone behind** (§77). For the Christian community, it is a concrete way of following Jesus, who proclaims good news to the poor and identifies himself with the lowly, the sick, the imprisoned, and strangers.

Social justice is characterized by the **preferential option for the poor** (§78), a framework given prominence by John Paul II that must guide both personal and societal choices. Pope Francis's denunciation of the "throwaway culture" is cited here: a culture that generates new forms of exclusion.

The encyclical's distinctive emphasis is **structures of sin** (§79). Following John Paul II, social justice recognizes that injustices do not arise solely from the wrong choices of individuals but also from "structures, mechanisms and economic and cultural systems that produce inequality almost automatically." This is decisive for the audit: a system can produce injustice without any individual within it intending injustice. The pattern is in the structure.

Justice has a restorative dimension (§79): it aims to mend broken bonds and reintegrate those who have been excluded, taking into account the wounds caused by past injustices — wars, colonialism, racial or gender discrimination, violence against entire peoples, exploitation.

**§80 is the encyclical's most operational paragraph for digital-age audits.** It names directly what social justice requires of digital systems:
- Prevent new forms of exclusion and deprivation of freedoms
- Address individuals and peoples hindered or denied access to basic technologies
- Address communities exposed to invasive surveillance
- Address social groups penalized by opaque algorithms that perpetuate prejudice and discrimination
- Guarantee equal access to opportunities
- Protect the youngest and weakest
- Combat hate and misinformation
- Subject the use of data and technology to public oversight
- Ensure the guiding principle is not solely profit but dignity and the common good

The encyclical also frames migrants and refugees as a litmus test for social justice (§81): "The way a society treats them reveals whether its sense of justice is driven by fear or by the spirit of fraternity."

## What honoring this principle looks like in software

A system that honors social justice:

- Provides equal access to its core functions regardless of payment, status, geography, language, or device class
- Designs from the perspective of the most vulnerable users — children, elderly, disabled, low-resource, language minorities, the formerly excluded
- Audits algorithms for disparate impact across protected and historically marginalized populations
- Provides meaningful recourse when algorithmic decisions harm a user, with that recourse weighted to protect those least able to defend themselves
- Combats misinformation and harassment in ways that protect those most at risk of being targeted
- Cooperates with public oversight (auditors, regulators, researchers) on the social-justice implications of the system
- Does not encode existing patterns of exclusion into its training data, defaults, or model behavior
- Treats data sovereignty seriously, especially for populations whose data has historically been extracted without consent or benefit (§178)
- Does not invisibly cost more — in time, attention, friction — for marginalized users than for the platform's privileged ones

## What violating this principle looks like

A system that violates social justice:

- Has consequential decisions made by opaque algorithms whose error patterns differentially harm marginalized users
- Surveils, predicts, and influences vulnerable populations without their meaningful consent
- Implements differential service quality that tracks with wealth, geography, or marginalization
- Trains models on data that reflects historical patterns of discrimination, then deploys those models in consequential contexts (hiring, lending, housing, healthcare, criminal justice)
- Provides recourse that is harder to invoke for the very users who most need it (language barriers, complex processes, no offline path)
- Amplifies harassment or hate that targets vulnerable users while protecting popular accounts
- Allows employer or institutional surveillance of workers, students, or beneficiaries that diminishes their dignity
- Externalizes the social costs of its operation onto communities not in the platform's economic interest
- Embodies what the encyclical names in §95: "control over platforms, infrastructure, data and computing power" that "tends to become opaque and evade public oversight, increasing the risk of distorted forms of development that give rise to new dependencies, exclusions, manipulations and inequalities"

The encyclical's framing in §102 is sharp: AI systems that present themselves as neutral and objective "end up reflecting and reinforcing the stereotypes or ideological bias of their designers and developers." This is not malice. It is structure. The audit must read structurally.

Per §103: "Entrusting an algorithm in practice with the power to select who is worthy or not, without anyone bearing responsibility for that judgment, is to hand over the task of redefining the boundaries of human possibilities. In this process, political responsibility is also lost, not just empathy toward those excluded, which can, after all, be simulated. The exclusion of the vulnerable becomes cloaked in a veneer of neutrality and objectivity, against which it becomes difficult to raise objections."

## Code-level signatures

Where to look in a codebase for evidence on this principle:

- **Consequential decision systems.** Hiring filters, lending decisions, housing platforms, healthcare triage, criminal-justice risk scores, content moderation that affects livelihoods. Read the model training data, the features, the validation against disparate impact.
- **Training data sources.** Where does the data come from? Whose patterns does it encode? Is it audited for representativeness?
- **Default settings by region or device.** Are users on lower-end devices, in less profitable regions, with non-English defaults, given a fundamentally degraded experience?
- **Pricing and feature gating.** Is the differentiation between tiers about optional features or about basic dignity? See `principles/1-human-dignity.md` for the overlap.
- **Content moderation and anti-abuse code.** Does it differentially affect users by language, by demographic, by political position? Is the appeal path equally accessible to all?
- **Surveillance and behavioral profiling.** Who is surveilled most intensely? What is done with the data? Are there populations whose patterns are studied more than others without their knowledge or benefit?
- **Worker- or student-facing surveillance.** Employee monitoring, student attention tracking, beneficiary surveillance — see §150 for the encyclical's specific critique.
- **Accessibility code.** Is it real or theatrical? Test the screen-reader path, the keyboard-only path, the high-contrast mode, the low-bandwidth mode.
- **Localization.** Does the product work in the languages and cultural contexts of its non-dominant users? Or are they second-class citizens of the platform?

## Common remediations

When the audit identifies a violation of social justice:

- **Audit algorithmic systems for disparate impact.** For any consequential decision the system makes, audit by population. Document the disparities. Where present, treat them as findings.
- **Add human review weighted toward the marginalized.** Where automated decisions are consequential, ensure that appeals from less-resourced users are not deprioritized. Make appeal paths short, multilingual, and accessible offline where needed.
- **Make accessibility production-grade.** Treat WCAG 2.1 AA as a floor, not a ceiling. Test with users who actually rely on accessibility features. Treat regressions as P0 bugs.
- **Diversify training data.** Source training data that represents the populations the system will be deployed to. Where representative data does not exist, acknowledge the limitation in the product itself.
- **Stop differential surveillance.** Apply the same standards of consent, oversight, and recourse to all users. Do not surveil the marginalized more intensely because they are less able to push back.
- **Equalize basic recourse across tiers.** See `principles/1-human-dignity.md`. The dignity-essential goods — recourse, support, ability to be heard — should not track with payment.
- **Submit to public oversight.** Cooperate with regulators, academic researchers, accredited journalists. Per §80, "subjects the use of data and technology to public oversight" is part of what social justice requires.
- **Repair past extraction.** Where data was collected from populations without their benefit, consider what is owed. Per §178, "restoring to individuals not only the data that describes them, but also the ability to decide how it is used, by whom and for whose benefit."

When the issue is structural — when the system itself is built on extractive or exclusionary patterns — the remediation requires more than tactical changes. Per §109, "social justice is not only a goal to be safeguarded after technologies are deployed, but a condition that must shape their very design from the outset."

## Typical diagnostic labels

Violations of social justice most often manifest as **technocratic-paradigm**, especially when the system masks exclusion in the appearance of objectivity. When the violation involves optimization of "the human" in ways that grade humans by capacity, **transhumanism** or **posthumanism** may also apply (§117 specifically warns that the optimization framing "places the burden on the most vulnerable in pursuit of a supposed optimization of the species").

## Connections to other principles

Social justice is the principle that translates dignity (Principle 1) into societal structure. It is also tightly linked to solidarity (Principle 5): solidarity is the disposition; social justice is the structure that disposition builds. The connection to subsidiarity (Principle 4) is important: just structures require accountable institutions, which is what subsidiarity provides.

Per §109, social justice in the digital age must engage every principle: "To speak of the universal destination of goods means finding ways of ensuring universal access to both technologies and the education needed to use them. To speak of subsidiarity calls for protecting the ability of communities to make choices and corrections. To speak of solidarity obliges us to recognize the hidden, often exploited workers, who sustain algorithmic systems. To speak of justice requires questioning the global distribution of power."

## Key encyclical paragraphs to cite

- **§77–78** for the foundational claim and the preferential option for the poor
- **§79** for structures of sin and the restorative dimension
- **§80** for the *direct application to digital systems* — **the most-cited paragraph for digital-justice findings**, with all of: surveillance, opaque algorithms, exclusion, hate, misinformation, public oversight
- **§95** for the concentration of digital power and its specific risks
- **§102–105** for algorithmic decision-making, bias, neutrality-as-mask, and the loss of compassion in automated systems
- **§109** for the integration with all other principles
- **§150** when the specific violation is worker surveillance
- **§178** when the violation involves digital colonialism
