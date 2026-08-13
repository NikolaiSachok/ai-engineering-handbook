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

## One attempt, decomposed

An attempt bills two streams at two rates, summed over every turn it takes: **input** (everything you
send — system prompt, rules, brief, prior turns, tool results) and **output** (what it generates).
Output usually costs several times more per token than input, which fools people into watching the
output. For agent work the trap is that input *volume* dwarfs output volume, so the
cheaper-per-token stream is the larger bill:

```text
attempt_cost = input_tokens × input_rate + output_tokens × output_rate
```

The output side of an agent turn is a diff, a tool call, a paragraph — hundreds of tokens. The input side is
the entire working context — thousands to tens of thousands. The multiplier on the small rate wins.

## Why context dominates: the re-send is quadratic

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

## Prompt caching bends the curve back

The `O(N²)` re-send has a direct remedy: providers let you **cache a stable prefix** so that re-sending it
costs a fraction of the fresh input rate — commonly on the order of a tenth (`REPORTED`; the exact discount is
a provider figure, read through the course's vendor rule — it is a pricing lever they set, not a measured
constant). The system prompt, the rules corpus, and settled earlier turns are the same bytes every call; cached,
they stop being re-billed at full price.

The design consequence is concrete and it ties back to earlier lessons. Caching only works on a **stable
prefix**, so put the unchanging material first and the volatile material last, and *keep it unchanging*. A
rules corpus edited mid-task, or one bloated enough to be truncated differently from call to call, breaks the
prefix and forfeits the discount — the same corpus hygiene the drift lesson argued for on correctness grounds
turns out to be a cost control too. Stable-prefix discipline is where the quadratic stops hurting.

## Batching trades latency for a discount

A second lever applies to work that is not waiting on a human. Batch APIs — submit many requests, collect
results minutes to hours later — commonly run at a substantial discount, often around half price (`REPORTED`,
provider pricing), because the provider schedules them off-peak. The trade is latency for cost, so it splits
your workload cleanly: an **interactive** agent turn, where someone is waiting, cannot batch; **offline** work
— bulk evaluation, a corpus-wide transform, regenerating fixtures — should. The verification passes from
Part III that run after the fact are often batchable even when the generation that produced them was not.

## The retry tax, and the break-even that inverts the price list

Now Part 1's headline claim, made exact. If a change lands on the first try with probability `p`, the expected
number of attempts is `1/p`, so:

```text
cost_per_accepted ≈ attempt_cost / p
```

Put two models against each other. An expensive one at price `C` and first-try rate `0.8` costs `C / 0.8 =
1.25 C` per accepted change. A cheap one at half the price, `0.5 C`, needs its success rate to clear a bar:

| Cheap model's success rate | Cost per accepted change | vs 1.25 C |
|---|---|---|
| 0.40 | 0.5 C / 0.40 = 1.25 C | tie |
| 0.50 | 0.5 C / 0.50 = 1.00 C | cheaper wins |
| 0.30 | 0.5 C / 0.30 = 1.67 C | *more* expensive |

The break-even is clean: the cheaper model wins only when `p_cheap / p_expensive > price_cheap / price_expensive`
— it can afford to be less reliable, but only by the factor it is cheaper: at half the price its success
rate must stay above half the expensive model's, which is 0.40. Half the price buys nothing at exactly
half the reliability, and costs you more below it. This is the whole of "retry
rate outweighs sticker price," reduced to one inequality you can actually measure.

## The lines a token discount cannot touch

One closing sum keeps the others honest. Of the four cost buckets from Part 1, only **human review** is
beyond the reach of token price — it is paid in salary, and its throughput is not for sale.
**Verification** is itself model calls, so a discount does lower it; what a discount cannot do is reduce
how many checks you run. So a token-price optimisation is bounded the way Amdahl bounds any speedup: if
human review is, say, 40% of the total cost of a change, then *no* token discount, however deep, can
reduce the total by more than the remaining 60%. When review dominates, shaving the token bill optimises
the smallest lever — which is exactly why Part 1 insisted the binding constraint is priced in salary, not
tokens.

## What to take away

- **Decompose the attempt:** `input_tokens × input_rate + output_tokens × output_rate`. Output costs more
  per token, but input *volume* is far larger, so input is the bill.
- **The context re-send is `O(N²)`:** a stateless model re-reads the whole transcript each turn, so doubling
  turns roughly quadruples input cost. Trimming context is the highest-leverage move.
- **Prompt caching needs a stable prefix** — unchanging material first, volatile last, and kept unchanging. A
  churning or bloated rules corpus forfeits the discount, so corpus hygiene is a cost control, not only a
  quality one.
- **Batch the offline work** (bulk eval, corpus transforms) for a large discount; interactive turns can't
  batch. Latency for cost, split along whether a human is waiting.
- **Retry tax:** `cost_per_accepted ≈ attempt_cost / p`. A cheaper model wins only if
  `p_cheap / p_expensive > price_cheap / price_expensive` — reliability has to beat the price gap.
- **A token discount is Amdahl-bounded** by the human-review fraction, which no token price touches. When
  review dominates, the token bill is the smallest lever.

**[New terms](../../glossary.md#cost-and-the-economics-of-agent-work)**: attempt-cost decomposition, input/output rate asymmetry, quadratic context re-send, prompt caching (stable prefix), batch discount, retry tax, break-even success rate, Amdahl bound on token savings.
