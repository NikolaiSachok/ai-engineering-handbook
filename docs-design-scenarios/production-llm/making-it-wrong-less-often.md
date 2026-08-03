---
id: making-it-wrong-less-often
title: Making it wrong less often
sidebar_position: 1
description: A customs desk drafts 1,470 tariff-code lines a day with an assistant, nine classifiers review them at two minutes a draft, and one 400-line audit in ten weeks decides whether the assistant stays. Three attempts at deciding what to build, in what order, and what would show the error rate had moved.
# The reveal is the method. A page TOC lists every heading inside the collapsed reveal —
# naming all three attempts and the principle before the reader has committed to an answer.
hide_table_of_contents: true
---

# Making it wrong less often

An eight-digit commodity code is a legal claim. It sets the duty an importer pays, and on some lines it
decides whether a container may move at all. It is also, to a model, a category — one branch of a tree of 21
sections and 97 chapters, picked out of text describing a product and text describing the tariff schedule.

This desk has an assistant that drafts those codes well enough to be worth keeping, and an instrument that
reports how often it gets them wrong: 400 lines re-worked from the original paperwork every quarter, 31 of
them different last time. Everything around the assistant is already spoken for — nine classifiers, two
minutes a draft, ten weeks, two engineers, and no new headcount.

[What a document is allowed to do](/design-scenarios/agentic-workflows/guardrails-at-the-boundary) on the way
in is another scenario's question. This one starts after that boundary, with a code that is well-formed,
present in the schedule, and wrong.

> You've joined the customs desk of a freight forwarder that files import declarations for about 600 client companies — roughly 1,400 declarations a working day, three lines each, so 4,200 lines. Every line needs an eight-digit commodity code out of the tariff schedule, and the code sets the duty rate.
>
> Around 65% of lines are the same product from the same client as last time, and a matching rule fills those in from the previous filing; the rule works off the desk's own declaration system, about six million filed lines over six years. The other 1,470 lines a day go to the assistant. On about 6% of those 1,470 the code also decides whether a licence or a certificate has to be on file before the goods move.
>
> The assistant reads the commercial invoice and the product description, retrieves eight passages from a corpus of 21,000 built out of the schedule's headings and its explanatory notes, and returns a code and a two-line rationale for every line it is handed. The schedule is a tree: 21 sections, 97 chapters, and rules sitting at section and chapter level govern everything beneath them. On its way to a classifier a draft passes a lookup against the schedule, which rejects about 0.4% of drafts.
>
> A classifier files. There are nine of them, and with the auto-filled lines, client calls and the rest of the desk's work out of it, they have about 58 hours a day between them for the drafted lines. The review screen shows the code, the rationale and the invoice. Reviewing a draft takes roughly two minutes, and a classifier changes the code on about 9% of drafts. Working a line from scratch — invoice, spec sheet, the notes — takes twelve minutes.
>
> Wrong means this. Every quarter two of the nine re-classify 400 assistant-drafted lines from the original paperwork, sampled at random from the roughly 92,000 the desk filed that quarter; they work the sample independently and confer where they differ, and what they land on is the desk's answer. Last quarter 31 of the 400 came back different. The three audits since the assistant went live ran 6.1%, 7.0% and 7.8%. An audit costs each of the two a full week, separate from the four hours a week the lead classifier has been told to give you. The last one also sampled 200 auto-filled lines and found 4 of those wrong.
>
> In three years the customs authority has raised 26 corrections against the desk's filings, most of them from before the assistant existed: €180,000 in back duty, interest and penalties. A wrong licence call is a different failure — the container sits at about €300 a day, and the desk absorbs it when the code was theirs.
>
> The classifiers have adapted. Two of them keep private spreadsheets of codes they've watched the assistant get wrong; one is about 600 rows. Several ask twice, rewording the product description, and file the code that comes back both times. Some of the larger clients now send a suggested code with the paperwork, and classifiers tend to file it. Two classifiers go to the schedule themselves for anything that isn't obvious, and last month the desk missed its ninety-minute filing commitment on 40 declarations.
>
> The model sits behind a vendor API; procurement has the vendor and the tier named for another two years, and the approval covers inference on the published model. A draft comes back in six seconds with the classifier waiting. Paperwork reaches the desk a median four hours before the filing deadline; for about a fifth of lines, under thirty minutes. Model spend runs about €2,100 a month against a €9,000 monthly envelope for the calls and anything you run alongside them; headcount is a separate budget and it is closed this year. You have two engineers. The next audit is in ten weeks, and the desk manager has said that if the number isn't better the assistant comes out.
>
> Bring the error rate down. Tell me what you'd build, in what order, and how you'd know it moved.

