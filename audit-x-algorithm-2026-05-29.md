# An anthropological audit of X “For You” Feed Algorithm

This reads the system against the seven principles of Catholic social doctrine set out in the encyclical *Magnifica Humanitas*, asking what its workings imply about the human person.

**Date:** 2026-05-29
**Scope:** The open-sourced X recommendation stack at `github.com/xai-org/x-algorithm` — `home-mixer` (Rust orchestration), `phoenix` (Python/JAX Grok-transformer retrieval + ranking), `grox` (Python Grok-as-judge content classifiers), `thunder` (Rust in-memory post store + Kafka ingestion), and the `candidate-pipeline` framework. ~25.5K LOC across 139 Rust and 68 Python files.
**Evidence:** Source code
**Repository:** https://github.com/xai-org/x-algorithm

---

## Synthesis

**Toward Babel** — 10 findings · of 7 principles: 7 violated

Read functionally, this system has one telos: to predict and maximize engagement. The final feed score is a pure weighted sum of predicted engagement probabilities — favorite, reply, repost, click, share, and crucially dwell time, with a not-dwelled penalty (`ranking_scorer.rs:125-173`). No term represents truth, accuracy, formation, well-being, or whether the user wanted the time they spent. Around that objective the system builds the apparatus Magnifica Humanitas names most precisely: it profiles users on inferred attributes they never declared — predicting gender even for accounts hours old — and force-enables that profiling on roughly half of live traffic by OR-ing past its own feature flag; it exports identifiable behavioral telemetry (raw IP, persistent `device_id`, the full served stream, per-post prediction vectors) to private training corpora with no consent, retention limit, or deletion path; it enacts consequential automated judgments over speech (safety/PTOS suppression, visibility filtering, a "quality" score) with no author notification, no appeal, and no accountable owner in code; it has no misinformation or synthetic-media category in its safety taxonomy; and it fetches the viewer's age, then discards it — a minor receives the identical attention-maximizing, adult-tuned feed.

This is the §172 anthropology stated almost verbatim in code: the person modeled "as an object to be manipulated or a resource to be optimized" — a bundle of predicted engagement and aversion probabilities. The principles most centrally violated are subsidiarity (§71: opacity, no recourse, the platform as unchecked "highest level"), the attention-economy and profiling power of §170–172, social justice (§80: surveillance, unprotected minors, no defense of the truth-commons), and the universal destination of goods (§67, §108: data and algorithms held as private capital).

It is not pure Babel. The system attenuates for author diversity, listens to explicit aversion (block/mute/report carry negative weight), runs a mandatory per-recipient safety filter rather than offloading harm to opt-in muting, honors deletion in its in-network store, and documents its own mechanics with unusual candor. The materials for Jerusalem are present. But against the §85 litmus — does it help the person become "more humane and fraternal"? — the objective never asks the question; it optimizes session length. Per §129, "if power grows while the heart withers and human bonds fray, then we are faced with a new form of Babel." On the evidence of what it measures and ignores, this system is built toward Babel — structurally, not maliciously — and the same machinery that already attenuates and listens could be turned toward the person if the telos changed.

---

## The findings, by principle

One row per finding, one column per principle. `●` = violates that principle · `◐` = strains it · `·` = not engaged.

| # | Anthropological bug | Dig | C.G. | U.D. | Sub | Sol | S.J. | I.D. | conf |
|---|---|---|---|---|---|---|---|---|---|
| 01 | The ranking objective is a pure weighted sum of predicted engagement – including attention-duration – with no truth, value, or well-being term | · | ◐ | · | · | · | · | ● | 88 |
| 02 | The safety taxonomy has no misinformation, disinformation, or synthetic-media category | · | ● | · | · | · | ● | · | 86 |
| 03 | The system infers protected attributes the user never declared – predicting gender even for hours-old accounts – and force-enables this profiling on ~50% of live traffic, bypassing its own gate, with no consent path | ● | · | · | ● | · | ● | · | 86 |
| 04 | Identifiable behavioral telemetry is exported to private training/analytics topics keyed to the real user, with identity over-provisioned beyond what the payloads require, and no consent, retention, or deletion path | · | · | ● | · | ● | ● | · | 85 |
| 05 | The corpus that supervises the model is built from users' own harvested behavior and held as a private, ungoverned asset – and deletion does not propagate to derived embeddings or summaries | ● | · | ● | · | · | · | · | 85 |
| 06 | Consequential automated judgments over content and persons are enacted with no author notification, no appeal, and no accountable owner in code | ● | · | · | ● | · | ● | · | 84 |
| 07 | The viewer's age is fetched, then discarded – minor status never escalates the safety gate nor gates the engagement ranking | · | · | · | · | · | ● | ● | 83 |
| 08 | The ranking and classification logic that governs people is not transparent to them: no in-product explanation, no off-switch or chronological alternative, and the operative policy prompts and weights are withheld from the "open" release | · | · | · | ● | · | · | · | 80 |
| 09 | Fully automated moderation of disturbing content discloses nothing about the human-labeled examples it depends on | · | · | · | · | ◐ | ◐ | · | 84 |
| 10 | Device advertising identifier and device/IP fingerprints are sent to ad selection with no per-ad targeting rationale carried back to the user | · | · | · | · | · | ◐ | · | 80 |

Column key — Dig: The dignity of the human person §48–58 · C.G.: The common good §59–64 · U.D.: The universal destination of goods §65–67 · Sub: Subsidiarity §68–72 · Sol: Solidarity §73–76 · S.J.: Social justice §77–81 · I.D.: Integral human development §82–85.

