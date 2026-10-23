---
tags: [technique, operation, method]
---

# Philosophia Artium Technicarum et Operis

> Reality is the total set of phenomena, entities, and processes that exist or occur, independently of an observer's perception or conceptualization, and which can, in principle, interact, change, or produce effects.

> Philosophia Artium Technicarum is the scaffolding used to transform, construct, and control reality through purposeful operation.

> This note is a guide connecting Reality with its Transformation — intervention, fabrication, operation, technique, and praxis. It is the complement of Philosophia Artium Epistemicarum et Operis: where that note systematizes how reality becomes intelligible, this one systematizes how reality is transformed.

## Formulation

### What is the nature of `technical practice`?

> Technical practice: (Reality; Knowledge, Resources) → Desired Transformation & Realized Difference.

> A technical activity is any operation performed by an agent to transform, construct, control, or maintain a segment of reality toward a desired state.

> The goal of technique is (1) to construct and maintain the scaffolding mechanisms of operation, and (2) to construct, deploy, and sustain the Domain Concrete Technical Artifact Set that realizes desired differences in reality.

### What is the role of the `technique` in human experience?

> Technique is an organized method for achieving a desired transformation through purposeful action.

> Technique enables agents to systematically transform, construct, and control aspects of reality to achieve desired states.

> The labour of technical practice goes hand in hand with a layout of reality — that is its operative template: every technical move presupposes an operative parsing of reality, and every operative distinction earns its keep through transformative use.

### What grounds `technical practice`?

> Technical practice is grounded in the purposive interaction of agents with reality through knowledge, resources, constraints, and techniques.

> Foundation - **Reality -** The ontological substrate comprising the physical, biological, informational, and social structures that constrain and respond to technical intervention. Steel beam, fluid flow, electric grid, living tissue, user population, software runtime environment.

### What is the reality we seek to transform?

> Observer-independent reality: it exists whether acted upon or modeled; it is composed of entities and processes with causal effects; it is dynamic and interconnected, producing emergent patterns; and it responds — imperfectly predictably — to intervention constrained by what actually exists.

> Reality is decomposed for operation in the Technical Order tree below.

### At which level of organization do we intervene?

> The hierarchical stratification of structural and functional components, from microscopic interactions to emergent macroscopic behaviors — crucial when intervening in systems with multiscale dynamics, memory, or adaptive laws.

- **Micro-level:** Individual elements and their local interactions.
- **Meso-level:** Subsystems, modules, clusters of interactions.
- **Macro-level:** Emergent patterns, global behavior, systemic properties.
- Systems thinking is **hierarchical**: different interventions require different levels of analysis.

### What is the ontology of the target?

> What is reality like as transformable? Which elements make it up? How do we identify them? Ontology answers by constraining what can be transformed; its operative constructs for parsing (entities, structures, regions, media, paths, interfaces, processes, states, constraints) live in the Technical Domain Reality Model below, and the full template in the Ontic Order branch of the epistemicarum guide.

### What Is the Structure of a `Technical Element`'s Decomposition Tree?

> How can we characterize the technical aspect of human experience?

> A taxonomy (conceptual structure) that renders the *intervention-oriented* and *fabrication-oriented* practice of agents intelligible.

> A `Technical Element` is a concept that denotes an element participating in the technical dimension of change experienced by humans or other purposeful agents, analytically identifiable as an instance of a technical element type and capable of being recursively decomposed into other technical elements through explicitly typed relationships. Note: This is a deliberately loose definition of the reality denoted by the concept.

> Note: Technical Element Type is recursive. The type of order of every technical element is the **Technical Order**. The `Permitted Link Forms` table below licenses how an element of one type decomposes into elements of another. Template slots (`<<…>>`), where used, are bound with `:=` instead of instances. Scaffold elements supporting, structuring, or evaluating intervention are distinct from operation's objects and targets, which are the content intervention acts upon. Relationships use `→` throughout.

> **Note on generic composites:** Different names may be used to refer to generic composites of technical elements, such as *Technical Domain*, *Technical Ecosystem*, *Technical System*, or similar concepts. Each carries its own semantics. For simplicity we use **`Technical Element Set`** as the generic type; ensemble scopes (ecosystems, DevOps sets) bind the placeholder as `Technical Element Set`. The composite `Production Technical System` heads the System spine.

> Recursion is introduced by allowing a composite to have another composite as an instance: a `Technical Element Set` may contain `Technical Element Set`s (a CI/CD practice within a DevOps set); a `Production Technical System` may contain further systems and whole sets besides its objects. Nesting composites in composites is what makes the type tree recursive.

#### What is the fundamental structure of a technical element's `Decomposition Tree`?

```text
Technical Element (parent)
  (→ <Relationship Type>) Technical Element*  (son)
```

> Instance paths use `→` throughout; typing reads from grouping segments rather than from the link, while the `Permitted Link Forms` table licenses which parent–child link may exist at the type level.

#### Which are some ideas to guide the decomposition of a `technical element`?

> A reference table defining the permitted link forms that govern and standardize the recursive decomposition of a `Technical Element` into its constituent and related technical elements.

> **Note:** If a `Technical Element` appears as a parent in a decomposition tree, only the child elements explicitly permitted by this reference table may be included, unless the child elements are defined by a template specified using `<<...>>`.
>
> **Note:** This kind of structure neither completes nor normates a decomposition. The table states only which parent–child links are permitted; it decomposes nothing by itself, and it does not dictate what any particular element must decompose into. A decomposition is complete only for a bound root instance, grown link by permitted link until every leaf resolves to an instance.

**Circuit questions.** Read the permitted links along the technical circuit:

- **Why?** What gap or purpose calls for intervention?
- **Who?** Which agent or practice acts?
- **With what?** Which techniques, supports, and resources?
- **On what?** Which object, target, or domain?
- **How transformed?** Which mechanism, interface, and acts?
- **What produced?** Which good or service?
- **How evaluated?** Which standard, verification, or validation?
- **Under what conditions?** Which configuration, parameters, constraints, hazards, risks, or trade-offs?
- **What sustains it?** Which maintenance, feedback, and lifecycle?

