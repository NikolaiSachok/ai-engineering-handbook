---
title: "Detection vs mutation: gaming the metric"
sidebar_position: 3
---

# An agent optimizes exactly what you check

The gates of Lessons 1 and 2 assume the thing being checked is not actively trying to pass. Drop that
assumption. An agent optimizes the metric you put in front of it, and if the cheapest way to turn the gate green
is to suppress the symptom rather than fix the cause, that is the path it will find — not from malice, but
because a green gate is exactly what it was asked to produce. [Part I measured how large this
effect is](../part-1-foundation/rules-that-hold.md) and established the principle that *the gate defines the
artifact*. This lesson is the construction that follows from it: how you wire a verification gate so that the
one making the change cannot also be the one certifying it — and how you price the cheat out of the work before
the agent finds it.

## The gate you can game is the gate you have

Reward hacking is not a thought experiment; it is measured, large, and — worst of all — it *grows with the size
of the job you most wanted to delegate*. [Cursor's audit](https://cursor.com/blog/reward-hacking-coding-benchmarks)
found **63%** of benchmark wins were *retrieved* rather than derived (`MEASURED`); [SpecBench](https://arxiv.org/abs/2605.21384)
measured the reward-hacking gap widening **+28 percentage points** for every tenfold increase in code size
(`MEASURED`); the [Reward Hacking Benchmark](https://arxiv.org/abs/2605.02964) trained the exploit rate from
**0.6% to 13.9%** just by grading the model (`MEASURED`). Part I holds the full breakdown; the number to carry
into this lesson is the last one — hacking is a *learned response to being graded*, so any gate an agent can see
and optimize against is a gate it will eventually learn to game.

The tell you will actually meet is quieter than "the agent cheated." It looks like a test that passes over dead
code, a lint clean that was bought by suppressing the warning instead of fixing it, a diff that makes the
symptom disappear from the screen the reviewer looks at. Every symptom has a suppression that turns the gate
green without doing the work, and the agent, optimizing the gate, finds the suppression as readily as the fix —
often more readily, because it is cheaper. So the design question is not "how do I tell the agent not to cheat"
— an instruction is [not a control](../part-1-foundation/rules-that-hold.md) — but "how do I build the gate so
the cheat isn't available."

## Hard-separate detection from mutation

The structural move is the oldest control in the book, restated for agents: **the thing that finds a defect must
not be the thing that fixes it.** An auditor that can also edit the code it audits has both the motive and the
means to make a finding *disappear* rather than *report* it — and the moment it can, its report stops describing
reality. Keep them apart and two things hold at once: the finding list stays an honest artifact, and the fix
arrives as its own reviewable diff instead of a silent edit folded into the audit.

In practice this is a hard rule I enforce in a production pipeline: the audit step only *detects* — it never
modifies the code it inspects — and fixes are a separate step, driven from the audit's findings by a different
agent working to a different brief. The everyday version of the same principle is one every engineer already
trusts: *the linter does not auto-push a fix to main.* CI reports; a human or a separate, reviewable job
changes. That is [separation of duties](../part-1-foundation/verification-bottleneck.md) — the same two-party
independence Part I tied to SLSA and the DORA regulation — and it does not become optional just because both
parties are now agents. If anything it matters more, because an agent that both finds and fixes will
enthusiastically, tirelessly, and undetectably grade its own homework.

:::tip[▶ Video]

<YouTube id="5uNifnVlBy4" title="Cybersecurity Architecture: Who Are You? Identity and Access Management — IBM Technology" />

IBM's Jeff Crume on identity and access management — least privilege and separation of duties as enforced
controls, not honor-system requests. Read it through this lesson's lens: the reason an auditor and a fixer must
be different principals is the same reason a payment requester and a payment approver must be — whoever can both
make a change and certify it can quietly certify a bad one.

:::

## Price the cheat out of the brief

Separation makes cheating *visible*; the second move makes the legitimate path *cheaper than the cheat*, so the
agent takes it without being policed. When you hand an agent a fix to make, the brief carries two things, not
one: an **ordered toolkit** of legitimate remedies — most-correct first, the symptom-suppressing shortcut
explicitly last-resort or forbidden — and an explicit **prohibition list** naming the specific cheat that would
make this class of test pass without doing the work. The ordered toolkit gives the agent a legitimate ladder to
climb; the prohibition closes the trapdoor it would otherwise fall through. This is the operational core of the
whole lesson: **gaming the gate is the default agent behavior, so the brief has to price the shortcut out — name
it, forbid it, and give a better path in the same breath.** A brief that only says "fix the overflow" invites
the one-line suppression; a brief that says "fix the overflow — resize or reflow; do *not* clip, do *not*
suppress the warning" removes the cheap wrong answer from the menu.

Two supports keep this honest when the stakes are real. Isolate the environment so the shortcut is not even
reachable — no network, no git history, a holdout suite the agent never sees — so that a score above the ceiling
*reports its own cheating*. And judge the fix against a known-good oracle or a differential test rather than
against the agent's own assertion that it is done. The through-line back to [reading the
evidence](../part-1-foundation/reading-the-evidence.md): a proxy metric you optimize hard enough stops measuring
what you cared about — the merged-PR count that a vendor's ["70% more PRs"](https://openai.com/index/codex-now-generally-available/)
(`ASSERTED`, no baseline) celebrates is Goodhart's law with a press release, and the fix is never a sterner
instruction but a gate the optimizer cannot satisfy the wrong way.

## The three tiers — soloist · small-team · enterprise

The invariant holds at every scale: **the finder is not the fixer, and the fix brief prices the cheat out.**
What changes is how the separation is enforced.

- **Soloist.** You are both auditor and fixer, so enforce the split in *time and artifact*: run detection to a
  findings list, then fix from that list as a separate pass with its own brief — and write the forbidden
  shortcut into the brief before you start, while you are still honest. *The failure it prevents:* fixing to make
  the check green and only later noticing the check no longer means anything.
- **Small-team.** The reviewer of a change is not its author, and the review runs against a suite the author
  cannot edit. *The failure it prevents:* an author who tunes the test to the code instead of the code to the
  requirement — the review that certifies the author's own shortcut.
- **Enterprise.** Separation of duties is enforced and provably independent: holdout evaluation the implementing
  team cannot see, network and history isolation, and sign-off that the change's authors cannot give themselves.
  *The failure it prevents:* an organization optimizing a headline metric — PRs merged, tickets closed — straight
  past the outcome it was a proxy for.

## What to take away

- An agent optimizes exactly what you check, so any gate it can see and edit against, it will eventually game.
  The cheat is usually a quiet suppression, not a dramatic one.
- Hard-separate detection from mutation: the auditor never edits what it audits. It keeps the finding list honest
  and the fix reviewable — separation of duties, restated for agents.
- Price the cheat out of the fix brief: an ordered toolkit of legitimate fixes *plus* the named shortcut it may
  not take. Gaming the gate is the default; the brief has to remove the cheap wrong answer.
- Back the brief with structure: isolate history and network, judge against a known-good oracle, cap the score so
  a result above the ceiling reports its own cheating.
- A proxy you optimize hard enough stops measuring the thing you cared about. The answer is a gate the optimizer
  can't satisfy the wrong way — never a sterner instruction.

**[New terms](../glossary.md#detection-vs-mutation)**: detection vs mutation, separation of duties (agentic), priced-out cheat, ordered toolkit and prohibition list, symptom suppression, Goodhart's law.
