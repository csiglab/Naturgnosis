---
tags: [public-organization, government, collective, actor, social-element]
---

# Public Organization

> A **Public Organization** is an organization wielding delegated public authority under law — the government subtype of [Organization](note.html?n=social/actor/organization.md), spanning ministries, arm's-length agencies, state-owned enterprises, municipalities, and public-private hybrids.

## Formulation

### What social element type does this social instance belong to?

**Public Organization belongs to the `Collective / Organization` social element type — a compound Interaction Unit with identity, membership, and rules, carrying its own agencies, roles, and practices.**

It is the government subtype of Organization: what individuates it is not its internal machinery (shared with every organization) but its constitutive relation to public authority — created or chartered under law, directed toward public purposes, and answerable through political oversight. Its layer is **Ontic**: ministries, agencies, and municipal bodies exist extra-mentally, with staff, premises, budgets, and address. Its facet is **political** — its dominant causal mechanism is authoritative rule-execution. Legal-instrument readings (statutes, charters) and economic readings (fees, commercial revenue) are prose here, not separate trees.

### What is this social instance?

> A public organization fixes *who exercises public authority and how*: the legal charter, the political principal to whom it answers, the agencies that form intention and select action, the internal governance stabilizing coordination, and the recurrent practices through which it serves, regulates, or trades. Canonical instances: ministry, public agency, state-owned enterprise, municipal organization, nonprofit public-private organization.

### What is the recursive instance decomposition of this social instance?

> Boundary: one generic Public Organization — direct subtypes plus the governance chain, at shallow depth. The full recursive expansion of the agency forms (statutory, incorporated-administrative, Swedish, UK executive) and of the Crown Corporation lives in the `Type` branch of [Organization](note.html?n=social/actor/organization.md) and is not duplicated here.
>
> Stopping rule: a row is terminal when it names a subtype, an agency, a role, a norm, an obligation, or a practice.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Collective / Organization` → Public Organization | Organization wielding delegated public authority under law. |
| `Collective / Organization` → Public Organization → `Type` | Grouping: direct subtypes of the public organization. |
| `Collective / Organization` → Public Organization → `Type` → Ministry | Central department of state directing a policy domain. |
| `Collective / Organization` → Public Organization → `Type` → Public Agency | Operational arm executing mandated functions at arm's length. |
| `Collective / Organization` → Public Organization → `Type` → State-Owned Enterprise | Commercial organization under controlling public ownership. |
| `Collective / Organization` → Public Organization → `Type` → Municipal Organization | Local organization governing a bounded territory and its services. |
| `Collective / Organization` → Public Organization → `Type` → Nonprofit Public–Private Organization | Mission-driven hybrid organization under mixed public-private control and funding. |
| `Collective / Organization` → Public Organization → `Agency` | Grouping: structured capacities forming intention and selecting action. |
| `Collective / Organization` → Public Organization → `Agency` → Governing Board | Structured capacity deciding direction and controlling execution. |
| `Collective / Organization` → Public Organization → `Institution` | Grouping: stabilized configurations of roles and rules hosted by the organization. |
| `Collective / Organization` → Public Organization → `Institution` → Internal Governance | Decision rights and coordination mechanisms: control, audit, and policy. |
| `Collective / Organization` → Public Organization → `Institution` → Internal Governance → `Social Role` | Grouping: expectation-tags binding members to conduct. |
| `Collective / Organization` → Public Organization → `Institution` → Internal Governance → `Social Role` → Membership Role | Expectation-tag binding a member, a context, and an interpretation to behavior. |
| `Collective / Organization` → Public Organization → `Institution` → Internal Governance → `Social Role` → Membership Role → `Norm / Regulation` | Grouping: shared protocols stabilizing member interaction. |
| `Collective / Organization` → Public Organization → `Institution` → Internal Governance → `Social Role` → Membership Role → `Norm / Regulation` → Membership Rule | Shared protocol stabilizing who may decide, contribute, and claim. |
| `Collective / Organization` → Public Organization → `Institution` → Internal Governance → `Social Role` → Membership Role → `Norm / Regulation` → Membership Rule → `Right / Obligation` | Grouping: deontic positions of the rule. |
| `Collective / Organization` → Public Organization → `Institution` → Internal Governance → `Social Role` → Membership Role → `Norm / Regulation` → Membership Rule → `Right / Obligation` → Duty of Public Service | Duty allocating lawful, impartial service to the public. |
| `Collective / Organization` → Public Organization → `Activity` | Grouping: bundles of situated doings. |
| `Collective / Organization` → Public Organization → `Activity` → Coordinating Activity | Coarse bundle reproducing the organization: meeting, reporting, rostering. |

## QA

### Which are the dimensions that make the government agency space?

Five dimensions jointly locate any government agency in the `Type` branch of [Organization](note.html?n=social/actor/organization.md):

| Category | Dimension | Description |
| --- | --- | --- |
| Legal constitution | Statutory basis | Own-act creation with legal personality (Autonomous Statutory Public Agency) vs. executive creation (UK Executive Agency, Swedish Government Agency) |
| Direction | Autonomy from ministerial direction | No individual ministerial rule, under collective government decision (Swedish); framework-document autonomy (UK); managerial autonomy within minister-set medium-term objectives (Japan IAA) |
| Control | Ownership and control | Wholly public vs. mixed public-private (Nonprofit Public–Private Organization) |
| Resourcing | Funding source | Budget appropriation, fees, or commercial revenue |
| Purpose | Function | Policy direction (Ministry), operation (Public Agency), or commercial enterprise (State-Owned Enterprise, Crown Corporation) |

### How do autonomous statutory, incorporated-administrative, executive-agency, Swedish-agency and crown-corporation forms differ?

> Along the five dimensions above: the **Autonomous Statutory Public Agency** draws autonomy from its own statute and legal personality; the **(Japan) Incorporated Administrative Agency** trades incorporation for bounded autonomy inside minister-set objectives; the **UK Executive Agency** trades a framework document for operational autonomy without separate legal personality; the **Swedish Government Agency** is constitutionally insulated from individual ministerial command while remaining under collective government direction; the **Crown Corporation** sits at the commercial pole — Crown-owned, board-governed, revenue-funded — bordering the Private Organization reading.

## References

- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- [Organization](note.html?n=social/actor/organization.md) (parent: the generic element type; carries the full recursive agency expansion)
- [Firm](note.html?n=social/actor/firm.md) (economic subtype of Organization)
- [Political Party](note.html?n=social/actor/political-party.md) (political subtype of Organization)
- [Market](note.html?n=social/market/market.md) (arena public organizations buy, employ, and regulate in)
- Graph nodes of the same names: `public-organization`, `organization`, `government-agencies`, `executive-agency`, `statutory-boards-and-councils` (Social Space, dataset `social`)
