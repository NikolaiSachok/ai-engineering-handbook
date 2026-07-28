# German locale (de) — translation playbook

How to add a fourth locale to the handbook. Written before the work starts so the executing agent inherits
the decisions, not just the task. **Read this whole file before touching anything.**

It is the counterpart of [`sk-locale-playbook.md`](./sk-locale-playbook.md) and deliberately mirrors its
shape. Where German is the same problem as Slovak, this file says "as SK" and moves on. The value is in the
three places where it is *not* the same problem: the gate stack (§4), the Slovak post-mortem (§5), and the
German-only risks (§6).

---

## 1. Stakes, and the premise correction that shapes everything

The German locale is presentation-grade: it will be read by native German speakers as a showcase of the
book. A visibly machine-translated German course is worse than no German course.

**The tempting framing is wrong.** It is not "Slovak had the author's eye and German won't." Slovak already
ran without the owner as final proofreader — the SK playbook says so in its own line 9: *"The author cannot
proofread Slovak the way he proofreads Russian — there is no human ground truth downstream."* Every SK
quality mechanism ran as **gates only**. German is therefore **not inventing a substitute gate stack; it is
porting a proven one.** That is the single most important sentence in this file, because it changes the job
from "design a replacement for the owner" to "re-aim an existing rig at a language whose failure modes
differ."

**What German actually loses is narrower, and it is worth stating precisely — two things, not three:**

1. **The owner's residual *passive* comprehension.** As a Russian speaker he could read Slovak
   approximately: cognates, shared morphology, a wrong-looking word standing out. That residual signal goes
   to **zero** at A1 German. Nothing in the pipeline should assume the orchestrator can eyeball the output.
2. **The one native human read of the pilot.** SK secured it
   ([`sk-pilot-naturalness-check.md`](./sk-pilot-naturalness-check.md)); it must be secured again for German,
   and §4 Gate 7 says why that is *easier*, not harder, here.

**What German does NOT lose — and this is why the port works.** The owner's contribution to Slovak was never
*feel*. It was **semantic rulings** issued in Russian and English *about meaning*: sense cards, term-class
decisions, whether a coinage says the true thing, whether a figure survives probation. Read the SK canon's
phase appendix and the pattern is unmistakable — the owner adjudicated *what a word means and whether the
evidence supports it*, not *whether it sounds German*. **Those rulings port to German unchanged and lose
nothing.** The A1 gap touches naturalness judgement only, and §4 Gates 2, 4 and 6 exist to replace exactly
that.

---

## 2. Doctrine (inherited from the RU/SK/EN experience — unchanged)

These carry over from the SK playbook with no German-specific amendment. Read them there; they are not
restated here.

1. **Native composition from a fact skeleton — never sentence-by-sentence translation.** Skeleton extracted
   from the **EN** page; the German writer composes from the skeleton alone and never sees the EN, RU or SK
   prose.
2. **Authorial figures do not port.** Not from RU, and — important, because the temptation is new — **not
   from SK either.** German composes its own or writes plain prose. A figure enters on probation.
3. **The glossary is the term ledger — settle it FIRST.** Per-term class decisions before page one. §5
   explains what it cost Slovak to half-do this.
4. **Voice and recurring block strings decided once, in the canon bootstrap.** See §7 for the German
   decisions.
5. **Strongest available model** for German runs.
6. **Loading contract** per [`canon/README.md`](./canon/README.md) and
   [`style-canon.md`](./style-canon.md): load `canon/de/_language.md` + the target course's ledger, and
   **nothing else**. Priming a German writer with the SK canon imports Slovak reflexes — and §6.1 shows the
   Slovak reflexes are actively *wrong* for German.

One amendment to the SK doctrine, and it is load-bearing: **rule 3's expectation is inverted.** SK expected
its kept-EN set to be *larger* than RU's. German's will be larger again — but not as a concession. See §6.1.

---

## 3. What the corpus actually is (measured 2026-07-28)

The SK playbook was written when the book was one course of 38 pages. It is now two courses of **67 pages**.
German inherits the whole thing from day one, so plan against these numbers, not against SK's.

| Surface | Files | EN words |
|---|---:|---:|
| **RAG course** (`docs/`) | **39** | **92 586** |
| — Part I | 13 | 25 457 |
| — Part II | 14 | 32 719 |
| — Part III | 10 | 25 231 |
| — intro + glossary | 2 | 9 179 |
| **AI-SDLC course** (`docs-ai-sdlc/`) | **28** | **45 227** |
| — intro + glossary | 2 | 6 969 |
| — Part I | 5 | 11 770 |
| — Part II | 5 | 5 299 |
| — Part III | 5 | 7 299 |
| — Part IV | 5 | 6 695 |
| — Part V | 6 | 7 195 |
| **Total** | **67** | **137 813** |

**Non-prose surfaces.** UI strings: **130 keys / ~531 words** across five JSON files (`code.json` 85 —
of which **74 auto-fill** from `@docusaurus/theme-translations/locales/de` and only **11 `landing.*` are
authored**; `navbar.json` 6; `footer.json` 11; the two docs-plugin `current.json` files 22 + 6). **No
`_category_.json` files** — locale copies never render and were deleted repo-wide in #290; the two
`current.json` files carry every category label. **49 `<YouTube>` embeds** (videos stay English; the
one-line "why watch" note is German and says the video is in English — same convention as RU/SK).

