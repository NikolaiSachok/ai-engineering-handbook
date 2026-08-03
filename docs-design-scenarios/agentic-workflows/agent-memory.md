---
id: agent-memory
title: What an agent should remember, and what it must not
sidebar_position: 4
description: What a long-running agent persists, what it must let expire, and what it may never write down. Three attempts at a memory design for a workflow that runs for weeks, usually wakes on a newer deploy than the one that opened it, and must never tell a user their money is safe when it isn't.
# The reveal is the method. A page TOC lists every heading inside the collapsed reveal —
# naming all three attempts and the principle before the reader has committed to an answer.
hide_table_of_contents: true
---

# What an agent should remember, and what it must not

> You're designing memory for an agent in a consumer app that cancels subscriptions and disputes wrong
> charges. It works merchant portals and a mail alias, and reads a bank feed.
>
> About 4,000 workflows start daily. Median close is six days; three in a hundred run eleven weeks waiting on
> a merchant; mean lifetime is about eleven days, so ~45,000 sit open at once. Each wakes around nine times —
> a reply, a feed change, a retry — usually on a newer deploy than the one that opened it. Wakes are
> asynchronous; nobody waits.
>
> Inference budget: $12,000 a month against 120,000 workflows — ten cents each, across nine wakes.
>
> Three engineers own it. Coverage is 300 merchant flows today; the 18-month plan is 2,000.
>
> Quality: never tell a user a charge is stopped when the bank feed later says otherwise. It happens on 1.2%
> of closed workflows; nobody can tell a bad read from a bad tool result.
>
> Card numbers and portal passwords live in a vault, referenced by handle. Forwarded merchant mail carries
> statement lines and one-time codes. A deletion request must be honoured in 30 days, even against an open
> workflow.
>
> What persists, what expires, what is never written — and what does a wake read?

:::note[Why this question]

A **wake**, since the prompt counts them: one resumed run. The workflow comes back on an event, reads, decides,
and suspends again, and it is both the unit of cost here and the unit of correctness.

Two of the postings this course samples ask for memory across multi-step workflows, which usually gets read as
*wire up a store*. The phrase hides obligations that behave nothing alike. What **persists** is whatever survives
the suspend — the durable record a later run is allowed to draw on. What **expires** splits in two, and the
prompt supplies one of each: a *retention rule* is a clock you can schedule against, while a *deletion request*
is an erasure you must be able to perform on demand, mid-workflow, whether or not a clock was due. Both are
harder than they sound for the same reason — a fact sits in its own row and copies of it sit in an index, a trace
and a cached prompt, so it has to die in four places. What is **never written** is different in kind again:
material that must pass through the agent and must not survive it, like a one-time code that has to be usable and
must not be storable.

Then the prompt asks a last question separately, and the separation is the point: which slice of that durable
record a given wake actually loads. Keeping and reading are not the same decision, and an answer can be careful
about one while never stating the other.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard.

Three model-written attempts follow. Each comes from a separate agent given one engineer's habits and the
prompt above. No agent saw the other two, and none saw the scoring standard the verdicts are written against —
that was fixed before any attempt existed, and a separate assessor applies it. The attempts introduce figures
of their own; where one of those is load-bearing and unchecked, the verdict under that attempt says so. That
arrangement is described in [how these are made](/design-scenarios/how-these-are-made).

<Reveal>

## Attempt A — the common answer

*Persona given to the agent: Thinks in components and named patterns, and can name the standard pieces of an agent-memory design — short-term against long-term, a vector store for semantic recall, summarisation to keep the window manageable. Sketches the architecture first and fills in the boxes. Numbers feel like an implementation detail to settle once the design is agreed. Has never had to defend a per-request cost to anyone angry about a bill, and has always had someone reviewing the output before it reached a user, so a stale stored fact surfaced on its own and was somebody else's catch.*

**The shape**

I'd build this as four memory tiers with one rule: the workflow record is the only thing a wake trusts for state, everything else is retrieval that makes the wake cheaper or smarter.

