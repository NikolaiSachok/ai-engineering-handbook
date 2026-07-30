---
id: framework-or-primitives
title: Framework or your own primitives
sidebar_position: 3
description: Adopt a named agent framework or build the primitives yourself. Three attempts at a grading pipeline that must reopen published cases and hand its records to an auditor fifteen months later.
# The reveal is the method. A page TOC lists every heading inside the collapsed reveal —
# naming all three attempts and the principle before the reader has committed to an answer.
hide_table_of_contents: true
---

# Framework or your own primitives

> You grade submitted engineering exercises: 12,000 submissions an intake, four intakes a year. Today it is
> one pass per submission — 900 lines of Python behind a queue, no persisted intermediate state, and a re-run
> costs about two cents, so failures just re-run. Next comes appeals. Each criterion is scored separately;
> low-confidence criteria route to a human moderator who may take a week; a second-marker agent contests
> borderline grades. And a candidate can appeal up to 30 days after publication; the appeal reopens the case
> and re-scores it. About one in forty is appealed — 300 an intake. Every published grade must be reproducible
> on demand — inputs, rubric version, model version, each intermediate judgement — and retained for the
> accreditation review in fifteen months, where an auditor will read your records. The appeals version must be
> live for the January intake, five months out and before that review. Three engineers own this; the one who
> wrote the queue moves teams in six weeks, leaving two, and none of the three has used LangGraph — which your
> open req lists, and which a principal engineer named in a design review. Done is appeals working end to end
> for that intake. Tell us what you do.

:::note[Why this question]

Four of the postings this course samples name LangGraph or LangChain, usually as a proxy for whether you have
shipped orchestration at all. The choice is not between packages. It is between primitives, and this workload
needs five: durable state per unit of work, branching on partial results, a join where a second agent contests
the first, and a pause a human can hold for a week. The fifth is different in kind — reopening a case that was
closed and published a month ago, where nothing is waiting to be resumed.

Argued as framework against hand-rolled, the question never separates those last two waits, which behave
nothing alike. Which of them an execution engine can hold for you is the whole design. Also at stake: a record
an auditor reads is your artefact, whoever executes the steps.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard.

Three model-written attempts follow. Each comes from a separate agent given one engineer's habits and the
prompt above. No agent saw the other two, and none saw the scoring standard the verdicts are written against —
that was fixed before any attempt existed, and a separate assessor applies it. The attempts introduce figures
of their own; where one of those is load-bearing and unchecked, the verdict under that attempt says so.

All three answered this prompt as printed. An earlier version of the question was discarded before publication
because all three answers to it agreed — a failure recorded in
[how these are made](/design-scenarios/how-these-are-made), not here.

<Reveal>

## Attempt A — the common answer

*Persona given to the agent: Follows the agent-tooling ecosystem closely and can name the frameworks' features accurately. Thinks in components, adapters and seams, and is decisive about architecture. Has never owned a record somebody outside the team reads back to them, so persistence has always been the framework's job — a thing you configure rather than a thing you are accountable for the shape of.*

**The shape of it**

Two cents a run and no state was the right call for one-pass. It stops being right the moment a case can be
*reopened*, because the thing you reopen is not the submission, it's the judgement — per criterion, with the
moderator's note attached, thirty days later. So the real change isn't appeals as a feature. It's that a
submission stops being a function call and becomes a long-lived case with a history. Everything else falls out
of that.

**Architecture**

I'd rebuild the pipeline as a LangGraph graph with a Postgres checkpointer, thread per submission. That one
decision buys almost all of the requirements at once.

