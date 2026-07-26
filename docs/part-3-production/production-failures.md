---
id: production-failures
title: Why AI systems fail in production
sidebar_label: Why AI fails in production
sidebar_position: 0
---

# Eight ways a working demo dies in production

<Infographic
  src="/img/infographics/production-failures/hero.webp"
  alt="A small tidy demo platform and a much larger production platform, joined by a bridge with its middle section missing and warning signs scattered across the gap"
  caption="The gap this part of the handbook exists to close — eight failures, and the shape that answers each."
/>

A demo has to win once, on a path someone chose. Production has to catch itself on the paths nobody
scripted, thousands of times a day, while the people who built it are asleep. Those are two different
engineering problems, and the list below is the bill for having solved only the first one.

Read the eight cards as a map rather than a warning. Each one names a failure, shows the shape that answers it,
and points at the lesson where the mechanism is actually taught. Some you have already met — retrieval quality
in Part I, tool failure in Part II. The rest are what this part is for. And if a single thread runs through all
of them, it is this: **almost nothing here is a model failure.** The model is the one component you did not
write. Everything around it is yours.

:::note[Where this map comes from]

These eight are the failure modes that circulate widely in production-AI discussion; the arrangement here was
prompted by a much-shared infographic from Alex Xu (ByteByteGo). Two deliberate differences. That version
shows only the failures, which is the honest scope of a diagnostic poster — these cards show the **production
shape** alongside each failure, because knowing that data arrives messy is not the same as knowing what to
build. And in three places we disagree with the popular fix: on drift, on eval sets, and on routing to a
cheaper model. Each disagreement is flagged where it comes up.

:::

## 1 · The corpus is the product

<Infographic
  src="/img/infographics/production-failures/01-corpus.webp"
  alt="A demo lane where clean uniform documents go straight into an index, a document falling out of it marked 'silently dropped', and a production lane running mixed sources through layout-aware chunking into an ingestion manifest"
  caption="Production ingestion reports what it took, what it dropped, and what it never saw."
/>

The demo corpus is a folder someone curated. Production is PDFs with two-column layouts, spreadsheets whose
meaning lives in the header row, wiki pages half-migrated from a tool that died, and scans. The common advice —
validate schemas at ingestion — is right for records and misses the target for documents, because the thing
that breaks a RAG answer is rarely a malformed field. It is **structure**: a table flattened into prose, a
footer glued onto every chunk, and above all a chunk boundary that separates a fact from the qualifier that
made it true. "Rates rose 4%" is not wrong until you cut it away from "in the 2019 pilot only."

Worse, a strict validator fails *quietly*. It drops the documents that don't conform, the index comes up
looking healthy, and the model answers from a partial corpus — confidently, because nothing told it that a
third of the source material never arrived. So the production shape is not a stricter gate, it is a
**manifest**: ingestion reports what it *included*, what it *excluded and why*, and where its *blind spots*
are, as a build artefact you can read. An excluded document is a decision; an excluded document nobody can
enumerate is a defect. The mechanics — parsing, layout, chunking strategies, metadata — are
[ingestion](../part-1-rag/ingestion/index.md).

## 2 · Retrieval has to be allowed to say no

<Infographic
  src="/img/infographics/production-failures/02-retrieval.webp"
  alt="A demo pipeline that always returns top-k, against a production pipeline where a score floor after reranking permits an empty result"
  caption="A relevance floor applied after reranking, and a generator allowed to answer 'no context'."
/>

This is the failure that costs teams the most time, because the system looks healthy the whole way through.
Nothing errors. The service returns 200. The wrong chunks simply arrive, and the model does what it was built
to do — write a fluent answer from whatever it was given.

Grading retrieval separately from generation is the diagnostic half, and Part I makes that case: without the
split you cannot tell a retrieval miss from a model that ignored good context, and you will spend a fortnight
tuning a prompt to fix an indexing bug. But the *production* half is a refusal path, and it is the piece most
demos have no concept of. A demo returns **top-k, always** — top-k is a slice, not a judgement, and a
similarity ranking will hand back its best five candidates whether or not any of them is about your question.
So put a **score floor** after the stage whose scores mean something. Fused hybrid scores — dense and lexical
rankings combined — are not calibrated on a comparable scale, so a threshold on a fusion score is
approximately arbitrary; a cross-encoder reranker's score is the one you can actually tune a floor against.
Below the floor, retrieval returns **an empty set on purpose**, and the generator says it has no supporting
context instead of assembling something plausible from a weak batch.

That last step only works if the generator was built to refuse — which
[generation](../part-1-rag/generation/index.md) argues at length, and
[retrieval](../part-1-rag/retrieval/index.md) supplies the hybrid search and reranking that make a meaningful
floor possible. The demo answers everything. The production system is allowed to say no.

## 3 · One eval set is not enough

<Infographic
  src="/img/infographics/production-failures/03-eval-sets.webp"
  alt="A demo lane where a day-one test set leads to a green dashboard labelled 'false confidence', and a production lane where a frozen set and a live sample together feed one honest scoreboard"
  caption="Two sets, two different questions: did I break what worked, and does my eval still resemble reality?"
