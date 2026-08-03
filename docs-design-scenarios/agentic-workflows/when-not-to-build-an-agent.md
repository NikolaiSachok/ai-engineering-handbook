---
id: when-not-to-build-an-agent
title: The work that should stay a workflow
sidebar_position: 8
description: A 34-person accredited testing laboratory has an unspent model budget, a director who has promised the board an agent by year end, and a scheduler leaving in twelve weeks with the only copy of how the lab plans its day. Three attempts at deciding which pieces of work take a model and which must not.
# The reveal is the method. A page TOC lists every heading inside the collapsed reveal —
# naming all three attempts and the principle before the reader has committed to an answer.
hide_table_of_contents: true
---

# The work that should stay a workflow

Four things in this laboratory look like a job for a model. Submissions arrive as photographs of filled-in
paper and then sit for days waiting on a question nobody has asked yet. A scheduler spends ninety minutes an
afternoon building tomorrow's run sheets, and overrides her
own written rules ten times a week for reasons that never repeat. Analysts spend forty minutes each on thirty
out-of-spec results. And fifteen percent of reports carry a claim that only four people in the building are
permitted to make.

The last of those is the one that cannot be taken back. Everything else is a draft somebody corrects before it
leaves the building. A signed report is what a client releases a batch against, and what an assessor pulls at
the next assessment and asks how it came to say what it says.

So the difficulty is not whether to build an agent here. It is four pieces of work that look alike from the
outside and have four different shapes underneath — and twelve weeks that do not leave room to be wrong twice.

> You've joined an independent contract testing laboratory — 34 staff, one site, accredited to an ISO/IEC 17025-style standard for 40 methods across four techniques. Clients send samples; the lab tests them and issues a report under that accreditation, and for a lot of clients that report is what lets them release a batch, close a claim, or sign off a structure. There are 19 analysts. You are the only software engineer. The LIMS is a commercial system, eight years in, with a REST API covering samples, tests, results, statuses and report records. Model spend of €2,500 a month is approved and none of it is being used. The lab director came back from an industry conference in the spring and has told the board there will be "an agent in the lab" by year end.
>
> About 900 samples arrive a week in roughly 260 submissions. A submission is one client's consignment — anywhere from a single sample to forty — and it produces exactly one report. Those 900 samples generate about 2,200 individual tests. Of the 260 submissions, 140 come through the client web portal, which will not accept a submission with a required field missing; 95 arrive as email with a form attached — the lab's PDF, the client's own spreadsheet, a phone photograph of a filled-in paper form; and 25 come as paper in the box with the samples. The portal has been live three years and has sat at roughly 54% of submissions for the last two. The rest either won't use it, or, like the lab's largest client at about 18% of submissions, send files their own system generates.
>
> Of those 120 non-portal submissions a week, about 35 can't be booked in as they arrive: a test named in words that match no method on the schedule, a client spec referenced but not attached, sample volume too small for everything requested, no purchase order. Someone emails the client and waits — median 1.8 working days to an answer, and the sample sits.
>
> A standard job is promised in 10 working days and the median is 9: 3.5 days before the first test starts, 2 on the bench, 3.5 between the last result and the issued report. That 3.5-day front end is the median across all standard jobs, the ones that got chased and the ones that didn't. 215 of the 260 weekly submissions run at that standard rate and about 26 miss the promised date; there's no penalty clause on those, but the two biggest client complaints last year were both about dates and one ended in a credit. The other 45 submissions are express — 5 days, €150 surcharge — and about 6 a week land late, which by contract waives the surcharge. Those waived surcharges are lost revenue; the €2,500 is approved IT spend and doesn't move if the lateness stops.
>
> Every afternoon the scheduler builds tomorrow's run sheets off the LIMS queue: which samples go on which of the nine benches, in which batch, in what order, around sample hold times, prep capacity, and who is signed off to run what. It takes her about 90 minutes. The rules are a six-page controlled work instruction she wrote herself. She also overrides them around ten times a week, and when you ask why, she gives you a reason each time, and it is not the same reason. She has given notice: her last day is twelve weeks out, which is roughly where the director's "by year end" falls too.
>
> About 30 of the 2,200 weekly tests come back outside a client's spec or the lab's own quality-control limits. The procedure for those is written and the outcomes are enumerated — repeat the test, re-prepare from the retained sample, invalidate the run, or report the result with a note — and whichever is chosen is recorded with the reason. Getting to the choice means reading the run record, the prep sheet, the analyst's notes, and what that client's samples did the last few times; analysts put about 40 minutes into each one.
>
> Reports come out of the LIMS: the results table is generated, method and deviation sections assemble from templates. About 15% carry a statement of conformity — this batch meets the standard the client named — which under the accreditation may only be made by one of the four authorised signatories. All four are working analysts drawn from the 19.
>
> Two years ago the lab issued three reports it later had to withdraw. One client had already shipped against theirs. The investigation ran four months; for six weeks two of the four signatories signed nothing they hadn't personally re-worked, and that client moved about half its volume elsewhere — a different client from today's largest. At the accreditation assessment, for reports the assessor picks, the lab has to show how each result came to be what it is and who decided anything that was decided.
>
> Twelve weeks, one of you. Tell me what you build, in what order, what you deliberately don't, and what you say to the director in December when she asks where the agent is.

