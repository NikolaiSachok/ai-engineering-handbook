---
id: where-the-knowledge-lives
title: Where the knowledge lives
sidebar_position: 1
description: Four collections, 400 million tokens, part of it under per-customer NDA, and a commercial director who has heard that a competitor trained a model on their manuals over a weekend. Three attempts at deciding where an organisation's knowledge should live, and which constraint gets applied first.
# The reveal is the method. A page TOC lists every heading inside the collapsed reveal —
# naming all three attempts and the principle before the reader has committed to an answer.
hide_table_of_contents: true
---

# Where the knowledge lives

Four collections hold what this assistant would have to know, and they cannot all be treated the same way.
Six thousand manuals and drawing sets, a third of them scans. Eleven thousand service bulletins, arriving at
forty a month, any of which can cancel an earlier one. Ninety thousand free-text reports written by engineers
at customer sites. And fourteen hundred commissioning dossiers full of other people's trade secrets.

The people who need the answers are mostly not employees: 600 of the 910 work for nineteen dealer companies,
on nineteen different contracts. The last internal knowledge tool was switched off after part of a dossier
reached a public chatbot, and nobody noticed for three weeks.

So the difficulty is not which method grounds an assistant in a private body of knowledge. It is that the
properties deciding it — who may read what, what may leave the building, what a usable answer has to carry,
what a question is allowed to cost — do not all point the same way, and one of them has to be applied first.

> You've joined a manufacturer of industrial food-processing lines — mixers, fillers, thermal tunnels — thirty-four years in the business. 480 employees, 3,100 installed lines across 1,900 customer sites in 26 countries. You are being brought in to decide the shape of an assistant that answers technical questions about that equipment, and to defend that decision to the group commercial director, who signs it off, does not read code, and has already heard from a counterpart at another manufacturer that they "just trained the model on their manuals" over a weekend.
>
> What such an assistant would have to know lives in four collections. There are 6,200 machine manuals and drawing sets as PDFs, about a third of them scans of pre-2009 documents that OCR unevenly. There are 11,000 service bulletins and retrofit notices — that is the cumulative total; the current rate is roughly 40 new ones a month, and a bulletin can supersede an earlier one. There are 90,000 field service reports, free text written by an engineer after a site visit, arriving at roughly 1,100 a month. And there are 1,400 commissioning dossiers, one for each line commissioned since 2011; the other 1,700 installed lines predate the practice and have none. A dossier records that customer's own process settings — temperatures, dwell times, line speeds — which are their trade secrets and sit under per-customer NDAs. Text-extract all four collections and you are looking at roughly 400 million tokens. The documentation for one machine family, drawn from the same four collections, comes to about 300,000 tokens. The model vendor you hold a contract with advertises a one-million-token context window; your contracted rate is €2.40 per million input tokens and €9.60 per million output tokens.
>
> There are two audiences. 310 of the 480 employees work in service and applications. Alongside them sit 600 technicians employed by 19 independent dealer companies — not your staff, on contracts that differ from one another. A commissioning dossier may be read only by the account team assigned to that customer. Last year an internal knowledge tool was switched off after a support engineer pasted part of a dossier into a public chatbot; it took three weeks to notice, and the policy written afterwards says customer identifiers and process settings must not reach an external vendor's servers in clear. Field engineers nevertheless ring the service desk to ask what a named customer's line was set to at commissioning, and they expect the numbers back.
>
> Steady-state usage is estimated at 1,800 questions per working day across those 910 users, over roughly 240 working days a year. The service desk wants an answer inside ten seconds; the full-text bulletin search they use today returns in under a second and is useless to anyone who does not already know the bulletin number. Any answer that touches a procedure has to name the machine family and serial range it applies to, cite the manual or bulletin with its revision, and carry the isolation step where the procedure enters a guarded area. A pilot built over the summer produced fluent paragraphs with none of that. It pasted a 700,000-token slice of the corpus into a single prompt and was graded on 100 questions by two service engineers; 61 answers were judged acceptable, and the two engineers could not agree on why it missed what it missed.
>
> You have €260,000 a year to run the thing, separate from the salaries of the two engineers and the half-time data person you would be given. It is mid-October. The dealer conference is five months out, in mid-March, and the aftersales director has said it needs to be in front of dealers there.
>
> I want the decision procedure, not just the destination. Take me through the criteria you would apply and the order you would apply them in, what each one rules out when you apply it, and where that chain lands on the facts I have given you. Then tell me how you would put the result to the commercial director.

