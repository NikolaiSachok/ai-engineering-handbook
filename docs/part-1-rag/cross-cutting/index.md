---
title: "Cross-cutting"
slug: /part-1-rag/cross-cutting/
---

# The concerns no single stage owns

Ingestion, retrieval and generation each have a place in the pipeline where they happen. Three
things do not. You cannot point at the step where a system becomes trustworthy, or safe, or
visible — those properties are either built into every stage or they are absent from all of them.
That is what makes these three concerns *cross-cutting* rather than a fourth, fifth and sixth stage.

They are also the three that separate a demo from a production system, which is why they come last
in Part I and get the most attention in interviews.

## What's inside

- **[Evaluation](./evaluation/index.md)** — how you know the system works, instead of believing it
  does. Retrieval and generation break in different ways and get fixed with different levers, so
  they are measured apart. This is the one to read first: without a number, every other change in
  the pipeline is a guess that feels better.
- **[Guardrails](./guardrails/index.md)** — how you keep it safe. A model cannot reliably tell
  instructions from data, so everything that reaches the context is something it may decide to
  obey. Guardrails are the layer on the input and on the output that assumes exactly that.
- **[Observability](./observability/index.md)** — how you see what it is doing once real users have
  it. Traces, spans and sampling turn "quality dropped" into "quality dropped *here*, starting
  *then*, because of *this* change" — and the failing traces it surfaces become new evaluation cases.

Each of the three is a lesson plus a **deep dive**: the lesson gives you the working model, the deep
dive takes one layer down into the mechanisms and the failure modes. Follow the "Next — part 2 of
the lesson" pointer at the foot of any lesson page.

The order is not arbitrary. Evaluation first, because guardrails and observability both produce
signals that are worthless if you have nothing to measure them against. Observability last, because
it closes the loop: what production breaks on becomes what evaluation tests next.