**By principle:** **The dignity of the human person** — violated: Never the primary locus of a finding, but explicitly violated by the profiling, retention, and judgment findings — the person modeled as a bundle of predicted engagement and aversion probabilities (§172). **The common good** — violated: Violated through the truth-commons: the feed shapes public discourse with no misinformation axis, and per §132 truth is a common good the design leaves unguarded. **The universal destination of goods** — violated: Among the most centrally violated: behavioral data, served history, and derived embeddings — the product of many contributors (§108) — are held and exported as private training capital with no consent, retention limit, or deletion path. **Subsidiarity** — violated: Among the most centrally violated (§71): opacity, no recourse, the platform as unchecked "highest level" — consequential judgments enacted with no appeal and the operative criteria withheld from the release. **Solidarity** — violated: Violated by the identifiable-telemetry export and engaged by the hidden, undocumented human labeling labor the safety classifiers depend on (§173). **Social justice** — violated: Among the most centrally violated (§80): invasive surveillance, inferred protected attributes, unprotected minors, and no defense of the truth-commons. **Integral human development** — violated: Violated most directly by the objective itself: pure engagement-and-dwell maximization that never asks the §85 question — whether it helps the person become more humane.

---

## The findings, in detail

### 01. The ranking objective is a pure weighted sum of predicted engagement – including attention-duration – with no truth, value, or well-being term — confidence 88

*Engages:* violates Integral human development · strains The common good

**Code evidence:**

```rust
// compute_weighted_score — each term is apply(score, weight) = score × weight
//   :159  dwell_score × dwell             (attention-duration term)
//   :163  dwell_time × cont_dwell_time    (continuous dwell, a regression target: phoenix/runners.py:257,424)
//   :164  click_dwell_time
//   :170  not_dwelled penalty — summed into the negated group at :83
// inputs: PhoenixScores (candidate_pipeline/candidate.rs:30-51) — predicted-action fields only;
// duplicated in scorers/weighted_scorer.rs:44-67
```
`Location: home-mixer/scorers/ranking_scorer.rs:125-173`

```text
Final Score = Σ (weight_i × P(action_i))
```
`Location: README:286-292`

```python
# quality_score / slop_score — computed offline by the grox "banger" classifier,
# never referenced in the serving path
```
`Location: grox/classifiers/content/banger_initial_screen.py`

**Behavior:** Each term is `apply(score, weight) = score × weight`. Every positive term is a predicted engagement probability (favorite, reply, retweet, photo_expand, click, profile_click, video-quality-view, share, share-via-DM, share-via-copy-link, dwell, quote, quoted-click, dwell_time, click_dwell_time, follow_author); the only negative terms are predicted aversive reactions (not_interested, block_author, mute_author, report, not_dwelled). The `PhoenixScores` struct contains exclusively these predicted-action fields — no truth, accuracy, source-credibility, content-quality, or user-value field exists. The system additionally rewards content predicted to hold attention longer (continuous `dwell_time`, not a capped did-the-user-look flag) and demotes content the user would scroll past (`not_dwelled`). A `quality_score`/`slop_score` is computed offline by the grox "banger" classifier but is architecturally disconnected and never enters the score: truthful and false content rank identically when they engage equally.

**From *Magnifica Humanitas*:**

> §104 “embodies choices through what it measures, ignores and optimizes”
> — This objective measures and optimizes engagement and dwell, and ignores whether content is true, formative, or wanted; the demonstrable existence of an unused quality signal sharpens the §104 charge.

> §170 “platforms... capture users' time and attention, exploiting their vulnerabilities”
> — Rewarding attention-duration is exactly this attention-economy mechanism — when a business model "thrive[s] on human weakness, the person is treated as a means rather than as an end."

**Violation:** This violates integral human development and the technocratic-paradigm warnings most directly. Per §94 the score rewards "having more" without "being more." Per §132 truth is a common good; with no truth term, false and true content rank alike. It cannot pass the §85 litmus, because no part of the objective asks whether it makes the person "more humane."

**Resembles:** technocratic-paradigm — discourse and attention reduced to predicted engagement probabilities; the operative standard of worth becomes capacity-to-engage, and the user's attention-duration is an input to be optimized for session length rather than a good to be served.

**Remediation:**
- Introduce a non-engagement objective term sourced from periodic user surveys ("was this worth your time?") and weight it materially in the final score; treat sustained declines in self-reported value as non-shippable ranking regressions even when engagement rises.
- Wire the already-computed `quality_score`/`slop_score` into the scorer as an explicit term weighted to downrank likely-false-but-engaging content; today it is computed and discarded.
- Cap the dwell signal at a short "did the user actually look" threshold rather than a monotonic longer-is-better reward, and weight explicit-intent signals (favorite/reply/share/follow) above passive duration.
- Per §104, document what each weight optimizes for and publish the default weight vector and the action set.

**Structural note:** An objective composed only of engagement proxies is the rational design under an attention/advertising business model; the dwell reward exists because the model monetizes session time and ad impressions. Wiring in a well-being or truth term that can lower engagement is a telos change, not a code change — the weights are operator-tunable params (`xai_feature_switches`), so the emphasis on dwell is ultimately a policy decision, not fixed in source.

---

### 02. The safety taxonomy has no misinformation, disinformation, or synthetic-media category — confidence 86

*Engages:* violates Social justice, The common good

**Code evidence:**

```python
SUPPORTED_POLICY_CATEGORIES = {
    SafetyPolicyCategory.ViolentMedia,
    SafetyPolicyCategory.AdultContent,
    SafetyPolicyCategory.Spam,
    SafetyPolicyCategory.IllegalAndRegulatedBehaviors,
    SafetyPolicyCategory.HateOrAbuse,
    SafetyPolicyCategory.ViolentSpeech,
    SafetyPolicyCategory.SuicideOrSelfHarm,
}
# _get_policy_prompt (:166-185) routes only these and raises ValueError otherwise
# no misinformation / disinformation / synthetic-media axis
```
`Location: grox/classifiers/content/safety_ptos.py:217-225`

```rust
// NSFA_COMMUNITY_NOTE — the only truth-adjacent artifact — feeds solely the ads
// brand-safety verdict ("Not Safe For Advertising" inventory gating);
// consumed nowhere in organic ranking (scored_posts_server.rs:203)
```
`Location: home-mixer/models/brand_safety.rs:24`

