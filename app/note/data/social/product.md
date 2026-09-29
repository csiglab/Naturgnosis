---
tags: [product, good, asset]
---

# Product

> A **Product** is the exchangeable outcome of production offered into a market: a good or service carrying value from a firm's portfolio to a buyer. Source: Produceologia `docs/Catalog/Product.md` and `docs/Catalog/Good/` (read-only import; the originals are untouched).

## Formulation

### What social element type does this social instance belong to?

**Product belongs to the `Price / Asset` social element type — a scalar coordination variable and claim-object: the product as priced, contracted, claimable offer.**

Its layer is **Synontic** under this reading: the offer exists through shared recognition of price, contract, and brand. Readable secondarily, as all market goods are, through its **Ontic** substrate — the physical good with materiality and lifecycle stage (cf. the markets-and-firms QA: Synontic coordinators over Ontic substrates). That substrate reading is prose, not a second root; the tree below is typed once. Its facet is economic.

### What is this social instance?

> A product fixes *what is exchanged*: the portfolio position, the deliverable offer, and the terms under which it changes hands. The Catalog distinguishes the generic product from concrete goods (Lemon, Cheese, Wine, …), each with its own production base and market.

### What is the recursive instance decomposition of this social instance?

> Boundary: one generic Product, decomposed at shallow depth — root plus the exemplar goods family only.
>
> Stopping rule: a row is terminal when it names the product or one exemplar good.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Price / Asset` → Product | Priced, contracted outcome of production offered into a market. |
| `Price / Asset` → Product → `Price / Asset` | Grouping: exemplar goods realizing the product family. |
| `Price / Asset` → Product → `Price / Asset` → Lemon | Citrus fruit good traded fresh and processed. |
| `Price / Asset` → Product → `Price / Asset` → Cheese | Dairy good traded fresh and aged. |
| `Price / Asset` → Product → `Price / Asset` → Wine | Fermented beverage good traded bottled and bulk. |

## References

- Produceologia `docs/Catalog/Product.md` and `docs/Catalog/Good/Agriculture/`
- Produceologia `docs/Firm/Toolkit/Product/` (MVP, lifecycle, strategy)
- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
