---
id: model-routing
title: Routing queries across models
sidebar_position: 1
description: When a router earns its own latency and cost — three attempts at cutting an LLM bill without silently losing answer quality.
---

# Routing queries across models

> You own the assistant feature inside a B2B web app: users ask questions and draft documents against
> content they've uploaded. Two million requests a day, peaking around 40,000 an hour. The mix is lopsided —
> roughly 70% are short lookups over one or two retrieved passages, 25% need a few paragraphs of synthesis,
> 5% are long multi-step drafting jobs. It's interactive and streamed: 800ms to first token at p95, full
> response inside six seconds for everything except the drafting jobs. Today every request goes to a single
> frontier model and the bill is $180k a month. You've been asked to take 40% out of that this quarter.
> Quality here means the answer is supported by the user's own documents — a confident wrong answer costs us
> far more than a slow one, and only a small fraction of output is ever seen by a human. Four engineers own
> this, sharing the product's on-call rotation. There's no ML team. Design it.

:::info[Why this question]

Cost work is where engineers reveal whether they optimise against measurements or against intuitions.

The theme invites a tidy answer — classify the query, dispatch to a tier — and that answer is a design
sketch, not an engineering plan: it spends latency and money on every request to save money on some, and it
ships no instrument that could tell you afterwards whether the trade was good.

So the question separates people who can hold three coupled budgets at once — money, latency, quality — and
reason about a change none of them can be evaluated in isolation, from people who can name the components of
a router. A weak answer reveals someone who has read about LLM routing and never had to defend a cost saving
against a quality regression they couldn't see.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard. The three
attempts below were written blind — each author saw only the prompt above, none saw the scoring rubric, and
none saw the others.

<details>
<summary>Show the three attempts</summary>

## Attempt A — the common answer

Let me draw it, because the shape of the problem is that we have one component doing three jobs.

**The seam is the router.** Right now the gateway is a pass-through: request in, frontier model out. I'd make
it a real layer with three responsibilities — classify, route, verify — and keep each one swappable behind an
interface, because whatever I pick today for classification I will replace in two months.

```text
client → gateway ──► cache ──► classifier ──► model pool
                                   │              ├─ small
                                   │              ├─ mid
                                   ▼              └─ frontier
                             grounding verifier ──► escalate
```

**Tiering the pool is where the 40% lives.** The mix hands it to us: 70% of traffic is a lookup over one or
two passages. That is not a frontier-model job. That's extraction with citation — a small model does it, and
the retrieval layer has already done the hard part. The 25% synthesis band goes to a mid-tier model. The 5%
drafting jobs stay on frontier, no argument; they're the ones with real reasoning depth and they're also the
ones not bound by the six-second SLA, so they're the least interesting cost-wise per request even though
they're the most expensive.

Moving the bulk of traffic down two tiers is a big multiple on the majority of requests. That gets us past
40% before we've touched anything else, and the remaining levers are gravy: prompt caching on the system
preamble and the tenant's document boilerplate, which is nearly free to turn on; and a semantic cache in
front of everything, keyed per-tenant so we never serve one customer's answer to another. In a B2B app with
shared uploaded corpora you get real repeat rates on lookups — same document, same questions, many seats.

**Classification.** Start with a cheap classifier — a small model call, or honestly a heuristic first pass on
query length, retrieved-passage count, and whether the request is a draft action from the UI, which the
product already knows. The product surface tells us a lot for free; drafting is a different button. Route on
that signal, and keep the classifier behind an interface so we can upgrade it to something learned later
without touching the pool.

**Now the quality problem, which is the actual risk.** Cheap models fail differently — they don't get slower,
they get confidently wrong, and nobody's reading the output to catch it. So the verifier isn't optional
garnish, it's a first-class box on the diagram. Every routed response gets a grounding check: is each claim
supported by the retrieved passages we actually gave it. Small model as judge, or an NLI-style entailment
check against the passages — cheap enough to run on the majority tier.

The elegant part is that verification composes with streaming instead of fighting it. We stream from the
cheap tier immediately, so first-token latency actually *improves* — small models are faster. The verifier
runs on the completed stream, and when it flags an ungrounded span we escalate that request to frontier and
re-render. That's a fallback path, not a hot path, so it only costs us on the tail.

