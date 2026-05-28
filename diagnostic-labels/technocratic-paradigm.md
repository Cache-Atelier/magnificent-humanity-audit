# Diagnostic Label: technocratic-paradigm

## The encyclical's definition

*Magnifica Humanitas* draws the concept of the technocratic paradigm from *Laudato Si'*, where Pope Francis named it as a defining feature of the modern condition. *Magnifica Humanitas* §92 articulates it directly:

> "The tendency to let the logic of efficiency, control and profit alone shape personal, social and economic decisions. This makes it clear that technology is not simply a tool. When it becomes the standard by which everything is judged, it begins to dictate what matters and what can be discarded, reducing creation to an object of exploitation and human beings to mere cogs in a system driven toward ever greater efficiency."

The encyclical extends this framing in §93–94. The technocratic paradigm is fueled by the expansion of AI, cognitive science, nanotechnology, robotics, and biotechnology — innovations that, "precisely because of their power, can also hasten the expansion of the technocratic paradigm and therefore require a new spiritual, ethical and political framework."

Guardini's line is cited here in §93: "Contemporary man has not been trained to use power well." The technocratic paradigm is, in part, the institutional encoding of this untrained power — efficiency as default without the moral formation that would orient efficiency toward human good.

## What it looks like in software

The technocratic paradigm is the most common diagnostic label in audits because most contemporary software is shaped by it. Patterns that warrant this label:

- The user is modeled as a behavioral profile to be optimized
- Engagement, retention, conversion, or revenue are the system's primary success metrics, with no comparable measure of user good
- A/B testing infrastructure treats human responses as data points to optimize against, without question of what is being optimized toward
- Decisions about users are made by algorithm because algorithms are faster; the absence of human judgment is celebrated
- The system measures, classifies, scores, ranks, and segments persons as a default mode of operation
- "Efficiency" is taken as self-evidently desirable, without question of what is being made efficient
- Data is collected because data is valuable, without specific use cases requiring it
- The system's design proceeds from what is technically feasible to what is profitably deployed, without a deliberate moral pause

Per §93, "more power does not necessarily imply something better." The technocratic paradigm is the institutional inability to recognize this — to recognize that increased technical capability creates the need for increased moral attention, not less.

## What the encyclical opposes it with

The encyclical's alternative is not anti-technology. Per §85, "Technological innovations, including artificial intelligence, are not neutral, for they can either foster participation and justice or exacerbate inequality, control and exclusion." Technology is not the problem. The technocratic paradigm is — the framing in which technology becomes the standard by which everything is judged.

The alternative is integral human development (Principle 7). Technology evaluated by whether it helps individuals and peoples become more humane and fraternal, while respecting the common home and future generations. Per §94, "having more" without "being more" — the technocratic paradigm produces the former; integral human development requires the latter.

## When to use this label

Use technocratic-paradigm when:

- The finding turns on the system measuring, optimizing, or extracting something from persons that should not be treated as input
- The finding turns on the absence of human judgment where human judgment is morally required
- The finding turns on efficiency or scale being treated as self-evidently good
- The finding turns on the user being treated as means rather than end
- The system's logic of operation is consistent across personal, social, and economic dimensions — efficiency, control, profit as the integrated logic

Most findings under principles 1, 2, 4, 5, and 6 will warrant this label. Findings under principle 3 (universal destination of goods) often warrant it as well — concentration of platform capacity is the technocratic paradigm at scale.

## Example finding

```
2. Recommendation algorithm uses 47-feature engagement model with no community-health signal
   
   Location: services/feed/ranker.py:204-340
   Confidence: 95
   
   Behavior: The feed ranking model uses 47 features, all engagement-derived (click probability, 
   dwell prediction, share probability, comment probability, return probability, etc.). No 
   feature represents community health, user-reported satisfaction, content accuracy, or aggregate 
   effect on the platform's conversation. The model is retrained weekly against fresh engagement 
   data.

   Violation: This violates the principle of the common good. Per Magnifica Humanitas §61, 
   "the mere sum of individual interests is not capable of generating a better world for the 
   whole human family." The ranker optimizes individual-engagement signals exclusively; the 
   "plus" of common good — the aggregate effect on the platform's conversation, on user 
   well-being, on truth in public discourse — is not modeled. The result is a system that may 
   maximize engagement while degrading the commons it serves.

   Resembles: technocratic-paradigm — the user's attention is treated as input to be optimized 
   for system metrics; the broader effects on the platform's culture and the user's life are 
   treated as externalities outside the model's scope.

   Remediation:
   — Add community-health signals to the ranking model: user-reported satisfaction with what 
     they see, share of users who report feeling worse after using, ratio of constructive to 
     inflammatory engagement
   — Treat downranking of inflammatory or false content as a first-class signal, not an 
     after-the-fact moderation step
   — Establish a regular review where ranking changes that increase engagement but decrease 
     community-health signals are not shipped
   
   Structural note: This finding is likely tied to the platform's business model. If revenue 
   tracks engagement, the engineering team alone cannot solve the principle-violation without 
   revenue-model engagement from leadership.
```

## A note on charity

The technocratic paradigm describes a structural pattern, not malice. Per §102, AI systems that present as neutral and objective "end up reflecting and reinforcing the stereotypes or ideological bias of their designers and developers." The pattern is structural, often unwitting, and pervasive precisely because it is the water in which contemporary software development swims.

The audit names the pattern without imputing bad faith to the developers. Most engineers operate within institutions whose logic is technocratic; naming the pattern is part of the work of reorientation, not accusation.
