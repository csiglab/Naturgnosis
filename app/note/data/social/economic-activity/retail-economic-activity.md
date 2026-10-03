---
tags: [economic-activity, retail, economic, social-element]
---

# Retail Economic Activity

> Matching supply with demand — or somehow organizing supply — to deliver products at the minimal, and falling cost to consumers.

## QA

- How predictable is retail demand? How much of future demand can actually be predicted or forecast, under real-world retail conditions, and what determines the attainable level of accuracy?

## Index

## Operation

> How does a **retail firm - agent - operate**?

> How to decomposed the operation - or the task space?

- Distribution (How to get to the client?)
- …

## Problem Specification

| Problem | Fundamental question | Retail decision |
| --- | --- | --- |
| **1. Demand identification** | What do consumers want, where, when, and in what quantity? | Demand forecasting / market research |
| **2. Assortment** | Which products should be offered? | SKU selection, category mix |
| **3. Quantity / inventory** | How much of each product should be available? | Inventory levels, replenishment |
| **4. Location** | Where should supply be positioned relative to demand? | Store/network location, distribution centers |
| **5. Timing** | When should products be available? | Replenishment frequency, seasonal planning |
| **6. Pricing** | At what price can supply and demand be matched profitably? | Pricing, markdowns, promotions |
| **7. Procurement** | From whom and under what terms should products be obtained? | Supplier selection, contracts, purchasing |
| **8. Allocation** | How should available inventory be distributed across locations? | Store allocation, distribution |
| **9. Logistics** | How should products physically move from producers to consumers? | Transportation, warehousing, distribution |
| **10. Uncertainty** | How should the retailer deal with uncertain demand and supply? | Safety stock, flexibility, diversification |
| **11. Quality / condition** | How can the retailer ensure that the product reaching consumers has the required quality? | Quality control, cold chain, handling |
| **12. Coordination** | How should the retailer coordinate independent suppliers, logistics providers, stores, and consumers? | Supply-chain governance |
| **13. Information** | How can information about demand and supply be transmitted through the system? | POS data, forecasting, information systems |
| **14. Transaction costs** | Is it cheaper to perform an activity internally or through the market? | Make/buy, vertical integration |
| **15. Risk allocation** | Who bears the risk of unsold, damaged, obsolete, or unavailable inventory? | Contracts, ownership, guarantees |
| **16. Service level** | How much availability should the retailer provide? | In-stock rate, delivery speed |
| **17. Capacity** | How much retail, warehouse, and logistics capacity should be built? | Store size, DC capacity, labor |
| **18. Profitability** | Does the entire matching system create sufficient economic value? | Margin, inventory turnover, ROIC |

### Theoretical Formulation

> At its core, **retailing is the problem of allocating scarce resources to satisfy uncertain and heterogeneous consumer demand while maximizing long-term economic value**.

> **Given heterogeneous consumers, uncertain demand, scarce resources, competitors, multiple channels, and intertemporal decisions, what prices, products, inventory, locations, services, and channels should a retailer choose to maximize long-term economic value?**

> Let a retailer choose, over time, $a_t=(p_t,A_t,I_t,m_t,s_t,c_t,L_t)$
where $p$ is price, $A$ assortment, $I$ inventory, $m$ marketing, $s$ service, $c$ channel allocation, and $L$ location/network.

The retailer solves the dynamic optimization problem

$$
\boxed{
\max_{\{a_t\}}
E_0\left[
\sum_{t=0}^{T}\beta^t
\Pi_t(a_t,S_t,\theta_t)
\right]
}
$$

subject to

$$
\boxed{
D_{jt}
=
D_j(p_t,A_t,m_t,s_t,c_t,L_t,
X_t,Z_t,P_{-t},\theta_t,\varepsilon_t)
}
$$

$$
\boxed{
I_{j,t+1}
=
I_{jt}+O_{jt}-Q_{jt}
}
$$

$$
\boxed{
Q_{jt}\leq D_{jt},\qquad
Q_{jt}\leq I_{jt}+O_{jt}
}
$$

and the retailer's profit is

$$
\boxed{
\Pi_t
=
\sum_j(p_{jt}-w_{jt})Q_{jt}
-C_t(I_t,A_t,m_t,s_t,c_t,L_t)
}
$$

where \(w\) is acquisition cost and \(C\) includes operating, inventory, fulfillment, marketing, labor, occupancy, and other costs.

Demand itself emerges from consumer choice:

$$
\boxed{
U_{ijt}
=
V(X_j,Z_i,A_t,c_t,L_t,s_t)
-\alpha_i p_{jt}
+\varepsilon_{ijt}
}
$$

so that consumers choose the alternative that maximizes utility.

Because competing retailers affect prices, assortment, locations, and consumer demand, the retailer's optimization is embedded in a **strategic equilibrium**:

$$
\boxed{
a_r^*
\in
\arg\max_{a_r}
E[\Pi_r(a_r,a_{-r}^*)]
}
$$

Finally, because demand, preferences, competition, costs, and technology evolve through time, the complete problem is a **dynamic stochastic optimization and equilibrium problem**:

$$
\boxed{
V(S_t)=
\max_{a_t}
\left\{
\Pi(S_t,a_t)
+
\beta E[V(S_{t+1})\mid S_t,a_t]
\right\}.
}
$$

Thus, the **science of retail** can be summarized as:

$$
\boxed{
\text{Consumer Choice}
\rightarrow
\text{Demand}
\rightarrow
\text{Price \& Assortment}
\rightarrow
\text{Inventory \& Operations}
\rightarrow
\text{Channels \& Location}
\rightarrow
\text{Competition}
\rightarrow
\text{Profit}
\rightarrow
\text{Long-Term Firm Value}
}
$$

## QA

### Which are the keys results on the Retail Industry Literature?

| **8. Data/technology** | Retail operations research has increasingly moved toward data-driven optimization of assortment, fulfillment, and inventory as transaction-level data and computing capacity have expanded. (DOI) | Information becomes an operational input into the retail production system. |
| --- | --- | --- |
| Problem | Main research result | Why it matters |
| **Demand Forecasting** | Retail demand is forecastable, but accuracy depends strongly on aggregation, promotions, product life cycle, and information. Causal models generally outperform simple benchmarks; evidence for ML superiority is much less settled. (ScienceDirect) | The retailer can make money only if demand is sufficiently predictable to support purchasing, inventory, pricing, and replenishment. |
| **Inventory** | Inventory is not simply a cost: it simultaneously provides availability, service, assortment, and sometimes stimulates demand. (ScienceDirect) | The fundamental retail optimization is **availability vs. capital/holding cost vs. markdown/obsolescence risk**. |
| **Inventory Turnover** | Inventory turnover varies enormously across retailers and is systematically related to gross margins, capital intensity, and sales surprises. One empirical model explained 66.7% of within-firm variation and 97.2% of total variation. (PubsOnline) | Turnover cannot be evaluated independently of the retailer's margin and business model. |
| **Assortment** | Retailers face a genuine economies-of-scope problem: highly productive stores tend to offer more categories and sell more within those categories, while strong demand shocks can induce specialization in top-selling categories. (ScienceDirect) | The retailer is choosing **which products to carry**, not merely how many units to stock. |
| **Scale and Productivity** | There is evidence of increasing returns to scale in retail. More broadly, productivity growth can arise through the replacement of low-productivity establishments by more productive entrants. (ScienceDirect) | Scale, logistics, purchasing, technology, and store networks can create structural advantages. |
| **Retail Output** | Retail output is theoretically more complicated than sales. A retailer produces both **goods sold and distribution services**. Sales-based and margin-based measures capture different aspects of retail productivity. (Bureau of Labor Statistics) | This is crucial for understanding what a retailer actually *produces*. |
| **Omnichannel Fulfillment** | The store is increasingly a node in a fulfillment network, not merely a selling location. Research identifies network design, order assignment, assortment, inventory, forecasting, replenishment, and returns as interconnected problems. (ScienceDirect) | The modern retailer is simultaneously a **distribution network + inventory system + selling system**. |

### How is productivity measure in the retail industry?

> …
>

### What is the production funcion of retail?

> …
>

### What makes a retail firm more productive than other?