**Rollout.** Shadow first — mirror production traffic to the routed path, compare against the frontier
answer, look at where they disagree. Then canary by tenant, five percent, with a global kill switch in config
that puts everything back on frontier in one deploy. Four engineers on a shared rotation means the router
config is a data file, not code: tier assignments, thresholds, escalation rules, all hot-reloadable. Nobody
should have to ship a binary at 3am to fix a routing decision — they flip the switch and we look at it
Monday.

**Verdict.** The architecture is right and the operations are the best-specified of the three: routing policy
as a hot-reloadable data file, per-tenant cache keys stated unprompted, canary by tenant with a one-deploy
global revert. It breaks on arithmetic and on streaming. "They're the least interesting cost-wise per
request even though they're the most expensive" dismisses the 5% drafting slice in the same clause that
concedes it dominates per-request spend — so "that gets us past 40% before we've touched anything else" is
asserted against a distribution nobody measured. And "verification composes with streaming" is false:
escalating after the stream completes means retracting text already rendered. The grounding judge is also a
second model call on 70% of traffic, unpriced.

## Attempt B — the strong answer

First thing I do is stop guessing where the money is. Two million requests at $180k is $0.003 a request
blended, and that average is lying to me. I want a cost histogram by segment: tokens in, tokens out, per
request class, per tenant. My prior is that the 5% drafting jobs and the retrieval context on everything else
are most of the bill, and request count is nearly irrelevant. You can't take 40% out of a distribution you
haven't looked at.

What I won't do: train a router. Four engineers sharing an on-call rotation and no ML team means every model
you own is a thing you retrain, monitor, and get paged for at 3am. Same reason I won't self-host a small
model to save on inference — GPU capacity planning for spiky interactive traffic is a full-time job you don't
have. Buy the small model from an API.

Three levers, in the order I'd ship them.

**Context hygiene and caching, first, because it's free.** Cache the system prompt and tool definitions —
that's a 90% discount on tokens you're paying full price for on every one of 60 million monthly calls. Then
cut top-k. If you're stuffing eight passages in and two of them answer the question, the other six cost money
*and* hurt you: distractor passages are a documented cause of ungrounded answers. A reranker in front, top-k
from eight to three, is cheaper and more grounded at the same time. Cap output tokens hard — you told me most
output is never read by a human, so verbosity is pure waste. Call it 15–20%, banked in a month, with no
quality risk.

**Then tier the 70%.** A short lookup over one or two passages is extraction, not reasoning. That's a
small-model job at roughly a tenth the price. The routing decision uses signals you already have — passage
count, retrieval score margin, whether the request came from the drafting endpoint — as deterministic rules.
Route on the *shape of the evidence*, not on a prediction of difficulty.

**The part that makes tiering safe is verification, not router confidence.** Require the cheap model to emit
span citations, then mechanically check that the cited spans exist in the retrieved passages and actually
cover the assertions. That's string work, sub-20ms, no model call. Fails the check, escalate to the frontier
model. Now escalation rate is your quality dial: you tune it, you watch it, and if it climbs you know
something upstream moved.

The honest cost is latency, and it's a real one. You cannot verify after you've started streaming without
retracting text on screen, which is worse than being slow. So for short lookups I don't stream from the model
— I generate the whole thing, which for a two-sentence answer on a small model is 300–400ms, verify, then
stream the buffer out. TTFT lands well inside 800ms. For the 25% synthesis I stream directly from the mid or
frontier model and verify asynchronously, feeding a dashboard rather than a gate. Drafting jobs I touch last:
decompose them so the planning step uses the frontier model and the sub-steps drop a tier.

**Nothing ships without an eval, and this is the constraint that shapes everything.** Because almost no
output is human-seen, you have no thumbs-down signal — silent wrong answers stay silent. So pay once for
500–1000 human groundedness labels on sampled real traffic, calibrate an LLM judge against them, report the
agreement number so everyone knows what the judge is worth. That runs in CI on every prompt, model, and
routing change. New paths go to shadow first — same traffic, both models, compare judged groundedness and
escalation — then 5%, 50%, 100%.

Rollout: instrumentation and eval weeks 1–3, saving nothing. Caching and context trim week 4, banks 20%.
Router plus verifier through week 9. Every routing decision logged with its reason, per-tier kill switch that
sends everything back to the frontier model with one config flag.