**Behavior:** The complete enforced safety taxonomy is seven categories — ViolentMedia, AdultContent, Spam, IllegalAndRegulatedBehaviors, HateOrAbuse, ViolentSpeech, SuicideOrSelfHarm; `_get_policy_prompt` routes only these and raises `ValueError` otherwise. A repo-wide search for misinfo / disinfo / fact-check / deepfake / manipulated-media / civic-integrity / synthetic returns nothing in the content-judgment pipeline. The only truth-adjacent artifact, `NSFA_COMMUNITY_NOTE`, feeds solely the ads brand-safety verdict (`brand_safety.rs:24`, "Not Safe For Advertising" inventory gating) and is consumed nowhere in organic ranking.

**From *Magnifica Humanitas*:**

> §80 “combat hate and misinformation”
> — §80 lists this as a co-equal social-justice requirement; the pipeline implements hate (HateOrAbuse) but has no misinformation, manipulated-media, or false-claim axis at all.

> §132 “the ability to manipulate content, images and videos”
> — Per §132 truth is a common good threatened by exactly this ability.

> §135 “present a particular vision of reality as desirable”
> — Per §135 platform controllers hold this power.

**Violation:** This violates social justice and the common good. A pipeline that screens gore, nudity, and spam but is structurally blind to fabricated narratives leaves the truth-commons unguarded — and the one truth-adjacent signal that exists protects advertisers, not the public.

**Resembles:** technocratic-paradigm — "safety" is operationalized as enumerable harmful-content classes; truth/falsity is not modeled as a classifiable axis, so it is neither measured nor acted on (§104).

**Remediation:**
- Add a `SafetyPolicyCategory` for manipulated/synthetic media and demonstrably false claims, distinguishing deliberate fabrication from honest error.
- Where AI-generated or deepfake media is detected, write an integrity label into the existing `SafetyPostAnnotations` sink — a low-friction extension of an existing path.
- Promote an integrity signal into organic ranking as a downrank (not only ads gating), and decouple the truth axis from the NSFA/ads pathway so it protects the content-commons, not only advertiser inventory.

**Structural note:** Defining falsity at platform scale is contested, and delegating truth to crowdsourced Community Notes is a coherent good-faith philosophy. But the code undercuts that defense: the Community-Notes-derived signal exists only as a brand-safety/ads verdict, never as an organic integrity signal — so the truth axis is absent from the content-judgment pipeline entirely, not deliberately restrained within it.

---

### 03. The system infers protected attributes the user never declared – predicting gender even for hours-old accounts – and force-enables this profiling on ~50% of live traffic, bypassing its own gate, with no consent path — confidence 86

*Engages:* violates Social justice, Subsidiarity, The dignity of the human person

**Code evidence:**

```rust
// enable() returns:
query.params.get(EnableInferredGenderHydration) || query.is_shadow_traffic

// if no stored label and the account is brand new —
//   None if is_new_user(query.user_id)   // is_new_user: days_since_creation(user_id) == 0
// — it calls grpc_client.predict(query.user_id): an inferred gender label
// plus a prediction_score, written into the scoring query
// (demographics hydrated the same way: user_demographics_query_hydrator.rs:14-25)
```
`Location: home-mixer/query_hydrators/user_inferred_gender_query_hydrator.rs:31,34-58`

```rust
is_shadow_traffic = is_sampled(request_id, 0.5)  // a deterministic ~50% sample of real requests
// real viewer_id + scores published to Kafka: phoenix_experiments_side_effect.rs:134-138
// the fetched-but-unread age field: models/query.rs:74,177; server.rs:119
```
`Location: home-mixer/server.rs:117`

**Behavior:** The inferred-gender hydrator fetches a stored gender label; if none exists and the account is brand new — `None if is_new_user(query.user_id)`, where `is_new_user` is `days_since_creation(user_id) == 0` — it calls `grpc_client.predict(query.user_id)` to infer a gender label plus a `prediction_score`, writing both into the scoring query. Demographics are hydrated the same way. Critically, the only gate is OR-ed away for shadow traffic: `enable()` returns `query.params.get(EnableInferredGenderHydration) || query.is_shadow_traffic`, and shadow traffic is a deterministic ~50% sample of real requests — so half of live users are profiled on their real `user_id` even when the operator flag is off, with the real `viewer_id` plus scores published to Kafka. No read/correct/opt-out/delete path exists in the release. By contrast `user_age_in_years` is populated but read by no released code: the inferred targeting signal is computed and serialized while the protective signal sits unused.

**From *Magnifica Humanitas*:**

> §80 “social groups penalized by opaque algorithms”
> — Inferring and scoring on a protected attribute the user never declared — even predicting it for zero-history accounts — is exactly this risk.

> §171 “to profile, predict and influence behavior... without individuals being fully aware of it”
> — The §171 power, exercised here on half of live traffic with no consent.

> §104 “how it classifies people”
> — §104 locates the harm here: the system classifies by gender (a targeting signal) while ignoring the age field that could protect the vulnerable.

> §102 “the stereotypes or ideological bias of its designers”
> — §102 warns such inference reflects exactly this under a veneer of objectivity.

**Violation:** This violates social justice, subsidiarity, and human dignity. §70–71 (digital subsidiarity): the operator-level decision "do not profile" is overridden for the shadow half, with no algorithm transparency, equitable data access, or avenue for recourse — and any future user opt-out would likewise be defeated by this `||`. §108: the inference manufactures a personal-data label without the person's participation.

**Resembles:** technocratic-paradigm — persons are classified and profiled as a default substrate of model experimentation rather than through a consented act; the `flag || is_shadow_traffic` idiom recurs across hydrators, so the defect is structural, not an isolated oversight.