:::note[Why this question]

Every check you add costs something, and on this desk every cost lands on a budget somebody else already
fixed — nine people's minutes, a capped inference envelope, a ninety-minute filing clock. None of them can be
raised inside ten weeks, and headcount is closed for the year.

The number that decides whether any of it worked is one measurement, taken once, at a size you had no say in.
The deadline and the budget were set the same way.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard.

Three model-written attempts follow. Each comes from a separate agent given one engineer's habits and the
prompt above, and nothing else. No agent saw the other two, and none saw the scoring standard the verdicts are
written against — that was pre-registered before the attempts it judges existed, by an interviewer who has
never read an attempt, and a separate assessor applies it. The attempts introduce figures of their own; this
scenario is arithmetic most of the way down, and where one of those figures is load-bearing and unchecked, the
page says so. That arrangement is described in
[how these are made](/design-scenarios/how-these-are-made).

<Reveal>

## Attempt A — the common answer

*Persona given to the agent: reaches for what the write-ups have converged on — a judge model, an eval set, better prompts — thinks in layers to add on top of what is there, and checks cost once it works.*

**First, where the number is actually coming from.** The audit measures post-review error. Classifiers already change the code on 9% of drafts, and after all that changing, 7.8% of what gets filed is still wrong — and it's gone 6.1, 7.0, 7.8. So the review layer is not a filter I can lean on harder. And I can't buy more of it: 1,470 drafts times two minutes is 49 hours against the 58 they have, with client calls in that same 58. Anything I build has to fit inside a review budget that's already 85% consumed. That rules out "flag more for careful review" as a strategy on its own, and it rules out from-scratch work entirely — twelve minutes times 1,470 is not a number anyone can spend.

**Week one and two: the eval set, because right now I'd be guessing.** I have better labels available than people realize. Three audits at 400 lines each is roughly 1,200 independently double-worked, adjudicated labels — that's a real gold set, and it's already paid for. On top of that, the classifier with the 600-row spreadsheet of codes she's watched the assistant miss is a curated adversarial set someone built by hand for free; I want it in the repo on day two, and I want the other one too. Then the review-screen overrides: 9% of 1,470 is about 130 a day, thousands of weak labels a quarter — not gold, because a classifier changing a code isn't proof they were right, but excellent for mining where the assistant and the humans disagree.

I'd freeze about 1,500 lines as a held-out set, stratified by chapter and with the licence-implicated lines over-sampled, and I would not touch it while iterating. Everything below gets scored against it before it goes near production.

**Build one: retrieval that respects the tree.** Eight flat passages pulled by similarity out of 21,000 chunks, over a corpus whose defining property is that it's a hierarchy, is the most likely single source of the error. Section and chapter notes govern everything beneath them — they're exclusions, mostly — and a flat similarity search will happily return the heading that matches the product words and drop the chapter note that excludes it, because the note doesn't mention the product. That failure looks exactly like a plausible code with a plausible rationale, which is the failure that survives a two-minute review.

So: two-stage. Classify to chapter first, then retrieve headings only within the candidate chapters, and inject that chapter's notes and its section's notes unconditionally — not by similarity, always. If the model is choosing between two chapters, both note sets go in.

**Build two: a legality check on the draft.** A second call that takes the proposed code plus the governing notes and answers one narrow question — does any note at section or chapter level exclude this good from this heading? I want the judge scoped to something checkable. "Is this code right" is a judge I can't validate; "does note 1(a) to chapter 39 exclude this" is a question with an answer in the text, and I can score it on the gold set. This slots in beside the lookup that already rejects 0.4%, and it fails the same way — back for a second pass rather than to the classifier.

**Build three: make the consistency trick official.** Several classifiers already ask twice with a reworded description and file the code that comes back both times — that's self-consistency, hand-rolled, and it's a signal we're currently throwing away and paying for in their time. Sample three times with description order varied, and use agreement as confidence. Where all three agree, that goes to review as-is. Where they split, the review screen shows the competing codes and the note that separates them, so the classifier spends their two minutes on the actual decision instead of reconstructing it. And the rationale should say which note applied, not just restate the product.

