---
id: observing-a-non-deterministic-system
title: What the dashboard cannot see
sidebar_position: 7
description: A pipeline publishes eight thousand catalogue entries a day into a public record, three cataloguers verify half a percent of them, and the last fault ran five months before an outsider mentioned it on a mailing list. Three attempts at designing a signal where there is no label, no error and no timely feedback.
# The reveal is the method. A page TOC lists every heading inside the collapsed reveal —
# naming all three attempts and the principle before the reader has committed to an answer.
hide_table_of_contents: true
---

# What the dashboard cannot see

Every instrument in this archive's cataloguing pipeline answers a question about the process rather than about
the product. The error rate counts the records that crashed. The latency chart counts seconds. The billing
export counts tokens. All three were healthy through a fault that ran five months and touched a sixth of
everything the pipeline produced in that window.

What makes the archive hard is that the world does not correct it on any useful horizon. Twenty-five reports in
fourteen months, at a median age of eleven months, is feedback but not a signal. Three cataloguers see half a
percent of the work, and the rest is published, searched and cited unread — by researchers who treat it as the
register of fact.

So the question is not which monitor to add. It is what a step has to write down about its own decision while
it still remembers it, what can be checked when nobody knows the right answer, and where a very small supply of
human attention goes.

> A national archive is nine years into digitising its holdings. About forty million pages are still in the backlog. Fourteen months ago the archive replaced manual cataloguing with an agent pipeline, and it has published about 3.4 million catalogue entries since.
>
> The pipeline runs five steps per record. It reads the scanned images, extracts the metadata fields, normalises them — dates, place names, name forms — links every person, place and organisation it finds to the archive's authority file, and writes a catalogue entry into the public catalogue, where researchers search it.
>
> **Volume.** Eight thousand records a day, every day. A record averages six pages, so roughly forty-eight thousand pages a day, forty thousand step executions, and — at about three entity mentions per record — twenty-four thousand authority-link decisions a day.
>
> **What it costs to run.** Model spend is about four cents a record. At 240,000 records a month that is roughly €9,600, and it is a visible line on a public budget. Separately, the directorate has approved €2,500 a month for infrastructure — everything that is *not* the pipeline itself, including anything you build. Nothing here is latency-sensitive; a record may take an hour and nobody notices.
>
> **What is instrumented today.** Every step writes one structured log line: timestamp, step name, record id, duration, status. Logs roll off after thirty days, which was the default and nobody changed it. There is a dashboard: throughput, p95 latency, error rate. The error rate has been 0.3% for eight months — about twenty-four records a day that genuinely crash on corrupt scans and timeouts — and it is the only number anyone looks at. Model calls are not recorded individually; the only record of them is the provider's daily token total on the billing export. No prompt, no response and no tool argument is persisted anywhere. The linker writes one authority ID into the entry and nothing else.
>
> **Systems in the building.** Each scan batch arrives from the scanning operation with a manifest listing every image file. The cataloguing system keeps every revision of every entry, with author and timestamp, forever. The reading room fulfils about 120 orders a week for physical originals, and the retrieval slips are logged in the reading-room system, which is not connected to the pipeline. The public catalogue takes about three thousand searches a day — searches, not records; most of them land on entries catalogued by hand decades ago — and the front end logs every search and what was clicked, kept thirty days.
>
> **Who checks the work.** Three cataloguers, five days a week, twenty records each a day. That is a full verification: reading the scan against the entry, line by line. Three hundred records verified a week, against roughly fifty-six thousand the pipeline produced that week — about half a percent.
>
> **What ground truth costs and when it arrives.** In fourteen months, researchers have written in about twenty-five times to report an error in an entry the pipeline produced — twenty-five, against 3.4 million entries. The median age of the entry when it was reported was eleven months. The archive still receives corrections to catalogue cards typed in the 1970s.
>
> **Two things that happened.** Eleven weeks ago an outside volunteer transcription group mentioned on a mailing list that a run of one region's civil registers had been catalogued with the wrong dates. It had been running for five months. About 190,000 entries were affected — roughly a sixth of everything the pipeline produced in that window, because provenance streams are worked through in order and that region's registers were what it was on. Nothing in the pipeline had flagged anything. The cleanup took the three cataloguers six weeks — not re-reading 190,000 entries, but establishing which batches were affected, re-running them and checking the result — and during those six weeks no new records were verified at all. Separately, a one-off audit six months ago found that in about one in four hundred multi-page records, one page had never reached the extraction step. About seventy percent of records are multi-page, so if the rate still holds that is roughly fourteen records a day. The entries read as complete.
>
> **What a mistake costs.** An entry that is wrong is searched, found and cited, and the citation outlives the correction. A wrong entity link merges two people, or splits one, in the record that researchers treat as the register of fact.
>
> **You.** You and two engineers. Six weeks ago the provider deprecated the model the pipeline started on and you moved to its successor; nobody could say afterwards whether anything changed. The next funding tranche is decided in four months, and the directorate has said it will not fund more autonomy in this pipeline until somebody can tell them what it is actually doing.
>
> **The question.** What do you record while this runs, what do you look at, and how does anyone here find out something is wrong before an outsider tells them?