```text
                     ┌─ criterion_1 ─┐
 ingest → rubric ────┼─ criterion_2 ─┼──→ aggregate → publish
   │      (pin ver)  ├─ criterion_3 ─┤        │
   │                 └─ criterion_N ─┘        │
   │                        │                 │
   │              low conf? ▼                 │
   │                  interrupt()             │
   │                  human moderator         │
   │                  (days–week)             │
   │                        │                 │
   │             borderline ▼                 │
   │                second_marker (subgraph)  │
   │                        │                 │
   └────────── appeal (≤30d) ─────────────────┘
                  resume same thread,
                  new superstep
     Postgres checkpointer = every superstep, forever
```

Criteria fan out with `Send` — map-reduce over the rubric, each criterion its own node writing into a
reducer-merged state key. That's what makes per-criterion scoring natural instead of one prompt returning a
blob you can't take apart later.

Low-confidence routing is `interrupt()`. The graph parks, the checkpointer holds the exact state, the
moderator takes a week, and `Command(resume=...)` picks it up at that node with nothing recomputed. No queue
timeout to fight, no orphaned job. The second-marker agent is a subgraph on the borderline edge with its own
state, so its reasoning is recorded separately from the first pass rather than overwriting it.

Appeals are the same mechanism, and this is the part I like: an appeal is just resuming a thread that already
has thirty days of history. You don't rebuild the case, you don't re-ingest, you don't guess what the original
run saw. You load the thread, you branch from the checkpoint before `aggregate`, you re-score with the appeal
context added. The prior judgement stays in history — it isn't clobbered.

**Reproducibility**

The checkpointer is the record. Every superstep persists the full state, so inputs, rubric version, model
version, and each intermediate judgement are all in there — the versions get stamped into state at the
`rubric` node so they travel with the case rather than living in config. Reproducing a published grade fifteen
months out is `get_state_history(thread_id)`, walk the supersteps, and if the reviewer wants to see it happen,
replay from the checkpoint with the pinned versions and it lands on the same numbers. Same code path the
appeal uses, so it's exercised three hundred times an intake instead of being a cold compliance feature nobody
has run.

Costs go up — Postgres writes on 12,000 threads with N criteria each, plus retention. Call it a few cents a
submission instead of two. Immaterial against a moderator hour.

**Six weeks and two engineers**

The queue author is the constraint, not LangGraph. What's in his head is the ingestion and retry semantics,
and the graph absorbs the retry half — durable checkpoints replace re-run-from-scratch — so the handover is
narrower than it looks. First two weeks: he pairs on porting ingest into the graph's entry node and writes
down the failure modes he's been carrying informally. Then he's replaceable.

The 900 lines of scoring logic don't get rewritten. They get wrapped as node functions, near-verbatim, so the
port is structural and reviewable rather than a rewrite with new bugs.

Nobody's used LangGraph, including me on this codebase, but the mental model is small: state, nodes, edges,
reducers, checkpointer. A week of building the one-pass path as a graph and hitting parity against current
output on a few hundred submissions gets everyone fluent, and it de-risks the port before appeals logic lands
on top. Weeks 1–3 port and parity. Weeks 4–9 interrupt, moderator, second marker. Weeks 10–14 appeals reopen
plus the reviewer-facing read over thread history. Two weeks of slack before January.

<Verdict>

A's opening read is right: what gets reopened is the judgement, not the submission. Then "Appeals are the same
mechanism" collapses the two waits. A moderator pause holds an open run; an appeal arrives after `publish`,
with nothing running. A resumes the case thread anyway, branching from the checkpoint before `aggregate`, which
makes publication rewindable. The API names are correct; the guarantees read off them are not. Resume does not
pick up "with nothing recomputed": the interrupted node re-executes from its start. And a replay is not a
record read — everything after the checkpoint it branches from runs again, model calls included — so "it lands
on the same numbers" is a prediction about a non-deterministic call, not a check. Two-cent re-runs make the
recompute harmless; the reproducibility claim is what breaks, and "the checkpointer is the record" puts that
claim in a dependency's tables. Wrapping the 900 lines and hitting parity against current output is its best
de-risking move.

</Verdict>

## Attempt B — the strong answer

