---
id: intro
title: Introduction
sidebar_position: 1
slug: /
---

# How to read this course

Each scenario in this course is one hard question about building an AI system in production,
answered three times, with a verdict on each answer.

[RAG & Agents](/rag-agents/) and [AI SDLC](/ai-sdlc/) teach how the machinery works. This course
puts that machinery under constraint. A scenario hands you a latency budget, a team size, a
regulated dataset, and then makes you choose. Several options are defensible; you still have to pick
one and say why.

Each scenario is staged as an interview, because that is the format that reliably produces a question
this sharp: a constraint, a clock, and someone who will ask why. The question and the rubric that
judges answers are written first; the attempts are written afterwards, against the question alone.

**The answers are written by language models** — one agent per attempt, each given a set of
engineering habits and the question, and nothing else: not the scoring rubric, not the other two
attempts. Read one as a reconstruction of how an engineer at that level reasons, not as a report from
somebody who lived it. [How these are made](/design-scenarios/how-these-are-made) sets out the whole
arrangement, including what it cannot buy.

:::note[Status]

The first batch is complete. Eight scenarios, one archetype —
[routing queries across models](/design-scenarios/agentic-workflows/model-routing),
[knowing an agent works](/design-scenarios/agentic-workflows/trajectory-vs-outcome),
[framework or your own primitives](/design-scenarios/agentic-workflows/framework-or-primitives),
[what an agent should remember, and what it must not](/design-scenarios/agentic-workflows/agent-memory),
[when an agent may try again](/design-scenarios/agentic-workflows/tools-that-fail),
[what a document is allowed to do](/design-scenarios/agentic-workflows/guardrails-at-the-boundary),
[what the dashboard cannot see](/design-scenarios/agentic-workflows/observing-a-non-deterministic-system) and
[the work that should stay a workflow](/design-scenarios/agentic-workflows/when-not-to-build-an-agent).
Whether a second archetype follows is being decided.

:::

## Why three answers instead of one

A single worked answer teaches you what someone concluded. It does not teach you why the
alternatives were worse, and that is where the reasoning lives.

So each scenario carries three attempts, written independently and without sight of each other or of
the rubric:

- **The common answer** — the one you will hear most often, and the one most write-ups stop at. It
  is never a strawman: plausible, popular, and usually wrong in one specific place.
- **The strong answer** — what someone who has run such a system in production reasons through,
  constraints first.
- **The over-built answer** — the complete architecture, arrived at before the problem earned it.

Then a verdict on each, and one sentence stating the principle that carries to other scenarios.

## Reading a scenario

Read the question. Answer it yourself, out loud or on paper, before you open the reveal: the three
attempts stay hidden until you do. Then read them and find out which one you just wrote.

Do it the other way round and you will nod along, feel informed, and retain nothing. Recognising a
good answer is not the skill that produces one.

Two sections then close the scenario. **Read next** points into the other two courses, at the
lessons that teach the mechanics an answer leaned on. A scenario shows you a decision; the machinery
under it is taught there. **If they push** lists the follow-up questions the interviewer would reach
for next. Those questions separate understanding from memory: if you memorised an answer here, the first
one will find that out.

## Where the questions come from

The questions are sampled, not invented. They come from the stated requirements of real
AI-engineering job postings, clustered and weighted by what recurs across them. Themes that appear
in one posting wait for evidence that they appear in more.

They are abstracted to role archetypes, and no employer is named. The constraints are chosen to make
the engineering hard, not to identify anyone.

Those archetypes are also how the scenarios are grouped. Each scenario is tagged with the kind of
role that asks it, and the tags become tracks. The first track is **agentic workflows** —
orchestration, tools, state, and the cost and quality tradeoffs that come with them. A track opens
when the postings ask for that kind of role often enough to fill one.

---

The other two courses are translated. This one is written in English and stays that way, and the
reason is register. Scenario pages carry argument, hedging, and the specific vocabulary of engineers
disagreeing with each other. That is the hardest kind of prose to move between languages without it
reading as moved. And the three attempts have to read as three distinct engineers, which is hard
enough to hold in one language.
