# Source bank — `part-1-rag/structured-knowledge/` (#405, #406, #407)

Every mechanism claim on the pair must trace to a row here. Checked **2026-08-03** against the primary
source, never against this handbook — the #374 precedent (our own page once asserted the error a verdict was
correcting). Locale renders consume this file too: a translator who needs to check a number reads this,
not the English page.

## Graph — #405

| Claim as it may be written | Source | Checked wording |
|---|---|---|
| The indexing pipeline runs six phases: TextUnits → Documents → Graph Extraction → Graph Augmentation → Community Summarization → Text Embedding | [GraphRAG dataflow](https://microsoft.github.io/graphrag/index/default_dataflow/) | phase names verbatim; TextUnits default 1200 tokens |
| Graph Extraction produces entities, relationships **and covariates** | ibid. | "Entities, Relationships, and Covariates tables" |
| Claim/covariate extraction is **off by default** | ibid. | "claim extraction is _optional_ and turned off by default… generally requires prompt tuning to be useful" |
| Communities come from the **Hierarchical Leiden** algorithm, recursively | ibid. | named explicitly |
| Community reports exist at multiple granularity levels; each carries an executive overview + key entities, relationships, claims | ibid. | quoted |
| **Local search** combines the extracted graph with raw text chunks; for questions about specific entities | [query overview](https://microsoft.github.io/graphrag/query/overview/) | quoted |
| **Global search** runs map-reduce over *all* community reports; for whole-corpus questions; "resource-intensive" | ibid. | quoted — the "resource-intensive" is the vendor's own word |
| **DRIFT search** folds community context into local search, refining a query into follow-up questions | ibid. | quoted |
| **Basic search** is plain vector RAG, shipped as the comparison baseline | ibid. | quoted |
| Conventional RAG "fails on global questions directed at an entire text corpus"; the win is comprehensiveness and diversity, at ~1M-token corpora | Edge et al., *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*, [arXiv:2404.16130](https://arxiv.org/abs/2404.16130) | abstract |
| **Full GraphRAG indexing costs ~1000× vector RAG** — LazyGraphRAG's indexing is "identical to vector RAG and 0.1% of the costs of full GraphRAG" | [LazyGraphRAG, Microsoft Research](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) | the vendor quantifying its own build cost — the strongest available sourcing for the cost criterion |
| Entity resolution in the popular systems is **string matching**: MS GraphRAG and LightRAG dedup by name, so aliases and abbreviations stay fragmented across nodes | *Less is More: Denoising Knowledge Graphs for RAG*, [arXiv:2510.14271](https://arxiv.org/html/2510.14271v1) | this is what makes "entity resolution is the unsolved middle" a sourced claim rather than an opinion |
| Edge hallucination is real: incorrect facts in the corpus yield erroneous triples in LLM-generated graphs | ibid. | |

**Do not write:** any first-person experience of running a production knowledge graph. The author has not
shipped one. Analysis is permitted; invented experience is not (#405 *Honesty constraint*).

## Schema — #406

| Claim | Source | Checked wording |
|---|---|---|
| SHACL is "a language for validating RDF graphs against a set of conditions… expressed in the form of an RDF graph" | [W3C SHACL](https://www.w3.org/TR/shacl/), Recommendation 2017-07-20 | opening definition |
| SHACL validates a **data graph** against a **shapes graph** and emits a **validation report** (`sh:ValidationReport`) | ibid. | |
| OWL 2 is "an ontology language for the Semantic Web with formally defined meaning" — the point is model-theoretic semantics and automated reasoning | [W3C OWL 2 Overview](https://www.w3.org/TR/owl2-overview/), Recommendation 2012-12-11 | |
| OWL 2 profiles trade expressivity for tractability: **EL** polynomial-time reasoning for very large ontologies, **QL** conjunctive queries in LogSpace over standard relational technology, **RL** polynomial-time rules over RDF triples | ibid. | the profiles are the honest answer to "is the formal stack expensive" — it was designed with that dial |
| SPARQL expresses "queries across diverse data sources, whether the data is stored natively as RDF or viewed as RDF via middleware"; a query is pattern matching over a directed labelled graph | [W3C SPARQL 1.1 Query](https://www.w3.org/TR/sparql11-query/), Recommendation 2013-03-21 | |

**Note the dates.** RDF/OWL/SPARQL/SHACL are stable 2012–2017 Recommendations. That is a *feature* to state
plainly — this is settled, interoperable ground, not a moving target — and it is also why the ecosystem
feels unfashionable next to the vector stack.

## Semantic layer — #407

| Claim | Source | Checked wording |
|---|---|---|
| The problem is metric inconsistency: "multiple analysts working on the same data, each using their own query method — this can lead to confusion, inconsistencies" | [dbt MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow) | |
| A semantic model carries **entities** (join keys), **dimensions** (how you slice) and **measures** (the quantities); a metric is defined once in YAML and queried across dimensions without rewriting SQL | ibid. | |
| Cube "centralizes metric definitions, joins, access rules, and caching upstream of every BI tool, application, and AI agent that queries the data" | [Cube docs](https://docs.cube.dev/docs/introduction) | |
| "Without one, agents writing SQL against a warehouse end up with inconsistent metrics and ungoverned access" | ibid. | the vendor making the agent argument directly |
| Every query "passes through the semantic layer runtime, where it's validated against the data model and has access policies applied **deterministically** before reaching the warehouse" | ibid. | the join to #409's access-control criterion, and to the deterministic-gate argument in `layered-gates` |
| Cube's **Meta API** exists so "AI agents discover what's queryable" | ibid. | |
| LookML is "the language that is used in Looker to create semantic data models"; analysts write it once, Looker's SQL generator translates user queries into database-specific SQL | [LookML](https://docs.cloud.google.com/looker/docs/what-is-lookml) | |
| **BIRD**: 12 751 question-SQL pairs, 95 databases, 33.4 GB, 37+ domains; **human 92.96%** vs **best model 81.95%** execution accuracy (both reported 2025-09-25) | [BIRD](https://bird-bench.github.io/) | the number that makes "selection instead of derivation" an argument rather than a preference — an eleven-point gap to a *human* on realistic schemas |
| BIRD's values "retain their original and frequently 'dirty' format", so a parser must handle non-standard values before reasoning | ibid. | why curated-benchmark text-to-SQL scores mislead |

**Leaderboard numbers move.** The two BIRD figures carry their as-of date on the page. Re-check before any
edit that touches them; do not quietly refresh one and leave the other.
