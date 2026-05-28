# Locus 7: Monetization, Access, and Equity

> "The Church recognizes the positive potential of the market and private initiative only if they remain subordinate to the moral law and are guided by the principle of solidarity, without sacrificing the most vulnerable to the rationale of profit." — *Magnifica Humanitas* §39, citing *Centesimus Annus*

## What this locus covers

How the system is paid for and how that economics shapes what users get. This includes:

- Pricing models: free, freemium, subscription, transactional, ad-supported
- Tier structures: what differentiates free from paid; what differentiates paid tiers
- Advertising: who pays, who is targeted, what is sold
- Data monetization: when user data is the product
- Differential pricing: same product at different prices for different users
- Paywalls: what is gated; whether dignity-essential goods are behind them
- Promotional and growth mechanics: referrals, viral loops, growth hacks
- Affiliate and recommendation economics: who is paid when the user is shown what

The encyclical's framing in §157–162 is the operational anchor. Economic freedom is not absolute; it must be measured against the common good and the dignity of every person. Entrepreneurial initiative can be a true vocation when it serves society; it becomes problematic when investment in disadvantaged people "is seen as useless or inconvenient."

## Principles most engaged

- **Universal destination of goods** (Principle 3): per §67, what should be common cannot be treated solely as private property monetized.
- **Common good** (Principle 2): per §161, "there are a few who have too much, and too many who have little, that is the logic of today." Monetization that intensifies this is a violation.
- **Social justice** (Principle 6): per §80 and §158, the most vulnerable cannot be sacrificed to the rationale of profit.
- **Human dignity** (Principle 1): per §51, when monetization grades users by capacity to pay and degrades those who cannot, dignity is violated.

## What to look for

### What is gated vs. universal

The decisive question for this locus: what is behind the paywall, and is any of it dignity-essential?

Acceptable to gate:
- Optional convenience features
- Storage beyond reasonable limits
- Advanced or specialized functionality
- Custom integrations and API access
- Higher rate limits
- Premium content the platform creates

Not acceptable to gate (or gate with strong justification):
- The ability to delete one's account
- The ability to export one's data
- The ability to reach a human for support on consequential decisions
- The ability to appeal automated decisions
- Basic safety features
- The right to be free of advertising in certain contexts (e.g., children's products, health/medical, grief, vulnerability)

Per §158, "investment in disadvantaged people or in those with slower development paths" should not be viewed as "useless or inconvenient." A tier structure that treats non-paying users as the marginal case to be handled cheaply is operating with the logic the encyclical names.

### Advertising and targeting

If the system is ad-supported, the audit reads how:

- Are ads behaviorally targeted? Based on what data?
- Are ads contextually targeted (based on what the user is currently looking at) vs. profile-based?
- Is the targeting transparent — can the user see why an ad is being shown?
- Are there categories that should not be targeted (children, mental health, addiction, vulnerable demographics)? Are they protected?
- Are ads distinguished from content? Or blurred deliberately?
- Are advertorial relationships disclosed?
- Does the system permit ads from categories that contradict its stated values (gambling on a children's product, predatory loans, weight-loss products in eating-disorder-adjacent contexts)?

### Differential pricing

- Are users shown different prices based on profile?
- Are the differentials documented? Or is dynamic pricing opaque?
- Are users in lower-resource markets charged less, or charged more (the latter happens when extraction is the model)?
- Is there evidence that vulnerable users are targeted with worse offers?

### Data as the product

If user data is monetized:
- Is the user informed?
- Is the user compensated? Or does the system extract value the user does not share in?
- Per §108, "data is the product of many contributors." A platform that extracts value from data without recognizing the contributors is operating in tension with the principle.

### Growth and referral mechanics

- Do referrals exploit the user's existing relationships for the platform's growth?
- Are referral rewards material — substantial enough to pressure friends into joining for the wrong reason?
- Are viral loops designed to recruit non-users without their consent (uploading contacts, suggesting to contacts they join, etc.)?
- Per §75, solidarity requires "willingness to challenge habits and privileges — including those related to digital consumption and the use of technology — when they prevent others from living with dignity." Growth mechanics that use the user's relationships against those relationships' integrity violate this.

### Sponsored and affiliate content

- Are recommendations driven by user fit, or by economic relationship with the recommended item?
- Are sponsored placements disclosed?
- Are affiliate commissions disclosed?
- Where the system claims neutrality (search, recommendation), is the claim warranted?

## Common findings

- **Dignity-essential goods behind a paywall.** Account deletion, data export, human support — gated by payment.
- **Vulnerability-targeted advertising.** Ads for predatory loans, gambling, weight-loss, addictive products served to users whose profile suggests vulnerability.
- **Children targeted by behavioral ads.** Despite stated protections, ads in children's products use behavioral targeting. Per §141–142, the encyclical is direct about the protection minors require.
- **Opaque dynamic pricing.** Same product, different prices, no disclosure. Often correlated with profile signals.
- **Data monetization without disclosure.** User data sold or licensed to third parties; the user is not told.
- **Tier structures that systematically degrade non-paying users.** Slower support, fewer rights, worse error handling. The platform's two-tier dignity structure is in the product itself.
- **Viral loops that exploit relationships.** Contact uploads, friend invitations sent without explicit per-invitation consent, social pressure embedded in invitation copy.
- **Sponsored placement without disclosure.** "Top picks" that are paid placements, recommendations whose ranking is influenced by affiliate economics.
- **Manipulative cancellation flows.** Subscriptions easy to start, hard to stop. Phone calls required to cancel; "save offer" pages between the user and the cancel button.

## How to gather evidence

When source code is available:
- Read the billing and subscription code; map the tier structure
- Identify feature flags gated by tier
- Read the ad serving code; identify targeting signals
- Search for `pricing`, `tier`, `subscription`, `paywall`, `gating`
- Read the referral and growth code
- Read sponsored content and affiliate integration code
- Search for `cancel`, `unsubscribe`, `downgrade`; document the friction

When only product access is available:
- Subscribe to each tier; document differences
- Attempt to cancel subscriptions; document the path
- Create accounts in different regions, different demographic configurations; check for differential pricing
- Document the advertising the system serves; cross-reference with your profile
- Read transparency reports for ad targeting documentation

## Remediation patterns

- **Equalize dignity-essential goods across tiers.** Whatever a paying user gets in account management, data rights, and recourse must be available to non-paying users.
- **Limit behavioral advertising.** Default to contextual advertising; require opt-in for behavioral. Excluded categories for vulnerable contexts and users.
- **Disclose differential pricing.** When users see different prices based on profile, the system tells them. Standard prices are published.
- **Symmetric subscription flows.** Cancellation is as easy as signup. No phone requirements, no save-offer obstacles, no friction designed to prevent cancellation.
- **Disclose sponsored placements.** Every paid placement is labeled. Affiliate relationships are visible.
- **Honor referral consent.** Invitations to non-users require explicit per-invitation consent. No mass contact-upload that broadcasts to all contacts.
- **No targeting of vulnerable users.** Ads in contexts of grief, addiction recovery, eating disorders, financial distress are restricted; if served, they are not behaviorally targeted to vulnerability signals.
- **Share value with data contributors.** Where user data is the product, the contributors share in the value. Per §108, "manage data as a common or shared good."

The structural note for this locus is often unavoidable. Per §163, "in the age of AI and robotics, it is no longer possible to rely solely on the 'invisible hand' of the market." Where the audit identifies monetization patterns that contradict the principles, the tactical remediation may be incomplete; the structural fix engages the business model and regulatory environment.