Expected landing: 45–55%. I want the headroom because the first time groundedness dips, I'm going to spend
some of it backing off — and I'd rather explain a 40% cut than a hallucination in a customer's contract
draft.

**Verdict.** The only attempt that computes before it designs — $0.003 blended, "that average is lying to
me" — and the only one that banks the free levers first: prompt caching, top-k from eight to three, hard
output caps, roughly 20% with no quality risk. It resolves the conflict A gets wrong, buffering short answers
at 300–400ms and verifying asynchronously on the synthesis tier. The crack is inside the verifier: checking
that cited spans *exist* is string work at sub-20ms, but checking they "actually cover the assertions" is
entailment, and no string comparison performs it. The quality dial is softer than claimed. Deferring drafting
to last also contradicts its own opening prior about where the money sits.

## Attempt C — the over-built answer

The 40% is a symptom. The real statement of the problem is: we have no policy layer. Every request,
regardless of what it needs, gets the most expensive possible execution path, and we have no mechanism that
could ever decide otherwise. Solve that once and the 40% falls out as a side effect — and so does the next
ask, when someone comes back in March wanting another 30%, or wanting the drafting jobs to get *better*
rather than cheaper.

So I'd build the routing and evaluation substrate, not a cost cut.

**Layer one — an inference gateway.** Everything goes through one service. All model calls become a
capability request — "answer this, grounded in these passages, under this latency budget" — not a call to a
named vendor endpoint. Behind it, a model registry: the frontier model, a mid-tier, one or two small
open-weight models we serve ourselves on vLLM with continuous batching and prefix caching, and later our own
distilled model. Nothing in the product code names a model ever again. That's the abstraction that makes
everything after it possible.

**Layer two — routing as a learned policy, not an if-statement.** The naive version is a classifier on
request shape: short lookup → cheap model, synthesis → mid, drafting → frontier. I'd ship that as the
bootstrap, but hand-tuned thresholds rot within a quarter as the traffic mix drifts. What I actually want is
a contextual bandit over the model set, features being retrieval-set size, passage entropy, query embedding
cluster, tenant, and history; reward being a composite of grounding score, latency, and cost. It explores on
a small slice of traffic continuously, so the routing policy keeps improving without anyone tuning it. That's
the closed loop. A rules table is a snapshot of one afternoon's understanding; a bandit is a system that
keeps learning after we stop paying attention to it.

**Layer three — grounding as a measured signal.** You told me a confident wrong answer is the expensive
failure and almost nothing is human-reviewed. That means we cannot route on cost without a continuous,
automated measure of faithfulness. So: an entailment check of every claim against the retrieved passages, run
as a small self-hosted NLI model on a sampled slice, plus an LLM-judge on a smaller slice with human-labelled
calibration. That score is the reward signal for the router and the gate for promotion. On low-confidence
outputs, escalate to the frontier model and re-answer — cascade, not gamble.

**Layer four — the eval and observability platform.** A golden set per tenant segment, versioned. Every
model, prompt, and routing-policy change replays against it in CI. Shadow traffic for anything new.
Per-request cost, latency, grounding, and route attribution in a warehouse, with dashboards and alerts on
grounding drift, not just error rate. Feature store for the router features so training and serving don't
skew.

**Then harvest.** Semantic cache in front — 70% short lookups over a shared corpus means real hit rates.
Prefix-cache the system prompt and document context. Distill the frontier model on our own logged traffic for
the lookup class; that's where the step-change is, and it's only safe because the eval harness can prove it.
Speculative decoding on the self-hosted tier for the 800ms budget.

On four engineers: that's precisely the argument *for* this. Four people cannot hand-tune routing rules
forever while carrying on-call. They can own one gateway with a policy that tunes itself and a harness that
tells them when it's wrong. The automation is what makes the headcount survivable.

Sequencing: gateway and telemetry first — you cannot optimise what you can't attribute. Eval harness second.
Bootstrap classifier plus cache next, and that alone lands near 40%. Bandit and distillation follow, which is
where we get to 60% and a system that keeps compounding instead of being re-litigated every quarter.

