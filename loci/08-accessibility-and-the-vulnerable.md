# Locus 8: Accessibility and the Vulnerable

> "A just social order guarantees everyone equal access to opportunities, protects the youngest and weakest members of society, combats hate and misinformation and subjects the use of data and technology to public oversight." — *Magnifica Humanitas* §80

## What this locus covers

How the system treats users who are not its default demographic. This includes:

- Children and adolescents
- The elderly
- People with disabilities (visual, auditory, motor, cognitive)
- Language minorities
- Users on low-end devices, low-bandwidth connections, or in low-resource regions
- People in conditions of vulnerability — grief, illness, addiction recovery, financial distress
- The formerly incarcerated, immigrants, refugees, asylum seekers
- Users without standard government documentation, banking, or smartphones
- People in oppressive political contexts who need privacy protection
- Workers, students, and beneficiaries subject to surveillance by employers, schools, or social services

The encyclical's framing in §78 is direct: social justice requires looking at individuals and communities "starting with the most vulnerable." The audit reads this locus with the preferential option for the poor as its discipline.

## Principles most engaged

- **Human dignity** (Principle 1): per §51–53, dignity precedes and transcends capacity. The system's treatment of those whose capacities are reduced is the test of whether dignity is operative.
- **Social justice** (Principle 6): the foundational principle for this locus. Per §78, "social justice begins with the least among us."
- **Solidarity** (Principle 5): per §73, "no one is saved alone." The system's treatment of the vulnerable is the most concrete test of solidarity.
- **Integral human development** (Principle 7): per §141, "early and unsupervised exposure to digital devices and social media can negatively impact... the most vulnerable stages of life."

## What to look for

### Accessibility (technical)

Accessibility is not optional. The audit reads:

- Does the system meet WCAG 2.1 AA at minimum? AAA where appropriate?
- Is the screen reader experience actually usable, or does it produce a broken experience?
- Is the keyboard-only path complete? Can a user accomplish all essential tasks without a mouse?
- Are images and media accessible (alt text, captions, transcripts)?
- Is the color contrast adequate? Are choices available for users who need higher contrast?
- Does the system work with browser zoom, OS text-size settings, screen magnification?
- Are forms accessible? Labels properly associated, error messages reachable?
- Is interactive content (modals, carousels, dynamic content) accessible?
- Is accessibility tested with actual users who rely on assistive technology?

### Children and adolescents

Per §141–142, the encyclical's concern about minors is direct and specific. The audit reads:

- Is the system age-gated? Is the age gate real (verified somehow) or theatrical (a self-report checkbox)?
- If minors use the system, is there a distinct children's product, or just the adult product with cosmetic adjustments?
- What protections exist against grooming, exploitation, harmful content?
- Are recommendation algorithms different for minors, or the same engagement-extracting machinery?
- Are engagement mechanics that exploit weakness (streaks, variable rewards, social-comparison cues) present in children's features?
- Are parental and school controls real? Do they actually grant control?
- Per §142, are public-policy protections (age limits, accountability) being met or circumvented?

The encyclical's language in §141 is worth quoting: "early and unsupervised exposure to digital devices and social media can negatively impact sleep, attention span, control of emotions and relationships, especially during the most vulnerable stages of life, at times with tragic consequences." This is the framing for any audit involving minors.

### The elderly

- Is the system usable for users unfamiliar with current UI conventions?
- Is text size adjustable; is the default readable?
- Are confirmations clear; are destructive actions reversible?
- Is the system patient with slower interaction; does it timeout aggressively?
- Are scams, predatory ads, and manipulative copy protected against — or do they target the elderly?

### Language and cultural minorities

- Is the system localized into the languages of its users? In what depth?
- Is the localization machine-translated and approximate, or thoughtful and reviewed?
- Are non-English-named users handled correctly (names with accents, non-Latin scripts, name structures with multiple family names or no family name)?
- Are date, time, currency, address formats adapted appropriately?
- Are content moderation and safety systems effective in non-English languages, or are these users effectively unprotected?

### Low-resource users