:::note[Why this question]

Three terms first. *An enumerable decision* is one whose complete set of possible outcomes is known and written
down in advance: the work is to establish which item on a fixed list applies, and nothing outside the list can
be produced. Open-ended work is the other case — the set of possible outputs is not knowable ahead of time, so
there is no list to choose from. *A controlled work instruction* is a document issued under the laboratory's
quality system — formally approved, versioned, and changed only through that system; *controlled* is the
load-bearing word, and the largest unexamined finding on this page turns on it. And the *LIMS* is the
laboratory information management system: the commercial database in which samples, tests, results and reports
live.

Almost every constraint in this prompt pushes toward autonomy. An approved budget nobody has spent. A director
who has already told the board what will exist by year end. A person twelve weeks from the door who is the
only copy of something. And human time stuck in plain sight: ninety minutes an afternoon on the run sheet,
twenty analyst-hours a week on out-of-spec results, a hundred and twenty submissions a week that somebody has
to read before anything happens to the samples. Against all of that the lab has exactly one irreversible act —
a report a named person signs, which an assessor may later pull and audit.

What is under test is whether an engineer decides the shape of each piece of work separately, on properties
they can name, rather than deciding the shape of the whole system once and then defending it. An engineer who
builds an agent everywhere and an engineer who builds one nowhere fail in the same way: they answered a
question about a laboratory with a question about a technology.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard.

Three model-written attempts follow. Each comes from a separate agent given one engineer's habits and the
prompt above. No agent saw the other two, and none saw the scoring standard the verdicts are written against —
that was fixed before any attempt existed, and a separate assessor applies it. The attempts introduce figures
of their own; where one of those is load-bearing and unchecked, the page says so. That arrangement is
described in [how these are made](/design-scenarios/how-these-are-made).

<Reveal>

## Attempt A — the diagnostic answer

*Persona given to the agent: Has stood in front of an outside assessor and explained, step by step, why a system did what it did, to someone who did not know or care what a model is. Has also been the only person left maintaining something built three jobs ago, so thinks about what survives them — the smallest permanent thing that still works when nobody remembers why it exists. Unmoved by whether something is called an agent.*

**Week one I measure, I don't build.** The LIMS has a REST API with statuses, so every timestamp I need is already there. The number I want first is the distribution behind that 3.5-day front end, not its median. Here's why: 35 of 260 submissions are blocked at intake, that's 13%, and 13% of a population does not move a median. So the 3.5 days most standard jobs wait before their first test is *not* the query loop — it's structural queue time. The query loop lives in the tail, and the tail is where the express jobs die. That single check changes what I build first and in what order, and it costs me two days.

