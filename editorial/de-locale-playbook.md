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

**Cannot catch — established by the pilot (2026-07-28), and it is structural, not a tuning problem: Gate 5
judges strings IN ISOLATION and therefore cannot see a page-level pattern.** Every string can win its own
blind round and the page can still read as machine output. Three observed instances, all on the pilot pages:

- **heading-sequence rhythm** — three counted headings in a row („Der Tool-Call in vier Schritten", „Vier
  Fehlerbilder …", „Drei Kosten …"). Each is a good German heading; the run is a listicle metronome.
- **one referent under four names** — `Bestand` / `Satz an Tools` / `Tool-Liste` / `Tool-Katalog`. This is
  the wobble the canon calls the loudest MT tell, one level up from gender.
- **paragraph cadence** — eleven consecutive paragraphs ending on a pointed short sentence.

**Also established: the blind cross-model judge and the naive cold reader disagree about headings
systematically, and neither is right alone.** The judge rewards `Nominalstil` and information structure —
both genuine German heading virtues; the reader calls several of the same headings stilted. Do not resolve
this by picking a favourite judge.

⇒ **A page-level consistency check must follow Gate 5** (heading sequence as a whole, one referent = one
name, no cadence metronome). It is a *page* pass, not a string pass, and it is the reason Gate 5 alone did
not protect the layer it exists for.

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

### Gate 6.5 — reconciliation pass over parallel attestation batches *(added after the pilot, 2026-07-28)*

**Numbered 6.5 deliberately: it sits between 6 and 7 and renumbers nothing.**

Gate 6 is run in parallel batches because that is the only way it finishes. The pilot ran **five**. Two of
the five collided at the seam, **and each was locally right** — no batch can see its neighbours, so no batch
can detect the collision:

1. **`write tools` / `read tools`.** Batch B attested the German participle skeleton („rein **lesende**
   Services", „eine **schreibende** Transaktion") and proposed „schreibende **Werkzeuge**". Batch C had
   measured `Tools` : `Werkzeuge` ≈ **15 : 2–3** in native German agent prose and confirmed `Tool` as
   kept-EN. → Keep the attested skeleton, substitute the corpus's settled head noun: **„schreibende Tools"**.
2. **`runtime` in the fan-out sentence.** Batch C's worked example wrote „**Die Laufzeitumgebung** verteilt
   die Aufrufe …". Batch E, which studied that referent specifically, rules `Laufzeitumgebung` the wrong
   referent (JVM/CLR-class host platform) and `Laufzeit` a categorical false friend. → **Batch E wins**;
   „**Ihre Anwendung** verteilt die Aufrufe …".

**Without this step both would have shipped** — a head noun against a corpus-wide decision and a wrong
referent — and **both would have passed every fluency gate**, because both are fluent German.

**Procedure.** One agent, all batch outputs at once, no new research: (a) build the union of every ruled
term; (b) flag any term two batches touched, and any term whose *worked example* uses a word another batch
ruled on; (c) resolve by the ranked-authority rule, with the batch that studied the referent **specifically**
outranking the batch that used it in passing; (d) write the resolution into the term sheet as binding, with
both sides recorded. **The output of Gate 6 is not the batches — it is the reconciled sheet.**

**Cannot catch:** anything a single batch got wrong on its own; this gate only sees disagreements.

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

### The gates' own repair record — two mechanical gates could not accept a partial locale *(pilot, 2026-07-28)*

Both were found empirically, by staging the English pages as `i18n/de/**` and running the gates **before a
line of German existed**. Neither was a bug in the German; both were gates that could not represent the state
the pilot was in.

- **`scripts/locale_parity.py`, file-set check.** The moment `current/` exists it compared the **full** file
  set and reported every not-yet-translated page as a defect. Correct for a *released* locale; for an
  *unreleased* one, partial translation is the **normal state**. The script already knew the asymmetry —
  `missing_translation()` applies it to a wholly absent course — just not one level down. **Effect without
  the fix: the locale would have been all-or-nothing and the pilot could never have gone green.** Fix:
  missing pages are informational in an unreleased locale; the **reverse** direction (a page with no English
  source) stays a hard error in *every* locale — that is the half that must not fail open.
