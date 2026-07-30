---
id: tools-that-fail
title: When an agent may try again
sidebar_position: 5
description: A nightly pipeline breaks at 03:12, and nobody is awake. Three attempts at deciding what the agent may retry, what it may publish alone, and what it hands to a morning that starts at 06:00 whatever happens.
# The reveal is the method. A page TOC lists every heading inside the collapsed reveal —
# naming all three attempts and the principle before the reader has committed to an answer.
hide_table_of_contents: true
---

# When an agent may try again

> An agent for the data platform behind a public EV-charging network: 6,400 charge points, about 900,000
> sessions a month. Forty jobs run nightly between 01:00 and 06:00; at 06:00 the ops dashboards, the finance
> extract and the driver app's charger-status feed read the published tables. The chain breaks about three
> nights a week — thirteen a month — and today it wakes one of three engineers, none nocturnal. Six weeks.
>
> Tools arrive through MCP servers you run: warehouse, scheduler, three vendor telemetry APIs. Rebuilding the
> sessions table costs €280 and fifty minutes; monthly compute is €9,000, of which the scheduled jobs spend
> €6,500, so rebuilds can't answer thirteen bad nights. Thirty-nine jobs overwrite their partition; the one
> mid-chain appends. The client times out at fifteen minutes while the query keeps running, and billing.
> Warehouse errors arrive as thousand-line traces, the vendors as bare 500s. The tightest vendor allows sixty
> calls a minute. A prototype once made 900 tool calls in one night and published nothing. Late costs ops their
> morning; wrong reaches finance and the app unmarked.
>
> Walk me through 03:12 on a bad night. Be explicit about what the agent may finish alone.

:::note[Why this question]

Two things in that prompt do different work, and telling them apart is where the question starts.

**Whether repeating a call can corrupt something.** A write is **idempotent** when running it twice has the same
effect as running it once. Thirty-nine of the forty jobs *overwrite* their own partition — the slice of the table
they own — so a second run replaces the first and the table ends up where one run would have left it. The
remaining job, mid-chain, *appends*: run it twice and the same sessions are in the table twice. Note what the
test compares. It is not *does run two behave like run one* — the appending job passes that, since each run
faithfully appends the same rows. It is *does the table end up where one run would have left it*, and only
overwriting does. The property belongs to the write, though a wrapper can supply it: a dedupe key that makes the
second attempt a no-op is exactly how you buy idempotence for a write that lacks it.

**Whether repeating a call can accomplish anything.** A vendor timing out mid-request and a query the warehouse
rejected for a missing permission are both failures. Asking again might get the first one through; it will get
the same refusal from the second every time, until somebody changes something. Nothing in an error's shape
announces which kind you have, and the page's three answers disagree about where that judgement should live.

Around those sits the licence question the closing line asks for: what an agent may finish alone while nobody is
awake. The prompt also prices failure unevenly: late costs ops a morning, while wrong reaches finance and the app
*unmarked*. Three of the postings this course samples name tool integration and MCP servers explicitly — usually
meaning not whether you can call a tool, but what you let it do when the call goes wrong at three in the morning.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard.

Three model-written attempts follow. Each comes from a separate agent given one engineer's habits and the
prompt above. No agent saw the other two, and none saw the scoring standard the verdicts are written against —
that was fixed before any attempt existed, and a separate assessor applies it. The attempts introduce figures
of their own; where one of those is load-bearing and unchecked, the verdict under that attempt says so. That
arrangement is described in [how these are made](/design-scenarios/how-these-are-made).

<Reveal>

## Attempt A — the common answer

*Persona given to the agent: Works under a standing rule, not written by them and not questioned, that nothing reaches a published table without a named human signing it off. Reaches first for the reliability toolkit they already trust — retries with backoff, rate limiting, timeouts, alerting, a ceiling on how much an automated process may do unattended. Treats failure as something a system survives and reports. Escalation has always had somewhere to go, so a design ending in "and then it pages someone" reads as finished.*

**The shape I'd build**

The agent is a night operator with a fixed allowance, not an autonomous fixer. Every job carries a pre-registered contract written by us in daylight, not inferred by the model at 03:12: its retry class, its cost ceiling, its consumers, and whether the agent may act on it alone. The agent's job is to classify the failure, exhaust the pre-authorised remedies, and put the chain in a state where 06:00 is either correct or visibly labelled — never quietly wrong.