```text
                  ┌─────────────────────────────┐
   wake event ───▶│  context assembler          │
 (mail/feed/retry)│  (deterministic, no LLM)    │
                  └──────────┬──────────────────┘
                             │ reads
   ┌─────────────────────────┼──────────────────────────┐
   │                         │                          │
┌──▼──────────────┐  ┌───────▼────────┐  ┌──────────────▼───┐
│ WORKFLOW STATE  │  │ MERCHANT       │  │ USER PROFILE     │
│ (episodic, hot) │  │ PROCEDURAL     │  │ (prefs, aliases, │
│ facts + ledger  │  │ MEMORY         │  │  vault handles)  │
│ + rolling summ. │  │ 300 → 2,000    │  │                  │
└──┬──────────────┘  └────────────────┘  └──────────────────┘
   │ overflow                    ▲
┌──▼──────────────┐              │ promoted, reviewed
│ SEMANTIC STORE  │──────────────┘
│ (mail chunks,   │
│  vector recall) │
└─────────────────┘
```

**What persists**

*Workflow state* — a typed record, not prose: `workflow_id`, merchant, dispute amount, current stage, the tool-call ledger (every portal action and mail send, with request/response), and a rolling summary that gets rewritten each wake so the eleven-week outliers don't grow unbounded. Every fact carries `source` (`bank_feed` / `tool_result` / `merchant_mail` / `model_inference`), `observed_at`, and `schema_version`. Provenance is the field that answers your 1.2% question — see below.

*Merchant procedural memory* — this is the tier that matters most for three engineers going 300 → 2,000. Per merchant: the cancellation path (selectors, steps, the confirmation string that means "done"), typical response latency, escalation address, known failure modes. Learned from successful runs, promoted only after it's been seen work more than once. The agent should not rediscover a merchant's flow on every workflow; that's both the cost lever and the coverage lever, since a new merchant is then a data entry, not a code change.

*User profile* — mail alias, notification preferences, vault handles, dispute history. Small, long-lived.

*Semantic store* — embedded chunks of forwarded merchant mail and portal text, scoped by `workflow_id`, so a wake can pull "what did this merchant actually say about the refund window" without carrying eleven weeks of thread in context.

**What expires**

Workflow state closes out to a compact archived record 90 days after close. Semantic chunks expire with the workflow. Merchant procedural entries carry a 180-day TTL and re-validate on failure — portals redesign, and a stale selector is the main rot risk. One-time codes get a 15-minute TTL, which brings me to:

**What is never written**

Card numbers and passwords, obviously — handles only, resolved at tool-call time and never echoed into the ledger or summary. One-time codes are consumed in-flight and never persisted; the ingest path strips them with a regex pass before mail touches storage. Statement lines get tokenised down to the fields we need (amount, date, descriptor hash) and the raw line is dropped. And no model-authored claim about the outcome ever gets written as a fact — outcomes are written by the bank feed only.

**What a wake reads**

The assembler builds the context deterministically: current stage + open questions, the last three ledger entries in full, the rolling summary, the merchant procedural entry, the profile slice, and top-k semantic hits against the wake trigger. That's a small read — call it a couple of thousand tokens — which sits comfortably inside the per-wake share of the ten cents, and leaves headroom for the summarisation write. Nine wakes at that size is not where the budget goes; tool-heavy wakes are.

**Never say stopped when it isn't**

Two mechanisms. First, the state machine has no transition into `stopped` that a model can trigger — only a bank-feed confirmation writes it, and until then the user sees `cancellation submitted`. Second, provenance makes the 1.2% attributable: when a feed contradiction fires, we replay the ledger and see whether the offending fact came in tagged `tool_result` (the portal lied or the flow is wrong — fix the merchant entry) or `model_inference` (the agent over-read a confirmation page — fix the prompt or the confirmation string). That distinction is exactly what's missing today, and it's a schema property, not a model property.

**Deletion**

`user_id` is the partition key across all four tiers, so a request is a cascade over partitions plus a tombstone that keeps the workflow runnable on pseudonymous state (merchant, amount, stage) with identity fields nulled. Thirty days is generous for a scheduled job.

<Verdict>