**The licence lines get their own path.** Six percent of 1,470 is about 88 lines a day, and each mistake is €300 a day of demurrage. Those always get the full treatment — every sample, the legality check, and the review screen says out loud that this code triggers a licence requirement. At 88 lines the cost of being thorough there is rounding error.

**Cost, now that the shape is fixed.** Three samples plus a verifier is roughly 4-5× on a €2,100 base — call it €9-10k, which busts the €9,000 envelope. So the multi-sample path runs only where the first pass is low-confidence or a licence is implicated; that's maybe a quarter of lines and lands around €4,500. Latency goes to roughly twelve seconds, which is fine against a four-hour median and still fine against the thirty-minute tail.

**How I'd know it moved.** Offline on the frozen set at each step, with a gate: retrieval change has to beat baseline before the verifier goes on top of it. Then a shadow week — old and new pipeline on the same live lines, and the lead classifier spends her four hours adjudicating a hundred cases where they disagree. That's the honest read before the audit.

One thing I'd say to the manager now, not in week ten: at n=400 the audit's confidence interval is around ±2.7 points. If we land at 6.0 it's a real move; anything between 6.5 and 7.8 is not distinguishable from noise, and I'd rather agree in advance that the shadow comparison counts as evidence than have the assistant pulled on a sampling artifact. I'd also ask them to look at the auto-fill: 4 of 200 wrong is 2% on 2,730 lines a day that nobody reviews at all. That's more wrong lines leaving the desk than the assistant produces.

<Verdict>

It opens on the right question — the audit measures error *after* review, and the review budget is already 85%
consumed — and it is right that this forecloses "flag more for careful review" as a standalone strategy. Two
engineering moves are genuinely good. A is the only one that carries the retrieval diagnosis through to *why
that failure survives review*: "a flat similarity search will happily return the heading that matches the
product words and drop the chapter note that excludes it, because the note doesn't mention the product." And
that failure, it adds, "looks exactly like a plausible code with a plausible rationale". The verifier is
scoped with real discipline — "'Is this code right' is a judge I can't validate; 'does note 1(a) to chapter 39
exclude this' is a question with an answer in the text, and I can score it on the gold set." That is the
correct instinct: narrow the check until it is falsifiable, then score it.

The arithmetic around those moves is what breaks. The cost paragraph declares three samples plus a verifier
"roughly 4-5× on a €2,100 base — call it €9-10k, which busts the €9,000 envelope", and retreats to "maybe a
quarter of lines". At the low end of its own 4–5× range the envelope holds, with €600 of slack — an answer
worth stating rather than stepping around. Taking the high end instead narrows the design to a quarter of the
population and leaves roughly €4,500 a month unspent, unnoticed.

Worse is the close. It quotes ±2.7 points and in the next clause says "if we land at 6.0 it's a real move" —
1.8 points, inside the band it just stated. And its substitute evidence, a shadow week adjudicated by the lead
in four hours, prices 100 adjudications at 2.4 minutes each against the prompt's twelve. It buys a cheap,
human-budget-neutral design. It costs the one thing it promised the manager: a defensible read before the
audit.

</Verdict>

## Attempt B — the strong answer

*Persona given to the agent: has been paged for a system whose dashboard said it was fine; does the arithmetic before the architecture, and will not claim a number moved without saying what would have shown otherwise.*

**Start with what the audit can and can't see.** Thirty-one of four hundred is 7.75%. The standard error on a proportion that size at n=400 is about 1.3 points, so the 95% interval runs from roughly 5.2% to 10.4%. Do the same for the 6.1% audit and you get 3.8% to 8.5%. Those intervals overlap almost entirely — the standard error on the *difference* between the first audit and the last is about 1.8 points, and the difference is 1.7. So 6.1 → 7.0 → 7.8 is not a trend. It's one number drawn three times with noise wider than the movement. I'd say that in week one, in writing — saying it afterwards sounds like an excuse.

The consequence is the thing that shapes the whole plan: to be *visible* in an n=400 audit, an improvement has to be about 3.6 points or more. Getting to 6% and calling it progress is a coin flip. My working target is under 4%, and the instrument I steer by cannot be the audit — it fires once, in week ten, with ±2.6 points of slop.

**What the capacity math rules out.** Fourteen hundred and seventy drafted lines at twelve minutes from scratch is 294 hours a day against 58 available. Removing the assistant isn't a fallback, it's a shutdown of the desk. Review at two minutes is 49 of those 58 hours, so there are about nine hours a day of slack, and that slack is my only budget for spending more attention on hard lines. Headcount is closed.

