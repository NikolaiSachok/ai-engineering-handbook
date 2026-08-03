# Design Scenarios — term ledger (English-only course)

The term ledger for the **Design Scenarios** course. It lives in `canon/ru/` because the router's
pointer table pairs **RU + EN** on one `_language.md`, and this course's prose is **English**.

**Load with `_language.md`.** The shared RU/EN language rules apply to this course's English prose:
British spelling, the bold budget (~0.36 spans per prose line), the metaphor/figure budget,
figure-probation. The **bridge rule does not apply** — in English the terms are already native.

**No SK or DE ledger exists for this course, deliberately.** The course declares `locales: ['en']`
in `docusaurus.config.ts`, so there is no Slovak or German prose to govern. The one non-English
surface is the landing card, whose three strings are recorded in a single scoped section below
rather than in three near-empty ledgers.

**Peek-don't-load across siblings.** For a term that overlaps `rag.md` or `ai-sdlc.md`, do a
targeted read-only lookup: reuse a matching decision verbatim and cite it, or flag a genuine
sense-difference. `rag.md` is FROZEN — never edit it.

## Language policy

- The course is authored in English and is **not translated**. Reason of record — the unheaded closing passage of `intro.md`: interview-register prose — argument, hedging, engineers disagreeing — is the
  corpus's most idiom-dense text, and a translated scenario reads as translated.
- **The landing card IS localized**, so a reader in any locale learns what the course is before
  clicking. The card copy **describes the course and never comments on its language** — the card
  renders `course.languages` as its own UI element (`src/pages/index.tsx`), and neither sibling
  blurb carries a language phrase.

## Book units

The corpus's shared units are lesson · layer · part · cross-cutting aspects. This course uses
neither "lesson" nor "part"; it adds two:

| unit | meaning |
|---|---|
| **scenario** | one page: one production design question, three attempts, a verdict on each, one transferable sentence. The unit "lesson" names elsewhere. |
| **track** | scenarios grouped by the role archetype that asks them. Lowercase in prose ("the agentic workflows track"), sentence case in sidebar labels. Bold only at first defining mention. |

## Recurring block strings (exact strings — carried by every scenario page unless noted)

All **ON PROBATION**: they were coined in the PR that introduced this ledger, and per the
no-self-issued-exemption rule the pass that proposed them may not mark them settled. A later cold
read or milestone pass confirms or strikes them.

| block | exact string |
|---|---|
| attempt 1 | `the common answer` — the popular answer; never a strawman |
| attempt 2 | `the strong answer` — constraints-first, operator's reasoning |
| attempt 3 | `the over-built answer` — the complete architecture, arrived at before the problem earned it |
| commit line | `Answer it before you read on.` — bold, full stop inside the bold, then the sourcing statement |
| reveal control | `Show the three attempts` — the `<summary>` text; the string the reader actually clicks |
| disagreement section | `Where they actually disagree` |
| transferable sentence | `The principle` — H2, one sentence in a blockquote (see below) |
| curriculum pointer | `Read next` — points OUT of the course, into RAG & Agents / AI SDLC lessons |
| follow-up probes | `If they push` — the questions that separate understanding from memory |
| verdict block | `<Verdict>` … `</Verdict>` — the component, one per attempt, blank line inside each tag. Its rendered label is `The assessor's verdict` (`src/components/Verdict/index.tsx`), inherited, never overridden on a page. **A bolded `**Verdict.**` lead-in is REJECTED**: the attempts are full of bolded spoken section labels, so it reads as one more of them; and it cannot be an admonition, because `:::` does not render inside `<Reveal>`. Corrected 2026-07-30 (Gate 5, scenario #2) — the earlier row mandated the rejected string and had 0 occurrences on either shipped page. |
| disagreement lead | `Each disagreement below is a decision you will have to make yourself.` — the section's first paragraph, before any item. Scenario #2 first shipped without it and a reader landed on a bare H3; the editorial gate added one, and the cold read cut its opening clause (`The gaps between the attempts are worth more than any of them alone` — unsupported puffery about the page's own value, and the second clause did all the work). **On probation** — coined in this batch, so the next scenario's Gate 5 confirms or strikes it. |
| follow-up lead | `These are the three follow-ups an interviewer reaches for next, and what each one exposes.` — one sentence, **indefinite article**. **Never state what the interviewer has seen:** the interviewer role never sees the answers (`how-these-are-made.md`), so "the interviewer has the attempts in front of them" is factually wrong as well as a register slip — the same role conflation #356 removed from the `<Verdict>` label. |
| frontmatter comment | `# The reveal is the method. A page TOC lists every heading inside the collapsed reveal —` / `# naming all three attempts and the principle before the reader has committed to an answer.` Two YAML comment lines above `hide_table_of_contents: true`. Scenario #1 said `the collapsed <details>`, stale since `<Reveal>` replaced the raw element; retro-fitted 2026-07-30. A YAML comment is silent, which is exactly why it drifts. |

**Probation cleared 2026-07-30 (Gate 5, scenario #3), by a pass that coined none of them.** #3 reproduced the
attempt headings and their tier labels, the commit line, the `<Reveal>` summary string, `Where they actually
disagree`, the **disagreement lead**, `The principle`, `Read next`, `If they push`, the **follow-up lead**
(indefinite article and the "three" intact) and the two frontmatter comment lines **byte-exactly**. Three
independent pages, no drift: **the recurring block strings are SETTLED.** The tier labels themselves stay
probationary as *labels* — that is a separate question about the words, recorded in the localized-card section.

**Scoped amendment to the provenance paragraph, 2026-07-30.** The recurring clause is "no agent saw the other
two, or the rubric, which was written first". #3's prompt is the first to use `rubric` in the *other* sense
("inputs, rubric version, model version"), four lines above, so on that page bare "the rubric" binds to the
submissions' grading rubric. #3 reads **"or the assessor's rubric"**, which also anchors to the `<Verdict>`
component's rendered label. **Rule: qualify it only where the prompt uses `rubric` in the grading sense** — the
ledger binds senses, not strings, so this is not a fork.

**`the reveal` is NOT a page string.** It is the corpus's *name* for the boundary (`intro.md`, "before
you open the reveal") and is registered in the terms table below. Scenario pages carry `Show the three
attempts`. Recorded 2026-07-29: the earlier block-string row claimed a string that appears on no
scenario page — it was written before any page existed to check it against.

**Label form.** Bold, capitalised at list-item or sentence start (`**The common answer** — …`),
lowercase in running prose ("you will agree with the strong answer"). The article stays outside the
bold when the label appears mid-sentence. **In an attempt heading the label is lowercase and
unbolded**, after the letter and an em dash: `## Attempt A — the common answer`. A heading is already
navigation, so bold inside it would breach `_language.md` §8. **CONFIRMED 2026-07-30** — scenario #2
reproduced all three headings byte-identically, in order, with the tier vocabulary `intro.md` defines;
Gate 5 and Gate 4 confirmed it independently, and neither pass was the one that coined it.

## The closing takeaway — structure SETTLED, placement OPEN

**Structure — settled, and not by accident.** A scenario does **not** carry the corpus's
`## What to take away` (59 uses across `docs/` + `docs-ai-sdlc/`). It carries `## The principle`: one
transferable sentence in a blockquote. The decision has warrant predating scenario #1 — `intro.md`
already promised "one sentence stating the principle that carries to other scenarios", and this
ledger's own `scenario` book-unit row already read "one transferable sentence". Scenario #1 and the
template implement that promise rather than improvising it. The template supplies the test: it must
survive the specific numbers being wrong.

**Placement — open, for the milestone pass to settle.** The earlier row did not ask this question.
`## The principle` sits **inside** the `<details>` reveal and is **not** the last section — the page
continues with `Read next` and closes on `If they push`. So it differs from the corpus's closing
takeaway on two axes, and only the first was decided. Two consequences to rule on: a reader who never
opens the reveal never sees the transferable sentence; and scenario pages become the only pages in the
corpus that do not close on a takeaway. Both may be intended — the sentence is a verdict on the
attempts, so hiding it with them is coherent. Do not let scenario #2 settle it by repetition.

**#3 makes it three, and gives the OPEN question its first hard evidence.** #3 also puts `The principle` inside
the reveal and not last. But on #3 the section that renders *outside* the reveal (`If they push`) turns on the
very distinction the principle states — so a reveal-skipper meets the payoff sentence's argument without ever
having met the sentence. The gate closed the gap by spelling the distinction out in `If they push` rather than by
moving the principle, because moving it is the author's call. **Three pages is de facto convention; rule on it
before #4.**

## Jurisdiction — the three attempt bodies are testimony

The attempts are quoted, written blind by three independent authors. **Terminology that diverges between
attempts is signal, not drift.** No canon rendering is applied inside an attempt, and no pass aligns them to
each other; a canon divergence found inside one is reported as an observation and left alone. Only outright
mechanical errors — a typo, a broken construct, an ungrammatical sentence — may be touched.

The **frame** takes the full pass: prompt, `Why this question`, the commit line, the provenance paragraph,
every `<Verdict>`, `Where they actually disagree`, `The principle`, `Read next`, `If they push`. The italic
`*Persona given to the agent: …*` line is fixed furniture — reproduce it, never reword it. **A verdict is frame even
though it quotes an attempt.** Scenario #1 shipped `top-k` in Verdict B, inherited from Attempt B's lever
list; the verdict instance is a defect and was corrected to `top-K`, the attempt's is not and was left.
A cold-read reviewer later proposed matching the verdict back to the attempt for local consistency — refused:
`_language.md` §3 fixes `top-K` (corpus 21×, 0× `top-k`), and canon binds the frame regardless of what it
quotes.

Observed and deliberately left standing in scenario #1: Attempt C's `an LLM-judge` and Attempt B's
`an LLM judge`, where `_language.md` §3 mandates `LLM-as-a-judge`. Both stand. **A future mechanical spelling
gate must exempt the attempt line-ranges or it will silently rewrite testimony.**

**An AI tell inside an attempt is a finding to report, never to fix** — it means the persona failed, and the
pipeline owner needs to know rather than have it smoothed away.

## Cross-course reference conventions

- **Cross-course links use absolute routes** — `/rag-agents/`, `/ai-sdlc/`. Relative `.md` links do
  **not** resolve across Docusaurus docs-plugin instances, and `onBrokenLinks: 'throw'` makes the
  wrong form a build failure. Precedent: the blog's `/ai-sdlc/part-3-verification/escape-ledger`.
- **A link label reproduces a name the target actually carries** — its `title` or its `sidebar_label` —
  verbatim, `&` and `+` intact. Do not expand them to "and": the reader must land on a page that calls
  itself what the link called it. Same rule that keeps **RAG & Agents** and **AI SDLC** ampersanded, one
  level down. Precedent for the failure: scenario #1 shipped `Metric internals and judge calibration`,
  `Sampling, SLOs and budgets` and `Serving — FastAPI and Docker` against targets named with `&` and `+`.
  Every link resolved; three of five lied about where they went, and no build check can see that.
- **Nothing outside the reveal may point into it by position.** `Read next` and `If they push` render for a
  reader who never opened `<details>`, so a bare attempt letter or "the disagreement above" dangles. Name
  the referent instead. Caught by the cold read on scenario #1.
- The siblings' proper names are **RAG & Agents** and **AI SDLC** (their `navbarLabel`s, reused by
  the navbar, landing cards and footer).

## Terms reused from sibling ledgers (peek-verified, senses match)

| term | source | sense |
|---|---|---|
| **latency budget** | `rag.md` — «бюджет латентности» | a budget allotted to latency |
| **rubric** | `rag.md` registry — «критерии оценки», never «рубрика» (false friend) | evaluation criteria, not a grid or template |
| **production** | `rag.md` — «прод»; `ai-sdlc.md` — "the loop closes on production" | the live environment |
| **super-step** | `docs/glossary.md` L628; `part-2-agents/orchestration-frameworks/deep-dive.md` L43 | the checkpointer's write unit. Corpus **2× `super-step`, 0× `superstep`** — hyphenated, in the frame, always |
| **checkpointer** | same glossary entry | the component that saves graph state at every super-step, keyed by a thread |
| **thread** / **thread_id** | `docs/glossary.md` L634 | the id isolating one run's checkpoint history. **Not a synonym for `case`** — a thread is the engine's handle, a case is the unit of work with a history. An attempt may map one onto the other; the frame must not merge them |
| **interrupt node** | `orchestration-frameworks/deep-dive.md` L53 | the durable human-in-the-loop pause. **`durable interrupt` is Attempt C's phrase** on #3 — quote or convert. #3's frame used the lesson's words: recorded as the positive precedent |
| **append-only** | `docs-ai-sdlc/glossary.md` L390; `part-4-platform/secrets.md` L22 | industry-standard, not a coinage; frame adoption is safe |
| **model snapshot id** | `docs/glossary.md` L1013 (**Model pinning**) | a pinned model version. See the `snapshot` sense card — the bare word must not travel |
| **oracle** (testing sense) | `docs-ai-sdlc/part-3-verification/detection-vs-mutation.md` L87, L119 | a trusted reference answer. Corpus vocabulary; needs no gloss |
| **primitives** | `orchestration-frameworks/index.md` L8, L124, L151 ("primitives first") | the mechanisms a framework packages. Scenario #3's title term is the target lesson's word |

### Sense card: `production` (reservation)

**Reserved sense:** the live environment, and by extension live operation — "an AI system in
production", "production work".

**Breach to watch for:** `production` as *the act of producing* (the recognition-vs-production
contrast from learning science). On a page that already uses the reserved sense, this reads as a
slip even when the sentence is correct. **Ask before writing the word: does this mean *where the
system runs*, or *the act of generating something*?** For the second, write it out — "producing
one". Caught and fixed in the intro's editorial pass.

## Terms new to this course — ON PROBATION