**Build one: intake triage, live by week four.** 120 non-portal submissions a week arrive as PDFs, client spreadsheets, and phone photos of paper. A model reads them, extracts the fields, maps the requested tests against the method schedule, and checks the four failure classes you named — unmatched test name, spec referenced but not attached, insufficient volume, missing PO. Where it finds one, it drafts the client query and puts it in the receptionist's outbox. She sends it.

I cannot compress the client's 1.8 days. I can compress the hours or days before anyone notices there's a question to ask. That's the whole win, and it lands almost entirely on the 45 express submissions where 1.8 days eats a third of a 5-day promise. Six late express jobs a week at €150 is about €45k a year in waived surcharge. If I halve that I've paid for myself several times over, and unlike the standard-job lateness it's a number the finance director already recognises.

It does not book the sample in. It pre-fills the booking and a human confirms it, because a mis-booked test is a wrong test, and a wrong test is a wrong report.

**The scheduler is the actual emergency, and it starts day one.** She leaves in twelve weeks with ten decisions a week that aren't in her six-page work instruction, each with a different reason. That's the part of the lab that isn't written down anywhere, and it's walking out the door on the same date the director's deadline lands.

From day one, every override gets captured at the moment she makes it, in her words. Twelve weeks is roughly 120 of them. Meanwhile I write a solver — not a model — that produces tomorrow's draft run sheet from the documented rules: hold times, prep capacity, competency sign-off. Constraint satisfaction is a solved problem and I'm not putting a language model in the middle of it. She reviews the draft each afternoon instead of building from scratch. Every edit she makes is a labelled example, and I use a model for the one thing it's genuinely good at here: turning her free-text reason into a structured candidate rule I can read, argue with, and either promote into the instruction or leave as a documented exception.

By her last day the draft is mostly right, and where it's wrong there's a written reason. Her successor edits instead of guessing. That's the smallest permanent thing on this list — it will still be doing its job when everyone involved has moved on.

**Build three, weeks eight to eleven: the out-of-spec brief.** Thirty a week at forty minutes is twenty analyst-hours, and most of it is gathering — run record, prep sheet, analyst notes, that client's recent history. The model assembles all of it into one page with the four enumerated outcomes and the evidence for and against each. It does not pick one. The analyst picks and records the reason, as now. Forty minutes to fifteen is roughly twelve hours a week back to the bench.

**What I deliberately don't build.** Nothing goes near the statement of conformity. Not on risk grounds — on accreditation grounds. The standard names four people who may make that call. A tool that pre-fills it turns a signatory into someone who agrees with a screen, which is precisely the failure mode that produced three withdrawn reports and a four-month investigation. I don't touch the portal's 54%; your largest client sends machine-generated files, so the answer there is a parser for their format, not a campaign. And I don't touch report generation until I know whether that back-end 3.5 days is composition time or signatory queue time. I suspect queue.

**Spend.** I expect to use two to three hundred a month, not €2,500. The budget was never the constraint.

**December.** I show her three things running and the express lateness curve. Then I tell her the constraint isn't the model and it isn't the money — it's that at the next assessment we have to show, for a report the assessor picks, who decided what. Everything here has a name attached to every decision and a record of what the machine put in front of that person. That's the version of "an agent in the lab" that survives an assessor, and it's the only version worth having her name on.

<Verdict>

A is the only attempt that asks whether the headline number means what everyone assumes. "Week one I measure,
I don't build." Then the argument: "35 of 260 submissions are blocked at intake, that's 13%", and "13% of a
population does not move a median." The conclusion is right and it is the most valuable single thought on the
page — the 3.5-day front end is mostly structural queue that would still be there if every query were answered
instantly, so a queue-clearing intake tool will barely shift it. A alone also notices that the *other* 3.5
days is undiagnosed and refuses to guess: "I don't touch report generation until I know whether that back-end
3.5 days is composition time or signatory queue time. I suspect queue."

