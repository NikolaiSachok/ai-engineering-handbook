---
id: how-these-are-made
title: How these are made
sidebar_position: 90
description: The scenario pipeline — five agents, a rubric written before any answer exists, and what the arrangement buys and cannot buy.
---

# How these are made

Every answer on these pages is written by a language model. The short version sits on the
[introduction](/design-scenarios/), because a reader deserves it before they read an attempt, not after.
This is the long version: the arrangement, why each part of it is shaped the way it is, and where it has
already been wrong.

It is here for two reasons. The first is disclosure — naming a role ("the candidate") is not the same as
saying who wrote the text, and a page that grades answers cannot be coy about where they came from. The
second is that the pipeline is a worked example of the thing the [AI SDLC](/ai-sdlc/) course argues for, built
under the same constraints it describes. If you are reading this course to get better at production AI, the
machinery below is as much a case study as any scenario.

## Five roles, and what each one cannot see

| Role | Writes | Deliberately cannot see |
|---|---|---|
| **Interviewer** | The question, its constraints, and a hidden rubric — what a strong answer must reach, what disqualifies, which plausible directions earn nothing | The answers. It never sees them. |
| **Candidate ×3** | One attempt each, in the voice of an engineer with a given set of habits | The rubric, and the other two attempts |
| **Assessor** | The verdict on each attempt, scored against the rubric, plus the transferable principle | Nothing — it is the only role that sees everything |
| **Curriculum linker** | The *Read next* links, and a report of every mechanic an attempt leaned on that no lesson teaches | — |
| **Orchestrator** | Nothing on the page. It runs the other four, adjudicates what the review gates report, and assembles | The attempts, until every one of them is finished — it must not write one, having read the rubric |

The blindness is the whole mechanism. A candidate that has seen the rubric writes toward it, and the common
answer collapses into a strawman — which would make the comparison worthless, because the interesting thing
about the common answer is that it is *genuinely* the answer most people give.

## The rubric is written first, on purpose

The interviewer commits to a standard before any answer exists. This is not ceremony. A rubric written after
the answers is a rationalisation of them: whatever the strongest attempt happened to do becomes, in
retrospect, what a strong answer was always supposed to do. Pre-registering it means an attempt can reach
something the rubric never anticipated — and when that happens, the assessor is asked to say so, because a
rubric that only ever tests what its author already knew to ask is a rubric that stops improving.

## What the arrangement buys, and what it cannot

It buys **independence**. Three answers to one question, produced without sight of each other, differ in ways
that are informative rather than decorative. Where they contradict each other, that contradiction is a
decision a real engineer has to make, which is why every scenario has a section for it.

It cannot buy a scar. Nobody was paged at 3am for the system in any of these prompts. An attempt is a
reconstruction of how an engineer at that level reasons — good enough for the comparison to teach, and not a
report from somebody who lived it. Where a scenario needs a real production failure, it links to a lesson that
has one.

## Where it has already been wrong

Three failures are worth recording, because each was invisible until something specific was checked.

**The personas converged.** The first run briefed the three candidates by *competence level* — "competent,
well-read, has shipped features". All three produced near-senior answers. A model asked how good someone is
defaults to answering well, so competence is the wrong axis. Re-briefed by *habits* — how this engineer
thinks, and what they have never had to do — the attempts diverged. The personas you see under each heading
are written that way for this reason.

**Some tells no persona can move.** In that same run, all three attempts contained exactly ten em-dashes. Half
of all paragraphs opened with a bolded declarative. All three closed on a neat final line, where real answers
tend to just run out. Persona instruction moved content, rhythm and pronouns; it did not move punctuation or
paragraph shape. That is a measured limit of the method, and it is the reason the editorial pass is forbidden
from touching the attempts: fixing those tells would erase the evidence that they exist.

