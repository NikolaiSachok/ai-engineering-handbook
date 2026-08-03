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
  LangGraph question, asked where the record you produce outlives the decision by more than a year.
- **[What an agent should remember, and what it must not](/design-scenarios/agentic-workflows/agent-memory)** —
  persist, expire, never write; and what a workflow that has been running for eleven weeks is allowed to trust
  when it wakes.
- **[When an agent may try again](/design-scenarios/agentic-workflows/tools-that-fail)** — a nightly chain breaks
  at 03:12 with nobody awake; what the agent may retry, and what it may publish without a signature.
- **[What a document is allowed to do](/design-scenarios/agentic-workflows/guardrails-at-the-boundary)** — a
  supplier's PDF becomes a legally binding record; containment or detection, and which personal data the record
  is obliged to keep.

Two more are being written: observing a non-deterministic system, and when not to build an agent at all.