**Remediation:**
- Remove the `|| query.is_shadow_traffic` override so shadow traffic respects the same gate (and any user opt-out) as production; audit the same idiom across sibling hydrators.
- Default `EnableInferredGenderHydration` off; require explicit, revocable opt-in; stop predicting gender on the first session for brand-new accounts.
- Add a user-level consent object (modeled on the existing `allow_for_you_recommendations` preference at `server.rs:76`, which proves such gates are feasible) evaluated before — and not overridable by — any traffic-class flag.
- Let users view, correct, and delete the inferred label and score; audit ranking outcomes for disparate impact across inferred classes and publish the methodology.

**Structural note:** Inferring protected attributes to improve engagement-optimized ranking is intrinsic to a behavioral-targeting business model; removing it (versus making it transparent) is a business-model decision. Shadow-traffic feature parity is a platform-wide convention, so whether unbiased offline evaluation may run non-consensual profiling on live users at all is a telos question. The downstream consumer (`build_prediction_request`) is out of release, so whether inferred gender materially changes ranking cannot be proven here; the inference, scoring, and hydration are present and provable regardless.

---

### 04. Identifiable behavioral telemetry is exported to private training/analytics topics keyed to the real user, with identity over-provisioned beyond what the payloads require, and no consent, retention, or deletion path — confidence 85

*Engages:* violates The universal destination of goods, Solidarity, Social justice

**Code evidence:**

```rust
// RequestInfo: user_id + raw ip_address (:79) + user_agent (:80),
// alongside the full served stream — Kafka target: the Phoenix training cluster (:30)
```
`Location: home-mixer/side_effects/served_candidates_kafka_side_effect.rs:73-100`

```rust
// LogBase stamps raw IP (:280) + persistent client-supplied device_id (:285)
// onto aggregate tallies (served-tweet counts, video counts, request-size buckets)
// that need no device-level join key; enable gate at :38-40, no sampling
```
`Location: home-mixer/side_effects/client_events_kafka_side_effect.rs:277-301`

```rust
// 5% sample: the top-50 selected AND non-selected candidates,
// each carrying ~20 prediction scores, keyed to the raw viewer_id
// counter-example: phoenix_experiments_side_effect.rs:134-158 publishes NO ip / user_agent
```
`Location: home-mixer/side_effects/reranking_kafka_side_effect.rs:28-93`

**Behavior:** Multiple side effects ship identifiable per-user telemetry to Kafka. `served_candidates` carries `user_id`, raw `ip_address`, and `user_agent` alongside the full served stream to the continuously-trained Phoenix cluster. `client_events` stamps raw IP plus a persistent client-supplied `device_id` onto every served-feed event — yet those payloads are aggregate tallies (served-tweet counts, video counts, request-size buckets) that need no device-level join key. `reranking` exports, for a 5% sample, the top-50 candidate set (including candidates never shown) with ~20 predicted engagement/aversion scores each, keyed to the raw `user_id`. The team's own sibling `phoenix_experiments` side effect deliberately publishes no IP and no user-agent — demonstrating they are unnecessary for learning ranking. No anonymization, retention limit, or deletion path exists in the released tree (the only `delete` is a 50-row rolling-window capacity trim, not user erasure).

**From *Magnifica Humanitas*:**

> §108 “the product of many contributors”
> — Data "cannot be left solely in private hands" — here a user's served history, prediction profile, IP, and device fingerprint are piped into a private training corpus with no consent, retention limit, or way to access, control, or delete one's own contribution.

> §171 “when every action leaves a trace, a new power emerges: to profile, predict and influence behavior, often without individuals being fully aware of it”
> — Bundling raw IP + persistent device_id enables location inference and cross-session/cross-account linkage on payloads that do not need it — an over-provisioning the team's own sibling code avoids.

**Violation:** This violates the universal destination of goods, solidarity, and social justice. Per §80 this is invasive surveillance that should be subject to public oversight; §67 frames the underlying imbalance of concentrating data and infrastructure without sharing.

**Resembles:** technocratic-paradigm — a real user's served history, IP, and prediction vector become private training capital for the model-improvement flywheel; structurally adjacent to §178 digital-colonialism extraction (the code shows internal topics, not proof of monopolization).

**Remediation:**
- Strip `ip_address` and `user_agent` from the training-cluster export and drop raw IP + persistent `device_id` from the client-events LogBase; the sibling code and the existing `country_code`/`IpQueryHydrator` geo path prove neither is needed for these payloads.
- Pseudonymize the viewer key in training topics, segregate any re-identification keys under audited access, and replace persistent `device_id` with a rotating per-purpose pseudonym where a device signal is genuinely required.
- Document a retention/TTL and wire deletion propagation so account deletion purges these events and the user's Phoenix contributions; make model-training use of personal served history opt-in and offer users an export (portability).

**Structural note:** Treating the served stream as a private training asset is the core of the continuously-trained model flywheel; §108's demand to "manage data as a common or shared good" with control for contributors is a business-model change. The IP/user-agent inclusion, however, is a local code defect fixable immediately.

---

### 05. The corpus that supervises the model is built from users' own harvested behavior and held as a private, ungoverned asset – and deletion does not propagate to derived embeddings or summaries — confidence 85

*Engages:* violates The universal destination of goods, The dignity of the human person

**Code evidence:**

```python
# the supervision vocabulary IS users' behaviors:
# favorite, reply, repost, dwell, not_interested, block_author, report, dwell_time
# engagement-logit output head — the supervision targets: recsys_model.py:464-474,641
# phoenix/README.md:29-30 — "trained on the same real-time engagement data"; "trained continuously"
```
`Location: phoenix/runners.py:233-253`

```python
# per-post embedding + v3 summary text persisted, keyed by int(post.id)
# kafka_loader.py:157-232 — loaders subscribe only to content-understanding/embedding
# topics: no delete consumer, delete topic, or tombstone handler anywhere
# contrast thunder/posts/post_store.rs:69,279 — delete applied only to thunder's in-memory store
```
`Location: grox/tasks/task_write_mm_embedding_sink.py:47-91`