*Persona given to the agent: Has owned a system whose records an outside party read back to them, and has been in the meeting where two runs of the same thing disagreed and couldn't be explained. Reads a requirements list looking for the two items that sound alike and are not. Unsentimental in both directions — own code is not an achievement to defend, a popular dependency is not a decision. Treats a colleague's departure as work to be scheduled rather than a risk to be mentioned.*

**Where the money is**

The 900 lines and the queue aren't the problem. The problem is that today the durable state is "the grade,"
and appeals needs the durable state to be "every judgement that produced the grade." That's not a refactor of
the grader, it's the introduction of a store that didn't exist. Re-run costing two cents is what let us get
away with having no state — and it stops being true the moment a case can be reopened, because a re-run in
November with November's model is a *different answer*, not a cheaper copy of the same one. So the first thing
I write is not code, it's the record: per submission per criterion, a row with input hash, rubric version,
model version/snapshot id, the judgement, the confidence, who or what wrote it, and when. Append-only. Nothing
overwrites a published judgement; a moderator decision and an appeal outcome are new rows that supersede, and
the published grade is a pointer into that history.

**The two requirements that sound alike**

"A second-marker agent contests borderline grades" and "low-confidence criteria route to a human moderator"
read as one feature — two flavours of escalation. They're not. The second marker is inside one run, seconds,
cheap, and it's mine to retry. The moderator is a week long, outside the process, and the case must survive a
deploy, a restart, and someone's laptop closing. If I build them with the same mechanism I'll have built the
fast one and pretended the slow one works. Same trap with "re-run" versus "re-score on appeal": one is
idempotent recovery, the other is a new decision that must be *distinguishable* from the original forever.

And the lifetime that actually sets the design is the model version. Fifteen months of retention against
providers who deprecate snapshots — I pin snapshot ids, and I ask procurement in week one for retention
commitments in writing. If a snapshot dies, reproducibility means "here is the recorded judgement and its
provenance," not "we can re-derive it." I'd rather decide that now than discover it in front of the
accreditation reviewer.

```text
  submission ──> per-criterion judge ──> confidence?
                        │                  │
                        │ high             │ low
                        ▼                  ▼
                  [judgement row]    moderator task
                        │             (days–week, durable)
                        ▼                  │
                  second marker  ◀─────────┘
                   (contest, in-run)
                        ▼
                  [publish: pointer to rows]
                        │
                  30d ──┴──> appeal ──> new rows, supersede
```

**Two engineers, five months**

Everything is timed backwards from January, and I schedule the departure rather than mention it. Six weeks
means his queue knowledge has a deadline: weeks one to four he pairs on the store and the moderator wait, and
the deliverable isn't a doc, it's *the other two shipping a change to the queue with him watching*. He doesn't
own new work. If we can't clear it in four, I cut appeals scope — the second marker is the first thing to go,
because low-confidence-to-human already covers the accreditation obligation and contest is a quality
improvement.

**LangGraph**

The open req and the principal's design review are things the organisation said out loud. What the engineering
argues is separate. The durable half here is a case that lives for weeks and is inspected in a year — that's a
database and a task queue, and I'm not putting a fifteen-month legal record inside a framework's checkpointer
schema that I'd then have to explain to an auditor. So: state and audit log are mine, in Postgres,
framework-independent. Inside a single run, LangGraph is a legitimate candidate for the per-criterion fan-out
plus the second-marker branch, and I'll spend one week of one engineer on a spike against the real fan-out.

Condition to adopt: it holds run orchestration only, no durable state, and the two remaining engineers can
debug a failed run unaided at the end of that week. If not, it's a for-loop and a queue, and I say that to the
principal with the spike as the argument. I revisit in April, after the intake — not before, because with two
engineers and a fixed date, learning a framework on the critical path is how you miss January.

<Verdict>