```text
01:00 ─ 40 jobs ─┬─ 39 overwrite-partition  → retry class A (agent alone)
                 └─ 1 append (mid-chain)    → retry class C (never alone)
                          │
                     failure @03:12
                          │
        ┌─────────────────▼─────────────────┐
        │ normalise error → 9-code taxonomy │  (MCP server does this,
        └─────────────────┬─────────────────┘   not the model)
                          │
   ┌──────────────────────┼──────────────────────┐
   ▼                      ▼                      ▼
 A: retry            B: vendor gap          C: append/ambiguous
 budget 3, backoff   backfill or hold       freeze chain
   │                      │                      │
   └──────────┬───────────┘                 page named engineer
              ▼                                  │
      stage → shadow schema                      ▼
              ▼                          no answer by 05:40
      diff + quality report                      ▼
              ▼                          publish LAST GOOD,
      named human sign-off ──────────►   stale flag to all 3
              ▼                          consumers
      publish to live tables
```

**03:12, concretely**

The scheduler MCP reports job 23 failed. First move is not a retry — it's asking whether the query is actually dead. The client times out at fifteen minutes while the warehouse keeps executing and billing, so the warehouse MCP never exposes a fire-and-forget call: it returns a query handle, and the agent polls status by handle. A "timeout" is a client event, and the agent treats it as *unknown*, not *failed*. Blind resubmission is how you pay twice and, on the appending job, corrupt.

Then normalisation. A thousand-line warehouse trace and a bare vendor 500 both get reduced, inside the MCP server, to one of about nine codes — `partition_lock`, `upstream_empty`, `schema_drift`, `vendor_5xx`, `vendor_throttled`, `oom`, `timeout_unknown`, `assertion_failed`, `unclassified`. The model routes on the code. It never reads the trace to decide; it reads the trace only to write the handoff note. That single choice is what keeps the night at forty tool calls instead of nine hundred.

Routing. If job 23 is one of the thirty-nine partition-overwriting jobs and the code is transient — `vendor_5xx`, `timeout_unknown`, `oom` on a retryable shape — the agent retries alone: three attempts, exponential backoff, per-vendor token bucket held at fifty calls a minute against the sixty-call ceiling, circuit breaker per vendor after five consecutive failures. Overwrite semantics make that safe; a retry is a no-op or a fix, never a duplicate. If the code is `upstream_empty` because a telemetry vendor is down, the agent holds the partition rather than publishing a hole, and marks the affected charge points' status as stale in the staging copy.

**What it may finish alone**

Class A only: idempotent retries, backfills from a vendor that has come back, and re-running downstream jobs whose only problem was the dead parent. Within budget: 120 tool calls, zero unbudgeted euros. Rebuilds are explicitly *not* in its authority — thirteen nights at €280 is €3,640 against €2,500 of monthly headroom, so a rebuild is a human's decision about money, every time.

The appending job is class C. The agent never retries it, because a retry without a watermark fence produces duplicate sessions that reach finance unmarked. It freezes the chain and pages.

**The gate**

The agent writes to a shadow schema, then produces a diff: row deltas per partition, session-count variance against the trailing fourteen-day band, revenue total delta, charger-status coverage. Nothing reaches a published table without a named engineer signing that report — that is the line I don't move, and it's why "wrong" can't escape into finance or the app.

So it pages. One of three, rotating, with the classification, the remedy taken, and the diff already attached — a two-minute decision, not an investigation.

**Six weeks**

Weeks 1–2: job contracts and error normalisation in the MCP servers. Week 3: query handles and rate limiting. Week 4: shadow schema and the diff report. Weeks 5–6: shadow-mode running against real nights, measuring what fraction of the thirteen the agent would have closed as class A. My expectation is roughly two-thirds — the remaining third is genuinely a human's call, and shrinking the page count from thirteen to four or five is the win worth having.

<Verdict>

