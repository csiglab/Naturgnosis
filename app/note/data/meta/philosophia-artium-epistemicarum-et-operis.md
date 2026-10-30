---
tags: [epistemology, ontology, method]
---

# Philosophia Artium Epistemicarum et Operis

> Reality is the total set of phenomena, entities, and processes that exist or occur, independently of an observer’s perception or conceptualization, and which can, in principle, interact, change, or produce effects.

> Philosophia Artium Epistemicarum is the scaffolding used to parse, and render intelligible, reality.

> This note is a guide connecting Reality (Nature) with its Representation — modeling, computation, formal systems, algorithms, observers, and representations. It is the complement of Philosophia Artium Technicarum et Operis: where that note systematizes intervention in reality, this one systematizes how reality becomes intelligible.

## Formulation

### What is the nature of epistemic practice?

> Epistemology: (Reality; Ontology) → Description & Validation.

> An epistemic activity is any operation performed by an observer to construct, transform, evaluate, or apply knowledge about reality.

> The goal of epistemology is (1) to construct and maintain the scaffolding mechanisms of inquiry, and (2) to construct, validate, and derive the set of constructions about a domain — the Domain Epistemic Construction Set (DCESA) — that represents reality.

### What is the role of the `episteme` in human experience?

> The episteme renders reality intelligible: it compresses observations into descriptions that explain, predict, and enable intervention — and it disciplines thinking through formal artifacts rather than mental representations alone.

> Humanity identifies aspects of reality worth describing by discovering recurring patterns that enable explanation, prediction, intervention, or compression of experience. A worthy aspect compresses observations of reality by minimizing description length while maximizing our ability to intervene.

### What ground 'epistemic practice'?

> Epistemic practice is grounded in an observer-independent reality accessed through observation and inference.

> **Ontology and epistemology are the right hand and left hand of knowledge construction: they are mutually constraining duals of the same epistemic act.**
>
> - **Ontology** = what *is* (constraint space of reality)
> - **Epistemology** = how it is *accessed/represented* (constraint space of knowing)
> - They are not separate domains, but **co-dependent operators on the same reality-model interface.**

### What is the reality we seek to represent?

> Observer-independent reality: it exists whether perceived or modeled; it is composed of entities and processes with causal effects; it is dynamic and interconnected, producing emergent patterns; and it is accessible — imperfectly — through observation and inference constrained by what actually exists.

> Reality is decomposed for inquiry in the Ontic Order tree below.

### At which level of organization do we inquire?

> The hierarchical stratification of structural and functional components, from microscopic interactions to emergent macroscopic behaviors — crucial when modeling systems with multiscale dynamics, memory, or adaptive laws.

- **Micro-level:** Individual elements and their local interactions.
- **Meso-level:** Subsystems, modules, clusters of interactions.
- **Macro-level:** Emergent patterns, global behavior, systemic properties.
- Systems thinking is **hierarchical**: different questions require different levels of analysis.

### What is the ontology of the target?

> What is reality like? Which elements make it up? How do we identify them? How do we think deeply about change — and about change as an element of reality itself? Ontology answers by constraining what can be known; its constructs for parsing (segments, entities, processes, phenomena) live in the Artifact tree below, and its full template in the Ontic Order branch of the table.

### What Is a `Epistemic Element`?

> An Epistemic Element is anything that occupies a role in the practice by which reality is made intelligible: the reality cut as a target; the practice that investigates it; the constructions it produces; or anything that enables, constrains, evaluates, communicates, or conditions that practice.

> Its boundaries are broad by design — a domain, a task, a notation, a dataset, and an ontic segment sit in the same category — but they are not empty: an element qualifies when its absence, substitution, or alteration changes what inquiry can reach, produce, or warrant, and the types order what it admits. The term denotes the category; the elements it covers are its instances.

#### What is the fundamental structure of an epistemic element's `Decomposition Tree`?

```text
Epistemic Element (parent)
  (→ <Relationship Type>) <Epistemic Element>*  (son)
```

#### Which are some ideas to guide the decomposition of an `epistemic element`?

> A reference table defining the permitted link forms that govern and standardize the recursive decomposition of an `Epistemic Element` into its constituent and related epistemic elements.

> **Note:** If an `Epistemic Element` appears as a parent in a decomposition tree, only the child elements explicitly permitted by this reference table may be included, unless the child elements are defined by a template specified using `<<...>>`.
>
> **Note:** This kind of structure neither completes nor normates a decomposition. The table states only which parent–child links are permitted; it decomposes nothing by itself, and it does not dictate what any particular element must decompose into. A decomposition is complete only for a bound root instance, grown link by permitted link until every leaf resolves to an instance.