A's load-bearing move is the rolling summary — "rewritten each wake so the eleven-week outliers don't grow
unbounded", then read back on the wake after that. The cost is A's own best idea. A tags every fact with
`source` (`bank_feed` / `tool_result` / `merchant_mail` / `model_inference`) and rightly calls that "exactly
what's missing today", then writes mixed-provenance content into one prose blob that carries a single tag over
sources the tag cannot distinguish. A wake reads "the last three ledger entries in full", so recent provenance
survives item by item; older material arrives either as that blob or as "top-k semantic hits" over mail and
portal text, and only the second of those is still traceable to a source. On a 77-day case the blob is carrying
most of the history. A is also right that merchant procedural
memory is "the tier that matters most" — but "`user_id` is the partition key across all four tiers" falsifies
it, because a shared tier cannot be user-partitioned, so the deletion cascade cannot reach the one store
holding facts learned from a user's mail. The read cost is asserted, never computed.

</Verdict>

## Attempt B — the strong answer

*Persona given to the agent: Has been woken at three in the morning by this class of system. Starts from what breaks and works backwards — before naming a store, asks what reads it, how often, and what happens when the read is wrong. Prices things out loud, having lost an argument about a bill. Has watched a generated summary become the only surviving record of something that mattered, and has not trusted model-written text as evidence since. Wary of anything that cannot be deleted, after answering a deletion request against a system that had copied the same records into four undocumented places.*

**The shape of it**

Not "memory." A workflow is a row in a state machine plus an append-only ledger of typed facts, each with provenance. Nothing else persists. No rolling summary, no agent notes carried forward, no "context" blob. I have watched a generated summary become the only surviving record of something that mattered, and I will not put one in the closing path of a system that tells people their money is safe.

A fact row is: `(workflow_id, ts, source, kind, payload, artifact_ref, confidence)`. `source` is a closed enum — `bank_feed`, `portal_dom`, `merchant_mail`, `model_inference`. That field is the whole answer to your 1.2%.

**The 1.2% is a provenance bug, not a memory bug**

Nobody can tell a bad read from a bad tool result because both arrive as prose in the same slot. Separate the channels and the ambiguity disappears: a model-inferred fact can never satisfy a terminal transition. `stopped` requires a `bank_feed` observation — no new charge past the next expected bill date, or an explicit merchant confirmation ID plus one clean cycle. The agent reading "Your subscription has been cancelled" on a portal writes `model_inference: merchant_claims_cancelled`, which moves the workflow to `pending_confirm`, not `closed`. `pending_confirm` is cheap: it sleeps on feed diffs and costs no inference. That state also absorbs your eleven-week tail, which is otherwise the thing that eats the budget.

**What a wake reads**

```text
event (reply | feed_delta | timer)
  |
  v
[router: deterministic]---- ~60% exit here, no model
  |
  v
workflow header      ~200 tok   state, merchant_id, deadlines, deploy_schema
decision-grade facts ~600 tok   typed rows the state machine gated on (capped ~40)
recent tail          ~400 tok   last 5 events, typed
merchant playbook    ~800 tok   retrieved by (merchant_id, state) — the step, not the doc
the new event        ~300 tok
                    ---------
                     ~2.3k tok in, bounded by construction
```

Never the full history. Never a prior model output as input — that is how a bad read becomes canon on wake seven.

**Cost**

$12k / 120k workflows / 9 wakes ≈ 1.1¢ per wake. That doesn't buy a big-model call, so most wakes must not be model calls. Feed deltas, retries, and timer expiries route deterministically; merchant replies and ambiguous portal states get a small model on a ~2.5k-token context. At roughly 40% model-touched, you have ~2.5¢ each, which fits a Haiku-class model with room for a second pass on the ones that matter. The budget holds because context is capped per wake, not because we trimmed prompts.

**Never written**

Card numbers and passwords: handles only, resolved in-process, never logged, never in a trace, never in a fact payload. One-time codes: used in flight, never persisted — not even hashed. Statement lines from forwarded mail: extracted into typed fields; free text does not enter the ledger. Agent scratch reasoning: discarded at step close. Prompts: not stored. Store the input IDs and rebuild the prompt on demand — that is what makes a trace deletable.

**Deletion**

