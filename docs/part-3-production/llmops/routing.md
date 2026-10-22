---
title: "Model routing — cost and latency"
sidebar_label: "Routing cost & latency"
sidebar_position: 3
---

# Model routing: pay for the whole request

[LLMOps](./index.md#route-between-models) introduced routing between models. A routing policy earns its place only if the deployed system meets quality, cost, and latency targets together. Sending 70% of requests to a small model does not imply saving 70% of the bill. Checking its answer before release may also consume the entire first-token budget.

This companion works through those two traps. All prices, timings, and traffic counts below are invented teaching inputs, not provider quotes or benchmarks.

## Choose before generation, or check after it? \{#choose-before-generation-or-check-after-it}

An upfront router selects one model before generating an answer. Start with signals you already have: the product action the user selected, retrieved-passage count, missing citations or conflicting sources, and the score margin between retrieval candidates. These require no extra model call *once retrieval has run*; retrieval itself still costs time and money. A margin is meaningful only within a calibrated retriever and query population. Two passages can contain a hard contradiction; twenty can repeat one easy fact. Evidence shape is a routing feature, not a difficulty label.

Predicting difficulty is a separate step. A rule, trained classifier, or LLM can estimate whether a cheaper tier will meet the quality bar. A learned router needs representative labels and held-out evaluation for the actual model pair and workload; a score learned on one distribution need not transfer. Count classifier inference in the request budget.

A **model cascade** starts with a cheaper model, checks the result, and invokes a stronger tier when a check fails. The **escalation rate** `r` is the fraction of requests entering that cascade that invoke its next tier. An availability fallback responds to an error or rate limit; this escalation responds to an answer-quality signal.

| Design | What you pay for | What a wrong routing decision leaves behind |
|---|---|---|
| Upfront selection | Router plus one selected generation | A weak answer can pass unnoticed unless you independently audit or check it |
| Cheap-first cascade | Cheap generation and check on every entry; stronger generation on escalations | A detected weak answer can be replaced before release, if the remaining deadline permits |

Neither design guarantees correctness. A cascade's verifier can accept an unsupported answer or reject a good one. A stronger model can repeat the same error, and neither tier can recover evidence retrieval never supplied. Schema checks and citation existence checks are useful but do not establish that a claim follows from a passage. Calibrate semantic checks against human-labelled cases; audit accepted answers as well as rejected ones. The [evaluation deep dive](../../part-1-rag/cross-cutting/evaluation/deep-dive.md) covers judge calibration.

Recovery also has a boundary: hold the answer before release if replacement must be invisible. Tokens already shown cannot be withdrawn from the user's memory, and an external tool action may be irreversible. Restrict this cascade to answer generation or put an explicit approval boundary before side effects. Upfront routing can also use checks and recovery; the distinction here is the order of model selection, not a guarantee that one design is observable and the other is not.

## Compute request mix and spend separately \{#compute-request-mix-and-spend-separately}

Consider 100 requests. Compare each row with the cost of sending *that same class* to the strong tier. Costs include the assumed input and output lengths; these lengths can differ across classes.

| Class | Requests | Selected cost per request | Strong-only cost per request | Selected total | Strong-only total |
|---|---:|---:|---:|---:|---:|
| Lookup | 70 | $0.001 | $0.010 | $0.070 | $0.700 |
| Synthesis | 25 | $0.006 | $0.020 | $0.150 | $0.500 |
| Long drafting | 5 | $0.050 | $0.050 | $0.250 | $0.250 |
| Total | 100 | — | — | $0.470 | $1.450 |

Before routing overhead, the saving is `(1.450 − 0.470) / 1.450 ≈ 67.6%`. The lookup tier handles 70% of requests but only `0.070 / 0.470 ≈ 14.9%` of routed spend. Request share and spend share answer different questions. Add a $0.001 classifier to every request and the routed total becomes $0.570; the saving falls to about 60.7%.

For a two-tier cascade, assume fixed per-entry costs: `Cs` for the small generation, `Cv` for verification, `Cl` for the additional large generation. Then the expected cost per entry is:

`E[C] = Cs + Cv + r × Cl`

With `Cs = $0.002`, `Cv = $0.001`, `Cl = $0.010`, a 20% escalation rate costs `$0.005` per entry, half the strong-only `$0.010`. Break-even is `r = (Cl − Cs − Cv) / Cl = 0.70`. At 80% escalation, the cascade costs `$0.011`, more than using the stronger tier directly. Escalated requests pay for both generations, not necessarily exactly twice the money.

This formula assumes escalated requests have the stated large-call cost. If they have longer contexts or outputs, use their *conditional* average cost. Include router cost, retries, duplicate context, extra verification, and tool calls where applicable. For a bypass path, weight cascade cost by the fraction entering it, then add direct-to-strong spend. Compare with the same workload and quality target; a cheaper wrong answer is not a saving.

## A two-pass path changes the percentile \{#a-two-pass-path-changes-the-percentile}

First name the clock. Provider TTFT measures arrival of its first token; user-visible TTFT includes retrieval, routing, queueing, and any checks that block release. End-to-end latency ends only when the answer finishes. A fully buffered answer can have excellent provider TTFT and poor user-visible TTFT. The [serving lesson](../serving/index.md) explains buffering versus incremental validation.

For a serial buffered cascade, each accepted request takes the small generation plus verification. Each escalated request adds the large generation and any final blocking checks. Add elapsed times **within each trace**, then calculate percentiles over complete requests. Do not add span p95s: those quantiles may describe different requests, and escalation selects a conditional subset.

Here is a deterministic distribution of 100 requests with two distinct latency groups. Each small answer finishes at 450 ms; verification takes 100 ms; an escalated large answer adds 1,200 ms including its final release check. All other overhead is zero in this toy example. Accepted answers are released at 550 ms, escalated answers at 1,750 ms. For a nearest-rank p95, sort all 100 latencies and take the 95th.

| Escalations | At 550 ms | At 1,750 ms | p95 | Fraction meeting 800 ms |
|---|---:|---:|---:|---:|
| 4% | 96 | 4 | 550 ms | 96% |
| 5% | 95 | 5 | 550 ms | 95% |
| 6% | 94 | 6 | 1,750 ms | 94% |

With fully separated paths, escalation above 5% puts p95 on the slow path. At exactly 5%, the nearest-rank definition still selects the fast path; percentile interpolation and finite windows can change the boundary. Even at 4%, escalated users wait 1,750 ms. A passing p95 does not protect every request.

More generally, let `Fa(t)` be the latency CDF conditional on acceptance and `Fe(t)` the CDF conditional on escalation, including *all* serial work. The request distribution is `F(t) = (1 − r) × Fa(t) + r × Fe(t)`. The policy meets the 95% deadline-attainment target when `F(deadline) ≥ 0.95`. If paths overlap, or accepted requests sometimes breach the deadline, 5% is no universal safe escalation threshold. Measure the joint request traces under load: shared queues and backpressure can slow even the accepted path as escalation grows. The [observability deep dive](../../part-1-rag/cross-cutting/observability/deep-dive.md) covers latency budgets and the [serving deep dive](../serving/deep-dive.md) covers capacity and backpressure.

A workable policy might synchronously verify the fast tier, where the measured budget permits it, while auditing slow-tier answers asynchronously. Asynchronous checking cannot block a bad answer already delivered. Use it only where that residual risk is acceptable, retain required pre-release safety checks, and provide abstention or a deferred response when quality cannot be established before the deadline. Moving every check to a dashboard does not satisfy a pre-release correctness requirement.

## Operate the policy, not just the threshold \{#operate-the-policy-not-just-the-threshold}

Increasing a verifier threshold may increase escalation and recover more errors, but the quality gain is empirical, not guaranteed. Track escalation alongside accepted-answer error rate, verifier false accepts and false rejects, final quality, cost per successful request, and user-visible TTFT and completion latency. Break these down by workload and tier. A rising `r` can mean input drift, worse retrieval, a changed verifier, or a small-model regression; lowering the threshold solely to restore spend can hide the cause.

Version routing policy as validated, hot-reloadable configuration: eligible tiers, workload rules, thresholds, deadlines, spend caps, and the action when a check times out. Test changes on held-out cases, then apply them atomically to a canary while monitoring live quality signals. Trace the policy version and decision reason, and retain the previous configuration for rollback. Thresholds have no universal expiry date; review them when evidence or dependencies change.

Give each tier a kill switch. Disabling the small tier should bypass its generation and check; disabling the strong tier needs an explicit degraded action such as abstention or deferred processing. Define a safe response when the verifier is unavailable. Cap attempts and total elapsed time so an escalation chain cannot retry indefinitely. A kill switch redirects load and spend: verify destination capacity and budget before using it. Fall back to a known policy, not an unbounded search for a model that says yes.

## What to take away \{#what-to-take-away}

- Start with available evidence features, then test whether they predict which tier meets your quality bar.
- Count every generation and check; distinguish the share of requests from the share of spend.
- Calculate request percentiles from full traces. A rare second pass can dominate p95, and low escalation alone cannot prove the latency target.
- A cascade recovers only detected errors before the release or action boundary. Audit accepted answers, define degraded behaviour, and cap attempts and total elapsed time.

**[New terms](../../glossary.md#llmops):** model cascade, escalation rate. See also [model routing](./index.md#route-between-models) and [evaluation](../../part-1-rag/cross-cutting/evaluation/deep-dive.md).
