# Wave 4 — binding decisions for the German glossary (`#283`)

The two reconciliation ledgers (`WAVE4-GLOSSARY-A.md`, sections 1–10; `WAVE4-GLOSSARY-B.md`, sections 11–19)
rule 298 headwords between them. This file settles the things that are **not** per-headword and that the
ledgers either split on or could not see from inside a slice. **A rendering agent obeys this file over either
ledger where they differ.**

## 1. The section heading table — verbatim, in this order, no latitude

19 sections. The anchor ids are **English, unchanged, and in the English order**;
`scripts/locale_parity.py` asserts ordered equality across locales. Each section carries **both** an HTML
anchor line and an explicit heading id. The backslash in `\{#id}` is load-bearing: `future.v4: true`
disables the MDX1 compat preprocessor, so a bare `{` is parsed as JSX and hard-fails the build.

| # | `<a id>` line | heading line |
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
| 11 | `<a id="multi-agent"></a>` | `## Agenten – Multi-Agenten-Systeme \{#multi-agent}` |
| 12 | `<a id="orchestration-frameworks"></a>` | `## Agenten – Orchestrierungs-Frameworks \{#orchestration-frameworks}` |
| 13 | `<a id="mcp"></a>` | `## Agenten – MCP und Agentenprotokolle \{#mcp}` |
| 14 | `<a id="real-agents"></a>` | `## Agenten – echte Agenten (Abschluss dieses Teils) \{#real-agents}` |
| 15 | `<a id="production-failures"></a>` | `## Produktivbetrieb – warum KI im Betrieb versagt \{#production-failures}` |
| 16 | `<a id="serving"></a>` | `## Produktivbetrieb – Bereitstellung \{#serving}` |
| 17 | `<a id="cloud-platforms"></a>` | `## Produktivbetrieb – Cloud-KI-Plattformen \{#cloud-platforms}` |
| 18 | `<a id="tooling-ecosystem"></a>` | `## Produktivbetrieb – das Tooling-Ökosystem \{#tooling-ecosystem}` |
| 19 | `<a id="llmops"></a>` | `## Produktivbetrieb – LLMOps \{#llmops}` |

### Why the family token is German — the ledgers split on this, and A was right

`WAVE4-GLOSSARY-A.md` proposed `Agenten`; `WAVE4-GLOSSARY-B.md` proposed keeping `Agents` and `Production`
in English, on cross-locale symmetry (RU and SK both keep the English tag). **Ruled for German**, on the
corpus:

- `i18n/de/…/current.json` ships `Part II — Agents` → **`Teil II – Agenten`** and
  `Part III — Production & LLMOps` → **`Teil III – Produktivbetrieb und LLMOps`**. Every navigational
  surface a German reader meets — sidebar, footer, part title, part H1 — writes `Agenten` and
  `Produktivbetrieb`. A glossary heading reading `## Agents – Tool-Einsatz` would be the **only** place in
  the German corpus that writes `Agents`.
- The tokens that **stay** English do so because German keeps them as terms of art, and the corpus proves it
  per token: `Ingestion`, `Retrieval`, `Generation`, `Guardrails`, `Observability` are kept-EN in the shipped
  sidebar. `Agents` and `Production` are **not** — the corpus Germanises both.

So the rule is not "translate the tag" or "keep the tag", it is **use the form the German corpus already uses
for that token**, checked per token. That is the `#328` corpus-precedence rule, and it happens to break
cross-locale symmetry in exactly two slots — which the Vorrangregel permits.

Two consequences a renderer must not "fix": the id under a Germanised heading is still English
(`#evaluation` under „Evaluierung", `#tools` under „Agenten – Tool-Einsatz"), and headings 15–19 say
`Produktivbetrieb` while the ids say `production-*`.

## 2. Two shipped defects this pass found — fix in the same PR

Both are **term-level** disagreements between a page title and its sidebar label, i.e. the same referent
under two German names in one locale. Not length abbreviations — those are legitimate and stay.

| surface | ships | should be | evidence |
|---|---|---|---|
| `current.json` category `Evaluation` | `Evaluation` | **`Evaluierung`** | the lesson's own page is `title: "Evaluierung"`; `Evaluierung` 16× in the lesson vs `Evaluation` 2×, **both English strings** (a YouTube title, and `RAG-Evaluierung`); canon `rag.md` §6.6 rules „*Evaluation* wird zu **Evaluierung**" |
| `current.json` category `Serving — FastAPI + Docker` | `Serving – FastAPI und Docker` | **`Bereitstellung und Betrieb – FastAPI und Docker`** | the lesson's own page is `title: "Bereitstellung und Betrieb – FastAPI + Docker"` |

A third is **not** a defect and must be left alone: the LLMOps sidebar label
(`LLMOps – Bereitstellung, Überwachung, Kosten`) differs from the page title
(`LLMOps – ausrollen, überwachen, Kosten`) as *nouns vs verbs*, a legitimate label/title difference.

## 3. Standing rules for the glossary page

- **Register:** «Sie». Action labels take the infinitive. A glossary definition is usually verbless, so most
  entries never address the reader at all — do not insert an addressee to sound friendly.
