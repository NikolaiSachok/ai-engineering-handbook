---
id: overview
title: Production LLM
sidebar_position: 0
description: The scenario track for systems already answering real traffic — what you can change around a model you cannot change, and whether the number you are judged by can see the difference.
---

# Production LLM

The track for work that starts after the launch. Something is already answering real traffic, somebody's day
already depends on the output, and the brief is not *build this* but *make this better by a date*, usually with
the team, the budget and the deadline all decided by someone else before you arrived.

Scenarios here share a shape, and the first half of it is a constraint people underrate: *the model is not one
of the things you can change.* It sits behind a vendor API, on a tier procurement has committed to, under an
approval that covers inference on the published model and nothing else. What you can change is everything
around it — what it retrieves, what checks it, what a person sees, when a person is asked at all. Every one of
those levers is paid for in latency, in money, or in somebody's attention, which is the scarcest of the three
and the only one that cannot be topped up with budget.

The second half is the instrument. A live system already has a number attached to it, and somebody is already
deciding things by that number. Whether the instrument can resolve the improvement you are about to make is a
separate question from whether the improvement is real, and the two get confused most often in exactly the
situation where the answer matters — a deadline, one measurement, and a decision waiting on it.

## In this track

- **[Making it wrong less often](/design-scenarios/production-llm/making-it-wrong-less-often)** — a customs
  desk whose assistant drafts tariff codes, nine classifiers at two minutes a draft, and one 400-line audit
  ten weeks out that decides whether the assistant stays.

**One scenario so far.** The track opens with it rather than waiting for a set, because the first scenario is
the frame the next ones get written against. The obvious neighbours are not written yet: serving cost and
latency under load, holding a service together when a provider degrades or goes down, and versioning against a
model you do not control. None of them should be assumed from what is here.