| term | working sense |
|---|---|
| **scenario**, **track** | book units, above |
| **attempt** | one of the three independently written answers. Distinct from `rag.md`'s `pass^k` "attempts" (trial runs) — do not cross-cite. |
| **verdict** | the judgement delivered on one attempt |
| **the reveal** | the boundary the reader crosses after answering for themselves |
| **role archetype** | the abstracted role a scenario is sampled from; the anonymisation device |
| **exception type** | the domain's class-of-problem axis a scenario segments by. House form is `exception type`; `exception class` / `exception taxonomy` are an attempt's words — convert in the frame, or quote them. |
| **replay environment** / **replay suite** | **two different objects, not synonyms.** An *environment* is the frozen-snapshot substrate with a determinism contract; a *suite* is a fixed set of cases run against it. `replay harness` is not a third house term. Disambiguate at first use if a page needs both. **Row extended 2026-07-30 (Gate 5, scenario #3) — the taxonomy had a hole, and the hole is why the barred term keeps arriving.** The row named no term for *the thing that runs a replay*, so #3's frame reached for `harness` four times for an artefact that is neither an environment nor a suite: a CI job that **samples** published cases, replays them and compares. Compliant moves, both used in #3's fixes: quote it as the attempt's word, or write the mechanism plainly (`the weekly CI run that replays sampled cases`, `the CI job that replays it`). **A prohibition with no replacement term gets overridden by the next author who needs the concept.** |
| **the record** | the artefact an auditor reads — **the house term** for the object `judgement row` (#3's B), `event log` / `judgement ledger` (#3's C) and `the record` all name. It is also the prompt's word, which is why it wins. |
| **execution engine** | the vendor-neutral noun for whatever runs the steps. Used once on #3, in `The principle`, where `framework` would date the sentence. **ON PROBATION.** |
| **pause-versus-reopen** | #3's compressed name for its own distinction. **ON PROBATION**, and the sharper lesson is the counter-example beside it: the compound was legal only where the box had stated both halves, and the same section's `the checkpoint` was not. When in doubt, spell the distinction out — #3 shipped "the difference between suspending an open run and reopening a closed one", which needs no anchor at all. |
| **a contested prompt term, quoted in a heading** | the device at `### Reproducible: replay it or retain it`, where the prompt's own word is under dispute and the frame quotes rather than adopts any attempt's definition of it. New on #3, **ON PROBATION**. |
| **golden set** | the curated human-labelled evaluation set. `anchor set` is **not** a synonym. |
| **trajectory eval** / **outcome eval** | peek-verified against `docs/part-2-agents/planning-loops/deep-dive.md` ("Trajectory eval requires a full trace of the run"; "outcome eval plus a step count can be plenty") — senses match, reuse verbatim. Keep the short `eval`; do not expand to "evaluation" in prose. The lesson also calls the axis **outcome versus process**, so a page that sends the reader there should bridge the two names once. |
| **reviewer-weeks** | a generic unit of account for review capacity, usable in `The principle`. **Not for arithmetic on this course's prompts**, where "two reviewers audit ~200 cases a week" makes the natural person-week reading wrong by 2× — write "N weeks of the pair's entire output" instead. |

### Sense card: `LLM judge` vs `LLM-as-a-judge` (peek-verified, sense split) — **SETTLED**

**`LLM-as-a-judge`** names the **method** ("the paper that established LLM-as-a-judge as a method").
**`an LLM judge`** names the **instrument instance** ("calibrate the LLM judge that scores it"). `docs/` carries
both, stably and deliberately. `LLM-as-judge` and `LLM-judge` are wrong in either sense (§3).

**Ask before writing it:** *am I naming the technique, or the thing doing the scoring on this page?*

**Correction to this ledger, 2026-07-30 (Gate 5, scenario #2).** The jurisdiction note above previously read
that "§3 mandates `LLM-as-a-judge`" and logged Attempt B's `an LLM judge` as a divergence left standing. That
over-read §3, which bars `LLM-as-judge`, not the instrument noun. Scenario #2's frame uses `an LLM judge`
twice and is **correct**; Attempt C's `an LLM-judge` remains the real (unfixed, reported) divergence.
**A ledger row asserting a prohibition must cite the corpus count that supports it** — this one did not, and
would have driven a later reviewer to "fix" compliant prose. **CONTESTED for the author**, since it reverses
a call scenario #1's Gate 5 recorded.

### Sense card: `replay` / `resume` / `re-run` / `re-score` / `reopen` / `pause` — **ON PROBATION**

Scenario #3 exists because two of these are confusable, so six words carry six meanings and the frame may not
blur them:

| word | meaning | owner |
|---|---|---|
| **pause** / **suspend** | an open run held; something is waiting | frame + prompt |
| **reopen** | a closed, published case re-entered; nothing is waiting | prompt |
| **resume** | picking up a *suspended* run — **never a published one** | frame, from the target lesson |
| **re-run** | idempotent recovery of the same decision | prompt |
| **re-score** | a **new** decision, permanently distinguishable from the original | prompt |
| **replay** | re-executing from a checkpoint. **Not a record read** — see the framework-semantics row below | frame |

**The page's whole argument is that `resume` and `reopen` are different operations**, so a frame sentence that
resumes a published case denies the page's own principle. `If they push` shipped exactly that; see the rejected
rows.

### Sense card: `record` (three senses on one page) — **ON PROBATION**

**Reserved sense:** the artefact an auditor reads — the object with a retention duty. Also live: the plain verb
*to record*, and the prompt's plural `records`. The senses separate by article and form, and #3 does not slip.
**Ask before writing it:** *is this the thing an auditor reads, or the act of writing something down?*

### Sense card: `state` (three senses) — **ON PROBATION**

**durable state** — what survives a deploy, a restart and a closed laptop; the reserved sense, and the axis one
whole disagreement item turns on · **graph state** — the framework's in-run object (an attempt's) · **case
state** — a fold over events (#3's C). The frame stays on *durable* except in a `Read next` gloss about the
target lesson, which is correct in place. **Ask:** *does this survive a restart, or is it what the running graph
is holding?*

### Sense card: `snapshot` (three senses) — **the bare word must not travel**

**model snapshot** — a pinned model version (glossary-verified) · **frozen snapshot** — the replay
environment's substrate · and the **corpus's dominant sense**, a dated picture of a fast-moving market ("the
product names are a snapshot", 7+ in `docs/`). Always qualify.

### Sense card: `verdict` — reservation **REINFORCED; the breach has now shipped twice**

Reserved for the assessment of one attempt, on the one page where the word is also a rendered UI label
(`The assessor's verdict`). #2 shipped "says whether that verdict blocks a release"; #3 shipped "the
adopt-or-decline verdict". Both in the *decision-outcome* sense, both caught at Gate 5, both after the row
existed. **Ask before writing it:** *am I naming the assessor's judgement on one attempt? If not, write
`ruling`, `call` or `split`.*

## A page that grades a framework claim is itself making one — **NEW, and it is the class this course should fear most**

Scenario #3 is the first page whose own voice asserts how a named third-party framework behaves, and it grades
an attempt down on those assertions. **Every such assertion is verified against the vendor's live
documentation, at gate time, with the doc language quoted into the report — never from a reviewer's
recollection and never from what this handbook's own lessons say.** #3 shipped two claims and one was wrong:

| claim in Verdict A, as first drafted | ruling |
|---|---|
| resuming from `interrupt()` re-executes the interrupted node from its start | **CORRECT**, and not config-dependent: the docs state it twice, index-based resume matching presupposes it, and it holds across all three `durability` modes (`exit` writes *fewer* intermediate checkpoints, so it widens re-execution rather than narrowing it). Task-level memoisation in the Functional API is *sub-node* and does not rescue a node-level claim |
| "replaying stored super-steps returns recorded values without re-invoking anything, so it verifies nothing" | **WRONG.** LangGraph replay skips nodes *before* the checkpoint and **re-executes everything after it, LLM calls included**. The verdict attributed a history-walk's semantics to a replay and concluded the claim was vacuous. It is not vacuous — it is falsifiable and probably false, which is the stronger criticism. Corrected to "everything after the checkpoint it branches from runs again, model calls included — so 'it lands on the same numbers' is a prediction about a non-deterministic call, not a check" |

**Two structural lessons, both cheap and both missed by every prose gate:**
1. **A wrong framework claim contradicts the page's own later prose, and that contradiction is the free
   detector.** The bad verdict said replay re-invokes nothing; `Where they actually disagree` said "both replay
   positions assume the model … is still callable", and Verdict C stated the re-invoke-or-compare-stored
   disjunction correctly. **Grep the frame for its own claim restated elsewhere before reaching for the docs.**
2. **Do not calibrate against this handbook's own lessons.** `orchestration-frameworks/deep-dive.md` L53 says an
   interrupted run "resumes exactly where it paused", which is the error Verdict A prosecutes. The lesson is
   wrong, not the verdict — filed separately, because it is a translated published page and a locale-synced
   change. A sibling course is not a primary source.

## The frame's stance — assess, never endorse, never design — **SETTLED (warrant predates #2)**

**Third person about the attempt.** Both shipped pages hold this. Scenario #1 opens its verdicts on the
artefact under judgement ("The only attempt that computes before it designs") and uses the bare letter in
subordinate position; scenario #2 opens all three on the bare letter ("A gets the layer separation right").
Both are third-person and neither is a defect. **#1's form is the house form** — it names the move before the
author. Recorded so #3 does not fork it further.

**Assess, never endorse.** An attempt's claim restated unquoted becomes the page's own claim. Quote it, or
attribute it with a reporting verb ("the outcome label, **it says**, rewards handing out money").

**Never design.** The frame states both positions and says which is right; it does **not** propose a fourth
architecture. Scenario #2 shipped two prescriptions — "The right shape is C's source with B's discipline:
mine the dispositions automatically…" and "Both belong, and the ordering is decidable" — neither of which any
attempt wrote. Both were cut at the gate. Scenario #1 closes every disagreement analytically instead
("Neither of them can settle it without the measurement B insists on taking first"). **Naming what is
*missing* from both is assessment; naming what to build is not.**

**Register: no scoreboard.** #1's strongest stance is one clause — "and B is right." `B is right here` matches
it. `C wins this one outright` and `A's is the losing position` do not: a contest metaphor is a fourth
evaluative axis stacked on common / strong / over-built. Both were softened at the gate ("C has the better
source here", "A's is the weakest of the three here").

**Every superlative is a checkable claim about all three attempts.** "the only answer that…", "something many
answers skip", "the one number B does not derive" — each gets read against the other two attempts before it
ships. Scenario #2 shipped four that a reader could falsify by scrolling up; that is the single most
expensive defect class this course has, and it has now appeared on both pages.

**Scenario #3 makes it three, and adds the shape the rule missed: an exclusivity claim about the ARGUMENT, not
about an attempt.** "which is exactly the reconciliation neither side of the framework argument settles on its
own" was falsified by Attempt B, which holds that very reconciliation as an explicit gate ("Condition to adopt:
it holds run orchestration only, no durable state"). Nothing in the sentence named an attempt, so a
letter-keyed check would have passed it. **Read every claim about what "neither side", "the usual answer" or
"both designs" does against all three attempts, exactly as if it had named them.** Also caught on #3: "Three
positions, mutually exclusive" (retracted by the same item's next paragraph, which shows C reducing to B) and
"B and C both: … the engine is replaceable" (over-attribution — C adopts LangGraph and calls durability a
property of the substrate).

**Verdict openings — the designated house form is now the minority practice, and that needs the author.** All
three of #3's verdicts open on the letter or its possessive ("A's opening read is right", "B states the
distinction", "C buys something real") — #2's form. #3 did not fork it further, but it made #2's form the
incumbent **by count**, 2–1, against #1's form which the row above declares the house form **by ruling**.
Either the designation moves to #2's shape or #3's three verdicts move. **CONTESTED for the author** — it
cannot stay a ruling that two of three pages contradict.

## `Why this question` — what it may not contain — **SETTLED (extends the rejected row above)**

The box is read **before** the reader commits, so it says what is under test and nothing about who gets it
right. #1's form is the model: the trap is described **agentlessly** ("The tidy answer is to classify the
query and dispatch it to a tier"), and no tier label appears in the section at all.

**Barred: naming a tier label here, in any polarity.** The existing rejected row struck "you will agree with
the strong answer…" for naming the winner; #2 shipped the mirror defect and named two *losers with their
diagnoses* — i.e. two of the three verdicts, pre-commit. Also barred by the same logic: inventing a tier to
dodge the rule.

**And the box is checkable prose, written LAST — against the verdicts, not first against the prompt.** #2's
box contradicted its own Verdict A (box: "without pricing the judge"; verdict: "prices that judge … without
computing it") and mischaracterised C.

**Third consecutive page, and the TEMPLATE is why — now fixed at the source.** #3's box wrote "**The common
answer** argues framework against hand-rolled and never separates the two kinds of waiting, which is where both
designs actually fail" — a tier label with a diagnosis attached, pre-commit. The reason the class recurs was
identifiable and mechanical: `_scenario-template.md` said only *"Do not name a quality tier the course does not
have"*, which bars **inventing a fourth tier**, not **naming one of the three**. An author following the
template shipped this defect and passed their own check. **The template was rewritten in this run** to carry
the ledger's wording (name no tier at all, in any polarity; describe the trap agentlessly; write the box last).
A ledger rule the template contradicts will lose to the template every time.

Two further defects rode in the same sentence, both already-rejected shapes: **`both designs`** had no
antecedent (no design has been shown to a pre-commit reader), and the claim was **falsifiable against the
attempt a reader maps it to** — Attempt A never argues framework against hand-rolled; it adopts a framework
without arguing.

## No interview-coach register anywhere in the frame — **SETTLED**

`If they push` is the highest-risk zone: it is the only section written *about the reader*. It states what a
question exposes, and stops. **Barred:** motivational or careerist framing; a maxim about professional
virtue; an ungraded population claim about engineers or candidates. See the rejected rows for the four
instances scenario #2 shipped and the replacements.

## The reveal boundary — the rule extends to TERMS and ALLUSIONS

The recorded rule bars pointing into the reveal **by position**. Scenario #2 shipped two further shapes:

- **By term.** `If they push` used "the trajectory layer" twice — Attempt A's coinage, defined only inside
  `<Reveal>`. **A frame section outside the reveal may use only terms it or the prompt has defined.**
- **By allusion.** "both slogans apply" (no slogan exists anywhere on the page) and "the part of the answer
  already agreed" (no singular "the answer" exists, and no agreement was shown to a reader who did not open
  the reveal). **Anchor a callback in the prompt.**

**A callback is a checkable claim.** Every attributed or quoted fragment is grepped against its source before
the page ships. Scenario #2's twelve verified quotes were; these two were not, and two more were inexact.

**Scenario #3 shipped the by-term shape twice more, and surfaced a genuine gap in the rule.**

- **The breaches.** `If they push` used **`the checkpoint`** — Attempt A's mechanism, defined only inside the
  reveal — and the box used **`the graph`**, which the prompt never mentions. Both were replaced with prompt-
  anchored wording (`the run that produced the grade`; `whoever executes the steps`).
- **The compliant counter-example on the same page**, worth keeping because it shows the rule is workable:
  `pause-versus-reopen` was legal in the same section because the box states both halves before a reader
  commits. Anchor the callback in the prompt or the box. #3 went further and spelled the distinction out.
- **The gap, RULED this run.** #3's `Read next` glosses introduce `checkpointer`, `super-step`, `thread_id`,
  `durability modes` and `interrupt node` outside the reveal. These are not an attempt's coinages — they are the
  **target lesson's** vocabulary, arriving inside a gloss that says what the destination teaches, so nothing
  dangles. **Scoping: the rule bars terms the frame relies on for its OWN argument; a link gloss naming the
  destination's vocabulary in place is exempt.** Recorded as a ruling so #4 does not relitigate it.

## The disagreement items — H3, parallel — **SETTLED; retro-fit CONTESTED**

Scenario #1 wrote the items as bolded questions inline; scenario #2 wrote them as `###` headings and shipped
with **no lead paragraph at all**, so a reader landed on a bare H3 straight after the H2 (2 occurrences of
that shape in 251 corpus files). The lead paragraph is now a recurring block string (above).

**Settled:** the items are `###` headings, and **parallel with each other**. The reason for H3 over bold is
`_language.md` §8 — a clause-length question in bold is intonation, not navigation — and `hide_table_of_
contents: true` means H3s cost no TOC noise. The parallel form is the incumbent one two of #2's four headings
already used: **`Topic: option A or option B`**. #2 shipped four different shapes and was normalised to that.

**CONTESTED, for the author:** whether #1 is retro-fitted to H3s; and whether a disagreement section at 2.7×
the sibling's length is wanted at all — at that weight it rivals an attempt, inside the reveal, which sharpens
the OPEN question about `The principle`'s placement. Do not let scenario #3 settle either by repetition.

**Scenario #3 forked the settled shape 0 of 4, and was normalised to it at the gate.** #3 first shipped four
headless interrogatives (`What "reproducible" means`, `Who owns the durable state`, `Whether the 900 lines get
rewritten`, `What the six weeks extract`) — parallel with each other, so half this row held, but none in the
incumbent form, and two failed the shuffle test outright: "the 900 lines" and "the six weeks" have no referent
read from a sidebar, and `extract` sat there transitive with no object. Normalised to `Reproducible: replay it or
retain it` · `Durable state: the framework's or yours` · `The 900 lines: wrap them or replace them` ·
`The six weeks: a document or a demonstration`. **The shape's real virtue is the shuffle test, not tidiness** —
naming both options makes the heading decode cold, which the question form cannot.

**Honest residual, recorded rather than papered over:** items 1 and 4 discuss three positions, not two, so
their headings name the dominant axis and the third position is met in the body. That is the shape working at
its limit, not a defect. **The retro-fit question is now downstream of this** — settle nothing on #1 until the
shape is ratified, or #1 gets retro-fitted twice.

**Length — the repetition the row warned about happened.** Disagreement sections, prose lines: #1 = 15, #2 = 40,
**#3 = 40** — ~0.7× one of #3's own attempts. Two pages at this weight, inside the reveal, in front of
`The principle`. **Still CONTESTED, now three pages old and compounding.**

## Numeral register in the frame — **SETTLED**

The verdicts **mirror the numeral register of the attempt they judge** (A and C spell figures out, so Verdict
A and Verdict C spell them out; B uses digits, so Verdict B uses digits), and the neutral analytical
register — `Why this question` and `Where they actually disagree` — uses **digits**. This is a coherent
system, not drift, and it was verified before being recorded rather than assumed. Ranges take an en dash in
the frame (`1–5`, `3–5%`) even where the attempt being paraphrased used a hyphen — the `top-K` precedent.

**CONTESTED, for the author:** the blockquotes in `If they push` spell numbers out as spoken register
("up sixty percent"), where scenario #1's interviewer speaks in numerals ("the bill is down 45%"). Pick one
for the course. **#3 sides with #2** — its three probes spell out throughout and use no digits — so the count is
now 2–1 for spoken-register spelling-out, the third item this course has settled by repetition. Cheapest
resolution: ratify the majority and correct #1.

**The row states a register rule and describes a magnitude rule — reconcile it.** It says the neutral analytical
register "uses **digits**", but #2 and #3 both spell small numbers and use digits above ~100: #2's box has
"eleven steps" beside "200 cases a week … against 63,000 a week"; #3's has "Four of the postings" beside "the
900 lines". Two pages agree on a **magnitude** rule; the row records a register rule, and applied literally it
would demand "4 of the postings". **Nothing on either page is the defect — the row is.** Not rewritten here,
because a pass may not silently reverse a row it did not evidence: **CONTESTED for the author.**

## Figures — scenario #2 (frame only) — **ALL ON PROBATION**

Per the no-self-issued-exemption rule none of these may be marked protected by the pass that shipped them.
Reviewers keep testing them like ordinary text until a cold read or milestone pass confirms or strikes.

- **"a diagram, not a measurement"** (`The principle`) — the page's controlling image.
- **"the odd figure out"** (Verdict B) — idiom play on *the odd one out*, applied to a number.
- **"Then the bill."** (Verdict C) — elliptical; the cost as the sentence that ends the credit.
- **"where the arithmetic belonged"** (Verdict C).

Struck at the gate: **"the losing position"** and **"a review process that compounds"** (scoreboard and
anti-coach rulings). **Standing, reused from #1 and the template:** the **buy** family ("what it buys, what
it costs"). Keep `buys` for *what an approach gains*; do not also use it for *paying* in the same section.

**Attribution warning for the next reviewer.** "buying silence", "settlement signal", "rounding error",
"rotting", "malpractice", "blast radius", "circuit breaker", "correlated garbage", "ten thousand real
yesterdays" all live **inside attempts**. They are testimony: not the page's figures, not canon material, not
counted against the figure budget. Where the frame reuses one it quotes it — the correct handling.

## Figures — scenario #3 (frame only) — **ALL ON PROBATION**

Per the no-self-issued-exemption rule none of these may be marked protected by the pass that shipped them.
Ten frame figures against #2's four, in a shorter frame — the aggregate, not any single item, was the finding,
and two were cut at the gate for stacking.

- **"making publication rewindable"** (Verdict A) — the page's sharpest image, and the exact name for A's error.
  Corpus-anchored: the glossary's Checkpointer entry already says a run can be "rewound".
- **"the guarantees read off them"** (Verdict A) — reading a value off an instrument.
- **"puts that claim in a dependency's tables"** (Verdict A).
- **"a routine upgrade migrates evidence"** (`Where they actually disagree`) — the strongest of the new set:
  entirely concrete, and it carries the argument in five words.
- **"the argument eats itself"** (Verdict C) — the over-build indicting itself; kin to #2's "Then the bill."
- **"C buys something real, and pays for it twice"** (Verdict C) — compliant use of the **buy** family, and the
  clearest instance yet of what that rule permits: `buys` for what an approach gains, `pays` for cost.
- **"B's answer wearing C's clothes"** (`Where they actually disagree`) — rides *wolf in sheep's clothing*.
- **"current output is a free oracle"** — *oracle* is corpus vocabulary in the testing sense, so reuse, not
  coinage; needs no gloss.
- **"what walks out is operational"** (`Where they actually disagree`).
- **"with nowhere to hide"** (`If they push`), mild.

**Struck at the gate for figure-stacking, not for being bad:** "its test only **bites** on the deterministic
layer" (→ "only reaches"), which sat in one sentence with "B's answer wearing C's clothes" — two figures for one
idea, the ROADS/MACHINERY ruling. And `collapses` was carrying two senses eleven screens apart (Verdict A
"collapses the two waits" = *conflates*; the item's "collapses into B's answer" = *degenerates into*) — the
second became "reduces to". **The `buys` precedent generalises: a verb doing figurative work in the frame gets
one sense per page.**

**Attribution warning for the next reviewer.** "the substrate", "a liability we're carrying", "the cheapest
moment this rewrite will ever be", "Then he's replaceable", "a different answer, not a cheaper copy",
"his queue knowledge has a deadline" all live **inside attempts** on #3. Testimony: not the page's figures, not
canon material, not counted against the figure budget.

## The reader-of-record — house name is `auditor`

The frame's word for whoever reads the record later is **`an auditor`**. **`the accreditation review` names the
event, not the reader.** #3's prompt first read "the accreditation review … which will read your records", where
a review cannot read; it was corrected to "where an auditor will read your records", which also bridges the
frame's own noun to the prompt at its first appearance. Recorded because the attempts supply four more names
(`an outside party`, `the accreditation reviewer`, `the reviewer`, `the review`) and the frame must not pick
them up.

## Quoting mechanics in the frame — what may and may not change

Stated once, because Gate 5 caught four instances of the same slip on one page.

- **Adjusting the initial capital** to integrate a quotation mid-sentence is permitted. A later pass must not
  "fix" it back.
- **Re-nesting quotation marks** (a source's `"…"` inside yours becomes `'…'`) is required, not an edit.
- **Everything else inside the marks is byte-exact**, ellipsis for elision, and **the frame's own punctuation
  goes outside the closing mark.** Dropping a source's italics is acceptable; adding a comma is not.

## The serial comma is free variation — do not normalise it

Corpus is **364 Oxford / 224 non-Oxford**. #3's frame mixes both. **There is no house rule and none is being
made.** Recorded so no future pass mistakes it for drift and opens a 588-instance sweep. A mixed comma is
invisible; the sweep would not be.

## Jurisdiction note — scenario #3: divergences observed inside attempts, deliberately left standing

- **Attempt A: `superstep` ×5** where the corpus is `super-step`. Stands. **Verdict A's instance was the
  defect** — the same split as #1's `top-k`.
- **Attempt C: `durable interrupt`** where the target lesson says `interrupt node`. Stands; the frame used the
  lesson's words, which is the correct handling.
- **Three names for one object across three attempts** — `judgement row` (B), `event log` / `judgement ledger`
  (C), `the record` — plus `thirty days` (A) against `30 days` (C). Stands, and is the page's best evidence of
  genuine independence.
- **Attempt B's US comma-inside-quotes**, where A and C use British placement. Stands, and the frame reproduces
  it faithfully when quoting B.
- **One mechanical fix inside an attempt, the first this course has made:** Attempt A's diagram had `borderline
  ▼` one column right of its own flow line (col 30 against col 29 on four neighbouring rows). Character-level,
  no wording touched. **Recorded as the worked example of what "outright mechanical error" licenses inside
  testimony** — a misaligned box-drawing column, not a word.
- **All three attempts came in British-clean** — a full US-spelling sweep returns zero hits page-wide. First
  scenario needing no spelling exemption inside the attempts. The standing warning holds anyway: a mechanical
  spelling gate must exempt the attempt line-ranges, because `superstep` is exactly what it would rewrite.

## The attempts converged on a CONSTRUCTION — a third tell class, for the pipeline owner

Not a page defect and not fixed. #3's three blind attempts share one syntactic frame: **`stops being …`, five
times across all three**, and A and B share the subordinate clause **"the moment a case can be reopened"**
near-verbatim. This differs from the two tells `how-these-are-made.md` records — personas converging on *level*,
and instruction failing to move *paragraph shape*. Here independent agents converge on a **construction**, which
points at the prompt rather than the personas. Also convergent: B and C both closing on a bold `**LangGraph**`
section, and all three producing exactly one ASCII diagram unprompted, third page running. Moving in the right
direction: em-dashes 7/6/9 against #1's 10/10/10, and bolded-declarative paragraph openings at 29–40% against
#2's 75–89%.

## HOUSE — an instrument as the subject of *tells you* — **SETTLED, do not flag**

"a tagged score slice **tells you** what the surge cost", "carrier and WMS state **tells you** whether the
reroute moved the parcel" are house form, not actor–verb defects: the corpus carries 11 instances of a
measurement or property as the subject ("Recall@K tells you whether…", "residency tells you *where* your data
sits"). Recorded because the Gate-2a actor–verb sweep flags this shape on sight every page. **The rule still
stands for agents that decide** ("the metric rewards", "a credit closes").

## Bold budget on a scenario page — measured

Measure the **frame only**; the attempts' bolded spoken section labels are their register and are excluded.
Re-measured across all three pages with one method (code fences and blank lines excluded, frontmatter
excluded, attempt line-ranges separated) so the numbers are comparable rather than each page's own arithmetic:

| page | frame | attempts |
|---|---|---|
| #1 model-routing | 4 / 115 = **0.035** | 14 / 126 = 0.111 |
| #2 trajectory-vs-outcome | 3 / 143 = **0.021** | 22 / 126 = 0.175 |
| #3 framework-or-primitives | **1 / 138 = 0.007** | **13 / 133 = 0.098** |

Cap is ~0.36; no page is close. #3's single frame span is the fixed commit line. The attempts' number is
**never** a budget finding — it is pipeline signal about persona bleed, reported to the producer, never fixed.

**Correction to this row, 2026-07-30 (Gate 5, scenario #3) — a recorded measurement was wrong.** The row
previously read "Scenario #2's frame: **1 bold span / 122 prose lines = 0.008** … The single span is the fixed
commit line." #2's frame carries **three**: `**outcome**` and `**trajectory**` in `Why this question` — both
legitimate first-defining-mention anchors under `_language.md` §8 — plus the commit line. The verdict is
unchanged; the count was not. **A row asserting a measurement must state its method**, or the next pass cannot
tell a real change from a different way of counting.

**Under-use is now the trend.** Frame bold has gone 0.035 → 0.021 → 0.007 while the attempts hold near
0.1–0.18. #3's box uses **zero** term anchors where #2 anchored its two controlling terms. The budget is a cap,
not a floor — but §8 says bold's first job is the anchor at a defining mention, and #3's box defines the page's
controlling distinction (suspending an open run versus reopening a closed one) with nothing marked.

## Product and vendor names inside an attempt — **RULED, KEEP; author may overturn**

Scenario #2's Attempt A names "Braintrust or LangSmith-style dataset" and Attempt C "dumps traces to S3".
The sourcing rule bars naming a **company the scenario came from**, obliquely or directly — it is about
anonymising the source, not about a candidate name-dropping a tool. And the names are *persona evidence*: A
was given "follows the eval-tooling ecosystem closely", and removing them erases the tell. Precedent cuts
the same way in the stricter register — #1's Verdict C names "The vLLM tier" in the page's own voice.
**Ruling: keep, inside attempts.** Recorded as a decision rather than an oversight, because #3 will hit it
again. If the author overturns it, #1's verdict is the more serious instance and moves first.

**#3 extends it to the FRAME, deliberately.** `LangGraph` now appears in the `description`, the
`Why this question` box and the track overview's gloss ("the LangGraph question"), because the prompt names it
and it is *why* this question gets asked. **RULED, KEEP** — with one recorded asymmetry the author may want to
revisit: the course titles its decisions vendor-neutrally (`Framework or your own primitives`), so the gloss
makes the scenario look narrower than its own title.

**`your open req` in the prompt — RULED, KEEP.** Gate 5 proposed striking it as US recruiting jargon colliding
with the course's own `posting`. Overruled at adjudication: `req` is what a hiring manager actually says out
loud, the prompt is spoken register, and the jargon rule targets **needless erudition**, not real workplace
vocabulary. The provenance formula is untouched — it governs how the *course* describes its sources
("published job postings"), not what an interviewer calls their own open role.

## Scenario #4 — `agent-memory` (Gate 4 + Gate 5, 2026-07-30)

**Block strings.** #4 reproduces byte-exactly: the three attempt headings and tier labels, the commit line, the
`<Reveal>` control (inherited, never overridden), `Where they actually disagree`, `The principle`, `Read next`,
`If they push`, both frontmatter comment lines, the `<Verdict>` form, the persona furniture, and #3's long
provenance paragraph. **Two misses, both fixed at the gate:** the **disagreement lead** was absent entirely (the
reader landed on a bolded item straight off the H2 — the shape #2 shipped and the gate fixed), and the
**follow-up lead** was replaced with an interview-coach sentence. Both restored to the ledger strings.

**Correction to the probation-clearing note above.** That note claims #3 reproduced the follow-up lead
byte-exactly. It did not: #1 = "These are the follow-ups… what each one exposes.", #2 = "These are the **three**
follow-ups… what each one exposes.", #3 = "Three follow-ups an interviewer reaches for next, and what each
exposes." Three pages, three strings; only #2 matches the row. **A row cleared as "SETTLED, three pages
byte-exact" must cite the three strings it compared** — this one was cleared on assertion.

**Disagreement shape — SETTLED, forked 0 of 5, and the settlement is not reaching authors.** #4 shipped #1's
bolded-inline-question form plus numbering new to the course, five items where the template says two to four, and
no lead. Normalised at the gate to `The wake's read path: …` · `Evidence a charge stopped: …` ·
`Deletion mid-workflow: …` · `Shared merchant knowledge: …` · `A stricter close condition: …`. One original
heading failed the shuffle test outright ("Is the stronger evidence bar free?" — no referent read cold), and the
replacement had to be recast a second time for the same reason. **Two consecutive pages have forked a SETTLED
shape 0-of-N, which means the shape lives in the ledger and not in `_scenario-template.md`. Put the H3 form, the
`Topic: A or B` pattern, the lead-paragraph string and the two-to-four count into the template** — the
`Why this question` fix proves that is the intervention that works.

**Bold budget — measured, same method, plus two method amendments.** Frame **as shipped: 15 / 166 = 0.090**
(11 of the 15 spans were attempt-register bolding migrated into the frame); **after the gate: 4 / 177 = 0.023**,
in the #1/#2 band. Method amendments forced by this page: **(a) pair `**` delimiters across line breaks** — a
per-line regex undercounts by 3; **(b) the per-line denominator requires wrapped source.** #4's attempt
paragraphs are unwrapped (27 lines of 200–727 characters against the siblings' ≤~110), which inflates the
attempts' figure to a meaningless 0.440 where per-1,000-words they are 9.83 against #2's 10.00. **Report
per-1,000-words alongside, or state a wrap precondition.** Re-wrapping was considered and declined: whitespace
normalisation inside testimony is not one of the three mechanical licences.

**`Why this question` — the template fix is VALIDATED, and a new failure axis is recorded.** #4 is the first page
written against the rewritten template and complies cleanly on every barred item: no tier label in any polarity,
no fourth tier, nothing about who gets it right, no claim about interviews sat, and a provenance figure with **no
denominator** ("Two of the postings this course samples…") that instantiates `intro.md`'s published rule. Record
the mechanism: **a ledger rule the template contradicts loses to the template; a ledger rule the template carries
wins on the next page.** Every future rule in this section ships into the template in the same commit.
The new axis is the `persists` row in the rejected table — **the box's definition of each axis is checked against
what the verdicts score, not only against the prompt's wording.**

**Verdict openings — the CONTESTED row can no longer be settled by count.** #4 splits 1–1–1: Verdict A opens on
the move (#1's designated house form), B on the letter (#2's form), C on the artefact (neither). Four pages, no
convergence. **The designation is not being followed even by accident, which is the strongest argument yet that
it should be dropped rather than re-designated.** CONTESTED for the author.

**Numeral register — both CONTESTED halves now resolvable by majority.** #4's three `If they push` probes spell
throughout with zero digits, so spoken-register spelling-out is **3–1** and #1 is the outlier. And its neutral
analytical register applies the **magnitude** rule (`six days`, `thirty-odd`, `week nine` beside `~45,000`,
`$12,000`, `1.2%`), so three consecutive pages contradict the row's literal "uses digits". Nothing on any page is
the defect; the row is, and it is three pages behind. Author's to rewrite.

**`verdict` reservation — the row is WORKING.** #4 is the first page since the row was written not to breach it:
every occurrence is the reserved sense plus the six component tags. Keep REINFORCED.

**A FIFTH frame section — CONTESTED for the author.** #4 adds `## The copy of state nobody priced`, which no
sibling carries and the template's fixed section list does not admit. **Gate ruling: retained, recast from a
design proposal into an assessment.** As shipped it proposed a fourth architecture in the page's own voice,
argued for it, then graded its own proposal — a structural breach of **never design**, whose boundary test is
"naming what is *missing* from both is assessment; naming what to build is not". Two of four roles voted to cut
it outright; it was kept because the arithmetic it performs belongs to no attempt and no `Read next` bullet could
carry it, and because the caller listed the section as in scope for editing rather than deletion. Recast so the
subject is the omission, not the design: *all three store a copy of state two durable external records already
hold, and not one prices the alternative.* **The author must rule on whether a fifth H2 is admissible at all** —
`how-these-are-made.md` gives every voice on the page an author and assigns the Orchestrator "Nothing on the
page", so an ungraded fourth answer in the frame's voice is a disclosure question as well as a structural one.
Related precedent, and it licenses a *sentence* rather than a section: #3 routed its un-taken third option
through a `Read next` bullet crediting the lesson that covers it.

**`The principle`'s placement — #4 makes it four, and adds the sharpest evidence yet.** #4 again puts it inside
the reveal and not last. But `Read next` bullet 1, which renders **outside** the reveal, originally announced the
verdicts' own position on the principle's subject — i.e. the payoff leaked out of the container while the sentence
stayed in. Four pages, four gate fixes of the same shape. **Rule: either the principle moves outside the reveal,
or the sections rendering outside it are barred from touching its subject.** The second is what four gates have
now done by hand.

**Disagreement-section length — CONTESTED, four pages, #4 the heaviest.** Prose lines: #1 = 15, #2 = 40,
#3 = 45, **#4 = 44, or 53 counting the fifth section in the same zone**. #4's disagreement zone exceeds one of
its own attempts, inside the reveal, in front of `The principle`. The author has the full curve now.

### New terms — ON PROBATION (coined in this batch; the pass that proposed them may not settle them)

| term | working sense |
|---|---|
| **wake** | one resumed run — the workflow comes back on an event, reads, decides, and suspends again; **also the unit the budget divides by.** #4 used it as a count noun three times in the prompt before defining it, and two independent naive readers stalled on the page's most load-bearing word. **Glossed in the box at the gate. Rule: a unit the page prices in gets defined before it is counted.** |
| **read path** | what a wake assembles and reads, as against what persists. Plain and self-glossing; no attempt writes it. |
| **open inventory** | the stock of concurrent workflows; glossed in place by "the ~45,000 concurrent workflows". |
| **attribution test** | the frame's general name for the mechanism separating a bad read from a bad tool result; self-glossed by the quoted mechanism that follows. |
| **77-day tail** / **week-nine workflow** | derived from the prompt's eleven weeks, arithmetic verified, used consistently. |

### Sense card: `state` — a FOURTH sense, ON PROBATION

#4 adds **state-machine state**: a named phase of a workflow (`pending_confirm`, `cancellation_asserted`,
`abandoned_user_deleted`, `stopped`). On #4 this is the *dominant* sense and the frame does not slip — every
occurrence is disambiguated by a code span or an adjacent qualifier. Card now reads: **durable** (survives a
restart) · **graph** (the framework's in-run object) · **case** (a fold over events) · **state-machine** (a named
phase, usually in a code span). **Ask:** *does this survive a restart, is it what the running graph holds, is it
derived from events, or is it the phase the workflow is in?*

### `record` on a page with no auditor — ON PROBATION

#4 carries a **deletion** duty, not a retention-and-auditor duty, so `the record` is not this page's house term
and the frame correctly does not force it (one plain-plural use). The reader-of-record row is dormant too: no
`auditor`, and the frame picks up none of the attempts' role nouns. **Recorded so no later pass "normalises" a
page toward a house term its prompt does not license.**

### Figures — scenario #4 (frame only) — ALL ON PROBATION

- **"A model-written summary can only cite itself"** (`The principle`) — the controlling image. Three
  independent roles flagged the shipped form ("A summary can **only ever** cite itself") as literally
  falsifiable, since a summary *can* carry citations; the qualifier `model-written` closes it and is the page's
  own argument. **A maxim in the collection's most-quoted slot must survive a literal reading, not only survive
  the numbers being wrong.**
- **"laundering the attribution its own 1.2% answer depends on"** (Verdict A) — a money-laundering image on
  provenance, on a page about disputed charges. Domain-resonant. **Cut at the gate** for the separate reason that
  the claim it carried was overstated (A's ledger survives the summary).
- **"It buys bounded context … The cost is A's own best idea"** (Verdict A) — compliant **buy**-family use,
  the clearest instance yet: `buys` for what an approach gains, `cost`/`price` for what it pays. One sense each
  per page, honoured throughout.
- **"asserts the arithmetic instead of doing it"** (Verdict A) — plain and reusable.
- **"changing the denominator, not the prompt"** (Verdict B) — arithmetic as argument; carries the verdict in a
  clause.
- **"Two cracks."** (Verdict B) — elliptical, kin to #2's "Then the bill."
- **"leaves mail-body `artifact_ref`s dangling … the evidence expires with the case still open"** (Verdict B).
- **"sits in the open inventory"** / **"draw on the same account"** (disagreement 5) — one sustained accounting
  figure rather than three competing ones, which is the correct way to spend the budget. A third money figure in
  the same paragraph was cut.
- **"deletion is a property you build in, not a job you schedule"** (`If they push`) — a **technical** maxim, so
  the anti-coach rule permits it. Note it is the page's second maxim and it lives **outside** the reveal where
  `The principle` lives inside; bears on the placement ruling above.
- **Struck at the gate:** "you just deleted them" (glib second person about a user); "goes looking for the
  seams" (and `seam` is #1's Attempt A's coinage — **cross-page borrowing of a sibling attempt's word into a
  later frame is the same adoption breach**); "Credit first:" (signposting about the verdict's own rhetoric).

### Jurisdiction note — divergences observed inside #4's attempts, deliberately left standing

1. **Attempt A: `top-k`** where §3 fixes `top-K`. Stands; #4's frame contains no `top-k`, so no verdict instance
   to correct — the first page where the split resolved itself.
2. **US `artifact`/`artifacts` in B and C, none in A.** Stands. **Verdict C's instance was the defect** — the
   same split as #1's `top-k` and #3's `superstep`.
3. **US `normalize` / `normalized` / `generalizes` in C only.** First page since #2 needing a spelling exemption
   inside the attempts; #3 came in British-clean. Stands.
4. **`2,000` (A, B) against `2000` (C)**; **`Thirty days` (A) against `30 days` (B, C)**; **`in-flight` (A)
   against `in flight` (B)**; **`ten cents` (A) against `$12k / 120k`, `1.1¢` (B) against `~3k` (C)**. Stand.
5. **Three vocabularies for one object** — A `workflow state` / `rolling summary`; B `fact row` / append-only
   ledger; C `Observation` / `WORKFLOW LEDGER` / `WAKE BRIEF`. Plus A's `merchant procedural memory` against C's
   `MERCHANT PROCEDURE MEMORY` against B's `merchant playbook`. Stands, and is the page's best evidence of
   independence.
6. **A's own contradiction on one-time codes** (`15-minute TTL` vs "never persisted") — priced by Verdict A ✓.
7. **Three attempt-internal errors NO verdict prices, reported to the assessor, not edited:** B's
   `decision-grade facts ~600 tok … (capped ~40)` = 15 tokens per seven-field row, under the one claim B rests on
   ("bounded by construction"); B's `~2.5¢ each` where 1.1¢ ÷ 0.40 = 2.78¢; A's `user_id` as "the partition key
   across all four tiers" against A's own cross-user merchant tier, which a per-user cascade would delete. Also
   B's closing "Two stores" against its own third (the versioned playbook).
   **Zero mechanical errors were found inside the attempts — no typo, no broken construct, all three ASCII
   diagrams column-verified. First page of the four needing no mechanical fix inside testimony.**
8. **The exemption is now urgent, not theoretical.** #4 needs the attempt ranges exempted from **three**
   mechanical sweeps (`top-k`, `artifact`, `normalize`), and the same sweeps must run **on** the frame — the
   frame instance of the shared word has been the defect on **all four** pages (`top-k` #1, `artifact` #2,
   `superstep` #3, `artifacts` #4). **One gate, two ranges, opposite polarity.**

### Cross-course reference conventions — new row, ON PROBATION

#4 is the first page to go **5-for-5** reproducing a target's `sidebar_label` verbatim, `&` and `:` intact
(`Plan search & memory`, `Sampling, SLOs & budgets`, `Graphs & durable execution`, `The arithmetic: context,
caching, and the retry tax`, `Injection defence & red-teaming`), against #1's three invented names. But #4 labels
`planning-loops/deep-dive` by its **`sidebar_label`** where #2 labels the same target by its **`title`**. Both
are legal under the existing row; the result is one destination with two names in one course. **Rule to add: when
a target is linked from more than one scenario, reuse the same one of its two names — the first page to link it
fixes the choice.**

### Recurring-block candidate, ON PROBATION

#4 adds a fourth provenance sentence: `That arrangement is described in [how these are made](…)`. #1/#2 carry the
link parenthetically inside the recurring clause; #3 puts it in a separate paragraph on a different subject; #4
gives it its own sentence, which leaves the recurring clause unbroken and still lands the link before the reveal.
Two pages must reproduce it before it becomes a block string.

## Scenario #5 — `tools-that-fail` (Gate 4 + Gate 5, 2026-07-30)

**Block strings — the first 5-for-5 page, zero misses.** #5 reproduces byte-exactly: the three attempt headings
and tier labels, the commit line **and its second sentence**, both frontmatter comment lines, `Where they actually
disagree`, the disagreement lead **including #4's exception clause**, `The principle`, `Read next`, `If they push`,
the follow-up lead (indefinite article and "three" intact, and the count matches the three blockquotes), the
`<Verdict>` form with blank lines inside all six tags, the inherited `<Reveal>` control, the persona furniture, and
#4's provenance paragraph. First page needing no block-string restoration at the gate.

**Promote to block strings (candidates, ON PROBATION until a sixth page confirms):**
`Out loud or on paper, whichever you'd do at a whiteboard.` — the commit line's second sentence, **5 of 5 pages
byte-exact and never recorded**; and `That arrangement is described in [how these are made](…)` — #4's candidate
row now has its second page.

**Correction: the provenance clause moved two pages ago and the `rubric` amendment is stale.** #3, #4 and #5 carry
"none saw **the scoring standard the verdicts are written against**". The recorded clause ("or the rubric, which
was written first") survives only on #1 and #2. Incumbent by count and by three independent passes: the
no-`rubric` form. The scoped `rubric` amendment now governs nothing on the current pages — leave it as history.

**Disagreement shape — forked 1 of 4, the best result since the shape was settled** (#3: 0/4, #4: 0/5). Items 1–3
arrived in `Topic: A or B`; item 4 (`One state for the night, or one per consumer`) named both options and no
topic, and was normalised to `The stale publish: one state for the night, or one per consumer`. Item 5 is the
shared-blind-spot closer, correctly flagged in the lead and correctly **not** promoted to a fifth `##`. Four
disagreements plus the exception sits inside the template's two-to-four count. **The `Why this question` mechanism
is confirmed a second time: a rule that ships into `_scenario-template.md` stops being forked.** Two commas before
`or` in headings 2 and 3 were dropped — 0 of 13 sibling `###` headings use one.

**Disagreement length — the CONTESTED curve turns down for the first time.** Non-blank lines / words between the
H2 and the next H2: #1 = 14/202 · #2 = 39/627 · #3 = 44/686 · #4 = 66/1,158 · **#5 = 34/533**. #5's zone is ~0.77×
one of its own attempts, the first page since #1 where it does not rival an attempt. The author now has a curve
with a downward point on it.

**Bold budget — measured, same method, and the trend reversed then was corrected.** Method: frontmatter, fenced
blocks, blank lines, the three attempt headings and the three persona lines excluded; `**` delimiters paired
**across line breaks**; attempt ranges separated. Script: `scratchpad/bold.py`.

| page | frame | frame /1k words | attempts |
|---|---|---|---|
| #1 model-routing | 4 / 115 = 0.035 | 2.56 | 14 / 120 |
| #2 trajectory-vs-outcome | 3 / 143 = 0.021 | 1.45 | 22 / 120 |
| #3 framework-or-primitives | 1 / 148 = 0.007 | 0.47 | 13 / 127 |
| #4 agent-memory | 6 / 195 = 0.031 | 2.03 | 22 / 44 (unwrapped) |
| **#5 tools-that-fail** | **as shipped 10 / 143 = 0.070 → after the gate 4 / 145 = 0.028** | 1.84 | 18 / 38 (unwrapped); **8.73 /1k w** |

Six spans were struck: **five bolded whole-sentence rulings** in `Where they actually disagree` and one
mid-sentence stress (`**from its start**`) in `Read next`. **This is an already-rejected row shipping again** (#4,
×6) — a defect class that ships after its own rejected row exists is a missing gate, not an author slip: the §8
sweep must run **on the frame ranges and skip the attempt ranges**, the same two-range shape as the spelling sweep.
The attempts' figure is pipeline signal only, never a budget finding, and it is the lowest since #3.

**Two recorded measurements do not reproduce.** Under the method that reproduces #1 (4/115) and #2 (3/143)
byte-exactly, #3 measures **1/148** (recorded 138) and #4 measures **6/195**, not the recorded "after the gate
4/177". #4's extra spans are `**never written**` (L45) and **`**or**` at L305, inside a quotation** — the rejected
"emphasis ADDED inside a quotation" row, still live on a published page. **A gate fix recorded in the ledger is not
evidence the fix reached the file: cite the line and re-grep after the edit.** Handed up, not fixed here.

**`Why this question` — the template fix VALIDATED a second time, and one NEW defect axis.** Clean on every barred
item: no tier label in any polarity, no fourth tier, nothing about who gets it right, the trap described
agentlessly, no claim about interviews sat, and a provenance figure with no denominator. Three gate fixes:

- **The definition of the page's key term was wrong** (see the rejected row below). This is the #4 `persists`
  shape a second time and the caller's own predicted failure: a definition **present, confident, and inverting the
  page's argument** is far harder to spot than a missing one. **Rule, now twice-evidenced: check the box's
  definition of its key term against (a) what the verdicts score, (b) the corpus glossary, and (c) the term's real
  meaning in the field, verified at a primary source at gate time.**
- **Two of the box's illustrative facts were Attempt C's specifics** ("eleven minutes", a permission failure),
  imported into the pre-commit box as if they were the prompt's — and they pre-empted Verdict C's central charge.
  **New sub-rule: the box's examples are drawn from the prompt only. An attempt's figure entering the box is worse
  than one entering a verdict, because the pre-commit reader cannot know whose it is.**
- The provenance figure lost its partitive (`Three postings` → `Three of the postings`), matching #3 and #4.

**Verdict openings — a FOURTH form, and the CONTESTED row is now dead even.** All three of #5's verdicts arrived
opening `The judged move is …` — #1's designated house form, applied as a fixed four-word formula three times. At
the gate the form was kept and the formula varied (A keeps it; B opens `B buys the property…`; C opens `The retry
gate turns on…`), so the designation holds without the template cadence. Page tally: #1 move ×3 · #2 letter ×3 ·
· #3 letter ×3 · #4 split 1–1–1 · #5 move ×3 → **pages 2–2 with one split, instances 7–7. Five pages, no
convergence.** New sub-question for the author: if the designation is ratified, ratify it as a **shape** (name the
move before the author), never as a string — an identical opener three times reads as a template, not an assessor.

**`verdict` reservation — NOT working. Third shipping.** "one **verdict** for everybody" in the decision-outcome
sense, after #2 and #3 shipped the same breach and #4 did not. Corrected at the gate (→ "one **decision** for
everybody"; `call` was tried first and rejected — on a page where "call" means *tool call* throughout, "one call"
decodes wrong on first pass). Keep REINFORCED and add the count.

**Numeral register — the row is now four pages behind.** #5's neutral analytical register spells throughout and
carries no figure above ~100, so it evidences only the magnitude rule's lower half — a fourth consecutive page
contradicting the row's literal "uses digits". Its three probes spell every count (one digit ordinal, `the 4th`,
was struck), so spoken-register spelling-out is **4–1** with #1 the sole outlier. **And the mirroring rule is
untestable on this page:** all three attempts share one magnitude register, so "A and C spell, B digitises" has
nothing to discriminate. The row's evidence base is #1–#2 and it should say so. Author's to rewrite.

**British spelling — the cleanest page of the five, and the recurring frame-instance split has no exposure here.**
Page-wide: 0 × `artifact`, 0 × `top-k`, 0 × `superstep`, 0 × US `-ize/-yze`. All three attempts came in
British-clean (second time in five, after #3). **And the `licence`/`license` noun–verb split is correct in all
four places** — nouns `the licence question`, `the licence to recover`; verbs `What licenses a retry`,
`Idempotency licenses a retry`. The hardest spelling trap on the page and no pass had to touch it.

**Attempt jurisdiction — ZERO mechanical fixes, and the byte-identity check is now mechanised.** All three attempt
bodies are byte-identical to the authors' originals (sha256 pair per attempt; `scratchpad/attempt-identity.sh`
carves the bodies structurally, by heading and persona line rather than by line number, so it survives frame
edits). **Recommend the script become a standing gate**: it is the only check that proves testimony was not
touched, and it costs one command.

One candidate mechanical fix was **examined and declined**: Attempt B's diagram has `│` at column 41 where the
same run sits at column 40 two rows above. Unlike #3's licensed fix (a `▼` one column off its OWN flow line across
four neighbouring rows), these are **two different descenders** — gate→last-good at col 40, last-good→page at col
41 — so nothing is misaligned against itself. **Ruling: a one-column difference between two independent descenders
is the author's drawing, not a mechanical error.** Recorded because it is the first time the #3 precedent was
tested and found not to apply.

### Jurisdiction note — divergences observed inside #5's attempts, deliberately left standing

1. **Three names for one object** — `LAST GOOD` (A's diagram) · `last-good` (B) · `last-known-good` (C). Stand.
   **The frame instance was the defect, twice**: the frame used two of the three as its own general term six lines
   apart. Fifth page, fifth time this split lands in the frame (`top-k` #1, `artifact` #2, `superstep` #3,
   `artifacts` #4). Normalised to the house form below.
2. **Three vocabularies for error classification** — `9-code taxonomy`/`the code` (A) · `typed errors` (B) ·
   `error class` (C). Stand. The frame adopting C's `error class` was the defect → `the kind of failure`.
3. **Three diagram grammars** — A box-drawing `▼ ┬ ► ─`; B ASCII `^ v ──> │`; C `v | ──>`. Stand, and the page's
   clearest evidence of independent authorship. One ASCII diagram each, unprompted, **fifth page running**.
4. **Different failing job numbers** — A's "job 23" against B's and C's "Job 22". Stand; the frame reproduces each
   faithfully.
5. **Numeral divergence** — `sixty calls a minute` (A) · `50/min … against the vendor's 60` (B) ·
   `sixty-per-minute` (C); `as_of` in B's diagram against `as-of` in B's prose; `idempotent` (A) against
   `idempotence` (B); 14-day band (A) against 28-day (B, C). Stand.
6. **Attempt-internal errors NO verdict prices — reported to the assessor, not edited.** B's `roughly €600/month`
   does not follow from its own `around €40` × 13 nights = €520 (€600 needs ~15 nights), and B's
   "Cheaper than one rebuild every fortnight" is a wash — a fortnightly rebuild is 2.17 × €280 ≈ €607. That
   arithmetic, not the €38 the verdict does flag, is what carries B's affordability case. C states its retry
   ceiling three ways: `three repair attempts per job`, diagram `retry (≤2)`, and "Retry any overwrite job,
   twice". A's `forty tool calls` sits against A's own `120 tool calls` budget.
7. **Convergent moves, prompt-driven rather than persona-driven — for the pipeline owner.** All three put error
   normalisation **inside the MCP server rather than in the model**; all three use submit-then-poll query handles;
   all three set a hard pre-06:00 clock (05:40 / 05:15 / 05:20); A and B both pick a 50-against-60 token bucket;
   A and C both budget exactly 120 tool calls. **Two blind agents landing on the same round number twice, and all
   three landing on the same four mechanisms, points at the prompt, not the personas.**
8. **A fourth tell class: the antithesis as a paragraph-closing device.** `X, not Y` / `X rather than Y` appears
   ~12 times inside the attempts (A 4, B 2, C 6), with C closing four consecutive paragraphs on it and using
   ordinal signposts (`First action… Second action… Third,`). A and B also share a near-verbatim cleft — A's
   "That single choice is what keeps the night at…" against B's "That single fact is what forces a human into
   every recovery." This is #3's construction-convergence tell recurring on a different construction.
   **The frame caught the same tic** (18 instances before the gate) — which is evidence the prompt teaches it.
9. **Bolded-declarative paragraph openings** 13% / 30% / 30% (A/B/C) and em-dashes 9/9/5, both improving on #3.

### New terms — ON PROBATION (coined in this batch; the pass that proposed them may not settle them)

| term | working sense |
|---|---|
| **last-known-good** | the previous run's published output, served when tonight's cannot be. **House form, hyphenated** — 0 corpus occurrences, and the three attempts supply three forms. **Rule: where three attempts name one object three ways and no form is prompt-anchored, the frame picks ONE and quotes the others.** |
| **staleness marker** | the frame's general noun for A's "stale flag", B's "as-of" and C's "staleness timestamp". Plain, self-glossing via the three quoted variants that follow it — the compliant way to generalise across attempts. |
| **the kind of failure** | the frame's general term for the axis C calls `error class`. Prefer the box's own word (`failure`) over any attempt's. **This is the replacement term the `exception type` row's lesson demands: a prohibition with no replacement gets overridden by the next author who needs the concept.** |
| **the licence question** | the frame's name for what the prompt's closing line asks. Self-glossed in place, prompt-anchored. Reusable. |
| **the give-up path** | what the system publishes when it stops trying (`If they push`). Coined in the frame's own voice **outside the reveal**, so it was glossed in place at the gate — a bare coinage on the always-visible path is the same class as a by-term reveal breach. |
| **a three-state publish record** | the frame's plain rendering of C's `manifest`. `manifest` is C's word for C's own artefact and is legal inside C's verdict, but two naive readers could not decode it cold — **when an attempt's artefact noun is itself undefined, the verdict names the object plainly instead of inheriting it.** |
| **replayability** | Attempt C's `replayable` nominalised. 0 corpus occurrences, 0 in any attempt. Legal inside Verdict C as C's own criterion **once quoted at first use** (which #5 now does: `one word of C's own — "replayable"`); in the frame's general voice use the box's `idempotent` or plain words. It is also a **second name for the property the box defines**, so the `replay` sense card gains this split. |

### Sense card: `state` — a FIFTH sense, ON PROBATION

Scenario #5 adds **publication state**: what a consumer is served tonight — fresh, stale last-known-good, or withheld
("names a channel, not a state, and the question asked for a state"; "a new state, not a sharper check"). On #5
this is the *only* sense in the frame and it does not slip. Card now reads: **durable** · **graph** · **case** ·
**state-machine** · **publication**. **Ask:** *does this survive a restart, is it what the running graph holds, is
it derived from events, is it the phase the workflow is in — or is it what a consumer is served tonight?*

### Sense card: `contract` (two senses on one page) — ON PROBATION

**the policy object** — a per-job or per-consumer set of pre-registered checks; all three attempts' word, so
naming it inside a sentence about that attempt is description, not adoption · **the migration step** — the third
move of `expand → migrate → contract`, the destination lesson's vocabulary inside a `Read next` gloss, exempt
under the ruled link-gloss scoping. **Ask: is this a set of checks, or the last step of a migration?** No defect
on #5 — the arrow notation disambiguates and the pre-commit reader meets only the migration sense. Recorded because
the two sit ~50 lines apart and a later pass could "harmonise" them. **Residual for the author:** two naive readers
wanted the *policy* sense glossed once in the frame, since the frame's `deterministic gate` heading rests on it.

### Terms reused from sibling ledgers — new row (peek-verified, sense matches)

| term | source | sense |
|---|---|---|
| **deterministic gate** | `docs-ai-sdlc/glossary.md` L146 ("Deterministic vs semantic gate"); `part-4-platform/environments-migrations-data.md` L114; `part-3-verification/layered-gates/index.md` L80 | a check that is reproducible and cannot be argued with. Corpus vocabulary, 6 occurrences in 3 files — reuse, not a coinage, and it is the vocabulary of the lesson #5's own `Read next` links. Used in a disagreement heading and in the frame's own voice: the model case of a frame term needing no attempt and no quotation |

### Figures — scenario #5 (frame only) — ALL ON PROBATION

Eight coined figures in a ~2,300-word frame (against #2's four and #3's ten). **Budget: IN BAND, no stacking
defect, and the money family is spent correctly — one sustained domain rather than three competing ones.**

- **"Idempotency licenses a retry but never motivates one"** (`The principle`) — the controlling image, built on
  the box's own two axes. Survives a literal reading *and* the numbers being wrong. The strongest principle
  sentence of the five, and the one line three independent cold readers named as the page's best.
- **"What A buys is real, though."** (Verdict A) — the **buy** family. `The buy` as a bare countable noun was the
  shipped form and was struck: two naive readers met it as a coinage nine lines before the page seeds the idiom.
- **"Two costs."** (Verdict B) — the elliptical count-sentence, **third page running** (see the pattern below).
- **"One property bought once, instead of a human in every recovery"** (Verdict B) — the clearest **buy**-family
  antithesis yet. Replaced "instead of forty exceptions maintained forever", which was falsifiable: the scenario
  has **one** exception.
- **"A feed that arrives complete and carries wrong numbers passes green"** (Verdict B) — `green` as a gate verdict
  is corpus vocabulary, so reuse. Reworded from C's own seven-word phrase, which Verdict B had used unquoted forty
  lines before the reader meets C.
- **"the page's strongest answer to *unmarked*"** (Verdict C) — the prompt's own word italicised as the criterion,
  and now anchored in the box before the reveal.
- **"the chain freezes until somebody answers"** (disagreement 2).
- **"one decision for everybody"** (disagreement 4).

**The `buy` family is fully compliant, one sense each:** `buy/buys` for what an approach gains, `costs/pays/paid`
for what it pays. **No verb carries two figurative senses** — `collapses`, the #3 defect, does not appear.

**Attribution warning for the next reviewer — these live INSIDE attempts.** Testimony: not the page's figures, not
canon material, not counted against the frame's budget. A: "a night operator with a fixed allowance", "the line I
don't move", "publishing a hole", "a two-minute decision, not an investigation", "the win worth having". B: "the
fifteen-minute client timeout stops being a trap", "two queries billing in parallel with one orphaned", "how you
turn a bad night into an invoice", "An instruction in a prompt is not a rate limit", "Nobody's phone makes a
sound", "three engineers sleeping badly", "the deal I'd sign". C: "not a wall", "the sharpest edge here", "sends
someone to a dead post", "the clock is what makes it publish something", "a defect rather than an incident".

### Quoting mechanics — three additions, forced by #5

- **The quoted string must EXIST in the source.** Verify every frame quotation by fragment-match (splitting on
  `…`) before shipping. #5 shipped `"may not touch the appending job until it's converted"`, which Attempt B does
  not contain — the frame had spliced B's bolded label `**What it may not:**` to the clause after it. **A
  five-second automated check that has now caught something on two consecutive pages.**
- **Adding emphasis is the same class as adding a comma — italics included.** #5 italicised *and* inside a
  quotation of Attempt A. The existing row named bold; it now names both. Correct handling: put the emphasis in
  the frame's own voice outside the marks ("A requires both conditions at once: …").
- **An ASCII diagram is quoted by cell, never by reconstruction.** #5 reflowed A's box diagram into an inline
  quotation and **interpolated a `→` the diagram does not have at that point**. Ruling: joining adjacent cells
  *within one box* is a faithful linearisation and is permitted **when attributed to the diagram**
  ("A's diagram shows…"); interpolating a connector glyph is not, and a truncation still takes an ellipsis.
  **New class, ON PROBATION — no earlier page quoted a diagram.**

### The reveal boundary — one scoping ruling, ON PROBATION

**Ordinary vocabulary in a spoken hypothetical is not a by-term breach.** #5's probe says "the budget is gone"
where neither the prompt nor the box defines a budget (all three attempts set one, inside the reveal). Ruled
**compliant**: the probe posits a property of *the reader's own* design, so nothing dangles for a reveal-skipper.
The rule targets a term the frame **relies on for its own argument** whose definition lives inside the reveal —
contrast the real breaches, `memory tiers` (#4) and **`staging-then-swap` + "both … answers"** (#5, `Read next`),
which name an attempt's mechanism and count attempts a reveal-skipper has not met.

**Corollary from #5: a coinage the frame introduces in its OWN voice outside the reveal must be glossed in place.**
`the give-up path` was coined and used once, on the always-visible path, and rescued only by the following
sentence. Same reader cost as a by-term breach, different cause.

## Scenario #9 — `where-the-knowledge-lives`, opening the **lead & client-facing** track (Gate 4 + Gate 5, 2026-08-03)

**First page of a second track, and the ledger is four pages behind.** #6 `guardrails-at-the-boundary`,
#7 `observing-a-non-deterministic-system` and #8 `when-not-to-build-an-agent` shipped unledgered; this section
records only what a #9 pass could verify about them in passing. Two of those observations bear on live
CONTESTED rows and are folded in below — the verdict-opening count and the tier-label fork.

**Tier labels — #9 restores them, and #6–#8 did not carry them.** #6 shipped `the layered answer` /
`the provable answer` / `the minimal-authority answer`, #7 `the purchased-instrument` / `the borrowed-label` /
`the outside-in answer`, #8 `the diagnostic` / `the plumbing-first` / `the hours-back answer`. #9 is
`common` / `strong` / `over-built`, byte-exact. **The label row (SETTLED) is therefore forked on three of the
four unledgered pages and honoured on the ninth — the author must rule on whether the three labels are the
course's taxonomy or a default a page may replace.** Recorded because a Gate 5 that only reads its own page
cannot see a settled row dissolving one page at a time.

**Block strings — 12 of 13 byte-exact, and the one miss was a REGRESSION, not drift.** #9 reproduces exactly:
the three attempt headings and tier labels, the commit line and its second sentence, both frontmatter comment
lines, the inherited `<Reveal>` control, `Where they actually disagree`, the disagreement lead through
`…the exception:`, `The principle`, `Read next`, `If they push`, the follow-up lead (indefinite article and
`three` intact, matching three blockquotes), the `<Verdict>` form with blank lines inside all six tags, and the
persona furniture.

**The miss, FIXED at this gate: the provenance paragraph had reverted to the retired `rubric` form.** #3–#8 —
six consecutive pages, verified byte-exact this pass — carry `none saw the scoring standard the verdicts are
written against — that was fixed before any attempt existed, and a separate assessor applies it.` #9 first
shipped `none saw the rubric the verdicts are written against: an interviewer wrote that rubric before any
attempt existed and never read the answers`, and added `, given` and `and nothing else` to the preceding
sentence. All three of #9's attempts use `rubric` in the *grading* sense inside the reveal, which is the exact
ambiguity the retired scoped amendment was written for. The six-page incumbent was restored. **The clause's
tail stays `the page says so` (#8's variant, 1 of 6) rather than `the verdict under that attempt says so`
(5 of 6): on #9 the unchecked figures are priced in `Where they actually disagree`, not in a verdict, so the
majority string would be false here.** An evidenced deviation, not drift.

**Lesson: a clause the ledger records as superseded comes back unless `_scenario-template.md` carries the
current string.** Same mechanism as the `Why this question` recurrence, one row over — and the same fix.

**Persona-line capitalisation — a silent convention, now recorded.** All 24 sibling instances capitalise the
first word after `*Persona given to the agent: `. #9 shipped all three lowercase and was corrected at the gate.
The line is **frame furniture, not testimony** — reproduce it, never reword it, and capitalise it.

### The reveal boundary — the bare attempt letter, RULED

**#9 was the first page in nine to put bare attempt letters outside the reveal, and it did it nine times.** A
sweep of all eight siblings returns **zero** instances after `</Reveal>`; every `A`/`B`/`C` there is a
sentence-initial article. The rule is explicit (*"a bare attempt letter … dangles"*), and **the link-gloss
scoping exemption does not reach it**: that exemption is justified by *destination-ownership* of a **term**,
and an attempt letter is this page's internal index, owned by nobody outside the reveal.

**The aggravation is the real finding: `Read next` and `If they push` had become a summary of the reveal.**
Bullet 1 announced *"the two criteria the eliminations on this page rest on"* (a bullet may name the
destination's position, never this page's); bullet 3 reported what one attempt priced and what none did; probe
2 delivered a three-sentence account of all three attempts **including an unattributed quotation of Attempt B**.

**Rule, stated so #10 cannot miss it: the sections rendering outside the reveal are written for a reader who
will never open it. They may name the question, the prompt's facts and the destination's teaching, and nothing
else. Not a letter, not a count of attempts, not a quotation, not a verdict.**

**Two by-term breaches inside the same zone**, both the `memory tiers` (#4) / `staging-then-swap` (#5) class:
`entitlement` and `the entitlement table` (A's and C's word; the prompt grants the access rule but never the
noun, and no attempt writes *table* — the `fold projection` welding defect), and **`rerank depth`, Attempt A's
exact phrase used unquoted**. Replaced with prompt-anchored wording (`who may read what`, `how deep the ranking
pass goes`).

### `Why this question` — clean on every barred item, and a NEW failure axis

Clean: no tier label in any polarity, no fourth tier, nothing about who gets it right, the trap described
agentlessly (*"which method is the wrong thing to ask a lead"*), no attempt's specifics imported, no claim
about interviews sat, no provenance figure (checking #6–#8 confirms that figure is **not** a fixture — only #5
among the four recent pages carries one). Third consecutive page clean on the rewritten-template axis.

**New axis 1 — the box may not forecast a finding the verdicts do not deliver.** #9's box closed on *"It is
where the ordering either survives contact or turns out to have been a preference."* Checked against all three:
Verdict A never discusses A's director section; Verdict B convicts B's for mislabelling its own best number, an
economics inversion, with the ordering intact; Verdict C convicts C's for naming subsystems by component to a
man who does not read code. **Zero of three orderings turn out to have been a preference.** The sentence is
uncheckable in both directions — a reader who finishes and comes back can neither confirm nor falsify it.
Aggravating: `preference` is a move two attempts make *inside* the reveal (B: *"not a quality preference, it's
an admissibility rule"*; C: *"That is not a preference, it is per-customer NDA"*), so the box performed their
rhetorical move for them pre-commit. Replaced with a prompt-anchored statement of what is asked: *"It asks for
the same decision a second time, to someone who does not read code and has already heard a simpler story."*
**The existing rule says the box is checked against the verdicts for CONTRADICTION; this extends it to
NON-DELIVERY — a box claim no verdict supports is the same defect wearing the other polarity.**

**New axis 2 — where the frame states the page's axis set more than once, the lists are checked against each
other for MEMBERSHIP and NAMING.** #9's box listed five properties; the lead-in twenty lines above listed four,
dropped the one Verdict A calls *"the load-bearing call"* (volatility), and renamed another (`what a usable
answer has to carry` against the box's `an admissible answer` and `The principle`'s `what makes an answer
admissible`). A pre-commit reader meets both and is taught the axis set wrong before a single attempt is read.
**Carve-out, so #10 does not over-apply this:** the two lists may legitimately NAME one axis differently when
the lead-in glosses in plain language what the box then names compactly — #9 ships `how fast the material
underneath it goes out of date` (lead-in) against `volatility` (box), which is gloss-then-term, the correct
pedagogical order. What the rule bars is two lists that DISAGREE on membership, or that name one axis two ways
with neither introducing the other.
**And the lead-in additionally reproduced `The principle`'s three-item triple in the principle's own order, two
of three verbatim** — the list was spent before the reader committed, even though the rule was not. Fixed by
scrambling the lead-in's order, matching membership to the box, and adopting `admissible`. Kin to the `persists`
(#4) and `idempotent` (#5) findings: a box that is *present and confident* while quietly disagreeing with the
page is harder to see than an absent one.

**The track overview is a pre-commit surface too, and it leaked worse than the box did.**
`lead-and-client-facing/overview.md` described the track — a track with one page in it — as turning on
*"whether the elimination was computed from the numbers on the table or merely asserted with conviction"*: that
is `The principle`'s clause (ii) near-verbatim **and** Verdict A's conviction, delivered before the H1. Cut.
**Rule: a track overview naming one scenario is describing that scenario. It gets the pre-reveal sweep.**

### The cold read earned its place on #9 — three findings the main gate missed, one class each

The main batch cleared this page. A blind adversarial reader then falsified three things, and **two of the
three were defects the main gate's own fixes had introduced.** Recorded because it is the strongest evidence
yet for the mandatory cold read.

1. **A prompt-count the frame invented, in the paragraph whose job is to restate the prompt.** The lead-in
   said dealers work `on nineteen different contracts`; the prompt says only `contracts that differ from one
   another`. All three attempts infer 19, and the frame took the number from them and put it eleven lines
   above the blockquote that contradicts it. **Rule: the lead-in restates the prompt and nothing else — every
   figure in it is grepped against the blockquote, and a number all three attempts share is exactly the one
   most likely to have leaked upward.**
2. **The frame hardened an attempt's hedge, then graded and priced it for the hardened version.** A wrote that
   the dossier tier `probably wants to run against a model you host`; the frame wrote `A stands up a second,
   self-hosted model tier` and entered it as one of three flat, incompatible positions. **Rule: a hedge is
   part of the claim. Restating a "probably" as a commitment is the same defect class as sharpening a
   comparative — it manufactures the thing being judged.**
3. **`by name` was true of one attempt and false of the other it was applied to.** `A and C then put an
   in-house component inside the €260,000 by name — a self-hosted tier, an in-house path for dossiers`: C
   wrote `the in-house path for dossiers` verbatim; A wrote only `the hosted tier`, which in a design whose
   general tier runs on a *vendor*-hosted model does not name an in-house component at all. Verdict A had
   made the same silent substitution one screen earlier, rendering A's `the hosted tier` as `a self-hosted
   tier` **outside the quotation marks it had just closed**. Both quote A's own words now. **Rule: when the
   frame paraphrases an attempt just outside a quotation, the paraphrase is checked as if it were inside it.
   A disambiguation that runs in the direction the frame's own claim needs is the tell.**

**And two defects the gate's own fixes introduced, in sentences the gate itself wrote:** `the one place
"under a second" turns up at all is B` (false — the phrase is in the prompt too; → `the one attempt it turns
up in at all is B`), and `the documentation changes forty times a month`, which corrected Attempt A's slip
*in the frame's own voice* and thereby still owned it (→ attributed: `the corpus changes forty times a month,
it says`). **A fix is a new claim and gets the same check the original did.**

### New terms — ON PROBATION (coined in this batch; the pass that proposed them may not settle them)

| term | working sense |
|---|---|
| **criterion** (not `constraint`) | the frame's house noun for one test in the ordering — 8 frame occurrences against 0 in the frame's own voice for `constraint` (its three instances quote A and C). The prompt's word is `criteria`, which is why it wins. **The frontmatter `description` shipped `constraint` and was the only surface out of step; corrected.** |
| **admissible** / **admissibility** | the frame's house term for what an answer must carry to be usable at all. It is Attempt B's word (`it's an admissibility rule`), adopted as the frame's general term — legal under the pick-one rule (`last-known-good`, #5), which is what a page does when three attempts name one property three ways (B `admissibility`, C `what makes an answer usable at all`, A `the answer contract`) and the prompt names it not at all. |
| **masking boundary** | the frame's name for the substitute-then-rehydrate mechanism. **Not a coinage — corpus vocabulary:** `docs/glossary.md` L393, *"Reversible vs irreversible masking"*, plus 10 occurrences in `part-1-rag/cross-cutting/guardrails/deep-dive.md`. Needs no gloss. Cited here so no later pass re-opens it. |
| **supersession** | the nominalisation of the prompt's own verb, and all three attempts' word. Prompt-anchored, so legal outside the reveal. **Its antonym trap is the finding: the lead-in shipped `cancel`, which asserts invalidation and contradicts the page's own credited move (B's `superseded does not mean deleted`). One word, chosen for variety, denying an argument the verdicts turn on.** |
| **long context / long-context** | noun open, attributive hyphenated — `_language.md` §3's `KV cache` / `KV-cache` split, applied to a term the ledger had not carded. **Positive precedent; the page gets it right in all three places.** |
| **fine-tune / fine-tuning** | the frame's term for the model operation. **Reserve it: bare `tuning` is the ATTEMPTS' word for the ordering sense** (`everything downstream is then a tuning question`, `those are tuning parameters`, `Cost and model choice are tuning`) — and #9's Verdict A quotes that sense while `If they push` made the other sense the subject of a whole probe, ~290 lines apart. Corrected to `fine-tune` throughout the frame. **The `collapses` rule (#3) generalises past figurative verbs: a TERM-OF-ART also gets one sense per page, and the frame gives the second sense back to the attempts.** The destination lesson writes `Fine-tuned / custom model`, which settles the form. |
| **the existing search** | the frame's noun for the full-text bulletin search already in the building. #9 first shipped `the incumbent`, a bare definite whose referent is not identified for sixteen screens; corrected. **A bare definite in a verdict must resolve inside that verdict.** |

### Rulings carried this run

- **`B's is the strongest of the three` — COMPLIANT, and the superlative row is EXTENDED to positive
  polarity.** It is the exact mirror of the accepted softening `A's is the weakest of the three here`, carries
  no contest metaphor, and states its ground in the same sentence. Recorded so #10 does not relitigate it.
- **`it both wins and breaks there` (Verdict A) — KEPT, and the scoreboard row is SCOPED.** The row's struck
  examples (`C wins this one outright`, `A's is the losing position`) are all *cross-attempt rankings*. Here
  `wins` means one filter succeeded, within one attempt, and the next two sentences are built on it (`It wins
  by…` / `It breaks by…`). **The ruling binds the sense, not the string: the bar is on ranking attempts against
  each other, not on the verb.**
- **`Someone who has been paged for this says which percentile they mean…` — STRUCK** (anti-coach). The
  participial shape is house form, but the approved instances state a property of the ANSWER; this states a
  property of a population defined by BIOGRAPHY, which is the credential half of the rule. → `The trade stays
  unnamed until the answer says which percentile it means and what it would spend to move it.`
- **`the candidate` — a REJECTED ROW shipping again**, in the one section written about the reader. Replaced,
  and the sentence's by-position pointer into the reveal went with it.
- **`buys` family, one sense per page — VIOLATED and fixed.** `A's buys a second model to run and keep
  current` used the family for a COST on a page whose other `buy` (probe 2, *what does that buy him*) is
  correctly a gain. → `A's pays for a second model`.

### Numeral register — a third register appears, and the row is now five pages behind

#9's `If they push` spells throughout (one prompt-quoted `19`), so spoken-register spelling-out is **5–1** with
#1 the sole outlier. Its neutral analytical register applies the **magnitude** rule (spells below ~1,000,
digits above), a fifth consecutive page contradicting the row's literal *"uses digits"*. **New: the verdicts
introduce an abbreviated register** — `400M`, `1M`, `300k`, `6–10k`, `12k+800`, `30–50×` — where the attempts
they judge spell the same figures out. Abbreviation is precedented in the frame (`~3×` in a #6 verdict, `4×` in
a #7 verdict, `$180k` in #1's prompt), so this is not a fork; but **it contradicts the mirroring rule
directly**, and the row now describes none of the three registers the course actually uses. **Left untouched at
this gate — CONTESTED, author's to rewrite.** One internal collision left standing for the same reason: the
lead-in's `600 of the 910 work for nineteen dealer companies` mixes digits and spelling in one clause.

### Verdict openings — the count has moved decisively against the designated house form

#9 opens all three on the move (#1's form). Classifying the unledgered pages: #6, #7 and #8 open all three on
the letter. Running tally: **move — #1, #5, #9 (3 pages / 9 instances); letter — #2, #3, #6, #7, #8 (5 pages /
15 instances); split — #4.** Nine pages, no convergence, and the ledger's "2–2, 7–7" is stale. #5's
sub-question is what #9 answers well and should be recorded: **ratify the designation as a SHAPE (name the move
before the author), never as a string** — #9's three openers vary their syntax while keeping the move first.
**Still CONTESTED for the author.**

### Disagreement section — shape clean, length still compounding

**Forked 0 of 5, the first clean arrival since the shape was settled** (#3 0/4, #4 0/5, #5 1/4). Four items in
`Topic: A or B` plus the shared-assumption closer, correctly flagged in the lead and correctly not promoted to
a fifth `##`. All five pass the shuffle test read cold. **Third confirmation of the template mechanism: a rule
that ships into `_scenario-template.md` stops being forked.**

**Length — CONTESTED, nine pages, no trend.** Non-blank lines / words between the H2 and the next H2, one
method: #1 14/202 · #2 40/639 · #3 44/686 · #4 66/1,158 · #5 42/704 · #6 55/908 · #7 60/1,007 · #8 73/1,239 ·
**#9 69/1,159, or ~1.15× its own mean attempt.** Second-heaviest of nine, again exceeding its own attempts,
inside the reveal, in front of `The principle`. **Correction to a recorded measurement:** the #5 row records
34/533; under the method that reproduces #1–#4 byte-exactly #5 now measures 42/704 — the file changed under
commit `fceb567` after the gate. **A measurement in this ledger dates from the moment it was taken; re-measure
before citing, do not quote the row.**

### `The principle` — length is now a checkable property

#9 first shipped a **79-word** single sentence. Measured against the eight siblings — 22 / 22 / 24 / 28 / 28 /
30 / 34 / 42 / 51 words, mean 32 — that is 1.5× the longest and 2.5× the mean, and its third and fourth clauses
stated the same claim twice, once abstractly and once operationally. Cut to 57 by dropping the abstract
restatement only. **Recorded as a soft bound: one sentence, and if it runs past ~50 words it is usually saying
the same thing twice.** The surviving image — *"name the price or volume the computation assumed, because that
is the number whose change reopens the option you just closed"* — passes both accumulated tests: it survives a
literal reading, and it survives the specific numbers being wrong *because the numbers being wrong is its
subject*.

### Bold budget

Frame **3 spans / 231 non-blank frame lines = 0.013** against the ~0.36 cap (frontmatter, fenced blocks, blank
lines, attempt ranges and persona lines excluded; `**` paired across line breaks). Fourth data point on the
**under-use** trend, and the box again defines the page's controlling idea with zero anchors. Under the cap, so
not a defect — but the trend is now four pages old and one of the three surviving spans (`**named customer's**`,
Verdict C) is intonation rather than navigation, kept because it is the word the whole criticism turns on.

### Figures — scenario #9 (frame only) — ALL ON PROBATION

Roughly fifteen coined figures in a ~3,200-word frame (against #5's eight in ~2,300 and #3's ten): at the top of
the band, no systematic stacking, one family spent correctly.

- **"the number whose change reopens the option you just closed"** (`The principle`) — the controlling image.
- **"it leaves itself a second leg"** / **"survives losing the first"** / **"rests on one leg only"** (Verdict
  B, Verdict C, `Where they actually disagree`) — **one sustained figure across three sections, one sense,
  carrying the page's central distinction between a computed elimination and an asserted one.** The clearest
  instance yet of the #4 accounting-figure precedent: one domain sustained beats three competing ones.
- **"an assertion, unlike a wrong computation, leaves nothing to check"** (Verdict A) — plain and reusable.
- **"It dissolves the scenario's sharpest tension rather than resolving it: no model, no surface to defend"**
  (Verdict B) — dissolve-against-resolve, one domain.
- **"A criterion with a branch attached, not a consideration"** (Verdict A).
- **"hands the director the wrong label on its own best number"** (Verdict B).
- **"Half the policy is unhandled inside a sentence declaring both constraints satisfied"** (Verdict C).
- **"C hardens its figure into an exclusion and has nothing behind it"**.
- **"One collision, three incompatible answers."** — the elliptical count-sentence, **fourth page running**
  ("Then the bill." #2, "Two cracks." #4, "Two costs." #5). **Promote it to a recorded device or strike it; at
  four pages it is a house cadence, not a coinage, and reviewers keep re-testing it.**
- **"They foreclose each other's surfaces"** — foreclosure over attack-surface; mild stacking, kept because
  `surface` is consistent with the page's own *"no surface to defend"*.

**Attribution warning for the next reviewer — these live INSIDE attempts.** Testimony: not the page's figures,
not canon material, not counted against the frame's budget. A: "permissions are not a feature on top of the
assistant", "a post-filter still means the model saw it", "training bakes knowledge in, we need it looking
knowledge up", "the failure you already bought once", "Two tiers, one interface". B: "treat collection three as
contaminated until proven otherwise", "after training there are no sentences, only weights", "the dossiers are
not a corpus at all … that's a table", "it isn't a model result, it's a measurement failure", "he hears that in
December, not in March". C: "weights have no access-control list", "This one criterion does most of the
demolition", "the one wrong answer that reaches a guarded area", "the parts that look deferrable are the ones
that cannot be retrofitted".

### Structural reconciliations forced by a second track (Gate 4)

Opening a track touches four surfaces outside the scenario, and three of them were stale. **Record this as the
checklist a #10 in a NEW track runs:**

1. **`intro.md`'s `:::note[Status]`** said *"Eight scenarios, one archetype"* and *"Whether a second archetype
   follows is being decided."* — while the sidebar already showed two. Reconciled.
2. **`intro.md`'s "Where the questions come from"** said *"The first track is **agentic workflows**"* and named
   no second. Reconciled.
3. **`docusaurus.config.ts` `footerLinks`** omitted the new track. The type's own comment makes this mandatory
   — *"the footer is the only always-visible navigation on phones, so a gap here is a gap for most readers."*
   Added, with the label taken verbatim from `_category_.json`.
4. **The `live:` comment above the COURSES entry** still described one archetype. Updated. (A stale
   *"Currently moot because `inNavbar` is false"* comment, left over from the go-live flip, was corrected in
   passing.)

**Locale scope — RULED, and it needs nothing.** The course declares `locales: ['en']`, so
`scripts/locale-parity-check.sh` and `scripts/i18n-link-check.sh` both scope themselves off that declaration
and never check `docs-design-scenarios/` against `ru`/`sk`/`de`. There is no
`i18n/<loc>/docusaurus-plugin-content-docs-design-scenarios/` tree in any locale, so **there is no
`current.json` for a localized category label to live in, and none must be created** — a non-English locale
renders the EN `_category_.json` label verbatim, which is correct. The one localized surface, the landing-card
blurb, counts no scenarios and names no track, so a new track requires no re-translation.

**Adjacent finding for the author, pre-existing:** the three localized landing blurbs hard-code the tier casting
(RU «привычный, сильный и избыточный»; SK "bežná, silná a predimenzovaná"; DE "die gängige Antwort, die starke
und die überdimensionierte") where the EN source deliberately does not — `intro.md` documents that some pages
cast by *position* instead. Still accurate for #9, but the cards over-promise a uniformity the course does not
have.

### Jurisdiction note — divergences observed inside #9's attempts, deliberately left standing

**No frame instance of any of these exists, so — for the first time in the series — there was no frame-side
correction to make.**

1. **Attempt A: bare `k` for top-K** — *"The exact **k**, chunk size, and rerank depth I'd settle empirically"*.
   `_language.md` §3 fixes `top-K`. Stands. **And for the first time the split has no frame instance to
   correct** — the frame writes "how deep the ranking pass goes", never `k`. (#1 `top-k`, #2 `artifact`,
   #3 `superstep`, #4 `artifacts`, #5 `last-good` were all frame defects.)
2. **Three registers for one figure.** A writes *"Four hundred million tokens"* and *"a factor of four
   hundred"*; B and C write their sums in digits; A alone spells `forty times a month` where B and C write
   `40 bulletins a month`. Stand.
3. **Three vocabularies for one object.** Who may read what: A `entitlements` / `confidentiality class`; B *(no
   noun — describes the policy)*; C `the entitlement model`. The dossier path: A `two model tiers`; B `a
   structured store` / `a table`; C `two paths` / `placeholders` + `rehydrated`. Stand — **the page's best
   evidence of genuine independence: three answers to one collision with no shared noun.**
4. **A's `ours change forty times a month`, said of manuals.** The prompt's 40/month is new *bulletins*. A's own
   slip. Stands — but the frame had restated it unquoted, adopting the error in the page's own voice; the frame
   instance was corrected to `the documentation changes forty times a month`. **`Assess, never endorse` catches
   an attempt's factual slip as well as its claims.**
5. **B's `€0.037 a question`** — 12,000 × €2.40/M + 800 × €9.60/M = €0.03648, which rounds to €0.036. A 1.4%
   over-round, downstream-harmless (€16k/year is right either way). Stands; Verdict B's `internally consistent`
   hedge survives it.
6. **C's `about six cents a question all-in — call it €27,000 a year`** — €0.06 × 432,000 = €25,920. Reaching
   €27,000 needs ~1,510 output tokens C never states. Stands. **But Verdict C's blanket `The arithmetic
   recomputes.` did not** — it was narrowed to `The elimination arithmetic recomputes.`, and the disagreement
   section's `The computations that exist recompute correctly` to `The eliminations recompute correctly`, and
   `C's €27,000 a year is its 20,000-token window multiplied out and nothing else` (arithmetically false —
   20,000 × €2.40/M × 432,000 = €20,736) to `rests entirely on its own 20,000-token figure`. **A frame sentence
   endorsing an attempt's arithmetic is itself arithmetic, and gets recomputed.**
7. **C's `1,900 customers' process settings`** — the prompt says 1,900 customer *sites*, and only 1,400 lines
   have dossiers. C inflates and re-labels a prompt figure. Stands; the frame wisely drops the number.
8. **All three attempts came in British-clean** — a full US-spelling sweep returns zero hits page-wide, third
   time in nine. The standing warning holds: a mechanical `top-K` sweep would rewrite A's bare `k`.
9. **Zero mechanical errors inside the attempts, and no ASCII diagram** — **the first scenario in nine where
   all three attempts produced prose only.** The one-diagram-each convergence recorded on #3, #4 and #5 does not
   recur. For the pipeline owner: a change in the tell, not a defect.

### AI-tell measurement across the three attempts — REPORTED, NOT FIXED

Run as a dedicated measurement pass, forbidden to edit. Recorded because the ledger's jurisdiction rule says a
tell inside an attempt is a finding for the pipeline owner, and a finding needs a number.

| metric | A | B | C | frame |
|---|---|---|---|---|
| words | 951 | 958 | 940 | 2,175 |
| em dashes / 100 w | 1.37 | 1.04 | 1.49 | 1.33 *(verdicts: **2.40**)* |
| sentence-length SD | 11.7 | 10.3 | **8.8** | 16.8 |
| coefficient of variation | **0.462** | 0.580 | 0.575 | 0.658 |
| max sentence (words) | 46 | 47 | 43 | 114 |
| paragraphs opening on a bolded declarative | **8/8 = 100%** | 9/11 = 82% | 8/23 = 35% | 1/26 = 4% |
| bolded FULL sentences | 6 | 6 | 0 | 1 |
| tricolons / 100 w | 0.74 | 0.42 | 0.53 | 0.55 |
| antithesis family / 100 w | 0.74 | **1.04** | 0.53 | 0.41 |
| hedges / 100 w | 0.21 | 0.42 | **0.74** | 0.74 |
| AI-vocabulary hits | 0 | 0 | 0 | 1 (`Worth noticing:`, since cut) |
| literal "not just X, but Y" | 0 | 0 | 0 | 0 |

**The measurement that most undermines "three separate engineers": B and C share an 18-word verbatim span** —
`a year. One machine family's documentation is 300,000 tokens; at €2.40 per million that is €0.72` — followed
two sentences later by a second shared 8-word span (`is €1.68 a question, €726,000 a year.`), inside a paragraph
where the two agree on ~40 of ~55 content words in the same order, **including the placement of a semicolon**.
Shared *numbers* prove nothing: €0.72, €311k, €1.68 and €726k follow deterministically from prompt figures. The
signal is that they **narrate** the sum identically. Convergent arithmetic is expected; convergent punctuation
is not.

Two supporting convergences, in different pairings and different parts of the page: **A and B compress the
prompt's answer-contract list by deleting the same three words and then pivot on the identical four words
`That's not a`**; **A and C open criterion 1 with the same five words, `who is allowed to see`**, in a slot the
prompt does not supply. And **B and C order their six criteria identically, six for six**, while A — the
*weakest* persona — is the only one that diverges. If persona were driving the output, the two strongest
personas would not be the pair that agrees most.

**Prompt-induced convergence, separated out and NOT counted as a tell:** that there is an ordered criteria list
at all, a "where the chain lands" beat (the prompt supplies the phrase), a March scoping section, a closing
director pitch, and the verb `rules out` — the prompt asks for every one of these. **Not prompt-induced:**
rendering the criteria as bolded ordinal labels in the same lexical family (`First filter:` / `First:` /
`First criterion:`), all three putting confidentiality in slot 1, and all three closing on a short beat about
March after a long paragraph.

**What still distinguishes the three is formatting, not voice.** Sentence-length CVs span only 0.462–0.580 and
paragraph CVs only 0.381–0.403; what separates them reliably is that C uses standalone bold headers, A has no
plain-prose paragraph opening at all, and B alone opens in prose and closes unlabelled. **For the pipeline
owner: the personas are landing in layout, not in rhythm.**

**And one measurement about the frame, worth keeping.** The frame is markedly *less* uniform than the testimony
it judges (SD 16.8 against 8.8–11.7; 4% labelled openings against 35–100%) — but **the verdicts run em dashes at
2.40 per 100 words, 61% above the densest attempt.** The assessor voice is the page's em-dash outlier, not any
candidate.

## Rejected variants (EN)

| rejected | why |
|---|---|
| "a mechanically checkable **artifact**" | US spelling in `The principle`, the page's most-quoted sentence. `_language.md` §3 names **artefact** explicitly; `docs/` is 23× artefact, 0× artifact. `docs-ai-sdlc/`'s `artifact` count is pre-existing drift in a sibling course, not a precedent. |
| "prompt caching, **top-k** from eight to three" (in a verdict) | `_language.md` §3 fixes **top-K** everywhere in prose; corpus 21× / 0×. The verdict inherited the spelling from the attempt it quoted — a verdict is frame and does not inherit an attempt's spelling. |
| "the same **seven parts**, in this order" | `part` is the corpus's book unit (Part I/II/III) and this course deliberately does not use it; the collision lands in the sentence declaring the page's structure. Corpus form: **section**. Separately the enumeration reads as eight, so the count was also wrong — drop the number. |
| "**A weak answer** comes from someone who…" | invents a fourth quality tier. The course taxonomy is common / strong / over-built; a cold reader mapped *common* → *weak* and was then contradicted by Attempt A's own verdict ("the operations are the best-specified of the three"). Describe the failure without naming a tier. |
| "**The theme** invites a tidy answer" | no antecedent — the reader has met a question, not a theme — and a theme cannot invite. Also "The obvious answer is tidy", its first replacement: a cold reader read *the obvious answer* as Attempt A, which then contradicted A's verdict. Scope the criticism to the bare version: "Stated that way it is a design sketch." |
| "**Two rules the page dies on**" | inverts *the hill you die on* (the thing worth fighting for); the intended sense is the opposite, and a page does not die *on* a rule. |
| "the parity gate counts fence languages" (as the reason to fence ASCII as `text`) | **factually backwards, twice.** `scripts/locale_parity.py` *exempts* `text` from its per-language count, and it skips a course that does not claim the locale — Design Scenarios is `locales: ['en']`, so the gate never runs on it. The rule stands; the reason was invented. |
| "`onBrokenLinks` relaxes… CI is not checking these for you" | **false.** `scripts/i18n-link-check.sh` re-fails those warnings for any page that is not an untranslated fallback, so a dead link from this course fails CI today. The true gap is narrower and worth stating: no gate catches a link that resolves and is wrong. |
| "answered three times **by three different engineers**" | claims human authorship the project cannot evidence, and the same page later says the attempts must sound "like three people rather than one machine". Say the count and the independence; not the authorship. |
| "Senior engineers **fail upward** far more often than they fail downward" | two defects: an ungraded population-scale claim, and a false-friend idiom — *fail upward* means *to be promoted despite incompetence*, not *to err toward over-engineering*. The editorial commitment ("gets as much room here as the failure in the other direction") survives without it. |
| "while **the rest of the site** is translated" | **false.** The Field notes blog is English-only by declaration too (no `i18n/**/…-content-blog` tree). Correct form: "The other two courses are translated." |
| "**the pile** reflects what employers keep asking for" | wrong register, and a "pile" connotes unsorted mess in the sentence arguing the set is sorted. |
| "a regulated **data set**" | corpus is 29× `dataset`, 0× `data set`. |
| "which of these **three** defensible options" | forward-pointing count that collides with the three attempts, and two of the three are then judged not defensible. Drop the number. |
| "the other roads were worse, and **the other roads** are where the reasoning lives" | the ROADS figure is coined, doubled for emphasis and never used again, while MACHINERY is the page's controlling image two paragraphs above — two figures for one idea. Say "the alternatives", keep the machinery. |
| "you will agree with **the strong answer**, feel informed, and retain nothing" | names the winner inside the how-to-read section, which undercuts "find out which one you just wrote". "You will nod along" carries the argument without the spoiler. |
| "as much room here as **the failure in the other direction**" | points at a category the page never names — the common answer is described as *wrong in one specific place*, not as under-built. Compare against a category that exists. |
| "**These pages** carry argument…" | no noun *page* appears earlier; and the trailing "which is the hardest kind of prose" binds to the nearest NP rather than to the register. Name it: "Scenario pages… That register is…". |
| the Status note at the **bottom** of the page | every claim about what a scenario contains is present-tense, and a note retracting them arrives only after they have all landed. The note goes **directly under the opening**, where it frames the rest as a format description rather than a shelf of finished pages. |
| "is the one **artifact** that makes every later eval cheap" (in a verdict) | **the already-rejected US spelling, shipped a second time** — see the `The principle` row above. A verdict is frame. Corrected 2026-07-30. |
| "clears **fulfillment** exceptions" (in the prompt) | US spelling; §3 is British, and this was the only `fulfil-` token in the corpus. → **fulfilment**. **The prompt is frame**: an interviewer's spoken register does not suspend the spelling canon. |
| "says whether that **verdict** blocks a release" / "produces **verdicts** at all" | **reservation breach**, on the one page where the word is also a UI label (`The assessor's verdict`). `verdict` is reserved for the assessment of one attempt. → **ruling**, or name what the layer emits. |
| "**Reroute-versus-hold** on a parcel with no fresh scan" | the frame extended the prompt's action space. The prompt grants reroute / split / reprint / credit / escalate — there is no `hold`. `escalate and hold` is Attempt C's phrase and may be *quoted*; a frame claim may not be built on an affordance the prompt does not grant. → `Reroute-versus-escalate`. |
| "C wins this one outright: **it** is buying with money what is arriving for free" | the pronoun's antecedent is the winner; the buyer is the loser. A reader parses the winner's ruling as its own indictment. **Name the party.** |
| "**The interviewer has the attempts in front of them**" | contradicts `how-these-are-made.md` — the interviewer role never sees the answers. Same conflation #356 removed from the `<Verdict>` label; a role's blindness is a fact of the pipeline, not a narrative convenience. |
| "**Memorised answers only ever add layers.**" | ungraded population-scale claim — the "fail upward" defect without the idiom error. Scope it to the answer in front of you. |
| "**a memoriser**" | a coinage, 1 corpus occurrence. The corpus form is participial: "someone who memorised an answer". |
| "and **fatal** to someone who memorised one" | escalated adjective; the template's register is the flatter "defeats a reader who memorised the strongest attempt". |
| "which is also the difference between **a review process that compounds** and one that re-spends the same capacity every week" | a virtue maxim bolted onto a finished sentence, where scenario #1 ends diagnostically. Cut the trailing clause. |
| "I'm not measuring the counterfactual**,** whether a human would have done better" | **a quoted fragment silently repunctuated** — the attempt's em dash became a comma inside quotation marks, and a qualifier was dropped without ellipsis. Canon binds the frame; it does **not** license editing what the frame quotes. Quote byte-exactly or elide with an ellipsis. |
| "**both slogans apply**" | no slogan is stated anywhere on the page — a callback with no referent, in a section that renders outside the reveal. |
| "which is the part of **the answer** already agreed" | there is no singular "the answer" on a three-attempt page, and no agreement was shown to a reader who never opened the reveal. **Anchor a callback in the prompt**, which every reader has seen. |
| "the **1,300** daily escalations" (page's own voice) | 15% of 9,000 is **1,350**. The page adopted Attempt C's own rounding, unquoted and converted to digits, so the page owned the error. C's "thirteen hundred" stays untouched — it is testimony and immaterial to C's argument. **An attempt's unchecked figure never enters the frame unquoted.** |
| "seven and a half **reviewer-weeks**" | 1,500 cases ÷ 200 a week is 7.5 weeks **of a two-person pair**, i.e. 15 person-weeks — the word invited the wrong arithmetic, and Verdict A on the same page named the same resource correctly ("two and a half weeks of the entire two-hundred-a-week review budget"). → "seven and a half weeks of their entire output". `reviewer-weeks` survives only in `The principle`, where it is a generic unit of account and no arithmetic hangs on it. |
| "**B is the only answer that asks what signal already arrives on its own**" | **falsified by Attempt C two screens down** ("that disposition is a label") and by the page's own later section, which awards C that very point. What was unique to B was the *kind* of signal — post-action physical state — not the question. **Every superlative in a verdict is a claim about all three attempts; check it against the other two.** |
| "**C buys three things the others don't.** The replay environment…" | item 1 was not unique: A proposes a "replay harness" and B "300 replayable exceptions with pinned tool responses". What C alone buys is the *contract*. Same class as the row above. |
| "**The over-built answer labels trajectories** a team of four could never label" (in `Why this question`) | C labels correct **actions**, not trajectories — as the page's own subheading said. And the scarce resource is the **two ops reviewers**, not the four engineers. |
| "B says don't trust the agent at all" | **denies a move B makes.** B wrote "I'd eval that as a load-and-degraded-input scenario, **and** I'd hard-cap…". The section dropped the first clause, manufactured a contradiction B does not hold, and built a superlative ("the only one of the three testable before deploy") on the omission. The inverse of scenario #1's failure: denying a move rather than inventing one. |
| "an evaluation is worth **exactly** the signal that already arrives for free **plus the human hours you can actually staff**" | the principle excluded a third category the page had just credited — **assertions checkable without a human** (C's replay contract, C's stale-feed assertion, B's preconditions). A principle must not contradict the verdicts above it. |
| "**anchor set**" | a third name for the same object. Corpus term is **golden set** (`docs/` ×4, scenario #1 ×1). |
| "a **per-class** policy spec" | House term is **exception type** (the prompt's register, and 2 of 3 attempts). `exception class` / `exception taxonomy` are Attempt C's words: convert, or quote them as C's. |
| "the **disposition** is a comparator" (unquoted, page's voice) | `disposition` is Attempt C's coinage. The frame may **quote** an attempt's coinage; it does not adopt it as a house term. **Clarified 2026-07-30 (Gate 5, scenario #3):** the bar is on adopting a coinage as the page's **general term**. Naming *that attempt's own artefact* inside its own verdict is description, not adoption — `the ledger` and `reproduction tuple` for C's objects are legal (and `ledger` is corpus vocabulary anyway: `docs-ai-sdlc/part-3-verification/escape-ledger`). What is illegal is the coinage becoming the frame's word for a general thing. **Prefer quotation at first use either way**, which is what #1's "C's replay contract" did and what #3 now does with "reproduction tuple". |
| "without **golden-path brittleness**" | a compound the page never introduces — C says *golden set* and *golden policy*, never *golden path*. → "without pinning one correct path per case". |
| "What settles it here is staffing, not **epistemics**" | needless erudition for a practitioner audience; nothing on the page needs the word. → "not theory". |
| "the **ordering is decidable**" / "stale-feed **conduct**" | borrowed formal-logic register, and *conduct* is a person-word used of a system. → "the order is clear" / "behaviour on a stale feed". |
| "bounds the loss at **$9 a reroute**" | $9 is the unit price, not a bound — a volume cap bounds *how many*. → "limits how many nine-dollar reroutes a bad hour can spend". |
| "Multi-step agents break **the habit that** final-answer scoring is enough" | a habit is a practice, not a proposition; `the habit that <clause>` is not a construction. → "the habit of treating a score on the final answer as enough". |
| "**What separates people** is what they choose not to measure" | interview-coach register, and it makes the page a judge of persons rather than of answers. → "What the answers separate on is…". |
| "against 63,000." (in `Why this question`) | elided unit on a figure the box asks the reader to compute with. → "against 63,000 a week". |
| "can be bought for $75" (frontmatter `description`) | on the one surface a search-result reader sees, this decodes as *the label is purchasable from a vendor*. → "can be bought off with a $75 credit". |
| "replaying stored **supersteps** returns recorded values without re-invoking anything" (in a verdict) | **two defects in one clause, and the worse one is factual.** Spelling: corpus is 2× `super-step`, 0× `superstep`, and the same page's `Read next` already wrote `super-step` — the `top-k`-in-a-verdict defect a third time. Substance: **wrong about LangGraph.** Replay skips nodes *before* the checkpoint and re-executes everything after it, model calls included. → "a replay is not a record read — everything after the checkpoint it branches from runs again, model calls included". See the framework-claims section. |
| "which is exactly the reconciliation **neither side of the framework argument** settles on its own" | **falsified by Attempt B**, which holds that very reconciliation as an explicit gate ("Condition to adopt: it holds run orchestration only, no durable state"). Named no attempt, so a letter-keyed superlative check passed it. → name B's condition instead. |
| "Three positions, **mutually exclusive**." | retracted by the same item's next paragraph, which shows C reducing to B for the model call. The count of three was right; the modifier was not. → "Three positions." |
| "B and C both: the record is theirs and **the engine is replaceable**" | over-attribution. B says it ("framework-independent"); C adopts LangGraph and calls durability "properties of the substrate". → "the record is theirs and the orchestration sits on top of it". |
| "the adopt-or-decline **verdict**" | **reservation breach, second shipping** (see the `verdict` sense card). → **call**. |
| "**The only person who knows how the current grader behaves** leaves in six weeks" | a frame claim the prompt does not grant, plus backwards causality. The prompt says three engineers own the system and "the one who wrote **the queue** moves teams"; and the parity oracle is *the running code*, which survives his departure. → "The author of the queue moves teams in six weeks; while the current pipeline still runs, its output is a free oracle". Same class as `Reroute-versus-hold`. |
| "this is the one axis where **A beats B**" | scoreboard — the `C wins this one outright` ruling. → "it is the one axis where A answers something B does not." |
| "Someone reciting **a strong answer** resumes from **the checkpoint**" (in `If they push`) | **three defects at once.** `the checkpoint` is Attempt A's mechanism, defined only inside the reveal, in the one section written about the reader. `a strong answer` is the tier label for Attempt **B**, while the error described is Attempt **A**'s — the sentence hands A's disqualifier to B. And the corpus form is participial. → "Someone reciting a memorised answer resumes the run that produced the grade, which is not something a finished, published run can do." |
| "whoever executes **the graph**" (in `Why this question`) | `graph` appears nowhere in the prompt and only inside the reveal — a by-term breach in the pre-commit box, which is worse than in `If they push` because it also presupposes one of the three architectures. → "whoever executes the steps". |
| "a **fold projection**" / "an **event store**" (in a verdict) | two compounds the page never introduces. C says `fold` and `event log`; `projection` has **one corpus occurrence, this one**. The `golden-path brittleness` defect: frame coinages welded out of an attempt's words. → "an event log … a fold over it". |
| "the CI **harness**" / "a **replay harness**" (frame, ×4) | `replay harness` is not a house term — but the prohibition had no replacement noun for *the runner*, which is why it was overridden. → "the weekly CI run that replays sampled cases" / "the CI job that replays it". Ledger row extended. |
| "**so it gets asked constantly**" (in `Why this question`) | a claim about interviews actually sat, on a course whose sourcing rule is that questions come from **published postings, never from an interview anyone sat**. Same class as "by three different engineers". Cut; the evidenced half ("usually as a proxy for whether you have shipped orchestration at all") carries it. |
| "Four of **the \<N\>** postings this course samples" | the first and only statement of the course's sample size, landing in a scenario's pre-commit box, with a definite article inviting a reader to check a number the course has never published. → drop the denominator. **The denominator is redacted in this row too**: a ledger that quotes a struck number verbatim republishes it one directory over, which is exactly how withheld content re-enters a public repo — the row teaches the rule without carrying the datum. **A provenance figure enters the corpus through `intro.md` §Where the questions come from, not through a scenario's box** — a scenario may then cite it. |
| "The choice is not between packages. **It is over primitives**" | a *disagreement* is over something; a *choice* is between things — and the parallelism the sentence sets up demands the same preposition. → "It is between primitives — which ones this workload needs:". |
| "recorded on **the how-these-are-made page**" | the URL slug used as a prose noun, three lines after the same target is linked by its real name. A slug is never a name. → "recorded there rather than here." |
| "because **every attempt at it agreed**" | `attempt` is the course's book unit for *one of the three answers*, breached on the page that also uses it correctly nine lines below; and "every attempt agreed" leaves *with what* open. → "because all three answers to it agreed". |
| "which the prompt lists inside appeals **and inside done**" | two inferential steps presented as one listing claim: the prompt lists the second marker among the appeals features, and separately defines `done` as "appeals working end to end". Say both. |
| "a week-four trigger to cut scope **if it isn't clear**" | misreads B, whose "If we can't **clear it** in four" is a transitive verb (finish the transfer), not the adjective. → "if the transfer is not done by then". |
| "**Not recitable** — it requires the record's actual shape." | the `a memoriser` defect in adjective form. → "It cannot be recited: the answer requires the record's actual shape." |
| "State ownership under a genuine **multi-writer loop**" | nothing loops — three parties disagree over one record, which is a conflict, not a cycle; and `genuine` is filler. → "State ownership with three writers disagreeing". |
| "A grade goes out in **March**. In **April** the candidate appeals." | the probe depends on the appeal landing inside the 30-day window, and March-to-April can be 60 days. → "at the end of March … Three weeks later". |
| "**Your** engineer who wrote the queue **leaves** in six weeks" (in `If they push`) | possessive stacked on a restrictive relative, and it hardens the prompt's "moves teams" into "leaves" in the same interviewer's voice that spoke the prompt. → "The engineer who wrote the queue moves teams in six weeks." |
| "**the two kinds of waiting**", one sentence after "nothing is waiting" | the box asserted the second thing is not waiting and then named the pair as two kinds of waiting — a self-contradiction on the page's controlling distinction, which a cold reader hits on the first pass. → name it the way `The principle` does: "suspending an open run from reopening a closed one". |
| "its test only **bites** on the deterministic layer … it **collapses into** B's answer wearing C's clothes" | two figures for one idea in one sentence (the ROADS/MACHINERY ruling), and `collapses` was already carrying a different figurative sense in Verdict A. → "only reaches" / "reduces to". |
| "the record you produce outlives the decision **by a year**" (track overview) | every other surface says **fifteen months**. → "by more than a year". |
| "the rewrite **ships with a note** stating the strongest one-sentence case for each side" (`how-these-are-made.md`) | **no such note ships** — grep returns the sentence and nothing else. The artefact is pipeline-internal, like the rubric. → state it as a rule the rewrite had to satisfy, not as a published artefact. |
| "**Three engineers** with three different sets of habits read it and gave the same answer" (`how-these-are-made.md`) | the already-rejected "by three different engineers" claim, shipped on the one page whose subject is that a model wrote every answer. → "Three agents briefed with three different sets of habits". |
| "the **two** failures above" (`how-these-are-made.md`, Read next) | stale count in a file the same commit edited to add a third failure. **A count that lives away from the thing it counts goes stale silently** — grep the page for its own totals whenever an item is added. |
| "Raw **artifacts** kept '30 days or close + 7…'" (in a verdict) | **the already-rejected US spelling, shipped a THIRD time, and a third time in a verdict.** `_language.md` §3 fixes `artefact`; `docs/` 23×/0×. The word sat *outside* the quotation marks, so the frame owned it. → **artefacts**. **A defect class that has shipped on three of four pages is not an author slip, it is a missing gate:** a mechanical spelling sweep must run on the frame ranges and skip the attempt ranges. |
| "is **the only retention policy** that survives the 77-day tail" | falsified by A's "Semantic chunks expire with the workflow" — A's derived chunks do outlast day 77. → "the only rule that carries the **raw material** through the 77-day tail", with the disposal of A's chunks stated. **And the shape is the finding: three exclusivity claims in one verdict run is what makes them unchecked. A verdict gets one per breath.** |
| "is **the only design** where a week-nine workflow stays interpretable on a newer deploy" | **falsified by Attempt B explicitly** — "the record is versioned data read through an upcasting reader. Persist facts and state position — those migrate." → "C alone pins the prompt, policy and fold version into each transition … B's upcasting reader migrates the data, not the decision." |
| "C's is … **the only one that loses the user's refund**" | falsified by B's own "or **terminates**" branch. → "C hard-codes losing it." |
| "and **both are wrong about the size**" | over-attribution: C names the currency and stops — silent, not wrong. → "and **neither sizes it**". |
| "It is also **the only page** that separates thread-scoped checkpoint state from a cross-thread store keyed per user" (`Read next`) | **a new shape: an exclusivity claim about the CORPUS.** Falsified in one grep — `docs/glossary.md` draws the same distinction. → "It is also where … is separated". **Extend the superlative rule: every exclusivity claim is read against its population, whether that population is three attempts or the whole handbook.** |
| "the three-in-a-hundred workflows that wake **forty-odd times**" | a page-owned figure with no derivation and no prompt support (~9 wakes over an ~11-day mean scales to ~63 over 77 days). The `1,300 daily escalations` class. → derive it on the page ("a workflow wakes roughly once a day, so an eleven-week case takes sixty-odd"). |
| "re-reading an eleven-week thread … **spends the entire envelope**" | the arithmetic overshoots its own claim: 63 wakes × ~1.1¢ ≈ 69¢ against a 10¢ allowance, so the tail is already over before any re-reading. The ten cents is a **mean**, not a cap. → name the cross-subsidy: "Those cases are subsidised by the six-day median today; re-deriving on every wake is what spends the subsidy." **Frame arithmetic that is individually correct can still license a wrong conclusion — check the conclusion too.** |
| "**All three are compliant**" | a **regulatory** judgement in the page's own voice, un-evidenced and legally load-bearing. → "All three honour the 30-day obligation the prompt states." **A page that grades a compliance claim is itself making one** — the framework-claims rule, one domain out. |
| "Those two are **already durable, already externally auditable**, and already the records a disputed claim will be settled against" | three affordances the prompt grants none of (it grants only "a mail alias" and "reads a bank feed"). → mark them as the assumption they are: "Take those two as durable and as the records a disputed claim gets settled against, and …". |
| "moves typical close from six days toward **thirty-odd**" | the prompt never states a billing cadence, so the frame owned a monthly assumption. → "toward thirty-odd, if the subscriptions bill monthly". |
| "`The interviewer has your design` … easy if you reasoned your way to your answer and **fatal** if you recited someone else's" | **three defects in one opener.** It displaces the recurring follow-up lead; it swaps the flagged **indefinite** article for a definite one; and **`fatal` is already a rejected row** (escalated adjective). → restore `These are the three follow-ups an interviewer reaches for next, and what each one exposes.` |
| "rank their own **memory tiers**" (`If they push`) | **an attempt's coinage adopted as the frame's general term** (A's "four memory tiers"), in the one section written about the reader and rendered outside the reveal. → "order the things a design stores". |
| "it asks **the candidate** to…" | the only `candidate` in the frame against `the reader` elsewhere; imports the interviewee register, and collides with #3's prompt sense (an exam candidate). → **the reader**, or name the operation. |
| "whose **replay window** has most likely expired" | a compound the page never introduces and no attempt writes (the `fold projection` / `event store` class), **and** a by-term reveal breach — `replay` is reveal-only. → "the raw material behind them is the likeliest to have aged out under a retention rule". |
| "the *other* side of **the summary question**" (`Read next`) | by-term **and** by-allusion breach: `summary` is defined only inside the reveal. Worse, "which is the position this page's verdicts argue against" **spoils the verdicts from outside the reveal**, to a reader told to answer first. → state the axis instead: "Whether a woken agent may trust its own earlier prose is exactly what this question turns on." **New sub-rule: a `Read next` bullet may name the destination's position; it may not name this page's.** |
| "the cost decomposition **per attempt**" (`Read next`) | **book-unit breach.** `attempt` is this course's unit for one of the three answers, breached on a page that uses it correctly a dozen times. The destination-vocabulary exemption does not cover a word the course has reserved. → "of one model call". |
| "The arithmetic behind '**most wakes must not be model calls**'." (`Read next`) | an **unattributed quotation of Attempt B rendered outside the reveal** — a reveal-skipper meets quoted words with no speaker. → drop the marks and state the claim. |
| "only a bank-feed confirmation writes it**.**" / "…one full billing cycle with no charge**.**" / "hard-fails to a terminal `abandoned_user_deleted`**.**" | **the silently-repunctuated-quotation row, three instances on one page** — each substitutes a full stop inside the marks where the source continues. Quote byte-exactly with the frame's stop **outside**, or elide with an ellipsis. |
| "degrades to its pseudonymised typed facts **or** terminates." | **emphasis ADDED inside a quotation.** The quoting row named only subtraction (dropping italics is fine, adding a comma is not); **adding bold is the same class**, and it breaches §8 as one-word rhetorical stress. Recorded explicitly. |
| "**What you would have done differently** at write time" | a callback misquoting the page's **own** probe three lines above ("say what you would have **had to** do differently"). The cheapest defect class there is — grep the page's own blockquotes before quoting them. |
| bolded clause-length questions as disagreement items (×5) and bolded whole-sentence rulings (×6) | `_language.md` §8 — bold is navigation, not intonation. The questions take the settled H3 form; the rulings take plain prose in position, as #1's "and B is right." does. |
| "The **axis under test** is what a wake is allowed to trust" (`Why this question`) | assessor back-office vocabulary leaking into the pre-commit box; a naive reader named it as rubric language. → state the question. |
| "An operation **you can safely repeat** is **idempotent**" (`Why this question`, #5) | **the run's most valuable finding, and the #4 `persists` shape a second time: a definition present, confident, and inverting the page's own argument.** Idempotence is defined on the **effect**, not on safety — MDN's Glossary and RFC 9110 §9.2 hold *idempotent* and *safe* apart as separate properties, and the corpus already agrees (`docs/glossary.md` L474: "running it twice with the same input has the same effect as running it once"). Three costs: it collapses the very distinction the page's own first `Read next` bullet exists to teach (retry safety is a property of the tool, *bought* with idempotency keys); it makes the row's true second clause ("no retry policy can grant it") **false**, since an idempotency key grants retry-safety without making an append idempotent; and it inverts the page's money case, where an overwrite rebuild is idempotent and emphatically **not** safe to repeat at €280 a go. → "An operation whose second run **has the same effect as its first** is **idempotent**. The word describes the write, not the retry policy wrapped around it, and no policy can grant what the write does not have." **Rule: the box's definition of its key term is checked against what the verdicts score, the corpus glossary, AND the term's real field meaning, verified at a primary source at gate time.** |
| "A vendor returning nothing for **eleven minutes** and a query that failed on **a permission**" (`Why this question`, #5) | **two of Attempt C's specifics imported into the pre-commit box** — `PERMISSION_DENIED` and "eleven minutes" both live only inside C, neither is in the prompt. Worse than the `1,300 escalations` class: the box is read **before** the reveal, so the reader cannot know whose facts they are, and these two *are* the reasoning Verdict C convicts C for ("one failure carries two incompatible classes"). The box silently repairs, in the page's own voice, the confusion the verdict later charges. → prompt-licensed examples only: "A vendor still returning bare 500s and a query the warehouse rejected outright". **New sub-rule: the box's examples come from the prompt, full stop.** |
| "One property bought once instead of **forty exceptions maintained forever**" (in a verdict) | falsifiable by scrolling: the scenario has **one** exception — thirty-nine jobs are already safe to run twice, which is B's entire argument. If the intended referent was A's forty per-job contracts, that is an unattributed cross-attempt claim inside Verdict B. → "instead of **a human in every recovery**", which is B's own text ("That single fact is what forces a human into every recovery"). |
| "Because the signature sits on the **sole path to publication**" (in a verdict) | **self-falsified two sentences earlier**, where the same verdict quotes A's diagram publishing last-good to all three consumers unattended. A verdict cannot exhibit the second path and then call the first one sole. → "The signature does gate every publish of **freshly built data**." **The free detector: a wrong claim usually contradicts the page's own prose nearby — grep the frame for its own claim restated elsewhere before reaching for anything else.** |
| "It moves **four lines earlier**, in A's own diagram" (in a verdict) | a checkable count no reading of the diagram supports: the quoted sentence is ~21 lines below the diagram, and inside it the branch sits 1–3 rows from the sign-off. The pun on *line* (the boundary A won't move / the text row) is good and was kept; **the number went**. And a rendered page has no line numbers, so the locator was unfollowable even if the count had been right. → "A's own diagram moves it. On the branch marked 'no answer by 05:40' …". |
| "**A is right about what neither B nor C answers:** a deterministic gate only ever checks what somebody wrote into it" | **falsified by Attempt C and by the page's own Verdict C nine lines above**, which credits C with exactly this answer ("a manifest carrying 'published-unverified' … a state rather than a better check"). Named no attempt, so a letter-keyed superlative check passes it — the `neither side of the framework argument` shape, **second shipping**. → scope it to the limit and claim nothing about who answers: "A's insistence points at where a deterministic gate stops: it only ever checks what somebody wrote into it." |
| "**C is right, on A's own source text:** … a uniform stale last-good hands the driver app precisely the failure **the asymmetry sentence** singles out" | **three defects.** (a) The item awards C a position **Attempt B also holds** — B's prose "holds the finance extract" and degrades the app feed explicitly — the `C buys three things the others don't` class. (b) The failure the prompt singles out is *unmarked* wrong, and **A does mark it** ("stale flag to all 3 consumers"), so the claim is falsified by the quotation in the same paragraph; the real cost of A's design is **uniformity**, not unmarkedness. (c) "A's own source text" and "the asymmetry sentence" are coined referents a reader cannot resolve — the prompt is everybody's source text. → name B, rule for both, and state the cost as uniformity: "B and C are right on the prompt's own grading… A does flag the staleness. One flag for all three still treats a dashboard panel and a driver's charger status as the same failure, and the prompt does not." |
| "**C comes nearest** with finance's 'explicit non-publication record with reason and ETA'" (on the age question) | **wrong ranking, falsifiable by scrolling.** C's ETA is about when data will arrive; **B** names an age *and* prefers refusing to serve — "sending someone to a charger on five-hour-old status is worse than telling them we don't know" — which is the axis the paragraph says nobody addressed. → split the credit: C nearest on the consecutive-nights question, **B furthest on the age question**, and neither names a threshold. |
| "it is **the one thing all three did the same way**, and none of them checked" (disagreement lead) | falsified by at least four other shared moves: error normalisation inside the MCP server rather than the model, submit-then-poll query handles, a hard pre-06:00 clock, and a 50-against-60 token bucket (A and B, same number). Only the *conjunction* is unique. → "a move all three made the same way, and none of them checked." **Inherited byte-exactly from #4, so this is a canon-propagation fix, not a one-page typo** — the string is easier to falsify on a page whose attempts converge on four mechanisms. |
| "about **a fifth of what the stated headroom allows**" / "the €2,500 the prompt **leaves unspent**" (in a verdict) | **two successive defects on one clause.** First: read literally, €40 against €2,500 is 1.6%; the fifth appears only after multiplying by thirteen nights (13 × €40 = €520 ≈ 21%), a step the sentence withheld — **a per-night figure compared against a monthly budget.** Second, caught on the cold read after the first fix: the €2,500 is **derived** (€9,000 − €6,500) and the prompt never grants that the remainder is available. → "thirteen nights of it would spend about a fifth of the €2,500 of monthly compute the scheduled jobs do not account for." |
| "which is why **this night costs forty calls** and not nine hundred" (in a verdict) | *nine hundred* is the prompt's; **forty is Attempt A's own projection entering the frame unquoted**, while the same page flags B's "€38" and C's "€40" as unchecked — so the page states a provenance policy in its own provenance paragraph and breaks it one verdict later. A's own cap is 120 calls, so forty is an expectation, not a bound. → attribute it: "the choice A credits for a night of forty tool calls instead of nine hundred". |
| "a **class-A** success still needs somebody awake to sign" (in a verdict) | `class A` is a label defined only in a row of A's own ASCII diagram, and it collides with **Attempt A** and with **Vendor B**/`class B` elsewhere on the page; a naive reader stopped to check which A was meant. → self-glossing and box-anchored: "an **idempotent retry that works** still needs somebody awake to sign." |
| "the reversible write shape **both staging-then-swap answers** reach for" (`Read next`) | **three defects.** By-term and by-allusion breach outside the reveal (`staging-then-swap` is B's and C's mechanism; "both … answers" counts attempts a reveal-skipper has not read) — and the "both" is in fact **A and B**, not the two who re-engineer the job, so a reader who does open the reveal maps it wrong. Third: the target lesson teaches **schema** change and contains no swap and no staging-table data write, so the shape was attributed to a lesson that does not teach it. → describe the lesson only: "expand → migrate → contract: additive first, every step independently reversible, contraction as its own deliberate step, and a deterministic gate that fails any migration carrying a destructive statement." |
| "which is a bill **the human gate** creates rather than prevents" (`Read next`) | **spoils the page's own verdict from outside the reveal** — it is Verdict A's charge and disagreement 1's ruling, delivered to a reader told to answer first. `the human gate` is also a by-term breach. And the mechanism as stated did not yield the conclusion (approval precedes the step, so nothing is paid twice) because the load-bearing half was missing: the lesson's point is that **every line before the pause runs a second time**. → state the mechanism, then the lesson's own remedy, and pass no verdict. |
| "a design that pauses for approval" (`Read next`) | over-general: the linked lesson and the vendor both scope re-execution to **the graph node containing the `interrupt()`**. → "a graph node that pauses for approval". Destination vocabulary in a link gloss is exempt from the reveal rule, so `graph node` is legal here. |
| "the €280 can be paid twice by **the resume** itself" (`Read next`) | `the resume` is a definite noun with no antecedent (the clause before it uses only the verb), and on a career-adjacent site the *résumé* homograph wins on first pass — a naive reader read it as a CV. → name the mechanism instead: "A €280 rebuild that ran there is charged again". |
| "This **separates candidates** whose verification is independent … from **those who** reach for a better prompt … where **they** think the defect lives" | the **judge-of-persons** row (`What separates people…`) and the **`candidate`** row together, in the one section written about the reader, plus the longest single-breath sentence on the page. → "What the answers separate on is whether verification is independent of the agent's own account of what it did. An answer that reaches for a better prompt or a stronger model has **located** the defect in the model rather than at the tool boundary." (`has put` was the first replacement and reads as *caused*, which is not the claim.) |
| "This **rewards anyone who** designed the give-up path as a deliverable" | a question cannot reward, and it is scoreboard register in the section where careerist framing is barred; the paragraph then said "not a state" and "asked for a state" in one breath. → "The question asks for a state, so the give-up path … has to be a deliverable rather than an absence." |
| "**For anyone who gets through it**, the follow-up is harder: the owner of the appending job says it cannot change this quarter. **Does the design change, or only tonight?**" | grades the reader on the previous question, and smuggles a **fourth** probe into probe 1's exposure paragraph under a fixed lead that says *three* — no sibling embeds a question in an exposure paragraph. The constraint is also orphaned there: probe 1 is about a timed-out query, and the ownership exposure is already carried by disagreement 2. **Cut.** *Hand-up: the interviewer's pre-registered probe-1 twist now has no home in the three-probe shape — the author should rule on whether `If they push` may carry nested escalations at all.* |
| "requires having decided much earlier that the warehouse exposes **a handle on the operation** at all" (`If they push`) | by-term reveal breach — the query handle is A's, B's and C's mechanism and the prompt never grants it — in a section rendering outside the reveal. → define it in place: "that a query still running can be identified and asked about, not only resubmitted." |
| "**Four of seven steps** are done and the budget is gone" (`If they push`) | invents a seven-step chain against the prompt's forty jobs; `step` appears nowhere in the prompt and no attempt has seven of anything. The `Reroute-versus-hold` class. → "The chain is four jobs short of done". |
| "nobody noticed until finance asked **on the 4th**" (`If they push`) | the only non-clock digit in three probes that otherwise spell throughout (spoken-register spelling-out is 4–1), **and** it asserts a monthly finance calendar the prompt does not grant. → "until finance came back on it a week later", which keeps the detection-lag point and invents nothing. |
| "**the one thing** … / **the buy** / **the converse exposure** / **one call for everybody** / **the manifest**" (#5, five bare-noun defects with one cause) | each is a countable noun the frame introduces with a definite article and no gloss, and two naive readers stalled on four of the five. `the converse exposure` additionally points **backward** at a referent that arrives two lines **later**. → `What A buys is real`; `B and C take the opposite exposure` after A's cost is stated; `one decision for everybody`; `a three-state publish record`. **Pattern worth its own rule: the frame's own coinages get the same first-use discipline the ledger already imposes on an attempt's.** |
| bolded whole-sentence rulings (×5) in `Where they actually disagree` and `**from its start**` in `Read next` | `_language.md` §8 — bold is navigation, not intonation — and **an already-rejected #4 row shipping again**. Plain prose in position, as #1's "and B is right." does. The destination page's own bolding does not travel. |
| "What **persists** is whatever a woken process **may read** to work out where it had got to" (`Why this question`) | **the run's most valuable single finding, and it survived the first full gate.** The box defined `persists` as the *read set* — collapsing the exact distinction all three attempts draw and Verdict A's central criticism turns on, and erasing the prompt's deliberate **fourth** question ("what does a wake read?"). A cold naive reader met Attempt A with the wrong model and was corrected by a verdict rather than by the box. → "whatever survives the suspend — the durable record a later run is allowed to draw on", plus a sentence naming the read set as the separate fourth question. **Rule: the box's definition of each axis is checked against what the verdicts score, not only against the prompt's wording.** |
| "none saw **the rubric** the verdicts are written against: an interviewer wrote that rubric…" (provenance, #9) | **a retired clause reinstated.** #3–#8, six consecutive pages, carry "none saw **the scoring standard the verdicts are written against** — that was fixed before any attempt existed, and a separate assessor applies it", and #9's own three attempts all use `rubric` in the *grading* sense inside the reveal. → restore the six-page incumbent. **A string the ledger records as superseded comes back unless `_scenario-template.md` carries the current one.** |
| "which **constraint** gets applied first" (frontmatter `description`, #9) | the frame's house noun is **criterion** (8 occurrences; the prompt's own word), and the three frame `constraint`s all quote an attempt. The defect lands on the one surface a search-result reader sees. → "which criterion gets applied first". |
| "a **competitor** trained a model on their manuals" (frontmatter `description`, #9) | the prompt says "a **counterpart** at another manufacturer", and the frame uses `counterpart` correctly four times; `competitor` also names a **different** referent in probe 1 (a rival distributor), so one word carried two referents on one page. `their` was additionally ambiguous — as written it read as *trained on OUR manuals*. → "a counterpart at another manufacturer trained a model on their own manuals". |
| "any of which can **cancel** an earlier one" (lead-in, #9) | the prompt, all three attempts and the frame elsewhere say **supersede**; and `cancel` asserts invalidation, contradicting the page's own credited move ("superseded does not mean deleted"). → "supersede". **A synonym chosen for variety can deny an argument the verdicts turn on.** |
| "what a **usable** answer has to carry" (lead-in) beside "the shape of an **admissible** answer" (`Why this question`) | one property, two names, twenty lines apart, both before the reader commits — and `The principle` uses the second. → "what makes an answer admissible". The same edit re-ordered the lead-in list, which had been reproducing `The principle`'s triple in the principle's own order. |
| "already fast, already deployed, and already **trusted**" (`Where they actually disagree`, closing line) | the prompt grants *used today*, *sub-second*, and *useless without the bulletin number*; **trusted** is the frame's inference, owned in the page's voice, in the section's last sentence. → "already in use for the questions it can answer". The `already durable, already externally auditable` class. |
| "**Six thousand** manuals and drawing sets" (lead-in, #9) | the only rounded figure in a four-item list where every other number is exact (11,000 → "Eleven thousand", 90,000 → "Ninety thousand", 1,400 → "fourteen hundred"); 6,200 rounded down by 3.2%. → "Six thousand two hundred". **In a spelled-out list, spelling is the register, not a licence to round.** |
| "Eleven thousand service bulletins, **arriving at** forty a month" (lead-in, #9) | the participle attaches to the wrong noun — as written the 11,000 arrive at forty a month. The prompt guards this distinction explicitly ("that is the cumulative total; the current rate is roughly 40 new ones a month"). → "forty more every month". |
| "the set's **only** single-leg elimination" (Verdict C, #9) | falsified by A (rules two things out on confidentiality alone), by B twice (a single index; a rebuild cycle), and by C's own criteria 3 and 5. The em-dash gloss beside it already stated the true, narrower claim. → "rests on one leg only: nothing else in the six criteria touches the family pack." **The fix WEAKENS to what the texts support; a superlative may never be repaired by inventing a stronger one.** |
| "cannot express a rule that differs per customer" as B's third exclusive ground (`Where they actually disagree`, #9) | the first two grounds are genuinely B-exclusive; the third is **C's headline ground** ("weights have no access-control list"). → cut the third item. |
| "**Only C** demolishes it on confidentiality; A refutes it on volatility and B on admissibility" (`If they push`, #9) | falsified by B ("it can't enforce who may see what, because the access rule is per customer and the weights are one object") — **and the page contradicted itself**, since `Where they actually disagree` credits B with that very ground twenty screens earlier. Dissolved by the reveal-boundary rewrite, which removed attempt attribution from the section entirely. **A self-contradiction between two frame sections is the free detector: grep the frame for its own claim restated elsewhere before checking the attempts.** |
| "C's €27,000 a year is its 20,000-token window multiplied out **and nothing else**" (#9) | arithmetically false: 20,000 × €2.40/M × 432,000 = €20,736, not €27,000 — the figure demonstrably contains an unstated output allowance. → "rests entirely on its own 20,000-token figure". Two neighbouring endorsements were narrowed with it: "The arithmetic recomputes." → "The elimination arithmetic recomputes."; "The computations that exist recompute correctly" → "The eliminations recompute correctly". **A frame sentence endorsing an attempt's arithmetic is itself arithmetic.** |
| "the manuals change forty times a month" (`Where they actually disagree`, #9) | the prompt's 40/month is new **bulletins**; "manuals" is Attempt A's own slip, restated **unquoted** in the frame's voice and thereby adopted. → "the documentation changes forty times a month". **`Assess, never endorse` catches an attempt's factual slip as well as its claims.** |
| "the general form of **taking the model out of the dossier path**: a model selects a defined **query** instead of deriving one" (`Read next`, #9) | two defects in one bullet. The lead-in is the page's own best-move finding delivered outside the reveal; and the gloss **inverts its destination's distinction** — `structured-knowledge` reads "It no longer derives a query; it *selects* a **defined metric**", so "selects a defined query" collapses the two nouns the source holds apart. → "the case where the answer is a lookup rather than a passage: … selects a defined metric instead of deriving a query." **A link label may be byte-perfect while the gloss beside it misstates the lesson; verify both.** |
| "**Someone who has been paged for this** says which percentile they mean" (`If they push`, #9) | the participial shape is house form, but the approved instances state a property of the ANSWER; this states a property of a population defined by BIOGRAPHY — the credential half of the anti-coach rule, and the page's only sentence grading a person. → "The trade stays unnamed until the answer says which percentile it means and what it would spend to move it." |
| "It is where the ordering either **survives contact or turns out to have been a preference**" (`Why this question`, #9) | a finding forecast pre-commit that **no verdict delivers** — A's director section is not judged, B's fails on a mislabelled number with its ordering intact, C's on register. Uncheckable in both directions, and it performs pre-commit the `preference` move B and C each make inside the reveal. → "It asks for the same decision a second time, to someone who does not read code and has already heard a simpler story." **Extends the box rule from CONTRADICTION to NON-DELIVERY.** |
| "whether the elimination was **computed from the numbers on the table or merely asserted with conviction**" (track `overview.md`, #9) | `The principle`'s clause (ii) near-verbatim **and** Verdict A's conviction, on a surface read before the H1, describing a track that contains exactly one scenario. → cut. **A track overview naming one scenario is describing that scenario; it gets the pre-reveal sweep.** |

## Localized card copy — `landing.course.design-scenarios.blurb`

The single non-English surface of this course. Recorded together, in one scoped table, because
three separate ledgers for one sentence each would be filing, not canon. **Not priming material:**
an author writing in one of these languages reads their own `_language.md`, not this table.

| locale | string | notes |
|---|---|---|
| **ru** | Трудные вопросы проектирования, взятые из требований в опубликованных вакансиях AI-инженеров: у каждого три ответа — привычный, сильный и избыточный — и разбор компромиссов, которыми они различаются. | `AI`, never «ИИ» (`_language.md` §3). Noun-first enumeration («три ответа» before the adjectives) so the elided triple parses 1+1+1, and so the closing «они» has a plural antecedent on the page. |
| **sk** | Náročné otázky pri návrhu AI-systémov, zostavené podľa verejných pracovných ponúk pre AI-inžinierov: ku každej tri odpovede — bežná, silná a predimenzovaná — a kompromisy, ktoré ich odlišujú. | `<noun> pri návrhu` shape from `sk/rag.md`, given an object (`AI-systémov`) so `návrh` cannot read as *a proposal/draft*; `AI-` hyphenated per SK `_language.md` §3. |
| **de** | Schwierige Entwurfsfragen aus veröffentlichten Stellenanzeigen für KI-Engineering-Rollen, jede dreimal beantwortet: die gängige Antwort, die starke und die überdimensionierte – dazu die Abwägungen, in denen sich die drei unterscheiden. | `KI`, not `AI` (DE `_language.md` §3); Durchkopplung on `KI-Engineering-Rollen`; en dash, not em dash. The elided adjectives stay **lowercase** — the noun is elided, not nominalised; a later pass must not "correct" them to `die Starke`. |

**Provenance formula — a content-honesty row, not a style row.** Every locale renders the source of
the questions as **published job postings**, never as interviews attended, never a named employer.
RU «опубликованных вакансий», SK «verejných pracovných ponúk», DE «veröffentlichten Stellenanzeigen», EN
"published … job postings".

*Corrected 2026-07-29 by the pre-publication leak audit.* The row previously recorded DE «echten
KI-Engineering-Rollen» — *real roles* — as satisfying this formula, and the EN source said "real
**AI-engineering roles**" too. Neither carried the *published* qualifier that does the honesty work; the
contrast in «echt» is authentic-versus-invented, not public-versus-private. The row looked like it had
audited three strings when it had only recorded them. **A ledger row that restates a rendering is not
evidence that the rendering was checked against the rule above it.**
A rendering that implies insider sourcing is a *factual* defect, not a stylistic one.

**Term decisions behind the card, with the rejections:**

| concept | ru | sk | de | rejected, and why |
|---|---|---|---|---|
| the common answer | привычный | bežná | gängige | RU «расхожий» — dismissive, pre-judges an answer the page insists is never a strawman. SK «obyčajná» — reads *second-rate*. DE «Standardantwort» — German sense is *canned/form-letter reply*. |
| the strong answer | сильный | silná | starke | Kept plain in all three. Rejected RU «проработанный» / SK «kvalitná» / DE «belastbare»: each adds a merit claim the plain English word withholds, and the page's own bullet defines the label. |
| the over-built answer | избыточный | predimenzovaná | überdimensionierte | RU «переусложнённый» — **struck by the cross-model gate**: leans toward *needlessly complicated*, which impugns judgement, where the label must describe a competent engineer building too much too early. «избыточный» also reuses the corpus's attested `over-` → «избыточ-» pattern (`rag.md` over-retrieval, `ai-sdlc.md` over-compliance). RU «перепроектированный» — false friend, dominant sense is *re-designed*. RU «с запасом» — valence inversion, «запас прочности» is praise. DE «überkonstruierte» — German `konstruiert` also means *contrived*. DE «überbaute» — `Überbau` is a superstructure. |
| tradeoffs | компромиссы | kompromisy | Abwägungen | Canon terms reused (`rag.md`, `sk/rag.md`, `de/_language.md` §1.1.b). Rejected RU «которые их разделяют» / SK «ktorými sa líšia» / DE «die sie trennen» — the actor–verb check: tradeoffs are not the agent that separates. Use "the tradeoffs **in which** they differ". |
| design question | вопрос по проектированию | otázka pri návrhu | Entwurfsfrage | DE «Designfrage» — German `Design` is dominantly visual; the course title stays English, so the blurb is the German reader's only gloss on what "design" means here. |

**SK `predimenzovaná` — RESOLVED, incumbent confirmed.** The cross-model reviewer challenged it as
reading like *a faulty technical design* and proposed `predčasne naddimenzované`. A separate naive
Slovak reader — a different pass from the one that proposed the word, as the no-self-blessing rule
requires — confirmed it lands on the intended sense: „predimenzovaná konštrukcia" is built with more
capacity than the load needs, i.e. competent, correct and wastefully large, not wrong. Incumbent
kept. Residual, recorded so it is not rediscovered: the word carries *bigger*, not *earlier* — the
"before the problem earned it" half lives in the page's bullet, not in the label. The same gap
applies to RU «избыточный» and DE «überdimensionierte».

**Cross-locale flag for the author — "the strong answer" is the thin label.** Independently, all
three locale readers reported the middle label as the palest of the three: it states a verdict
without naming a dimension, and each proposed a more specific word (RU «проработанный», SK
`premyslená`, DE `die belastbare`). All three were **refused**: each adds a merit claim the plain
English label withholds, and forking one locale would desynchronise a recurring label. The signal is
about the **English** label, not the renderings — if the author ever sharpens it, all four move
together, and the config blurb moves with them.

**RU «избыточный» — gloss it on the course pages.** The RU naive reader confirmed it reads as *more
than was needed* rather than as *redundancy/failover* (the syntax rules that sense out), but its
valence is mildly reproachful — "наворотил" — where the label should describe a competent engineer.
Acceptable unglossed on a card; on a scenario page, gloss it at first use.

## Scenario `making-it-wrong-less-often` (production-llm track, Gate 5, 2026-08-04)

**First page of a second track, and the first inline scenario→scenario link in the course.** The ledger
stops recording at #5; four shipped pages are unrecorded, so this entry uses the slug, not an ordinal, and
every measurement below was re-taken against the LIVE corpus rather than quoted from a recorded row.

**SCOPING CONFLICT — UNRESOLVED, for the author to settle.** This run's brief FROZE the prompt (report,
never edit: three agents answered it exactly as printed and the page asserts that). The ledger's line 119
classifies the prompt as *frame*, i.e. full-pass:

> The **frame** takes the full pass: prompt, `Why this question`, the commit line, the provenance paragraph,
> every `<Verdict>`, `Where they actually disagree`, `The principle`, `Read next`, `If they push`.

The brief won for this run. **Not reconciled in either direction.** Cheap fact for whoever settles it: the
prompt was read read-only against the full canon and is clean under either reading — British throughout, no
hyphenated range, no reserved word misused, magnitude numeral register. The conflict costs nothing here and
must be settled before a page whose prompt is *not* clean.

**Block strings — the provenance paragraph forked in six places and was restored.** Six sibling pages carry
"none saw **the scoring standard** the verdicts are written against — that was fixed before any attempt
existed, and a separate assessor applies it" byte-exactly. This page shipped `scoring rubric`, `and nothing
else`, an expanded interviewer clause, and a split sentence. Restored, keeping the two page-specific
additions that earn their place: `this scenario is arithmetic most of the way down` and `the page says so`
(the latter precedented by `when-not-to-build-an-agent`, and correct here because the *disagreement* section,
not only a verdict, prices the unchecked figure). **The recurring mechanism: this paragraph lives in the
ledger and not in `_scenario-template.md`, and it forks on every page that does not copy a sibling. Put it in
the template.** Everything else byte-exact: the commit line and its second sentence, both frontmatter comment
lines, the tier labels, the persona furniture, the disagreement lead with its exception clause,
`The principle`, `Read next`, `If they push`, `<Verdict>` blank lines.

**`gold set` → `golden set` in the FRAME only.** Corpus 43 × `golden set` in 14 files, **0 × `gold set`**
outside this page. Two of three attempts say `gold set`, so this is the recurring frame-instance split —
sixth page, sixth time (`top-k` #1, `artefact` #2, `superstep` #3, `artefacts` #4, `last-good` #5). Corrected
at four frame sites plus one straggler the first pass missed (`the gold labels` → `the adjudicated labels`,
caught by the cold read). Left untouched in the attempts and inside every quotation. **The two-range
mechanical sweep is now overdue by four pages.**

**Bold budget — measured, ledger method, and "under-use is the trend" no longer holds.** Frame **5 / 234
prose lines = 0.021**; attempts 8.03 per 1,000 words (their register, excluded from the budget). Series:
0.035 → 0.021 → 0.007 → 0.026 → 0.032 → 0.023 → 0.061 → 0.030 → **0.021**. Cap ~0.36; nothing near it.
One §8 breach fixed: a **two-line multi-part clause** in bold under `What none of them checked`, shortened to
its claim clause. The other three single-sentence item leads in that block **stand** — `observing-a-non-
deterministic-system` and `when-not-to-build-an-agent` already ship the shape, and a Gate-5 pass may not
reverse an incumbent it did not evidence. **Author's ruling wanted: is a bolded single-sentence item lead
inside the shared-blind-spot closer a definition-list lead (§8 permits) or a bolded ruling (§8 bars)? Three
pages now depend on the answer.**

**Figures — ALL ON PROBATION** (no self-blessing; the pass that shipped them may not protect them).
Struck at the gate: **`flanks onto` / `the flank`** (0 corpus occurrences; failed the cold naive read outright
— "flanks onto" is not a construction English has, and it sat in a bolded jump-in surface) → `goes after` /
`the move`; **`in the round`** ×2 (0 corpus occurrences, interview register against a SETTLED anti-coach rule)
→ `of the three` and `any of them produced` — note the second: `of the three` misreads as *of three
sentences* when the head noun is `sentence`, so the substitution is **not** mechanical; **`epistemics`** (the
exact rejected token) → `ways of knowing`; **`A slip narrows the design`** (a slip is an event, not an agent)
→ `Taking the high end instead`. Surviving, on probation: **`the noise floor`**, **`graded by luck`**,
**`mistaken a draw for a result`** (flagged: `draw` in the sampling sense is defined only INSIDE the reveal,
and this line renders outside it — the sports reading is a live misparse). Reuse, not coinage, recorded so no
later pass re-probates them: **`the instrument`** (established course vocabulary — `model-routing`,
`trajectory-vs-outcome`, `when-not-to-build`, `ai-sdlc/part-1-foundation/overview`), the **`buy` family**
(one sense each, cleanest since #5), **`wearing the same name`** (corpus-wide family), **`Worse is the
close.`** (the elliptical count/verdict sentence, fourth page running — a fifth settles it as house cadence).
**`disposition` CLEARED**: the rejected row bars Attempt C's *coinage on #2*; no attempt here uses the word
and the frame's use is ordinary English. **The canon binds SENSE, not the string — check the sense before
enforcing a rejected row.**

**The reveal boundary had its densest page yet — six breaches, all fixed.** `If they push` carried **six bare
attempt letters and six reveal-only mechanisms** in the one section written for a reader who may never expand
the `<details>`; `Read next` named two of the page's own H3s by term (`the gold-set disagreement`, `the
two-minute disagreement`) and one attempt-shared design (`the two-stage chapter-then-heading build`).
**NEW SUB-SHAPE, ON PROBATION: outside the reveal, refer to attempts by COUNT and position in the argument,
never by letter** — "all three answers spend them…", "Two of the three… The third…". The recast keeps the
claim falsifiable while naming nothing the reader cannot see. **Residual cost the cold read named and the
author should weigh: the reader can no longer check the A/B/C mapping by scrolling.**

**The anti-coach row caught the judge-of-persons shape a THIRD time.** "**An engineer who** reasoned their way
to a design can trade those three… **One who** assembled a stack of techniques cannot" is the rejected "This
**separates candidates** whose verification is independent … from **those who**" verbatim in structure.
Recast onto answers with the row's own pattern. **A cold reader then objected that an *answer* cannot reason,
trade or say — the actor–verb rule pulling against the anti-coach rule.** Held the anti-coach recast: these
are *spoken* interview answers, so the verbs fit, and the canon rule is SETTLED while the objection was one
reader's. **Recorded because the tension is real and will recur: when the anti-coach row forces a human
subject out, the replacement noun must be one that can plausibly take the section's verbs.**

**Cross-course link names — the one-destination-one-name row caught its first collision.**
`guardrails-at-the-boundary:315` labels `part-1-rag/generation/deep-dive` by its `sidebar_label`
(**Self-verification & structured output**); this page labelled it by its `title` (**Generation — deep
dive**). Both legal alone; the result was one destination under two names in one course. Normalised to the
incumbent (guardrails shipped first — `94372bd` before `dac94e0`). **Promote the row from ON PROBATION to
SETTLED**, and record the names now fixed by first use: `production-failures` → *Why AI systems fail in
production* · `layered-gates` → *Layered gates and mechanism diversity* · `review-at-volume` → *Reviewing
agent output at volume* · `generation/deep-dive` → *Self-verification & structured output* ·
`retrieval/deep-dive` → *Retrieval — deep dive* (first linked here, so this page fixes it). **Known residue:
bullets 2 and 3 now name two halves of one lesson pair by two different conventions (`title` vs
`sidebar_label`). That is the row working as designed, not a defect — but say so, or the next pass "fixes"
it back.**

**NEW ROW, ON PROBATION — the inline scenario→scenario link.** First cross-link between two scenario pages in
running prose. It shipped as `[another scenario's question](…)` with the destination's real title sitting
*outside* the link in the same sentence. **Rule: an inline scenario link goes on the target's own title.**
Second rule the shape needs: **an inline cross-scenario link may state what the other scenario ASKS, never
what it concludes** — the reader may not have read it, and the reveal discipline does not travel across pages.

**A gloss beside a byte-perfect label can still be wrong — and this page had two.** Both `Read next` label
sets were correct; two glosses misdescribed their destinations. (a) Bullet 1 attributed the
frozen-versus-rotating discipline to "the gold-set disagreement", which turns on a different axis entirely
(enriched vs random) — retargeted to the destination's own words. (b) Bullet 3 said "a verification pass must
not see **the reasoning** it is checking"; the destination withholds **the draft / baseline response**, and
holds self-consistency and chain-of-verification explicitly apart, which the gloss collapsed into one.
**A correct label is not a pass. Open the destination and check what the gloss claims it teaches.**

**`Why this question` — the box RESOLVED the principle, and the fix cost two rounds.** The shipped box named
both of the principle's numbers in the principle's own terms ("Two facts… pull against each other" +
"a second question the scenario does not settle for you" ↔ *the two numbers the brief leaves you to compute
yourself*; "what that instrument is capable of telling anyone ten weeks from now" ↔ *what the instrument that
will judge you can actually resolve*; "the only place a check can finally be resolved is a person's attention
— already spent down to the minute" ↔ *whose minutes absorb every check you add*). It also carried two
**orphan** claims no verdict delivers, one of them contradicted by Attempt A's own legality check.
**This passed the ledger's barred-items list** (no tier label, no fourth tier, agentless trap) — the list was
checking the wrong axis. **New rule: the box is checked against THE PRINCIPLE, proposition by proposition,
not only against the barred-items list. If the box states a conclusion the reveal is supposed to deliver, it
is a leak however clean it is on the list.** Rewrite kept to prompt-given facts (nine people's minutes, the
capped envelope, the ninety-minute clock, closed headcount, one measurement at a fixed size) and states no
conclusion about whether the instrument can resolve anything. Final length **80 words**, at the template's
floor — the first rewrite came in at 69 and the cold read caught it.

**THE GATE'S OWN FIX INTRODUCED A FALSE CLAIM — caught by the cold read, as designed.** The first rewrite of
the box asserted "every cost lands somewhere that is **already full** — nine people's minutes, a fixed
inference envelope, a ninety-minute filing clock." **False of the envelope: €2,100 against €9,000 is 23%
consumed**, and the page states €6,900 of headroom twice in its own voice. Worse, it asserted in the framing
box the precise error Verdict A convicts Attempt A of committing, so a reader who believed the box could not
follow the verdict. Corrected to "lands on a budget somebody else already fixed… None of them can be raised
inside ten weeks". **Second consecutive page on which the gate's own first round of fixes shipped a new false
claim. The edit-auditor pass — a fresh agent given the gate's own diff and told to verify every NEW assertion
against source — is what caught it, and it is now mandatory, not optional.**

**Mechanical lesson worth more than the page: a whole-file rewrap is a content-editing operation.** Re-wrapping
paragraphs to restore the house column after in-place edits stripped the two-space continuation indent from
every `Read next` list item and split a markdown link across a line inside its own label. Both were caught by
re-inspecting the block, not by the word-content assertion the script carried (it passed — the words were
identical). **A whitespace-only assertion does not protect list structure or inline constructs. Rewrap
paragraph-by-paragraph with lists and links excluded, and re-read the rendered blocks afterwards.**

**Jurisdiction — observed inside the attempts, deliberately left standing.** Attempt A's US `realize` and
`artifact` (the frame is clean, `artefact`); `gold set` in A and C; Attempt B's `replay harness` (the term the
extended row bars *in the frame* — and `harness` appears exactly once page-wide, so the frame never picked it
up: the first clean run for that row); `top-8` in B; three names for one instrument (A `held-out set`,
B `frozen set`, C `frozen internal gold set`) — the page's best evidence of independent authorship;
hyphenated ranges `4-5×` / `€9-10k` inside A, reproduced faithfully inside quotation marks while the frame
uses en dashes in its own voice two lines later. **That pairing is the worked example the numeral row needed:
the en-dash rule governs paraphrase, the byte-exact rule governs quotation, and both apply in one paragraph
without conflict.** **Zero mechanical errors inside the three attempt bodies**, and — first time in the
series — **no ASCII diagram in any attempt**, breaking a five-page run. For the pipeline owner.