:::note[Why this question]

Every option here can be made to sound reasonable in a paragraph, which is why *which method* is the wrong
thing to ask a lead. This question asks for the ordering: which property of the situation you test first, and
what that test eliminates before you get to the next one. The facts are arranged so that volatility, who may
read what, what may leave the building, cost per question and the shape of an admissible answer do not all
push the same way — so an ordering that works on these facts has to say what each criterion rules *out*,
by name, rather than what it prefers. The second half, addressed to someone holding a budget and a competing
anecdote, is not a communication exercise bolted on. It is where the ordering either survives contact or turns
out to have been a preference.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard.

Three model-written attempts follow. Each comes from a separate agent, given one engineer's habits and the
prompt above and nothing else. No agent saw the other two, and none saw the rubric the verdicts are written
against: an interviewer wrote that rubric before any attempt existed and never read the answers, and a
separate assessor wrote every verdict below against it. The attempts introduce figures of their own; where one
of those is load-bearing and unchecked, the page says so. That arrangement is described
in [how these are made](/design-scenarios/how-these-are-made).

<Reveal>

## Attempt A — the common answer

*Persona given to the agent: reaches for the pattern the write-ups have converged on and is good at assembling it — thinks in components, treats numbers as an implementation detail to settle once the design is agreed.*

**How I'd order the decision.** I don't start from the architecture, I start from the constraints that eliminate architectures, hardest-first — the non-negotiable ones collapse the option space fastest, and everything downstream is then a tuning question. The order here: confidentiality, then corpus shape against the context window, then the answer contract, then latency and unit cost, then the calendar.

**First filter: who is allowed to see what.** This is the one that can't be designed around later, and it's the one that killed the last tool. The dossiers sit under per-customer NDAs, the policy says identifiers and process settings don't leave in clear, and there are three populations — your service and applications staff, 600 dealer technicians on nineteen different contracts, and account teams with dossier access scoped to their own customer. So permissions are not a feature on top of the assistant, they're a property of the retrieval layer. Every chunk carries metadata at ingestion — collection, machine family, serial range, customer ID, document revision, confidentiality class — and every query is filtered against the caller's entitlements *before* the retriever ever scores anything. Not filtered after; a post-filter still means the model saw it. That immediately rules out one shared index everyone queries, and it rules out any design where a single system prompt is trusted to keep the secrets apart. It also tells you the dossier tier probably wants to run against a model you host, so process settings never transit the vendor at all, with the general tier on the contracted vendor. Two tiers, one interface.

**Second filter: does the corpus fit the window.** This is where I'd take on the "just train it on the manuals over a weekend" story, and the pilot. Four hundred million tokens against a one-million-token window is a factor of four hundred — the corpus does not fit, and no window that ships next year makes it fit. One machine family at 300,000 tokens does fit, which is exactly why the summer pilot half-worked: 61 out of 100 is what you get when the right passage happens to be in the slice you pasted. It's not a stable 61 either, it's 61 on whatever the slice covered. And fine-tuning doesn't solve it, because 40 bulletins a month and 1,100 service reports a month means the knowledge is *moving*; you'd be retraining continuously to chase content that a retrieval index absorbs the same day it lands. So: retrieval, not stuffing, and not training. That's the load-bearing call.

**Third filter: the answer contract.** Machine family and serial range, manual or bulletin with its revision, and the isolation step where the procedure enters a guarded area. That's not a prompt-engineering nicety — it means the pipeline has to be able to *produce* those fields, which pushes work back into ingestion. Bulletin supersession has to be modelled as a real relation, so the retriever can prefer the current one and the answer can say what it replaced. Serial ranges have to be extracted into structured metadata, not left in prose. The third of manuals that OCR badly need a quality pass and a re-OCR on the worst, because a citation you can't trust is worse than no answer. And generation gets a structured output contract — if the citation slots can't be filled from retrieved context, the assistant declines and routes to the service desk. Fluent paragraphs with none of that is the failure you already bought once.

