---
id: overview
title: Part V — Scale & Governance
sidebar_label: Part overview
---

# Part V — Scale & Governance

Everything so far described one stream of work: a loop, a chain of gates, and a platform under it. Part V asks
what breaks when you run many at once — and the answer is four ceilings, none of which is compute.

**Sharing** is the first. Agents parallelise only across state they do not share, and the classic collision is
banal: one working tree has one checked-out branch, so two agents building two branches in it fail by
construction. The fix is to remove the sharing, not to coordinate access to it. **Decay** is the second: rules
and project memory encode a codebase that keeps moving, and a stale rule is worse than no rule, because where
a human shrugs at an obsolete convention an agent complies with it. **Cost** is third, and it is a denominator
problem before it is a spending one — the unit is cost per *accepted* change, with retries, verification
calls, and human review time in the numerator. And **proof** is the fourth: the enterprise tier that has
closed every lesson in this course finally becomes the subject, and the finding is that its mechanisms are
usually not stronger, only demonstrable.

The through-line is Part I's, arriving in different currencies. Doubling the agents doubles the output and
the review queue — but the capacity to work that queue, the gate chain and the human router, does not double
with them. Every ceiling here is that one constraint, priced differently.

## What's inside

- **[Running agent fleets: isolation and parallelism](./agent-fleets.md)** — what is shared is what
  serialises. Isolate the workspace, keep the accretive artefacts serial, and size the fleet to what the
  verification chain can absorb.
- **[Drift control and rule rot](./drift-and-rot.md)** — staleness, contradiction, bloat. Executable rules
  rot loudly; prose rules rot in silence and keep being obeyed.
- **[Cost and the economics of agent work](./cost-economics/index.md)** — cost per accepted change, not per
  token. Context is the line item people forget, and human review is the input that does not scale with spend.
- **[The enterprise tier: audit, provenance, and what's required](./enterprise-tier/index.md)** — the closing
  lesson: non-repudiation, provenance that names the agent and model, and separation of duties when both
  parties are agents.

## Prerequisites

Part I's **verification bottleneck**, read as a claim about *capacity* rather than about quality — the first
lesson here caps fleet size with it directly. Then Part I's *Project memory* and *Rules that hold*, because
the second lesson is entirely about what becomes of both once the code moves out from under them. The cost
lesson prices Part III's semantic gates and Part IV's per-task credentials, and the closing lesson assumes
Part III's separation-of-duties argument.

## What changes after this part

You can size a fleet to what the chain absorbs rather than to the budget, and say which fraction of the work
is irreducibly serial. You can put a bill on a rules corpus instead of only a quality complaint. And you can
tell an enterprise control that exists for **capability** from one that exists for **proof** — which is the
distinction that lets you argue for the first and stop dismissing the second as ceremony.

:::note[Status]

Part V is complete — all four lessons are published, and it closes the course. Two of them, **Cost and the
economics of agent work** and **The enterprise tier**, carry a deep-dive second pass; follow the "Next — part
2 of the lesson" pointer at the bottom of either lesson to reach it. The other two stand as single pages.

:::
