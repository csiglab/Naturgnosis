# Philosophia Artium Technicarum et Operis

> In this note, we will analyze the concept of purposeful (agentic) operation and its primary driver —  technique.

> This note seeks to systematize a philosophy of technique and operation that can serve as a conceptual foundation for organizing the ideas used to explain operation and praxis across diverse fields and tasks.

> It’s the complement of Philosophia Naturalis.

## Formulation

### What is the nature of the `technique`?

> Technique is an organized method for achieving a desired transformation through purposeful action.

### What is the role of the `technique` in human experience?

> Technique enables agents to systematically transform, construct, and control aspects of reality to achieve desired states.

### What is a `technical element`?

> It is a concept that denotes an element participating in the technical dimension of change experienced by humans or other purposeful agents. Note: This is a deliberately loose definition of the reality denoted by the concept.

### What grounds `technical practice`?

> Technical practice is grounded in the purposive interaction of agents with reality through knowledge, resources, constraints, and techniques.

> Foundation - **Reality -** The ontological substrate comprising the physical, biological, informational, and social structures that constrain and respond to technical intervention. Steel beam, fluid flow, electric grid, living tissue, user population, software runtime environment.

## How can we characterize the technical aspect of human experience?

> A taxonomy (conceptual structure) that renders the *intervention-oriented* and *fabrication-oriented* practice of agents intelligible.

> **Note:** Different names may be used to refer to generic composites of technical elements, such as *Technical Domain*, *Technical Ecosystem*, *Technical System*, or similar concepts. Each of these terms carries its own specific semantics. For the sake of simplicity and generality, however, we use the term **`Technical Element Set`** as the generic type. The specific semantics are then provided by the particular set itself, rather than being encoded in the generic type.

> Recursion is introduced by allowing a composite to have another composite as an instance: a `Technical Element Set` may contain `Technical Element Set`s (a CI/CD practice within a DevOps set). Nesting composites in composites is what makes the type tree recursive.

> **Note on relations :** Regarding instance decomposition and the recursive view of the technical element type tree, the relations between elements are not specified in this document and are intentionally left open for now.

> Every non-generic type is defined exactly once, in the Tabular view above. The Recursive view below states expansion rules only and introduces no subtypes of its own. The generic composite `Technical Element Set` is embodied by the placeholder binding itself, not by a child row; the composite `Production Technical System` heads the System spine.

> Each type with its category, role description, and instances.

### Tabular View