**Weeks 1–2: build the instrument.** Three audits give me 1,200 lines adjudicated by two classifiers who conferred — labels drawn from exactly the process I'll be graded by, roughly 84 of them errors. That becomes a frozen set, and nothing in it ever touches a prompt, a rule, or a retrieval index. Alongside it I instrument the live path: retrieved passages, draft code, filed code, chapter, client, licence flag. Then a replay harness over the six million historical lines — run the pipeline offline, compare to what was filed. Disagreement isn't error, but I can calibrate the disagreement-to-error ratio on the 1,200 I have gold answers for, then apply it to a stratified 20,000-line replay and get an estimate with an interval a fraction as wide as the audit's. At roughly seven cents a line that's €1,400 against €6,900 of headroom.

**Weeks 3–5: make retrieval match the schedule's shape.** The schedule is a tree with governing notes at section and chapter level; retrieval is flat top-8 over 21,000 passages. Those don't fit. Flat similarity search pulls lexically similar sibling headings and systematically misses the note that *excludes* a chapter, because an exclusion note rarely resembles the product description. So: two-stage. Classify to chapter first, then to heading within the candidates, and inject the section and chapter notes unconditionally rather than hoping they rank. And the lookup gate, rejecting 0.4%, only checks that a code exists. I'd extend it to check the draft against the exclusions in its own governing notes and against the chapter stage one chose — cheap, deterministic, testable on the frozen set.

**Weeks 4–6, second engineer, in parallel: confidence and triage.** Right now every line gets a flat two minutes. Rank them and the same 58 hours buys far more: six minutes on the riskiest 10%, ninety seconds on the rest, still about 48 hours. The ranking signals are self-consistency across three samples — which is the double-ask two classifiers already do by hand, done properly — retrieval margin, chapter ambiguity between the two stages, and per-client historical agreement. Latency is a real constraint: six seconds with someone waiting, and a fifth of lines arrive under thirty minutes from deadline. Median paperwork lands four hours early, so I pre-draft on arrival and reserve single-shot for the rush lines. The 6% of lines where the code triggers a licence get a hard route regardless of score, to the two classifiers with the best audit record, with the licence condition on screen. That 88 lines a day carries container demurrage the audit's uniform error rate doesn't price at all.

**Weeks 7–8: the review screen, and absorbing the workarounds.** The screen shows code, rationale, invoice. It doesn't show the runner-up code or the note that decides between them — which is most of what a classifier needs in two minutes. I'd add both. The private spreadsheets, one of them 600 rows, are a hand-built error corpus; they become a rules layer and a set of eval cases. Client-suggested codes stop being a silent default and become a displayed signal with that client's historical agreement rate beside it, because some clients are careful and some are optimising duty downward, and nobody currently knows which.

**How I'd know it moved.** Primary: the calibrated replay estimate on the frozen set, pre-registered target under 4% raw draft error. Secondary and high-volume: the 9% change rate, about 132 changes a day, broken out by change type — six thousand-odd events over ten weeks, enough to see real movement. Guardrails: gate rejections, licence escalations, and the ninety-minute commitment, which already missed 40 declarations last month and must not get worse.

**And what would tell me it didn't.** If the offline estimate drops and the change rate doesn't, I've overfit to my own set. If the change rate drops and the audit doesn't, I've taught classifiers to trust the assistant more without making it better — the outcome I'd least like and the reason the 1,200 stay quarantined. I'd also ask the lead for a 100-line read at week six: too small to prove improvement, big enough to work as a tripwire if it comes back above 12%.

<Verdict>

The measurement argument here is not decoration — it changes the plan. The interval work is correct to
the decimal (SE ≈ 1.3 at n=400; SE on the *difference* ≈ 1.8 against a movement of 1.7), and it yields
the consequence most answers skip: "to be *visible* in an n=400 audit, an improvement has to be about
3.6 points or more." Hence a target under 4% and "the instrument I steer by cannot be the audit".

The replacement instrument is the proudest move and the engineering is good: rather than buy labels it
cannot afford, it calibrates a *ratio* — disagreement-to-error — on the audit labels it already has and
transfers it to a "stratified 20,000-line replay", priced correctly at the only per-line unit in the
round — "roughly seven cents a line… €1,400 against €6,900 of headroom."

