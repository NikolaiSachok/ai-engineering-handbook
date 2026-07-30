---
id: agent-memory
title: What an agent should remember, and what it must not
sidebar_position: 4
description: What a long-running agent persists, what it lets expire, and what it may never write down. Three attempts at a workflow that runs for weeks, wakes on a newer deploy each time, and must never tell a user their money is safe when it isn't.
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

Two of the postings this course samples ask for memory across multi-step workflows, which usually gets read as
"wire up a store". The phrase hides three different obligations, and this prompt pulls them apart. What
**persists** is whatever a woken process may read to work out where it had got to. What **expires** is whatever
stops being allowed to exist once a retention rule or a deletion request reaches it — and *reaching* it is the
work, because one fact copied into an index, a trace and a cached prompt has to die in all four places. What is
**never written** is different in kind again: material that must pass through the agent and must not survive
it, like a one-time code that has to be usable and must not be storable.

The axis under test is what a wake is allowed to trust. Any answer will produce a list of things to store; what
separates them is whether the list keeps what the world reported apart from what the agent concluded, and
whether it prices that against the per-wake budget it actually has.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard.

Three model-written attempts follow. Each comes from a separate agent given one engineer's habits and the
prompt above. No agent saw the other two, and none saw the scoring standard the verdicts are written against —
that was fixed before any attempt existed, and a separate assessor applies it. The attempts introduce figures
of their own; where one of those is load-bearing and unchecked, the verdict under that attempt says so. The
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

The judged move is the rolling summary — "rewritten each wake so the eleven-week outliers don't grow
unbounded" — read back on every wake. It buys bounded context on a 77-day workflow, and A alone says where the
mail alias and vault handles live. It costs A its own best idea: A tags every fact with `source`
(`bank_feed` / `tool_result` / `model_inference`) and rightly calls that "exactly what's missing today", then
funnels mixed-provenance content into one prose blob under one tag, laundering the attribution its own 1.2%
answer depends on. The read path is unpriced too — "a couple of thousand tokens … sits comfortably inside the
per-wake share" asserts the arithmetic instead of doing it, and never names a model tier, the one thing that
decides whether it is true. One-time codes are also both "never persisted" and given "a 15-minute TTL".

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
`pending_confirm` state that "sleeps on feed diffs and costs no inference". That is the strongest move on the
page. Two cracks. "Never a prior model output as input" is falsified by B's own read list — the 800-token
merchant playbook is model-proposed ("The agent may *propose* playbook changes from observed failures"); the
honest rule is never *ungated* model output, and the risk simply moved into one eval gate on a fact shared by
every open workflow at that merchant. And "TTLs: raw mail 30 days" strands every `artifact_ref` on an
eleven-week workflow at day 30, while traces "carry IDs, not content" — the evidence expires while the case is
still open. The 60/40 split is invented.

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

Credit first: three things here nobody else buys. Raw artifacts kept "30 days or close + 7, whichever is
later" is the only retention policy that survives the 77-day tail. Pinning "the prompt + policy + fold version
into each StateTransition" is the only design where a week-nine workflow stays interpretable on a newer deploy.
And its attribution test is the sharpest — a bad read is "an Observation whose `extractor_ver` disagrees with
`raw_ref` on replay", separating bad parse from bad tool. The price is the WAKE BRIEF, which C's own words call
"cache-only", "transient", rebuilt by a fold that is "deterministic, pure": a third store that saves only CPU,
yet still needs a version key and a deletion entry. Same instinct in the closer — "this as a standalone memory
service" — offered to three engineers who owe 1,700 more merchant flows.

</Verdict>

## Where they actually disagree

**1. Does a model-written summary belong in the wake's read path?**
A says yes — the rolling summary is read every wake and rewritten from its own predecessor. B says categorically
no: "No rolling summary, no agent notes carried forward, no 'context' blob… Never a prior model output as input
— that is how a bad read becomes canon on wake seven." C agrees ("Speculation persisted becomes evidence to the
next wake"). **B and C are right, and the reason is mechanical rather than stylistic:** A's own answer to the
1.2% is per-fact provenance, and a summary is one blob with one provenance covering mixed sources. The summary
destroys exactly the attribution A built the schema to provide.

**2. What counts as bank-feed evidence that a charge stopped?**
A: "only a bank-feed confirmation writes it." B: "no new charge past the next expected bill date, or an explicit
merchant confirmation ID plus one clean cycle." C: "two independent attestations: a merchant-side confirmation
*and* one full billing cycle with no charge." **B and C are right on the mechanism.** A bank feed emits
charges, not cancellations — the only feed evidence of a stopped subscription is an *absence* over a window,
and absence-of-evidence needs a named window. A never names one, so its "bank-feed confirmation" is a state
transition with no trigger.

**3. What happens to an open workflow when a deletion request lands?**
A pseudonymises and keeps running — "a tombstone that keeps the workflow runnable on pseudonymous state
(merchant, amount, stage) with identity fields nulled." B: "degrades to its pseudonymised typed facts **or**
terminates." C: "hard-fails to a terminal `abandoned_user_deleted`." All three are compliant; they differ on
whether exercising a privacy right silently kills an in-flight money recovery. C's is the harshest and the only
one that loses the user's refund with no way to tell them — you just deleted them. **A's default is the most
user-serving here, and B's is the best framed**, because B is the only one that states the choice exists rather
than hard-coding it. This is a product decision the reader has to make, not a completeness gap.

