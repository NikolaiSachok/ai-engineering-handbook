---
id: overview
title: Part IV — The Platform
sidebar_label: Part overview
---

# Part IV — The Platform

Parts I through III lived inside the loop — planning, decomposing, generating, gating. Part IV is the ground
the loop runs on: the layer that decides how much damage a mistake can do. It takes one sentence from Part I
— *an instruction is not a control* — and applies it four times over: to what the agent holds, what it can
reach, what it looks at, and how fast its change can be stopped once it is live. Stated for this layer:
**enforcement is a property of the platform, never of the prompt.**

*Where this sits on [the course map](../intro.md#course-map): the ground the loop runs on — the layer that bounds how much damage a mistake can do.*

The lessons widen outward from the smallest thing you can withhold. First the credential the agent should
never hold at all, because a coding agent is a far wider channel than a developer: it reads a whole tree,
transmits it to a model provider, logs its reasoning, and can reproduce what it read somewhere you never
looked. Then the access it legitimately has — two controls that get casually merged, the *size of the grant*
and the *box it runs inside*, which fail differently and therefore compose. Then what that access points at:
data realistic enough to be useful and not real enough to be dangerous, and schema changes that carry a way
back you have actually exercised. Then what happens once the change is live.

That last lesson closes the loop the introduction drew. Production is not "after verification" — it is the
**terminal gate**, telemetry is its sensor, and a defect that reaches it is an escape that belongs in
Part III's ledger with the gate that missed it named.

## What's inside

- **[Secrets](./secrets.md)** — the value reaches neither the repository nor the agent's context. Hold a
  reference, inject at runtime, block server-side, and rotate rather than delete.
- **[Least privilege and sandboxing](./least-privilege-sandboxing/index.md)** — size the grant on four dials,
  then assume prompt injection succeeds and make it survivable. An instruction is not a permission.
- **[Environments, migrations, and real data](./environments-migrations-data.md)** — realistic, not real;
  expand → migrate → contract; and a backup you have never restored is not a backup.
- **[Observability, rollout, and the kill switch](./observability-rollout.md)** — few signals watched well, a
  ramp bound to automatic reversal, and a switch that is a state change rather than a build.

## Prerequisites

The sentence this part opens on, from Part I's *Rules that hold*. Every lesson here is that sentence at the
platform layer, and several cite the same incidents, so that one lesson buys you more here than Parts II and
III together. Two more from Part III: **mechanism diversity** returns twice — the deterministic secret
scanner composed with review, and the box composed with the grant — and the **escape ledger**, which the last
lesson writes into every time a defect reaches production.

## What changes after this part

For any agent you run, you can answer four questions with platform facts instead of promises: what it holds,
what it can reach, what data it is looking at, and how fast one person can stop it without producing a new
artefact. You will also stop reading enterprise credential machinery as ceremony — short-lived per-workload
credentials and egress allowlists are capability controls that exist because the cheap version demonstrably
broke.

:::note[Status]

Part IV is complete — all four lessons are published. One of them, **Least privilege and sandboxing**,
carries a deep-dive second pass on the layers of confinement that make an injection survivable; follow the
"Next — part 2 of the lesson" pointer at the bottom of that lesson to reach it. The other three stand as
single pages.

:::