/>

Test cases written in week one describe how the team imagined people would ask. Six months of real traffic
describes how they actually ask, and the gap is where a green dashboard starts lying. The usual prescription is
to sample live traffic weekly and use that as the benchmark — and here is our first disagreement, because
*replacing* the fixed set trades one blindness for another. A benchmark that changes every week cannot tell you
whether this week's change broke something that worked last week; that is what a frozen set is for.

Keep both. A **frozen regression set** answers "did I break what worked," and it has to stay still to answer
it. A **rotating set sampled from live traffic** answers "does my evaluation still resemble reality," and it
has to move. There is a second reason to rotate, which comes from the other direction: a fixed benchmark that
the team optimises against for months stops measuring quality and starts measuring familiarity with the
benchmark. Both sets need labels, which is the part nobody budgets for —
[evaluation](../part-1-rag/cross-cutting/evaluation/index.md) is blunt about that: no dataset, no evaluation.

## 4 · Green is not the same as correct

<Infographic
  src="/img/infographics/production-failures/04-green-not-correct.webp"
  alt="A healthy dashboard beside a wrong answer, with a pipeline trace and a sampled judge added"
  caption="Uptime is a property of the service. Correctness is a property of the answer."
/>

Every standard signal can be healthy while the system is wrong. Latency is fine, error rate is zero, the pod
is up — and the answers are confidently incorrect, because no ordinary monitor has an opinion about the
*content* of a 200. Uptime is a property of the service; correctness is a property of the answer, and you
cannot infer the second from the first.

Two things close the gap. A **trace** that records the whole path of one request — the query, which chunks came
back and with what scores, the prompt as sent, the answer, the tokens — because without the chunk identifiers
you cannot even reconstruct *why* an answer was wrong. And an **independent judge sampling live traffic**, so
that quality is a monitored metric with a threshold and an alert, not something you discover from a support
ticket. That's [observability](../part-1-rag/cross-cutting/observability/index.md), and the loop where it feeds
eval.

One thing to design deliberately rather than inherit: logging sized for debugging is not logging sized for
proof. Debugging wants the last few days in as much detail as you can afford. An audit — a regulated
industry, a disputed answer, a customer asking what your system told them in March — needs to reconstruct what
was retrieved and returned *months later*, which is a retention and integrity requirement, not a verbosity
setting. Decide which one you are building before an auditor decides for you.

## 5 · The unit is cost per accepted answer

<Infographic
  src="/img/infographics/production-failures/05-cost.webp"
  alt="Three cheap attempts against one expensive attempt, with the retry tax marked"
  caption="A cheaper model only wins if its success rate beats the expensive one by more than the price gap."
/>

Costs that look like rounding errors in a demo compound in three ways at once: agents retry, conversations
re-send their entire history every turn, and users paste whole documents into a box you sized for a sentence.
The re-send is the one people miss — a stateless model re-reads the transcript on every turn, so a task that
runs twice as long costs roughly four times as much, and trimming what rides in context is the highest-leverage
lever you have. A stable prompt prefix that can be cached is worth more than most model shopping.

Which brings the second disagreement: *route routine work to a lighter model* is advice with a condition
attached, and the condition is usually left out. The unit that matters is cost per **accepted** answer, not
cost per token, so a cheaper model that needs three attempts where the expensive one needed one is not
cheaper — that gap is the **retry tax**:

```text
cost_per_accepted ≈ attempt_cost / p          (p = first-try acceptance rate)

the cheaper model wins only when:
    p_cheap / p_expensive  >  price_cheap / price_expensive
```

Half the price buys nothing at less than half the reliability. Measure `p` per route before you believe a
saving. [LLMOps](./llmops/index.md) covers the levers — routing, caching, the batch tier, budgets that
actually close the loop — and the AI-SDLC course works the same arithmetic out for a different unit, cost per
accepted code change.

## 6 · Re-index before you retrain

<Infographic
  src="/img/infographics/production-failures/06-drift.webp"
  alt="A demo lane going straight from detected drift to retraining the model, and a production lane stepping through re-index, retrieval mix and prompt before reaching a greyed-out chip labelled 'weights last'"
  caption="Three drifts, one ladder — and weights are the last rung, not the first."
/>

Quality decays without a deploy. Users bring new vocabulary, the documents underneath change, and a hosted
model you didn't pin moves under you. This is the third disagreement, and the sharpest one: the standard
reflex — wire drift thresholds to trigger **retraining** — is an MLOps answer imported into a system whose
weights are almost never the problem.

In a retrieval system, drift is usually a **corpus** or a **query** phenomenon, so the ladder starts far below
the model: re-index and re-chunk, adjust the retrieval mix, revise the prompt, and only then consider touching
weights — which for most teams means a vendor's next release rather than a training run. Three flavours of
drift and how to watch each are in [LLMOps](./llmops/index.md). The useful corollary is that **the corpus is a
release**: it deserves a version, a diff, and a rollback, exactly like code.

## 7 · The prompt and the corpus are releases