Having established that the median is structural, A builds the same three things as everyone else and never
returns to the queue — the finding changes the justification, not the plan. A claims more than that: "That
single check changes what I build first and in what order". It never states what the order would otherwise
have been, and intake goes first regardless, exactly as it does for B and C. And the justification is wrong.
"it lands almost entirely on the 45 express submissions" does not survive A's own arithmetic: allocate the 35
blocked submissions proportionally and about 29 are standard, six express. A standard job runs a nine-day
median against a ten-day promise, so a day of slack against a 1.8-day median chase — a chased standard job
is late by construction, and at 29 chased against 26 misses, chased standard jobs are numerous enough to be
the whole miss population. A discards the larger half of its own case. A's audit record is the thinnest of the
three, asserted as a property of everything in the closing paragraph and never scheduled or given fields.

</Verdict>

## Attempt B — the plumbing-first answer

*Persona given to the agent: What has bitten them, repeatedly, is undocumented knowledge walking out of the door. Treats a departure date as the hard edge of a project and plans backwards from it. Comfortable with the unglamorous half of a problem, low tolerance for building the interesting part first. When told a decision "depends", wants to know how much of it actually depends and how much was simply never written down.*

**The date that governs this project is week twelve, not December.** The scheduler leaving is the only irreversible event on the board. Everything else — late reports, stuck intake, the director's agent — will still be there in January. Her override reasons will not. She makes roughly ten a week and can justify each one on the spot, which means the knowledge exists and is simply unwritten. Twelve weeks of capture is about 120 cases. Start in week four instead of week one and I've thrown away a quarter of the only training and specification data I will ever get, for free.

**Week 1–2: the capture instrument and the decision log.** Two pieces of plumbing, both dull. First, a shim on the daily run-sheet build: her final sheet, the sheet the six-page work instruction would have produced, the diff, and for each override a reason — picked from a list that grows as she uses it, free text alongside. Thirty seconds per override, ten a week. Second, a decision log that every later component writes to: inputs seen, proposal made, model and prompt version, who accepted or changed it, when. That log is not compliance theatre. At the assessment the lab has to show how a result became what it is and who decided anything decided. If I bolt that on at the end I will be reconstructing it from logs and memory, which is the position the four-month investigation put people in two years ago.

**Week 2–5: intake, starting with the boring 18%.** The largest client is about 47 submissions a week, all generated by one system in one shape. That is a parser, not a model. It's the single biggest intake win in the lab and there is nothing intelligent about it. Then the remaining ~73 non-portal submissions: extract fields from the PDF, the spreadsheet, the photograph; match requested tests against the method schedule by name and synonym; check volume against the sum of what's requested; check the PO and any referenced spec is actually attached. Output is a draft booking with a confidence per field and a completeness verdict, sitting in front of the receipt clerk. It does not book anything itself.

The win isn't only the 1.8-day median wait on the 35 stuck submissions. It's that the query email leaves within the hour of receipt rather than whenever someone opens the box. The 3.5-day front end is 39% of the 9-day median, and it is the part of the job where nothing is happening to the sample. That is where the 26 standard and 6 express misses live. Six waived surcharges a week is roughly €43k a year against a €30k model budget — the budget isn't the constraint, but it's the number I'd want on the record.

**Week 4–10: the scheduler's rules, shadow-running.** I code the work instruction as a deterministic solver — hold times, prep capacity, bench assignment, analyst sign-off. It proposes tomorrow's sheet every afternoon; she corrects it; we spend thirty minutes on the diff. Those thirty minutes are the highest-value half hour in the twelve weeks, because that is how I find out how much of "it depends" is a rule nobody wrote down. My expectation is that most of the ten weekly overrides collapse into four or five recurring conditions and a genuine tail stays judgement. The tail is fine — it just has to be visible, so her successor knows where the model ends.

**Week 9–11: evidence packs for out-of-spec results.** Thirty a week at 40 minutes is about half an analyst. I assemble the run record, the prep sheet, the analyst's notes and that client's recent history into one page, with the four enumerated outcomes listed and the prior decisions on similar cases shown. I do not have it choose. Halving 40 minutes by removing the fetching is worth more than a recommendation nobody will trust.

