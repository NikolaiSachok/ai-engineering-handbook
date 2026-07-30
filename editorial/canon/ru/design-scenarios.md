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
| "Four of **the ten** postings this course samples" | the first and only statement of the course's sample size, landing in a scenario's pre-commit box, with a definite article inviting a reader to check a number the course has never published. → drop the denominator. **A provenance figure enters the corpus through `intro.md` §Where the questions come from, not through a scenario's box** — a scenario may then cite it. |
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
