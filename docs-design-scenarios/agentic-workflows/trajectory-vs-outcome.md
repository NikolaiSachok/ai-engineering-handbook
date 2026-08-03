---
id: trajectory-vs-outcome
title: Knowing an agent works
sidebar_position: 2
description: Trajectory eval or outcome eval — three attempts at measuring a multi-step agent whose only ground-truth label arrives two weeks late and can be closed with a $75 credit.
# The reveal is the method. A page TOC lists every heading inside the collapsed reveal —
# naming all three attempts and the principle before the reader has committed to an answer.
hide_table_of_contents: true
---

# Knowing an agent works

> You own the agent that clears fulfilment exceptions in a parcel network — stuck shipments, item
> mismatches, bad addresses, parcels a carrier can't locate. It reads the exception, queries the warehouse
> system, the order database and two carrier APIs, then acts: reroutes, splits a shipment, reprints labels,
> issues a credit up to $75, or escalates. Nine thousand exceptions a day, about 375 an hour, nearly 1,100 an
> hour once a tracking feed goes stale. Median eleven tool calls per task, p95 forty; forty seconds to six
> minutes end to end; about $76,000 a month in model calls. Each reroute costs the network around nine
> dollars, and a credit is real money. Fifteen percent escalate to the ops floor's own queue, which is
> staffed separately. Four engineers maintain it, one of them half-time on quality. A case counts as resolved
> when the parcel is delivered and the customer doesn't write again within ten days — a label that lands two
> weeks late, and a credit closes almost anything. For quality work you get two ops reviewers, who can audit
> about two hundred cases a week. The customer sees one message; nobody reads the tool logs. Design the
> evaluation.

:::note[Why this question]

An agent that takes eleven steps to answer can be judged two ways. Score the **outcome** — did the parcel
arrive, did the customer stay quiet — and you get one cheap number per case that says nothing about how it
got there. Score the **trajectory** — which systems it read, which action it chose, whether it had the
evidence to choose it — and you get a per-case verdict within minutes, provided you can state what a good
trajectory looks like. Here the outcome label is late, and buying it is cheaper than earning it. No correct
trajectory is written down anywhere. So the question is what you measure when the honest signal is
unavailable and the available one is confounded, and whether the arithmetic of your own eval closes: two
reviewers, 200 cases a week, against 63,000 a week. The answers separate on what they choose not to measure,
and what they admit stays invisible.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard.

Three model-written attempts follow. Each comes from a separate agent given one engineer's habits and the
prompt above — no agent saw the other two, or the rubric, which was written first
([how these are made](/design-scenarios/how-these-are-made)). The prompt has been clarified once since they
answered — it now says outright that the escalation queue and the two quality reviewers are staffed
separately, which no attempt disputed. Every figure in it was checked against every other before the attempts
ran; the attempts introduce figures of their own, and where one of those is load-bearing and unchecked, the
verdict under that attempt says so.

<Reveal>

## Attempt A — the common answer

*Persona given to the agent: Has shipped LLM features that work and follows the agent-framework and eval-tooling ecosystem closely. Thinks in components, layers and rubrics. Has never had to work without labels — every feature they evaluated came with a dataset, a benchmark, or a human reading the output, so "define the metric" has always meant choosing one rather than manufacturing a signal from nothing.*

**How I'd frame it**

Three layers plus a guardrail lane. The mistake I want to avoid is a single number for "is the agent good,"
because this thing does five different jobs and they fail differently.

```text
  outcome        delivered + no re-contact in 10d, $ per resolved case
     ^           (slow, ground truth)
  trajectory     LLM judge over the trace, rubric per exception type
     ^           (fast, continuous, every case)
  component      tool-call correctness, retrieval sufficiency, arg validity
     ^           (pinned datasets, runs in CI)
  guardrails     credit policy, action authority, escalation triggers
                 (hard checks, not scored — pass/fail)
```

**Outcome layer.** Resolution rate is the label the business already owns, so I'd take it, but never in
aggregate — segment it by exception type and by action taken. Stuck-shipment reroutes and bad-address
reprints are completely different problems and a blended 85% hides which one is rotting. Alongside it I want
cost per resolved case with the nine-dollar reroute and the credit dollars folded in, because an agent that
resolves everything by rerouting twice is a quality regression that looks like a win. The ten-day window
means this layer trails, so I treat it as the monthly truth check, not the thing I steer on day to day.