**Load-bearing-strings surface ≈ 654** (Layer 1.5 of the `authoring-team` skill): 91 frontmatter strings
(67 `title:` + 24 `sidebar_label:`) + 472 headings (`##`–`######`) + 91 translatable card strings (57
`label` + 17 `badge` + 8 `InfoCard title` + 9 `caption`). *Correction to an earlier estimate of 124 card
strings and ~690 total: the 124 figure counted the `icon=` attribute, which is a lexicon key, not a string.
All 91 card strings live in a single page, `docs/part-3-production/production-failures.md` — which makes
that one page the densest width-budgeted surface in the corpus. See §6.5.*

---

## 4. The gate stack

In run order. Each gate states its **scope** and — the part that matters — **what it cannot catch**. A gate
whose blind spot is unwritten is a gate people trust too far.

### Gate 0 — structural parity script *(new; does not exist today)*

Language-independent. Asserts, per locale pair:

- identical `.md` file set;
- identical heading **count and level sequence**;
- identical counts of `<InfoCard>`, `<Node label=`, `<YouTube>`;
- **byte-identical fenced code blocks**;
- identical numeric and unit tokens.

**Catches:** dropped sections, dropped cards, dropped or mutated numbers, silently reordered structure — the
failures that survive every prose gate because the prose that remains reads fine.
**Cannot catch:** anything about the German. A perfectly parallel corpus of fluent nonsense passes Gate 0.
*Owned by another agent (see the milestone). Reference it; do not build it here.*

### Gate 1 — fidelity diff against the fact-locked EN

Mechanical claim-by-claim diff against the extracted skeleton.
**Catches:** drift, dropped nuance, invented facts.
**Cannot catch:** register. A faithful calque passes Gate 1 cleanly.

### Gate 2 — blind back-translation

A fresh agent, **no sight of the EN**, renders the German back into natural English; diff against the
source. Two independent signals:

1. **semantic drift** shows up as content difference;
2. **a calque round-trips suspiciously exactly, while natural German round-trips with a shift.**

**This is the single most valuable gate for an A1 owner, because its output is in a language he reads
fluently.** It converts a judgement he cannot make into one he can. Run it on the load-bearing strings
always, and on a sampled section of body prose per page.
**Known false positive:** a figure or glossary headword deliberately identical across locales round-trips
exactly by construction. Check the term ledger before acting on an exact round-trip.

### Gate 3 — cold read, comprehension axis

A naive monolingual German reader; no English, no source. Does every term and figure decode from German
alone?
**Documented blind spot — stated here because it is the failure that created Layer 1.5:** *a
stilted-but-decodable heading passes.* The gate asks "is this understandable", and a translated-sounding
heading **is** understandable. Comprehension and naturalness are orthogonal axes.
**Cadence:** twice, in separate sessions, per page. **Three times on the pilot if Gate 7 secures no native
human.**

### Gate 4 — Sol as native-register judge

Monolingual German, **a different model family from the renderer** (the cross-model naturalness gate —
same-family self-assessment grades its own reflexes as native). Verdict per string: **native / suspect /
translated**, each carrying a **linguistically named tell**: Satzklammer, verb-final order in the
subordinate clause, government/case, loanword gender, nominal style, Denglisch participle, *von*-genitive.

**A verdict without a tell is discarded.** The named tell is what makes the gate falsifiable and what lets
an orchestrator who does not speak German adjudicate at all.

**Not redundant with Gate 3.** Gate 3 measures comprehension; Gate 4 measures naturalness. Layer 1.5 of the
`authoring-team` skill exists precisely because a corpus that passed comprehension shipped a translated H1.
**Cannot catch:** fidelity — a fluent German sentence that says something false scores "native".

### Gate 5 — the load-bearing-strings pass (Layer 1.5)

Per `authoring-team` SKILL.md §Layer 1.5, and run **before** the body so the body inherits the headings'
decisions:

- compete **3–4 candidates per string with deliberately divergent SYNTACTIC STRATEGIES** — nominal vs.
  verbal, different semantic actor as subject, relative clause vs. prepositional phrase vs. apposition,
  scenario frame vs. means frame. *Three variants differing only by synonym are a failed generation.*
- **judge blind, in a separate call, with the incumbent hidden** among A–D and its position varied;
- **require the linguistic reason**, name the runner-up and what it lacks, and **grade the margin**;
- **negligible margin against the incumbent ⇒ keep the incumbent.** "Already natural" is a valid and
  expected outcome — this is a review, not a rewrite quota.

**This is the highest-yield gate for German**, more so than it was for Slovak, because the German heading
genre diverges from the English one *further* than Slovak's does: nominal style over verbal, no title case,
compound-heavy, and a strong preference for a bare noun phrase where English writes a clause. A German
heading rendered by tracking English word order is wrong in a way a Slovak one often is not.

Record the recurring shapes in `canon/de/<course>.md` as a **constructions** section — **conditions, not
substitutions**, each entry naming the English shape, the candidate frames, the test that decides between
them, and a worked example of each branch. An entry that reads as a lookup table has failed.

### Gate 6 — attestation-based term adjudication

**This is the real replacement for the owner's eye, and it is the reason the A1 gap is survivable.**

When two renderings of a term compete, **never ask a model which sounds better.** Require **citable evidence,
ranked by authority**:

1. binding norms and standards (BSI IT-Grundschutz, DIN/ISO in German);
2. reference works (Duden, DWDS);
3. de.wikipedia lemma titles;
4. university CS teaching material;
5. professional publishing and journalism (dpunkt, Rheinwerk, O'Reilly DE, heise/iX/c't).

**Mandatory MT-signal check.** A vendor's localised documentation that **disagrees with the same vendor's
other Germanic/Slavic pages** is machine output, not native usage — down-weight or discard it. *This exact
check saved a Slovak ruling:* in SK phase 26, `Microsoft Learn sk-sk` was excluded as a weak MT-signal
because the same vendor's Czech page led with a different form and the Polish pages split — the vendor's own
localisation chain contradicted itself.

**Resolution rule when the evidence does not decide: keep the incumbent, mark the row `DISPUTED`, change
zero strings, and route the question to the native-reader packet.** This is not a stalemate; it is the
correct outcome, and SK's `least privilege` row is the worked example of it.

**German's advantage.** Its corpora are far richer than Slovak's — BSI IT-Grundschutz, DIN/ISO German,
de.wikipedia, Duden/DWDS, university CS material, heise/iX/c't, dpunkt/Rheinwerk/O'Reilly DE. Slovak had to
adjudicate `least privilege` across four competing families with a single binding decree as the only high
authority. German will usually find a real answer.

**What this gate really does: it converts "the owner reads it" into "the source says so" — a claim a
non-speaker can verify independently.** That is the whole trick.

### Gate 7 — one native German reader, once, on the pilot

Reproduce [`sk-pilot-naturalness-check.md`](./sk-pilot-naturalness-check.md) in German. Its proven shape:

- both pilot pages **verbatim**, so the reader sees shipped text, not a sample;
- the instruction is **"mark it, don't fix it"** — no correction proposals wanted;
- **~20 minutes**, stated up front;
- a short context note explaining the deliberate kept-English policy, so the reader judges *flow*, not
  vocabulary;
- **~12 closing questions, each probing exactly one phenomenon** (a term family, a figure, a recurring block
  string, typography, overall impression) — mostly yes/no, with a free line;
- **every `DISPUTED` row from Gate 6 becomes one of the questions.**

**The German-speaking developer pool is far larger than the Slovak one, so this is the cheapest high-value
item in the milestone.** Budget it as a scheduled task, not a hope.

**Documented fallback if no human is secured:** a third independent cold read on the pilot (Gate 3 ×3), and
every `DISPUTED` row stays disputed — it does not get resolved by model consensus.

---

## 5. Why Slovak actually failed — cautions, each with its "cheaper up front"

The SK canon's phase appendix (`canon/sk/rag.md`, Fáza 1–26) is the honest record. These are the failures
worth paying to avoid twice.

| What went wrong in SK | The caution for German | What would have been cheaper up front |
|---|---|---|
| The pilot's first repair pass **substituted words** to soften calques instead of removing them; a full method change to reconstruction-from-the-proposition followed (Fáza 2b → 3). | **Calque repair is rewriting from the proposition, never word substitution.** State it on day one, in the canon and in every renderer brief. | Saying it before the pilot instead of discovering it after. |
| **One universal verb painted onto every object** was ratified as settled style, then revoked. | A **verb-by-object table** belongs in the canon bootstrap: for each object (text, structured output, tool call, request, intent, result, error), the two or three idiomatic verbs *and the one that does not fit*. | A one-page table in Phase 1. |
| Several **native coinages passed one reviewer** and were later struck as semantically wrong. | **The figure-probation rule applies to TERMS too**, not only to figures: a newly coined term is on probation until a cold read or a milestone pass confirms it. | Marking coinages as probationary at birth. |
| **Glossary and body drifted in opposite directions** — headwords led English while the body led Slovak, corrected corpus-wide at Fáza 25. | **The per-term class decision (kept-EN-led vs. German-led) precedes page one** and binds headword *and* body. | Settling direction, not just wording, in Phase 1. |
| A settled row was defended with a **reason that a later check falsified** ("weak Slovak attestation" — Fáza 26 found the attestation). | **Every term ruling carries a citable attestation at the moment it is made**, plus a record of **what the grep actually covered** (which forms, which trees, which case). | Writing the citation down when the ruling is made, not when it is challenged. |
| A canon recorded a decision about a string that **did not exist in any page** (a cross-reference label nothing carried), superseded at Fáza 25. | **Check ground truth before settling a cross-reference.** Grep the corpus for the string first. | One grep. |

---

## 6. German-only risks — no RU or SK experience covers these

This is the section with no counterpart in the SK playbook. Slovak's load-bearing artefact was its
anti-bohemism section; German has no near-identical sister language, and the slot is filled by a different
set of hazards.

### 6.1 Anglicism tolerance is INVERTED — and the SK gate must not be ported

The RU and SK canons are native-first: an anglicism is, by default, a defect. **German technical prose is
not.** It keeps *Retrieval, Embedding, Chunking, Prompt, Token, Cache, Deployment, Tool Call, Guardrail,
Trace, Span, Endpoint, Rate Limit* in English, inflected with German articles, and a reader of dpunkt or
heise expects exactly that.

**Two consequences, both mandatory:**

1. **Mechanically porting Slovak's Slovak-led class decisions to German would be a systematic, corpus-wide
   register defect** — 67 pages of "Einbettung", "Zerstückelung", "Zwischenspeicher" reading like a 1990s
   translation.