The population is where it breaks. The audit measures assistant-drafted lines — the residual the
matching rule *could not* fill. The replay runs over "the six million historical lines", every line the
desk ever filed, majority easy repeats by the prompt's own 65%, with no stratum restricting it to that
residual. The calibration does not reach this: it converts disagreement into error, not one population
into another. The one sentence naming the primary metric — "the calibrated replay estimate on the
frozen set" — fuses the right-population instrument (the 1,200) with the wrong-population one (the
20,000), so which denominator carries "pre-registered target under 4%" cannot be recovered from the
text. Relatively the replay is sound; the absolute target is pre-registered on the ambiguity.

The second load-bearing weakness is the triage: "six minutes on the riskiest 10%, ninety seconds on the
rest, still about 48 hours" computes correctly, but the ninety seconds is invented — at the prompt's two
minutes the same split costs 58.8 hours, over budget.

</Verdict>

## Attempt C — the over-built answer

*Persona given to the agent: builds the whole thing at once because bolting the missing half on afterwards costs more; brings the complete shape rather than a first slice, and is comfortable defending its size.*

**Start with the diagnosis, because it decides the shape.** The schedule is a legal traversal — general rules, section notes, chapter notes, heading, subheading. The notes are mostly exclusionary: this chapter does not cover that. The assistant does flat similarity retrieval over 21,000 passages and keeps eight. A binding exclusion three levels up almost never wins a similarity contest against heading text that describes the product well. So the system answers "what does this look like" while the correct answer is "what is this branch legally allowed to contain." That mismatch is the biggest single contributor, and it explains the 0.4% gate — it checks that a code exists, not that it's lawful on its own branch. There is no legality check anywhere in the pipeline.

Second, the two-line rationale is post-hoc narrative. A classifier reviewing it is checking whether a story sounds right, not whether a chain holds — which is why review is such a weak filter: 9% of codes get changed and 7.8% still come back wrong. Third, everything is one lane, so a repeat consumable and a composite article with a competing heading get the same two minutes.

**The classifiers have already told you the answer.** Two keep private error spreadsheets — one is 600 rows of labelled failures nobody has digitised. Several ask twice with reworded descriptions and file the answer that agrees with itself: that is self-consistency, invented by hand, and they're right. Two go to the schedule themselves, which is why 40 declarations blew the ninety-minute commitment last month. The adaptations are a specification. Build them in rather than leave them as unpaid shadow work.

**Measurement first, and not the audit.** 31 of 400 is 7.8% with a 95% interval of roughly 5.3 to 10.8. The 6.1 / 7.0 / 7.8 sequence is not a trend; it is three draws from one distribution. You cannot steer on a ±2.6-point instrument that fires once a quarter and costs two people a week each. So week one builds a frozen internal gold set: the private spreadsheets, the 1,200 adjudicated lines from the three audits already run, the 26 authority corrections, and a draw from the six million historical lines that survived their correction window. Two to three thousand lines, stratified across the 97 chapters, over-weighted on licence-bearing lines. Roughly ±1 point, runs in an hour, and costs the lead classifier's four hours a week rather than a week of two classifiers.

**Then the pipeline, built as one thing.** Staged traversal instead of flat retrieval: shortlist three to five candidate chapters against an index built at section and chapter granularity, pull the binding notes for each branch and force an explicit admit/exclude decision against each, then descend to heading and eight digits. Because notes attach to branches, every candidate code drags its governing notes with it — that's what makes an exclusion check mechanically possible.

On top of that, a verification pass: a separate call sees the proposed code and its governing notes only, and argues against it. Any note on this branch that excludes these goods? A competing heading at the same level? Plus one divergent path for self-consistency. Disagreement between paths becomes the confidence signal, calibrated against the gold set.

Then routing on confidence and stakes. Confident non-licence lines get a fast lane. Disagreement, low confidence, or a verifier contradiction gets flagged with the competing candidates and the deciding note side by side. Licence-bearing lines — 88 a day, where the €300-a-day container sits — escalate by default.

The review screen is part of the build, not a follow-on. The rationale becomes a citation: the code, the heading text, the note clause that admits it, the clause that killed the runner-up. Checking a citation is faster and more accurate than checking a narrative. Every override writes the before/after code and a reason tag into the gold set, which retires the private spreadsheets by doing their job.

