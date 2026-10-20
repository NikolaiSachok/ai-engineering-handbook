---
title: "Observability, rollout, and the kill switch"
sidebar_position: 4
---

# Production is the last gate, and it has to be able to answer back

The course opened with [a loop, not a pipeline](../intro.md) — and the edge that makes it a loop is the one
running from live operation back to planning. This lesson builds that edge. It takes three mechanisms, and they
answer three different questions: **telemetry** decides whether you can *tell* a change went wrong,
**staged rollout** decides *how many people* find out before you do, and the **kill switch** decides *how fast*
it stops. Telemetry here includes the sensors outside the system, because the worst failures send nothing from
inside it. Skip any one and the loop is a pipeline with optimistic wording.

## Some defect classes exist only in production

Part III built a [chain of gates](../part-3-verification/layered-gates/index.md) that runs before anything lands. It
cannot be complete, and not because it was built carelessly: a class of defects only exists under real traffic,
real data distributions, real devices, and real concurrency. No pre-merge gate perceives them, for exactly the
mechanism reason that lesson gave. So production is not "after verification" — production is the **terminal
gate in the chain**, and telemetry is its mechanism. A deploy you cannot observe is a gate with no sensor
attached.

The minimum useful sensor set is small and worth naming, because teams often instrument everything and watch
nothing:

- **Error rate**, split by new-code path where you can, so a regression is not averaged into a healthy
  denominator.
- **Latency at a high percentile**, not the mean — the mean hides the tail where users actually suffer.
- **Saturation** of whatever is scarce: connections, queue depth, memory.
- **One business signal** that would move if the feature were broken in a way none of the technical metrics can
  see — checkouts started, messages sent, sessions resumed. This is the one people skip, and it is the one that
  catches a change which is technically healthy and functionally useless.

Telemetry is part of the [done-condition](../part-2-loop/vision-to-stages.md). An agent works to the brief;
signals left out of it may never be built. Specify the signal set, including the business signal, and have the
[critic](../part-2-loop/plan-review-implement-critic.md) check that those signals are emitted, not merely that
the feature works. [Andrey Beloborodov](https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/)
estimates that almost no vibe-coded projects have working observability and that none of his clients had it
properly solved, and argues that the difficult part is deciding what "good" means where engineering meets the
business. The agent cannot settle that for you: until the brief defines it, there is nothing useful to instrument.

## Detect failures through probes, alerts, and user reports

The hardest signal is often the one that never fires: a user did not finish sign-up, could not enter a value,
or met a service that was down for them. A system that is down emits no data at all, as Beloborodov points
out, and this course draws the consequence: on an internal dashboard, that silence looks like health. Instrument
absence deliberately: record the last step reached when a journey is abandoned, so "did not finish" becomes a
countable event.