2. **The "an anglicism is a defect" check MUST NOT be ported.** It is the RU/SK gate. Running it on German
   text actively damages it. Replace it with the German check: *is this word one German engineers actually
   say, and is it inflected correctly?*

Per-term decisions still go through Gate 6 — "keep English" is a ruling that needs attestation like any
other, and a few of these words genuinely are Germanised.

### 6.2 Gender, plural and genitive of every kept-EN noun — **there is no template to copy**

Neither RU nor SK has this section, because both assign gender **morphologically** from the word's shape.
German does not: the gender of a borrowed noun is a lexical fact, and native usage is **genuinely split** —
*der/das Cache*, *der/das Prompt*, *das Embedding*.

So `canon/de/_language.md` needs a table that neither sibling canon has: **article, plural, genitive
singular** for every kept-EN noun, plus an explicit `SPLIT` marker where usage really is divided and a
single pinned choice for the corpus.

**Why it is not cosmetic: wobble within a single page is the loudest possible machine-translation tell.** A
German reader who sees *der Cache* and *das Cache* on one screen stops reading the content.

### 6.3 Denglisch verb morphology

**Participle II and auxiliary, pinned once per borrowed verb** — *gecacht* or *gecached*; *deployt* or
*deployed*; *gemergt*; *habe* or *bin*. Pin them in the canon bootstrap or 67 pages will each re-decide, and
the inconsistency reads as machine output for the same reason 6.2 does. Where no established form exists,
the canon's ruling is **"rephrase"**, not "invent".

### 6.4 Durchkopplung

German binds a multi-word English term into **one hyphenated compound** as soon as it combines with a German
word: *Prompt-Injection-Angriff*, *Retrieval-Qualität*, *Tool-Call-Schleife*. Leaving them space-separated
(*Prompt Injection Angriff*) is both **the commonest error and a reliable MT signature.** The canon states
the rule, the conditions under which the English multiword stays intact (as a quoted term, a product name,
or inside code), and a grep for the space-separated forms belongs in the pre-launch cleanup.

### 6.5 Compounds versus the card label budget — a **width-budgeted** surface

The `create-infographic` skill §4 caps card labels at **≤4 words** with an **11px legibility floor at
360px**, and [`infographics/STYLE.md`](./infographics/STYLE.md) §16 records that composed cards **already
break words mid-word** at that floor (measured: `confiden/t`, `retriev/al`, `re-/index`).

**German compounds are single unbreakable runs where Slovak wraps at spaces.** *Retrieval-Qualität* has one
break opportunity; *Werkzeugaufruf* has none. This is a layout risk, not a translation risk.

- **Prerequisite:** the `hyphens: auto` work (owned by another agent — it does not exist in `src/` today).
  Reference it; German card strings cannot be finalised before it lands.
- **Treat all 91 card strings and all 91 frontmatter titles as a width-budgeted surface, verified by
  rendering at 360px** — not merely as a translation surface. The check is visual, and it is per-string.
- **Lane pill:** `DEMO / PRODUKTION` is **10 characters** against Slovak's `PRODUKCIA` (9) and Russian's
  `ПРОД` (4). It ties the EN worst case (`PRODUCTION`, 10), so it is not a *new* worst case — but verify it
  at 360px anyway, and fall back to `PROD` if the pill wraps. The pill labels are authored inline in the
  markdown, so each locale's copy is its own string.

### 6.6 Anrede — German has a third attractor the Slavic languages lack

RU and SK choose between two persons. German has **three**: *du*, *Sie*, and the impersonal **man** — the
default reflex of German documentation prose, which is no form of address at all and **drifts mid-paragraph**
unless it is named and constrained. Naming the address form in the canon is not enough; the canon must also
name `man`, say exactly which of its uses collide with it, and list what replaces those. The naive form of
this rule — "ban `man`" — is wrong, and §7.1 records why.

**And German's choice of address is not only a pronoun choice — it is a *verb form* choice.** The imperative
is the corpus's highest-frequency construction, and it is built differently for each person: *Gib eine
Meldung zurück* versus *Geben Sie eine Meldung zurück*. Whichever way §7.1 falls, the decision propagates
into nearly every instruction on all 67 pages, which is why it belongs in the injection block and not merely
in the canon.

### 6.7 Gendering — an axis with no RU/SK analogue and no neutral default

There is no unmarked option: generic masculine, double naming, Genderstern/Doppelpunkt, and systematic
rephrasing are all *choices*, and each is read as a position by some part of the audience. **An undecided
corpus wobbles between them, and a German reader reads wobble as machine output** — which is the real risk
here, more than any individual choice. Decide once; see §7.2.

### 6.8 Typography

- **„…" primary with ‚…' nested** — identical to Slovak, so that part of the SK canon ports directly.
- **»…« must be forbidden by name.** It is perfectly legitimate German and *will* appear if it is not
  explicitly excluded; a corpus mixing „…" and »…« is inconsistent, not stylish. See §7.6.
- **ß vs. Swiss ss** — decided; see §7.3.
- **Thousands separator** — decided; see §7.4.
- **Percent** — decided, and it **diverges** from the RU/SK convention; see §7.5. Flag it in the canon as an
  intentional divergence, or a future consistency pass will "correct" it back.

### 6.9 No sister-language interference slot — what fills it

