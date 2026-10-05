#!/usr/bin/env python3
"""Two-level topic classifier for research nodes (metadata.topics).

Scores a node against the taxonomy documented in "Topics" in
``spec/research/README.md``: Level-1 domain first, then its Level-2
subfields. Evidence weights: work title x3, venue x2, prose body x1.
Venue priors for domain-specific venues; none from multidisciplinary
venues (Nature/Science/PNAS/arXiv) or general publishers. Generic words
(policy/model/system) count only with reinforcement.

Shared by ``bin/import_research.py``-style importers. Re-runnable; used
for references and documents that lack a notes body (body weight is then
simply unused).

Usage as a library::

    from topics import classify
    topics = classify(title="...", venue="...")
"""

import re
from collections import Counter

# venue regex -> [L1]; checked in order, first match wins the prior.
VENUE_PRIORS = [
    (r"neural information processing|icml|iclr|aaai|ijcai|jmlr|mach\.?\s*learn|machine learning|machine intelligence|artificial intelligence", ["artificial-intelligence"]),
    (r"comput\.?\s*linguist|computational linguistics", ["artificial-intelligence", "cognitive-science"]),
    (r"\bacm\b|ieee|usenix|black hat|defcon|nordsec|secure it|sosp|osdi|sigcomm|sigmod|vldb|sigmobile|computing|computer(?!.*psych)|software|operating systems|programming|functional programming", ["computer-science"]),
    (r"physical review|physics|astrophys|quantum|fluid mechanics", ["physics"]),
    (r"econometrica|american economic|quarterly journal of economics|journal of (political|monetary|labor|public|urban|international|financial|development) economics|econometric|finance|banking|elsevier.*economics|\beconom\w*|small business economics", ["economics"]),
    (r"economic histor|history of.*econom", ["economics", "history"]),
    (r"research policy|research.?technology management|technology management|technovation|management science|organization science|harvard business|strategic management|academy of management|administrative science|oper\.?\s*res", ["management", "economics"]),
    (r"cognition|cognitive|psycholog|american psychologist|linguist", ["psychology", "cognitive-science"]),
    (r"journal of.*business|business.*studies", ["management"]),
    (r"sociolog", ["sociology"]),
    (r"mathematic|siam|annals of|ann\.?\s*(appl\.?)?\s*probab|j\.?\s*am\.?\s*stat|american mathematical|statistics|biometrika|jasa|statistical science|formal logic|journal of.*logic", ["mathematics", "statistics"]),
    (r"cell\b|neuron|genetics|genomics|ecology|evolution|immunolog|plos|pnas|national academy", ["biology"]),
    (r"\bcomplexity\b", ["physics"]),
    (r"sociolog|social forces|american journal of sociology|social simulation|artificial societies|jasss", ["sociology"]),
    (r"political science|world politics|international organization|comparative politic|policy sciences|policy studies", ["political-science"]),
    (r"philosophy|journal of philosophy|philosophical", ["philosophy"]),
    (r"historical|history of|past & present|economic history", ["history"]),
    (r"asme|transactions on (automatic )?control|signal processing|power systems|bell system|bell labs|at&t", ["engineering"]),
]