| Dimension | Description | Productivity Impact |
| --- | --- | --- |
| **Purchasing & procurement** | Ability to source products at low cost, negotiate favorable terms, and consolidate purchasing volumes. | **↑ Output per dollar of input** through lower COGS and better supplier terms. |
| **Demand forecasting** | Accuracy in predicting demand by product, location, time, and customer segment. | **↑ Sales and ↓ waste/stockouts** from better matching of supply with demand. |
| **Inventory management** | Determining how much inventory to hold, where to hold it, and when to replenish. | **↑ Inventory turnover; ↓ working capital and markdowns.** |
| **Assortment management** | Selecting the right products, categories, SKUs, pack sizes, and brands. | **↑ Sales per m² and per SKU** by allocating space to high-productivity products. |
| **Pricing** | Setting prices dynamically or strategically according to demand, competition, costs, and inventory. | **↑ Gross margin and revenue** from better price–volume trade-offs. |
| **Store operations** | Efficient receiving, shelving, replenishment, checkout, cleaning, and other store activities. | **↑ Sales per labor hour; ↓ operating cost per transaction.** |
| **Labor productivity** | Matching staffing levels and employee skills to customer traffic and workload. | **↑ Revenue per labor hour; ↓ idle labor.** |
| **Store format & layout** | Designing store size, location, layout, shelf configuration, and customer flow. | **↑ Sales per m² and ↓ cost per transaction.** |
| **Distribution & logistics** | Efficient movement of goods from suppliers → distribution centers → stores/customers. | **↓ Transportation, handling, and lead-time costs.** |
| **Supply-chain coordination** | Integration of procurement, inventory, distribution, stores, and suppliers. | **↓ Buffers and coordination costs; ↑ product availability.** |
| **Private-label capability** | Developing and sourcing retailer-owned products rather than relying entirely on national brands. | **↑ Gross margin and differentiation; potentially ↓ procurement cost.** |
| **Technology & information systems** | POS, ERP, inventory systems, forecasting, replenishment, pricing, and analytics. | **↑ Decision accuracy and ↓ information/coordination costs.** |
| **Data & analytics** | Using transaction, customer, inventory, and supplier data to improve decisions. | **↑ Revenue and margin per unit of resources.** |
| **Automation** | Automating checkout, replenishment, warehouses, ordering, pricing, and administrative activities. | **↓ Labor and transaction costs; ↑ throughput.** |
| **Supplier relationships** | Long-term relationships, information sharing, contracts, quality control, and supplier development. | **↓ transaction costs and supply uncertainty.** |
| **Economies of scale** | Spreading fixed costs and exploiting purchasing, distribution, technology, and advertising scale. | **↓ Average cost per unit/transaction.** |
| **Economies of density** | Concentrating stores and distribution operations geographically to exploit local infrastructure. | **↓ Logistics and operating costs per store.** |
| **Capital productivity** | Efficient use of stores, warehouses, equipment, refrigeration, IT, and other assets. | **↑ Sales and profit per dollar of invested capital.** |
| **Working-capital management** | Managing inventory, accounts payable, and cash conversion efficiently. | **↓ Capital required to generate a given level of sales.** |
| **Customer acquisition & retention** | Attracting customers and increasing visit frequency, basket size, and lifetime value. | **↑ Revenue generated from existing assets and customers.** |
| **Organizational design** | Effective division of decision rights between headquarters, regions, stores, distribution centers, and suppliers. | **↓ Coordination costs through aligned decision rights.** |

### What is the structure of the retail firm operation model space?

| Dimension | Description |
| --- | --- |
| **Customer interface** | How the firm interacts with customers: physical stores, e-commerce, marketplace, mobile, delivery, etc. |
| **Value proposition** | What the retailer competes on: price, assortment, convenience, quality, service, experience, speed, specialization, etc. |
| **Merchandising model** | How assortment, categories, SKUs, private labels, and product lifecycle are designed. |
| **Sourcing model** | How products are obtained: direct sourcing, wholesalers, distributors, manufacturers, farmers/producers, marketplaces, etc. |
| **Procurement model** | How suppliers are selected, negotiated with, contracted, ordered from, and evaluated. |
| **Pricing model** | How prices are established and changed: EDLP, high-low, dynamic pricing, algorithmic pricing, personalized pricing, etc. |
| **Demand-management model** | How demand is forecast, stimulated, measured, and translated into purchasing and replenishment decisions. |
| **Inventory model** | Where inventory is held, how much is held, and how inventory flows through the network. |
| **Replenishment model** | How products are reordered and allocated between suppliers, distribution centers, stores, and customers. |
| **Supply-chain architecture** | Structure of suppliers, distribution centers, transportation, warehouses, stores, and fulfillment nodes. |
| **Store operating model** | How stores are staffed, organized, supplied, maintained, and operated. |
| **Fulfillment model** | How online/offline orders are picked, packed, shipped, delivered, or collected. |
| **Labor model** | Workforce structure, staffing levels, scheduling, specialization, automation, and managerial hierarchy. |
| **Technology architecture** | POS, ERP, WMS, OMS, CRM, forecasting, pricing, AI, automation, and other technological capabilities. |
| **Information architecture** | How information flows between customers, stores, headquarters, suppliers, logistics, and management. |
| **Decision architecture** | Where decisions are made: headquarters, category managers, stores, algorithms, suppliers, etc. |
| **Coordination architecture** | Mechanisms used to coordinate independent activities across the retail system. |
| **Organizational structure** | Functional, geographic, category-based, product-based, matrix, decentralized, centralized, etc. |
| **Supplier relationship model** | Spot purchasing, negotiated contracts, long-term partnerships, vendor-managed inventory, strategic sourcing, etc. |
| **Capital model** | Ownership versus leasing of stores, warehouses, vehicles, technology, and other assets. |
| **Channel integration** | Degree to which stores, e-commerce, mobile, delivery, and other channels operate independently or as one system. |
| **Performance-management system** | Metrics, incentives, budgets, targets, and mechanisms used to control the organization. |
| **Economic model** | How the retailer converts its operating configuration into revenue, margin, cash flow, and return on capital. |