| **Technical Category** | **Technical Element Type** | **Description (Role)** | **Instance(s)** |
| --- | --- | --- | --- |
| **Composite** | Technical Element Set | A collection of technical elements. | Semiconductor manufacturing ecosystem; modern LLM ecosystem |
|  | Production Technical System | Organized set of production technical objects whose interaction realizes a technical capability. It is composite: a system may contain further systems and whole `Technical Element Set`s (practices, tooling sets) besides its objects. | Power plant; computer system; manufacturing line |
| **Technical Context** | Technical Problem | Discrepancy between a current or projected state and a desired technical state that calls for intervention. | Reducing query latency below 200 ms under 10× load |
|  | Technical Purpose | Intended ultimate effect or value of the technical endeavor. | Transport passengers; cure an infection; provide real-time financial data |
|  | Technical Constraint | Bound on technical action imposed by reality, resources, regulations, or other conditions. | Material strength; power budget; latency floor; regulatory restriction |
|  | Technical Resource | Input required or consumed by technical activity. | Silicon wafers; electricity; RAM; labor-hours; capital |
|  | Technical Domain Reality Model | Operative model of the domain/environment in which technical practice is embedded and which grounds its operations: bounded tuple of entities, structures, regions, media, paths, interfaces, processes, states, and constraints. | Operating-site model for a surgical robot; urban street model for autonomous driving; software runtime environment model |
| **Requirements & Definition** | Technical Requirement | Formalized desired state, need, or performance objective a solution must satisfy. | 99.99% uptime; <50 dB noise |
|  | Technical Specification | Precise statement of requirements, parameters, performance, and interface conditions used to define and verify a solution. | API response time <200 ms p99; −40°C to +85°C operating range |
|  | Technical Parameter | Variable whose value characterizes or controls a technical object or process. | Voltage; timeout; CPU frequency; thread count; tolerance |
|  | Technical Standard | Normative specification governing form, function, safety, interoperability, or performance. | POSIX; HTTP; ISO standards; electrical codes |
| **Knowledge & Methodology** | Technical Research | Systematic investigation aimed at discovering technical knowledge, principles, methods, materials, or capabilities. | Novel battery chemistry; new semiconductor process |
|  | Technical Principle | General rule governing construction or operation of technical systems. | Least privilege; redundancy; fail-safe; separation of concerns |
|  | Technical Framework | Overarching logic for structuring technical problems and generating or evaluating solutions. | Systems engineering; TRIZ; control theory; FMEA |
|  | Technical Strategy | Context-sensitive regime for planning, sequencing, prioritizing, and allocating technical work. | Agile; waterfall; prototyping-first; blue-green deployment |
|  | Technical Institution | Durable social structure that organizes, governs, or sustains technical practice and knowledge. | IEEE; FAA; corporate R&D division; standards body |
| **Agents & Competence** | Technical Agent | Entity capable of executing Techniques using tools, resources, and knowledge. | Engineer; robot; compiler; build pipeline |
|  | Technical Labor | Purposive expenditure of human cognitive or physical effort in technical activity. | Programming; machining; electrical installation |
|  | Technical Competence | Acquired capacity to reliably execute technical processes and techniques. | Surgeon’s procedural skill; engineer’s systems expertise |
| **System Structure** | Technical Architecture | Fundamental structural organization of a technical system, including components, relationships, boundaries, and governing principles. | Client-server; microkernel; microservices; layered architecture |
|  | Technical Blueprint | Generative description prescribing how to create, assemble, or configure an artifact. | Engineering drawing; source code; CAD model; IaC template |
|  | Technical Configuration | Particular arrangement of components, parameters, versions, and settings determining operational state. | FreeBSD kernel configuration; Kubernetes deployment configuration |
|  | Technical Interface | Defined boundary through which technical elements exchange matter, energy, information, or control. | API; electrical connector; CLI; network protocol |
|  | Production Virtual Technical Object | A technical object whose operative structure is primarily informational or computational and whose operation is realized through computation. | LLM, database, algorithm, simulation |
|  | Production Technical Object | Technical object produced within a production system and intended to enable action or further production. | Aircraft; server; turbine; software product |
|  | Constitutive Technical Object | Component or sub-assembly constituting a larger technical object or system. | CPU; battery cell; bearing; database schema |
| **System Relations** | Technical Dependency | Relation in which one technical element requires another for production, operation, or maintenance. | Application → operating system → hardware |
|  | Technical Interaction | Relation through which technical elements affect one another during operation or transformation. | Sensor → controller → actuator |
| **Mechanism & Capability** | Technical Capability | Value-producing possibility enabled by a technical function. | Network communication; secure authentication; high-speed computation |
|  | Technical Mechanism | Physical, procedural, or logical arrangement through which a function or transformation is produced. | Milling; refactoring; soldering; garbage collection |
|  | Technical Property | Characteristic attributable to a technical object, process, or system. | Mass; latency; modularity; reliability |
|  | Technical Quality | Degree to which desirable technical properties are possessed under relevant conditions. | Reliability; maintainability; efficiency; safety |
|  | Technical Performance | Realized quantitative behavior under specified conditions. | 10 Gbit/s throughput; 99.99% availability |
| **Technique** | Technical Practice | Repeatable, organized pattern of technical work integrating activities, techniques, principles, standards, and tools. | CI/CD; TDD; SRE; preventive maintenance |
|  | Technical Task | Discrete unit of planned technical work assigned to an agent. | Implement authentication; calibrate sensor |
|  | General Technique | Generalized method for performing a class of technical operations. | TIG welding; unit testing; photolithography |
|  | Operative Technique | Situated application of a technique by an agent to a particular technical situation. | Applying TIG welding to a specific aluminum joint |
|  | Constitutive Technique | A technique embodied in a technical element that constitutes part of its technical organization, establishing an internal dynamic logic through which the element operates and fulfills its technical role. | Parsing, optimization, code generation |
|  | Technical Act | Primitive Technique performed by an agent on reality or a technical object. | Cutting; welding; compiling; deploying; measuring |
|  | Technical Interface & Actuation | Boundary and means through which an agent encodes intent and acts upon a technical object or reality. | CNC spindle + G-code; robotic gripper + controller |
| **Technical Control** | Technical Feedback | Information about intervention effects or system state that enables adjustment and error correction. | Sensor reading; build error; crash report; quality inspection |
|  | Technical Evaluation | Systematic determination of properties, performance, adequacy, or conformity. | Benchmarking; inspection; testing |
|  | Verification | Evaluation of whether an artifact conforms to its specification or blueprint. | Unit tests; static analysis; dimensional inspection |
|  | Validation | Evaluation of whether an artifact fulfills its intended purpose or solves the intended problem. | User validation; operational trials |
|  | Technical Hazard | Condition or source capable of producing an undesirable or harmful technical outcome. | Exposed voltage; thermal runaway; race condition |
|  | Technical Risk | Possibility and consequence of an undesirable technical outcome under uncertainty. | Structural failure risk; security breach risk |
|  | Technical Trade-off | Relationship in which improvement in one property or objective constrains another. | Performance vs. energy consumption; flexibility vs. complexity |
|  | Technical Failure | State or event in which a technical object or process fails to perform a required function or satisfy a specification. | Crash; structural fracture; thermal runaway |
|  | Technical Security | Principles and practices concerned with protecting systems against unauthorized or adversarial actions. | Access control; encryption; authentication |
| **Lifecycle & Continuity** | Technical Maintenance | Activity performed to preserve or restore an artifact's functional state. | Patching; lubrication; recalibration; replacement |
|  | Technical Service | Technical capability delivered to an external agent or system through an operational interface. | DNS resolution; payment processing; electricity delivery |
|  | Technical Lifecycle | Temporal trajectory of a technical object from conception through production, operation, maintenance, modification, and retirement. | Design → production → deployment → operation → retirement |
|  | Technical Evolution | Historical change in technical artifacts, processes, knowledge, and capabilities over time. | Vacuum tubes → transistors → integrated circuits |
|  | Technical Obsolescence | Condition in which a technical artifact loses technical, economic, or social viability relative to alternatives. | Legacy operating system; obsolete communication protocol |

