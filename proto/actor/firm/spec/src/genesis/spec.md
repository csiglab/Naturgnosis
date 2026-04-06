# 1 Firm Genesis

> Representation of the **initial formation of the firm as an economic and organizational system**.

The Genesis section reconstructs the **initial state of the firm at the moment of formation**, including its founding event, factor endowment, technological base, strategic orientation, and institutional origins.

The goal is to explain:

* **why the firm emerged**
* **how it entered the economic system**
* **what resources and capabilities it possessed**
* **how it initially produced value**
* **what institutional ecosystem enabled its creation**

## Conceptual Structure

```text
Firm Genesis
│
├ Genesis Summary
├ Founding Event
├ Entry Mechanism
├ Founders
├ Founding Context
├ Initial Factor Configuration
├ Initial Production System
├ Initial Strategic Configuration
├ Initial Product Portfolio
├ Organizational Architecture
├ Capability Inheritance
├ Network Origin
└ Genesis Timeline
```

Each subsection represents a **distinct dimension of the firm's initial configuration**.

---

# 1 Genesis Summary

> Concise narrative overview of the firm’s creation.

This section synthesizes the founding story.

### Fields

* Founding Year
* Founding Date
* Founding Location
* Founders
* Initial Industry Domain
* Core Founding Idea
* Initial Strategic Intent

### LLM Generation Instructions

The summary should answer:

* What opportunity triggered the firm's creation?
* What capabilities existed at formation?
* What market problem was addressed?

### Example HTML

```html
<section class="firm-genesis-summary">

<h3>Genesis Overview</h3>

<p>
The firm was founded in <b>{Founding Year}</b> in <b>{Founding Location}</b> by 
<b>{Founders}</b>. The company was created to {initial strategic intent}.
</p>

<p>
At formation the firm focused on <b>{initial market}</b> using 
<b>{core technologies}</b>.
</p>

</section>
```

---

# 2 Founding Event

> Formal creation of the firm.

### Fields

| Field                  | Description               |
| ---------------------- | ------------------------- |
| Founding Year          | Year of formation         |
| Founding Date          | Exact date if available   |
| Founding Location      | City and country          |
| Legal Incorporation    | Legal entity created      |
| Initial Capitalization | Initial funding           |
| Initial Facilities     | Initial offices or plants |
| Initial Employees      | Early workforce           |

### UI Representation

Metadata panel.

```html
<div class="founding-metadata">

<table>
<tr><td>Founded</td><td>{Founding Date}</td></tr>
<tr><td>Location</td><td>{Founding Location}</td></tr>
<tr><td>Legal Form</td><td>{Legal Form}</td></tr>
<tr><td>Initial Capital</td><td>{Initial Capitalization}</td></tr>
</table>

</div>
```

---

# 3 Entry Mechanism

> Structural pathway through which the firm entered the economic system.

### Fields

| Field                 | Description                              |
| --------------------- | ---------------------------------------- |
| Entry Type            | Mechanism of formation                   |
| Precursor Entity      | Organization from which the firm emerged |
| Institutional Sponsor | State, corporation, university           |
| Entry Motivation      | Opportunity, restructuring, policy       |

### Entry Mechanism Taxonomy

| Entry Type                   | Description                        |
| ---------------------------- | ---------------------------------- |
| Entrepreneurial Startup      | New independent firm               |
| Corporate Spin-off           | Derived from existing company      |
| Research Spin-off            | Derived from research institution  |
| State Creation               | Created by government              |
| Privatization                | Former state enterprise privatized |
| Joint Venture                | Created by multiple organizations  |
| Corporate Division Formation | Division turned into firm          |

---

# 4 Founders

> Individuals or organizations that created the firm.

### Fields

| Field             | Description             |
| ----------------- | ----------------------- |
| Name              | Founder                 |
| Background        | Professional background |
| Prior Experience  | Relevant experience     |
| Role at Formation | Technical / managerial  |
| Ownership Stake   | Initial equity share    |

### Example HTML

```html
<div class="founder-card">

<h4>{Founder Name}</h4>

<ul>
<li><b>Background:</b> {Background}</li>
<li><b>Role:</b> {Role}</li>
<li><b>Equity:</b> {Ownership}</li>
</ul>

</div>
```

---

# 5 Founding Context

> Structural conditions that enabled the firm’s emergence.

### Fields

| Field                 | Description            |
| --------------------- | ---------------------- |
| Industry State        | Structure of industry  |
| Market Opportunity    | Opportunity exploited  |
| Technological Context | Available technologies |
| Institutional Context | Regulatory conditions  |
| Economic Context      | Macro environment      |

This section situates the firm within **its historical economic environment**.

---

# 6 Initial Factor Configuration

> Production inputs available at formation.

The section reconstructs the **initial economic endowment of the firm**.

### Factor Categories

```text
Factor Configuration
│
├ Capital
├ Labor
├ Knowledge
├ Physical Assets
└ Organizational Capital
```

### Fields

