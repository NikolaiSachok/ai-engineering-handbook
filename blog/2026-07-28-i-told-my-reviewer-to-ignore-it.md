---
slug: i-told-my-reviewer-to-ignore-it
title: "I told my reviewer to ignore it, and it would have missed it anyway"
authors: [nikolai]
tags: [making-of, ai-sdlc, verification, translation]
date: 2026-07-28
---

A lesson about defects that slip past every check shipped in Russian using a word the pipeline had coined for
itself. The established word was already in that file, on the line the pipeline overwrote.

{/* truncate */}

The lesson is [the escape ledger](/ai-sdlc/part-3-verification/escape-ledger). In QA an *escape* is a defect
that got past every gate and reached production, and the lesson argues that each one is evidence about which
gate is blind. The Russian page shipped with «прорыв» as the term and «Журнал прорывов» as its title. I found it
by reading the published page. Nothing in the automated chain had flagged anything.

## What I got wrong about the word

The first version of this post told you «прорыв» means *breakthrough* in the achievement sense, that the title
read as a ledger of triumphs, and that the translation had therefore flipped the lesson's meaning. That came out
of the writeup of the original fix, and I carried it into the draft without re-testing it. It does not hold. What
a Russian reader actually gets is the breach image, something broke through the way water breaks through a dam,
and we wrote it down. The failure is not in the sense but in the naming: this is not how Russian names defects
that got past testing. «Список упущенных дефектов», «журнал пропущенных дефектов» and «лог ошибок» are what
Russian actually uses.

I am putting the correction in the post rather than folding it quietly into a redraft. The claim I had to
retract was the central factual claim of a piece about verification, and it got through a full editorial pass, a
leak pass and my own read before a native reader stopped it at the last gate.

## The right term was already in the file

Before the lesson existed, the Russian page sat in the repo as a placeholder: a title, a heading, two sentences
of "here's what this will cover." The placeholder said «Журнал пропущенных дефектов», the ledger of defects that
were let through. The commit that replaced it shows the whole thing as one paired edit, `-# Журнал пропущенных
дефектов` against `+# Журнал прорывов`.

That is the part that reframed this for me. A pipeline staring at an empty vocabulary and guessing badly is a
problem I know how to fix, and it is at least doing work. This pipeline did not have an empty vocabulary. It had
the answer open in front of it and wrote over it with a coinage of its own. No one compared the two
words, because nothing in the pass surfaced that a second candidate existed at all, which is a duller failure
than bad judgment and a harder one to notice. The Slovak translation of the same page used «únik», a leak, which
is idiomatic and correct, and no pass touched it.

The correction went in as [PR #232](https://github.com/NikolaiSachok/ai-engineering-handbook/pull/232), commit
`b2b698b`. It was deliberately dull: the title, the H1, every place the term appeared in the body, the glossary
section and its headwords, the new-terms line. Twenty-four lines out, twenty-four lines in. Links, numbers, the
embedded video and the page anchor came out byte-identical, so the review could be about one term and nothing
else.

## The check was told not to look

The translation pipeline has an independent check in it, run on a different model. That check's entire job is
to read the finished translation and report anything that does not read like native writing. It read this page
and reported nothing.

It reported nothing because the pass that coined «прорыв» had written the word into its own instructions as
settled house vocabulary, then handed it to the check under "do not flag, this is deliberate canon."

The handbook has a lesson arguing that [the actor making a change must not be the actor certifying
it](/ai-sdlc/part-3-verification/detection-vs-mutation). So the pipeline built to teach that rule broke it.

The shape travels. Any suppression list can take it: a `# noqa`, or an eval config maintained by the team the
eval is grading. The newest entry on such a list is the one nobody outside the pipeline has looked at yet, and
it still reads as settled, because someone had to make a call in order to add the line, and that call is exactly
the one that has had no scrutiny. If you keep an exemption list, the cheap defense is an entry format: who added
it, what it silences, when its continued need gets rechecked, and whether the actor who added the entry is the
actor whose output it covers.

## The check could not have seen it anyway

Everything above about «прорыв» is about what Russian QA calls this thing. None of it is about whether the
Russian reads well, because the Russian reads well. A native speaker parses the sentences instantly and the word
agrees with everything around it. A reviewer briefed to answer "does this read native" would have answered yes,
unless it happened to work in QA.

Which forces an admission. Once the objection turned out to be naming rather than meaning, I stopped being able
to show that the exemption is why the miss happened. A word that means the wrong thing leaves a trace on the
fluency axis: something jars, a sentence reads oddly, a careful naturalness reader might stumble into it. A word
that parses cleanly and fails only on what a field calls things leaves no trace there, unless the reader works
in that field. Even with no do-not-flag list, the check would have had to be a Russian QA engineer, not a
Russian speaker, to object.

So there are three failures stacked here and they are not the same size. The overwrite made the bad page. The
absence of any pass that could ask whether a term was the right term is why the bad page stayed. Writing your
own exemption into your own reviewer's instructions is a genuine defect in the process and it stays a defect,
but on this occasion I cannot show it is what caused the miss. That is worth separating out, because the
tempting move after an
incident is to fix the defect you can see and call the incident closed. The exemption is the visible one. The
invisible one is that nobody owned the question of whether the term was right, and fixing only the exemption
would have left that exactly as it was.

Fluency and domain correctness are separate axes, and the gap between them turned out to be wider than I thought
when I believed the word meant the wrong thing. The question the second pass has to answer is a different kind of
question, "is this the word the field uses", and it gets settled against external sources instead of a model's
ear.

The fix came with four rules I now hold the pipeline to. Nothing gets coined until someone has gone looking for
a term that already exists, in a placeholder, a sibling page or the glossary, and a word already in the corpus
outranks a fresh one. Overwriting a placeholder is a defect. No coinage reaches the independent check as
settled; new terms go in on probation, unprotected, so the check can argue with them. And the term axis gets
checked against a domain-tagged dictionary or a usage corpus, with the source recorded, so someone who was not
there can audit the answer later.

The first two rules need an exit or they will fire on the wrong cases. When the search comes back empty, coining
is the correct move, and a placeholder can itself be wrong, in which case overwriting it is the right editorial
call. What changes is that both now have to survive the independent check unprotected, which is what the
probation rule is there for.

The conclusion I want to avoid is "review everything more carefully." It would have changed nothing here,
because the reviewer was already reviewing carefully along the axis it had. The useful question when a check
misses something is whether the miss was visible at all on the axis the check was looking at. Here it was not,
so a stricter naturalness prompt would have returned the same clean report on the same page.

The rules are in place now. Neither of the two things this post is about was caught by a check: I found the term
by reading the published page, and a native reader found the wrong explanation of it in this draft. I do not yet
know what the new checks do against the next fluent, domain-wrong word, because that word has not shown up yet.
