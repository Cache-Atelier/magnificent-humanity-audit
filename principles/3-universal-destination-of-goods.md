# Principle 3: The Universal Destination of Goods

> "Among the goods that are universally intended for everyone, we must also include new forms of property, such as patents, algorithms, digital platforms, technological infrastructure and data." — *Magnifica Humanitas* §67

## What the encyclical teaches

The universal destination of goods is the principle that **the earth's goods — and now also patents, algorithms, digital platforms, technological infrastructure, and data — are given by God to the entire human family** (§65–67). Every person has an inherent right to the use of such goods, both now and in the future. The principle predates the digital age but is given a new and decisive application in *Magnifica Humanitas*.

The encyclical's foundation: "God gave the earth to the whole human race for the sustenance of all its members, without excluding or favoring anyone" (§65). "It is not in accordance with God's plan to use this gift in such a way that its benefits accrue solely to a select few."

In §66, the encyclical names a doctrine the agent must hold operationally: **private property is subordinate to the universal destination of goods**. This is not "a mere theological opinion, but a doctrine of the Church." "The Christian tradition has never recognized the right to private property as absolute or inviolable." Per John Paul II, this subordination is "the golden rule of social conduct and the first principle of the whole ethical and social order."

In §67, the encyclical extends the principle explicitly to the digital age. Algorithms, platforms, infrastructure, and especially **data** belong to the family of goods that are universally intended for the human family. When these are concentrated in the hands of a few, "a new imbalance is created that contradicts the universal destination of goods. In turn, it widens the gap between the included and the excluded."

In §108 the encyclical is even sharper: **"Ownership of data cannot be left solely in private hands but must be appropriately regulated. Data is the product of many contributors and should not be treated as something to be sold off or entrusted to a select few. It is necessary to think creatively in order to manage data as a common or shared good."**

This principle is operationally distinctive. It is the encyclical's strongest direct claim against the concentration of digital wealth and capacity in major platforms. An audit grounded in this principle will often find that the most central pattern of a modern platform — collect data from users, treat it as a private asset, sell or use it to advantage — is in direct contradiction to the magisterial position.

## What honoring this principle looks like in software

A system that honors the universal destination of goods:

- Treats data the user generates as belonging in significant part to the user, not to the platform
- Provides genuine data export — complete, in a usable format, with the data that matters, not just the data that is convenient
- Provides data deletion that actually deletes — across backups, derivative models, analytics warehouses, third-party processors
- Treats the platform's reach and visibility as a common good to be distributed fairly, not a private good to be sold to the highest bidder
- Does not extract from users disproportionately to what it returns
- Makes core capabilities (search, communication, basic services) accessible regardless of payment
- Where the system uses user data to train models, does so transparently and shares the resulting benefit
- Maintains interoperability — the user can leave and bring their data with them
- Considers the impact of resource use (energy, water, rare earths) on those distant from the system's beneficiaries

## What violating this principle looks like

A system that violates the universal destination of goods:

- Treats user-generated data as a wholly-owned private asset
- Sells, licenses, or monetizes user data in ways the user did not knowingly consent to and cannot revoke
- Trains models on user data and treats the resulting model as private property, with no return to the contributors
- Provides "data export" that is incomplete, partial, or in formats that are not portable
- Provides "data deletion" that is theatrical — the user-visible record disappears but derivative data, model weights, and warehoused analytics remain
- Engineers lock-in: APIs designed to be one-way, formats designed not to migrate, social graphs that cannot be exported
- Concentrates reach and visibility in ways that the platform monetizes (paid promotion as the primary distribution mechanism)
- Uses computational and resource infrastructure that disproportionately externalizes costs to populations that do not benefit (§101 on environmental impact)
- Treats the public's data and attention as private inputs to private profit