# L1 -> title/body keywords (phrases preferred; single generic words flagged).
L1_KEYWORDS = {
    "artificial-intelligence": ["artificial intelligence", "neural network", "deep learning", "machine learning", "reinforcement learning", "transformer", "language model", "large language", "machine intelligence", "human feedback", "convolution", "agent", "ai", "computer vision", "robot", "motion planning", "knowledge representation", "expert system", "natural language", "generative model", "diffusion model", "foundation model", "random forest", "summarization", "text mining", "information extraction", "ant colony", "swarm intelligence", "layer normalization", "classification", "reasoning", "travelling salesman", "traveling salesman"],
    "archival-records": ["archival", "archive", "archives", "archivo", "manuscript", "manuscrit", "record", "records", "catalogue", "catalog", "fonds", "collection", "primary source", "signatura", "expediente", "legajo", "pares", "merit report", "merits and services", "meritos y servicios", "merits", "appointment", "nomination", "petition", "colonial", "indiferente", "capitulaciones", "informacion", "memorial"],
    "biology": ["biology", "cell", "genome", "genomic", "protein", "neuron", "neural coding", "cellular", "molecular", "metabolic", "bacteria", "biochemistry", "evolv", "ecolog", "species", "immune", "epidemic", "pandemic", "brain", "cortex", "synaptic", "mutation", "dna", "rna"],
    "cognitive-science": ["cognitive science", "cognition", "cognitive", "linguistic", "language", "syntactic", "thinking", "reasoning", "categorization", "syntax", "predictive processing", "embodied", "perception", "perceptual", "memory", "attention", "mental model", "conceptual", "embodied cognition"],
    "computer-science": ["computer science", "operating system", "database", "file system", "compiler", "computation", "computational", "scheme", "lisp", "haskell", "prolog", "libraries", "shared librar", "api", "paxos", "quorum", "software", "unix", "programming", "design pattern", "object oriented", "computer graphics", "rendering", "linux", "java", "binary", "git", "fpga", "verilog", "natural computing", "information system", "programming language", "distributed system", "consensus", "replication", "concurrency", "transaction", "cache", "scheduling", "virtualization", "network protocol", "routing", "congestion control", "software engineering", "formal verification", "type system", "garbage collection", "computer architecture", "processor", "cryptograph", "blockchain", "human computer", "information retrieval", "data mining", "stream processing", "query", "algorithm"],
    "economics": ["economic growth", "economi", "economy", "economies", "firm", "das kapital", "capital volume", "wealth of nations", "microeconomics", "diversification", "portfolio", "price", "commodit", "discrete choice", "theory of production", "growth", "cluster", "creative destruction", "trade", "wall street", "labor market", "unemployment", "inflation", "monetary", "fiscal", "game theory", "auction", "econometric", "development", "inequality", "income", "wage", "firm productivity", "industrial organization", "banking", "financial crisis", "foreign direct investment"],
    "engineering": ["finite element", "control system", "feedback control", "signal processing", "filter", "antenna", "power grid", "manufacturing", "supply chain", "materials science", "thermodynamics", "heat transfer", "mechanical engineer", "chemical engineer", "civil engineer", "circuit", "electronic", "robotics"],
    "history": ["history of", "history", "historia", "historical", "cold war", "industrial revolution", "nineteenth century", "twentieth century", "middle ages", "enlightenment"],
    "management": ["management", "innovation", "entrepreneurship", "business", "patent", "organization", "technological change", "industrial", "efficien", "information system", "system dynamics", "organizational", "strategy", "strategic", "operations management", "supply chain", "marketing", "leadership", "absorptive capacity", "dynamic capabilities", "firm performance", "corporate"],
    "mathematics": ["theorem", "probability", "tensor analysis", "real analysis", "inverse problem", "algebra", "topology", "stochastic", "markov", "graph theory", "combinatorics", "differential equation", "fourier", "optimization", "convex", "linear programming", "number theory", "cryptographic protocol"],
    "philosophy": ["philosophy", "scientific explanation", "justified true belief", "human nature", "epistemology", "ethics", "moral", "metaphysics", "causation", "pure reason", "speech act", "consciousness", "intentionality", "philosophy of", "phenomenology", "free will", "ontology"],
    "physics": ["physics", "quantum", "complex system", "complexity", "scale free", "power law", "zipf", "relativity", "thermodynamic", "heat", "entropy", "particle", "condensed matter", "superconduct", "astrophysics", "cosmology", "electromagnetism", "turbulence", "phase transition", "fluid", "field theory", "renormalization", "photon", "nano", "chemistry", "polymer", "physical chemistry", "organic chemistry", "quantum chemistry", "chemical physics"],
    "political-science": ["political science", "politics", "national security", "policy analysis", "democracy", "democratic", "voting", "election", "governance", "government", "authority", "corruption", "reason of state", "public policy", "policy", "authoritarian", "civil war", "international relations", "welfare state", "political party", "legislature", "federalism"],
    "psychology": ["psychology", "behavior", "behavioral", "emotion", "motivation", "personality", "psychopathology", "therapy", "attachment", "stereotype", "prejudice", "well-being", "psychological"],
    "sociology": ["sociology", "social network", "network society", "social capital", "social stratification", "urban", "sociedad", "culture", "cultural", "community", "migration", "urban sociology", "social movement", "norms"],
    "statistics": ["statistics", "statistical", "statistical inference", "randomness", "causal", "bayesian", "regression", "time series", "hypothesis testing", "experimental design", "causal inference", "sampling", "likelihood", "nonparametric"],
}