### Recursive view

> This table defines the **expansion grammar** for valid type trees. It specifies how a `Technical Element Type` may recursively expand; it does not enumerate technical element types. Types and their instances are defined in the **Tabular View**.
>
> **Expansion**
>
> * The root binds `(root) -> <<Technical Element>>` to any type defined in the Tabular View.
> * A bound type may expand through a **down-spine** or by **nesting** another composite.
> * `Technical Element Set` and `Production Technical System` are recursive composites: they may contain any technical element type, including further sets or systems, at any depth.
>
> **Notation**
>
> * `->` means **containment in scope**, not a specified relationship.
> * `...` means zero or more intermediate composite nestings.
> * `{any Technical Element Type}` means any terminal type defined in the Tabular View.
>
> An instance `Tree Path` is valid when it can be generated by these expansion rules.

| **Technical Element Type Tree Expansion Path** | **Expansion Rule** |
| --- | --- |
| `(root) -> <<Technical Element>>` | Binding rule: per decomposition the placeholder takes the root instance's Tabular type, and the path continues down that type's spine or facet attachments. It embodies the generic composite: ensemble scopes (ecosystems, DevOps sets) bind here as `Technical Element Set`. `->` links type-expansion steps: binding at the root, containment-in-scope below. Instance-tree paths use plain `→` for instance containment. |
| `(root) -> <<Technical Element>> -> ... -> Technical Element Set` | Recursion: a set nests inside a composite at any depth. |
| `(root) -> <<Technical Element>> -> ... -> Production Technical System` | Recursion: a system nests inside a composite at any depth. |
| `(root) -> <<Technical Element>> -> ... -> Production Technical System -> <<Technical Element>>` | System-composite rule: any technical element type may occur scoped inside a `Production Technical System` at any depth. |
| `(root) -> <<Technical Element>> -> ... -> {any Technical Element Type}` | General rule: any technical element type may occur at any depth beneath the bound root. |

## How to decompose any technical instance?

> A decomposition of a technical instance is essentially an expansion of its tree, starting from the root—the technical element itself—and adding nodes that are related to it, complement it, form part of it, support it, operate it, etc.