The encyclical names the structural pattern in §178: digital colonialism. "Colonialism assumes new forms. It no longer dominates only bodies, but appropriates data, transforming personal lives into exploitable information. Entire regions, especially those marked by structural fragility and limited geopolitical relevance, are currently subjected to a new mindset of extraction." When user data, especially from less protected populations, is extracted asymmetrically, the violation is acute.

## Code-level signatures

Where to look in a codebase for evidence on this principle:

- **Terms of service and privacy policy.** Read them. What does the platform claim ownership over? What does it license to itself? What does it claim the right to use for model training?
- **Data export endpoints.** Does an export endpoint exist? What does it include? Run a test export and compare to what the user has put in. Look for: missing data types, formats that are not standard, broken references, missing metadata.
- **Data deletion endpoints.** Does deletion propagate to backups, replicas, derived analytics, ML training sets? Look in the deletion code for what it touches and what it does not.
- **Model training data sources.** Where does training data come from? Is user data included? Is consent explicit or buried in terms? Is there an opt-out, and is it default-on or default-off?
- **API design.** Is the API read/write or read-only for the user's own data? Can a third-party tool (with the user's permission) access the user's full data? Or only what the platform chooses to expose?
- **Storage layer.** Where is user data stored? In what regions? Under whose jurisdiction? Who has access for what purposes?
- **Resource consumption.** What is the energy, water, and infrastructure footprint? Who bears the cost?

## Common remediations

When the audit identifies a violation of the universal destination of goods:

- **Implement complete, standard-format data export.** A user must be able to retrieve all their data — including derived data, social graph, content, history — in a format that lets them move to another service. Half-exports do not satisfy the principle.
- **Implement actual deletion.** "Delete" must propagate through backups, derived analytics, embeddings, training sets, and third-party processors. Document where this is not yet implemented; treat each gap as a finding.
- **Default model training to opt-in.** Per §108, data is the product of many contributors. The default should be that user data is not used for model training without explicit, granular consent. Opt-out buried in settings does not constitute consent.
- **Open the API.** A third-party tool authorized by the user should be able to access the user's data with the same fidelity as the platform's own clients. Hidden APIs, undocumented rate limits, and selective access break the universal destination of goods.
- **Support interoperability protocols.** Adopt and implement existing portability standards. Resist the temptation to invent a non-standard format that prevents migration.
- **Consider the resource footprint.** Per §101, AI systems consume significant resources, often distant from the beneficiaries. Document the system's energy and water footprint; consider what is owed to those whose environments bear the cost.
- **Where data is monetized, share returns.** If a platform's value depends on aggregated user data, the question of whether contributors share in that value is real. Per §108, "manage data as a common or shared good."

When the issue is non-local — when the entire business model is predicated on owning what the encyclical says belongs to all — the structural note is unavoidable: the audit finding will require revisiting the business model itself.

## Typical diagnostic labels

Violations of the universal destination of goods most often manifest as **technocratic-paradigm** — the logic of extraction and accumulation treated as the system's natural state. When the specific pattern is the concentration of platform capacity in a few entities that have effectively monopolized the digital common, this also engages subsidiarity (Principle 4). When the data extraction patterns parallel historical colonial patterns — extracting from the periphery to the metropole — the diagnostic of digital colonialism from §178 applies.

## Connections to other principles

This principle is closely linked to subsidiarity (§4): when platforms become the "highest level" exercising de facto power over the conditions of everyday life, the subordination of property to the universal destination of goods is what gives subsidiarity its bite. It is also tightly connected to solidarity (§5): per §76, the digital ecosystem can be "preserved or exploited, shared or monopolized." Solidarity demands the former; the universal destination of goods names the rule by which we discern which it is.

## Key encyclical paragraphs to cite

- **§65** for the foundational claim
- **§66** for the subordination of private property
- **§67** for the explicit extension to data, algorithms, and platforms — **the most-cited paragraph for digital-age applications**
- **§108** for data ownership specifically as a common good
- **§178** when digital colonialism is the specific pattern
