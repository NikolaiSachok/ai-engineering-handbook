# LEDGER-G — binding ledger, slice G (the partition hole), German RAG wave 3 / Part III

Stage 1 of Gate 6.5. Inputs: `OUT-G-run1.md` (846 lines, read in full), `OUT-G-run2.md` (354 lines, read
in full), `dewave3-concord-G.txt`, `REFERENTS-baseline-verdicts.md`, and my own greps over the 27 shipped
German pages (issue #328). I did no new lexicographic research; every external attestation below is one of
the two runs', attributed. Every count marked `CORPUS(n)` is one I ran myself in this pass.

---

## 0. The finding this slice exists to produce, stated before the table

Slice G exists because A–F were drawn from a frequency count and left ~42 term-shaped head words
unassigned. **A term nobody was assigned is invisible to every doubled run** — both runs of every slice
agree it was not theirs, and that agreement is indistinguishable from coverage. Doubling protects against
a wrong answer; it does nothing about a missing question.

**This pass found the same shape one level down, inside slice G itself, and it is the transferable
result:** the wave's method greps *the English loan* in the shipped locale to decide whether a field has
an incumbent. Five fields were declared zero-incumbent on that basis — `Perimeter`, `Souveränität`,
`Residency`, `Managed`, `Enterprise`. **Two of the five are wrong.**

- **`Managed`.** `grep -i Managed i18n/de/` → **0**. `grep -i verwaltet` → **9**, inflected, attributive,
  in the exact construction Part III needs („semantisches RAG als **verwalteter Baustein**").
- **`Enterprise`.** The one shipped hit is not the `Gemini Enterprise Agent Platform` brand run1 recorded —
  it is the UI label **`Enterprise-Reifegrad`**, i.e. the German-hyphenated compound form both runs
  independently recommend. The field had an incumbent *and it was the recommended one.*

Three of the five are genuine zeros and I confirmed them: `Perimeter` **0**, `Souverän*` **0**,
`Residenz`/`Residency` **0** (plus `Compliance` 0, `Serverless` 0, `Proxy` 0, `Exporter` 0).

The corpus had answered two of the five questions in German, so the English probe could not see them.

> **A zero on the loan is not a zero on the referent.** The probe that declares a gap must be run in the
> target language, or it manufactures the gap it then goes and fills with research. This is the third wave
> of the "unapplied, not incomplete" pattern (`Fehlerbild`, `Dashboard`, `Hebel`) — but the first time the
> *instrument* produced the appearance of absence rather than a lookup failing.

The same probe error is why both runs missed `frontier` (§3, D-06), and it is why I re-ran every row
against the corpus before ruling.

**Second, smaller instance, caught in my own hands:** my first context grep for `Leitung` used
`grep -ohE ".{25}Leitung.{25}"` and returned six hits, all substrings of *Anleitung / Weiterleitung /
Einleitung / Ableitung* — and **silently dropped the one occurrence that matters**, because
`…über die Leitung geschickt.` has fewer than 25 characters after the match. A trailing-context matcher is
a narrowing matcher. That is the wave-2 defect for the fifth time in this project, this time in the
verification of the verification.

---

## 1. Binding table

`Class`: 1 = identifier/untouchable · 2 = kept-EN loan · 3 = German-led (first-mention gloss) · 4 = fully
German. `Status`: BOUND · CORPUS PRECEDENT · OPEN · THIN×2. `Evidence`: CORPUS(n) = my grep over the 27
shipped German pages · AGREED×2 · RECONCILED · THIN×2 · COINED (probation).

### 1a. Rows the shipped corpus settled (do not re-derive, do not re-research)

| Terminus | German | Class | Status | Artikel/Plural/Genitiv | Kollokation | ⛔ rejected | Evidence |
|---|---|---|---|---|---|---|---|
| **managed** (attributive) | **verwaltet** (flektiert) | 3 | **CORPUS PRECEDENT** | adj., strong/weak endings | „semantisches RAG als **verwalteter Baustein**"; „eine **verwaltete** RAG Engine"; „auf **verwaltetes** RAG" | ⛔ run1's ban on attributive `verwaltet` — overturned, see D-01 | **CORPUS(9)**, `real-agents.md:103,107,112,113,182` |
| **managed** (self-host pole) | **der Eigenbetrieb** — *bound, never bare* | 3 | **CORPUS PRECEDENT + BOUND** | der Eigenbetrieb, des Eigenbetriebs | „die Wahl zwischen **Eigenbetrieb** und fremder API"; „**Eigenbetrieb** (Datenschutz)" | ⛔ bare `Eigenbetrieb` in the sovereignty pages (municipal legal form — run1 §C4, Duden+DWDS+de.wp unanimous) | **CORPUS(3)**, 2 of 3 already bound against an explicit API/privacy pole |
| **frontier** | **das Spitzenmodell · die Spitzenmodelle** | 3 | **CORPUS PRECEDENT** | das Spitzenmodell, des -modells, die -modelle | „**Spitzenmodelle** kommen auf unter 50 % Erfolg"; „bei τ-bench fallen die **Spitzenmodelle** schon einmalig unter 50 %" | ⛔ `Grenzmodell` (0, both runs) | **CORPUS(2)** — `planning-loops/deep-dive.md:132,144`. **Both runs ⛔'d or dispreferred this word.** See D-06 |
| **roster** (the frame) | **die Momentaufnahme** + „die Kategorie überdauert" | 3 | **CORPUS PRECEDENT** | die Momentaufnahme, der -, die -n | „behandeln Sie die Einteilung als **Momentaufnahme**, die bereits altert"; „**Momentaufnahme** von Philosophien, nicht als haltbare Rangliste" | ⛔ **`die Aufzählung`** — the corpus uses it for *bullet lists* („**Aufzählungen** oder Tabellen"), a live collision | **CORPUS(5)** + baseline verdict (`Momentaufnahme` = metaphorical snapshot). Run1 right, run2 refuted |
| **uptime theatre** | **das Verfügbarkeitstheater** | 3 | **CORPUS PRECEDENT** | das -theater, des -theaters | „ist **Verfügbarkeitstheater**: eine Wand grüner Dashboards über einem Dienst, der … falsch liegt" | — | **CORPUS(1)**, `observability/deep-dive.md:95`. Run1 declared this unsolvable; it was already written |
| **uptime** | **die Verfügbarkeit** | 3 | **CORPUS PRECEDENT** + canon `_language.md` §9.3 | die Verfügbarkeit, der -, kein Pl. | „**Verfügbarkeit ist nicht Korrektheit**"; „**Verfügbarkeit** ist eine Eigenschaft des Dienstes" | ⛔ `die Betriebszeit` (duration, not reachability); ⛔ `die Uptime` | **CORPUS(3)** + AGREED×2. §9.3 rules it **verbatim on Part III's own English sentence** |
| **correctness** | **die Korrektheit** | 3 | **CORPUS PRECEDENT** | die Korrektheit, der -, Pl. meiden | „Faithfulness misst das Grounding, **nicht die Korrektheit**"; „**Für die Korrektheit** braucht es …" | ⛔ *Richtigkeit*, ⛔ *Genauigkeit* (= accuracy) | **CORPUS(8)**, AGREED×2 |
| **org-level** | **unternehmensweit** | 3 | **CORPUS PRECEDENT** | Adjektiv/Adverb | „**unternehmensweite** Richtlinien"; „Diese Mechanismen **unternehmensweit** zu betreiben" | ⛔ **`organisationsweit`** — **CORPUS(0)**; ⛔ `organisationsübergreifend` (means *between* organisations — run1) | **CORPUS(2) vs 0.** Both shipped sentences **forward-reference this very lesson**. Run1 right, run2 refuted |
| **attribution** (verb) | **zuordnen** (+ Dativ) | 4 | **CORPUS PRECEDENT** | — | „Versehen Sie die Spans mit dem Feature, dem **Mandanten**, der Route und dem Modell … **zuordnen**"; „erst erkennen, dann **zuordnen**" | ⛔ `die Attribution` (psychology + marketing + IT-security attribution — AGREED×2, three false owners) | **CORPUS(10)**, incl. the exact source paragraph Part III links to |
| **attribution** (noun) | **die Kostenzuordnung** | 3 | **BOUND** (follows the shipped verb) | die Kostenzuordnung, der -, die -en | „**Die Kostenzuordnung** muss auf der Anwendungsschicht entstehen"; adverb **verursachungsgerecht** (run1, 20 hits, all cost accounting — keep) | ⛔ run1's `die Kostenzurechnung` — see D-04 | **RECONCILED**; noun itself CORPUS(0), chosen for morphological agreement with the shipped verb |
| **tenant** | **der Mandant** (n-Dekl.) | 3 | **CORPUS PRECEDENT** | **des Mandanten**, dem/den Mandanten, die Mandanten | „mit dem Feature, **dem Mandanten**, der Route"; „mehrere **Mandanten** bedient"; multi-tenancy → **die Mandantenfähigkeit** | ⛔ „des Mandants" ✗ (n-Dekl., the `Agent` trap repeated); ⛔ `der Tenant`; ⛔ `der Mieter` | **CORPUS(3)** + AGREED×2 (DWDS masc.; de.wp lemma `Mandantenfähigkeit`) |
| **isolation** | **die Isolation** — **als Genitivattribut, nie nackt** | 3 | **CORPUS PRECEDENT** | die Isolation, der -, Pl. meiden | „die **Isolation der Kontexte**" (10/10 shipped are bound); „die Isolation **der Sitzungen**", „**zwischen Mandanten**" | ⛔ `die Isolierung` — **CORPUS(0)**; insulation/IR-act. ⚠ bare `Isolation` = Dominanzfalle (*Isolationshaft*) | **CORPUS(10), 10/10 bound.** The binding habit *is* the ruling |
| **dial** | **der Regler** | 3 | **CORPUS PRECEDENT** | der Regler, des Reglers, die Regler | **BOTH verbs are shipped**: „an dem Sie *nachträglich* **drehen**" (×3) **and** „ein Regler, den Sie auf die Aufgabe **einstellen**" | ⛔ `die Raste`/`die Rastung` (run1); ⛔ `der Schalter` (binary) | **CORPUS(6).** Run2's „`einstellen`, **nicht** `drehen`" is overturned by the corpus |
| **policy dial / notch** | **die Stellschraube** · notch → **die Stufe** | 3 | **CORPUS PRECEDENT** | die Stellschraube, der -, die -n | „Die **Stellschrauben** dafür sitzen beim Anbieter"; „Gemini macht aus der **Stellschraube** eine Zahl" | — | **CORPUS(3).** ⚠ Run2 claimed `Stellschraube` is reserved for `lever`; **`lever` is `der Hebel` — CORPUS(15) + the baseline's explicit verdict.** Run2's premise is false, see D-07 |
| **ladder / rung** | **die Leiter** · **die Sprosse** · verb **erklimmen** | 3 | **CORPUS PRECEDENT** | die Leiter, der -, die -n; die Sprosse, der -, die -n | „nicht **die erste Sprosse einer festen Leiter**"; „auf **der obersten Sprosse**"; „wie **die Leiter** gezeigt hat" (anaphoric) | ⛔ `die Stufenleiter` (dated / rank order) | **CORPUS(8 Sprosse + 8 Leiter)**, AGREED×2. ⚠ homograph `der Leiter` (a person / an electrical conductor) — keep in nom./akk. or dative-fem, prefer „die Sprossen **dieser** Leiter" |
| **backend** | **das Backend** | 2 | **CORPUS PRECEDENT** | des Backends, die Backends | „mit **einem dauerhaften Backend**"; „das ADK **tauscht das Backend aus**" — attested verb **austauschen/tauschen** | ⛔ spelling `Back-End` | **CORPUS(12)** + Duden/DWDS Neutrum, AGREED×2 |
| **adapter** (pattern/software) | **der Adapter** | 2 | **CORPUS PRECEDENT** | des Adapters, **Nullplural die Adapter** | „**keinen Adapter** je Framework" (Akk.); „damit Sie **die Adapter** nicht von Hand schreiben" | ⛔ `das Adapter`; ⛔ `die Adapters`; ⛔ `Adaptermuster` (0) | **CORPUS(2)**, AGREED×2 |
| **wrapper** (structural) | **der Wrapper** | 2 | **CORPUS PRECEDENT** | des Wrappers, Nullplural die Wrapper | „dazu **einen** `AgentTool`-**Wrapper**" (Akk. masc.) | ⛔ `die Hülle`, `die Verpackung`, `der Aufsatz` (= essay), `der Umschlag` (already = *envelope* in Part II) | **CORPUS(1)**, case-marked. Evaluative sense → **OPEN**, D-08 |
| **benchmark** | **der Benchmark** | 2 | **CORPUS PRECEDENT** | **des Benchmarks**, die Benchmarks | „**einem Benchmark** aus Tool, Agent und Nutzer" (Dat. — **excludes feminine**); „Auf **den Benchmarks** des Papers" | ⛔ `die Benchmark` for the computing sense (feminine hits are finance) | **CORPUS(4), one case-decisive token neither run cited.** Upgrades run1's self-declared WEAK |
| **capability** | **die Fähigkeit** (meist Plural) | 3 | **CORPUS PRECEDENT** + canon §1.1.g | die Fähigkeit, der -, die -en | „eine **Fähigkeit**, die das Framework bereitstellt"; „die **Fähigkeiten** eines Servers" | ⛔ `die Capability`; ⛔ `die Fähigkeitskategorien` (stacked coinage) | **CORPUS(21)** + AGREED×2. Two added branches, §2 card K |
| **sample** | **die Stichprobe** | 3 | **CORPUS PRECEDENT** | die Stichprobe, der -, die -n | „messen Sie **an einer Stichprobe**"; „solange keine menschliche **Stichprobe** …"; verb **ziehen** | ⛔ `das Muster`, `das Sample`, `sampeln` (Musik-Falle) | **CORPUS(3)** + AGREED×2. Split against settled `das Sampling` — card S |
| **refusal** | **die Antwortverweigerung**; Verb **verweigern + Akk.** | 3 | **CORPUS PRECEDENT** | die Antwortverweigerung, der - | H2 „**## Die Antwortverweigerung ist gewollt, keine Fehlfunktion**"; „eine **erlaubte Antwortverweigerung**" | ⛔ bare `die Verweigerung` (Dominanzfalle §1.1.f); ⛔ `die Verweigerungsrate`/`Ablehnungsrate` (both unbelegt) | **CORPUS(5)** + AGREED×2 |
| **refusal rate** | **der Anteil verweigerter Antworten** | 3 | **CORPUS PRECEDENT** (prescribed rebuild is live) | — | „…, **der Anteil verweigerter Antworten**, wie oft die Guardrails eingreifen" | — | **CORPUS(1)** + `rag.md` §3 |
| **refusal path** | **der Weg zur Antwortverweigerung** | 3 | **BOUND** (built from settled parts) | — | „Das Retrieval braucht **einen vorgesehenen Weg, die Antwort zu verweigern**" | ⛔⛔ `der Refusal-Pfad` — **`Pfad` is bound to the agent-trajectory sense, CORPUS(8)** | **AGREED×2 + CORPUS(8)**. Both runs found this collision independently |
| **enterprise** (attributive) | **`Enterprise-`, nur durchgekoppelt** | 2 | **CORPUS PRECEDENT** | gender from the head noun | shipped UI label „**Enterprise-Reifegrad**: Audit, Herkunft, Vorgaben"; canon `ai-sdlc.md` §2 „**Enterprise bleibt kept-EN**" | ⛔ free `das/die Enterprise` with an article (0 on every tier, AGREED×2) | **CORPUS(1 compound).** ⚠ Run1's claim that all shipped hits are the `Gemini Enterprise Agent Platform` brand is **factually wrong** |
| **enterprise** (the company) | **das Unternehmen** | 4 | **CORPUS PRECEDENT** | das Unternehmen, des -s, die - | „ob **Ihr Unternehmen** zustimmen darf" | ⛔ `Großunternehmen` as a rendering of the maturity tier | **CORPUS(22)** |
| **offering** | **das Angebot** | 4 | **CORPUS PRECEDENT (thin)** | des Angebot[e]s, die Angebote | „jetzt fertig eingebaut **im Angebot**"; „**souveräne Cloud-Angebote**" | ⛔ `das Offering`; ⛔ `die Offerte` (narrow commercial bid); ⛔ `die Lösung` | **CORPUS(1)** + AGREED×2 (DWDS Neutrum; BSI „ein Cloud-**Angebot**") |
| **quantisation** | **die Quantisierung** | 3 | **BOUND** (existing canon row, reused) | die Quantisierung, der - | „die **Quantisierung** des KV-Cache" | ⛔⛔ **`die Quantifizierung`** — named false friend in the canon twice | AGREED×2, canon `_language.md` §1.1.g + `rag.md` §2. **CORPUS(0)** — the row is canon-borne, not corpus-borne |
| **relevancy** | Ragas metric names = **Klasse 1**; the Part I concept = **Answer-Relevance** (kept-EN, artikelfrei) | 1 / 2 | **BOUND** | „der **Answer-Relevance**-Wert" | „**Der Answer-Relevance-Wert** beurteilt ausdrücklich **nicht** die Korrektheit" | ⛔ `die Antwortrelevanz` (canon: „nicht abwegig, nur unbelegt"); ⛔ German-ising the Ragas names | **CORPUS(1)** + AGREED×2. ⚠ The sentence is a *rename note* — both English names stay, only the explanation is German |
| **guard** (verb) | **schützen** (general) · **absichern** (access) | 4 | **CORPUS PRECEDENT** | — | „die Evaluierung misst, die **Guardrails schützen**"; „die Leitplanken, die es **absichern**"; „die Zuverlässigkeitsseite **wacht darüber**" | ⛔⛔ **`bewachen`** (DWDS Wortprofil entirely human-guard: *Leibwächter, Kaserne, Hühnerstall*) — AGREED×2 | **CORPUS(2 constructions)** + AGREED×2 |
| **Guard** (product/code) | `Llama Guard`, `Granite Guardian`, `Guard()` | 1 | **BOUND** | untranslated, uninflected | „Sie hängen einen Validator mit `.use()` an einen `Guard`." | ⛔⛔ merging with `Guardrails` — that row is **Plural only, Singular OPEN**; a „Guard" invents the banned singular | AGREED×2 |
| **isolation → network** | **die Netztrennung** | 3 | **BOUND** | die Netztrennung, der - | „Der Verkehr zum Modell verlässt das öffentliche Internet nie." | ⛔⛔ `die Netzwerkisolierung` (de.wp 0, BSI 0) | run1 only, uncontradicted; BSI 18 / de.wp 29 |

### 1b. Rows where the two runs disagreed and I resolved them

| Terminus | German (RULED) | Class | Status | Kollokation | ⛔ rejected | Evidence |
|---|---|---|---|---|---|---|
| **wire** — 4 senses | see card **W** (§2). One string per branch, none of them a noun-for-noun swap | 3 | **BOUND (a,b,c) / RECONCILED (d)** | see card | ⛔ the whole `Leitung` **word field** in the locative; ⛔ `Draht`; ⛔ `das Drahtformat` (0); ⛔ „ein Protokoll sprechen" (0) | **RECONCILED (run1 vs run2, I chose run2 on the verb, run1 on the standard).** Corpus: free `Leitung` **CORPUS(1)**, directional only; `Draht` bare **CORPUS(0)** |
| **to wire (together/into)** | **verdrahten / die Verdrahtung** — *licensed, with one narrow ban* | 4 | **CORPUS PRECEDENT** | „**Verdrahten Sie** diese Teile zum kanonischen ReAct-Agenten"; „die **Verdrahtung** der Tool-Calls"; „wie Subagenten miteinander **verdrahtet** sind" | ⛔ **`fest verdrahtet`** — that fixed form means *hardcoded* and inverts any sentence about swappability | **CORPUS(5)**, `orchestration-frameworks/*` ×5. **Run1's blanket ⛔ is overturned**, D-02 |
| **ceiling** | **die Kapazitätsgrenze** (physical limit) · **die Grenze** (anaphoric) · **ausgereizt** (technique exhausted) | 3 | **DECISION — see §7 D-A** | „an seine **Kapazitätsgrenze stoßen**"; „Prompting und RAG sind **ausgereizt**" | ⛔⛔ **`die Decke`** (*durch die Decke gehen* = skyrocket — inverted polarity), AGREED×2; ⛔ `der Grenzwert` | **RECONCILED, and NOT clean** — the corpus does **not** support run1's premise. See D-A |
| **floor** | **die Untergrenze** (both senses); Kartenlabel **Score-Untergrenze** | 3 | **DECISION — see §7 D-A** | „Setzen Sie **eine Score-Untergrenze** hinter die Stufe, deren Scores etwas bedeuten"; „…2 CPU-Kerne und 4 GB RAM **als Untergrenze**" | ⛔ `der Boden`; ⛔ bare `die Schwelle` (canon: Eisenbahnschwelle); ⛔ `Mindestscore`, `Mindestrelevanz` (0) | **RECONCILED (I chose run2's `Untergrenze` over run1's `Mindestwert`)**, reasons in D-A |
| **residency** | **die Data Residency** (the *term*, fem., obligatory first-mention gloss) · **der Speicherort** (the plain location, running prose) | 2 / 3 | **DECISION — see §7 D-B** | „**die Zusicherung zur Data Residency**"; „**Anforderungen an den Speicherort**"; „global heißt ausdrücklich: **keine Zusicherung zum Speicherort**" | ⛔⛔ **`die Datenhoheit`** = *sovereignty* — collapses the distinction the whole section stands on (AGREED×2); ⛔ `die Residenzgarantie` (0, and `Residenz` = palace); ⛔ `die Datenlokalisierung` (a statutory obligation, not a product property) | **RECONCILED.** `der Speicherort` is the **AGREED×2 core**; only the term-level form was disputed. CORPUS(0) for everything |
| **serverless** | **kept-EN, gebunden**: `Serverless GPU`, `die Serverless-Laufzeitumgebung`; **`serverlos` only next to an explicit cloud head noun** | 2 | **OPEN (incumbent held: kept-EN; closes when a heise/iX sentence has `serverlos` + an unambiguous FaaS head noun)** | „**Serverless GPU** mietet Kapazität sekundenweise" | ⛔ `das Serverless` with an article (0, AGREED×2); ⛔ bare `serverlos` — de.wp majority = **peer-to-peer, no server at all** (run1's measurement) | **RECONCILED.** Run1 measured the homonym (18 hits, 1 cloud); run2 declared `serverlos` unbelegt without measuring. Run1's measurement is the better evidence and it argues *against* the free adjective. **CORPUS(0)** |
| **cross-region** | **prepositional/verbal rebuild**: „Datenverkehr **zwischen Regionen**", „**über Regionsgrenzen hinweg**" | 3 | **OPEN (incumbent held: the rebuild; closes when a heise/iX/c't sentence has `regionsübergreifend` on an IT noun)** | „die **Egress-Kosten zwischen Regionen**" | ⛔ `regionsübergreifend` as a running term — **the same 10 hits, read**: all urban planning / demography / tourism | **RECONCILED — the decisive case of the pass.** Both runs counted **10**; run1 read the sentences and found zero IT, run2 read the number and wrote WEAK. A count is not a reading |
| **air-gapped** | **physisch getrennt / die physische Trennung** (normative register) · **die Air-Gap-Umgebung** (trade register, compound only) | 3 / 2 | **BOUND, split by register; Genus of bare `Air Gap` stays OPEN** | „Netzsegmente **physisch trennen**"; „**per Air Gap getrennte** Installationen"; „eine **physisch getrennte** Umgebung" | ⛔⛔ **`luftgekapselt`** — 0 across five corpora (run1); ⛔ `der Luftspalt` (magnetics/plumbing, 206 hits); ⛔ bare `Air Gap` with an invented article | **RECONCILED (complementary, not contradictory).** Run1 supplies the BSI register, run2 supplies the loan + the honest „no case-decisive token" verdict. Take both. **CORPUS(0)** |
| **on-demand** | **`On-Demand-` as a kept-EN compound former** (`das On-Demand-Modell`); scaling sense → **bei Bedarf** | 2 / 3 | **BOUND** | „**On-Demand**-Instanzen"; „**bei Bedarf** hoch- und herunterskalieren" | ⛔ bare `On-Demand` as a free article-bearing noun (unattested — run1); ⛔ `bedarfsgesteuert` (logistics) | **RECONCILED.** ⚠ Run2's `auf Abruf` **is** shipped — **CORPUS(1)** — but for a *metaphor* („Meisterschaft **auf Abruf**"), not a pricing tier. Licensed as a paraphrase, refused as the term |
| **reserved** | vendor tier name → **Klasse 1** (`Reserved`); the property → **reserviert** (Partizip) + **Laufzeit/Rabatt**; „reserved for enterprise plans" → **den Enterprise-Tarifen vorbehalten** | 1 / 3 | **BOUND** | „einen **Rabatt gewähren auf**"; „**bleiben auf einem toten Worker reserviert**" | ⛔ **`reservierte Kapazität` as a TERM** — run1 measured **0**; run2 used it without measuring | **RECONCILED (I chose run1's measurement).** ⚠ Run2's real contribution is the *collocation* ban: „für Enterprise-Pläne reserviert" is an English scaffold; German is **`jemandem vorbehalten sein` + Dativ** |
| **frontier** | **das Spitzenmodell** (see 1a) | 3 | **CORPUS PRECEDENT — overrides both runs** | „die **Spitzenmodelle** hinken in souveränen Umgebungen hinterher"; degree sense → „die **Leistungsfähigkeit** der Spitzenmodelle" | ⛔ `das Frontier-Modell` as the running term (de.wp 0; run2's heise hits are real but the corpus has already ruled); ⛔ `Grenzmodell` | **RECONCILED against BOTH runs by CORPUS(2).** D-06 |
| **in-flight** | **laufend** — *but bound*: „die **bereits angenommenen** Anfragen" where *drain* is the verb | 3 | **OPEN (incumbent held: `laufend`; closes when a German Kubernetes/graceful-shutdown text renders *drain*)** | „jede **laufende Anfrage** hält KV-Cache-Blöcke"; „die **bereits angenommenen, noch nicht abgeschlossenen** Anfragen zu Ende bedienen" | ⛔⛔ `schwebend` (= *sub judice*, a fixed legal idiom — AGREED×2); ⛔ `in Flug`/`im Flug`; ⛔ `entleeren`/`abfließen` for *drain* | **RECONCILED.** ⚠ **CORPUS(20) for `laufend`, and that is the problem**: the corpus already runs it in two other senses (`laufende Kosten` = recurring, „am **laufenden** Verkehr" = live). A third sense on a loaded word — see D-C |
| **idle** | **im Leerlauf** (hardware state) · **ungenutzt** (capacity you pay for) | 3 | **BOUND** | „skaliert **im Leerlauf** auf null"; „nicht für **ungenutzte** Kapazität zahlen" | ⛔ `untätig` (animate, faintly blameworthy); ⛔ `im Ruhezustand` (= Suspend/Hibernate — a trap inside our own field, run2); ⛔ `brachliegen` | **AGREED×2.** ⚠ **CORPUS(0) — and I caught my own false positive**: my raw count returned 1, which is `leerlaufen` (a verb about the loop spinning). `idle` has no nominal incumbent |
| **exporter** | **der Exporter** — **compound head only** | 2 | **THIN×2** | „die **Exporter-Konfiguration**"; „**den** Exporter **konfigurieren**" | ⛔ `der Exportierer`, `das Ausgabemodul` | **THIN×2 + HOUSE.** No Duden/DWDS/de.wp lemma; DWDS redirects to **`Exporteur`** (a goods exporter — a named false friend). Masculine rests on the `-er` analogy (`der Worker` is WEAK for the same reason) and on run1's three heise tokens, all attached to *named* exporters. **CORPUS(0)** |
| **engine** | **die Engine** (feminin) · product names → **Klasse 1** | 2 | **CORPUS PRECEDENT (thin)** | „eine **verwaltete** RAG Engine" (weak attributive `-e` after `eine` ⇒ feminine); „**die Inferenz-Engine**" | ⛔⛔ **`der Motor`** for software — English-only metaphor, no DWDS example applies it to a program component (run1) | **RECONCILED.** ⚠ **Run1 recorded a null here — „all 12 shipped hits are `-Engineering` or brand" — and it is a fabricated absence.** `real-agents.md:107,360` carry a German feminine determiner + adjective. **CORPUS(2)** |
| **proxy** | **der Proxy** (network) · **die Ersatzgröße** (the stand-in metric) — **two words, mandatory split** | 2 / 3 | **BOUND** | „etwas **als Proxy für** etwas verwenden"; „eine verletzte **Ersatzgröße** für Qualität oder Kosten" | ⛔ `die Proxies` (0 — it is **die Proxys**); ⛔ `der Stellvertreterwert`/`-größe` (0); ⛔ running both senses on one German word | **RECONCILED (I chose run2's split).** Both found DWDS Bedeutung 2 = „Synonym zu Ersatzgröße"; run1 concluded one word suffices, run2 that the split is obligatory. **In a chapter dense with gateways and routers, `der Proxy` for a metric sends the reader to the network device.** Canon already lists `Proxy-Metrik` (`ai-sdlc.md` §1). **CORPUS(0)** |
| **perimeter** | **der Perimeter**, **des Perimeters** — gloss on first use | 2 | **BOUND** | **`innerhalb`/`außerhalb` + GENITIV**: „**innerhalb des eigenen Perimeters** betreiben"; „**am Perimeter**" | ⛔ `der Perimeterschutz` unqualified (BSI INF.1.A35 = **fences, lighting, Haustechnik**); ⛔ `die Perimetersicherheit`, `der Sicherheitsbereich`; ⚠ `die Netzgrenze` = topological only | **AGREED×2, and both runs cite the same iX headline + the same DWDS sense 3.** ⚠ **THIN on one axis:** DWDS *defines* sense 3 as a **Vorrichtung** (a device) while every quoted Beleg means the **boundary** — run2's honest note. No collision with `Vertrauensgrenze`/`Sicherheitsgrenze` (run1 §C3, checked and clean). **CORPUS(0)** |
| **sovereignty** | **die (digitale) Souveränität** — lowercase adjective; **die souveräne Cloud** (market register) | 3 | **BOUND (term) / OPEN (capitalisation)** | *digitale Souveränität* **erreichen/stärken/wahren**; „**der Preis der Souveränität** bemisst sich in …" | ⛔ free-form adjectival `souverän` (DWDS sense 3 = *masterful, commanding* — „souverän gewinnen"); ⛔ `die Datenhoheit`; ⛔ `die Hoheit` bare; ⛔ `die souveräne Region` (de.wp's one hit is **constitutional geography**) | **AGREED×2 on the noun.** ⚠ **THIN×2 on register:** run1 measured that **BSI never writes `souveräne Cloud`** (`Souveränität` = 0 in C5) and prefers `Souveränitätseigenschaften` / `selbstbestimmt genutzt`. Pick one register per page. **CORPUS(0)** |
| **jurisdiction** | **die Gerichtsbarkeit** (whose authority) · **die anwendbare Jurisdiktion** (which law reaches) | 3 | **BOUND** | **`unterliegen` + DATIV**: „**der** US-Gerichtsbarkeit **unterliegen**" | ⛔ **`der Gerichtsstand`** — confirmed false friend, it is *venue* | **THIN×2** — run1 only, and it rests **entirely on BSI C5 (BC-01/BC-05)**. Per brief §2 that is worth *less*, not more. Counter-check owed: a heise/iX full-text count |
| **compliance** | **die Compliance**, Gen. *der Compliance*, Plural meiden — **prefer compounds** | 2 | **BOUND / THIN on the bare noun** | „die **Compliance-Anforderungen** erfüllen"; „**die Einhaltung** + Gen." | ⛔ `die Regelkonformität` (a dictionary-shaped calque, BSI 0); ⛔ `die Gesetzestreue` | **AGREED×2** (Duden + DWDS feminine, Wirtschaftsjargon). ⚠ **Two live cautions, both from run1:** Duden lists the **medical** senses first (patient adherence, lung distensibility); **BSI never bares it** (0 bare, `Compliance Management` 19). **CORPUS(0)** |
| **governance** | **die Governance**, Gen. *der Governance*, **nur Singular** | 2 | **BOUND / THIN on register** | „spend governance" → **die Governance der Ausgaben** (Genitiv, **nicht** ein Kompositum); „Die **Governance** ist die Schicht darüber." | ⛔ `die Governances`; ⛔ `die Spend-Governance`; ⛔ `das Regelwerk` (the artefact), `die Aufsicht` (a body), `die Unternehmensführung` | **RECONCILED.** Run2 SETTLED on DWDS; **run1's BSI counter-check is the finding and it survives**: BSI Zero-Trust **0**, Kompendium **2** (both the same sentence), Duden flags the bare form *„besonders schweizerisch"*. **This is consultancy German, not standards German** — right for a spend chapter, wrong in a controls passage. **CORPUS(7)**, all AI-SDLC sidebar labels, artikellos → no gender from the corpus |
| **identity** | **die Identität**; IAM → **das Identitäts- und Berechtigungsmanagement (IAM)**; the AgentCore component `Identity` → **Klasse 1** | 3 / 1 | **BOUND** | „ein zentrales **Identitätsmanagement** aufbauen"; „hinter **IAM** und OAuth" | ⛔ `die Identitäts- und Zugriffsverwaltung` — **run1's own proposal, refuted (de.wp 2, BSI 0)**; ⛔ `die Identity` with a German article | **RECONCILED (complementary).** Run1 supplies the BSI Baustein title (ORP.4, 69×) — use the long form where IAM means identity **plus** authorisation, which is Part III's sense. Run2 supplies the class-1 split for the product component. **CORPUS(2)** |
| **regulated** | **`in regulierten Branchen` / `regulierte Bereiche`** — the **collocation** is the unit | 3 | **BOUND** | „**in** regulierten Branchen **tätig sein**" (Dat. Pl., usually article-free); „**stark reguliert**" | ⛔⛔ **`regulierte Workloads`** — DWDS's `regulieren` = *to adjust/tune*, its only marked domain sense is *settling an insurance claim*. **The supervision meaning lives in the NOUN, never in the adjective alone** | **AGREED×2** on `stark regulierte Branchen`; run1 adds four independent converging sources and the semantic argument. **CORPUS(0)** |
| **finops** | **FinOps — artikellos**, compound-preferring; gloss once as **das Cloud-Kostenmanagement** | 2 | **BOUND** | „**Bei FinOps** geht es um Menschen, Daten und Werte"; „**der FinOps-Ansatz**" | ⛔⛔ **`das FinOps` / `die FinOps`** — zero attestations, do not assign a gender; ⛔ `der Finanzbetrieb`, `die Finanzoperationen` | **AGREED×2** — the `Backpressure` class (`_language.md` §1.1.d: „in jedem nativen Beleg ARTIKELLOS"). **CORPUS(0)** |
| **chargeback** | **kept-EN, Genus NICHT setzen**; corpus form is the PP „**beim Chargeback**"; compound `das Chargeback-Modell` | 2 | **OPEN (Genus) — incumbent held: artikellos; closes on one nom./akk. case-marked German token** | „**Beim Chargeback** stellt man die Kosten … tatsächlich **in Rechnung**" | ⛔⛔ `die Rückbelastung` (the German banking word for *card* chargeback — imports the sense you are escaping); ⛔⛔ `die Kostenumlage` (an `Umlage` is a pro-rata spread of costs that could **not** be traced — the inverse of the point) | **RECONCILED (I chose run2's restraint).** Run1 ruled **die (IT-)Leistungsverrechnung** on Gabler + de.wp 57. That is a real German term — **but it renames the referent**: Part III contrasts *showback* (report only) with *chargeback* (actually bill), and `Leistungsverrechnung` covers both. Keep the loan, offer `IT-Leistungsverrechnung` as the one-time gloss |
| **showback** | **kept-EN, Genus NICHT setzen**; „**beim Showback**", compound `das Showback-Modell` | 2 | **OPEN (Genus) — same closing condition** | „**Beim Showback** bekommt jede Mannschaft ihren eigenen Verbrauch ausgewiesen, während die Kosten auf einem zentralen Budget bleiben." | ⛔ `der Kostenausweis` (de.wp 1, an 1838 building-cost statement); ⛔ `die verursachungsgerechte Kostenausweisung` (0) | **RECONCILED.** Run1 found exactly **one** flexion-bearing token (a genitive) and proposed `das Showback`; one token is not a paradigm. ⚠ Both runs note **every German source glosses it** — treat as a term of art needing a definition |
| **make-or-buy** | **die Make-or-Buy-Entscheidung / -Frage**; the concrete software instance → **selbst betreiben oder einkaufen** | 2 / 4 | **BOUND** | „eine Make-or-Buy-Entscheidung **treffen**"; „**vor** einer … **stehen**" (Dat.) | ⛔ `Eigenfertigung oder Fremdbezug` for software (*Fertigung* = manufacturing of physical goods) | **AGREED×2** (de.wp `insource` 45 in both runs). ⚠ Run1's honest caveat stands: **neither loan is quite Part III's contrast** — the corpus opposes *self-hosting* to *buying SaaS*, not *building* to *buying*. `selbst betreiben` is the accurate verb and it dovetails with `der Eigenbetrieb` |
| **multi-cloud** | **das Multi-Cloud-Gateway** (Durchkopplung § 44(1)) | 2 | **BOUND** | „**hinter einem Multi-Cloud-Gateway** portabel bleiben" | ⛔ `Mehrwolken-`; ⛔ spaced `Multi Cloud Gateway` | **AGREED×2**; gender inherited from `das Gateway` (§6 canon gap). **CORPUS(3)** for bare plural `Gateways` — no gender shown, so the gap is real |
| **egress** (in `cross-region egress`) | **die Egress-Kosten / -Gebühren** (Plural, **compound only**) | 2 | **BOUND** | „die **Egress-Kosten zwischen Regionen**" | ⛔⛔ **`die Datenausleitung`** — both de.wp hits are **surveillance/exfiltration** (Port-Mirroring, Patientenakte); ⛔ `die Datenausgangsgebühr` (0) | run1 only (three native tokens, two publishers), uncontradicted. ⚠ **Bare `Egress` is owned elsewhere: 45 de.wp hits, none cloud billing** (MPLS routers, egress filtering, coax signal leakage) |
| **break-even** | **der Break-even / der Break-even-Point** | 2 | **BOUND** | „**den Break-even erreichen**"; „die **Auslastungsschwelle, ab der eine Reservierung günstiger ist**" | ⚠ ⛔ **`die Gewinnschwelle`** — right word, wrong sense: it is a *minimum sales quantity*; Part III's break-even is a **crossover of two cost curves** with no `Gewinn` in it | run1 only (Duden lemma, masc.), uncontradicted |

---

## 2. Sense cards

Each card gives the question to ask **before writing the word**, and a worked German **sentence** per
branch. The measured finding this obeys: sense splits that ship a *sentence* survive contact with prose;
ones that ship only a *word* get dodged.

### Card W — `wire` (4 referents; 11 tokens, not 8)

**Frage vor dem Schreiben:** *Meine ich (a) den Standard, auf den sich beide Seiten einigen, (b) das
serialisierte Nachrichtenformat, (c) „gerade unterwegs", oder (d) das Verb „verbinden"?*

- **(a) der Kompatibilitätsvertrag** — „the de facto **wire** standard", „speaks one **wire** standard",
  „behind one OpenAI-compatible **wire**".
  → **„Die OpenAI-kompatible Schnittstelle hat sich als De-facto-Standard für LLM-Endpunkte durchgesetzt."**
  → **„… ein vereinheitlichender Router, der nach außen eine einzige, einheitliche Schnittstelle anbietet."**
  → **„Ein Multi-Cloud-Gateway hält Sie hinter einer einzigen OpenAI-kompatiblen Schnittstelle portabel."**
  ⚠ **`Nachrichtenformat` is too narrow here** — a wire *standard* covers the endpoint, the verbs and the
  error shapes, not only how a message is serialised. This is the branch wave 2 never had to rule.
  ⛔ **„ein Protokoll sprechen"** — 0 German attestation, an English collocation scaffold (run2, measured).
- **(b) das Nachrichtenformat** — „They also agree on the **wire**."
  → **„Und auch im Nachrichtenformat stimmen sie überein."**
  Wave 2's ruling, unchanged, **CORPUS(6)**. Reuse verbatim; do not re-coin.
- **(c) schon unterwegs** — „the 200 is already on the **wire**".
  → **„Der Statuscode 200 ist längst übertragen, wenn die Generierung auf halber Strecke abbricht."**
  ⛔⛔ **„steht schon auf der Leitung"** — the fixed idiom. **This is the single highest-risk site in Part III.**
- **(d) das Verb** — „the tools **wire** together", „**wire** into a single stack", „**wired** to its tools",
  „**wired** into CI", H2 „The stack, **wired**", „**wire** drift thresholds to trigger retraining".
  → **„… und wie die Werkzeuge für Evaluierung, Guardrails und Observability zu einem einzigen Stack
  verdrahtet werden."**
  → **„… eine RAG-Pipeline, die zu einem Agenten gewachsen ist und an ihre Tools angebunden wurde."**
  → **„… jetzt in die CI eingebunden, mit einem Rot-Grün-Urteil."**
  → **„Schwellenwerte für Drift an ein Retraining koppeln"** (for `wire X to Y`, the verb is **koppeln + an**).
  → H2 **„Der Stack, verdrahtet"**.
  ⛔ **`fest verdrahtet`** — and *only* that fixed form. It means *hardcoded*, so it inverts the exporter
  sentence („an **exporter configuration change**, not an application rewrite").

> **Why this card and not a table row.** Three of the four branches are not a word choice at all — they are
> a preposition, a case and a verb. `Leitung` is *correct German for the referent* in branch (c) and wrong
> because of what stands next to it: **`über die Leitung` (Akk., directional, with *schicken*) is ordinary
> transmission German; `auf der Leitung` (Dat., static, with *stehen/sitzen*) is the idiom.** The shipped
> `real-agents.md:17` uses the directional form and is **not** a defect — but it must not be extended.
> **The rule is the case and the verb, not the noun**, and that is exactly what a term ledger cannot hold.

### Card R — `residency` (3 referents behind 30 tokens)

**Frage:** *Meine ich (a) den Ort selbst, (b) die vertragliche Zusage über den Ort, oder (c) den Ort, an dem
das MODELL läuft?*

- **(a) der Ort** → **„Der *Speicherort* sagt Ihnen, *wo* Ihre Daten liegen."**
- **(b) die Zusage** → **„… eine ausdrückliche *Zusicherung zum Speicherort*."** / negative:
  **„… wobei *global* ausdrücklich heißt: *keine Zusicherung zum Speicherort*."**
  ⚠ **This branch breaks a careless one-word ruling.** A form chosen only for (a) has to be bent into a
  guarantee, and the obvious bend — ⛔ *die Residenzgarantie* — has no attestation and a palace in it.
- **(c) der Ort des Modells** → **„… deshalb muss die Souveränität auch abdecken, *wo das Modell läuft*,
  nicht nur, wo die Daten liegen."** — build this branch as a **clause**; ⛔ *KI-Residenz* has no attestation.
- **The term itself** (H2 „Privacy and data residency", „AI residency is not the same as data residency")
  → **die Data Residency**, feminine, glossed once. See D-B.

**Frame for the whole field, from a German legal source rather than a translation:**
„Erstens verabschieden sich beide ausdrücklich **vom Speicherort als Anknüpfungspunkt**." That is Part III's
residency-versus-sovereignty thesis already written in German.

### Card M — `managed` (3 referents behind 47 tokens — the slice's largest row)

**Frage:** *Ist es (a) ein Attribut an Produkt oder Stufe, (b) der eine Pol des Zwei-Bahnen-Gegensatzes, oder
(c) schlicht „unter Kontrolle gebracht"?*

- **(a) Attribut** → **verwaltet, flektiert** (CORPUS(9)): **„die *verwaltete* RAG-Stufe"**,
  **„eine *vollständig verwaltete*, je Sitzung isolierte Agentenlaufzeit"**, **„semantisches RAG als
  *verwalteter Baustein*"**. Product names stay Klasse 1 (`Managed Knowledge Base`).
  ⛔ **nacktes `Managed Endpoint`** — struck in `rag.md` §2 (in the German IT market *Managed + Endpoint* is
  the standing name of the endpoint-security/MDR sector) → **der Endpunkt des Anbieters**.
- **(b) der Gegenpol zum Selbstbetrieb** → **„Jede Kategorie hat eine Bahn zum *Eigenbetrieb* und eine als
  *verwaltetes Angebot*."** · **„*Plattformseitig verwaltet* heißt: weniger Kontrolle, keine Wartung, ein
  Anbieter."** · **„… wie Sie ihn *selbst betreiben*, wenn die *verwaltete Fassung* nicht reicht."**
  ⚠ `Eigenbetrieb` is licensed but **bound** — `IT-Eigenbetrieb`, or against an explicit cloud/provider pole.
  ⛔ *gemanagt* (Duden marks it umgangssprachlich; de.wp's 598 hits are **bands and athletes**).
- **(c) „unter Kontrolle gebracht"** — one occurrence, and it is a different word: „Discipline turns these
  levers into a **managed** number." → **„Disziplin macht aus diesen Hebeln eine *beherrschbare Größe*."**
  ⛔ „eine verwaltete Zahl" — this branch must not inherit branch (a)'s word.

### Card P — `perimeter`

**Frage:** *Der Perimeter der Cloud, den ich erbe — oder meiner, den Daten nicht verlassen dürfen?*
- **(i) geerbt** → **„Was Sie kaufen, ist das Modell *hinter dem bestehenden Perimeter Ihrer Cloud*: IAM,
  Abrechnung, private Netzanbindung, Audit-Logs."**
- **(ii) der eigene** → **„… die Standardwahl, wenn Daten *Ihren Perimeter* nicht verlassen dürfen."** ·
  **„… Sie können es *innerhalb des eigenen Perimeters* betreiben, sodass die Trace-Daten nie hinausgehen."**
  — the attested government is **`innerhalb`/`außerhalb` + GENITIV**.
- **(iii) jurisdiktionell, einmal** → the compound will not survive; rebuild as a clause:
  **„… der Perimeter aus *Zugriff und Gerichtsbarkeit*, um den sich dieser ganze Abschnitt dreht."**

⚠ **Gloss on first use, and the model is iX, not an invention:** „der »**Perimeter**«, *die ehemals starre
Netzwerkgrenze*". The word needs it because **Duden has no IT sense at all** and everyday German `Perimeter`
is an ophthalmic instrument, a geometry term, a Swiss planning boundary — and a basketball zone.

### Card C/F — `ceiling` and `floor` (ruled together, per instruction)

**Frage:** *Ist das eine Größe, die jemand einstellt — oder eine, an die das System stößt?*
- **eingestellt** (this is `cap`, not `ceiling`) → **die Obergrenze** — settled, **CORPUS(41)**.
- **gestoßen** → **„Ein LLM-Dienst *stößt an seine Kapazitätsgrenze* bei einer überraschend niedrigen
  Anfragerate."** · **„Nicht die reine Rechenleistung, sondern der KV-Cache ist *die eigentliche Grenze*."**
- **erschöpft** (a technique) → **„Prompting und RAG sind *ausgereizt*."**
- **Score-Untergrenze** → **„Setzen Sie *eine Score-Untergrenze* hinter die Stufe, deren Scores etwas
  bedeuten."** · **„*Oberhalb der Untergrenze* ist die Antwort belegt."**
- **Mindestausstattung** → **„Rechnen Sie je Container mit rund 2 CPU-Kernen und 4 GB RAM *als Untergrenze*."**

⚠ **The pair is deliberately asymmetric and the reason must be stated once:** `floor` may take the antonym
of `Obergrenze` precisely because nothing else claims it; `ceiling` may **not** take `Obergrenze` because
`cap` already owns it, in the same Part, 41 times. ⚠ `threshold` stays **der Schwellenwert** —
**CORPUS(8)**, and DWDS separates it as a *trigger point* (`überschreiten`) from `Untergrenze`
(`unterschreiten`). Three English words, three German ones, no merging.

### Card S — `sample`

**Frage:** *Die behaltene Teilmenge, der Vorgang, oder das Ziehen aus einer Verteilung?*
- **Teilmenge** → **„ein Judge, der *eine Stichprobe* des Produktivverkehrs bewertet"**; Kartenlabel
  **„Live-Stichprobe"**, **„Judge auf Stichprobe"**.
- **Vorgang** → **das Sampling** (settled §1.1.e) — untouched by this card.
- **Verteilung** → **„Für jeden Prompt *erzeugt* die Plattform mehrere Antwortkandidaten."**
  ⛔ *Stichprobe* here: it is not a draw from a population, and the canon already resolved this once.

### Card K — `capability`

**Frage:** *Kann das System etwas (ein Merkmal) — wie gut kann es etwas (ein Grad) — oder hat das Produkt
eine Funktion?*
- **Merkmal** → **die Fähigkeit**: „request-driven autoscaling **als Fähigkeit**".
- **Leistungsgrad** → **die Leistungsfähigkeit**: **„Der Preis der Souveränität bemisst sich in der
  *Leistungsfähigkeit des Modells*."**
- **Produktmerkmal** → **die Funktion**: **„… die am häufigsten gewünschte *Funktion* des Jahres."**
This **does not reopen** §1.1.g — that row's evidence is the MCP handshake field, a *Merkmal*. It adds two
branches, in the shape §1.1.g itself uses for `Skill` („anderer Referent, beide Zeilen gelten").

### Card G — `guard`

**Frage:** *Verb, Produktname, oder Codebezeichner?*
- **Verb, allgemein** → **„was man misst, was man schützt, was man sieht"** (parallel to the shipped triad).
- **Verb, Zugriff** → **„Dieselben IAM-Rollen, die schon Ihre Buckets absichern, sichern jetzt auch das
  Modell ab."** ⛔ *bewachen* — that puts sentries on a storage bucket.
- **Produktname** → **Llama Guard**, **Granite Guardian** (unübersetzt, unflektiert).
- **Codebezeichner** → **„Sie hängen einen Validator mit `.use()` an einen `Guard`."**
⛔⛔ Never merge with `Guardrails` — that row is **Plural only, Singular OPEN**; a „Guard" for the verb sense
would invent exactly the singular the canon forbids.

---

## 3. RUN DISAGREEMENTS

Wave 2's measured finding held again: **the two runs contradicted each other frontally, and on the slice's
single largest row.** Fourteen substantive disagreements; every one recorded with both positions.

| # | Row | run 1 | run 2 | Resolution + reason |
|---|---|---|---|---|
| **D-01** | **`managed`** (47 occ., the slice's biggest) | kept-EN `Managed-` compound former; ⛔ „ein verwalteter Dienst ist **unbelegt (0)**, und die einzigen Quellen dafür sind disqualifizierte Herstellerlokalisierungen" | attributive **`verwaltet`**, „ausgeliefert 9×" | **run 2, by CORPUS(9).** Run1 measured the *string* `verwalteter Dienst` on de.wikipedia and generalised to the *construction*. The corpus writes `verwalteter Baustein`, `verwaltete RAG Engine`, `verwaltetes RAG` — different head nouns, same construction. **A string count is not a construction count.** Run1's `Managed Service` **33 : 0** is still true and still useful — it governs the *fixed English compound*, not German attributive use |
| **D-02** | **`to wire` (verb)** | ⛔ `verdrahten` — „a **semantic reversal** of the teaching point", same class as ⛔ *Anonymisierung für redaction* | **verdrahten** (cites slice F, „ausgeliefert 8× in Teil II") | **run 2 on the verb, run 1 on the narrow form.** **CORPUS(5)**: `die Verdrahtung der Tool-Calls`, `Verdrahten Sie diese Teile`, `wie Subagenten miteinander verdrahtet sind` — the assemble-components sense is shipped and idiomatic. Run1's argument is **correct but over-scoped**: the reversal lives in the **fixed collocation `fest verdrahtet`** (= hardcoded), not in the verb. Ban the collocation, keep the verb |
| **D-03** | **`ceiling`** | **die Kapazitätsgrenze**, never `Obergrenze`; „the corpus draws the distinction *itself*" | **die Obergrenze / die eigentliche Grenze** | **run 1's ruling, run 2's premise-check.** I could not confirm run1's corpus claim: of 41 shipped `Obergrenze`, **at least two are limits you run into** („die **ehrliche Obergrenze**" of judge agreement; „die Obergrenze, die das Kontextfenster setzt"). The corpus does **not** keep the distinction clean, so run1's row is a *design* decision, not a corpus finding. Ruled in D-A |
| **D-04** | **`attribution` (noun)** | **die Kostenzurechnung** (Gabler, de.wp 8) | **die Kostenzuordnung** (informatik-aktuell, article-bearing) | **run 2, by CORPUS(10) on the verb.** The shipped corpus writes **`zuordnen`** ten times, including in the exact paragraph Part III cross-references. `Kostenzuordnung` is the noun of the shipped verb; `Kostenzurechnung` would introduce a second verb (`zurechnen`) for a movement the corpus already names. Both nouns are CORPUS(0); morphological agreement with the shipped verb decides. Run1's adverb **`verursachungsgerecht`** (20 hits, all cost accounting) is kept — it collides with nothing |
| **D-05** | **`floor`** | **der Mindestwert** (prose) + `die Untergrenze` (resource) + HOUSE label `Score-Mindestwert` | **die Untergrenze** for both + label `Score-Untergrenze` | **run 2.** One word covers both Part III senses; DWDS defines `Untergrenze` as exactly „ein Schwellenwert, der … nicht unterschritten werden darf"; it is the free antonym of the corpus's 41× `Obergrenze`; and `Score-Untergrenze` rides a 557-hit lemma where `Score-Mindestwert` is a house coinage. Run1's own §S8 concedes the label form is HOUSE |
| **D-06** | **`frontier`** | OPEN; „`Spitzenmodell` … semantically off" (74 hits, mostly automotive); rec. `die leistungsstärksten Modelle` | ⛔⛔ `das Spitzenmodell` („585 hits, Dominanzfalle mit Zahl"); rec. `das Frontier-Modell` | **NEITHER — CORPUS(2) overrides both.** The shipped German writes **„Spitzenmodelle kommen auf unter 50 % Erfolg"** and „bei τ-bench fallen die **Spitzenmodelle** …", in exactly the frontier-model sense. **Both runs measured de.wikipedia's topic mix and neither grepped the delivered locale for this row.** Run2's ⛔⛔ would have reversed a shipped ruling. This is the clearest instance in the slice of a count standing in for a reading |
| **D-07** | **`Stellschraube`** | free; use it for the **policy** dial (`on_fail`), `Regler` for the continuous dial | ⛔ „von Slice D für `lever` belegt — zwei englische Wörter brauchen zwei deutsche" | **run 1.** Run2's premise is false: **`lever` is `der Hebel`** — the referent baseline says so explicitly („a precedent slice D must reuse, not re-coin", incl. „das Signal, **zu einem der Hebel zu greifen**"), and **CORPUS(11 free `Hebel`/`Hebeln`; 15 incl. compounds `Grundhebel`, `Qualitätshebel`)** confirms —
the baseline's 10 and my 11 differ by one inflected plural, not by a reading. `Stellschraube` is shipped **CORPUS(3)** for a *provider-side parameter* („Die **Stellschrauben** dafür sitzen beim Anbieter"), which is precisely run1's policy-dial referent. Three German words, three referents, no collision |
| **D-08** | **`Regler` + verb** | „`an einem Regler drehen` is NOT dictionary-attested … the fully attested verb is **einstellen**" | „Attestiertes Verb: **einstellen** (nicht *drehen* — das gehört zur *Stellschraube*)" | **Both overruled by CORPUS(6).** The delivered German uses **`drehen` three times** with `Regler` („an dem Sie *nachträglich* **drehen**", „kein Regler, an dem Sie beiläufig **drehen**") and `einstellen` once. Both verbs are licensed; the corpus is the register |
| **D-09** | **`cross-region`** | **OPEN**, rebuild verbally — the 10 `regionsübergreifend` hits are „**all ten** urban planning / demography / tourism, **zero IT**" | **`regionsübergreifend`**, WEAK, „de.wikipedia `insource` = **10**" | **run 1.** Same source, same number, opposite conclusion: run1 opened the hits, run2 reported the count. Per brief §3, „grep widely, then read the sentences" |
| **D-10** | **`residency`** | **der Speicherort** (German-led, ranked list) | **die Data Residency** (kept-EN, fem., two case-marked tokens) + `der Speicherort` in prose | **Split — see D-B.** Both agree on `der Speicherort` for the plain location; that agreement is the strong part. The disputed half is the *term* |
| **D-11** | **`serverless`** | DISPUTED — `serverlos` only next to an explicit cloud head noun, because **de.wp `serverlos` is overwhelmingly peer-to-peer** (17 of 18) | kept-EN; ⛔ `serverlos` „unbelegt in Fachprosa" | **run 1's evidence, run 2's conclusion.** Run2's ⛔ is right for the wrong reason — `serverlos` **is** attested in heise (run1 quotes four inflected instances); the hazard is the **homonym**, not absence. Held OPEN with kept-EN as incumbent |
| **D-12** | **`reserved`** | ⛔ **`reservierte Kapazität` = 0 hits** (verified after ruling out a rate-limit artefact) | uses **`reservierte Kapazität`** for *idle reserved capacity* | **run 1's measurement stands** — a measured zero beats an unmeasured use. But run2's collocation finding is kept and is the more useful half: „für Enterprise-Pläne **reserviert**" is an English scaffold; German is **`jemandem vorbehalten sein` + Dativ** |
| **D-13** | **`chargeback`** | **die (IT-)Leistungsverrechnung** — lead with it | kept-EN, **Genus nicht setzen**, „beim Chargeback" | **run 2.** `Leistungsverrechnung` is real German — but it names *both* poles of Part III's contrast (report vs actually bill), so it erases the showback/chargeback distinction the section is built on. Keep the loan, use `IT-Leistungsverrechnung` as the one-time gloss. ⛔ Both runs agree on `die Rückbelastung` (card payments) and run1's ⛔ `die Kostenumlage` (inverts the point) is kept |
| **D-14** | **`Engine` in the shipped locale** | „12 hits, **0 usable** — every hit is `Prompt-Engineering` or a brand. **A raw count that looks like an incumbent and is not** — recording it so nobody cites my own table against me" | „**Ausgeliefert, femininmarkiert:** eine **verwaltete** RAG Engine" | **run 2, by CORPUS(2).** Run1's disclaimer is exactly the right instinct applied to a wrong reading: `real-agents.md:107` and `:360` carry a German feminine determiner **and** a weak-ending adjective. **The gender is disclosed by the German words around the brand name, not by the brand name.** A pass that filters out "brand hits" filters out the evidence |
| **D-15** | **`roster`** | frame = **Momentaufnahme**; noun = `die Riege` | **die Aufzählung** (self-declared guess) | **run 1, by CORPUS(5)** — and run2's candidate is worse than unattested, it **collides**: the shipped corpus uses `Aufzählungen` for *bullet lists*. Run2 flagged this as „my weakest ruling; if one row comes back it is this one." It came back |
| **D-16** | **`uptime theatre`** | „does not survive … the English pun is lost either way. **Flag for the editorial pass, do not solve it in the ledger**" | **das Verfügbarkeitstheater**, „ausgeliefert" | **run 2, by CORPUS(1).** The German was written eleven months of project-time ago. Run1 escalated a solved problem — the §C1 „unapplied, not incomplete" pattern committed inside the sheet that names it |
| **D-17** | **`org-level`** | **unternehmensweit** (shipped; BSI-vs-general-corpus divergence named) | **auf Organisationsebene** (`organisationsweit` „zu dünn") | **run 1, by CORPUS(2 vs 0)** — and the two shipped sentences **forward-reference this very lesson**, so the incumbent was chosen for this text before it existed |
| **D-18** | **`proxy`** | one word covers both senses — „the expected sense-split turns out to be unnecessary" | **two words obligatory**: `der Proxy` / `die Ersatzgröße` | **run 2.** Both found the same DWDS Bedeutung 2. Run2's argument is contextual and decisive: in a chapter dense with gateways, routers and proxies, `der Proxy` for a *metric* sends the reader to the network device. The canon already carries `Proxy-Metrik` |
| **D-19** | **`Enterprise` in the shipped locale** | „the shipped locale's 3 `Enterprise` hits are all inside `Gemini Enterprise Agent Platform` — **a brand, Klasse 1, not an attestation**" | shipped UI label **`Enterprise-Reifegrad`** + canon `ai-sdlc.md` „Enterprise bleibt kept-EN" | **run 2.** The corpus hit is `Enterprise-Reifegrad: Audit, Herkunft, Vorgaben` — a German-hyphenated compound, i.e. *supporting* evidence for the compound-former ruling both runs reached. Run1 wrote a null into a card built to prevent exactly that mistake |
| **D-20** | **`Enterprise-Tarif`** | ⛔ „**my own candidate, refuted: de.wp insource 0**" (logged in §C6 on purpose) | uses `Enterprise-Tarife` in worked sentences | **run 1's measurement.** Prefer `das Enterprise-Abo` / `die Enterprise-Version` / `die Enterprise-Lizenz` (35 hits). ⚠ Run2 independently found the sharper trap on this row: **DWDS `Enterprise` returns the French `Entreprise` (feminine)** — a pass that "looks up the gender" cites impeccably and is wrong |
| **D-21** | **`isolation`** | split `Isolation` (state) / `Isolierung` (IR act), on a BSI count | `die Isolation` only; ⛔ `Isolierung` = insulation | **run 2 for Part III, run 1's split recorded as true-but-out-of-scope.** **CORPUS: Isolation 10, Isolierung 0**, and 10/10 are the genitive-bound `Isolation der Kontexte`. Part III has no incident-response isolation, so the split does not arise here. **The binding construction, not the lexeme, is the ruling** |

**Where the runs agreed and the agreement is worth *less*, not more** (brief §2):
`jurisdiction` (run1 only, resting entirely on BSI C5 BC-01/BC-05) → **THIN**. `compliance` and `perimeter`
are AGREED×2 but both runs read the same two dictionaries and the same iX headline → the counter-check owed
is a heise/iX/c't full-text count, not a third dictionary. `air-gapped`'s BSI half rests on two IT-Grundschutz
Bausteine → **THIN×2 by source, strong by construction** (the German is a *requirement title*, which is
stronger than a running-prose token).

---

## 4. VOCABULARY FOOTPRINT

Flat, deduplicated list of every German content word appearing in my worked sentences and sense cards.
Stage 2 uses this to detect cross-slice collisions.

`abdecken` · `absichern` · `Abrechnung` · `Anbieter` · `Anfrage` · `Anfragerate` · `Angebot` ·
`anbieten` · `anbinden` · `Anforderung` · `angenommen` · `Antwort` · `Antwortkandidat` ·
`Antwortverweigerung` · `Anwendungsschicht` · `Audit-Log` · `ausgereizt` · `austauschen` · `Baustein` ·
`bedienen` · `Bedarf` · `beherrschbar` · `bemessen` · `Benchmark` · `bereits` · `Branche` ·
`Break-even` · `Chargeback` · `Compliance` · `Data Residency` · `De-facto-Standard` · `drehen` ·
`durchsetzen` · `Egress-Kosten` · `Eigenbetrieb` · `einbinden` · `Einhaltung` · `einigen` ·
`einstellen` · `Endpunkt` · `Engine` · `Enterprise-Abo` · `Enterprise-Version` · `erklimmen` ·
`Ersatzgröße` · `erzeugen` · `Evaluierung` · `Fähigkeit` · `FinOps` · `Funktion` · `Gateway` ·
`Gerichtsbarkeit` · `Governance` · `Grenze` · `Guardrails` · `Hebel` · `Identität` ·
`Identitätsmanagement` · `Isolation` · `Judge` · `Kapazität` · `Kapazitätsgrenze` · `Kategorie` ·
`koppeln` · `Korrektheit` · `Kostenzuordnung` · `KV-Cache` · `laufend` · `Leerlauf` ·
`Leistungsfähigkeit` · `Leiter` · `Make-or-Buy-Entscheidung` · `Mandant` · `Mandantenfähigkeit` ·
`Momentaufnahme` · `Multi-Cloud-Gateway` · `Nachrichtenformat` · `Netzanbindung` · `Netztrennung` ·
`Obergrenze` · `Perimeter` · `Produktivverkehr` · `Proxy` · `Quantisierung` · `Rabatt` · `Regler` ·
`reguliert` · `reserviert` · `Route` · `Router` · `Schnittstelle` · `schützen` · `Schwellenwert` ·
`Sitzung` · `Souveränität` · `Speicherort` · `Spitzenmodell` · `Sprosse` · `Stack` · `Stellschraube` ·
`Stichprobe` · `stoßen` · `Stufe` · `übertragen` · `Umgebung` · `Untergrenze` · `Unternehmen` ·
`unternehmensweit` · `verdrahten` · `Verdrahtung` · `Verfügbarkeit` · `Verfügbarkeitstheater` ·
`vergeben`→`vorbehalten` · `verwaltet` · `verweigern` · `verursachungsgerecht` · `Weg` · `Werkzeug` ·
`Wrapper` · `ziehen` · `zuordnen` · `Zusicherung`

⚠ **Collision candidates I can already name for stage 2:**
- **`Grenze` / `Obergrenze` / `Untergrenze` / `Kapazitätsgrenze` / `Schwellenwert` / `Netzgrenze` /
  `Vertrauensgrenze` / `Sicherheitsgrenze` / `Perimeter`** — **nine boundary-shaped German words** now in
  play across slices. This is the `Laufzeitumgebung`/`Werkzeuge` shape and it is the densest collision
  surface in the wave. Stage 2 must lay them out on one page.
- **`Hebel` (lever) / `Regler` (dial) / `Stellschraube` (policy knob) / `Stufe` (notch, tier)** — four
  control-metaphor words; all four are shipped; the assignment above is corpus-derived but crosses slices D and G.
- **`Momentaufnahme`** — I use it for `roster`; the baseline warns slice E that `snapshot` (29 occ.) is
  **a pinned model version**, a different referent. **Two referents must not collapse onto this word.**
- **`laufend`** — I license it for `in-flight`; the corpus already uses it for *recurring* (`laufende Kosten`)
  and for *live* (`am laufenden Verkehr`). Third sense, same word. Flagged, not resolved.
- **`Laufzeit` / `Agentenlaufzeit`** — appears in my `managed` card („eine vollständig verwaltete
  Agentenlaufzeit"); this is slice A's row and the baseline's one real finding. **I defer entirely.**
- **`Angebot`** — I use it for `offering`; run1 also proposes it inside `Managed-Angebot`. One word, two jobs.
- **`Stufe`** — I use it for `notch` and for `tier` (`die verwaltete RAG-Stufe`). Two referents, flag it.

---

## 5. SPREAD (from the concordance; 10 Part III files)

File keys: `ov` = overview · `pf` = production-failures · `sv/i`,`sv/d` = serving · `cp/i`,`cp/d` =
cloud-platforms · `te/i`,`te/d` = tooling-ecosystem · `lo/i`,`lo/d` = llmops.

**Terms spanning ≥3 files — these need ONE binding string decided centrally:**

| Term | occ. | files | where |
|---|---|---|---|
| **guard** | 13 | **6** | ov, pf, cp/i, te/i, te/d, lo/d |
| **managed** | 47 | **5** | cp/i, cp/d, te/i, te/d, lo/d |
| **governance** | 10 | **5** | cp/i, cp/d, te/i, lo/i, lo/d |
| **engine** | 8 | **5** | cp/i, cp/d, sv/i, sv/d, lo/d |
| **wire** | 8 (+3 `wired` = 11) | **5** | pf, sv/i, cp/d, te/i, te/d |
| **perimeter** | 10 | 4 | cp/i, cp/d, te/i, te/d |
| **enterprise** | 15 | 4 | ov, cp/i, cp/d, te/i |
| **capability** | 8 | 4 | cp/i, cp/d, sv/d, lo/d |
| **serverless** | 9 | 4 | cp/i, cp/d, sv/i, sv/d |
| **org-level** | 5 | 4 | cp/i, cp/d, lo/i, lo/d |
| **regulated** | 5 | 4 | cp/i, cp/d, pf, te/i |
| **reserved** | 7 | 4 | cp/i, cp/d, te/i, lo/d |
| **make-or-buy** | 6 | 4 | cp/i, cp/d, te/i, te/d |
| **offering** | 7 | 4 | cp/i, cp/d, te/i, lo/d |
| **proxy** | 5 | 4 | cp/d, sv/i, sv/d, lo/d |
| **roster** | 6 | 4 | cp/d, sv/i, sv/d, te/d |
| **residency** | **30** | 3 | cp/i, cp/d, te/d |
| **adapter** | 10 | 3 | cp/d, sv/d, lo/d |
| **idle** | 8 | 3 | cp/i (via cp/d), sv/i, sv/d |
| **finops** | 9 | 3 | cp/i, cp/d, lo/d |
| **cross-region** | 7 | 3 | cp/i, cp/d, lo/d |
| **exporter** | 7 | 3 | sv/d, te/i, te/d |
| **tenant** | 6 | 3 | cp/d, sv/d, lo/d |
| **isolation** | 6 | 3 | cp/i, cp/d, sv/d |
| **dial** | 6 | 3 | cp/i, cp/d, te/d |
| **sample** | 9 | 3 | pf, lo/i, lo/d |
| **correctness** | 5 | 3 | pf, lo/i, lo/d |
| **refusal** | 5 | 3 | pf, cp/d, lo/i |

**Single-file terms** (a renderer can hold these locally): `air-gapped` 8 → cp/d only · `chargeback` 6 and
`showback` 4 → lo/d only · `wrapper` 5 → cp/i only · `relevancy` 6 → te/i only.

⚠ **Note the shape:** `cloud-platforms/deep-dive.md` carries **35 of the 48 live terms** in this slice.
It is the single densest page in the wave and it is where `residency` (30), `sovereignty` (12),
`air-gapped` (8), `perimeter` (10) and `managed` all land at once. **If one page gets a native-speaker
read, it is that one.**

---

## 6. CANON DELTA (reported, never edited)

| # | File / section | Current text | Proposed | Reason |
|---|---|---|---|---|
| **G-1** | `_language.md` §1.1.e (Observability und Messgrößen) | register lists `Observability, Monitoring, Metrik, Telemetrie, Sampling, Drift, Fehlerbudget, SLA/SLO, SLI, Evaluierung, Grader` — **no `Uptime`** | add a **Querverweis** to §9.3, in the shape §1.1.e already uses | §9.3 rules `uptime`/`correctness` **verbatim, on Part III's own English sentence**, under a „Präzedenz" heading — and it is in a *constructions* section, so a renderer looking up the word never finds it. Third instance of the pattern (`Fehlerbild`, `Dashboard`, now this). **A pointer at an empty cell looks exactly like a pointer at a full one — and so does no pointer at all** |
| **G-2** | `_language.md` §1.1 (Fallenkasten) | — | add: **`Leitung` is a banned WORD-FIELD in the locative, not a banned phrase** — Duden lists four fixed expressions on the lemma, three mean *begriffsstutzig sein*; `über die Leitung` (Akk. + *schicken*) is licensed, `auf der Leitung` (Dat. + *stehen/sitzen*) is not. `Draht`: seven idioms, all human rapport. **`fest verdrahtet` = hardcoded** | The wave-2 reversal **exists only in the shipped prose and in the briefs**. Run1 grepped the whole canon for `Nachrichtenformat|Leitung|Drahtformat|wire` → **no output at all**. `rag.md` §8's own standard is that reversals are „sichtbar gestrichen, nicht still entfernt"; this one was never written down. **A ruling that lives only in the output is one rewrite away from being lost** |
| **G-3** | `_language.md` §1.1 (Fallenkasten) | — | add: **do not look `Enterprise` up in DWDS** — the lemma there is the French `Entreprise`, **feminine**, and a pass that derives a gender from it cites impeccably and is wrong | run2's find. This is the `Attest` shape: a flawless citation of the wrong lemma. `ai-sdlc.md` carries `Enterprise` as kept-EN **without** this warning |
| **G-4** | `_language.md` §1.1.a, next to `cap → die Obergrenze` | — | add **`floor → die Untergrenze`** and **`ceiling → die Kapazitätsgrenze`**, with the asymmetry stated: *floor takes the antonym of `Obergrenze` because nothing else claims it; ceiling may not, because `cap` owns `Obergrenze`* | Three English words (`cap`, `ceiling`, `floor`) and a fourth (`threshold`) currently map onto two German rows. The corpus ships `Obergrenze` 41× and `Schwellenwert` 8×; `Kapazitätsgrenze`, `Untergrenze` and `Mindestwert` are all **CORPUS(0)** |
| **G-5** | `_language.md` §1.1 (new rows) | no row for any of them | **`das Gateway`** (Duden, Neutrum, *des Gateways*, *die Gateways*, **Gebrauch: EDV**); **`der Mandant`** (n-Dekl., *des Mandanten*); **`der Regler`**; **`die Leiter` / `die Sprosse`** (⚠ homograph `der Leiter` = a person / an electrical conductor); **`die Stichprobe`**; **`der Benchmark`** (*des Benchmarks*); **`die Korrektheit`** | The `Budget`/`Cap`/`Golden Signals` shape, third instance: the canon has `LLM-Gateway` (a brand) and no row for the appellative Part III needs 8×+. The rest are shipped incumbents with no register entry. `Mandant` is the second member of the n-declension class the canon already flags for `der Agent` |
| **G-6** | `_language.md` §1.1.f / §1.1.g (new rows — the five new fields) | — | **`der Perimeter`** (des Perimeters, gloss on first use) · **`die Souveränität`** / `die digitale Souveränität` (lowercase; no plural) · **`die Data Residency`** (fem., obligatory gloss) + **`der Speicherort`** · **`die Compliance`** (Plural meiden) · **`Enterprise-`** as a compound former only | Five word fields Part III opens with **CORPUS(0)** — the wave's real risk surface. Attestation supplied in §1 above |
| **G-7** | `_language.md` §1.1.e (new rows — the FinOps field) | — | **`FinOps`** (artikellos, `Backpressure` class) · **`die Kostenzuordnung`** + adverb `verursachungsgerecht` · **`Chargeback`/`Showback`** (Genus **OPEN**, PP form „beim X") · **`die Egress-Kosten`** (Pl., compound only) · **`der Break-even`** | `rag.md` §2 lists the *knobs* (`Soft/Hard Cap`, `Error Budget`, `Provisioned Throughput`). Part III is the first lesson that treats **cost as an organisational accounting practice**. 27+ occurrences across five head words, zero incumbents. A genuine new register, not a coverage gap |
| **G-8** | `rag.md` §2 | `Managed Endpoint` struck → *der Endpunkt des Anbieters* | **no change — confirmed**, and add the corpus form: attributive **`verwaltet`** is the shipped rendering for `managed`, **CORPUS(9)** | Taking §327/§2 as given per brief §5. Part III contains the trigger sentence („models run as managed endpoints"). I dissent from nothing; I add the positive form the struck row leaves open |
| **G-9** | `_language.md` §1.1.g | `Capability → die Fähigkeit` (Welle 2) | **no change**; add two branches in the `Skill` shape: *Leistungsgrad* → **die Leistungsfähigkeit**, *Produktmerkmal* → **die Funktion** | §1.1.g's evidence is specifically the MCP handshake *feature*. Part III uses the word as a degree („frontier capability lags sovereignty") and as a product feature („the most-requested tooling capability"). Neither reopens the row |
| **G-10** | `rag.md` §2 / §3 | `Guardrails`: **Plural only, Singular OPEN** | **no change** — add an explicit note that `guard` (verb, 8 appellative occ.) and `Guard` (product/code, class 1) are **separate rows** and must never merge | A „Guard" for the verb sense would invent exactly the singular the canon forbids. Both runs found this independently |

⚠ **Not proposed, deliberately:** `Showback`/`Chargeback` genders, `Air Gap` gender, `Serverless`,
`in-flight`+*drain*, `frontier` as a §1.1.g row (the corpus already answers it), `unit economics`,
`cross-region`. Each has its closing condition stated in §1.

---

## 7. NEEDS A DECISION, NOT MORE RESEARCH

Three rows. Further attestation will not help: for two of them German has no settled term, and for the
third the evidence is genuinely balanced and someone must simply rule.

### D-A — `ceiling` / `floor`: does `Obergrenze` stretch, or does `ceiling` get its own word?

**The question.** `cap → die Obergrenze` is settled and the corpus ships it **41×**. Part III's `ceiling`
is the opposite kind of object — a limit you *discover by hitting it* („the KV cache **is the real
ceiling**", „hits its concurrency **ceiling**", „prompt and RAG **have hit a ceiling**"). Run1 rules
`die Kapazitätsgrenze`; run2 reuses `die Obergrenze`.

**Why more research will not settle it.** I checked run1's decisive premise — that the corpus itself draws
the distinction — and **it does not hold**: at least two of the 41 shipped `Obergrenze` are limits nobody
configured („die **ehrliche Obergrenze**" of judge agreement; „die Obergrenze, die das Kontextfenster
setzt"). And `Kapazitätsgrenze` is **CORPUS(0)**. So this is a register decision between two defensible
German words, not a lookup.

**My recommendation, firmly: rule the pair asymmetrically —**
**`ceiling` → `die Kapazitätsgrenze` (+ `die Grenze` anaphorically, `ausgereizt` for an exhausted
technique); `floor` → `die Untergrenze` (both senses, label `Score-Untergrenze`); `cap` keeps
`die Obergrenze`; `threshold` keeps `der Schwellenwert`.**
And state the asymmetry once in the canon so a later sweep does not "fix" it: *floor may take the antonym
of `Obergrenze` because nothing else claims it; ceiling may not, because `cap` owns it.*

**Cost of being wrong.** Asymmetric, which is why I recommend this side.
- If `Kapazitätsgrenze` is the wrong call, the cost is **stylistic**: a five-syllable compound in 6
  occurrences across 2 files. Nothing is misread.
- If `Obergrenze` is the wrong call, the cost is **factual**: the KV-cache paragraph is the take-away of
  the serving deep-dive, it sits in the same Part as the LLMOps budgets, and a reader who meets
  `Obergrenze` in both places reads a physical constraint as something someone configured. That is the
  class the canon calls „sachlich falsch, keine stilistische Frage" (⛔ *die Ausreißer* für *tail*).
- On the `floor` half I am confident either way; `Untergrenze` costs nothing if wrong and buys the free
  antonym symmetry if right.

### D-B — `residency` (30 occurrences, 3 files): kept-EN term, or German-led?

**The question.** Tier 1 (BSI C5 BC-01: „**Lokationen** der Daten"), trade press (heise: „Anforderungen an
den **Speicherort**", but headlining in English and scare-quoting „die sogenannte ‚**Datenresidenz**'") and
the vendors (`Datenresidenz` vs `Datenstandort`, and the two big vendors disagree with each other) all
diverge. **CORPUS(0)** for every candidate. Run1 ranks `der Speicherort`; run2 rules kept-EN
`die Data Residency` on two independent case-marked German tokens (heise dative, storage-insider genitive,
both feminine).

**What is already agreed and should not be re-litigated:** both runs independently choose **`der
Speicherort`** for the plain location sense, and both ⛔ **`die Datenhoheit`** — which is *sovereignty* and
would collapse the exact distinction the section is built on. Those two are settled.

**My recommendation, firmly: split by position, not by taste.**
**`die Data Residency`** (feminine, kept-EN, **obligatory gloss on first mention**) for the ~5 **term-level**
positions — the H2 „Privacy and data residency", the contrast „AI residency is not the same as data
residency", „a residency guarantee", „residency policy". **`der Speicherort`** for the ~25 running-prose
occurrences where the sentence means *where the data sits*.

Reasons: (i) a common noun cannot carry „AI residency is not the same as data residency" — German-ising it
produces a true sentence that loses that these are two *named product properties*; (ii) run2 has two
case-marked German tokens for the loan and run1 has none for a term-level German form; (iii) keeping the
term English is a **firebreak against `Datenhoheit`** — a renderer reaching for variation on a German term
goes there, and that is the costliest single confusion the chapter permits.

**Cost of being wrong, and it is real on both sides.**
- If kept-EN is wrong: an English term in an H2 of a **sovereignty** chapter about European control. That
  is a tonal own-goal and a reviewer will notice it. Mitigation is built into the recommendation — the loan
  appears ~5 times, not 30.
- If German-led is wrong: the residency-versus-sovereignty distinction — the section's thesis — degrades,
  and the `Datenhoheit` trap opens. That is worse and it is not visible until a reader misreads it.
- ⚠ **Whichever way it is ruled, it must be ruled ONCE and written into the canon**, because `residency`
  spans three files including the densest page in the wave. This is the row most likely to drift.

### D-C — `in-flight` + *drain*, and `wrapper` (evaluative sense): the German does not exist

**The question.** Neither run found a German rendering of *drain the in-flight connections* — targeted
searches over Kubernetes graceful-shutdown prose returned nothing; heise/INNOQ keep the English. And no
German source carries `wrapper` in Part III's evaluative sense („the wrapper is the product", „the
differentiators shift to the wrapper"); every attestation is the narrow structural one.

**My recommendation: rule a construction, not a word, and mark both as HOUSE on probation.**
- `in-flight` → **`laufend`** in the ordinary cases („jede **laufende Anfrage** hält KV-Cache-Blöcke"), but
  the *drain* sentence takes the explicit rebuild: **„die *bereits angenommenen, noch nicht abgeschlossenen*
  Anfragen zu Ende bedienen."** ⚠ Note the reason `laufend` is not simply BOUND: **CORPUS(20)**, and the
  corpus already runs it in two other senses (`laufende Kosten` = recurring, „am **laufenden** Verkehr" =
  live). This would be a third sense on an already-loaded word — acceptable, but a deliberate choice.
- `wrapper` → keep **`der Wrapper`** (masc., **CORPUS(1)**, case-marked) and carry the evaluative sense on
  the same word plus one descriptive clause on first use: **„die Schicht, die ein Anbieter um eine
  Standardkomponente legt."**

**Cost of being wrong:** low and local. `in-flight` occurs 6× in 2 files, `wrapper` 5× in **one** file
(`cloud-platforms/index.md`) — a single-page term is cheap to revise. ⛔ The alternatives are the expensive
ones: `schwebend` for in-flight is a **fixed legal idiom** (*ein schwebendes Verfahren* = sub judice), and
`der Aufsatz` for wrapper reads as a school essay. Both runs agree on those bans.

---

## 8. WHAT THIS PASS COULD NOT DO

1. **I did no new attestation, by instruction.** Every external count above is one of the two runs'. Where
   they disagreed on a *number* (`Spitzenmodell` 74 vs 585; `der Benchmark` 36/28, which run2 then declared
   contaminated by plural substrings), **I did not adjudicate the number** — I went to the corpus instead.
   Two of those numbers are still unreconciled and I have flagged them rather than picking one.
2. **Eight rows stay OPEN and I did not guess them:** `serverless`, `cross-region`, `in-flight` + *drain*,
   `wrapper` (evaluative), `chargeback`/`showback` genders, `Air Gap` gender, `sovereign region`,
   `unit economics`. Each has a stated closing condition. Per brief §2 that is a correct outcome; it is
   also a real limit and I am not dressing it up.
3. **`residency` is the largest row in the slice and I recommended rather than settled it** — correctly, I
   think, but it means the wave's biggest single row leaves stage 1 unresolved.
4. **I could not counter-check the THIN rows.** `jurisdiction` rests entirely on BSI C5; `perimeter` and
   `compliance` are AGREED×2 across the *same* two dictionaries. The brief does not require me to run the
   heise/iX/c't counter-count, and I did not. **Those rows are labelled so the renderers do not read
   `AGREED×2` as „checked".**
5. **Cross-slice rows: I stated my position and deferred the merge.** `Laufzeit`/`runtime` (slice A — I use
   `Agentenlaufzeit` once inside a `managed` example and defer entirely), `snapshot`/`Momentaufnahme`
   (slice E — I claim `Momentaufnahme` for `roster` and the baseline warns E that `snapshot` is a *pinned
   model version*; **two referents, they must not collapse**), `lever`/`Hebel`/`Stellschraube` (slice D —
   run2's premise about slice D is false, see D-07, but slice D holds the row), `queue`, `budget`,
   `Anbieter`/`Provider`, `Endpunkt`. Stage 2 merges.
6. **The corpus can only convict, not acquit.** Everything I marked `CORPUS PRECEDENT` rests on the
   assumption that the shipped German is right. **Both runs of this slice were told to grep `i18n/de/`
   first, so where the locale is wrong both runs agree and the agreement looks like verification.**
   Run1 caught one such case in the act — **`Eigenbetrieb`**: three clean shipped uses, and Duden, DWDS and
   de.wikipedia are unanimous that the word is a **municipal-enterprise legal form**. The row survives only
   **bound**. The rows I would re-check next on the same suspicion, in order: **`der Regler`**,
   **`die Leiter`/`die Sprosse`**, **`die Engine`** (2 tokens, both inside a brand name), **`das
   Verfügbarkeitstheater`** (1 token), **`das Angebot`** (1 token). *Finding a word in the shipped corpus
   attests the house's habit, not the language.*
7. **A native ear was not available and three of my recommendations are the class that needs one** —
   multi-word, idiom-adjacent: „eine einzige, einheitliche Schnittstelle anbieten", „an seine
   Kapazitätsgrenze stoßen", „die bereits angenommenen, noch nicht abgeschlossenen Anfragen zu Ende
   bedienen". Each is checked against DWDS Mehrwortausdrücke and none collides. **„No collision found" is
   not „confirmed by ear."**
8. **Arithmetic, per brief §6.** I state no project-wide total. Deltas my slice would cause, named without
   values: the count of terms where **German leads** grows by the `frontier → Spitzenmodell` and
   `managed → verwaltet` reversals (**+2** against what the two sheets between them proposed); the count of
   **§1.1 rows with no register entry** grows by the seven in canon delta G-5 plus the five in G-6 plus the
   five in G-7; the count of **verified zero-incumbent fields** shrinks by **two**, because neither
   **`Managed`** nor **`Enterprise`** is one (§0). Stage 2 computes the values from the union.
9. **The concordance under-counted this slice's flagship row, and both runs caught it independently.**
   `wire` prints `{'wire': 8}`; the term field is **11** — `wired` ×3, one of them an **H2** („## The stack,
   wired"), and the verb sense (6 of 11) is *larger* than the protocol sense. I verified this myself:
   `grep -rhoiE "\bwire[a-z]*\b"` → `wire 8, wired 3`. **The extractor's surface-form list is a whitelist,
   and a whitelist cannot find an inflection nobody predicted.** Same failure family as wave 2's `(?![a-z])`,
   one layer up — and the fourth instance in this wave of *the gate failing in its input, never in its
   judgement*. Run2 found the same gap in `refusal`: the concordance carries the noun (5) and misses the
   verb family (`refuse`/`refuses`/`refusing`, 4 more) — **and the canon row is SETTLED for the verb and
   only WEAK for the noun**, so the concordance hid the more important half.