The four-copies scar decides this. Raw artifacts — mail bodies, portal captures — live in exactly one store, encrypted under a per-user key, referenced everywhere else by `artifact_ref`. Traces carry IDs, not content. Eval sets carry IDs, not content. Deletion is a key destroy: everything personal goes opaque in one operation, including inside an open workflow, which then degrades to its pseudonymised typed facts or terminates. TTLs: raw mail 30 days; portal captures until step close plus the dispute window; ledger facts for the financial retention period, personal fields already behind the key.

If I cannot name every place a statement line lands, the design is not finished. Two stores, one key, pointers everywhere else.

**Deploy skew and 300 → 2,000**

Every wake lands on a newer deploy, so the record is versioned data read through an upcasting reader. Persist facts and state position — those migrate. Prose and plans do not; they rot silently. Merchant knowledge is data, not code: a versioned playbook per merchant, reviewable independently. The agent may *propose* playbook changes from observed failures; promotion goes through an eval gate. Three engineers cannot review 2,000 flows as code, but they can review diffs to 2,000 rows.

Boring, inspectable at 3am, and the close decision comes from the bank, not from the model.

<Verdict>

B passes the budget by changing the denominator, not the prompt: "~60% exit here, no model", and a
`pending_confirm` state that "sleeps on feed diffs and costs no inference". C reaches the same conclusion — "most
wakes must not be inference at all" — but B is the only one that puts a number on the split, and the number is
B's own invention, unchecked. The sharper crack is
"~2.3k tok in, bounded by construction": that bound needs forty gated fact rows inside 600 tokens, about fifteen
tokens for a seven-field row carrying a payload. It will not hold, so the cap is asserted rather than
constructed — the one defect B is otherwise strongest for refusing. And the merchant playbook is a third
persisted store, model-proposed ("The agent may *propose* playbook changes from observed failures"), which both
"Nothing else persists" and "Never a prior model output as input" deny; the honest rule is never *ungated* model
output, on a fact shared by every open workflow at that merchant.

</Verdict>

## Attempt C — the over-built answer

*Persona given to the agent: Likes to get the foundation right the first time, having watched teams pay for years for a shortcut taken in week two. Designs for the system this will be in three years. Enjoys the hard general case — versioning, schema evolution, a policy layer, lineage, a service other teams could adopt rather than reinvent. Finds it genuinely difficult to leave a visible problem unaddressed in a design being presented, because naming it and deferring it feels like handing someone a known defect. Has mostly worked somewhere with a platform team to hand things off to, so "who operates this" has rarely been the binding constraint.*

**The shape I'd build**

Three stores, not one, because they have three different lifetimes and three different owners. Collapsing them is the shortcut that costs you in year two, when the retention rule and the learning loop end up fighting over the same table.

```text
  ingest (mail alias, portal, bank feed)
        │  redact → normalize → typed Observation
        ▼
  ┌──────────────────────────────┐
  │ 1. WORKFLOW LEDGER           │  append-only, typed, versioned
  │   Observations + Actions     │  source, tool_result, extractor_ver,
  │   + StateTransitions         │  raw_ref (TTL'd), never model prose
  └──────────┬───────────────────┘
             │ fold (deterministic, pure)
             ▼
  ┌──────────────────────────────┐
  │ 2. WAKE BRIEF (projection)   │  derived, rebuildable, cache-only,
  │   ~3k tokens, budgeted       │  invalidated by ledger append
  └──────────┬───────────────────┘
             │ + merchant card
             ▼
  ┌──────────────────────────────┐
  │ 3. MERCHANT PROCEDURE MEMORY │  cross-workflow, no PII, curated,
  │   300 → 2000 flows           │  promoted by eval, version-pinned
  └──────────────────────────────┘
```

**The ledger is the memory.** Everything durable is a typed event with provenance: what source produced it, which extractor version parsed it, what the tool actually returned, and a handle to the raw artifact. Nothing the model *says* is ever persisted as fact — the model proposes actions, the executed action and its result get written. That single rule is what makes a bad read distinguishable from a bad tool result: a bad read is an Observation whose `extractor_ver` disagrees with `raw_ref` on replay; a bad tool result is a tool_result claiming success against a bank feed that never moved. Right now you can't tell those apart because you're storing a conclusion, not its derivation.

