# WAVE3-TERMS.md — the binding sheet for the German RAG wave 3 (Part III, production & LLMOps)

**Gate 6.5, stage 2 — the cross-slice collision gate.** Produced from the seven slice ledgers
`LEDGER-{A…G}.md`, with drill-downs into the fourteen raw attestation sheets, the concordances, the
**27 shipped German pages**, the German canon and the 134-label Mermaid inventory.

**Where this sheet and the German canon differ, this sheet wins and says why (§11 `CANON DELTA`).**
Nothing in the canon was edited. No git was run. The worktree was read only.

---

## 0. How to read this sheet — and the one rule that governs it

**This sheet is authoritative for everything it names. For every term it does NOT name, the slice ledger
binds unchanged.** Reproducing ~250 rows from seven ledgers would introduce transcription drift, which is
the defect this gate exists to prevent — so this sheet carries exactly four things:

1. every row a **collision** changed (§1, §2);
2. every **cross-page binding string** — one string per term that spans several files (§4), including the
   **Mermaid labels** (§5), a surface no prose gate reads;
3. every row this gate had to **decide** rather than derive (§8), and every row left **OPEN** (§9);
4. the **arithmetic**, computed once from the union (§10), and the **canon delta** (§11).

**Routing for everything else** — `serving mechanics · runtime · compute` → **LEDGER-A** ·
`queueing · load · latency` → **LEDGER-B** · `platform · sovereignty · residency · tenancy` → **LEDGER-C** ·
`money` → **LEDGER-D** · `release · gating · versioning · incidents` → **LEDGER-E** ·
`tooling · eval · observability · guardrails` → **LEDGER-F** · everything the A–F partition missed → **LEDGER-G**.

> ### The rule this sheet is built on, and it is a measurement of this project, not a preference
> **A sense split that ships a WORKED SENTENCE survives contact with prose; one that ships only a word gets
> dodged.** Therefore every branch below ships a German sentence, and **every worked sentence here has been
> checked against the ruling in its own row** and diffed against the wave's ban list
> (`banscan.py --skip-group=typography`). Renderers copy these sentences verbatim. That is what they are for.

**Run the scanner. It is now longer than it was.** This merge added **28 rules** in a new group
`wave3_merge_bans` — every one of them a ban that **no single slice could see**, because no slice can see
its neighbours. It also **narrowed two rules that were too wide** (`Laufzeitumgebung`, `einfrieren`): an
over-broad ban is not a safe ban, it teaches the renderer to ignore the scanner.

---

## 1. The collisions — what was found, and how each was resolved

Resolution used the two ranked tie-breakers from the brief: **(a)** the slice that studied a referent
**specifically** outranks the slice that used it **in passing**; **(b)** where a sheet and the shipped corpus
disagree, **the register is the suspect**. Both sides of every collision stay on the record.

### 1.1 The twelve that would have shipped as errors

| # | Collision | Sides | **RULING** | Why |
|---|---|---|---|---|
| **X-1** | `inference server` | **A**: `die Inferenz-Engine`, ⛔ *der Inferenzserver* on a measured triple zero · **C**: writes „ein Inferenzserver auf Ihren eigenen GPUs“ **in a worked sentence** | **`die Inferenz-Engine`** | Tie-breaker (a): A studied it (19 occ, 4 files, both runs measured the coinage at zero). C used it in passing. A confirmed incumbent beats a coinage |
| **X-2** | `Semaphor` **gender** | **B**: `der Semaphor` / des Semaphors / die Semaphore, canon row filed · **A**: „mit **einer** Semaphore“ | **`der Semaphor`, „mit einem Semaphor“** | Tie-breaker (a). A gender error in a Mermaid label and a take-away sentence |
| **X-3** | `event loop` **gender + word** | **A**: `der Event-Loop`, ⛔ *die Ereignisschleife* (0 in the corpus, 0 in the one native article) · **B**: „die **Ereignisschleife** blockieren“ · **E**: „legt **die gesamte** Event-Loop lahm“ | **`der Event-Loop`, Verb `blockieren`** | Tie-breaker (a): A owns the row and resolved a frontal two-house gender split on **case-marked** evidence. Two other slices independently got it wrong, in two different ways |
| **X-4** | `queue` | **B**: `die Queue`, 45 of 45; ⛔ *Warteschlangentiefe*, ⛔ *Queue-Tiefe* · **A**: „skalieren Sie auf **Warteschlangentiefe**“ · **C**: „**Warteschlangen** je Mandant“ · **E**: „zur gewöhnlichen **Warteschlange**“ | **`die Queue`** everywhere; **„die Länge der Queue“** for *queue depth*; „**Queues je Mandant**“ | Tie-breaker (a). `die Warteschlange` stays canon-licensed for the data structure, which has **zero** Part III occurrences |
| **X-5** | `Red-Team*` compound | **F**: `Red-Teaming-Läufe` (the attested compound family is `Red-Teaming-`, never `Red-Team-`) · **A**: `Red-Team-Durchläufe` (`Lauf` ships 0, `Durchlauf` 43 case-marked) | **`der Red-Teaming-Durchlauf`** | **Two-way collision, each slice half right.** Take F's base form and A's head noun. Each slice violated the other's half |
| **X-6** | `merge` (git) | **F**: „Metriken unter dem Schwellenwert blockieren **die Zusammenführung**“ · **E**: „eine Prüfung blockiert **den Merge**“ | **„den Merge blockieren“** | **Settled at the corpus by this gate.** All 12 shipped `Zusammenführung` are in `retrieval/{index,deep-dive}.md` and every one is **retrieval-result fusion** (RRF) — including a deep-dive title and a `sidebar_label`. The word is occupied. `Merge` ships 3×, all git |
| **X-7** | `traffic` | **E** writes both `Traffic` („auf den vollen Traffic ausgeweitet“) and `Verkehr` | **`der Verkehr`** | Contradiction **inside one sheet**. `Traffic` ships exactly once, inside the quoted Golden-Signals enumeration — a class-1 citation, not a running term |
| **X-8** | `Datenresidenz` | **C** and **G** both reject the coinage · **D** („der Regler zwischen Datenresidenz und Kapazität“) and **E** („aus Gründen der Datenresidenz“) use it **in worked sentences** | **`die Data Residency`** (term positions) + **`der Speicherort`** (running prose) — see §8, D-1 | Tie-breaker (a). Both slices that studied `residency` reject it; both that used it in passing wrote it |
| **X-9** | „Daten **in der Region** halten“ | **C**: ⛔ — „in der Region“ is the standing German idiom for *im Umland* · **E**: writes it twice | **„in derselben Region halten“ / „in der gewählten Cloud-Region“ / „an eine Region binden“** | Tie-breaker (a). C owns `region` (24 occ, 4 files) and produced the idiom evidence |
| **X-10** | `regionsübergreifend` | **G**: ⛔ — both runs counted the same 10 de.wikipedia hits; the one that **read** them found all ten are urban planning / demography / tourism, zero IT · **C** licenses it, **E** uses it | ⛔ — rebuild: **„zwischen Regionen“ · „über Regionsgrenzen hinweg“** | A count is not a reading. 0 in the shipped German |
| **X-11** | `Agentenlaufzeit` | **A**: ⛔ — a canon coinage, de.wikipedia insource **0**, shipped through `_language.md`'s obligatory `Host` gloss · **G**: uses it in a worked sentence | **`die Agenten-Laufzeitumgebung`** | A files the canon repair (C3); G inherited the defect from the same gloss that caused it |
| **X-12** | `Preisstufe` | **B**: measured `insource:"Preisstufe"` = **95, all Verkehrsverbund fare zones**, 0 shipped · **D**: binds it for *pricing tier* | **`der Tarif`** | Tie-breaker (a): B owns `tier` (30 occ, 7 files). D's row was written one slice away from B's measurement |

### 1.2 The four frontal disagreements between two slices that each studied the term