| Permitted Link Form | Description | Tags |
| --- | --- | --- |
| `Technical Element (→ Kind) Technical Element Set` | A collection of technical elements. | Classification; Composite |
| `Technical Element (→ Kind) Production Technical System` | Organized set of production technical objects whose interaction realizes a technical capability. It is composite: a system may contain further systems and whole `Technical Element Set`s (practices, tooling sets) besides its objects. | Classification; Composite |
| `Technical Element (→ Kind) Technical Problem` | Discrepancy between a current or projected state and a desired technical state that calls for intervention. | Classification; Context |
| `Technical Element (→ Kind) Technical Purpose` | Intended ultimate effect or value of the technical endeavor. | Classification; Context |
| `Technical Element (→ Kind) Technical Constraint` | Bound on technical action imposed by reality, resources, regulations, or other conditions. | Classification; Context |
| `Technical Element (→ Kind) Technical Resource` | Input required or consumed by technical activity. | Classification; Context |
| `Technical Element (→ Kind) Technical Domain Reality Model` | Operative model of the domain/environment in which technical practice is embedded and which grounds its operations: bounded tuple of entities, structures, regions, media, paths, interfaces, processes, states, and constraints. | Classification; Context |
| `Technical Element (→ Kind) Technical Requirement` | Formalized desired state, need, or performance objective a solution must satisfy. | Classification; Requirements |
| `Technical Element (→ Kind) Technical Specification` | Precise statement of requirements, parameters, performance, and interface conditions used to define and verify a solution. | Classification; Requirements |
| `Technical Element (→ Kind) Technical Parameter` | Variable whose value characterizes or controls a technical object or process. | Classification; Requirements |
| `Technical Element (→ Kind) Technical Standard` | Normative specification governing form, function, safety, interoperability, or performance. | Classification; Requirements |
| `Technical Element (→ Kind) Technical Research` | Systematic investigation aimed at discovering technical knowledge, principles, methods, materials, or capabilities. | Classification; Knowledge |
| `Technical Element (→ Kind) Technical Principle` | General rule governing construction or operation of technical systems. | Classification; Knowledge |
| `Technical Element (→ Kind) Technical Framework` | Overarching logic for structuring technical problems and generating or evaluating solutions. | Classification; Knowledge |
| `Technical Element (→ Kind) Technical Strategy` | Context-sensitive regime for planning, sequencing, prioritizing, and allocating technical work. | Classification; Knowledge |
| `Technical Element (→ Kind) Technical Institution` | Durable social structure that organizes, governs, or sustains technical practice and knowledge. | Classification; Knowledge |
| `Technical Element (→ Kind) Technical Agent` | Entity capable of executing Techniques using tools, resources, and knowledge. | Classification; Agency |
| `Technical Element (→ Kind) Technical Labor` | Purposive expenditure of human cognitive or physical effort in technical activity. | Classification; Agency |
| `Technical Element (→ Kind) Technical Competence` | Acquired capacity to reliably execute technical processes and techniques. | Classification; Agency |
| `Technical Element (→ Kind) Technical Architecture` | Fundamental structural organization of a technical system, including components, relationships, boundaries, and governing principles. | Classification; Structure |
| `Technical Element (→ Kind) Technical Blueprint` | Generative description prescribing how to create, assemble, or configure an artifact. | Classification; Structure |
| `Technical Element (→ Kind) Technical Configuration` | Particular arrangement of components, parameters, versions, and settings determining operational state. | Classification; Structure |
| `Technical Element (→ Kind) Technical Interface` | Defined boundary through which technical elements exchange matter, energy, information, or control. | Classification; Structure |
| `Production Technical System (→ Has) Production Technical Object` | Technical object produced within a production system and intended to enable action or further production; subdivided into physical and virtual objects. | Composition; Structure |
| `Production Technical Object (→ Kind) Physical Production Technical Object` | A production technical object whose operative structure is primarily material and whose operation is realized through physical effect. | Classification; Structure |
| `Production Technical Object (→ Kind) Production Virtual Technical Object` | A technical object whose operative structure is primarily informational or computational and whose operation is realized through computation. | Classification; Structure |
| `Production Technical Object (→ Part) Constitutive Technical Object` | Component or sub-assembly constituting a larger technical object or system. | Composition; Structure |
| `Production Technical System (→ Has) Producing Technical Element` | A technical element whose primary function is to transform reality itself — matter, energy, information, or a service performed on entities — yielding a Good. Implements that merely hold, house, meter, or convey that transformation (production facilities, instruments, tools, conveyors) are typed as `Production Support`, not as producers. | Composition; Structure |
| `Producing Technical Element (→ Kind) Material Good Producer` | Transforms matter into a delivered material good — formed, shaped, treated, or relocated matter whose finished state is the output. | Classification; Production |
| `Producing Technical Element (→ Kind) Energy Good Producer` | Transforms energy into delivered power, force, or conditioned energy. | Classification; Production |
| `Producing Technical Element (→ Kind) Information Good Producer` | Transforms information into a delivered informational or computational artifact. | Classification; Production |
| `Producing Technical Element (→ Kind) Service Good Producer` | Transforms reality by performing a service on entities, patients, or stocks, where the performed service *is* the good. | Classification; Production |
| `Production Technical Object (→ Kind) Production Support` | A production technical object that enables a producer's operation without itself transforming reality into the delivered good. | Classification; Structure |
| `Producing Technical Element (→ Has) Production Support` | Identifies the supports a producer relies on — tools, instruments, equipment, facilities, and machines. | Composition; Structure |
| `Production Support (→ Kind) Production Tool` | Implement that bears directly on the workpiece or target, shaping, holding, cutting, or joining it. | Classification; Production |
| `Production Support (→ Kind) Production Instrument` | Implement that measures, indicates, regulates, or monitors a production variable. | Classification; Production |
| `Production Support (→ Kind) Production Equipment` | Apparatus that conveys, holds, positions, or otherwise enables production without transforming the delivered good. | Classification; Production |
| `Production Support (→ Kind) Production Facility` | Built structure or site that houses, protects, and services production. | Classification; Production |
| `Production Support (→ Kind) Machine` | Drive, motion, or power package that actuates a tool or equipment. | Classification; Production |
| `Technical Element (→ Kind) Technical Dependency` | Relation in which one technical element requires another for production, operation, or maintenance. | Classification; Relation |
| `Technical Element (→ Kind) Technical Interaction` | Relation through which technical elements affect one another during operation or transformation. | Classification; Relation |
| `Technical Element (→ Kind) Technical Capability` | Value-producing possibility enabled by a technical function. | Classification; Capability |
| `Technical Element (→ Kind) Technical Mechanism` | Physical, procedural, or logical arrangement through which a function or transformation is produced. | Classification; Capability |
| `Technical Element (→ Kind) Technical Property` | Characteristic attributable to a technical object, process, or system. | Classification; Capability |
| `Technical Element (→ Kind) Technical Quality` | Degree to which desirable technical properties are possessed under relevant conditions. | Classification; Capability |
| `Technical Element (→ Kind) Technical Performance` | Realized quantitative behavior under specified conditions. | Classification; Capability |
| `Technical Element (→ Kind) Technical Practice` | Repeatable, organized pattern of technical work integrating activities, techniques, principles, standards, and tools. | Classification; Technique |
| `Technical Practice (→ Has) Technical Task` | Discrete unit of planned technical work assigned to an agent. | Composition; Technique |
| `Technical Task (→ Has) General Technique` | Generalized method for performing a class of technical operations. | Composition; Technique |
| `General Technique (→ Instance) Operative Technique` | Situated application of a technique by an agent to a particular technical situation. | Classification; Technique |
| `Operative Technique (→ Has) Technical Act` | Primitive Technique performed by an agent on reality or a technical object. | Composition; Technique |
| `Technical Practice (→ Has) Constitutive Technique` | A technique embodied in a technical element that constitutes part of its technical organization, establishing an internal dynamic logic through which the element operates and fulfills its technical role. | Composition; Technique |
| `Technical Practice (→ Has) Technical Interface & Actuation` | Boundary and means through which an agent encodes intent and acts upon a technical object or reality. | Composition; Technique |
| `Technical Element (→ Kind) Technical Feedback` | Information about intervention effects or system state that enables adjustment and error correction. | Classification; Control |
| `Technical Element (→ Kind) Technical Evaluation` | Systematic determination of properties, performance, adequacy, or conformity. | Classification; Control |
| `Technical Evaluation (→ Kind) Verification` | Evaluation of whether an artifact conforms to its specification or blueprint. | Classification; Control |
| `Technical Evaluation (→ Kind) Validation` | Evaluation of whether an artifact fulfills its intended purpose or solves the intended problem. | Classification; Control |
| `Technical Element (→ Kind) Technical Hazard` | Condition or source capable of producing an undesirable or harmful technical outcome. | Classification; Control |
| `Technical Element (→ Kind) Technical Risk` | Possibility and consequence of an undesirable technical outcome under uncertainty. | Classification; Control |
| `Technical Element (→ Kind) Technical Trade-off` | Relationship in which improvement in one property or objective constrains another. | Classification; Control |
| `Technical Element (→ Kind) Technical Failure` | State or event in which a technical object or process fails to perform a required function or satisfy a specification. | Classification; Control |
| `Technical Element (→ Kind) Technical Security` | Principles and practices concerned with protecting systems against unauthorized or adversarial actions. | Classification; Control |
| `Technical Element (→ Kind) Technical Maintenance` | Activity performed to preserve or restore an artifact's functional state. | Classification; Lifecycle |
| `Technical Element (→ Kind) Technical Service` | Technical capability delivered to an external agent or system through an operational interface. | Classification; Lifecycle |
| `Technical Element (→ Kind) Technical Lifecycle` | Temporal trajectory of a technical object from conception through production, operation, maintenance, modification, and retirement. | Classification; Lifecycle |
| `Technical Element (→ Kind) Technical Evolution` | Historical change in technical artifacts, processes, knowledge, and capabilities over time. | Classification; Lifecycle |
| `Technical Element (→ Kind) Technical Obsolescence` | Condition in which a technical artifact loses technical, economic, or social viability relative to alternatives. | Classification; Lifecycle |