**Fourth filter: latency and cost.** Ten seconds is generous for a retrieval pipeline — hybrid search plus a cross-encoder rerank over a few dozen candidates lands well inside that, and it's why I'd keep the agentic loop shallow rather than multi-hop by default. Cost points the same way: pushing 300,000 tokens per question at the contracted input rate is real money at 1,800 questions a day, where retrieving six to ten thousand tokens is an order of magnitude cheaper and faster. The exact k, chunk size, and rerank depth I'd settle empirically on the real documents — those are tuning parameters, and the €260k envelope has room for the index, the embedding refresh, the hosted tier, and the inference.

**Where that lands.** Hybrid retrieval — BM25 for bulletin numbers and part codes, dense embeddings for symptom-shaped questions asked in field language — over a chunked, metadata-rich index; entitlement filtering ahead of scoring; a reranker; two model tiers split on confidentiality; structured, citation-bearing generation with refusal when the evidence isn't there. Then a golden set of questions from the service desk's own ticket history, graded on the citation contract, so we're measuring against a written rubric instead of two engineers disagreeing.

**Scoping to March.** Five months. I'd take the two or three machine families that drive the most service desk volume, all four collections but only for those families, general tier first, dossier tier behind it. That's a demo at the dealer conference that answers real questions with real citations, and a rollout path afterwards.

**Putting it to the commercial director.** I'd say: the counterpart's weekend story works until the manuals change, and ours change forty times a month — training bakes knowledge in, we need it looking knowledge up, so ours stays current by construction. Second, the pilot didn't fail on the model, it failed because it was shown a fraction of the library and couldn't cite what it saw; we fix that by giving it a searchable library rather than a bigger paste. Third, and this is the one he signs for: the last tool died over a leaked dossier, and this design cannot leak one, because entitlements are enforced before the search runs and customer settings never leave our own hardware. Then a date — dealers see two machine families working in March, with the citations on screen.

<Verdict>

The ordering is real: constraints that eliminate architectures first, "everything downstream is then a
tuning question." The first filter does genuine work — "every query is filtered against the caller's
entitlements *before* the retriever ever scores anything. Not filtered after; a post-filter still means the
model saw it" — and rules two things out by name. A criterion with a branch attached, not a consideration.

The second filter is what this attempt calls "the load-bearing call," and it both wins and breaks there. It
wins by being the only attempt to state the corpus-to-window ratio out loud: 400M against 1M is "a factor of
four hundred". It breaks by explaining the pilot — "61 out of 100 is what you get when the right passage
happens to be in the slice you pasted." The prompt says the graders could not agree why it missed; this
supplies the cause they could not, and attaches it to the wrong object: the pilot pasted a 700,000-token
slice, not the 300,000-token family pack just introduced.

The costlier failure is the fourth filter. Every input needed to price this sits in the prompt and it spends
none of them: 300k per question is "real money," retrieval is "an order of magnitude cheaper" (30–50× on its
own 6–10k figure), and "the €260k envelope has room" for an index, an embedding refresh, a self-hosted tier
and inference — an asserted fit, on a budget never divided by 432,000. It is the only attempt producing no
computed euro figure anywhere — and an assertion, unlike a wrong computation, leaves nothing to check.

Best move nobody else makes: splitting retrieval by question shape — BM25 for bulletin numbers, dense for
"symptom-shaped questions asked in field language" — engineering against the incumbent's stated failure mode
without ever naming it.

</Verdict>

## Attempt B — the strong answer

*Persona given to the agent: has operated a knowledge system that the people who depended on it stopped trusting; prices a thing before proposing it, and will not put up a figure not divided out personally.*

I order the criteria so the ones that change the *shape* of the system come before the ones that change its *tuning*. Cost and model choice are tuning. The first two here are shape.

**First: what is allowed to leave the building.** This is first because it partitions the corpus, and everything downstream inherits the partition. The dossiers are per-customer NDA material and the post-incident policy says identifiers and process settings don't reach a vendor's servers in clear. That rules out a single index over all four collections immediately. But the interesting part isn't the dossiers — it's that 90,000 free-text field reports written after site visits will be full of customer names and quoted settings too, and nobody has classified them. Treat collection three as contaminated until proven otherwise: my first week has the data person sampling a few hundred reports to find out how badly. If it's bad, they get entity-scrubbed before indexing or they stay inside.

