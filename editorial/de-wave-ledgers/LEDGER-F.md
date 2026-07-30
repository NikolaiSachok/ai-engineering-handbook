# LEDGER-F — Gate 6.5, stage 1 · slice F (tooling · evaluation · observability · guardrails)

**Inputs read in full:** `OUT-F-run1.md`, `OUT-F-run2.md`, `dewave3-concord-F.txt`,
`REFERENTS-baseline-verdicts.md`. **New evidence raised by this pass (issue #328):** my own greps over
the 27 shipped German pages of Parts I + II. Nothing in the worktree was touched; no git was run.

**Headline.** Slice F sits on the largest body of already-shipped German in the project, and that turned out
to be true in the strong sense: **twelve rows were settled from the corpus, and the corpus overturned a
ruling in one run or the other in six of them.** The two runs disagreed frontally on five rows, and the two
most consequential (`tooling` → *Werkzeuge* vs *das Tooling*; `eval set` → coined compound vs periphrasis)
were both resolved *against* a coinage and *for* a form the corpus had already exercised. The corpus also
answered two rows **both runs recorded as gaps** (`Red-Teaming` gender, `Registry` gender) and produced one
defect **neither run saw** (a third shipped name for this very Part III lesson).

---

## 1. Binding table

Class: 1 = identifier/untouchable · 2 = kept-EN loan · 3 = German-led (first-mention gloss) · 4 = fully German.
Corpus counts are over the 27 shipped German pages unless stated.

| Terminus | German | Cl. | Status | Artikel / Plural / Genitiv | Kollokation | ⛔ rejected | Evidence grade |
|---|---|---|---|---|---|---|---|
| **golden set** | **der Goldstandard** | 3 | **CORPUS PRECEDENT** | der Goldstandard · die Goldstandards · **des Goldstandards** | „einen Goldstandard **aufbauen**"; „einen schlechten Trace **in den Goldstandard aufnehmen**"; from the trace's side „**zu neuen Fällen im Goldstandard aufsteigen**"; „**ein Fall im Goldstandard**"; „den Goldstandard **durch die Pipeline schicken**" | ⛔ `Golden Set` (struck; regressed once already) · ⛔ `Goldstandard-Fall` / `Goldstandardfall` / `Goldstandard-Metriken` — the corpus uses a **prepositional phrase**, a compound would be a third name | **CORPUS(31)** — `Goldstandard` 29 + `Goldstandards` 2, `Golden Set` **0** case-sensitive. ✅ The ruled *lowercase italic* `golden set` in the class-3 parenthetical (`evaluation/index.md:34,109`) and in the `**[Neue Begriffe]**` footer are **CORRECT and must survive** |
| **eval** (process) | **die Evaluierung** | 3 | **CORPUS PRECEDENT** | die Evaluierung · die Evaluierungen · der Evaluierung | „**die Evaluierung in der CI**"; „**Observability versorgt die Evaluierung mit Material**" (shipped) | ⛔ *das Evaluieren* as a noun | **CORPUS(90)** — `Evaluierung` 89 + `Evaluierungen` 1 |
| **eval** (countable case) | **der Fall / der Testfall** | 4 | **CORPUS PRECEDENT — overrides a canon Hausform** | der Fall · die Fälle · des Falls | „**ein Fall im Goldstandard**"; „fehlgeschlagene Traces werden **zu neuen Fällen im Goldstandard**" (shipped verbatim) | ⛔ **`das Eval` / `die Evals`** in running German prose | **CORPUS(0 vs 90)** — bare `Eval` is **0** shipped; the only `Eval` string is `Eval-Score` ×2 (head noun carries the gender). §1.1.e's Hausform `das Eval` has **never been exercised**; see CANON DELTA D5 |
| **eval set** | **(a) der (eingefrorene) Goldstandard · (b) der Datensatz für die Evaluierung** | 3 | **BOUND (periphrasis; nothing coined)** | see the two settled parts | (b) H2 „**Ein Datensatz für die Evaluierung reicht nicht**"; card title „**Zwei Datensätze für die Evaluierung, nicht einer**"; holdout → verbal, „**Sie halten einen Teil der Beispiele zurück, den das Training nie sieht**" | ⛔ **`die Evaluierungsmenge`** (run 1's coinage, self-declared unattested) · ⛔ **`der Evaluierungsdatensatz`** · ⛔ **`das Eval-Set`** (re-imports the struck loan in a new spelling) · ⛔ calling **both** sets `Goldstandard` | **RECONCILED (run1 coined a compound, run2 built a periphrasis from two settled parts — I chose run2; §3's "prefer a confirmed incumbent over a coinage")** |
| **grader** | **der Bewerter** (alt. **das Bewertungsmodell**) | 3 | **CORPUS PRECEDENT — upgrades the canon's OPEN** | der Bewerter · die Bewerter · **des Bewerters** (shipped) | „**der Bewerter vergibt** dafür Scores"; „**ein Bewerter, den Sie selbst festlegen**"; „auf **Ihren Bewerter hin** optimiert" | ⛔ **`die Bewertungsfunktion`** — that string is the **ToT/LATS scoring function** (CORPUS 5); reusing it fuses two referents · ⛔ `der Grader` as running term (canon reserves it for the API name) · ⛔ *der Benoter*, *der Zensor* | **CORPUS(11)** — `Bewerter` 10 + `Bewerters` 1. The canon calls the row OPEN because there is **no lexicographic** attestation; the *corpus* has settled the string, genitive included |
| **judge** | **der Judge**; verb split **bewerten** / **beurteilen** | 2 / 4 | **CORPUS PRECEDENT** | der Judge · die Judges · **des Judges** | „**Frameworks orchestrieren, Klassifikatormodelle bewerten**"; „**ein Judge auf einer Stichprobe des Verkehrs**"; „**zu Judge-Preisen**"; „ein Werkzeug **danach beurteilen, welches Konzept es umsetzt**" | ⛔ *der Richter* · ⛔ flattening **bewerten** (assign a value to an output) into **beurteilen** (form a judgement about a thing) — the source needs both **on one page** (`tooling-ecosystem/index.md`) | **CORPUS(67)** — `Judge` 54 + `Judges` 13. Verb split: **RECONCILED (run1 had it, run2 gave only `bewerten` — I kept run1's split; the corpus ships both verbs)** |
| **observability** | **die Observability** | 2 | **CORPUS PRECEDENT** | die Observability · **kein Plural** · der Observability | „**die Observability-Plattformen**"; „die Observability **versorgt die Evaluierung mit Material**" | ⛔ *die Beobachtbarkeit* as a running term | **CORPUS(51 : 2)** — and both German hits are the one-off introduction gloss, read line by line, not counted |
| **trace** | **der Trace** | 2 | **CORPUS PRECEDENT** | der Trace · die Traces · des Traces | „**der Trace beginnt in Ihrem Dienst**"; „**über die Spans des Traces** einer Stufe zuordnen" (shipped); verb → „**nachverfolgen / protokolliert**" | ⛔ *die Trace*, *das Trace* · ⛔ *tracen* (OPEN) · ⛔ *die Spur* | **CORPUS(81)** |
| **span** | **der Span** | 2 | **CORPUS PRECEDENT** | der Span · **die Spans** · des Spans | „**Spans erzeugen**" (shipped verb: „erzeugt seinen eigenen lokalen Trace"); „**die Spans weiterleiten**"; „**Sie bekommen jeden Span doppelt**" | ⛔ **`die Späne`** (Duden's plural for the woodchip — the single highest-probability inflection defect in this slice) · ⛔ *Spans emittieren* (⟶ `emittieren` is rationed) | **CORPUS(32)** |
| **OpenTelemetry / OTel** | **OpenTelemetry**, kurz **OTel** | 1 | **BOUND** | proper name, **artikellos**; compounds durchgekoppelt: *der OpenTelemetry-Collector*, *die OTel-Instrumentierung* | „**einmal gegen OTel instrumentieren**"; „**nie doppelt instrumentieren**"; „**OTel ist das Bindegewebe**" | ⛔ any translation of the product name · ⛔ *der OpenTelemetry-Sammler* · ⛔ „ein OpenTelemetry Collector" undurchgekoppelt | **AGREED×2 + CORPUS(12)**; `der Collector` ships with its own gloss („Der Collector – die Komponente, die die Spans einsammelt") |
| **semantic conventions** | running form **die GenAI-Konventionen von OpenTelemetry**; citation form **die GenAI Semantic Conventions von OpenTelemetry** (once, first mention); version citation **Semantic Conventions v1.41.x** | 2/3 | **CORPUS PRECEDENT (running form) — RECONCILED against both runs' first choice** | die Konventionen · Plural only · der Konventionen | „**die Konventionen vereinheitlichen die Namen der Spans und Attribute**"; „**Diese Konventionen haben den Status *Development***" (shipped verbatim) | ⛔ **bare `die Konvention`** for the standard (Duden has treaty / social norm / fencing, **no technical-standard sense**) · ⛔ `die semantischen Konventionen` as the **running name** · ⛔ **adding a sixth name** | **CORPUS(3 on the owning page, incl. its take-away)** vs `GenAI Conventions` 2, `GenAI Semantic Conventions` 1, `semantische Konventionen` 1, `GenAI-Instrumente` 1. **RECONCILED (run1 wanted kept-EN `die Semantic Conventions` on a real heise citation, run2 wanted the German running form — I chose run2 because the corpus's owning page decides, and run1's citation licenses the *citation* form, which I kept)** |
| **dashboard** | **das Dashboard** | 2 | **CORPUS PRECEDENT** | das Dashboard · die Dashboards · des Dashboards | „**ein grünes Dashboard fängt an zu lügen**"; shipped near-verbatim „**eine Wand grüner Dashboards über einem Dienst, der falsch liegt**" | ⛔ *die Übersichtsseite*, *die Instrumententafel* | **AGREED×2 + CORPUS(7)**. ⚠ The row lives in `_language.md` **§1.1.a**, not §1.1.e — run 2 verified the §1.1.e cross-reference resolves |
| **dataset** | **der Datensatz**; escape **der Datenbestand** | 3 | **CORPUS PRECEDENT + binding class** | der Datensatz · die Datensätze · des Datensatzes | „**die Qualität des Datensatzes bleibt Ihre Aufgabe**"; „**ein flacher, verrauschter Datensatz**"; „**kein Datensatz, keine Evaluierung**" | ⛔ *das Dataset*, *das Datenset* · ⛔ *die Datenmenge* as the artefact's name | **CORPUS(17)**, always in the collection sense. ⚠ Duden defines `Datensatz` as the **record/row**; on `tooling-ecosystem/deep-dive.md` Postgres, ClickHouse and rows are within three sentences — there switch to the shipped **`der Datenbestand`** (CORPUS 1) or bind by apposition |
| **classifier** | **der Klassifikator** | 3 | **CORPUS PRECEDENT** | der Klassifikator · die Klassifikatoren · des Klassifikators (Latin `-or`, **no n-declension**) | „ein **trainierter Klassifikator** sagt vorher …" (shipped); „**Klassifikatormodelle bewerten**"; „einen Klassifikator **davorsetzen**" (shipped) | ⛔ *der Klassifizierer* · ⛔ *der Classifier* | **AGREED×2 + CORPUS(5)**. ⚠ de.wikipedia's *first* sense is a **person** (library cataloguer) — bind at first mention: „der Klassifikator (ein Modell, das Text auf Risikokategorien bewertet)" |
| **safety classifier** | **der Klassifikator für Sicherheitsrisiken**, short form thereafter **der Klassifikator** | 3 | **OPEN (incumbent held: none exists; closes when a non-MT German source names the component)** | see head noun | first mention „**der Klassifikator für Sicherheitsrisiken** – ein Modell, das Text **auf Risikokategorien** bewertet"; thereafter „**der Klassifikator**" | ⛔ **`der Sicherheitsklassifikator`** — **both runs reject it**: its only source is MT-disqualified (Google Cloud de), *and* `Sicherheit-` collapses German's one word for *safety* **and** *security*, which these very pages carry side by side (`die Vertrauensgrenze`, `das Prinzip der geringsten Berechtigungen`) | **RECONCILED (run1 `Klassifikator für Sicherheitsrisiken` on the ASR "Kopfnomen + Attribut" canon precedent; run2 `der Safety-Klassifikator` on the shipped `Tool-Katalog` durchkopplung pattern — I chose run1's, because it coins nothing and the source's own apposition already says it; run2's remains a defensible fallback). See §7.1** |
| **guardrail** (plural / concept) | **die Guardrails** | 2 | **CORPUS PRECEDENT** | **plural only**; first mention per page glossed „(**Leitplanken – Schutzregeln um das Modell**)" | compound first element is **`Guardrails-`**: „**die Guardrails-Schicht**" (shipped ×3), „eine Konfigurations- oder **Guardrails-Richtlinie**"; „**die Auslöserate der Guardrails**" | ⛔ `Guardrail-` as the compound first element (the corpus writes `Guardrails-`) | **CORPUS(38 + 3 `Guardrails-Schicht`)** — **RECONCILED (run1 `Guardrails-Richtlinie`, run2 `Guardrail-Richtlinien`; the corpus decides for run1)** |
| **guardrail** (countable singular) | **die Schutzregel** — or pluralise, or use a compound whose head carries the gender | 3 | **OPEN (incumbent held: the plural; closes when a German sentence writes „das Guardrail" or „der Guardrail" at heise/iX/INNOQ/dpunkt)** | die Schutzregel · die Schutzregeln · der Schutzregel | „die Einheit **einer selbst gebauten Schutzregel**"; „**eine gut gemeinte Schutzregel** beginnt, berechtigte Anfragen abzulehnen"; „das Stück **einer Schutzregel**, das keine Bibliothek mitliefert" | ⛔ **inventing `der/das Guardrail`** — the one shipped singular („Was sich umgehen lässt, ist **kein** Guardrail") is **gender-blind** and pins nothing · ⛔ **`der Schutzmechanismus`** (run 1) — 0 anywhere, a third name for one referent | **RECONCILED (run1 rebuilt the 11 singulars around `Schutzmechanismus`/plural, run2 around `Schutzregel`/plural — I chose `Schutzregel`: it is the corpus's own gloss noun, CORPUS(2, plural), and singularising it is safe because `die Regel` carries the gender)** |
| **red-teaming** | **das Red-Teaming** | 2 | **CORPUS PRECEDENT — this closes a row run 2 declared OPEN** | **das** Red-Teaming · **kein Plural** · **des Red-Teamings** | „**Red-Teaming ist der systematische Angriff auf die eigene Anwendung**" (shipped); „**ein ernsthaftes Red-Teaming fährt beides**" (shipped — this is the sentence that pins the gender); „**Red-Teaming-Läufe** vor der Freigabe **ansetzen**"; „**die Erfolgsrate der Angriffe** von Release zu Release **verfolgen**" | ⛔ `red-teamen` / `geredteamt` · ⛔ `der Red-Teamer` (**0** in Part III — nothing to coin) · ⛔ `Red Teaming` spaced in running prose · ⛔ `Red-Team-Läufe` (mixed base form; heise's attested compound is `Red-Teaming-…`) | **CORPUS(12)** — `Red-Teaming` 9 + `Red-Teamings` 2 + 1 footer. **Gender attested, not derived:** „**ein ernsthaftes** Red-Teaming" (neuter `ein …-es`) plus two genitives „eines ernsthaften / automatisierten **Red-Teamings**". **RECONCILED (run1 held Neutrum by rule; run2 declared the article OPEN — the corpus proves run1 right)** |
| **safety** (other senses) | see SC-2 | 1 / 3 | **BOUND (the split) / HOUSE (the wording)** | — | product names untouched: „**Azure AI Content Safety**", „**Vertex Model Armor**", „**Bedrock Guardrails**"; *multi-tenant safety* → „**Sitzungsisolierung, damit sich mehrere Mandanten nicht in die Quere kommen**"; *content safety on MCP traffic* → „**die Prüfung der Inhalte** auf MCP- und A2A-Verkehr" | ⛔ bare `die Sicherheit` as a running rendering of *safety* on any page that also carries *security* · ⛔ *die Inhaltssicherheit* (0 Belege) · ⛔ *die Inhaltsmoderation* (canon-⛔; the DSA form is „Moderation von Inhalten", and that is not this referent) | **AGREED×2 on the split, HOUSE on (c)** — run1 treated `content safety` as a vendor feature (class 1), run2 as appellative. **RECONCILED: class 1 where the Azure product is named, appellative „die Prüfung der Inhalte" where APIM is described as doing it** |
| **validator** | **der Validator** | 2 | **BOUND (paradigm partly derived)** | der Validator · **die Validatoren** · **des Validators** *(genitive inherited from the `-or` class, §1.1.b `Annotator`)* · Dat. Pl. den Validatoren | „einen Validator **schreiben**"; „den Validator mit `.use()` in einen `Guard` **einbinden**"; „einen Validator **mit `noop` ausliefern**"; „**gegen ein Schema validieren**"; „ein Validator **ist nicht umsonst**" | ⛔ **der Prüfer** (Duden gives only person senses; also on the canon's write-away list) · ⛔ **die Prüfregel** (wrong referent — the source calls it „the smallest piece … you **author**", a code unit; the rule lives in `on_fail`) · ⛔ **die Prüfinstanz / die Kontrollinstanz** (`Instanz` collides with the object instance — and on this very page a `Validator` subclass is derived and a `Guard()` instantiated) · ⛔ *die Validators*, *der Validierer* | **AGREED×2, both WEAK, and honestly so.** Duden 404, DWDS 404, **`Validator` 0 in the shipped corpus and 0 in all three canon files**. Two independent tier-3 lemma definitions (de.wikipedia, SELFHTML); plural attested twice; **genitive derived** |
| **validate / validation** | verb **validieren**, noun **die Validierung** | 3 (verb) / 1 (`validate()` method) | **CORPUS PRECEDENT** | die Validierung · die Validierungen · der Validierung | „**Guardrails AI validiert** auch strukturierte Ausgaben"; „Daten **gegen ein Schema validieren**"; „die **Eingabevalidierung**" | ⛔ *validaten*, *gevalidiert* · ⛔ *validieren* for *to verify* (→ **prüfen / nachweisen**) | **CORPUS(14)** — `Validierung` 8 + `Validieren`/`validieren` 3 + `validiert` 2 + `Validierungsfehler` 1. ⚠ run 2 prefers plain **`prüfen`** in running prose and reserves `validieren` for where the API name is on screen — recorded as a **register note**, not a conflict |
| **seam** | **die Nahtstelle** | 3 | **CORPUS PRECEDENT + dictionary** | die Nahtstelle · die Nahtstellen · der Nahtstelle | „die **eine Nahtstelle**, über die Persistenz, Gedächtnis und Observability allesamt **andocken**" (shipped verbatim); „die Nahtstelle **zwischen** X **und** Y"; „**die Schleife wird an zwei Nahtstellen zu einem einzigen System**" | ⛔ **die Naht** bare — DWDS lists only textile/welding/surgical senses plus „aus allen Nähten platzen"; ⚠ **the corpus does contain one bare `Naht`** („Es übertüncht **die Naht**, die Sie hätten sehen müssen", `generation/deep-dive.md`) — that is a **different, concrete image** and does **not** license the word for this referent · ⛔ **die Schnittstelle** = *interface*, occupied, including a Part II **H1** · ⛔ *die Fuge*, *die Bruchstelle* | **AGREED×2 + CORPUS(2) + DWDS figurative sense.** The best-founded row in the slice: dictionary and corpus agree independently |
| **wiring / to wire** | **die Verdrahtung**, verb **verdrahten** | 3 | **CORPUS PRECEDENT + narrow prohibition** | die Verdrahtung · die Verdrahtungen (avoid) · der Verdrahtung | „die **Verdrahtung der Tool-Calls**" (shipped); „**wie die Werkzeuge zu einem einzigen Stack verdrahtet werden**"; „**diese Seite gehört der Verdrahtung**"; H2 „The stack, wired" → „**Der fertig verdrahtete Stack**" | ⛔⛔ **any degree adverb with `verdrahtet`** — „gut / bestens / eng / exzellent verdrahtet" is a fixed German idiom meaning *well-connected, has the right contacts*; „now wired into CI" → „**jetzt in die CI eingebunden**", never „gut verdrahtet" · ⛔ **`fest verdrahtet`** = *hardwired/hardcoded*, inverts the sentence · ✅ **`fertig verdrahtet`** is neither and is shipped · ⛔ **die Verkabelung** as a second name (shipped once — see D10) | **AGREED×2 + CORPUS(11 forms).** Both runs independently ran the idiom check and both hit the participle. Duden lemma for the noun with **no** idiom; DWDS `verdrahten` sense 2 = electronics. The *software* sense rests on the corpus, not a dictionary |
| **stack** (noun) | **der Stack** — **never bare at first mention** | 2 | **THIN×2 (single-source agreement) — BOUND with an obligatory binding gloss** | der Stack · die Stacks · **des Stacks** *(genitive derived, the weakest string in this slice)* | first mention bound: „**ein einziger Stack – die Reihe aufeinander aufbauender Werkzeuge**"; „**zu einem einzigen Stack zusammenwachsen**"; H1 „… die Nahtstellen, **die einen Stack zusammenhalten**" | ⛔ *der Stapel*, *der Werkzeugstapel* (sends the reader to the LIFO) · ⛔ *das Stack* | **THIN×2.** Both runs agree — on **one tier-3 source each and no dictionary** (run1: a heise definition sentence; run2: de.wikipedia `Softwarestack`). **Duden 404, DWDS 404. `Stack` is 0 in the shipped corpus and the only hit is `Stacktrace` ×2**, i.e. the *competing* referent is the reader's only prior in this book. Two runs, one hole |
| **stack** (verb) | **hintereinanderschalten** | 4 | **BOUND** | — | „**Sie können sie hintereinanderschalten: erst SFT, dann DPO**" | ⛔ *stacken* · ⛔ *kombinieren* (run1's alternative — it loses the ordering the sentence asserts) | **RECONCILED (both runs offered `hintereinanderschalten`; run1 also allowed `kombinieren` — dropped)** |
| **tooling** (bare appellative) | **die Werkzeuge** (plural) | 4 | **CORPUS PRECEDENT — this reverses run 1** | die Werkzeuge · pl. · der Werkzeuge | „**welche Werkzeuge** Sie um das laufende System legen"; „**die Werkzeuge für den Produktivbetrieb**"; „**die eigenen Red-Teaming-Werkzeuge einer Plattform**"; „**die Werkzeuge für die DSGVO**" | ⛔ **`das Tooling`** as a **free noun** (no Duden lemma, no DWDS lemma, **0 shipped**; run 1's evidence was a single article-marked heise headline) · ⛔ **`die Tools`** for this referent — `Tool(s)` is bound to the **agent-callable tool** (**CORPUS 219**) and both referents live on the same Part III pages · ⛔ *die Werkzeugkette*, *das Werkzeugwesen* | **CORPUS(6 in exactly this referent)** — „(**Die Werkzeuge** – LangSmith, Langfuse, Arize Phoenix, OpenTelemetry …)", „(**Die Werkzeuge** dafür – Guardrails AI, NeMo Guardrails, Llama Guard …)", „**Werkzeuge** dafür gibt es. Ragas …", „**Werkzeuge** gibt es: Ragas …", „**Tracing-Werkzeuge** setzen Traces … zusammen", „**Ein paar Werkzeuge** zeigen die wichtigsten Ansätze". **RECONCILED — see §3, R-1; this is the highest-traffic decision in the slice (9 of 10 files)** |
| **tooling** (compound first element) | **Tooling-** | 2 | **CORPUS PRECEDENT** | takes the head noun's gender | „**das Tooling-Ökosystem**" | ⛔ „Tooling Ökosystem" undurchgekoppelt | **CORPUS(3)** |
| **tooling ecosystem** | **das Tooling-Ökosystem** | 2 | **CORPUS PRECEDENT (the page's own name)** | das Tooling-Ökosystem · die Tooling-Ökosysteme · des Tooling-Ökosystems | page title „**Das Tooling-Ökosystem**", deep-dive „**Das Tooling-Ökosystem – Vertiefung**"; cross-reference form (shipped) „**beim Tooling-Ökosystem in Teil III**" | ⛔ **das Werkzeug-Ökosystem** (0 shipped; it exists **only** in `rag.md` §8 Phase 6 metaprose) · ⚠ **`das Tool-Ökosystem` is shipped once and is a defect — see D9** | **CORPUS(3 forward references) vs `Tool-Ökosystem` 1 vs canon metaprose 0 shipped.** Head noun `das Ökosystem` **CORPUS(10)** with genitive „auf der Ebene **des Ökosystems**" + DWDS's explicit IT sense. ⚠ `Werkzeugkatalog` (1×, the catalogue of *products*) is a **different referent** and the Wave-2 ruling on it stands untouched |
| **framework** | **das Framework** | 2 | **CORPUS PRECEDENT** | das Framework · die Frameworks · des Frameworks | „**Frameworks orchestrieren**"; „**Unterstützung für eigene Frameworks**" | ⛔ *das Rahmenwerk* | **CORPUS(89)** |
| **library** | **die Bibliothek** — **not bare at first mention** | 3 | **CORPUS PRECEDENT** | die Bibliothek · die Bibliotheken · der Bibliothek | „eine **Python-Bibliothek für Validatoren**" (⚠ **not** „Python-Validator-Bibliothek"); „eine **eigene Bibliothek für die Evaluierung**"; „das **keine Bibliothek für Sie mitliefert**" | ⛔ *die Library*, *die Lib* | **AGREED×2 + CORPUS(6)**. ⚠ Duden lists four senses, **all books and buildings, no EDV sense** — rescued at tier 3 by de.wikipedia `Programmbibliothek`, whose lemma **licenses the short form itself**. In a book about documents, bind at first mention |
| **integration** | **(a) die Anbindung** (a connector) · **(b) die Integration** only inside the shipped compounds | 3 | **CORPUS PRECEDENT for the split** | die Anbindung · die Anbindungen · der Anbindung | „**die einfachste Anbindung, die es gibt**"; „**die engste Anbindung, die Sie bekommen**"; „**Konnektoren und die Anbindung an AgentCore**"; layer/problem → „**die Integrationsschicht**", „**das M×N-Integrationsproblem**" | ⛔ collapsing the two into one German word · ⛔ **bare plural `die Integrationen`** as a running term (0 shipped; the shipped plural is `Anbindungen`) | **CORPUS(14 `Anbindung(en)` + 6 `Integrations-` compounds)**, both halves in one shipped sentence: „Die **Integrationsschicht** besteht aus breiten Bibliotheken fertiger **Anbindungen**". **RECONCILED (run1 used `Anbindung` for everything; run2 split — I chose run2, with run1's ⛔ on the bare plural kept)** |
| **integration** — the *two integrations* in `tooling-ecosystem/deep-dive.md` | **die Nahtstellen** | 3 | **BOUND** | — | „**Bringen Sie diese beiden Nahtstellen in Ordnung**" | ⛔ „diese beiden Anbindungen" (run 2) | **RECONCILED (run1 wins on a source reading: the paragraph calls them *seams* two sentences later — verified in the concordance)** |
| **data store** | **der Datenspeicher** — never without the enumeration in reach | 3 | **OPEN (incumbent held: `der Datenspeicher`; closes when a German sentence calls running services — Postgres/ClickHouse/S3 — `Datenspeicher`)** | der Datenspeicher · **die Datenspeicher** (null plural) · des Datenspeichers | H1 „**Vier Datenspeicher**, ein selbst geschriebener Validator und die Nahtstellen, die einen Stack zusammenhalten"; „**Sie betreiben jetzt vier Datenspeicher**: Postgres, ClickHouse, Redis/Valkey und S3/Blob" | ⛔ *der Data Store* · ⛔ **der Store** (canon-assigned to a **different** referent with an obligatory gloss) · ⛔ *vier Datenhaltungen* (run 2 flagged it unattested itself) · ⛔ *die Datenbanken* (S3/Blob is not one) | **AGREED×2, both uneasy, and the corpus is silent — `Datenspeicher` is 0 shipped.** Both dictionaries define the **medium**; our referent is **services**. Held because both runs preferred a thin lemma over a coinage. run 2's escape `vier Speichersysteme` is **not** adopted: both source occurrences carry the enumeration, and a second name is the worse risk |
| **prompt management** | **das Prompt-Management** (feature name); the corpus's running term for the thing is **die Prompt-Registry** | 2 | **BOUND (compound rule) / gender of `Registry` now CORPUS** | das Prompt-Management · kein Plural · des Prompt-Managements · **die Registry** · die Registrys · der Registry | „eine **Prompt-Registry** – das Prompt-Management in LangSmith oder Langfuse – lässt sie …"; „**Prompt-Management, Datensätze und Evaluierung sowie Kostendashboards**" | ⛔ *die Promptverwaltung* / *die Prompt-Verwaltung* (a second name for a referent the corpus already names) · ⛔ `Prompt Management` spaced (§ 45 E1) | **BOUND for the compound (rule-built, unattested → weak); CORPUS(6) for `die Registry`** — „In **einer** Registry gelistet zu sein ist keine Prüfung", „**Eine** Registry veröffentlicht Metadaten", „**Die offizielle MCP-Registry**". **Both runs reported `Registry`'s gender as an unrecorded gap; the corpus had already settled it as feminine** |
| **adopt / adoption** | verb **einführen**, noun **die Einführung** | 4 | **BOUND** | die Einführung · die Einführungen · der Einführung | H2 „**Wann Sie was einführen**"; „**Standardreihenfolge der Einführung: Tracing → Evaluierung in der CI → Guardrails**"; „**der Aufwand für die Einführung geht gegen null**"; „**Ein Werkzeug für die Evaluierung einzuführen ist nicht dasselbe, wie zu evaluieren.**" | ⛔⛔ **die Adoption / adoptieren** — Duden gives `Adoption` **exactly one** sense, the adoption of a child; **no technology sense on any tier** · ⛔ *die Übernahme* (reads as a takeover) | **AGREED×2**, and both runs independently found the same tier-1 trap |
| **annotation** | — | — | **N/A — verified null in Part III** | — | — | — | **Concordance 0 + both runs' own greps 0.** The German register nevertheless exists (`_language.md` §1.1.b `Annotator / Übereinstimmung`; shipped „Übereinstimmung der **Annotationen** (κ = 0,88)") — the pointer resolves, Part III simply does not need it |
| **experiment tracking** | — | — | **N/A — verified null in Part III and in all three canon files** | — | — | ⚠ **Do not pre-coin** `Experiment-Tracking` for a later wave | **Concordance 0 + both runs' greps 0 + `Experiment` 0 in canon.** Both sides zero: the concept is **absent**, not merely unnamed |
| **Mermaid** `EG{"Eval gate<br/>(golden set)"}` | **`Evaluierung<br/>(Goldstandard)`** in the diamond; the verdict moves to the edges: „**gibt die Auslieferung frei**" / „**blockiert die Auslieferung**" | 3 | **OPEN (cross-slice: `gate` is not mine to bind) — my slice's position** | — | sibling edge „gates the deploy" → „**gibt die Auslieferung frei**" (`Freigabe` **CORPUS 4**) | ⛔ **`das Eval-Gate`** (run 1) — `gate` as a bare noun is standing-OPEN and ships **constructions, not a word** · ⚠ `der Kontrollpunkt` (run 2) is the canon's word but is **0 in the shipped corpus** | **RECONCILED (run1 coined `Eval-Gate` against the standing `gate` ruling; run2 used the canon word `Kontrollpunkt`, which has never shipped — I let the **diamond shape** carry the gate and moved the verdict to the shipped `Freigabe` edge). Final string belongs to the slice that owns `gate`** |

**Two ⚠ carve-outs that a checker will read as regressions and must not "fix":**
1. the class-3 parenthetical „der **Goldstandard** (*golden set*) – der handgeprüfte Referenzdatensatz" — the
   lowercase italic English is **prescribed**;
2. the `**[Neue Begriffe]**` footer of both `tooling-ecosystem` pages —
   `instrumentation, OpenTelemetry GenAI conventions, safety classifier, red-teaming, observability, guardrails` —
   stays **English and lowercase** until the glossary wave. `instrumentation` there is **not** a regression of
   the German-led `die Instrumentierung`.

---

## 2. Sense cards

Every branch ships a **German sentence**, not a word.

### SC-1 · `golden set` ↔ `eval set` ↔ `dataset` — three referents, three names, and a whole card in `production-failures` hangs on it

**Ask before writing:** *Is this set (a) the one hand-checked reference the regression is measured against,
(b) one of two sets the text is currently holding up against each other, or (c) the raw material?*

- **(a) the frozen reference** → **der Goldstandard**.
  > „**Die Evaluierung in der CI ist das Regressionsgate: Jede Änderung läuft gegen den Goldstandard, und Metriken unter dem Schwellenwert blockieren die Zusammenführung.**"
- **(b) one of two juxtaposed sets** → **der Datensatz für die Evaluierung** (periphrasis; nothing coined).
  > „**Ein Datensatz für die Evaluierung reicht nicht.**" · „**Zwei Datensätze für die Evaluierung, nicht einer.**"
  > „**Behalten Sie beide: Der eingefrorene Goldstandard fängt die Regressionen ab; ein zweiter, aus dem Live-Verkehr nachgezogener Datensatz fängt die Wirklichkeit ein.**"
- **(b′) the held-out set in fine-tuning** → go **verbal**, following the shipped construction.
  > „**Sie halten einen Teil der Beispiele zurück, den das Training nie sieht, trainieren, und schicken das nachtrainierte Modell danach durch dieselbe Prüfung wie jede andere Auslieferung.**"
- **(c) the raw material** → **der Datensatz**.
  > „**Kein Datensatz, keine Evaluierung.**" · „**Die Qualität des Datensatzes bleibt Ihre Aufgabe.**"

⚠ **The error this card exists to prevent:** in `production-failures` §3 **only the frozen one** is the
Goldstandard. Calling both `Goldstandard` deletes the section's thesis. And the compound both runs were
tempted by — `Evaluierungsmenge` / `Evaluierungsdatensatz` — would sit next to `Goldstandard` as a synonym
on the same page while being attested nowhere.

### SC-2 · `safety` — no single German word carries all three, and one of them is a *security* word

**Ask before writing:** *Is `safety` inside a **product name**, a property of **tenancy**, or **content risk**?*

- **Product name** → class 1, untouched.
  > „**Dieselben Konzepte gibt es als verwaltete Dienste: Bedrock Guardrails, Azure AI Content Safety, Vertex Model Armor.**"
- **Tenancy / isolation** → **Trennung**, never `Sicherheit`.
  > „**Sitzungsisolierung, damit sich mehrere Mandanten nicht in die Quere kommen.**"
- **Content risk** → bind to the risk.
  > „**Der Klassifikator für Sicherheitsrisiken – ein Modell, das Text auf Risikokategorien bewertet – ordnet die Eingabe einer Kategorie zu.**"
  > „**Das Gateway legt eine Prüfung der Inhalte über den MCP- und A2A-Verkehr.**"

⚠ German has **one** word for *safety* and *security*, and these pages carry both — `die Vertrauensgrenze`,
`das Prinzip der geringsten Berechtigungen`, Prompt-Injection on one side, harmful-content scoring on the
other. Any rendering that puts bare `Sicherheit` on both is the "one German word, two English referents"
defect.

### SC-3 · `seam` ↔ `wiring` ↔ `interface` — the metaphor that carries an H1 and an H2

**Ask before writing:** *Is this the **place** where two systems meet, the **act/arrangement** of connecting
them, or an **API**?*

- **Place** → **die Nahtstelle**.
  > „**Die Schleife wird an zwei Nahtstellen zu einem einzigen System: OTel ist das Bindegewebe zwischen dem Produktivsystem und der Observability, und die Aufnahme eines Traces in den Goldstandard ist die Übergabe zwischen Observability und Evaluierung.**"
- **Act / arrangement** → **die Verdrahtung**, verb **verdrahten**.
  > „**Diese Seite gehört der Verdrahtung, nicht der Theorie.**" · „**Der fertig verdrahtete Stack.**"
  > „**Die Verdrahtung ist das Gegenteil: Sie ändert sich mit jedem Stack, jedem Wechsel des Backends, jeder Entscheidung über die Skalierung.**"
- **API** → **die Schnittstelle** — and **never** for the two above; the corpus has already given that word to
  *interface*, including in a Part II H1.

⚠ **The collocation check that makes this card expensive:** „**gut / bestens / eng verdrahtet**" is a fixed
German idiom meaning *well-connected, has the right contacts*. „now wired into CI" must become
„**jetzt in die CI eingebunden**". „**fest verdrahtet**" means *hardwired*. Only „**fertig verdrahtet**" is
safe — and it is the shipped form.

### SC-4 · `stack` — the tool stack and the call stack are one word in German too, and only the call stack has shipped

**Ask before writing:** *Is this the layered set of products, or a data structure?*

- **Product stack** — bound at first mention on every page, bare thereafter.
  > „**… wie die Werkzeuge für Evaluierung, Observability und Guardrails zu einem einzigen Stack – der Reihe aufeinander aufbauender Werkzeuge – verdrahtet werden statt zu drei zusammenhanglosen Produkten.**"
- **`stack` as a verb** — a different word entirely.
  > „**Sie können sie hintereinanderschalten: erst SFT, dann DPO.**"

The reason this card exists: the shipped German contains `Stacktrace` and **not one** free `Stack`, so the
reader's only prior for this string **in this book** is the call stack.

### SC-5 · `judge` — the component, scoring an output, and forming a judgement about a thing

**Ask before writing:** *Does something assign a value to an **output**, or does someone form a **judgement
about a thing**?*

- **Component** → **der Judge**.
  > „**Jede Prüfung eines Validators, die selbst ein LLM-as-a-judge ist, kostet einen Modellaufruf pro Anfrage.**"
- **Score an output** → **bewerten**.
  > „**Frameworks orchestrieren, Klassifikatormodelle bewerten.**"
- **Judge a thing** → **beurteilen**.
  > „**Beurteilen Sie ein Werkzeug danach, welches Konzept aus Teil I es umsetzt.**"

⚠ Both verbs are needed on **one** page (`tooling-ecosystem/index.md`). Flattening them is a reading error,
not a style one.

### SC-6 · `tooling` vs `tools` — two referents that share a page

**Ask before writing:** *Are these the **products you install around the system**, or the **functions an
agent can call**?*

- **Products around the system** → **die Werkzeuge**.
  > „**Welche Werkzeuge Sie um das laufende System legen, entscheidet die nächste Lektion.**"
  > „**Die eigenen Red-Teaming-Werkzeuge der Plattformen decken denselben Bereich ab.**"
- **Functions an agent calls** → **die Tools**.
  > „**Das Gateway macht aus einem MCP-Server ein aufrufbares Tool und legt eine Identitätsschicht darunter.**"

The reason this card exists: `cloud-platforms/deep-dive.md` puts both on the same page — a tool gateway that
turns an API into a callable **tool**, described in a lesson about the production **tooling**. The shipped
German already keeps them apart, `Tool(s)` 219 : `Werkzeug(e)` 11, and the eleven are **exactly** this slice's
referent (LangSmith/Langfuse/Arize, Guardrails AI/NeMo/Llama Guard, Ragas, ingestion tools).

### SC-7 · `dataset` — in German, the row before it is the collection

**Ask before writing:** *Could a reader on this page hear `Datensatz` as a single record?*

- **Collection sense** (ours, all 9 occurrences).
  > „**Ein kleiner, sauberer, für die Domäne repräsentativer Datensatz schlägt einen großen, verrauschten.**"
- **Danger zone** — `tooling-ecosystem/deep-dive.md` has Postgres, ClickHouse and rows within three sentences.
  > „**ein flacher, verrauschter Datenbestand**" · „**eine flache, verrauschte Menge von Beispielen**"

---

## 3. RUN DISAGREEMENTS — every place run 1 and run 2 differ

| # | Row | run 1 | run 2 | Resolution & reason |
|---|---|---|---|---|
| **R-1** | **`tooling` (bare)** — *the most consequential row of this slice; 9 of 10 files* | **`das Tooling`** (WEAK, one article-marked heise headline + the `-ing`-neuter rule); ⛔ `die Werkzeuge` as a running term, citing the Wave-2 count `Tools : Werkzeuge ≈ 15 : 2–3`; sets of products → `die Tools` | ⛔ **`das Tooling`** bare (no attested gender, Kompositumsbildner class only); appellative → **`die Werkzeuge`**, with three shipped citations | **run 2, and the corpus is decisive.** I re-measured and read the sentences: `Werkzeug(e)` occurs **11×** and **six** of them are precisely slice F's referent — „(Die Werkzeuge – LangSmith, Langfuse, Arize Phoenix, OpenTelemetry …)", „(Die Werkzeuge dafür – Guardrails AI, NeMo Guardrails, Llama Guard …)", „Werkzeuge dafür gibt es. Ragas …", „Werkzeuge gibt es: Ragas …", „Tracing-Werkzeuge setzen Traces … zusammen", „Ein paar Werkzeuge zeigen die wichtigsten Ansätze". **run 1's Wave-2 count is not wrong — it is about a different English word.** `Tool(s)` (219) is the agent-callable tool; `Werkzeuge` (11) is the product you install. Both referents appear on the same Part III pages, so the split is not optional. run 1's `die Tools` for "a set of products" would fuse them |
| **R-2** | **`eval set`** | coins **`die Evaluierungsmenge`**, WEAK, and says openly the compound is unattested; ⛔ `Goldstandard` for the contrasted pair | branch split: frozen = **`der Goldstandard`**, generic/held-out = **`der Datensatz für die Evaluierung`**; ⛔ `Evaluierungsdatensatz` as an unattested compound | **run 2.** §3: *prefer a confirmed incumbent over a coinage.* Neither compound is attested; run 2's periphrasis is built from two settled parts and coins nothing, and the corpus's own construction for a set you measure against is exactly this shape („Red-Teaming braucht einen eigenen **Datensatz** mit Angriffen, eben diese **Menge**, so wie die Evaluierung einen **Goldstandard** braucht"). run 1's thesis-protection (only the frozen one is the Goldstandard) is **kept** — both runs agree on it |
| **R-3** | **`eval` (countable)** | **`das Eval / die Evals`** — the canon Hausform, §1.1.e | **`der Fall / der Testfall`** — measured `Evaluierung` 89 : bare `Eval` **0** over the shipped corpus | **run 2.** I re-measured: bare `Eval` **0**, the only `Eval` string is `Eval-Score` ×2. Six renderers over two waves independently declined the countable form and wrote „neue **Fälle** im Goldstandard". The canon row is **not flipped** (that is stage 2's / the canon owner's call) but it is marked **never-exercised** — see D5. Part III has 86 `eval` occurrences; letting `das Eval` in here would create the incumbent retroactively |
| **R-4** | **`semantic conventions`** | **`die Semantic Conventions`** kept-EN, plural only, with a real heise citation (article- and pronoun-bearing) — run 1 calls it "the best find of the sheet" | **`die GenAI-Konventionen von OpenTelemetry`** as the running form, citation form once; reports **five** shipped names as a live defect | **run 2 for the running form, run 1's find kept as the citation form.** The corpus is *not* consistent here (that is the finding), but the **owning page** uses `GenAI-Konventionen von OpenTelemetry` **3×**, including in its take-away, and it is the only variant that inflects as German. run 1's heise sentence is genuine and licenses the **proper-name citation** („die GenAI Semantic Conventions von OpenTelemetry", shipped ×1) — which I keep, once, at first mention. Part III's actual need is small: 1 prose occurrence + 1 repo path (class 1) |
| **R-5** | **`safety classifier`** | **`der Klassifikator für Sicherheitsrisiken`** (Kopfnomen + Attribut, on the ASR canon precedent); ⛔ `Safety-Klassifikator` (0 Belege) | **`der Safety-Klassifikator`** (English first element durchgekoppelt, on the `Tool-Katalog` pattern); ⛔ `Sicherheitsklassifikator` for the safety/security collapse | **run 1 — narrowly, and it stays OPEN.** Both forms are house calls with zero attestation; both runs reject `Sicherheitsklassifikator` for independent reasons, which is the load-bearing agreement. I chose run 1's because it **coins nothing**, the English apposition already supplies it („a model that scores text for risk categories"), and half the occurrences are already the bare short form. run 2's durchkopplung is regelkonform with a shipped pattern (`Tool-Katalog` 13, `Prompt-Injection` 13, `Guardrails-Schicht` 3) but `Safety-` is 0 shipped as a first element. **Recorded in §7 as a decision, not research** |
| **R-6** | **`red-teaming` — gender/article** | **`das Red-Teaming`**, Neutrum **by rule**, genitive `des Red-Teamings`, HOUSE | **artikellos; OPEN for the article** — BSI writes it parenthetically without an article, heise flexes it only through compounds | **run 1 — and the corpus upgrades it from HOUSE to attested.** The shipped German writes „**ein ernsthaftes Red-Teaming** fährt beides" — `ein …-es` pins **Neutrum** — plus two genitives, „drei Eigenschaften **eines ernsthaften Red-Teamings**" and „Die ASR **eines automatisierten Red-Teamings**". run 2 declared OPEN a row the corpus had already answered; this is the clearest instance in my slice of #328 paying for itself |
| **R-7** | **`red-team` attributive** | **`Red-Team-Läufe`** (mirrors the English base form) | **`Red-Teaming-Läufe`** (heise's attested compound family: `Red-Teaming-Partner`, `Red-Teaming-Anbieters`) | **run 2.** No `Red-Team-` compound is shipped; the only attested German compound family is `Red-Teaming-…`. `Red-Team-` would introduce a second base form of a term the corpus writes one way 11 : 1 |
| **R-8** | **`guardrail` compound first element** | **`Guardrails-`** („Guardrails-Richtlinie", „Guardrails-Prüfung") | **`Guardrail-`** („die Guardrail-Richtlinien") | **run 1, from the corpus.** The shipped compound is **`Guardrails-Schicht`** ×3, i.e. the first element keeps the `-s` |
| **R-9** | **`guardrail` countable singular** | rebuild around **`der Schutzmechanismus`** + pluralising | rebuild around **`die Schutzregel`** + pluralising + head-carrying compounds | **run 2.** `Schutzregeln` is the **corpus's own gloss noun** („Leitplanken – Schutzregeln um das Modell", shipped ×2); singularising it is safe (`die Regel` carries the gender). `Schutzmechanismus` is 0 anywhere and would be a third name. ⚠ Honest caveat: `Schutzregel` is shipped only in the **plural**; the singular is a house singularisation |
| **R-10** | **`integration`** | one word, **`die Anbindung`**, for all senses | split: layer/problem **`die Integration…`**, connector **`die Anbindung`** | **run 2 for the split**, on a shipped sentence carrying both: „Die **Integrationsschicht** besteht aus breiten Bibliotheken fertiger **Anbindungen** – an Modelle, an Tools, an Datenquellen". run 1's ⛔ on the **bare plural `die Integrationen`** is kept |
| **R-11** | **"get those two integrations right"** | → **„diese beiden Nahtstellen"** (the source calls them *seams* two sentences later) | → **„diese beiden Anbindungen"** | **run 1**, on a source reading I verified in the concordance: the same paragraph says „The loop becomes *one system* at two **seams**" |
| **R-12** | **Mermaid `Eval gate (golden set)`** | **`Eval-Gate<br/>(Goldstandard)`** | **`Kontrollpunkt: Evaluierung<br/>(Goldstandard)`** | **Neither, and the row is OPEN cross-slice.** run 1's `Eval-Gate` writes a word that is standing-OPEN; run 2's `Kontrollpunkt` is the canon word but is **0 in the shipped corpus** (`Gate` bare 0, `Gateways` 3, `Freigabe` 4, `Kontrollpunkt` 0). My position: the **decision diamond already is the gate** — label it `Evaluierung<br/>(Goldstandard)` and put the verdict on the edges with the shipped `Freigabe`. Final string belongs to the slice that owns `gate` |
| **R-13** | **H2 „The stack, wired"** | **„Der Stack, verdrahtet"** | **„Der fertig verdrahtete Stack"** | **run 2.** A bare participle is one degree adverb away from the social idiom both runs identified; `fertig verdrahtet` is shipped and is the safe form |
| **R-14** | **`data store` escape hatch** | ⛔ *vier Speichersysteme* (0 Belege) | offers **„vier Speichersysteme"** / „vier getrennte Datenhaltungen" (flagging the latter itself) | **run 1's restraint.** Both source occurrences carry the enumeration (Postgres, ClickHouse, Redis/Valkey, S3/Blob), so the binding works without a second name. Row stays OPEN on `Datenspeicher` |
| **R-15** | **`stack` verb** | „kombinieren / hintereinanderschalten" | „hintereinanderschalten" | **run 2.** „SFT, dann DPO" asserts an **order**; `kombinieren` loses it |
| **R-16** | **`validieren` in running prose** | terminus everywhere | prefer plain **`prüfen`** in prose, reserve `validieren` for where the API name is on screen | **Not a conflict — recorded as a register note.** `validieren`/`die Validierung` remain the terminus (canon §1.1.a, CORPUS 14); `prüfen` stays available as ordinary prose |
| **R-17** | **counts** | `Goldstandard` 31, `Tooling-Ökosystem` 3, `Werkzeugkatalog` 1 | `Goldstandard` 29 (+2 inflected), `Tooling-Ökosystem` 2 | **run 1's counts are right**; run 2 undercounted `Tooling-Ökosystem` by one (`observability/index.md:65`). Same total either way for `Goldstandard` |

**Rows where the two runs agreed and the agreement is worth something** (independent method, plus a
dictionary *and* the corpus): `Nahtstelle`, `Verdrahtung`, `Goldstandard`, `Klassifikator`, `Bibliothek`,
`Einführung`/⛔`Adoption`, `Trace`/`Span`/`Observability`/`Framework`/`Dashboard`, `Judge`, `Bewerter`,
`Validator` (agreement on the ⛔ list is the valuable half).

**Rows where the agreement is worth LESS than it looks:** see `Stack` in the binding table — **THIN×2**,
one tier-3 source per run, no dictionary lemma, no incumbent, and the competing referent (`Stacktrace`)
shipped. No row in this slice rests **entirely on BSI**: run 1's BSI-leaning rows (`Datensatz`,
`Validierung`, `Bibliothek`) and run 2's (`Red-Teaming` spelling) all have an independent corpus or
dictionary counter-check, which I ran. That is reported so nobody re-runs it.

---

## 4. VOCABULARY FOOTPRINT

Deduplicated German content words appearing in my worked sentences and sense cards (stage 2 uses this to
detect cross-slice collisions):

Anbindung · Angriff · Angriffe · Ansätze · Attribute · Aufgabe · Aufnahme · aufnehmen · aufsteigen ·
Aufwand · ausliefern · Auslieferung · Auslöserate · Beispiele · bewerten · Bewerter · Bewertungsmodell ·
Bibliothek · Bindegewebe · blockieren · Dashboard · Datenbestand · Datensatz · Datenspeicher · Dienst ·
einbinden · einführen · Einführung · eingefroren · Eingabe · Entscheidung · erzeugen · Evaluierung ·
Fall · fangen · festlegen · Frameworks · Freigabe · freigeben · Goldstandard · Guardrails ·
hintereinanderschalten · Inhalte · instrumentieren · Instrumentierung · Judge · Kategorie · Klassifikator ·
Klassifikatormodelle · Konnektoren · Konventionen · Kostendashboards · lügen · Mandanten · Menge ·
Metriken · Modell · Modellaufruf · nachgezogen · nachtrainiert · nachverfolgen · Nahtstelle · Nahtstellen ·
null · optimieren · orchestrieren · Pipeline · Plattform · Produktivbetrieb · Prompt-Management ·
Prompt-Registry · protokolliert · Prüfung · Quere · Red-Teaming · Referenzdatensatz · Regel ·
Regressionen · Registry · Reihe · repräsentativ · Risikokategorien · sauber · Schicht · Schleife ·
Schnittstelle *(as the ⛔ contrast only)* · schreiben · Schutzregel · Schwellenwert · Score ·
Sicherheitsrisiken · Sitzungsisolierung · Skalierung · Span · Spans · Stack · Stichprobe · System ·
Testfall · Token · Trace · Traces · Training · Übergabe · Übereinstimmung · umsetzen · validieren ·
Validierung · Validator · Validatoren · verdrahten · verdrahtet · Verdrahtung · vereinheitlichen ·
verfolgen · vergeben · Verkehr · verrauscht · versorgen · Werkzeug · Werkzeuge · Wirklichkeit ·
zurückhalten · zusammenhalten · zusammenwachsen

**Collision candidates I can already name for stage 2** (a word my slice uses that another slice is likely
to want for a different referent): **`Werkzeug(e)`** (wave 1 collided on exactly this string — my slice binds
it to *tooling/products*, **not** to *tools*), **`Menge`** (I use it only in „die Menge der Beispiele";
slice-level `set`/`budget` work may want it), **`Prüfung`** (I use it for *check*; the `gate` owner may want
it for *to gate*), **`Freigabe`** (same), **`Schicht`**, **`Dienst`**, **`Fall`** (I bind it to the countable
eval case), **`Instrumentierung`** (already resolved; I only consume it), **`Registry`**, **`Stack`**,
**`Anbindung`**.

---

## 5. SPREAD — which of the 10 Part III files each term occurs in

Files abbreviated: `ov`=overview · `pf`=production-failures · `sv/i`,`sv/d`=serving · `cp/i`,`cp/d`=cloud-platforms ·
`te/i`,`te/d`=tooling-ecosystem · `lo/i`,`lo/d`=llmops.

| Terminus | n | files | which |
|---|---|---|---|
| **guardrail** | 81 | **10** | all ten |
| **tooling** | 40 | **9** | ov, pf, sv/i, cp/i, cp/d, te/i, te/d, lo/i, lo/d |
| **observability** | 57 | **9** | ov, pf, sv/i, sv/d, cp/d, te/i, te/d, lo/i, lo/d |
| **tooling ecosystem** | 31 | **8** | ov, pf, sv/i, cp/i, cp/d, te/i, te/d, lo/i |
| **eval** | 86 | **7** | ov, pf, cp/i, te/i, te/d, lo/i, lo/d |
| **trace** | 36 | **6** | pf, sv/i, te/i, te/d, lo/i, lo/d |
| **stack** | 10 | **4** | cp/d, te/i, te/d, lo/i |
| **framework** | 9 | **4** | sv/i, cp/d, te/i, te/d |
| **safety** | 12 | **4** | cp/i, cp/d, te/i, te/d |
| **golden set** | 23 | **4** | te/i, te/d, lo/i, lo/d |
| **judge** | 19 | **4** | pf, te/i, te/d, lo/i |
| **dashboard** | 7 | **4** | pf, te/i, te/d, lo/d |
| **dataset** | 9 | **4** | pf, te/i, te/d, lo/d |
| **OpenTelemetry** | 14 | **4** | cp/d, te/i, te/d, lo/d |
| **validator** | 27 | **3** | pf, te/i, te/d |
| **classifier** | 10 | **3** | te/i, te/d, lo/i |
| **span** | 12 | **3** | te/i, te/d, lo/d |
| **integration** | 4 | **3** | cp/i, te/i, te/d |
| library 6 · wiring 6 · red-teaming 12 · semantic conventions 2 · prompt management 2 · eval set 5 · grader 7 | | 2 | — |
| seam 4 · data store 2 · adopt 2 · adoption 2 | | 1 | te/d (seam, data store), te/i (adopt/adoption) |
| annotation 0 · experiment tracking 0 | | 0 | — |

**Terms spanning ≥3 files — ONE binding string must be decided centrally** (18 of them):
`guardrail`, `tooling`, `observability`, `tooling ecosystem`, `eval`, `trace`, `stack`, `framework`,
`safety`, `golden set`, `judge`, `dashboard`, `dataset`, `OpenTelemetry`, `validator`, `classifier`,
`span`, `integration`.

Of these, the four whose binding string is **not** already fixed by the shipped corpus, i.e. the ones a
central decision actually has to make, are **`tooling`** (resolved here to `die Werkzeuge` — highest traffic
in the slice), **`stack`** (THIN×2), **`safety`** (three referents, no clean source), and **`validator`**
(genitive derived).

---

## 6. CANON DELTA — reported, never edited

| # | File · section | Current text | Proposed | Reason |
|---|---|---|---|---|
| **D1** | `_language.md` §1.3.3, „**Verbindliche Schreibungen für dieses Korpus**" | „- **Golden Set** (Adj+Subst, § 37 E4) — aber **Golden-Set-Pflege**" | replace the example with `Hybrid Search` / `Late-Chunking-Verfahren` (both already stand beside it) | The loan is **struck twice** in `rag.md` §2, but it survives here **inside a rule section headed "binding spellings"**. A renderer that reads the rules and skips the struck boxes finds a **licence** to write `Golden Set`. This is the most plausible mechanism of the Wave-2 regression, and it is still armed. *(Raised by run 1; I confirm it is the only place in the chain that can produce the defect without anyone making a mistake.)* |
| **D2** | `rag.md` §2, the „*the list above is in CITATION form*" paragraph | „*adjective + noun → may stay spaced and capitalised (**Golden Set**, Hybrid Search, …)*" and „*Durchkopplung is obligatory: **Golden-Set-Pflege**, …*" | same substitution as D1 | Same residue, same mechanism, and §2 tells the reader „When in doubt, look up §1.3.3" — the two reinforce each other |
| **D3** | *(generalisation of D1/D2)* | — | **grep `_language.md` §1.3.3 and `rag.md` §2's citation-form paragraph against EVERY struck §2 row**, not only mine | `Error Budget`, `Latency Budget`, `Scratchpad`, `Super-Step` were struck in the same shape. The baseline shows the first three are currently clean **in the corpus** — this delta is about the **rules**, which is where the regression is authored |
| **D4** | `rag.md` §2 vs `rag.md` §3 / `_language.md` §1.1.e — `Grader` | §2 lists `Grader` under „Settled as kept-EN (class 2)"; §3 and §1.1.e hold it **OPEN, zero German attestation**, Korpusform *der Bewerter* | scope §2's entry explicitly to **the API name** (`model graders`), and record that the corpus has now shipped **`der Bewerter` 11× incl. the genitive `des Bewerters`** | Two canon locations disagree about the same row. §3/§1.1.e carry the evidence; §2 carries only the mention. Part III needs the word 7×, 6 of them appellative |
| **D5** | `_language.md` §1.1.e, `Evaluierung / Eval` row | „*die Evaluierung* für den Vorgang, *das Eval / die Evals* nur für den zählbaren Testfall" (gender declared as Analogie) | mark the second half **NEVER-EXERCISED** and name the corpus form **`der Fall`** | Measured: `Evaluierung*` **90**, bare `Eval` **0** across 27 pages; the only `Eval` string is `Eval-Score`. Six renderers over two waves declined the countable form. Part III is the densest `eval` slice in the project and would create the incumbent retroactively |
| **D6** | `_language.md` §1.1 — **no `Registry` row** | — | add: **`die Registry`**, die Registrys, der Registry — **feminine, corpus-attested** | Both runs reported the gender as an unrecorded gap. The corpus had already settled it: „In **einer** Registry gelistet zu sein ist keine Prüfung" ×3, „**Eine** Registry veröffentlicht Metadaten", „**Die** offizielle MCP-Registry". Needed for `die Prompt-Registry` (Part III) and `die MCP-Registry` (Part II) |
| **D7** | `_language.md` §1.1.f, `Red-Teaming` (in the *Spotlighting · Delimiting · …* collective row) | genus derived **from the `-ing` rule**, stated openly as not from a Beleg | upgrade to **corpus-attested Neutrum**: „**ein ernsthaftes Red-Teaming**", genitive „eines ernsthaften / automatisierten **Red-Teamings**" ×2 | The rule turned out to be right and the corpus now proves it. Leaving it as HOUSE caused run 2 to re-open a settled row |
| **D8** | `rag.md` §8, Phase 6 metaprose | „*und Teil III ist die Lektion über das **Werkzeug-Ökosystem** (Ragas, DeepEval, LangSmith …)*" | „*das **Tooling-Ökosystem***" | `Werkzeug-Ökosystem` is **0** in the shipped German; three published forward references already call the lesson `Tooling-Ökosystem`. The metaprose is a description, not a ruling, and it is the only thing standing behind the other name. ⚠ This does **not** touch the Wave-2 ruling that `Werkzeugkatalog` (products) and `Tool-Katalog` (an agent's registered tools) are two referents with two names |
| **D9** | **Shipped Part I defect — neither run saw it.** `part-1-rag/cross-cutting/guardrails/index.md` | „…sind eine eigene Schicht, und die behandelt **[die Lektion über das Tool-Ökosystem]**(…/part-3-production/tooling-ecosystem/index.md)" | „**die Lektion über das Tooling-Ökosystem**" | The shipped corpus has **three** German names pointing at this one Part III page: `Tooling-Ökosystem` **3**, `Tool-Ökosystem` **1**, plus `Werkzeugkatalog` **1** as a content description. `Tool-Ökosystem` is the odd one out and it also collides with the `Tool-` = *agent tool* binding. **Reported, not repaired** — the page is outside my slice |
| **D10** | **Shipped Part II defect.** `part-2-agents/multi-agent/deep-dive.md` | „Sie zahlen für das Routing und **die Verkabelung**" | „… und **die Verdrahtung**" | One referent, two names, already shipped: `Verdrahtung`/`verdrahten` **11 forms** vs `Verkabelung` **1**. DWDS puts the two verbs in one synonym group, so neither is wrong — which is exactly the Richtungswackeln condition. Part III must use only `Verdrahtung`. *(Raised by run 2; I confirm the counts.)* |
| **D11** | **Shipped Parts I/II — the OTel GenAI conventions carry five names** | „die **GenAI Semantic Conventions** von OpenTelemetry" 1 · „die **GenAI Conventions**" 2 · „die **GenAI-Konventionen von OpenTelemetry**" 3 · „die **semantischen Konventionen** von OpenTelemetry für GenAI" 1 · „die **GenAI-Instrumente** von OTel" 1 | running form **„die GenAI-Konventionen von OpenTelemetry"**; keep the full English proper name **once** as the citation form; keep `Semantic Conventions v1.41.x` as the **version** citation | The owning page uses form 3 three times including in its take-away, and it is the only variant that inflects as German. Part III must not add a sixth. **Reported, not repaired.** *(Raised by run 2; I re-measured and confirm the five.)* |
| **D12** | **No §1.1 row exists** for: `Validator` (WEAK, genitive derived), `Klassifikator` (SETTLED, corpus ×5), `Nahtstelle` (SETTLED, DWDS + corpus ×2), `Verdrahtung` (SETTLED + degree-adverb prohibition), `Stack` (**THIN×2**, "nie nackt"), `Ökosystem` (SETTLED, DWDS IT sense + corpus ×10), `Datenspeicher` (WEAK/OPEN), `Anbindung` (corpus Usus), `Bibliothek` (**Fallenkasten** — Duden has no EDV sense), `Datensatz` (**Fallenkasten** — Duden gives the *record*), `Guardrail` singular (**OPEN**), `Prompt-Management` (rule-built) | — | add rows with the paradigms and evidence grades from §1 above | Both runs produced substantially the same gap list independently; the differences are recorded in §3 |

---

## 7. NEEDS A DECISION, NOT MORE RESEARCH

**7.1 · `safety classifier`.** Two constructions, both defensible, **neither attested**, and more attestation
will not arrive: the one German compound that exists (`Sicherheitsklassifikator`) is MT-disqualified on two
independent counts, and it is the form **both runs reject**. Somebody must simply rule between
`der Klassifikator für Sicherheitsrisiken` (coins nothing; canon's ASR precedent) and
`der Safety-Klassifikator` (shorter; shipped durchkopplung pattern).
**Recommendation:** the periphrasis, with the bare short form thereafter.
**Cost of being wrong: low.** 6 occurrences, 2 files, both forms decodable, and the short form carries half
of them either way. The expensive error is the third option, `Sicherheitsklassifikator`, which collapses
*safety* and *security* on pages that carry both — and that one is already closed.

**7.2 · `der Datenspeicher` for running services.** Duden and DWDS both define the **medium**; our referent is
Postgres, ClickHouse, Redis/Valkey and S3/Blob — four **services**. No German source will settle this,
because the English term is itself loose. **Recommendation:** hold `der Datenspeicher`, require the
enumeration within reach (both source occurrences have it), and do **not** add a second name.
**Cost of being wrong: low-to-medium** — an H1 that reads slightly off to a native ear. It is 2 occurrences
on 1 file, but one of them is that file's **H1**.

**7.3 · `der Stack` — accept a THIN×2 row or restructure around it.** No dictionary lemma exists in either
Duden or DWDS, the shipped corpus has **zero** free `Stack` and ships `Stacktrace`, and both runs landed on
one tier-3 source each. **Recommendation:** accept `der Stack` **with the obligatory first-mention binding on
every page** (4 files), and treat the genitive `des Stacks` as derived. The alternative — restructuring 10
occurrences plus an H1 around „die Reihe der Werkzeuge" — costs more than the risk.
**Cost of being wrong: medium.** A reader who takes the LIFO reading at an H1 loses the page's thesis; the
binding gloss is what buys that back, so **the gloss is not optional**.

**7.4 · The `Werkzeuge` (tooling) ↔ `Tools` (agent tools) split must be ratified centrally.** It touches 9 of
10 Part III files and it reverses one run outright. It is corpus-grounded (11 : 219, and the eleven are all
our referent), but if stage 2 rules the other way, every file changes.
**Cost of being wrong: high** — this is the single highest-traffic string in the slice.

**7.5 · The Mermaid gate label.** Not mine to bind (`gate` is standing-OPEN, cross-slice). Somebody must
either ratify "the diamond is the gate" or give the renderers a word. **Cost of being wrong: low per
occurrence, high per class** — diagram labels are the one text unit a prose gate does not read, which is
where **both** Wave-2 `golden set` regressions and **both** of this slice's riskiest occurrences sit
(`GS["Golden set"]` and `EG{"Eval gate<br/>(golden set)"}`). Run 2's procedural recommendation is worth
adopting whatever the label ends up being: **the Part III gate should grep the rendered German for `Golden`
and `golden` inside `[mermaid]` blocks and treat a hit as a hard failure.**

---

## 8. WHAT THIS PASS COULD NOT DO

1. **The blind spot both runs share — and I inherit it.** Both runs read the same concordance, the same canon
   and the same shipped corpus, and I added a *third* read of that corpus. Where the **corpus itself is
   wrong**, all three of us agree with it confidently. D9, D10 and D11 prove that is not hypothetical.
   The rows that are strong **only because they shipped** are **`Tooling-Ökosystem`** and **`Datensatz`** —
   both would fall to WEAK if the shipped pages were discounted. `Nahtstelle` (DWDS figurative sense) and
   `Verdrahtung` (Duden lemma) also stand without the corpus; `Werkzeuge` stands on ordinary German.
2. **No native speaker and no independent model read the proposed sentences.** All collocation checks
   (`Naht`, `verdrahtet`, `Adoption`, `Späne`) ran against dictionaries. A **register** trap — right
   definition, wrong Wortprofil — survives a dictionary check. The highest residual risk of that kind in my
   slice is **`die Nahtstelle`** (Duden/DWDS definition is exact, but the Wortprofil is welding and
   administrative boundaries) and **`der Klassifikator für Sicherheitsrisiken`** (long, and nobody has heard
   it said aloud).
3. **The genitives `des Validators` and `des Stacks` are derived, not cited.** `Validator` inherits a
   well-defined class (`-or` agent nouns, settled for `der Annotator`); `Stack` inherits nothing but the
   regular `-s`. *What would close them:* one sentence at heise / iX / INNOQ / dpunkt or in university
   material.
4. **The EU AI Act in German was not read** (run 2's fetches returned empty bodies). It is the obvious tier-1
   source for `Datensatz`, `Annotation`, `Validierung` and — decisively — the *safety* vs *security* split
   that 7.1 turns on. **Still the single most valuable follow-up on this slice.**
5. **`die Funktionstrennung` is 0 in the shipped Parts I + II.** It is on the no-regress list but it is not a
   slice-F referent and I did not rule on it. **Do not read my silence as confirmation** — somebody should
   check where that string actually lives before a renderer is told it is an incumbent. (The other
   no-regress strings I *did* confirm in the corpus: `Goldstandard` 31, `der Bewerter` 11,
   `die Bewertungsfunktion` 5 — **and they are two different referents**, `die Instrumentierung` 1 +
   `instrumentieren` 3, `das Fehlerbudget` 4, `der Dienst` 12, `die Fähigkeit` 19, `die Vertrauensgrenze` 3,
   `das Geheimnis` 7, `das Prinzip der geringsten Berechtigungen` 18.)
6. **I did not verify the shipped Part I/II repairs** implied by D9, D10 and D11. Those pages are outside my
   slice, and per the Wave-2 `Werkzeugkatalog` lesson a pass that only counted should not reach into a file
   it has not read in full. Each is reported with counts and a quoted sentence so somebody who *has* read the
   file can act.
7. **What the doubling could not buy here.** `Stack` and `das Tooling` were the two rows where a second blind
   run was structurally certain to hit the same wall — no dictionary lemma exists, so both runs were always
   going to reach for the same thin tier-3 evidence. On `das Tooling` the **corpus** broke the tie; on
   `Stack` nothing did, and it is labelled **THIN×2** so no renderer reads two runs as two checks.