**Behavior:** The ranking model is supervised by users' captured engagement — the predicted-action vocabulary is the set of user behaviors, and the README states the production model "is trained continuously on real-time data." A grep for consent / opt-out / data-card / provenance / compensation returns nothing. Separately, grox derives per-post multimodal embeddings and (in v3) Grok-generated summary text and writes them to a persistent Strato sink keyed solely by `post.id`, republishing to Kafka. When a user deletes a post, thunder consumes `TweetDeleteEvent` and removes it from its in-memory store — but grox has no delete consumer, delete topic, or tombstone handler anywhere. The deletion is honored at the user-visible surface but never routed to the derived embedding/summary store, even though propagation is architecturally possible (thunder already consumes the event).

**From *Magnifica Humanitas*:**

> §108 “the product of many contributors”
> — Data should be managed "as a common or shared good"; here the supervisory corpus and the derived representations of the user's content (and, via the embedding space, of the user) are captured and valued purely privately, and a deleted post's embedding/summary persists after the user has withdrawn it.

> §178 “transforming personal lives into exploitable information”
> — §178 names the digital-colonial appropriation of data.

**Violation:** This violates the universal destination of goods and human dignity. §67 includes "algorithms... and data" among goods universally destined for all and warns that concentration "without adequate forms of sharing and access" creates "a new imbalance." Per §104 the system optimizes for retained derived signal and ignores the contributor's withdrawal.

**Resembles:** technocratic-paradigm — users' behaviors are a free input stream optimized into engagement predictions, and their contributions are retained as model inputs after withdrawal; the collectively-generated corpus is captured privately with no recognition, sharing, or governance.

**Remediation:**
- Add a `TweetDeleteEvent` consumer in grox that deletes the post's row from the embedding/summary sinks and emits an embedding-tombstone so downstream consumers purge it; key derived artifacts by `post_id` and `author_id` so per-author erasure can fan out.
- Ship a data card disclosing that training labels are first-party user behaviors, which actions become supervision targets, and the continuous-training/retention regime.
- Give users a visible record of, and opt-out over, whether their engagement contributes to training; emit deletion-confirmation audit records so erasure is verifiable rather than assumed.

**Structural note:** A system whose competitive value is a continuously harvested behavioral corpus has structural incentives against recognizing, sharing, or governing that value — a business-model question, not a local fix. True downstream deletion from vector stores and compacted Kafka logs is operationally hard, requiring a deletion-fan-out architecture. This is a frozen open-source mini-checkpoint, but the README itself asserts the production regime this finding addresses.

---

### 06. Consequential automated judgments over content and persons are enacted with no author notification, no appeal, and no accountable owner in code — confidence 84

*Engages:* violates Subsidiarity, The dignity of the human person, Social justice

**Code evidence:**

```python
# Grok-as-judge PTOS enforcement (safety_ptos.py:232-262) applied automatically;
# the outcome recorded only as logger.info(...) plus metric counters before
# persisting to the safety store and Kafka (also task_grok_upa_action_with_labels.py:38-49)
# grep for appeal / recourse / notify / human-review / dispute / author: nothing
```
`Location: grox/tasks/task_write_safety_post_annotations_result_sink.py:210-237,330`

```python
banger_initial_positive = score >= 0.4  # a hard binary cutoff on a single learned "quality" score
```
`Location: grox/classifiers/content/banger_initial_screen.py:129`

```rust
Some(_) => true  // catch-all drop on any non-safety visibility reason;
// visibility_reason recorded only to operator telemetry
// mirrored at candidate_hydrators/vf_candidate_hydrator.rs:155-162
```
`Location: home-mixer/filters/vf_filter.rs:22-30`

**Behavior:** A Grok VLM (temperature ≈ 0) is the sole judge of a post's policy violations across the gravest categories — including SuicideOrSelfHarm, HateOrAbuse, ViolentMedia — and the result sink applies enforcement labels automatically, recording the outcome only as `logger.info(...)` plus metric counters before persisting to the safety store and Kafka. A separate Grok screen reduces each post to a single learned `quality_score` and applies a hard binary cutoff at 0.4. The visibility filter drops candidates via a catch-all `Some(_) => true` on any non-safety reason, recording `visibility_reason` only to operator telemetry. A grep across these paths for appeal / recourse / notify / human-review / dispute / author returns nothing: no recourse hook, no human-in-the-loop branch, no author notification, no accountable-owner field. (Accuracy controls — a tiered deluxe/4.2 stack, near-deterministic sampling, an independent safe-model cross-check before NSFW enforcement — reduce false positives but do not close the recourse gap.)

**From *Magnifica Humanitas*:**

> §71 “transparency regarding algorithms”
> — Required of de facto platform power, together with "avenues for recourse."

> §104 “without the possibility of appeal”
> — A system applying a consequential label this way has "already introduced criteria that contradict the inalienable dignity of the human person."

> §103 “the power to select who is worthy... without anyone bearing responsibility”
> — §103's warning, realized here as enforcement labels owned by no one.

> §102 “does not know compassion, mercy, forgiveness... the hope that people are able to change”
> — Yet the model adjudicates self-harm and hate content alone.

> §171 “the architecture of visibility — what is amplified or rendered invisible”
> — §171 names visibility suppression as exactly this architecture.

**Violation:** This violates subsidiarity, human dignity, and social justice. §105 requires a locatable answer to who must justify, monitor, challenge, and remedy — only logs and counters exist.

**Resembles:** technocratic-paradigm — content fate is decided by model output and enacted as a label; persons are reduced to inputs of an enforcement metric with no human answerable for the judgment.