### What is the minimum number of non-business-model archetypes of leading retail firms that I should study to cover all possible configurations?

> Minimum archetype set = the smallest set of empirically observed configurations whose union spans the relevant dimensions of firm organization and operation, such that adding another leading firm does not introduce a substantively new configuration.
>

> Operating Model Dimension Combination: What makes this firms distinctive?
>

> Price Performnace: How much can this model lower the prices?
>

> Net Revenuew Performance: How much a firm with this model can make?
>

| Firm | Description | Operating Model Dimension Combination | Evolution | Price Performance | Net Revenue Performance |
| --- | --- | --- | --- | --- | --- |
| **Walmart** | Global mass retailer | **Scale + centralized procurement + broad assortment + standardized stores + integrated distribution + high-volume/low-margin operation** | Discount stores → supercenters → global supply-chain integration → omnichannel | **Very high** — scale and purchasing power support low prices | **Extremely high** — enormous transaction volume and broad market coverage |
| **Costco** | Membership warehouse retailer | **Membership + extremely limited assortment + bulk selling + warehouse format + low SKU complexity + high inventory turnover** | Price club → warehouse model → global expansion → omnichannel | **Extremely high** — low markup + membership economics + bulk purchasing | **Very high** — high sales per store and recurring membership revenue |
| **Amazon** | Digital commerce and fulfillment platform | **Digital interface + enormous assortment + marketplace + algorithmic decisions/pricing + distributed fulfillment + information-intensive operation** | E-commerce → marketplace → fulfillment network → omnichannel/ecosystem | **High** — enormous assortment, competition and scale can generate low prices | **Extremely high** — massive transaction volume + marketplace + ecosystem revenues |
| **Inditex** | Vertically coordinated fashion retailer | **Rapid product cycles + tight design/sourcing/production coordination + frequent replenishment + short demand-to-supply feedback loop** | Fashion retailer → fast-response system → integrated physical/digital model | **Medium–high** — efficiency comes primarily from reducing markdowns and inventory risk rather than lowest prices | **Very high** — high sales productivity and rapid inventory turnover |
| **IKEA** | Global furniture retailer | **Standardized global products + self-service + customer transport/assembly + large-format stores + global sourcing + low service intensity** | Catalog → warehouse-store → global standardized system → omnichannel | **High** — standardized products + customer participation + global sourcing reduce cost | **Very high** — global scale and high-volume standardized products |
| **TJX** | Off-price retailer | **Opportunistic procurement + unpredictable assortment + flexible buying + scarcity-based merchandising + low dependence on precise SKU forecasting** | Off-price buying → global sourcing network → increasingly digital operation | **High** — opportunistic purchasing allows substantial discounts | **Very high** — large store network + high inventory turnover + low merchandise acquisition costs |
| **7-Eleven** | Convenience-store network | **Small stores + localized assortment + high transaction frequency + frequent replenishment + franchise network + local demand adaptation** | Convenience stores → data-driven replenishment → digital ordering/services | **Low–medium** — convenience and location are prioritized over lowest price | **Very high** — enormous network + high transaction frequency |
| **Home Depot** | Home-improvement specialist | **Deep category assortment + large-format stores + supplier ecosystem + customer expertise + professional-customer orientation + interconnected fulfillment** | Warehouse retail → professional focus → interconnected omnichannel model | **Medium** — scale and category specialization support competitive prices, but assortment/service complexity raises costs | **Very high** — large baskets + professional customers + deep category penetration |
| **Mercado Libre** | Digital marketplace and commerce platform | **Third-party marketplace + platform governance + integrated payments + logistics infrastructure + network effects + digital information coordination** | Marketplace → payments → logistics → integrated commerce ecosystem | **High** — marketplace competition + scale + information efficiency | **Extremely high** — marketplace + payments + logistics + ecosystem revenues |