**Trajectory layer.** This is where the real signal lives, and it's an LLM judge reading the trace. Per
exception type I write a rubric — four or five dimensions: did it query the systems it needed before acting,
is the chosen action actually entailed by the evidence it retrieved, was the credit warranted or was it
buying silence, did it escalate when the case was outside its authority. Scored 1–5 with anchors, not a vibe
score. I'd run it over every trace — it's a small model reading text, it's rounding error against
seventy-six thousand a month in agent calls — and route judge-vs-judge disagreements to a stronger model.
That gives me a quality number by lunchtime instead of in eleven days.

The credit thing matters enough to be its own rubric dimension. If a credit closes almost anything, then the
outcome label rewards handing out money, and the judge is the only place I can catch "resolved by credit when
a reprint would have done it." So: credit-appropriateness as an explicit dimension, and credit dollars per
hundred cases on the dashboard next to resolution rate.

**Component layer.** Below the judge, deterministic stuff in CI. A replay harness — record real tool
responses, pin them, so the same case runs identically on every prompt change. Then unit evals: address
normalization accuracy, did it pick the right carrier API, are the arguments well-formed, is the retrieved
context sufficient to support the action. Braintrust or LangSmith-style dataset, gate on it, no prompt merges
without it green. Four engineers can maintain that; they can't maintain a hand-review culture.

**Guardrails.** Not scored, enforced. Credit ceiling at $75 checked in code, not trusted to the model.
Reroute requires a retrieved carrier status. Two reroutes on one parcel is a hard escalate. These produce a
violation count, and the target is zero, so it's a different kind of metric from the rubrics.

**Using the ops reviewers.** Two hundred cases a week is the scarcest thing I have, so I spend it on
calibration, not coverage. First, a stratified golden set — maybe five hundred cases across the exception
types, weighted toward the expensive actions — that becomes the anchor the judge is validated against; I want
per-dimension agreement with human labels before I believe any judge number. After that, their weekly quota
goes to judge-disagreement cases and to every case where the agent spent real money, because those are the
ones where being wrong costs the network.

**Online.** New prompt or new tool goes out shadow first on live traffic, judge-scored against the incumbent,
then a canary slice with the outcome layer catching up behind it. And I want a separate watch on the
stale-feed surge — 1,100 an hour is a different distribution, so I'd tag those cases and track the rubric
scores on them independently, because that's exactly when the agent will start guessing with thin retrieval
and the aggregate won't show it.

<Verdict>

A alone segments the outcome label itself — resolution rate by exception type and by action taken, cost per
resolved case beside it — so resolving everything by rerouting twice stops looking like a win. It also names
the hack: the outcome label rewards handing out money. Then it hands the catch to an LLM judge over every
trace, and prices that judge as "rounding error against seventy-six thousand a month" without computing it.
The conclusion happens to hold, as B's arithmetic shows. But the dimension A cares most about,
credit-appropriateness, is the one call with no recorded correct answer to check a judge against, and A's fix
for that — a five-hundred-case golden set — is two and a half weeks of the entire two-hundred-a-week budget,
spent before the eval runs. A calls that budget "the scarcest thing I have" and divides neither number.

</Verdict>

## Attempt B — the strong answer

*Persona given to the agent: Has run a multi-step agent that takes real actions in production and been paged for it. Asks what signal exists, how late it arrives, and who has time to look at it, before designing any measurement. Has watched a metric go up while the business got worse, so attacks a success definition before using it. Prices reviewer hours and judge calls as it goes, and does arithmetic out loud when a number is load-bearing.*

**What I'd attack first: the label.** "Delivered and no re-contact in ten days" is not a quality signal, it's
a settlement signal. A $75 credit buys silence on almost anything, so the metric rewards the cheapest way to
make a customer go away. And it lands two weeks late — useless for catching a bad deploy. So I split it in
two immediately. Keep the ten-day outcome as a slow business ledger, but stop calling it the eval. The eval
runs on **action correctness measured against the action's own preconditions**, checkable within minutes.

**What signal already exists, for free.** Carrier and WMS state is ground truth that arrives on its own: did
the reroute actually move the parcel, did the split produce two scannable labels, did the reprinted label get
scanned. That gives me a same-day automatic check on maybe 70% of actions with no reviewer involved. I
instrument every action with the facts the agent believed at decision time — parcel scan state, inventory,
address validation result — so I can later ask whether the precondition held, not just whether the customer
complained.

**The credit is where I spend the reviewer budget.** Arithmetic out loud: 9,000 a day is 270,000 a month. Two
reviewers do 200 cases a week, call it 800 a month — that's 0.3%. A uniform random sample at 0.3% tells me
nothing about a subclass. So I don't sample uniformly. Roughly:

```text
  400/mo  credits issued (esp. $60-75, and credit-without-a-fix)
  200/mo  disagreement cases: cheap monitor flags vs agent chose otherwise
  150/mo  escalations — both directions (bad escalate + should-have-escalated)
   50/mo  fixed regression set, re-audited every month
```

Credit-without-a-fix is the failure mode I actually fear: pay the customer, parcel still stuck, ten-day
window closes clean. That pattern is detectable from data alone, and I'd alert on its *rate* daily, not wait
for review.

**Then the judge, priced.** 270k cases at even a cent of judge tokens is $2,700/month against a $76k model
bill — affordable, so the constraint isn't money, it's calibration. I'd run an LLM judge on the decision
trace for a stratified 3-5% slice, and hold it accountable to the 800 human labels: measure judge-vs-human
agreement per action type, and only trust the judge where agreement clears something like 85%. On credits I
expect it won't, so credits stay human-gated. The reviewer sample's real job is calibrating the judge, not
measuring the system.

**Offline set, because online is too slow.** Build 300 replayable exceptions from real history with pinned
tool responses, weighted toward the ambiguous ones, and grow it from every audited failure. One engineer
half-time on quality means the suite has to be cheap to run and honest about coverage — it will cover the
known failure taxonomy and nothing else, and I'd say that out loud rather than pretend it's a safety net.

**The stale-feed case is a separate eval.** 375/hour going to 1,100/hour with p95 forty tool calls is where I
expect the worst behavior: the agent reads stale carrier state and reroutes confidently on bad data. Nine
dollars a reroute, so a thousand wrong reroutes in an hour is nine thousand dollars of network cost plus the
parcels it churns. I'd eval that as a load-and-degraded-input scenario, and I'd hard-cap reroute and credit
volume per hour with a circuit breaker rather than trust the agent to notice the feed died. That's a
guardrail, but its trip rate is a metric I watch.

**What nobody reads.** Two ops reviewers and four engineers means one dashboard, not a suite. Four numbers,
daily: credit rate and credit-dollars, reroute-per-case, precondition-violation rate, escalation rate.
Everything else lives in a weekly review doc that the half-time quality engineer owns.

**What I'm choosing not to measure.** Reasoning quality on the 85% that resolve cleanly and cheaply —
invisible, and I accept that. Per-tool-call efficiency, except as cost. Long-tail customer sentiment beyond
re-contact. And I'm not measuring the counterfactual — whether a human would have done better on the same
case — because pricing that costs more reviewer hours than I have. If I get a third reviewer, that's the
first thing I'd buy.

<Verdict>

B asks what signal arrives on its own before designing anything, and finds a kind the others miss: carrier
and WMS state, which reports whether the reroute moved the parcel and whether the split produced two
scannable labels — same day, no reviewer involved. That reframing is its best move. The reviewer table is
priced: 800 reviews a month against 270,000 cases, 0.3%. That makes "maybe 70% of actions" the one figure B
never checks. The coverage of that free check decides how much is left for the judge and the reviewers, and it
is the only claim about the world B leaves unmeasured. The other gap is a missing gate: the 300-case replay
suite has
no pass condition and nobody named to block a release, so the fast layer B built to replace a two-week label
never stops a bad change from shipping.

</Verdict>

## Attempt C — the over-built answer

*Persona given to the agent: Designs for where the system will be in two years. Has watched teams ship the quick version and then spend years unable to change it, and concluded that under-building is the expensive mistake. Turns the ad-hoc thing systematic — a schema instead of a convention, a platform instead of a script, a dataset instead of a sample. Does not naturally ask whether the current team, at its current size, can staff what has been drawn.*

**The label is not a label.** "Delivered and no second contact in ten days" is a satisfaction proxy that a
$75 credit can buy outright, and it arrives two weeks after the decision I need to fix. So I stop treating it
as ground truth and demote it to one column in an outcome ledger. The thing I actually evaluate is the
decision: given this exception and this world state, was *reroute* the right move, and was it the cheapest
right move? Delivery and silence become confounded downstream signals I regress against, not the score.

**What I build first is a replay environment.** Every case gets a frozen snapshot at decision time — the
exception payload, the warehouse read, the order record, both carrier responses, cassette-style, keyed and
versioned. That's the substrate everything else sits on, and it's the piece four engineers cannot skip,
because without it every eval is a live experiment against a network where a wrong answer costs nine dollars.
With it I can re-run any prompt change, any model swap, any tool refactor over ten thousand real yesterdays
in an afternoon. It's not a script that dumps traces to S3. It's a schema with a contract: if a tool call
can't be replayed deterministically, it doesn't ship.