**Second: what counts as a correct answer.** You've already specified it: machine family and serial range, manual or bulletin with revision, and the isolation step where the procedure enters a guarded area. That's not a quality preference, it's an admissibility rule — an answer missing the isolation step isn't a worse answer, it's a hazard. This criterion kills the weekend story. A model trained on the manuals cannot tell you which revision a sentence came from, because after training there are no sentences, only weights. It cannot be un-taught when a bulletin is superseded. And it can't enforce who may see what, because the access rule is per customer and the weights are one object. Fine-tuning changes how a model writes, not what it knows. Ruled out here, before cost comes up.

**Third: freshness and supersession.** 40 bulletins a month, and a bulletin can supersede an earlier one. That rules out anything with a rebuild cycle measured in weeks. It also forces a design detail people get wrong: superseded does not mean deleted. A line built in 2004 may still legitimately run the old procedure, so the index has to carry revision, supersession pointer, *and* serial-range applicability as first-class fields, and resolve them against the machine in the question. Getting that resolution right is most of the actual engineering; the retrieval part is comparatively ordinary.

**Fourth: unit economics at steady state.** 1,800 questions a day over 240 days is 432,000 questions a year. One machine family's documentation is 300,000 tokens; at €2.40 per million that is €0.72 of input per question before a word of output — €311,000 a year, over budget with nothing else in it. The pilot's 700,000-token prompt is €1.68 a question, €726,000 a year. Retrieval instead: twelve thousand tokens of prompt plus eight hundred of output is €0.037 a question — €16,000 a year. That leaves room to spend four times as much on reranking and multi-step lookups and still be nowhere near €260,000. The budget doesn't go to inference. It goes to ingestion, OCR remediation, and evaluation, where the risk actually lives.

**Fifth: latency.** Ten seconds. A 300,000-token prompt won't reliably return in that, and every retry doubles the bill. Retrieval plus one generation call fits with room. Confirmatory rather than decisive — but it independently rules out the same thing.

**Where the chain lands.** Two systems, not one. Retrieval over manuals, bulletins, and (scrubbed) field reports, with applicability and revision resolved before generation, using the contracted vendor. And separately: the dossiers are not a corpus at all. Temperatures, dwell times, line speeds, one dossier per line — that's a table. I'd extract them once into structured records and serve exact values by serial number from inside our network, with the account-team check at query time and no model in the path. That answers the question field engineers actually ring in with — exactly, in under a second, with no leak surface — and it's the cheapest thing on the list. It also has to answer *"no dossier exists for this line"* out loud for the 1,700 pre-2011 machines, rather than going quiet.

**The pilot's real lesson.** 61 out of 100 with two engineers who couldn't agree why it missed isn't a model result, it's a measurement failure. Before building, I want a labelled set where each question carries its expected serial range, its expected document and revision, and its expected isolation step — so a failure decomposes into retrieval miss, wrong applicability, missing citation, or invented procedure. Those have different fixes. Without it, in March we'd be arguing about impressions again.

**March.** Five months from mid-October, and I'd commit to one or two machine families in front of dealers, not the installed base. Dealers get no dossier access at all — they're 600 people on 19 different contracts, and mapping those contracts is legal's work, not mine. The scanned pre-2009 material gets fixed only for the pilot families, with a per-document extraction score and a hard rule that anything below the bar is excluded and flagged rather than silently indexed.

**To the commercial director,** three things and no architecture. One: the weekend approach costs €311,000 a year against a €260,000 budget, and it still can't tell an engineer which revision it read or keep a customer's settings on our side of the wall. Two: the number is seventy-two cents a question versus four. Three: in March dealers see one machine family answering with a bulletin revision and the isolation step, and a measured acceptance rate against a rubric our engineers agreed on *before* they graded anything.

I'd also tell him what would make me stop: if the field reports turn out to be so full of customer settings that scrubbing them isn't tractable by December, the March demo runs on manuals and bulletins only, and he hears that in December, not in March.

<Verdict>