# L1 -> {L2: [keywords]}; venue hints give the L2 directly.
L2_KEYWORDS = {
    "artificial-intelligence": {
        "machine-learning": ["machine learning", "supervised", "unsupervised", "classification", "regression"],
        "deep-learning": ["deep learning", "neural network", "backpropagation", "convolutional", "recurrent"],
        "natural-language": ["natural language", "language model", "translation", "parsing", "semantics", "transformer"],
        "vision": ["computer vision", "image", "object detection", "segmentation"],
        "robotics": ["robot", "manipulation", "locomotion", "slam"],
        "reasoning-planning": ["reasoning", "planning", "search", "knowledge representation", "logic programming"],
        "multi-agent": ["multi agent", "agent based", "game", "mechanism design", "swarm"],
    },
    "archival-records": {
        "colonial-administration": ["colonial", "capitulaciones", "indiferente", "virreinato", "indias", "agencies", "agencia", "government", "administration", "governor", "gobernador"],
        "personnel-records": ["merits", "merits and services", "meritos y servicios", "merit report", "curriculum", "curriculum vitae", "service record", "appointment", "nomination", "petition", "expediente", "personal", "officer", "employee"],
        "manuscripts-and-petitions": ["manuscript", "manuscrito", "manuscrita", "petition", "peticion", "solicitud", "memorial", "informacion", "request"],
        "printed-and-published-materials": ["printed", "impresa", "manuscript", "certificate", "certificaciones", "autos", "legal", "law"],
    },
    "biology": {
        "genetics-genomics": ["genome", "genomic", "gene", "mutation", "dna", "rna"],
        "neuroscience": ["neuron", "brain", "cortex", "synaptic", "neural coding"],
        "ecology-evolution": ["ecolog", "evolution", "species", "population", "selection"],
        "cell-molecular": ["cellular", "cell ", "protein", "molecular", "signaling"],
        "epidemiology": ["epidemic", "pandemic", "transmission", "vaccine", "public health"],
        "bioinformatics": ["bioinformatics", "sequence alignment", "phylogenetic"],
    },
    "cognitive-science": {
        "perception": ["perception", "perceptual", "vision", "auditory"],
        "memory-learning": ["memory", "learning", "categorization", "concepts"],
        "decision-making": ["decision", "judgment", "choice", "rationality"],
        "language-cognition": ["language", "linguistic", "syntax", "acquisition"],
    },
    "computer-science": {
        "databases": ["database", "query", "transaction", "index", "sql", "storage engine"],
        "operating-systems": ["operating system", "kernel", "scheduling", "file system", "virtualization", "memory management"],
        "networks": ["network", "routing", "congestion", "protocol", "internet", "wireless", "datacenter"],
        "programming-languages": ["programming language", "compiler", "type system", "type variable", "design pattern", "object oriented", "semantics", "functional programming", "functional", "scheme", "lisp", "haskell", "prolog", "lambda calculus"],
        "distributed-systems": ["distributed", "consensus", "replication", "fault tolerance", "paxos", "blockchain"],
        "computer-architecture": ["architecture", "processor", "cache", "gpu", "accelerator"],
        "security": ["security", "cryptograph", "privacy", "attack", "authentication", "leak", "secret", "covert channel", "side channel"],
        "software-engineering": ["software engineering", "testing", "debugging", "refactoring", "version control"],
        "interaction-design": ["human-computer", "usability", "interface", "interaction"],
        "information-retrieval": ["information retrieval", "search engine", "ranking", "recommender", "data mining"],
    },
    "economics": {
        "growth-development": ["growth", "development", "convergence", "poverty"],
        "trade": ["trade", "tariff", "globalization", "exports"],
        "labor": ["labor", "wage", "unemployment", "employment", "human capital"],
        "finance": ["finance", "financial", "banking", "asset", "stock market", "credit"],
        "game-theory": ["game theory", "auction", "mechanism", "bargaining", "equilibrium"],
        "econometrics": ["econometric", "identification", "instrumental variable", "regression discontinuity"],
        "innovation-economics": ["innovation", "patent", "r&d", "technology diffusion", "productivity"],
    },
    "engineering": {
        "control-systems": ["control", "feedback", "stability", "pid"],
        "signal-processing": ["signal", "filter", "fourier", "sampling"],
        "power-energy": ["power", "grid", "energy", "battery"],
        "manufacturing": ["manufacturing", "production system", "quality control"],
        "materials": ["material", "alloy", "semiconductor", "nanotube"],
    },
    "history": {
        "history-of-science": ["history of science", "scientific revolution", "darwin"],
        "economic-history": ["economic history", "industrial revolution", "great depression"],
        "modern-history": ["cold war", "twentieth century", "world war"],
    },
    "management": {
        "innovation": ["innovation", "patent", "r&d", "disruptive", "diffusion"],
        "organization-theory": ["organization", "bureaucracy", "routines", "culture"],
        "strategy": ["strategy", "strategic", "competitive advantage", "diversification"],
        "entrepreneurship": ["entrepreneur", "startup", "venture", "new venture"],
        "operations": ["operations", "supply chain", "inventory", "queuing"],
        "marketing": ["marketing", "consumer", "brand", "advertising"],
    },
    "mathematics": {
        "algebra": ["algebra", "group theory", "ring"],
        "analysis": ["analysis", "differential equation", "fourier", "measure theory"],
        "geometry-topology": ["geometry", "topology", "manifold"],
        "probability": ["probability", "stochastic", "markov", "random"],
        "optimization": ["optimization", "convex", "linear programming", "gradient"],
        "logic-foundations": ["logic", "set theory", "computability", "proof theory"],
    },
    "philosophy": {
        "epistemology": ["epistemology", "knowledge", "justification", "skepticism"],
        "ethics": ["ethics", "moral", "normative", "justice"],
        "metaphysics": ["metaphysics", "ontology", "causation", "time"],
        "philosophy-of-science": ["philosophy of science", "explanation", "reduction", "realism"],
        "philosophy-of-mind": ["consciousness", "intentionality", "mind", "qualia"],
    },
    "physics": {
        "quantum": ["quantum", "entanglement", "qubit"],
        "relativity-cosmology": ["relativity", "cosmology", "black hole", "gravitational"],
        "thermodynamics-statistical": ["thermodynamic", "entropy", "statistical mechanics"],
        "condensed-matter": ["condensed matter", "superconduct", "phase transition", "crystal"],
        "fluid-dynamics": ["fluid", "turbulence", "navier", "flow"],
    },
    "political-science": {
        "democracy-elections": ["democracy", "democratic", "voting", "election"],
        "governance": ["governance", "bureaucracy", "public administration", "regulation"],
        "conflict": ["conflict", "civil war", "violence", "peace"],
        "political-economy": ["political economy", "redistribution", "welfare state", "interest group"],
    },
    "psychology": {
        "behavioral": ["behavior", "conditioning", "reinforcement"],
        "developmental": ["development", "child", "adolescent", "aging"],
        "social-psychology": ["social", "stereotype", "prejudice", "group", "conformity"],
        "clinical": ["disorder", "depression", "anxiety", "therapy", "trauma"],
    },
    "sociology": {
        "social-networks": ["social network", "ties", "centrality", "contagion"],
        "inequality": ["inequality", "stratification", "mobility", "class"],
        "institutions-culture": ["institution", "culture", "norms", "values"],
        "demography": ["migration", "fertility", "mortality", "population", "urban"],
    },
    "statistics": {
        "inference": ["inference", "hypothesis testing", "confidence", "likelihood"],
        "bayesian": ["bayesian", "prior", "posterior", "mcmc"],
        "time-series": ["time series", "forecasting", "longitudinal", "panel data"],
        "experimental-design": ["experiment", "randomized", "causal", "treatment effect"],
    },
}