**Verdict.** Layer one and layer four are correct and undervalued: capability requests instead of vendor
endpoints, and per-request route/cost/grounding attribution, are what make any later savings claim checkable
at all. Then it funds them with a bill four people cannot carry. The bandit's reward is "a composite of
grounding score, latency, and cost", but grounding comes from a sampled judge — the policy trains on its own
estimator's noise, with no human in the loop and no retraining owner named. vLLM, speculative decoding, a
feature store and a distilled model each add a 3am owner; "the automation is what makes the headcount
survivable" inverts that. Its semantic cache asserts hit rates with no tenant-isolation rule, which A stated.

## Where they actually disagree

The gaps between the attempts are worth more than any of them alone, because each disagreement is a decision
you will have to make yourself.

**Can you verify after streaming has started?** A says the verifier runs on the completed stream and
escalation re-renders. B says that means retracting text on screen and buffers short answers instead. Same
architecture, opposite user-visible failure — and B is right.

**Should the policy be written or learned?** B routes deterministically on evidence shape and refuses to own
a model. C argues a rules table is "a snapshot of one afternoon's understanding" and that drift outruns four
engineers' maintenance. That concern is legitimate; it dies on the missing request-time reward signal, not on
the ambition.

**What is the 5% drafting slice?** A calls it the least interesting cost-wise. B's prior is that it and the
retrieval context are most of the bill. That single disagreement decides whether 40% is reachable from the
70% slice at all — and neither of them can settle it without the measurement B insists on taking first.

## The principle

> Downgrading a model is only safe on traffic whose output carries a mechanically checkable artifact — a
> citation, a schema, a tool result — because a misroute never pages anyone, it just returns a plausible
> answer nobody flags.

</details>

:::tip[Read next]

- [Why AI systems fail in production](/rag-agents/part-3-production/production-failures) — the arithmetic all
  three attempts are judged against: the unit is cost per *accepted* answer, and a cheap model wins only when
  its acceptance rate beats the price ratio. Also the cheapest-gate-first ordering — schema, then citations,
  then a judge.
- [LLMOps — deploy, monitor, cost](/rag-agents/part-3-production/llmops/) — the catalogue every attempt draws
  its levers from, with the honest clauses attached: prompt caching and its write premium, semantic caching
  and its false-hit risk, eval-in-CI, and why "a canary that answers fast, cheap, and slightly wrong is a
  failing canary."
- [Metric internals and judge calibration](/rag-agents/part-1-rag/cross-cutting/evaluation/deep-dive) — why
  faithfulness scores 1.0 on an answer grounded in the wrong context, and what B's 500–1000 labels actually
  buy: a judge-versus-human agreement number, and the systematic biases more data will not wash out.
- [Serving — FastAPI and Docker](/rag-agents/part-3-production/serving/) — the paragraph that settles the
  sharpest disagreement above: validating a streamed answer forces a choice between buffering and letting a
  bad prefix reach the user.
- [Sampling, SLOs and budgets](/rag-agents/part-1-rag/cross-cutting/observability/deep-dive) — per-request
  token accounting and cost attribution by feature, tenant, route and model, plus the rule that a service
  100% available and 30% hallucinating still meets its uptime SLO.

:::

## If they push

**"Do the arithmetic with me. Your router runs before every request. 70% of traffic is the cheap slice, p95
to first token is 800ms. What's the most that router can cost, and how accurate does it have to be before
this starts losing me money — and what's the loss when it routes wrong?"**
Whether the tiering was reasoned or recited. The reasoner reaches for expected value — savings on correct
downgrades, minus router cost on 100% of traffic, minus the cost of wrong downgrades — and notices that the
last term is the one they cannot price without an eval.

**"Six weeks in, the bill is down 45% and you're happy. How do you know you haven't shipped a quality
regression? And what would you have had to build in week one to be able to answer that today?"**
Counterfactual thinking. Routing changes quality invisibly by construction: nobody complains about the answer
they didn't get. Only someone who reasoned to shadow sampling or a held-out paired comparison can answer the
second half, because the instrument had to exist before the change.

**"Peak hour. Your strongest model starts returning 429s and 40-second timeouts for the next half hour. Walk
me through what happens to the 5% of long drafting jobs."**
Fallback design under the only conditions that test it. The trap answer degrades the hardest workload onto
the weakest model at the worst moment and calls it resilience.