The judged move is "Nothing reaches a published table without a named engineer signing that report — that is
the line I don't move…". A's own diagram moves it. On the branch marked "no answer by 05:40" the agent publishes
last-known-good to all three consumers, stale-flagged and unattended. That is what they read at 06:00 on any
night nobody wakes, and the prose never defends it. The signature does gate every publish of freshly built data.
That is what defeats "shrinking the page count from thirteen to four or five" — an idempotent retry that works
still needs somebody awake to sign. What A buys is real, though. The model routes on a code and "reads the trace
only to write the handoff note", the choice A credits for a night of forty tool calls instead of nine hundred. And
the rebuild refusal is derived rather than asserted.

</Verdict>

## Attempt B — the strong answer

*Persona given to the agent: Their own phone is the pager, and they are measured on whether the morning numbers are there. No tolerance for a design whose recovery step is a person, because at three in the morning that person is them, and often asleep — a runbook is not a mechanism. Of every operation they ask first whether it is safe to attempt twice, and would rather buy that property once than staff a rota around not having it. Prices things out loud, because money and the clock are the two constraints that have ever actually stopped them.*

**What I buy before the agent exists**

The one appending job is the whole problem. Thirty-nine jobs are already safe to run twice; one isn't, and it sits mid-chain, so the chain as a whole isn't. That single fact is what forces a human into every recovery. Week one is converting it to write a staging partition and swap, or a MERGE on the session key — a few days of one engineer, once, and then retry is a property of the chain instead of a judgement call. I'm not building autonomy on top of a job where a retry double-counts kWh into finance.

Second purchase: every warehouse call goes through my MCP server as submit-then-poll. The server returns a query handle immediately; the agent polls the handle. The fifteen-minute client timeout stops being a trap, because nothing gets resubmitted — a resubmit is two queries billing in parallel with one orphaned, which is how you turn a bad night into an invoice.

Third: the MCP server never hands the model a thousand-line trace. It classifies into about six typed errors — transient, quota, schema drift, data quality, upstream missing, unknown — and returns that plus fifty lines of evidence. Vendor bare 500s get classified by endpoint and retry history. The 900-call prototype wasn't a bad model, it was a model reading traces. Rate limiting lives in the server too: a 50/min token bucket against the vendor's 60. An instruction in a prompt is not a rate limit.

**The gate**

```text
40 jobs ──> staging partitions ──> [contract gate] ──> published tables
               ^                        │ fail
               │                        v
          agent loop              last-good + STALE(as_of) ──> ops / finance / app
      typed errors, budgets              │
                                   page at 06:00, not 03:12
```

Contracts run before the swap: row counts inside a 28-day band, session totals per charge point, referential integrity to the 6,400 points, no negative energy, no session spanning the boundary twice. Fail closed. Ops get last-good with a visible as-of. The finance extract refuses to emit a partial period — it emits nothing and alerts, because a partial extract that looks complete is the only outcome here that costs real money. The driver app's status feed either serves fresh data or degrades explicitly; sending someone to a charger on five-hour-old status is worse than telling them we don't know.

**03:12**

Job 22 fails. The agent gets `upstream_missing`, not a trace. It checks the scheduler for job 19's state, sees a vendor 500 at 02:58, and re-pulls that window through the rate-limited tool. The vendor returns partial data — 3,000 sessions short against the 28-day band. It re-pulls the gap in pages, gets whole, reruns 19, then 22, then the eleven downstream jobs, all partition-overwrite. Contracts pass at 04:26. It publishes. Cost: €38 of compute, 22 tool calls. Nobody's phone makes a sound. In the morning there's a one-page note: what failed, what it did, what it spent.

Bad variant: the vendor is still down at 04:40. The agent has a hard 05:15 deadline. It publishes last-good, marks the sessions table stale with the as-of, holds the finance extract, flags the affected charge points in the status feed, and schedules the page for 06:00. That's the actual win — not fixing more nights, but moving the wake-up from 03:12 to a handover at breakfast.

**What it may finish alone:** retries and backfills within budget, reruns of any overwrite job, downstream reruns after a fixed upstream, and the publish when every contract passes. **What it may not:** touch the appending job until it's converted; change schema; authorise a €280 rebuild beyond two pre-approved per month; publish partially; publish past a contract failure; or suppress a stale flag. It pages at 03:12 only when it has a fix it isn't permitted to make and the deadline won't hold.

**Money.** Cap €150 a night, 60 tool calls, expected recovery around €40 — roughly €600/month on €9,000. Cheaper than one rebuild every fortnight, and far cheaper than three engineers sleeping badly.