# venue substring -> L2 (famous venues pin the subfield).
VENUE_L2 = [
    (r"sigmod|vldb|icde|pods", ("computer-science", "databases")),
    (r"sosp|osdi|eurosys|fast", ("computer-science", "operating-systems")),
    (r"sigcomm|nsdi|infocom|mobicom", ("computer-science", "networks")),
    (r"pldi|popl|icfp|oopsla", ("computer-science", "programming-languages")),
    (r"neurips|nips|icml|iclr|aaai|ijcai|jmlr|uai", ("artificial-intelligence", "machine-learning")),
    (r"acl|emnlp|naacl|coling", ("artificial-intelligence", "natural-language")),
    (r"comput\.?\s*linguist|computational linguistics", ("artificial-intelligence", "natural-language")),
    (r"cvpr|iccv|eccv", ("artificial-intelligence", "vision")),
    (r"rss|icra|iros", ("artificial-intelligence", "robotics")),
    (r"physical review letters|jhep|astrophysical", None),  # L1 only, no L2 pin
]

# generic single words: count only with reinforcement (venue prior or 2+ other hits).
RESTRICTED = {"policy", "policies", "model", "models", "modeling", "modelling",
              "system", "systems", "theory", "theories", "analysis", "study",
              "growth", "cluster", "clusters",
              "business", "causal", "prediction", "evolv",
              "government", "authority",
              "approach", "framework", "dynamics", "review"}

