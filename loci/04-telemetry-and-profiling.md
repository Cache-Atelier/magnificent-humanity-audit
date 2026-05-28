# Locus 4: Telemetry and Behavioral Profiling

> "When every action—movements, purchases, relationships and preferences—leaves a trace, a new form of power emerges, namely the power to profile, predict and influence behavior, often without individuals being fully aware of it." — *Magnifica Humanitas* §171

## What this locus covers

What the system observes about its users, what it stores, what it infers, and what it does with the inferences. This includes:

- Event telemetry: what user actions are tracked
- Behavioral signals: hover, scroll, dwell time, micro-interactions
- Session replay and screen recording
- Cross-app and cross-site tracking
- Device, network, and identity fingerprinting
- Profile and segmentation systems: who is grouped with whom and why
- Inference systems: what the platform claims to know about the user beyond what the user has told it
- Prediction systems: what the platform predicts the user will do, want, or feel
- Targeting systems: what is selected for the user based on profile

The encyclical's §171 is direct about this: profiling and prediction "without individuals being fully aware of it" constitutes a "new form of power." A system that has built this power without commensurate accountability is precisely what the encyclical's social-doctrine principles oppose.

## Principles most engaged

- **Universal destination of goods** (Principle 3): per §67 and §108, data — including the behavioral data this locus concerns — belongs in significant part to its contributors, not to the platform as private asset.
- **Subsidiarity** (Principle 4): per §171, profiling that pre-empts the user's choices is decision already taken — the user is being predicted rather than consulted.
- **Social justice** (Principle 6): per §80, "communities exposed to invasive surveillance" is named directly.
- **Human dignity** (Principle 1): per §51, profiling that reduces the person to behavioral signatures treats them as a means.
- **Solidarity** (Principle 5): per §76, the digital ecosystem is preserved or exploited; intensive behavioral extraction without consent or return tips toward exploitation.

## What to look for

### What is tracked

Read the telemetry layer carefully. Catalog what is sent and when:

- Page views, screen views (standard)
- Click events, with what context attached
- Hover, mouse movement, scroll behavior (behavioral)
- Dwell time, time-on-element
- Form interaction patterns: fields filled, fields abandoned, edit patterns
- Keystroke timing (rare but exists)
- Session replay (records of literal user sessions)
- Device characteristics: screen size, OS, browser, fingerprintable attributes
- Network: IP, approximate location, ISP
- Connections to other accounts, devices, sessions

The line worth holding: telemetry that supports the user's stated function is one thing; telemetry that constructs a behavioral signature is another. The encyclical's framing in §171 distinguishes the two — it is when "every action... leaves a trace" that a new form of power emerges.

### What is inferred

The platform's inferred attributes about the user are often more revealing than what the user has stated:

- Interest categories
- Demographic inferences (when not directly given)
- Predicted purchase intent, predicted churn, predicted "lifetime value"
- Predicted political orientation, sexual orientation, religious affiliation
- Predicted mood, predicted vulnerability windows (worse, but exists in some systems)
- Predicted compatibility with content classes, ad categories, recommendations

A common pattern: the user has never been asked any of this. The platform has inferred it from behavioral telemetry. The user can typically not see what the platform has inferred about them. The user typically cannot correct it.

### Who is most surveilled

Per §80, social justice requires attention to which populations are most heavily surveilled. The surveillance footprint of a system is rarely uniform:

- Workers (gig workers, customer service workers, employees of large firms using monitoring software)
- Students (educational technology, attention tracking, "engagement" monitoring)
- Beneficiaries (welfare recipients, immigration applicants, parolees, social-service clients)
- Children (per §141, especially vulnerable)
- People in low-trust regions (visa applicants, refugees, the formerly incarcerated)

The same system often surveils different populations to different degrees. The audit must read for this asymmetry.

### Cross-platform tracking

- Does the platform receive data from third-party trackers on other sites?
- Does it provide data to third-party trackers?
- Are pixels and tracking scripts present? Whose?
- Is there cross-device linking? On what basis?
- Is the user informed?

### What inferences drive

The decisive question: what consequential outcomes flow from the profile?

- Pricing differentiation
- Feature availability
- Content surfaced or suppressed
- Eligibility for offers, credit, insurance
- Risk and fraud scoring
- Moderation and visibility decisions

A profile that is collected but does nothing is a privacy concern. A profile that drives consequential decisions is the concern of every principle the encyclical names.

## Common findings

- **Behavioral telemetry without functional necessity.** Hover, dwell, scroll, time-on-element tracked at fine granularity. The system uses these to model attention rather than to debug or improve. Per §170, this is the substrate of the attention economy.
- **Session replay.** Literal recordings of user sessions stored for "product improvement." The user is rarely informed in the specific.
- **Inference without disclosure.** The platform builds a profile of inferred attributes the user cannot see and cannot correct.
- **Cross-app/cross-site tracking by default.** The user is not informed; opt-out is buried or absent.
- **Differential pricing based on profile.** Same product, different prices, based on inferred willingness to pay.
- **Profile-driven manipulation.** Per §171, the architecture of visibility (what is amplified, suppressed, rewarded) is shaped by profile in ways the user does not perceive. The user thinks they are seeing what others see; they are not.
- **Worker surveillance products.** Software sold to employers that tracks employee screens, attention, keystrokes. Per §150, this "frequently forces workers to adapt to the speed and demands of machines, rather than machines being designed to support those who work."
- **Profile retention beyond user departure.** Profile data persists after account closure or consent withdrawal.

## How to gather evidence

When source code is available:
- Identify all analytics SDKs in dependencies: Mixpanel, Amplitude, Segment, Heap, FullStory, LogRocket, Hotjar, Sentry, custom telemetry
- Search the codebase for `track`, `event`, `pageView`, `identify`, `analytics`, `telemetry`
- Read the event taxonomy — often centralized in an `events.ts`, `analytics/`, or schema file
- Search for `fingerprint`, `device_id`, `session_replay`
- Read the profile model: what fields exist? Which are user-provided, which are inferred?
- Read the inference pipeline. Where does it run? What inputs? What outputs?
- Read the targeting/personalization code. What profile fields drive decisions?

When only product access is available:
- Open developer tools and inspect network traffic for analytics calls
- Use a browser extension that documents tracking (e.g., Privacy Badger, uBlock Origin in audit mode)
- Read the privacy policy for what is collected and inferred
- Request the data export and look for inferred attributes
- Note differential pricing or content if observable
- Check transparency reports and academic studies of the platform

## Remediation patterns

- **Minimum telemetry.** Track only what is necessary to provide the service. Behavioral signals (hover, dwell, micro-interaction) require strong justification; default to not tracking.
- **No session replay without granular consent.** Recording user sessions requires explicit per-session consent, with clear disclosure of what is recorded and for how long.
- **Make inferences visible.** Whatever the platform infers about the user, the user can see. Whatever the user can see, the user can correct or delete.
- **No cross-site or cross-app tracking by default.** Default off; explicit opt-in; revocable.
- **No profile retention after account closure.** Closure means the profile is deleted, along with derived data.
- **No differential pricing by profile without disclosure.** If users see different prices based on profile, they must be told.
- **Equal surveillance by user class.** Workers, students, beneficiaries, children — the standards of consent, oversight, and recourse are the same as for other users, not relaxed because the user is in a less-empowered position.
- **Document profile lineage.** Where each inference comes from. What signals contributed. What the inference drives.

Per §171, "freedom in the digital age is not merely a matter of interiority but also a public concern. It calls for clear rules, transparency, the possibility of recourse and proportionate limits on the use of intrusive technologies." This is the operational standard.
