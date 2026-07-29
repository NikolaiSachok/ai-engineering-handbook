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
| verdict lead | `**Verdict.**` — bold, full stop inside the bold, one per attempt |

**`the reveal` is NOT a page string.** It is the corpus's *name* for the boundary (`intro.md`, "before
you open the reveal") and is registered in the terms table below. Scenario pages carry `Show the three
attempts`. Recorded 2026-07-29: the earlier block-string row claimed a string that appears on no
scenario page — it was written before any page existed to check it against.

**Label form.** Bold, capitalised at list-item or sentence start (`**The common answer** — …`),
lowercase in running prose ("you will agree with the strong answer"). The article stays outside the
bold when the label appears mid-sentence. **In an attempt heading the label is lowercase and
unbolded**, after the letter and an em dash: `## Attempt A — the common answer`. A heading is already
navigation, so bold inside it would breach `_language.md` §8. **ON PROBATION** — coined in the same
batch as the labels; scenario #2's Gate 5 confirms or strikes it.

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

The **frame** takes the full pass: prompt, `Why this question`, the commit line, every `**Verdict.**`,
`Where they actually disagree`, `The principle`, `Read next`, `If they push`. **A verdict is frame even
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