**What I deliberately don't build.** Nothing writes to the LIMS unattended. Nothing goes near a statement of conformity — 15% of reports, four authorised signatories, and putting a model in that path is a nonconformity waiting for an assessor. No work on portal adoption; 54% for two years is a client-behaviour fact, and I'd rather parse one large client's format than argue with forty small ones.

**December.** I'd show her tomorrow's run sheet, generated, with the overrides it predicted and the ones it flagged as unlike anything it has seen. The agent proposes and a named person commits, and that boundary is the design, because the accreditation requires a decider and the last three withdrawn reports cost four months, six weeks of two signatories re-working everything, and half a client's volume. And the line for the board: the scheduler left and the schedule didn't.

<Verdict>

B's opening is the sharpest sentence in the set: "The date that governs this project is week twelve, not
December." And B is the only attempt that makes the audit record a build rather than a description — weeks one
and two, "a decision log that every later component writes to: inputs seen, proposal made, model and prompt
version, who accepted or changed it, when", justified by the one argument that forces the ordering: "If I bolt
that on at the end I will be reconstructing it from logs and memory, which is the position the four-month
investigation put people in two years ago." That is the audit obligation satisfied structurally rather than
rhetorically, and, with the override capture, one of the two components on this page that genuinely cannot be
retrofitted. B's intake split — "the boring 18%" as "a parser, not a model", then the variable remainder — is
the cleanest statement of the model-or-parser criterion anyone gives.

B's evidence that intake is where the dates break is the weakest of the three. "The 3.5-day front end is 39%
of the 9-day median" is arithmetically correct and inferentially inert: a median describes the ordinary case,
not the misses, and A's objection lands squarely on it. B also leans on "a draft booking with a confidence per
field" as the trust mechanism — a model's self-reported confidence is not evidence of accuracy, and B never
proposes to calibrate it, in a building whose entire professional culture is that an unvalidated measurement
is not a measurement.

</Verdict>

## Attempt C — the hours-back answer

*Persona given to the agent: Measured on hours given back, and looks for where expensive people spend time reading rather than deciding. Unstructured input does not worry them — a good model has consistently got through what rules could not. Conscious that whatever gets built has to be visible to somebody outside engineering by a date, because work nobody can see does not get funded twice.*

**Where the time actually is.** I have two deadlines, not one. Year end is the director's. Twelve weeks is the scheduler's, and hers is the real one, because on her last day the lab loses a capability it has no second copy of. So the first thing I do — week one, before I write anything — is instrument her. Every override gets a one-screen form at the moment she makes it: what the work instruction said, what she did instead, why, in her words. Ten a week for twelve weeks is about 120 labelled cases of the thing that isn't in the six pages. That costs her ninety seconds a day and it is the single highest-value artefact in this building. It's also the honest answer to why her reasons don't repeat: the work instruction is the part she could write down, and the overrides are the part she couldn't.

**Weeks 1–4: intake.** 120 submissions a week arrive as something a person has to read — the lab's PDF, a client spreadsheet, a photo of paper. The largest client is roughly 47 of those and its files come out of a machine, so they're consistent: that's a parser, not a model, and it's done in days. The other ~73 are where the model earns its keep. Extraction into the LIMS booking fields, then validation against the live method schedule, hold times, and volume — the same checks the portal enforces, applied to email and paper.

The output I care about isn't the booking. It's the query. 35 submissions a week stall on something enumerable — a test named in words that match no method, a spec referenced and not attached, not enough sample, no PO. Today someone finds that when they get to it, then writes an email, then waits 1.8 days. I want the gap detected within minutes of the file landing and a drafted client email naming precisely what's missing, for a human to send. That doesn't shorten the client's reply time; it removes the queue in front of it. Ground truth is free here: several thousand historical submissions with the LIMS record of what was actually booked. I can measure field-level extraction accuracy before anyone trusts it.