The strongest single move in the set is here, and it is not an AI move. "The dossiers are not a corpus at
all. Temperatures, dwell times, line speeds, one dossier per line — that's a table." Extract once, serve exact
values by serial number from inside the network, account-team check at query time, **no model in the path**.
It dissolves the scenario's sharpest tension rather than resolving it: no model, no surface to defend. It is
the only attempt to take the model out of the dossier path, and the rubric anticipated two resolutions, not
three.

The arithmetic is the cleanest of the three — €0.72/question at 300k, €311k/year against €260k, €0.037 at
12k+800, €16k/year — though "cleanest" here means internally consistent. Like C, it treats €2.40/M as the rate
a repeatedly-loaded 300,000-token pack attracts, and never marks that as the assumption its elimination turns
on. Unlike C, it leaves itself a second leg: latency, "confirmatory rather than decisive — but it
independently rules out the same thing."

Then it hands the director the wrong label on its own best number: "the weekend approach costs €311,000 a
year". €311k prices per-query long context. The weekend approach is a fine-tune, which is cheaper at
inference, not dearer — so the sentence answering the director's anecdote inverts its own economics. The
refutation that follows ("it still can't tell an engineer which revision it read") is the correct one and does
not need the number.

Two more things it alone does: it names what would stop it — if the field reports cannot be scrubbed by
December, March runs on manuals and bulletins, "and he hears that in December, not in March" — and it states
what fine-tuning *does* change ("how a model writes, not what it knows"), then declines to use it.

</Verdict>

## Attempt C — the over-built answer

*Persona given to the agent: designs for the system as it will have to be in three years; brings the complete shape rather than a first slice, and is comfortable defending its size.*

**The ordering principle**

I apply criteria in order of what they eliminate permanently. Constraints no later engineering can undo go first — contractual, then correctness-of-record, then freshness. Only after those do I let cost and latency in, because those are tuning parameters and the earlier ones are not. The other order is how you get something cheap and fast that legal switches off, which is what happened here last year.

**First criterion: who is allowed to see what, evaluated per request**

910 users, 600 of whom are not our employees — they work for 19 dealer companies on 19 different contracts. A dossier is readable only by the assigned account team. That is not a preference, it is per-customer NDA.

This one criterion does most of the demolition. It rules out training or fine-tuning on the corpus — the weekend story you heard — because weights have no access-control list. Once a customer's dwell times are in the parameters, there is no user for whom they are not, and no way to remove one customer without retraining. It rules out a single shared index queried identically for everyone. It rules out post-filtering results, because by then the text has been through the model and into the answer. Filtering happens before retrieval, against the caller's identity and the dealer contract behind it.

It also splits the corpus into two paths. Manuals, bulletins and reports can go to the vendor. Dossiers cannot, in clear — that is the written policy. But field engineers legitimately need those numbers. So dossier values are substituted with placeholders before anything leaves our network, and rehydrated on our side after generation, for a caller entitled to that customer. The vendor sees "commissioning temperature: [P1]". The engineer sees 84°C. Both constraints hold.

**Second criterion: what makes an answer usable at all**

Any answer touching a procedure must name family and serial range, cite manual or bulletin with revision, and carry the isolation step. The pilot scored 61 out of 100 and the two engineers could not agree on why it missed. The disagreement is the more serious finding. It means there was no rubric, and without a rubric you cannot tell improvement from drift.

So the answer is not free text. It is a structured object with required fields, rendered to prose at the end. A missing isolation step is then a mechanical failure, not a matter of taste, and grading is per-field and objective. This rules out free-form generation as the interface, and "acceptable / not acceptable" as the unit of evaluation.

**Third criterion: the corpus moves under you**

Roughly 40 bulletins and 1,100 reports a month, and bulletins supersede each other. This rules out any refresh cycle slower than the bulletin cycle, and it rules out inferring supersession from text — it is modelled as an explicit edge, and a superseded bulletin is either refused or redirected to its successor. Related: 1,700 lines have no dossier at all. The system must know that absence and say so, because the failure mode is quietly answering from a similar line's settings — the one wrong answer that reaches a guarded area.

**Fourth criterion: arithmetic**