:::note[Why this question]

One distinction is worth having straight before you start. A *liveness signal* reports that a process ran: it
started, it finished, it took this long, it did or did not throw. A *correctness signal* reports something
about the content of what the process produced — whether a value is right, whether a record is complete,
whether it agrees with something else that is known. Nearly every instrument that arrives by default is the
first kind, and only the second can move when the output is well-formed and wrong.

That is the property under test here. An agentic pipeline's failure surface is invisible to every mechanism an
ops team already owns: nothing throws, latency is normal, spend is flat, and what comes out is well-formed. So
the question asks whether an engineer can design a signal where the world supplies no label, no error and no
timely feedback — and whether the small supply of human attention already being spent can be made to *measure*
the population it is drawn from rather than merely *inspect* the records it happens to land on.

:::

**Answer it before you read on.** Out loud or on paper, whichever you'd do at a whiteboard.

Three model-written attempts follow. Each comes from a separate agent given one engineer's habits and the
prompt above. No agent saw the other two, and none saw the scoring standard the verdicts are written against —
that was fixed before any attempt existed, and a separate assessor applies it. The attempts introduce figures
of their own; where one of those is load-bearing and unchecked, the verdict under that attempt says so. That
arrangement is described in [how these are made](/design-scenarios/how-these-are-made).

<Reveal>

## Attempt A — the purchased-instrument answer

*Persona given to the agent: Two years of building evaluation harnesses, and reaches for a judge because it is the thing that produces a chart. Thinks in metrics and dashboards — a system is understood when a number describes it. Under one pressure: in four months, stand in front of the people holding the money and show a number that moved. Cost has rarely been the binding constraint before.*

**Start with the check that needs no model.** Every scan batch arrives with a manifest listing every image. Nothing ever compares that list to what the extraction step consumed, which is why one page in four hundred multi-page records vanishes and the entry still reads as complete — 8,000 × 0.7 ÷ 400 ≈ 14 records a day, silently short. This is a conservation check: pages in manifest = pages extracted = pages represented in the entry. It is a join, it costs nothing per record, and it catches all fourteen the same day. I would ship it in week one before I write a single evaluation prompt.

**What €2,500 actually buys, because it changes the design.** €2,500 over 240,000 records is about one cent a record for everything I build, against four cents for the pipeline itself. A judge that reads six scanned pages and compares them to the entry is a vision call — it costs *more* than the record cost to produce. Judging everything is therefore not "cheap, run it and see"; it is 100% of my budget spent to produce a monthly mean. I'd normally reach for exactly that. Here the arithmetic refuses it, and the refusal is a gift: full coverage buys an average, sampling buys detection. Five percent is 400 records a day, roughly €120 a month, and against a defect touching a sixth of production that's ~60 hits a day — visible inside forty-eight hours, not five months.

**So the money goes into storage, and storage is the actual fix.** A structured decision record of ~8 KB per record is ~2 GB a month, 25 GB a year. Full prompt and response text on the sampled slice plus 100% of anything flagged is maybe 15 GB a month. That is tens of euros of object storage. I keep decision records **forever**, keyed to the entry revision the cataloguing system already versions. Thirty-day retention is indefensible in a place where the median error report arrives eleven months after the entry and cards typed in the 1970s are still being corrected: the evidence expires ten months before the ground truth arrives.

**What goes in the record.** Per call: model id and version, prompt hash, tool arguments, tokens, cost. Per record: the page conservation counts, per-field extracted value plus the raw span it came from. Per authority link: the candidate set, the top score, **the margin to the runner-up**, and whether it minted a new authority record instead of matching. That margin is computed today and thrown away — the linker writes one ID. Merging two people or splitting one is precisely a low-margin decision, so the system is discarding the one number that identifies its most expensive failure, 24,000 times a day.

