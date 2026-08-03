---
title: Structured knowledge
slug: /part-1-rag/structured-knowledge/
---

# When the answer isn't in any passage

Part I has assumed one thing on every page so far, and never said so out loud: that your knowledge arrives
as **prose**. Parse the documents, cut them into chunks, embed the chunks, search, rerank, generate. The
whole pipeline is built on a bet that somewhere in the corpus there is a passage which, once you find it,
contains the answer.

For a great deal of enterprise knowledge that bet is correct, which is why the pipeline is the default and
why it deserved three lessons. But three ordinary questions break it, and each breaks it differently:

- *"What are the recurring risks across our ten thousand contracts?"* — no chunk contains that answer. It
  isn't hiding in a passage you failed to retrieve; it was never written down.
- *"How much revenue did the enterprise segment do last quarter?"* — the answer is a number nobody has
  written either. It has to be computed, from a definition of "revenue" that two departments may not share.
- *"Everything we know about this supplier"* — the supplier appears under six spellings across four systems,
  and no amount of reranking makes those six things one thing.

Each one asks for knowledge that has **structure** — entities, relations, definitions — and each has a
mature answer that is not a vector index. This lesson covers all three, and dwells mostly on when they are
worth building — because each is heavily marketed and each is frequently the wrong call.

:::note[Read the section you need]