| # | Collision | **RULING** | The losing argument, on the record |
|---|---|---|---|
| **X-13** | **`managed`** — **C**: kept-EN `Managed-`, ⛔ *verwaltet* („Herstellerlokalisierung; `Verwaltung` = IAM“) · **G**: attributive **`verwaltet`**, CORPUS(9) | **`verwaltet`, flektiert**, for the appellative. **`Managed`** stays kept-EN only inside a fixed product-category name with an **English head** (`Managed Service`, `Managed Knowledge Base`) and in product names (class 1) | **I re-measured: `verwaltet` 9, `Managed` 0** over the 27 pages, inflected and attributive, in exactly the construction Part III needs — „semantisches RAG als **verwalteter** Baustein“, „eine **verwaltete** RAG Engine“, „auf **verwaltetes** RAG“. C's ⛔ is an assertion; G's ruling is a measurement. **Both slices keep their strongest half**: C's `der Managed Service` row survives (English head), C's Durchkopplung rule survives for English first elements. Slice A had independently written „die **verwaltete** Agenten-Laufzeitumgebung“ — a third slice converging on G's side |
| **X-14** | **`Enterprise-`** — **C**: germanise (`der Rahmenvertrag`, `die Funktionen für Unternehmenskunden`) · **G**: `Enterprise-`, durchgekoppelt | **Germanise the appellative.** `Enterprise-` stays kept-EN only in a **plan name** (`das Enterprise-Abo`, `die Enterprise-Version`) and in `Enterprise-Reifegrad` (a different course, not forked) | **G refutes itself**: its own run 1 measured `Enterprise-Tarif` de.wikipedia insource = **0** and logged the refutation; its `reserved` row then writes „den **Enterprise-Tarifen** vorbehalten“. G's corpus hit `Enterprise-Reifegrad` is a **different referent** (the AI-SDLC maturity tier), which C flagged correctly. Corpus `Unternehmen` **22 : 0**. ⛔ `Enterprise-Tarif` |
| **X-15** | **`Werkzeugkatalog` vs `Tooling-Ökosystem`** — **C** binds `der Werkzeugkatalog` as a cross-reference duty (C-17, C:178) · **F** flags `Werkzeug-Ökosystem` / `Tool-Ökosystem` as defects (D8/D9) | **`das Tooling-Ökosystem`** | Per the brief's own measurement: **3 : 1 : 1** across five live cross-references into this very lesson; it is the form used in the two live navigational links; and `Werkzeugkatalog` additionally collides with the `Tool-Katalog` referent. **Slice C's argument is recorded and loses.** ⚠ A 3:1:1 corpus spread is a **defect signal, not a ruling** — the fix is to bind the majority form, not to follow the spread |
| **X-16** | **`Perimeterschutz`** — **C** lists it as a licensed collocation · **G** measured BSI INF.1.A35: fences, lighting, Haustechnik | ⛔ **`der Perimeterschutz`**. Use **„innerhalb / außerhalb des Perimeters“** (+ Genitiv) | A measured wrong referent beats an unmeasured collocation. Same shape: ⛔ **`die souveräne Region`** (G measured de.wikipedia's one hit as constitutional geography; C offers it without evidence) → „**eine Region in einer souveränen Cloud**“ |

### 1.3 The four the ban scan found — a defect two runs share looks exactly like confirmation

The brief's ADDENDUM A1 is the reason these exist. A ledger cannot catch what both of its runs did.

- **`die Generierung` in three slices' worked sentences (A, B, G)** — a **standing regression**; the corpus is
  unanimous (`Generation` **63** : `Generierung` **0**). ⚠ **And the repair is not one repair.** The plural
  `Generationen` is **0** in the corpus and reads as generations of people or products. So:
  - the *RAG stage* → straight swap: „…wenn **die Generation** auf halber Strecke abbricht.“
  - *concurrent generations* → **count the object**: „…**die Zahl gleichzeitiger Modellaufrufe**.“
    (This is slice A's own C2 rule — *count the referent object, not the property* — applied to its own sentence.)
- **`die Stapelverarbeitung`** — **A** licenses it for the pricing tier; **B**, which owns `tier`, bans it there
  because it names the **procedure** and flattens the distinction the corpus warns about twice. ⛔ on both sides.
- **`warm gehaltene Instanzen`** — **B**'s participle drags DWDS's *jmd. hält sich jmdn. warm* (= keep someone
  sweet), the exact idiom **A** banned. Bind A's rebuild: **„ein Vorrat bereits gestarteter Instanzen“**.
- **`die Erfolgsquote der Angriffe`** — **the corpus already split these two words and slice A crossed the
  line.** `die Erfolgsrate der Angriffe` (*attack success rate*) ships **12×**; `die Erfolgsquote` ships once,
  glossed *(task success rate)*. Two referents, two shipped words — so slice D's „seine **Erfolgsquote**“ for a
  model's task success is **correct** and A's for attacks is not. This is ADDENDUM A4 in miniature: the
  measurement was right and it was about the other word.

### 1.4 The three contradictions **inside a single sheet** (ADDENDUM A2)

Wave 2 found ruling-vs-example contradictions run-against-run. They also live inside one ledger, in the gap
between the ruling cell and the example beside it.

| Sheet | The ruling | Its own worked sentence | Bound |
|---|---|---|---|
| **E** | ⛔ `die Fassung` as the running term for `version` | „Ein Canary Release schickt einen Teil des Verkehrs auf **die neue Fassung**.“ | „…auf **die neue Version**.“ ⚠ `die Fassung` is not banned — the corpus ships it **29×** for the **edition of a specification or an offering** („in der **Fassung** 2025-03-26 der Spezifikation“). Two referents, two words |
| **G** | `managed` → attributive `verwaltet`; `Angebot` for the packaged product | writes **both** „die verwaltete **RAG-Stufe**“ and „verwaltetes **Angebot**“ | **„ein verwaltetes RAG-Angebot“** (see X-17 below) |
| **G** | run 1 measured `Enterprise-Tarif` = 0 and logged the refutation | the `reserved` row writes „den **Enterprise-Tarifen** vorbehalten“ | „…**den Tarifen für Unternehmen vorbehalten**“ |

**X-17 · `managed RAG tier`** — **C** and **G** write `die (Managed-)RAG-Stufe`; **B**, which owns `tier`,
measured the occupancy (`Stufe` **55** as *rung/stage*, `Ebene` **35**, `Angebot` **1**) and rules
`das Angebot` — the least-occupied word wins. **Bound: „ein verwaltetes RAG-Angebot (*managed RAG*)“**,
compact form **`das Managed-RAG-Angebot`**. ⛔ `die Managed-RAG-Stufe`.

### 1.5 The collision that lives only in a Mermaid edge

**X-18 · „gates the deploy“ — the same edge label in two diagrams, two German strings.** The facts index
requires this edge to be **identical** in `te/i` L134 and `te/d` L127. **Slice E** rules the verb sense of
`gate` as Mermaid „**gibt das Deployment frei**“; **slice F**, ruling the sibling edge from inside the diagram,
writes „**gibt die Auslieferung frei**“. **Ruling: „gibt das Deployment frei“ / „blockiert das Deployment“** —
tie-breaker (a): slice E owns `deploy` (30 occurrences, 9 files) and settled the countable `das Deployment` on
**4 shipped occurrences**, while `die Auslieferung` ships **once** and slice E had already flagged the word as
occupied. ⚠ **This one is worth its own number because of where it lives:** it is inside a fence, so the
census, the register pass and the cold read all skip it — **while the reader sees it rendered**. Two slices
diverging on a string no prose gate reads is the exact shape ADDENDUM A7 was written for.

**Three referents, three words, so nothing collapses:** `die Auslieferung` = the act of delivering or serving ·
`das Deployment` = one countable deploy event · `die Bereitstellung` = the deploy process and discipline.

### 1.6 Convergences worth recording — two slices reaching the same place independently is evidence

- **`die Kapazitätsgrenze`** for a limit you *hit*: **G** rules it (`ceiling`), **A** independently writes
  „jenseits der **Kapazitätsgrenze**“ for *past capacity*. Same phenomenon, same word, two slices, no contact.
  This materially strengthens G's D-A recommendation (§8, D-2).
- **`die Momentaufnahme`**: **E** hand-counts `snapshot` sense (B) at **19 of 29** and **G** independently
  claims the same word for `roster`. **They are the same occurrences.** No collision — and the brief's premise
  („overwhelmingly a pinned model version“) is refuted by a hand count: exactly **one** occurrence is that.
- **`der Hebel` / `die Stellschraube` / `der Regler`**: **D** and **G** reach the identical three-way split
  from opposite directions, both against their own runs. Bind it.
- **`der Anbieter`** (CORPUS 38 : 0) and **`der Eigenbetrieb`** (bound, never bare): **C** and **G** agree
  and each supplies the other's missing half (C the count and the referent reading, G the binding obligation).

---

## 2. Binding table — the rows this gate changed or decided

`Class`: 1 = identifier / product name · 2 = kept-EN loan with a German article · 3 = German-led (gloss at
first mention) · 4 = fully German.

| Terminus | German | Cl. | Status | Artikel / Plural / Genitiv | Kollokation | ⛔ rejected | Evidence |
|---|---|---|---|---|---|---|---|
| **runtime** (host platform) | **die Laufzeitumgebung**; Erstnennung **die verwaltete Agenten-Laufzeitumgebung**; Anapher **die Umgebung** | 3 | **BOUND — released against the canon's blanket ⛔** | die / die -en / der Laufzeitumgebung | „die Laufzeitumgebung **führt die Agentenschleife aus**“ | ⛔ bare `die Laufzeit` as a **component name** · ⛔ *die Agentenlaufzeit* (canon coinage, insource 0) · ⛔ *das/der Runtime* | A, RECONCILED + 4 houses. ⚠ **The brief's premise was wrong** (A6): the component sense ships **5× in 2 files**, four of them on one page — so the row stands on **attestation**, not on renderer convergence |
| **runtime** (vendor component) | **Runtime** im Namen, sonst **die Runtime** | 1 / 2 | **BOUND** | die / die -s / der Runtime | „**Die Runtime** gibt Ausführungsfenster von bis zu acht Stunden“ | ⛔ translating the product name | AGREED×2 + the one native article on this exact product |
| **runtime** (temporal) | **zur Laufzeit** | 3 | **CORPUS PRECEDENT** | adverbial | „**zur Laufzeit** durchsetzen“ | — | CORPUS(8) |
| **inference server / engine** | **die Inferenz-Engine**, Erstnennung mit Klammerglosse *(inference server)* | 2 | **OPEN — incumbent held** (§9) | die / die -s / der Inferenz-Engine | „**Die Inferenz-Engine hält das Modell, FastAPI hält das Produkt.**“ | ⛔ **der Inferenzserver** (measured triple zero) · ⛔ *der Inference Server* | X-1. ⚠ THIN: heise + iX are **one** Stilfamilie counted twice |
| **event loop** | **der Event-Loop** | 2 | **OPEN — incumbent held** (§9) | der / die -s / **des Event-Loops** | „**den Event-Loop blockieren**“ · „die Kontrolle **an den Event-Loop zurückgeben**“ | ⛔ *die* Event-Loop · ⛔ *die Ereignisschleife* · ⛔ *einfrieren* · ⛔ *lahmlegen* | X-3. Case-marked evidence outranks nominative article counts |
| **semaphore** | **der Semaphor** | 2 | **BOUND** | der / **die Semaphore** / des Semaphors | „**mit einem Semaphor begrenzen**“ | ⛔ *eine Semaphore* (feminine) | X-2 |
| **concurrency** (a number) | **das Bezugsobjekt zählen**: „die Zahl gleichzeitiger **Modellaufrufe**“ | 3 | **BOUND** | — | „**Obergrenzen je Mandant für gleichzeitige Modellaufrufe.**“ | ⛔ *gleichzeitige Generierungen* · ⛔ „eine große Nebenläufigkeit“ | §1.3. The German noun is a **property**, not a counter |
| **concurrency** (property) | adverbial **nebenläufig**; Substantiv **die Nebenläufigkeit** nur im Kontrast **und in der Deckel-Fügung** | 3 | **CORPUS PRECEDENT** | die / — / der Nebenläufigkeit | „**eine Obergrenze für die Nebenläufigkeit setzen**“ | ⛔ *die Concurrency* · ⛔ *die Gleichzeitigkeit* | A: CORPUS(16 adverbial, 0 noun) + B's cap construction. **Boundary stated so the two do not fight** |
| **queue** | **die Queue**; Erstnennung je Seite „die Queue (Warteschlange)“ | 2 | **BOUND — 45 of 45** | die / die Queues / der Queue | „die Queue **abarbeiten**“ · „**in die Queue stellen**“ | ⛔ bare *die Warteschlange* in Part III · ⛔ *die Warteschlangentiefe* / *Queue-Tiefe* | X-4 |
| **queue depth** | **die Länge der Queue** | 3 | **BOUND** | die / die -n / der Länge | „**auf die Länge der Queue und die GPU-Auslastung skalieren**“ | as above | X-4 |
| **merge** (git) | **der Merge** | 2 | **CORPUS PRECEDENT** | der / die Merges / des Merges | „**den Merge blockieren**“ · der Merge-Zustand | ⛔ **die Zusammenführung** — occupied by *retrieval fusion*, 12×, incl. a deep-dive title and a `sidebar_label` | X-6, measured by this gate |
| **managed** (attributiv) | **verwaltet**, flektiert | 3 | **CORPUS PRECEDENT (9 : 0)** | Adjektiv | „semantisches RAG als **verwalteter Baustein**“ · „eine **verwaltete** RAG Engine“ | ⛔ *gemanagt* · ⛔ kept-EN `Managed-` vor deutschem Grundwort | X-13. **§1.1.g row** |
| **managed** (Kategoriename mit engl. Kopf) | **Managed Service**, unflektiert, gespreizt | 2 | **BOUND** | der Managed Service / die -s / des Managed Service[s] | „die Guardrails **als Managed Services** beziehen“ | ⛔ *der verwaltete Dienst* als Kategoriename · ⛔ „Managed Plattform“ | C, unchanged |
| **managed RAG** | **ein verwaltetes RAG-Angebot** (*managed RAG*); kompakt **das Managed-RAG-Angebot**; `Managed RAG` artikellos in Subjektstellung | 2 / 3 | **BOUND** | das / die -e / des -Angebot[e]s | „**Jede Plattform verkauft außerdem ein verwaltetes RAG-Angebot: die Pipeline aus Teil 1 als fertigen Dienst.**“ | ⛔ *die Managed-RAG-Stufe* · ⛔ „das Managed RAG“ mit eigenem Artikel | X-17. `RAG` ships 124× and **never** with an article |
| **enterprise** (attributiv) | **eindeutschen**: der Rahmenvertrag · die Tarife für Unternehmen · die Funktionen für Unternehmenskunden | 3 | **BOUND** | — | „**Die Funktionen für Unternehmenskunden stehen erst im Rahmenvertrag.**“ | ⛔ *der Enterprise-Tarif* (insource 0) · ⛔ *die Enterprise-Angebote* | X-14. `Enterprise-` bleibt nur im **Plannamen** (das Enterprise-Abo, die Enterprise-Version) |
| **tier** (a) price | **der Tarif** · **der Batch-Tarif** (*batch tier*), Klammerpflicht | 2/3 | **THIN×2** (§8, D-3) | der / die Tarife / des Tarif[e]s | „**Batch ist der günstigste Tarif, den die Plattform Ihnen verkauft** – rund der halbe Preis gegen ungefähr 24 Stunden Vorlauf.“ | ⛔ *die Preisstufe* (95 hits, all fare zones) · ⛔ *der Batch-Betrieb* · ⛔ *die Batch-Stufe* · ⛔ *die Stapelverarbeitung* | X-12 + B |
| **tier** (b) offering | **das Angebot** | 3 | **BOUND** | das / die -e / des Angebot[e]s | „Viele Teams wachsen aus **dem verwalteten Angebot** heraus.“ | ⛔ bare *die Stufe* (55× *rung/stage*), *die Ebene* (35×) | X-17 |
| **tier** (d) app layer | **die Anwendungsschicht** — the **compound**, never bare `die Schicht` | 3 | **BOUND** | die / die -en / der -schicht | „**eine zustandslose Anwendungsschicht plus ein asynchroner Worker**“ | ⛔ bare *die Schicht* (96×, the curriculum metaphor) | B; also the Mermaid node `App layer` (§5) |
| **traffic** | **der Verkehr**; **der Produktivverkehr** | 3 | **CORPUS PRECEDENT** | der / — / des Verkehrs | „**Die Änderung wird automatisch auf den vollen Verkehr ausgeweitet.**“ · „ein Judge auf **einer Stichprobe des Verkehrs**“ | ⛔ *der Traffic* als Laufterm | X-7. `Traffic` survives **only** inside the Golden-Signals enumeration (class 1) |
| **residency** (Terminus) | **die Data Residency**, kept-EN, **Pflichtglosse bei Erstnennung** | 2 | **DECIDED — §8, D-1** | die Data Residency (fem.) | „**Data Residency ist die Zusage darüber, wo die Inferenz stattfindet.**“ | ⛔ *die Datenresidenz* · ⛔ *die Datenhoheit* (= sovereignty) · ⛔ *die Datenlokalisierung* | X-8 |
| **residency** (Fließtext) | **der Speicherort** | 3 | **DECIDED — §8, D-1** | der / die -e / des Speicherorts | „**Anforderungen an den Speicherort**“ · „**global heißt ausdrücklich: keine Zusicherung zum Speicherort**“ | as above | AGREED×2 core of C and G |
| **ceiling** | **die Kapazitätsgrenze**; anaphorisch **die Grenze**; erschöpftes Verfahren **ausgereizt** | 3 | **DECIDED — §8, D-2** | die / die -n / der -grenze | „**Nicht die reine Rechenleistung, sondern der KV-Cache setzt die eigentliche Grenze.**“ · „**Ein LLM-Dienst stößt schon bei einer überraschend niedrigen Anfragerate an seine Kapazitätsgrenze.**“ | ⛔⛔ **die Decke** · ⛔ `die Obergrenze` for `ceiling` — `cap` owns it | A + G converge (§1.6) |
| **floor** | **die Untergrenze**; Label **Score-Untergrenze** | 3 | **DECIDED — §8, D-2** | die / die -n / der -grenze | „**Setzen Sie eine Score-Untergrenze hinter die Stufe, deren Scores etwas bedeuten.**“ | ⛔ *der Boden* · ⛔ *der Mindestwert* | G, D-05 |
| **cap** | **die Obergrenze** | 3 | **CORPUS PRECEDENT(41)** | die / die -n / der Obergrenze | „**eine Obergrenze für die Nebenläufigkeit setzen**“ · „**je Mandant eine eigene Obergrenze**“ | ⛔ *das Cap* · ⛔ *deckeln* (canon `:1089`, by name) · ⛔ *kappen* | canon + B |
| **fallback** (chain / answer) | **kept-EN, artikellos, Kompositumsbildner**: die **Fallback-Kette**, die **Fallback-Antwort**; Plural **Fallbacks** | 2 | **OPEN (Genus) — §9. THE HOLE: no slice ruled this term** | **kein Artikel erfinden** | „**Der Produktivbetrieb hält eine Fallback-Kette bereit: Antwortet das erste Modell mit `429`, geht die Anfrage an das zweite.**“ · H3 „**Fallbacks und das Gateway**“ | ⛔ *der/das Fallback* mit erfundenem Artikel · ⛔ *der Rückfall*, *die Ausweichantwort* | `rag.md` §2 carries it as **settled kept-EN with no §1.1 row** — the `Admission Control` shape. 10 occ, **5 files, an H3, a Mermaid label and the `[New terms]` footer** |
| **fallback** (the way back after a tune) | **das Rollback** | 2 | **BOUND** | das / die -s / des Rollback[s] | „**LoRA macht den Rollback fast kostenlos: Adapter abhängen, und das Verhalten ist zurück.**“ | ⛔ using the routing-`Fallback` word here | Sense split found by this gate; E owns `rollback` |
| **red-teaming run** | **der Red-Teaming-Durchlauf** | 2/3 | **BOUND** | der / die -läufe / des -laufs | „**Setzen Sie Red-Teaming-Durchläufe vor der Freigabe an und verfolgen Sie die Erfolgsrate der Angriffe von Release zu Release.**“ | ⛔ *Red-Team-Läufe* · ⛔ *Red-Teaming-Läufe* · ⛔ *Red-Team-Durchläufe* | X-5 |
| **attack success rate** | **die Erfolgsrate der Angriffe** (ASR) | 3 | **CORPUS PRECEDENT(12)** | die / die -n / der Erfolgsrate | „**Messen Sie die Erfolgsrate der Angriffe.**“ | ⛔ *die Erfolgsquote der Angriffe* | §1.3 |
| **task success rate** | **die Erfolgsquote** | 3 | **CORPUS PRECEDENT(1, glossiert)** | die / die -n / der Erfolgsquote | „**Ein günstigeres Modell gewinnt nur, wenn seine Erfolgsquote den Preisabstand überbietet.**“ | ⛔ collapsing it into `Erfolgsrate` | §1.3 — two referents, two shipped words |
| **warm** (pools / headroom) | **umbauen** | 3 | **OPEN — incumbent held** (§9) | — | „**Rechnen Sie damit, dass der Cold-Start jede reaktive Hochskalierung zu spät kommen lässt; wer das nicht will, hält einen Vorrat bereits gestarteter Instanzen bereit.**“ | ⛔ *warm gehaltene Instanzen* · ⛔ *der Warm-Pool* · ⛔ „sich eine GPU warm halten“ | §1.3 |
| **version** | **die Version** | 3 | **BOUND** | die / die -en / der Version | „**eine exakte Prompt-Version**“ · „auf **die neue Version**“ | ⛔ *die Fassung* für eine nummerierte Version · ⛔ *die Versionierung* für *version control* | §1.4 |
| **edition / variant** | **die Fassung** | 3 | **CORPUS PRECEDENT(29)** | die / die -en / der Fassung | „**in der Fassung 2025-03-26 der Spezifikation**“ · „**die vom Anbieter betriebene Fassung**“ | ⛔ using it for a numbered software version | §1.4 |
| **tooling** (Produkte um das System) | **die Werkzeuge** (Plural) | 4 | **CORPUS PRECEDENT** | die Werkzeuge / Pl. / der Werkzeuge | „**Welche Werkzeuge Sie um das laufende System legen, entscheidet die nächste Lektion.**“ | ⛔ *das Tooling* als freies Substantiv | F, R-1. ⚠ **ADDENDUM A4 applies to the counter-evidence**: run 1's ban cited a real wave-2 count **of `tools`, not `tooling`**. **§1.1.g row** |
| **tools** (agent-callable) | **die Tools**; **der Tool-Katalog** | 2 | **CORPUS PRECEDENT** | — | „**Das Gateway macht aus einem MCP-Server ein aufrufbares Tool.**“ | ⛔ *die Werkzeuge* für diesen Referenten | Both referents share the Part III pages. `Tool-Katalog` (13, 7 files) is **correct and must not be touched** |
| **tooling ecosystem** | **das Tooling-Ökosystem** | 2 | **BOUND (cross-reference)** | das / die -e / des -Ökosystems | „**beim Tooling-Ökosystem in Teil III**“ | ⛔ *das Werkzeug-Ökosystem* · ⛔ *das Tool-Ökosystem* · ⛔ *der Werkzeugkatalog* für diesen Referenten | X-15 |
| **frontier model** | **das Spitzenmodell** | 3 | **CORPUS PRECEDENT(2) — overrides BOTH runs** | das / die -e / des -modells | „**Spitzenmodelle kommen auf unter 50 % Erfolg.**“ | ⛔ *das Frontier-Modell* · ⛔ *das Grenzmodell* | G, D-06. Neither run grepped the delivered locale for this row. **§1.1.g row** |
| **incident** | **der Vorfall** | 3 | **BOUND (Stufe 1 + Korpus)** | der / die Vorfälle / des Vorfalls | „**Ausfälle beim Anbieter und 429er sind keine Vorfälle, sondern Wetter.**“ | ⛔ *der Incident* mit deutschem Artikel · ⛔ *die Störung* · ⛔ *der Zwischenfall* | E, UNION. **§1.1.g row** |
| **provider / vendor** | **der Anbieter** | 3 | **CORPUS PRECEDENT(38 : 0)** | der / die Anbieter / **des Anbieters**, Dat. Pl. den Anbietern | „**die API des Anbieters**“ · *provider-agnostic* → „**anbieterunabhängig**“ | ⛔ *der Provider* (Duden + DWDS: der ISP) · ⛔ *der Betreiber* (KI-VO: das sind Sie) | C. **§1.1.g row** |
| **semantic cache** | **der semantische Cache** | 2/3 | **HOUSE** | der / die -s / des Caches | „**Ein semantischer Cache beantwortet eine schon gestellte Frage aus dem Speicher.**“ | ⛔ *der Semantik-Cache* | Label-and-prose term (4 occ, 2 files), **ruled by no slice**; head noun `der Cache` is a canon §1.1.a row |
| **result store** | **der Ergebnisspeicher** | 3 | **HOUSE — Mermaid only** | der / die -speicher / des -speichers | Mermaid: „**Ergebnisspeicher (Abruf / Webhook)**“ | ⛔ *der Result Store* | 1 occurrence, **a Mermaid label only** — ruled by no slice; built on F's `der Datenspeicher` |
| **failover** | **Failover**, artikellos, nur in der Aufzählung | 2 | **OPEN (Genus) — §9** | **kein Artikel erfinden** | Mermaid: „**Kostenrouting · Failover · Richtlinie zum Speicherort · Budgets**“ | ⛔ *der/das Failover* mit erfundenem Artikel | 3 occ, 1 file, one of them a Mermaid label; ruled by no slice |

---

## 3. Sense cards that cross a slice boundary

The per-slice sense cards in the seven ledgers stand. These four are the ones the merge had to rebuild
because their branches were owned by different slices.

### SC-M1 · `runtime` — Wirtsplattform, Produktbauteil, Zeitpunkt

**Frage vor dem Schreiben:** *Kann ich sie mieten, starten und beenden? Steht das Wort großgeschrieben neben
Memory, Gateway, Identity? Oder lässt sich „zur Ausführungszeit“ einsetzen, ohne dass der Satz kippt?*

- **L1 Wirtsplattform** → **die (verwaltete) Agenten-Laufzeitumgebung**, Anapher **die Umgebung**.
  > „**Eine verwaltete Agenten-Laufzeitumgebung führt die Agentenschleife für Sie aus** und legt Sitzungs- und
  > Gedächtnispersistenz, eine Tool-, Identitäts- und Gateway-Schicht, Observability und Scale-to-Zero darum.“
- **L2 benanntes Produktbauteil** → **Runtime** (Klasse 1); mit Artikel **die Runtime**.
  > „**Die Runtime gibt Ausführungsfenster von bis zu acht Stunden**, mit Sitzungsisolation in einer eigenen MicroVM.“
- **L3 Zeitpunkt** → **zur Laufzeit**.
  > „…und setzt **zur Laufzeit** pro Anfrage weiche und harte Obergrenzen durch.“

**Die Regel, die aus dem Minimalpaar folgt:** das Deutsche trennt hier über die **Wortbildung**, nicht über das
Wort — `-umgebung` oder kept-EN `Runtime` = das Ding, bloßes `Laufzeit` = die Zeit. Der Testfall ist Part III's
eigener Satz: „*Runtime gives execution windows up to eight hours*“. Mit bloßem `Laufzeit` stünde **dasselbe
Wort in beiden Bedeutungen in einem Satz**.

### SC-M2 · `residency` gegen `sovereignty` — Ort oder Macht

**Frage vor dem Schreiben:** *Geht es um einen ORT oder um MACHT? Und stehe ich an einer Terminusstelle
(Überschrift, Definition, Kontrast) oder im Fließtext?*

| Zweig | Deutsch | Gearbeiteter Satz |
|---|---|---|
| **Terminus** (H2, Definition, „AI residency is not data residency“) | **die Data Residency**, kept-EN, einmal glossiert | „**Data Residency ist die Zusage darüber, wo die Inferenz stattfindet.**“ · „**Wo das Modell rechnet, ist nicht dasselbe wie Data Residency**: auch mit GPUs in der Region können Prompts, Telemetrie und Ausgaben die Region verlassen.“ |
| **Ort, Fließtext** (~25 Vorkommen) | **der Speicherort** | „**Anforderungen an den Speicherort**“ · „**global heißt ausdrücklich: keine Zusicherung zum Speicherort**“ |
| **Macht / Jurisdiktion** | **die digitale Souveränität** | „**Die Frage nach dem Ort ist eine Frage der Geografie, die Souveränität eine Frage der Macht.**“ · „**Souverän ist nicht, wessen Daten in der EU liegen, sondern wer im Streitfall bestimmen kann, was mit ihnen geschieht.**“ |
| **der Regler dazwischen** | **der Regler zwischen Speicherort und Kapazität** | „**Daten aus Gründen der Data Residency in derselben Region zu halten, kann den Zugriff auf günstigere Kapazität in anderen Regionen kosten – das ist der Regler zwischen Speicherort und Kapazität.**“ |

⚠ **`die Datenhoheit` gehört ausschließlich in den Souveränitätszweig.** Im Ortszweig kollabiert sie genau die
Unterscheidung, um derentwillen der Abschnitt existiert. ⚠ Und **„in der Region“** ist die stehende deutsche
Wendung für *im Umland* — immer **„in derselben Region“** oder **„in der gewählten Cloud-Region“**.

### SC-M3 · Die Grenzwörter — neun deutsche Wörter, die alle „Grenze“ sagen

Slice G asked for this and it is the densest collision surface in the wave. **One page, so a later sweep
cannot „fix“ the asymmetry.**

| Englisch | Deutsch | Prüffrage | Gearbeiteter Satz |
|---|---|---|---|
| **cap** (jemand stellt sie ein) | **die Obergrenze** | Hat sie jemand konfiguriert? | „**Setzen Sie eine Obergrenze für die Nebenläufigkeit, je Mandant eine eigene.**“ |
| **ceiling** (man stößt dagegen) | **die Kapazitätsgrenze** | Entdecke ich sie, indem ich dagegenlaufe? | „**Ein LLM-Dienst stößt schon bei einer überraschend niedrigen Anfragerate an seine Kapazitätsgrenze.**“ |
| **floor** | **die Untergrenze** | Darf ein Wert sie nicht unterschreiten? | „**Setzen Sie eine Score-Untergrenze hinter die Stufe, deren Scores etwas bedeuten.**“ |
| **threshold** | **der Schwellenwert** | Löst das Überschreiten etwas aus? | „**Metriken unter dem Schwellenwert blockieren den Merge.**“ |
| **the limit, anaphorisch** | **die Grenze** | Ist die Sache im Satz schon benannt? | „**Nicht die reine Rechenleistung, sondern der KV-Cache setzt die eigentliche Grenze.**“ |
| **trust boundary** | **die Vertrauensgrenze** | Eine **Relation**, kein Ort | „**Innerhalb des Perimeters liegt trotzdem eine Vertrauensgrenze – abgerufene Inhalte sind auch dort nicht vertrauenswürdig.**“ |
| **security boundary** | **die Sicherheitsgrenze** | — | (Pilotzeile, unverändert) |
| **network boundary** | **die Netzgrenze** · Trennung → **die Netztrennung** | Topologie? | „**Der Verkehr zum Modell verlässt das öffentliche Internet nie.**“ |
| **service boundary** | **die Dienstgrenze** | — | „**innerhalb der Dienstgrenze verarbeitet**“ |
| **perimeter** | **der Perimeter** — ein **Ort** | „hinter dem Perimeter“ ✓ / „hinter der Vertrauensgrenze“ ✗ | „**Was Sie kaufen, ist das Modell hinter dem Perimeter Ihrer Cloud: IAM, Abrechnung, Netz, Audit.**“ |

⚠ **Die Asymmetrie muss einmal ausgesprochen stehen, sonst repariert sie jemand:** *`floor` darf das Antonym
von `Obergrenze` nehmen, weil es niemand sonst beansprucht; `ceiling` darf es nicht, weil `cap` es besitzt —
41 Belege in derselben Teillieferung.* ⛔ `der Perimeterschutz` (BSI: Zäune, Beleuchtung, Haustechnik).

### SC-M4 · Die Kontrollmetaphern — vier englische Wörter, vier deutsche, alle vier ausgeliefert

**Frage vor dem Schreiben:** *Ein benannter Mechanismus, eine Einstellung mit Namen und Wert, eine stufenlose
Größe — oder eine Raste in einer Reihe?*

- **lever → der Hebel.** „**Streaming ist der wirksamste Hebel für die gefühlte Latenz, den Sie haben.**“
  · „**zu einem der Hebel greifen**“. ⛔ „alle Hebel in Bewegung setzen“, ⛔ „am längeren Hebel sitzen“, ⛔ `der Kostenhebel`.
- **knob → die Stellschraube.** „**Drei Stellschrauben steuern diesen Pool**: `max_num_seqs` begrenzt …“
  · „**Die Stellschrauben dafür sitzen beim Anbieter.**“
- **dial → der Regler.** „**α ist der Regler zwischen Bedeutung und exakter Übereinstimmung.**“
  · „**der Regler zwischen Speicherort und Kapazität**“. Beide Verben sind ausgeliefert: **drehen an** (3×) und **einstellen** (1×).
- **notch → die Stufe.** ⚠ Auf einer Seite, die auch Anbietertarife aufzählt, tut `Stufe` zwei Dienste —
  dort die Tarifnamen als Klasse 1 setzen („die Stufen `Reserved`, `Priority`, `Standard`, `Flex`“) und
  `Stufe` sonst meiden.

---

## 4. Cross-page bindings — ONE string per term, decided HERE

Every term below spans ≥3 files. **Wave 2's `reason → decide → act → observe` had no row and three renderers
diverged.** These are the rows that prevent that.

| Terminus | Files | **THE BINDING STRING** |
|---|---:|---|
| `snapshot` (restorable) | 9 | **der Snapshot** · des Snapshots · die Snapshots — „**den vorherigen Snapshot wiederherstellen**“ |
| `snapshot` (dated picture, **19 of 29**) | 9 | **die Momentaufnahme** — „**Alles Folgende ist eine Momentaufnahme von Mitte 2026.**“ |
| `deploy` (Ereignis) | 9 | **das Deployment** — „**Jede Änderung an einem der fünf Artefakte ist ein Deployment.**“ |
| `deploy` (Vorgang) | 9 | **die Bereitstellung** — „**Wo der Server läuft, bleibt eine Frage der Bereitstellung.**“ |
| `change` | 8 | **die Änderung** — „**Jede Änderung an Prompt, Modell, Index oder Config läuft gegen den Goldstandard.**“ |
| `cost` | 10 | **die Kosten** (Pluraletantum) — ⛔ Zahl unmittelbar davor |
| `spend` | 7 | **die Kosten** als Laufterm; `die Ausgaben` **nur im expliziten Geldrahmen**; Verb **ausgeben**. H2 „**Die Kosten steuern**“ |
| `budget` | 8 | Kompositum bei Erstnennung einer Dimension (`das Token-Budget`, `das Schrittbudget`), danach **das Budget** anaphorisch |
| `price` | 7 | **der Preis** · **der Tokenpreis** |
| `bill` | 7 | **die Rechnung — nie frei stehend**: „die Rechnung **für** die Tokens“, „die **Monats**rechnung“ |
| `lever` | 6 | **der Hebel** (SC-M4) |
| `tier` | 7 | per Sinn (§2) — **nie appellativ `Tier`** |
| `job` | 7 | **der Job**, bei Erstnennung gebunden — „**ein Job – eine Arbeitseinheit, die die Queue trägt**“ |
| `rate limit` | 6 | **das Rate Limit**, **spaced**, Neutrum, Pl. `die Rate Limits`, Vorgang `das Rate Limiting` |
| `queue` | 5 | **die Queue** (X-4) |
| `fallback` | 5 | **Fallbacks**, artikellos; **die Fallback-Kette**; H3 „**Fallbacks und das Gateway**“ |
| `self-host*` | 5 | Substantiv **der Eigenbetrieb** (gebunden, nie nackt) · Verb **selbst betreiben** · „**API oder Eigenbetrieb**“ |
| `golden set` | 4 | **der Goldstandard** — „**Jede Änderung läuft gegen den Goldstandard.**“ |
| `batch tier` | 4 | **der Batch-Tarif** (*batch tier*) — THIN×2 |
| `app layer` | 4 | **die Anwendungsschicht** |
| `inference server` | 4 | **die Inferenz-Engine** *(inference server)* |
| `drift` | 4 | **der Drift**, alle Komposita **maskulin**: der Eingabedrift · der Korpusdrift · der Modelldrift |
| `AI delta` | 3 (H2 auf zwei) | **die Konstruktion, nicht das Wort**: „**Docker – wo der Unterschied wirklich liegt**“ · „**Was sich mit der KI ändert: Artefakt und Test**“ · „**Der Unterschied zur gewöhnlichen Anwendung: was sich ändert, sobald ein Sprachmodell im Spiel ist.**“ |
| `release gate` | 3 | **„die Freigabe vor dem Release“** — eine Zeichenkette |
| `gate` (gezählt) | 5 | **die Prüfung / die Prüfungen** — „**Nicht jede Prüfung kostet gleich viel.**“ |
| `managed` | 5 | **verwaltet** (X-13) |
| `platform` | **10 / 10** | **die Plattform**; Erstnennung gebunden **die KI-Plattform / die Cloud-Plattform** |
| `provider` | 6 | **der Anbieter** |
| `perimeter` | 4 | **der Perimeter**, gebunden — THIN×2 |
| `residency` | 3 | **die Data Residency** / **der Speicherort** (SC-M2) |
| `guardrail` | **10 / 10** | **die Guardrails** (Plural); zählbarer Singular **die Schutzregel**; Kompositum-Erstglied **`Guardrails-`** |
| `observability` | 9 | **die Observability** |
| `eval` | 7 | Vorgang **die Evaluierung** · zählbarer Fall **der Fall / der Testfall** |
| `trace` / `span` | 6 / 3 | **der Trace** / **der Span**, Pl. **die Spans** (⛔ *die Späne*) |
| `release` | 6 | **das Release** (Genus = Hausentscheidung, §8 D-4) |
| `version` | 6 | **die Version** |
| `pin` | 4 | **die Modellversion festlegen**; Substantiv **das Model-Pinning** |
| `CI` | 4 | **die CI** — Blockstring „**in der CI**“ |
| `wire` | 5 | vier Zweige, Card W in LEDGER-G — ⛔ das ganze `Leitung`-Wortfeld im Lokativ |
| `governance` | 5 | **die Governance**, nur Singular — „**die Governance der Ausgaben**“ (Genitiv, kein Kompositum) |
| `engine` | 5 | **die Engine** (feminin) |
| `scale-to-zero` | 4 | **Scale-to-Zero** (Klasse 2, artikellos); verbal „**skaliert im Leerlauf auf null**“ |
| `semantic conventions` | — | Laufform **die GenAI-Konventionen von OpenTelemetry**; Zitierform **einmal** „die GenAI Semantic Conventions von OpenTelemetry“; Versionszitat `Semantic Conventions v1.41.x` |

---

## 5. Mermaid labels — a gated surface from now on (ADDENDUM A7)

**134 labels across 8 files**, validated against the independent measurement. Mermaid is the one text unit a
prose gate does not read as prose — it sits inside a fence, so the census, the register pass and the cold read
all skip it, **while the reader sees it rendered**. Both wave-2 `golden set` regressions and both of slice F's
riskiest occurrences are in labels.

**Per term, whether the binding table covers it:**

| Label string (EN) | Where | Bound German | Covered by |
|---|---|---|---|
| `Golden set` | te/i, te/d | **Goldstandard** | §4 — ⚠ **the wave-2 regression site**; grep the rendered German for `Golden`/`golden` inside mermaid fences and treat a hit as a hard failure |
| `Eval gate<br/>(golden set)` | ll/d | **Evaluierung<br/>(Goldstandard)** — the **diamond is the gate** | §2, F R-12 |
| `Eval in CI` | ll/i, te/i, te/d | **Evaluierung in der CI** | §4 |
| `gates the deploy` (edge, **must be identical in two diagrams**) | te/i L134, te/d L127 | **gibt das Deployment frei** | X-18 (⛔ „gibt die Auslieferung frei“) |
| `red-teaming (ASR)` (edge, identical ×2) | te/i, te/d | **Red-Teaming (ASR)** | §2 |
| `Semaphore — concurrency cap N` | s/d | **Semaphor – Obergrenze für die Nebenläufigkeit: N** | X-2 |
| `Bounded queue<br/>max depth D` | s/d | **Begrenzte Queue<br/>max. Länge D** | X-4 |
| `Shed — fast-fail 429 / 503 + Retry-After` | s/d | **Abweisen – sofort `429` / `503` + `Retry-After`** | B |
| `Job queue<br/>(backpressure: bound in-flight)` | ll/d | **Job-Queue<br/>(Backpressure: laufende Arbeit begrenzen)** | B |
| `Producer<br/>enqueue → job id` | ll/d | **Producer<br/>in die Queue stellen → Job-ID** | B (⚠ B flagged the alternative; **as prose it is `stellen`**) |
| `Dead-letter queue<br/>(alert on growth)` | ll/d | **Dead-Letter-Queue<br/>(Alarm bei Wachstum)** | B |
| `App layer` (node **and** subgraph, 2 files) | s/d, cp/d | **Anwendungsschicht** | §2, §4 |
| `Inference server` (subgraph; must match the prose on 3 pages) | s/d, s/i, cp/i | **Inferenz-Engine** | X-1 |
| `Result store<br/>(poll / webhook)` | ll/d | **Ergebnisspeicher<br/>(Abruf / Webhook)** | §2 — **label-only term, ruled by no slice** |
| `Semantic cache` | ll/i | **Semantischer Cache** | §2 — **ruled by no slice** |
| `LLM gateway: routing, fallbacks, budgets` | ll/i | **LLM-Gateway: Routing, Fallbacks, Budgets** | §2 `fallback` — **the hole** |
| `LLM gateway / router<br/>cost routing · failover · residency policy · budgets` | cp/d | **LLM-Gateway / Router<br/>Kostenrouting · Failover · Richtlinie zum Speicherort · Budgets** | §2 `failover`, SC-M2 |
| `Prompt assembly: token diet` | ll/i | **Prompt-Aufbau: Token sparen** | D (`token diet` OPEN, verbal) |
| `Provider: prompt cache, batch tier` | ll/i | **Anbieter: Prompt-Cache, Batch-Tarif** | §2 |
| `Auto-promote → 100%` | ll/d | **Automatisch auf 100 % ausweiten** (schmales geschütztes Leerzeichen vor %) | E |
| `Auto-rollback:<br/>repin prompt / model / index / adapter` | ll/d | **Automatischer Rollback:<br/>Prompt / Modell / Index / Adapter wieder festlegen** | E |
| `Regresses? Repin previous /<br/>detach LoRA adapter` | ll/d | **Verschlechterung? Vorgänger wieder festlegen /<br/>LoRA-Adapter abhängen** | E |
| `Canary<br/>(slice of live traffic)` | ll/d | **Canary Release<br/>(ein Teil des laufenden Verkehrs)** | X-7 |
| `Change` / `Change<br/>prompt / model / index / config` | ll/i, ll/d | **Änderung** | §4 |
| `Blocked — fix, retry` | ll/d | **Blockiert – beheben, wiederholen** | B (`retry` → wiederholen) |
| `Worker pool<br/>(ack after work, shared rate budget)` | ll/d | **Worker-Pool<br/>(bestätigt erst nach der Ausführung, gemeinsames Ratenbudget)** | A, B |
| `Shed load: 429 / slow producers / scale` | ll/d | **Last abweisen: `429` / Producer drosseln / Worker-Pool vergrößern** | B |
| `Tensor parallelism — within one node` / `Pipeline parallelism — across nodes` | s/d | **Tensor-Parallelität – innerhalb eines Knotens** / **Pipeline-Parallelität – über Knoten hinweg** | A (uniform hyphen, HOUSE) |
| `GPU — KV-cache pool` | s/d | **GPU – KV-Cache-Pool** | A |
| `Admission — max_num_seqs cap` | s/d | **Annahme – Obergrenze `max_num_seqs`** | A, B |
| `Guardrails<br/>wrap the prod system` | te/d | **Guardrails<br/>legen sich um das Produktivsystem** | F |
| `Production system` (identical ×2) | te/i, te/d | **Produktivsystem** | F |
| `Langfuse Worker` / `Langfuse Web` | te/d | unverändert, **Klasse 1** — die Auszeichnung trägt die Unterscheidung gegen das Appellativ `ein Worker` | A |
| `Self-host<br/>from the serving lesson` | cp/d | **Eigenbetrieb<br/>aus der Serving-Lektion** | C, G |
| `The cloud's managed AI platform` | cp/i | **Die verwaltete KI-Plattform der Cloud** | X-13 |
| `The model inside the cloud perimeter:<br/>IAM, billing, network, audit` | cp/i | **Das Modell hinter dem Perimeter der Cloud:<br/>IAM, Abrechnung, Netz, Audit** | SC-M3 |
| `Your own GPUs + inference server` | cp/i | **Eigene GPUs + Inferenz-Engine** | X-1 |
| `Bills even while idle —<br/>hosting dwarfs tokens at low volume` | cp/d | **Kostet auch im Leerlauf –<br/>bei geringem Volumen überwiegt der Betrieb die Tokens** | G (`idle`) |
| `Cheap at low volume —<br/>you pay only for tokens used` | cp/d | **Günstig bei geringem Volumen –<br/>Sie zahlen nur für verbrauchte Tokens** | D (`cheap` = Modell-/Tarifpreis → **günstig**) |
| `The 200 left with the first bytes — a mid-stream error must travel in-band` (Note) | s/i | **Der Statuscode 200 ist längst übertragen – ein Fehler mitten im Strom muss im selben Kanal reisen** | G, Card W (c) |
| Sequence participants `User` · `App service (FastAPI)` · `Retrieval` · `LLM (provider or inference server)` | s/i | **Nutzer** · **App-Dienst (FastAPI)** · **Retrieval** · **LLM (Anbieter oder Inferenz-Engine)** | X-1 |

**What is NOT this gate's job:** the census and the Sol pass over the labels belong to the render. The
**label-width budget** does too — several bound strings above are longer than their English originals
(„eingefrorener Regressionsdatensatz“, „Automatisch auf 100 % ausweiten“), and 360 px is the phone width.

---

## 6. Terms that must NOT regress — flat checklist for renderers

Copy this into the render prompt. Each has regressed at least once in this project.

`Goldstandard` (⛔ *Golden Set*) · `das Fehlerbudget` · `der Dienst` (⛔ *der Service*) · `der Endpunkt`
(⛔ *Endpoint*) · `die Instrumentierung` · `der Durchsatz` · `das Arbeitsgedächtnis` · `der Bewerter`
(⛔ *Evaluator*) · `Überblick` (⛔ *Teilübersicht*) · `das Fehlerbild des Retrievals / der Generation` ·
**`die Generation`** (⛔ *Generierung* — und der Plural `Generationen` ist **0**; für *concurrent generations*
das Bezugsobjekt zählen) · `der Tool-Call` (⛔ *Werkzeugaufruf*) · `die Obergrenze` (⛔ *das Cap*, ⛔ *deckeln*) ·
`der Schwellenwert` (⛔ *die Schwelle*) · `das Verfahren` (⛔ *die Technik*) · `die Domäne` ·
`der Durchlauf` (⛔ *ein Lauf*) · `das Betriebshandbuch` · `die Fähigkeit` (⛔ *die Capability*) ·
`die Vertrauensgrenze` (⛔ *Trust Boundary*) · `die Kosinus-Ähnlichkeit` · `mehrsprachig` ·
`die Schwärzung` · `das Transportprotokoll` · `die Protokollierung` (⛔ *Prüfpfad*).

**Added by this merge:** `die Queue` (⛔ *die Warteschlange* in Part III) · `der Event-Loop` (⛔ *die*
Event-Loop, ⛔ *Ereignisschleife*) · `der Semaphor` (⛔ *eine Semaphore*) · `die Inferenz-Engine`
(⛔ *Inferenzserver*) · `verwaltet` (⛔ kept-EN `Managed-` vor deutschem Grundwort) · `der Verkehr`
(⛔ *der Traffic*) · `der Merge` (⛔ *die Zusammenführung* — occupied by retrieval fusion) ·
`die Erfolgsrate der Angriffe` · `das Tooling-Ökosystem` · `der Red-Teaming-Durchlauf` ·
`der Speicherort` / `die Data Residency` (⛔ *Datenresidenz*) · `die Kapazitätsgrenze` (⛔ *die Decke*).

**Two carve-outs a checker will read as regressions and must NOT „fix“:**
1. the class-3 parenthetical „der **Goldstandard** (*golden set*) – der handgeprüfte Referenzdatensatz“ — the
   lowercase italic English is **prescribed**;
2. the `**[Neue Begriffe]**` footer of both `tooling-ecosystem` pages stays **English and lowercase** until the
   glossary wave. `instrumentation` there is **not** a regression of the German-led `die Instrumentierung`.

---

## 7. `AGREED ×2` is not „checked" — and here are the rows it flatters

**Say this in the render prompt.** Both runs of a slice tend to read the **same** sources, so a
regulator-versus-trade-press divergence comes back looking like agreement. **A row that rests entirely on BSI
is worth LESS with `AGREED ×2`, not more** — the counter-check is a heise/iX/c't full-text count, not a second
BSI read. The proof that this is not theoretical: **both blind runs of slice A independently wrote a banned
string into their own sheets.**

**The rows carrying the most confident label on the thinnest evidence, ranked:**

| Row | Why the label flatters it | Counter-check owed |
|---|---|---|
| **`der Batch-Tarif`** | The two runs **coined different words** — so the row does not even have the false comfort of agreement. The positive side rests on **one Duden page**; three independent measurements found zero | any T1–T3 German source inflecting a noun for a cloud **pricing** tier |
| **`der Perimeter`** | `AGREED ×2` on **one BSI PDF** for genus, register *and* referent — and the two runs, reading the same file, report **28** vs **34** occurrences. The doubling did not even reproduce the measurement | a heise/iX/c't full-text count of `Perimeter` **with a German article** — *not* a second BSI read |
| **`die GPU`** | Highest-frequency row of slice A (**80 occurrences, 5 files**), **all** evidence on both sheets is de.wikipedia, **0** in the shipped German. Run 2 names the trap itself | one heise/iX sentence with a case-marked `die GPU` |
| **`der Stack`** | `AGREED ×2` on **one tier-3 source per run and no dictionary lemma**. Duden 404, DWDS 404, 0 shipped — and the reader's only prior in this book is `Stacktrace` | one sentence at heise / iX / INNOQ / dpunkt |
| **`dediziert`** | `AGREED ×2` resting on **one de.wikipedia sentence read twice**. Duden 404; DWDS carries only the elevated verb *dedizieren* | as above |
| **`das Batching`** | `AGREED ×2` — but both runs applied **the same canon `-ing` rule**. That is one derivation counted twice, not two data points. Label **HOUSE** | — |
| **`der Threadpool`** | `AGREED ×2` on the **same informatik-aktuell pattern** — one strand, twice | — |
| **`die Jurisdiktion` / `die Gerichtsbarkeit`** | run 1 only, resting **entirely on BSI C5** | heise/iX full-text |
| **`die Compliance`** | `AGREED ×2` across **the same two dictionaries**; BSI **never bares it** (0 bare, `Compliance Management` 19); Duden lists the **medical** senses first | heise/iX full-text |
| **`das Fehlerbudget`** | Both runs cite **the same canon reference** for the attestation. The *corpus* (4×) is the stronger evidence here, not the source situation | — |
| **`der Exporter`** | THIN×2 + HOUSE: no Duden/DWDS/de.wikipedia lemma; DWDS redirects to **`Exporteur`** (a goods exporter — a named false friend) | — |

**And two rows where a slice named its own blind spot — carry them forward as explicitly weaker, do not let
`AGREED ×2` flatten them:** `der Batch-Tarif` (run 2 pre-registered the failure mode in its own sheet) and
`der Anbieter` — except that **`Anbieter` was rescued**: it is **CORPUS PRECEDENT(38 : 0)**, 22
article-bearing, 10 genitives, 3 dative plurals, 8 pages. It was never a gap; it was an unrecorded ruling.

---

## 8. The rows this gate had to DECIDE, not derive

Attestation will not close these. Each records the recommendation **and the cost of being wrong**.

### D-1 · `residency` — 30 occurrences, 3 files, the head term of the load-bearing section

**Decided: split by POSITION.** **`die Data Residency`** (feminine, kept-EN, **obligatory gloss at first
mention**) for the ~5 **term-level** positions — the H2, the contrast „AI residency is not the same as data
residency“, „a residency guarantee“, „residency policy“. **`der Speicherort`** for the ~25 running-prose
occurrences. ⛔ `die Datenresidenz` (one de.wikipedia article, a heise **blog**). ⛔ `die Lokalisierung der
Daten` (0 in the corpus; in a handbook with a **localisation pipeline** it reads first as l10n; and BSI's
`Lokalisierung` names the **customer's option**, not the **provider's assurance** — a change of referent).

*Reasoning.* Slice C recommended pure construction; slice G recommended the split. **G's is better on one
decisive point C did not have:** a common noun cannot carry „AI residency is not the same as data residency“ —
germanising it produces a true sentence that loses that these are two **named product properties**. And run 2
of slice G has **two independent case-marked German tokens** for the loan (heise dative, storage-insider
genitive, both feminine) where nobody has one for a German term-level form. C's strongest argument survives
inside the ruling: `die Souveränität` is a strong, 130-fold-attested word, and a **weak fresh coinage beside it
loses inside the sentence** — so the running prose keeps a plain, transparent noun (`der Speicherort`) rather
than a coined one.

**Cost of being wrong.** *If kept-EN is wrong:* an English term in an H2 of a **sovereignty** chapter about
European control — a tonal own-goal a reviewer will notice. Mitigated by design: the loan appears ~5 times,
not 30. *If German-led is wrong:* the residency-versus-sovereignty distinction — the section's thesis —
degrades, and the `Datenhoheit` trap opens. **That is worse, and it is invisible until a reader misreads it.**
I chose the retractable loss. **Closing condition for an upgrade:** one inflected sentence at
heise/iX/c't/INNOQ/dpunkt or in a BSI/DIN document in which a German term-level noun **governs a data holding
in the genitive**.

### D-2 · `ceiling` / `floor` — does `Obergrenze` stretch?

**Decided: rule the pair ASYMMETRICALLY.** `ceiling` → **`die Kapazitätsgrenze`** (+ `die Grenze`
anaphorically, `ausgereizt` for an exhausted technique); `floor` → **`die Untergrenze`** (both senses);
`cap` keeps **`die Obergrenze`**; `threshold` keeps **`der Schwellenwert`**.

*Reasoning.* Slice G checked slice-G-run-1's decisive premise — that the corpus itself draws the distinction —
and it **does not hold**: at least two of the 41 shipped `Obergrenze` are limits nobody configured. So this is
a register decision, not a lookup. **What tips it is a convergence neither slice could see:** slice A,
studying a different field, independently writes „jenseits der **Kapazitätsgrenze**“ for the same phenomenon,
and independently rules ⛔ `die Decke` with the same replacement („setzt die eigentliche Grenze“). Two slices,
no contact, same word.

**Cost of being wrong — asymmetric, which is the argument.** If `Kapazitätsgrenze` is wrong the cost is
**stylistic**: a five-syllable compound, 6 occurrences, 2 files; nothing is misread. If `Obergrenze` were used
for `ceiling`, the cost is **factual**: the KV-cache paragraph is the take-away of the serving deep-dive and
sits in the same Part as the LLMOps budgets, so a reader meeting `Obergrenze` in both places reads a
**physical constraint as something someone configured**. That is the class the canon calls „sachlich falsch,
keine stilistische Frage“.

### D-3 · `tier` (a), the price track — ~16 occurrences, 4 files, a heading

**Decided: `der Tarif` / `der Batch-Tarif` (*batch tier*), English parenthesis obligatory at first mention.**
⛔ `der Batch-Betrieb` / `die Betriebsart` (they name a **mode of operation**, not a **price** — the same
defect for which run 1 rejected `Stapelverarbeitung`; and `Betrieb` is occupied 12× as *Produktivbetrieb*).
⛔ `die Preisstufe` (95 hits, all Verkehrsverbund fare zones). ⛔ `die Stapelverarbeitung`.

**Cost of being wrong — moderate, and a reversal is expected, not a failure.** ~16 occurrences, 4 files, plus a
heading; a reversal is a mechanical replace. But a wrong choice makes the corpus's own warning — „**this batch
is a pricing tier, not Continuous Batching**“ — unintelligible in German. This is the wave's **THIN×2** row and
it is labelled so throughout. **Closing condition:** any T1–T3 German source that inflects a noun for a cloud
**pricing** tier. A renderer who finds one should **report** it, not adopt it silently.

### D-4 · `das Release` — genus, 42 occurrences, 6 files

**Decided: Neutrum.** DWDS licenses **both**; the shipped corpus is silent (all 3 occurrences article-less).
This is a **choice** and it must be made once. Neutrum: DWDS lists it first, and every neighbour is neuter
(`das Deployment`, `das Canary Release`, `das Rollback`). **Cost of being wrong:** none semantically; a
mid-course flip would be visible on six pages.

### D-5 · `AI delta` — the brief instructs one thing, both sheets and the canon rule the other

**Decided: bind the CONSTRUCTION, keep the term OPEN.** `rag.md` §3 says **BLEIBT OPEN** and gives the pilot's
corpus form as plain prose; both runs ⛔ `das KI-Delta` on zero attestation; and Duden marks the obvious
fallback („einen Unterschied machen“) as an **explicit calque**, so that escape is closed too. The three
binding strings are in §4.

**Cost of being wrong in my direction:** two H2 headings and one definition line read as ordinary German prose
instead of naming a coined figure — the reader loses a label but loses no meaning. **The other way:** a coined
term on zero attestation, **on a heading, on two pages** — the `Latenzbudget` failure mode a third time, and
headings are the least reversible place to put a coinage. ⚠ If the orchestrator overrules, **the exact string
is `das KI-Delta`** (Durchkopplung per § 45 E1) — recorded so the instruction executes without a round trip.

### D-6 · `fallback` — the term no slice was assigned

**Decided: kept-EN, article-free, compound-former only** — `die Fallback-Kette`, `die Fallback-Antwort`,
plural `Fallbacks`. Gender stays **OPEN** (§9). This is the `Backpressure` / `FinOps` / `Chargeback` class.

*Why it needed deciding here.* `rag.md` §2 already carries `Fallback` in the **settled kept-EN** list — with
**no `_language.md` §1.1 row**, i.e. no gender, no plural, no genitive. That is exactly the `Admission Control`
shape slice B found. It has **10 occurrences in 5 files, an H3 heading, a Mermaid label and a `[New terms]`
footer** — the highest-exposure term in the wave with no owner. **Cost of being wrong:** an invented
`das Fallback` is unrecoverable once printed; article-free prose is merely stiffer. And a **sense split** falls
out of it: „LoRA makes the fallback almost free“ is the **rollback path**, not the routing chain.

### D-7 · `managed` — `verwaltet` or kept-EN

**Decided: `verwaltet`** for the appellative (X-13). **Cost of being wrong: high in reach, low in damage** —
47 occurrences across 5 files, but both forms are decodable and a reversal is mechanical. The asymmetry that
decides it: `verwaltet` is **measured** in the delivered locale nine times in exactly the needed construction,
while the ⛔ against it is an **assertion**. Reversing a shipped construction on an assertion is the more
expensive error.

---

## 9. OPEN rows and their closing conditions

**OPEN means: the incumbent is held, a construction ships, and the row is not a placeholder.** Each of these
ships a worked sentence, which is the difference between an open row that renders and one that gets dodged.

| Row | Incumbent held | Closes when |
|---|---|---|
| `gate` (+ `release gate`) | no bare `Gate`; the construction set (§4); `das Quality Gate` only as the fixed term | a native DE sentence from heise/iX/INNOQ/dpunkt/BSI carries a **case-marked bare singular** `Gate` without *Quality/Stage/Release* in front. ⚠ `gateway` occurs **31×** in the same file set and is the delivered incumbent |
| `AI delta` | the construction (§4) | a German trade sentence inflects `Delta` for a **qualitative** difference („des KI-Deltas“) |
| `Latenzbudget` | `die Obergrenze` / „Ziele für p50 und p95“ | a T1–T5 German source writes `Latenzbudget` in the SRE sense. ⚠ **The pattern licenses the FORM, not the WORD** — five compound siblings ship; this is the one the corpus does **not** write |
| `fallback` (Genus) | artikellos, Kompositumsbildner | one case-marked German token with an article |
| `failover` (Genus) | artikellos, in der Aufzählung | same |
| `Chargeback` / `Showback` (Genus) | artikellos; „beim Chargeback“; `das Chargeback-Verfahren` | one nom./akk. case-marked German token |
| `inference server` | `die Inferenz-Engine` | a house **outside Heise Medien** prints it, or prints a case-marked `Inferenzserver` |
| `event loop` (Genus) | `der Event-Loop` | a second house outside informatik-aktuell writes a case-marked `den/des Event-Loops` — or INNOQ's feminine is confirmed in a second house |
| `autoscaling` | `das Autoscaling` / `der Autoscaler` | a second house prints a case-marked form. ⚠ **ADDENDUM A3: this row is NOT open because a fetch failed.** Run 2 graded it OPEN because de.wikipedia rate-limited it; run 1 had found a dedicated article with a marked genitive and a dative plural. **That is *unmeasured*, not *unattested*** — regraded here to *one house, real evidence* |
| `prefill` / `decode` | Kompositumsbildner, kein freier Artikel | a German house prints „des Prefills“ / „beim Prefill“ with an article |
| `backpressure` (Genus) | artikellos | a heise/iX/dpunkt/Rheinwerk sentence writes *der/das Backpressure* with an article |
| `load shedding` (noun) | describe the action: „Anfragen gezielt abweisen“ | German trade press names the action at all. ⛔ `der Lastabwurf` (69 : 0 — power grid **and aviation**) |
| `admission control` | describe the mechanism | a T1–T3 German source names it. → CANON DELTA (move `rag.md` §2 → §3) |
| `tail latency` | rebuild: „die Latenz der langsamsten Anfragen“ / „der p99-Wert“ | a T1–T3 German source names the concept. ⛔ `die Ausreißer` (a **factual** falsification) |
| `unit economics` | „die Stückkosten des Features – die Kosten pro Anfrage, pro aktiven Nutzer“ | a T1–T5 source writes an article-bearing `die Unit Economics` or an established German full form |
| `token diet` | verbal: H3 „Token sparen“ | a T1–T5 source carries an established German noun |
| `serverless` | kept-EN, gebunden (`Serverless GPU`) | a heise/iX sentence has `serverlos` + an unambiguous FaaS head noun. ⚠ de.wikipedia's `serverlos` is **17 of 18 peer-to-peer** |
| `cross-region` | the rebuild „zwischen Regionen“ | a heise/iX/c't sentence has `regionsübergreifend` **on an IT noun** |
| `in-flight` + *drain* | `laufend`; the drain sentence takes the explicit rebuild | a German Kubernetes / graceful-shutdown text renders *drain*. ⚠ `laufend` would be a **third** sense on a word the corpus already runs twice |
| `guardrail` (zählbarer Singular) | `die Schutzregel` / pluralise | a German sentence writes „das/der Guardrail“ at heise/iX/INNOQ/dpunkt |
| `safety classifier` | `der Klassifikator für Sicherheitsrisiken`, kurz `der Klassifikator` | a non-MT German source names the component |
| `data store` | `der Datenspeicher`, Aufzählung in Reichweite | a German sentence calls running services (Postgres/ClickHouse/S3) `Datenspeicher` |
| `Air Gap` (Genus) | `physisch getrennt`; `die Air-Gap-Umgebung` im Kompositum | one case-decisive token |
| `wrapper` (evaluative) | `der Wrapper` + one descriptive clause at first use | a German source carries the evaluative sense |
| `open-weight` | die Umschreibung „ein Modell mit offenen Gewichten“ | a heise/iX/Fraunhofer sentence carries `Open-Weight-Modell` as a standing terminus |
| `managed RAG` (Artikel) | artikellos in Subjektstellung, sonst gebunden | a German technical sentence attaches an article to `RAG` or `Managed RAG` |
| `vendor lock-in` (Artikel) | artikellos | a case-marked „der/das Vendor-Lock-in“ at heise/iX/INNOQ/dpunkt |
| `Souveränität` (Groß-/Kleinschreibung des Adjektivs) | `souverän`, klein und flektiert | — (pick **one register per page**; BSI never writes `souveräne Cloud`) |
| `-bound` family (I/O-, memory-bandwidth-) | clauses; *compute-bound* → **rechenintensiv** (54 measured) | an inflected sentence with a German adjective for *I/O-bound* or *memory-bandwidth-bound* |
| the three sharding compounds | hyphenate all three, uniformly | the wave rules on German-first-element compounds |
| `portable` (Adjektiv) | die Substantiv-/Verbalkonstruktion | — (⛔ „portabel bleiben“ asserts the system is carryable) |

**Count: 30 OPEN rows**, every one with a stated closing condition and a shipped construction.

---

## 10. Arithmetic — computed ONCE, here, from the union

> **A number in canon prose is a shared mutable variable.** Wave 1 had three slices independently report
> „§1.1.g grows to fifteen“ and a fourth add a row — each right, all four together wrong.
> **No renderer and no slice may restate any number in this section.**

### 10.1 `_language.md` §1.1.g — the number that sits in the Injektionsblock

**Current: 22.** Wave 3 adds **6**, all of them rows where a fluent model reaches for the loan and is wrong,
each one attested and each one **reversing at least one blind run**:

| New §1.1.g row | Evidence | Reversed |
|---|---|---|
| `provider` / `vendor` → **der Anbieter** | CORPUS(38 : 0), 22 article-bearing, 10 genitives, 3 dative plurals, 8 pages | the slice's own declared „THIN×2“ self-assessment |
| `tooling` → **die Werkzeuge** | CORPUS(6 in exactly this referent, of 11) | slice F run 1 outright |
| `managed` → **verwaltet** | CORPUS(9 : 0), inflected, attributive | slice F run 1 **and** slice C |
| `frontier` → **das Spitzenmodell** | CORPUS(2) in the exact sense | **both** runs of slice G, in opposite directions |
| `traffic` → **der Verkehr** | corpus: `Traffic` **1**, and it is inside a class-1 citation | slice E, against itself |
| `incident` → **der Vorfall** | BSI DER.2.1 **117 : 13 : 10** + Duden paradigm + CORPUS(2) | — (UNION of both runs) |

> ### ⇒ **`_language.md` §1.1.g: 22 → 28.**
> This number must be written in **three** places and nowhere else: `_language.md`:53 (the Injektionsblock,
> „**Achtundzwanzig** Termini führt das Deutsche belegt selbst“), `_language.md`:1339
> („bei **achtundzwanzig** Termini falsch“), and a new „Zuwachs Welle 3“ note at `_language.md`:~1350.

### 10.2 New `_language.md` §1.1 register rows — the deduped union

Slice-by-slice, then deduplicated. **Nine terms were proposed by two or three slices at once** — the exact
shape that produced the wave-1 miscount:

| Slice | Proposed | Duplicates removed | Net new |
|---|---:|---|---:|
| A | 15 | — | **15** |
| B | 8 (⚠ the slice's own header says „+9 to §1.1 and +1 to §1.5“, which **double-counts `warten`**) | `Nebenläufigkeit` (A) | **7** |
| C | 12 | `Mandant` (B) | **11** |
| D | 4 | — | **4** |
| E | 11 | — | **11** |
| F | 13 | — | **13** |
| G | 17 | `Mandant`, `Regler` (D), `Perimeter` (C), `Souveränität` (C), `Egress` (C) | **12** |
| **this merge** | `Fallback`, `Merge` | — | **2** |

> ### ⇒ **`_language.md` §1.1 gains 75 rows.**
> ### ⇒ **`_language.md` §1.5 (Verb nach Objekt) gains 10 rows** — slice A's six object-verb pairs, slice B's
> `warten`-rection, and three added here (`Goldstandard` → läuft gegen · `Merge` → blockieren ·
> `Deployment` → freigeben / blockieren).

### 10.3 The other totals that moved

- **Zero-incumbent word fields: 5 → 4.** The brief named five (`Perimeter`, `Souveränität`, `Residency`,
  `Managed`, `Enterprise`). Slice G **refuted two of them**: `Managed` has an incumbent (`verwaltet` 9) and
  `Enterprise`'s one shipped hit is the German-hyphenated `Enterprise-Reifegrad`, i.e. the recommended form.
  Slice C **added one**: `Cloud` — 96 Part III occurrences, **0 appellative** in the delivered German, no
  §1.1 row. ⇒ **`Perimeter` · `Souveränität` · `Residency` · `Cloud`.**
  ⚠ *A zero on the loan is not a zero on the referent.* The probe that declares a gap must be run in the
  **target language**, or it manufactures the gap it then goes and fills with research.
- **German-led (Klasse 3) rows gained across the union: +8** — `Hebel`, `Regler`, `Anbieter`, `Werkzeuge`,
  `verwaltet`, `Spitzenmodell`, `Verkehr`, `Vorfall`. (Six of the eight are the §1.1.g additions in §10.1;
  `Hebel` and `Regler` are not, because there the reflex went to the **wrong German word**, not to the loan —
  which is the §1.1.g exclusion the canon already states.)
- **OPEN rows in this wave: 30** (§9), each with a closing condition.
- **Ban-list rules: 40 → 68** (+28 in the new `wave3_merge_bans` group; two existing rules narrowed).
- **Mermaid labels under gate: 134**, across 8 of the 10 Part III files (`overview.md` and
  `production-failures.md` carry none).

---

## 11. CANON DELTA — exact file, section, current text, proposed text, reason

The orchestrator applies these. **Nothing was edited here.** Deltas already filed identically by two or more
slices are merged into one row and attributed.

| # | File · Section | Current | Proposed | Reason |
|---|---|---|---|---|
| **W3-1** | `_language.md`:53 · :1339 · new note at ~:1350 | „**Zweiundzwanzig** Termini führt das Deutsche belegt selbst“ | „**Achtundzwanzig** …“, plus a „Zuwachs Welle 3 (22 → 28)“ note listing the six rows of §10.1 | **§10.1.** The number sits in the **Injektionsblock**, copied verbatim into every render prompt. Computed once, here, from the union. **No slice and no renderer may restate it** |
| **W3-2** | `rag.md` §8 Phase 3 §D | „`Laufzeitumgebung` ist die JVM/CLR-Klasse Wirtsplattform, `Laufzeit` ist ein **kategorialer** falscher Freund“ | Keep the ⛔ on bare `Laufzeit` **as a component name**. **Scope the `Laufzeitumgebung` rejection to its referent** — it was rejected *for the fan-out sentence*, where the subject was your own application code | The core stands; the **reach** was too wide. §D's own wording defines `Laufzeitumgebung` as exactly Part III's referent. ⚠ **And the procedural argument for reopening is withdrawn**: the component sense ships **5× in 2 files**, four on one page — the row now stands on **attestation**, not on renderer convergence (A6) *(slice A, C1)* |
| **W3-3** | `rag.md` §8 Phase 3 §D | „alle **neun** DWDS-Bedeutungen sind Zeitdauern“ | „**alle** DWDS-Bedeutungen sind Zeitdauern“ — drop the number | The finding holds verbatim; the count does not (run 2 counted **five** on 2026-07-29). A defender who cites the nine loses an argument they should win *(A, C2)* |
| **W3-4** | `_language.md` §1.1, `Host` row, Pflichtglosse | „… eine Chat-App, **eine Agentenlaufzeit**“ | „… eine Chat-App, **eine Agenten-Laufzeitumgebung**“ | The gloss is released for **verbatim** reuse and it **ships**. It instructs renderers to write the exact form §D forbids, and `Agentenlaufzeit` has **0** attestation. **This is the source of collision X-11** *(A, C3)* |
| **W3-5** | `_language.md` §1.1.a | `Container` „SETTLED — Duden“ · `Thread` „SETTLED — Duden“ · `Worker` „WEAK … *regelhaft abgeleitet*“ | `Container` → **SETTLED (Morphologie) / WEAK (IT-Sinn)** · `Thread` → **SETTLED (Paradigma) / WEAK (Referent)** · `Worker` → **upgrade: „des Workers“ and „den Workern“ SHIP** („der Span jedes Workers“, „bei ungleichartigen Workern“) | Duden gives `Container` three senses, all physical; Duden's **only** `Thread` sense is the **chat** thread; and both runs went hunting externally for `Worker` forms that are in our own delivered German *(A, C4–C6)* |
| **W3-6** | `rag.md` §2 kept-EN list | `Prefix Caching` (spaced) | in a German sentence: **`Prefix-Caching`** | `prefix` is a **Substantiv** → § 45 E1. Neighbours unaffected: `Continuous`, `Chunked`, `Late` **are** adjectives (§ 37 E4) and keep their space *(A, C7)* |
| **W3-7** | `rag.md` §2 vs `_language.md` §1.1 | twelve §2-„settled“ terms have **no §1.1 row** (`Prefill`, `Decode`, `Chunked Prefill`, `Prefix Caching`, `Continuous Batching`, `PagedAttention`, `KV-Cache`, `Cold Start`, `Scale-to-Zero`, `Provisioned Throughput`, `Little's Law`, `Admission Control`) — **and `Fallback` is a thirteenth** | add rows, or mark the class explicitly as *Kompositumsbildner ohne Genus* | Structural, not per-term. §2 itself orders a §1.1 row before a term's second use. **`Fallback` is the one that bites in wave 3** — 10 occurrences, 5 files, an H3 and a Mermaid label *(A C8 + this merge, D-6)* |
| **W3-8** | `_language.md` §1.3.3 / §1.1.d / `rag.md` §2 | `Cold Start` spelled three ways in three places | bind **`der Cold-Start`, `die Cold-Starts`, `des Cold-Starts`; `Cold-Start-Latenz`** | §1.3.3 is the binding list and carries the hyphen; §2's box says „**may** stay spaced“ — permissive, not a counter-ruling. Part III needs it 13× in 2 files *(A, C9)* |
| **W3-9** | `rag.md` §2, line 102 | `… Backpressure, Load Shedding, **Admission Control**, …` | **move `Admission Control` to §3 (OPEN)** with its closing condition and the descriptive corpus form | `grep -ci admission _language.md` = **0**, and there is nothing to add — no de.wikipedia lemma, and the only German candidates are translation-memory class. Same shape as the already-reversed `Latency Budget`, `Scratchpad`, `Super-Step` *(B, 1)* |
| **W3-10** | `rag.md` §2, mandatory-gloss table, line 262 | `Backpressure` → „(Gegendruck – Schutz vor Überlast)“ | „(**Schutz vor Überlast – der Empfänger bremst den Sender**)“ | `_language.md`:1255 **disqualifies** *Gegendruck* (AI-generated glossary content farm), and §2 releases this string for **verbatim shipping**. A gloss **explains**; it must not **name**. **Dissent recorded:** *Gegendruck* is ordinary German — but that position requires **changing §1.1.d, not ignoring it** *(B, 2)* |
| **W3-11** | `_language.md` §1.1.d `Queue` + `rag.md` §3 | „*die Warteschlange* für die Datenstruktur, *die Queue* für die konkrete Broker-/Job-Queue“ | **restate the criterion** as *broker/messaging register vs scheduler/everyday register* (do not retire the split) | The split's own cited source does not carry a referent boundary: `Message Queue` **redirects** to `Warteschlange (Datenstruktur)`; the data-structure page itself writes „**die Queue**“. **Zero Part III impact** (all 45 are the runtime object) and **zero shipped impact** (`Queue` 0, `Warteschlange` 0) — which is exactly why it is cheap to decide now *(B, 3)* |
| **W3-12** | `_language.md` §1.1.d `Rate Limit` vs §1.3.3 | §1.1.d prints **„das Rate Limit“** (spaced); §1.3.3 calls spaced noun+noun „nicht normgerecht“ | **report the tension; do NOT change the string in wave 3** | The delivered locale prints „einem **Rate Limit**“. Changing it on a rule argument would make Part III contradict a **shipped Part II sentence**. The rule argument stands **unrefuted — it is outranked, not answered** *(B, 4)* |
| **W3-13** | `_language.md` §1.1.d `Load Shedding` | records *Lastabwurf* as power grid / power plant | add the **aviation** sense (Transall C-160, Airbus A400M — dropping cargo) | A second wrong referent the canon does not record, found by reading the distribution of 69 hits *(B, 8)* |
| **W3-14** | `rag.md` §1, class-1 identifier list | lists `p95` / `p99` | add **`p50`** | Part III writes it and the corpus already ships it 4× („Ziele für **p50 und p95**“) *(B, 6)* |
| **W3-15** | `rag.md` §3 — new OPEN rows | — | add **`graceful shutdown`** (incumbent „das geordnete Herunterfahren“) and **`retry tax`** (⛔ *die Retry-Steuer*; running form „die Mehrkosten der Wiederholungen“ — the `token tax` precedent) | `retry tax` is bold-marked **and inside an image `alt` text**, so it needs a decision, not silence *(B, 7)* |
| **W3-16** | `_language.md` §1.1, `Stellschraube` row (`:1084`) | „Das ist die deutsche Wiedergabe für *the knobs that control this*.“ | add: „**⚠ Nur für `knob`.** `lever` → **der Hebel** (Korpus: 15 Token, 8 Seiten, 3 H2); `dial` → **der Regler** (Korpus: 6). Drei englische Wörter, drei deutsche — nicht zusammenlegen.“ | **Two independent blind runs widened this row to `lever` because it does not say it is narrow** — and then reported the resulting squeeze as a finding. Third instance of „unapplied, not incomplete“ *(D, CD-1)* |
| **W3-17** | `_language.md` §1.1, `Budget` row (`:1090`) | „das Kompositum trägt den Sinn, das nackte *Budget* trägt ihn nicht“ | add: „**Kompositum bei der Erstnennung einer Dimension, danach `das Budget` als Anapher**“ (Korpus: 57 free tokens, 13 pages). **Schreibung:** deutsches Erstglied geschlossen (`Schrittbudget`), englisches mit Bindestrich (`Token-Budget`). ⛔ `Tokenbudget` | The row as written forbids something the corpus does **57 times**, and one run therefore proposed a spelling that contradicts both the row and the corpus *(D, CD-5/CD-7)* |
| **W3-18** | `_language.md` §1.1 — new warning row | — | **`Ausgaben` (spend)** — ⚠ *Warnzeile, keine Freigabe*: „*spend* → **die Kosten** als Laufterm; **die Ausgaben** nur im expliziten Geldrahmen. ⛔ `Token-Ausgaben`, ⛔ `KI-Ausgaben`. Verb `ausgeben` frei.“ | The numerus split **both** runs relied on is contradicted by **12 shipped plural `Ausgaben`, all of them *outputs*** in 7 files — and the corpus writes **`Ausgabe-Token`**, which makes `Token-Ausgaben` an indefensible minimal pair. Highest-traffic wrong ruling in that slice *(D, CD-4)* |
| **W3-19** | `_language.md` §1.1 — new row | — | **`billig / günstig`** — Referentensplit: Modell-/Tarifpreis → **günstig** (Korpus 3/3); Verfahren/Aufwand → **billig** (Korpus 30 Token, 12 Seiten); Antonym durchgehend **teuer** (17) | Both runs banned `billig` outright; complying would require rewriting the shipped corpus in **12 files** *(D, CD-6)* |
| **W3-20** | `rag.md` §3, `burn-rate alerting` | OPEN, no German attestation | **keep OPEN for the attestation question**, and add the delivered form so no renderer re-opens the string: „**die Burn Rate** (feminin, artikeltragend) — „die Burn Rate **des Fehlerbudgets**““ | One run would have shipped an article-less form that **contradicts a delivered sentence**, on the strength of a null finding about *external* sources *(D, CD-7)* |
| **W3-21** | `_language.md` §1.1.e / `rag.md` §3, `Drift` | „Incumbent *der Drift*; … *die Datendrift*, *der Modelldrift*, *der Konzeptdrift* sind **besser belegt**“ | „**der Datendrift**, **der Modelldrift**, **der Konzeptdrift**“, and **strike „besser belegt“** | One head noun, **one feminine and two masculine articles in one canon line** — the wobble §1.1 itself names as the loudest MT signal, **inside the canon**. And the „besser belegt“ clause is false: de.wikipedia `insource` = **0** for all three. A presentation defect, **not** a reopening of the DISPUTED row *(E, 6.1)* |
| **W3-22** | `_language.md` §1.3.3 + §1.1.d — orthography of the Subst.+Subst. loans | `Quality Gate`, `Release Gate` classified as Adj+Subst (§ 37 E4); `das Canary Release` spread; `die MCP-Registry` durchgekoppelt | **rule the family ONCE** — `Canary Release`, `Shadow Deployment`, `Prompt Registry`, `Quality Gate`, `Release Gate` — and re-label the exceptions as **stated exceptions with a reason** rather than rule consequences | `Quality`/`Release` are English **nouns** in attributive position, so the governing rule is **§ 45 E1**; the canon's own cited heise sentence is hyphenated; and the canon is internally inconsistent one row away. **Five terms, ~20 occurrences, several spanning ≥3 files.** Deciding it inside a slice guarantees two spellings on one page — **this ledger holds the incumbents unchanged pending that decision** *(E, 6.2)* |
| **W3-23** | `rag.md` §2 vs `_language.md` §1.1.f / `ai-sdlc.md` §4/§127 — `Release Gate` | §2 lists it as settled kept-EN; §1.1.f and `ai-sdlc.md` hold it **OPEN, zero attestation**; §1.3.3 prescribes its **spelling** as binding | strike or footnote the `rag.md` §2 entry as a bootstrap remnant | The `Golden Set` / `Error Budget` / `Scratchpad` shape: same terminus, settled in one file, OPEN in another. Two ledgers plus `insource:"Release Gate"` = 0 **and** `insource:"Release-Gate"` = 0 outweigh a bootstrap list line *(E, 6.3)* |
| **W3-24** | `_language.md` §1.1 Fallenkasten, `Gate` | names one technical twin (LSTM) | add the **semiconductor** twin (`insource:"des Gates"` = 35: Transistor, MOSFET, Flash-Speicher) **and** the Part-III-specific reason: `gateway` occurs **31×** in the same files and the delivered German already writes `Gateway` | Strengthens the OPEN verdict rather than weakening it, and the third collision is the closest — both words live in **this** lesson *(E, 6.4)* |
| **W3-25** | `_language.md` §1.3.3 „Verbindliche Schreibungen“ **and** `rag.md` §2's citation-form paragraph | both use **`Golden Set`** as the worked example of the Adj+Subst rule | replace the example with `Hybrid Search` / `Late-Chunking-Verfahren` — **and grep both places against EVERY struck §2 row**, not only this one | The loan is **struck twice** in §2 and survives here **inside a section headed „binding spellings“**. A renderer who reads the rules and skips the struck boxes finds a **licence** to write it. **This is the most plausible mechanism of the wave-2 regression and it is still armed** *(F, D1–D3)* |
| **W3-26** | `rag.md` §2 vs §3 / §1.1.e — `Grader` | §2 lists `Grader` as settled kept-EN; §3 and §1.1.e hold it **OPEN, zero German attestation**, Korpusform *der Bewerter* | scope §2's entry explicitly to **the API name** (`model graders`), and record that **`der Bewerter` has now shipped 11× incl. the genitive `des Bewerters`** | Two canon locations disagree about one row; §3/§1.1.e carry the evidence, §2 carries only the mention. Part III needs the word 7×, 6 of them appellative *(F, D4)* |
| **W3-27** | `_language.md` §1.1.e, `Evaluierung / Eval` | „*das Eval / die Evals* nur für den zählbaren Testfall“ (genus declared as Analogie) | mark that half **NEVER-EXERCISED** and name the corpus form **`der Fall`** | Measured: `Evaluierung*` **90**, bare `Eval` **0** across 27 pages; the only `Eval` string is `Eval-Score`. **Six renderers over two waves declined the countable form.** Part III is the densest `eval` slice in the project and would create the incumbent retroactively *(F, D5)* |
| **W3-28** | `_language.md` §1.1 — `Registry`, `Red-Teaming` | no `Registry` row; `Red-Teaming` genus derived **from the `-ing` rule**, stated openly as not from a Beleg | add **`die Registry`** (feminine, corpus-attested); upgrade `Red-Teaming` to **corpus-attested Neutrum** („**ein ernsthaftes** Red-Teaming“ + two genitives) | Both runs reported both as unrecorded gaps; the corpus had already settled both. **Leaving `Red-Teaming` as HOUSE caused a run to re-open a settled row** *(F, D6–D7)* |
| **W3-29** | `rag.md` §8, Phase 6 metaprose | „…Teil III ist die Lektion über das **Werkzeug-Ökosystem**“ | „…das **Tooling-Ökosystem**“ | `Werkzeug-Ökosystem` is **0** in the shipped German; three published forward references already call the lesson `Tooling-Ökosystem`. **The metaprose is the only thing standing behind the other name.** ⚠ Does **not** touch the wave-2 ruling that `Werkzeugkatalog` and `Tool-Katalog` are two referents *(F, D8; = X-15)* |
| **W3-30** | **Shipped Part I defect — report, do NOT repair in this PR** · `part-1-rag/cross-cutting/guardrails/index.md` | „die Lektion über das **Tool-Ökosystem**“ | „die Lektion über das **Tooling-Ökosystem**“ | Three German names point at one Part III page (3 : 1 : 1). `Tool-Ökosystem` is the odd one out **and** collides with the `Tool-` = *agent tool* binding *(F, D9)* |
| **W3-31** | **Shipped Part II defect — report, do NOT repair** · `part-2-agents/multi-agent/deep-dive.md` | „Sie zahlen für das Routing und **die Verkabelung**“ | „… und **die Verdrahtung**“ | One referent, two names, already shipped: **`Verkabelung` : `Verdrahtung` = 1 : 6** (re-measured; the 1:11 in the brief is wrong). Neither points into Part III *(F, D10; A6)* |
| **W3-32** | **Shipped Parts I/II — five names for the OTel GenAI conventions** | „GenAI Semantic Conventions“ 1 · „GenAI Conventions“ 2 · „die GenAI-Konventionen von OpenTelemetry“ 3 · „die semantischen Konventionen … für GenAI“ 1 · „die GenAI-Instrumente von OTel“ 1 | **bind ONE for Part III**: running form **„die GenAI-Konventionen von OpenTelemetry“**; citation form **once**; version citation `Semantic Conventions v1.41.x`. Report the shipped spread | The owning page uses form 3 **three times including in its take-away**, and it is the only variant that inflects as German. **Part III must not add a sixth** *(F, D11; A6)* |
| **W3-33** | `_language.md` §1.1.e (Observability) | no `Uptime` row | add a **Querverweis to §9.3** | §9.3 rules `uptime`/`correctness` **verbatim, on Part III's own English sentence** — but it sits in a *constructions* section, so a renderer looking up the word never finds it. Third instance of the pattern (`Fehlerbild`, `Dashboard`, now this). **A pointer at an empty cell looks exactly like a pointer at a full one — and so does no pointer at all** *(G, G-1)* |
| **W3-34** | `_language.md` §1.1 Fallenkasten | — | add: **`Leitung` is a banned WORD-FIELD in the locative, not a banned phrase.** `über die Leitung` (Akk. + *schicken*) is licensed; `auf der Leitung` (Dat. + *stehen/sitzen*) is not. `Draht`: seven idioms, all human rapport. **`fest verdrahtet` = hardcoded** | **The wave-2 reversal exists only in the shipped prose and in the briefs** — a canon-wide grep for `Nachrichtenformat\|Leitung\|Drahtformat\|wire` returns **no output at all**. `rag.md` §8's own standard is that reversals are „sichtbar gestrichen, nicht still entfernt“. **A ruling that lives only in the output is one rewrite away from being lost** *(G, G-2)* |
| **W3-35** | `_language.md` §1.1 Fallenkasten | — | add: **do not look `Enterprise` up in DWDS** — the lemma there is the French `Entreprise`, **feminine**; a pass that derives a gender from it **cites impeccably and is wrong** | The `Attest` shape: a flawless citation of the wrong lemma *(G, G-3)* |
| **W3-36** | `_language.md` §1.1.a, next to `cap → die Obergrenze` | — | add **`floor → die Untergrenze`** and **`ceiling → die Kapazitätsgrenze`**, **with the asymmetry stated**: *floor may take the antonym of `Obergrenze` because nothing else claims it; ceiling may not, because `cap` owns it* | Four English words (`cap`, `ceiling`, `floor`, `threshold`) currently map onto two German rows. **State the asymmetry or a later sweep „fixes“ it** *(G, G-4; = §8 D-2)* |
| **W3-37** | `_language.md` §1.1 Fallenkasten | — | add **`Image`** (Duden+DWDS: only *Ruf*) · **`Prozess`** (Duden sense 1 = Gerichtsprozess, no EDV sense) · **`containern`** (DWDS: a full paradigm, **one** sense — dumpster-diving for food) · **`Kapazität`** (the person sense = *Koryphäe*) · **`Datensatz`** (Duden gives the **record/row**) · **`Bibliothek`** (Duden has **no EDV sense**) | `containern` is the single most dangerous and **the concordance never showed it** — only one of two runs ever saw the verb. „Eine Anwendung containern“ means, in German, fishing it out of the supermarket bin *(A C11, F D12)* |
| **W3-38** | `_language.md` §1.1 „verwenden, aber nie nackt“ class | — | add **`Worker`** (free German collocations are *Gig/Knowledge/Frontline Worker* — persons), **`Kapazität`**, **`Image`**, **`Prozess`**, **`Thread`**, **`Stack`**, **`Modellkatalog`**, **`Eigenbetrieb`**, **`der Mandant`** | Nine terms whose paradigm is fine and whose **bare singular reads as something else**. `Modellkatalog`: 10 of 10 de.wikipedia hits are **vehicle brochures** *(A C12, C C9, F D12)* |
| **W3-39** | `_language.md` §1.3.x — new collocation rule | — | **`pro` for a rate per EVENT · `je` for a share per PARTITION**, with the corpus figures (`pro Anfrage` 6, `pro Aufruf` 4, `pro Schritt` 4 · `je Chunk` 3, `je Token` 3, `je Dokument` 2) | And it corrects a **false citation** that would otherwise run on as a corpus form: one run banned `pro` citing „je Anfrage“ as the corpus form — **`je Anfrage` is 0 in the delivered German**. A doubling that reports the same error twice looks like confirmation *(C, C-16)* |
| **W3-40** | `rag.md` §2 / §3 | — | add **`Data Residency`** as an OPEN row with the §8 D-1 ruling and its closing condition; add **`Fallback`** to §1.1 with the §8 D-6 ruling | Otherwise the first renderer coins the head term of the most load-bearing section, and the one term nobody was assigned *(C C-14 + this merge)* |
| **W3-41** | `docs/part-3-production/**/_category_.json` (5 labels) | „Cloud AI platforms“, „Part III — Production & LLMOps“, „LLMOps — deploy, monitor, cost“, „Serving — FastAPI + Docker“, „The tooling ecosystem“ | German versions: **„Cloud-KI-Plattformen“** (⛔ „Cloud-AI-…“), **„Das Tooling-Ökosystem“**; Gedankenstriche als `–` | **Delivered, visible strings the concordance does not see.** ⚠ The U+2014 question in the labels is already logged in the canon — no new finding *(C, C-18; corrected to `Tooling-` per X-15)* |
| **W3-42** | `rag.md` §2 confirmations — **no change requested** | `~~Managed Endpoint~~` → *der Endpunkt* · `~~Provisioned Throughput~~` → Klasse 1 · `~~Instrumentation~~` | **confirmed by four slices; no dissent.** Slice C **withdraws** its earlier dissent — the strike now has corpus cover it does not cite (`Endpunkt` **6 : 0**). ⚠ Two neighbours on the same line are worth a look by their owning slices: **`Soft Cap`/`Hard Cap`** (kept-EN while canon and corpus lead `die Obergrenze`, 41 : 0) and **`Vendor-Lock-in`** (carries *Vendor* while the head noun's answer is `der Anbieter`, 38 : 0) | Reported, not litigated *(C C-15, D CD-8, E 6.7, G G-8)* |

---

## 12. What this pass could NOT do

1. **It did no new lexicographic research, by design.** Every external attestation in this sheet comes from one
   of the fourteen raw sheets, via a ledger. Where two runs disagreed about a source's *content* I could not
   adjudicate the source — only its **kind** (case-marked vs nominative-only; one house vs several; dictionary
   vs encyclopedia vs press). **What I did verify myself:** the shipped German corpus, the Part III English
   source, the canon, the concordances, the ban list and the Mermaid inventory.
2. **I did not run the heise/iX/c't counter-check** that the brief permits on two or three rows. It would have
   changed **`der Perimeter`** and **`die GPU`** — the two highest-exposure THIN rows — and it is the single
   most valuable follow-up on this sheet. They are labelled `THIN×2` rather than upgraded (§7).
3. **The corpus can convict, not acquit.** Everything marked `CORPUS PRECEDENT` assumes the shipped German is
   right. **Every slice was told to grep the delivered locale first, so where the locale is wrong all of us
   agree and the agreement looks like verification.** Three shipped defects prove it is not hypothetical
   (W3-30, W3-31, W3-32), and one row survives only *bound* for exactly this reason (`der Eigenbetrieb`:
   three clean shipped uses, and Duden, DWDS and de.wikipedia unanimous that it is a **municipal-enterprise
   legal form**). The rows I would re-check next on the same suspicion: `der Regler`, `die Leiter`/`die
   Sprosse`, `die Engine` (2 tokens, both beside a brand name), `das Verfügbarkeitstheater` (1 token),
   `das Angebot` (1 token).
4. **No native ear, and no independent model, read the sentences this sheet binds.** All collocation checks ran
   against dictionaries, and **an English-built German collocation survives exactly that check**. The highest
   residual risk, in order: „**die bereits angenommenen, noch nicht abgeschlossenen Anfragen zu Ende
   bedienen**“, „**an seine Kapazitätsgrenze stoßen**“, „**die Zusage darüber, wo die Inferenz stattfindet**“,
   „**der Eigenbetrieb großer Sprachmodelle**“, „**der Klassifikator für Sicherheitsrisiken**“,
   „**weitere Anfragen stauen sich**“. **„No collision found“ is not „confirmed by ear.“**
5. **I did not measure the Mermaid labels against the 360 px budget.** Several bound German strings are longer
   than their English originals. That belongs at the rendering gate — §5 says which.
6. **I could not resolve genuine ambiguity in the English source.** One instance is on record („stopped at the
   gate“ — merge or deployment? the sentence names both) and the ledger ruled *both*. Two blind runs reading
   one ambiguous source produce the same reading with doubled confidence; a third read does not help. **That
   one needs the English author, not a German attestation.**
7. **Four label-only or near-label-only terms are HOUSE rulings with zero attestation**, because no slice was
   assigned them and I would not leave a renderer to invent them: `der Ergebnisspeicher`, `der semantische
   Cache`, `Failover`, and `Fallbacks` in the gateway enumeration. They are marked HOUSE/OPEN, not settled.
8. **Two shipped defects are reported and deliberately not repaired** (W3-30, W3-31): they are outside this
   wave's PR, and per the wave-2 `Werkzeugkatalog` lesson a pass that only *counted* a file should not reach
   into one it has not read in full. Each carries counts and a quoted sentence so somebody who has read the
   file can act.
9. **The `gate` construction set is the ruling I am least able to verify.** Shipping constructions instead of a
   word is right and it is the harder thing to hold — only the rendered pages will show whether five files
   converge on the same four constructions across 31 occurrences.
10. **I state no total that is not in §10, and §10 states each total once.** Three slices additionally reported
    deltas in prose (`+2 Klasse-3 rows`, `±0 OPEN`, `+1 zero-incumbent field`, `−2 zero-incumbent fields`).
    **Those are inputs, not results** — the results are in §10 and nothing else may restate them.