**It fits the budgets, which is why it can be this size.** Today 1,470 drafts × 2 minutes = 49 hours against 58 available. At 90 seconds on a confident 70% and 4 minutes on a hard 30%, that's 55 hours — inside 58, with the time spent where it earns something. Spend: three to four calls a line against one today, so roughly €6,500 against a €9,000 envelope. Latency: four fifths of paperwork arrives more than thirty minutes ahead, so run the full pipeline asynchronously at intake and the classifier opens a finished draft; the rushed fifth runs traversal plus verification without self-consistency, about fifteen seconds.

**Order.** Weeks 1–2, both engineers on the eval spine. Weeks 2–5, tree-aware traversal — the largest expected mover. Weeks 4–7, verification, calibration, routing. Weeks 6–8, citation review screen and override capture. Weeks 8–10, batch path, plus a sweep of the auto-filled lines: 4 of 200 across 2,730 lines a day is about 55 wrong daily, comparable to the assistant's own contribution and entirely unwatched. Freeze two weeks out.

**How I know it moved.** Gold set per change, segmented by chapter and licence exposure. Daily live signals: override rate — it should fall in the fast lane and rise in the escalated lane; if it falls everywhere that's automation bias, not improvement, and I'd treat it as a regression. Path disagreement rate. Missed filing commitments, which should go to zero. Two asks of the manager: stratify the next audit toward licence-bearing lines, and agree the decision rule now — 7.8 to 5.0 reads as 20 of 400, and there's a real chance it prints 6.5 on luck alone.

One more thing: never feed the client-suggested code to the model. Their incentive runs toward lower duty. It's a post-hoc disagreement flag, nothing more.

<Verdict>

It leads with the diagnosis and says so: "Start with the diagnosis, because it decides the shape." The
diagnosis is the best-articulated of the three: "the system answers 'what does this look like' while the
correct answer is 'what is this branch legally allowed to contain.'" The design then follows from it properly
rather than being bolted on: because notes attach to branches, "every candidate code drags its governing notes
with it — that's what makes an exclusion check mechanically possible." The citation review screen is the same
idea carried into the human layer, and the observation that classifier workarounds "are a specification" is
the sharpest single sentence any of them produced. It is also the only answer that priced the *full* build —
traversal, verification, routing, review screen — against the human budget in one sum, correctly on its own
terms (55 hours of 58), and scheduled the freeze two weeks out.

The second declared foundation — "Measurement first, and not the audit" — is where it fails, and it fails
structurally rather than in a detail. The golden set mixes adversarial spreadsheet rows, the 26 authority
corrections, audit lines and historical lines "that survived their correction window", over-weighted on
licence-bearing lines, and then attaches "roughly ±1 point" to it. That interval is arithmetically right for a
random sample of 2,500 and meaningless for this one: no population rate can be read off a set built to
over-represent failures. And the survival label is nearly vacuous — 26 corrections against roughly three
million filings. Those two assumptions are also what make the set cost four hours a week instead of a week
each from two classifiers. The instrument it proposes to steer by for ten weeks cannot report the quantity it
claims.

</Verdict>

## Where they actually disagree

Each disagreement below is a decision you will have to make yourself. The last entry is the exception: not a
disagreement but what none of them stopped to check.

### The number to put in writing about the next audit: one you can hit, or one that would be visible

A would put it to the manager now that "if we land at 6.0 it's a real move". B computes that a visible
improvement must be "about 3.6 points or more" and therefore targets under 4%. C sets 5.0 and warns that
"there's a real chance it prints 6.5 on luck alone." These are not degrees of ambition; they are three
different promises, and whichever you choose you are stuck with it in week ten. A's is the one its own quoted
interval classifies as noise: it states ±2.7 and then offers a 1.8-point move as the threshold.

The same split runs backwards over the audits already taken. B: "6.1 → 7.0 → 7.8 is not a trend." C: it "is
not a trend; it is three draws from one distribution." A opens on the sequence as evidence — "it's gone 6.1,
7.0, 7.8. So the review layer is not a filter I can lean on harder" — and computes the ±2.7 that removes it in
its closing paragraph without going back to retract. The conclusion A draws there has other support in the
same paragraph, and survives; the evidence it is drawn from does not.