B states the distinction as a mechanism: a re-run in November with November's model is a different answer, not
a cheaper copy. From that follow an append-only row per criterion, a published grade that is a pointer into
history, and an appeal that writes new rows superseding rather than overwriting. It alone asks what happens
when a pinned snapshot is retired, and answers that reproducibility is then the record itself. It headlines the
wrong look-alike pair, though — second-marker versus moderator — and gets to the sharper one, re-run against
re-score, in a subordinate clause. Its first scope cut is the second marker, which the prompt lists among the
appeals features, and done is appeals working end to end. And "a for-loop and a queue" under-prices the
coordination it would then own — fan-out, join, and reopen.

</Verdict>

## Attempt C — the over-built answer

*Persona given to the agent: Designs for where the system will be in two years and for the teams that will touch it. Turns the ad-hoc thing principled — a declared graph instead of imperative code, an event log instead of a table someone updates, a platform instead of one team's script. Does not naturally ask whether this team, at this size, in this window, can absorb what has been drawn, and reads existing bespoke code as a liability by default.*

**What actually changed**

The unit of work stops being a submission-pass and becomes a case with a lifecycle measured in weeks. A
moderator takes a week. An appeal lands 30 days after publication. That means the state of a grade in progress
cannot live inside a running process, and it cannot live in a row someone updates — because the accreditation
review in fifteen months is going to ask what the score was *before* the moderator touched it, and a row that
got updated has already thrown that away. So the two-cent re-run stops being the recovery strategy. You can't
re-run a case that's carrying a human's judgement inside it.

**The record is the product**

I'd build the judgement ledger first, before any orchestration. Append-only event log, one event per
judgement: `CriterionScored`, `ModerationRequested`, `ModerationReturned`, `ContestRaised`, `GradePublished`,
`AppealOpened`. Case state is a fold over those events, never a mutable row. Every judgement event carries the
full reproduction tuple — input hash, rubric version, prompt hash, model id and params, and the hash of the
raw model response, with the submission bytes and rubric text in a content-addressed store. Grades aren't
reproducible because we promise they are; they're reproducible because replay is a test. I want a harness in
CI that takes a sample of published cases, replays them from the log, and byte-compares against what we
recorded. That runs every week from month one. The accreditation review then isn't an event we prepare for —
it's a report we already generate.

Fifteen months of text for 48,000 cases a year is nothing. The cost of this is schema discipline, not storage.

**The graph**

```text
submission ──► fan out per criterion
             C1  C2  C3 ... Cn        each node emits ONE event:
              │   │   │      │        {criterion, score, confidence, input_hash,
              ▼   ▼   ▼      ▼         rubric_ver, prompt_hash, model_id, raw_hash}
           confidence gate
            ├─ high ─────────────────► aggregate ──► publish
            ├─ borderline ─► second-marker ─► ContestRaised ─► aggregate
            └─ low ─► INTERRUPT (durable) ─► moderator ─► resume, days later
                                              │
   appeal (≤30d) ─► fork new run from log ────┘
```

Each criterion is its own node, so a criterion is independently retryable, independently versionable, and
independently explainable to the review. The moderator wait is a durable interrupt — the graph suspends on a
checkpoint and resumes when the decision arrives. No cron job scanning a table for stale work. The
second-marker is a node that emits a contest event, not a mutation of the score it disagrees with; both
judgements survive in the log, which is exactly what an appeal needs to read.

Appeals fall out of this almost free, and that's the point. An appeal is a new run that forks from the
published case's event log against frozen inputs. It doesn't overwrite anything. If we'd built appeals as a
second script that re-grades and updates the grade, we'd be building the same thing again in eighteen months
when someone asks to appeal an appeal.

**The six weeks**