**What I look at.** Not the aggregate error rate — 0.3% has been flat for eight months because it measures liveness, not correctness. I want distributions cut by provenance stream, batch, and model version: date-century histogram, place-name normalisation novelty rate, link-margin distribution, new-authority-record creation rate, per-field null rate. The civil-register run shifted an entire stream's dates. Against that stream's own history, and against the hand-catalogued legacy entries for the same region and period, that is a distribution break inside a day. Alarms fire per batch, because defects here arrive in runs, not as noise.

**The arithmetic that changes what the cataloguers do.** Over those five months the pipeline made ~1.23M entries, ~15% of them defective. The cataloguers verified ~6,600 in that window, so roughly a thousand bad entries passed under human eyes and no signal escaped. The capacity existed; the routing and the aggregation didn't. So: same three people, same sixty records a day, but sampling is stratified so every provenance stream is covered, and every verification is written down as structured per-field outcomes — a measurement series, not sixty corrected entries. Then a thousand hits becomes a stream-level alarm, not a thousand private shrugs.

**Labels are already in the building, free.** The cataloguing system keeps every revision with author and timestamp, forever — every cataloguer correction of a pipeline entry is a labelled pair, fourteen months' worth. From those plus the twenty-five researcher reports I freeze a regression set of a few hundred records: scan, verified entry, expected fields, expected links. That set runs on every model change. Six weeks ago you swapped models and nobody could say what moved; next time, that's a table.

**The number in four months.** Not throughput. A measured field-level error rate per stream with a confidence interval from the sampled judge — the first honest correctness number the archive has ever had — and beside it time-to-detection: five months for the register run, days now, with the seeded-defect test that demonstrates it. That is what "tell us what it is doing" means, and it's the only basis on which more autonomy should be funded.

<Verdict>

A is the only answer that treats the €2,500 line as a design constraint rather than a footnote, and its
reasoning is genuinely inverted by it: €2,500 over 240,000 records is a cent a record, a vision judge that
re-reads six scans costs more than that, so full coverage is unaffordable and the money buys detection instead
of an average — "full coverage buys an average, sampling buys detection". It opens on the manifest join — "It
is a join, it costs nothing per record, and it catches all fourteen the same day" — specifies what goes into
the record, down to the discarded link margin, and then works the arithmetic through to the cataloguers: over
the five months, roughly a thousand defective records passed under human eyes. "The capacity existed; the
routing and the aggregation didn't." It buys a standing correctness instrument with money, so the population
rate stops depending on human throughput at all; no other attempt purchases an ongoing estimator.

That instrument is mispriced by A's own prose. A says the judge "costs *more* than the record cost to produce"
— more than €0.04 — then prices 400 records a day (twelve thousand a month) at "roughly €120 a month", which
is a cent each. One of the two is wrong by 4×, and A's headline four-month deliverable hangs off the cheaper
one. A also never mentions the reading-room or search signals, not even to decline them, and says nothing
about what happens once an alarm fires. Nor does it state the selection bias of the revision-history labels it
calls "Labels are already in the building, free."

</Verdict>

## Attempt B — the borrowed-label answer

*Persona given to the agent: Counts people and hours before anything else. The scarce thing has always been a small number of humans whose attention everything depended on, so their week is a measurement budget to be justified line by line. Does power arithmetic out loud. "More reviewers" has never been available and stopped being proposed years ago.*

**Start with the dashboard question.** If this pipeline were badly broken, that dashboard would look exactly as it looks now. 0.3% is a liveness number — it counts records that crashed. Both real failures produced well-formed, confident, complete-looking entries: 190,000 wrong dates and roughly fourteen silently truncated records a day never touch it. So I'm not tuning that number, I'm replacing what gets measured.

**The labels already exist and nobody has read them.** The cataloguing system keeps every revision with author and timestamp, forever. That means every correction three cataloguers made in fourteen months is a labelled diff against pipeline output — about 16,000 fully verified records (300 a week, minus the six cleanup weeks). Week one, my first engineer diffs pipeline revision against the next human revision, field by field, and back-computes a per-field defect rate by month, by provenance stream, by model version. That retroactively answers the deprecation question, and it puts a real number in front of the directorate in week two instead of month six. It costs nothing; the data is sitting there.

