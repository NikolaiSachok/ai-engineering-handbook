---
# NOT A PUBLISHED PAGE. The leading underscore keeps Docusaurus from routing this file.
# Copy it to <track>/<scenario>.md and fill it in. Worked example: agentic-workflows/model-routing.md
id: scenario-template
title: Scenario template
---

# &lt;Scenario title — the decision, not the topic&gt;

Every scenario page has the same seven parts, in this order. The order is the method: the reader meets the
question, learns what it tests, commits to an answer, and only then sees three attempts to compare their own
against. Change the order and the page becomes a listicle about a topic.

> The prompt, as an interviewer would state it, in a blockquote. 120–200 words. It carries the constraints
> that make it hard — traffic shape and volume, a latency budget, a concrete cost pressure, the size of the
> team that maintains it, and what "quality" means for this product. **A prompt with no constraints has no
> wrong answers.** Do not hint at the answer you want.

:::info[Why this question]

80–150 words on the signal actually under test: what this separates, and what a weak answer reveals. Written
for a reader who is about to be told this is what was being tested — so it must be true, not flattering.

:::

**Answer it before you read on.** One line asking the reader to commit, and the sourcing statement: the
attempts were written blind, each author seeing only the prompt, none seeing the rubric or each other.

&lt;details&gt;
&lt;summary&gt;Show the three attempts&lt;/summary&gt;

## Attempt A — the common answer

The answer you will hear most often, and the one most write-ups stop at. **It is never a strawman.** If a
reader would not recognise it as a reasonable thing to say in a room, the page teaches nothing.

**Verdict.** 60–120 words. Where it breaks, what it buys, what it costs. Name the actual move being judged
and quote it. Not a score, not a checklist, and never a list of the rubric rows it missed — the mechanism of
the failure is the teaching.

## Attempt B — the strong answer

What someone who has operated this reasons through, constraints first, stating what each choice costs as
well as what it buys.

**Verdict.** Same shape. The strong answer gets a real verdict too — including its cracks. An attempt with no
criticism reads as the answer key this course exists not to be.

## Attempt C — the over-built answer

The complete architecture, arrived at before the problem earned it. Also not a strawman: this is a genuinely
strong engineer solving a problem the scenario does not yet have.

**Verdict.** Same shape.

## Where they actually disagree

Two to four disagreements where the attempts genuinely contradict each other — not where one is simply more
complete. Each is a decision the reader will have to make themselves, so state both positions and say which
is right where one is. **This is where the teaching concentrates**; a scenario whose attempts only differ in
thoroughness was not a hard enough question.

## The principle

> One sentence, in a blockquote. Transferable beyond this scenario, and it must survive the specific numbers
> being wrong. This is the sentence a reader should still have in a year. If it cannot be written, the
> scenario is not yet a scenario.

&lt;/details&gt;

:::tip[Read next]

At most five links into the RAG & Agents / AI SDLC lessons that teach the mechanics an attempt leaned on, in
the order they help a reader judge the attempts. Each carries one line on what it teaches.

**A missing lesson is a finding, not an inconvenience.** File it against the owning course's milestone. Never
substitute a loosely-related page: released builds throw on a dead link, but a plausible-and-wrong link
passes CI and misleads the reader.

:::

## If they push

Two or three follow-up questions in bold, each with a short paragraph on what it exposes. They must be
questions a reader who memorised Attempt B cannot survive and one who reasoned to it answers easily. This
section is the page's anti-memorisation defence, so it is not optional.

---

## Producing one

Use the `design-scenarios` skill. The pipeline is what makes the comparison real: an interviewer
pre-registers a hidden rubric, three candidate agents answer **blind** — prompt only, never the rubric, never
each other — an assessor writes the verdicts against the pre-registered rubric, and a curriculum linker finds
and verifies the lesson links.

Two rules the page dies on:

1. **Sourcing.** Derived from published job requirements. Never from an interview anyone sat, and no company
   named anywhere — including obliquely. Describe the product by its shape, not its industry.
2. **Honesty.** The attempts are archetypal engineers' reasoning. Analysing an approach nobody here has
   shipped is analysis, not a claim. Narrating a first-person war story that did not happen is neither.

Notes from the first run:

- **If two attempts converge, re-run with sharper personas.** Do not edit them apart. Divergence is evidence
  about the question; manufactured divergence is fiction. The first run's "common" persona produced a
  near-senior answer because the persona described competence rather than habits — say how the engineer
  thinks and what they have never had to do, not how good they are.
- **Admonitions do not render inside `<details>`.** Keep `:::info` and `:::tip` outside the reveal gate.
- **Fence the ASCII diagrams as `text`.** The markdown linter and the parity gate both count fence languages.