**Weeks 5–8: the run sheet.** The six pages are constraints, so I implement them as constraints — a solver, not a prompt. Benches, batches, hold times, prep capacity, signed-off analysts. Ninety minutes becomes a sheet on her desk in the morning that she edits rather than builds. The model's job is narration: which constraint bound, what it cost to satisfy, what would free up if one sample moved. Every edit she makes flows into the same override log. By her last day I want the sheet to be defensible without her, and I want her replacement reading her reasons rather than guessing at them.

**Weeks 7–11: the out-of-spec dossier.** 30 tests a week, 40 minutes each — about 20 analyst-hours, half an FTE, spent almost entirely assembling: run record, prep sheet, analyst notes, what this client's samples did the last several times. I build the assembly, not the verdict. One page, everything cited back to source, plus the enumerated four outcomes with what the record supports for each. The analyst chooses and writes the reason. That's not caution about accreditation, it's where the value is — the decision was never the expensive part. Two years of recorded decisions with reasons gives me a real eval set for whether the dossier surfaced what the analyst actually used.

**What I don't build.** Nothing touches the statement of conformity. Four signatories, and this lab withdrew three reports two years ago and spent four months and half a client's volume paying for it. Model output never becomes record — it becomes an input a named human accepts or edits, with prompt, version, retrieved sources and human action logged. That log is what I hand the assessor. I don't try to move the portal off 54%; three years flat is a settled preference. I don't replace the LIMS. No chat interface.

**The number that funds year two.** Six express jobs a week land late and waive €150 — about €43k a year. 26 standard jobs miss, with no penalty but two of last year's biggest complaints and one credit. The 3.5-day front end is where both live. I'll spend maybe a third of the €2,500.

**December.** I show her the agent working. It books in samples, drafts the queries, and it built this morning's run sheet without the person who used to. Then I tell her what it deliberately doesn't do and why that's the reason the accreditation body will still like us in March.

<Verdict>

C states the where-the-value-is criterion better than either rival and then applies it against the
temptation: "That's not caution about accreditation, it's where the value is — the decision was never the
expensive part." That is the version
of the argument you can compute with, and it generalises. C is also the only attempt that says how it would
know a model component works *before* anyone trusts it — "Ground truth is free here: several thousand
historical submissions with the LIMS record of what was actually booked. I can measure field-level extraction
accuracy before anyone trusts it", and again for the dossier: "Two years of recorded decisions with reasons
gives me a real eval set for whether the dossier surfaced what the analyst actually used." Nobody else names
existing records as labels. C's read of the scheduler is the most honest on the page: "the work instruction is
the part she could write down, and the overrides are the part she couldn't." And reusing the portal's existing
rule set as the intake validator — "the same checks the portal enforces, applied to email and paper" — is a
free win neither rival takes.

C is the only attempt that never says, at the intake step itself, who commits the booking — and the place it
shows is December: "It books in samples, drafts the queries, and it built this morning's run sheet without
the person who used to." That contradicts C's own governing rule — "Model output never becomes record — it
becomes an input a named human accepts or edits" — and it is the one place where the director's word visibly
pulls the description past the design.

</Verdict>

## Where they actually disagree

Each disagreement below is a decision you will have to make yourself. The last entry is the exception: not a
disagreement but the place all three arrived together, and what went unexamined once they had.

### Where the 3.5-day front end comes from: structural queue, or submissions waiting on a client answer

A contradicts B and C with an argument, and A is right about the median and wrong about the consequence. The
prompt says as much: the figure is "the median across all standard jobs, the ones that got chased and the ones
that didn't", and at 35 blocked of 260 the overwhelming majority of jobs in that median were never chased. So
the front end is queue, not query. A's stated reason is too strong — a 13% subpopulation
*can* move a median, bounded by the gap between roughly the 36th and 50th percentile, because shifting 13% of
the population can displace the median by at most 13 percentile points — but the defensible form, that a
1.8-day delay on 13% cannot *produce* a 3.5-day median, is correct. Then A mis-allocates: 35 split
proportionally, in the absence of any data on how express work splits between portal and post, is about 29
standard and six express, and a standard job runs a nine-day median against a ten-day promise, so a day of
slack against a 1.8-day chase makes a chased standard job late by construction. Twenty-nine chased against
26 misses.