<Infographic
  src="/img/infographics/production-failures/07-releases.webp"
  alt="A versioned prompt, a pinned model and a corpus snapshot moving through a canary release with a rollback path"
  caption="Everything that changes behaviour needs a version and a way back."
/>

When a prompt lives inside application code, editing a sentence is a deployment — so a copy fix carries
deployment risk, and nobody dares treat it as the small change it is. Lift prompts into **version-controlled
config** with their own quality gates and the harness becomes diffable and revertible instead of something you
pray over.

Then apply the same standard to everything else that changes behaviour without changing code: **pin the model
version**, **snapshot the corpus**, roll out through a canary, and keep a rollback path for each of the three
independently. A system where the prompt, the model and the index can all shift underneath you has no
reproducible state at all, and no amount of testing fixes that. The release mechanics are in
[LLMOps](./llmops/index.md).

## 8 · A pipeline needs gates between the steps

<Infographic
  src="/img/infographics/production-failures/08-gates.webp"
  alt="A multi-step pipeline with validation gates between stages, ordered cheapest check first"
  caption="Each stage rejects bad input, and the cheapest check runs first."
/>

In a multi-step pipeline, the first bad output becomes the next step's trusted input. A retrieval miss becomes
a confident summary, which becomes a decision, and by the time anything looks wrong the original error is
several transformations back. Validation between the steps is the answer, and every stage should be built to
**reject** bad input rather than do its best with it — a stage that never refuses is a stage that launders
errors.

The refinement worth adding is **ordering**. Gates are not equally expensive: a schema check costs
microseconds, a citation-grounding check costs a retrieval, a model-graded judgement costs a model call. Run
them cheapest-first, so the failures a regex could have caught are never paid for at judge prices. That
ordering argument is developed properly in the AI-SDLC course's layered-gates lesson; the RAG-side machinery —
what to guard on input, output and at ingestion — is [guardrails](../part-1-rag/cross-cutting/guardrails/index.md).

## 9 · Four that rarely make the list

<Infographic
  src="/img/infographics/production-failures/09-four-missed.webp"
  alt="Four quadrants: unscoped access, poisoned documents, one-language testing, and flaky tools"
  caption="Four failures the standard lists skip — and the last one fails before the model does."
/>

Four more, each of which has taken down a production system while everyone was watching the eight above.

**Unscoped access.** In the demo the agent runs with credentials that make everything work, and the index holds
every document the crawler could reach. In production that same arrangement is a data-exfiltration channel:
retrieval that isn't filtered by the caller's entitlements will happily quote a document the caller was never
allowed to open. Permission-aware retrieval is not a feature you add later — it changes the shape of the index.

**Poisoned documents.** Retrieved text is untrusted input. A document containing instructions can hijack the
model that reads it, which makes indexing time — not query time — the cheapest place to catch it.

**One language.** An embedder and a reranker trained on English will miss relevant English documents when the
question arrives in another language, and the failure is silent: fewer results, all plausible. If your users
are multilingual and your evaluation isn't, you have not measured the system your users have.

**Flaky tools.** The tools fail before the model does. APIs time out, an MCP server restarts, a vector store
rejects a connection — and an agent with no timeout, no retry and no fallback answer just hangs, which users
read as broken rather than slow. Degrade to a worse answer on purpose; the [tool-use](../part-2-agents/tool-use/index.md)
lesson covers the round-trip and its failure handling.

## What to take away

- **Almost none of these are model failures.** The model is the component you didn't write; the failures live
  in the system around it.
- **Ingestion should report, not just validate** — included, excluded with a reason, and blind spots. A silent
  drop produces a confident answer from a partial corpus.
- **Retrieval needs a refusal path**: a score floor after reranking, an empty set on purpose, and a generator
  that will say it has no context.
- **Two eval sets** — one frozen for regressions, one rotating from live traffic for reality. Neither replaces
  the other.
- **Uptime is not correctness.** Add a trace with chunk identifiers and a judge on sampled traffic; decide
  separately whether you owe anyone an audit trail.
- **Cost per accepted answer** is the unit. `cost ≈ attempt_cost / p`, and a cheaper model must beat the price
  ratio on reliability.
- **Drift is answered by re-indexing** long before retraining; the corpus is a release, with a version and a
  rollback.
- **Prompt, model version and corpus** each need a version and a way back, or the system has no reproducible
  state.
- **Gates between steps, cheapest first** — every stage rejects bad input instead of laundering it.
- **And the four nobody lists**: unscoped access, poisoned documents, one-language testing, flaky tools.

Part III now builds the answers: [serving](./serving/index.md) the system, the
[cloud platforms](./cloud-platforms/index.md) it runs on, the
[tooling ecosystem](./tooling-ecosystem/index.md) that measures and guards it, and
[LLMOps](./llmops/index.md) for its life after release.

**New terms**: score floor / relevance floor, ingestion manifest, blind spot (ingestion), frozen regression
set, rotating live-sampled set, benchmark familiarity, audit-grade logging, cost per accepted answer, retry tax,
drift response ladder, corpus as a release, permission-aware retrieval, cross-lingual retrieval gap, graceful
degradation (tools). All fourteen are defined in the glossary, under *Production — why AI fails in production*.