The three main sections stand alone and there is no reading order between them. If you are deciding whether
to extract structure at all, start with [the three kinds of structure](#three-kinds-of-structure) —
vocabulary, taxonomy, ontology. If someone has asked for a knowledge graph, go to
[when a graph earns its build cost](#when-a-graph-earns-its-build-cost).
If the question is about numbers and dashboards, go to [the semantic layer](#the-semantic-layer-names-two-different-things).
The [closing section](#which-of-the-three-you-actually-need) is the decision that connects them.

:::

## Three kinds of structure, and the cheapest one usually wins \{#three-kinds-of-structure}

Three things get called by each other's names constantly, and separating them removes most of the
confusion.

| | What it is | What it buys you |
|---|---|---|
| **Controlled vocabulary** | a fixed list of allowed terms | an extractor stops inventing labels |
| **Taxonomy** | a hierarchy over those terms | roll-up, inheritance, broader/narrower queries |
| **Ontology** | classes, properties, and constraints between them | validation, and inference of facts nobody stated |

**Most teams that say they need an ontology need a controlled vocabulary.** Say it to a stakeholder early,
because the gap between those two artefacts is roughly the gap between an afternoon and a permanent
staffing commitment.

The failure a controlled vocabulary fixes is the most familiar one in structured extraction. You ask a model
to pull relationships out of three thousand documents. It does, fluently. In one document a person
`works_for` a company; in the next they are `employed_by` it; in the third the relation comes back as
`is_employee_of`. Nothing downstream can join those, because as far as any query is concerned they are three
unrelated predicates. The model was not wrong in any single document — it was unconstrained across all of
them. Hand it a closed list of permitted relation types and the problem disappears — for the cost of writing
the list.

### Where a schema actually bites

Schema discipline pays in three separable places. Know which one you are buying:

**Extraction.** Give the model the class and property set up front and it stops inventing. This is the
`works_for` problem above, and it is where the cheapest structure returns the most.

**Validation.** A constraint layer can reject an extracted assertion that violates the schema — an employment
edge pointing at a document instead of an organisation, a date outside a permitted range. That is a
deterministic gate sitting over a probabilistic producer, which is exactly the shape the AI SDLC course
argues for in [layered gates and mechanism diversity](/ai-sdlc/part-3-verification/layered-gates).
A schema is what makes such a gate *possible* at all, because a gate needs something to check against.

**Query.** If you want to resolve a question to a concept rather than to a passage, you need a model of the
concepts. That is the [semantic layer](#the-semantic-layer-names-two-different-things) in its second sense,
and the domain model is the artefact it resolves against.

### Domain schema is not response schema

You have already met a JSON Schema in this handbook, constraining the *shape of a model's reply* —
required fields, permitted enum values, a parse that either succeeds or fails. An ontology constrains the
*shape of the world the reply talks about*.

They look similar on the page and they are entirely different artefacts. A response schema belongs to a
prompt, changes when the prompt changes, and is owned by whoever owns that feature. A domain model belongs
to the organisation, changes when the business changes, and outlives every prompt that ever read it. Treat
one as the other and you end up with your domain model versioned alongside a prompt template, which is how
a company discovers that its definition of "customer" was altered by a copy edit.

### The honest default, and the test for leaving it

For most LLM systems, a JSON Schema plus a validator delivers the working benefit at a fraction of the
cost: a closed set of types and a rejection path. That is not a lesser option to apologise for; it is the
right answer most of the time. The [formal stack](./deep-dive.md#the-formal-stack-by-purpose) — RDF, OWL,
SHACL, SPARQL — earns its weight under conditions you can name: you need to derive facts nobody stated, you
must interoperate with a standard vocabulary that already exists in your industry, or a regulator has
specified the schema and conformance is not optional.

Two costs decide it, and neither appears on a vendor slide. The first is that an ontology is maintained by
people, indefinitely, and the maintenance is judgement work rather than a job you can schedule. The second
is sharper: *a wrong ontology is worse than none.* A missing schema lets an extractor produce a mess that
looks like a mess. A wrong schema forces the extractor to mis-file, and mis-filed data looks *clean* — it
validates, it joins, it renders in a dashboard, and it is wrong in a way that no downstream check is
positioned to notice.

So the test for adding structure is not whether the structure would be tidier. It is: *can you name a query
you cannot answer today that this structure would answer?* If not, you are building for tidiness, and
tidiness does not survive its first maintenance handover.

## When a knowledge graph earns its build cost \{#when-a-graph-earns-its-build-cost}

A knowledge graph stores entities as nodes and the relations between them as edges, extracted from your
corpus by a model or curated by hand; **GraphRAG** is retrieval over such a graph, and as a proper noun it is
Microsoft's reference implementation. Start from what you can already do, because the usual opening claim for
knowledge graphs — that they solve multi-hop questions — is answered better and more cheaply elsewhere in
this course.

*"Who leads the department that issued policy X?"* looks like it needs a graph traversal. It doesn't.
Decompose it into two ordinary retrievals — find the department that issued X, then find who leads it — and
the static pipeline you already have answers it. That is [agentic RAG](../../part-2-agents/agentic-rag/index.md),
and it needs no extraction pass, no schema and no maintenance. If a graph proposal's headline benefit is
multi-hop, the proposal has not yet found its reason.

The reason exists, and it is a different question class.

### Three question classes, and only one of them is decisive

**Local — the entity neighbourhood.** *"What do we know about this supplier and what is it connected to?"*
A graph helps here. So does decomposition, and so does a well-filtered vector search over documents tagged
with the supplier. The win is modest, and it is not what justifies the machinery.

**Global — the whole corpus.** *"What themes recur across these ten thousand documents?"* *"Which risks
appear in more than one contract family?"* No retrieval over chunks can answer this. Retrieval assumes the
answer exists in the corpus and your job is to locate it; here there is no chunk to locate. The answer is a
*summary of the corpus*, and it has to be constructed before anyone asks. This is the case that justifies
the build. It is also what the GraphRAG paper is about — conventional RAG, its authors argue, "fails on
global questions directed at an entire text corpus"
([Edge et al., *From Local to Global*](https://arxiv.org/abs/2404.16130)).

**Entity disambiguation across sources.** The same organisation as `Acme Corp`, `Acme Corporation`,
`ACME Corp.`, and a misspelling. A graph is where this problem becomes visible — and where graph work
quietly turns into [entity-resolution work](./deep-dive.md#entity-resolution), a different discipline with a
different budget.

### The costs are decision criteria, not caveats

**Extraction is an LLM pass over your entire corpus**, so it is priced like one. The clearest available
figure comes from Microsoft Research's own follow-up work:
[LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)
was built specifically to avoid the up-front indexing cost of a full build, and its indexing is reported as
"identical to vector RAG and 0.1% of the costs of full GraphRAG". Read that backwards and it says the full
build is on the order of a thousand times the cost of simply embedding the same corpus. That is a number to
put in a proposal.

**The extraction hallucinates edges.** A relation the model inferred but no document states will sit in the
graph looking exactly like one that was stated. Incorrect facts in a corpus yield erroneous triples in an
LLM-generated graph, as [*Less is More: Denoising Knowledge Graphs for
RAG*](https://arxiv.org/html/2510.14271v1) documents while surveying how the popular systems handle
extraction noise. The vector path has no equivalent failure: a retrieved chunk is a chunk that exists.

**The graph goes stale like any derived artefact.** Incremental update on a changing corpus is the genuinely
hard part, and it is the same argument this handbook already makes about frozen model weights — see
[LLMOps](../../part-3-production/llmops/deep-dive.md). A graph built once and never rebuilt is a snapshot
that degrades from the day it is finished.

**Evaluating a graph is not evaluating retrieval.** Recall@K over chunks tells you nothing about whether the
extracted relations are *true*. You need extraction precision against a labelled sample, and end-to-end
answer evaluation on the question types only the graph can serve. The [evaluation
lesson](../cross-cutting/evaluation/index.md) has the machinery; the deep dive has the specifics.

### When not to build a graph

Small corpus. Lookup-shaped questions. Data that changes faster than you can re-extract. And the one that
decides it in practice: nobody has committed to keeping the extraction schema correct. Without that owner,
the failure will be blamed on the technology rather than on the staffing decision that caused it.

The normal production shape, when a graph is justified at all, is not graph instead of vectors. It is
vectors for lookup, the graph for structure, and a router deciding which question goes where — the same
routing machinery the [retrieval deep dive](../retrieval/deep-dive.md) already builds.

## The semantic layer names two different things \{#the-semantic-layer-names-two-different-things}

This phrase earns its place in the lesson mostly because it names two different things, and enterprise
conversations slide between them without anyone noticing. Both are real.

**The metrics layer.** A modelling tier over a warehouse — dbt's Semantic Layer, Cube, LookML and their
relatives — where a metric is defined *once*: what "revenue" means, which joins it implies, which filters
are legal, which dimensions it can be cut by. Every consumer then asks for the metric instead of
reconstructing it in SQL. [dbt](https://docs.getdbt.com/docs/build/about-metricflow) describes the problem
it solves as "multiple analysts working on the same data, each using their own query method", which leads to
"confusion, inconsistencies, and a headache for data management".

**The semantic layer over the linguistic layer.** In conversational AI: the assistant resolves an
utterance to a **domain concept** — an entity, a relation, an intent — rather than to a passage of text. The
answer is then produced against the domain model rather than against whatever the retriever happened to
return.

They are related, in that both replace ad-hoc interpretation with a shared model. They are not the same
layer, do not share tooling, and are usually owned by different teams. Say which one you mean in the first
sentence and the rest of the conversation gets easier.

### Text-to-SQL: selection instead of derivation

The practical payload belongs to the metrics layer, and it is the clearest case in this lesson of structure
changing how hard a problem is.

A vector top-K cannot count. Aggregate questions — sums, ratios, "how many", "compared to last quarter" —
need a structured path beside the semantic one. The obvious way to build that path is to let a model write
SQL against your warehouse. Pointed at a raw schema, the model has to **derive** the whole query: infer the
joins, guess which of four date columns is the business date, handle values that come in whatever format the
source system left them in. [BIRD](https://bird-bench.github.io/) is a benchmark built specifically around
large, realistic, messy databases, where values "retain their original and frequently 'dirty' format". On
it, human data engineers reach 92.96% execution accuracy while the leading system reaches 81.95% (both as
reported on the leaderboard, September 2025). Nearly one query in five is wrong on realistic schemas,
and a wrong SQL query does not announce itself — it returns a number.

Point the same model at a semantic layer and its job changes. It no longer derives a query; it *selects* a
defined metric and a set of dimensions. That is a far smaller decision, drawn from a closed list, and its
failure mode changes with it: a wrong *selection* instead of a wrong *derivation*. A wrong selection is
detectable — you can show which metric was chosen — whereas a subtly wrong join is not.
[Cube](https://docs.cube.dev/docs/introduction) makes this argument for agents directly: without a semantic
layer, "agents writing SQL against a warehouse end up with inconsistent metrics and ungoverned access".

The layer buys a second thing, and it matters more than it sounds. Because every query passes through it,
the enforcement point moves — Cube's phrasing is that a query "is validated against the data model and has
access policies applied deterministically before reaching the warehouse". That is the same principle the
retrieval deep dive insists on — [cut before the search, never
post-filter](../retrieval/deep-dive.md) — arriving from the structured side.

### Why enterprises want answers resolved to concepts

Resolving to a concept buys two things a passage citation does not. **Consistency**: the same question
phrased two ways reaches the same concept, and therefore the same answer. **Auditability**: you can show
*which* concept was resolved and why. A citation tells you which text the model read; it does not tell you
what the model took that text to mean.

This is where two of this lesson's three sections meet: the domain model being resolved against is exactly
[the ontology](#three-kinds-of-structure) — which is why "we need an ontology" and "we need a
semantic layer" are so often the same request arriving from two departments.

### What a semantic layer costs, and when to skip it

A semantic layer is a definition negotiation before it is a technical artefact, and the negotiation is the
expensive part. Two departments that define "active customer" differently must stop, and someone with
authority has to decide. The modelling is a week; the agreement can take a quarter. Then definitions drift,
so someone owns them permanently. A metric that silently changes meaning is worse than no metric, for the
same reason a wrong ontology is worse than none.

**When not to:** one team, a handful of metrics, no cross-department disagreement about definitions. Then
the layer is ceremony and a well-documented set of views does the job. The test is concrete — *have two
people ever produced different numbers for the same question?* If not, there is nothing to reconcile yet,
and you would be buying governance for a conflict you do not have.

## Vocabulary, graph or semantic layer: which you actually need \{#which-of-the-three-you-actually-need}

The three sections are three answers to one question: *where does the structure in your knowledge live,
and who maintains it?*

- If your extractor is inventing labels, you need a **controlled vocabulary**, and you need it this week.
- If your questions are about the corpus as a whole rather than about anything in it, you need a
  **graph** — and an owner for its schema, or you need neither.
- If your questions are arithmetic and two people disagree about the arithmetic, you need a **semantic
  layer**, and the hard part is the disagreement, not the modelling.
- If none of those describe you, the Ingestion → Retrieval → Generation pipeline is the right architecture
  and the structured detour is a cost with no return.

Ontology, graph and semantic layer share one failure mode: each fails silently and plausibly. A wrong
ontology validates. A stale graph returns confident relations. A drifted metric renders in a dashboard.
None of them throws. Every one of them needs a named owner and a check that would catch it.

## What to take away

- Part I's pipeline assumes the answer exists in some passage; three question classes break that assumption,
  and each has a different structural answer.
- Controlled vocabulary, taxonomy and ontology are three different commitments — most requests for an
  ontology are satisfied by a controlled vocabulary, and the test for going further is naming a query you
  cannot answer today.
- A JSON Schema plus a validator is the honest default; the formal stack earns its cost on inference,
  standards interoperability and regulated conformance.
- A domain schema is not a response schema: different owners, different change rates, and treating them as
  one puts your business definitions inside a prompt.
- Graphs are not justified by multi-hop questions, which decomposition already answers; they are justified by
  global, corpus-level questions where no chunk contains the answer at all.
- The graph build is an LLM pass over the whole corpus, it can hallucinate edges, and it goes stale — but
  the decider in practice is whether anyone owns the extraction schema.
- "Semantic layer" names both a metrics tier over a warehouse and concept resolution in conversation; say
  which you mean first.
- Against a semantic layer a model selects a defined metric instead of deriving a query. That shrinks the
  decision, turns the failure into a visible one, and lets access policies apply before the warehouse is
  touched.

**[New terms](../../glossary.md#structured-knowledge)**: controlled vocabulary, taxonomy, ontology, RDF,
OWL 2, SHACL, SPARQL, knowledge graph, GraphRAG, entity resolution, semantic layer, metrics layer,
text-to-SQL.

---

:::note[Next — part 2 of the lesson]

**[Extraction, schemas & the query surface](./deep-dive.md)** — how a graph is actually built (the six
indexing phases, hierarchical Leiden communities, and the four query methods), why entity resolution is the
part that disappoints, how to evaluate a graph when retrieval metrics don't apply, the formal stack
explained by purpose, and what text-to-SQL gets wrong that a semantic layer removes.

See also: where the chunks come from — [Ingestion](../ingestion/index.md); the routing machinery this lesson
reuses — the [Retrieval deep dive](../retrieval/deep-dive.md); multi-hop without a graph —
[Agentic RAG](../../part-2-agents/agentic-rag/index.md).

:::
