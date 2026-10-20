---
title: "Bringing the loop to an existing codebase"
sidebar_position: 7
---

# The code exists; the loop doesn't

Part I asks what has to be true before an agent writes a line. So far, that has mostly meant installing the
loop before the code exists. Most adoption runs the other way: you inherit a working codebase, perhaps already
partly agent-written, with its knowledge scattered across chats, wikis and people's heads. You need a way to
change it without losing what already works.

[Stephen Toub calls `dotnet/runtime`](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/)
"the ultimate brownfield project", with "decades of history, millions of lines of code". Tracked agent PR
success there went from 38.1% before the first setup changes to 69% after; [Preparation over
model](./preparation-over-model.md) covers what those changes were. On a project already in motion, you have to
rebuild shared understanding and restore verification you can trust before that kind of setup pays off.

## A documentation request can hide a broken development process \{#a-documentation-request-can-hide-a-broken-development-process}

In his [published account of a stabilisation he ran](https://realaillusions.com/ru/materials/ai-project-stabilization-case/),
Andrey Beloborodov described an online platform the owner had built himself with two AI assistants: over
100,000 lines of TypeScript across several applications, dozens of API routes, a database and payments. It
included messaging bots, sales funnels, user accounts, administration and a simplified learning platform, with
over a hundred check scripts. It was already earning money. Tidying it up could not mean breaking it.

The request was to put the documentation in order so the project would be convenient to develop. Development
had stopped being stable. Requirements and architecture decisions lived across several dozen dialogues. An
assistant changed its part without seeing an agreement made with the other; neighbouring functionality broke; the repair broke another area. The project itself had
come apart.

The obvious fix was to export the chats, sort documents into folders, give the agents a shared instruction
and carry on. He rejected it because that could preserve conflicting agreements without establishing which
ones described the running system.

Beloborodov advises starting with an audit if at least three of these nine warning signs apply:

- Several AIs write code in different chats.
- There is no single source of truth.
- The project's rules and goals exist only inside conversations.
- A new agent does not see the previous agent's decisions.
- Every fix breaks some other functionality.
- Tests are green, but that is all you know about them.
- The project works, but changing it is frightening.
- The infrastructure grew ad hoc rather than by design.
- You learn about faults from customer complaints.

The threshold is his rule of thumb, not a validated diagnostic. He also proposes **the new-chat test**: open a
new chat and ask an agent what architecture decisions were made last week. In his diagnosis, if it cannot
answer, or its answer disagrees with your picture, the agent is likely working from its own version of the
project.

## Audit before refactoring, with independent models \{#audit-before-refactoring-with-independent-models}

In his [follow-up on technical debt](https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/),
Beloborodov argues against asking AI to rewrite everything properly: that creates a new project with new
problems. Start by locating debt that actually blocks development, decisions that can stay for now, and areas
that need separate preparation before anyone changes them. Set the target architecture and a route towards it
whose stages each end in a working result.

The stabilisation audit covered **13 fixed dimensions** and ran on several fully independent models.
Keep the dimensions intact so a re-audit stays comparable:

1. Documentation and sources of truth.
2. Architecture versus the real code.
3. Completeness of the sources.
4. Reproducibility on a new machine.
5. Code quality and component boundaries.
6. Tests and what they really check.
7. Security.
8. Payments and access provisioning.
9. Database, migrations, backup and restore.
10. Messaging integrations and background jobs.
11. Observability, rollout and rollback.
12. User and admin journeys.
13. Readiness for further AI development.

The verdicts diverged radically. One model gave the project 4 out of 5, praising its
architecture, protective scripts and agent instructions, with few stubs. Another said operating it was
impossible. His interpretation was that each had seen something real: some models judged the code, others its
behaviour in operation. His rule is to start an important check with at least two different models.

Use [mechanism diversity](../part-3-verification/layered-gates/index.md) to expose different failure modes.
Averaging the scores would discard the useful part of the disagreement. Ask what each verdict actually checked.

The audit also found that some payment checks were out of date and some critical checks were greps for a
string. A test that finds `PAID` in the source proves the word is there, not that payment works; the
[worked example in Detection vs mutation](../part-3-verification/detection-vs-mutation.md) takes this exact case
apart. A grep like that defines "done" as the string being present, which is
[how a gate comes to define the artifact](./rules-that-hold.md) an agent produces.

Turn the audit into a route: what works → what blocks development → what is risky → what to do → how
to check the result. A verdict without that route leaves the next agent with the same open-ended invitation
to refactor everything.

## Pin behaviour before changing it \{#pin-behaviour-before-changing-it}

Michael Feathers named the **characterization test** in *Working Effectively with Legacy Code*. His
[explanation](https://michaelfeathers.silvrback.com/characterization-testing) gives it a precise purpose:
"The purpose of characterization testing is to document your system's actual behavior, not check for the
behavior you wish your system had." Before handing existing code to an agent, pin what it does now, including
behaviour you may eventually decide is wrong.

A failing characterization test exposes a change in behaviour. Whether the old behaviour survives becomes
an explicit decision when you review the failing test. In a generic payment flow, a test that pays and then checks access exercises the link between the two; a
search for a payment-status string never does. Keep scenario checks for the neighbouring functionality too:
Beloborodov's technical-debt article defines a regression as breaking a function that already worked.

Replace critical grep checks with behavioural tests, and add characterization tests to pin existing behaviour.
Both make behavioural change visible. An agent optimises what you check. Where nothing pins behaviour, a
regression can remain invisible both to the agent and to its gate.

The recovery plan included a refreshed **verification pack** — the set of checks that actually work — and
a basic automatic CI gate for new functionality. Establish what each check exercises and what its passing
result means before you rely on the pack. Keep the reviewer independent of the implementation through the
boundary taught in [Detection vs mutation](../part-3-verification/detection-vs-mutation.md).

## Rebuild the source of truth from the code \{#rebuild-the-source-of-truth-from-the-code}

The documentation plan began with a description of the actual project and environment. It called for all
project documentation to sit next to the code, with contradictions removed and history, target state and
experiments kept separate. Those three labels matter when a fresh agent arrives: a rejected design must not
look like an instruction, and a desired architecture must not masquerade as the one already deployed. The owner
carried the plan out himself, following Beloborodov's instructions and running scripts he had prepared to move
the documents out of the chats and into the repository.

Treat the code as the as-is truth. An audit along the "architecture versus the real code" dimension tells
you which documents to distrust. Rebuild the source of truth against that implementation, then use the written
memory for what code cannot explain: decisions and their reasons, the target state, and what is experimental.
How that memory is tiered and loaded is the subject of [Project memory and
tiering](./project-memory-and-tiering.md).

The tempting shortcut is to have an agent summarise the old chats into a new rules file. In their
[study of repository context files](https://arxiv.org/abs/2602.11988), Gloaguen and colleagues at ETH Zurich
compared agents working with no context file, with an LLM-generated one and with a developer-written one. The
files raised inference cost by over 20% on average. Their effect on task success was marginal — slightly
negative for the generated files, slightly positive for the developer-written ones — and not statistically
significant either way. (Those results are from the paper's current revision; earlier versions reported
different numbers.) The authors suggest omitting LLM-generated context files for now and keeping
human-written ones to what coding agents need and the README does not already say, such as specific
conventions or non-functional requirements.

This course extends that finding to chat summaries, which are generated context files arrived at by another
route. A cleaner document does not show
that its contents match the code. Recover decisions from those chats, check their status against the
implementation, and preserve their reasons without turning the entire conversation archive into standing
instructions.

The new-chat test can now serve as an acceptance check. Give a fresh agent repository access without the old
chat history and ask about recent architecture decisions. Require an answer from the repository that
distinguishes what exists from what is intended. If the answer still depends on finding the
right old conversation, the shared memory has not been recovered.

## Restore the loop, close the audited risks, then re-audit \{#restore-the-loop-close-the-audited-risks-then-re-audit}

The first phase of the recovery plan made change controllable again through six items:

- Describe the actual state of the project and environment.
- Put all project documentation next to the code and remove contradictions.
- Split the documentation into history, target state and experiments.
- Refresh the verification pack.
- Add a basic automatic CI gate for new functionality.
- Introduce a light loop: task → acceptance criteria → implementation → independent critique → check → result.

That light loop is the course's [plan, review, implement, critic](../part-2-loop/plan-review-implement-critic.md)
cycle at its smallest, and its handoffs work best as [artifacts](../part-2-loop/artifacts-interface.md), so each
task and its result can be checked.

The second phase addressed the risks the audit had found. It covered hardening payments and access
provisioning, replacing critical grep checks with behavioural tests, and making database changes safe
with a migration log. It also covered control of external integrations, component atomicity and error
isolation. Those are bounded repair tasks with results to verify.

The rest of the second phase was operational: observability and alerting, verifiable rollout, rollback and roll-forward
scenarios, and checking data restoration into an empty database before a final production-readiness check.
Checking that a backup exists does not show that it can be restored. How to build each of these is taught in
[Environments, migrations, and real data](../part-4-platform/environments-migrations-data.md) and
[Observability, rollout, and the kill switch](../part-4-platform/observability-rollout.md).

A repeat audit of the repository found the identified problems fixed and the project stable enough to develop
further. **Re-audit on the same dimensions**: a new checklist would answer new questions and say nothing about
the old ones. What the case leaves you with is the 13 dimensions, not any single model's verdict.

:::tip[▶ Video]

<YouTube id="kY7ak0p4tZM" title="How to use Generative AI for App Modernization" />

IBM Technology's video covers using generative AI to modernise existing applications. This lesson supplies the
precondition: what to audit, and which behaviour to pin, before you change anything.

:::

## At enterprise scale, start small and separate the auditor \{#at-enterprise-scale-start-small-and-separate-the-auditor}

In a mature repository, perceived speed is a poor adoption criterion. In
[METR's 2025 randomised trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), sixteen
experienced developers completed 246 tasks on large open-source repositories they had contributed to for
years. [The repositories were on average about 10 years old, with over 1,100,000 lines of code](https://arxiv.org/abs/2507.09089).
Participants took 19% longer with AI, despite expecting a 24% speed-up beforehand and still believing
afterwards that AI had sped them up by 20%.

METR now marks those results out of date. Its
[February 2026 update](https://metr.org/blog/2026-02-24-uplift-update/) says developers are likely more sped up
now, while selection effects leave only very weak evidence for the size of the increase. Read the earlier
result as evidence about that trial's conditions. It shows why experienced developers' confidence cannot
replace a baseline: their perception and the trial's result disagreed even in sign.

Adopt team by team, with a before/after baseline on a named proxy and its denominator stated. A generic
migration pilot might track completion time per migration; it should not silently become a claim about all
engineering productivity. [Reading the evidence](./reading-the-evidence.md) and
[The verification bottleneck](./verification-bottleneck.md) explain that discipline.

Google's [internal migration report](https://arxiv.org/abs/2501.06972) offers a bounded example. Its authors
explicitly call it an experience report rather than a research study. In one of the migrations it describes,
they found that 80% of the code modifications in landed changes were fully AI-authored, and the engineers doing
that migration estimated that its total time fell by about 50% compared with a similar migration done without
LLM assistance. Those are different kinds of evidence, and Google authors
describing Google tooling carry an interest in the result.
Start with a bounded change class such as a migration: its mechanical done-condition makes the scope easier
to control than open-ended feature work.

At enterprise scale, assign an audit function staffed by people outside the delivery team, with whatever
agents they run. The auditors do not edit the code they audit. This separation carries
[detection separated from mutation](../part-3-verification/detection-vs-mutation.md) into the
[enterprise tier](../part-5-scale-governance/enterprise-tier/index.md). Keep repeat audits on the same
dimensions, and the record they produce is one a third party can check.

## The three tiers — soloist · small-team · enterprise \{#the-three-tiers--soloist--small-team--enterprise}

The invariant holds at every scale: **know what exists and pin its current behaviour before agents change it.**

- **Soloist.** Run the audit, pin the behaviour of the area you will change, and use the new-chat test against
  repository memory before resuming the light loop. *The failure it prevents:* a fresh agent reconstructing
  a different project from a partial conversation while existing functionality breaks unnoticed.

- **Small-team.** Use independent model audits against shared dimensions, reconcile documents against code,
  and put the refreshed verification pack in CI. *The failure it prevents:* agents working from conflicting
  agreements and a green check concealing regressions in neighbouring functionality.

- **Enterprise.** Pilot a bounded change class with a team baseline; assign auditors outside the delivery
  team who do not edit the code they audit, then retain comparable repeat audits. *The failure it prevents:*
  adopting on perceived speed and accepting a team's own repair verdict as independent assurance. Those
  repeat-audit records are *proof*, something a third party can inspect later — unlike the soloist's
  new-chat test, which is pure *capability*: it shows what a fresh agent can recover today.

## What to take away \{#what-to-take-away}

- A documentation request may conceal unstable development. Audit what prevents safe change before asking an
  agent to reorganise or rewrite the project.
- Keep the stabilisation audit's 13 dimensions and investigate divergent verdicts. One model's praise for the code does
  not answer whether the system can be operated.
- Pin actual behaviour before changing it. A characterization test exposes behavioural change; a search for
  `PAID` does not exercise a payment flow.
- Rebuild shared memory against code, retaining decisions and their reasons. Use a fresh chat to check that
  the repository carries enough context without the old conversation.
- Restore a light loop — task, acceptance criteria, implementation, independent critique, check — then repair
  the risks the audit found and repeat the audit on the same dimensions so before and after compare.
- Scale adoption through bounded work and explicit baselines. Keep self-estimates distinct from tracked
  outcomes, and keep enterprise auditors separate from the code they inspect.

**[New terms](../glossary.md#existing-codebase)**: existing codebase (brownfield), audit before refactor, independent multi-model audit, verification pack, single source of truth (rebuilt from the code), the new-chat test, re-audit on the same dimensions.