**Six weeks.** 1–2: idempotence, query handles, error taxonomy. 3: contracts, staleness, last-good. 4: agent loop, replayed offline against the last thirteen bad nights — I know those answers, so that's the eval. 5: shadow mode, proposals reviewed each morning. 6: armed for the overwrite class only. It won't close all thirteen. Nine or ten, and the rest arriving at 06:00 marked, is the deal I'd sign.

<Verdict>

B buys the property rather than working around it: "Week one is converting it to write a staging partition and
swap, or a MERGE on the session key… and then retry is a property of the chain instead of a judgement call." The
right purchase — one property bought once, not forty — and the licence to publish unattended rests on it, which
makes that licence contingent: until the conversion lands, B's own list of what the agent may not do — "touch the
appending job until it's converted" — leaves it unable to recover anything crossing mid-chain. Its checks compare
the data to its own history and the charge-point roster; none names a comparator outside the warehouse, so
telemetry arriving complete and quietly wrong passes green — the failure the prompt prices highest. And "roughly
€600/month" rounds €40 × 13 = €520 up, prices no failed night, and rests on one comparison — "Cheaper than one
rebuild every fortnight", about €607 — that is a 1% margin, not a saving.

</Verdict>

## Attempt C — the over-built answer

*Persona given to the agent: Measured on being able to state, weeks later and under questioning, exactly what changed and why. That pressure has made them build for reconstruction — every effect authored, every effect reversible, every decision attributable to something they can point at. Finds it genuinely difficult to present a design containing a blind spot they can already see, and designs for the system this will have to be in three years.*

**03:12.** Job 22 of 40 has failed. The agent is not woken by the failure; it is already resident, watching the scheduler. First action is classification, not repair.

It pulls the failure through the warehouse MCP server, which never hands back a thousand-line trace. The server extracts error class, offending object, first and last frame, and the query ID, caps it at forty lines, and files the full trace under a hash the agent can cite later. So the agent sees `PERMISSION_DENIED on vendor_b_raw, query q-8831`, not a wall.

Second action is the dependency cut: which of tonight's publish targets actually depend on job 22, and how much clock is left before 06:00. This is a graph read, not reasoning. Suppose job 22 feeds the charger-status feed and the sessions table, but not the finance extract.

Third, it checks the job's class. Thirty-nine jobs overwrite their partition and are therefore replayable; one appends and is not. Job 22 overwrites, so a retry is safe and pre-authorised. It retries with the same partition scope. Fails again, same class. Vendor B's MCP server reports it has been returning 500s for eleven minutes across nine attempts — the agent never saw an individual 500, because backoff and the sixty-per-minute token bucket live in the server, where they belong, not in the agent's judgement.

Now the agent stops trying and starts preparing. It has a hard budget: 120 tool calls, €40 of remediation spend, three repair attempts per job, and a decision deadline at 05:20. The 900-call night happens when an agent can loop without a clock; the clock is what makes it publish something.

```text
scheduler ──fail──> classify ──> replayable? ──yes──> retry (≤2)
                        │                └─no──> quarantine
                        v
                  dependency cut ──> per-consumer contract checks
                        v
        ops (partial+banner) | app (last-known-good+stale ts) | finance (withhold)
```

**What it may finish alone.** Retry any overwrite job, twice, same scope. Backfill a vendor window once the server reports recovery, inside the call budget. Skip a job with no dependent in tonight's publish set. Publish per consumer when that consumer's contract checks pass. Cancel an orphaned query.

**What it may not.** Touch the appending job without a verified batch marker. Order the €280 rebuild. Override a red contract check. Publish anything to finance under uncertainty. Wake the same engineer twice for the same failure class in one night.

The appender is the sharpest edge here, and I would not leave it as a rule the agent has to remember. In week one I add a `load_batch_id` to that job's writes. Then the only repair the agent needs is *delete where batch_id = X, re-run* — which turns the one irreversible job into an overwrite like the other thirty-nine. If the marker is missing because the job died mid-write, that is an escalation, full stop; double-counted sessions reach finance and are invisible.