| Permitted Link Form | Description | Tags |
| --- | --- | --- |
| `<<Epistemic Element>> (→ <Relationship Type>) <<Epistemic Element>>` | Abstract form: any link between two epistemic element nodes, its label licensed by the relationship-type table in QA. | Form; General |
| `Epistemic Element (→ Kind) Epistemic Element Set` | Classifies an element as a coherent aggregate of epistemic elements. | Classification; Set |
| `Epistemic Element Set (→ Member) <<Epistemic Element>>` | Identifies a member of the aggregate; membership, not composition. | Composition; Set |
| `Epistemic Element Set (→ Kind) Epistemic Domain` | Classifies a set as an inquiry whole organized by a bounded cut of reality. | Classification; Set |
| `Epistemic Element Set (→ Kind) Epistemic Practice` | Classifies a set as an organized pattern of inquiry carried on by agents — the doing. | Classification; Set |
| `Epistemic Domain (→ Part) Epistemic Domain` | Identifies a sub-domain: field, sub-field, family, or specialty. | Composition; Domain |
| `Epistemic Domain (→ Has) Segment of Reality` | Identifies the bounded portion of reality the domain cuts. | Domain; Target |
| `Epistemic Domain (→ Has) Observable` | Identifies a feature of the segment registrable for inquiry. | Domain; Observable |
| `Epistemic Domain (→ Has) Epistemic Framework` | Identifies a lens system the domain reasons with. | Domain; Framework |
| `Epistemic Domain (→ Has) Epistemic Practice` | Identifies the practice carried on upon the cut; the inverse of `Addresses`. | Domain; Practice |
| `Segment of Reality (→ Kind) <<Ontic Element>>` | Binds the segment to its ontic type in the naturalis or social grammar. | Domain; Ontic |
| `Epistemic Practice (→ Part) Epistemic Practice` | Identifies a sub-practice: program, laboratory, school, or specialty. | Composition; Practice |
| `Epistemic Practice (→ Has) Epistemic Task` | Identifies a discrete unit of planned inquiry work assigned to an agent. | Composition; Practice |
| `Epistemic Task (→ Has) Epistemic Method` | Identifies a generalized method for a class of inquiry tasks. | Composition; Practice |
| `Epistemic Method (→ Instance) Epistemic Procedure` | Identifies the situated application of a method to a particular inquiry. | Composition; Practice |
| `Epistemic Procedure (→ Part) Epistemic Act` | Identifies a primitive inquiry act performed by an agent. | Composition; Practice |
| `Epistemic Procedure (→ Part) Epistemic Procedure` | Identifies a step or sub-routine of a larger procedure. | Composition; Practice |
| `Epistemic Task (→ Has) Epistemic Operation` | Identifies the operation a task applies. | Composition; Practice |
| `Epistemic Practice (→ Has) <<Epistemic Lane>>` | Identifies a lane the practice carries. | Composition; Practice |
| `Epistemic Practice (→ Addresses) Epistemic Domain` | Identifies the cut of reality the practice works on. | Composition; Practice |
| `Epistemic Practice (→ Produces) Epistemic Construction` | Identifies a construction the practice leaves behind. | Composition; Practice |
| `Epistemic Element (→ Kind) <<Epistemic Lane>>` | Classifies an element as one of the inquiry lanes. | Classification; Lane |
| `Epistemic Orientation (→ Has) <<Orientation Element>>` | Identifies a directing element of the orientation. | Orientation; Purpose |
| `Epistemic Agency (→ Has) Epistemic Agent` | Identifies an entity capable of performing epistemic operations. | Agency; Agent |
| `Epistemic Access (→ Has) Observation Interface` | Identifies a boundary mechanism coupling a segment to registration. | Access; Interface |
| `Observation Interface (→ Part) <<Observation Element>>` | Identifies an interface constituent. | Composition; Access |
| `Epistemic Access (→ Has) Observation Encoding` | Identifies the format in which a registered observation is carried. | Access; Encoding |
| `Epistemic Access (→ Has) Observation Record` | Identifies a registered representation of an observed aspect. | Access; Record |
| `Observation Record (→ Represents) Observable` | Identifies the observable feature a record stands for. | Access; Representation |
| `Epistemic Representation (→ Has) Representational System` | Identifies a sign system within which representations are formed and interpreted. | Representation; System |
| `Representational System (→ Part) Representation Element` | Identifies a combinable constituent of the system. | Representation; Element |
| `Representational System (→ Part) Constitutive Substrate` | Identifies the rules and structures constituting the system. | Representation; Substrate |
| `Representational System (→ Part) Epistemic Element` | General constituent link, used with care when no more specific classification applies. | Representation; Element; General |
| `Constitutive Substrate (→ Has) Property` | Identifies a property the system encodes. | Representation; Property |
| `Constitutive Substrate (→ Part) <<Constitutive Element>>` | Identifies a constituting rule or structure. | Representation; Substrate |
| `Epistemic Element (→ Kind) Epistemic Construction` | Classifies a construction: an artifact produced to organize, preserve, explain, or extend knowledge about a target. | Classification; Construction |
| `Epistemic Construction (→ Kind) <<Epistemic Construction>>` | Classifies a construction kind without asserting which kind before it is bound. | Classification; Construction |
| `Epistemic Construction (→ Part) Epistemic Construction` | Identifies a constituent construction: a theory holds models, a model holds constructs. | Composition; Construction |
| `Epistemic Construction (→ Has) Epistemic Blueprint` | Identifies the construction form the construction is built in. | Construction; Representation |
| `Epistemic Construction (→ Represents) <<Represented Aspect>>` | Identifies what the construction stands for. | Construction; Representation |
| `Epistemic Construction (→ Derived From) Observation Record` | Identifies the records the construction was built from. | Construction; Derivation |
| `Epistemic Construction (→ Evaluated By) Validation` | Identifies the check that discharges doubt about the construction. | Construction; Evaluation |
| `Epistemic Construction (→ Governed By) Epistemic Standard` | Identifies the standard the construction must satisfy. | Construction; Evaluation |
| `Epistemic Element (→ Kind) Epistemic Blueprint` | Classifies a construction form: a quasi-construction, the encoding format of constructions rather than their content. | Classification; Construction |
| `Epistemic Element (→ Kind) Epistemic Operation` | Classifies an operation of inquiry, read as a root in its own right. | Classification; Operation |
| `Epistemic Operation (→ Kind) <<Operation Element>>` | Classifies an operation of inquiry. | Operation; Action |
| `Action (→ Kind) Inference` | Classifies a derivation of content from premises. | Operation; Inference |
| `Inference (→ Kind) Deduction` | Classifies a derivation in which the conclusion follows necessarily. | Operation; Inference |
| `Organization (→ Kind) Principle` | Classifies a rule that guides proceeding. | Operation; Principle |
| `Epistemic Operation (→ Transforms) Epistemic Construction` | Identifies the construction an operation produces or rewrites. | Operation; Construction |
| `Epistemic Operation (→ Governed By) Epistemic Standard` | Identifies the standard the operation must satisfy. | Operation; Evaluation |
| `Epistemic Evaluation (→ Has) <<Evaluation Element>>` | Identifies an evaluative constituent. | Evaluation; Standard |
| `Epistemic Element (→ Kind) Epistemic Feedback` | Classifies feedback read as a root in its own right. | Classification; Evaluation |
| `Epistemic Communication (→ Has) <<Communication Element>>` | Identifies a communication constituent. | Communication; Inscription |
| `Epistemic Infrastructure (→ Has) <<Infrastructure Element>>` | Identifies an infrastructure constituent. | Infrastructure; Tool |
| `Epistemic Context (→ Has) Epistemic Condition` | Identifies a surrounding condition within which inquiry is interpreted. | Context; Conditions |
| `Epistemic Element (→ Kind) Epistemic Framework` | Classifies a lens system read as a root in its own right. | Classification; Framework |
| `Epistemic Framework (→ Part) Epistemic Tool` | Identifies a lens constituent. | Composition; Framework |
| `Epistemic Framework (→ Has) Epistemic Construction` | Identifies the constructs a framework holds. | Composition; Framework |
| `Epistemic Element (→ Kind) Ontic` | Classifies what exists, occurs, changes, or generates effects within a segment of reality. | Classification; Ontic |
| `Ontic (→ Kind) <<Ontic Element>>` | Binds the element to its ontic type in the naturalis or social grammar. | Classification; Ontic |