**What a wake reads.** Not the ledger. A deterministic fold produces a brief: workflow header (merchant, state, obligations, deadline), the last N transitions, open commitments, the merchant procedure card, and the new stimulus. Fixed token budget, ~3k. It's a cache — deletable at any time, rebuilt from the ledger, keyed by ledger offset *and* fold version, so a wake on a newer deploy either finds a valid projection or recomputes one under the new code. That's the answer to "newer deploy than the one that opened it": never migrate live state, upcast on read, and pin the prompt + policy + fold version into each StateTransition so an eleven-week workflow's history remains interpretable.

**Merchant memory is the actual asset.** Learned procedure per merchant flow — the cancel path, the selector that moved, the phrase their agent responds to, the observed reply latency — is non-personal, survives deletion requests, and is what gets you 300 → 2000 without linear headcount. Write-behind: a candidate procedure edit is proposed from a successful workflow, then promoted only when it wins on replayed workflows. Versioned, with lineage back to the workflows that justified it, so a regression is attributable.

**Never written.** Card numbers, portal passwords — handles only. One-time codes are consumed in the ingest path and never reach storage or a prompt; redaction happens before the first write, not before display. Statement lines get normalized to a charge fact (merchant, amount, date, last4-of-handle) and the raw body is a TTL'd blob. And no chain-of-thought, no speculation, no "the merchant seems to have…". Speculation persisted becomes evidence to the next wake.

**Expiry.** Raw artifacts: 30 days or close + 7, whichever is later, hash retained. Ledger: workflow lifetime + retention window. Projections: transient. Merchant memory: indefinite. Deletion is per-user crypto-shredding — every user-scoped store encrypts under a per-user key, drop the key and the ledger, blobs, and projections all die together, even mid-workflow. The workflow then hard-fails to a terminal `abandoned_user_deleted` and the merchant-side statistics survive because they were never keyed to the user.

**The 1.2%.** That's a state-machine defect, not a memory one, and memory is where you fix it. `stopped` requires two independent attestations: a merchant-side confirmation *and* one full billing cycle with no charge on the feed. Until both, the state is `cancellation_asserted` and the user sees exactly that. You trade a slower truthful answer for never lying.

**Budget.** Ten cents over nine wakes means most wakes must not be inference at all. The fold classifies the stimulus; deterministic transitions (delivery receipt, retry, expected feed line) close without a model. Reserve inference for novel merchant replies and contested feed events.

Things I'd want in the same design rather than deferred: a policy layer over the ledger so retention and redaction are enforced at write, not by convention; lineage from merchant-memory versions to eval runs; and this as a standalone memory service — the durable-workflow shape generalizes past this agent, and I'd rather the next team adopt it than rebuild it.

<Verdict>

C buys two things no other attempt does, and sharpens a third. Keeping raw artefacts "30 days or close + 7,
whichever is later" is the only rule that carries the raw material through the 77-day tail — B strands its mail
bodies at day 30, and A keeps only embedded chunks of it. And C alone pins "the prompt + policy + fold version
into each StateTransition", so a week-nine judgement can be read back under the code that made it; B's upcasting
reader migrates the data, not the decision. Its attribution test is the sharpest of the three: a bad read is "an
Observation whose `extractor_ver` disagrees with `raw_ref` on replay", which is a test rather than a label on the
channel. The price is the wake brief. C's own words call it "cache-only" and "transient", rebuilt by a fold that
is "deterministic, pure" — an extra store that saves only CPU, and one C then has to key by "ledger offset *and*
fold version" to keep valid. C closes off the obvious objection (the projections "all die together" on a key
destroy), which is the point: the store is defensible and it is still a third moving part bought to avoid
recomputing a pure function. C's last paragraph shows the same instinct: "this as a standalone memory service",
offered to three engineers who owe 1,700 more merchant flows.

</Verdict>

## Where they actually disagree

Each disagreement below is a decision you will have to make yourself. The last entry is the exception: it is
the one thing all three did the same way, and none of them checked.

### The wake's read path: a model-written summary or typed facts only