```text
exception ──▶ frozen world snapshot ──▶ agent ──▶ action + message
                                                    │
             ┌──────────────────────┬───────────────┴────────┐
       action grader          message grader            cost ledger
   (adjudicated golden set)  (does it match the       $9 reroute, credit $,
   + human-queue dispositions   action taken?)        escalation labour, tokens
                                                    │
                                                    10-day outcome ── weak, late, confounded
```

**Grading happens per action, weighted by money.** The action space is small — reroute, split, reprint,
credit, escalate — so I build a policy spec that says, for each exception class, which actions are correct,
which are acceptable-but-expensive, and which are forbidden. Then a golden set: about fifteen hundred cases,
stratified across the exception taxonomy, each with an adjudicated correct action and a note on why. That set
is a versioned dataset, refreshed weekly, not a spreadsheet someone owns.

And there's free labelled data already flowing: the fifteen percent that escalate. Thirteen hundred a day
where a human looks at the same case and decides something. That disposition is a label. It gives me both
directions of the escalation error — the model punting cases a human resolved in thirty seconds, which is the
expensive silent failure, and the cases it should have punted and didn't.

**Reviewer capacity goes to adjudication, not audit.** Two hundred a week against sixty-three thousand is a
rounding error, so spending it on random sampling is malpractice. It goes entirely to cases the automated
graders can't call: new exception patterns, disagreements between the model's action and the golden policy,
and every credit near the seventy-five-dollar ceiling. Everything else is auto-graded against replay plus the
ledger. Realistically I want a third reviewer and I'd argue for it, because adjudication throughput is what
caps how fast this thing can safely change — but the design doesn't break at two, it just iterates slower.

**Surge is a separate evaluation regime.** Eleven hundred an hour off a stale tracking feed isn't the same
distribution three times over — it's correlated garbage, every case looking like a stuck shipment, and the
failure mode is the agent confidently rerouting two thousand parcels at nine dollars each because the world
model was wrong. So I build a stale-feed suite explicitly: replay snapshots with deliberately poisoned
tracking, and assert the agent's action mix shifts toward escalate and hold rather than toward act. Alongside
it, an online blast-radius guard — action counts per class per hour against a rolling baseline, tripping to
escalate-only when the mix goes anomalous.

**And I grade the message on its own.** It's the only thing the customer sees, and nobody reads the tool
logs, so the failure nobody catches is a message that says "we've rerouted your parcel" when the agent
actually issued a credit and closed the case. That's a mechanical consistency check between the action record
and the text, plus a small rubric on whether it promises anything the system didn't do.

Cost, last. Seventy-six thousand a month is about twenty-eight cents a case, and one bad reroute is thirty
times that. Token efficiency is a metric I watch; action correctness is the metric I optimise.

<Verdict>

C buys three things the others don't. All three propose replay; C alone makes it a contract — "if a tool call
can't be replayed deterministically, it doesn't ship" — the artefact that makes every later eval cheap. Its
stale-feed suite asserts something falsifiable: poison the tracking snapshots, require the action mix to shift
toward escalate and hold. No other attempt grades the thing the customer actually sees: C checks the message
against the action record, so "we've rerouted your parcel" cannot go out on a credited case. Then the bill.
Fifteen hundred adjudicated cases, refreshed weekly, against two reviewers doing two hundred a week — seven
and a half weeks of their entire output for one build, and C has committed that capacity "entirely" elsewhere.
"The design doesn't break at two, it just iterates slower" is where the arithmetic belonged.

</Verdict>

## Where they actually disagree

Each disagreement below is a decision you will have to make yourself.

### What reads the trace: a judge or an assertion

A puts the primary quality signal in an LLM judge that scores every trace on four or five dimensions, 1–5,
against written anchors — "this is where the real signal lives". B demotes the judge to a stratified 3–5%
slice and makes the eval "action correctness measured against the action's own preconditions", trusting the
judge only per action type where agreement with human labels clears ~85%. This is a direct contradiction
about the instrument, not about thoroughness. B is right, and the reason is the dimension A already lost. A
judge scoring credit-appropriateness produces a number nobody can validate. *Did it read the latest carrier
scan before rerouting* is answerable from the state the agent already saw. A judge is a good tool for text
with a reference; the preconditions are checkable without one.

### The escalation queue: free labels or paid review

