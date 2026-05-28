# Locus 1: Defaults and Onboarding

> "Decisions are made at the closest level possible to the persons involved, thereby fostering community life and avoiding people being presented with decisions that have already been taken." — *Magnifica Humanitas* §70

## What this locus covers

The behaviors the system commits the user to before the user has chosen, and the path the user is required to walk to enter. This includes:

- Default settings on account creation
- Required vs. optional onboarding steps
- Permissions the system requests on first run
- Information the system collects as a precondition of access
- The user's implicit model of the system as conveyed by the onboarding flow
- What the system asks the user to accept (terms of service, privacy policy, marketing, telemetry)

Defaults and onboarding are revealing because they encode the system's anthropology before any interaction. They show what the system *assumes* about the user — and assumptions, in the encyclical's framing, are never neutral.

## Principles most engaged

- **Human dignity** (Principle 1): does the system treat the user as a person whose dignity precedes their utility, or as a profile to be filled in?
- **Subsidiarity** (Principle 4): does the system present the user with decisions already taken? Per §70, this is precisely what subsidiarity rejects.
- **Solidarity** (Principle 5): does the onboarding treat the user's existing bonds (contacts, social graph, prior data) as resources to extract or as goods to respect?
- **Integral human development** (Principle 7): does the onboarding orient the user toward the system as augmentation of their capacities, or as substitution for them?

## What to look for

### Defaults that maximize extraction

Look at the default state of:
- Notification permissions (default on or off?)
- Marketing and promotional communications (default opt-in?)
- Behavioral analytics and telemetry (default on?)
- Personalized advertising (default on?)
- Data sharing with third parties (default on?)
- Public profile visibility (default public?)
- Search-engine indexing of user content (default indexed?)
- Sharing of user-generated content for AI training (default consented?)
- Cross-app tracking (default permitted?)

Per the encyclical's framing in §70, the system that defaults to its own benefit and requires the user to opt out is precisely the system that "presents people with decisions that have already been taken." A virtuous default is the one the system would choose if it were optimizing for the user's stated good rather than its own metrics.

### What is required as a condition of entry

What information does the system require before granting access?
- Real name?
- Phone number?
- Date of birth (and what is done with it)?
- Photo or biometric data?
- Address?
- Linkage to other accounts (Google, Facebook, etc.)?
- Permission to access contacts, photos, location, microphone?

The principle in §51 applies: the user is being asked to "earn or justify" their access to the system. Required information that is not strictly necessary to provide the service is information the system has decided is worth more than the user's freedom to use the service.

### The onboarding narrative

Read the onboarding flow as text. What does it say to the user about who they are?
- Does it presume the user is a deficit (lonely, unproductive, missing out) to be filled by the system?
- Does it presume the user is a producer (of content, attention, social signal) for the system?
- Does it presume the user is a person with goals the system can support?

The narrative matters because, per §135, "the content that circulates within digital environments shapes how people perceive the world and introduces into the collective consciousness images and narratives that direct our desires and influence our daily choices." Onboarding is the first content the system circulates.

### Forced terms

What must the user accept to use the system?
- Are terms of service displayed, or just linked?
- Is there a granular consent flow, or single bundled "accept all"?
- Are required terms separable from optional terms?
- Can the user use the system at all without accepting marketing communications, behavioral analytics, or AI training contributions?

Per §70, presenting the user with a single take-it-or-leave-it bundle is decision already taken — the user "participates" only by accepting what was decided elsewhere.

## Common findings

Patterns that often surface in this locus:

- **Maximalist default permissions.** Notifications, telemetry, marketing, personalization all default on. The user is told they can opt out — somewhere, sometimes. The opt-outs are deeper in the menu than the opt-ins were.
- **Required oversharing.** The system asks for real names, phone numbers, photos, or other information not strictly necessary to the service. The information is then used for purposes beyond what is necessary.
- **Bundled consent.** The user cannot use the service without accepting terms that bundle the essential with the extractive. Cookies for functioning are bundled with cookies for cross-site tracking. Account creation is bundled with marketing consent.
- **Onboarding that frames the user as deficit.** "Find friends," "build your audience," "complete your profile to be discoverable" — language that treats the user's incompleteness as the problem the system solves.
- **Default-on AI training.** Especially in newer systems: user content is used to train models by default. The opt-out is buried or absent.
- **Default-public profiles.** The user must affirmatively choose privacy. The system's preferred state is the one where the user contributes maximally to the platform's network effects.

## How to gather evidence

When source code is available:
- Search for default values: `default = True`, `:default => true`, configuration files
- Read the user-creation handler. What fields are required? What is set on creation?
- Search the codebase for "opt-out" and "opt-in"; the ratio is often revealing
- Read the onboarding flow controllers (often `onboarding/`, `welcome/`, `signup/`, `setup/`)
- Read the consent and terms-acceptance code

When only product access is available:
- Create a new account and document every screen
- Inspect the cookie banner; count optional vs. required cookies
- Read the privacy policy for what is collected by default
- Note what is on vs. off in settings immediately after account creation
- Try to use core functions without accepting non-essential permissions; document what is blocked

## Remediation patterns

- **Privacy-respecting defaults.** Notification, marketing, telemetry, personalization all default off. The user explicitly opts in to each.
- **Minimum information collection.** Account creation requires only what is strictly necessary to provide the service. Additional information is requested only as features require it.
- **Granular consent.** Each category of data use has its own consent flow. The user can use the service while declining non-essential categories.
- **Honest onboarding.** The onboarding tells the user what the system is for and what it costs. It does not frame the user as deficit.
- **Visible opt-outs.** Opt-outs are at the same depth as the opt-ins. If the system can offer an opt-in in onboarding, it can offer the opt-out in settings.
