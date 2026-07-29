---
id: intro
title: Introduction
sidebar_position: 1
slug: /
---

# How to read this course

Every other page here is one hard question about building an AI system in production, answered three
times by three different engineers, with a verdict on each answer.

The other two courses on this site teach how the machinery works. This one puts it under constraint.
A scenario gives you a latency budget, a team size, a regulated data set — and then makes you choose,
because the interesting part of production engineering is never "does this technique exist", it is
"which of these three defensible options do I want to live with".

## Why three answers instead of one

A single worked answer teaches you what someone concluded. It does not teach you why the other roads
were worse, and the other roads are where the reasoning lives.

So each scenario carries three attempts, written independently and without sight of each other or of
the interviewer's rubric:

- **the common answer** — the one you will hear most often, and the one most write-ups stop at. It is
  never a strawman. It is plausible, popular, and usually wrong in one specific place;
- **the strong answer** — what someone who has operated this reasons through, constraints first;
- **the over-built answer** — the complete architecture, arrived at before the problem earned it.
  Senior engineers fail upward far more often than they fail downward, and this failure mode gets as
  much room as the other one.

Then a verdict on each, and one transferable sentence that outlives the specific scenario.

## How to actually use a page

Read the question. Answer it yourself, out loud or on paper, before you open the reveal. Then read the
three attempts and find out which of them you just wrote.

That order is the whole method. Read passively and you will agree with the strong answer, feel
informed, and retain nothing — recognition is not the same skill as production, and only one of them
is any use when the constraint is in front of you.

Every scenario ends with two things that matter more than the attempts. **Read next** points into the
lessons that teach the mechanics an answer leaned on, because a scenario shows you a decision, not the
machinery underneath it. **If they push** is a short list of follow-up questions that separate
understanding from memory. If you memorised an answer here, the first probe will find out.

## Where the questions come from

They are sampled, not invented. The scenarios are derived from the stated requirements of real
AI-engineering job postings, clustered and weighted by what recurs across them — so the pile reflects
what employers keep asking for rather than what happens to be fun to write about. Themes that appear
in one posting wait for evidence that they appear in more.

Nothing here comes from a private conversation, and no employer is named. The questions are abstracted
to role archetypes, and the constraints are chosen to make the engineering hard, not to identify
anyone.

## The tracks

Scenarios are tagged by the kind of role that asks them. The first track is **agentic workflows** —
orchestration, tools, state, and the cost and quality tradeoffs that come with them. Others follow the
same evidence: a track exists when the market asks for it often enough to fill one.

## English only

This course is written in English and stays that way, while the rest of the site is translated.

The reason is register. These pages carry argument, hedging, and the specific vocabulary of engineers
disagreeing with each other, which is the hardest kind of prose to move between languages without it
reading as moved. A translated scenario would be recognisably a translated scenario, and the value here
depends on the attempts sounding like three people rather than one machine.

:::note Status

In progress. The first batch of scenarios is being written; this page describes the plan, and the
tracks fill in as they land.

:::