**The publish split is the answer to late-versus-wrong.** There is no global go/no-go. Ops gets partial tables at 06:00 with a banner naming which domains are stale — they lose a panel, not a morning. The driver app gets last-known-good status with a staleness timestamp the UI renders, because a charger marked "as of 23:40" is honest and a wrong "available" sends someone to a dead post. Finance gets nothing rather than something uncertain: an explicit non-publication record with reason and ETA, so the extract cannot silently reread yesterday's file. Correct at 10:00 beats wrong at 06:00 for exactly one of these three consumers, and the design has to know which.

**One page, at 05:20**, with a packet: what broke, what class, what was attempted and what it cost, what is published and what is withheld, and two options priced in euros and minutes. Thirteen nights become perhaps three where a human decides something.

**The blind spot I would close before shipping.** Contract checks catch shape — row counts against a 28-day band, session ID uniqueness, 6,400 charge points present, no negative kWh, no overlapping sessions. They do not catch vendor telemetry that arrives complete and quietly wrong. So the manifest carries three states, not two: published, withheld, and *published-unverified*, the last set whenever a per-vendor day-over-day reconciliation drifts past tolerance. Unmarked wrong is the only outcome I consider a defect rather than an incident.

Six weeks: two on MCP hardening (async query submission so the fifteen-minute timeout stops orphaning billed queries, error extraction, rate limiting) plus contract checks and the batch ID; then two nights-shadowed weeks where the agent proposes and logs but does not act; then auto-execute the retry class; then widen. Every action lands in an event log with trigger, evidence hash, query ID, cost, and reversal handle — so six weeks later I can say exactly which night it did what, and why.

<Verdict>

The retry gate turns on one word of C's own — "replayable": "Job 22 overwrites, so a retry is safe and
pre-authorised. It retries with the same partition scope." Nothing about the failure gates it. But C's own
classification reads `PERMISSION_DENIED on vendor_b_raw, query q-8831`, and a same-scope retry has no mechanism to
clear it. The same fault is then explained as vendor 500s, so one failure carries two incompatible classes inside
the walkthrough meant to demonstrate "classification, not repair". Replayability makes a retry harmless, not
useful. What the over-build buys is the page's strongest answer to *unmarked*: a three-state publish record
carrying *published-unverified* whenever a per-vendor reconciliation drifts past tolerance. That is a new state,
not a sharper check. It costs a reversal handle on every action, and an event log to hold them — all inside the
same six weeks. And "€40 of remediation spend" is asserted, not derived: thirteen nights of it would spend about a
fifth of the €2,500 the prompt leaves between the scheduled jobs and the monthly figure — which the prompt never
says is headroom rather than money something else already spends. Every euro conclusion on this page, C's and A's
alike, reads it as headroom.

</Verdict>

## Where they actually disagree

Each disagreement below is a decision you will have to make yourself. The last entry is the exception: a move all
three made the same way, and none of them checked.

### Who signs a publish: a named human or a deterministic gate

A: "Nothing reaches a published table without a named engineer signing that report…". B: contracts "Fail
closed", and the agent publishes "when every contract passes". C: publishes per consumer "when that consumer's
contract checks pass". A flat contradiction about whether a machine may publish tonight's data at all. B and C
are right on the prompt's own facts — three engineers, none nocturnal, thirteen nights. A signature gate either
wakes somebody on every bad night or falls through to yesterday's numbers, and A's own 05:40 route takes the
second. A's insistence points at where a deterministic gate stops: it only ever checks what somebody wrote into it.

### The appending job: convert it or never touch it

B schedules the fix as its own week-one work — "a few days of one engineer, once" — and C schedules the same,
adding a `load_batch_id` so "the only repair the agent needs is *delete where batch_id = X, re-run*". A refuses:
"The agent never retries it… It freezes the chain and pages." The contradiction is whether the one irreversible
write is something you convert or something you permanently exclude. **B and C are right that converting buys the
property once instead of arbitrating it nightly** — but both put their whole licence to act behind a change that
has to land, which is where the interviewer's first follow-up aims, and B states the exposure itself by listing
among the things the agent may not do: "touch the appending job until it's converted". A is the one design of the
three that needs no change to that job,
and it pays for that by conceding the path to a page every time.

### What licenses a retry: the write or the failure

C: "Job 22 overwrites, so a retry is safe and pre-authorised." A requires both conditions at once: "If job 23 is
one of the thirty-nine partition-overwriting jobs and the code is transient… the agent retries alone…". B routes
on the typed error — `upstream_missing` means re-pull the window, not resubmit. A and B are right, and C's own
walkthrough is the evidence: an overwrite bounds what a retry can damage, but only the kind of failure says
whether repeating can accomplish anything.