1,800 questions over 240 days is 432,000 a year. One machine family's documentation is 300,000 tokens; at €2.40 per million that is €0.72 a question, €311,000 a year — over budget on input alone, before output, retries, or a second family. The pilot's 700,000-token slice is €1.68 a question, €726,000 a year. Long context per question is not a design choice here, it is arithmetically excluded.

Retrieval into a 20,000-token window costs about six cents a question all-in — call it €27,000 a year. That is what buys us the room for OCR reprocessing of the 2,000-odd bad scans, the in-house path for dossiers, logging, and the evaluation harness, inside €260,000.

**Fifth criterion: ten seconds**

That rules out an open-ended agent loop as the default path. Default is one retrieval, one rerank, one generation, with the cited header streamed first so the engineer sees the source before the prose. Multi-step reasoning exists, but it is the flagged minority route, not the norm.

**Sixth: five months**

Mid-March rules out all four collections at once. One machine family, manuals and bulletins first — they carry the citation obligation and they have structure. Dossiers second, because that path is mostly compliance work. The 90,000 free-text service reports last: noisiest, lowest precision, and the collection most likely to embarrass us in front of dealers. Dealers get the tier with no dossier access, which is also the tier that does not require renegotiating 19 contracts before March.

**How I put it to the commercial director**

Not as RAG versus fine-tuning. Three things.

The weekend story is probably true and does not apply. That manufacturer was not holding 1,900 customers' process settings under NDA — or they are, and they have not found the problem yet. What switched our last tool off was not answer quality.

Then the number he thinks in: six cents a question against seventy-two, and one figure to hold me to — acceptance rate on a fixed question set signed by named engineers, reported monthly, broken down by field, so "it's getting better" is a measurement.

Then the ask, plainly. I want the whole shape funded once, because the parts that look deferrable are the ones that cannot be retrofitted. Retrieval quality I can change in a fortnight. The entitlement model, the supersession graph, the evaluation harness and the logging — the last of which is why the leak took three weeks to notice — are load-bearing, and bolting them on later means rebuilding. And I tell him what will not exist in March, so nobody discovers it at the conference.

<Verdict>

The demolition is the best-argued in the set. "Weights have no access-control list. Once a customer's dwell
times are in the parameters, there is no user for whom they are not, and no way to remove one customer without
retraining." One criterion, three named eliminations, each with a mechanism.

Its proudest move is the masking boundary, and it does not hold as stated. "Dossier values are substituted
with placeholders before anything leaves our network, and rehydrated on our side after generation... The
vendor sees 'commissioning temperature: [P1]'. The engineer sees 84°C. Both constraints hold." The policy
quoted in the prompt covers *customer identifiers and process settings*. This mechanism substitutes values
only — and the query it exists to serve is a field engineer asking what a **named customer's** line was set
to, so the identifier is in the request before any value is masked. Half the policy is unhandled inside a
sentence declaring both constraints satisfied — and a masked value is also one the model cannot reason over.

The rest is disciplined. The 1,700 dossier-less lines become a safety rule: the failure mode is "quietly
answering from a similar line's settings — the one wrong answer that reaches a guarded area." The arithmetic
recomputes. But "long context per question is not a design choice here, it is arithmetically excluded" is the
set's only single-leg elimination — nothing else in the six criteria touches the family pack — so the whole
exclusion rests on €2.40/M applying to a 300,000-token prefix reused all day, and it never asks. The ask then
names four subsystems by component — "the entitlement model, the supersession graph, the evaluation harness
and the logging" — to a man who does not read code, and it is the only director section that does.

</Verdict>

## Where they actually disagree

Each disagreement below is a decision you will have to make yourself. The last entry is the exception: not a
disagreement but an assumption all three made and none of them named — and the difference in what each one had
left standing if it turned out to be wrong.

### Where a customer's commissioning numbers come from: masked through the vendor, a model you host, or no model at all

One collision, three incompatible answers. C sends the question through the vendor with the values replaced
and rehydrates them on return — the vendor sees a placeholder, the entitled engineer sees the number. A stands
up a second, self-hosted model tier so that process settings never transit the vendor at all. B takes the
model out of that path entirely: one dossier per line, temperatures, dwell times and line speeds, served by
serial number from a structured store with the account-team check at query time.

