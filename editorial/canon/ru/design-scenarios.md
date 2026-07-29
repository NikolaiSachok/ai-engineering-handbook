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
| **replay environment** / **replay suite** | **two different objects, not synonyms.** An *environment* is the frozen-snapshot substrate with a determinism contract; a *suite* is a fixed set of cases run against it. `replay harness` is not a third house term. Disambiguate at first use if a page needs both. |
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

## Numeral register in the frame — **SETTLED**

The verdicts **mirror the numeral register of the attempt they judge** (A and C spell figures out, so Verdict
A and Verdict C spell them out; B uses digits, so Verdict B uses digits), and the neutral analytical
register — `Why this question` and `Where they actually disagree` — uses **digits**. This is a coherent
system, not drift, and it was verified before being recorded rather than assumed. Ranges take an en dash in
the frame (`1–5`, `3–5%`) even where the attempt being paraphrased used a hyphen — the `top-K` precedent.

**CONTESTED, for the author:** the blockquotes in `If they push` spell numbers out as spoken register
("up sixty percent"), where scenario #1's interviewer speaks in numerals ("the bill is down 45%"). Pick one
for the course.

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

## HOUSE — an instrument as the subject of *tells you* — **SETTLED, do not flag**

"a tagged score slice **tells you** what the surge cost", "carrier and WMS state **tells you** whether the
reroute moved the parcel" are house form, not actor–verb defects: the corpus carries 11 instances of a
measurement or property as the subject ("Recall@K tells you whether…", "residency tells you *where* your data
sits"). Recorded because the Gate-2a actor–verb sweep flags this shape on sight every page. **The rule still
stands for agents that decide** ("the metric rewards", "a credit closes").

## Bold budget on a scenario page — measured

Measure the **frame only**; the attempts' bolded spoken section labels are their register and are excluded.
Scenario #2's frame: **1 bold span / 122 prose lines = 0.008** against the ~0.36 cap (#1: 0.038). The single
span is the fixed commit line. The attempts sat at 0.183 (#1: 0.117) and are **not** a budget finding —
that number is pipeline signal about persona bleed, reported to the producer, never fixed.

## Product and vendor names inside an attempt — **RULED, KEEP; author may overturn**

Scenario #2's Attempt A names "Braintrust or LangSmith-style dataset" and Attempt C "dumps traces to S3".
The sourcing rule bars naming a **company the scenario came from**, obliquely or directly — it is about
anonymising the source, not about a candidate name-dropping a tool. And the names are *persona evidence*: A
was given "follows the eval-tooling ecosystem closely", and removing them erases the tell. Precedent cuts
the same way in the stricter register — #1's Verdict C names "The vLLM tier" in the page's own voice.
**Ruling: keep, inside attempts.** Recorded as a decision rather than an oversight, because #3 will hit it
again. If the author overturns it, #1's verdict is the more serious instance and moves first.

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
| "the **disposition** is a comparator" (unquoted, page's voice) | `disposition` is Attempt C's coinage. The frame may **quote** an attempt's coinage; it does not adopt it as a house term. |
| "without **golden-path brittleness**" | a compound the page never introduces — C says *golden set* and *golden policy*, never *golden path*. → "without pinning one correct path per case". |
| "What settles it here is staffing, not **epistemics**" | needless erudition for a practitioner audience; nothing on the page needs the word. → "not theory". |
| "the **ordering is decidable**" / "stale-feed **conduct**" | borrowed formal-logic register, and *conduct* is a person-word used of a system. → "the order is clear" / "behaviour on a stale feed". |
| "bounds the loss at **$9 a reroute**" | $9 is the unit price, not a bound — a volume cap bounds *how many*. → "limits how many nine-dollar reroutes a bad hour can spend". |
| "Multi-step agents break **the habit that** final-answer scoring is enough" | a habit is a practice, not a proposition; `the habit that <clause>` is not a construction. → "the habit of treating a score on the final answer as enough". |
| "**What separates people** is what they choose not to measure" | interview-coach register, and it makes the page a judge of persons rather than of answers. → "What the answers separate on is…". |
| "against 63,000." (in `Why this question`) | elided unit on a figure the box asks the reader to compute with. → "against 63,000 a week". |
| "can be bought for $75" (frontmatter `description`) | on the one surface a search-result reader sees, this decodes as *the label is purchasable from a vendor*. → "can be bought off with a $75 credit". |

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
