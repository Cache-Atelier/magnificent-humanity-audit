# Locus 5: Engagement and Attention Design

> "Platforms and services are often designed to capture users' time and attention, exploiting their vulnerabilities and weakening their inner freedom. When business models thrive on human weakness, the person is treated as a means rather than as an end." — *Magnifica Humanitas* §170

## What this locus covers

The architecture by which the system holds and shapes user attention. This includes:

- Notification systems: triggers, timing, content
- Re-engagement campaigns: dormant-user nudges, win-back emails, push sequences
- Streaks, badges, points, and progress mechanics
- Variable-reward systems
- Pull-to-refresh, infinite scroll, autoplay
- "FOMO" cues, social-pressure prompts, ephemeral content with deadlines
- Friction in disengagement: how easy is it to stop, leave, log out, delete the app?
- Default attention claims: what the system surfaces unprompted

The encyclical names this directly in §170. The substance of the violation is the use of design choices that "thrive on human weakness." The audit reads engagement design not as one feature among many but as a primary indicator of what the system fundamentally values.

## Principles most engaged

- **Integral human development** (Principle 7): the foundational principle. Per §85, technologies must help individuals become more humane and fraternal. Attention-extracting design works against this aim.
- **Human dignity** (Principle 1): per §51 and §170, the user as means vs. end.
- **Solidarity** (Principle 5): engagement design that exploits loneliness, social anxiety, or attention vulnerability fails the encyclical's framing of solidarity.
- **Common good** (Principle 2): aggregate engagement-extraction degrades the broader culture, the user's relationships, and civic life.

## What to look for

### The notification system

Notifications are revealing because they are the system reaching out to claim attention. The audit asks:

- What triggers a notification? User-stated preference, or system-determined event?
- Is the timing fixed (user has chosen) or variable (system optimizes)?
- Are there random or pseudo-random elements in the timing? Variable-reward conditioning is named in psychology literature; the encyclical's framing in §170 is the moral counterpart.
- Is content modeled to maximize re-engagement? Is the prediction model itself a feature?
- What categories of notification exist? Are they user-controllable?
- What is the default notification setting?
- Are notifications truly informational, or are they emotional triggers (social signals, urgency cues, social-comparison content)?

### Retention mechanics

Beyond notifications, look at the system's broader retention apparatus:

- **Streaks.** Days-in-a-row counters that the user "loses" if they don't return. These are well-documented in psychological literature as exploitative. Per §170, they "thrive on human weakness" — specifically loss aversion.
- **Points, badges, levels.** Gamification that creates artificial goals beyond the user's stated reasons for being on the platform.
- **Social-pressure prompts.** "Your friends are posting without you." "X people have replied to this thread you haven't seen."
- **Ephemeral content with countdowns.** Stories that disappear in 24 hours, deals that expire. The cues induce urgency.
- **Variable-reward feeds.** Refresh shows new content; sometimes interesting, sometimes not; the variability itself is what hooks. This is a documented mechanism; the encyclical's framing names it morally.
- **Autoplay.** The next item starts before the user has decided to watch it.
- **Infinite scroll.** No natural stopping point.
- **Win-back campaigns.** Email, push, SMS sequences targeting users who have stopped using the system, often with escalating intensity.

### Disengagement friction

The encyclical's framing in §170 emphasizes "inner freedom." A system that respects inner freedom is one the user can leave easily:

- Is it easy to log out?
- Is it easy to take a break (snooze the app, mute notifications, set quiet hours)?
- Is there a "done for today" surface, or does the system always have a "what's next"?
- Is there friction when the user tries to delete or uninstall? Confirmations, alternatives, regret-engineering ("are you sure? you'll lose your streak")?

### Children and the vulnerable

Per §141, the encyclical is direct: "early and unsupervised exposure to digital devices and social media can negatively impact sleep, attention span, control of emotions and relationships." Engagement design aimed at or affecting minors warrants special scrutiny:

- Are age-gated systems actually gated?
- Are engagement mechanics that exploit weakness (streaks, variable rewards, social comparison) present in features children use?
- Are there parental controls? Real ones?
- Per §142, what is the system's response when its engagement mechanics conflict with the well-being of minors?

## Common findings

- **Variable-reward notification timing.** The notification scheduler uses randomization or model-driven variability to maximize the user's re-engagement probability. Variable reward is the explicit hook.
- **Streaks the user can lose.** Days-in-a-row counters with no upside but the streak itself; functions through loss aversion.
- **Social-pressure prompts.** Notifications that are not informational but social-pressure-driven. "Your friends..." cues.
- **No "done for today" surface.** The system has no concept of a user being finished. Every screen offers more.
- **Autoplay by default.** The user is not asked; the next item starts.
- **Re-engagement campaigns on dormant users.** Email and push sequences targeting users who have left, designed to bring them back.
- **Engagement mechanics on children's features.** Streaks, gamification, social-comparison cues, variable-reward feeds present in features used by minors.
- **Friction in uninstall or account deletion.** "Are you sure" stages, regret cues, alternatives offered (snooze, log out instead) that try to prevent the action.

## How to gather evidence

When source code is available:
- Read the notification scheduler. Search for `notification`, `push`, `schedule`, `re-engagement`, `winback`
- Look for models that predict user actions — they often feed notification timing
- Search for `streak`, `badge`, `points`, `level`, `gamification`
- Read the autoplay and infinite-scroll implementations; note default state and any user control
- Read the uninstall and account-deletion flows; note any retention attempts
- Search analytics events for re-engagement metrics: `notification_opened`, `winback_clicked`, `streak_continued`

When only product access is available:
- Create an account and use the app normally; document each engagement mechanic encountered
- Stop using the app for several days; document the win-back outreach (push, email, SMS)
- Attempt to log out, take a break, or delete; document the friction
- Read app store reviews and prior research; specific engagement patterns are often documented
- For children's products: assume children are using them; audit accordingly

## Remediation patterns

- **Notifications by user-stated preference, not by re-engagement modeling.** The user states what they want to be notified about and when; the system honors this.
- **Predictable timing.** Notifications arrive at predictable times the user has set. No variable-window randomization.
- **Remove streaks that punish exit.** Counters that work through loss aversion are replaced with achievements the user can hold without ongoing return.
- **Replace variable-reward feeds with predictable structures.** Where feeds exist, default to chronological or user-controlled. Variable-reward mechanics are an opt-in feature, not a default.
- **Add "done for today" surfaces.** When the user has accomplished what they came for, the system says so and lets them go. The system tracks user-stated tasks and respects their completion.
- **Disable autoplay by default.** The user is asked whether to continue.
- **Reduce friction on disengagement.** Logout, snooze, take-a-break, delete — all easy, no retention dark patterns, no regret-engineering.
- **Differentially restrict engagement mechanics for minors.** Per §141–142, age-appropriate design is the constraint. Streaks, variable rewards, social-pressure cues should be absent or reduced for users under 18.
- **Measure user-reported well-being alongside engagement.** Add metrics that ask whether the user feels the system supported what they came to do. Treat declines as failures.

When the issue is non-local — when the system's revenue depends on attention extracted — the structural note is unavoidable. Per §95, the encyclical names the structural pattern: "control over platforms, infrastructure, data and computing power... tends to become opaque and evade public oversight." The tactical remediation is the one above; the structural remediation engages the business model, which is outside the engineering team's control but within the audit's honest framing.
