# Locus 2: Consent, Data Ownership, and Deletion

> "Ownership of data cannot be left solely in private hands but must be appropriately regulated. Data is the product of many contributors and should not be treated as something to be sold off or entrusted to a select few." — *Magnifica Humanitas* §108

## What this locus covers

The lifecycle of the user's data and the rights the user retains over it. This includes:

- The legal and operational basis on which data is collected
- The granularity and revocability of consent
- The user's ability to access their own data (read)
- The user's ability to export their own data (portability)
- The user's ability to delete their data (deletion, including downstream)
- The treatment of derived data (analytics, embeddings, model weights)
- The user's ability to revoke prior consent and have downstream consequences honored
- Data sharing with third parties

This locus tests the encyclical's strongest direct claim about the digital age: that data belongs to the universal destination of goods (§67), that ownership cannot be left solely in private hands (§108), and that platforms which treat user data as a private asset are in direct contradiction with the principle.

## Principles most engaged

- **Universal destination of goods** (Principle 3): the foundational principle for this locus. Per §67, data is among the goods of common destination; per §108, data is the product of many contributors.
- **Human dignity** (Principle 1): the user's right to their own data, history, and presence; the right to leave with what they brought.
- **Subsidiarity** (Principle 4): the right to decide about one's own data is the right that subsidiarity protects at the closest level — the user themselves.
- **Solidarity** (Principle 5): the user who wants to leave should not lose the bonds they have built.

## What to look for

### The consent mechanism

- Is consent specific or bundled? Per §70, bundled consent is decision already taken.
- Is consent revocable? What happens downstream when revoked?
- What kinds of data are collected under what consent basis?
- Is consent granular by purpose (functioning, analytics, personalization, AI training, marketing)?
- Can the user withdraw consent for one purpose while keeping consent for another?
- Is the consent flow accessible — to non-native speakers, to users with disabilities, to children's parents?

### Data export

- Does an export function exist?
- What does it include? Compare to what the user has put in. Test exports systematically.
  - Posts, messages, photos, files
  - Connections and social graph
  - Activity history
  - Inferred attributes, scores, segments (often missing)
  - Model training contributions
  - Metadata, timestamps, edit history
- Is the format standard or proprietary?
- Is the format usable — can the user actually open and migrate it?
- How long does export take? Hours? Days? Weeks? Is there a deadline before the export expires?
- Is there a rate limit on how often export is allowed?

A "data export" that excludes derived data, social graph, history, or metadata is a partial export. Per §108, "data is the product of many contributors" — the user's data is what they contributed; the system's derivations from that data still belong in significant part to the contributors.

### Data deletion

- Does a deletion function exist?
- What does it actually delete?
- Does deletion propagate to:
  - Production databases
  - Replicas and backups
  - Analytics data warehouses
  - Derived ML training sets
  - Vector embeddings
  - Model weights (notoriously hard, but ask)
  - Third-party processors and shared platforms
  - Marketing systems
  - Search indexes
- Is there a deletion confirmation that tells the user what was actually deleted?
- Is there a delay before deletion completes? What is the delay's purpose?
- What about data the system claims to anonymize or aggregate — is it actually unlinkable, or theoretically re-identifiable?

A deletion that does not propagate is a theatrical deletion. The user-visible record disappears; the system's actual possession of the data does not.

### Data sharing

- What third parties receive what data, under what basis?
- Are these documented? In the privacy policy? In code?
- Is the user notified when a new third party is added?
- Can the user revoke sharing with specific third parties?
- Are sub-processors named, or hidden behind "trusted partners"?

### Account closure

- Can the user actually close their account?
- What is required to close it?
- Is the closure path symmetric with the opening path, or is it harder?
- After closure, what happens to data? What persists, and for how long?

## Common findings

Patterns that often surface in this locus:

- **Theatrical deletion.** Deletion removes the user-visible record but leaves derived analytics, model training contributions, and warehoused data intact.
- **Partial export.** Export gives the user back their content but not their social graph, history, scores, or inferred attributes. The platform retains the parts that matter most for migration.
- **Format lock-in.** Export is in a format that no other platform reads. Migration is theoretically possible but practically blocked.
- **Bundled consent that cannot be unbundled.** The user accepts everything at signup or uses nothing. Revocation of any single consent is treated as account closure.
- **Buried opt-outs.** Consents are simple at signup; the opt-out is deep in settings. Search the codebase: which is more thoroughly built?
- **Sub-processors hidden.** The list of third parties receiving user data is not enumerated or kept current.
- **Account closure friction.** Closure requires extra confirmation, phone verification, support contact, or a cooling-off period that signup did not require.
- **Derived data treated as the platform's.** Embeddings, recommendations, social graph derivatives, scores — the platform claims these as its own assets even though they describe and depend on the user.

## How to gather evidence

When source code is available:
- Search for `gdpr`, `ccpa`, `consent`, `delete`, `export`, `download_data`, `data_subject_request`
- Read the deletion code path. What tables does it touch? What does it not touch?
- Read the export code path. What is included? What is omitted? Are there comments about what was excluded and why?
- Search for `anonymize`, `pseudonymize`, `aggregate` — and verify that the anonymization is real
- Read the third-party processor list; compare to what is in code
- Read the consent withdrawal handler. Does it propagate?

When only product access is available:
- Initiate a data export. Document what is included.
- Compare to what the user has actually contributed (timeline, friends, photos, settings)
- Attempt deletion. Note delays, confirmations, what is preserved
- Test withdrawal of specific consents
- Read the privacy policy and the sub-processor list
- Try to close the account fully; document friction

## Remediation patterns

- **Specific, revocable, granular consent.** Each category of data use is separately consented; each consent is revocable; revocation propagates downstream.
- **Complete, standard-format export.** Everything the user has contributed, including derived data describing them, in a portable standard format.
- **Real deletion.** Deletion propagates through production, replicas, backups, analytics, derived data, and training sets. Each gap is documented.
- **Transparent sub-processor list.** Maintained, dated, accessible. Notification when changed.
- **Symmetric account closure.** Closing an account is no harder than opening it.
- **Honor revocation downstream.** When a user revokes consent for AI training, derived models are flagged. Where retraining is practical, the user's contributions are removed.

Per §108: "Manage data as a common or shared good." Where the platform's economics depend on hoarding user data, the remediation requires structural change — but the audit names what is, even when what is requires structural change to fix.
