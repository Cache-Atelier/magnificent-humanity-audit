# Locus 6: Communication, Copy, and Truth

> "Truthful information does not arise from centralized or automated control. In public discourse, the truth of facts has a rational dimension, as it requires verification, cross-checking of sources and responsible argumentation. Moreover, it is deeply relational, built through bonds of trust and shared practices, as well as an honest exchange with others and with the world." — *Magnifica Humanitas* §132

## What this locus covers

The language the system uses and the system's relationship to truth in public communication. This includes:

- Microcopy: error messages, prompts, button labels, confirmation dialogs
- Marketing and product communication
- Notifications and re-engagement copy
- AI-generated text returned to users
- Content moderation and disinformation policies
- The system's amplification or suppression of misleading content
- The system's treatment of synthetic media (deepfakes, AI-generated content)
- The honesty of the system about itself: what it is, what it does, what its limitations are
- Communication about errors, outages, breaches, and harms

The encyclical names truth as a **common good** (§132). A system that degrades truthful communication — through manipulation, omission, amplification of falsehoods, or AI-generated text passed off as authentic — damages a common good directly.

## Principles most engaged

- **Common good** (Principle 2): the foundational principle, per §132. Truth is a common good.
- **Human dignity** (Principle 1): per §51, copy that shames, manipulates, or instrumentalizes the user treats them as means.
- **Social justice** (Principle 6): per §80, "combats hate and misinformation" is a social-justice requirement.
- **Solidarity** (Principle 5): communication design that exploits the user's social bonds (fake urgency from "friends," manufactured social pressure) violates solidarity.

## What to look for

### Microcopy that manipulates

Read the system's microcopy as if it were addressed to a thoughtful adult. Look for:

- **Shaming copy.** Decline buttons labeled "No, I don't care about my security" or "Skip — I don't want to save money."
- **Manipulative defaults.** Buttons styled to differential prominence (the platform's preferred choice is bright, the alternative is gray).
- **False urgency.** Countdowns that reset, "limited time" offers that are permanent, "x people are looking at this now" cues that are inflated or fabricated.
- **Social-pressure misrepresentation.** "Your friends have read this" when they have not, "10 people from your contacts" when the platform inferred contacts.
- **Confirmation friction that nudges.** "Are you sure?" repeated for actions the platform doesn't want you to take, but absent for actions it does.
- **Anthropomorphizing copy.** "I'm sad to see you go" — system as person, exploiting the user's social instincts.
- **False scarcity.** "Only one left" when the inventory is digital or unlimited.

### Truth about the system itself

The system's honesty about what it is:

- Is AI-generated content labeled as such?
- Is the system honest about its limitations? Where AI might be wrong, hallucinate, or mislead?
- Is the system honest about what it tracks?
- Is the system honest about what it does with what it learns?
- Is marketing copy aligned with functional reality, or does it overpromise?
- When errors happen — outages, data breaches, misdeliveries — does the system communicate honestly and promptly?
- Does the system acknowledge when an AI feature has produced harm?

### Disinformation amplification

If the system distributes content, the audit reads its relationship to truth-as-common-good:

- Does the system have policies on disinformation? Do they distinguish between mistakes and deliberate fabrication?
- Are inflammatory or false claims amplified by ranking algorithms because they engage?
- Does the system label content as synthetic when AI-generated?
- Does the system identify deepfakes? Does it remove them?
- Are content-quality signals separated from engagement signals in ranking?
- Per §132, does the system support "verification, cross-checking of sources and responsible argumentation"?

### AI-generated communication

The system's use of AI in communication with users is distinct from its handling of communication between users:

- Are AI responses labeled as AI?
- Is the user clearly informed when a chatbot is automated vs. human?
- Are AI-generated suggestions (autocomplete, reply suggestions) clearly distinguished from the user's own words?
- Per §99, AI does not "feel joy or pain, mature through relationships, or know from within what love, work, friendship or responsibility mean." When the system uses AI to communicate care, support, friendship, or empathy, is the simulation acknowledged?
- Per §100, when AI simulates human warmth toward isolated users, the encyclical names a specific risk. The audit reads for it.

### Communication during failure

The most revealing copy is often the worst:

- Outage notifications — honest about scope and duration, or evasive?
- Breach notifications — prompt, complete, actionable, or minimized?
- Error messages — informative, or blame-shifting?
- Account suspension communications — explain what was decided, or refer to opaque policy?

## Common findings

- **Manipulative microcopy.** Shaming decline-buttons, false urgency, social-pressure misrepresentation, anthropomorphic appeals.
- **AI without label.** Chatbots that simulate human agents without disclosing automation. AI-generated content (text, images) presented as authentic without indication.
- **Engagement-driven amplification of falsehoods.** Ranking that uplifts inflammatory or false content because it engages, without compensating downrank for falsity.
- **Marketing overpromise.** Product pages claim capabilities the system does not reliably deliver.
- **Evasive communication during failure.** Outages, breaches, and harms communicated in minimizing language, with vague timeframes and limited apology.
- **AI-simulated care for the vulnerable.** Chatbots that offer emotional support, companionship, friendship to lonely or grieving users without acknowledging they are not persons. Per §100, this is named as a specific risk.
- **Unlabeled synthetic media.** AI-generated images, videos, audio circulating in the system without labeling. Deepfakes not detected or not removed.
- **Opaque suspension communications.** "You've violated our terms" — without specifying which, when, how.

## How to gather evidence

When source code is available:
- Search the codebase for user-facing strings: `i18n`, `locales/`, `strings.json`, `messages.yml`
- Read the error message catalog
- Read the notification and email template repository
- Read the marketing copy in product pages
- Read AI feature integrations: where is AI's output sent to the user? Is it labeled?
- Read content moderation policy and the code that enforces it

When only product access is available:
- Document microcopy at decision points: defaults, declines, confirmations
- Read marketing material; compare to functional behavior
- Test the system's response to fabricated content; check for labeling
- Engage with chatbots; test whether automation is disclosed
- Search for the system's response to past incidents (breaches, outages, harms); read their public communications

## Remediation patterns

- **Neutral microcopy.** Decline buttons say "No thanks" or "Skip," not shaming language. Defaults are visually balanced.
- **Honest framing.** No false urgency, no fabricated social signals, no manufactured scarcity. Where urgency is real, it is documented and time-bounded; where it is not, it is removed.
- **Label AI output.** AI-generated text, images, video, audio are labeled as such. Where they are returned to the user, the user knows they are AI-generated.
- **Disclose automation.** Chatbots disclose they are not human. The disclosure is at the start of the interaction, not buried in fine print.
- **Engagement-quality separation in ranking.** What is ranked because it is true is separated from what is ranked because it engages. Inflammatory falsehoods are explicitly downranked.
- **Marketing aligned with reality.** Product pages claim only what the system reliably delivers. Limitations are documented.
- **Honest failure communication.** Outages, breaches, and harms are communicated promptly, completely, with actionable guidance.
- **No AI companionship for the vulnerable without disclosure.** Where the system targets or is used by lonely or grieving users, AI-simulated relationship is disclosed clearly; the user is directed toward human support where appropriate.
- **Documented appeal language.** Suspension communications specify the violation, the evidence, the appeal process.

Per §137, the encyclical's framing of an "ecology of communication" suggests the broader frame: communication design is environmental. A platform that pollutes the commons of public communication is the analog of an industrial actor that pollutes a watershed. The audit reads it as such.
