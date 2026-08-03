---
id: overview
title: Part I — RAG
sidebar_label: Part overview
---

# Part I — RAG

RAG (retrieval-augmented generation) is how you make an LLM answer from **your** documents rather than from
what it memorised in training. Before generating, the system finds the relevant pieces of your data and
puts them in the model's context. Part I works through this path as a **static pipeline**: a fixed sequence
of steps, the same for every query.

One diagnostic backbone runs through the whole part — **failure decomposition**. A bad answer comes in one
of two kinds: a *retrieval failure* (the piece you needed never made it into the results) or a *generation
failure* (the piece was retrieved, but the model ignored or garbled it). Almost every decision in the
pipeline addresses one of these two breakages, and the first move is always to tell which one you're
looking at.

## What's inside

- **[Ingestion](./ingestion/index.md)** — the offline preparation of documents: chunking and embeddings,
  metadata. This is where the ceiling on all of search quality gets set.
- **[Retrieval](./retrieval/index.md)** — how to turn "nearest vectors" into genuinely relevant results: query
  transformation, hybrid search, reranking, filters and access control.
- **[Generation](./generation/index.md)** — how to ground the answer in the retrieved context: grounding,
  citations, an honest refusal instead of invention.
- **[Structured knowledge](./structured-knowledge/index.md)** — what to do when the answer isn't in any
  passage: controlled vocabularies and ontologies, knowledge graphs, the semantic layer and text-to-SQL.
  And, for each, whether it's worth its build cost.
- **Cross-cutting concerns** — what doesn't reduce to a single step: [eval](./cross-cutting/evaluation/index.md)
  (knowing the system works), [guardrails](./cross-cutting/guardrails/index.md) (keeping it safe),
  [observability](./cross-cutting/observability/index.md) (seeing what it does in production).

## Prerequisites

General familiarity with LLMs: what a prompt, a context, and an embedding are at the level of the idea. No
deep math required — we explain from first principles.

:::note[Status]

Part I is complete — every lesson is published, and each carries its deep-dive second pass: Ingestion,
Retrieval, Generation, Structured knowledge, and the cross-cutting concerns (eval, guardrails,
observability). Follow the "Next — part 2 of the lesson" pointer on any lesson page to reach its deep dive.

:::