**Power arithmetic on the humans.** 0.5% sounds too small, and it wasn't. The bad stratum was about 17% of output for five months — a uniform 300-a-week draw hits roughly fifty affected records in the *first* week. It was missed because verification produces corrections, not data: nobody aggregated, and I doubt the draw was random. So I don't ask for more cataloguers. I keep twenty a day each, change which twenty, and require the outcome as structured fields — which fields were wrong, how badly — instead of a silent edit.

Split of the 300: **150 uniform random**, which is the only defensible rate estimate; **100 as a mandatory first block every time the pipeline moves onto a new provenance stream or register series**, because that seam is exactly where the 190,000 entered; **50 targeted** at the lowest-margin authority-link decisions.

What that buys: against ~1,800 records after a change, a field with a 3% baseline has a standard error near 0.4 points, so I can see 3%→4.5% inside a month and a doubling in a week. What it cannot buy: anything at one-in-four-hundred. The dropped page would never separate from noise here, ever.

**So the rare mechanical failures get invariants, not sampling.** Each batch arrives with a manifest listing every image. The pipeline should account for every one of them, per record, and refuse to write an entry that doesn't reconcile. That is the entire fix for fourteen records a day — no model calls, no cataloguer attention, permanent. Alongside it: dates inside the register series' known range, empty/default-value rate, entry length, and authority-ID churn (a person suddenly acquiring four hundred records is a merge in progress).

**Daily per-stream distribution monitors.** For each provenance stream, compare today's date histogram, place-name novelty rate and name-form patterns against that stream's own first weeks and against the hand-catalogued neighbours. A whole register run catalogued with wrong dates is a distribution shift of absurd size. This is the layer with the shortest latency to that incident — days, not five months.

**What I record.** Forty thousand step executions a day: persist prompt, response, tool arguments, model and prompt version; from the linker, the candidate set with scores and the top-1/top-2 margin, since merge/split errors concentrate in thin margins and previously unseen name strings. At ~10KB a step that's 400MB/day, ~12GB/month raw, single-digit euros a month on object storage against a €2,500 budget. Nothing was recorded because nobody decided to, not because it was expensive. Retention is set by when ground truth arrives — median eleven months — so thirty days is a category error: ninety days hot, then cold for the life of the entry; the derived per-record row (values, confidences, margins, model id) is ~2KB, about 6GB a year, kept forever.

**A golden set.** 500 records verified once, about eight cataloguer-days spread over a month, then frozen. Re-run on every model or prompt change: €20 of model spend. "Nobody could say whether anything changed" stops being possible.

**What I look at weekly.** One page: per-field defect rate with an interval, split by stream and model version, plus the quarantine list from the daily monitors. Throughput and error rate move to a footnote.

**What I decline.** Reading-room slips and catalogue click logs. 120 orders a week, and the clicks mostly land on entries catalogued by hand in 1974. Too weak to spend three people on.

**In four months** the directorate gets a defect rate with a confidence interval, a before-and-after on the swap, and an explicit list of what we still cannot see. Autonomy gets funded against a detector, not a promise.

<Verdict>