**Remediation:**
- Add a human-reachable, time-bounded appeal step (ideally a human-in-the-loop checkpoint) before or after consequential label application — suppression, NSFW gating, spam.
- Persist a per-decision rationale and decision ID keyed to post/author, delivered to the affected author with the policy invoked (the `debug_string` already produced is logged, not delivered); enumerate each `FilteredReason` variant explicitly rather than collapsing into `Some(_) => true`, while keeping the fail-closed default for safety.
- Instrument appeal rate and overturn rate as first-class metrics; record an accountable owner (team/role) per enforcement-label type so the §105 locus is identifiable in code.

**Structural note:** Real recourse at this scale requires staffing human review and an organizational commitment to absorb the cost of overturning model decisions — it cuts against fully-automated moderation and likely also needs external regulatory pressure (DSA-style). The enforcement service and any appeal layer live in the out-of-tree `strato_http` service, so the absence is verifiable only as an in-code/opaque gap — which is itself the §71 transparency concern.

---

### 07. The viewer's age is fetched, then discarded – minor status never escalates the safety gate nor gates the engagement ranking — confidence 83

*Engages:* violates Social justice, Integral human development

**Code evidence:**

```rust
user_age_in_years: Option<i32>  // populated from Gizmoduck's viewer_data.age_in_years
// repo-wide grep: only the declaration and the single assignment — zero downstream reads;
// no minor flag is derived
```
`Location: home-mixer/server.rs:119 → models/query.rs:74,177`

```rust
// TwitterContextViewer built from user_id / country / language,
// then ..Default::default() — age is dropped
// SafetyLevel hard-coded to TimelineHome / TimelineHomeRecommendations,
// never escalated for minors (vf_candidate_hydrator.rs:49,76-90; vf_filter.rs:22-30 —
// the only organic safety gates: phoenix_candidate_pipeline.rs:318-319)
```
`Location: home-mixer/models/query.rs:214-224`

**Behavior:** The viewer's biological age is fetched and stored as `user_age_in_years: Option<i32>`, but a repo-wide grep finds only the declaration and the single assignment — zero downstream reads. No minor flag is derived. The `TwitterContextViewer` forwarded to visibility filtering carries only user_id, country, and language, then `..Default::default()` — age is dropped. The `SafetyLevel` sent to VF is hard-coded to `TimelineHome`/`TimelineHomeRecommendations`, never escalated for minors, and the engagement ranking branches on no recipient-age signal. The only "age" logic in the path keys on post recency or account-creation tenure, not the viewer's age. The same adult-tuned drop threshold and the same attention-maximizing feed reach a 12-year-old and an adult identically.

**From *Magnifica Humanitas*:**

> §141 “early and unsupervised exposure to digital devices and social media”
> — §141 warns this harms minors "during the most vulnerable stages of life, at times with tragic consequences."

> §142 “oppose the immediate interests of platforms when they conflict with the wellbeing of minors”
> — §142 requires policies that do exactly this, holding providers accountable "rather than shifting the burden to families."

> §80 “the youngest and weakest”
> — §80 names protecting them.

**Violation:** This violates social justice and integral human development. §104 is exact: age is measured, then ignored. The system holds the viewer's age yet never derives minor status, never forwards age or an escalated safety level to its one recipient-keyed chokepoint, and runs an age-blind engagement ranking.

**Resembles:** technocratic-paradigm — every viewer is reduced to the same engagement-optimization target; the one signal that would differentiate the vulnerable is collected as data but never permitted to change the system's behavior.

**Remediation:**
- Diagnostic first: confirm whether the external VF service already age-gates via the `for_user_id` it receives; if not, the gap is live and unmitigated.
- Thread the already-available `user_age_in_years` into the viewer context (alongside the country/language already passed) and request a stricter `SafetyLevel` for minors; where age is unknown, default to the stricter standard.
- Gate the engagement-amplifying ranking for minor viewers — disable or down-weight sensitive out-of-network recall and the dwell/not-dwelled signals — since content-dropping in VF does not address attention mechanics.
- Add metrics/alerts verifying minor-viewer requests actually take the protective path.

**Structural note:** A feed that does not maximize engagement for minors is less profitable, so the gap is unlikely to close from inside a ranking team optimizing engagement; §142 anticipates exactly this and holds that the wellbeing of minors must prevail. A minor-specific threshold also requires coordination with the external visibility-filtering service to accept a viewer-age dimension; whether a minor-aware field already exists downstream could not be confirmed from in-repo source.

---

### 08. The ranking and classification logic that governs people is not transparent to them: no in-product explanation, no off-switch or chronological alternative, and the operative policy prompts and weights are withheld from the "open" release — confidence 80

*Engages:* violates Subsidiarity

**Code evidence:**

```rust
// a named WeightedScorer combines per-action probabilities via named weight
// constants — only the action NAMES ship (README.md:53,265-292,324-325);
// the numeric weight values and the embeddings-to-logits map are not inspectable
// repo-wide grep: chronological / disable-ranking / explain / opt-out / user-control — zero hits
```
`Location: home-mixer/scorers/weighted_scorer.rs:44-91`

```python
# every grox classifier renders its operative criteria from grox.prompts.template —
# a module absent from the checkout (also spam.py:10,49; banger_initial_screen.py:13,63;
# reply_ranking.py:13,55; post_safety_screen_deluxe.py:14,50)
# .gitignore excludes only __pycache__/ — this is not a gitignore artifact
```
`Location: grox/classifiers/content/safety_ptos.py:15-24,80,166-185`

**Behavior:** Ranking is legible to engineers reading GitHub — a Grok transformer predicts per-action probabilities, then a named `WeightedScorer` combines them via named weight constants. But a repo-wide grep for chronological / disable-ranking / explain / opt-out / user-control returns zero hits: nothing is surfaced to the person whose feed it is — no off-switch, no chronological alternative, no per-post "why am I seeing this," no recourse. The numeric weight values (only the action names ship) and the embeddings-to-logits map are not inspectable. Separately, every grox classifier renders its operative criteria from a `grox.prompts.template` module that is absent from the release: the rendered prompt text is the policy — what counts as a violation, spam, low quality, or a high-quality post worth amplifying — and it is withheld, so the "open" classifiers cannot be independently checked. The README frames this as having "eliminated every single hand-engineered feature."