These are not degrees of thoroughness. Each forecloses the others' surface, they price differently, and they
answer different question shapes: B's cannot paraphrase or reason over what it returns, C's cannot compare a
masked value against a spec, A's buys a second model to run and keep current. B's is the strongest of the
three, and the reason is not that it is more thorough — it is that there is no model in the path to defend.
C's is the one that does not hold as stated, for the reason its verdict gives: the policy it quotes covers
identifiers as well as settings, and the request it exists to serve names the customer. B and C then attach the
same safety rule to whichever path is chosen: for the 1,700 lines commissioned before the practice began, the
system has to say out loud that no dossier exists, rather than answer from a similar line.

### Whether the 90,000 field reports may leave the building: safe to send, or the largest unclassified collection on the list

C states flatly that manuals, bulletins and reports can go to the vendor. B says the opposite about the same
collection — treat it as contaminated until proven otherwise, sample a few hundred in week one, and either
scrub the entities before indexing or keep the collection inside. A never asks whether the reports are
contaminated at all, though its own ingestion metadata carries a confidentiality class that would have held the
answer.

The same fact reads both ways: free text written after a site visit, at a customer, by an engineer who was
looking at that customer's machine. Nothing in the prompt classifies it, which is precisely the point. Only
one of the three treats an unclassified collection as a thing to find out about before deciding, and a
confidentiality criterion applied first is worth what it is worth only if it is applied to every collection
rather than to the one already labelled.

### The counterpart's weekend story: a defective method, or a method for a different situation

A refutes it on the merits — the manuals change forty times a month, and training bakes knowledge in. C
concedes it and denies its relevance: probably true, and that manufacturer was not holding customers' process
settings under NDA, or it is and has not found the problem yet. B kills it on a ground neither of the others
uses — admissibility, before cost is raised at all: a trained model cannot say which revision a sentence came from,
cannot be un-taught when a bulletin is superseded, and cannot express a rule that differs per customer.

The choice decides what the director believes on the way out of the room: that his counterpart was foolish, or
that his counterpart was differently situated. A refutes on volatility, which is true of this corpus and says
nothing about the counterpart's. B never has to take a position at all, because a method that cannot cite the
revision it read is inadmissible here whatever it did elsewhere.

### The dossier path: the cheap win, or the expensive deferral

C schedules dossiers second, because that path is mostly compliance work. A puts the general tier first and
the dossier tier behind it. B calls it the cheapest thing on the list and the one that answers the question
field engineers actually ring in with.

Identical facts, opposite classification — and the divergence traces straight back to the first one on this
list, because whether the dossier path is cheap depends entirely on whether there is a model in it. Decide
that question and this one is already decided; decide this one first and you have priced a path whose shape
you have not chosen.

### What all three assumed, and none of them named

All three apply a confidentiality criterion first, and all three are right to. A and C then put an in-house
component inside the €260,000 by name — a self-hosted tier, an in-house path for dossiers — while B's
in-network store is never costed at all. None of them asks whether that budget covers infrastructure, or only
inference.

The sharper one is underneath the arithmetic. Two of the three price the machine-family pack at the contracted
€2.40 per million and eliminate it on the result; the third asserts the same conclusion without producing a
figure. The computations that exist recompute correctly. What is missing is one sentence naming the rate and
the reuse pattern as the assumption the elimination turns on, so that a reader knows which number would have
to move for the option to come back.

The same defect sits under every retrieval estimate here. The prompt supplies no per-question token count, so
each attempt invents one — six to ten thousand for A, twelve thousand plus eight hundred for B, twenty
thousand for C — and every *this fits inside the budget* conclusion is a function of a number its own author
chose. C's €27,000 a year is its 20,000-token window multiplied out and nothing else. None of the three labels
that figure as an assumption either: C hedges it, B states it flat, A gives a range and never prices it.

B leaves itself a second leg — latency, which it marks as confirmatory
rather than decisive — and so survives losing the first. C hardens its figure into an exclusion and has
nothing behind it.

And none of the three so much as mentions the system these engineers use today. The prompt puts a full-text
bulletin search in the building that already returns in under a second and fails for one stated and narrow
reason, and no attempt uses it as a baseline, a fallback, or a comparison — the one place the phrase turns up
at all is B, describing the speed of its own dossier lookup. It is the only piece of software in the prompt
that is already fast, already deployed, and already trusted for the questions it can answer.