### How can we infer the degree of randomness in an observed data series when the underlying data-generating process is unknown?

- https://csrc.nist.gov/Projects/Random-Bit-Generation/Documentation-and-Software
- https://bitassay.com/

### How forecastable is demand? What are the different conditions that affect demand forecastability? How can the productivity of forecasting investments be measured?

> ….
>

### Which are the Retail Industry segments in `Demand`?

| **Demand Segment** | **Typical products** | **Demand Characteristics** |
| --- | --- | --- |
| **Grocery & Food** | Groceries, fresh food, beverages | **High frequency, predictable, low basket value, perishability** |
| **Convenience** | Convenience foods, tobacco, beverages, basic necessities | **Very frequent, immediate/urgent, location-sensitive** |
| **Apparel & Fashion** | Clothing, footwear, accessories | **Seasonal, trend-driven, highly variable, assortment-sensitive** |
| **Consumer Electronics** | Phones, computers, TVs, accessories | **Lower frequency, high value, technology/price sensitive, promotional** |
| **Home & Furniture** | Furniture, décor, mattresses, appliances | **Infrequent, high value, planned, bulky** |
| **Home Improvement & Building** | Hardware, tools, building materials, garden | **Project-driven, variable basket size, often bulky** |
| **Health & Personal Care** | Pharmacy, cosmetics, beauty, personal care | **Mixed: recurring necessities + discretionary purchases** |
| **Automotive** | Vehicles, parts, accessories, tires | **Very low frequency, high value, service/maintenance driven** |
| **Sporting, Hobby & Recreation** | Sports equipment, toys, games, books, musical instruments | **Discretionary, interest-driven, seasonal** |
| **Luxury & Specialty** | Jewelry, luxury goods, premium specialty products | **Very low frequency, high margin, experience/brand driven** |
| **General Merchandise** | Supercenters, department stores, warehouse clubs, dollar stores | **Broad heterogeneous demand; high basket breadth and substitution** |
| **E-commerce / Direct Retail** | Cross-category | **Demand is channel-mediated rather than product-specific: highly distributed, convenience-driven, delivery-sensitive** |

### Which are the the open theoretical problems in Retail?

| Theoretical Problem | Problem Description | Relevant Fields |
| --- | --- | --- |
| **Retail demand predictability** | What fundamentally determines the *forecastability* of retail demand, and is there a theoretical limit to how predictable a SKU–store–time series can be? | Forecasting, information theory, statistics |
| **Retail scale economies** | Why do some retailers obtain enormous cost advantages from scale while others exhibit diminishing or even negative returns to scale? | Industrial organization, operations |
| **Assortment complexity** | What is the theoretical relationship between assortment breadth, demand, inventory, substitution, and operating cost? | OR, consumer choice |
| **Inventory–variety trade-off** | Is there a fundamental law governing the amount of inventory required to provide a given level of product variety and availability? | Inventory theory |
| **Retail network optimality** | What is the optimal architecture of stores, warehouses, fulfillment centers and suppliers for a given spatial demand distribution? | Network optimization, geography |
| **Omnichannel equilibrium** | When should inventory be pooled across stores/channels versus dedicated to individual channels? | Operations, economics |
| **Retail price–service frontier** | Is there a fundamental frontier between price, availability, assortment, convenience and service speed? | Economics, operations |
| **Retail productivity** | What actually determines *retail productivity* at the store/SKU/process level, and why do apparently similar retailers have radically different productivity? | Productivity economics, operations |
| **Retail operating-model emergence** | Why do certain combinations of procurement, stores, logistics, technology and labor form stable high-performance configurations? | Strategy, organizational economics |
| **Retail format evolution** | Can retail formats be explained as solutions to changing cost structures and demand distributions rather than as business-model choices? | Evolutionary economics |
| **Substitution under stockouts** | How does consumer substitution propagate through an assortment, and what is the aggregate effect on demand forecasts and inventory? | Consumer choice, network theory |
| **Retail diseconomies of complexity** | Is there a measurable point at which additional SKUs, suppliers, stores, promotions or channels destroy more value than they create? | Complexity theory, operations |
| **Retail labor–automation frontier** | What determines the economically optimal division of retail work between humans, automation and customers themselves? | Labor economics, operations |
| **Information value in retail** | How much is better information actually worth when information changes decisions, prices, inventory and consumer behavior simultaneously? | Information economics |
| **Retail inventory pooling** | Under what structural conditions does pooling inventory create increasing returns, and when does localization dominate? | Probability, inventory theory |
| **Retail competitive advantage as an operating system** | Can persistent retail advantage be derived from the interaction of cost structure, demand density, process architecture and scale rather than from intangible "strategy"? | Strategy + operations |
| **Store location with endogenous demand** | How does competition between stores change the demand field itself, making conventional location models inadequate? | Spatial economics, game theory |
| **Retail labor–automation frontier** | What determines the economically optimal division of retail work between humans, automation and customers themselves? | Labor economics, operations |
| **Information value in retail** | How much is better information actually worth when information changes decisions, prices, inventory and consumer behavior simultaneously? | Information economics |
| **Retail inventory pooling** | Under what structural conditions does pooling inventory create increasing returns, and when does localization dominate? | Probability, inventory theory |
| **Retail competitive advantage as an operating system** | Can persistent retail advantage be derived from the interaction of cost structure, demand density, process architecture and scale rather than from intangible "strategy"? | Strategy + operations |

