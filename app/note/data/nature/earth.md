# Earth

> Earth read naturally: the inhabited rocky planet as an observer-independent system — interior,
> crust, ocean, atmosphere, and biosphere with their couplings — that remains when space
> programs, mining firms, states, and commodity prices are set aside. Parent instances
> [Nature](note.html?n=nature/nature.md) and
> [Natural Material](note.html?n=nature/natural-material.md); children
> [Natural Abiogenic](note.html?n=nature/earth-material.md) and
> [Natural Biogenic](note.html?n=nature/biogenic-material.md), composed in turn of
> [Mineral](note.html?n=nature/mineral.md) kinds. Worked per
> [How to decompose any natural instance?](note.html?n=meta/philosophia-naturalis-et-operis.md).

## Formulation

### What natural element type does this natural instance belong to?

`Natural System` at macro level of organization: a bounded segment (the planet and its
envelope) with interacting components (core, mantle, crust, ocean, atmosphere, biota),
inputs/outputs (solar influx, radiogenic heat, radiative loss, meteoritic input), and
feedback (plate — climate — weathering — biosphere loops). Complex-system behavior
(emergent climate regimes, biosphere regulation) is recorded as an ontic property of the
segment, not a second type on the same row.

### What is this natural instance?

**Earth**: the third planet of the solar system — an iron-cored, silicate-mantled, water- and
life-bearing rocky body with a nitrogen-oxygen atmosphere, liquid-water ocean, differentiated
interior, and active surface. The cut includes the body, its envelopes, and resident
organisms at macro scale with meso subsystems; it excludes launch systems and observatories
(technical reading), states, firms, and markets (social reading), and the models and
standards used to warrant claims about it (epistemic scaffolding) — those are secondary
readings (see below), each with its own tree.

### What is the recursive instance decomposition of this natural instance?

Instances are styled `**bold**`; bare grouping types `` `code` ``; every leaf resolves to a
natural instance; prefixes are valid paths (recursion rule).

| Instance Tree Path | Description | Natural Category | Natural Element Type Tree Path |
| --- | --- | --- | --- |
| **earth** | The planet system under study. | System | `(root) := Natural System` |
| **earth** > **inner core** | Solid iron-nickel sphere crystallizing at the center. | Constituent | `(root) := Natural System -> Natural Object` |
| **earth** > **outer core** | Liquid iron-nickel shell convecting around the inner core. | Constituent | `(root) := Natural System -> Natural Object` |
| **earth** > **mantle** | Convecting silicate shell driving plate motion. | Constituent | `(root) := Natural System -> Natural Object` |
| **earth** > **crust** | Thin differentiated shell of oceanic and continental rock. | Constituent | `(root) := Natural System -> Natural Object` |
| **earth** > **crust** > **limestone bed** | Recurring carbonate earth material worked into strata. | Constituent | `(root) := Natural System -> Natural Object -> Building Block` |
| **earth** > **crust** > **limestone bed** > **calcite** | Compositional mineral substance of the bed. | Constituent | `(root) := Natural System -> Natural Object -> Building Block -> Substance` |
| **earth** > **ocean** | Liquid-water hydrosphere with currents and chemistry. | System | `(root) := Natural System -> Natural System` |
| **earth** > **atmosphere** | Gaseous envelope with circulation and composition. | Constituent | `(root) := Natural System -> Natural Object` |
| **earth** > **biosphere** | The total living organization coupled to air, water, and rock. | System | `(root) := Natural System -> Ecosystem` |
| **earth** > **forest** | Terrestrial ecosystem; exemplar meso subsystem of the biosphere. | System | `(root) := Natural System -> Ecosystem` |
| **earth** > **cyanobacteria** | Self-maintaining oxygenic photoautotrophs; exemplar organisms. | Living | `(root) := Natural System -> Organism` |
| **earth** > **photosynthesis** | Biological transformation fixing carbon with light. | Living | `(root) := Natural System -> Living Process` |
| **earth** > **plate tectonics** | Causally continuous creation-destruction sequence of lithosphere. | Manifestation | `(root) := Natural System -> Natural Process` |
| **earth** > **plate tectonics** > **earthquake regime** | Unified explanatory object over rupture events. | Manifestation | `(root) := Natural System -> Natural Process -> Phenomenon` |
| **earth** > **hydrologic cycle** | Ordered state sequence of water through reservoirs. | Manifestation | `(root) := Natural System -> Natural Process -> Trajectory` |
| **earth** > **ocean chemistry state** | Snapshot configuration of salinity, pH, and dissolved load. | Manifestation | `(root) := Natural System -> Natural Process -> State` |
| **earth** > `Property` > **planetary mass** | Measurable attribute bounding gravity and escape. | Quantity | `(root) := Natural System -> Property` |
| **earth** > `Property` > **albedo** | Measurable reflectivity attribute bounding energy balance. | Quantity | `(root) := Natural System -> Property` |
| **earth** > `Constraint` > **surface gravity** | Scale-imposed bound on atmosphere retention and relief. | Constraint | `(root) := Natural System -> Natural Constraint` |
| **earth** > `Constraint` > **carrying capacity** | Scale-imposed bound on sustained biomass. | Constraint | `(root) := Natural System -> Natural Constraint` |

Limitation checklist (ontic properties of the segment, not method failures): Complexity
(coupled interior-surface-life systems), Nonlinearity (climate and rupture thresholds),
Uncertainty (deep interior and deep-time boundary conditions), Chaos (weather, turbulent
flow), Emergence (climate regimes, biosphere regulation), Scale (grain to planetary),
Data Availability (sparse deep-time proxies), Computational Complexity (coupled climate
ensembles), Irreducibility (turbulence, ecosystems), Partial Observability (interior,
deep ocean), Non-Repeatability (one planetary history), Many-Body coupling (fluids, plates,
biota). Measurement Disturbance applies only where the concrete observation shows it —
record per instance, do not assume.

Secondary readings (kept as prose, never merged into the tree above): readable as technique —
launch, sensing, drilling, and geoengineering methods (decompose under the technicarum
grammar); readable as social — states, firms, tenure, quotas, and markets drawn around the
planet and its resources (decompose under the socialium grammar; production-role nodes are
Social nodes tagged `production-view`); readable as epistemic — climate models, geodetic
standards, and stratigraphic scales (decompose under the epistemicarum grammar). The
instrument technically, the formation naturally
(`guideline/ambiguity_resolution.md`).

## References

- [Philosophia Naturalis et Operis](note.html?n=meta/philosophia-naturalis-et-operis.md) (workflow, schemas, Limitation checklist)
- [Philosophia Artium Epistemicarum et Operis](note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md) (presupposed definitions)
- Ambiguity Resolution (`guideline/ambiguity_resolution.md`) (multi-root forest rule)
- [Nature](note.html?n=nature/nature.md) (parent: all observer-independent reality)
- [Natural Material](note.html?n=nature/natural-material.md) (parent: all untransformed matter)
- [Natural Abiogenic](note.html?n=nature/earth-material.md) (child: all physical matter not made by life)
- [Natural Biogenic](note.html?n=nature/biogenic-material.md) (child: all matter made by life)
- [Quarry](note.html?n=nature/quarry.md) (worked instance: excavated rock mass)