A says the summary belongs there. It is read every wake, and rewriting it each wake means rewriting it from its
own predecessor. B says categorically no: "No rolling summary, no agent notes carried forward, no 'context'
blob … Never a prior model output as input — that is how a bad read becomes canon on wake seven." C agrees
("Speculation persisted becomes evidence to the next wake"). B and C are right, and the reason is mechanical:
A's own answer to the 1.2% is per-fact provenance, and a summary is one blob with one provenance covering mixed
sources. So A's schema can attribute the 1.2% on replay, while the summary a wake reads alongside it cannot —
and the summary is what carries the history once a case is older than three ledger entries.

### Evidence a charge stopped: a confirmation or an absence over a window

A: "only a bank-feed confirmation writes it". B: "no new charge past the next expected bill date, or an explicit
merchant confirmation ID plus one clean cycle." C: "two independent attestations: a merchant-side confirmation
*and* one full billing cycle with no charge on the feed." B and C are right on the mechanism. A bank feed emits
charges, not cancellations — the only feed evidence of a stopped subscription is an *absence* over a window, and
absence-of-evidence needs a named window. A never names one, so its "bank-feed confirmation" is a state
transition with no trigger.

### Deletion mid-workflow: pseudonymise and keep running or terminate

A pseudonymises and keeps running — "a tombstone that keeps the workflow runnable on pseudonymous state
(merchant, amount, stage) with identity fields nulled." B: "degrades to its pseudonymised typed facts or
terminates." C: "hard-fails to a terminal `abandoned_user_deleted`". All three honour the 30-day obligation the
prompt states; they differ on whether exercising a privacy right silently kills an in-flight money recovery. C
hard-codes losing it, and once the identity fields are gone there is nobody left to tell. A's default keeps the
recovery running. B is the only one that leaves both open — "degrades to its pseudonymised typed facts or
terminates" — but it is a bare disjunction, and B never says who picks or on what basis. All three leave that
unanswered, which is the gap: this is a policy question wearing a schema question's clothes, and none of the
three hands it to whoever should own it.

### Shared merchant knowledge: pinned per workflow or read live

C comes closest to pinning: the merchant card is "version-pinned", and each StateTransition carries "the prompt +
policy + fold version" — note that the playbook version is not itself in that list, so even C stamps the
machinery and not the merchant knowledge. B versions and eval-gates the playbook but retrieves it live by
`(merchant_id, state)`, migrating "facts and state position". A gives it a 180-day TTL plus "re-validate on
failure". C's instinct is the right one, and what makes it right is a consequence B states without drawing:
"three engineers cannot review 2,000 flows as code, but they can review diffs to 2,000 rows" is an argument about
reviewability, and reviewability at that scale implies the reach — a promoted row lands on every live workflow at
that merchant at once. So a workflow in week nine can switch playbook mid-flight, and no replay can say which
version drove which decision. None of the three closes that, and C only narrows it.

### A stricter close condition: absorbed by a cheap state or paid for in wakes

B says the mechanism that enforces it removes cost: "`pending_confirm` is cheap: it sleeps on feed diffs and
costs no inference. That state also absorbs your eleven-week tail, which is otherwise the thing that eats the
budget." C says it is bought: "You trade a slower truthful answer for never lying." A never meets the question,
having named no window at all. C is right that it is paid for, and neither sizes it. Requiring a full billing
cycle before a workflow may close moves typical close from six days toward thirty-odd, if the subscriptions bill
monthly. Every extra day sits in the open inventory. The ~45,000 concurrent workflows grow, each accruing wakes.
B is right that an idle `pending_confirm` wake costs no inference, and a wake that costs nothing subtracts
nothing — the objection is not that free wakes eat the allowance. It is that a longer hold does not only add free
wakes. A case held open for a billing cycle collects more merchant replies and more contested feed lines, and
those are exactly the wakes B routes *to* a model. At 4,000 starts a day a thirty-five-day mean puts about
140,000 workflows open at once instead of 45,000, holding three times the inventory for a year before the tail
even arrives. Neither attempt does that multiplication, and the page cannot do it for them: what a stricter close
costs depends on how many of the added wakes carry something a model has to read, which is a number this prompt
does not supply. That is the estimate a design owes when it moves the quality bar.

### What all three agreed on, and none of them priced