### Which are the available expansions of the slots?

> A slot (`<<…>>`) is bound with `:=`, never with an instance. Each row names one type the slot may take.

| Slot | Expansion | Description |
| --- | --- | --- |
| `<<Epistemic Element>>` | any type licensed in this guide | Binds the parent or child of the generic link form; the specific rows decide which pairs are permitted. |
| `<<Relationship Type>>` | any label in the relationship table | Names the relation asserted; the permitted table decides which labels may join which types. |
| `<<Ontic Element>>` | any type licensed in `philosophia-naturalis-et-operis` | The ontic reading of a segment; grown in the naturalis tree, never here. |
| `<<Epistemic Lane>>` | `Epistemic Orientation` | Why: the purpose, questions, goals, gaps, and roles directing the practice. |
| `<<Epistemic Lane>>` | `Epistemic Agency` | Who: the agents and roles that carry the practice. |
| `<<Epistemic Lane>>` | `Epistemic Access` | How registered: the interfaces, encodings, and records the practice works through. |
| `<<Epistemic Lane>>` | `Epistemic Representation` | In what: the notations and representational systems the practice reads and writes. |
| `<<Epistemic Lane>>` | `Epistemic Evaluation` | How judged: the standards, criteria, errors, checks, and feedback. |
| `<<Epistemic Lane>>` | `Epistemic Communication` | How shared: inscription, publication, and coordination. |
| `<<Epistemic Lane>>` | `Epistemic Infrastructure` | What supports it: tools, repositories, and institutions. |
| `<<Epistemic Lane>>` | `Epistemic Context` | Under what conditions: the surrounding conditions of the practice. |
| `<<Orientation Element>>` | `Epistemic Purpose` | The intended ultimate effect or value of the inquiry. |
| `<<Orientation Element>>` | `Epistemic Question` | A formulated question directing inquiry toward a gap. |
| `<<Orientation Element>>` | `Epistemic Goal` | A desired epistemic outcome toward which inquiry is directed. |
| `<<Orientation Element>>` | `Epistemic Gap` | A deficiency in available knowledge relative to the target. |
| `<<Orientation Element>>` | `Epistemic Role` | The function an element or agent performs within the practice. |
| `<<Observation Element>>` | `Transduction` | The conversion of a segment's state into a registrable signal. |
| `<<Observation Element>>` | `Sampling` | The selection of which occurrences or positions are registered. |
| `<<Constitutive Element>>` | `Convention` | A stabilized notational or interpretative choice. |
| `<<Constitutive Element>>` | `Formation` | A rule of well-formed combination. |
| `<<Constitutive Element>>` | `Foundation` | The axioms or principles a system is founded on. |
| `<<Constitutive Element>>` | `Interpretation` | A meaning assignment from symbols to what they denote. |
| `<<Epistemic Construction>>` | `Description` | A structured affirmation about a segment of reality. |
| `<<Epistemic Construction>>` | `Record` | An observation persisted as an addressable entry. |
| `<<Epistemic Construction>>` | `Dataset` | A structured collection of records for analysis. |
| `<<Epistemic Construction>>` | `Concept` | A constructed discriminator of aspects of the segment. |
| `<<Epistemic Construction>>` | `Model` | A construction enabling prediction or explanation of the segment. |
| `<<Epistemic Construction>>` | `Explanation` | A description clarifying cause, mechanism, or relation. |
| `<<Epistemic Construction>>` | `Prediction` | A description asserting an unobserved state or outcome. |
| `<<Epistemic Construction>>` | `Theory` | A system of constructs and claims about the segment. |
| `<<Epistemic Construction>>` | `Trajectory` | An ordered sequence of states attributed to the segment. |
| `<<Represented Aspect>>` | `Segment of Reality` | The bounded portion of reality a construction stands for. |
| `<<Represented Aspect>>` | `Observable` | A registrable feature of the segment a construction encodes. |
| `<<Operation Element>>` | `Action` | An operation that directly transforms, compares, or derives content. |
| `<<Operation Element>>` | `Organization` | An arrangement of actions into a reproducible structure. |
| `<<Operation Element>>` | `Epistemic Operator` | A named transformation read as an operator. |
| `<<Evaluation Element>>` | `Epistemic Standard` | The norm against which an artifact or operation is judged. |
| `<<Evaluation Element>>` | `Epistemic Criterion` | The property on which the judgment turns. |
| `<<Evaluation Element>>` | `Epistemic Constraint` | A bound on what the inquiry can achieve or hold. |
| `<<Evaluation Element>>` | `Epistemic Error` | A deviation of an artifact or operation from its standard. |
| `<<Evaluation Element>>` | `Validation` | A check that tests an artifact against reality. |
| `<<Evaluation Element>>` | `Verification` | A check that tests an artifact against its blueprint. |
| `<<Evaluation Element>>` | `Epistemic Feedback` | The return of an evaluation into the next operation. |
| `<<Communication Element>>` | `Epistemic Inscription` | A persistent rendering of epistemic content. |
| `<<Communication Element>>` | `Epistemic Publication` | The release of content to a readership. |
| `<<Communication Element>>` | `Epistemic Coordination` | The alignment of several agents' epistemic work. |
| `<<Infrastructure Element>>` | `Epistemic Tool` | An implement that extends what an agent can do. |
| `<<Infrastructure Element>>` | `Information Repository` | A store consulted instead of recomputed. |
| `<<Infrastructure Element>>` | `Epistemic Institution` | A body that sustains inquiry across generations. |

## How to decompose any epistemic element?