The engineer who wrote the queue leaves in six weeks, and what I want out of those six weeks isn't
documentation of the 900 lines. I want the rubric semantics out of his head and into a versioned schema — what
a criterion is, what confidence means, which thresholds are real. The 900 lines themselves I treat as scoring
logic to lift into node bodies as pure functions and otherwise replace. Undocumented glue with a departing
author is a liability we're carrying whether we admit it or not, and it has no persisted state to preserve, so
there's nothing to migrate — it's the cheapest moment this rewrite will ever be.

Two engineers is the argument *for* the platform, not against it. Two people cannot maintain bespoke glue
across appeals, moderation, and an accreditation audit. They can maintain a declared graph over an event log,
because the parts that would otherwise be code — retry, resume, audit trail, replay — are properties of the
substrate instead of things they hand-wrote.

**LangGraph**

Nobody's used it; that's a couple of weeks, and I'd spend them in the first month on a spike that carries one
criterion end to end through a durable interrupt and out the replay harness. The alternative is hand-rolling
checkpointing and resume, which is the same work with none of the leverage. The principal named it in review
and the open req lists it — so the hire we make lands into a declared graph rather than into someone's script,
which is the failure mode we're currently escaping.

<Verdict>

C buys something real, and pays for it twice. Three moves are the right order and the right shape: building
the ledger before any orchestration, carrying a full "reproduction tuple" per event, and forking an appeal from
the published case's log. The weekly CI run that replays sampled cases turns "reproducible on demand" from a
promise into something already generated. Then it byte-compares against a stored hash of a raw model response —
a comparison that either re-invokes a model which will not return identical bytes, or replays recorded
responses and tests only the deterministic fold. And the two-engineer argument runs both ways: two cannot maintain
bespoke glue, so they get an event log, a content-addressed store, a fold over it, and the CI job that replays
it, while the framework costs "a couple of weeks" and appeals arrive "almost free". No condition that would
reverse the decision, no dated path to January.

</Verdict>

## Where they actually disagree

None of the four disagreements below is the adopt-or-decline verdict, and that is not an omission. Two of the
three attempts adopt the framework and reach opposite conclusions about everything that matters; the
disagreements that decide the design sit underneath the choice of package.

### Reproducibility: replay it or retain it

Three positions. A: reproducibility is the checkpointer's stored state, walked or replayed —
"`get_state_history(thread_id)`, walk the supersteps", and "replay from the checkpoint with the pinned versions
and it lands on the same numbers." C: reproducibility is replay *proven* — a weekly CI run replays sampled
published cases and byte-compares against what was recorded, so "grades aren't reproducible because we promise
they are; they're reproducible because replay is a test." B: reproducibility is retention — "if a snapshot
dies, reproducibility means 'here is the recorded judgement and its provenance,' not 'we can re-derive it.'"

Fifteen months and an external reader settle this. Both replay positions assume the model that produced the
judgement is still callable and still deterministic; neither is guaranteed, and only B plans for the answer
being no. C's position is a genuine advance on A's — it distrusts the promise and builds a test — but the test
only reaches the deterministic layer, the fold from events to case state. For the model call C stores a hash of
the response rather than the response, so its byte-compare has nothing to compare against without calling the
model again, which is the thing that will not return identical bytes.

### Durable state: the framework's or yours

A: "The checkpointer is the record." B and C both: the record is theirs and the orchestration sits on top of
it — B puts "state and audit log … in Postgres, framework-independent"; C builds the ledger "first, before any
orchestration."

A schema owned by a dependency means a routine upgrade migrates evidence, and this record has a retention duty
and a named reader. B and C are right. The split runs
independently of the adopt-or-decline call — C adopts LangGraph and still keeps the record, and B's condition
to adopt is precisely that the framework "holds run orchestration only, no durable state".

### The 900 lines of existing Python: wrap or replace

A wraps them: node functions, "near-verbatim, so the port is structural and reviewable rather than a rewrite
with new bugs", verified by parity against current output. C replaces them: scoring lifted as pure functions,
the rest "undocumented glue with a departing author", and with no persisted state "there's nothing to
migrate — it's the cheapest moment this rewrite will ever be." B leaves them alone: "the 900 lines and the
queue aren't the problem", because for B the missing piece is a store that never existed.