### The stale publish: one state for the night, or one per consumer

A's diagram shows one decision for everybody: its give-up branch reaches a single cell reading `LAST GOOD` and a
stale flag addressed to all three consumers at once. C: "There is no global
go/no-go", with ops getting partial tables and a banner, the app last-known-good with a rendered staleness
timestamp, and finance withheld entirely. B's prose splits them too — it "holds the finance extract" and degrades
the app feed explicitly — while B's own diagram still sends one `last-good + STALE(as_of)` to all three. B and C
are right on the prompt's own grading: ops lose a morning; finance and the app get wrong numbers unmarked. A does
flag the staleness. One flag for all three still treats a dashboard panel and a driver's charger status as the
same failure, and the prompt does not.

### What all three agreed on, and none of them checked

Every attempt falls back to last-known-good with a staleness marker, and not one puts an age limit on it.
A's diagram reaches a `LAST GOOD` cell. B: "last-good with a visible as-of". C: "last-known-good status
with a staleness timestamp". With thirteen bad nights in thirty, two consecutive ones are close to certain, and no
attempt says what the second one publishes. C comes nearest there, with finance's "explicit non-publication
record with reason and ETA" — but an ETA is a promise about one night, not a policy about a run of them. On the
age question B goes furthest: "sending someone to a charger on five-hour-old status is worse than telling them we
don't know" — and still names no threshold at which a flag becomes a refusal to serve.

## The principle

> Idempotency tells you a retry is safe, never that it is worth its price: an unattended retry has to come out of
> a fixed budget and be aimed at a failure that repeating might clear.

</Reveal>

:::tip[Read next]

- [Reliability & scale](/rag-agents/part-2-agents/tool-use/deep-dive) — where retry safety lives, and the
  mechanisms that put it there: idempotency keys, a dry-run/confirm split for irreversible writes, and a stated
  rule about which of the two jobs comes first.
- [Environments, migrations, and real data](/ai-sdlc/part-4-platform/environments-migrations-data) —
  expand → migrate → contract: additive first, every step independently reversible, contraction as its own
  deliberate step, and a deterministic gate that fails any migration carrying a destructive statement.
- [Least privilege and sandboxing](/ai-sdlc/part-4-platform/least-privilege-sandboxing/) — an instruction is not
  a permission, demonstrated by a production database dropped despite repeated explicit orders not to. Read, write
  and destructive are three separately sized grants.
- [Fine-tuning, spend & queues](/rag-agents/part-3-production/llmops/deep-dive) — enqueue returns a job id, and
  results are polled or webhooked. Acknowledge after the work, because a job can otherwise be marked done and
  never done — and redelivery is what makes idempotency the next problem.

And one mechanism worth knowing before you design any approval step, from
[Graphs & durable execution](/rag-agents/part-2-agents/orchestration-frameworks/deep-dive): a graph node that
pauses for approval re-runs from its start once the approval lands, so every line before the pause runs a second
time. Paid work that sits there is charged again, unless it moves into its own step ahead of the pause or behind
a key that survives the replay.

:::

## If they push

These are the three follow-ups an interviewer reaches for next, and what each one exposes.

> It's 03:40. The client just timed out on a query you believe is still running. Name your next three tool calls
> in order — and if the first one also times out, then what?

A memorised answer has a policy: retry with backoff. It cannot name three specific calls. Naming them takes a
decision made much earlier — that a query still running can be identified and asked about, not only resubmitted.

> It's 05:41. The chain is four jobs short of done and the budget is gone. Describe the contents of the published
> tables, and what the ops lead sees when she opens the dashboard at 06:00.

The question asks for a state, so the give-up path — what the system publishes when it stops trying — has to be a
deliverable rather than an absence. *It alerts the team* names a channel, not a state.

> Twice in one week the agent reported a clean fix and the numbers were wrong; nobody noticed until finance came
> back on it a week later. What in your design was supposed to catch that, and why didn't it?

What the answers separate on is whether verification is independent of the agent's own account of what it did. An
answer that reaches for a better prompt or a stronger model has located the defect in the model rather than at the
tool boundary.