> See the worked case in QA below (### (Case Study) What is the recursively decomposed instance tree of a CRM System?). Read the case table as the worked in-path-typed tree: the empty table here is filled the same way, typing each row from its grouping segments and the declared root binding.

> **Technical Element Type Tree Path:** the expansion path typing one instance row (fourth column) — `(root) -> <<Technical Element>>` bound to the row's Tabular type, continued by exactly one licensed expansion: a spine-ordered suffix, a facet attachment, or a schema nesting. In other words, a Tree Path is what a Tree Expansion Path licenses. It is a type-level path (`->`), never to be confused with the Instance Tree Path (first column), which strings instances with `→`.

> **Constructing the path:** (1) type the instance — find its row in the Tabular view; (2) bind — write `(root) -> <<Technical Element>>` as that type; (3) extend — continue with exactly one licensed expansion from the bound position (spine-ordered suffix, facet attachment under the bound root, or schema nesting); (4) check — single types and spine-ordered chains always license; anything else must match a schema row.

The tree is governed by the following rules:	

* **Root:** The root is the technical element type to which the technical instance being decomposed belongs or is related.
* **Structure:** Intermediate nodes provide the structure needed to organize the decomposition - they can be technical instances - or technical types. Technical Types cannot be the final nodes in the tree - may be used as grouping nodes, but they are not themselves instances.
* **Leaves:** Every leaf must resolve to a technical instance.
* **Typing:** Every instance is typed — by its fourth-column Tree Path where the table carries one, otherwise by its nearest enclosing grouping segment, with the decomposition root's type declared once.
* **Recursion:** Any technical instance identified in the tree may itself be decomposed recursively.
* **No repetition:** The root's own type must not be unnecessarily repeated as an intermediate grouping node. Exception: a same-type segment is allowed when it scopes a genuine instance family that would otherwise hang untyped (e.g. a `Technical Standard` grouping scoping the standards family inside a Biotechnology decomposition, whose fourth-column counterpart is `(root) -> <<Technical Element>> -> ... -> Technical Standard`); a same-type segment with only generic description and no scoping function stays forbidden.
* **Well-Form Instance Tree Path Rule:** Ensure the decomposition provides a rich set of intermediate (internals) nodes - both - type and instances, aiding understanding. The set of intermediate instance nodes representing relationships such as subtyping, composition, support, dependency, or other useful structural relationships.
* Style Rules for Intermediate Nodes
  * **Instances:** Style intermediate nodes that represent actual technical instances as plain text (no adornment).
  * **Naming:** Name every instance node in Title Case — capitalize every whitespace- or hyphen-separated word (`Contact record` -> `Contact Record`, `Stage-entry criterion` -> `Stage-Entry Criterion`); preserve established all-caps acronyms (`API`, `CRM`). Type segments keep their Tabular casing. The rule governs node names in Instance Tree Paths only; descriptions stay sentence-case prose.  
  * **Composite Instance Naming**: A *composite* instance — a nested ensemble (a `Technical Element Set`, `Production Technical System`, `Technical Practice`, or sub-domain set), not an ordinary object, record, or mechanism — takes a name ending in `Set` once it sits at a depth greater than 2. Depth counts every segment of the Instance Tree Path, backticked type groupings included, the root type grouping being depth 1. At depth 2 or less the suffix is permitted but never required: `Technical Element Set` -> `Pharmaceutical Technical Domain Set` (depth 2) keeps it, `Technical Element Set` -> `Drug Discovery Set` (depth 3) requires it.
  * **Types:** Style bare technical element types used as grouping nodes as `` `code` ``.
  * **Distinction:** Never style an instance and a type in the same way; the distinction must be immediately visible.
  * **Grouping types:** A type used only to group instances is not itself an instance and must not terminate a branch.
  * The path link - is →.
* **Technical Element Type Tree Path**: Contains only a concrete path of technical element types; it cannot contain expansion patterns or placeholders.

| Instance Tree Path | Description
| --- | --- |
|  |  |

## QA

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

> A Technical Capability is a latent functionality: a function that a technical element is capable of exercising but is not currently exercising. A Technical Function is a capability being exercised in operation.
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

### How to decompose an instance that belongs to multiple element types?

> By default, a **multi-root forest**: one root per candidate type, each root growing its own well-formed tree. No instance row ever carries two types — where the table carries a fourth column it holds exactly one type path per row; otherwise typing reads from grouping segments and the declared root binding. Ambiguity is resolved by multiplication of trees, not by compromise typing.

> A technical element can belong to many types: OpenAPI is a `Technical Standard` readable as a `Technical Element Set`; JobRunr is a `Constitutive Technical Object` readable as a `Technical Element Set` and as a `Production Technical System`; a DevOps practice is a `Technical Practice` readable as a `Technical Element Set`. Each reading gets its own root and its own tree: the OpenAPI-as-Standard tree decomposes spec versions and objects (normative content), while the OpenAPI-as-Set tree decomposes documents, tooling, and practices (ecosystem members). Well-formedness per tree is unchanged — every fourth-column path, where the table carries one, must be licensed by an expansion rule; leaves are instances, intermediate nodes give structure.

> When the root typing is ambiguous, ask the user for disambiguation instead of guessing. If no answer comes, build the **default root**: a primary type chosen from the Tabular view above (the "How can we characterize the technical aspect of human experience?" table), recorded as the note's primary belonging in the "What technical element type does this technical instance belong to?" Formulation answer, with secondary readings kept as `readable as …` prose. The default root is therefore always explicit in the note itself.

### Which note schema used - in order to document a technical element?

```bash
# (Technical Element)

> (Intro)

## Formulation

### What technical element type does this technical instance belong to?
### What is this technical instance?
### What is the recursive instance decomposition of this technical instance?

## References

- ...
```

## References

- https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Onto/Synontic/Technique/
- https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Facet/Technical/Technology/
- Agency
- Problem
- https://plato.stanford.edu/entries/questions/
- Ontology
> `Mechanism` is to dynamics, what `program` is to  computation.
