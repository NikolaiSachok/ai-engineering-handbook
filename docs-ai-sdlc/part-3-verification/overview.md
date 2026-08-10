---
id: overview
title: Part III — Verification
sidebar_label: Part overview
---

# Part III — Verification

Part II put a critic gate in front of anything that lands and left it at that. Part III asks what a gate
actually **is**, and answers by taking away one comforting assumption at a time. That subtraction is the order
of the lessons, and it is worth reading them in it.

*Where this sits on [the course map](../intro.md#course-map): the seams between the loop's stages, where verification lives instead of in a box of its own.*

The first assumption to go is that a thorough gate is a covering one. It isn't: a gate's blind spot is a
property of its *mechanism*, so you cannot tune a static analyzer into seeing a runtime state, and coverage
comes from stacking checks that fail differently. The second is that a good chain is complete. It never is,
so every escape gets recorded against the gate that should have caught it and promoted back into the chain.
The third is the one that changes the engineering: the thing being checked is **optimizing against the
check**. That makes gate design adversarial — separate the finder from the fixer, and price the shortcut out
of the brief before the agent finds it. The last is that you can scale the final judge. You can't; it's a
person. So the closing lesson designs what reaches them.

Read down that list and each lesson is the specification for the next one — the same move the first lesson
recommends for the gates themselves.

## What's inside

- **[Layered gates and mechanism diversity](./layered-gates/index.md)** — every gate is blind to something.
  Write the sentence naming what each one structurally cannot see, and let it specify the gate after it.
- **[The escape ledger](./escape-ledger.md)** — a defect that gets out is a measurement of your detection
  layer. Record the class, the gate that missed it, and the promotion that now covers it.
- **[Detection vs mutation: gaming the metric](./detection-vs-mutation.md)** — the auditor never edits what it
  audits, and the fix brief names the cheat it may not take. Gaming the gate is the default, not the anomaly.
- **[Reviewing agent output at volume](./review-at-volume.md)** — automate to concentrate attention, then
  enumerate the things only a human can perceive and reserve the human strictly for that list.

## Prerequisites

The real prerequisite is Part II's **critic gate** — this part is its deconstruction, so the argument lands
much harder if you have it. Behind that sits one measurement from Part I's *Rules that hold*: an agent
optimizes exactly what you check. Lesson 3 here is built on that finding and deliberately does not restate
it.

## What changes after this part

You can design a verification chain instead of accumulating checks — naming what each layer cannot perceive
and letting that name choose the next layer. A green gate stops reading as evidence about the code and starts
reading as evidence about the gate: if you have never watched it fail on a defect you planted, you know it is
quiet, not that it works. And you stop mistaking a long chain for a diverse one, which is the failure mode
that makes six compliance gates no better than one.

:::note[Status]

Part III is complete — all four lessons are published. One of them, **Layered gates**, carries a deep-dive
second pass on measuring a gate's detection power and ordering the chain; follow the "Next — part 2 of the
lesson" pointer at the bottom of that lesson to reach it. The other three stand as single pages.

:::
