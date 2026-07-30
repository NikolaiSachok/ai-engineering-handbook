# WAVE4-GLOSSARY-A.md — the binding term-direction mapping for `glossary.md` sections 1–10 (DE)

**Issue #283, reconciliation pass, slice A.** Covers the **first ten** sections of `docs/glossary.md` —
`## Ingestion — chunking` (line 15) through `## Agents — planning & loops` (line 490) inclusive. The
remaining ten sections are slice B and are **not** touched here.

**Scope in numbers, measured not estimated:** **157 bold headwords**, **188 em-dashes (U+2014)** that must
each become `–` (U+2013, with spaces) in the German rendering, **10 anchors**, **36 external references**.

```
python3 - <<'PY'   # run from repo root
import re
src=open('docs/glossary.md',encoding='utf-8').read().split('\n')
heads=[(i,l) for i,l in enumerate(src) if l.startswith('## ')]
for k,(i,l) in enumerate(heads[:10]):
    end=heads[k+1][0] if k+1<len(heads) else len(src)
    body='\n'.join(src[i:end])
    print(len(re.findall(r'^\*\*(.+?)\*\*\s+—',body,re.M)), body.count('—'), l[:48])
PY
```

---

## 0. How to read this sheet, and the rule that governs it

**The governing rule is #328: where the canon is silent or disagrees with the shipped corpus, the shipped
corpus wins, and the evidence class is `corpus precedent`, not `attestation`.** Every row below therefore
carries an **evidence class**, and the classes are not interchangeable:

| class | meaning |
|---|---|
| `corpus precedent` | measured in the shipped German pages. Convicts. Does **not** acquit — where the shipped German is already wrong, this sheet will confidently agree with it. |
| `canon` | a row in `editorial/canon/de/_language.md` or `rag.md`, with its own attestation behind it |
| `canon OPEN` | the canon has a row and it says *undecided*; the row prescribes a rebuild, not a word |
| `ledger` | `WAVE3-TERMS.md` / `LEDGER-*.md` |
| **`none`** | **no corpus occurrence, no canon row, no ledger row. An unfilled cell. This is a finding, not a gap in the work.** |

**Self-limits this sheet states about itself:**

1. **A count is not a ruling.** Several rows below have a large corpus count and still land in the flag list,
   because the count measures a *word* and the ruling needs a *referent*.
2. **The section scope is the lesson, not the corpus.** Where a term is absent from its own lesson but present
   elsewhere in the shipped German, the row says so and the flag list records it — `RAG tracing` is the case.
3. **`concord.py` undercounts German. Do not use it alone.** Measured, this pass: see §13. Every count in this
   sheet comes from raw `grep`, and the command is named.

### Command shorthand used in every evidence cell

All commands run from `i18n/de/docusaurus-plugin-content-docs/current`.

```
count P S   →  grep -rEo  --include='*.md' 'P' S | wc -l
forms X S   →  grep -rEoh --include='*.md' '[A-Za-zÄÖÜäöüß-]*X[A-Za-zÄÖÜäöüß-]*' S | sort | uniq -c | sort -rn
art   T S   →  grep -rEoh --include='*.md' '(Der|Die|Das|Dem|Den|Des|der|die|das|dem|den|des|Ein|ein|einem|einen|eines|eine) T([^A-Za-zÄÖÜäöüß-]|s\b|es\b)' S | sort | uniq -c
line  P S   →  grep -rn   --include='*.md' -E 'P' S
```

Scopes, one per section, mapped by anchor per the brief:

| § | anchor | scope (shipped German lesson) |
|---|---|---|
| 1 | `ingestion-chunking` | `part-1-rag/ingestion` |
| 2 | `ingestion-embeddings` | `part-1-rag/ingestion` |
| 3 | `retrieval` | `part-1-rag/retrieval` |
| 4 | `generation` | `part-1-rag/generation` |
| 5 | `evaluation` | `part-1-rag/cross-cutting/evaluation` |
| 6 | `guardrails` | `part-1-rag/cross-cutting/guardrails` |
| 7 | `observability` | `part-1-rag/cross-cutting/observability` |
| 8 | `agentic-rag` | `part-2-agents/agentic-rag` |
| 9 | `tools` | `part-2-agents/tool-use` |
| 10 | `planning-loops` | `part-2-agents/planning-loops` |

### Three global bindings the rendering agents must apply before writing a single row

**(a) The `[Neue Begriffe]` footers stay English, in every locale.** Measured: **all 35** shipped German
glossary references are `[Neue Begriffe]` footers, and every one lists the **English** lemma names
(`**[Neue Begriffe](../../glossary.md#ingestion-chunking)**: chunk, chunk overlap, recursive / structural
chunking, …`); RU does the same. This is a **convention, not a defect** — so a German glossary entry must keep
its **English lemma visibly recoverable**: for a kept-EN term the headword *is* the English; for a German-led
term the English original must stand alongside it, or the inbound footer link lands on an entry the reader
cannot match to the word they clicked.

```
grep -rh 'glossary.md#' i18n/de/docusaurus-plugin-content-docs/current | wc -l            # 35
grep -rh 'glossary.md#' i18n/de/docusaurus-plugin-content-docs/current | grep -vc 'Neue Begriffe'  # 0
```

**(b) Em-dash → en-dash, everywhere, including the definition separator.** The English uses `**Term** — …`;
the German uses `**Term** – …` (U+2013 with spaces), 188 times in this slice. The only U+2014 tolerated in the
shipped German corpus is inside verbatim English `<YouTube title="… — IBM Technology" />` strings (26 of them,
all of that shape) — the glossary has no such component, so its target is **0× U+2014**.

```
grep -rn --include='*.md' $'—' part-1-rag part-2-agents part-3-production
```

**(c) Article and inflection are not optional.** `_language.md` §1.0: a bare English term with no German
article, an *undurchgekoppeltes* compound, and a wobbling gender are the three named defects. An anglicism is
**not** one of them — do not "improve" a kept-EN row into a German coinage.

---

## §1 — `Ingestion — chunking` (9 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Chunk** | kept-EN | **Chunk** | *der* Chunk, die Chunks, des Chunks | `forms Chunk part-1-rag/ingestion` → `Chunk` 39, `Chunks` 17, `Chunk-Größe` 6, `Chunk-Grenzen` 2, `Chunk-Vektoren` 2; `art Chunk` → `dem Chunk` 4, `des Chunks` 2, `einen Chunk` 2, `einem Chunk` 1 | corpus precedent + canon (`_language.md` §1.1.a, WEAK→flexionstragend) |
| **Chunk overlap** | kept-EN | **Overlap** (bare, as the strategy name) | *der* Overlap, die Overlaps, des Overlaps | `forms '([Oo]verlap\|berlapp)' part-1-rag/ingestion` → `Overlap` 2, `Überlappung` 1, `überlappen` 1, `overlap` 1 (footer); `Chunk-Overlap` **0** in this scope, 1 in `part-1-rag/generation` (`Chunk-Overlaps`) | corpus precedent (thin) + canon `_language.md` §1.1.b |
| **Recursive / structural chunking** | German-led | **Rekursiv oder strukturell** (strategy label); running: *an der Dokumentstruktur orientiertes Chunking* | adjectives; no noun coined | `line 'Rekursiv oder strukturell' part-1-rag/ingestion` → index.md:76; `line 'Dokumentstruktur orientiert'` → index.md:85, deep-dive.md:51, deep-dive.md:111 | corpus precedent |
| **Semantic chunking** | German-led | **Semantisch** (strategy label); running: *semantisches Chunking* | adjective; `das Chunking` if nominalised | `line 'Semantisch' part-1-rag/ingestion` → index.md:80 (`4. **Semantisch.**`), index.md:133 (`→ semantisch →`); `count 'semantische[sn]? Chunking'` → **0** | corpus precedent (label only) |
| **Chunk metadata** | mixed compound | **Chunk-Metadaten** | *die* Chunk-Metadaten (Pluralwort, no singular) | `count 'Chunk-Metadaten' part-1-rag/ingestion` → 1 (index.md:102, an H3); `count Metadaten` → 12 | corpus precedent + canon (`Metadaten` = Pluralwort, `rag.md` §2) |
| **Parent-document (small-to-big) retrieval** | kept-EN | ***Parent-Document*- bzw. *Small-to-Big-Retrieval*** | artikellos, italic, as a family name | `line 'Parent-Document' part-1-rag/ingestion` → index.md:125–126 verbatim: „Diese Verfahrensfamilie heißt *Parent-Document*- bzw. *Small-to-Big-Retrieval*." | corpus precedent |
| **Document parsing / layout-aware extraction** | kept-EN head + German modifier | **Parsing**; layout-aware → *ein Parsing, das die Struktur zuerst erkennt* | *das* Parsing, des Parsings; *der* Parser, die Parser | `forms Parsing part-1-rag/ingestion` → `Parsing` 14, `Parser` 9; `line '^## Parsing'` → deep-dive.md:15 „## Parsing begrenzt alles, was danach kommt"; `line 'Struktur zuerst erkennt'` → deep-dive.md:111 | corpus precedent + canon `_language.md` §1.1.b |
| **OCR (optical character recognition)** | kept-EN abbreviation | **OCR**, gloss „(optische Zeichenerkennung – abgebildete Schrift wieder in Zeichen verwandeln)" | artikellos in corpus | `line OCR part-1-rag/ingestion` → deep-dive.md:25 (gloss verbatim), deep-dive.md:33–34 (Mermaid), index.md:247; `count Texterkennung` → **0** | corpus precedent |
| **Late chunking** | kept-EN | **Late Chunking** | *das* Late Chunking, des Late Chunkings; compound *das Late-Chunking-Verfahren* | `art 'Late Chunking' part-1-rag part-2-agents` → `Das Late Chunking` 5, `das Late Chunking` 2 | corpus precedent + canon (`rag.md` §3, **OPEN on attestation, decided on spelling**) |

### Flags — §1