# exact (+plural) matching: suffix-tolerant would mis-fire (firm->firmware,
# trade->trademark). PREFIX matches word-start (nano->nanoelectronics).
EXACT = {"firm", "trade", "cell", "agent"}
PREFIX = {"nano"}

W_TITLE, W_VENUE, W_BODY = 3.0, 2.0, 1.0
L1_THRESH, L2_THRESH, MAX_TOPICS, MAX_L1 = 2.0, 2.0, 6, 2


def hits(score_text, keywords):
    found = []
    for kw in keywords:
        if " " in kw:
            if kw in score_text:
                found.append((kw, False))
        elif kw in RESTRICTED:
            if re.search(r"\b%s\b" % re.escape(kw), score_text):
                found.append((kw, True))
        elif kw in EXACT:
            if re.search(r"\b%ss?\b" % re.escape(kw), score_text):
                found.append((kw, False))
        elif kw in PREFIX:
            if re.search(r"\b%s\w*" % re.escape(kw), score_text):
                found.append((kw, False))
        elif len(kw) <= 4:
            # short tokens match exactly (gene must not fire on general)
            if re.search(r"\b%s\b" % re.escape(kw), score_text):
                found.append((kw, False))
        elif re.search(r"\b%s\w*\b" % re.escape(kw), score_text):
            found.append((kw, False))
    return found


def classify(title, venue="", body=""):
    """Return ordered [L1.., L2..] general -> specific. [] = unclassified."""
    v = re.sub(r"\\['`^\"~=.][a-z]|\\[{}&%$#_]|~", "", (venue or "").lower())
    v = re.sub(r"[{}]", "", v)
    t = (title or "").lower()
    b = (body or "").lower()
    # hyphens to spaces so 'nineteenth-century' matches 'nineteenth century'
    t, v, b = (s.replace("-", " ") for s in (t, v, b))

    l1_scores = Counter()
    l1_venue_prior = set()
    for pat, doms in VENUE_PRIORS:
        if re.search(pat, v, re.IGNORECASE):
            for dom in doms:
                l1_venue_prior.add(dom)
                l1_scores[dom] += W_VENUE
            break
    for l1, kws in L1_KEYWORDS.items():
        for kw, restricted in hits(t, kws):
            if not restricted or l1 in l1_venue_prior:
                l1_scores[l1] += W_TITLE
        for kw, restricted in hits(b, kws):
            if not restricted:
                l1_scores[l1] += W_BODY
        # venue text itself carries semantics (edited volumes, proceedings)
        for kw, restricted in hits(v, kws):
            if not restricted:
                l1_scores[l1] += W_VENUE
    # reinforcement: restricted title hits count when L1 already evidenced
    for l1, kws in L1_KEYWORDS.items():
        if l1_scores[l1] >= W_TITLE and l1 not in l1_venue_prior:
            for kw, restricted in hits(t, kws):
                if restricted:
                    l1_scores[l1] += W_TITLE * 0.5

    ranked_l1 = [l1 for l1, s in l1_scores.most_common() if s >= L1_THRESH][:MAX_L1]
    if not ranked_l1:
        return []

    topics, l2_seen = [], set()
    for l1 in ranked_l1:
        topics.append(l1)
    for l1 in ranked_l1:
        scored = Counter()
        for l2, kws in L2_KEYWORDS.get(l1, {}).items():
            for kw, _ in hits(t, kws):
                scored[l2] += W_TITLE
            for kw, _ in hits(v, kws):
                scored[l2] += W_VENUE * 0.5
            for kw, _ in hits(b, kws):
                scored[l2] += W_BODY
        for pat, pin in VENUE_L2:
            if pin and pin[0] == l1 and re.search(pat, v, re.IGNORECASE):
                scored[pin[1]] += W_VENUE
        for l2, s in scored.most_common():
            if s >= L2_THRESH and l2 not in l2_seen:
                topics.append(l2)
                l2_seen.add(l2)
    return topics[:MAX_TOPICS]