**A question had only one answer.** The framework scenario's first question pushed every constraint the same
way — a system already in production doing everything the future needed, a hard deadline, and money that could
not be spent twice. Three agents briefed with three different sets of habits read it and gave the same answer,
correctly, because there was only one. The personas were not at fault; the question was. Divergence is evidence
about the question, so the question was thrown away rather than the answers edited apart — and the rewrite had
to state the strongest one-sentence case for each side, and the fact that makes each available, before any
attempt was written. That check now runs before the candidates do.

**A question can be contested and still go unexplored.** The memory scenario passed that new check — four
architectures, each defensible, each defeated by a different fact in the prompt. Three of the four then went
unvisited or half-visited, and the fourth was empty. The reason was not the question: all three sets of habits
described engineers who build stores, so no agent was equipped to argue for building almost nothing and
re-deriving state from records that already exist. Proving a question is contested and casting agents who can
occupy the contested ground are two different jobs, and only the first had a check. The empty position was also
the one the prompt defeats *on cost*, which is why the standard about tail-heavy spending drew nothing from any
attempt — the rubric row was reachable, and nobody had been cast to reach it.

**A prompt that ends in a list gets answered as a list.** The same scenario's prompt closed on an enumeration —
*what persists, what expires, what is never written* — and all three agents answered in that order, using those
words as their section headings. It is the only prompt of the four to end that way and the only one whose blind
attempts share a skeleton. The wording stayed as it shipped, because rewriting a prompt after the attempts have
answered it makes the printed question no longer the one they were asked.

**An agent hands back the words it was given.** Two of that scenario's three attempts reproduced their own
persona brief nearly verbatim — one of them three times over, in a line about a summary becoming the only
surviving record of something that mattered. The briefs are printed above each attempt, so a reader can see the
seam, which is the honest outcome: the reasoning underneath was still independent and still divergent, but the
phrasing was borrowed, and the brief now has to say so explicitly. Briefs had also been growing — 42 words, then
80, then 87, then 110 — and a longer brief is more material to recite.

## The gates, and the one that had to be inverted

A scenario passes through the same layered checks as the rest of the handbook — an editorial team, a
deterministic secret-and-path scan, an adversarial review for anything that should not be public, and a cold
read by fresh eyes at the end. They are stacked because their mechanisms are blind to different things.

One gate runs backwards here. The editorial pass would normally unify voice across a page; on a scenario it is
told the three attempts are **quoted testimony** and may only be corrected for outright mechanical errors. If
it finds an AI tell inside an attempt it reports it and leaves it, because a tell is evidence about the
pipeline rather than a defect in the page. Barred from fixing, that reviewer found something a fixing reviewer
would have quietly smoothed away: the two sentences where an attempt hands agency to an abstraction — "the mix
hands it to us", "the 40% falls out" — are exactly the sentences where it skips the arithmetic.

The verdicts, by contrast, get the full pass. They are the page's own voice, and on the first scenario two of
the three misstated the attempt they judged in ways a reader could falsify by scrolling up. Prose *about*
someone else's text turns out to be where attention is thinnest.

## What this exemplifies

- [The verification bottleneck](/ai-sdlc/part-1-foundation/verification-bottleneck) — why the machinery is
  weighted toward checking rather than producing. Generating three attempts is the cheap part.
- [Plan, review, implement, critic](/ai-sdlc/part-2-loop/plan-review-implement-critic) — a standard agreed
  before the work, a critic before anything lands. The pre-registered rubric is that first gate.
- [Layered gates and mechanism diversity](/ai-sdlc/part-3-verification/layered-gates) — every gate is blind to
  something, so they are stacked to be blind to different things. The cold read exists because the main gate
  cannot see the fixer.
- [The escape ledger](/ai-sdlc/part-3-verification/escape-ledger) — the three failures above are recorded
  rather than quietly fixed, and each one changed how the next scenario is made.

## Honest accounting

This is heavier than writing one good answer would be, by a wide margin, and most of the cost is in the
checking rather than the writing. That is the trade the AI SDLC course argues for, and this course is where it
gets tested on prose instead of code. Where the arrangement stops paying for itself, that will be recorded
here too.