B and C also publish different intervals for the same 31 of 400. B names its method and its bounds follow it,
two of the four a tenth off the values that method gives — 5.1 and 8.4, against B's 5.2 and 8.5, which changes
nothing it concludes. C names no method: its "95% interval of roughly 5.3 to 10.8" has an upper bound
that is the Wilson figure to a tenth and a lower bound that belongs to neither convention, and it sits
asymmetrically against the ±2.6 C quotes two sentences later. Both reach the same conclusion, and only one of
them can tell you how.

### The classifier's two minutes: a measured fact of the desk, or a parameter you may re-cut

A treats it as fixed and says so — the review layer is not something to lean on harder — and spends its effort
on changing what those two minutes contain: the competing codes and the note that separates them, on screen. B
and C both treat review duration as a variable, compressing an easy lane to ninety seconds to fund a hard lane
of four to six minutes.

Both re-tiering plans go over budget at the prompt's own figure. B's 10/90 split costs 58.8 hours against 58
available once the fast lane runs at two minutes rather than ninety seconds; C's 30/70 split costs 63.7. Each
computes correctly from the ninety seconds, and neither *measured* it: C at least names a mechanism —
"Checking a citation is faster and more accurate than checking a narrative" — but attaches no evidence to the
figure, and B simply asserts it. Which is the whole question, because a fixed two-minute review makes triage a
way of moving attention and a re-cuttable one makes it a way of buying attention. Those are different plans
wearing the same name.

The verdicts price this unevenly: B makes the ninety seconds carry its capacity claim outright, so the flag
lands there; the same unsupported figure sits under C's 55-of-58 sum, which is arithmetically sound on the
assumption and no better supported there. It is priced here for both.

### A golden set enriched with known failures: an instrument that reports a rate, or one that only signals regressions

C builds one deliberately over-weighted toward failures and licence lines — the private spreadsheets, the 26
authority corrections, audit lines, historical lines — and attaches "roughly ±1 point" to it. That interval
belongs to a random sample of 2,500 and says nothing about a set built to over-represent failures; the same
set also mixes the authority's view of a filing with the desk's own, which the prompt defines as what the two
auditing classifiers land on when they confer. B does the opposite by construction: quarantine the adjudicated
labels, calibrate a ratio on them, and apply that ratio to a separately drawn replay — the design exists to
avoid reading a rate straight off an enriched set, though it then draws that replay from the wrong population.
A freezes a mixed set of about 1,500 and attaches no rate to it at all.

This is a live methodological fork, and it decides whether your ten-week instrument reports a number you can
hand to a manager or only a regression signal you can steer by. Neither route is free. B's one mid-flight
check on new labels its own pipeline did not produce is "a 100-line read at week six" — 100 lines worked from
scratch is about 20 hours, against a lead classifier who has four hours a week, and the nine hours a day of
slack B does identify is already committed to its own hard lane.

### The client-suggested code: an incentive you act on, or a reliability you measure

C: "never feed the client-suggested code to the model. Their incentive runs toward lower duty." The prompt
says only that some larger clients send a suggested code and that classifiers tend to file it; the motive is
C's own. B refuses the assumption and pays for the answer instead, displaying the code "with that client's
historical agreement rate beside it, because some clients are careful and some are optimising duty downward,
and nobody currently knows which."

Same artefact, opposite ways of knowing. C's disposition lands on the safe side and costs nothing to adopt,
which is a real argument in a ten-week plan. B pays for instrumentation instead, and buys the only version of
the judgement that can later be shown to be wrong — and it is the desk's larger clients being judged. A never
raises the client codes at all.

### What none of them checked

Four things, and none of them is a disagreement.

**Neither attempt that goes after the auto-filled lines ranks them correctly against the assistant's own
contribution.** The 55 a day is right — 2% of 2,730 — but 7.8% of 1,470 is about 115, and neither computes it.
A inverts the ranking outright: "That's more wrong lines leaving the desk than the assistant produces." C
calls 55 "comparable" to a number that is 115. The move itself is legitimate, and 2,730 lines a day that
nobody reviews is worth somebody's week; the comparison offered to justify it is not. B does not raise the
auto-filled path at all.

**Two of the three price in multiples of the model bill rather than per line**, and both take the end of their
own range that suits the conclusion. A reads its 4–5× as busting a €9,000 envelope its low end fits inside; C
reads "three to four calls a line" as "roughly €6,500", the low end of a range whose ceiling is €8,400 — 93%
of the envelope, with a batch path and an auto-fill sweep still to fund out of it. Both then decide
affordability on the figure they landed on. B is the one that divides: seven cents a line.