### Which are the tags(adjectives) that can be used to enrich the nodes of the decomposition?

> `Tags` are analytical qualifiers attached to a node to characterize its properties, composition, relationships, formation, or mode of operation without creating a separate subtype for every variation.

Usage rules

- Tags qualify nodes; they do not replace the underlying type. For example, Deprecated [Technical Standard] remains a technical standard.
- Use a subtype when the distinction defines a recognized kind. Use a tag when the distinction qualifies an instance or can apply across multiple kinds.
- Allow multiple tags per node. A `Production Technical Object` can be `Virtual`, `Certified`, and `Obsolescent` simultaneously.
- Do not confuse a tag with a relationship. `Verified` describes an assessed standing; a permitted link such as `Technical Evaluation (→ Kind) Verification` expresses decomposition.
- Avoid redundant tags. If a subtype already entails a characteristic in the intended context, do not add the same tag unless it provides meaningful additional information.
- Distinguish a known absence from missing information. `Non-Reproducible` should be used only when the failure to reproduce is established, not merely because reproduction has not been attempted.

Case:

| Technical Category | Tags | Description | Usage |
| --- | --- | --- | --- |
| Technical Standard | `Deprecated` | Superseded by a later specification but still in use. | Legacy Protocol |
| Production Technical Object | `Virtual` | Operative structure primarily informational or computational. | Database Engine |
| Technical Maintenance | `Preventive` | Performed before failure to preserve functional state. | Scheduled Recalibration |


## How to decompose any technical instance?

> A decomposition recursively expands a technical instance tree from its root: bind the root instance, then grow its subtree by attaching only links the `Permitted Link Forms` table allows, down to instance leaves. The reference tables above are scaffolding — necessary but not sufficient, and never normative: they say which links *may* appear, not which decomposition is correct for any given element. Choosing instances, depth, and stopping point remains the decomposer's work on the instance itself.