**4. Should shared merchant knowledge be pinned to the workflows running under it?**
C says yes — "version-pinned", with the fold, policy and prompt version stamped into each StateTransition and
"lineage back to the workflows that justified it, so a regression is attributable." B versions and eval-gates
it but does not pin per workflow: B migrates "facts and state position", and its playbook is retrieved live by
`(merchant_id, state)`. A gives it a 180-day TTL plus "re-validate on failure". **C is right, and it is right
about the thing B itself named as the danger.** B's own argument — "three engineers cannot review 2,000 flows as
code, but they can review diffs to 2,000 rows" — implies a bad promoted row steers every live workflow at that
merchant the moment it lands. Without a pin, a workflow in week nine silently switches playbook mid-flight and
no replay can say which version drove which decision. C paid for a lot of machinery; this is one place it earns
its keep.

**5. Is the stronger evidence bar free?**
B says the mechanism enforcing it takes cost away: "`pending_confirm` is cheap: it sleeps on feed diffs and
costs no inference. That state also absorbs your eleven-week tail, which is otherwise the thing that eats the
budget." C says it is bought, and names the currency: "You trade a slower truthful answer for never lying." A
never meets the question, having named no window at all. **C is right that it is paid for, and both are wrong
about the size.** Requiring a billing cycle before a workflow may close moves typical close from six days
toward thirty-odd, and every extra day sits in the open inventory — the ~45,000 concurrent workflows grow, each
accruing wakes, and wakes are the unit the $12,000 is divided into. B is correct that an idle `pending_confirm`
wake costs no inference; what gets charged is the *number* of them, and neither attempt multiplies it.
Strengthening the quality bar and holding the budget draw on the same account, so a design that moves one owes
an estimate to the other.

## The position nobody took

A fourth position is available here, and none of the three takes it: persist almost nothing, and re-derive the
workflow's state at each wake from the mail thread and the bank feed. Those two are already durable, already
externally auditable, and already the records a disputed claim will be settled against — a second copy is a
divergence bug three engineers have to keep honest forever, and not having one removes every stale-memory false
close at the root. What defeats it is the budget: ten cents buys roughly nine wakes at a penny each, and
re-reading an eleven-week thread on the three-in-a-hundred workflows that wake forty-odd times spends the
entire envelope on reconstructing what you already knew. It is the cheapest design to own and the most
expensive to run; which of those two you can afford is the decision.

## The principle

> A summary can only ever cite itself, so nothing an agent may later have to defend should be read from one.

</Reveal>

:::tip[Read next]

- [Plan search & memory](/rag-agents/part-2-agents/planning-loops/deep-dive) — the handbook's memory
  taxonomy: working, episodic, semantic, procedural, and paging between a window and a store. Read it knowing
  it argues the *other* side of the summary question, presenting a model-written reflection buffer read back on
  the next attempt as the canonical pattern.
- [Sampling, SLOs & budgets](/rag-agents/part-1-rag/cross-cutting/observability/deep-dive) — redaction before
  the trace store, retention set by tier, and the reversible-versus-irreversible masking axis where a
  recoverable value makes the key itself the liability. This is what lets you judge whether per-user key
  destruction is a mechanism or a slogan.
- [Graphs & durable execution](/rag-agents/part-2-agents/orchestration-frameworks/deep-dive) — checkpointers,
  `thread_id`, and what a woken process actually loads to resume. It is also the only page that separates
  thread-scoped checkpoint state from a cross-thread store keyed per user.
- [The arithmetic: context, caching, and the retry tax](/ai-sdlc/part-5-scale-governance/cost-economics/deep-dive)
  — the cost decomposition per attempt, and why re-sending state grows context cost quadratically in turns.
  The arithmetic behind "most wakes must not be model calls".
- [Injection defence & red-teaming](/rag-agents/part-1-rag/cross-cutting/guardrails/deep-dive) — where PII gets
  caught and how it is masked, on input before the logs and the provider call, and detection priced as a
  precision/recall tradeoff. Relevant to any answer that strips one-time codes with a pattern match.

:::

## If they push

The interviewer has your design and now goes looking for the seams. Each of these is easy if you reasoned your
way to your answer and fatal if you recited someone else's.

> A merchant changes its cancellation flow on Tuesday. Twelve hundred workflows are mid-flight against the old
> flow; forty of them are in week nine. What changes in your design — and what happens to the facts those forty
> are already carrying?

A memorised answer describes the new flow. The question is about the old one: stored derived state is now
wrong, and the design owes a way to detect that, invalidate it, or re-derive it. The forty are the test, because
they are the ones whose stored facts are oldest and whose replay window has most likely expired.

> A deletion request arrives for a user with three closed workflows and one open one. Enumerate every place a
> fact about them exists in your design, and say which a delete actually reaches. For any it cannot, say what
> you would have had to do differently at write time.

Rehearsed answers name the primary store. The enumeration is the point — indexes, event payloads, shared
merchant facts, traces, caches — and so is the admission of which are unreachable. "What you would have done
differently at write time" is where the second half of the question lives: deletion is a property you build in,
not a job you schedule.

> Your inference budget drops to two cents per workflow. What is the first thing your design stops remembering,
> and which failure surfaces first?

This cannot be recalled, only derived: it asks the candidate to rank their own memory tiers by marginal value
against the quality bar they committed to, and then to name what breaks. An answer that trims everything
evenly has no ranking.