B has the best first week of the three. It notices the revision table is a fourteen-month label archive —
"every correction three cataloguers made in fourteen months is a labelled diff against pipeline output" — and
spends week one back-computing per-field defect rates by month, stream and model version, which retroactively
settles the deprecation question and puts a real number in front of the directorate with nothing yet built.
Its standard-error arithmetic is the only correct one on the page (n≈1,800, p=3% → SE ≈0.4pp). It is the only
attempt to ring-fence an unbiased slice — "which is the only defensible rate estimate". It is the only one to
doubt the representativeness of the historical labels it is about to dig into ("and I doubt the draw was
random"). And it is the only one to state the hard limit plainly: "What it cannot buy: anything at
one-in-four-hundred." It names the cause underneath all of it too: "Nothing was recorded because nobody
decided to, not because it was expensive."

The golden set is where its own discipline breaks. "500 records verified once, about eight cataloguer-days
spread over a month, then frozen." — at twenty records per cataloguer-day that is twenty-five cataloguer-days,
not eight: roughly 1.7 weeks of the entire verification budget, and B never says what stops to pay for it. It
is also avoidable: it paid fresh human capacity for labels its own free source supplies, identified earlier in
the same answer. And its power claims quietly pool a sample its own design splits: the arithmetic is exact,
but 1,800 records is six weeks at 300 a week rather than the month claimed, and "a doubling in a week" needs
the full 300 — on the 150 that B calls the only defensible rate estimate, it is marginal, not a detection.

</Verdict>

## Attempt C — the outside-in answer

*Persona given to the agent: Looks at the organisation around a system before the system. The useful signal is almost always already being produced by somebody not thinking about you. Applies a standing constraint to their own proposals — whatever gets built must not require anybody in the building to do new work, because designs that depend on new human effort quietly stop being done by the third month.*

**The error rate is a liveness check, not a quality signal.** 0.3% is the rate at which the pipeline notices it has failed. Every failure that has actually cost this archive anything was a success by that measure: the dropped page produces an entry that reads as complete, and the 190,000 wrong dates produced 190,000 perfectly valid entries. Twenty-four crashes a day tells you the process is running. It has never told you anything else, and eight flat months should have been the tell.

**Record every call, and stop deleting at thirty days.** Thirty-day retention is why the cleanup cost six weeks. The date fault ran five months; by the time it surfaced, the evidence of where it started was gone, so three cataloguers spent six weeks reconstructing which batches were affected — and verified nothing while they did it. That is 1,800 records of verification capacity spent on forensics that a retained batch trail answers as a query.

Per step execution: model id, prompt version, the prompt, the response, tool arguments, token counts, and the batch and provenance stream the record came from. Forty thousand executions a day at roughly 8KB of text is 320MB raw, about 2GB a month compressed, 25GB in a year. Object storage for that is noise; a columnar index over 15M rows a year sits on one modest instance. Two to three hundred euros a month against the €2,500. Retention 24 months, because the median researcher report arrives at eleven.

From the linker specifically: the candidate set, the scores, the margin — not one ID. Twenty-four thousand decisions a day whose failure mode is merging two people, and right now there is no record anywhere of whether the decision was close.

**Three sources already exist in the building.**

The scan manifest lists every image in the batch. Extraction knows how many pages it read. Comparing two integers catches the dropped-page fault — all fourteen a day, deterministically, no model call, no sampling. That is a week of work and it should have existed on day one.

The cataloguing system keeps every revision with author and timestamp, forever. When a cataloguer corrects a field, that correction is already a labelled diff sitting in a table, currently discarded as workflow. Diffing pipeline-authored revisions against human-authored ones yields a per-field error rate, per stream, weekly, from work that already happens — 300 a week, 15,000 a year, and nobody does anything new.

Reading-room slips and search logs give the outside-in view. Orders per thousand entries, pipeline-catalogued versus hand-catalogued, joined on item ID. Click-through per stream across the 3,000 daily searches: registers with wrong dates become unfindable by date, which appears as a stream whose entries get returned and never clicked.

**The sample isn't too small — it's blind.** Three hundred against fifty-six thousand is half a percent and gets dismissed on that basis. But the wrong-date run was a sixth of that window's output. A sample stratified by provenance stream puts roughly 48 of those 300 weekly records inside the affected run, in week one, at a defect rate near 100%. It didn't fire because nobody knows what the 300 are a sample of, and because nobody writes down what the cataloguer found. I change which twenty records land on each desk. Not how many, not the reading, not the job.

Alongside it, per-stream distributions: date histograms, place-name vocabulary, rate of new authority records created, linker margin spread. None of this needs ground truth. A five-month drift in one region's dates is visible within days as a shifted histogram against that stream's own history.

**The model swap.** Freeze 2,000 cataloguer-verified records as a replay set and re-run them field-by-field on any model or prompt change. Two thousand records at four cents is €80. "Nobody could say whether anything changed" stops being a sentence anyone here can say, for eighty euros.

**Six weeks, and what's visible from outside.** Manifest reconciliation live by week two, catching fourteen records a day that currently ship broken. Retention extended and per-call capture running behind it. Stratified queue and label capture from revision history by week four. Per-stream drift monitors by week six.

What the directorate gets in four months is not a dashboard. It is a per-field accuracy figure per provenance stream, with an interval on it, refreshed weekly from work already being done — and a measured detection latency. The honest version of the ask they made is: how long between a fault starting and this building knowing. Today that answer is five months and the source was a mailing list. I want it under a week, and I want it demonstrated on a real fault, not asserted.

<Verdict>

C is the most operationally complete: a dated six-week sequence, three named existing sources, and the only
attempt to price the read side of observability rather than only the bytes. Its opening reframe does the whole
job in one line — "0.3% is the rate at which the pipeline notices it has failed". It is also the only one to
cost the last incident in the currency that actually ran out: "That is 1,800 records of verification capacity
spent on forensics that a retained batch trail answers as a query." Then it builds the outside-in detector,
using search logs not as ground truth but as a label-free distribution monitor — "registers with wrong dates
become unfindable by date, which appears as a stream whose entries get returned and never clicked". That is a
real signal from a source the other two either declined or never noticed, at no human cost. And it closes by
recasting the directorate's demand as "how long between a fault starting and this building knowing" —
something to be demonstrated on a real fault rather than asserted.

"Two to three hundred euros a month against the €2,500." is the one figure C does not derive, in an answer
that derives everything else, and it commits up to an eighth of the infrastructure budget on an unshown
number. C also credits stratification with a hit rate uniform sampling already delivers — a sixth of 300 is
fifty affected records in the weekly draw whether or not anyone stratifies — so the arithmetic is right and
the attribution is not. Its 24-month retention is the weakest of the three answers in an archive still
receiving corrections to cards typed in the 1970s.

</Verdict>

## Where they actually disagree

Each disagreement below is a decision you will have to make yourself. The last entry is the exception: not a
disagreement but the place all three arrived together, and what went unexamined once they had.

### Labels for the defect rate: bought from a judge, or borrowed from cataloguer corrections

A spends model budget on a standing sampled judge — 400 records a day across all streams, independent of human
throughput — and treats the cataloguers as pure stratified detectors. B and C spend nothing on judging and
take every label from cataloguer revisions, accepting 300 a week concentrated wherever the queue points.
Twelve thousand machine-judged records a month with unknown judge error, against three hundred human-verified
records a week with none.

### Outside-in usage signals: wire them or decline them

C joins reading-room retrievals and per-stream click-through and gets a free detector out of them. B declines
both explicitly — "Too weak to spend three people on." — because the traffic is thin and skews to entries
catalogued by hand in 1974. A never raises them. Worth noting that B's stated reason argues against *staffing*
those signals rather than against joining a log that already exists. The reader has to decide whether a biased
signal that costs nothing to join is worth having.

### How long the recorded decisions live: forever, tiered, or twenty-four months

What is being kept is the per-call and per-record trail all three would write where nothing is written today —
model and prompt version, tool arguments, the extracted values, the link margins — instead of a single log
line that rolls off after thirty days. A keeps it forever, keyed to the entry revision. B splits it — "ninety
days hot, then cold for the life of the entry", with a small derived row kept forever. C sets a flat 24
months, "because the median researcher report arrives at eleven". C's is the position that has to be defended:
the same prompt says cards typed in the 1970s are still being corrected, so a median is the wrong statistic
for choosing a horizon.

### Whether any of the sample stays uniform: a ring-fenced random slice, or every record allocated

B ring-fences 150 a week as random and calls it "the only defensible rate estimate", spending the rest on
thin-margin links and on what it calls the seam — the point where the pipeline moves onto a new provenance
stream, which is where the 190,000 wrong dates entered. A and C allocate by stratum — A backfilling the
population rate from its paid judge, C reporting per-stream rates and no pooled figure. Underneath: does a
monitoring programme need an unbiased population number at all, or only per-stratum movement?

### What all three agreed on, and none of them tested

All three rejected the framing that 300 a week is too small — B and C prospectively, A after the fact. Two of
them derive it the same prospective way — the bad stratum was a sixth of that window's output, so a weekly
draw of 300 lands roughly fifty affected records inside it in week one — and the third derives it
retrospectively, computing that about a thousand defective entries had already passed under human eyes during
the incident and left no trace. Two routes, not three: but one is forward-looking and one is a post-mortem,
and a prospective power calculation and a retrospective one meeting at the same verdict is a stronger
convergence than three variants of a single derivation would have been. The conclusion is also unusually
actionable: it converts a resourcing argument into a routing argument, so it ships in week one with no budget
ask.

All three also found the same buried signal — the linker computes a margin and writes only the ID. All three
demoted the error rate to liveness without being told to, and the two that mention throughput demote it in the
same breath. Latency is a non-event: no attempt treats p95 as a quality signal, and the only two uses of the
word in the whole set mean *detection* latency — the time from a fault starting to anyone knowing — which is
the opposite quantity and the right one.

Two things went unexamined inside that agreement.

**Nobody tested which branch they were in.** If the cataloguers did correct affected records — which A's own
arithmetic implies for about a thousand of them — then the revision table already contains the wrong-date
fault, and the failure was not missing aggregation but a populated table nobody read. If the draw never
touched that stream — which B suspects out loud — then the historical label mine that two of the three designs
stake their first number on is far thinner than sixteen thousand usable labels. One attempt runs the query
that would settle it — "my first engineer diffs pipeline revision against the next human revision, field by
field" — and a second proposes a weaker version of the same diff. But both treat the output as a baseline to
report, not as a fork in the plan: no attempt says what it would do differently depending on which branch the
answer puts it in, and the two branches imply different first weeks.

**The re-aimed 300 is double- and triple-booked.** In two of the three designs the same 300 records a week are
simultaneously the detector, the label source feeding the defect rate, and the only crew available to triage
an alarm. The third decouples the middle leg — its rate comes from the purchased judge, so the humans carry
two jobs rather than three — which makes it the only design where triage does not directly erode the number
being reported. None of the three says which use yields when an alarm fires, and one of them itself computes
that a single incident consumed 1,800 of those records on forensics. Nor does anyone mention that the entries
are already public, that a confirmed fault means correcting published records, or who would do that.

## The principle

> Before asking for a bigger sample, check whether the sample you already take is being written down —
> capacity that produces fixes instead of records detects nothing, however large it is.

</Reveal>

:::tip[Read next]

- [Why AI systems fail in production](/rag-agents/part-3-production/production-failures) — §4 states this
  page's premise as a principle: uptime is a property of the service, correctness a property of the answer,
  and no ordinary monitor has an opinion about the content of a 200. It also draws the retention distinction,
  that logging sized for debugging is not logging sized for proof.
- [Observability — deep dive](/rag-agents/part-1-rag/cross-cutting/observability/deep-dive) — why
  "interesting" for an LLM system cannot be defined by error and latency, and the rule that at least one SLI
  must be a quality SLI computed by online eval. Its sampling is trace retention — which traces you store —
  and not an allocation of human review.
- [Mutation testing and the order of the chain](/ai-sdlc/part-3-verification/layered-gates/deep-dive) — the
  method behind proving a detector instead of trusting a green board: plant a defect, and a surviving mutant
  is a demonstrated blind spot rather than a suspected one. Includes the limit — a seeded fault only certifies
  the fault class you thought to seed.
- [Drift control and rule rot](/ai-sdlc/part-5-scale-governance/drift-and-rot) — the one-line version for a
  live check: a rule that has never fired is an unverified rule, not evidence of health.
- [Observability, rollout, and the kill switch](/ai-sdlc/part-4-platform/observability-rollout) — the minimum
  sensor set, including the one business signal that moves when a change is technically healthy and
  functionally useless.

:::

## If they push

These are the three follow-ups an interviewer reaches for next, and what each one exposes.

> Your monitoring has been live a month. Every signal you built is flat and green. What is the first thing you
> check, and what would convince you the system is healthy rather than that your instrumentation is blind?

Nothing in a flat month distinguishes a clean pipeline from a detector wired to the wrong column, and the
honest answer has to be a positive test rather than a reassurance: plant a defect of a class you claim to
catch and confirm it appears, then look at when each check last fired on something real. A monitor with no
firing history is untested code sitting in front of the only decision it exists to inform.

> One of your checks now fires on about forty records a day. The cataloguers can do sixty a day, total. What do
> you do on day two?

This is the triple-booking made concrete, and it defeats any answer that treated detection and response as
separate budgets. Forty alarms against sixty verifications consumes the measurement to service the alert, so
the design has to say what yields — routine sampling, most likely — and how the alarm is handled without
record-by-record triage: quarantine before adjudication, a decision taken at batch or stream level, a
threshold that fires on a run rather than on a record.

> The provider deprecates your model again next month. What exactly do you compare, on what set, to say whether
> the swap made anything worse — and what does that comparison cost?

A comparison is only available if the set was frozen before the change, so this asks whether the regression
set is an artefact or an intention. The answer has to name where its labels came from, what selection bias
they carry, which fields it compares one by one rather than in aggregate, and the token cost of a re-run. It
should also note that a set drawn only from records humans already corrected is biased toward the failures
somebody had already caught.