**From *Magnifica Humanitas*:**

> §71 “transparency regarding algorithms... and avenues for recourse”
> — §71 names major platforms as the new "highest level" defining "rules of visibility" — and owes users both.

> §70 “people being presented with decisions that have already been taken”
> — §70 forbids this — the feed offers no off-switch or chronological alternative.

> §102 “present[ing] itself as neutral and objective”
> — An algorithm doing so reflects "the bias of its designers."

> §72 “we cannot allow a handful of actors to dictate these processes on their own”

**Violation:** This violates subsidiarity and the non-neutrality of design. §104: "eliminated every hand-engineered feature" does not remove choices, it relocates them into learned weights and unpublished numeric values that cannot be inspected; the operative classification criteria live in the absent prompts. §105 grounds the contestability gap. The defect is sharpest for the quality/amplification criteria (`BangerMiniVlmScreenScore`, `ReplyScoringSystem`), where the abuse-resistance argument for secrecy is thin.

**Resembles:** technocratic-paradigm — transparency is performed at the harness layer while the substantive judgment criteria that classify persons and rank speech remain private and non-auditable, and the legible-to-engineers account is never translated for the person it governs.

**Remediation:**
- Surface the existing account in-product: a plain-language "why am I seeing this" per post derived from the dominant predicted actions and weights; publish the numeric weight values (only action names ship today).
- Add user-facing structural controls: turn ML ranking off, see a chronological feed, exclude content categories, and a recourse path for misranking.
- For the quality/amplification classifiers, publish the operative rubric or a faithful detailed summary; for safety/spam, publish a per-category policy taxonomy with thresholds and intended outcomes (verbatim prompts may be withheld to resist evasion), versioned and changelogged.
- Stand up a researcher-access program for independent checks; if criteria stay private, state in the README which components are and are not auditable so "open" is not overclaimed.

**Structural note:** Two layers stay opaque for different reasons: the transformer's embeddings-to-logits map is intrinsically hard to explain (genuine transparency needs a surrogate/attribution layer — a non-local architectural commitment), while the missing user-facing surfacing, off-switch, chronological mode, and recourse are product/business-model choices, independently fixable. If "quality" is in fact a proxy for predicted engagement, publishing the rubric forgoes strategic opacity the business model benefits from.

---

### 09. Fully automated moderation of disturbing content discloses nothing about the human-labeled examples it depends on — confidence 84

*Engages:* strains Solidarity, Social justice

**Code evidence:**

```python
# policy prompts and categories: a Grok vision/reasoning model classifies posts
# against ViolentMedia, AdultContent, HateOrAbuse, ViolentSpeech,
# SuicideOrSelfHarm, and IllegalAndRegulatedBehaviors prompts
# repo-wide: no model card, data card, or annotation-labor provenance
```
`Location: grox/classifiers/content/safety_ptos.py:166-185,217-225`

```python
# label application — derived isGore, hard/soft sexual
```
`Location: grox/tasks/task_write_safety_post_annotations_result_sink.py:67-93`

**Behavior:** A Grok vision/reasoning model classifies posts against ViolentMedia, AdultContent, HateOrAbuse, ViolentSpeech, SuicideOrSelfHarm, and IllegalAndRegulatedBehaviors prompts, emitting labels including a derived `isGore`. Classification is fully model-driven, and the repository contains no model card, data card, or training/eval provenance for these classifiers.

**From *Magnifica Humanitas*:**

> §173 “data labeling, model training and content moderation, often involving disturbing material”
> — §173 names this hidden labor, performed by "young people, predominantly women... for minimal wages."

