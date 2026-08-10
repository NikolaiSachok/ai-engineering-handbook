---
id: overview
title: Part I — The Foundation
sidebar_label: Part overview
---

# Part I — The Foundation

The course's thesis is that verification capacity, not model capability, is what limits agent-built software.
Part I argues that thesis from the evidence and then draws the consequence: almost everything you can do about
the constraint happens **before an agent writes a line**. This is the part with no code in it, and it is the
part the rest of the course leans on.

*Where this sits on [the course map](../intro.md#course-map): underneath the loop — what has to be true before any stage runs.*

It runs in two movements. The first two lessons are about knowing what is true — the measured picture
(throughput up, quality and comprehension down, self-assessment broken) and the instrument for grading any
claim you meet about it. The other three are the foundation itself: the setup you hand an agent, the memory it
works against, and the rules it cannot talk its way past.

Those last three share a shape worth carrying into them. Each is something you prepare in advance, and each
one **decays**. A harness encodes assumptions about the model that expire as models improve. A memory file is
not stored but billed: it is re-sent on every turn, at a measured cost of over 20% more inference spend per
turn. A rules corpus with no owner rots until two authoritative files prescribe opposite architectures.
Preparation is never one-time — that is the part of "preparation over model" people drop.

## What's inside

- **[The verification bottleneck](./verification-bottleneck.md)** — the thesis, argued from the primaries:
  output rises and replicates, quality and comprehension fall, and you cannot feel either effect on yourself.
- **[Reading the evidence](./reading-the-evidence.md)** — the `MEASURED` / `REPORTED` / `ASSERTED` ladder,
  the four checks a number has to survive, and why the most-repeated figure in a genre is usually the one
  nobody can check.
- **[Preparation over model](./preparation-over-model.md)** — setup and scope move agent success further than
  any model upgrade in the evidence; and how to read a first-party success number without importing it.
- **[Project memory and tiering](./project-memory-and-tiering.md)** — agents keep nothing between runs, but
  writing more down is the failure mode too. Tier the knowledge instead of producing more of it.
- **[Rules that hold](./rules-that-hold.md)** — an instruction is not a control. What an agent optimizes is
  exactly what you check, so a rule you can execute should never merely be written down.

## Prerequisites

None from this course — this is where it starts. What it does assume is that you have run a coding agent on
real work and formed an opinion about whether it made you faster. Lesson 1 is largely about why that opinion
is not evidence, so bring it and be willing to put it down.

## What changes after this part

You can take any productivity claim in this field and place it: what the denominator was, who paid for the
study, whether the number is still current, and whether "17%" was percent or percentage points. You can look
at a written convention and say whether it is a control or a suggestion. And before dispatching an agent, you
know the four things worth preparing — a bounded scope, an environment it can build and test in, a memory
tiered by what the task actually needs, and rules that execute.

:::note[Status]

Part I is complete — all five lessons are published. It carries no deep-dive second pass; the material that
would go there is picked up directly by Parts II–V, which apply each of these five ideas to a stage of the
loop.

:::
