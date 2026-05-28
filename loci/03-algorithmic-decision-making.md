# Locus 3: Algorithmic Decision-Making

> "Entrusting an algorithm in practice with the power to select who is worthy or not, without anyone bearing responsibility for that judgment, is to hand over the task of redefining the boundaries of human possibilities." — *Magnifica Humanitas* §103

## What this locus covers

The decisions the system makes about users through automated systems, and the structures of accountability, recourse, and transparency around those decisions. This includes:

- Ranking and recommendation
- Visibility decisions (what is shown, what is suppressed)
- Eligibility decisions (who can access what, who is offered what)
- Credit, lending, insurance, employment, housing, and other consequential decisions
- Content moderation
- Account suspension, restriction, demonetization, deboosting
- Fraud, abuse, and risk scoring
- Identity and authentication decisions
- Personalization that materially differentiates between users

This locus is among the most explicit areas of the encyclical's concern. Chapter 3 paragraphs 102–110 address algorithmic decision-making directly, with §80, §102, §103, §104, and §105 the operational anchors.

## Principles most engaged

- **Subsidiarity** (Principle 4): the foundational principle. Per §71, the four operational requirements (independent checks, algorithmic transparency, equitable data access, recourse) are the test.
- **Human dignity** (Principle 1): per §103, when algorithms decide who is "worthy" without responsibility, dignity is directly violated.
- **Social justice** (Principle 6): per §80, opaque algorithms that perpetuate prejudice and discrimination are explicitly named as the concern of social justice in the digital age.
- **Common good** (Principle 2): algorithms that decide visibility decide the conditions of public communication and the shape of the commons.

## What to look for

### Where algorithms make decisions

Identify every place in the system where an automated decision affects a user:

- **Ranking and recommendation.** What is surfaced and what is hidden? What signals drive the surfacing?
- **Search and discovery.** Whose content is found? Whose is rendered invisible?
- **Eligibility for features.** Who is offered what? Why?
- **Credit and risk scoring.** What scores does the system compute? What do they cause?
- **Moderation.** What content is removed automatically? What accounts are suspended automatically? What is the false-positive rate?
- **Fraud and abuse detection.** Who is flagged? What happens when flagged? What is the appeal path?
- **Verification and identity.** Who is verified? On what grounds? What happens to those who can't or won't verify?
- **Personalization that materially differentiates.** Different prices? Different terms? Different content libraries?

### The accountability structure

For each decision the system makes:

- **Is the decision explainable?** Can the system articulate why the decision was made? Can the affected user be told why?
- **Is there a human in the loop?** Before the decision is enacted? After, on appeal? At what point in the chain?
- **Is there an appeal path?** Documented? Reachable? Bounded in time?
- **Does the appeal reach a human?** Or is the appeal also algorithmic?
- **Who is responsible if the decision was wrong?** A team? A person? "The model"?
- **Is the decision auditable?** Logged? Reviewable? Reproducible?

Per §105, "the possibility of identifying who must 'account' for decisions, justify them, monitor them, and, when necessary, challenge them and remedy any harm caused."

### Disparate impact

For consequential decisions, the system must be auditable for disparate impact:

- Are the decision outcomes audited by demographic, geographic, linguistic, or other protected and historically marginalized classes?
- Are these audits public, or only internal?
- When disparities are found, what is the response?
- Is the training data itself audited for representativeness?
- Are model updates evaluated for changes in disparate impact?

Per §102, "When AI systems present themselves as neutral and objective, they end up reflecting and reinforcing the stereotypes or ideological bias of their designers and developers." This is structural, not malicious. The audit must read structurally.

### The illusion of neutrality

Per §104: "every technical tool embodies choices and priorities through what it measures, ignores and optimizes, and how it classifies people and situations." Look for places where the system claims neutrality but is making consequential choices:

- "The algorithm decides" framing in user-facing copy
- Documentation that asserts objectivity without grounding it
- Decisions presented as numerical (a score, a probability) without explanation of what feeds into the score
- The absence of human responsibility framed as a feature ("removed bias by removing humans")

## Common findings

Patterns that often surface in this locus:

- **Consequential decisions without appeal.** Account suspensions, content removals, eligibility denials issued by algorithm with no human review and no reachable appeal path.
- **Theatrical appeal.** An appeal path exists in policy; the appeal process is also algorithmic; the second decision matches the first.
- **Buried recourse.** The right exists; the surface to invoke it is six menus deep, in legal language, in English only.
- **Score-driven differential treatment.** A score the user cannot see drives the experience: visibility, support quality, eligibility for features. The user cannot improve the score because they don't know what it tracks.
- **Black-box recommendation.** Recommendations are entirely opaque. No user controls, no documented signals, no way to know why something was surfaced.
- **Anti-abuse systems that discriminate.** Fraud and abuse detection that flags users by language, dialect, region, behavior pattern, in ways that correlate with marginalization.
- **Identity verification that excludes.** Verification requirements that exclude users without specific government documents, smartphones, or English fluency.
- **Moderation by algorithm with no human review.** Speech that's removed by AI with no human in the loop. False-positive rates undocumented; appeal closes the loop without changing outcomes.

## How to gather evidence

When source code is available:
- Identify every decision endpoint. Search for terms like `decide`, `predict`, `score`, `classify`, `rank`, `recommend`, `flag`, `moderate`, `suspend`, `restrict`, `verify`, `approve`, `deny`
- Read the model training pipeline. What data trains it? What does it predict?
- Read the appeal handler, if one exists. Is the appeal also automated?
- Search for "human review," "manual review," "escalation." How frequently is human review triggered?
- Read content moderation policies and the corresponding code
- Read fraud and abuse detection code; note the features used
- Look for documentation: model cards, system cards, fairness audits

When only product access is available:
- Trigger decisions and document them. Account suspension paths, content removal, eligibility denials
- Test the appeal process. How long does it take? What is the response? Who responds?
- Read public transparency reports
- Search for academic papers studying the system's algorithmic decision-making
- Test the system with edge-case users: minority languages, non-Western names, content in dialects, low-resource regions

## Remediation patterns

- **Document the algorithm.** Publish the signals, the approximate weights, the model's purpose. Per §71, "transparency regarding algorithms" is a subsidiarity requirement.
- **Add human-in-the-loop for consequential decisions.** Define which decisions are consequential and require human review before enactment (or human-reachable appeal after).
- **Bound the appeal time.** An appeal that takes weeks while the user's account is suspended is not real recourse. Set bounded timeframes; meet them.
- **Make recourse legible.** The path from "I think this decision was wrong" to "a human is reviewing it" should be one or two clicks from where the user encountered the decision.
- **Audit for disparate impact.** Regularly, publicly, by population. When disparities are found, treat them as bugs.
- **Document model lineage.** Where data came from, how it was labeled, what populations are represented, what the known limitations are.
- **Remove the score where the score is consequential and uncontested.** If a fraud score is causing user harm and the user has no way to contest the score, the score is operating outside the principle of subsidiarity. The remediation is either to expose the score (so the user can contest it) or to remove its consequential weight.

Per §107, "what is needed is a more active political involvement that is capable of slowing things down when everything is accelerating." For algorithmic decision-making, the analog is: where the system cannot defend its decision, the system must slow down. Decisions without accountability should not be issued.