Slovak's anti-bohemism section was its load-bearing artefact. German has no near-identical sister language,
so the slot is filled by three different things, and `canon/de/_language.md` should carry them under one
heading:

1. **Denglisch morphology** (§6.2, §6.3);
2. **English syntactic order** — Satzklammer violations (the finite verb's partner stranded or misplaced),
   the *von*-genitive where German wants a compound or a real genitive (*die Qualität von dem Retrieval* →
   *die Retrieval-Qualität*), progressive constructions, *nicht* placement, and the English cleft (*Es ist
   der Prompt, der…*);
3. **Regional variance** — Swiss and Austrian forms that a Bundesdeutsch corpus should not mix in.

### 6.10 The print bar must name its exemplars

**dpunkt, Rheinwerk, O'Reilly DE, heise/iX/c't** — and explicitly **NOT enterprise marketing German**, which
is the register a model reaches for when told "professional German" and which produces nominal, agentless,
buzzword-dense prose that no engineer writes. Name both halves in the canon; the negative half is the one
that does the work.

### 6.11 One upside — German gets a real stemmer

Unlike Slovak, **German has a working lunr stemmer**: `lunr.de.js` ships with the search plugin and `de` is
already in the `LUNR_SUPPORTED_LANGUAGES` whitelist in `docusaurus.config.ts`. Adding `de` to `LOCALES`
enables it with **zero extra work** — a functional payoff on top of the correctness one.

**Caveat worth a ten-minute test at scaffold time:** German compounds defeat stemming — a search for
*Werkzeug* will not match *Werkzeugaufruf*. And if hyphens tokenise, then §6.4's hyphenated compounds are
*more* searchable than solid ones, which is a second, independent reason to get Durchkopplung right. Test
both before the pilot; record the result in the scaffold issue.

---

## 7. Decisions — settled, with reasoning and reopening conditions

Recorded the way the SK canon records rulings: the decision, the linguistic reason, the attestation, and
**the condition under which it reopens.** Verified with the cross-family model (Sol) before pinning.

**Two of the three recommendations that went in came back amended.** That is the gate working, and both
amendments are recorded rather than quietly absorbed.

### 7.1 Anrede — `Sie`. And `man` is *restricted*, not banned

**Decision.** The polite form **`Sie`**, capitalised (with `Ihr/Ihre/Ihnen`), corpus-wide — **and every
instruction in the Sie-imperative**: *Öffnen Sie die Konsole*, *Geben Sie eine Meldung zurück*.

> **Decision history — this row was reversed, and the record says so.**
> **Made as `du`** when this playbook was written, on corpus-internal symmetry with «ты»/„ty".
> **Reversed to `Sie` by the owner on 2026-07-28**, on the attestation the `du` ruling itself had recorded
> against it. A canon that quietly overwrites its own reversals is the SK Fáza 26 failure mode; this is why
> the original decision is left legible above the new one instead of being deleted.

**Reason — the attestation, which is unanimous.** Every openable German publisher source that was checked
uses `Sie`: the Rheinwerk Openbook; two dpunkt Leseproben (76×*Sie/Ihnen* vs 1×*du*, and 35×*Sie* vs
0×*du*); the GNOME translation guidelines ("grundsätzlich in der Höflichkeitsform"); and Microsoft's
localisation style guide, which reserves `du` for readers **under 18**. The tekom article confirms a `du`
trend in the industry but advises in the same direction ("Mit dem Sie macht man im Zweifelsfall nichts
Grundsätzliches verkehrt").

**And the counter-case collapsed on inspection.** The three "independent exemplars" once cited for `du` are
**one style family, not three data points** — dpunkt belongs to Heise Medien and has run the German
O'Reilly programme since 2015. So the unanimous `Sie` evidence never had a second strand facing it; it had
the same strand counted three times.

**The load-bearing reason is the missing check.** The German locale has **no native proofreader** — the
owner reads Russian and Slovak, his German is ~A1. With no human able to hear whether an unconventional
register lands as *informal and modern* or as *foreign*, the attested publisher norm beats cross-locale
symmetry. `du` was consistency with «ты»/„ty"; `Sie` is what a German engineer actually expects from a
technical handbook.

**What is now recorded as a divergence is RU/SK, not German publishing.** The canon flags the address form
as a deliberate departure from the sister locales — the same shape as the `KI` vs `AI` divergence in §3 of
the canon — so a later consistency pass does not "correct" it back.

**Decision — `man`.** The proposal to forbid `man` by name was **rejected on linguistic grounds and is not
adopted.** `Sie` is a personal address; `man` is an indefinite pronoun with general reference. They do
different jobs, and a blanket ban conflates them. The rule is **restriction, not prohibition**:

- **`man` is forbidden for the reader's own actions.** That is where it collides with the address form and
  produces the mid-paragraph drift §6.6 warns about. Replace with, in order of preference: `Sie`; the
  **Sie-imperative** (*Öffnen Sie …*); the passive (*wird gespeichert*); a reflexive construction (*lässt
  sich prüfen*); an infinitive (*zum Prüfen*); a factual subject (*Der Retriever liefert …*). `wir` only for
  a thought the text and the reader perform together. *(The replacement construction changed with the
  reversal: it used to be the du-imperative *Öffne …*.)*
- **`man` stays correct for genuine statements about people in general**, where the reader is not the
  subject: *Was man unter einem Agenten versteht, hängt vom Kontext ab.*

The gate to run in review is therefore not "grep for `man`" but *"does this `man` mean the reader?"* — and
note that `man` sits **closer** to the `Sie` register than it did to `du`, so it is now less conspicuous,
not less wrong.

**Reopening condition.** A binding publisher house style prescribing `du`; or a native-reader finding
(Gate 7) that `Sie` reads as distant for this audience. Owner decision either way.

### 7.2 Gendering — rephrase the role away; generic masculine as the fallback

**Decision.** Prefer to **formulate the role away** — *beim Review* not *der Reviewer*, *im Betrieb* not
*der Betreiber*, *das Entwicklungsteam* not *die Entwickler* — by nominalisation, collective noun, or
factual reference. Where that fails, **generic masculine.** No Genderstern, no Doppelpunkt, no Binnen-I, no
double-naming requirement.

**Reason.** The mechanism is nominalisation / collective reference / factual subject, which removes the
person-denoting noun rather than decorating it.

**⚠️ Amendment — the justification is narrower than proposed.** The claim that this is the *least marked*
choice is **UNDECIDED and must not be written into the canon as fact.** Publisher usage is genuinely split:
dpunkt uses the Doppelpunkt consistently in a current Scrum title alongside paired forms and generic
masculines elsewhere; O'Reilly DE ships both paired forms and explicitly generic-masculine translations;
Rheinwerk uses generic masculines in book marketing but Genderstern and paired forms on event pages; heise
Developer's own author guidelines prescribe the Doppelpunkt. **There is no industry rule to follow.** The
amtliche Regelwerk (2024, pp. 153–154) places Doppelpunkt, Asterisk and Unterstrich *inside* words outside
the core inventory of German orthography and names unresolved grammatical consequences (*der\*die
Präsident\*in*) — that is a real fact, and it supports the decision as an *orthographic* choice; it does not
support a claim about political neutrality. **So the canon records this as a consistency decision, not as a
neutrality claim.** §6.7's real risk is wobble, and any single consistent choice removes it.

**Where rephrasing breaks — name these in the canon, or each renderer improvises.** They carry **more**
weight since §7.1 flipped to `Sie`: an earlier version of the canon justified the rephrase rule partly by
claiming the `du` address "dodges most gendering occurrences by construction". That justification is void —
the polite form does not dodge agent nouns — so these four are where the corpus actually has to decide, and
they occur more often than the original framing implied.

1. **Responsibility** — *Der Betreiber haftet.*
2. **Authorisation** — *Nur Administratoren dürfen Schlüssel rotieren.*
3. **Role contrast** — *Autor und Reviewer müssen verschieden sein.*
4. **Defined framework roles** — *Product Owner*, *Scrum Master*.

In all four, the generic masculine applies. For a *specific, known* person, the actual form applies.

**Reopening condition.** A binding style guide; a change to the amtliche Regelung; a legal requirement for
person-precision; or audience testing that clearly prefers another form.

### 7.3 ß vs. ss — regular ß/ss distinction, Bundesdeutsch

**Decision.** Distinguish **ß and ss by rule**; no blanket Swiss `ss`.

**Reason.** **ß** after a long vowel or diphthong (*Maß, Straße, heißen*), **ss** after a short vowel
(*Masse, Fluss, müssen*). Blanket `ss` is a regional Swiss/Liechtenstein variant and blurs real minimal
pairs (*Maße* / *Masse*).

**Attestation — verified in the primary source, not from memory.** Amtliches Regelwerk **§ 25**, with **E2**
restricting blanket `ss` to Switzerland and Liechtenstein ("in der Schweiz und in Liechtenstein kann immer
ss geschrieben werden") or to the technical case where ß is unavailable.

**Reopening condition.** A Swiss/Liechtenstein regional edition; ß technically unavailable; all-caps
setting (where both **STRAẞE** and **STRASSE** are permitted).

### 7.4 Thousands separator — thousands point, with the norm's dissent on the record

**Decision.** **`137.813`** — thousands point. Decimal separator: **comma** (`3,14`). Ranges: **`10–20`**,
en dash, no spaces.

**Reason and the conflict, stated honestly.** This is the one decision here where the norm and the print bar
disagree, so both are recorded:

- **DIN 5008:2020-03 §11.2** recommends grouping in threes with a **space** above four digits, and Duden's
  number guidance gives *34 500* / *3 134 512*. On a web page that means a narrow no-break space (U+202F).
- **The §6.10 print-bar exemplars all use the point**: dpunkt/O'Reilly *4.319*, *100.000*; Rheinwerk
  *12.000*; heise *100.000*.

**The ruling follows the print bar**, because §6.10 makes those publications the calibration target and
because DIN 5008 governs business correspondence and word processing rather than book typography. Unspaced
`137813` is wrong under both and is excluded. Note the stakes are low — four-plus-digit figures barely occur
in this corpus's prose — which is itself a reason not to spend a native reader's attention on it.

For the range dash the sources also split (DIN §9.4 normative sets *10 – 20*; annex F.5 and Duden book
setting set compressed *10–20*); a typeset online handbook takes the compressed form.

**Reopening condition.** A binding house style; the renderer emitting U+202F unreliably; or numbers
appearing as code, database values or API literals, where the source form is kept verbatim.

### 7.5 Percent — `20 %`, and the German locale therefore DEVIATES from the inherited convention

**Decision.** **`20 %`** — a narrow no-break space between value and sign. **The project's inherited
tight-percent convention (`20%`, settled 2026-07 for RU/SK) does not carry into German.**

**Reason.** In a percentage the sign behaves as a postposed unit name and is separated from the value by a
fixed space.

**Attestation — and note that unlike §7.4 the sources do NOT split.** Duden gives *"5 Prozent oder 5 %"*;
DIN 5008:2020-03 §10.7 ("Prozent- und Promillezeichen") likewise requires the space. Both agree.

**Exception.** Adjectival derivation is written solid: **`20%ig`** (Duden attests *100%ig*), or spelled
`20-prozentig`.

**Why this deviation is correct rather than a break in consistency.** A typographic convention is a property
of a **locale**, not of a corpus. Forcing `20%` into German for cross-locale symmetry would import a defect
in exchange for a symmetry no reader can perceive — only one locale is on screen at a time. Record it in
the canon as an explicit, reasoned divergence so nobody "fixes" it later.

**Reopening condition.** Only for code, UI strings or foreign-language quotations reproduced verbatim, and
for genuine derivations/compounds. Parallelism with the other locales is explicitly *not* a reason.

### 7.6 Quotation marks

**Decision.** **„…"** primary, **‚…'** nested — identical to Slovak, so the SK canon section ports.
**»…« is forbidden by name.** It is legitimate German and will appear unless it is explicitly excluded;
a corpus mixing both is inconsistent, not stylish. English quotations inside German running text take the
German marks.

**Reopening condition.** None foreseen; a corpus-wide switch would be a mechanical find-and-replace, so the
cost of changing later is low and the cost of *inconsistency* is what is being avoided.

---

## 8. Mechanics (Docusaurus)

Mostly as SK. The differences are flagged.

- **Locale registration:** add `de` to `UNRELEASED_LOCALES` in `docusaurus.config.ts` plus a `localeConfigs`
  label. The config is locale-list-driven, so the browser-language detector, the switcher and the search
  plugin pick `de` up with no other code change. Content mirrors the **EN default in `docs/` and
  `docs-ai-sdlc/`** under `i18n/de/docusaurus-plugin-content-docs*/current/**`.
- **Gated visibility:** merge German content to `main` continuously with `de` in `UNRELEASED_LOCALES`; CI
  builds it via `HANDBOOK_INCLUDE_UNRELEASED=1` while the deployed build excludes it. Flip to
  `RELEASED_LOCALES` only at launch. Docusaurus falls back to the **default locale, EN**, for missing pages —
  a public dropdown pointing at a half-translated locale undermines the showcase purpose.
- **`scripts/i18n-link-check.sh` already understands the gating**: it fails on a broken link in a released
  locale or on a *translated* page in an unreleased one, and tolerates a broken link only where an
  unreleased-locale page has no translation file yet. It needs no change for German.
- **Theme strings:** run `npm run write-translations -- --locale de`. **74 of `code.json`'s 85 keys auto-fill
  from `@docusaurus/theme-translations/locales/de`**; only the **11 `landing.*` keys are authored**. Theme
  chrome in English inside German pages is a defect.
- **Sidebar category labels — `current.json` only.** Set every category label in
  `i18n/de/docusaurus-plugin-content-docs*/current.json` under
  `sidebar.<sidebarId>.category.<English label>` (the English label is the lookup key). **Do not create a
  single `_category_.json` under `i18n/de/`** — Docusaurus overrides such a file with `current.json` at
  render time, so it does not render and editing it silently does nothing. The 58 pre-existing locale copies
  were deleted in #290 after a measured rebuild showed the generated sidebars byte-identical without them.
  Structure (`position`, `link`) comes from the **EN** `_category_.json` in `docs/`, which decides for every
  locale. *A label left out of `current.json` renders as the English source string — that regression has
  already happened once, on the EN-canonical flip.*
- **Glossary anchors:** German glossary headings produce German slugs. Verify anchors in the build; do not
  assume SK or RU slug parity.
- **Do not translate:** code blocks and identifiers, product names, Mermaid node IDs (labels and captions DO
  translate and pass the prose gates), YouTube video content.
- **Local search:** confirmed working for `de` — see §6.11.

**Code touchpoints that a launch must not miss** (each is a real hard-coded string or test, verified
2026-07-28):

- `COURSES[].languages` in `docusaurus.config.ts` (two occurrences) — currently
  `['English', 'Русский', 'Slovenčina']`, rendered on the landing page.
- `src/theme/BlogListPage/index.tsx` — `EnglishOnlyNote` hard-codes **"English, Russian and Slovak"** in
  untranslated JSX.
- `e2e/locale-detection.mjs` — uses **`de-DE` as its *unsupported*-language fixture**. The day German ships,
  that assertion inverts and becomes a **false pass**; it must be re-pointed at a genuinely unsupported
  locale.
- `README.md` and `CLAUDE.md` — the locale model and the locale-parity rule.

---

## 9. Unit of work and sequencing

Waves, part by part, batched by page — as SK. A deepened lesson is TWO pages, so ≈2–4 pages per PR.

**The sequencing lesson from Slovak is the reason this section is longer than SK's.** The SK playbook
planned **7 phases and "16–20 PRs"**; the SK canon records **26 numbered phases**. The unplanned ones
cluster at exactly two points, and they are scheduled here rather than discovered:

| Phase | What |
|---|---|
| **0** | Infrastructure: `de` scaffold as gated UNRELEASED; Gate 0 parity script; card hyphenation; the stemmer test (§6.11). |
| **1** | Canon bootstrap: `canon/de/_language.md` (voice, the `man` **restriction**, gendering, typography, Denglisch morphology, Durchkopplung, English-syntax tells, print bar) + the **kept-EN register** (§6.2/§6.3) + both course ledgers seeded + the full German glossary = all term decisions materialised, each with a Gate 6 attestation. |
| **2** | **Pilot** — ONE mid-complexity lesson, both its pages, through the FULL stack (Gates 0–6, cold read ×2). Recommended: *Tool use*, as SK — long enough to exercise every gate, central enough that its terminology feeds everything after, **and directly comparable to the Slovak pilot.** |
| **2b** | ⚠️ **Scheduled risk cluster 1 of 2 — pilot re-edit.** |
| **2c** | ⚠️ **Method change: full reconstruction-from-the-proposition pass.** Budgeted, not discovered. |
| **2d** | ⚠️ **Polish pass.** |
| **3** | **Native-reader calibration** (Gate 7) + method retro: amend canon and persona instructions with what leaked. **Waves do not start until the retro lands.** |
| **4–7** | RAG waves: Part I (13 files) → Part II (14) → Part III (10) → intro+glossary (2). |
| **8** | RAG corpus milestone pass (consistency + managing editor + cold-read spot checks). |
| **9–10** | AI-SDLC waves: intro+glossary+Parts I–II (12 files) → Parts III–V (16). |
| **11** | AI-SDLC corpus milestone pass. |
| **12** | UI strings: `code.json`, navbar, footer, both `current.json` files (no `_category_.json` — see §8). |
| **13** | ⚠️ **Scheduled risk cluster 2 of 2 — pre-launch cross-cutting cleanup** across all 67 pages. Delta editing, not re-translation. In SK this was Fáza 25: a deferred backlog discovered at launch time and never planned. |
| **14** | **Launch:** flip `de` to `RELEASED_LOCALES`, plus every code touchpoint in §8, plus the locale-parity rule. |
| **15** | ⚠️ **Post-launch pilot copy-edit** after an external review of the live pages. In SK this was Fáza 26 — prose only, zero fact movement, a large diff is a failure. Also where `DISPUTED` rows get their reckoning. |

**19 named phases. Budget ≈27** — roughly **1.4×** — because the two clusters above being scheduled does not
mean no *other* surprise appears; it means the two known ones no longer surprise you. Expect **≈25–32 PRs**
end to end (SK ran 26 phases over a 38-page corpus; German is 67 pages).

**Why the clusters land where they do.** Cluster 1 is the pilot correcting the *method*, and it is
structural: the first real page is where the canon meets prose and loses. Cluster 2 is the corpus paying
for every deferral: items waved through as "fix in the milestone pass" accumulate, and the launch gate is
where they come due.

---

## 10. Preconditions

- **Both courses must be content-complete and clean at wave start.** German inherits whatever the skeleton
  extractor reads. During German waves, treat EN/RU/SK content as frozen; a mid-wave EN change re-enters
  the affected German page into the pipeline.
- **Gate 0 and the card hyphenation must land before the pilot**, not before launch — the pilot is what
  calibrates the gates, and it cannot calibrate a gate that does not exist.
- **`canon/de/_language.md` §kept-EN register must be complete before page one.** SK's most expensive
  correction (Fáza 25, all 38 pages) was a term-direction drift that a complete Phase 1 would have
  prevented.

---

## 11. What the orchestrator sends to the skills (per lesson)

To **`authoring-team`**: target language `de` (audience-primary for the run); skeleton extracted from the EN
page (the writer never sees EN/RU/SK prose); voice/register per `canon/de/_language.md`; term decisions from
the German glossary/ledger, **including the kept-EN register with article, plural and genitive**; 1–2
existing German sibling pages for voice calibration (post-pilot only); house skeleton strings per canon;
figures composed natively — **RU and SK figures do not port**; coined German figures *and terms* → probation
list in the handoff note. **Run Layer 1.5 first** (Gate 5).

To **`editorial-team`**: primary language `de`; naive reader excludes EN entirely; the literary editor
carries the §6.9 checks (Denglisch morphology, English syntactic order, regional variance) **instead of**
the SK anti-bohemism check and **without** the RU/SK anti-anglicism check (§6.1); collocation
web-verification allowed and encouraged; canon = the German section; **mandatory cold read ×2**; deliver via
PR with canon updates in the same PR.

To **Sol (cross-family judge)**: monolingual German, no source text, verdict + **named linguistic tell**
per string (Gate 4); and, separately, attestation-ranked term adjudication with the MT-signal check
(Gate 6).

---

## 12. Effort shape (for planning, not billing)

**67 pages / 137 813 EN words**, across two courses — versus the 38 pages the SK playbook planned against.
Per page ≈ 1 skeleton extractor + 1 Layer-1.5 pass + 1 writer + ~6 gate personas + 2×2 cold-read personas.
Plus Phase 0/1 infrastructure, two corpus milestone passes, the two scheduled clusters, and the UI-string
phase.

The honest comparison: **German is ~1.76× Slovak's prose surface and carries one entirely new canon section
(§6.2, the kept-EN morphology register) that no sibling locale could donate a template for.** Everything
else is a port.