## The principle

> Apply first the criteria that no later engineering can undo — who may read what, what may leave the
> building, what makes an answer admissible — and make each elimination binding by computing it from the
> numbers you were handed, remembering that a computed elimination binds only as tightly as the price or
> volume assumed inside it, so the option you just closed stays closed only if you can name the number whose
> change would reopen it.

</Reveal>

:::tip[Read next]

- [Fine-tuning, spend & queues](/rag-agents/part-3-production/llmops/deep-dive) — the two criteria the
  eliminations on this page rest on, in the curriculum's own terms: a permission is expressible as a retrieval
  filter and not as a weight, and corpus against context window is a prior question rather than a cost one.
- [Fusion, ranking & metrics](/rag-agents/part-1-rag/retrieval/deep-dive) — why access control has to cut
  before the search rather than after it, which A and C both insist on, and the cost neither prices: a
  selective pre-filter fights the vector index unless the engine supports filtered search natively.
- [Cost, agents & sovereignty](/rag-agents/part-3-production/cloud-platforms/deep-dive) — the customisation
  ladder none of the three priced: B puts a long-context figure on the weekend approach and nobody prices a
  tune at all. Also the serving fee under a tuned endpoint, and the catch under a self-hosted tier — frontier
  capability lags sovereign and air-gapped environments.
- [Structured knowledge](/rag-agents/part-1-rag/structured-knowledge/) — the general form of taking the model
  out of the dossier path: against a governed semantic layer a model selects a defined query instead of
  deriving one, with access policies applied deterministically before the data is read.
- [Metric internals & judge calibration](/rag-agents/part-1-rag/cross-cutting/evaluation/deep-dive) — the
  pilot's real finding. Two engineers who cannot agree why an answer missed have produced an opinion rather
  than a label; inter-annotator agreement, chance-corrected, is how you find that out before you rebuild.

:::

## If they push

These are the three follow-ups an interviewer reaches for next, and what each one exposes.

> Two of the 19 dealer companies are acquired next spring by a group that also distributes for your closest
> competitor. What in your design changes, and what does not?

This separates a design where access is a runtime property of the request from one where it was settled at
build time. All three attempts put a confidentiality criterion first, though only A and C describe a filter
that cuts before retrieval, and B's runtime check sits on its structured dossier store. The easy half should
follow from any of them: the filter is a data change, and nothing is rebuilt. The harder half is what a flag cannot revoke — anything the old
entitlement already produced and something else now holds. A cached answer, a summary written into an index, a
tuned artefact, an evaluation set assembled from real documents. An answer that stops at *we change the
entitlement table* has not asked where else that content went.

> The commercial director comes back with a quote for a fine-tune that the vendor says will make the answers
> 'sound like us'. What does that buy him, and what does it leave exactly where it was?

This is the same question the weekend story asked, arriving with an authority figure behind it, and the tell
is whether the answer can say yes and no in the same breath. Tuning can genuinely fix answer shape and house
vocabulary, which is the failure the summer pilot actually exhibited — fluent paragraphs carrying none of the
three mandatory elements. It moves nothing about supersession, nothing about per-customer permission, and
nothing about citing a revision that did not exist when the weights were frozen. Worth noticing: none of the
three attempts proposes a tuned model for anything, including format. Only C demolishes it on confidentiality;
A refutes it on volatility and B on admissibility. Only B names what tuning would still change — "how a model
writes, not what it knows" — and even it does not come back to ask what that is worth once the knowledge
question is settled elsewhere.

> Six months in, answers are good and the service desk says it is slower than the old bulletin search. What do
> you look at first, and what would you be willing to make worse?

This forces a named trade rather than a promise to optimise: context size, rerank depth, a small-model first
pass, a separate route for the questions that are lookups. It also walks the candidate back to the thing every
attempt on this page stepped over. The old search is sub-second and useless to anyone who does not already
know the bulletin number, so the desk may be comparing two different classes of question, and which class got
slower is the first thing to establish. Someone who has been paged for this says which percentile they mean
before saying what they would spend to move it.
