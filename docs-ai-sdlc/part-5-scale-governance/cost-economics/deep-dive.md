---
title: "Cost and the economics of agent work — deep dive"
sidebar_label: "The arithmetic: context, caching, and the retry tax"
sidebar_position: 2
---

# The numbers behind cost per accepted change

[Part 1](./index.md) fixed the unit — cost per *accepted* change, not per token — and named the usual
surprises: retry rate beats sticker price, and context is the line item people forget. This page does the
arithmetic that makes those claims precise. None of it is exotic; it is a few multiplications, and the reason
they matter is that the intuitions from a price list invert once you carry the numbers through. The rates below
are illustrative — plug in your provider's — but the *shape* of the sums is what decides your bill.

## One attempt, decomposed \{#one-attempt-decomposed}

The generation token subtotal bills two streams at two rates, summed over every turn it takes: **input** (everything you
send — system prompt, rules, brief, prior turns, tool results) and **output** (what it generates).
Output usually costs several times more per token than input, which fools people into watching the
output. For agent work the trap is that input *volume* dwarfs output volume, so the
cheaper-per-token stream can dominate the token bill:

```text
attempt_cost = input_tokens × input_rate + output_tokens × output_rate
```

Here `attempt_cost` is the generation model-token subtotal. Add external tool resources, verification, and human review when calculating the full cost per accepted change.

The output side of an agent turn is a diff, a tool call, a paragraph — hundreds of tokens. The input side is
the entire working context — thousands to tens of thousands. The multiplier on the small rate wins.

## Why context dominates: the re-send is quadratic \{#why-context-dominates-the-re-send-is-quadratic}

Here is the part a per-call price hides. A multi-turn agent re-sends the whole conversation each turn, because
the model is stateless — turn 5 pays to read turns 1 through 4 again. If a task runs `N` turns and the context
grows by roughly a constant amount per turn, the total input billed across the task is not `N` times one turn;
it is the sum `1 + 2 + … + N`, which is **`O(N²)`**. Double the turns and you roughly *quadruple* the input
cost.

That single fact reorganises where you look. It is why a task that took twice as many turns pays
roughly four times the input cost, why a bloated context is expensive on every turn and not just
once, and why the [rules-corpus bloat](../drift-and-rot.md) from the drift lesson has a bill
attached, not only a quality cost. Trimming what rides in context is the highest-leverage cost
move in agent work, and it is invisible on a price list that quotes one call.

## Prompt caching bends the curve back \{#prompt-caching-bends-the-curve-back}

The `O(N²)` re-send has a direct remedy: providers let you **cache a stable prefix** so that re-sending it
costs a fraction of the fresh input rate — commonly on the order of a tenth. The exact discount is
a provider figure, so read it through the course's vendor rule: it is a pricing lever they set, not a measured
constant. The system prompt, the rules corpus, and settled earlier turns are the same bytes every call; cached,
they stop being re-billed at full price.

The design consequence is concrete and it ties back to earlier lessons. Caching only works on a **stable
prefix**, so put the unchanging material first and the volatile material last, and *keep it unchanging*. A
rules corpus edited mid-task, or one bloated enough to be truncated differently from call to call, breaks the
prefix and forfeits the discount — the same corpus hygiene the drift lesson argued for on correctness grounds
turns out to be a cost control too. Stable-prefix discipline is where the quadratic stops hurting.

## Batching trades latency for a discount \{#batching-trades-latency-for-a-discount}

A second lever applies to work that is not waiting on a human. Providers commonly list Batch APIs — submit
many requests, collect results minutes to hours later — at a substantial discount, often around half price,
because they schedule the work off-peak. The trade is latency for cost, so it splits
your workload cleanly: an **interactive** agent turn, where someone is waiting, cannot batch; **offline** work
— bulk evaluation, a corpus-wide transform, regenerating fixtures — should. The verification passes from
Part III that run after the fact are often batchable even when the generation that produced them was not.

## The retry tax, and the break-even that inverts the price list \{#the-retry-tax-and-the-break-even-that-inverts-the-price-list}

For a token-cost illustration, assume each attempt costs the same model-token amount and succeeds independently with the same probability `p`, with `0 < p ≤ 1`. If you repeat until success without a retry cap, the expected number of attempts is `1/p`. A first-try success rate alone does not establish these assumptions. Under this simplified model:

```text
token_cost_per_accepted = attempt_cost / p
```

Here `attempt_cost` remains the generation model-token subtotal. Compare two models on that subtotal: one costs `C` per attempt and succeeds with probability `0.8`, giving `C / 0.8 = 1.25 C` in expected generation token cost per accepted change. The other costs `0.5 C` per attempt:

| Cheaper model's success probability per attempt | Expected generation token cost per accepted change | vs 1.25 C in tokens |
|---|---|---|
| 0.40 | 0.5 C / 0.40 = 1.25 C | tie |
| 0.50 | 0.5 C / 0.50 = 1.00 C | lower token cost |
| 0.30 | 0.5 C / 0.30 = 1.67 C | higher token cost |

In this model, lower token cost per accepted change requires `p_cheap / p_expensive > price_cheap / price_expensive`, where each price is the generation token cost per attempt. At half the price, success probability must exceed half the other model's, or `0.40`. This break-even compares tokens, not total cost.

For the full comparison, include all five buckets from Part 1: context, retries and rework, verification, human review, and external tool resources. Account for when each is incurred, without counting the same expense twice. A retry may reuse cached context, repeat paid compute, require another verification pass, or add human rescue time. Those differences can reverse the token-only ranking. With capped retries, changing attempt costs, or dependent outcomes, measure total spend across accepted and abandoned runs per accepted change rather than applying the geometric estimate unchanged.

## The line a token discount cannot touch \{#the-line-a-token-discount-cannot-touch}

Token discounts affect model-based generation and verification, but neither human review nor external tool resources become cheaper merely because tokens do. Bound the saving by the share of the total bill actually priced in tokens. If human review is 40% and external compute is 30%, even eliminating the remaining token bill saves at most 30%, assuming those costs stay fixed. Review capacity and external-service capacity can each limit throughput. Measure their shares before deciding which optimisation matters.

## What to take away \{#what-to-take-away}

- **Decompose generation token cost:** `input_tokens × input_rate + output_tokens × output_rate` is a subtotal. Larger input volume can outweigh its lower rate within that subtotal.
- **The context re-send is `O(N²)`:** a stateless model re-reads the whole transcript each turn, so doubling
  turns roughly quadruples input cost. Trimming context is the highest-leverage move.
- **Prompt caching needs a stable prefix** — unchanging material first, volatile last, and kept unchanging. A
  churning or bloated rules corpus forfeits the discount, so corpus hygiene is a cost control, not only a
  quality one.
- **Batch the offline work** (bulk eval, corpus transforms) for a large discount; interactive turns can't
  batch. Latency for cost, split along whether a human is waiting.
- **Token-only retry estimate:** `token_cost_per_accepted = attempt_cost / p` assumes equal-cost independent attempts with fixed success probability and no retry cap. The price/success inequality compares token subtotals; compare all five cost buckets and their retry behaviour before choosing a model on total cost.
- **Token savings are bounded by the token-priced share.** Human review and external tool resources remain outside that discount.

**[New terms](../../glossary.md#cost-and-the-economics-of-agent-work)**: attempt-cost decomposition, input/output rate asymmetry, quadratic context re-send, prompt caching (stable prefix), batch discount, retry tax, break-even success rate, Amdahl bound on token savings.