**All three read three audits as roughly 1,200 adjudicated labels.** The prompt states the audit's size as a
standing 400 and never confirms the earlier two ran at it — and 6.1% is not a count out of 400.
None of the three noticed either way, and all three size their golden set off the larger number.

**All three score every candidate change against one frozen set for ten weeks** — A: "Everything below gets
scored against it before it goes near production"; B: "the calibrated replay estimate on the frozen set"; C:
"Gold set per change". Each intends the set to be held-out, and each will have selected against it repeatedly
by week three, which makes it a development set whatever the label says. And none of them asks how often the
two auditing classifiers differ *before* they confer — the adjudicated answer is taken as gold, and nobody
measures the noise floor under the labels all three plan to build on.

## The principle

> An error-reduction plan is worth exactly the two numbers the brief leaves you to compute yourself — what the
> instrument that will judge you can actually resolve, and whose minutes absorb every check you add — because
> getting either wrong means the engineering is graded by luck.

</Reveal>

:::tip[Read next]

These five teach the mechanisms the attempts reach for. What none of them teaches is the arithmetic that
decides whether a mechanism is worth doing — sizing a measurement, and pricing a design against a fixed number
of human minutes — which is a gap in both courses rather than something this page can settle.

- [Why AI systems fail in production](/rag-agents/part-3-production/production-failures) — a frozen regression
  set that never moves, beside a rotating one sampled from live traffic. It is the mechanic under every week-one
  move here, and the reason a frozen set selected against for ten weeks stops measuring quality and starts
  measuring familiarity with the set.
- [Retrieval — deep dive](/rag-agents/part-1-rag/retrieval/deep-dive) — routing as a positional decision: route
  to the wrong candidate set and no amount of downstream reranking recovers the passage that was never in it.
  Classifying to a chapter before retrieving inside it is that decision, and it is the half of a two-stage
  design the curriculum already owns.
- [Self-verification & structured output](/rag-agents/part-1-rag/generation/deep-dive) — self-consistency, with
  the applicability test that makes an eight-digit code a fair thing to vote on and the cost multiplier that
  forces it onto a subset; and, held separate from it, chain-of-verification, whose checks are answered with the
  draft they are checking kept out of context.
- [Layered gates and mechanism diversity](/ai-sdlc/part-3-verification/layered-gates) — for every gate, name
  the defect class it structurally cannot catch and pick the next gate to cover exactly that. The rule under
  adding an exclusion check beside a lookup that only asks whether a code exists.
- [Reviewing agent output at volume](/ai-sdlc/part-3-verification/review-at-volume) — automate the cheap checks
  ahead of the human, enumerate what only a person can perceive, then risk-weight what is left. The lesson
  against which a fixed two-minute review has to be argued.

:::

## If they push

These are the three follow-ups an interviewer reaches for next, and what each one exposes.

> Ten weeks are up. The audit comes back at 7.4%. Did anything you built work, and how do you know?

This exposes whether the answer ever understood its instrument. At n=400, 7.4% sits well inside the band the
audit can resolve, so the honest replies are a measurement built on a larger denominator, or a concession that
this audit cannot answer the question and a statement of what would have been needed to answer it — agreed in
week one, when it was still free. An answer that argues about the 0.4 points has mistaken a draw for a result.

> The lead classifier's four hours a week. Show me what you spend them on, and what you give up to spend them
> on something else.

Twenty lines a week worked from scratch is the ceiling those four hours buy, and all three answers spend
them — one on building a labelled set, one on adjudicating a shadow comparison, one on a mid-flight spot
check. An answer that reasoned its way to a design can trade those three against each other out loud. One
assembled from techniques cannot say what any of the four hours is buying, because it never priced them.

> Your checker calls the same model with the same eight passages. Name the class of error it will never catch,
> and tell me how you'd find out how big that class is.

Correlation, asked as falsification rather than as disclosure. Two of the three answers add a second model
call, and both narrow what it sees — the proposed code and its governing notes, not the rationale — which is
the right engineering move and is not the same as knowing the blind spot that remains. The third declines the
model in the check itself and hardens the deterministic lookup instead, which sidesteps the correlation in the
gate and buys a narrower check; the question separates them before it is answered. The class is nameable: an
error already present in the passages both calls read, which no amount of arguing between them removes. Its
size is measurable, but only against labels the pipeline did not produce, which is why the answer to this
question is decided by the eval design and not by the checker.
