# Diagnostic Label: transhumanism

## The encyclical's definition

*Magnifica Humanitas* §115–117 introduces the framing. The encyclical's articulation in §116:

> "Transhumanism envisions the enhancement of human beings through technologies — such as biomedicine, body engineering, devices and algorithms — with the aim of increasing performance and capabilities."

In §117 the encyclical names what makes the framing problematic:

> "If the human being is treated as something to be perfected or surpassed, it becomes easier to accept that some lives are less useful, less desirable or less worthy. In the name of progress, 'necessary sacrifices' may begin to be justified, placing the burden on the most vulnerable in pursuit of a supposed optimization of the species."

§112 sets the broader context:

> "The fullness of life is equated with having more, reducing weakness, eliminating uncertainty and exerting total control. When efficiency becomes the ultimate measure of value, human beings are tempted to see themselves as a project to be optimized rather than as persons called to relationship and communion."

The encyclical's critique is not of every form of human enhancement. Eyeglasses, antibiotics, surgical intervention, and accessibility technology are not what is at stake. The critique is of the *framing* — the implicit anthropology in which human limitations are defects, and technology is the means of eliminating them.

The deeper objection is in §118–122. The encyclical insists that humanity flourishes not despite limitations but often through them. Compassion, generosity, spiritual experience, the wisdom learned through suffering and failure — these are not pathologies to be optimized away. They are constitutive of what it is to be human. A technology that promises to eliminate them, even if successful, would eliminate something essential.

## What it looks like in software

The transhumanist framing in software is often subtle. It typically appears not in explicit transhumanist marketing (rare outside niche communities) but in product framings that treat limitations as defects:

- AI features that treat the user's inability to remember as a defect to be corrected by total recall systems
- Productivity tools that treat the user's tendency to be distracted as a defect to be corrected by attention modeling and elimination of friction
- Communication tools that treat the user's pace of thought and writing as a defect to be corrected by AI completion and generation
- "Augmented" experiences that progressively reduce the user's role to that of an approver of system-generated outputs
- Health and wellness products framed around the elimination of weakness, suffering, or vulnerability rather than their integration
- AI companions that promise to eliminate loneliness through perfect simulated relationship
- Optimization framings applied to relational, emotional, or spiritual dimensions of life

The clearest indicator is in the system's framing copy: language about "optimizing" or "upgrading" or "enhancing" the human, or about "removing the friction" of being a person.

## When to use this label

Use transhumanism when:

- The system treats a human capacity, limitation, or weakness as a defect to be corrected
- The system's AI features replace rather than augment a capacity the user has
- The framing of the product positions the user's limitations as the problem the system solves
- The system promises to eliminate friction in domains where friction is part of the good (writing, thinking, deliberating, relating, grieving)
- The system's metric of success is the user being optimized in some dimension where optimization is anthropologically suspect (attention, mood, productivity, relationship)

Distinguishing from posthumanism: transhumanism wants to enhance the human; posthumanism wants to surpass the human. Transhumanism keeps the human as the subject of optimization; posthumanism dissolves the boundary between human and machine. In ambiguous cases, transhumanism is the more conservative and more commonly applicable label.

Distinguishing from technocratic-paradigm: the technocratic paradigm describes any logic of efficiency-optimization-control applied broadly; transhumanism describes that logic specifically applied to the human person as object of optimization. A monetization scheme might be technocratic without being transhumanist; an AI feature that promises to eliminate the user's need to think might be both.

## Example finding

```
4. AI writing assistant operates as substitute rather than augmentation
   
   Location: features/writing-assistant/composer.ts:108-245
   Confidence: 85
   
   Behavior: The writing assistant generates complete drafts from minimal prompts. The interface 
   centers the AI's output as the document; the user's role is to approve, lightly edit, or 
   regenerate. The flow is optimized to minimize the user's writing input — the most common 
   path through the feature involves the user writing a single-sentence prompt and accepting 
   the generated draft with minor edits.

   Violation: This violates the principle of integral human development. Per Magnifica Humanitas 
   §140, "the speed and ease with which answers or summaries can be obtained risk extinguishing 
   the desire to ask questions, which is a process that bears fruit only over time... we must 
   learn, then, how to exercise restraint in the use of AI and to protect our young people from 
   the promise of the perfect machine, from that subtle temptation which renders human thought 
   seemingly superfluous precisely when it is most needed." The composer here renders human 
   thought superfluous in exactly this sense — the writing capacity the user is exercising is 
   the AI's, not their own.

   Resembles: transhumanism — the user's writing capacity is treated as friction to be 
   eliminated; the AI is positioned as a replacement for, rather than augmentation of, the 
   user's own thought.

   Remediation:
   — Reframe the assistant from generation to augmentation: suggest phrasings on user-drafted 
     text, surface alternatives at user request, offer to develop a thread the user has begun
   — Default the flow to user-led: the user writes; the assistant supports
   — Add explicit acknowledgment of AI contribution to the document, so the user remains aware 
     of which parts are their own thought and which are the AI's
   — Consider adding a "no AI" mode that gives the user the editor without the generation feature
   
   Structural note: where the product's stated value proposition is "AI does the writing for 
   you," the remediation requires revisiting the value proposition. This is a structural 
   conversation, not only a feature change.
```

## A note on grace

The encyclical's deepest counter to transhumanism is theological. §127 introduces Christian humanism's claim that human beings *are* called to self-transcendence — to become "more than human" — but through grace received in Christ, not through technical enhancement.

Aquinas is cited here: the process of elevation and transformation "surpasses every capability of created nature" (§127). Per Francis quoted in §128: "We become fully human when we become more than human, when we let God bring us beyond ourselves in order to attain the fullest truth of our being."

This is the encyclical's claim that transhumanism is, in part, a heretical imitation of authentic Christian self-transcendence — promising through technology what only grace can deliver. The audit does not impose this theological framing on findings; it operates with the encyclical's more accessible critique that transhumanism treats human limitation as defect rather than as the condition in which we mature.