- **`scripts/i18n-link-check.sh`, tolerance rule.** It tolerated a broken link only when the **source** page
  was an untranslated EN fallback. But the first translated lesson of a locale necessarily links to
  untranslated siblings and an untranslated glossary, and Docusaurus cannot resolve `.md` links across the
  fallback/translation boundary. The gate's own header comment promised it "maintains itself as locales fill
  in"; **in fact it did so only at 0 % and at 100 %.** Fix: the tolerance now judges the **pair** — tolerated
  when the source is in an unreleased locale **and the target is not yet translated there**. Once the target
  exists the link must resolve, so a wrong glossary anchor into an already-translated page still fails
  (#307). Self-test grew from 9 to 19 cases, 10 of them new pair cases.

> **The generalisable lesson, and it is about gate design, not about these two scripts: both gates were
> written against a locale's END state and were untested against its FIRST state.** A gate that checks the
> target state looks like a working gate for as long as nobody drives the transition. ⇒ **The pilot is the
> first moment the gates themselves are tested, and it must be run BEFORE the prose, not after it** — stage
> the English pages in the locale tree and run the whole mechanical stack against them.

**Two further findings about gate *inputs*, from the same pilot — both are the same failure:**

- **Do not gate an artefact that is still being produced.** A mechanical gate was run against a file an agent
  was still writing and reported a defect that did not exist. The gate judged correctly — about an
  intermediate state, which is not a subject of review.
- **A gate's input preparation is part of the gate.** The register judge was fed sentences truncated at 300
  characters and returned **eleven "Satzabbruch" verdicts** that were artefacts of the extraction, not
  properties of the text. (The judge flagged the pattern itself.) ⇒ When standing up any gate, verify the
  **input** first — complete? finished? unmutilated? — then read the verdict.

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
- **Thousands separator** — decided: **narrow no-break space**, `1 000 000`; see §7.4. This row was
  **reversed on 2026-07-28** (it used to say thousands point) and the reversal is on the record there.
- **Percent** — decided: **`20 %`**, and it **diverges** from the RU/SK convention; see §7.5. Flag it in the
  canon as an intentional divergence, or a future consistency pass will "correct" it back.
- **Both of those rows once contradicted the canon**, which said tight percent and narrow-space thousands —
  so whichever document a renderer opened first won. Reconciled 2026-07-28 under the canon's new
  **Vorrangregel** (`canon/de/_language.md` § Typografie): *where a project-wide convention collides with an
  attested German norm, German wins, and the divergence from the sister locales is recorded rather than
  silently absorbed.* The canon is the normative home of that rule; this playbook records how it was reached.

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

> ### The standing rule these decisions now share (2026-07-28)
>
> **Where a project-wide convention collides with an attested German norm, German wins — and the divergence
> from the other locales is recorded, not silently absorbed.**
>
> It is the principle the owner used to settle the Anrede (§7.1): `du` was cross-locale consistency with
> «ты»/„ty", `Sie` is what German publishing actually attests, and the attested norm won **because there is
> no native German reader on this project to hear whether an unconventional choice lands as deliberate or as
> foreign.** §7.5 (percent) is the same question in another guise and gets the same answer.
>
> **The counter-consideration is real and is being traded knowingly:** cross-locale *visual* consistency —
> the same number looking identical on the EN, RU, SK and DE pages — is given up. It is worth giving up
> because only one locale is ever on screen, while the norm is visible to a German reader in every sentence.
> A later consistency pass that "fixes" one of these rows back is undoing an owner decision.
>
> **What the rule does not decide:** rows where the *German sources themselves* disagree (DIN 5008 vs.
> Duden). Those stay DISPUTED, or are decided by register with the losing source left on the record — see
> §7.4's print-bar dissent and the range-dash split in the canon.
>
> The normative statement lives in `canon/de/_language.md` § Typografie ("Vorrangregel"); this box is the
> playbook's record of how it was reached.

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

### 7.4 Thousands separator — narrow no-break space, with the print bar's dissent on the record

**Decision.** **`137 813`** — narrow no-break space (U+202F), grouping in threes. Four-digit numbers stay
ungrouped (`5423`). Decimal separator: **comma** (`3,14`). Ranges: **`10–20`**, en dash, no spaces.
**Point only for money amounts** (`5.340 EUR`) — that exception comes from the norm itself.

> **Decision history — this row was reversed, and the record says so.**
> **Made as the thousands point** (`137.813`) when this playbook was written, on the §6.10 print bar.
> The canon meanwhile carried the **narrow space**, marked DISPUTED — so the two documents disagreed and
> whichever a renderer read first won. **Reversed to the space by the owner on 2026-07-28**, on the standing
> rule above: the separator follows DIN 5008. The original decision is left legible here rather than deleted
> — a canon that quietly overwrites its own reversals is the SK Fáza 26 failure mode.

**Attestation — verified in this pass, and note that DIN and Duden do *not* split here.**

- **DIN 5008:2020, §11.2:** "Zahlen mit mehr als drei Stellen links oder rechts des Kommas werden mithilfe
  eines **ganzen Leerschritts** – vom Komma ausgehend – in dreistellige Gruppen gegliedert." Examples
  *7 654 321,08 CHF*, *0,373 18 g*. Four digits are optional either way: "Bei vierstelligen Zahlen ist neben
  der Schreibung mit Zwischenraum bzw. ganzem Leerschritt auch die ohne möglich." Money is the one exception:
  "Bei Geldbeträgen können aus Sicherheitsgründen auch Punkte zur Gliederung verwendet werden."
- **Duden:** "Ganze Zahlen mit 5 oder mehr Ziffern werden von der Endziffer aus durch **Zwischenräume** in
  dreistellige Gruppen gegliedert" — *34 500*, *600 000*, *3 134 512*.

**What is given up, honestly.** The §6.10 print-bar exemplars all use the point — dpunkt/O'Reilly *4.319*,
*100.000*; Rheinwerk *12.000*; heise *100.000* — and so does every system de-DE locale. That is widespread
German **practice**, but it is not the norm, and in this corpus it additionally collides with the English
decimal point that appears in code and numeric examples on the same page. The norm decides; the practice
stays on the record as dissent.

**One precision the earlier version got slightly wrong.** DIN prescribes a *full* space for thousands
(a typewriter/word-processing context) and a *narrow fixed* space only for the percent sign. A full space in
typeset prose reads as a word gap, so the corpus sets **U+202F as the typographic realisation of DIN's
grouping rule** and says so in the canon, rather than presenting U+202F as DIN's literal letter. Fallback
U+00A0; never a plain space, never the point outside money, never unspaced (`137813` is wrong under both
sources). Stakes stay low — four-plus-digit figures barely occur in this corpus's prose.

For the range dash the sources genuinely **do** split — DIN's normative part sets *24. – 25. Oktober*, while
Duden sets no space (*24.–25. Oktober*), as do korrekturen.de and the GfdS. A typeset handbook takes the
compressed form; that is a **register** ruling, not the standing rule above, and both sources are kept in the
canon row.

**Reopening condition.** A binding house style; the renderer emitting U+202F unreliably; or numbers
appearing as code, database values or API literals, where the source form is kept verbatim. Consistency with
the other locales is explicitly *not* a reason.

### 7.5 Percent — `20 %`, and the German locale therefore DEVIATES from the inherited convention

**Decision.** **`20 %`** — a narrow no-break space between value and sign. **The project's inherited
tight-percent convention (`20%`, settled 2026-07 for RU/SK) does not carry into German.**

**Reason.** In a percentage the sign behaves as a postposed unit name and is separated from the value by a
fixed space.

> **The canon disagreed with this row until 2026-07-28.** `canon/de/_language.md` carried **tight `20%`**,
> marked DISPUTED, and called it "der auffälligste bewusste Normbruch des deutschen Kanons" — while this
> playbook already said `20 %`. Two documents, opposite rules, and whichever a renderer opened first won.
> The owner settled it on the standing rule above; the canon row is now SETTLED at `20 %` with its own
> reversal note. Recorded here because the disagreement, not just its outcome, is the lesson.

**Attestation — re-verified in this pass, and unlike §7.4 the sources do NOT split.**

- **DIN 5008:2020, §10.7 ("Prozent- und Promillezeichen"):** "Prozent- und Promillezeichen sind durch einen
  Leerschritt von der zugehörigen Zahl zu trennen." For text-processing systems the standard specifies
  "einen **kleineren Zwischenraum (Festabstand)**" — i.e. U+202F is the norm's own prescription, not an
  interpretation — plus "Die Trennung von Zahl und Prozent- bzw. Promillezeichen am Zeilenende sollte
  vermieden werden."
- **Duden** (Rechtschreibung, 24th ed.): *"5 Prozent oder 5 %"*.
- **typolexikon:** "Zwischen Zahl und Prozentzeichen wird **immer** ein Leerraumzeichen gesetzt."
- **korrekturen.de** names the contrast explicitly: "**Anders als teilweise im Englischen** werden im
  Deutschen Maßeinheiten und Symbole stets mit Abstand vor oder hinter die Zahl gestellt: € 25, **80 %**,
  3 t Gewicht." The tight form is an import from English typography, and a German source says so.

**Exception.** Adjectival derivation is written solid: **`20%ig`** (Duden D 30.1 attests *75%ig*), or spelled
`20-prozentig`; and `5-%-Klausel`, which the amtliches Regelwerk 2024 lists under *fünf*. DIN states the
exception in the same clause: "Das Leerzeichen entfällt bei Ableitungen."

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

**Checked against the standing rule — no collision.** The `„…"` choice is not carried by Slovak symmetry
alone: it is independently the form the amtliches Regelwerk 2024 uses in its own examples (§ 79). So no
German norm is being traded for a project convention here, and the row may stay a house ruling. `»…«`
remains legitimate German that this corpus simply does not use.

### 7.7 Every other typography row, checked against the standing rule (2026-07-28)

The percent and thousands rows were found by accident, so the whole typography inventory in
`canon/de/_language.md` was swept for the same shape: *a value inherited from the project-wide or RU/SK
convention that a German norm contradicts.* A confirmed row is as useful as a changed one.

| Row | Verdict | Basis |
| --- | --- | --- |
| Quotation marks `„…"` / `‚…'` | **confirmed** | Amtliches Regelwerk 2024 § 79 sets exactly this. Matches SK by coincidence, not by dependence. |
| `»…«` excluded by name | **confirmed** (house) | Legitimate German, but not the Regelwerk's own form; excluding it costs no norm. |
| `ß` vs. blanket `ss` | **confirmed** | Regelwerk § 25 + E2; a German-internal regional question, no inherited convention involved. |
| Decimal **comma** | **confirmed** | German norm; RU/SK also use the comma, so the inherited value happens to be right. |
| Thousands separator | **changed** → narrow no-break space | DIN 5008 §11.2 + Duden agree on the space; the point survives only for money amounts. Print-bar dissent recorded. |
| Percent sign | **changed** → `20 %` | DIN 5008 §10.7 + Duden + typolexikon + korrekturen.de, unanimous. Divergence from EN/RU/SK recorded. |
| Range dash, compressed `10–20` | **confirmed**, and promoted from DISPUTED to *settled by register* | Duden, korrekturen.de and the GfdS set it compressed; DIN's normative part spaces it. A DIN-vs-Duden split, so the standing rule does not apply — the book register decides and both sources stay on the record. |
| No-break space between value and unit (`128 GB`, `24 h`) | **confirmed** | German norm; korrekturen.de names the one exception, angle degrees (`45°`, but `45 °C`). The clause that exempted `%` from this row was the contradiction and is gone. |
| Sentence-initial capitalisation of lowercase-styled terms (`Top-K`, `vLLM`) | **confirmed** | German sentence-initial capitalisation; no inherited convention pushes against it. The canon's advice to rebuild the sentence rather than force the capital stands. |
| Durchkopplung / hyphenation of English multiword terms | **confirmed**, out of scope here | Orthography, not typography, and already decided against the Regelwerk § 45 E1 (canon §1.3.3) — no RU/SK convention feeds it. |

| **Gedankenstrich (parenthetical / title separator)** | **changed** → U+2013 **with** spaces; U+2014 dropped | **Ruled in #313; corpus rolled out in #314 (21 occurrences, counted); tally corrected in #315.** This row is added here because the sweep MISSED the value and the playbook still did not record it. Canon: `_language.md` § Typografie. **The term-ledger pass (#275/#276) reached the same conclusion independently and contributed the tier-1 attestation the original ruling lacked** — DIN 5008 prescribes the Halbgeviertstrich with a space each side and does not sanction the Geviertstrich at all; the Regelwerk § 77 section uses **66 × U+2013, 0 × U+2014**; measured across eight German sources, **≈ 220 en dashes, zero em dashes**. |

**The sweep above missed a row, and the miss is instructive rather than embarrassing.** It swept for values
inherited **from RU/SK** — and the em dash is inherited from **EN**, which no row was looking at. Every
`Part I — RAG` and `Retrieval — deep dive` in the source tree carries it, so it was the single most frequent
typographic value in the corpus. **Widen the question for any future sweep: *inherited from anywhere*, not
just from the sister locales.** *(The canon makes the sharper version of this point: a claim of completeness
is itself an assertion and carries no evidence. Two sweeps in a row erred on exactly this value.)*

There is also a compounding defect worth stating once, because it is the exact tell this locale exists to
avoid: English em-dash convention is **compressed** (`word—word`). `Retrieval — deep dive` with **full
spaces around an em dash** is neither the German form nor the English one — it is the widened-em-dash
pattern typical of machine-generated English. Fixing the glyph fixes the tell.

**With that row added, nothing else in the two documents carries an inherited typographic value.** The
remaining formatting decisions (bold budget, figure probation, bridge direction) are editorial, not
typographic.

### 7.8 Gate 6 has run — the term ledgers are settled (2026-07-28)

Issues **#275** (kept-EN register) and **#276** (per-course ledgers + glossary decisions) are complete.
Method as prescribed here: six parallel attestation batches by domain, a cross-model register judge for the
recurring block strings and the constructions, and an independent verification pass over that judge's
citations. Where it landed:

- **Fourteen terms went German-led against the "German keeps English" instinct** — collected in
  `_language.md` **§1.1.g**, which is the single most important table for anyone rendering a page. The
  measured pattern: German wins on **measurements and processes** (*Durchsatz, Latenz, Inferenz,
  Quantisierung, Instrumentierung, Fehlerbudget, Endpunkt*), English holds on **artefacts you can point at**
  and on the closed **`-ing`** family, and — the sharpest finding — **the noun stays English while the verb
  is Germanised** (*das Embedding* / *vektorisieren*, *der Trace* / *nachverfolgen*).
- **Five previously-open rows closed because the evidence existed and nobody had looked in the right
  place** — *Retrieval* (a Duden EDV lemma for the **bare** loan; the earlier search had only looked up
  *Information Retrieval*), *Log* (a **second** Duden lemma, EDV, alongside the nautical DWDS one),
  *Embedding*, *Chunk*, and **Least Privilege** at BSI. §6.2's premise that German "will usually find a real
  answer" held.
- **Nine wrong-sense dictionary traps** are now named in a single box in `_language.md` §1.1, with the two
  meta-rules they teach: a search snippet describing an entry is not the entry, and a trap in *one*
  dictionary does not mean the *other* lacks the right sense.
- **Three rows were opened as DISPUTED** — *Harness*, *Cold Start*, *Drift* — each because German sources
  contradict **each other** (twice within a single publisher, once within a single article). Incumbents
  held, nothing changed, and every one of them becomes a question in the native-reader packet (#278), per
  Gate 7.
- **Six vendor-localisation sources disqualified** by the MT-signal check, each with the contradiction
  named. Worth recording as method: **the check works better as a *self-consistency* test than as a blanket
  vendor ban** — one German AWS page was internally consistent and kept as weak evidence, while the
  Dead-Letter-Queue pages produced four renderings across three vendors and were thrown out.
- **Method note that should propagate to later gates: measure, don't characterise.** The dash evidence was
  settled by counting codepoints over served HTML (≈ 220 : 0), and three BSI rulings by `pdftotext | grep`
  counts (*Geheimnis* 5 : *Zugangsdaten* 0; *Betriebshandbuch* 4 : *Runbook* 0; SBOM feminine 35 :
  masculine/neuter 0). Those numbers are more defensible than any prose citation, and they cost one command
  each. **Asking a model to characterise a corpus invites a plausible answer; counting produces a fact.**
  *(Same family as #315's standing rule that a surface tally is counted, never inherited.)*
- **And the counter-rule, because a count can also mislead: a null result is not evidence until the
  source-language twin is grepped too.** BSI TR-03183-2 has zero hits for every German provenance word —
  which says nothing, because the **English** edition has zero hits for `provenance` as well. The document
  simply does not treat the concept. Read the German zero alone and you manufacture a finding.
- **`audit` was checked for the first time and `Prüfpfad` did not survive it** (`canon/de/ai-sdlc.md` §4b).
  It is a **§ 14 UStG** term for the link between an *invoice* and the *service supplied*; Duden has no
  entry and DWDS flags its declension as computer-generated, while BSI's own audit module runs *Audit* 140×
  against *Prüfpfad* 0×. #313 had explicitly left the word untouched, so this overrides nothing — it
  examines something nothing had examined. The shipped label still carries it.

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
| **2** | ✅ **RUN 2026-07-28.** **Pilot** — ONE mid-complexity lesson, both its pages, through the FULL stack (Gates 0–6, cold read ×2 — in the event ×3). Recommended and used: *Tool use*, as SK — long enough to exercise every gate, central enough that its terminology feeds everything after, **and directly comparable to the Slovak pilot.** Full record: `canon/de/rag.md` §8, Phase 3. |
| **2b** | ⚠️ **Scheduled risk cluster 1 of 2 — pilot re-edit.** ✅ **Needed, and substantial.** Three cold reads (two comprehension, one naturalness) plus the cross-model register judge produced a real repair round: wrong-path words, a non-native coinage on both pages, English collocation skeletons, and page-level defects Gate 5 cannot see. **The pilot did not sail through.** |
| **2c** | ⚠️ **Method change: full reconstruction-from-the-proposition pass.** Budgeted, not discovered. — ❌ **Did NOT recur.** The 2b repairs were propositional from the first pass, because the Slovak lesson („die Reparatur ist nie ein Wortersatz, sondern ein Neubau aus dem Sinn") was **already in the canon before the pilot started** (`_language.md` §1.4) and the renderer briefs carried it **verbatim**. **That is the port working.** ⚠️ **The limit of that claim, plainly: it shows a KNOWN trap is avoidable, not that no unknown ones remain** — §I–§N of the phase record are the unknown ones this pilot found. **Keep the phase budgeted** for the waves: it did not fire on the pilot, which is not evidence that it cannot. |
| **2d** | ⚠️ **Polish pass.** — folded into 2b; no separate round was needed on the pilot. Not deleted from the plan: a two-page pilot is the cheapest possible case for folding it in, and a 13-page wave is not. |
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

**What the pilot actually did to cluster 1 (2026-07-28) — half the prediction held.** The *re-edit* (2b)
happened and was substantial; the *method change* (2c) did not, because the method was already in the canon
and in the briefs before page one. **But the cost did not vanish, it moved**, and the three places it moved
to are not in the phase table above:

1. a **terminology round before the prose** that ran ≈5× its planned size — the kept-EN register had been
   seeded from a *term inventory* (glossary lemmas, chapter headings) and did not contain the connective
   tissue running prose actually needs (*retry, timeout, backoff, side effect, namespace, validation*).
   ⇒ **Seed each wave's register from a frequency count over that wave's running English text, not from the
   glossary.**
2. **two infrastructure repairs** to gates that could not represent a partially translated locale (§4, "The
   gates' own repair record"). Without them the pilot could not have gone green at all.
3. a **reconciliation round between parallel attestation batches**, for which there was no gate — now
   Gate 6.5.

**Planning consequence: the pilot's real deliverable is the calibrated gate stack, not two translated
pages.** Budget it that way, and run the mechanical gates against staged English pages *before* any German
is written.

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