> A decomposition recursively expands an epistemic instance tree from its root: bind the root instance, then grow its subtree by attaching only links the `Permitted Link Forms` table allows, down to instance leaves. The reference tables above are scaffolding — necessary but not sufficient, and never normative: they say which links *may* appear, not which decomposition is correct for any given element. Choosing instances, depth, and stopping point remains the decomposer's work on the instance itself.

> See the worked case in QA below (### (Case Study) What is the recursively decomposed instance tree of Arithmetic?). Read the case table as the worked in-path-typed tree: the empty table here is filled the same way, typing each row from its nearest enclosing grouping segment and naming every link with its relationship type.

> Begin with the ontic questionnaire — which entities, substances, mechanisms, processes, events, and phenomena constitute the fundamental ontic elements of the target science? — then type each answer below.

> Note: Instance rows in the Instance Tree Path name instances, never types. Type names appear only as backticked grouping segments and never terminate a branch.

> **Constructing the instance path:** (1) bind the root — name the instance being decomposed; (2) extend — append each child by exactly one link the `Permitted Link Forms` table licenses, labelling it `(→ Relationship Type)`; (3) type — resolve each segment to its nearest enclosing grouping segment, declaring the root's type once; (4) check — every leaf resolves to an instance, no bare type terminates a branch, and no bare arrow remains.

**Rules:**

- **Form of the Table:** `Instance Tree Path | Description`.
- **Instance Tree Path**: A unique, recursively extended path identifying an instance within the decomposition tree. It begins at the root node `Epistemic Element`, descends the licensed kind chain to the instance's type, and appends each successive child through an explicitly labeled relationship, using the form Parent Instance (→ Relationship Type) Child Instance. Each successive path must preserve the complete path from the root to the current instance.
- **Root**: Every path begins at `Epistemic Element`; an inquiry whole binds `Epistemic Element Set → Kind → Epistemic Practice` (the doing) or `Epistemic Element Set → Kind → Epistemic Domain` (the cut), and takes its instance name as the root. A domain-rooted tree reaches its practice by `Has`; a practice-rooted tree reaches its domain by `Addresses`.
- **Relationship Labeling:** Every link between a parent and child names its relationship type, styled `(→ Kind)`, `(→ Has)`, `(→ Part)`, `(→ Instance)`, `(→ Addresses)`, `(→ Produces)`, or another label from the relationship table. A bare arrow is not permitted. Typing reads from grouping segments, never from the link: an instance resolves to its nearest enclosing grouping segment's type, with the decomposition root's type declared once.
- **Grouping Segments:** Every backticked grouping segment names a type licensed by the `Permitted Link Forms` table. A type that is not a row there may not appear in a tree, even when the relationship itself is permitted.
- **One Type per Distinction:** Do not type the same distinction twice. A discipline is an `Epistemic Domain` carrying the `Institutionalized` tag, never a `Epistemic Discipline` row; a set is disaggregated by `Member`, never by `Part`.
- **Permitted Links:** Every relationship must conform to a link form allowed by the `Permitted Link Forms` table. A link form licenses a possible relationship; it does not establish that the relationship actually exists in the instance being decomposed. `Instance` binds a type segment to an instance and needs no entry in that table.
- **Recursive Expansion:** Any epistemic instance identified in the tree may itself be decomposed recursively.
- **Decomposition Scope:** Select the aspects of the instance that need to be represented. A decomposition need not include every conceivable aspect of epistemic reality; it must adequately cover the aspects relevant to its stated purpose.
- **Stopping Condition:** Stop expanding a branch when its instance is sufficiently specified for the decomposition's purpose, when further expansion is unnecessary, or when the available evidence does not justify additional decomposition. A leaf is a stopping point in the current decomposition, not necessarily an intrinsically indivisible element. Every leaf must resolve to an epistemic instance.
- **Completeness:** A decomposition is complete relative to its declared scope and stopping criteria, not merely because every branch terminates. Relevant constituents, relations, structures, processes, states, and other aspects must not be omitted simply because the tree is syntactically valid.
- **Unlicensed or Uncertain Relationships:** If a necessary relationship is not covered by the reference table, do not silently invent a permitted link or substitute an unrelated one. Identify the gap and extend the reference table when justified. If the existence of a relationship is uncertain, mark that uncertainty rather than presenting the relationship as established.
- **Instance Identity:** Distinguish different instances even when they share the same type or description. The full `Instance Tree Path` identifies an instance's position within the particular decomposition; it does not, by itself, establish a globally unique identity outside that tree.
- **Tree Structure:** Each non-root row must extend an existing parent path by exactly one child relationship. The same instance may appear in multiple branches when it plays different roles in the decomposition; each occurrence must have its own path. Ensure a rich set of intermediate (internal) nodes — both types and instances — aiding understanding: composition, representation, transformation, validation, or other useful structural relationships.
- **Non-Normativity of Reference Tables:** The reference tables constrain which link forms may be used. They do not prescribe a universal decomposition order, determine which children must be included, or guarantee that a decomposition is conceptually adequate.
- **Well-formedness:** an instance decomposition is well-formed when every non-root row extends an existing path by exactly one link the `Permitted Link Forms` table licenses, every grouping segment carries a licensed type, branch order is never skipped, and every leaf resolves to an instance. Any row may serve as a decomposition root for recursive decomposition.
- **Naming Guidelines:**
  * **Naming:** Name every instance node in Title Case.
  * **Composite Instance Naming**: Name an ensemble — a set, a practice, a domain, or a construction corpus — with the suffix Set (Epistemic Element Set, Drug Modelling Set), etc.
* **Description:** Describe what the instance is, what role it plays, or why it is included in the decomposition. Descriptions clarify the instance but do not substitute for explicit relationship labels.

| Instance Tree Path | Description |
| --- | --- |
|  |  |


## QA

### Why is this note relevant?

> To reflect on and create a guide involving ontology and epistemology, with the goal of clarifying the target of study.

### Do I need a Theory of Modelling? Or should that theory emerge from ontology and epistemology?

> For now, the node of modeling is only a placeholder — for a theory of epistemology and ontology.

### What is the relationship between Ontology and Epistemology?

> They are mutually constraining duals of the same epistemic act: ontology constrains what can be known; epistemology constrains how the known is accessed and represented.

### Why use formal artifacts instead of relying on mental representations?

> To discipline our thinking.

| **Purpose** | **Description** |
| --- | --- |
| **Prediction** | Forecast behavior or outcomes under different conditions. |
| **Explanation** | Explain underlying mechanisms leading to observed phenomena. |
| **Design** | Design or optimize systems for specific purposes. |
| **Evaluation** | Assess performance and effectiveness. |
| **Exploration** | Explore complex systems difficult to study directly. |
| **Communication** | Communicate complex ideas understandably. |

### How do we figure out how nature works in practice?

> Not by looking randomly at isolated aspects, nor by relying uncritically on derived artifacts such as mathematical formalisms that represent a system only indirectly. Instead: ground inquiry in experiments, attend to deviations from current theory, and focus on unexplained processes, phenomena, or event streams — using discrepancies to locate gaps in understanding.

### Which aspects of reality are worth describing?

> Those exhibiting recurring patterns that enable explanation, prediction, intervention, or compression of experience — e.g. motion, mass, force, opportunity cost, trade-offs, Production–Possibility Frontier. **(Reader: notice the recursion here.)**

> Two different kinds of artifacts compress reality, and they must not be confused:
>
> - **Fundamental descriptive artifacts (concepts/aspects)** — concepts directly describing recurring structures of reality, enabling compression; meaningful standalone (motion, mass, force, opportunity cost). These identify **what** is described.
> - **Epistemic scaffolding tools** — frameworks supporting construction, organization, and reasoning about descriptions (numbers, geometry, logic, probability, calculus, graphs). These provide **how** descriptions are represented and manipulated.

### What is an epistemic activity?

> Any operation performed by an observer to construct, transform, evaluate, or apply knowledge about reality.

### What is the relation between `Epistemic Practice` and `Epistemic Activity`?

> **Practice is the pattern; Activity is the pattern exercised in time.** A practice organizes what recurs — tasks, methods, procedures, acts, roles, standards, instruments, and notations; an activity is one scheduled exercising of it — a field season, a modelling run, a proof campaign, a classification batch. Every activity belongs to a practice the way every exercised function belongs to a capability: the same duality, temporal instead of modal.

### Do we need `Epistemic Activity` as an epistemic element in the decomposition?

> **No.** A fully specified `Epistemic Practice` — its tasks, methods, procedures, acts, roles, standards, and control points — leaves no additional structural role for activity to contribute. Activity describes operation rather than structure, so it is not a decomposition node: decompose the practice.

### What is a description?

> A structured affirmation about a segment of reality, carried by an epistemic construction.

### What is an explanation?

> A very special form of description — maybe the ultimate form — clarifying cause, mechanism, or relation.

### How do we validate our descriptions of reality?

> By testing the construction against reality: prediction error, replication, and failed or successful intervention.

### Which aspects of reality result from multiplicative interaction?

> **Interaction-derived quantities** are ontic aspects quantifying the **joint state** of two or more independent ontic variables: momentum, kinetic energy, angular momentum, gravitational force, heat, revenue, cost, wage bill, information gain.

### Which area of reality is best suited for studying in order to improve my epistemic practice?

> Physics is a training ground for rigorous modeling because it enforces precise, testable, and feedback-rich representations of reality. The value lies in transferring this epistemic discipline — rather than its specific models — into more complex domains like social systems.

### Which relationship types can be used to explicitly label the → operator?

| Category | Type | Description | Link Case for |
|---|---|---|---|
| Classification | `Kind` | Establishes a taxonomic relationship in which the child specifies what kind of element the parent is. | Classifying an element under a more specific type. |
| Composition | `Part` | Identifies a constituent that forms part of the parent element. | Decomposing a system, structure, or aggregate into its constituent elements. |
| Composition | `Member` | Identifies an element belonging to a set or aggregate, without asserting that it forms part of another element. | Disaggregating an `Epistemic Element Set` or `Epistemic Domain`. |
| Composition | `Has` | Identifies an element, property, or feature belonging to or associated with the parent. | Identifying components, attributes, properties, or associated elements. |
| Composition | `Instance` | Identifies a situated realization of a generalized type — a method, a technique, a practice. | Connecting a generalized method to the procedure that applies it. |
| Composition | `Addresses` | Identifies the domain a practice works on. | Connecting an `Epistemic Practice` to the cut it targets. |
| Composition | `Produces` | Identifies the construction a practice or task leaves behind. | Connecting an `Epistemic Practice` to its constructions. |
| Constitution | `Constituted By` | Identifies the elements, rules, or structures that constitute the identity or organization of the parent. | Decomposing a representational or conceptual system into its constitutive foundations. |
| Realization | `Realized By` | Identifies a concrete instance through which an abstract type, system, or mechanism is realized. | Connecting an abstract structure or type to its concrete realization. |
| Instantiation | `Instance Of` | Identifies the general type or class to which a particular instance belongs. | Connecting a concrete instance to its defining type. |
| Derivation | `Derived From` | Identifies the source from which an element is obtained or derived. | Identifying the premises, data, or elements from which another element originates. |
| Transformation | `Transforms` | Identifies an element that is transformed or produced through an operation performed by the parent. | Representing transformations between input and output elements. |
| Representation | `Represents` | Identifies the reality, entity, or content represented by the parent. | Connecting a representation to its referent or represented target. |
| Causation | `Causes` | Identifies an element whose action or occurrence produces an effect in another element. | Representing causal relationships between phenomena or processes. |
| Regulation | `Regulates` | Identifies an element that controls, constrains, or modulates the behavior of another element. | Representing regulatory relationships and feedback structures. |
| Dependence | `Depends On` | Identifies an element whose existence, behavior, or operation depends on another element. | Representing structural, functional, or operational dependencies. |
| Association | `Related To` | Establishes an association between elements when no more specific relationship applies. | Representing a relevant relationship that cannot be classified more specifically. |
| General | `Unspecified` | Establishes a relationship between two elements when the nature of their connection is relevant but has not yet been identified or classified. | Representing a known or suspected connection whose specific relationship type remains undetermined. |


### (Case Study) What is the recursively decomposed instance tree of Arithmetic?

> Worked decomposition of arithmetic as an organized inquiry system, grown from the epistemic-act definition above to full intermediate detail. 

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic | The organized inquiry whole of discrete quantity, read as the practice of exact reckoning and the domain it cuts. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Addresses) `Epistemic Domain` | Grouping: the cut the practice addresses — discrete quantity, cut from the segment of reality below. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` | Grouping: orientation of arithmetic. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Purpose` | Grouping: purposes of the inquiry. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Purpose` (→ Instance) Exact Reckoning Purpose | Telos: determine exact discrete quantity — count, sum, product, quotient — leaving no remainder of doubt. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Question` | Grouping: questions directing reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Question` (→ Instance) Uncomputed Product | Formulated question directing reckoning toward the gap: what is seven times eight, as yet uncomputed. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Gap` | Grouping: gaps motivating reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Gap` (→ Instance) Missing Product Gap | Deficiency in available reckoning: the product not yet known, represented, or warranted. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` | Grouping: agencies of arithmetic. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` (→ Has) `Epistemic Agent` | Grouping: agents performing reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` (→ Has) `Epistemic Agent` (→ Instance) Reckoner | Entity counting, calculating, and proving; pupils, clerks, and mathematicians realize this agent. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Addresses) `Epistemic Domain` (→ Has) `Segment of Reality` | Grouping: the bounded portion of reality arithmetic cuts — collections of distinct items. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Addresses) `Epistemic Domain` (→ Has) `Segment of Reality` (→ Instance) Discrete Multitude | The segment itself: countable collections — heads of a flock, coins in a purse, days in a month. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Addresses) `Epistemic Domain` (→ Has) `Observable` | Grouping: features of the segment registrable for reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Addresses) `Epistemic Domain` (→ Has) `Observable` (→ Instance) Cardinality | The registrable feature: how many, independent of what is counted. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` | Grouping: the access regime through which multitude is registered. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` (→ Has) `Observation Interface` | Grouping: interfaces coupling multitude to count. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` (→ Has) `Observation Interface` (→ Instance) Tally Stick | Notched stick coupling a flock to the reckoner's count, one notch per head. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` (→ Has) `Observation Encoding` | Grouping: encodings of the count. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` (→ Has) `Observation Encoding` (→ Instance) Five-Bar Tally Encoding | Strokes grouped in fives for reading at a glance. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` | Grouping: representations of number. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` | Grouping: sign systems of arithmetic. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System | Signs with place rules forming numerals; notations realize this system. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Instance) Hindu-Arabic Numerals | Exemplar notation realizing the system: place-valued decimal digits. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Instance) Roman Numerals | Exemplar notation realizing the system: additive letter signs. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` | Grouping: combinable constituents. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` (→ Instance) Decimal Digit | One of 0–9 combining into numerals. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` (→ Instance) Operator Glyph | `+ − × ÷ =` combining numerals into equations. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` (→ Instance) Forty-Two | The numeral token `42` denoting forty-two. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` (→ Instance) Product Equation | The equation expression `7 × 8 = 56` as a checkable artifact. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` | Grouping: rules and structures constituting the system. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Instance) Number | Abstract construct identifying discrete multitude, order, and ratio. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Instance) Place Value | Position-weighted magnitude carried by numeral places. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Convention` | Grouping: stabilized notational choices. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Decimal Convention | Ten symbols including zero; positions weigh powers. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Formation` | Grouping: rules of well-formed combination. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Numeral Formation Rule | How digits compose into well-formed numerals. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Successor | Next-after relation generating the number series. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Instance) Zero | The empty count constituted as a number. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: axioms and foundings. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Addition Definition | Addition recursed from successor: adding one is taking the successor. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) First-Order Arithmetic | Axiom system underlying formal reckoning: zero, successor, induction; axiom systems realize these axioms. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) First-Order Arithmetic (→ Instance) Peano Arithmetic | Exemplar axiom system realizing these axioms: induction over all predicates. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) First-Order Arithmetic (→ Instance) Presburger Arithmetic | Exemplar axiom system without multiplication: complete and decidable. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` | Grouping: meaning assignments. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Decimal Place Encoding | Number → numeral mapping under decimal place value. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` | Grouping: the discrete units of planned reckoning work. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` | Grouping: the generalized methods the tasks run. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Column Arithmetic Method | Generalized method adding place-ordered numerals from the units column upward. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Column Arithmetic Method (→ Instance) `Epistemic Procedure` | Grouping: the situated procedure the method is applied as. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Column Arithmetic Method (→ Instance) `Epistemic Procedure` (→ Instance) Column Addition | Place-ordered summation with carrying. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Column Arithmetic Method (→ Instance) `Epistemic Procedure` (→ Instance) Column Addition (→ Part) `Epistemic Procedure` | Grouping: the carry sub-procedure. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Column Arithmetic Method (→ Instance) `Epistemic Procedure` (→ Instance) Column Addition (→ Part) `Epistemic Procedure` (→ Instance) Carry Step | Ten-for-one regrouping moving excess to the next place. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Shift-And-Add Multiplication | Generalized routine reducing products to shifted additions. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Tallykeeping Method | Generalized routine recording one stroke per item counted. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Tallykeeping Method (→ Instance) `Epistemic Procedure` | Grouping: the situated tallying procedure. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Tallykeeping Method (→ Instance) `Epistemic Procedure` (→ Instance) Tally Procedure | The situated tallying routine. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Tallykeeping Method (→ Instance) `Epistemic Procedure` (→ Instance) Tally Procedure (→ Part) `Epistemic Act` | Grouping: the primitive acts of tallying. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Tallykeeping Method (→ Instance) `Epistemic Procedure` (→ Instance) Tally Procedure (→ Part) `Epistemic Act` (→ Instance) Tallying Act | Primitive act marking one stroke per item counted. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Calculating Method | Generalized sequence of calculational acts toward exact reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Method` (→ Instance) Proving Method | Generalized derivation of arithmetical propositions from stated axioms. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` | Grouping: operations on numerals. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Action` | Grouping: direct transformations. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Action` (→ Instance) Reckoning | Rule-governed transformation of represented quantities. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Action` (→ Instance) Magnitude Comparison | Operational act judging greater, lesser, or equal between numerals. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Action` (→ Kind) `Inference` | Grouping: derivations from premises. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Action` (→ Kind) `Inference` (→ Kind) `Deduction` | Grouping: necessary derivations. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Action` (→ Kind) `Inference` (→ Kind) `Deduction` (→ Instance) Induction Proof | Proof by mathematical induction: base and step deriving the universal claim — deductive in epistemic standing. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Organization` | Grouping: coordinated routines. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Organization` (→ Kind) `Principle` | Grouping: rules guiding reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Organization` (→ Kind) `Principle` (→ Instance) Induction Principle | What holds of zero and passes to successors holds of all numbers. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Task` (→ Has) `Epistemic Operation` (→ Kind) `Organization` (→ Kind) `Principle` (→ Instance) Commutativity Principle | Order-independence of addition and multiplication. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` | Grouping: the constructions arithmetic produces about discrete quantity — what the DCESA does not leave unrecorded. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Instance) Sum Statement | A description: seven times eight are fifty-six, carried as a claim about the segment. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Instance) Evenness | A concept: the constructed property a number carries when it divides into two exact halves. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Instance) Multiplication Table | A dataset: products indexed by factor, consulted instead of recomputed. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Instance) Carrying Explanation | An explanation: why regrouping ten ones into one ten preserves the sum. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` | Grouping: assessments of reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Standard` | Grouping: standards judging arithmetic. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Standard` (→ Instance) Correctness Standard | A computation stands only if independent recomputation agrees. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Standard` (→ Instance) Proof Validity Standard | A proof stands only if each step follows by stated rule. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Standard` (→ Instance) Place-Value Standard | A numeral stands only if each place weighs its power of ten. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Criterion` | Grouping: evaluated properties. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Criterion` (→ Instance) Exactness Criterion | The result is exact or it is wrong; approximation has no standing here. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Constraint` | Grouping: limits on reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Constraint` (→ Instance) Working Memory Limit | Only so many partial products are held at once; the column relieves memory. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Error` | Grouping: deviations from the true value. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Error` (→ Instance) Dropped-Carry Error | Off-by-ten slip losing a carry, rendering seven times eight as fifty-four. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Validation` | Grouping: checks discharging doubt. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Validation` (→ Instance) Inverse Check | Division undoing multiplication to validate the product. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Validation` (→ Instance) Casting Out Nines | Modular-nine checksum validating long reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Feedback` | Grouping: evaluations returned to reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Feedback` (→ Instance) Recount After Mismatch | Recomputation ordered by a failed check. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` | Grouping: transmission of reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Inscription` | Grouping: persistent renderings. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Inscription` (→ Instance) Chalkboard Sum | Worked reckoning kept on the board for checking. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Publication` | Grouping: published reckonings. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Publication` (→ Instance) Reckoning Primer | Printed tables and rules teaching reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Publication` (→ Instance) Reckoning Primer (→ Instance) Liber Abaci | Exemplar primer realizing the genre: Fibonacci's 1202 transmission of place-valued reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` | Grouping: structures enabling reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Tool` | Grouping: tools of the reckoner. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Tool` (→ Instance) Calculator | Device performing calculation for the reckoner. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Tool` (→ Instance) Calculator (→ Instance) Abacus | Exemplar calculator realizing the tool: place-valued beads. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Information Repository` | Grouping: stored reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Information Repository` (→ Instance) Table Book | Bound addition and multiplication tables consulted instead of recomputed. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Institution` | Grouping: bodies sustaining reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Institution` (→ Instance) Schoolroom | Instruction drilling reckoning across generations. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Context` | Grouping: the surrounding conditions under which reckoning is situated. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Context` (→ Has) `Epistemic Condition` | Grouping: the conditions under which reckoning is carried on. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Context` (→ Has) `Epistemic Condition` (→ Instance) Oral Transmission Condition | Reckoning must be held in memory and recited: no external store is assumed. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Context` (→ Has) `Epistemic Condition` (→ Instance) Exactness Demand Condition | Exchange and accounting admit no approximation: a wrong count is a loss, not an estimate. |

### What Is a critical conceptual evaluation of `Epistemic Element`?

> Evaluated is the definition, not its use: "An `Epistemic Element` is anything that occupies a role in the practice by which reality is made intelligible — the reality cut as a target, the practice that investigates it, the constructions it produces, or what enables, constrains, evaluates, communicates, or conditions that practice. An element qualifies when its absence, substitution, or alteration changes what inquiry can reach, produce, or warrant; what passes no such test lies outside the category. Epistemic elements are typed as kinds of the Epistemic Order and, when composite, decompose into further epistemic elements through explicitly typed relationships."

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Specification** | | |
| Conceptual Identification | High | **Identity:** the differentia is stated — "occupies a role in the practice by which reality is made intelligible" — and the role list (target cut, practice, construction, enabling, constraining, evaluating, communicating, conditioning element) marks the category off from `Epistemic Domain`, `Epistemic Practice`, and `Epistemic Framework`, which are positions inside it. |
| Definitional Clarity | Moderate–High | **Intelligibility:** the definiens is explicit and non-circular; the residual vagueness sits in "made intelligible" and "can reach, produce, or warrant", both of which require the inquiry to be named. |
| Conceptual Determinacy | Moderate–High | **Boundary rules:** the removal test decides borderline cases — a notation that changes what can be warranted is in, a set of data that changes what can be predicted is in, a distant fact no inquiry reaches is refused. |
| Definitional Completeness | Moderate–High | **Constitutive conditions:** membership condition, role list, test, exclusion principle, typing, and decomposition are all stated; an exhaustive list of exclusions is not. |
| Internal Consistency | High | **Logical integrity:** membership does not run through the type system; typing only classifies what the role test has already admitted, and decomposability follows membership instead of establishing it. |
| Structural Coherence | High | **Internal organization:** one criterion (role), one test (change on removal), two consequences (typing and decomposition), stated in that order, with no competing register. |
| Conceptual Tractability | High | **Evaluability:** name the inquiry, place the element in a role, test whether it changes anything; then type and decompose. |
| **Representational Adequacy** | | |
| Extensional Fidelity | Moderate–High | **Classification accuracy:** identical elements are admitted or refused by the role test; the extension of the kinds remains bound to the reference table. |
| Intensional Adequacy | High | **Defining properties:** the inquiry and the role positions are the stated defining properties, not a proxy for them. |
| Ontological Adequacy | High | **Kind of entity:** it defines elements; the category/instance distinction is carried explicitly, and an ontic segment enters only as the target role, never as a second category. |
| Discriminative Power | Moderate–High | **Relevant distinctions:** separates target cut, doing, lens, construction, and ontic segment — roles the earlier wording merged into "epistemic content". |
| Granularity Adequacy | High | **Level of abstraction:** role membership is level-free, and recursion fixes granularity per purpose. |
| Empirical Adequacy | Moderate | **Evidence:** the removal test is checkable case by case, though the definition itself is analytic rather than empirical. |
| Representational Coverage | High | **Domain coverage:** the role positions cover domains, practices, tasks, methods, constructions, interfaces, standards, constraints, feedback, infrastructure, and the ontic segments they target. |
| **Conceptual Economy** | | |
| Ontological Parsimony | Moderate–High | **Structural economy:** one criterion, one test, two consequences in a single sentence — at the cost of a longer definiens than the loose original. |
| Conceptual Distinctiveness | High | **Unique contribution:** role-plus-test is not the vocabulary of the neighbouring philosophiae. |
| Redundancy Control | High | **Conceptual overlap:** domain, practice, and framework are disjoint wholes, so the membership test does not repeat the typing rules; typing and decomposability each do one job. |
| Boundary Differentiation | Moderate–High | **Separation from neighbours:** domain, practice, framework, construction, and ontic segment are marked by role position rather than by table entry alone. |
| **Epistemic Performance** | | |
| Epistemic Leverage | High | **Analytical yield:** admission becomes a decision that can be made and audited before any typing or decomposition begins. |
| Inferential Productivity | Moderate | **Reasoning capacity:** it supports role-based inference — if a construction represents a segment, the access, standards, and practice that produced it exist — beyond the trivial "decomposes into epistemic elements". |
| Explanatory Power | Moderate | **Explanatory contribution:** it says why an element is epistemic: what can be understood or warranted changes without it. |
| Predictive Utility | Low–Moderate | **Anticipatory capacity:** it predicts role-mates, not behaviour. |
| Information Compression | Moderate | **Representational efficiency:** the admission rule is compressed into one sentence, longer than the loose original but usable. |
| Problem-Solving Utility | High | **Practical contribution:** admission and decomposition are both checkable operations. |
| **Integration and Generality** | | |
| Contextual Robustness | High | **Contextual stability:** no knower or experience clause; the definition holds where inquiry is distributed, institutional, or non-human. |
| Combinatorial Fluidity | Moderate–High | **System integration:** a role in one inquiry types cleanly into the shared link grammar; composition still depends on the reference table. |
| Relational Compatibility | Moderate | **Compatibility:** compatible across the epistemic, ontic, and social orders by re-reading an element under a role, though relation vocabulary remains unshared. |
| Cross-Domain Portability | High | **Domain transfer:** role-in-inquiry travels across domains without reformulation. |
| Scale Invariance | High | **Scale transfer:** roles apply at every scale, and composites recurse. |
| Temporal Stability | Moderate | **Historical continuity:** "made intelligible" is epoch-relative; what counts as an epistemic problem is historically redefined. |
| **Operational and Methodological Validity** | | |
| Operationalizability | High | **Procedural applicability:** name the inquiry, assign the role, test removal — then type and decompose. |
| Measurement Validity | Not applicable | **Construct representation:** no measurement is intended at the category level; measures sit beneath it as `Epistemic Standard` and `Epistemic Criterion`. |
| Reliability | Moderate–High | **Repeatability:** the test narrows divergence to what the inquiry is taken to be. |
| Inter-Subjective Reproducibility | Moderate | **Agreement:** clear cases converge; a contested purpose still needs a user question, which the guide already requires for ambiguous roots. |
| Falsifiability or Refutability | Moderate | **Exposure to criticism:** the test can fail — an element whose removal changes nothing is refused. |
| Sensitivity to Evidence | Moderate–High | **Revisability:** evidence about an inquiry can reclassify an element, or expose a missing role. |
| **Normative and Strategic Adequacy** | | |
| Purpose Adequacy | High | **Functional fit:** fit for admission, typing, and decomposition in one instrument. |
| Normative Justification | Not applicable | **Value justification:** no values are embedded; prescriptions enter through `Epistemic Standard` and the normative philosophia. |
| Strategic Effectiveness | High | **Intervention utility:** the role positions map onto the circuit questions (why, who, what, how accessed, what is done, what is produced, how judged, under what conditions, what supports it). |
| Performative Effects | Moderate | **Effects of classification:** admission still reorganises how an inquiry is taught, funded, and governed, now with a test behind it. |
| Misuse Resistance | Moderate | **Resistance to abuse:** the role test blocks mere relabelling, though "intelligible" can still be stretched by a determined user. |

### Which note schema used - in order to document an epistemic element?

```bash
# (Epistemic Element)

