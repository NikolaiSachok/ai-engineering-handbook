---
id: overview
title: Agentic workflows
sidebar_position: 0
description: The scenario track for orchestration, tools, state, and the cost and quality tradeoffs that come with them.
---

# Agentic workflows

The first track, because it is what the postings ask for most. Across the requirement text this course
samples from, agentic orchestration is the single most frequent theme after "production, not demos" — and it
is where the three budgets that make these questions hard all meet: money, latency, and a notion of quality
that no single number reports.

Scenarios here share a shape. Something has to decide — which model, which tool, what to keep, when to stop —
and the decision is cheap to make and expensive to check. That asymmetry is the whole difficulty. A wrong
routing decision, a tool call retried against a non-idempotent endpoint, a memory that quietly went stale:
none of them raise an error. They return a plausible answer, and the system reports success.

## In this track

- **[Routing queries across models](/design-scenarios/agentic-workflows/model-routing)** — when a router
  earns its own latency and cost, and how you would know afterwards whether it did.
- **[Knowing an agent works](/design-scenarios/agentic-workflows/trajectory-vs-outcome)** — trajectory eval or
  outcome eval, when the outcome label lands two weeks late and a credit can buy it.
- **[Framework or your own primitives](/design-scenarios/agentic-workflows/framework-or-primitives)** — the
  LangGraph question, asked where the record you produce outlives the decision by a year.

Five more are being written: agent memory, tools that fail, guardrails at the boundary, observing a
non-deterministic system, and when not to build an agent at all.