A is right, and it is the one place where A holds something neither sibling does. The author of the queue moves
teams in six weeks; while the current pipeline still runs, its output is a free oracle, and parity on a few
hundred submissions is the cheapest correctness evidence available. C's "nothing to migrate" is true about
state and false as an inference about behaviour. B reaches A's conclusion — leave the grader where it is — and
names no check that would tell it whether the behaviour survived.

### The departing engineer's six weeks: document or demonstrate

A wants ingestion and retry semantics, the failure modes written down, and pairing on the port. B refuses a
document and names a demonstration — "the other two shipping a change to the queue with him watching" — with a
week-four trigger to cut appeals scope if the transfer is not done by then. C explicitly does not want
"documentation of the 900 lines"; it wants rubric semantics in a versioned schema.

B's mechanism is right — transfer demonstrated by the recipients doing the work, on a deadline, with a
consequence attached. A names the right content (retry and failure modes) and the weaker mechanism. C is
targeting the wrong knowledge: rubric semantics are grading policy that must be versioned regardless of who
leaves, while what walks out is operational.

## The principle

> Suspending an open run and reopening a closed one are different problems, and only the first is one an
> execution engine can solve for you.

</Reveal>

:::tip[Read next]

- [Orchestration frameworks](/rag-agents/part-2-agents/orchestration-frameworks/) — enumerates what you own if
  you skip the framework, then prices the framework: abstraction cost, ecosystem churn,
  portability-versus-lock-in, and a primitives-first sequencing rule.
- [Graphs & durable execution](/rag-agents/part-2-agents/orchestration-frameworks/deep-dive) — the deep dive
  beneath that lesson; it names the state model a framework hands you, from a checkpointer writing at every
  super-step keyed by `thread_id` to an interrupt node that persists and then waits days.
- [Reliability & scale](/rag-agents/part-2-agents/tool-use/deep-dive) — retry safety is a property of the
  tool, not the retry policy: an idempotency key per intended operation, a dry-run/confirm split for
  irreversible writes, and why fixing idempotency comes before allowing retries.
- [Real agents — Claude, OpenAI, Gemini](/rag-agents/part-2-agents/real-agents) — three vendors' resume
  machinery under one pattern, and the caveat this question turns on: state you never persisted is state you
  cannot resume, and even persisted, resume is only safe if you can tell what actually completed.
- [Cost, agents & sovereignty](/rag-agents/part-3-production/cloud-platforms/deep-dive) — its
  managed-runtime section names a third option neither the question nor any attempt considers — a hosted agent
  loop with session persistence — and weighs it both ways: six things you stop building, against platform
  lock-in and less control over the loop.

:::

## If they push

Three follow-ups an interviewer reaches for next, and what each exposes.

> A grade goes out at the end of March. Three weeks later the candidate appeals. Walk me through it — what do
> you load, what do you create, and is that the same run as the one that published the grade or a different
> one?

This is the difference between suspending an open run and reopening a closed one, with no room to answer around
it. Someone who reasoned it out describes a retained case record and a new linked run. Someone reciting a
memorised answer resumes the run that produced the grade, which a finished, published run cannot do.

> The moderator disagrees with the second-marker agent, which disagreed with the first pass. Who writes the
> final judgement into the record, and what does the auditor see about the disagreement fifteen months later?

The answer has to name a field layout: three writers disagreed, and the record either holds the contested
history or it holds whichever verdict was written last.

> The engineer who wrote the queue moves teams in six weeks. What is on the list for those six weeks under your
> plan, and what would be on it if you had made the opposite call on the framework?

Two lists, and the second one is the test. It exists only if both options were reasoned through, and it differs
from the first only if handover was treated as work rather than mentioned as a risk.