> See the worked case in QA below (### (Case Study) What is the recursively decomposed instance tree of a CRM System?). Read the case table as the worked in-path-typed tree: the empty table here is filled the same way, typing each row from its nearest enclosing grouping segment.

> Note: Instance rows in the Instance Tree Path name instances, never types. Type names appear only as backticked grouping segments and never terminate a branch.

> **Constructing the instance path:** (1) bind the root — name the instance being decomposed; (2) extend — append each child by exactly one link the `Permitted Link Forms` table licenses; (3) type — resolve each segment to its nearest enclosing grouping segment, declaring the root's type once; (4) check — every leaf resolves to an instance, and no bare type terminates a branch.

**Rules:**

- **Form of the Table:** `Instance Tree Path | Description`.
- **Instance Tree Path:** A unique, recursively extended path identifying an instance within the decomposition tree. It begins with the root instance and appends each successive child instance through a directed link, using the form `Parent Instance → Child Instance`. Each successive path must preserve the complete path from the root to the current instance. Type grouping segments are styled `` `code` ``; instance nodes are plain Title Case text.
- **Root:** The root is the technical element type to which the technical instance being decomposed belongs or is related.
- **Relationship Labeling:** Every link between a parent and child uses `→`. Typing reads from grouping segments, never from the link: an instance resolves to its nearest enclosing grouping segment's type, with the decomposition root's type declared once.
- **Permitted Links:** Every relationship must conform to a link form allowed by the `Permitted Link Forms` table. A link form licenses a possible relationship; it does not establish that the relationship actually exists in the instance being decomposed.
- **Instance Grounding:** Each child must represent an element of the particular instance being decomposed, rather than merely a type that could theoretically occur within it. Type labels may be used to identify or organize instances, but classification alone does not establish that a corresponding instance exists.
- **Recursive Expansion:** Any technical instance identified in the tree may itself be decomposed recursively; any row may serve as a decomposition root.
- **Decomposition Scope:** Select the aspects of the instance that need to be represented. A decomposition need not include every conceivable aspect of technical reality; it must adequately cover the aspects relevant to its stated purpose.
- **Description:** Describe what the instance is, what role it plays, or why it is included in the decomposition. Descriptions clarify the instance but do not substitute for explicit typing.
- **Stopping Condition:** Stop expanding a branch when its instance is sufficiently specified for the decomposition's purpose, when further expansion is unnecessary, or when the available evidence does not justify additional decomposition. A leaf is a stopping point in the current decomposition, not necessarily an intrinsically indivisible element. Every leaf must resolve to a technical instance.
- **Completeness:** A decomposition is complete relative to its declared scope and stopping criteria, not merely because every branch terminates. Relevant constituents, relations, structures, processes, states, and other aspects must not be omitted simply because the tree is syntactically valid.
- **Unlicensed or Uncertain Relationships:** If a necessary relationship is not covered by the reference table, do not silently invent a permitted link or substitute an unrelated one. Identify the gap and extend the reference table when justified. If the existence of a relationship is uncertain, mark that uncertainty rather than presenting the relationship as established.
- **Instance Identity:** Distinguish different instances even when they share the same type or description. The full `Instance Tree Path` identifies an instance's position within the particular decomposition; it does not, by itself, establish a globally unique identity outside that tree.
- **Tree Structure:** Each non-root row must extend an existing parent path by exactly one child relationship. The same instance may appear in multiple branches when it plays different roles in the decomposition; each occurrence must have its own path. Ensure a rich set of intermediate (internal) nodes — both types and instances — aiding understanding: composition, support, dependency, transformation, validation, or other useful structural relationships.
- **Non-Normativity of Reference Tables:** The reference tables constrain which link forms may be used. They do not prescribe a universal decomposition order, determine which children must be included, or guarantee that a decomposition is conceptually adequate.
- **Well-formedness:** an instance decomposition is well-formed when every non-root row extends an existing path by exactly one link the `Permitted Link Forms` table licenses, every grouping segment carries a licensed type, branch order is never skipped, and every leaf resolves to an instance. Any row may serve as a decomposition root for recursive decomposition.
- **No repetition:** The root's own type must not be unnecessarily repeated as an intermediate grouping node. Exception: a same-type segment is allowed when it scopes a genuine instance family that would otherwise hang untyped (e.g. a `Technical Standard` grouping scoping the standards family inside a Biotechnology decomposition); a same-type segment with only generic description and no scoping function stays forbidden.
- **Well-Form Instance Tree Path Rule:** Ensure the decomposition provides a rich set of intermediate (internals) nodes - both - type and instances, aiding understanding. The set of intermediate instance nodes representing relationships such as subtyping, composition, support, dependency, or other useful structural relationships.
* Style Rules for Intermediate Nodes
  * **Instances:** Style intermediate nodes that represent actual technical instances as plain text (no adornment).
  * **Naming:** Name every instance node in Title Case — capitalize every whitespace- or hyphen-separated word (`Contact record` -> `Contact Record`, `Stage-entry criterion` -> `Stage-Entry Criterion`); preserve established all-caps acronyms (`API`, `CRM`). Type segments keep their table casing. The rule governs node names in Instance Tree Paths only; descriptions stay sentence-case prose.
  * **Composite Instance Naming**: A *composite* instance — a nested ensemble (a `Technical Element Set`, `Production Technical System`, `Technical Practice`, or sub-domain set), not an ordinary object, record, or mechanism — takes a name ending in `Set` once it sits at a depth greater than 2. Depth counts every segment of the Instance Tree Path, backticked type groupings included, the root type grouping being depth 1. At depth 2 or less the suffix is permitted but never required: `Technical Element Set` -> `Pharmaceutical Technical Domain Set` (depth 2) keeps it, `Technical Element Set` -> `Drug Discovery Set` (depth 3) requires it.
  * **Types:** Style bare technical element types used as grouping nodes as `` `code` ``.
  * **Distinction:** Never style an instance and a type in the same way; the distinction must be immediately visible.
  * **Grouping types:** A type used only to group instances is not itself an instance and must not terminate a branch.
  * The path link - is →.

| Instance Tree Path | Description |
| --- | --- |
|  |  |

## QA

### What type of technical element is a conveyor belt?

> A conveyor belt is **equipment, not a producer** — unless relocation is itself the delivered good. The test: does the element transform reality itself into the Good that is delivered?
>
> - **Producer** when the transformation *is* the service being delivered: a parcel depot's sorting conveyor delivers *delivered goods* — matter relocated to its destination is the good — so it types as a `Service Good Producer` (or `Material Good Producer` when the delivered good is the relocated material itself).
> - **Support** when it only carries another producer's output to the next station: the same belt inside a bottling line transforms nothing and produces nothing; it is a `Production Equipment` support attached under the bound `Producing Technical Element` through `Production Support`, never a producer itself.
>
> The same rule demotes the other supports: a `Production Facility` houses production, a `Production Instrument` meters it, a `Production Tool` bears on the workpiece, a `Machine` supplies the drive package. Each is a `Production Support` kind — none transforms reality on its own. Capacity alone is not production; transformation of reality is.

### What  type of technical element is a LLM?

> An LLM is a **virtual informational technical object**: an engineered computational artifact whose structure is constituted primarily by software, learned parameters, representations, and computational procedures rather than by directly observable physical structure. Its technical functions are realized through computation executed on physical infrastructure.
> 

### On the bad use of the term ‘Technology’?

> **Technology** — properly, the systematic study, knowledge, or theory of **technique and technical elements**; in everyday language, however, *technology* is commonly used metonymically to refer to the **technical elements themselves**—especially technical objects, systems, and artifacts.
> 

### What is the **most abstract formulation** that operation can take?

- Requirements → Technique → Product (Good, Service).
- Desired Difference → Controlled Transformation → Realized Difference.

### What is the relationship between `Technical Function` and `Technical Capability`?

> Note: **Technical Capability** and **Technical Function** are closely related and overlapping. **Function** is the raw concept: *what the artifact does*. **Capability** refers to the **value or possibility enabled by that function**: *what the function makes possible*.
> 

### Is every function realized through a mechanism?

> **Yes.** A function is realized by a mechanism that produces the required effect. However, **mechanism is a more abstract concept than process**: the same mechanism can realize different functions, depending on how it is organized or operated.
> 

### Is a mechanism identical to an underlying process?

> **No.** A mechanism is not necessarily identical to a single underlying process. A mechanism may **coordinate or combine multiple processes** to realize a function. Conversely, the same underlying process may participate in different mechanisms and contribute to different functions.
> 

### What is the relation between Function, Mechanism and Process?

> **Function** = what is achieved.
> 

> **Mechanism** = how the function is realized.
> 

> **Process** = an organized sequence of transformations or events that may constitute part of the mechanism.
> 

### What is the relation between 'Technical Capability' and 'Technical Function'?

> This is the modal reading of the same relation, not a rival definition. **Function** is what the element does; **capability** is the value-producing possibility that function enables. Modally, a capability is a function the element can exercise but is not currently exercising, while an exercised function is that capability in operation. A pump's function is to move fluid; its capability is the water supply it makes possible; idle, the capability is latent; running, the function is exercised.
> 

> A technical decomposition describes the **structure** of a technical element, not its real-time operation; therefore, **specifying its technical function is not necessary**.
> 

### What is the relation between `Technical Practice` and `Technical Activity`?

> **Technical Practice** is the pattern; **Technical Activity** is the pattern exercised in time. A Practice organizes *what* recurs — activities, techniques, principles, standards, tools; an Activity is one scheduled exercising of it — brief → build → launch → monitor → close. Every Activity belongs to a Practice the way every exercised Function belongs to a Capability: the same duality, temporal instead of modal.
> 

### Do we actually need `Technical Activity` as a technical element in the decomposition of a technical element, or is it already covered by `Technical Practice`, similar to the relationship between `Technical Function` and `Technical Capability`?

> **No.** A fully specified `Technical Practice`—including its Tasks, Techniques, Acts, standards, and control gates—leaves no additional structural role for `Technical Activity` to contribute. An Activity is the **temporal instantiation of a Practice**: it describes the Practice as it is actually being performed over time. Like `Technical Function`, it therefore describes **operation rather than structure** and is not necessary for the structural decomposition of a technical element.


### Why is the category `Technical Element Set` required?

> A **Technical Element Set** is required to represent coherent technical ensembles whose members belong to different technical element types but are related through a common technical object, standard, capability, production process, or technical domain.
> 

> Without this category, the taxonomy can describe the individual elements of such an ensemble, but it lacks a type for representing **the ensemble itself as a technical entity of organization**.
> 

> **Take as example:** the OpenAPI technical ecosystem. It comprises the OpenAPI Specification (OAS), OpenAPI documents, annotations, generators, plugins, libraries, validation tools, documentation tools, and generated artifacts. These elements have different technical element types, but are related through the common purpose of specifying, producing, validating, documenting, and consuming API interfaces. The **Technical Element Set** category provides a type for representing this coherent ensemble as a whole.
> 

### Why shouldn't `Technical Knowledge` be a technical element type?

> Technical Knowledge should not be a technical-element type because knowledge is already represented by the taxonomy as a distinct ontological category; making it a technical element would conflate the knowledge about a technical reality with the technical reality itself.

### Why do we need a `Technical Domain Reality Model Type`?

> A **Technical Domain Reality Model** fills the ontological gap between **reality itself** and the **technical practice that operates upon it**. It represents the **bounded, operative model of the relevant domain reality**—its entities, structures, processes, states, resources, interfaces, paths, and constraints—needed to make technical operations intelligible and executable.

> A `Technical Domain Reality Model` is needed because technical activity requires a bounded model of the part of reality it acts upon. It provides the domain-specific reality structure against which technical elements are defined, coordinated, executed, constrained, and evaluated.

### Is the genesis of a technical element its whole story?

> The genesis of an element — the invention or first demonstration of its working principle, registered under `Technical Evolution` — is necessary but not sufficient. An element becomes a *deployed* technical element only when its enabling conditions exist: the producing elements and tooling that make it manufacturable, the `Technical Resource`s it consumes, and the `Technical Constraint`s it must satisfy. These are as constitutive as the genesis, and often the harder problem.

> The steam engine is the standard case. James Watt's separate-condenser engine was conceived by the 1760s, but it could not be built until a cylinder could be bored round enough to hold steam; John Wilkinson's cannon-boring machine (patented 1774) supplied that condition, and by 1776 Boulton advertised a fifty-inch cylinder accurate to a shilling's thickness. The invention was Watt's; the enabling conditions that made it deployable were Wilkinson's. Type both: the genesis side is a `Technical Evolution` entry for the element, and the enabling side is its own element — a `Producing Technical Element` (a `Material Good Producer`, e.g. a machine tool) — joined to the deployed element by a `Technical Dependency`, with the resources and limits it answers typed as `Technical Resource` and `Technical Constraint`. Never file the enabling element as a footnote to the invention.

> Consequence for the decomposition: a tree that stops at the invention while leaving the producing element, resource, and constraint untyped has dropped a branch as load-bearing as the genesis it records. See [John Wilkinson](note.html?n=social/actor/private/persona/john-wilkinson.md).

### What is the role of engineering?

> Engineering is a training ground for rigorous intervention because it enforces precise, testable, and feedback-rich transformations of reality. The value lies in transferring this technical discipline — rather than its specific artifacts — into more complex domains like social systems.

### How to decompose an instance that belongs to multiple element types?

> By default, a **multi-root forest**: one root per candidate type, each root growing its own well-formed tree. No instance row ever carries two types — typing reads from grouping segments and the declared root binding. Ambiguity is resolved by multiplication of trees, not by compromise typing.

> A technical element can belong to many types: OpenAPI is a `Technical Standard` readable as a `Technical Element Set`; JobRunr is a `Constitutive Technical Object` readable as a `Technical Element Set` and as a `Production Technical System`; a DevOps practice is a `Technical Practice` readable as a `Technical Element Set`. Each reading gets its own root and its own tree: the OpenAPI-as-Standard tree decomposes spec versions and objects (normative content), while the OpenAPI-as-Set tree decomposes documents, tooling, and practices (ecosystem members). Well-formedness per tree is unchanged — every non-root row extends by exactly one link the `Permitted Link Forms` table licenses; leaves are instances, intermediate nodes give structure.

> When the root typing is ambiguous, ask the user for disambiguation instead of guessing. If no answer comes, build the **default root**: a primary type chosen from the `Permitted Link Forms` table in Formulation (under "What Is the Structure of a `Technical Element`'s Decomposition Tree?"), recorded as the note's primary belonging in the "What technical element type does this technical instance belong to?" Formulation answer, with secondary readings kept as `readable as …` prose. The default root is therefore always explicit in the note itself.

### (Case Study) What is the recursively decomposed instance tree of a CRM System?

> Worked decomposition of a CRM System, grown from the marketing-note subtree to full intermediate detail. Children are grouped under bare type-name segments, so the typing reads directly from the instance path: `CRM System` and `CRM Application` give structure (system scoping its production object; the application grouping its records beneath it); `Contact Record`, `Consent Record`, and `Lifecycle Stage` further structure their attributes beneath them, and `Contact Attribute Schema`, `Dedupe Mechanism`, `Stage-Transition Automation`, `Forms API`, and `Import API` structure a third level of fields, rules, and contracts beneath them; every grouping segment has its own row carrying the grouped type. Typing reads directly from the instance path: each instance resolves to the nearest enclosing grouping segment's type; the tree roots at `Production Technical System` scoping `CRM System`, decomposed here as scoped to the marketing practice. The remaining rows are final-node instances — concrete fields, tokens, formats, schedules, and measured values — and `HubSpot CRM` and `Salesforce` hang directly under the application as exemplar leaves realizing it, with one concrete deployment identifier each. Deployment-specific values and named vendors appear only in rows marked exemplar.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → CRM System | Production system of record for contacts, consent, and lifecycle stage. |
| `Production Technical System` → CRM System → `Production Technical Object` | Grouping: production objects realizing the system. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application | Vendor-neutral production object realizing the system of record; deployments realize this object. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Technical Parameter` | Grouping: parameters of the application. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Technical Parameter` → Schema Version | Version of the contact-and-consent schema the application enforces (exemplar value per deployment). |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` | Grouping: constitutive objects of the application. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record | Constitutive object holding one addressable contact. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Specification` | Grouping: specifications of the record. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Specification` → Contact Attribute Schema | Field contract: identifiers, consent flags, lifecycle stage. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Specification` → Contact Attribute Schema → `Technical Parameter` | Grouping: fields of the schema. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Specification` → Contact Attribute Schema → `Technical Parameter` → Identifier Field | Addressable key of the record, e.g. email (exemplar values per deployment). |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Specification` → Contact Attribute Schema → `Technical Parameter` → Consent Flag Field | Boolean flags recording consent state per contact (exemplar values per deployment). |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Specification` → Contact Attribute Schema → `Technical Parameter` → Lifecycle Stage Field | Stage attribute carried on the record, mirroring the lifecycle configuration (exemplar values per deployment). |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Mechanism` | Grouping: mechanisms of the record. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Mechanism` → Dedupe Mechanism | Merge logic resolving duplicate identities. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Mechanism` → Dedupe Mechanism → `Technical Specification` | Grouping: rules of the mechanism. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Mechanism` → Dedupe Mechanism → `Technical Specification` → Match Rule | Rule declaring which field comparisons constitute identity, e.g. email-exact plus name-fuzzy. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Technical Mechanism` → Dedupe Mechanism → `Technical Specification` → Survivorship Rule | Rule declaring which record's values survive a merge. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Verification` | Grouping: evaluations of the record. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Contact Record → `Verification` → Contact Verification | Check that a record conforms to the attribute schema and is deliverable. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record | Constitutive object holding opt-in evidence per contact (exemplar entries per deployment). |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Parameter` | Grouping: consent attributes. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Parameter` → Opt-In Timestamp | Proof-of-consent attribute (exemplar values per deployment). |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Parameter` → Consent Source | Origin of the consent: form, import, or manual entry (exemplar per deployment). |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Parameter` → Retention Window | How long consent evidence is kept, e.g. 24 months (exemplar value per deployment). |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Specification` | Grouping: consent norms. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Specification` → Consent Basis | Lawful basis recorded for the processing, e.g. consent, contract, legitimate interest. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Mechanism` | Grouping: consent lifecycle. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Mechanism` → Consent Capture | Recording of opt-in evidence from forms and imports into the Consent record. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Mechanism` → Withdrawal Handling | Propagation of preference-center withdrawals onto consent state. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Interface` | Grouping: consent boundaries. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → `Constitutive Technical Object` → Consent Record → `Technical Interface` → Preference-Center Boundary | Boundary through which a contact reviews and withdraws consent. |
| `Production Technical System` → CRM System → `Technical Configuration` | Grouping: configurations of the system. |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage | Stage marker moving contacts from lead to customer (exemplar stages per deployment). |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Specification` | Grouping: stage norms. |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Specification` → Stage Definition | Ordered stage list, e.g. lead, qualified, opportunity, customer (exemplar stages per deployment). |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Specification` → Stage-Entry Criterion | Condition a contact must satisfy to enter a stage. |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Mechanism` | Grouping: lifecycle mechanisms. |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Mechanism` → Stage-Transition Automation | Rule-driven moves on behavior or operator acts. |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Mechanism` → Stage-Transition Automation → `Technical Parameter` | Grouping: automation triggers. |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Mechanism` → Stage-Transition Automation → `Technical Parameter` → Behavior Trigger | Observed behavior firing a transition, e.g. form submit (exemplar per deployment). |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Mechanism` → Stage-Transition Automation → `Technical Specification` | Grouping: transition norms. |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Mechanism` → Stage-Transition Automation → `Technical Specification` → Transition Rule | Rule mapping triggers and operator acts onto stage moves. |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Capability` | Grouping: lifecycle capabilities. |
| `Production Technical System` → CRM System → `Technical Configuration` → Lifecycle Stage → `Technical Capability` → Progression Capability | Value realized: moving contacts from lead to customer. |
| `Production Technical System` → CRM System → `Technical Interface` | Grouping: interfaces of the system. |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API | Capture boundary for web-originated contacts. |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API → `Technical Specification` | Grouping: forms contracts. |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API → `Technical Specification` → Form Field Mapping | Contract binding form fields onto contact attributes. |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API → `Technical Parameter` | Grouping: forms parameters. |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API → `Technical Parameter` → Forms Auth Token | Credential authorizing submissions (exemplar value per deployment). |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API → `Technical Parameter` → Submission Rate Limit | Maximum accepted submissions per interval (exemplar value per deployment). |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API → `Technical Interface` | Grouping: forms endpoints. |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API → `Technical Interface` → Submission Endpoint | Endpoint receiving form payloads. |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API → `Technical Mechanism` | Grouping: submission mechanisms. |
| `Production Technical System` → CRM System → `Technical Interface` → Forms API → `Technical Mechanism` → Form Submission Flow | Submit-to-contact flow populating Contact and Consent records from form payloads. |
| `Production Technical System` → CRM System → `Technical Interface` → Import API | Bulk-ingestion boundary for lists (exemplar files per deployment). |
| `Production Technical System` → CRM System → `Technical Interface` → Import API → `Technical Specification` | Grouping: import contracts. |
| `Production Technical System` → CRM System → `Technical Interface` → Import API → `Technical Specification` → Import File Format | Accepted list-file format and column contract, e.g. CSV. |
| `Production Technical System` → CRM System → `Technical Interface` → Import API → `Technical Specification` → Import Column Map | Mapping of file columns onto contact attributes (exemplar per deployment). |
| `Production Technical System` → CRM System → `Technical Interface` → Import API → `Technical Parameter` | Grouping: import parameters. |
| `Production Technical System` → CRM System → `Technical Interface` → Import API → `Technical Parameter` → Import Schedule | Cadence of bulk ingestion, e.g. nightly (exemplar value per deployment). |
| `Production Technical System` → CRM System → `Technical Interface` → Import API → `Technical Mechanism` | Grouping: ingestion mechanisms. |
| `Production Technical System` → CRM System → `Technical Interface` → Import API → `Technical Mechanism` → Import Batch Flow | File-to-record flow bulk-loading Contact and Consent records from validated import files. |
| `Production Technical System` → CRM System → `Technical Interface` → Import API → `Validation` | Grouping: import evaluations. |
| `Production Technical System` → CRM System → `Technical Interface` → Import API → `Validation` → Import Validation | Check that an ingested file conforms to the import format before its rows enter the application. |
| `Production Technical System` → CRM System → `Technical Evaluation` | Grouping: system evaluations. |
| `Production Technical System` → CRM System → `Technical Evaluation` → Contact-Base Audit | Periodic determination of record quality across the contact base. |
| `Production Technical System` → CRM System → `Technical Evaluation` → Contact-Base Audit → `Technical Mechanism` | Grouping: audit execution. |
| `Production Technical System` → CRM System → `Technical Evaluation` → Contact-Base Audit → `Technical Mechanism` → Audit Sweep | Scheduled traversal measuring record quality across the contact base. |
| `Production Technical System` → CRM System → `Technical Quality` | Grouping: measured qualities of the base. |
| `Production Technical System` → CRM System → `Technical Quality` → Duplicate-Contact Rate | Measured share of duplicate identities in the base (exemplar measured value per deployment). |
| `Production Technical System` → CRM System → `Technical Performance` | Grouping: realized system behavior. |
| `Production Technical System` → CRM System → `Technical Performance` → Read Availability | Realized availability of contact reads (exemplar measured value per deployment). |
| `Production Technical System` → CRM System → `Technical Performance` → Read Availability → `Technical Mechanism` | Grouping: measurement. |
| `Production Technical System` → CRM System → `Technical Performance` → Read Availability → `Technical Mechanism` → Availability Probe | Probe sampling contact-read success to realize the availability measure. |
| `Production Technical System` → CRM System → `Technical Maintenance` | Grouping: continuity work on the system. |
| `Production Technical System` → CRM System → `Technical Maintenance` → Nightly Snapshot Backup | Backup preserving a restorable functional state, run nightly (exemplar schedule per deployment). |
| `Production Technical System` → CRM System → `Technical Service` | Grouping: services delivered by the system. |
| `Production Technical System` → CRM System → `Technical Service` → Contact Resolution Service | Contact-lookup capability delivered to the campaign pipeline through an operational interface. |
| `Production Technical System` → CRM System → `Technical Service` → Contact Resolution Service → `Technical Interface` | Grouping: delivery boundary. |
| `Production Technical System` → CRM System → `Technical Service` → Contact Resolution Service → `Technical Interface` → Resolution Endpoint | Operational boundary through which the campaign pipeline resolves contacts. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → HubSpot CRM | Exemplar production CRM realizing the application. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → HubSpot CRM → `Technical Parameter` | Grouping: deployment identifiers. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → HubSpot CRM → `Technical Parameter` → HubSpot Portal Identifier | Deployment identifier of the HubSpot portal (exemplar value per deployment). |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → Salesforce | Exemplar production CRM realizing the application. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → Salesforce → `Technical Parameter` | Grouping: deployment identifiers. |
| `Production Technical System` → CRM System → `Production Technical Object` → CRM Application → Salesforce → `Technical Parameter` → Salesforce Org Identifier | Deployment identifier of the Salesforce org (exemplar value per deployment). |

### What is the difference between a `Technical Element` and a `Technical Object`?

> `Technical Element` is the category: any element that participates in the technical dimension of change and is analytically identifiable as an instance of a technical element type. `Technical Object` is one type within that category — a relatively stable, functioning artifact, physical or virtual. Practices, tasks, constraints, standards, evaluations, and relations are technical elements without being technical objects. Every technical object is a technical element; not every technical element is an object. The table's `Production Technical Object`, `Physical Production Technical Object`, `Production Virtual Technical Object`, and `Constitutive Technical Object` are the production-side specializations of the object type.

### What is the difference between a `Technical Object` and a `Technical System`?

> A technical object is a bounded, functioning artifact; a technical system is a composite technical element whose organized objects, practices, and supports interact to realize a capability. A system is not merely a large object: it includes organization, interfaces, and often practices, and its capability belongs to the arrangement rather than to any single object. A CRM application is an object; the CRM system includes the application, records, import interfaces, lifecycle configuration, maintenance, and the practices that operate them.

### What distinguishes a `Production Support` from a `Producing Technical Element`?

> A producer transforms reality into the delivered good; a support enables that transformation without being its source. The test is whether the element's operation is the good delivered. A boring machine that cuts a cylinder is a `Material Good Producer`; the boring bar it drives, the gauge that measures the bore, the conveyor that carries the work, the factory that houses it, and the motor that supplies the drive are `Production Support` kinds — `Production Tool`, `Production Instrument`, `Production Equipment`, `Production Facility`, and `Machine` respectively. Capacity, housing, metering, conveyance, or drive is not production; transformation of reality is.

### What is the difference between `Technique`, `Technical Object`, and `Technology`?

> `Technique` is a structured method of action. `Technical Object` is an artifact that embodies and operationalizes techniques. `Technology` is the systematic study of technique and technical elements — or, in ordinary use, a metonym for the objects and systems. A technique can be performed without a dedicated object; an object can embody several techniques; technology is the knowledge field, not the artifact. See also "On the bad use of the term ‘Technology’" above.

### What is the difference between `Verification` and `Validation`?

> Verification asks whether an artifact conforms to its specification or blueprint — "was it built right?" Validation asks whether it fulfills its intended purpose or solves the intended problem — "was the right thing built?" A boring bar can verify against its dimensional specification and still fail validation if the cylinder does not hold steam. Verification is specification-relative; validation is purpose-relative.

### What is the relation between `Mechanism` and `Dynamics`?

> A mechanism is the structured arrangement through which a function or transformation is produced; dynamics is the temporal unfolding of that arrangement in operation. The mechanism states the organization; the dynamics states how it evolves, responds, and propagates effects over time. `Mechanism` is to dynamics what `program` is to computation: the program fixes the organized transitions, computation is their actual unfolding.

### Which note schema used - in order to document a technical element?

```bash
# (Technical Element)

> (Intro)

## Formulation

### What is this technical instance?
### What technical element type does this technical instance belong to?
### Is the type of this `technical element instance` ambiguous?
### What is the recursive instance decomposition of this technical instance?
### What Is a critical conceptual evaluation of this `technical element instance`?

## References

- ...
```

## References

- [Philosophia Naturalis et Operis](note.html?n=meta/philosophia-naturalis-et-operis.md)
- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- [Philosophia Artium Epistemicarum et Operis](note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md)
- [Technique](note.html?n=social/coordinator/technique.md)
- [Technology](note.html?n=social/structural/technical/technology.md)
- [Agency](note.html?n=social/action/public/agency.md)
- [Problem](note.html?n=social/problem/problem.md)
- [Questions](https://plato.stanford.edu/entries/questions/)
- [Philosophy of Technology](https://plato.stanford.edu/entries/technology/)
- Ontology (no dedicated note yet — see the Formulation question above)
- [Glossarium: Technique](/glossarium/?t=technique)
- [Glossarium: Technology](/glossarium/?t=technology)
- [Glossarium: Mechanism](/glossarium/?t=mechanism)
- [Glossarium: Technicity](/glossarium/?t=technicity)
- Simondon, G. (1958/1980). *On the Mode of Existence of Technical Objects*.
- Ellul, J. (1964). *The Technological Society*.
- Mitcham, C. (1994). *Thinking through Technology*.
- Vincenti, W. G. (1990). *What Engineers Know and How They Know It*.
- Simon, H. A. (1969). *The Sciences of the Artificial*.