All three keep a durable record of things the mail thread and the bank feed already hold — what the merchant said,
what the bank shows. Take those two as durable and as the records a disputed claim gets settled against, and that
overlap becomes a divergence three engineers have to keep honest for as long as a workflow lives. Every
stale-memory false close starts in the overlap. What none of the three does is price the alternative: re-reading
those two sources at each wake instead of trusting a copy of what they said. The arithmetic is available. Ten
cents buys nine wakes at about a penny each; nine wakes over an eleven-day mean is a wake every day and a bit, so
an eleven-week case takes sixty-odd of them, all drawing on the same ten cents. Those cases are subsidised by the
six-day median today, and re-reading a growing thread on every one of sixty wakes is what spends the subsidy on
reconstructing what was already known.

Note the limit of that comparison, which is also why it is not a fourth attempt: the overlap is partial. Neither
the mail thread nor the bank feed holds the tool-call ledger of portal actions, or the state-machine position, so
a design that re-derives everything would have to re-drive the portals, not merely re-read two feeds. The honest
version is narrower than it first looks — and still unpriced by all three.

## The principle

> A summary carries one provenance for everything inside it, so nothing an agent may later have to defend should
> be read from one.

</Reveal>

:::tip[Read next]

- [Plan search & memory](/rag-agents/part-2-agents/planning-loops/deep-dive) — the handbook's memory
  taxonomy: working, episodic, semantic, procedural, and paging between a window and a store. Start here if the
  words in the attempts' diagrams are unfamiliar — and read its section on reflection buffers against what the
  attempts do, because the lesson and this page do not agree.
- [Sampling, SLOs & budgets](/rag-agents/part-1-rag/cross-cutting/observability/deep-dive) — redaction before
  the trace store, retention set by tier, and the reversible-versus-irreversible masking axis where a
  recoverable value makes the key itself the liability. This is what lets you judge whether a design that
  promises one deletion switch has named a mechanism or a slogan.
- [Graphs & durable execution](/rag-agents/part-2-agents/orchestration-frameworks/deep-dive) — checkpointers,
  `thread_id`, and what a woken process actually loads to resume. It is also where thread-scoped checkpoint
  state is separated from a cross-thread store keyed per user.
- [The arithmetic: context, caching, and the retry tax](/ai-sdlc/part-5-scale-governance/cost-economics/deep-dive)
  — the cost decomposition of one model call, and why re-sending state grows context cost quadratically in
  turns. The arithmetic behind deciding how many of nine wakes may be model calls at all.
- [Injection defence & red-teaming](/rag-agents/part-1-rag/cross-cutting/guardrails/deep-dive) — where PII gets
  caught and how it is masked, on input before the logs and the provider call, and detection priced as a
  precision/recall tradeoff. Relevant to any design that strips one-time codes with a pattern match.

:::

## If they push

These are the three follow-ups an interviewer reaches for next, and what each one exposes.

> A merchant changes its cancellation flow on Tuesday. Twelve hundred workflows are mid-flight against the old
> flow; forty of them are in week nine. What changes in your design — and what happens to the facts those forty
> are already carrying?

A memorised answer describes the new flow. The question is about the old one: stored derived state is now
wrong, and the design has to detect that, invalidate it, or re-derive it. The forty are the test, because their
stored facts are the oldest and the raw material behind them is the likeliest to have aged out under a
retention rule.

> A deletion request arrives for a user with three closed workflows and one open one. Enumerate every place a
> fact about them exists in your design, and say which a delete actually reaches. For any it cannot, say what
> you would have had to do differently at write time.

The enumeration is the whole question, and the primary store is the easy entry on it. The list is longer — indexes, event payloads, shared merchant facts,
traces, caches — and the answer has to say which of those a delete cannot reach. The harder half is what would
have had to be done differently at write time: deletion is a property you build in, not a job you schedule.

> Your inference budget drops to two cents per workflow. What is the first thing your design stops remembering,
> and which failure surfaces first?

Two cents across nine wakes is about a fifth of a penny each, which on the attempts' own figures does not fund a
single model call on a two-thousand-token context. So this is not a trimming exercise: it asks which wakes stop
using a model at all, and therefore which stored things stop being worth keeping. Ordering memory by marginal
value against the quality bar cannot be recalled from anyone's answer — it has to be derived from the one the
candidate gave.
