# LEDGER-A — Gate 6.5 stage 1, slice A (serving mechanics, runtime, compute)

**Scope:** the 10 English files of `docs/part-3-production/`.
**Inputs read in full:** `OUT-A-run1.md` (355 lines), `OUT-A-run2.md` (333 lines), `dewave3-concord-A.txt`,
`REFERENTS-baseline-verdicts.md`, `_language.md` §1.1/§1.3.3, `rag.md` §2/§3/§8 Phase 3 §D.
**New evidence raised here:** a full pass of the **27 shipped German pages** (issue #328) — it settles seven
rows the two runs left WEAK or hunted for externally, and it **overturns the brief's own count** on `Laufzeit`.
Nothing in the worktree was touched; no git was run.

---

## 0. The three things stage 2 should read even if it reads nothing else

1. **`Laufzeit` for `runtime` — slice A's position (§6 of the brief).** The row splits **three ways**, not two,
   and the split is anchored in a native German sentence about the exact product Part III names. Bare
   `die Laufzeit` as a component name stays **banned**; `die Laufzeitumgebung` is **released** for the
   host-platform referent (the canon's own §D text calls `Laufzeitumgebung` "die JVM/CLR-Klasse Wirtsplattform"
   — which is *precisely* what a managed agent runtime is); `Runtime` stays **Klasse 1** inside vendor
   component names. **The brief's premise is measurably overstated:** the component sense ships **5 times in
   2 files**, not "six shipped German pages". Detail in §1, §3-D1 and §6.
2. **Both runs shipped a metaphor the wave has already banned.** Run 1 and run 2 *independently* wrote
   „der KV-Cache … **ist die eigentliche Decke**" for *the ceiling*. The brief rules `die Decke` out
   (*durch die Decke gehen* points the opposite way). Two blind runs converging on a banned string is the
   agreement-is-not-verification shape in its purest form. **Ruling: ⛔ `die Decke`; use
   „setzt die eigentliche Grenze" / „ist der eigentliche Engpass".** See §3-D9.
3. **The shipped corpus already holds the paradigms both runs went looking for and could not find.**
   `der Worker` ships with **genitive singular** („der Span jedes **Workers**") and **dative plural**
   („bei ungleichartigen **Workern**") — run 1 wrote „Wer diese Zeile hochstuft, braucht einen deutschen Satz
   mit *des Workers* … Ich habe keinen gefunden." It is in our own delivered German. Same for `der Durchlauf`
   (43 case-marked instances, `ein Lauf` = **0**), `die Parallelität`, `der Batch`, `der Durchsatz`.

---

## 1. Binding table

`Class`: 1 = identifier / product name · 2 = kept-EN loan with German article · 3 = German-led (first-mention
gloss where marked) · 4 = fully German, no gloss.
Counts in the German column are **my grep over the 27 shipped German pages**; EN counts come from the
concordance, re-measured by both runs.

| Terminus | German | Class | Status | Artikel / Plural / Genitiv | Kollokation | ⛔ rejected | Evidence grade |
|---|---|---|---|---|---|---|---|
| **runtime** (a) host platform | **die Laufzeitumgebung**, Anapher **die Umgebung**; Erstnennung **die verwaltete Agenten-Laufzeitumgebung** | 3 | **BOUND** (canon §D narrowed to its actual referent — report only, §6) | die Laufzeitumgebung / die Laufzeitumgebungen / der Laufzeitumgebung | „die Laufzeitumgebung **führt die Agentenschleife aus** / **betreibt** sie"; ⛔ „hält" | ⛔ **bloßes `die Laufzeit` als Bauteilname** (§D holds); ⛔ *die Agentenlaufzeit* (de.wikipedia insource 0, a canon coinage); ⛔ *das/der Runtime* | **RECONCILED** (run1 wanted `die Runtime` as head, run2 `die Laufzeitumgebung`; I chose run2's head + run1's release argument) + 4 independent houses, 2 in-domain |
| **runtime** (b) vendor component | **Runtime** (`AgentCore Runtime`), artikellos im Namen, sonst **die Runtime** | 1 / 2 | **BOUND** | die Runtime / die Runtimes / der Runtime | „**Die Runtime** gibt Ausführungsfenster von bis zu acht Stunden" | ⛔ übersetzen des Produktnamens | **AGREED×2**, and the bigdata-insider sentence covers this exact product |
| **runtime** (c) temporal | **zur Laufzeit** | 3 | **CORPUS PRECEDENT** | adverbial | „**zur Laufzeit** durchsetzen"; „Laufzeit statt Entwurfszeit" | ⛔ nothing — the row was never in dispute | **CORPUS(8)** — 8 correct temporal uses across 4 shipped pages |
| **run / runs** — countable | **der Durchlauf** | 3 | **CORPUS PRECEDENT** | der Durchlauf / die Durchläufe / **des Durchlaufs** | „einen Durchlauf **anstoßen / starten**"; „ein Durchlauf **bricht ab / endet**"; „**mitten im Durchlauf**" | ⛔⛔ **„ein Lauf"** (Duden `Lauf` = Sport/Fluss/Maschine + „einen Lauf haben"); ⛔ *der Run* (Duden = Ansturm); ⛔ „einen Durchlauf **fahren**" | **CORPUS(43 case-marked)** — 11 *ein D.*, 9 *der D.*, 8 *den D.*, 4 *im D.*, 3 *eines Durchlaufs*, 2 *des Durchlaufs*, 2 *Durchläufen*, 2 *Durchläufe*; **`ein Lauf` = 0**. Plus run2's Duden EDV sense |
| **run** — betreiben | **betreiben** (Akk.); Selbstbetrieb **selbst betreiben** | 3 | **BOUND** | verb | „eine eigene Queue **betreiben**"; „Sie haben **keine Worker zu betreiben**" | ⛔ *laufen lassen* (= gewähren lassen) | **AGREED×2** + heise title „KI-Modelle produktiv **betreiben**" (already cited by canon §1.1.d) |
| **run** — 4 further senses | see Sense card **SC-R** | 3 | **BOUND** | — | laufen auf · ausgehen/aufgebraucht sein · greift zuerst / zieht sich durch · die laufenden Kosten | ⛔ überall `laufen` schreiben (the strongest surviving translation trace) | **AGREED×2** (branch inventories differ by one; merged) |
| **worker** | **der Worker** — **nie nackt bei Erstnennung** | 2 | **CORPUS PRECEDENT** (upgrades canon's WEAK) | der Worker / **die Worker** / **des Workers**; Dat. Pl. **den Workern** | „ein Worker **zieht** aus der Queue"; „**bestätigt erst nach der Ausführung**"; „ein Worker **fällt** mitten im Auftrag **aus**"; „**den Worker-Pool aufstocken**" | ⛔ „die Workers"; ⛔ *der Arbeitsprozess*; ⛔ *der Arbeiter*; ⛔ „ein Worker **stirbt**" (personifiziert) | **CORPUS(43)** incl. „der Span **jedes Workers**", „bei ungleichartigen **Workern**", „gibt **jedem Worker** einen Anteil" |
| **Langfuse Worker** | **`Worker`** (Produktkomponente neben *Web*, *Postgres*, *ClickHouse*) | 1 | **BOUND** | artikellos / Auszeichnung trägt die Unterscheidung | „der **`Worker`**-Dienst von Langfuse" | ⛔ Kleinschreibung als Appellativ auf derselben Seite | **RECONCILED** (run2 only; run1 missed the proper-name sense) |
| **event loop** | **der Event-Loop** | 2 | **OPEN (incumbent held: `der`; closes when a second house outside informatik-aktuell writes a case-marked `den/des Event-Loops` — or when INNOQ's feminine is confirmed in a second house)** | der Event-Loop / die Event-Loops / **des Event-Loops** | „den Event-Loop **blockieren**"; „die Kontrolle **an den Event-Loop zurückgeben**"; „er **verzahnt** Hunderte wartender Anfragen"; „**Blockieren Sie niemals den Event-Loop.**" | ⛔ **einfrieren** (see own row); ⛔ *die Ereignisschleife* als Laufterm (0× im einschlägigen nativen Artikel); ⚠ **die** Event-Loop is *attested* but loses on canon consistency | **RECONCILED — a frontal gender split.** run1: INNOQ **die** ×4. run2: informatik-aktuell **der**, case-marked ×4 incl. genitive. I chose **der**: it is the case-marked evidence, and the canon already licenses **`der Loop`** (Duden, echter EDV-Sinn, §1.1.g rejection note) — a `der Loop` / `die Event-Loop` switch on one page is §1.1 wobble |
| **blocking call** | **ein blockierender Aufruf** | 3 | **BOUND** | der blockierende Aufruf / die blockierenden Aufrufe | **blockieren + Akk.**; Reparatur: „den Aufruf **in einen Thread auslagern**" | ⛔ *ein Blocking Call*; ⛔ *ein blockender Aufruf*; ⛔ *sperrender Aufruf* (`sperren` ist §1.1.f für Token-Masking vergeben) | **AGREED×2** + **CORPUS(5)** — `blockieren` ships 5× in the German, `einfrieren` 0× |
| **freeze** (the loop / requests) | **blockieren** — never *einfrieren* | 3 | **BOUND** | — | „**blockiert jede Anfrage in diesem Prozess**" | ⛔⛔ **einfrieren** — DWDS's dominant transitive sense is *Löhne/Guthaben einfrieren* = **aussetzen, sperren**: it asserts a **deliberate** act. A blocking call is not a decision to suspend anything. **This is a factual error, not a style one** | **AGREED×2**, independently reasoned (run1 from the sense field, run2 from DWDS) — one of the few AGREED×2 rows here that is worth its label |
| **concurrency** (property) | **die Nebenläufigkeit**; im Regelfall **adverbial**: *nebenläufig ausführen*, *die nebenläufige Ausführung* | 3 | **CORPUS PRECEDENT (adverbial) / BOUND (noun)** | die Nebenläufigkeit / kein Plural / der Nebenläufigkeit | „**nebenläufig ausführen**"; „**nebenläufige Worker**"; Substantiv nur im Kontrastsatz | ⛔ *die Concurrency*; ⛔ *die Gleichzeitigkeit* als Terminus; ⛔ *der Nebenlauf* | **CORPUS(16 adverbial, 0 noun)** — the shipped German never nominalises it. run1 graded WEAK (Duden/DWDS 404), run2 SETTLED (de.wikipedia lemma); **the corpus resolves it: the adjective is the incumbent, the noun is the exception** |
| **concurrency** (a number / cap) | **die Zahl gleichzeitiger Anfragen** · **Obergrenzen für gleichzeitige Generierungen** | 3 | **BOUND** | — | „die Nebenläufigkeit **begrenzen/beschränken**"; „**zweihundert gleichzeitig in Bearbeitung**" | ⛔ „eine große Nebenläufigkeit", „die Nebenläufigkeitsdecke" — the German noun is a **property**, not a counter; ⛔ *kappen* (§1.1.a: abruptes Abschneiden) | **AGREED×2** (both runs split the sense independently — the strongest agreement on the sheet) |
| **parallelism** | **die Parallelität** | 3 | **CORPUS PRECEDENT** | die Parallelität / (Plural meiden) / der Parallelität | „**Parallelität auf Prozessebene**"; „**Parallelität über mehrere GPUs und Knoten**" | ⛔ **der Parallelismus** (im Deutschen die **Stilfigur** — echter falscher Freund im Nachbarfach) | **CORPUS(5)** — „die Parallelität von weiter oben", „aufteilen … für Parallelität", Abschnittslabel „**Parallelität.**"; `Parallelismus` = 0 |
| the three sharding strategies | **die Tensor-Parallelität · die Pipeline-Parallelität · die Daten-Parallelität** | 3 | **OPEN (incumbent held: hyphenate all three; closes when the wave rules on German-first-element compounds — see §7-N3)** | je feminin, Genitiv *der …-Parallelität* | „**Tensor-Parallelität innerhalb eines Knotens, Pipeline-Parallelität über Knoten hinweg**"; Erstnennung mit englischer Klammer | ⛔ undurchgekoppelt („die Tensor Parallelität") | **RECONCILED** (run1: all three hyphenated; run2: *Datenparallelität* solid). I chose the **uniform hyphen**: the three names appear as a set in the same sentence and a mixed set reads as an error. **HOUSE, flagged.** |
| **throughput** | **der Durchsatz** | 3 | **CORPUS PRECEDENT** | der Durchsatz / die Durchsätze / des Durchsatzes | „**mit hohem Durchsatz laufen**" (corpus); „**Durchsatz erkaufen / verschenken**"; „**Durchsatz gegen Qualität eintauschen**" | ⛔ *der Throughput* | **CORPUS(3)** + canon §1.1.a (Duden, expliziter EDV-Sinn) + **AGREED×2** |
| **Provisioned Throughput / PTU** | unübersetzt | 1 | **BOUND (ALREADY RESOLVED, rag.md §2)** | artikellos | „Azure verkauft sie als PTU, Vertex als **Provisioned Throughput**" | ⛔ *bereitgestellter Durchsatz* — that would invent a product name | given; both runs concur |
| **batching** (generic) | **das Batching** | 2 | **HOUSE (genus rule-derived, not attested)** | das Batching / kein Plural / des Batchings | Vorgang verbal: „**zu einem Batch zusammenfassen**" (⚠ nie nacktes *zusammenfassen* — liest als *summarize*) | ⛔ *batchen* (§1.3.2 OPEN, 0 Belege) | **AGREED×2 — but zero evidence.** Both runs applied the same `-ing`→Neutrum canon rule; that is one derivation counted twice, not two data points. Label **HOUSE**, not settled |
| **continuous / static batching** | **das Continuous Batching** (gespreizt, Adj+Subst) · **das statische Batching** | 2 | **BOUND (kept-EN by rag.md §2)** | wie oben | „**Continuous Batching ist im Kern Scheduling auf Iterationsebene**"; „**statisches Batching lässt den ganzen Batch auf sein langsamstes Mitglied warten**" | ⛔ *kontinuierliches Batching*; ⛔⛔ **die Stapelverarbeitung** hier — das ist der **Batch-Tarif** der Cloud-Lektion, und der Korpus warnt zweimal selbst vor genau dieser Verwechslung | **AGREED×2** + corpus ships `der Batch` and the phrase „**zu einem Batch zusammenfassen**" |
| **prefill / decode** | **nur gebunden**: die **Prefill-Phase**, die **Decode-Phase**, der **Decode-Schritt**, das **Chunked-Prefill-Verfahren**; koordiniert artikellos „Prefill und Decode" | 2 | **OPEN (incumbent held: Kompositumsbildner, kein freier Artikel; closes when a German house prints „des Prefills" / „beim Prefill" with an article)** | — (bewusst kein Genus geprägt) | „**In der Prefill-Phase wird der gesamte Prompt in einem Durchlauf verarbeitet; sie ist rechenlastig.**" · „**In der Decode-Phase entsteht je Schritt ein Token; sie ist durch die Speicherbandbreite begrenzt.**" | ⛔ „das/der Prefill" (kein attestiertes Genus); ⛔ *das Vorbefüllen* / *die Vorbefüllung*; ⛔ *die Dekodierung* (durch **Constrained Decoding** besetzt) | **AGREED×2**, both refusing to coin — precedent `Retry`/`Backoff`, `_language.md` §1.1 Kompositumsbildner-Kasten |
| **KV cache** | **der KV-Cache** | 2 | **BOUND (Genus vom belegten Kopf `der Cache`)** | der KV-Cache / die KV-Caches / **des KV-Caches** | „**KV-Cache-Blöcke belegen**"; „**der KV-Cache-Pool**"; „Blöcke **lassen sich gemeinsam nutzen**"; „**der KV-Cache füllt sich**" | ⛔ „KV Cache" getrennt (§45 E1); ⛔ *der Schlüssel-Wert-Cache*; ⛔ Genuswackeln „das KV-Cache"; **⛔ „ist die eigentliche Decke"** → „**setzt die eigentliche Grenze**" / „**ist der eigentliche Engpass**" | **AGREED×2** for the form; **the collocation is a REVERSAL of both runs** (§3-D9) |
| **prefix caching** | **das Prefix-Caching** (Bindestrich) | 2 | **BOUND — Schreibung korrigiert gegen die Zitierform** | das Prefix-Caching / — / des Prefix-Cachings | „**Prefix-Caching setzt an derselben Wiederholung von der anderen Seite an.**" | ⛔ *das Präfix-Caching*; ⛔ *das Präfix-Zwischenspeichern* | **RECONCILED** (run1 hyphen, run2 spaced). run1 wins on grammar: `prefix` is a **Substantiv** → §45 E1 / §1.3.3(b). run2 misanalysed it as Adj+Subst. Cross-check: `Continuous`/`Chunked`/`Late` **are** adjectives → those stay spaced. Internally consistent |
| **paged attention** | **PagedAttention** (Verfahrensname) · beschreibend: **ein in Seiten verwalteter KV-Cache** | 1 / 3 | **BOUND** | artikellos | „**PagedAttention hält den KV-Cache in Blöcken fester Größe, so wie ein Betriebssystem den Arbeitsspeicher in Seiten verwaltet.**" | ⛔ *die geseitete Aufmerksamkeit*; ⛔ *seitenbasierte Attention*; ⛔ *seitenweise verwaltet* (run1's form — `seitenweise` kommt im de.wikipedia-Lemma *Paging* **0×** vor) | **RECONCILED** — both runs found the concordance's printed `0` to be a **narrowing-matcher artefact** (the corpus writes the CamelCase name, 5×, plus 1 adjectival `a paged KV cache`). I chose run2's descriptive phrase on evidence |
| **inference server / engine** | **die Inferenz-Engine** — Erstnennung mit Klammerglosse *(inference server)* | 2 | **OPEN (incumbent held: `die Inferenz-Engine`; closes when a house outside Heise Medien — INNOQ, dpunkt, Fraunhofer, Hochschule — prints it, or prints a case-marked *Inferenzserver*)** | die Inferenz-Engine / die Inferenz-Engines / der Inferenz-Engine | „**Die Inferenz-Engine hält das Modell, FastAPI hält das Produkt.**"; „der **Scheduler der Inferenz-Engine**"; ⛔ „besitzt die GPU" → „**verwaltet die GPU**" / „**die GPU liegt bei der Inferenz-Engine**" | ⛔ **der Inferenzserver** — **run2's own coinage, with a measured triple zero** (de.wikipedia insource: `Inferenzserver` 0, `Inference Server` 0, `Inferenz-Server` 0); ⛔ *der Inference Server*; ⚠ *der KI-Server* ist attestiert, aber unschärfer | **RECONCILED — the sharpest disagreement on the sheet.** run1: attested `die Inferenz-Engine` (heise + iX, one of them definitional). run2: coined `der Inferenzserver`, explicitly *nicht belegt*. **Brief §3: a confirmed incumbent beats a coinage.** ⚠ Still **THIN**: heise+iX are **one** Stilfamilie counted twice (run1 says so itself) |
| **GPU** | **die GPU** — Erstnennung „die **GPU** (der Grafikprozessor)" | 2 | **THIN×2 (form held)** | die GPU / die GPUs / der GPU (Gen./Dat.) | **auslasten + Akk.** („kann die GPU nicht auslasten"); „**ein Modell über mehrere GPUs verteilen**"; „**Auf Kubernetes ist eine GPU eine ganzzahlige Ressource**"; Komposita durchgekoppelt: die **GPU-Auslastung**, der **GPU-Speicher**, der **GPU-Scheduler**, die **GPU-Stunde** | ⛔ „der GPU" **als Nominativ** (der Reflex kommt von *der Grafikprozessor*); ⛔ *das GPU*; ⛔ *die Grafikkarte* als Terminus (Karte ≠ Chip) | **THIN×2 — flagged deliberately.** Both runs say `die`; **all** evidence on both sheets is **de.wikipedia** (run1: *Grafikprozessor* + *CUDA* + *GPGPU*, all four cases; run2: *Grafikprozessor*). run2 names the trap itself: two runs reading one register is not confirmation. **0 occurrences in the shipped German** — no corpus precedent to lean on. Highest-frequency row of the slice (80) with no §1.1 line |
| **scheduler** | **der Scheduler** | 2 | **BOUND** | der Scheduler / **die Scheduler** (Nullplural) / des Schedulers | „**Der Scheduler lässt bei jedem Decode-Schritt neue Anfragen zu und räumt fertige ab.**" (*admits / evicts*); „der **GPU-Scheduler**" | ⛔ **der Planer**, ⛔ **der Disponent**, ⛔ *der Ablaufplaner* — **beide ersten sind im Deutschen Personenbezeichnungen** (und ausgerechnet die de.wikipedia-Begriffsklärungsglossen); ⛔ *das Steuerprogramm* als Laufterm | **AGREED×2, and the two runs used different sources** — run1 Duden (Gebrauch **EDV**, exact referent), run2 de.wikipedia *Prozess-Scheduler*; plus **CORPUS(1)**: der shipped Mermaid-Knoten „Steuerung · **Scheduler**" |
| **scheduling** | **das Scheduling**; als Mechanismus **Scheduling auf Iterationsebene**; in Überschriften **verbal** | 2 / 3 | **BOUND** | das Scheduling / kein Plural / des Schedulings | Überschrift: „**GPUs einplanen und automatisch skalieren**"; „**Auf Kubernetes ist eine GPU eine planbare Ressource**" | ⛔⛔ **die Terminierung** — `_language.md` §1.1 bindet das Wort an *termination* („ob der Durchlauf überhaupt endet") und warnt, dass die Duden-Sinne davor *Terminfestlegung/Scheduling* sind. Wer hier `Terminierung` schreibt, hebelt eine frische Welle-2-Entscheidung aus; ⛔ **die Ablaufplanung** als Laufterm (Fertigungs-/Projektregister) | **RECONCILED** (run1 allowed *die Ablaufplanung* freistehend and coined *das Iteration-Level-Scheduling*; run2 rejected both). run2 wins — and **run1's own worked sentence writes „Scheduling auf Iterationsebene"**, contradicting its own table cell (§3-D6) |
| **autoscaling / autoscaler** | **das Autoscaling** · **der Autoscaler**; in Überschriften und Merksätzen **verbal: automatisch skalieren** | 2 | **OPEN (incumbent held: `das Autoscaling`, single-house attestation; closes when a second house prints a case-marked form)** | das Autoscaling / — / **des Autoscalings** · der Autoscaler / die Autoscaler / des Autoscalers | „**Skalieren Sie auf Warteschlangentiefe und GPU-Auslastung, nie auf CPU.**"; „**anfragegesteuertes Autoscaling**"; „**skaliert im Leerlauf auf null**"; „der **Cluster Autoscaler** kann GPU-Knoten hinzunehmen" | ⛔ **die Autoskalierung** als Laufterm; ⛔ *die Selbstskalierung*; ⛔ *autoscalen* → **skalieren** (Duden, kein `ge-`, §1.3.2) | **RECONCILED** — run1 found a dedicated German article (informatik-aktuell, ~41 occurrences incl. **genitive** „die Effizienz *des Autoscalings*" and dative plural „bei *Autoscalern*"); run2 was rate-limited and graded it OPEN. run1's evidence is real and decides the paradigm; run2's verbal preference is kept for headings. **Still one house** |
| **cold start** | **der Cold-Start** (Bindestrich) | 2 | **DISPUTED (unverändert) — für Teil III als tauglich bestätigt** | der Cold-Start / die Cold-Starts / des Cold-Starts | „**Rechnen Sie damit, dass der Cold-Start jede reaktive Hochskalierung zu spät kommen lässt.**"; „die **Cold-Start-Latenz**"; „**der Preis des Cold-Starts**" | ⛔ **die Cold-Start-Steuer** für *the cold-start tax* — „Steuer" ist die staatliche Abgabe; und rag.md §3 hat die Parallelfigur *token tax* bereits gestrichen; ⛔ *der Kaltstart* (Motor + Rechenzentrums-Blackstart) | **AGREED×2, row not reopened.** run1 adds two more German serverless articles containing **neither** `Kaltstart` **nor** `Cold Start` — DISPUTED is **confirmed, not moved**. **CORPUS(0)** — the term has not shipped yet |
| **warm** | **kein Terminus — umbauen** | 3 | **OPEN (incumbent held: rebuild; closes when a German house uses `warm` attributively of a **preloaded** instance)** | — | *always-warm GPU* → „**eine dauerhaft laufende GPU**"; *warm pools* → „**ein Vorrat bereits gestarteter Instanzen**"; *warm headroom* → „**Reserve an bereits laufenden Instanzen**"; *loaded and warm* → „**geladen und einsatzbereit**" | ⛔⛔ „**sich eine GPU warm halten**" — DWDS: ⟨jmd. hält sich jmdn. warm⟩ = *(sich jmds.) Wohlwollen bewahren*. Die dativ-reflexive Fügung ist eine feste Redewendung mit anderer Bedeutung; ⛔ *der Warm-Pool*, *die Warmreserve* (0 Belege); ⛔ *der Warmstart* (anderer Referent) | **AGREED×2 on the rebuild**; run2 supplies the DWDS idiom evidence that makes the ⛔ hard |
| **capacity** | **die Kapazität** — **nie im nackten unbestimmten Singular** | 3 | **CORPUS PRECEDENT (compute sense) + Bindungsregel** | die Kapazität / die Kapazitäten / der Kapazität | „**Kapazität zusichern / bereitstellen / reservieren**"; „**GPU-Kapazität, sekundengenau abgerechnet**"; „**jenseits der Kapazitätsgrenze**"; „**wenn die Kapazität erschöpft ist**" | ⚠ **„eine Kapazität" liest zuerst als *Koryphäe*** (Duden führt den Personensinn); ⛔ *das Fassungsvermögen*; ⛔ *die Leistung*; ⛔ `Kapazität` für die **Pool-Größe** → „**eine Standardgröße von rund vierzig Threads**" | **CORPUS(2)** — die ausgelieferte Prosa schreibt „das Dekodieren … **verbraucht Kapazität**" und „kostet aber **Modellkapazität**", also artikellos-massenhaft: genau die Fügung, die die Koryphäen-Lesart *nicht* auslöst. ⚠ **die beiden Läufe nennen verschiedene Duden-Bedeutungsnummern** (run1: 5, run2: 4) — der Befund hält, die Nummer nicht |
| **utilisation** | **die Auslastung** | 3 | **BOUND** | die Auslastung / die Auslastungen (meist Sg.) / der Auslastung | **auslasten + Akk.**; „**bei hoher Auslastung**"; die **GPU-Auslastung**; (c) verbal: „**ab welcher Auslastung sich die Zusicherung rechnet**" | ⛔ *die Ausnutzung* (Beiklang *ausbeuten*); ⛔ *die Nutzung* (das Ob, nicht der Grad); ⛔ *die Utilisation*; ⛔ *die Auslastungsschwelle* (regelhaft, unbelegt); ⚠ `gpu_memory_utilization` = Klasse 1 | **AGREED×2** (DWDS, technisches Wortprofil, gradierbar) — **CORPUS(0)**, keine ausgelieferte Präzedenz |
| **saturation** | — | — | **NULL — beidseitig geprüft, kein Ruling** | — | — | — | **AGREED×2**: `saturat*` = 0 in Teil III; Gegenprobe `golden signal*` ebenfalls 0. Der Terminus **die Sättigung** existiert im Kanon und **ist ausgeliefert** („Latenz, Traffic, Fehler und **Sättigung**", observability/deep-dive) — er kommt in Teil III nur nicht vor |
| **container** (Substantiv) | **der Container** — Erstnennung einmal binden | 2 | **BOUND (Kanonzeile besteht seit dem Bootstrap)** | der Container / die Container / des Containers | „**ein Container – ein isolierter Prozess mit eigenem Dateisystem**"; „**Jeder Container muss in UTC laufen.**"; die **Container-Runtime**, das **Container-Image** | ⛔ *der Behälter* / *das Behältnis* | **CORPUS(1)** („mit eingeschränkten Rechten laufen – **in einem Container**") + canon §1.1.a. ⚠ **the brief lists `container` as a canon gap; it is not** (§3-D8) |
| **containerise** (Verb) | **in einen Container packen** | 3 | **BOUND** | verbal | „**Eine LLM-Anwendung in einen Container zu packen unterscheidet sich nicht davon, eine gewöhnliche Python-Anwendung in einen Container zu packen.**" | ⛔⛔ **containern** — DWDS führt ein **volles Verbparadigma** mit **einer** Bedeutung: *aus dem Müllcontainer entsorgte Lebensmittel entnehmen*. „Eine Anwendung containern" heißt auf Deutsch, sie aus dem Supermarktmüll zu fischen. Kein IT-Sinn auf irgendeiner Stufe; ⛔ *containerisieren* (0 Belege) | **RECONCILED — run2 only.** Die Konkordanz zählt nur das Substantiv; **run1 hat die zwei Verbvorkommen nie gesehen**. Das ist die teuerste Einzelfalle, die nur ein Lauf gefunden hat |
| **image** | **das Image** — **nie nackt**; Erstnennung **das Container-Image** | 2 | **BOUND (Genus + Genitiv doppelt belegt) — mit Pflichtbindung** | das Image / die Images / **des Images** | „**Die Gewichte bleiben außerhalb des Images**"; „**eine neue Replik muss ein mehrere Gigabyte großes Image ziehen**"; „**das Ziehen des Images**"; „**hält die Images schlank**" | ⛔ „ein Image **pullen**" (`pullen` ist Kanon-⛔); ⛔ *das Abbild* als Laufterm; ⚠ **das nackte „das Image" sagt einem deutschen Leser *den Ruf*** — Duden **und** DWDS führen nur den Reputationssinn | **AGREED×2 with independent sources** — run1: heise Docker, Genus durch starke Adjektivendung gepinnt („**ein temporäres** Image") + „innerhalb **des Images**"; run2: de.wikipedia *Docker (Software)* („**Das Image** besteht aus mehreren Layern", „die Historie **des Images**"). **CORPUS**: `Abbild` erscheint nur als *abbilden* / *Abbildungen* — die ⛔ ist kollisionsfrei |
| **image** (rhetorisch) | **das Schlussbild** | 3 | **BOUND** | — | „**Und damit zum Schlussbild des Handbuchs:** …" | ⛔ „das Image des Handbuchs" = *der Ruf des Handbuchs*. Keine Stilfrage | **AGREED×2** (1 von 12 Vorkommen, `llmops/index.md`) |
| **process** (Betriebssystem) | **der Prozess** — **bei Erstnennung gebunden** (*der Worker-Prozess*, *ein eigener Betriebssystemprozess*) | 3 | **BOUND — mit Bindungsregel** | der Prozess / die Prozesse / des Prozesses | „**Ein Worker ist ein eigener Betriebssystemprozess – er verschafft Ihnen Kerne, keine Nebenläufigkeit.**"; „**einen Prozess starten / beenden**" | ⚠ **Duden-Bedeutung 1 ist der Gerichtsprozess** („einen Prozess verlieren"), kein EDV-Sinn — und die Falle feuert, weil Teil III den OS-Prozess neben *Judge*, *Urteil*, *Audit* und *Governance* stellt; ⛔ *der Vorgang* (zu unspezifisch); ⛔ *die Programminstanz* als Laufterm | **AGREED×2** + **CORPUS(1)**: die ausgelieferte Prosa schreibt den **gebundenen** `Unterprozess`, nie den nackten `Prozess` |
| **process** (organisatorisch) | **der Ablauf** · **das Verfahren** · gebunden *der Freigabeablauf* | 3 | **BOUND** | — | „**Was der Freigabeablauf mit einer erkannten Regression tut**, ist der Gegenstand dieses Abschnitts." | ⛔ nacktes `Prozess` in einem LLMOps-Kapitel | **AGREED×2** |
| **to process** (Verb) | **verarbeiten** | 3 | **BOUND** | verbal | „**verarbeitet den gesamten Prompt in einem Durchlauf**"; „**innerhalb der Dienstgrenze verarbeitet**" | — | **RECONCILED — run2 only** (run1 zählte die 9 Verbformen nicht getrennt) |
| **thread** (OS) | **der Thread** — **nie nackt bei Erstnennung**: *der Worker-Thread*, *der Haupt-Thread*, *ein Betriebssystem-Thread* | 2 | **BOUND (Paradigma) / OPEN (Referent: die Kanonzeile belegt den falschen)** | der Thread / die Threads / des Thread[s] | „**einen Thread belegen**"; „auf einen **freien Thread warten**"; „die Arbeit **in einen Thread auslagern**"; der **Thread-pro-Anfrage-Server** | ⛔ *der Ausführungsstrang* (unbelegt); ⛔ undurchgekoppeltes *thread-per-request-Server* | **RECONCILED** — run1 hielt die Kanonzeile für SETTLED; run2 zeigt, dass Dudens **einzige** Bedeutung der **Chat-Thread** ist: richtiges Paradigma, falscher Referent. run2 wins on evidence. **CORPUS** verschärft es: die ausgelieferten Seiten benutzen `Thread` **ausschließlich** im LangGraph-Sitzungssinn (21 Treffer, alle Teil II) |
| **threadpool** | **der Threadpool** | 2 | **HOUSE** | der Threadpool / die Threadpools / des Threadpools | „**Der Threadpool ist erschöpft, und weitere Anfragen warten auf einen freien Thread.**"; „**ein Threadpool mit einer Standardgröße von rund vierzig Threads**" | ⛔ `Kapazität` für die Pool-Größe | **AGREED×2**, beide auf demselben informatik-aktuell-Muster (*Worker-Pool*, *Haupt-Thread*) — **ein** Strang, zweimal gezählt |
| **thread** (rhetorisch) | **ein roter Faden** | 4 | **BOUND — die teuerste einzelne Zeile des Slice** | der rote Faden / — / des roten Fadens | „**Wenn sich ein roter Faden durch all diese Ausfälle zieht, dann dieser:** …" | ⛔ „ein einzelner **Thread** zieht sich durch alle …" — ein Betriebssystem-Thread an dieser Stelle ist eine **harte Fehlübersetzung, und sie überlebt jede Flüssigkeitsprüfung** | **RECONCILED** — run1 identifiziert und benennt sie; run2 fängt den Satz unter `run` ab („zieht sich durch"), ohne das Bild zu setzen. **Beide Lösungen sind richtig für *verschiedene* Sätze** (§3-D7) |
| **thread** (LangGraph-Sitzung) | **`Thread`** — Teil II, **anderer Referent** | 2 | **BOUND (nicht Teil III's Zeile)** | — | Teil III erbt ihn **nicht** stillschweigend | — | **CORPUS(21)** — der ausgelieferte Bestand gehört diesem Referenten allein |

---

## 2. Sense cards

Each card leads with **the question to ask before writing** and ships **a German sentence per branch** —
splits that ship a word get dodged, splits that ship a sentence survive contact with prose.

### SC-R — `run` / `runs` (the largest row of the slice; 9 of 10 files)

**Frage vor dem Schreiben:** *Meine ich eine gezählte Ausführung, das Betreiben eines Dienstes, das Laufen auf
einer Maschine, das Erschöpfen eines Vorrats, eine Reihenfolge — oder die laufenden Kosten?*

| Zweig | Erkennungsfrage | Deutsch | Gearbeiteter Satz |
|---|---|---|---|
| **R1 gezählte Ausführung** (*eval runs*, *scoring runs*, *red-team runs*, *a training run*) | Kann ich sie **zählen** und **wiederholen**? | **der Durchlauf** | „**Planen Sie Red-Team-Durchläufe als Prüfung vor der Freigabe ein** und verfolgen Sie die Erfolgsquote der Angriffe über die Zeit." |
| **R2 betreiben** (*run it yourself*, *run your own queue*, *no workers to operate*) | Steht ein **Dienst** oder eine **Infrastruktur** im Objekt? | **betreiben** (Akk.) | „**Betreiben Sie eine eigene Queue nur dann, wenn die Arbeit eine Pipeline ist, die Sie steuern.**" · „**… und Sie haben keine Worker zu betreiben.**" |
| **R3 ausführen / durchlaufen** (*every change runs the golden set*, *re-run eval*) | Ist das Objekt eine **Prüfung** oder ein **Datensatz**? | **durchlaufen · ausführen · erneut ausführen** | „**Jede Änderung durchläuft den Goldstandard**; Werte unter dem Schwellenwert blockieren die Freigabe." |
| **R4 laufen auf** (*where the model runs*, *every container must run in UTC*) | Steht ein **Ort** dabei? | **laufen auf / in** (Dat.) | „**Wo das Modell läuft**, entscheidet die Lektion zu den Cloud-Plattformen." · „**Jeder Container muss in UTC laufen.**" |
| **R5 sich erstrecken** (*a stream can run for tens of seconds*, *weights run from GB to tens of GB*) | Steht eine **Spanne** dabei? | **dauern · reichen von … bis** | „Ein LLM-Stream **kann mehrere zehn Sekunden dauern**." · „Modellgewichte **reichen von Gigabyte bis zu mehreren zehn Gigabyte**." |
| **R6 ausgehen** (*the pool runs out*, *the budget runs out*) | Wird ein **Vorrat** leer? | **ausgehen · aufgebraucht sein · erschöpft sein** | „… lange bevor **der GPU die Rechenleistung ausgeht**." · „was geschieht, **wenn das Fehlerbudget aufgebraucht ist**, und wer dann handelt." |
| **R7 Reihenfolge / Durchgängigkeit** (*the cheapest check runs first*, *one idea runs through all six sections*) | Geht es um **Ordnung**, nicht um Ausführung? | **greift zuerst · zieht sich durch** | „Jede Stufe weist schlechte Eingaben ab, und **die billigste Prüfung greift zuerst**." · „**Ein Gedanke zieht sich durch alle sechs Abschnitte.**" |
| **R8 laufende Kosten** (*bills around the clock*, *cache reads run ~90% below input*) | Geht es um **Geld über Zeit**? | **die laufenden Kosten · liegen bei** | „Ein fein abgestimmter Endpunkt auf schwacher Last **verursacht rund um die Uhr laufende Kosten** für Kapazität, die er kaum nutzt." · „**Cache-Lesezugriffe liegen rund 90 % unter dem Eingabepreis.**" |

⚠ **Der eine Satz, der über alle acht wacht:** die stärkste überlebende Übersetzungsspur (§1.5) wäre es,
überall `laufen` zu schreiben. `laufen` gehört **nur** zu R4. R2 ist *betreiben*, R3 *durchlaufen*, R6
*ausgehen*, R7 *greifen/sich ziehen*.
⚠ **Ein Referent, ein Name:** wer `Durchlauf` wählt, schreibt auf derselben Seite **nicht** zusätzlich *Lauf*,
*Ausführung* oder *Run*.

### SC-L — `runtime` (slice A's decisive row; 3 files)

**Frage vor dem Schreiben:** *Ist es eine Wirtsplattform, ein Produktbauteil mit Namen — oder ein Zeitpunkt?*

| Zweig | Erkennungsfrage | Deutsch | Gearbeiteter Satz |
|---|---|---|---|
| **L1 verwaltete Wirtsplattform** (*a managed agent runtime*, *the runtimes that host the agent loop*) | Kann man sie **mieten, starten und beenden**? Führt sie **fremden Code** aus? | **die (verwaltete) Agenten-Laufzeitumgebung**, Anapher **die Umgebung** | „**Eine verwaltete Agenten-Laufzeitumgebung führt die Agentenschleife für Sie aus** und legt Sitzungs- und Gedächtnispersistenz, eine Tool-, Identitäts- und Gateway-Schicht, Observability und Scale-to-Zero darum." · Überschrift: „**Die Umgebungen, in denen die Agentenschleife läuft**" |
| **L2 benanntes Produktbauteil** (*AgentCore **Runtime** gives execution windows…*) | Steht das Wort **großgeschrieben neben Memory, Gateway, Identity**? | **Runtime** (Klasse 1); mit Artikel **die Runtime** | „**Die Runtime gibt Ausführungsfenster von bis zu acht Stunden**, mit Sitzungsisolation in einer eigenen MicroVM." *(Genau so schreibt es der einzige deutsche Fachtext über dieses Produkt — und im selben Satz `Laufzeiten` für die Dauer.)* |
| **L3 Zeitpunkt** (*at runtime*, *runtime enforcement of those caps*) | Lässt sich „**zur Ausführungszeit**" einsetzen, ohne dass der Satz kippt? | **zur Laufzeit** — unverändert richtig, nie Gegenstand des Streits | „… und setzt **zur Laufzeit** pro Anfrage weiche und harte Obergrenzen durch." |

**Die Regel, die aus dem Minimalpaar folgt:** das Deutsche trennt hier nicht über das Wort, sondern über die
**Wortbildung** — `-umgebung` oder kept-EN `Runtime` = das Ding, bloßes `Laufzeit` = die Zeit. Wer bloßes
`Laufzeit` zum Bauteilnamen macht, hebt genau die Trennung auf, die die Quellsprache braucht. Der Testfall ist
Part III's eigener Satz: „*Runtime gives execution windows up to eight hours*" — „die Laufzeit gibt
Ausführungsfenster von bis zu acht Stunden" stellte **dasselbe Wort in beiden Bedeutungen in einen Satz**.

### SC-C — `concurrency` vs `parallelism`

**Frage vor dem Schreiben:** *Eigenschaft oder Zahl? Und trägt das Wortpaar den Lehrsatz überhaupt?*

- **C1 Eigenschaft** → **nebenläufig / die nebenläufige Ausführung**; das Substantiv **die Nebenläufigkeit**
  nur dort, wo der Kontrast es verlangt.
- **C2 Zahl / Deckel** → **nicht** `Nebenläufigkeit`, sondern das Bezugsobjekt zählen:
  „**Begrenzen Sie die Zahl gleichzeitiger Generierungen mit einer Semaphore** und stellen Sie eine
  beschränkte Queue dahinter." · „**Obergrenzen je Mandant für gleichzeitige Generierungen.**"
- ⚠ **C3 — die Konstruktionsfalle, nicht die Wortfalle.** Der Korpus baut einen harten Gegensatz
  („*a worker gives you process-level parallelism … what it does not give you is concurrency*"). Das
  de.wikipedia-Lemma *Nebenläufigkeit* öffnet aber mit „mitunter auch **Parallelität** genannt". **Die zwei
  deutschen Substantive allein tragen den Lehrsatz nicht** — der Satz muss den Mechanismus mitliefern:
  „**Ein Worker verschafft Ihnen Parallelität auf Prozessebene – eigener Prozess, eigener Interpreter,
  eigener Event-Loop. Was er Ihnen nicht verschafft, ist Nebenläufigkeit: Die kommt aus dem Event-Loop,
  nicht aus der Zahl der Prozesse.**"

### SC-K — `capacity` (4 Referenten)

**Frage vor dem Schreiben:** *Gekaufte Menge, Lastpunkt, Pool-Größe — oder das, was Sharding verschafft?*

| Referent | Deutsch | Satz |
|---|---|---|
| gekaufte/zugesicherte Menge (*committed, provisioned, dedicated, reserved*) | **zugesicherte / bereitgestellte / dedizierte / reservierte Kapazität** | „**Zugesicherte Kapazität ist ein Gedanke unter drei Namen**: Azure verkauft sie als PTU, Vertex als Provisioned Throughput, Bedrock als Provisioned Throughput mit Reservierungslaufzeit." · „**Unterhalb davon gewinnt die Abrechnung nach Verbrauch, weil Sie nicht für ungenutzt reservierte Kapazität zahlen.**" |
| Lastpunkt (*past capacity*) | **jenseits der Kapazitätsgrenze** / **wenn die Kapazität erschöpft ist** | „**Jenseits der Kapazitätsgrenze explodiert die Wartezeit in der Queue, und der p99-Wert bricht ein.**" |
| Pool-Größe (*threadpool default capacity ~40 threads*) | **die Größe** — ⛔ Kapazität | „**Ein Threadpool mit einer Standardgröße von rund vierzig Threads**" |
| was Sharding verschafft / mietbare Rechenressource | **Kapazität**, gebunden **GPU-Kapazität** | „**Das Aufteilen verschafft Ihnen Kapazität, die Sie vorher nicht hatten; Durchsatz verschenkt es Ihnen nie.**" · „**GPU-Kapazität, sekundengenau abgerechnet**" |

⚠ **Nie im nackten unbestimmten Singular** („eine Kapazität" = *eine Koryphäe*). Die ausgelieferte Prosa
schreibt es **artikellos-massenhaft** („verbraucht Kapazität") — das ist die sichere Fügung.
⚠ `verbrauchen` passt für die **verbrauchte** Rechenkapazität (so ausgeliefert), **nicht** für zugesicherte
Kapazität — die wird bezahlt, nicht aufgebraucht.

### SC-B — `batch` / `batching`: der Tarif gegen den GPU-Scheduler

**Frage vor dem Schreiben:** *Rede ich über einen Preistarif — oder über das, was der Scheduler auf der GPU tut?*
Der Korpus warnt **zweimal selbst** vor dieser Kollision. Deutsch löst sie **lexikalisch**:

- **Preistarif / Betriebsmodus** → **der Batch-Modus**, **die Batch-API**, **die Batch-Stufe**;
  daneben zulässig **die Stapelverarbeitung** (de.wikipedia-Lemma).
- **GPU-Verfahren** → **das Continuous Batching**, **das statische Batching**, **der laufende Batch**.
  **Hier ⛔ *Stapelverarbeitung*** — sie ist die Cloud-Bedeutung, und wer sie hier einsetzt, baut die
  Verwechslung, vor der der Korpus warnt, im Deutschen erst richtig auf.

„**Verwechseln Sie das nicht mit dem Continuous Batching aus der Serving-Lektion: Dieser Batch ist eine
Preisstufe der API, jenes ein GPU-Scheduler, der etwas völlig anderes tut.**"

### SC-I — `image`: Datei oder Ruf?

- **I1 Container-Image** (11 von 12) → Erstnennung **das Container-Image**, danach **das Image**.
  „**Ein Container-Image mit eingebackenen Gewichten ist unveränderlich und exakt reproduzierbar – was Sie
  getestet haben, ist das, was läuft.**"
- **I2 das rhetorische Schlussbild** (`llmops/index.md`) → **das Schlussbild**.
  „**Und damit zum Schlussbild des Handbuchs:** …" ⚠ „das Image des Handbuchs" sagt **den Ruf**.

### SC-P — `process`: Betriebssystem, Organisation oder Verb?

- **P1 Betriebssystemprozess** → **der Prozess**, Erstnennung gebunden:
  „**Ein Worker ist ein eigener Betriebssystemprozess – er verschafft Ihnen Kerne, keine Nebenläufigkeit.**"
- **P2 organisatorischer Ablauf** → **der Ablauf / das Verfahren / der Freigabeablauf**.
  „**Was der Freigabeablauf mit einer erkannten Regression tut**, ist der Gegenstand dieses Abschnitts."
- **P3 das Verb** → **verarbeiten**: „**verarbeitet den gesamten Prompt in einem Durchlauf**".
  Grund für P1/P2: Duden-Bedeutung 1 von `Prozess` ist der **Gerichtsprozess**, und dieses Kapitel steht
  voller *Judge*, *Urteil*, *Audit* und *Governance*.

### SC-T — `thread`: Betriebssystem, Agentensitzung oder Metapher?

- **T1 Betriebssystem-Thread** (Teil III) → **der Thread**, **der Threadpool** — **nie nackt bei Erstnennung**:
  „**Lagern Sie die Arbeit in einen Thread aus, damit der Event-Loop weiter ausliefert.**"
- **T2 LangGraph-Sitzung** (Teil II, 21 ausgelieferte Vorkommen) → **anderer Referent**; Teil III erbt ihn
  **nicht** stillschweigend.
- **T3 Metapher** (`production-failures.md`: *if a single thread runs through all …*) → **ein roter Faden**:
  „**Wenn sich ein roter Faden durch all diese Ausfälle zieht, dann dieser:** …"
  ⚠ Ein Betriebssystem-Thread an dieser Stelle ist eine harte Fehlübersetzung, und sie überlebt jede
  Flüssigkeitsprüfung.

### SC-W — `worker`: Prozess, Menge oder Produktbauteil?

- **der Prozess** (ASGI, Celery) → **der Worker**, gebunden bei Erstnennung: „**ein Worker – ein eigener
  Prozess mit eigenem Interpreter und eigenem Event-Loop**".
- **die Menge** → **der Worker-Pool**, Dat. Pl. **den Workern**.
- **`Langfuse Worker`** (Produktkomponente neben *Web*, *Postgres*, *ClickHouse*) → **Klasse 1**, unflektiert;
  **die Auszeichnung trägt die Unterscheidung, nie der Großbuchstabe** — „der **`Worker`**-Dienst von Langfuse"
  gegen „ein Worker". (Dieselbe Lage wie `Reflexion` in `_language.md` §1.1: derselbe String ist auf derselben
  Seite Appellativ und Eigenname, und das Englische unterscheidet über einen Großbuchstaben, den das Deutsche
  jedem Substantiv gibt.)
- ⚠ **Die Menschenfalle liegt im freien Singular:** die dominanten freien deutschen Kollokationen von `Worker`
  sind *Gig Worker*, *Knowledge Worker*, *Frontline Worker* — alle **Personen**. Kein Wörterbuch entschärft das.

---

## 3. RUN DISAGREEMENTS

Both positions recorded; my resolution and its reason follow each. **Nothing here is silently overwritten.**

**D1 — `runtime`: which German word heads the component sense.** ⭐ *the wave's highest-value row*
- **run 1:** **`die Runtime`** (kept-EN, Klasse 2) as the running term, `die Laufzeitumgebung` only where "the
  frame" is meant. Argues canon §D's ⛔ on `Laufzeitumgebung` is **categorically too broad** and cites four
  independent houses using it for a component, two in our domain.
- **run 2:** **`die Laufzeitumgebung`** (Klasse 3) as head, `die Runtime` only as a vendor proper name. Argues
  §D never *was* categorical for this referent — Batch E rejected it **for the fan-out sentence**, where the
  subject was your own application code, not a host platform. "Zwei Referenten, zwei Rulings; kein Widerspruch."
- **Resolution: run 2's head, run 1's release argument, plus a third branch neither ran alone.** I read the
  canon text: §D's own wording is „`Laufzeitumgebung` ist die **JVM/CLR-Klasse Wirtsplattform**" — which is
  *exactly* Part III's referent. The canon therefore does not have to be overruled to release it; it has to be
  **read**. And the deciding evidence is a native German sentence about the exact product Part III names
  (Bedrock AgentCore): `Runtime` for the component, `Laufzeiten` for the durations, **in one sentence**.
  ⇒ **L1 `die Laufzeitumgebung` · L2 `Runtime` Klasse 1 in vendor names · L3 `zur Laufzeit` untouched · bare
  `die Laufzeit` as a component name stays ⛔.** Run 1's `die Runtime` is *not* wrong — it is attested and
  feminine in both runs' sources — it is **demoted to the vendor-name branch**, where its attestation is
  strongest (FaaS-Runtime, Kubeless-Runtime, AgentCore Runtime: all named things).
- **Measurement correction, and it weakens the procedural argument for reopening the row:** the brief and the
  referent baseline say the component sense ships on **six pages / five shipped pages**. My grep of the 27
  pages: **5 occurrences in 2 files** (`real-agents.md` 40/199/218/325 + `orchestration-frameworks/deep-dive.md`
  :73). The baseline counted `mcp/index.md`:46 („Ein Protokoll für **die Laufzeit**") as a component use; read
  in context it is the **temporal** contrast the same page then spells out („**Laufzeit statt Entwurfszeit**")
  and is correct German. So the standing rule *"where a register and several independent renderers diverge, the
  register is the suspect"* **does not fire at the claimed strength** — four of five hits are one page. The
  canon is still the suspect, but **on the attestation, not on renderer convergence.** That distinction is the
  difference between an evidenced and a procedural argument, and it belongs in the record.

**D2 — `event loop`: the gender is frontally contradicted.** ⭐
- **run 1: `die Event-Loop`** — INNOQ, feminine in four positions, with a self-gloss „eine Ereignisschleife
  („Event Loop")". Run 1 explicitly names the trap: the canon licenses `der Loop`, so a switch to `die` on the
  same page is §1.1 wobble — **and then chooses `die` anyway.**
- **run 2: `der Event-Loop`** — informatik-aktuell, masculine and **case-marked** four times including a
  genitive („**des Event-Loops** Thread", „**den Event-Loop**", „**den Event-Loop-Thread**"), plus the mnemonic
  „Blockiere niemals **den** Event-Loop". Notes `Ereignisschleife` = 0× in that article.
- **Resolution: `der Event-Loop`.** Two reasons, in order. (1) **Case-marked evidence outranks nominative
  article counts** — accusative and genitive are the forms a renderer will get wrong. (2) **Canon-internal
  consistency**: `_language.md` §1.1.g's rejection note records `der Loop` as Duden-licensed with a real EDV
  sense; `der Loop` / `die Event-Loop` on one page is exactly the wobble run 1 itself flagged.
  **Status stays OPEN, incumbent held** — this is a genuine two-house gender split in native German, not a
  settled row, and stage 2 should not read the binding form as a settled one.
  *(No corpus help: `Event-Loop` = 0 in the shipped German. The corpus's word for the agent loop is
  `die Schleife`, a different referent and a different string — no collision either way.)*

**D3 — `inference server`: attested term vs coined term.** ⭐
- **run 1: `die Inferenz-Engine`** — heise/iX ×2, one definitional („Eine Inferenz-Engine ist eine
  Laufzeitumgebung, die den Prompt verarbeitet …"). Explicitly ⛔ `der Inferenzserver` on a measured zero.
- **run 2: `der Inferenzserver`** — a **pattern-licensed coinage**, with run 2's own measured triple zero on
  de.wikipedia and its own warning: "nach der Kanonregel muss ein späterer Durchgang sie tragen oder streichen.
  **Nicht als belegt darstellen.**"
- **Resolution: `die Inferenz-Engine`.** Brief §3 is explicit — a confirmed incumbent beats a coinage, and a row
  that had to be coined is weaker than one confirmed. Two runs independently measured `Inferenzserver` at zero;
  only one of them then wrote it anyway.
  ⚠ **But the incumbent is THIN and I am labelling it so:** heise and iX are **one** publishing house counted
  twice (run 1 says this itself, citing the wave-1 lesson that dpunkt/O'Reilly/heise are one Stilfamilie).
  Status **OPEN, incumbent held**, closing condition in the table.
  ⚠ **Where the English distinguishes *inference server* from *inference engine*, rebuild the sentence** rather
  than coin a second German noun: „**Die Inferenz-Engine hält das Modell, FastAPI hält das Produkt.**"

**D4 — `prefix caching`: hyphen or space.**
- **run 1: `das Prefix-Caching`** (K7 — `prefix` is a noun, §45 E1 / §1.3.3(b) applies, against rag.md §2's
  citation form). **run 2: `das Prefix Caching`** (asserts Adj+Subst → spaced).
- **Resolution: run 1.** `prefix` is a substantive; run 2 misanalysed the part of speech. The result is
  internally consistent with the neighbours the canon already spells spaced — `Continuous`, `Chunked`, `Late`
  **are** adjectives (§37 E4), so `Continuous Batching`, `Chunked Prefill`, `Late Chunking` keep their space
  and `Prefix-Caching` takes its hyphen. Not a re-decision; a spelling clarification the wave needs 4× in one
  file. **CANON DELTA filed.**

**D5 — `autoscaling`: WEAK-with-evidence vs OPEN.**
- **run 1** found a dedicated German article on autoscalers carrying ~41 occurrences, a **marked genitive**
  („die Effizienz **des Autoscalings**") and a **dative plural** („bei **Autoscalern**") ⇒ `das Autoscaling`,
  `der Autoscaler`. **run 2** was rate-limited by the de.wikipedia API, measured only thin insource counts, and
  graded the free noun **OPEN**, leading verbally.
- **Resolution: run 1's paradigm, run 2's register.** The evidence is real and run 2 simply did not reach it —
  an asymmetry of access, not of judgement. Bind `das Autoscaling` / `der Autoscaler`; **prefer the verbal
  construction in headings and mnemonics** („GPUs einplanen und automatisch skalieren"). Still **one house** ⇒
  status OPEN, incumbent held.

**D6 — run 1 contradicts itself twice, inside its own rows.** (Neither is a run-vs-run disagreement; both are
the shape wave 2 measured — the contradiction hides in the worked example, not the summary row.)
- **`scheduling`:** the table cell rules „**das Iteration-Level-Scheduling**"; the worked sentence in the same
  row writes „Continuous Batching ist in Wahrheit **Scheduling auf Iterationsebene**". Run 2 rules the latter.
  ⇒ **`Scheduling auf Iterationsebene`** binds; the triple-English compound is dropped.
- **`prefill`:** the row rules „ein langer Prefill" **⛔** (no article, Kompositumsbildner only) and then the
  worked sentence writes „**zerlegt einen langen Prefill in Stücke**" — a bare inflected noun, the exact form
  it just banned. ⇒ „**Chunked Prefill zerlegt einen langen Prompt in Stücke und mischt sie unter die laufenden
  Decode-Schritte.**"

**D7 — `thread`, the rhetorical sense: both right, about different sentences.**
- **run 1** identifies it as the slice's most expensive line and ships **„ein roter Faden"**.
- **run 2** never lists it under `thread`; it catches the sentence under `run` → „zieht sich durch", and its
  worked example is „**Ein Gedanke zieht sich durch alle sechs Abschnitte**".
- **Resolution: both, assigned to their own corpus sentences.** Part III has *two* different sentences —
  „*a single thread runs through all*" (`production-failures.md`) → **„Wenn sich ein roter Faden durch all
  diese Ausfälle zieht"**; and „*one idea runs through all six sections*" → **„Ein Gedanke zieht sich durch
  alle sechs Abschnitte"**. Neither run had both. The OS-thread mistranslation is closed either way.

**D8 — the canon-gap inventory: run 2 is right and the brief's premise is wrong.**
- **run 1** files `Container`, `Image`, `GPU`, `Scheduler`, `Kapazität`, `Auslastung` etc. as canon gaps and
  separately (K4) criticises the existing `Container` line for overreaching its status marker.
- **run 2** checks and reports that **`Container`, `Thread` and `Worker` all have §1.1.a lines already**.
- **Resolution: run 2, verified by me** — `_language.md` §1.1.a carries `Container`, `Thread`, `Worker`,
  `Batch`, `Cache`, `Durchsatz`, `Latenz`, `Queue`, `Server`. Run 1's *status* critique still stands and is a
  separate matter (CANON DELTA C4). **Real gaps in this slice: GPU · Event-Loop · Nebenläufigkeit ·
  Parallelität · Kapazität · Auslastung · Scheduler · Scheduling · Image · Prozess (EDV) · Durchlauf ·
  Laufzeitumgebung · Autoscaling/Autoscaler · Threadpool · Inferenz-Engine.** *(That is a delta to the §1.1
  gap list; the total is stage 2's to compute.)*

**D9 — the shared blind spot: both runs shipped a banned metaphor.** ⭐
Run 1 (`KV cache` collocation column) and run 2 (`KV cache` worked sentence) both wrote
„der KV-Cache … **ist die eigentliche Decke**" for *the ceiling*. The brief rules `die Decke` out —
*durch die Decke gehen* points the opposite way. Two blind runs converging on it is not confirmation; it is one
English collocation surviving twice. ⇒ **⛔ `die Decke`. Bind: „Nicht die reine Rechenleistung, sondern der
KV-Cache **setzt die eigentliche Grenze**." / „… **ist der eigentliche Engpass**."**
(Related, same shape, and worth one line for stage 2: `Obergrenze` is already carrying *cap* in this wave — do
not spend it on *ceiling* as well.)

**D10 — `containerise`: a whole word only one run saw.**
The concordance counts the noun; run 2 re-grepped the family and found the **verb** twice, then found that
`containern` has a full DWDS paradigm meaning *dumpster-diving for food*. Run 1 never saw the form. ⇒ run 2's
⛔⛔ and the rebuild „**in einen Container packen**" bind. *Method note for stage 2: three of the four
concordance holes both runs found were **inflection or case-form holes**, not missing entries.*

**D11 — smaller splits, resolved without ceremony.**

| Row | run 1 | run 2 | Resolution |
|---|---|---|---|
| `concurrency` status | WEAK (Duden/DWDS 404) | SETTLED (de.wikipedia lemma) | **Corpus decides**: 16 adverbial uses shipped, **0** nominalisations ⇒ adverbial is the incumbent, the noun the exception |
| `paged KV cache` | „ein **seitenweise** verwalteter KV-Cache" | „ein **in Seiten** verwalteter KV-Cache" | run 2 — it measured `seitenweise` = 0× in the *Paging* lemma |
| `evicts` | „wirft fertige **heraus**" | „räumt fertige **ab**" | run 2 — `abräumen` carries the sense without the combat image |
| the three sharding compounds | all hyphenated | *Datenparallelität* solid, others hyphenated | run 1's **uniform** hyphen — the three appear as a set in one sentence; mixed spelling reads as an error. **HOUSE, flagged in §7** |
| `Kapazität` person-sense | „Duden-Bedeutung **5**" | „Duden-Bedeutung **4**" | **One of them miscounted.** The finding holds; the number does not. Cite the sense, never the number |
| `warm` | „umbauen", ⛔ *Warm-Pool* on a zero | same, plus the DWDS `warmhalten` idiom | run 2's evidence added; ruling unchanged |
| `run` branches | 7 | 6 | Merged to 8 (SC-R) — run 1's *R5 sich erstrecken*, run 2's *R7 Reihenfolge*; neither had both |
| `Durable Execution` gloss (run 1's K3) | argues the canon gloss says „**ein Lauf**" and must lose to `Durchlauf` | notes the defect is „gerade repariert" | **Both are out of date: the canon already reads „ein *Durchlauf*"** (`_language.md`:1231) and the shipped page reads „ein Durchlauf". Run 2's claim of a shipped „ein Lauf" is **not reproducible** — I grepped: the only `ein lauf*` hits in the corpus are *ein laufendes Dokument* / *ein laufender Agent*. **Row closed on all three levels; no repair needed.** |

---

## 4. VOCABULARY FOOTPRINT

Flat, deduplicated German content words appearing in this ledger's worked sentences and sense cards. Stage 2
uses this for cross-slice collisions.

**Nouns:** Ablauf · Änderung · Anfrage · Angriff · Arbeitsspeicher · Aufruf · Auftrag · Auslastung ·
Ausführungsfenster · Batch · Batch-API · Batch-Modus · Batch-Stufe · Betriebssystem · Betriebssystemprozess ·
Block · Cold-Start · Cold-Start-Latenz · Container · Container-Image · Datei­system · Decode-Phase ·
Decode-Schritt · Dienst · Dienstgrenze · Durchlauf · Durchsatz · Eingabepreis · Einheit · Endpunkt · Engpass ·
Ereignis · Event-Loop · Fehlerbudget · Freigabe · Freigabeablauf · Gedächtnispersistenz · Gewicht · Gigabyte ·
Goldstandard · Grafikprozessor · Grenze · Größe · GPU · GPU-Auslastung · GPU-Kapazität · GPU-Knoten ·
GPU-Scheduler · GPU-Speicher · GPU-Stunde · Handbuch · Identitätsschicht · Image · Inferenz-Engine ·
Instanz · Interpreter · Kapazität · Kapazitätsgrenze · Kern · Knoten · Kosten · KV-Cache · KV-Cache-Block ·
KV-Cache-Pool · Ladung · Laufzeit · Laufzeitumgebung · Lektion · Mandant · MicroVM · Modell · Nebenläufigkeit ·
Obergrenze · Ordnung · Parallelität · Pipeline · Prefill-Phase · Prefix-Caching · Prompt · Prompt-Präfix ·
Prozess · Prüfung · Queue · Rechenleistung · Regression · Replik · Reserve · Ressource · Roter Faden ·
Scheduler · Scheduling · Schleife · Schlussbild · Schritt · Schwellenwert · Seite · Semaphore ·
Sitzungsisolation · Sitzungspersistenz · Speicherbandbreite · Stapelverarbeitung · Stück · Thread ·
Threadpool · Token · Tool-Schicht · Umgebung · Vorrat · Warteschlangentiefe · Wartezeit · Werkzeug · Worker ·
Worker-Pool · Worker-Prozess · Zahl · Zusicherung

**Verbs:** abräumen · anstoßen · ausfallen · ausführen · ausgehen · auslagern · auslasten · aufbrauchen ·
aufstocken · begrenzen · beschränken · bestätigen · betreiben · blockieren · durchlaufen · durchsetzen ·
einplanen · entstehen · erschöpfen · greifen · halten · hinzunehmen · laufen · legen · packen · reichen ·
skalieren · starten · stellen · verarbeiten · verbrauchen · verschaffen · verschenken · verteilen · verwalten ·
verzahnen · warten · wiederverwenden · ziehen · zulassen · zusammenfassen · zusichern

**Adjectives / adverbs:** anfragegesteuert · dauerhaft · dediziert · durchgekoppelt · eingebacken · einsatzbereit ·
frei · ganzzahlig · gebunden · geladen · gemeinsam · gleichzeitig · hoch · langsam · laufend · nebenläufig ·
planbar · rechenlastig · reserviert · schlank · sekundengenau · statisch · synchron · unveränderlich ·
verwaltet · zugesichert

⚠ **Collision candidates I can already see from my own list** (stage 2 owns the merge):
`die Umgebung` / `die Laufzeitumgebung` (wave 1 collided on `Laufzeitumgebung`), `das Werkzeug` (wave 1's
`Werkzeuge` collision — I use it **once**, in the *the right tool is …* frame, and defer to slice C's
`Tools` ruling), `die Obergrenze` (carrying *cap*; see D9), `die Queue`, `das Budget`, `die Grenze`,
`der Engpass`, `die Schleife`, `der Knoten`, `die Prüfung`, `der Durchsatz`, `laufend`.

---

## 5. SPREAD (from the concordance; 10 Part III files)

Terms in **≥3 files need ONE binding string decided centrally** — marked ⭐.

| Terminus | Occ. | Files | Where |
|---|---:|---:|---|
| ⭐ **run / runs** | largest row of the slice | **9** | llmops/dd, llmops/idx, serving/dd, tooling/dd, cloud/dd, production-failures, serving/idx, cloud/idx, tooling/idx |
| ⭐ **process** | 29 | **6** | serving/dd, serving/idx, cloud/idx, llmops/dd, tooling/dd, llmops/idx |
| ⭐ **GPU** | 80 | **5** | serving/dd (36), serving/idx (17), cloud/idx, cloud/dd, llmops/dd |
| ⭐ **worker** | 36 | **4** | llmops/dd, serving/dd, tooling/dd, serving/idx |
| ⭐ **throughput** | 29 | **4** | serving/dd, cloud/idx, serving/idx, cloud/dd |
| ⭐ **capacity** | 33 | **4** | cloud/dd (14), serving/dd, cloud/idx, llmops/dd |
| ⭐ **inference server** | 19 | **4** | serving/idx (9), serving/dd, cloud/idx, overview |
| ⭐ **container** | 17 | **4** | serving/idx, tooling/dd, cloud/dd, overview |
| ⭐ **batching** | 12 | **4** | serving/idx, serving/dd, cloud/idx, cloud/dd |
| ⭐ **continuous batching** | 9 | **4** | serving/idx, serving/dd, cloud/idx, cloud/dd |
| ⭐ **concurrency** | 17 | **3** | serving/dd (14), serving/idx, llmops/dd |
| ⭐ **scheduler** | 7 | **3** | serving/dd, cloud/idx, cloud/dd |
| ⭐ **warm** | 8 | **3** | serving/dd, serving/idx, cloud/idx |
| ⭐ **utilisation** | 5 | **3** | serving/dd, cloud/dd, llmops/dd |
| ⭐ **runtime** | 12 | **3** | cloud/dd (8), llmops/dd (2), cloud/idx (1) |
| ⭐ **image** | 12 | **3** | serving/idx (9), serving/dd, llmops/idx |
| ⭐ **thread** | 8 | **3** | serving/dd, production-failures, serving/idx |
| event loop | 10 | 2 | serving/dd, serving/idx |
| blocking call | 6 | 2 | serving/dd, serving/idx |
| parallelism | 15 | 2 | serving/dd, serving/idx |
| prefill / decode | 9 / 6 | 2 | serving/dd, cloud/dd |
| KV cache | 19 | 2 | serving/dd, serving/idx |
| scheduling | 8 | 2 | serving/dd, serving/idx |
| autoscaling | 5 | 2 | serving/dd, serving/idx |
| cold start | 13 | 2 | serving/dd, serving/idx |
| prefix caching | 4 | 1 | serving/dd |
| paged attention | 0 printed / **6 real** | 1 | serving/dd — **the printed zero is a narrowing-matcher artefact** |
| saturation | 0 | 0 | verified true zero, both directions |

**Note on the `run` count:** the concordance prints `run` and `runs` as separate head entries whose figures do
not compose the way the two runs' greps do (both runs measured 44 + 38). I have not restated a total — the
row's *shape* (9 of 10 files, the widest spread in the slice) is what binds.

---

## 6. CANON DELTA — report only, nothing edited

| # | File / section | Current | Proposed | Reason |
|---|---|---|---|---|
| **C1** | `rag.md` §8 Phase 3 §D | „`Laufzeitumgebung` ist die JVM/CLR-Klasse Wirtsplattform, `Laufzeit` ist ein **kategorialer** falscher Freund" | Keep the ⛔ on bare `Laufzeit` **as a component name**. **Scope the `Laufzeitumgebung` rejection to its referent**: it was rejected *for the fan-out sentence*, where the subject was your own application code. Where the referent genuinely **is** a host platform, `die Laufzeitumgebung` is the right word — by §D's own definition of it | Four independent houses, two in our exact domain, use `Laufzeitumgebung` for a component. The row is not wrong; it is **stated as categorical while its evidence is referent-bound**. Precedent: §1.3.1, „die Regel steht, die Begründung war falsch" — here inverted: the core stands, the **reach** was too wide |
| **C2** | `rag.md` §8 Phase 3 §D | „alle **neun** DWDS-Bedeutungen sind Zeitdauern" | „**alle** DWDS-Bedeutungen sind Zeitdauern" (drop the number) | Run 2 retrieved the DWDS page on 2026-07-29 and counted **five** numbered senses. **The finding holds verbatim — every sense is a duration — the count does not.** A defender who cites the nine loses an argument they should win |
| **C3** | `_language.md` §1.1, `Host` row, Pflichtglosse | „… eine Entwicklungsumgebung, eine Chat-App, **eine Agentenlaufzeit**" | „… eine Entwicklungsumgebung, eine Chat-App, **eine Agenten-Laufzeitumgebung**" | The gloss is a string §2 releases for **verbatim** reuse, and it ships (`part-2-agents/mcp/deep-dive.md`:15). It instructs renderers to write the exact form §D forbids, and `Agentenlaufzeit` has **0** de.wikipedia attestation — a canon coinage. The replacement keeps the triple's `-umgebung` parallel |
| **C4** | `_language.md` §1.1.a, `Container` | „SETTLED — Duden" | „**SETTLED (Morphologie) / WEAK (IT-Sinn)**" | Duden gives the full paradigm and **three senses, all physical**; no EDV sense. The referent comes from levels 3–5. The German does not change; the **citability** does — and the canon lists `Container` in its own trap box already |
| **C5** | `_language.md` §1.1.a, `Thread` | „SETTLED — Duden" | „**SETTLED (Paradigma) / WEAK (Referent)**", referent stützen auf de.wikipedia *Prozess (Informatik)*; add to the „verwenden, aber nie nackt" class | Duden's **only** sense is „Folge von Nachrichten zu einem Thema in einem **Chat**". Correct paradigm, wrong referent — Falle 1 in Reinform, and Part II already occupies the string with the LangGraph session (21 shipped occurrences) |
| **C6** | `_language.md` §1.1.a, `Worker` | „WEAK (2026-07-28, hochgestuft von HOUSE) … des Workers (*regelhaft abgeleitet*)" | **Upgrade with corpus evidence**: „des Workers" and „den Workern" are **no longer derived — they ship**: „der Span **jedes Workers**", „bei ungleichartigen **Workern**", „gibt **jedem Worker** einen Anteil" | Issue #328 in one line. Both runs went hunting externally for exactly these forms; run 1 recorded them as not found |
| **C7** | `rag.md` §2 kept-EN list | `Prefix Caching` (spaced) | In a German sentence: **`Prefix-Caching`** | `prefix` is a **Substantiv** → §45 E1 / §1.3.3(b). §2 itself orders multi-word terms to be spelled per §1.3.3 once they sit in a German sentence. Neighbours are unaffected: `Continuous`, `Chunked`, `Late` are adjectives (§37 E4) and keep their space |
| **C8** | `rag.md` §2 kept-EN list vs `_language.md` §1.1 | Twelve §2-„settled" terms — `Prefill`, `Decode`, `Chunked Prefill`, `Prefix Caching`, `Continuous Batching`, `PagedAttention`, `KV-Cache`, `Cold Start`, `Scale-to-Zero`, `Provisioned Throughput`, `Little's Law`, `Admission Control` — **have no §1.1 row**, though §2 orders one before a term's second use | Add rows, or mark the class explicitly as *Kompositumsbildner ohne Genus* (§E) | Structural, not per-term. Same shape as wave 2's missing MCP register — **noticed before shipping this time**. `Prefill`/`Decode` in particular are „settled" with no article, which is exactly why both runs (correctly) refused to write one |
| **C9** | `_language.md` §1.3.3 / §1.1.d / `rag.md` §2 | `Cold Start` spelled three ways across three places | Bind **`der Cold-Start`, `die Cold-Starts`, `des Cold-Starts`; Kompositum `Cold-Start-Latenz`** | §1.3.3 is the *verbindliche* list and carries the hyphen; §1.1.d's article column confirms it; §2's box says „**may** stay spaced" — permissive, not a counter-ruling. Part III needs the word 13× in 2 files |
| **C10** | `_language.md` §1.5 (Verb nach Objekt) | — | Add: **Event-Loop** → blockieren, freihalten, verzahnen (⛔ *einfrieren*, *festfrieren*) · **Durchlauf** → anstoßen, starten; bricht ab, endet (⛔ *fahren*) · **Kapazität** → zusichern, bereitstellen, reservieren; ist erschöpft (⛔ *verbrauchen* für zugesicherte K.) · **Worker** → zieht, bestätigt, fällt aus (⛔ *stirbt*) · **Scheduler** → lässt zu, räumt ab (⛔ *vertreibt*) · **GPU** → auslasten, aufteilen (⛔ *warm halten*) | Six object-verb pairs where the fluent German verb is the wrong one. Every ⛔ here is dictionary-grounded, not taste |
| **C11** | `_language.md` §1.1 Fallenkasten | — | Add **`Image`** (Duden+DWDS: only *Ruf*) · **`Prozess`** (Duden sense 1 = Gerichtsprozess, no EDV sense) · **`containern`** (DWDS: full paradigm, **one** sense = dumpster-diving) · **`Kapazität`** (Duden's person sense = *Koryphäe*) | All four verified at the dictionary by run 2; `Image` and `Prozess` independently by run 1. `containern` is the single most dangerous and **the concordance never showed it** |
| **C12** | `_language.md` §1.1 „verwenden, aber nie nackt" class | — | Add **`Worker`** (free German collocations are *Gig/Knowledge/Frontline Worker* — persons), **`Kapazität`**, **`Image`**, **`Prozess`**, **`Thread`** | Five terms whose paradigm is fine and whose *bare* singular reads as something else |
| **C13** | new §1.1 rows (the real gaps) | — | **GPU** (die/die GPUs/der GPU — ⚠ THIN×2, see §7-N1) · **Event-Loop** (der/die Event-Loops/des Event-Loops — ⚠ OPEN) · **Nebenläufigkeit** (die/–/der) · **Parallelität** (die/–/der) · **Kapazität** (die/die Kapazitäten/der — nie nackt) · **Auslastung** (die/die Auslastungen/der) · **Scheduler** (der/die Scheduler/des Schedulers) · **Scheduling** (das/–/des Schedulings, HOUSE) · **Image** (das/die Images/des Images — nie nackt) · **Prozess** EDV (der/die Prozesse/des Prozesses — nie nackt) · **Durchlauf** (der/die Durchläufe/des Durchlaufs — **CORPUS**) · **Laufzeitumgebung** (die/die -en/der) · **Autoscaling** (das/–/des Autoscalings) + **Autoscaler** (der/die Autoscaler/des Autoscalers) · **Threadpool** (der/die Threadpools/des Threadpools, HOUSE) · **Inferenz-Engine** (die/die -s/der — ⚠ OPEN, THIN) | Fifteen rows this slice needs. **This is a delta to the §1.1 gap list, not a total** |

---

## 7. NEEDS A DECISION, NOT MORE RESEARCH

**N1 — `die GPU`. 80 occurrences, 5 files, no canon row, and both runs read the same register.**
Recommendation: **bind `die GPU`** (Nom./Akk.), `der GPU` (Gen./Dat.), `die GPUs`, with the first-mention gloss
„die **GPU** (der Grafikprozessor)". Both runs concur; run 1's evidence spans three de.wikipedia articles and
all four cases with **zero** masculine/neuter; the shipped corpus has no precedent either way. Run 2 names the
risk honestly: the German reflex runs through *der Grafikprozessor* → *der* GPU.
**Cost of being wrong:** a gender error repeated ~80 times across five files, in the slice's most frequent term,
visible in every compound. It is also the **cheapest possible fix later** (one string, mechanical) — which is
precisely why it should be **decided now and marked THIN**, not left to a renderer's ear.

**N2 — `der` vs `die Event-Loop`.** Two native houses, opposite genders, both case-bearing. No further
attestation will break the tie; somebody must rule. Recommendation: **`der Event-Loop`**, for canon-internal
consistency with the Duden-licensed `der Loop`. **Cost of being wrong:** 10 occurrences in 2 files, and a
mismatch with whatever slice B/D bind for `loop` — which is exactly why it should be ruled **with** those
slices at the merge, not independently.

**N3 — the three sharding compounds: `Tensor-Parallelität`, `Pipeline-Parallelität`, `Daten-Parallelität`.**
No German source attests the specific fusions; the **head** is corpus-attested and the **pattern** is legal.
The only real question is spelling uniformity, and it is a taste call dressed as a rule. Recommendation:
**hyphenate all three**, first mention with the English in parentheses. **Cost of being wrong:** cosmetic —
a mixed set (`Datenparallelität` beside `Tensor-Parallelität`) reads as sloppiness rather than as an error.

**N4 — `die Inferenz-Engine` on a single Stilfamilie.** Both runs measured `Inferenzserver` at zero; the
attested alternative rests on heise+iX, i.e. one house. No cheap research closes this — the decisive article is
behind heise+. Recommendation: **ship `die Inferenz-Engine` with a first-mention parenthetical
*(inference server)*** and rebuild the two sentences where the English contrasts *server* with *engine*.
**Cost of being wrong:** 19 occurrences across 4 files including the part overview; but the fallback
(`der Inferenzserver`) is a coinage with a measured zero, so the risk is *asymmetric in favour of the attested
form*. ⚠ **Do not let run 2's coinage reach the renderers as if it were evidenced** — run 2 itself says so.

**N5 — `das Autoscaling` on one house.** Recommendation: **bind it**, lead verbally in headings. The genitive
and dative plural are marked in the source, which is the hard part. **Cost of being wrong:** 5 occurrences in
2 files — the lowest-stakes of these five.

---

## 8. WHAT THIS PASS COULD NOT DO

- **I did no new lexicographic research, by design.** Every external attestation in this ledger comes from one
  of the two runs. Where they disagreed on a source's content I could not adjudicate the source itself — only
  its **kind** (case-marked vs nominative-only; single house vs several; dictionary vs encyclopedia vs press).
  The one place this bites is **D2 (`event loop`)**: I resolved a genuine gender split on structural grounds,
  not by reading INNOQ and informatik-aktuell myself.
- **The two runs share a method, and therefore share a blind spot.** Both attested overwhelmingly by
  **full-text extraction plus regex** — i.e. by strings. Run 1 says so explicitly and names the three rows most
  exposed (`warm`, `capacity`, `scheduling` — the three where it ships rebuilds rather than terms). **Their
  agreement on those rows is worth less than it looks**, and I have not upgraded any of them on agreement alone.
  D9 is the proof that the shared blind spot is real: they converged on a banned metaphor.
- **`die GPU` remains a single-register row** even though it is the slice's most frequent term. The shipped
  corpus contains **zero** GPUs, so #328 could not help here. This is the one high-frequency row where the
  ledger's confidence is procedural rather than evidential — flagged `THIN×2` for exactly that reason.
- **`Prefill`, `Decode` and `warm` are honestly open.** Neither run found an article-bearing German sentence,
  and I did not coin one. The Kompositum/rebuild solution **is the ruling**, not a stopgap — but it is not
  evidence either.
- **I could not verify the runs' German-language sources are still live or quoted in full.** Where a run quotes
  a sentence, I treated the quotation as accurate; that is an assumption, and run 2's own DWDS re-count (C2)
  shows the assumption is not free.
- **The corpus pass sees Parts I + II only.** A term whose German is decided for the first time in Part III has
  no precedent to find, which is most of the serving vocabulary (`GPU`, `Event-Loop`, `Cold Start`, `Prefill`,
  `Decode`, `Auslastung`, `Autoscaling` all = 0 shipped). #328 pays for the *shared* vocabulary — `Worker`,
  `Durchlauf`, `Parallelität`, `Batch`, `Durchsatz`, `Kapazität`, `Container`, `Prozess`, `Thread`, `Laufzeit` —
  and for those ten it paid very well.
- **Cross-slice rows I state a position on but do not merge:** `snapshot` — in slice A it is a *saved instance
  state* in the cold-start/warm-pool sentence, **not** the pinned model version and **not** the metaphorical
  `Momentaufnahme` the baseline found shipped; slice E owns the word and slice A should not spend it.
  `queue`/`budget` — I use the canon incumbents (`die Queue` WEAK; „das Budget aufbrauchen") without reopening
  them. `lever`/`Hebel` — not in my terms; the baseline's corpus precedent stands.
- **Not touched:** `Little's Law`, `admission control`, `backpressure`, `load shedding`, `scale-to-zero`,
  `TTFT`, `SSE`, `quantisation`, `Managed Endpoint`, `Provisioned Throughput`, `Instrumentation`. They border
  this slice, already sit in `rag.md` §2/§3, and are not slice A's head terms.