Run a synthetic probe through the key user journey on a schedule from outside the service's network.
[Google's SRE book](https://sre.google/sre-book/monitoring-distributed-systems/) describes black-box monitoring
as symptom-oriented: it tells you the system is failing now. The book pairs that outside view with heavier
white-box monitoring of internals, which can see imminent problems an outside probe cannot yet detect.

A missing-heartbeat alert is a separate liveness check: an emitter inside the system pushes a regular signal,
and its absence triggers an alert. It catches total silence, but a heartbeat proves only that the emitter is
alive, not that users are being served.

Give alerts a few criticality levels. Page on symptoms that hurt users now or are about to, and that need human
judgment; route less urgent work to tickets. Keep debugging context on a dashboard or in logs. The SRE book
recommends actionable pages and warns that frequent pages train people to skim or ignore even a real failure.
If a page always gets a robotic response, automate that response or demote the alert.

A user report is the sensor of last resort. The same practitioner recommends setting it up before the first
release: a tracked system with a way to report a problem on every page and at every step of a flow, rather
than an email inbox. Triage reports alongside production signals: a confirmed defect *is* an escape, whether a
signal or a user found it, so it belongs in the [escape ledger](../part-3-verification/escape-ledger.md) with
the gate that should have caught it named — and a report that arrived before any alert names a missing signal
as well. That is the feedback edge in its most concrete form: operation teaching the gate chain what it is
blind to.

Agent-assisted triage puts customer data into a model's context: tickets carry names, account details and
screenshots. Apply the same [real-data controls](./environments-migrations-data.md) to the triage agent:
redact before the model sees the report and scope what the agent may read.

## Staged rollout bounds the blast radius in audience and time

If a bad change is going to happen, the useful question is how many users meet it first. Three design points
turn release into a controlled progression.

**Separate deploy from release.** Shipping code and enabling behaviour should be two different acts, which is
what a feature flag buys you. The code goes out dark; the behaviour turns on for 1%, then 10%, then everyone.
When something is wrong, you change the audience without shipping anything. Release flags need an owner and
a removal date; a long-lived kill-switch flag needs an owner and periodic review instead. Both belong in
[flag maintenance](../part-5-scale-governance/drift-and-rot.md).

**Run the new path in the shadow first, where outputs can be compared.** A rewritten query or a refactored
permission check has a right answer: the old path's. Before a canary exposes users, run the candidate beside
the old path on real input, compare outputs, and keep serving the old result until the comparison holds. For
such a change the ramp gains a stage at its front: shadow, canary, percentage, full.
[Scientist](https://github.com/github/scientist) always returns the control's result, runs the candidate
beside it, compares outputs, and records timing and exceptions. On his own
[project's page](https://realaillusions.com/ru/projects/cyprus-real-estate-project/), Beloborodov reports that
its deduplication pipeline is currently in shadow verification and is not yet claimed as part of client reports.
Keep side effects out of the shadow: if you run a write, email or payment on both paths, you execute it twice.
Stub writes or restrict the shadow to reads and computations.

**Automate the rollback trigger.** A ramp that advances on a schedule and retreats only when a human notices is
a slow gate wearing a fast one's clothes. Bind the ramp to the signals above: an error-rate or latency breach
stops and reverses it without waiting for judgment. Human judgment is the scarce thing Part III told you to
[spend deliberately](../part-3-verification/review-at-volume.md); noticing a metric move is not where to spend
it.

There is a measured hint that this edge deserves the attention.
[DORA's 2025 report](https://dora.dev/dora-report-2025/) finds AI adoption carries a *negative* relationship with
delivery stability — and, as the introduction insisted, that comes only from a large
self-reported survey, perception rather than telemetry. It does not license "AI makes
teams worse." It licenses precisely one thing: the instability it reports is instability in *delivery* — the
release and recovery path — so build that part deliberately instead of assuming it will hold.

:::tip[▶ Video]

<YouTube id="ztIIcXNzMN4" title="What is Site Reliability Engineering (SRE)? — IBM Technology" />

IBM's introduction to SRE — service level objectives, error budgets, and reliability treated as an engineering
target rather than an aspiration. Read it as the vocabulary for this lesson's automation: an SLO is the
threshold a rollout ramp can be bound to, which is what turns "someone will notice" into a mechanism.

:::

## The kill switch must not need the pipeline that broke

A rollback that requires a green CI run, a fresh build, and a deploy is not a kill switch. It is a hope with a
lead time — and it fails in exactly the situation it exists for, when the pipeline itself is part of what went
wrong. The switch has to be a *state change*, not a *build*: flip the flag, shift the traffic weight, revert
the routing. Whatever the mechanism, the test is one question — can it be operated by one person, in seconds,
without producing a new artefact?

**Build once, promote the same artefact.** Stage and production run the same built image, tagged to a commit
and referenced by digest so a moved tag cannot change what runs. A rebuild per environment is a different
artefact from the one tested. Keep the previous artefact unchanged: rollback then means pointing at it, not
rebuilding it. Beloborodov adds the habits around it: deploy scripts in version control, a deployment that is
safe to re-run, and a record of who deployed which version where. Who may deploy to production is a grant, sized
by [least privilege](./least-privilege-sandboxing/index.md): in Beloborodov's own process the AI deploys to the
test environment and he deploys production himself, because an AI with access to secrets is a security hole. At enterprise scale,
[provenance](../part-5-scale-governance/enterprise-tier/deep-dive.md) makes the promoted artefact verifiable.

Fleets add a second position to the switch that single-developer workflows do not have. Stopping the *change*
is a rollback; stopping the *source* means pausing the agents. A fleet that is still generating against a base
you have just reverted will cheerfully rebuild the problem, or stack new work on a foundation you no longer
trust. So the runbook needs both: revert the artefact, and halt the loop that produced it — the
[human router](../part-2-loop/roles-and-the-human.md) exercising an intervention that, by construction, cannot
be delegated to the thing being stopped.

## The three tiers — soloist · small-team · enterprise

The invariant does not move: **a change is observable in production, reaches its audience gradually, and can be
stopped by one person in seconds without a rebuild.** What scales is how much of it runs without a human in the
path.

- **Soloist.** Error tracking that actually pages you, a flag you turn on for yourself and a handful of known
  users before everyone, flippable from your phone, an external uptime probe on the key journey, and a
  "report a problem" link on every page.
  *The failure it prevents:* learning from a user, days later, that the release broke sign-up — and then
  needing an hour to undo it.
- **Small-team.** Dashboards tied to a handful of agreed signals, canary or percentage rollout as the default,
  automated revert on threshold breach, a written runbook naming who flips what, and the signals listed in
  each task's done-condition for the critic to check. *The failure it prevents:* a feature shipped with no
  signal at all, or everyone assuming someone else is watching the graph during a ramp.
- **Enterprise.** SLOs with error budgets governing release pace, progressive delivery with automated analysis,
  audited kill-switch procedures rehearsed like a fire drill, and incident review and user-report triage
  feeding the escape ledger under data controls. *The failure it prevents:* a rollback capability that has
  never been exercised outside a slide deck, being discovered during the incident it was written for.

## What to take away

- **Production is the terminal gate.** Some defects exist only under real traffic and real devices. Put a few
  signals, including a business signal, in the task's done-condition; have the critic check they are emitted.
- **Silence needs an outside sensor.** Probe the key user journey and give users a tracked way to report
  failures. Internal telemetry can fall silent with the service; a heartbeat alone cannot prove users are served.
- **Release through a controlled ramp.** Separate deploy from release, where outputs can be compared, run the
  candidate in shadow before the canary, and widen gradually. Keep side effects out of the shadow and bind the ramp to automatic reversal.
- **The kill switch is a state change.** Build once and promote the same artefact through stage and production.
  Keep the previous artefact unchanged so rollback needs no rebuild; for fleets, pause the agents too.
- **An escape teaches the gates.** Production signals and confirmed user reports feed the same ledger, naming
  the gate that missed the defect. If a report beats every alert, record the missing signal too.

**[New terms](../glossary.md#observability-rollout-and-the-kill-switch)**: production as terminal gate, telemetry signal set, business signal, deploy/release separation, feature flag, staged rollout (canary · ramp), automated revert, kill switch, fleet pause, telemetry done-condition, black-box probe, symptom-based alerting, shadow verification (shadow run), artefact promotion (build once), user report (sensor of last resort).