## References

- Agrawal, N., & Smith, S. A. (Eds.). (2009). *Retail supply chain management: Quantitative models and empirical studies*. Springer.
- Betancourt, R. R., & Gautschi, D. A. (1988). The economics of retail firms. *Managerial and Decision Economics, 9*(2), 133–144.
- Coelli, T. J., Rao, D. S. P., O'Donnell, C. J., & Battese, G. E. (2005). *An introduction to efficiency and productivity analysis* (2nd ed.). Springer.
- Foster, L., Haltiwanger, J., & Krizan, C. J. (2002). The link between aggregate and micro productivity growth: Evidence from retail trade (NBER Working Paper No. 9120). National Bureau of Economic Research.
- Higón, D. A., Muñoz, M. J., & Williams, A. M. (2010). The determinants of retail productivity: A critical review of the evidence. *International Journal of Management Reviews, 12*(2), 159–177.
- Keh, H. T., & Chu, S. (2003). Retail productivity and scale economies at the firm level: A DEA approach. *Omega, 31*(2), 75–82.
- Levy, M., & Grewal, D. (2026). *Retailing management* (11th ed.). McGraw Hill.
- Metcalfe, R. D., Sollaci, A., & Syverson, C. (2023). *Managers and productivity in retail* (NBER Working Paper No. 31192). National Bureau of Economic Research.
- Milgrom, P. R., & Roberts, J. (1992). *Economics, organization, and management*. Prentice Hall.
- Phillips, R. L. (2005). *Pricing and revenue optimization*. Stanford University Press.
- Shephard, R. W. (1970). *Theory of cost and production functions*. Princeton University Press.
- Simon, H. A. (1997). *Administrative behavior: A study of decision-making processes in administrative organizations* (4th ed.). Free Press.
- Talluri, K. T., & van Ryzin, G. J. (2004). *The theory and practice of revenue management*. Springer.
- Underhill, P. (2009). *Why we buy: The science of shopping*. Simon & Schuster.
- Varian, H. R. (1992). *Microeconomic analysis* (3rd ed.). W. W. Norton.
- Williamson, O. E. (1985). *The economic institutions of capitalism: Firms, markets, relational contracting*. Free Press.
- [Economic Activity](note.html?n=social/economic-activity/economic-activity.md)
- [Market](note.html?n=social/market/market.md)
- [Retail Supply–Demand Matching](note.html?n=technique/retail-supply-demand-matching.md)
- [Logistics System](note.html?n=technique/logistics-system.md)
- [Marketing Technical Practice](note.html?n=technique/systems/multinode/marketing-technical-practice.md)
- [Costco Wholesale Corporation](note.html?n=social/actor/firm/costco-wholesale-corporation.md)
- [Amazon.com, Inc.](note.html?n=social/actor/firm/amazon-com-inc.md)
- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