**What turns on it is the instrument, not the build.** All three build intake triage first and all three are
right to. But ship it, watch the 3.5-day median, and you will see almost nothing move and conclude it failed —
because most of that median never had a query in it. The measurements that move are the late counts,
receipt-to-query latency, and the P90 of the front end. A was the only candidate equipped to avoid that trap
and aimed at the wrong half of the population; B and C aimed at the right population with an argument that
would have mismeasured it.

### What the model does inside the scheduling piece: her reasons, the diff, or the output

A puts it on her reasons — "turning her free-text reason into a structured candidate rule I can read, argue
with, and either promote into the instruction or leave as a documented exception." B puts no model there at
all: a reason list, a diff, and "we spend thirty minutes on the diff." C puts it on the output — "The model's
job is narration: which constraint bound, what it cost to satisfy, what would free up if one sample moved."

A's is the only one that converts them without the engineer in the room. B and C both aim at the successor —
B wants the judgement tail visible, C wants her replacement reading the reasons rather than guessing — but
only A makes the conversion a component rather than a standing meeting. B's is the most reliable and the least
scalable: it works because the engineer is sitting next to her, a condition with the same twelve-week expiry
as the knowledge. C's narration solves a real and different problem — a successor trusting a sheet she did not
build — and does nothing about the overrides themselves.

### The audit log: a first build, or a property of later ones

B schedules it in weeks one and two as plumbing. A and C describe it as a property of everything else — A in
the December paragraph, C under what it will not build, though C names the richer field set including
retrieved sources. B's argument is drawn from the prompt's own history: a record assembled afterwards is the
four-month investigation. C's fields are better, B's placement is better, and placement wins, because fields
can be added in week six and history cannot.

### Why the out-of-spec decision stays with the analyst: nobody would trust it, or it is not where the money is

Two reasons and an omission, and this is the most instructive disagreement here. B: nobody would use it —
"Halving 40 minutes by removing the fetching is worth more than a recommendation nobody will trust." C: it is
not where the money is — "the decision was never the expensive part." A gives no reason at all, and simply has
the analyst pick "as now."

C's is the strongest because it is the only one you can compute: A's own estimate puts assembly at 25 of the
40 minutes, capping the decision half at about 7.5 analyst-hours a week — automating a bit over a third of the
time for all of the risk. B's trust argument concedes the case the moment trust improves. A, having done the
arithmetic that supports C's position, declines to state the conclusion.

### Whether the extraction is measured before anyone relies on it: checked against the record, or controlled by a human

C alone proposes to check it against what the LIMS already recorded as booked. B substitutes a model
self-report; A substitutes a human confirm. Both are reasonable operational controls and neither is evidence.
Shipping an extraction step with no measured accuracy, into a building whose professional norm is that a method
is not trusted until its performance has been demonstrated, is the deepest mismatch on the page — and two of
three made it.

### What all three agreed on, and none of them examined

All three: capture the overrides from week one; implement the six-page instruction as a deterministic solver;
keep the model on the unstructured and the assembling work, never on the commit; assemble but never decide the
out-of-spec case; put nothing near the statement of conformity; refuse the portal campaign; fund the argument
on the waived express surcharge. The plans are near-identical, and that is evidence about the **problem**
rather than about the candidates — this prompt's facts are strongly over-determining, so a careful reader is
walked to the architecture. The candidates separated only on the questions the prompt did not answer for them: what the
numbers mean, how you would know it worked, and who owns it afterwards.

