# Locus 9: Supply Chain, Labor, and Ecological Cost

> "A significant part of the digital economy's functioning relies on the silent work of millions of people engaged in essential yet largely unseen activities, such as data labeling, model training and content moderation, often involving disturbing material. In many cases, these workers are young people, predominantly women, working under demanding conditions for minimal wages." — *Magnifica Humanitas* §173

## What this locus covers

The costs of operating the system that are not visible to its users. This includes:

- The labor of data labelers, annotators, content moderators, and AI trainers
- The labor and conditions of workers extracting minerals used in devices and infrastructure
- The energy consumption of model training and inference
- The water consumption of data centers
- The carbon footprint of operation
- The treatment of workers within the system's own organization
- The treatment of workers using the system (gig workers, employees of customer firms, etc.)
- Supply-chain transparency and accountability
- The disposal and end-of-life of devices and infrastructure

The encyclical introduces this locus directly in §173 — naming as a defining feature of the digital economy the "silent work of millions of people" whose labor sustains the system but who are invisible to its users. The audit is among the first formal artifacts to read this locus as the encyclical does: not as externalities, but as integral to the moral assessment of the system.

## Principles most engaged

- **Solidarity** (Principle 5): the foundational principle. Per §73, "no one is saved alone." A system whose operation depends on hidden suffering is not in solidarity with those who suffer.
- **Social justice** (Principle 6): per §80, social-justice considerations cannot be bracketed by geography or invisibility.
- **Universal destination of goods** (Principle 3): per §66, the goods of creation are for the entire human family; extraction that benefits a few at others' cost violates the principle.
- **Human dignity** (Principle 1): per §148–150, the dignity of work is foundational; conditions that deskill, exploit, or endanger workers violate dignity directly.

## What to look for

### Data labelers and content moderators

The first concrete site of hidden labor in AI:

- Where is the system's labeled training data sourced from?
- Who labels it? Under what conditions? At what wages?
- Are content moderators exposed to traumatic material? With what support?
- Is the labor outsourced through contractors that obscure responsibility?
- Per §173, "these workers are young people, predominantly women, working under demanding conditions for minimal wages." The audit reads for whether the system's documentation acknowledges this.
- Is there a documented commitment to ethical labor in the AI training pipeline?

### Mineral and material extraction

- What materials does the hardware require?
- Where are they sourced from?
- Are there documented conflict minerals (per established conflict-mineral law)?
- Per §173, "in some regions of the world, children and adolescents work in dangerous conditions, crushing the materials from which rare earth elements are extracted."
- Are supply-chain audits conducted? Published?
- Are there commitments to responsible sourcing? Verified by independent third parties?

### Energy and water

Per §101, "current AI systems require enormous amounts of energy and water, significantly influencing carbon dioxide emissions, and place heavy demands on natural resources."

- What is the system's electricity consumption? At what carbon intensity?
- What is the water consumption of training and inference data centers?
- Where are data centers located? Are they in regions of water stress?
- Are renewable energy commitments real (additional renewable generation) or accounting fictions (renewable energy certificates on the existing grid)?
- Is there public reporting of resource consumption?
- Per §85, integral human development requires respect for "our common home and future generations" — energy and water use are part of this.

### Workers within the organization

- How are the platform's own engineers, contractors, customer support staff treated?
- Are content moderators within the company treated like core staff or like outsourced labor?
- Is there a documented commitment to fair labor practices?
- Are there documented patterns of worker complaint, organizing, retaliation?

### Workers using the system

- If the system is used by gig workers (delivery, ride-share, freelance task platforms), what are the conditions?
- Per §150, "AI promises to boost productivity by taking over mundane tasks" — but does it in fact deskill, surveil, and erode worker agency?
- Are workers compensated for the data they produce?
- Is algorithmic management transparent? Contestable?
- Can workers organize? Communicate with each other?
- Is there a path of recourse for unfair algorithmic decisions about a worker's livelihood?

### End-of-life

- What happens to devices and infrastructure at end of life?
- Is e-waste handled responsibly?
- Are old models, datasets, and infrastructure retired with environmental care?
- Is there a documented commitment to circular materials?

## Common findings

- **Outsourced moderation with poor support.** Content moderators reviewing traumatic material for low wages, often via contractors. Mental health support inadequate. Per §173 named directly.
- **Conflict-mineral exposure unaudited.** Hardware supply chain has known conflict-mineral exposure; no published audit.
- **Energy claims that don't add up.** Net-zero claims based on offset accounting, not additional renewable generation. Real grid mix is fossil-heavy.
- **Water consumption hidden.** Data center water consumption not reported. Located in water-stressed regions without local consultation.
- **Gig-worker algorithmic management without recourse.** Workers managed by algorithm with opaque pay calculations, opaque suspensions, opaque "quality" scores. No appeal path that reaches a human.
- **Worker surveillance treated as feature.** Employee monitoring tools that surveil keystrokes, attention, screen content sold as "productivity" features.
- **Supply chain treated as out of scope.** The system's documentation treats labor and materials as not the company's concern — handled by suppliers, suppliers' suppliers, distant from "the product."
- **Resource costs externalized.** The environmental cost of training and inference is borne by populations the system does not serve.

## How to gather evidence

When source code is available:
- Supply-chain questions are rarely answered in code. They are answered in documentation, public reporting, sustainability reports, and investigative journalism.
- Read the system's public sustainability and labor reports
- Identify the contractors and suppliers; research their conditions
- Read the energy procurement strategy

When only product access is available:
- Read sustainability reports, ESG disclosures, public commitments
- Read investigative journalism about the company's supply chain
- Read worker testimony, organizing statements, regulatory filings
- Read academic research on the system's environmental and labor footprint
- Compare claims to verifiable third-party assessment

This locus often has less code-level evidence than others. Findings here lean on documented organizational behavior rather than file:line citations. That is fine — the encyclical's framing in §173 is precisely about labor and ecology *as the system's reality*, regardless of where in the code that reality is encoded.

## Remediation patterns

- **Audit labor in the AI training pipeline.** Identify labelers and moderators. Document wages, conditions, mental health support. Publish.
- **Direct employment of moderators.** Where content moderation involves traumatic material, the company employs moderators directly, with full benefits and trauma-informed support, rather than outsourcing to contractors.
- **Supply-chain audit with independent verification.** Conflict minerals, working conditions, child-labor exposure. Audited by independent third parties. Published.
- **Real renewable-energy procurement.** Power-purchase agreements that create additional renewable generation, not offsets. Reported transparently.
- **Water disclosure.** Data center water consumption reported by site. Withdrawal from water-stressed basins addressed.
- **Algorithmic management with recourse.** Where the system manages gig workers, decisions are transparent, contestable, and have human-reachable appeal paths.
- **Worker organizing protected.** Workers (in the company and on the platform) can communicate, organize, and raise concerns without retaliation.
- **End-of-life responsibility.** Hardware take-back, responsible recycling, model retirement that does not orphan deployed systems without support.
- **Per §111, developers' "particular ethical and spiritual responsibility."** The audit notes that developers themselves bear responsibility for design choices that depend on hidden labor; the responsibility cannot be fully delegated to procurement or sustainability functions.

This locus often has the longest path to remediation, because the supply chain reaches deep into geopolitics, mining, and global labor markets. The audit names what is, even where what is requires systemic change to fix. Per §174, "in continuity with the tradition inaugurated by Leo XIII, the Church renews her firm condemnation of all forms of slavery, trafficking and the commodification of persons." The audit reads digital supply chains in this lineage.