C treats the 15% that escalate — about 1,350 cases a day — as data already flowing ("that disposition is a
label") and gives reviewer time only to cases the automated graders cannot call. B spends 150 of its 800
monthly reviews on escalations in both directions. C has the better source here, and B's own framing ("what
signal already exists") should have caught it. But only one direction of the error is free. A disposition
exists only where the agent escalated, so the queue prices over-escalation and is silent on the cases that
should have been escalated and were not — which never reach a human, and which are what B's 150 escalation
reviews are actually buying. And a human who closes a case with a credit produces the same confounded outcome C
rejects everywhere else, so even the direction the dispositions do cover is a comparator with unmeasured
reviewer variance, not ground truth.

### Correct-action labels: author them or grade invariants

C builds a policy spec per exception type plus ~1,500 adjudicated cases as the grading substrate. B never
authors correct-action labels at all; the nearest it comes is a costed refusal: "I'm not measuring the
counterfactual — whether a human would have done better on the same case — because pricing that costs more
reviewer hours than I have." It grades invariants over 300
replayable cases instead. Which of them is right depends on whether the action has a determined answer.
Reroute-versus-escalate on a parcel with no fresh scan is precondition-determined, and C's three-tier policy
(correct / acceptable-but-expensive / forbidden) is the right way to encode that without pinning one correct
path per case. Credit-versus-reprint is a business tradeoff with no correct label. That is the general
answer, and staffing overrides it here: 1,500 adjudicated cases is a hiring decision and 300 replayable ones
is not, so B's version is the one that exists.

### Degraded input: an infrastructure invariant or an eval target

A tags surge cases and tracks the same rubric scores on them separately. B does both: it calls the surge "a
load-and-degraded-input scenario" and then declines to trust the agent anyway, hard-capping reroute and
credit volume per hour with a circuit breaker whose trip rate it watches. C names the assertion such a
scenario has to make — poisoned tracking snapshots, action mix must shift toward escalate and hold. B and C
are the same idea at two levels of precision, and the order follows: B's cap ships this week and limits how
many nine-dollar reroutes a bad hour can spend while nothing else is ready, and C's assertion is the only one
of the three precise enough that it can fail before a deploy. A's tagged score slice is the weakest of the
three — it tells you what the surge cost after it was spent.

## The principle

> When the only ground-truth label is late and confounded, your evaluation is the signal that already arrives
> for free plus the assertions you can check without a human plus the review hours you can actually staff —
> anything you cannot price in reviewer-weeks is a diagram, not a measurement.

</Reveal>

:::tip[Read next]

- [Planning & loops — deep dive](/rag-agents/part-2-agents/planning-loops/deep-dive) — splits agent eval into outcome
  and process, and states that a correct answer down a wrong path is luck. Names the process metrics, and why
  only those localise a failure to a step.
- [Reviewing agent output at volume](/ai-sdlc/part-3-verification/review-at-volume) — human review is
  designed, not stretched: cheap automated gates ahead of the person, then an enumeration of what only a
  person can judge, then a risk-weighted queue.
- [Detection vs mutation: gaming the metric](/ai-sdlc/part-3-verification/detection-vs-mutation) — why a proxy
  pushed hard enough stops measuring what you cared about, and why the remedy is a gate the optimiser cannot
  satisfy the wrong way rather than a sterner instruction.
- [Metric internals & judge calibration](/rag-agents/part-1-rag/cross-cutting/evaluation/deep-dive) — the
  calibration procedure a judge depends on: hold out human labels, measure agreement, and know the ceiling.
  Also why judge bias is systematic, so more volume never averages it out.
- [Layered gates and mechanism diversity](/ai-sdlc/part-3-verification/layered-gates) — writing, for each
  gate, the one sentence naming what it structurally cannot see, and letting that sentence specify the next
  gate.

:::

## If they push

These are the three follow-ups an interviewer reaches for next, and what each one exposes.

> Your suite has been green for a month. Resolution rate is flat and credit spend is up sixty percent. Which
> of your checks should have caught that, and at what point?

This asks whether cost per resolved case is a wired gate with a threshold and an owner, or a phrase in a
plan. Someone who reasoned it out points at a specific check and a specific day. Someone who memorised an
answer re-explains that credits confound the label, which the prompt already states outright.

> One case: the agent rerouted before reading the carrier's last scan, and the parcel arrived on time. Pass
> or fail — and what does your system actually do with it?

Right outcome, wrong path: the outcome check passes and the path check fails, so both halves of a rehearsed
answer apply and neither settles it. What the question wants is a ruling — the invariant that was violated,
what the path check emits, and whether that blocks a release. It also exposes whether the path check produces
rulings at all, or only scores.

> Two reviewers, two hundred cases a week, and you want them on the highest-value cases. What's on next
> week's list, and what did you stop showing them to make room?

Subtraction, which is the one operation an eval plan never volunteers. Anyone who has run a fixed review
budget can name the trade, and say why next week's queue differs from last week's.