Four things went unexamined inside the agreement. **Nobody puts their own software under the quality system.**
An accreditation regime of this kind normally carries validation and change-control obligations for software
affecting results, and no attempt asks whether this one does — C's accuracy measurement, the closest anyone
comes, is an engineering check rather than a controlled one. And the solver does not merely assist the
scheduler, it replaces a controlled work instruction. All three designed for the assessor's question about
reports and forgot the assessor's question about tools. **Nobody computes the signatory load** — 15% of 260 is
about 39 reports a week needing one of four authorised signatories who are also working analysts, which nobody
sized, and which is the only candidate on the table for the back-end 3.5 days and the step the prompt shows to
be fragile. **Nobody names an owner for what they built** — four new systems, one engineer, and all three
correctly identify the scheduler as a single point of failure whose departure is the emergency, then replace
her with themselves, unremarked. **And nobody talks to the director before December**
— every candidate avoided building to her word, correctly, and then left the date itself unexamined, when week
one is when that conversation costs least.

## The principle

> Before you build to move a number, check that the number contains the thing you are fixing — a median is
> made of the ordinary cases, and the work that breaks promises lives in the tail.

</Reveal>

:::tip[Read next]

Unusually for a page filed under agentic workflows, most of these links are in the AI SDLC course, because
that is where this scenario's back half — gating the irreversible step, and the record an external assessor
reads — is taught.

- [Agentic RAG](/rag-agents/part-2-agents/agentic-rag/) — the agency ladder as a spectrum, router → query
  planning → full loop, which this scenario extends to the rung below the router: no loop at all. A full loop
  is a cost, not a prize.
- [Reviewing agent output at volume](/ai-sdlc/part-3-verification/review-at-volume) — the rebuttal to blanket
  review, and the constructive move most teams skip: write down the list of things only a human can perceive,
  and spend the human strictly on that list.
- [Roles, and where the human stays](/ai-sdlc/part-2-loop/roles-and-the-human) — why a successor should sit
  *above* the loop rather than inside it, and the named failure any of these builds walks toward: overload
  evicts the human first.
- [Reliability & scale](/rag-agents/part-2-agents/tool-use/deep-dive) — the concrete shape of gating one step
  and not the rest: a dry-run/confirm split on irreversible writes, and read tools kept structurally separate
  from write tools.
- [The enterprise tier: audit, provenance, and what's required](/ai-sdlc/part-5-scale-governance/enterprise-tier/)
  — what an external assessor's record must contain once part of the path was automated, and why
  non-repudiation rather than completeness is what makes it evidence.

:::

## If they push

These are the three follow-ups an interviewer reaches for next, and what each one exposes.

> She's not leaving after all — she withdrew her notice this morning. Does anything you just told me change?

This exposes whether the twelve-week date was a deadline or a rationale. A plan that captured the overrides
only because she was leaving now has no reason to capture them — which is the wrong conclusion, because the
six pages are still the only written version of the rules and the ten weekly exceptions are still nowhere.
What should change is the urgency and the sequencing, not the artefact: a longer shadow-running period, and
candidate rules promoted into the work instruction with her sitting there to argue about them rather than
inferred from a log after she has gone. An answer in which nothing at all moves is as weak as one in which
everything does.

> Budget doubles and you get a second engineer for six months. Which of the things you just declined becomes
> worth building, and what would have to be true before you started it?

This exposes whether the declines were principled or merely resourced. They were not the same kind of refusal:
the portal campaign was declined because client behaviour is not something money moves, the report back end
because the number underneath it has never been diagnosed, and the statement of conformity because four named
people are permitted to make it — and that last one does not become available at any budget. An answer that
reaches for it first has misread why it was off the table. The honest place for new capacity is the
unglamorous half: the extraction accuracy nobody measured, and the validation and change control the solver
now needs as the replacement for a controlled work instruction.

> The assessor picks a report where a result was reported with a note, and asks how that was decided. Walk me
> through what you put in front of them.

This exposes whether the audit record was designed or described. The answer has to name a row and its fields:
what the model was shown, what it proposed, which prompt and model version produced it, who accepted or
changed it, and when — with the decision itself attributable to the analyst whose name is against it. Offering
logs plus a recollection is exactly the position the four-month investigation put people in. It should also
handle the harder half of the question: where a model assembled the evidence, the assessor is entitled to ask
whether the analyst saw everything relevant, which is a question about what was retrieved and not about the
verdict that followed.