| Factor                 | Fields                        |
| ---------------------- | ----------------------------- |
| Capital                | Initial funding and investors |
| Labor                  | Workforce size and skills     |
| Knowledge              | Patents, know-how, expertise  |
| Physical Assets        | Facilities, equipment         |
| Organizational Capital | Processes, management systems |

### Example HTML

```html
<section class="factor-configuration">

<h3>Initial Factor Configuration</h3>

<ul>
<li><b>Capital:</b> {initial funding}</li>
<li><b>Labor:</b> {initial workforce}</li>
<li><b>Knowledge:</b> {technical knowledge}</li>
<li><b>Physical Assets:</b> {equipment}</li>
<li><b>Organizational Capital:</b> {management practices}</li>
</ul>

</section>
```

---

# 7 Initial Production System

> Technological system used to transform inputs into outputs.

### Components

```text
Production System
│
├ Production Function
├ Production Processes
├ Technology Stack
├ Production Scale
└ Production Facilities
```

### Fields

| Field                 | Description                        |
| --------------------- | ---------------------------------- |
| Production Function   | Input-output relationship          |
| Core Processes        | Manufacturing or service processes |
| Technology Stack      | Machinery, tools, software         |
| Production Scale      | Small batch / industrial           |
| Production Facilities | Locations                          |

### Analytical Representation

The production structure may be described conceptually as:

[
Q = f(K, L, T, A)
]

Where:

* **K** = capital
* **L** = labor
* **T** = technology
* **A** = organizational capability

---

# 8 Initial Strategic Configuration

> Intended competitive position at formation.

### Fields

| Field                | Description            |
| -------------------- | ---------------------- |
| Initial Mission      | Strategic intent       |
| Target Market        | Customer segment       |
| Value Proposition    | Customer value         |
| Competitive Strategy | Cost / differentiation |
| Geographic Focus     | Initial market region  |

---

# 9 Initial Product Portfolio

> Products or services initially offered.

### Fields

| Field              | Description            |
| ------------------ | ---------------------- |
| Product Categories | High-level categories  |
| Initial Products   | Specific offerings     |
| Product Function   | Product purpose        |
| Target Customers   | Customer segment       |
| Production Scale   | Early production scale |

### Example HTML

```html
<table class="initial-products">

<tr>
<th>Product</th>
<th>Category</th>
<th>Target Market</th>
</tr>

<tr>
<td>{Product}</td>
<td>{Category}</td>
<td>{Market}</td>
</tr>

</table>
```

---

# 10 Organizational Architecture

> Initial internal governance and structure.

### Fields

| Field               | Description               |
| ------------------- | ------------------------- |
| Governance Model    | Founder-led / board       |
| Leadership Roles    | CEO, CTO, etc             |
| Initial Departments | Engineering, sales        |
| Decision Structure  | Centralized / distributed |
| Workforce Size      | Initial employees         |

---

# 11 Capability Inheritance

> Capabilities inherited from pre-existing institutions.

Many firms inherit knowledge from prior organizations.

### Fields

| Field                  | Description                      |
| ---------------------- | -------------------------------- |
| Source Institution     | Institution providing capability |
| Capability Type        | Technical / managerial           |
| Transfer Mechanism     | Founder migration, licensing     |
| Capability Description | Knowledge transferred            |

Examples of sources:

* parent firms
* universities
* military programs
* industrial clusters

---

# 12 Network Origin

> Institutional ecosystem from which the firm emerged.

### Network Types

| Network Type               | Description                      |
| -------------------------- | -------------------------------- |
| University Ecosystem       | Academic research networks       |
| Military-Industrial System | Defense R&D ecosystem            |
| Industrial Cluster         | Regional manufacturing ecosystem |
| Corporate Ecosystem        | Large firm employee network      |
| Government Program         | State innovation programs        |

### Fields

| Field              | Description                   |
| ------------------ | ----------------------------- |
| Network Type       | Type of ecosystem             |
| Key Institutions   | Organizations involved        |
| Geographic Cluster | Region                        |
| Network Role       | Knowledge, funding, suppliers |

---

# 13 Genesis Timeline

> Events leading to the creation of the firm.

### Fields

| Time | Event                 |
| ---- | --------------------- |
| t-3  | Idea formation        |
| t-2  | Prototype development |
| t-1  | Funding acquisition   |
| t0   | Incorporation         |

### Example HTML

```html
<div class="timeline">

<div class="event">
<span class="year">t-1</span>
<p>{Event}</p>
</div>

</div>
```

---

# Internal Data Representation

Recommended structured format:

```json
{
  "firm_genesis": {

    "summary": {},
    "founding_event": {},

    "entry_mechanism": {},

    "founders": [],

    "founding_context": {},

    "factor_configuration": {
      "capital": {},
      "labor": {},
      "knowledge": {},
      "physical_assets": {},
      "organizational_capital": {}
    },

    "production_system": {},

    "initial_strategy": {},

    "initial_products": [],

    "organizational_architecture": {},

    "capability_inheritance": [],

    "network_origin": {},

    "timeline": []
  }
}
```