> §109 “must shape [technologies'] very design from the outset”
> — §109 holds this of social justice — a condition of design, not a post-deployment safeguard.

> §111 “toward affected communities”
> — §111 places responsibility on developers — here, toward the unseen annotators.

**Violation:** This engages solidarity and social justice. Automating gore/self-harm/abuse triage with a model can be a genuine good that spares frontline reviewers — itself aligned with §173's concern. The bug is narrower: a learned safety classifier necessarily rests on upstream human-labeled examples of exactly this disturbing material, and the code documents neither the provenance of those examples nor the labelers' conditions or support. §179 requires supply-chain due diligence over precisely this dependency.

**Resembles:** technocratic-paradigm — the disturbing-content review the classifier depends on is abstracted into a model-driven classification problem, the human labelers behind the training data rendered invisible.

**Remediation:**
- Publish a model/data card for each safety classifier documenting the source of its labeled examples, the labor conditions of the annotators, and any trauma-informed support provided.
- Apply ethical due-diligence and disclosure to the annotation/moderation vendors (§179); retain a directly-employed, supported human-in-the-loop audit path for the highest-severity categories rather than full automation as the only check.
- Track and report the proportion of high-severity decisions made with no human review as a governance metric.

**Structural note:** Whether the upstream labeling labor is in fact exploitative is not visible in this code; the finding flags that the dependency exists and is wholly undocumented, not that exploitation is proven. Confirming or curing it requires supply-chain disclosure — an organizational act, not a code change.

---

### 10. Device advertising identifier and device/IP fingerprints are sent to ad selection with no per-ad targeting rationale carried back to the user — confidence 80

*Engages:* strains Social justice

**Code evidence:**

```rust
// build_ad_index_request packs ip_address, user_agent, user_roles, device_id,
// mobile_device_id, and mobile_device_ad_id (the OS advertising identifier),
// plus country/language, into a ClientContext sent to get_eligible_ads;
// returned ads are interleaved at position 0 (promoted: true; EntryType::PROMOTED_TWEET)
```
`Location: home-mixer/sources/ads_source.rs:41-60`

```rust
// each served ad logged server-side with impression_id, advertiser_id, position —
// but the only fields carried back to the surface are insert_position and the
// impression/advertiser IDs (served_candidates_kafka_side_effect.rs:142-159)
// grep for rationale / why_this / explanation / targeting_reason: zero hits
```
`Location: home-mixer/side_effects/ads_injection_logging_side_effect.rs:106-115`

**Behavior:** `build_ad_index_request` packs `ip_address`, `user_agent`, `user_roles`, `device_id`, `mobile_device_id`, and `mobile_device_ad_id` (the OS advertising identifier), plus country/language, into a `ClientContext` sent to `get_eligible_ads`; returned ads are interleaved at position 0. Ads are labeled as ads (`promoted: true`; `EntryType::PROMOTED_TWEET`) and each served ad is logged server-side with `impression_id`, `advertiser_id`, and position. But the only fields carried back to the surface are `insert_position` and the impression/advertiser IDs — no field conveys why a given ad was matched to this user. A grep for rationale / why_this / explanation / targeting_reason returns zero hits.

**From *Magnifica Humanitas*:**

> §171 “to profile, predict and influence behavior, often without individuals being fully aware of it”
> — §171 (primary) names this emergent power; forwarding the OS advertising identifier plus device/IP fingerprints to ad selection is behavioral targeting whose rationale is opaque to the user — the surface can say "this is an ad" but never "why THIS ad to YOU."

> §170 “thrive on human weakness... those who design or finance such systems bear a moral responsibility”
> — §170 grounds the moral responsibility when business models do so.

**Violation:** This engages the attention-economy/profiling power and social justice. §80 applies on its "invasive surveillance" and "public oversight" clauses, with "the dignity of every person" as guiding principle rather than profit; the gap is user-legible oversight and recourse, not absent server-side logging (which exists).

**Resembles:** technocratic-paradigm — the person's device and identity signals are inputs optimized for ad match, with the matching rationale withheld from the person it describes.

**Remediation:**
- Plumb a targeting-rationale field alongside each `AdIndexInfo` so the client can render a "why am I seeing this ad" disclosure listing the signal categories used.
- Default to contextual signals (country/language/current-surface) and gate transmission of `ip_address` and `device_id`/`mobile_device_id` behavioral fingerprints behind an explicit advertising-personalization opt-in. (`mobile_device_ad_id` is the OS advertising identifier, already zeroed by iOS ATT / Android consent unless the user opted in at the OS layer, so the in-app gate matters most for the non-OS-gated fingerprints.)
- Surface a user-facing recourse path (opt out of personalization, report an ad) alongside the existing "Promoted" label.

**Structural note:** Behavioral ad targeting via the advertising identifier and device/IP fingerprints is the revenue mechanism; constraining it to contextual-by-default trades measurable ad performance for user inner-freedom — a business-model tradeoff §170 places on those who design or finance the system, not on the engineer who plumbs the request.

---

## What the system does well

- **Author-diversity attenuation** (The common good) — the `AuthorDiversityScorer` attenuates repeated-author scores (`ranking_scorer.rs:186-217`), a genuine diversity mitigation
- **Listens to explicit aversion** (The dignity of the human person) — the objective carries negative weights for block, mute, report, and not-interested — the system listens to explicit aversion, not only engagement
- **Mandatory per-recipient safety filter** (Social justice) — a mandatory, platform-side, per-recipient visibility filter (`vf_candidate_hydrator.rs` → `vf_filter.rs`) runs before brand-safety and irrespective of user opt-in, so harm avoidance is not offloaded to opt-in muting
- **Deletion honored in-network** (The universal destination of goods) — `thunder` honors post deletion in its in-network store (`post_store.rs:69,279`)
- **Documents its own mechanics with unusual candor** (Subsidiarity) — the README documents the ranking mechanics with unusual candor — these are the materials from which a more humane system could be built

---

## Dropped and consolidated

- **Spam scrutiny "polices the small and shields the prominent" — the follower-count buckets key on the replied-to audience, not the replier's own following, so high-follower spammers are fully in scope** — conf — — refuted
- **Brand safety protects advertisers but not viewers — the per-viewer VF hard-drop path runs first** — conf — — refuted
- **Thunder deletion is "theatrical" / resurrectable — the retention filter drops stale replayed creates before the tombstone is consulted, and thunder is a recent-only serving cache, not the system of record** — conf — — refuted
- **Reply-ranking favoring account size, Grok-inferred topics driving new-user feeds, and a new-user OON weight "overriding follow choices"** — conf — — refuted or unsupported by the visible code
- **A mutual-follow minhash "profiling" finding — the minhash is a privacy-preserving sketch derived from an overt follow action** — conf — — downgraded
- **Energy/water/carbon accounting — true, but an ML code release is not where kWh counters belong, and verified cost controls (`max_qps`, TTL dedup, `max_audio_duration_s`, min-traction gating) bound the magnitude** — conf 65 — wrong artifact

---

## Limits of this audit

- Several decisive consumers are referenced but not vendored: `util::phoenix_request::build_prediction_request` (whether inferred gender materially changes ranking), the external visibility-filtering service (whether it independently age-gates via `for_user_id`), and the served-history/safety storage clients (whether a data-subject deletion path exists out-of-tree).
- Where a finding depends on these, the confidence and language reflect the in-code/opaque boundary — which is itself, per §71, part of the transparency concern.
- Model weights (LFS) were not analyzed.

---

## Methodology note

This audit was conducted using the [Magnificent Humanity Audit](https://github.com/Cache-Atelier/magnificent-humanity-audit/releases/latest) agent skill made by [Cache Atelier](https://cacheatelier.work), applying the seven principles of Catholic Social Doctrine as articulated in Pope Leo XIV's encyclical *Magnifica Humanitas* (15 May 2026). Findings are reported only at confidence ≥80. The encyclical is at https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html.
