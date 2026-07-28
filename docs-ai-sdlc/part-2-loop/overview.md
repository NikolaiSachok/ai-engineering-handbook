---
id: overview
title: Part II — The Loop
sidebar_label: Part overview
---

# Part II — The Loop

Part I left you with a constraint: checking is what limits agent-built software, not generating. Part II is
the answer to it — a loop that spends cheap generation freely and concentrates the scarce resource, review,
at the few places where it changes the outcome.

Five lessons, and they answer one question in sequence: **where does verification actually get spent?** In
the shape of the plan, because a stage is a done-condition you can check, not a step you can describe. In the
size of the unit, because you control the work at the granularity you cut it into. In what crosses each
boundary, because a decision that lived only in a conversation cannot be reviewed or diffed. In two gates —
review the plan before the work, critique the work before it lands. And finally in where you stand: above the
loop as its router, not inside it as one more stage.

One tension runs under all of it and the part never resolves it, because it does not resolve. The written
artifacts that make the loop checkable are the same ones that, unmanaged, drown it. Artifact overload is
measured, it gets *worse* when you decompose more finely, and the first thing it evicts is the human it was
supposed to serve. So read this part as an argument about how much to write down, not only about what.

## What's inside

- **[From vision to verifiable stages](./vision-to-stages.md)** — give every stage a done-condition you can
  confirm without trusting the agent that it's done. Prefer the check that can't be argued with, and size the
  stage to it.
- **[Atomic tasks: decomposition as control](./atomic-tasks.md)** — the largest unit you can still verify in
  one read. Cut larger and "done" goes inferential; cut smaller and coordination overhead swamps the work.
- **[Artifacts as the only interface](./artifacts-interface.md)** — stages hand off through things on disk,
  not conversation. Reset the context onto a durable artifact rather than dragging a summary forward.
- **[Plan, review, implement, critic](./plan-review-implement-critic.md)** — the keystone. Two gates that
  matter, generation between them, and a critic that is never the agent whose work it checks.
- **[Roles, and where the human stays](./roles-and-the-human.md)** — on the loop, not in it. Three
  irreducible checkpoints, and why "review everything" is a rubber stamp rather than oversight.

## Prerequisites

Not all of Part I. Two ideas carry the weight: the **verification bottleneck** itself, and the split between
**computational and inferential** controls from *Rules that hold* — the first lesson here builds on that split
by name and does not re-derive it. The tiering discipline from *Project memory* is useful background for the
overload thread but is not load-bearing.

## What changes after this part

You can read a plan and say whether agents can be run against it: whether each stage names a fact that turns
true, whether the units are sized to a check you could actually perform, and whether anything crosses a
boundary that no one can inspect. You can also place yourself in the work — which checkpoints are yours
because nothing else can hold them, and which you can hand over without losing the thing that made the loop
trustworthy.

:::note[Status]

Part II is complete — all five lessons are published. It carries no deep-dive second pass; the loop's
gate is taken apart in Part III, and the platform it runs on in Part IV.

:::