- Does the system work on older devices, slower processors, less RAM?
- Does it work on slow or intermittent connections?
- Is data consumption documented; is there a low-data mode?
- Are essential functions available offline?
- Is the system installable and updatable in regions with limited storage and bandwidth?
- Per §80, "individuals and peoples hindered or denied access to basic technologies" is named directly.

### Users in vulnerable conditions

- Does the system identify users who might be in vulnerable states (grief, illness, financial distress) and protect them, or target them?
- Are services for sensitive contexts (mental health, addiction recovery, domestic violence) appropriately careful, or do they import the engagement mechanics of mainstream products?
- Per §170, when business models thrive on weakness, the most vulnerable users are most damaged.

### Surveilled populations

- Are workers, students, beneficiaries, parolees, or other surveilled populations subject to the system?
- Is the surveillance proportionate?
- Is consent meaningful, given the power asymmetry?
- Per §150, "AI promises to boost productivity by taking over mundane tasks" but "frequently forces workers to adapt to the speed and demands of machines" — a violation the audit reads for explicitly.

## Common findings

- **Theatrical age gates.** Self-reported birthday with no verification; minors trivially access adult-targeted features.
- **Children's features with adult engagement mechanics.** Streaks, variable rewards, social-comparison cues; recommendation algorithms unchanged for minors.
- **Accessibility regressions accepted.** Accessibility is implemented at launch and then degraded by subsequent updates. Screen-reader paths break and stay broken.
- **Localization that masks rather than serves.** Machine-translated UI in many languages but no native review; content moderation effective only in English.
- **Non-English content moderation gaps.** Harassment, hate speech, and exploitation in non-English content go unmoderated because the system lacks coverage.
- **Differential surveillance of the marginalized.** Welfare recipients, immigration applicants, parolees subjected to more intensive monitoring than other users.
- **Predatory targeting.** Advertising or product placement targeted at vulnerable demographics — predatory loans, gambling, weight-loss in eating-disorder contexts, etc.
- **Low-resource exclusion.** The system is unusable on older devices, slow connections, in less-served regions; its presence in those regions is theatrical.

## How to gather evidence

When source code is available:
- Audit accessibility with automated tools (axe, Lighthouse), then verify with manual screen-reader testing
- Read the age-verification code; identify where it actually verifies vs. self-reports
- Read children's-product code paths; identify differences from adult product
- Read localization files; identify language coverage and depth
- Read content moderation code by language; identify gaps
- Read the worker- or beneficiary-facing code; identify surveillance and pacing mechanisms

When only product access is available:
- Test with screen reader, keyboard only, browser zoom, high contrast
- Create an account as a minor; document what is restricted vs. what is not
- Read terms about children's protection; test against behavior
- Test in the system's stated supported languages; assess depth
- Test on older devices and slow connections
- Read academic literature on the system's treatment of vulnerable populations

## Remediation patterns

- **Accessibility as P0.** Treat accessibility regressions as launch-blocking. Include actual users with assistive technology in testing.
- **Real age gating where it matters.** Where the platform is used by minors, age verification must be more than self-report. Where verification is impractical, treat all users as if they might be minors — apply the stricter standard.
- **Children's products as distinct products.** Different recommendation algorithms, different engagement mechanics, different safety defaults. Not "the adult product with parental controls."
- **Native-language content moderation.** Where the system serves a language, it moderates that language with comparable resources.
- **Names handled correctly worldwide.** Accept the full range of human naming systems.
- **Low-resource modes.** Offline functionality, low-bandwidth modes, support for older devices treated as design requirements, not afterthoughts.
- **Restrict targeting in vulnerable contexts.** Mental health, addiction recovery, grief, financial distress — restricted targeting categories, additional content moderation, lower engagement-extraction thresholds.
- **Reduce surveillance of the marginalized.** Equal standards of consent and oversight applied to all users regardless of their position in employment, education, or social services.

Per §78, the framing is the preferential option for the poor. A finding under this locus typically also implicates social justice (Principle 6) and human dignity (Principle 1). When the audit identifies systemic exclusion or differential treatment, the principles compound.