- 🟡 **`Chunk overlap` — two forms, arguably two referents, and the canon row names a third.** The corpus
  writes `**Overlap.**` as the *strategy name* and `die Überlappung` as the *extent* („sofern sie kürzer ist
  als die Überlappung"). `Chunk-Overlap` — the form `_language.md` §1.1.b actually registers — is **0× in the
  ingestion lesson** and appears once, in `part-1-rag/generation/deep-dive.md:110` (`des Chunk-Overlaps`).
  **Ruling for the corpus:** headword **Overlap**, with `die Überlappung` named in the definition as the
  measured extent. Recording both because a renderer that picks `Chunk-Overlap` from the canon will produce a
  glossary headword the body never uses — the exact SK Fáza-25 shape.
- 🟡 **`Recursive / structural chunking` and `Semantic chunking` have no nominal German term at all.** Both
  exist only as **adjectival strategy labels** in a numbered list. A glossary headword needs a nominal or
  quasi-nominal form, and the corpus does not supply one. **Ruling:** keep the corpus adjectives as the
  headwords (`Rekursiv oder strukturell`, `Semantisch`) rather than coining `das rekursive Chunking` /
  `das semantische Chunking` — the coinage would be the first occurrence anywhere in the German corpus.
- ℹ️ **Not a defect: `Matryoshka` vs `Matrjoschka`.** `part-1-rag/ingestion/deep-dive.md:94` carries both in one
  paragraph — `Matryoshka Representation Learning` (the technique, proper name) and `die ineinandergesteckte
  Matrjoschka` (the nesting doll, in the etymological aside). Two referents, two spellings, correct. Checked
  because a naive two-forms-one-referent scan flags it.

### Heading and anchor block — §1

```
<a id="ingestion-chunking"></a>

## Ingestion – Chunking \{#ingestion-chunking}
```

Heading form is prescribed **verbatim** by `editorial/canon/de/rag.md` §6.6 („**Ingestion – Chunking**"),
consistent with the shipped German lesson (`title: Ingestion`, H2 `## Chunking` in
`part-1-rag/ingestion/index.md:26`).

---

## §2 — `Ingestion — embeddings` (11 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Embedding** | kept-EN | **Embedding** | *das* Embedding, die Embeddings, des Embeddings | `forms '([Ee]mbedd\|inbett)' part-1-rag/ingestion` → `Embedding` 13, `Embeddings` 11, `Embedding-Modell(e/s/n)` 10, `einbetten` 5, `Token-Embeddings` 1 | corpus precedent + canon `_language.md` §1.1.a |
| **Embedding space** | German-led | **der Vektorraum** | *der* Vektorraum, die Vektorräume, des Vektorraums | `line Vektorraum part-1-rag` → ingestion/deep-dive.md:100 („einen gemeinsamen **sprachübergreifenden Vektorraum**"), retrieval/deep-dive.md:21 („liegen im Vektorraum weit auseinander"); ingestion/index.md:151 paraphrases: „ein Vektor in einem Raum, in dem geometrische Nähe **Nähe in der Bedeutung** heißt"; `count Einbettungsraum` → **0** | corpus precedent (thin: 2 occurrences, neither a definitional first mention) |
| **Bi-encoder** | kept-EN | **Bi-Encoder** | *der* Bi-Encoder, die Bi-Encoder, des Bi-Encoders | `forms Encoder part-1-rag/ingestion` → `Cross-Encoder` 6, `Bi-Encoder` 4, `Encoder` 4; H3 `### Bi-Encoder vs. Cross-Encoder` at index.md:170 | corpus precedent + canon `_language.md` §1.1.b |
| **Cross-encoder** | kept-EN | **Cross-Encoder** | *der* Cross-Encoder, die Cross-Encoder, des Cross-Encoders | as above | corpus precedent + canon |
| **Dimensionality** | German-led | **die Dimensionszahl** | *die* Dimensionszahl, die Dimensionszahlen, der Dimensionszahl | `count Dimensionszahl part-1-rag/ingestion` → 3 (index.md:192, index.md:224, deep-dive.md:94); `count Dimensionalität` **whole DE corpus** → **0** | corpus precedent (**no canon row**) |
| **Cosine similarity** | German-led | **die Kosinus-Ähnlichkeit** | *die* Kosinus-Ähnlichkeit, der Kosinus-Ähnlichkeit | `count 'Kosinus-Ähnlichkeit' part-1-rag` → 3 in ingestion + 1 in retrieval/deep-dive.md:79; `count 'Cosinus-Ähnlichkeit'` → **0** | corpus precedent + canon `rag.md` §2 (8 : 0, de.wikipedia lemma) |
| **Retrieval-optimised (asymmetric) embeddings** | hybrid adjective | **retrieval-optimiert** (`für das Retrieval trainiert`) | adjective, lowercase | `line 'retrieval-optimiert' part-1-rag/ingestion` → index.md:189 („**Für das Retrieval trainiert (retrieval-optimiert).**"), index.md:224; `count asymmetr` → 1, and it is the **English footer** (index.md:230) | corpus precedent |
| **Multilingual embeddings** | German-led | **mehrsprachige Embeddings** | adjective *mehrsprachig* + `das Embedding`; `die Mehrsprachigkeit` for the property | `forms '([Mm]ultiling\|ehrsprach)' part-1-rag/ingestion` → `mehrsprachig*` 8, `Mehrsprachigkeit` 3, `multilingual` 4 — of which 1 is the model name `multilingual-E5` (class 1) and 3 are footer/EN | corpus precedent + canon `rag.md` §2 (Welle 1) |
| **Self-hosted vs. API embeddings** | German-led | **API oder Eigenbetrieb** | *der* Eigenbetrieb, des Eigenbetriebs | `line 'Eigenbetrieb\|self-hosted' part-1-rag/ingestion` → index.md:199 („**API oder Eigenbetrieb.**"), index.md:225; `self-hosted` 1× and it is the English footer | corpus precedent (**no canon row**) |
| **Embedding fine-tuning** | kept-EN | **Fine-Tuning** (of the embedding model) | *das* Fine-Tuning, die Fine-Tunings, des Fine-Tunings; gloss „(Nachtrainieren des Modells)" | `forms '([Ff]ine-?[Tt]un\|achtrain)' part-1-rag/ingestion` → `Fine-Tuning` 8, `Nachtrainieren` 1 | corpus precedent + canon `rag.md` §2 (obligatory gloss) |
| **Matryoshka Representation Learning (MRL)** | kept-EN, bare name | **Matryoshka Representation Learning (MRL)** | artikellos (name); ZERO gloss per `rag.md` §2 | `count Matryoshka part-1-rag/ingestion` → 6; H3 at deep-dive.md:92 | corpus precedent + canon `rag.md` §2 |

### Flags — §2

- 🔴 **`Embedding space` is the weakest ruling in this slice.** The lesson **defines** the concept without
  naming it (`index.md:151` paraphrases: „ein Vektor in einem Raum, in dem …"), and the only two occurrences of
  `Vektorraum` are downstream and incidental — one inside the compound `sprachübergreifender Vektorraum`, one
  in the retrieval deep-dive. No canon row exists. **Ruled for `der Vektorraum` on corpus precedent, but a
  renderer should know it is resting on two non-definitional occurrences**, not on a shipped definition.
- 🟡 **`Dimensionality` → `die Dimensionszahl` is a corpus coinage with no canon row.** It is used 3× and
  consistently, so it convicts; `Dimensionalität` is 0× corpus-wide. **This row belongs in the canon and is
  not there** — recorded here as a canon delta to route, not to decide.
- 🟡 **`Retrieval-optimised (asymmetric)` — the parenthetical has no German rendering at all.** The corpus
  carries `retrieval-optimiert` but *never* renders `asymmetric`; the only `asymmetr` string in the German
  tree is inside the untranslated English term footer. **Ruling:** keep the English `(asymmetric)` in the
  glossary parenthesis, per binding (a) — do **not** coin `asymmetrisch` as if it were a corpus term.
- ℹ️ **Pre-existing English-source defect, reported not fixed: the `#ingestion-embeddings` anchor has no
  inbound link.** All three ingestion term footers — in EN, DE and RU alike — point at
  `glossary.md#ingestion-chunking`, including the one that lists `embedding, embedding space, bi-encoder, …`.
  So the embeddings section exists and nothing links to it, and the anchor-parity gate cannot see this because
  the anchor *is* present and *is* in order.
  `grep -rn 'glossary.md#ingestion' docs/part-1-rag/` → deep-dive.md:113, index.md:130, index.md:214, all
  `#ingestion-chunking`.

### Heading and anchor block — §2

```
<a id="ingestion-embeddings"></a>

## Ingestion – Embeddings \{#ingestion-embeddings}
```

Descriptor is the plural `Embeddings`, matching the shipped German lesson: `sidebar_label: "Parsing und
fortgeschrittene Embeddings"` (`part-1-rag/ingestion/deep-dive.md:3`) and H2 `## Embedding-Modelle`
(`index.md:144`).

---

## §3 — `Retrieval` (22 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Dense retrieval** | kept-EN | **Dense Retrieval**, gloss „(die dichte Vektorsuche)" | *das* Dense Retrieval, des Dense Retrievals | `count 'Dense Retrieval' part-1-rag/retrieval` → 9; `art 'Dense Retrieval'` → `Das Dense Retrieval` 1 (index.md:24, with the gloss verbatim) | corpus precedent + canon (`das Retrieval`, `rag.md` §3 SETTLED) |
| **Top-K** | class 1 (variable expression) | **top-K** | *die* top-K (as a set), lowercase `t`, capital `K` | `count 'top-K' part-1-rag/retrieval` → 11; `line '(der\|die\|das\|den) top-K'` → `die top-K` 2 (index.md:51 „in die top-K geraten", deep-dive.md:61 „bewertet die top-K neu"); `count 'Top-K'` → **0** | corpus precedent + canon `_language.md` §1.1.b (`~~Top-k~~ → top-K`) |
| **Query transformation** | German-led, verbal | **die Frage umformulieren** (noun: *die Umformulierung*) | *die* Umformulierung, die Umformulierungen | H2 `## Die Frage umformulieren, bevor gesucht wird` (index.md:28); `count Umformul part-1-rag/retrieval` → index.md:33, index.md:74, deep-dive.md:9; `count 'Query-Transform'` → **0** | corpus precedent + canon `_language.md` §1.1.b |
| **Multi-query** | kept-EN | **Multi-Query** | artikellos in corpus; hyphenated, both parts capital | `count 'Multi-Query' part-1-rag/retrieval` → 2 (index.md:33 as a bold label, index.md:74); `count 'Multi-query'` → **0** | corpus precedent |
| **HyDE (Hypothetical Document Embeddings)** | kept-EN, bare name | **HyDE**, gloss `(*hypothetical document embeddings*)` — **English, italic** | artikellos; ZERO German gloss per `rag.md` §2 (bare names) | `count HyDE part-1-rag/retrieval` → 10; index.md:34 and deep-dive.md:19 both carry `(*hypothetical document embeddings*)` verbatim | corpus precedent + canon |
| **BM25 / sparse retrieval** | kept-EN name + German-led descriptor | **BM25 / die Stichwortsuche** | *die* Stichwortsuche, der Stichwortsuche | `count BM25 part-1-rag/retrieval` → 12; `count Stichwortsuche` → 2 (index.md:40 table header `**Sparse / Stichwortsuche (BM25)**`, index.md:36 H2); `count lexikalisch` → **0** | corpus precedent |
| **Hybrid search** | German-led | **die hybride Suche** | *die* hybride Suche, der hybriden Suche (adjective lowercase) | `count 'hybride Suche' part-1-rag/retrieval` → 10; `count 'Hybrid Search'` → **0**; `count 'Hybrid-Search'` → **0** | corpus precedent (**convicts the canon's WEAK marker**, `rag.md` §2) |
| **Reciprocal Rank Fusion (RRF)** | kept-EN, bare name | **Reciprocal Rank Fusion (RRF)** | artikellos; ZERO gloss | `count RRF part-1-rag/retrieval` → 11; `count 'Reciprocal Rank Fusion'` → 2 | corpus precedent + canon `rag.md` §2 |
| **Score fusion / score normalisation** | German-led | **die score-basierte Zusammenführung** / **die Score-Normierung** | *die* Zusammenführung; *die* Score-Normierung, der Score-Normierung | `count Zusammenführung part-1-rag/retrieval` → 12; `count 'Score-Normierung'` → 4; deep-dive.md:36 „Die **score-basierte Zusammenführung** normiert beide Retriever…"; deep-dive.md:131 „Die rangbasierte Zusammenführung ist die robuste Voreinstellung" | corpus precedent + canon `rag.md` §3 (`fusion` OPEN → *Zusammenführung*, rebuild prescribed and shipped) |
| **Reranking** | kept-EN | **Reranking** | *das* Reranking, kein Plural, des Rerankings | `count Reranking part-1-rag/retrieval` → 8; `art Reranking part-1-rag part-2-agents` → `das Reranking` 8, `Das Reranking` 1 | corpus precedent + canon `_language.md` §1.1.a |
| **LLM reranker** | kept-EN | **LLM-Reranker** | *der* LLM-Reranker, die LLM-Reranker, des LLM-Rerankers | `line 'LLM-Reranker' part-1-rag/retrieval` → deep-dive.md:65 („Der **LLM-Reranker** übergibt…"), deep-dive.md:132; `art Reranker` → `der Reranker` 4, `des Rerankers` 1, `dem Reranker` 1 | corpus precedent + canon `_language.md` §1.1.b |
| **Two-stage retrieval** | German-led | **das zweistufige Schema** | adjective *zweistufig* + `das Schema`, die Schemata | `count zweistufig part-1-rag/retrieval` → 3 (index.md:53 „Das ist das kanonische zweistufige Schema", deep-dive.md:13) | corpus precedent (**no canon row**) |
| **Late interaction / ColBERT** | kept-EN | **Late Interaction / ColBERT** | **artikellos**; if an article is unavoidable: *die* Late Interaction | `count 'Late Interaction' part-1-rag/retrieval` → 6; `count ColBERT` → 4; `count MaxSim` → 2; `art 'Late Interaction'` → **no article-bearing occurrence anywhere in the corpus** | corpus precedent + canon `_language.md` §1.1.b |
| **Multi-vector retrieval** | kept-EN | **Multi-Vector-Darstellung** (the representation) | *die* Multi-Vector-Darstellung | `line 'Multi-Vector' part-1-rag/retrieval` → deep-dive.md:79, sole occurrence: „ein Bündel von Vektoren, eines je Token – eine **Multi-Vector-Darstellung**" | corpus precedent (1 occurrence) |
| **Contextual retrieval** | kept-EN | **Contextual Retrieval** | *das* Contextual Retrieval, des Contextual Retrievals | `art 'Contextual Retrieval' part-1-rag part-2-agents` → `Das Contextual Retrieval` 5, `das Contextual Retrieval` 1 | corpus precedent + canon `rag.md` §2 |
| **Query routing** | mixed | **das Routing der Frage**; the component: **der Query-Router** | *das* Routing, des Routings; *der* Router, die Router (Nullplural) | `line 'Routing\|Router' part-1-rag/retrieval` → deep-dive.md:101 („**Das Routing der Frage** ist die vorab getroffene Entscheidung…"), index.md:105 (`**Der Query-Router.**` — in `part-2-agents/agentic-rag/index.md`), plus `die Routing-Entscheidung`; `count 'Query-Routing'` → **0** | corpus precedent + canon `_language.md` §1.1.d |
| **Metadata filtering** | German-led, verbal | **nach Metadaten filtern** | verbal; `die Metadaten` = Pluralwort, no singular | `line Metadaten part-1-rag/retrieval` → index.md:59 („**Nach Metadaten filtern**"), deep-dive.md:103, deep-dive.md:113 (Mermaid `Pre-Filter: ACL + Metadaten`); `count Metadatenfilter` **whole DE corpus** → **0** | corpus precedent + canon `rag.md` §3 (`der Metadatenfilter` OPEN/HOUSE — corpus confirms the verbal rebuild) |
| **Pre-filter / post-filter** | kept-EN | **Pre-Filter / Post-Filter** | *der* Pre-Filter, *der* Post-Filter; die -Filter, des -Filters | `art '(Pre\|Post)-Filter' part-1-rag/retrieval` → `Der Pre-Filter` 2, `der Pre-Filter` 1, `Der Post-Filter` 1, `der Post-Filter` 1, `ein Post-Filter` 1; `count 'Vorfilter\|Nachfilter'` → **0** | corpus precedent (**no canon row**) |
| **Access control (ACL)** | German-led | **die Zugriffssteuerung (ACL)** | *die* Zugriffssteuerung, der Zugriffssteuerung | `count Zugriffssteuerung part-1-rag/retrieval` → 7; `count ACL` → 6; `count Zugriffskontrolle` → **0** | corpus precedent + canon `rag.md` §2 („Zugriffskontrolle" is a calque of *control*) |
| **Recall@K / Precision@K** | kept-EN, artikelfrei | **Recall@K / Precision@K** | **artikelfrei**, glossed once | `count Recall part-1-rag/retrieval` → 9; `count Precision` → 7; `count Trefferquote` → **0** | corpus precedent + canon `rag.md` §3 (**DISPUTED**, incumbent kept-EN held) |
| **nDCG (normalized discounted cumulative gain)** | kept-EN, bare name | **nDCG** | artikellos; ZERO gloss | `count nDCG part-1-rag/retrieval` → 6 | corpus precedent + canon `rag.md` §2 |
| **MRR (mean reciprocal rank)** | kept-EN, bare name | **MRR** | artikellos; ZERO gloss | `count MRR part-1-rag/retrieval` → 6 | corpus precedent + canon `rag.md` §2 |

### Flags — §3

- 🟢 **Canon-vs-corpus, resolved for the corpus: `Hybrid search`.** `rag.md` §2 marks `die hybride Suche`
  **WEAK** („dünner belegt als die übrigen Zeilen dieser Gruppe"). The shipped corpus is not thin: **10 : 0**
  in the retrieval lesson alone, no fallback to the loan. **Ruling: `die hybride Suche`, and the WEAK marker
  should be lifted** — routed as a canon delta, not decided here.
- 🟡 **`Two-stage retrieval` and `Pre-filter / post-filter` have no canon row.** Both are consistent in the
  corpus (3× and 6× respectively) and both need a `_language.md` §1.1 line before a second course uses them —
  `der Pre-Filter` in particular, because a renderer with no row will reach for `der Vorfilter` (0× corpus)
  by reflex.
- 🟡 **`Multi-vector retrieval` rests on one occurrence.** `Multi-Vector-Darstellung`, once, and it is a
  compound — no bare `Multi-Vector` with an article exists. The headword form is therefore a *derivation from*
  the corpus, not a form the corpus ships. Marked so nobody later reads it as attested.
- ℹ️ **`fusion` is the canon OPEN row that the corpus has already closed in practice.** `rag.md` §3 prescribes
  „die Zusammenführung der beiden Ergebnislisten" and „die score-basierte vs. die rangbasierte
  Zusammenführung"; the shipped page writes exactly that, 12×. The row stays OPEN (no *external* attestation
  appeared), but the **corpus form is settled** and the glossary must use it.

### Heading and anchor block — §3

```
<a id="retrieval"></a>

## Retrieval \{#retrieval}
```

Layer name is kept-EN per `rag.md` §6.6 and matches the shipped German `title: Retrieval`.

---

## §4 — `Generation` (13 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Grounding** | kept-EN | **Grounding**, gloss „(Rückbindung der Antwort an den Kontext)" | *das* Grounding, kein Plural, des Groundings | `forms Grounding part-1-rag/generation` → `Grounding` 9, `Grounding-Anweisung(en)` 10; gloss verbatim at index.md:40 and evaluation/index.md:93 | corpus precedent + canon `rag.md` §2 (obligatory gloss) |
| **Grounding instructions** | kept-EN compound | **Grounding-Anweisung** | *die* Grounding-Anweisung, die -Anweisungen, der -Anweisung | `count 'Grounding-Anweisung' part-1-rag/generation` → 10 (H2 at index.md:38: „## Grounding-Anweisungen – der wichtigste Hebel gegen Halluzinationen") | corpus precedent |
| **Context packing** | German-led, **verbal** | **einen langen Kontext zusammenstellen** — **no noun** | verbal only; H2 form „Einen langen Kontext zusammenstellen" | `line 'zusammenstell' part-1-rag/generation` → index.md:22, deep-dive.md:89, deep-dive.md:112; `count 'Packing\|Kontextpackung'` **whole DE corpus** → **0** | corpus precedent + canon `rag.md` §3 (**OPEN — the absence of a German noun IS the finding**) |
| **Lost-in-the-middle** | kept-EN | **Lost-in-the-Middle** | **artikellos**; in compounds *der Lost-in-the-Middle-Effekt*, *die Lost-in-the-Middle-Regel* | `forms Lost-in-the-Middle part-1-rag part-2-agents` → bare 7, `-Effekt` 2, `-Regel` 1; `art` → **no article-bearing bare occurrence** | corpus precedent + canon `rag.md` §2 |
| **Citations / attribution** | German-led | **die Quellenangabe** | *die* Quellenangabe, die Quellenangaben, der Quellenangabe | `count Quellenangabe part-1-rag/generation` → 18; `count 'Zitat\|Attribution'` → **0** | corpus precedent + canon `_language.md` §1.1.b (`citation → die Quellenangabe`) |
| **Refusal / abstention** | German-led | **die Antwortverweigerung** | *die* Antwortverweigerung, die -en, der -ung | `line verweiger part-1-rag/generation` → H2 index.md:46 („## Die Antwortverweigerung ist gewollt, keine Fehlfunktion"), index.md:59, index.md:69, generation/deep-dive.md:9; `count Abstention` → **0** | corpus precedent + canon `_language.md` §1.1.f |
| **Faithfulness / groundedness** | kept-EN | **Faithfulness** (running term); `Groundedness` **only as a compound member** | Faithfulness: **artikelfrei**, no attested gender. Groundedness: no article-bearing singular — *die Groundedness-Metrik*, *der Groundedness-Wert* | `count Faithfulness part-1-rag/generation` → 7, `Quellentreue` → 5 (the gloss), `Groundedness` → 1 and it is `**Groundedness**-Metrik` (index.md:52). Obligatory gloss verbatim: „(Quellentreue – wie treu die Antwort den herangezogenen Quellen bleibt, ohne unbelegte Informationen hinzuzufügen)" | corpus precedent + canon `rag.md` §2, `_language.md` §1.1.b |
| **Parametric knowledge** | German-led, **rebuilt** | **das im Modell gespeicherte Wissen** (*parametric knowledge*); short anaphora **das Modellwissen** | *das* Wissen; *das* Modellwissen, des Modellwissens | `line 'Modellwissen\|gespeicherte Wissen' part-1-rag/generation` → index.md:12 („**das im Modell gespeicherte Wissen** (*parametric knowledge*)"), index.md:61, deep-dive.md:75, deep-dive.md:79, deep-dive.md:131; `count parametrisch` **whole DE corpus** → **0** | corpus precedent + canon `rag.md` §3 (**OPEN**; rebuild prescribed and shipped verbatim) |
| **Hallucination** | German-led | **die Halluzination** | *die* Halluzination, die -en, der -ion; verb *halluzinieren* | `count Halluzination part-1-rag/generation` → 5 | corpus precedent + canon `rag.md` §2, `_language.md` §1.1.g |
| **Self-consistency** | kept-EN | **Self-Consistency** | artikellos in corpus | `count 'Self-Consistency' part-1-rag/generation` → 8; `count Selbstkonsistenz` → **0** | corpus precedent + canon `rag.md` §2 |
| **Chain-of-verification (CoVe)** | kept-EN | **Chain-of-Verification (CoVe)** | artikellos; related German noun *die Prüffrage* (verification question) | `count 'Chain-of-Verification' part-1-rag/generation` → 5, `CoVe` → 3; `line Prüffrage` → deep-dive.md:42 | corpus precedent + canon `rag.md` §2, `_language.md` §1.1.b |
| **Knowledge conflict (context–memory conflict)** | German-led, **rebuilt** | **der Widerspruch zwischen abgerufenem Kontext und Modellwissen** | *der* Widerspruch, die Widersprüche, des Widerspruchs; verb *widersprechen* **+ Dativ** | `count Widerspruch part-1-rag/generation` → 6, `widerspr` → 4; H2 deep-dive.md:73 „## Wenn der Kontext dem Wissen des Modells widerspricht"; deep-dive.md:79 carries the full nominal form in bold; `count Konflikt` → **0** | corpus precedent + canon `rag.md` §3 (**OPEN**; rebuild shipped verbatim) |
| **Answer-shaping** | German-led | **die Gestaltung der Antwort** | *die* Gestaltung, der Gestaltung | `count 'Gestaltung der Antwort' part-1-rag/generation` → 3 (deep-dive.md:124, deep-dive.md:133, plus index.md:78 as a section pointer) | corpus precedent + canon `_language.md` §1.1.b |

### Flags — §4

- ℹ️ **This is the cleanest section in the slice, and the reason is worth recording: four of its thirteen rows
  are canon `OPEN` rows whose prescribed *rebuild* the shipped page executed verbatim.** `context packing`,
  `parametric knowledge`, `knowledge conflict`, and (in §7) `latency budget` / `alert fatigue`. So the glossary
  ruling for each is not "undecided" — it is "the rebuild is the ruling", exactly as `rag.md` §3 says of
  `Gate` and `Load Shedding`. **A renderer must not read `OPEN` as licence to coin.**
- 🟡 **`Context packing` cannot have a nominal headword.** The English headword is a noun phrase; German has
  no noun for it, corpus-wide and dictionary-wide. **Ruling:** render the headword as the corpus H2 does —
  **Einen langen Kontext zusammenstellen** *(context packing)* — accepting a verbal headword in a glossary,
  rather than coining `das Kontext-Packing`. This is a **shape decision the English glossary's own format does
  not anticipate** and the rendering agents need it stated once, here, because §7 has the same problem
  (`regression triage`, `cost attribution`, `non-termination`).
- 🟡 **`Faithfulness` and `Quellentreue` are one referent with two surfaces, deliberately.** 7 : 5 in the
  lesson. Checked rather than assumed: `Quellentreue` occurs only as the **gloss** at first mention and as an
  ordinary common noun thereafter („dem Grounding und der **Quellentreue** nachgeordnet"), never as the
  metric's name. Not a wobble. The glossary entry must keep `Faithfulness` as the headword.

### Heading and anchor block — §4

```
<a id="generation"></a>

## Generation \{#generation}
```

Kept-EN layer name (`rag.md` §6.6; `die Generation` per `_language.md` §1.1.b), matching the shipped
`title: Generation`.

---

## §5 — `Evaluation` (20 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Evaluation** | German-led | **die Evaluierung** | *die* Evaluierung, die -en, der -ung; short form *das Eval* (Hausform) | `count Evaluierung part-1-rag/cross-cutting/evaluation` → 16; `count Evaluation` → 2, both **English strings** (a YouTube title at index.md:50, and `RAG-Evaluierung` context at deep-dive.md:17); page `title: "Evaluierung"` | corpus precedent + canon `_language.md` §1.1.e, `rag.md` §6.6 |
| **Retrieval failure / generation failure** | German-led | **das Fehlerbild des Retrievals / das Fehlerbild der Generation** | *das* Fehlerbild, die Fehlerbilder, des Fehlerbild[e]s | `count Fehlerbild part-1-rag/cross-cutting/evaluation` → 7; index.md:92–93 verbatim: „Fehlerbild des Retrievals → Recall@K zu niedrig" / „Fehlerbild der Generation → Faithfulness zu niedrig" | corpus precedent (**no canon row**) |
| **Golden set / golden dataset / ground truth** | German-led + one OPEN loan | **der Goldstandard** (*golden set*); `Ground Truth` **artikelfrei** | *der* Goldstandard, die -s, des -s. `Ground Truth`: artikelfrei, compounds *die Ground-Truth-Labels* | `count Goldstandard …/evaluation` → 20; `count 'Golden Set'` → **0**; `count 'Ground Truth'` → 2 | corpus precedent + canon `rag.md` §2 (Welle-1 reversal: 29 : 0 corpus-wide), `_language.md` §1.1.b (`Ground Truth` OPEN) |
| **Answer relevance** | kept-EN, artikelfrei | **Answer-Relevance**; the number: **der Answer-Relevance-Wert** | artikelfrei bare; *der* Answer-Relevance-Wert, des -Werts. Durchkopplung obligatory | `count 'Answer-Relevance' …/evaluation` → 18; deep-dive.md:47 „In Teil 1 stand **Answer-Relevance** als Metrikname; die Zahl, die sie liefert, ist der **Answer-Relevance-Wert**"; `count Antwortrelevanz` → **0** | corpus precedent + canon `rag.md` §3 (**OPEN**; incumbent kept-EN, gloss „(wie gut die Antwort die gestellte Frage trifft)" shipped verbatim at deep-dive.md:47) |
| **Correctness** | German-led | **die Korrektheit** | *die* Korrektheit, der Korrektheit | `grep -rin 'correctness\|korrektheit' .` → `…/evaluation/index.md:25` (metric table: „**Faithfulness**, **Answer-Relevance**, Korrektheit"), `index.md:101`, `deep-dive.md:43` („Faithfulness misst das Grounding, nicht die Korrektheit"); also `part-3-production/production-failures.md:166,184,389` | corpus precedent (**no canon row**) |
| **LLM-as-a-judge** | kept-EN | **LLM-as-a-judge**, gloss „(ein Modell bewertet die Ausgabe eines anderen)" | artikellos as the pattern name; the component is *der Judge* | `count 'LLM-as-a-judge' …/evaluation` → 4; `art Judge part-1-rag part-2-agents` → `der Judge` 10, `den Judge` 9, `dem Judge` 4, `des Judges` 2, `eines Judges` 2, `die Judges` 1 | corpus precedent + canon `rag.md` §2, `_language.md` §1.1.b |
| **Judge bias** | mixed | **die Bias-Formen eines Judges**; the three: **Positionsbias**, **Ausführlichkeitsbias**, **Self-Preference** | *der* Bias, des Bias (endungslos), Plural meiden; *der* Positionsbias, *der* Ausführlichkeitsbias | `count …/evaluation`: `Positionsbias` 7, `Ausführlichkeitsbias` 3, `Self-Preference` (see flag) ; deep-dive.md:144 lists all three; `count Selbstbevorzugungsbias` **whole DE corpus** → **0** | corpus precedent (**overrides canon**, see flag) |
| **Offline vs online eval** | kept-EN adverbs | **offline und online** | adverbs/adjectives, no article; H2 „Offline und online – zwei Schleifen" | `line 'Offline\|Online' …/evaluation` → index.md:70 (H2), index.md:72, index.md:75, index.md:105 | corpus precedent |
| **Regression eval** | German-led | **die Regression** (mit Pflichtglosse) / **auf Regressionen prüfen** | *die* Regression, die -en, der -ion | `line Regression …/evaluation` → index.md:73 („eine **Regression** (eine durch eine Änderung verursachte Verschlechterung)"), index.md:83, index.md:105 | corpus precedent + canon `rag.md` §2 (obligatory gloss; ⛔ verb *regredieren*) |
| **A/B testing** | kept-EN abbreviation + German head | **der A/B-Test** | *der* A/B-Test, die A/B-Tests, des A/B-Tests | `line 'A/B' …/evaluation` → index.md:76, index.md:105, deep-dive.md:101 (`A/B-Test`) | corpus precedent |
| **Faithfulness** | kept-EN | **Faithfulness** | artikelfrei; obligatory gloss at first mention (see §4) | `count Faithfulness …/evaluation` → 24 | corpus precedent + canon |
| **Context precision** | kept-EN | **Context-Precision** | artikelfrei bare; hyphenated (Durchkopplung) | `count 'Context-Precision' …/evaluation` → 7; `count 'Context Precision'` → 1 and it is the **English footer** (deep-dive.md:148) | corpus precedent + canon `rag.md` §2 + §1.3.3 |
| **Context recall** | kept-EN | **Context-Recall** | artikelfrei bare; hyphenated | `count 'Context-Recall' …/evaluation` → 13 | corpus precedent + canon |
| **Reference-free vs reference-based evaluation** | German-led adjectives | **referenzfrei / referenzbasiert** | adjectives; *die referenzfreie Evaluierung* | `count …/evaluation`: `referenzfrei` 5, `referenzbasiert` 4; deep-dive.md:21 table header „**Referenzfrei** (Frage + Kontext + Antwort) / **Referenzbasiert** (braucht eine Referenzantwort)" | corpus precedent + canon `_language.md` §1.1.b |
| **LLM-judge calibration** | German-led | **die Kalibrierung** (des Judges) | *die* Kalibrierung, der Kalibrierung; Plural meiden | `count Kalibrierung …/evaluation` → 10; deep-dive `sidebar_label: "Innenleben der Metriken und Judge-Kalibrierung"` | corpus precedent + canon `rag.md` §2 (⚠ only the judge sense) |
| **Pointwise vs pairwise evaluation** | kept-EN | **Pointwise / Pairwise** | artikellos, capitalised | `count …/evaluation`: `Pointwise` 5, `Pairwise` 8; deep-dive.md:97, :99 both introduce them in bold with a German gloss (`**Pointwise** – eine einzelne Antwort für sich bewerten –`) | corpus precedent + canon `rag.md` §2 |
| **Inter-annotator agreement (IAA)** | German-led paraphrase | **die Übereinstimmung zwischen den Annotatoren (IAA)** | *die* Übereinstimmung + *zwischen* + Dativ; *der* Annotator, die Annotatoren; heading form *die Interrater-Reliabilität* | `count …/evaluation`: `'Übereinstimmung zwischen den Annotatoren'` 3, `IAA` 1, `Interrater` 2 | corpus precedent + canon `rag.md` §3 (**OPEN on the loan's gender**; the paraphrase is the corpus form) |
| **Cohen's kappa** | German genitive + kept-EN | **Cohens Kappa** | *das* Kappa, des Kappa[s]; *der* Kappa-Wert. **No apostrophe** — German genitive-s | `line Cohen …/evaluation` → deep-dive.md:125 „- **Cohens Kappa** – die um den Zufall bereinigte Übereinstimmung zweier Annotatoren" | corpus precedent + canon `_language.md` §1.1.b |
| **Fleiss' kappa** | German genitive + kept-EN | **Fleiss' Kappa** | as above. **Apostrophe kept** — the name already ends in `-ss` | `line Fleiss …/evaluation` → deep-dive.md:126 „**Fleiss' Kappa** überträgt dieselbe Idee auf mehr als zwei Annotatoren." | corpus precedent |
| **Active sampling / active learning** | kept-EN | **das Active Sampling** (im maschinellen Lernen: *Active Learning*) | *das* Sampling, des Samplings | `line 'Active Sampling' …/evaluation` → deep-dive.md:132 („Das **Active Sampling** – im maschinellen Lernen als *Active Learning* …"), deep-dive.md:146, index.md:121; `count 'aktives Lernen'` → **0** | corpus precedent + canon `_language.md` §1.1.e (`das Sampling`) |

### Flags — §5

- 🔴 **Canon-vs-corpus disagreement, ruled for the corpus: `self-preference bias`.** `rag.md` §3 marks
  **WEAK** and prescribes **„der Selbstbevorzugungsbias (Self-Preference Bias)"** as a pattern-licensed
  coinage. The shipped corpus does **not** use it: `Selbstbevorzugungsbias` is **0× corpus-wide**, and the
  page writes kept-EN **`Self-Preference`** with a German explanation —
  `…/evaluation/deep-dive.md:89` „**Self-Preference** – im Paper trägt dasselbe Fehlerbild den förmlichen
  Namen *self-enhancement bias* – heißt: Der Judge bewertet Ausgaben im eigenen Stil höher"; `index.md:58`
  „die Neigung, **Antworten im eigenen Stil** höher zu bewerten (Self-Preference)"; `deep-dive.md:144`
  „Positionsbias …, Ausführlichkeitsbias und Self-Preference".
  **Ruling: `Self-Preference`, kept-EN, artikellos, with the German explanation — the corpus wins, explicitly
  over the canon row.** Note the asymmetry the corpus chose and the canon did not anticipate: the *other two*
  biases **were** Germanised (`Positionsbias` 7×, `Ausführlichkeitsbias` 3×) and only the third was not. The
  canon row's own reasoning („das Muster lizenziert die FORM, nicht das WORT") is what predicts this outcome;
  the row's prescription contradicts it.
  ```
  grep -rn --include='*.md' -E 'Selbstbevorzug|Self-Pref' part-1-rag part-2-agents part-3-production
  ```
- 🟡 **`Correctness` → `die Korrektheit` has no canon row, and I nearly recorded it as absent.** My first pass
  grepped `Correctness` (0) and `Richtigkeit` (0 in scope) and would have filed the term as undecided. The
  referent is there, 3× in the evaluation lesson, under `Korrektheit`. **This is the "zero on the loan is not
  a zero on the referent" trap firing on a third word neither the loan nor my first German guess.** Row needs
  a canon line; `die Richtigkeit` is separately in use for a *different* referent
  (`part-3-production/llmops/index.md:212`, `part-1-rag/retrieval/deep-dive.md:103`) and must not be merged.
- 🟡 **`Retrieval failure / generation failure` → `das Fehlerbild des Retrievals` has no canon row** and is
  load-bearing: it is the diagnostic backbone the whole course refers back to, and the same construction
  recurs in `tool-use` („Vier Fehlerbilder des Tool-Einsatzes"), `planning-loops` („Das zentrale Fehlerbild")
  and `agentic-rag`. Consistent, 7× in scope; needs a canon line.
- ℹ️ **`Cohens Kappa` vs `Fleiss' Kappa` — the apostrophe difference is correct German, not a wobble.** Checked
  because a mechanical consistency gate will flag it. German genitive of *Cohen* is *Cohens*; a name ending in
  a sibilant takes the apostrophe. The English `Cohen's` / `Fleiss'` pair maps to a **different** German pair,
  and the glossary must not normalise them to one shape.

### Heading and anchor block — §5

```
<a id="evaluation"></a>

## Evaluierung \{#evaluation}
```

⚠ **This is the one heading in my slice where German diverges from both RU and SK.** RU and SK both keep
`## Evaluation` (the layer name, English) — `i18n/ru/…/glossary.md:215`, `i18n/sk/…/glossary.md:220`. German
does **not**: `rag.md` §6.6 rules explicitly that „*Evaluation* wird zu **Evaluierung**", and the shipped
German lesson is `title: "Evaluierung"`. **The anchor id stays `evaluation`.** A renderer that reasons from
cross-locale symmetry will get this wrong; the German canon and the German corpus agree against the symmetry.

---

## §6 — `Guardrails` (12 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Guardrails** | kept-EN, **plural only** | **Guardrails**, gloss „(Leitplanken – Schutzregeln um das Modell)" | *die* Guardrails. **⛔ no German singular** — rephrase, never invent | `count Guardrails …/guardrails` → 12; bare singular `Guardrail` (word-boundary) → **0**; `count Leitplanken` → 1 (the gloss) | corpus precedent + canon `rag.md` §2 + §3 (OPEN on the singular) |
| **Prompt injection** | kept-EN | **Prompt-Injection** | *die* Prompt-Injection, die -Injections, der -Injection. **Hyphenated** (§1.3.3) | `count 'Prompt-Injection' …/guardrails` → 5; `count 'Prompt Injection'` → 3, **all three are English strings**: the YouTube title at index.md:25 and two `[Neue Begriffe]` footers | corpus precedent + canon `_language.md` §1.1.a, §1.3.3 |
| **Spotlighting** | kept-EN, incl. the three sub-terms | **Spotlighting**; **Delimiting**, **Datamarking**, **Encoding** | *das* Spotlighting, des Spotlightings (same for all three sub-terms) | `count …/guardrails`: `Spotlighting` 17, `Delimiting` 7, `Datamarking` 6, `Encoding` 6; `art Spotlighting part-1-rag` → `das Spotlighting` 5; `art '(Delimiting\|Datamarking\|Encoding)'` → **no article-bearing occurrence** | corpus precedent + canon `_language.md` §1.1.f |
| **Instruction hierarchy** | German-led | **die Rangfolge der Anweisungen** (*instruction hierarchy*) | *die* Rangfolge, die -n, der -folge | `count 'Rangfolge der Anweisungen' …/guardrails` → 6; index.md:34 „**Die Rangfolge der Anweisungen** (*instruction hierarchy*)"; `count 'Instruction Hierarchy'` → 1 and it is the English footer | corpus precedent + canon `_language.md` §1.1.f |
| **PII redaction** | German-led + kept-EN abbreviation | **personenbezogene Daten (PII) erkennen und maskieren**; noun: **die Maskierung** | *die* Maskierung, die -en, der -ung; `PII` artikellos | `count …/guardrails`: `Maskierung` 7, `PII` 3, `personenbezogen` 12+; H2 deep-dive.md:79 „## Wo personenbezogene Daten abgefangen werden und wie Sie sie maskieren"; `count Schwärzung` in this scope → **0**, but `schwärzen`/`Schwärzung` **3× in `…/observability/deep-dive.md`** | corpus precedent + canon `rag.md` §2, `_language.md` §1.1.f |
| **Reversible vs irreversible masking** | German-led | **die reversible / die irreversible Maskierung** | adjectives + `die Maskierung`; *die Pseudonymisierung*, *die Anonymisierung* | `count …/guardrails`: `reversibel*` 7, `irreversibel*` 2, `Pseudonymisierung` 1, `Anonymisierung` 2; `…/observability/deep-dive.md:43` „Die irreversible Maskierung – entfern…" | corpus precedent + canon `_language.md` §1.1.f |
| **Input / output validation** | German-led, **verbal** | **die Eingabe prüfen / die Ausgabe prüfen** — **no noun** | verbal; attributive *geprüfte Eingaben, geprüfte Ausgaben* | `line 'prüfen' …/guardrails` → index.md:35 („**Die Eingabe prüfen.**"), index.md:36 („**Die Ausgabe prüfen.**"), index.md:55 („geprüfte Eingaben, geprüfte Ausgaben"); `count Validierung` in this scope → **0** | corpus precedent |
| **Content safety / moderation** | German-led, **verbal** | **schädliche Inhalte abwehren** — **no noun** | verbal; H2 form „Schädliche Inhalte abwehren – Eingabe wie Ausgabe" | `line …/guardrails` → index.md:43 (H2), index.md:45, index.md:57; `count Moderation` → **0**; `count Inhaltssicherheit` → **0** | corpus precedent |
| **Jailbreak** | kept-EN | **Jailbreak** — preferably in a compound | *der* Jailbreak, die Jailbreaks, des Jailbreaks; *der Jailbreak-Angriff* | `count Jailbreak …/guardrails` → 4; `art Jailbreak part-1-rag` → `der Jailbreak-` 1 (compound) | corpus precedent + canon `_language.md` §1.1.f |
| **Least privilege / tool allow-listing** | German-led | **das Prinzip der geringsten Berechtigungen** | *das* Prinzip, des Prinzips; allow-listing → *das Allowlisting*, *die Allowlists* (**no bare singular**) | `count 'geringsten Berechtigungen' …/guardrails` → 3 (index.md:37, :55, and `part-2-agents/tool-use/index.md:92`); `count 'Least Privilege'` → **0**; `count Allowlist` in `part-1-rag` → 1 (deep-dive.md:11) | corpus precedent + canon `_language.md` §1.1.f (BSI, Stufe 1) |
| **Attack success rate (ASR)** | German-led + kept-EN abbreviation | **die Erfolgsrate der Angriffe (ASR)** | *die* Erfolgsrate, die -n, der -rate | `count …/guardrails`: `Erfolgsrate` 12, `ASR` 6; `count Angriffserfolgsrate` → **0** | corpus precedent + canon `rag.md` §2 (BSI 5 : 0) |
| **Defence-in-depth** | kept-EN | **Defence-in-Depth**, gloss „(eine gestaffelte Abwehr aus mehreren Schichten)" | artikellos in corpus | `line Defence …/guardrails` → index.md:49, sole occurrence: „Was es gibt, ist **Defence-in-Depth**: eine gestaffelte Abwehr aus mehreren Schichten." `count mehrschichtig` → **0** | corpus precedent (1 occurrence) + canon `rag.md` §2 |

### Flags — §6

- 🟡 **Two headwords are nouns in English and have no noun in German: `Input / output validation` and
  `Content safety / moderation`.** Both are shipped **verbally**. `Validierung` — which *is* in the canon
  (`_language.md` §1.1.a) and *is* used in the tools lesson for argument validation — is **0× in the guardrails
  lesson**, which means the German corpus deliberately separated the two referents. **Ruling:** verbal
  headwords (`Die Eingabe und die Ausgabe prüfen`, `Schädliche Inhalte abwehren`) with the English original
  alongside. ⚠ **Do not reach for `die Ein-/Ausgabevalidierung`** — it would be a coinage that also collides
  with the tools lesson's `die Validierung`.
- 🟡 **`PII redaction`: the canon offers `die Schwärzung / die Maskierung`; the two words are split across two
  lessons and the split looks deliberate.** `…/guardrails` uses only **Maskierung** (7×, `Schwärzung` 0×);
  `…/observability` uses **schwärzen / Schwärzung** (3×) for writing to the trace store. **Ruled for
  `die Maskierung`** as the guardrails-section headword form, with `die Schwärzung` named in the definition —
  but recorded because if the two are in fact one referent, the corpus has a cross-lesson wobble that no
  per-page gate can see.
- 🟡 **`Defence-in-depth` rests on a single occurrence, and the canon marks the neighbouring row HOUSE.**
  1× in the whole German corpus. Thin, but it is a shipped bolded first-mention with its gloss, so it counts.
- ℹ️ **`Guardrail` singular: the 0 is real and it is a *success*, not a gap.** `rag.md` §3 leaves the singular
  OPEN and instructs "rephrase, do not invent"; the shipped page does exactly that across 12 occurrences.
  The glossary headword must therefore be **plural**, `**Guardrails**`, even though the English headword
  reads as a mass noun.

### Heading and anchor block — §6

```
<a id="guardrails"></a>

## Guardrails \{#guardrails}
```

Kept-EN layer name (`rag.md` §6.6), matching the shipped `title: "Guardrails"`.

---

## §7 — `Observability` (22 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Observability** | kept-EN | **Observability**, gloss „(deutsch die Beobachtbarkeit)" | *die* Observability, kein Plural, der Observability | `count Observability …/observability` → 18; `count Beobachtbarkeit` → 1 and it is the gloss (index.md:10 „Deutsch die Beobachtbarkeit – zeigt, was das System … tatsächlich tut"); `art` → „**Die** Observability einer LLM-Anwendung" (deep-dive.md:91) | corpus precedent + canon `_language.md` §1.1.e |
| **Trace / span** | kept-EN | **Trace / Span** | *der* Trace, die Traces, des Traces; *der* Span, die Spans, des Spans | `count …/observability`: `Trace` 59, `Span` 19; index.md:32 „Ein **Trace** ist genau diese Aufzeichnung"; deep-dive.md:9 „Ein Trace ist die vollständige Aufzeichnung einer Anfrage, Span für Span" | corpus precedent + canon `_language.md` §1.1.a |
| **RAG tracing** | kept-EN | **RAG-Tracing** — ⚠ **derived, not shipped** | *das* Tracing, kein Plural, des Tracings | `count 'RAG-Tracing' …/observability` → **0**; `count Tracing …/observability` → **0**; `count Tracing` **whole DE corpus** → 12, in `part-2-agents/orchestration-frameworks` (4) and `part-3-production/tooling-ecosystem` (5) + others, e.g. „Ist **das Tracing** einmal eingeschaltet" (orchestration-frameworks/deep-dive.md:83) | **corpus precedent for the head noun only; the compound is `none`** |
| **Cost per request / token accounting** | German-led | **die Kosten pro Anfrage / die Zählung der Token pro Anfrage** | *die* Kosten (Pluraletantum, no singular, `der Kosten`); *die* Zählung | `line Kosten …/observability` → index.md:45 („Pro Schritt: Latenz, Zahl der Token, Kosten, Modellversion"), deep-dive.md:79 („fängt alles mit der Zählung der Token pro Anfrage an"), deep-dive.md:105; `count 'Token-Abrechnung'` → **0** | corpus precedent + canon `_language.md` §1.1.a (`die Kosten`) |
| **Latency (p50 / p95)** | German-led + class 1 identifiers | **die Latenz (p50 / p95)** | *die* Latenz, die Latenzen, der Latenz; `p50`/`p95` lowercase, class 1; compound *der p95-Wert*, *die p95-Latenz* | `count …/observability`: `Latenz` 25, `p50` 4, `p95` 6, `p95-Latenz` 3 (deep-dive.md:49, :51, index.md:103); `count Perzentil` → 1 | corpus precedent + canon `rag.md` §6.7(d), `_language.md` §1.1.e |
| **Three pillars (metrics / logs / traces)** | German-led | **die drei Säulen (Traces, Metriken, Logs)** | *die* Säule, die Säulen; *die* Metrik, die Metriken; *das* Log, die Logs | `count 'drei Säulen' …/observability` → 2; index.md:17 „Die drei Säulen der Observability – **Traces, Metriken, Logs** –"; index.md:86 | corpus precedent + canon `_language.md` §1.1.e, `rag.md` §3 (`Log` CLOSED/SETTLED) |
| **Feedback loop (observability → eval)** | mixed | **die Schleife** *Observability → Evaluierung*; the signal: **das Feedback** | *die* Schleife, die -n; *das* Feedback, des Feedbacks | H2 index.md:54 „## Feedback: Die Observability liefert der Evaluierung neue Fälle"; index.md:61 („Schleife."); deep-dive.md:59 („hier wird die Schleife aus Teil 1 zur Betriebspraxis"); `count Rückkopplung` → **0** | corpus precedent + canon `_language.md` §1.1.a |
| **Head-based sampling** | kept-EN | **Head-based Sampling** (short anaphora: *Head-Sampling*) | *das* Sampling, des Samplings. ⚠ **no case-marked occurrence** — article inherited from `das Sampling` | `grep -rn -oE '(Head\|Tail\|Priority\|Trace)-?(based)? ?Sampling' …/observability` → `Head-based Sampling` deep-dive.md:17, :99; `Head-Sampling` deep-dive.md:17, :21, :27(Mermaid) | corpus precedent + canon `_language.md` §1.1.e (article) |
| **Tail-based sampling** | kept-EN | **Tail-based Sampling** (short anaphora: *Tail-Sampling*); the processor `tail_sampling` is class 1 | *das* Sampling | same command → `Tail-based Sampling` deep-dive.md:19, :99; `Tail-Sampling` deep-dive.md:21, :92 | corpus precedent |
| **Priority / hybrid sampling** | kept-EN + German adjective | **Priority-Sampling**, auch **hybrides Sampling** | *das* Sampling | same command → `Priority-Sampling` deep-dive.md:21, :99; `hybrides Sampling` deep-dive.md:21 | corpus precedent |
| **Message-content capture (opt-in)** | German-led | **das Erfassen der Nachrichteninhalte** (ausdrücklich einzuschalten) | *das* Erfassen (substantivierter Infinitiv, no plural) | `line 'Erfassen\|opt-in' …/observability` → deep-dive.md:39 („muss **das Erfassen der Nachrichten*inhalte*** … ausdrücklich eingeschaltet werden"), deep-dive.md:101; `count Retention` → **0** | corpus precedent (**no canon row**) |
| **Retention tiers** | German-led | **die Aufbewahrungsstufe** | *die* Aufbewahrungsstufe, die -n, der -stufe | `line Aufbewahrung …/observability` → deep-dive.md:102 („eine Entscheidung pro Feld und pro **Aufbewahrungsstufe**"), index.md:100; `count TTL` → 1 | corpus precedent (**no canon row**) |
| **Golden signals** | kept-EN, **plural, HOUSE** | **die Golden Signals**, gloss „(Latenz, Traffic, Fehler, Sättigung)" | *die* Golden Signals (plural only). ⛔ „die goldenen Signale" | `art 'Golden Signals'` → `die Golden Signals` 1; `line …/observability` → deep-dive.md:47 („die **Golden Signals** der Google-SRE-Schule, also Late…"), deep-dive.md:103 | corpus precedent + canon `rag.md` §3 (**HOUSE, explicitly not attested**) |
| **SLI / SLO** | kept-EN abbreviations | **SLI / SLO** | *das* SLI, die SLIs, des SLIs; *das* SLO, die SLOs, des SLOs | `count …/observability`: `SLI` 7, `SLO` 7; deep-dive.md:49 „Sie wählen **SLIs** – Service-Level-Indicators, also die Größen…" | corpus precedent + canon `_language.md` §1.1.e |
| **Error budget** | German-led | **das Fehlerbudget** | *das* Fehlerbudget, die -s, des Fehlerbudget[e]s | `count Fehlerbudget …/observability` → 4; `count 'Error Budget'` → **0** | corpus precedent + canon `rag.md` §2 (Welle-1 reversal, Computerwoche + iX) |
| **Burn-rate alerting** | kept-EN noun, **rebuilt clause** | **die Burn Rate des Fehlerbudgets** — spaced, not hyphenated | *die* Burn Rate (no attested inflection); ⛔ *die Brennrate* | `count 'Burn Rate' …/observability` → 3; deep-dive.md:51 „Gemeldet wird nur, was am anderen Ende ankommt: die **Burn Rate** des Feh…"; `count 'Burn-Rate'` → **0**; `count Brennrate` → **0** | corpus precedent + canon `rag.md` §3 (**OPEN**; Google-Cloud-de disqualified) |
| **Alert fatigue** | **described, not named** | **wer zu viel alarmiert, wird nicht mehr gehört** (rebuild) | no noun | `count 'Alert Fatigue' …/observability` → **0**; `count Alarmmüdigkeit` **whole DE corpus** → **0**; deep-dive.md:94 „Für jede Metrik einen Alert einzurichten endet damit, dass niemand mehr hinsieht, und dann scrollt die echte Regression ungelesen vorbei." | corpus precedent + canon `rag.md` §3 (**OPEN**; register problem, Intensivmedizin) |
| **Regression triage** | German-led, **verbal** | **einen Qualitätseinbruch auf seine Ursache zurückführen** — **no noun**; the two-step: *erst erkennen, dann zuordnen* | verbal; *die* Regression for the drop itself | `count Triage …/observability` → **0**; H2 deep-dive.md:53 „## Einen Qualitätseinbruch auf seine Ursache zurückführen"; deep-dive.md:104 „Bei einer Regression gilt: erst erkennen, dann zuordnen" | corpus precedent |
| **Cost attribution** | German-led, **verbal** | **die Kosten zuordnen** — **no noun** | verbal; „über die Spans des Traces zuordnen" | `count 'Kostenzuordnung\|Kostenattribution' …/observability` → **0**; deep-dive.md:81 „dafür müssen Sie **die Kosten zuordnen**"; deep-dive.md:64 (Mermaid) „Über die Spans des Traces zuordnen" | corpus precedent |
| **Token accounting** | German-led | **die Zählung der Token pro Anfrage** | *die* Zählung; `das Token`, **die Token** (unmarked plural) | deep-dive.md:79, deep-dive.md:105, index.md:102; `count 'Token-Zählung'` → **0** | corpus precedent + canon `_language.md` §1.1.a (`die Token`) |
| **Latency budget** | German-led, **rebuilt** | **eine Obergrenze für die Latenz** / **Ziele für p50 und p95** | *die* Obergrenze, die -n, der -grenze. ⛔ „das Latency Budget" mit deutschem Artikel | H2 deep-dive.md:77 „## Eine Obergrenze dafür, was eine Anfrage verbrauchen darf"; deep-dive.md:83 „Sie setzen Ziele für p50 und p95 und zerlegen die Latenz nach Spans"; `count 'Latenzbudget\|Latency Budget'` **whole DE corpus** → **0** | corpus precedent + canon `rag.md` §3 (**OPEN — this row was a §2 reversal**) |
| **Soft cap / hard cap** | German-led, pattern name kept-EN | **die weiche / die harte Obergrenze** (**Soft- und Hard-Cap** as the pattern name) | *die* Obergrenze. ⛔ „das Cap" / „der Cap" — no attested gender | `count Obergrenze …/observability` → 9; deep-dive.md:85 „wenn die Vorgabe zwischen einer **weichen** und einer **harten Obergrenze** unterscheidet (**Soft- und Hard-Cap**)"; `count 'Soft Cap\|Hard Cap'` → **0** | corpus precedent + canon `rag.md` §2 (the `Soft Cap / Hard Cap` note) + §6.5 |

### Flags — §7

- 🔴 **`RAG tracing` — a section-local zero that is not a corpus-wide zero, and the compound is genuinely
  undecided.** `Tracing` is **0× in the observability lesson** (which uses `der Trace` 59× and verbs instead)
  but **12× elsewhere in the shipped German** with a clean article: „Ist **das Tracing** einmal eingeschaltet"
  (`part-2-agents/orchestration-frameworks/deep-dive.md:83`), „Zuerst **das Tracing**"
  (`part-3-production/tooling-ecosystem/index.md:138`). So: **the head noun is settled (`das Tracing`), the
  compound `RAG-Tracing` is `none`** — zero occurrences anywhere. **Ruling: `das RAG-Tracing`, marked as a
  derivation, not as corpus precedent.** ⚠ This is the row where the section-scoped method fails: had I
  measured only the mapped lesson, I would have filed the whole term as undecided.
  ```
  grep -rn --include='*.md' -E 'Tracing' .
  ```
- 🔴 **`Head-based sampling` / `Tail-based sampling` — two forms per referent, both shipped, on one page.**
  `Head-based Sampling` (2×, both at first-mention and in the summary) vs `Head-Sampling` (3×, as short
  anaphora and as a Mermaid label); same for Tail. Reading the paragraphs, the split is **deliberate**: full
  name where the term is introduced, short compound in running reference. **But it is still a
  referent-inventory defect for the glossary**, because a glossary headword must be one string, and the
  `-based` form is a **hybrid** (English adjectival suffix inside a German noun phrase) with no canon row.
  **Ruling: headword `Head-based Sampling` / `Tail-based Sampling`** — the introduced form — with
  `Head-Sampling` / `Tail-Sampling` named in the definition as the short form. Flagged, not silently decided.
- 🟡 **Four headwords in this section are English nouns with no German noun, all shipped verbally:**
  `regression triage`, `cost attribution`, `alert fatigue`, `latency budget` (and `message-content capture`
  survives only as a substantivised infinitive). Together with §4's `context packing` and §6's two, that is
  **eight of my 157 headwords whose German rendering is not a noun.** The rendering agents need the shape
  ruling stated once: **a verbal or clausal headword is correct German here and is the ruling, not a
  stopgap** (precedent: `rag.md` §3 on `Gate`, `Load Shedding`, `packing`). What is *not* acceptable is
  inventing `die Kostenzuordnung`, `die Regressionstriage`, `das Latenzbudget`, `die Alarmmüdigkeit` — every
  one of those is 0× corpus-wide and three of them are explicitly ⛔ in the canon.
- 🟡 **`Message-content capture` and `Retention tiers` have no canon row.** `das Erfassen der
  Nachrichteninhalte` (2×) and `die Aufbewahrungsstufe` (1×, in a compound) are the corpus forms;
  `die Aufbewahrungsstufe` in particular rests on **one** occurrence.
- 🟡 **`Golden signals` is HOUSE, and the glossary will make that invisible.** `rag.md` §3: no German
  attestation on any tier, for the loan *or* a German form; the incumbent is held as house style. The corpus
  ships `die Golden Signals` twice. A glossary entry looks like a decision; this one is a convention.

### Heading and anchor block — §7

```
<a id="observability"></a>

## Observability \{#observability}
```

Kept-EN layer name, matching the shipped `title: Observability`.

---

## §8 — `Agents — agentic RAG` (13 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Agentic RAG** | kept-EN | **Agentic RAG** | **artikellos**; genitive uninflected: *des Agentic RAG* | `count 'Agentic RAG' …/agentic-rag` → 10; `art 'Agentic RAG' part-1-rag part-2-agents` → `des Agentic RAG` 1 (index.md:159). ⚠ the one `die Agentic RAG` hit is a **false positive** — a relative pronoun for `die Freiheit` (`planning-loops/index.md:89`) | corpus precedent |
| **Agent loop** | German-led, EN name once | **die Schleife** (der **Agent Loop**) | *die* Schleife, die -n, der Schleife. The loan: *der* Agent Loop (1 nominative) | `count Schleife …/agentic-rag` → 57; `line 'Agent Loop'` → index.md:55, sole occurrence: „Im Kern steht eine einfache Schleife, der **Agent Loop**."; `count 'Agentenschleife\|Agenten-Schleife'` → **0** | corpus precedent |
| **ReAct (Reasoning + Acting)** | kept-EN, bare name | **ReAct (Reasoning + Acting)** | artikellos; ZERO gloss | `count ReAct …/agentic-rag` → 4; deep-dive.md:11 „`Plan-and-Execute` gegen ReAct (Reasoning + Acting)" | corpus precedent + canon `rag.md` §2 |
| **Routing / query router** | mixed | **der Query-Router**; the act: **das Routing** | *der* Router, die Router (Nullplural), des Routers; *das* Routing, die Routings, des Routings; *die* Routing-Entscheidung | `count …/agentic-rag`: `Routing` 8, `Router` 5; index.md:105 „**Der Query-Router.** Der leichteste Schritt in die Autonomie"; index.md:127, :133, deep-dive.md:37 (`die Routing-Entscheidung`) | corpus precedent + canon `_language.md` §1.1.d |
| **Multi-hop retrieval** | German-led phrase around a kept-EN noun | **das Retrieval über mehrere Hops** | **der Hop, die Hops, des Hops** (full paradigm measured) | `art Hop …/agentic-rag …` → `der Hop` 3, `des Hops` 3, `einem Hop` 2, `den Hops` 2, `dem Hop` 2, `eines Hops` 1, `ein Hop` 1, `die Hops` 1; H2 deep-dive.md:61 „## Was ein Hop an den nächsten weitergibt"; `count 'Multi-Hop'` → **0** | corpus precedent (**no canon row for `der Hop`**) |
| **Query planning** | German-led, verbal | **die Abfragen planen** | verbal; *die* Abfrage, die -n (index/DB sense, ≠ `die Anfrage`) | `line …/agentic-rag` → index.md:108 („**Die Abfragen planen.** Das Modell zerlegt eine schwierige Frage vorab in Teilfragen."), index.md:145 („Router → Abfragen planen → volle Schleife") | corpus precedent + canon `rag.md` §2 (`die Abfrage` vs `die Anfrage` vs `die Frage`) |
| **Self-correction / self-reflection** | German-led | **die Selbstkorrektur** | *die* Selbstkorrektur, die -en, der -korrektur | `count Selbstkorrektur …/agentic-rag` → 11; `count 'Selbstprüfung\|Selbstreflexion'` in this scope → **0** (⚠ `die Selbstprüfung` is the *generation* lesson's term for self-verification — different referent, keep separate) | corpus precedent |
| **Iterative retrieval** | German adjective + kept-EN noun | **das iterative Retrieval** | adjective *iterativ* + `das Retrieval` | `count 'Iteratives Retrieval' …/agentic-rag` → 2 (deep-dive `sidebar_label`, index.md:158); `count iterativ` → 8; index.md:47 „der Rückweg in die Suche mit einer geschärften Frage heißt **iteratives Retrieval**" | corpus precedent |
| **Self-RAG** | kept-EN, bare name | **Self-RAG** | artikellos | `count 'Self-RAG' …/agentic-rag` → 8 | corpus precedent + canon `rag.md` §2 |
| **Corrective RAG (CRAG)** | kept-EN, bare name | **Corrective RAG (CRAG)** | artikellos; the component: **der Bewerter der abgerufenen Dokumente** | `count …/agentic-rag`: `CRAG` 8, `Corrective RAG` 2; deep-dive.md:19 „**Corrective RAG (CRAG)** … in einem eigenen, schlanken **Bewerter der abgerufenen Dokumente**" | corpus precedent + canon `rag.md` §2, `_language.md` §1.1.g (`Evaluator → der Bewerter`, with obligatory object) |
| **Adaptive RAG** | kept-EN, bare name | **Adaptive RAG** | artikellos | `count 'Adaptive RAG' …/agentic-rag` → 5 | corpus precedent + canon `rag.md` §2 |
| **Retrieval budget** | kept-EN compound | **das Retrieval-Budget** | *das* Retrieval-Budget, die -s, des -Budgets (gender from head `Budget`) | `count 'Retrieval-Budget' …/agentic-rag` → 2; deep-dive.md:55 „Ein **Retrieval-Budget** ist eine harte Obergrenze – höchstens so viele Hops, so viele Suchen, so viele abgerufene Tokens" | corpus precedent + canon `_language.md` §1.1.a (`das Budget`) |
| **Sufficient context** | German-led | **ausreichender Kontext** | adjective + `der Kontext`, des Kontext[e]s | `line 'ausreichend' …/agentic-rag` → deep-dive.md:94 („die Prüfungen auf **ausreichenden Kontext**"), deep-dive.md:104; `count 'hinreichender Kontext\|Sufficient Context'` → **0** | corpus precedent |

### Flags — §8

- 🟡 **`der Hop` has a full corpus paradigm and no canon row.** 15 case-marked occurrences, gender
  unambiguous, plural `die Hops`, genitive `des Hops`, and an H2 built on it. It is one of the most heavily
  used nouns in the agentic-RAG lesson. **Needs a `_language.md` §1.1.c line** — routed as a canon delta.
- 🟡 **`Agent loop`: the corpus runs the German and names the English once. The glossary inverts the ratio.**
  `die Schleife` 57× vs `der Agent Loop` 1×. A glossary headword `**Agent Loop**` would present as the term a
  form the body uses once. **Ruling: German-led headword `die Schleife (des Agenten)` with `Agent Loop` as
  the English original in parentheses** — class 3 per `_language.md` §1.0, and the direction the corpus
  actually leads with. Flagged because it is the opposite of what the kept-EN default would produce.
- 🟡 **`Selbstkorrektur` vs `Selbstprüfung` — two German words, two referents, one page apart.** The
  agentic-RAG lesson uses `die Selbstkorrektur` for the retrieval judgement; the generation deep-dive uses
  `die Selbstprüfung` for chain-of-verification / self-consistency; `planning-loops` uses `die Reflexion` for
  the plan-level judgement. `…/agentic-rag/deep-dive.md:101` makes the separation explicit („Halten Sie die
  Selbstkorrektur des Retrievals … von der Reflexion der Planung … getrennt"). **The glossary must preserve
  all three and must not merge any two** — this is the referent-separation the corpus paid for.
- ℹ️ **`Agentic RAG` gender: one genitive, uninflected.** `des Agentic RAG`, once. `RAG` itself has **no**
  article-bearing occurrence anywhere in the German corpus and **no** `_language.md` §1.1 row. So the
  glossary must keep `Agentic RAG` artikellos and must not assign it a gender.

### Heading and anchor block — §8

```
<a id="agentic-rag"></a>

## Agenten – Agentic RAG \{#agentic-rag}
```

⚠ **The family prefix is `Agenten`, translated — not `Agents`.** `rag.md` §6.6 gives the pattern verbatim
(„**Agenten – Planung und Schleifen**"). **This differs from RU and SK**, which both keep the English `Agents`
(`i18n/ru/…/glossary.md:401`, `i18n/sk/…/glossary.md:416`). Descriptor `Agentic RAG` matches the shipped
German `title: Agentic RAG`, capitalised as a German noun phrase.

---

## §9 — `Agents — tools` (14 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Tool use / function calling** | hybrid compound + kept-EN alt name | **der Tool-Einsatz**, auch **Function Calling** | *der* Tool-Einsatz, des Tool-Einsatzes; `Function Calling` **artikellos, als Apposition** | `count 'Tool-Einsatz' …/tool-use` → 8, page `title: Tool-Einsatz`; index.md:10 „**Tool-Einsatz**, auch **Function Calling** genannt, ist der allgemeine Mechanismus"; H2 index.md:73 „## Vier Fehlerbilder des Tool-Einsatzes" | corpus precedent + canon `_language.md` §1.1.c |
| **Tool definition** | kept-EN | **die Tool-Definition** | *die* Tool-Definition, die -en, der -Definition | `count 'Tool-Definition' …/tool-use` → 10; index.md:44 „**Die Tool-Definition** – ein Name, ein Beschreibungstext und ein Parameterschema" | corpus precedent + canon `_language.md` §1.1.a |
| **Tool call** | kept-EN | **der Tool-Call** | *der* Tool-Call, die Tool-Calls, des Tool-Calls | `count 'Tool-Call' …/tool-use` → 12; index.md:45 „**Der Tool-Call** – statt gewöhnlichen Textes…"; `count 'Tool Call'` → 1, and it is the **YouTube title** at index.md:23 | corpus precedent + canon `_language.md` §1.1.a, `rag.md` §3 (CLOSED, amtliches Regelwerk § 45 E1) |
| **Tool result** | kept-EN | **das Tool-Result** | *das* Tool-Result, die -s, des -Results | `count 'Tool-Result' …/tool-use` → 3 | corpus precedent + canon `_language.md` §1.1.a |
| **Tool selection** | kept-EN + German head | **die Tool-Auswahl** | *die* Tool-Auswahl, der Tool-Auswahl | `count 'Tool-Auswahl' …/tool-use` → 3; deep-dive.md:109 „Die **Tool-Auswahl** wird nämlich schlechter, je größer der Katalog wird"; `count Toolauswahl` → **0** | corpus precedent |
| **JSON Schema** | class 1 / kept-EN | **JSON Schema** — spaced, not hyphenated | *das* Schema, die Schemata, des Schemas | `count 'JSON Schema' …/tool-use` → 6; `count 'JSON-Schema'` → **0** | corpus precedent + canon `rag.md` §2 (adj+noun may stay spaced), `_language.md` §1.1.a |
| **Structured output** | German-led (generic) | **die strukturierte Ausgabe** — ⚠ **distinct from the class-1 product name `Structured Outputs`** | adjective + *die* Ausgabe, die -n, der Ausgabe | `line 'strukturierte Ausgabe\|Structured Output' …/tool-use` → index.md:45 („liefert das Modell eine **strukturierte Ausgabe**: JSON mit dem Namen des Tools"); `Structured Outputs` appears only as OpenAI's feature name (deep-dive.md:59) and in the English footer | corpus precedent + canon `_language.md` §1.0 (`Structured Outputs` = Klasse 1) |
| **Parallel tool calls** | German adjective + kept-EN noun | **parallele Tool-Calls** | adjective + `der Tool-Call`; the vendor switches `parallel_tool_calls` / `disable_parallel_tool_use` stay class 1 | `count 'Parallele Tool-Calls' …/tool-use` → 2; deep-dive.md:31 „Zwei Arten von Aufrufen haben in einem parallelen Batch nichts zu suchen" | corpus precedent + canon `rag.md` §1 (Klasse 1 identifiers) |
| **Constrained decoding** | kept-EN | **Constrained Decoding**; where an article is needed: **das Constrained-Decoding-Verfahren** | `Constrained Decoding` **artikellos** (no case-marked occurrence); *das* …-Verfahren, des -Verfahrens | `count 'Constrained Decoding' …/tool-use` → 5; `art 'Constrained Decoding'` → **none**; `line 'Constrained-Decoding-Verfahren'` → deep-dive.md:69, :87, :133, :149 | corpus precedent + canon `_language.md` §1.0 |
| **Strict mode / Structured Outputs** | kept-EN + class 1 | **der Strict Mode** / **Structured Outputs** (Feature-Eigenname) | *der* Strict Mode, dem/den Strict Mode; `Structured Outputs` artikellos, unflected | `art 'Strict Mode' …/tool-use` → `der Strict Mode` 4, `Der Strict Mode` 3, `dem Strict Mode` 2, `den Strict Mode` 1; `count 'Structured Outputs'` → 2 | corpus precedent + canon `_language.md` §1.0, `rag.md` §1 |
| **Idempotency / idempotency key** | German-led + kept-EN | **die Idempotenz** / **der Idempotency-Key** | *die* Idempotenz, der Idempotenz (no plural); *der* Idempotency-Key, die -Keys, des -Keys | `count Idempoten …/tool-use` → 7; H2 deep-dive.md:117 „## Idempotenz: Welche Aufrufe sich gefahrlos wiederholen lassen"; `count 'Idempotency-Key'` → 2 | corpus precedent + canon `_language.md` §1.1.c |
| **Tool-RAG / dynamic tool loadout** | kept-EN + German-led | **die dynamische Tool-Auswahl**, auch **Tool-RAG** | adjective + *die* Tool-Auswahl; `Tool-RAG` artikellos | `count 'Tool-RAG' …/tool-use` → 3; deep-dive.md:111 „Die **dynamische Tool-Auswahl** – auch **Tool-RAG** genannt – ruft nur die Tools ab, die zur aktuellen … passen" | corpus precedent + canon `rag.md` §2 |
| **Argument validation** | German-led | **die Validierung der Argumente** — split: **die technische / die fachliche Validierung** | *die* Validierung, die -en, der -ung; *das* Argument, die Argumente | `count 'Validierung der Argumente' …/tool-use` → 1; deep-dive.md:136 („**Die fachliche Validierung** fängt die Argumente ab…"), deep-dive.md:149 („Validieren Sie die Argumente vor der Ausführung, auf zwei Ebenen: technisch für die Form, fachlich für die Bedeutung"); `count Argumentprüfung` → **0** | corpus precedent + canon `_language.md` §1.1.a |
| **Retry budget** | kept-EN compound | **das Retry-Budget** | *das* Retry-Budget, die -s, des -Budgets (gender from head `Budget`). ⚠ no case-marked occurrence | `line 'Retry-Budget' …/tool-use` → deep-dive.md:99, sole occurrence: „Eine Obergrenze für Wiederholungen (**Retry-Budget**) – hart, pro Aufruf und pro Durchlauf"; `count Wiederholungsbudget` → **0**; `count Wiederholung` → 17 | corpus precedent + canon `_language.md` §1.1.a (`das Budget`), `rag.md` §3 (`Retry` bare loan is OPEN — but the **compound** is licensed by the head) |

### Flags — §9

- 🟡 **`Structured output` is TWO entries wearing one English headword, and the corpus separates them.** The
  generic capability is German-led **`die strukturierte Ausgabe`**; OpenAI's feature is class-1
  **`Structured Outputs`**, unflected, and it appears in the glossary's *own* next headword
  (`Strict mode / Structured Outputs`). **Ruling: keep them separate and say so in the definition.** A
  renderer that unifies them will either Germanise a product name or leave a generic concept untranslated —
  and the shipped page does neither.
- 🟡 **`Constrained decoding` and `Retry budget` have no case-marked corpus occurrence.** `Constrained
  Decoding` is used **artikellos** 5× and takes an article only through the compound
  `das Constrained-Decoding-Verfahren` (4×); `Retry-Budget` occurs exactly once, in a parenthesis, uninflected.
  Both genders below are **inherited from the head noun** (canon), not measured. Marked so nobody reads them
  as attested.
- 🟡 **`der Tool-Einsatz` is a hybrid the class policy does not have a slot for.** English first element,
  German head, German inflection — neither kept-EN (class 2) nor German-led (class 3) as `_language.md` §1.0
  defines them. It is the shipped **page title**, used 8×, so it is settled by corpus precedent; but the
  **class policy has a gap** that `rag.md` §8 §E already noted in a different context („Der Kanon braucht eine
  Klasse, die er nicht hat"). Recorded as a canon-structure finding, not a term question. The same shape
  recurs in `die Tool-Auswahl`, `die Grounding-Anweisung`, `die Chunk-Größe`, `das Fehlerbild des Retrievals`.
- ℹ️ **`Tool Call` spaced, once — and it is a YouTube title, i.e. class 1.** Checked, because
  `rag.md` §3 records the spaced spelling as the pressetypical defect and a mechanical grep will flag it.

### Heading and anchor block — §9

```
<a id="tools"></a>

## Agenten – Tool-Einsatz \{#tools}
```

Prefix `Agenten` per `rag.md` §6.6; descriptor from the shipped German `title: Tool-Einsatz`
(`part-2-agents/tool-use/index.md:2`). ⚠ **The anchor id stays `tools`** even though the German descriptor is
`Tool-Einsatz` — `rag.md` §7 point 3 and `scripts/locale_parity.py`.

---

## §10 — `Agents — planning & loops` (21 headwords)

| EN headword | class | German headword form | grammar | evidence | evidence class |
|---|---|---|---|---|---|
| **Planning** | German-led | **die Planung** | *die* Planung, die -en, der Planung | `count Planung …/planning-loops` → 9; page `title: Planung und Schleifen` | corpus precedent |
| **Task decomposition** | German-led | **die Zerlegung** (des Ziels in Teilaufgaben) | *die* Zerlegung, die -en; *die* Teilaufgabe, die -n | `count …/planning-loops`: `Zerlegung` 4, `Teilaufgaben` 5; deep-dive.md:9 („das Ziel zerlegen"), index.md:170, :184 („Zerlegung und Abbruch sitzen auf der Schleife") | corpus precedent |
| **Plan-and-execute** | kept-EN, bare name | **Plan-and-Execute** — capital `E` | artikellos; often in backticks (`` `Plan-and-Execute` ``) | `count 'Plan-and-Execute' …/planning-loops` → 8; deep-dive.md:11 „`Plan-and-Execute` gegen ReAct (Reasoning + Acting)" | corpus precedent + canon `rag.md` §2 |
| **Re-planning** | German-led | **die Umplanung**; verb **umplanen** | *die* Umplanung, die -en | `count Umplanung …/planning-loops` → 4; deep-dive.md:15 („Teil 1 hat eine Abfolge geplant und umgeplant, wenn sie zerbrach"), deep-dive.md:39 („planen bei einem Fehlschlag um"); `count 'Neuplanung'` → **0** | corpus precedent (**no canon row**) |
| **Reflection / self-critique** | German-led | **die Reflexion** (*reflection / self-critique*) | *die* Reflexion, die -en, der Reflexion | `count Reflexion …/planning-loops` → 34; index.md:121 „**Die Reflexion** (reflection / self-critique) ist ein eigener Schritt"; `count Selbstkritik` → **0** | corpus precedent |
| **Termination criterion** | German-led | **die Abbruchbedingung** | *die* Abbruchbedingung, die -en, der -bedingung; „ein Tool zum Beenden" | `line Abbruch …/planning-loops` → index.md:107 („**Eine Abbruchbedingung.** Legen Sie fest, was „fertig" überhaupt heißt"), index.md:197 („die ausgeschriebene Abbruchbedingung"); `count Abbruchkriterium` → **0** | corpus precedent (**no canon row**) |
| **Step budget / iteration limit** | German-led + kept-EN compound | **das Schrittbudget** / **eine harte Obergrenze** | *das* Schrittbudget, die -s, des -budget[e]s; *die* Obergrenze | `count …/planning-loops`: `Schrittbudget` 2, `Obergrenze` 9+; index.md:97 („**Budgets und Limits.** Eine harte Obergrenze – für Schritte, Tool-Calls, Tokens, Kosten oder die verstrichene …"); `count Iterationsgrenze` → **0** | corpus precedent + canon `_language.md` §1.1.a |
| **Loop detection** | German-led | **die Schleifenerkennung** | *die* Schleifenerkennung, der -erkennung | `count Schleifenerkennung …/planning-loops` → 2; also `…/agentic-rag/deep-dive.md:57` („Dazwischen sitzt die **Schleifenerkennung** für das Retrieval") | corpus precedent (**no canon row**) |
| **Scratchpad / working memory** | German-led | **das Arbeitsgedächtnis** (das Scratchpad aus Teil 1) | *das* Arbeitsgedächtnis, des -gedächtnisses. ⛔ „das Scratchpad" mit deutschem Artikel im Fließtext; ⛔ `der Arbeitsspeicher` (= RAM, reserved) | `count …/planning-loops`: `Arbeitsgedächtnis` 12, `Scratchpad` 2 (both back-references); deep-dive.md:88 „**Das Arbeitsgedächtnis** – das Scratchpad aus Teil 1 –"; index.md:163 „nur das noch Relevante in einem **Arbeitsgedächtnis** (scratchpad / working memory)" | corpus precedent + canon `rag.md` §3 (**Welle-2 reversal out of §2**), §2 |
| **Non-termination** | **described, not named** | **die Schleife endet nicht richtig** (rebuild); the property: **die Terminierung** | no noun for the failure; *die* Terminierung for the property | `count 'Nichtterminierung' …/planning-loops` → **0**; H2 index.md:75 „## Das zentrale Fehlerbild – eine Schleife, die nicht richtig endet"; index.md:77, :194; `count Terminierung` → 3 | corpus precedent |
| **Plan search (tree / graph search over plans)** | German-led | **die Suche im Raum möglicher Pläne**; short name **die Baumsuche** | *die* Suche, der Suche; *die* Baumsuche, der Baumsuche | `count …/planning-loops`: `Baumsuche` 4 (incl. `sidebar_label: "Baumsuche und Gedächtnis"`), H1 deep-dive.md:7 „# Im Raum möglicher Pläne suchen…", deep-dive.md:140 („Planung kann zur Suche im Raum möglicher Pläne werden"); `count Plansuche` → **0** | corpus precedent |
| **Tree of Thoughts (ToT)** | kept-EN, bare name | **Tree of Thoughts (ToT)** | artikellos | `count …/planning-loops`: `Tree of Thoughts` 3, `ToT` 5 | corpus precedent + canon `rag.md` §2 |
| **Graph of Thoughts (GoT)** | kept-EN, bare name | **Graph of Thoughts (GoT)** | artikellos | `count …/planning-loops`: `Graph of Thoughts` 3, `GoT` 2 | corpus precedent + canon `rag.md` §2 |
| **LATS (Language Agent Tree Search)** | kept-EN, bare name | **LATS** | artikellos; ZERO gloss | `count LATS …/planning-loops` → 5 | corpus precedent + canon `rag.md` §2 |
| **Self-Refine** | kept-EN, bare name | **Self-Refine** | artikellos | `count 'Self-Refine' …/planning-loops` → 5 | corpus precedent + canon `rag.md` §2 |
| **Reflexion** | kept-EN, bare name — **code-styled to disambiguate** | **`Reflexion`** (in backticks, always) | artikellos, unflected. ⚠ **the backticks are load-bearing in German only** | `grep -rn -F '`Reflexion`' …/planning-loops` → deep-dive.md:47, :63, :141; deep-dive.md:47 states the reason: „`Reflexion` ist der Name eines Frameworks, n[icht]…" | corpus precedent (**and see the flag — this is the most important German-only ruling in my slice**) |
| **Episodic memory** | German-led | **das episodische Gedächtnis** | adjective + *das* Gedächtnis, des Gedächtnisses | `count …/planning-loops`: `episodische*` 10; deep-dive.md:92 „**Das episodische Gedächtnis** ist ein Speicher vergangener Erfahrungen" | corpus precedent |
| **Semantic memory** | German-led | **das semantische Gedächtnis** | as above | deep-dive.md:94 „**Das semantische Gedächtnis** sind dauerhafte Fakten, die der Agent kennt oder gelernt hat"; deep-dive.md:100, :143 (with `prozedurales Gedächtnis`) | corpus precedent |
| **Virtual context management (MemGPT)** | kept-EN, **English, italic, artikellos** | ***virtual context management*** (MemGPT) | artikellos, italic; no German noun | `line MemGPT …/planning-loops` → deep-dive.md:106 „Das ist *virtual context management*, und es ist der Mechanismus, mit dem das Arbeitsgedächtnis die Grenze des Kontextfensters überschreiten kann"; `count MemGPT` → 3; `count Kontextverwaltung` **whole DE corpus** → **0** | corpus precedent + canon `rag.md` §2 (MemGPT = bare name, ZERO gloss) |
| **Trajectory evaluation** | German-led | **die Bewertung des Pfades** / **Signale auf Pfadebene** | *die* Bewertung, der Bewertung; *der* Pfad, die Pfade, des Pfad[e]s | `count 'Bewertung des Pfades' …/planning-loops` → 2; index.md:177 („die Evaluierung misst jetzt die Qualität des Pfades"), index.md:212, deep-dive.md:130, `…/agentic-rag/deep-dive.md:90` („**Signale auf Pfadebene**"); `count Trajektorie` **whole DE corpus** → **0** | corpus precedent |
| **pass^k** | class 1 identifier | **pass^k** | artikellos, lowercase, unflected — as is `pass@1` | `grep -F 'pass^k' …/planning-loops` → deep-dive.md:132, :144, :146; deep-dive.md:132 „**pass^k** misst den Anteil der Aufgaben, die in *allen* …" | corpus precedent |

### Flags — §10

- 🔴 **`Reflexion` vs `Reflection / self-critique` — a homograph collision that exists ONLY in German, and the
  glossary is where it does maximum damage.** English has two distinct strings (`reflection` the concept,
  `Reflexion` the framework) and puts both in this section as separate headwords. German renders the concept
  as **`die Reflexion`** (34×) — which is **letter-for-letter the framework's name**. The shipped corpus
  solves it with **code-styling plus an explicit statement**: `` `Reflexion` `` in backticks, and
  `deep-dive.md:47` says outright that the name is a name. **Binding ruling for the glossary: the framework
  headword is `` **`Reflexion`** `` with backticks, the concept headword is `**die Reflexion**` without them,
  and the framework's definition must repeat the disambiguation sentence.** Two adjacent glossary entries
  whose headwords differ only by backticks is exactly the „plausible wrong definition nobody reports" failure
  `rag.md` §7 point 3 describes for anchors — here it arrives through the term list instead, and **no current
  gate looks for it**, because both entries are individually correct.
- 🟡 **Five headwords in this section have no canon row:** `die Umplanung`, `die Abbruchbedingung`,
  `die Schleifenerkennung`, `das episodische / semantische Gedächtnis`, `die Bewertung des Pfades`. All are
  consistent in the corpus; all need `_language.md` §1.1.c lines. ⚠ **`Gedächtnis` in particular**, because it
  is the head of a four-member family (`Arbeits-`, `Langzeit-`, `Kurzzeit-`, `episodisch/semantisch/
  prozedural`) and the canon's only nearby row is the ⛔ against `der Arbeitsspeicher`.
- 🟡 **`Non-termination` and `Plan search` are English nouns with no German noun** (the §7 shape again).
  `Nichtterminierung` and `Plansuche` are both 0× corpus-wide. **Ruling:** the corpus rebuilds —
  „eine Schleife, die nicht richtig endet" and „die Suche im Raum möglicher Pläne" (short: `die Baumsuche`) —
  are the rulings.
- ℹ️ **`Virtual context management` stays English and italic, artikellos.** The one occurrence is explicitly
  framed as naming an English concept („Das ist *virtual context management*"). Not a gap — a decision the
  page already made, and the glossary must match it rather than coin `die virtuelle Kontextverwaltung` (0×).

### Heading and anchor block — §10

```
<a id="planning-loops"></a>

## Agenten – Planung und Schleifen \{#planning-loops}
```

Prescribed **verbatim** by `rag.md` §6.6 („**Agenten – Planung und Schleifen**") and matching the shipped
German `title: Planung und Schleifen`. Note the English `&` becomes `und`.

---

## §11 Consolidated register

### 11.1 The ten anchors, in the binding order, exactly as they must appear

Each section carries **both** lines, in this order, separated by one blank line, with the heading id in
`\{#id}` form — **literal backslash**. `docusaurus.config.ts` sets `future: { v4: true }`, so a bare `{` is
parsed as JSX and the build **hard-fails**. `scripts/locale_parity.py` asserts the **ordered sequence** of
explicit heading ids against English — not the set, the sequence.

| # | `<a id>` line | heading line (German) |
|---|---|---|
| 1 | `<a id="ingestion-chunking"></a>` | `## Ingestion – Chunking \{#ingestion-chunking}` |
| 2 | `<a id="ingestion-embeddings"></a>` | `## Ingestion – Embeddings \{#ingestion-embeddings}` |
| 3 | `<a id="retrieval"></a>` | `## Retrieval \{#retrieval}` |
| 4 | `<a id="generation"></a>` | `## Generation \{#generation}` |
| 5 | `<a id="evaluation"></a>` | `## Evaluierung \{#evaluation}` |
| 6 | `<a id="guardrails"></a>` | `## Guardrails \{#guardrails}` |
| 7 | `<a id="observability"></a>` | `## Observability \{#observability}` |
| 8 | `<a id="agentic-rag"></a>` | `## Agenten – Agentic RAG \{#agentic-rag}` |
| 9 | `<a id="tools"></a>` | `## Agenten – Tool-Einsatz \{#tools}` |
| 10 | `<a id="planning-loops"></a>` | `## Agenten – Planung und Schleifen \{#planning-loops}` |

**Three things the ids are NOT:** they are not translated; they are not reordered; and they are not derivable
from the German heading text — `#evaluation` under „Evaluierung", `#tools` under „Tool-Einsatz",
`#agentic-rag` under „Agenten – Agentic RAG". Verify against
`grep -nE '^<a id=|^## ' docs/glossary.md`, never from memory.

**The two heading decisions that break cross-locale symmetry** (both German-canon-mandated, both easy for a
renderer to "fix" wrongly): `Evaluation → Evaluierung` and `Agents → Agenten`. RU and SK keep the English in
both slots.

### 11.2 Flags by class

**(a) Corpus inconsistent — two forms for one referent (referent-inventory defect)**

| term | forms + counts | ruling |
|---|---|---|
| `head-based / tail-based sampling` | `Head-based Sampling` 2 / `Head-Sampling` 3; `Tail-based Sampling` 2 / `Tail-Sampling` 2 | headword = the **introduced** full form; short compound named in the definition. Split is deliberate but the glossary must pick one string. |
| `chunk overlap` | `Overlap` 2 / `Überlappung` 1 / `Chunk-Overlap` 0 in scope, 1 elsewhere; canon registers a third form | headword **Overlap**; `die Überlappung` in the definition as the measured extent |
| `PII redaction` (cross-lesson) | `Maskierung` 7 in guardrails, `Schwärzung` 0 there / 3 in observability | headword **die Maskierung**; `die Schwärzung` named. Possible cross-lesson wobble — no per-page gate can see it. |

**(b) No corpus occurrence AND no canon/ledger row — genuinely undecided, needs a decision at render time**

| term | what is zero | what is available |
|---|---|---|
| `RAG tracing` | `RAG-Tracing` **0×** corpus-wide; `Tracing` 0× in the mapped lesson | head noun `das Tracing` is settled elsewhere (12×). Compound is a derivation. |
| `embedding space` | no definitional German term | `der Vektorraum`, 2 incidental occurrences |
| `asymmetric` (in `retrieval-optimised (asymmetric) embeddings`) | no German rendering anywhere | keep the English parenthetical |

**(c) Ledger/canon disagrees with the shipped corpus — recorded, ruled FOR THE CORPUS**

| term | canon says | corpus ships | ruling |
|---|---|---|---|
| `self-preference bias` | `rag.md` §3 WEAK: **der Selbstbevorzugungsbias (Self-Preference Bias)** | **`Self-Preference`** kept-EN, 3 sites; `Selbstbevorzugungsbias` **0× corpus-wide** | **Self-Preference**, kept-EN, artikellos, German explanation. Corpus wins, explicitly. |
| `hybrid search` | `rag.md` §2 marks `die hybride Suche` **WEAK** | `die hybride Suche` **10 : 0** in the retrieval lesson alone | `die hybride Suche`; **WEAK marker should be lifted** (canon delta) |
| `chunk overlap` | `_language.md` §1.1.b registers `der Chunk-Overlap` | `Chunk-Overlap` 0× in the ingestion lesson | headword `Overlap` (see (a)) |

**(d) Zero on the loan that is NOT a zero on the referent — checked, referent found**

| headword | the loan | the referent, as shipped |
|---|---|---|
| `Correctness` | `Correctness` 0, `Richtigkeit` 0 in scope | **die Korrektheit**, 3× in the evaluation lesson (and it nearly went in as undecided) |
| `Context packing` | `Packing` 0, `Kontextpackung` 0 | **einen langen Kontext zusammenstellen**, verbal, H2 |
| `Alert fatigue` | `Alert Fatigue` 0, `Alarmmüdigkeit` 0 | „wer zu viel alarmiert, wird nicht mehr gehört" — described |
| `Regression triage` | `Triage` 0 | „einen Qualitätseinbruch auf seine Ursache zurückführen", H2 |
| `Cost attribution` | `Kostenzuordnung` 0 | **die Kosten zuordnen**, verbal |
| `Latency budget` | `Latenzbudget` 0, `Latency Budget` 0 | „eine Obergrenze für die Latenz", „Ziele für p50 und p95" |
| `Non-termination` | `Nichtterminierung` 0 | „eine Schleife, die nicht richtig endet" |
| `Plan search` | `Plansuche` 0 | „die Suche im Raum möglicher Pläne" / `die Baumsuche` |
| `Multi-hop retrieval` | `Multi-Hop` 0 | **der Hop**, 15 case-marked occurrences |
| `Trajectory evaluation` | `Trajektorie` 0 | **die Bewertung des Pfades** |
| `Virtual context management` | `Kontextverwaltung` 0 | *virtual context management*, English, italic |
| `Dimensionality` | `Dimensionalität` 0 | **die Dimensionszahl**, 3× |

**(e) Canon deltas to route (rows the corpus has decided and the canon does not carry)**

`die Dimensionszahl` · `der Eigenbetrieb` · `das zweistufige Schema` · `der Pre-Filter / der Post-Filter` ·
`das Fehlerbild des Retrievals / der Generation` · `die Korrektheit` · `das Erfassen der Nachrichteninhalte` ·
`die Aufbewahrungsstufe` · **`der Hop`** · `die Umplanung` · `die Abbruchbedingung` ·
`die Schleifenerkennung` · `das Gedächtnis` (+ the `Arbeits-/Langzeit-/Kurzzeit-/episodisch/semantisch/
prozedural` family) · `die Bewertung des Pfades` · plus the **class-policy gap** for hybrid compounds
(`der Tool-Einsatz`, `die Tool-Auswahl`, `die Grounding-Anweisung`, `die Chunk-Größe`).

**Nothing in this list is decided here.** They are recorded against the canon so the glossary wave does not
re-derive them and so the next wave does not re-open them.

### 11.3 Eight headwords whose German rendering is not a noun

`context packing` · `input / output validation` · `content safety / moderation` · `regression triage` ·
`cost attribution` · `alert fatigue` · `non-termination` · `plan search` — plus `latency budget` and
`query transformation` / `metadata filtering` / `query planning`, which the canon already rebuilds verbally.

**Shape ruling, stated once so twelve rendering decisions do not each reinvent it:** a **verbal or clausal
glossary headword is correct and is the ruling**, not a stopgap (precedent: `rag.md` §3 on `Gate`,
`Load Shedding`, `packing` — „die Verbalkonstruktion ist kein Notbehelf, sondern das Ruling"). What is
forbidden is coining the missing noun. Each of `die Kontextpackung`, `die Ein-/Ausgabevalidierung`,
`die Regressionstriage`, `die Kostenzuordnung`, `die Alarmmüdigkeit`, `das Latenzbudget`,
`die Nichtterminierung`, `die Plansuche` is **0× corpus-wide**, and four are explicitly ⛔ in the canon.

---

## §12 External references — all 36 verified, 0 dead

Verbatim English sources; **not translated**, per the glossary's own convention. Verified by request, not
trusted from the file:

```
sed -n '15,564p' docs/glossary.md | grep -oE '↗ \[[^]]+\]\((https?://[^)]+)\)' \
  | sed 's/.*(\(http[^)]*\))/\1/' | sort -u \
  | while read u; do echo "$(curl -sS -o /dev/null -w '%{http_code}' -L --max-time 25 -A 'Mozilla/5.0' "$u")  $u"; done
```

**Result: 36 unique URLs, all HTTP 200 after redirects. No 404s, nothing to report.**

- 22 × `arxiv.org/abs/…` — 2004.12832, 2203.11171, 2205.13147, 2210.03629, 2212.10496, 2303.11366,
  2303.17651, 2305.10601, 2306.05685, 2307.03172, 2308.09687, 2309.11495, 2309.15217, 2310.04406,
  2310.08560, 2310.11511, 2401.15884, 2403.14403, 2403.14720, 2404.13208, 2406.12045, 2409.04701
- 9 × `en.wikipedia.org/wiki/…` — `Cohen%27s_kappa`, `Cosine_similarity`, `Discounted_cumulative_gain`,
  `Fleiss%27_kappa`, `Idempotence`, `Mean_reciprocal_rank`, `Okapi_BM25`,
  `Optical_character_recognition`, `Precision_and_recall`
- 1 × `cormack.uwaterloo.ca/cormacksigir09-rrf.pdf` (SIGIR'09, the RRF paper)
- 2 × `sre.google/sre-book/…` (`monitoring-distributed-systems`, `service-level-objectives`)
- 1 × `opentelemetry.io/docs/concepts/sampling/`
- 1 × `www.anthropic.com/news/contextual-retrieval`

⚠ **The percent-encoding in the two kappa URLs is load-bearing** (`%27` for the apostrophe). A renderer that
"tidies" them to a literal `'` breaks both links, and the German entries are the two whose headwords change
shape (`Cohens Kappa` / `Fleiss' Kappa`) — i.e. exactly where a rewrite is tempting.

---

## §13 Instrument note — `scripts/locale-review/concord.py` undercounts German, measurably

The brief warned that this tool once missed stem-changing inflections (`cache` 35→66). **It still undercounts,
by a different and German-specific mechanism.** Measured this pass, same scope, same files:

| term | `concord.py` | raw `grep` | gap |
|---|---|---|---|
| `Chunking` | 44 | 44 | — |
| `Reranker` | 18 | 18 | — |
| `Sampling` | 47 | 47 | — |
| **`Obergrenze`** | **38** | **41** | **−3** |
| **`Gedächtnis`** | **45** | **70** | **−25 (36 %)** |

```
python3 scripts/locale-review/concord.py wave4-a terms.txt \
  i18n/de/.../part-1-rag i18n/de/.../part-2-agents          # concord
grep -rEoi --include='*.md' 'Gedächtnis' part-1-rag part-2-agents | wc -l   # raw
```

**Cause, printed by the tool itself in its own header:**

```
surface forms SOUGHT: gedächtnisers, gedächtnising, gedächtniser, gedächtnises,
                      gedächtnised, gedächtnis's, gedächtniss, gedächtnis', gedächtnis
```

The enumerated surface-form union is **English morphology** — `-s`, `-es`, `-ed`, `-ing`, `-er`, `-ers`,
`'s`, `'`. Two consequences, both real:

1. **German inflections outside that set are invisible.** `Obergrenzen` (plural `-n`) and `Gedächtnisses`
   (strong genitive `-ses`) are missed. Verified as prose, not code fences:
   `grep -rn -E 'Obergrenzen|Gedächtnisses' part-1-rag part-2-agents` → 4 hits, all running text.
2. **Worse: the stem is invisible when it is the SECOND element of a German compound.** `Arbeitsgedächtnis`
   13×, `Langzeitgedächtnis` 5×, `Kurzzeitgedächtnis` 2× — **20 occurrences of the head noun the tool cannot
   see**, because a word-initial boundary match cannot reach a head-final compound. German is a
   compounding language; this is not an edge case, it is the normal shape of its technical vocabulary.

**Practical rule for the rendering agents: never take a German count from `concord.py` alone.** It is reliable
for kept-EN loans that do not compound (`Chunking`, `Reranker`, `Sampling` all matched exactly) and it
systematically understates any German head noun. Its *sentence extraction* remains valuable — that is what it
is for. Its *arithmetic* is not.

---

## Lessons

**1. The corpus told me things the canon did not, and one of them reverses a canon prescription.**
`self-preference bias` is the sharp case: the canon prescribes a pattern-licensed coinage
(`der Selbstbevorzugungsbias`) and the shipped pages ship kept-EN `Self-Preference` instead — 0× vs 3 sites —
while *Germanising the other two biases in the same list*. The canon row's own reasoning („das Muster
lizenziert die FORM, nicht das WORT") predicts exactly that outcome; its prescription contradicts its
reasoning. **A canon row can be internally inconsistent in a way only the corpus exposes**, and this is the
fourth instance in this project's record of *the register was the defective part, not the prose*
(`Error-Budget`, `Golden Set`, the U+2014 glosses, now this).

**2. A ruling can be undecidable from the mapped lesson and settled two directories away.** `RAG tracing`:
`Tracing` is 0× in the observability lesson (which runs on `der Trace` and verbs) and 12× with a clean article
in `orchestration-frameworks` and `tooling-ecosystem`. Had I honoured the anchor→lesson mapping strictly, I
would have filed the whole term as undecided. **The mapped lesson is where a term is *authoritative*, not
where it is *exhaustively* evidenced** — and for a glossary, whose entries are read from every page, the
corpus-wide scope is the honest one. This is a defect in the *method as briefed*, and the mapping is still
right for direction; it is wrong for existence.

**3. The instrument misled me in a new way, and it is German-specific.** `concord.py` reported `Gedächtnis`
45× where the tree has 70. Not the documented stem-change bug — its surface-form union is English morphology,
so it misses `-n` plurals, `-ses` genitives, and **every occurrence where the stem is the head of a compound**
(`Arbeitsgedächtnis` 13×, `Langzeitgedächtnis` 5×, `Kurzzeitgedächtnis` 2×). The tool's own docstring says a
narrowing regex fabricates *absences*; this is that failure recurring one abstraction up — the enumeration
fixed English morphology and thereby hard-coded the assumption that a term's occurrences begin at a word
boundary. **In a compounding language that assumption is false by default**, and the error is silent and
one-directional: it can only ever under-report, which means it can only ever manufacture a false "this term
is rare / absent" verdict.

**4. Defect classes no current gate would catch.**
- **The German-only homograph.** `die Reflexion` (the concept) and `Reflexion` (the framework) are one string
  in German and two in English. The glossary puts both in one section, adjacent. The shipped corpus solved it
  with backticks plus an explicit sentence; **nothing enforces that**, and both entries are individually
  correct, so a term-consistency gate, a naturalness gate and a parity gate all pass a glossary that has
  quietly merged them. The failure mode is `rag.md` §7's „plausible wrong definition nobody reports", arriving
  through the *term list* instead of through an *anchor*. A gate would have to be: *for each pair of headwords
  in a section, is the German rendering identical?*
- **The anchor with no inbound link.** `#ingestion-embeddings` exists, is in order, is parity-clean — and
  **nothing in any locale links to it**; all three ingestion footers point at `#ingestion-chunking`, including
  the one listing the embeddings terms. `locale_parity.py` checks id sequence, not reachability, so an anchor
  can be structurally perfect and functionally dead. A gate would have to be: *every explicit heading id has
  ≥1 inbound `glossary.md#id` reference somewhere in `docs/`.*
- **The cross-lesson term wobble.** `Maskierung` (guardrails, 7×) vs `Schwärzung` (observability, 3×) for what
  may be one referent. Every per-page gate passes; the split is only visible when you diff two lessons'
  vocabularies against each other, which nothing does.
- **The headword whose German is not a noun.** Eight of my 157. The English glossary's `**Noun** — definition`
  format silently assumes the target language has a noun. It is not a translation problem — it is a **format**
  problem, and the format is what a renderer will try to satisfy, by coining.

**5. What convicted, and what could not acquit.** Every ruling above that rests on `corpus precedent` rests on
a form the German pages already ship, so where the shipped German is wrong my sheet is confidently wrong with
it — the README's second self-limit, in force. The rows most exposed are the ones I flagged as thin:
`der Vektorraum` (2 incidental occurrences), `Multi-Vector-Darstellung` (1), `Defence-in-Depth` (1),
`die Aufbewahrungsstufe` (1), `das Retry-Budget` (1, uninflected). **A single-occurrence ruling is a ruling
about one sentence**, and I have said so in each cell rather than letting the count column imply otherwise.
