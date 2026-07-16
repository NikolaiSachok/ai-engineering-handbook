# Style canon — router / index

The handbook keeps a style & term canon organised on **two axes — language × course**. This file is the
**router**: it holds the language-agnostic spine (the principles every locale inherits) and points at the
per-language files. It stays the **default entry point** — the `editorial-team` skill resolves
`editorial/style-canon.md` first, then loads the files for the language and course it is editing.

**Structure — `canon/<lang>/`.** Each language folder splits its canon in two:

- **`_language.md`** — the **course-independent** language rules (spelling & register, voice, the
  bridge-direction rule, the bold budget; for SK also anti-bohemism, the EN→SK calque templates, and
  verb-by-object). These hold for **every** course in that language.
- **`<course>.md`** — one **per-course term ledger** (`rag.md`, `ai-sdlc.md`, …): the term registry,
  semantic reservations / sense cards, repeated exact strings, book units, and the progress appendix for that
  course. `rag.md` is the original canon and is **frozen**; the language rules in `_language.md` were
  extracted from it verbatim.

**Loading contract.** Load **`_language.md` (always)** + **the target course's ledger** — and nothing else.
An author/editor working in one language never reads the other language's figures, false-friends, or calque
lists (priming the SK writer with RU figures imports the wrong reflexes). Across **courses within a
language**, the sibling ledger is **peek-don't-load**: for a term that plausibly overlaps a sibling course
(shared AI-engineering vocabulary — agent, prompt, token, context, eval, guardrail, retrieval…), do a
TARGETED, read-only lookup; if a decision exists and the sense matches, REUSE it verbatim and cite it; if the
sense genuinely differs, FLAG for a human — never silently fork, and never edit a frozen sibling ledger
(`rag.md`). Loading a whole sibling ledger as priming context is prohibited — that is the pollution this split
prevents. Separating the files is a real quality lever, not just filing.

## Honesty rule (whole project)

The canon is **normative**: new pages are written to it, and deviations found in the corpus are corrected to it.
The canon **lives with the text** — a canon update ships **in the same PR** as the page that motivates it.
Process rules (editorial passes, checklists) live in `CLAUDE.md` and in the skills (`editorial-team`,
`authoring-team`); the canon holds only language and structural norms. Never enshrine a form the naturalness
gate has not cleared; a form still awaiting a native check is marked *proposed, pending human check*, not settled.

## Pointer table

| Language(s) | Language rules | Course ledgers | Role |
|---|---|---|---|
| **RU + EN** | [`canon/ru/_language.md`](./canon/ru/_language.md) | [`canon/ru/rag.md`](./canon/ru/rag.md) (frozen) · [`canon/ru/ai-sdlc.md`](./canon/ru/ai-sdlc.md) | RU is audience-primary (written natively, never by translation); EN is the canonical source locale in `docs/`. |
| **SK** | [`canon/sk/_language.md`](./canon/sk/_language.md) | [`canon/sk/rag.md`](./canon/sk/rag.md) (frozen) · [`canon/sk/ai-sdlc.md`](./canon/sk/ai-sdlc.md) | Slovak — presentation-grade secondary locale, composed natively from EN meaning. Mirrors the RU/EN canon's *shape*, not its decisions; carries the anti-bohemism gate + EN→SK calque templates in `_language.md`. |

**Add a language** → add `canon/<lang>/_language.md` (its own kept-EN set / false friends / figures) plus one
`canon/<lang>/<course>.md` ledger per course **and add a row here**. **Add a course** → add
`canon/<lang>/<course>.md` for each language (seed its terms-to-settle table); the shared `_language.md` is
reused unchanged. Keep this router's filename stable — it is the fixed entry point.

## Cross-language principles (stated once; both files inherit)

These are the language-agnostic spine. The per-language files specialise them; they do not restate them.

- **What a canon is.** A single ledger of term decisions, semantic reservations, casing/typography, recurring
  block strings, voice, and rejected variants — so every page stays consistent with the rest of the corpus and
  a new page is written *to* the ledger, not from scratch.
- **The ledger binds SENSE, not the string.** Registry and reservation rows bind the **terminological meaning**,
  not the raw word. When a term's word is used as an ordinary word, the translation follows the natural idiom,
  not the term gloss (e.g. *the core failure of this approach* → "the fundamental problem," not the taxonomic
  "failure" term). Each locale spells out its own collisions.
- **Bridge rule (principle).** At a term's **first defining mention on a page**, bridge it once in parentheses;
  refresh once at the first mention in a new major section of a long page. Direction is per-locale: a kept-EN
  term gets a native-language gloss; a native term gets the English original. Never two bridges of the same term
  within a screen. Video captions and preview/announce lists do **not** count as the first mention. (RU/EN: §7 in
  `canon/ru/_language.md`; SK: §7 in `canon/sk/_language.md`. The RAG glossary-direction decisions in SK §7.1
  stay in `canon/sk/rag.md`.)
- **Bold budget.** Bold is a **navigation** tool, not intonation: a soft cap of ~0.36 bold spans per line of
  prose. Emphasise a term anchor at its first defining mention, a definition-list lead, or a rare lone page
  maxim — never rhetorical stress, whole clauses, or repeats of already-introduced terms. A clause-length maxim
  goes in quotes or italics, not bold. (RU/EN: §8; SK: §8 — both in `canon/<lang>/_language.md`.)
- **Metaphor / figure budget + figure-probation.** Authorial figures are language-bound coinages and do **not**
  port across locales — each language composes its own (or plain prose) and confirms it **for itself**. A figure
  introduced in a PR enters **on probation** («(на испытании)» / „(na skúšobnej dobe)") and reviewers check it
  like ordinary text until the next cold read / milestone pass confirms it (a naive monolingual reader decodes it
  at first contact, without the English page) or strikes it (then it joins the rejected variants). Keep the
  per-page figure count modest. (RU/EN: §6; SK: "Figúry (§6)" — both in `canon/<lang>/_language.md`.)
- **Sense cards.** Where one word carries several senses across the corpus, a **sense card** fixes one meaning
  per frame and names the disambiguating question to ask before writing the word — a reservation breach is a
  defect even when the sentence is otherwise correct. Each locale keeps its own cards (their polysemy differs;
  e.g. Slovak has clean pairs where Russian must disambiguate one word). Sense cards are **course-specific** —
  they live in the per-course ledger, not `_language.md`. (RU/EN: §2; SK: §2 — in `canon/<lang>/rag.md`.)
- **Book units.** The corpus's structural vocabulary is shared: **lesson** (one page), **layer** (a conceptual
  pipeline stage), **part** (Part I / II / III), **cross-cutting aspects** (eval, guardrails, observability).
  Reference lessons **by name, never by number**; internal links point at the `.md` file. Book-unit rules are
  kept in the per-course ledger. (RU/EN: §5; SK: §4 + the RU §5 rules it inherits — in `canon/<lang>/rag.md`.)
- **Method lives in the skills.** Structural checks (grammatical anchor, explicit object, metaphor budget,
  clause-split, agreement sweep — the editorial-team **Gate 2a**) and the authoring **meaning-first** method are
  **language-agnostic and live in the skills**, not here. The canon only names each language's specific traps.