> (Intro)

## Formulation

### What is this epistemic instance?
### What epistemic element type does this epistemic instance belong to?
### Is the type of this `epistemic element instance` ambiguous?
### What is the recursive instance decomposition of this epistemic instance?
### What Is a critical conceptual evaluation of this `epistemic element instance`?

## References

- ...
```

## References

- [Philosophia Naturalis](https://app.notion.com/p/Philosophia-Naturalis-32ac0f5171ec807b9388c870ab664abf?source=copy_link)
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
- [Concept](note.html?n=technique/systems/concept.md)
- Reality (no dedicated note yet — see the Formulation question above)
- Ontology (no dedicated note yet — see the Formulation question above)
- Observer (no dedicated note yet)
- Nature (no dedicated note yet)
- https://en.wikipedia.org/wiki/Reality
- Schopenhauer, A. (2016). The World as Will and Representation, Volume 1.
- Unger, R. M. (2024). The world and us. Verso Books.
- Lange, F. A. (1865). History of Materialism and Criticism of Its Present Importance. Leipzig: Verlag von Duncker & Humblot.
- Feynman, R. P. (1963). The Feynman lectures on physics. 1, 46.
- Landau, L. D., & Lifshitz, E. M. (2013). Course of Theoretical Physics. Elsevier.
- https://www.youtube.com/watch?v=X4PdPnQuwjY&t=19s
- A Guide to Reading
- System
- Energy
- Epistemic Artifact
- Philosophy
- Modelling