- **Typography:** the Gedankenstrich is a **spaced en dash `–`**. The corpus is decisive at **1533 `–` vs 26
  `—`**, and all 26 em dashes are inside `<YouTube title="…">` attributes, i.e. verbatim English citations.
  So: **zero em dashes in this file.** Quotation marks are `„…"` (223 balanced pairs corpus-wide, zero
  guillemets). `20 %` takes U+202F.
- **Headword format:** `**Headword** – definition.` The dash after the headword is the spaced en dash, not
  the em dash the English uses.
- **Headword direction** is per the ledgers, term by term. Kept-EN headword leads English with a German
  gloss; German-led headword leads German with the English original alongside. **The direction must match
  the body.** This is the failure Slovak paid for at Fáza 25 and the reason the ledgers exist.
- **External references** (`↗ [Wikipedia](…)`, `↗ [arXiv](…)`) are English sources and are **not** translated.
  All 48 URLs across both slices were verified HTTP 200 (36 in A, 12 in B). Do not re-coin, do not re-order,
  do not drop the `↗`.
- **Eight headwords have no German noun** (`context packing`, `alert fatigue`, `regression triage`,
  `cost attribution`, `non-termination`, `plan search`, input/output validation, content safety). The
  English `**Noun** — definition` shape assumes the target language has a noun. **Do not coin one.** Use the
  corpus-attested construction the ledger names for each (usually verbal, e.g. `die Kosten zuordnen`).

## 4. The `[Neue Begriffe]` trap — read this before grepping the corpus

Every German lesson page ends with an English, lowercase `[Neue Begriffe]` term list. So a naive
`grep -i <term> i18n/de/` returns **English footer hits** and will misrule a German-led term as kept-EN.
`grep -roi handoff` returns 2 — both English footers — while the corpus writes `die Übergabe` **28×** and
`der Subagent` **11×**. Three headwords nearly went in wrong on this. `WAVE3-TERMS.md` §6 recorded the
carve-out for two pages; it is **corpus-wide**.

**And the licence expires with this wave.** Those footers are English *"until the glossary ships"*. This is
that wave. Left alone, ~30 footers become live regressions of `die Instrumentierung` / `die Übergabe` /
`der Bewerter`; translated, every occurrence count in every earlier ledger silently shifts, because the
footers were the excluded set. **Decide it in this PR** — see §6.

## 5. `concord.py` undercounts German, in two independent ways

Do not trust it as a sole source; verify with your own `grep -oiE` on the stem.

1. Its surface-form union is **English morphology**, so it misses `-n` plurals, `-ses` genitives, and
   **every occurrence where the stem heads a compound**. Measured: `Gedächtnis` **45 vs 70** (−36 %;
   `Arbeits-` 13×, `Langzeit-` 5×, `Kurzzeit-` 2× invisible), `Obergrenze` 38 vs 41.
2. It previously missed stem-changing inflections outright (`cache` 35 → 66).

Both are **silent and one-directional**: they can only manufacture false "rare" or "absent" verdicts. And the
mirror-image trap is a raw stem grep, which **over**counts — `grep -i brech` matches inside `Berechnung`,
`grep -i erfahren` matches inside `Verfahren`. Anchor the pattern, and read the hits.

## 6. Open items this wave must decide rather than inherit

- **The `[Neue Begriffe]` footers** (§4) — translate now, or record an explicit expiry. Either is defensible;
  silence is not, because the next term pass will read them as regressions.
- **`die Agentenlaufzeit`** — a coinage the canon **bans**, which nevertheless **shipped** at
  `part-2-agents/mcp/deep-dive.md:15`, leaked out of the canon's own `Host` Pflichtglosse. `WAVE3-TERMS.md`
  W3-4 predicted the mechanism; this is the live token.
- **`Rug-Pull` 4 : `Rug Pull` 2** and **`Reinforcement-Fine-Tuning` 3 : 1** — shipped spelling
  inconsistencies (referent-inventory defects), Part I.
- **`die Reflexion`** — a German-only homograph: *Reflexion* (the concept) and *Reflexion* (the framework)
  are two English strings and **one** German string, sitting as **adjacent headwords in the same section**.
  The shipped corpus disambiguates with backticks plus an explicit sentence; nothing enforces it, and both
  entries are individually correct, so term-consistency, naturalness **and** parity gates all pass a glossary
  that has quietly merged two referents. The rendered section must keep them apart explicitly.
- **`self-preference bias`** — the canon prescribes `der Selbstbevorzugungsbias`; the corpus ships kept-EN
  `Self-Preference` at 3 sites and the coinage **0×**, while the other two biases in the same list *were*
  Germanised (`Positionsbias` 7×, `Ausführlichkeitsbias` 3×). Ruled for the corpus. Canon delta to route.
- **`hybride Suche`** — canon marks it WEAK; corpus ships it **10 : 0**. The WEAK marker should be lifted.
- **`#ingestion-embeddings` has zero inbound links in every locale** — structurally parity-clean,
  functionally dead. A pre-existing English-source defect, not a German one; file against `en-source`.
