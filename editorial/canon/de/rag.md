# RAG term ledger (DE)

The **living** term ledger for the RAG & Agents course in German. It records this course's term decisions —
kept-EN vs native form, casing, bridge glosses, rejected variants — the way `canon/sk/rag.md` does for Slovak.
It grows with the course: every new lesson seeds its new terms here and settles them during native authoring.

**This is a bootstrap.** The Slovak `rag.md` accumulated 26 phases of sense cards, repeated block strings and
decision appendices; this file has the class policy and the seeded register and nothing else yet. **Terms with
no attestation are marked OPEN and are not settled** — an honest skeleton beats a complete-looking fiction.

**Load with `_language.md`.** The shared German language rules (term-direction policy, the loanword table with
gender/plural/genitive, Denglisch verb morphology, Durchkopplung, regional variance, calque templates,
verb-by-object, typography, register, bridge, bold, probation) are course-independent and live there. This
file holds only what is specific to the RAG course.

> **Cross-course term consistency — peek, don't load.** When authoring this course, load ONLY `_language.md` +
> this ledger as standing context. For a term that plausibly overlaps a sibling course (shared AI-engineering
> vocabulary — agent, prompt, token, context, eval, guardrail, retrieval…), do a TARGETED, read-only lookup in
> `canon/de/ai-sdlc.md`: if a decision exists and the sense matches, REUSE it verbatim and cite it — do not
> re-coin. If the sense genuinely differs, FLAG for a human — do not silently fork. Loading a whole sibling
> ledger as priming context is prohibited.

---

## §1 Class policy for this course

Per `_language.md` §1.0 the German default is **English-led with a German article**. This table records only
where this course's terms land and why — the direction itself is decided once, in `_language.md`.

| Class | Meaning | This course's members |
|---|---|---|
| **1 — exact identifiers / branded features** | English, code-styled or as a proper name; never translated, never inflected | `parallel_tool_calls`, `tool_choice`, `strict: true`, `additionalProperties`, `top_k`, **Structured Outputs**, product/model names |
| **2 — English-led with a German article (the DEFAULT)** | English term, German article, German inflection, Durchkopplung in compounds; one German gloss at first mention | the bulk of §2 below |
| **3 — German-led (the EXCEPTION)** | German term in the body; English original once in parentheses | das Modell, der Kontext, die Anfrage, die Abfrage, die Antwort, der Fehler, der Ausfall, die Latenz, der Durchsatz, die Berechtigung, die Zugriffssteuerung, die Bereitstellung |

**Reminder that governs every row below:** *an anglicism is not a defect in German* (`_language.md` §1.0).
Do not "improve" a class-2 row into a German coinage. What is a defect: a bare English term with no German
article, an undurchgekoppeltes compound, and a wobbling gender.

---

## §2 Kept-EN register — seeded from this corpus's actual high-frequency terms

Frequency counts are from the English source tree (`docs/`), so the list is ordered by what the German pages
will actually have to carry, not by what a glossary would list.

**Gender, plural and genitive for every term below live in `_language.md` §1.1.** If a term is not in that
table, it must be added there *before* its second use on any page.

### Settled as kept-EN (class 2)

*RAG, Retrieval, Ingestion, Generation, Guardrails, Observability, Serving, Pipeline, Embedding, Chunk,
Chunking, Chunk-Overlap, Bi-Encoder, Cross-Encoder, Reranking, Reranker, Trace, Tracing, Span, Grounding,
Prompt, Token, Top-K, HyDE, BM25, RRF, nDCG, MRR, ColBERT, MaxSim, Late Interaction, Multi-Vector, Contextual
Retrieval, Hybrid Search, Zero-Shot, Few-Shot, Faithfulness, Golden Set, LLM-as-a-judge, ReAct, Self-RAG,
Corrective RAG (CRAG), Adaptive RAG, Plan-and-Execute, Tree of Thoughts (ToT), Graph of Thoughts (GoT), LATS,
Self-Refine, Reflexion, MemGPT, Chain-of-Thought, Chain-of-Verification (CoVe), Self-Consistency, Scratchpad,
Context Precision, Context Recall, Reference-Free, Reference-Based, Pointwise, Pairwise, Prompt Injection,
Jailbreak, Spotlighting, Delimiting, Datamarking, Encoding, Instruction Hierarchy, PII, Red-Teaming,
Defence-in-Depth, Tool Poisoning, Rug Pull, Confused Deputy, MCP, Roots, Sampling, Elicitation, stdio,
Streamable HTTP, JSON Schema, Structured Outputs, Strict Mode, Constrained Decoding, Idempotency Key,
Dry-Run, Race Condition, Tool-RAG, Lost-in-the-Middle, Human-in-the-Loop (HITL), Checkpointing, Checkpoint,
StateGraph, Store, Durable Execution, Super-Step, Thread, A2A, Blackboard, Agent Card, TTFT, SSE,
PagedAttention, Continuous Batching, Prefill, Decode, Chunked Prefill, Prefix Caching, KV-Cache, LoRA, PEFT,
Fine-Tuning, SFT, DPO, Cold Start, Scale-to-Zero, Backpressure, Load Shedding, Admission Control,
Little's Law, Vendor-Lock-in, Managed Endpoint, Provisioned Throughput, Instrumentation, OpenTelemetry
(OTel), Canary Release, Shadow Deployment, Prompt Registry, Model Pinning, Model Routing, Fallback,
LLM-Gateway, Prompt Caching, Semantic Caching, Drift, Grader, Error Budget, Release Gate, Dead-Letter Queue
(DLQ), SLI, SLO, SLA, IAM, Golden Signals, Latency Budget, Soft Cap / Hard Cap, Alert, Dashboard, Matryoshka
(MRL), MTEB, Contrastive Learning, Hard Negatives, Extended Thinking, Reasoning Effort, Thinking Budget,
Hooks, Callbacks, Permission Modes.*

> **The list above is in CITATION form, not in running-prose form.** Multi-word terms are spelled per
> `_language.md` §1.3.3 the moment they sit in a German sentence: **noun + noun → hyphenated**
> (*Prompt-Injection*, *Tool-Poisoning*, *Rug-Pull*, *Model-Routing*, *Prompt-Caching*, *Error-Budget*,
> *Context-Precision*, *Dead-Letter-Queue*), **adjective + noun → may stay spaced and capitalised**
> (*Golden Set*, *Hybrid Search*, *Dense Retrieval*, *Strict Mode*, *Constrained Decoding*, *Cold Start*,
> *Semantic Caching*, *Durable Execution*). As soon as either kind heads a German compound, Durchkopplung is
> obligatory: *Golden-Set-Pflege*, *Strict-Mode-Fehler*, *Prompt-Injection-Angriff*. **When in doubt, look up
> §1.3.3 — do not guess from this list.**

**Bare names take a ZERO gloss** — the German gloss explains a definition, not a name: BM25, HyDE, ColBERT,
ReAct, MRL, RRF, nDCG, MRR, LATS, MemGPT, MaxSim, code identifiers, product names.

### Kept-EN with an OBLIGATORY German gloss at first mention

| Terminus | Glosse beim ersten Vorkommen |
|---|---|
| Fine-Tuning | „(Nachtrainieren des Modells)" |
| Guardrails | „(Leitplanken — Schutzregeln um das Modell)" — Bild bei heise belegt |
| Grounding | „(Rückbindung der Antwort an den Kontext)" |
| Store | „(Langzeitspeicher des Frameworks)" |
| Scale-to-Zero | „(Herunterskalieren auf null Instanzen)" |
| Backpressure | „(Gegendruck — Schutz vor Überlast)" |
| Load Shedding | „(gezieltes Abwerfen von Last)" |
| Zero-Shot | „(ohne Trainingsbeispiele)" |
| Race Condition | „(Fehler durch unkontrolliertes Timing zweier nebenläufiger Zugriffe)" — **nicht** „Wettlaufsituation" als Terminus |
| Confused Deputy | „(getäuschter Stellvertreter — eine privilegierte Komponente wird zum Missbrauch ihrer Rechte verleitet)" |
| Rug Pull | „(Austausch eines Tools nach der Freigabe)" |
| Dry-Run | „(Probelauf ohne Wirkung)" |
| Golden Set | „(handgeprüfter Referenzdatensatz)" |
| LLM-as-a-judge | „(ein Modell bewertet die Ausgabe eines anderen)" |

### German-led (class 3) — this course

| Kanon | Original | Hinweis |
|---|---|---|
| das Modell | model | „das Model" ✗ |
| der Kontext | context | — |
| die Anfrage | request | *der Request* nur für das Protokollobjekt |
| die Abfrage | query (an Index/Datenbank) | nicht mit *Anfrage* mischen |
| die Frage | query (Nutzerfrage) | — |
| die Antwort | answer / response | — |
| der Fehler | error | — |
| der Ausfall | outage | Verfügbarkeit, nicht Korrektheit (`_language.md` §9.2) |
| die Latenz / der Durchsatz | latency / throughput | Duden belegt beide, inkl. EDV-Sinn von *Durchsatz* |
| die Zugriffssteuerung | access control (ACL) | „Zugriffskontrolle" ist Kalke von *control* |
| die Bereitstellung; bereitstellen, ausrollen | deployment; to deploy | Substantiv *Deployment* bleibt kept-EN |
| die Halluzination; halluzinieren | hallucination | im deutschen KI-Diskurs etabliert |
| die Einbettung | embedding **als mathematischer Begriff** | **nur** dort, wo wirklich der mathematische Einbettungsbegriff gemeint ist; der Korpusterminus ist *das Embedding* |
| **der Endpunkt** | endpoint | **NEU 2026-07-28 — umgedreht.** heise schreibt in jedem geprüften Register *Endpunkt*, auch im ML-Serving („mit KServe **ein Endpunkt** bereitstellen"). „der Endpoint" ist im Deutschen fast nur der **Endgeräte**-Sinn der IT-Sicherheit |
| **die Inferenz** | inference | Duden-Lemma; heise durchgängig „Inferenz-Engine", „LLM-Inferenz". „die Inference" nicht verwenden |
| **die Quantisierung**; quantisieren | quantization | ⚠ **nicht** *Quantifizierung* — anderer Begriff, echter falscher Freund |
| **die Vektordatenbank** | vector database | de.wikipedia-Lemma + heise bis in die Schlagzeile. **„Vector Database" nie in deutscher Prosa** |
| **das Kontextfenster** | context window | heise definiert und verwendet es; der Loan nur in Herstellerdoku |
| **die Wissensbasis / die Wissensdatenbank** | knowledge base | Hausaufteilung: *Wissensbasis* = das abstrakte Wissen, über das ein System schließt; *Wissensdatenbank* = der konkrete gespeicherte Bestand. **„Knowledge Base" verliert deutlich** |
| **der Goldstandard** | golden set / golden dataset | Duden, richtiger Sinn. **„Golden Set" hat praktisch keine deutsche Attestierung**; deutsche Prosa schreibt *Golden Dataset (Goldstandard-Datensatz)* |
| **die hybride Suche** | hybrid search | Adjektiv+Substantiv, Adjektiv klein: *die hybride Suche*, *der hybriden Suche*. Der Loan zwingt zu *Hybrid-Search-Verfahren* und wirkt im deutschen Satz fremd. **WEAK** — dünner belegt als die übrigen Zeilen dieser Gruppe |
| **die Instrumentierung** | instrumentation | der Loan lebt im Deutschen nur noch in API-Eigennamen weiter |
| **das Fehlerbudget** | error budget | Computerwoche und iX schreiben ausschließlich deutsch |
| **die Protokollierung / das Protokoll** | audit trail | ⚠ **nie** *Prüfpfad* — umsatzsteuerrechtlicher Terminus, siehe `_language.md` §1.1.f |
| **die Bereitstellung / der Betrieb** | serving | „das Serving" mit deutschem Artikel ist unbelegt |
| **der Bewerter / das Bewertungsmodell** | grader | der Loan hat null deutsche Attestierung |
| **die Nutzlast / die Nutzdaten** | payload | das Lehnwort hat **kein** Wörterbuchlemma und kein stabiles Genus |

---

## §3 Nicht entschieden — OPEN und DISPUTED, nicht als Kanon präsentieren

**Zwei verschiedene Zustände, und die Unterscheidung ist ab 2026-07-28 scharf:** **OPEN** heißt *kein
brauchbarer Beleg gefunden* — jede Zeile nennt deshalb, **welcher Beleg sie schließen würde**. **DISPUTED**
heißt *die deutschen Quellen widersprechen einander* — dort wird der Incumbent **benannt und gehalten**, und
nichts geändert. **Nicht mehr DISPUTED ist „deutsche Norm gegen Projektkonvention"**: das entscheidet seit
2026-07-28 die Vorrangregel (`_language.md` § Typografie).

These need either an attestation or a cold read before they become rules. **Until then: avoid the word or
paraphrase.** Writing a plausible-sounding German form here is exactly the failure the Slovak locale hit with
„súbeh" — a coinage that passed one reviewer and was later struck as semantically wrong.

> **Die ausgelieferte UI-Locale ist KEIN Beleg für diese Zeilen.** Eine Prüfung aller 139 deutschen
> UI-Nachrichten (`i18n/de/**`, Stand #314) fand **keinen** Verstoß gegen die Tabelle unten — kein
> `Guardrail`-Singular, kein nacktes `Gate`, kein `Log`/`Queue`, keine `embedden`/`chunken`-Partizipien.
> **Das heißt nicht, dass die Zeilen erledigt sind.** Zwei Gründe, und nur der erste ist Verdienst:
> `Gate` und `Guardrail` wurden bewusst über die Sense-Card bzw. die Nur-Plural-Regel geführt — `Log`,
> `Queue` und die beiden Partizipien kamen schlicht **nicht vor**, weil eine Navigationsoberfläche sie nicht
> braucht.
>
> **Die erste deutsche Lektionsprosa hat dieses Glück nicht.** Genau diese vier sind in laufendem Text über
> Observability und Ingestion **unvermeidlich**. Wer aus „die Locale ist sauber" schließt, die offenen Zeilen
> seien geklärt, zieht den Schluss aus einer Oberfläche, die sie nie berührt hat. *(Befund: `de-ui-strings`,
> nach #314.)*
>
> **Aussagekraft der Prüfung: Wörter, nicht Begriffe.** Technisch wurden die Zeichenketten der 139
> UI-Nachrichten mit regulären Ausdrücken durchsucht; der Befund zeigt daher nur, welche Wörter nicht
> vorkommen, nicht, ob die betreffenden Begriffe inhaltlich vertreten sind. Dass die Suche nach `Gate` ohne
> Treffer bleibt, ist bei der gemäß der Sense-Card gewählten Umschreibung das erwartete Ergebnis: Die
> ausgelieferte Überschrift „Gestaffelte Kontrollpunkte" gibt den Gate-Begriff wieder, ohne das Wort zu
> verwenden.
>
> **Nachtrag aus dem Termledger-Durchgang (#275/#276), damit dieser Kasten nicht veraltet:** `Log` steht in
> der Aufzählung oben als offene Zeile — **es ist seither geschlossen** (Duden führt ein **eigenes
> EDV-Lemma** „das Log, die Logs" neben dem seemännischen DWDS-Eintrag). Die **Aussage des Kastens ändert
> das nicht**, sie wird nur schärfer: von den vier Zeilen, die in der UI „schlicht nicht vorkamen", sind
> jetzt drei noch offen (`Queue`, `embedden`, `chunken`) — und **genau die drei sind in Lektionsprosa über
> Ingestion und Observability unvermeidlich.**

> **Belegdurchgang 2026-07-28 — was sich hier geändert hat.** Von den Zeilen, die dieser Abschnitt als
> „offen" führte, sind **fünf geschlossen** worden, weil die Belege existierten und nur niemand an der
> richtigen Stelle nachgeschlagen hatte. Sie stehen als **durchgestrichene** Zeilen unten, mit dem, was sie
> geschlossen hat — ein Ledger, das seine eigenen Umkehrungen still überschreibt, ist der
> SK-Fáza-26-Fehlermodus.

| Terminus | Warum offen | Vorläufige Behandlung |
|---|---|---|
| ~~**Retrieval (Genus)**~~ | **GESCHLOSSEN 2026-07-28 — SETTLED.** Duden führt das **nackte Lehnwort** im EDV-Sinn: „das Retrieval; Genitiv: des Retrievals" <https://www.duden.de/rechtschreibung/Retrieval>. Es war nie unbelegt; die Recherche hatte nur *Information Retrieval* gesucht | **das Retrieval, des Retrievals** — jetzt zitierfähig. **Plural bleibt strittig** (DWDS markiert „nur im Singular") → im Korpus vermeiden |
| ~~**Log (IT-Sinn)**~~ | **GESCHLOSSEN 2026-07-28 — SETTLED.** Die DWDS-Warnung war richtig **und irrelevant**: der Duden hat ein **zweites, eigenes Lemma** „Log, Neutrum, Gebrauch **EDV**, die Logs" <https://www.duden.de/rechtschreibung/Log_EDV> | **das Log / die Logs** für die Signalklasse, **die Logdatei** für die Datei, *das Protokoll* nur ohne Verwechslungsgefahr mit dem **Netzwerk**protokoll |
| ~~**Embedding (Genus)**~~ / ~~**Chunk (Genus)**~~ | **auf WEAK hochgestuft 2026-07-28** — beide sind jetzt **flexionstragend** belegt (starke Adjektivendung bzw. Genitiv), siehe `_language.md` §1.1.a | **das Embedding**, **der Chunk** — nicht mehr bloße Analogie |
| ~~Tool Call / Tool Result — Schreibung~~ | **GESCHLOSSEN im Bootstrap.** Amtliches Regelwerk § 45 E1 entscheidet: Substantiv+Substantiv aus dem Englischen wird **zusammen oder mit Bindestrich** geschrieben, getrennt ist nicht normgerecht | **der Tool-Call, das Tool-Result, die Prompt-Injection** — siehe `_language.md` §1.3.3. Die in der Fachpresse verbreitete Getrenntschreibung ist genau die vom Regelwerk als „im Deutschen nicht normgerechte Getrenntschreibung" bezeichnete |
| **Guardrail (Singular)** | **präzisiert 2026-07-28.** Die frühere Notiz „nirgends belegt, auch nicht bei der BSI" ist **falsch**: die BSI-Handreichung zu LLM-Gegenmaßnahmen enthält *Guardrail* dreimal — aber **nur innerhalb englischer Maßnahmennamen** („Human Input Guardrail"), nie flektiert, **nie mit Artikel**. Der Kern hält: **kein Genus ist attestiert**, und die BSI übersetzt selbst mit **Filterung** | **nur im Plural** *Guardrails* (Glosse „(Leitplanken)"); *Leitplanken* ist im KI-Sinn belegt, aber **ebenfalls nur im Plural**. Singular umformulieren, **nicht erfinden** |
| **Queue (IT-Sinn)** | Wörterbuch kennt nur Billardstock und (veraltet) Warteschlange von Personen; **der Message-Queue-Sinn steht in keinem Wörterbuch** | Femininum ist in nativer Fachprosa gesichert → **die Queue** für die konkrete Broker-/Job-Queue, **die Warteschlange** für die **Datenstruktur** (de.wikipedia-Lemma) |
| **Gate (IT-Sinn)** | Wörterbuchgenus *das Gate* betrifft den Flughafen-Sinn | nur im festen Kompositum: **das Quality Gate** (heise-belegt, frisch nachgeprüft); **Release Gate** ist im Deutschen **OPEN** |
| **Ground Truth (Genus)** | **NEU 2026-07-28.** Kein deutscher Satz weist dem Ausdruck einen Artikel zu; *die* (nach *die Wahrheit*) und *der* (nach *der Grund*) sind **beide** begründbar | **artikelfrei verwenden** („als Ground Truth dienen", „die Ground-Truth-Labels") oder auf **der Goldstandard** ausweichen (Duden-belegt). *Grundwahrheit* wird in der deutschen Wissenschaftsprosa selbst infrage gestellt |
| **Recall / Precision (Richtung)** | **NEU 2026-07-28 — DISPUTED, die deutschen Quellen widersprechen einander.** de.wikipedia führt *Trefferquote* / *Genauigkeit*, das Fraunhofer IKS behält *Precision, Recall, Accuracy, F1-Score* englisch | **Incumbent kept-EN halten.** Zusatzgrund: „Genauigkeit" ist auch die übliche Wiedergabe von *accuracy* — eine deutsch geführte Metriktabelle kollidiert mit sich selbst. Einmal glossieren, dann artikelfrei |
| **Backpressure (Genus)** | **NEU 2026-07-28.** In **jedem** nativen Beleg **artikellos** verwendet | artikellos schreiben oder umformulieren („die Flusskontrolle") |
| **Load Shedding** | **NEU 2026-07-28.** *Lastabwurf* ist ein starkes deutsches Wort — **aber ausschließlich für Stromnetz und Kraftwerk**; die deutsche IT-Fachpresse verwendet **weder** die deutsche **noch** die englische Form und hat für diesen Vorgang **kein Wort** | den Vorgang beschreiben: „Anfragen gezielt abweisen", „Last gezielt abwerfen" |
| **Serving (als freies Substantiv)** | **NEU 2026-07-28.** Der Loan überlebt nur in englischen Komposita (*Serving Endpoints*); „das Serving von Modellen" hat null Attestierung | **die Bereitstellung / der Betrieb** |
| **Grader** | **NEU 2026-07-28 — zero German attestation at any tier** für die KI-Evaluationsbedeutung | **der Bewerter / das Bewertungsmodell / die Bewertungsinstanz** |
| **Cold Start** | **NEU 2026-07-28 — DISPUTED.** Ein einziger deutscher Artikel schreibt auf derselben Seite *Kaltstart* **und** *Cold-Start*; erschwerend ist *Kaltstart* im Deutschen zusätzlich mit dem **Motoren**- und dem **Rechenzentrums**-Sinn besetzt | Incumbent **der Cold-Start** halten, nichts ändern |
| **Drift (Genus)** | **NEU 2026-07-28 — DISPUTED.** Duden hat *die* Drift (Strömung) **und** *der* Drift (Motorsport), **keines im ML-Sinn** | Incumbent **der Drift**; **möglichst das Kompositum schreiben** — *die Datendrift*, *der Modelldrift*, *der Konzeptdrift* sind besser belegt |
| **„AI delta" → „KI-Delta"** | Autorenfigur, im Deutschen nicht geprüft | auf Probe; im Zweifel schlichte Prosa |
| **„token tax"** | im Russischen bestätigt, im Slowakischen **gestrichen** | **nicht übernehmen**; „die laufenden Kosten der Tool-Beschreibungen" |

---

## §4 Sense cards (to be filled as the course is authored)

A sense card fixes **one meaning per frame** and names the disambiguating question to ask before writing the
word. A reservation breach is a defect even when the sentence is otherwise correct. German polysemy differs
from Slovak and Russian polysemy — **do not port their cards**; the collisions are not the same.

Seeded from collisions already visible in the corpus:

- **`Fehler`** — *error* (ein einzelner Vorfall) vs. *failure* (der Name einer Fehlerklasse) vs. *bug*.
  Frage vor dem Schreiben: *Meine ich einen Vorfall, eine Kategorie oder einen Programmierfehler?* Vorschlag:
  Vorfall → **der Fehler**; Kategorie → **das Fehlerbild / die Fehlerklasse**; Ausfall der Verfügbarkeit →
  **der Ausfall**. **Auf Probe.**
- **`Suche` / `Retrieval` / `Recherche`** — *retrieval* (die Schicht/der Terminus) vs. *search* (die
  Handlung) vs. *search over a tree* (der algorithmische Durchlauf). Vorschlag: Terminus → **Retrieval**;
  Handlung → **suchen / die Suche**; Baum-/Graphdurchlauf → **die Suche im Suchraum / das Durchsuchen**.
  **Auf Probe.**
- **`Bewertung`** — *evaluation* (die Disziplin) vs. *score* (die Zahl) vs. *rating*. Vorschlag: Disziplin →
  **die Evaluation**; Zahl → **der Score**; „Bewertung" nicht für die Zahl. **Auf Probe.**
- **`Schicht`** — *layer* (Pipelinestufe des Buches) vs. *layer* (Verteidigungsschicht). Vorschlag: bei
  Verwechslungsgefahr nie nackt — **die Pipelinestufe** vs. **die Verteidigungsschicht**. **Auf Probe.**
- **`Speicher`** — *memory* (Agentengedächtnis) vs. *storage* (Ablage) vs. *cache*. Vorschlag: Gedächtnis →
  **das Gedächtnis / die Memory** (OPEN), Ablage → **der Speicher**, Zwischenspeicher → **der Cache**.
  **OPEN — nicht entschieden.**

---

## §5 Wiederkehrende Blockstrings — einmal entschieden, wörtlich zu übernehmen

**Diese Zeichenketten stehen 8–49-mal im Korpus.** Sie werden **nicht** pro Seite neu formuliert; wer eine
davon anders schreibt, erzeugt genau das Wackeln, das ein deutscher Leser als Maschinenausgabe liest.
**Die Zählungen sind am englischen Quellbaum gemessen (2026-07-28), nicht geschätzt** — die
Ground-Truth-Prüfung, die der slowakischen Locale in Fáza 25 gefehlt hat.

| EN (Quelle) | Vorkommen | **Deutsch — verbindlich** | Begründung / Status |
|---|---|---|---|
| `## What to take away` | 35 (RAG) + 26 (AI-SDLC) | **`## Das Wichtigste`** | bezeichnet unmittelbar die inhaltliche Zusammenfassung; „mitnehmen" wirkt metaphorisch und seminarsprachlich. Verworfen: „Das nehmen Sie mit". **HOUSE** — Registerurteil, kein Beleg |
| `:::note[Next — part 2 of the lesson]` | 20 | **`:::note[Als Nächstes: Teil 2 der Lektion]`** | „als Nächstes" ist ein vollständiger temporaler Verweis, der Doppelpunkt kündigt die Konkretisierung an. Verworfen: „Weiter: …". **HOUSE** |
| `:::note[Next — going deeper]` | 1 | **`:::note[Als Nächstes: die Vertiefung]`** | Gleichlage mit der Zeile darüber und mit dem Titelsuffix |
| `:::tip[▶ Video]` | 49 | **`:::tip[▶ Video]`** — unverändert | „Video" ist im Deutschen vollständig etabliert; das Symbol trägt die Funktion. **SETTLED, weil nichts zu entscheiden ist** |
| Videonachsatz (RU/SK setzen ihn, EN nicht) | 49 | **`(Das Video ist auf Englisch.)`** | Standarddeutsch setzt bei der Sprache die Präposition **auf**, und das Sprachadjektiv wird dabei **großgeschrieben** (Duden D 72: „etwas **auf Deutsch** sagen"). Verworfen: „(Video auf Englisch.)" — elliptisch, Anzeigenregister. **SETTLED für die Konstruktion** |
| `:::note[Status]` | 8 | **`:::note[Bearbeitungsstand]`** | benennt den Gegenstand und vermeidet die Mehrdeutigkeit von „Status" (Zustand vs. Rang). **HOUSE** |
| `:::note[Prerequisites]` | 3 | **`:::note[Voraussetzungen]`** | Duden, Bedeutung 3: „etwas, was vorhanden sein muss, um etwas anderes zu ermöglichen; Vorbedingung" <https://www.duden.de/rechtschreibung/Voraussetzung>. **SETTLED** |
| `:::note[Field note]` | 4 (nur AI-SDLC) | **`:::note[Aus der Praxis]`** | kennzeichnet Herkunft und Erfahrungscharakter natürlicher als das wenig etablierte Kompositum „Praxisnotiz". **HOUSE** |
| `:::info[How to read this]` | 2 | **`:::info[So lesen Sie diese Seite]`** | adressiert den konkreten Gebrauch und wahrt die Sie-Anrede. Verworfen: „Lesehinweise" (behördlich). **HOUSE.** ⚠ **Gegen die Infinitiv-Ausnahme geprüft:** ein Admonition-Titel ist **keine Bedienelementbeschriftung** (`_language.md` § Stimme und Anrede) — er steht auf keinem anklickbaren Element und benennt keine auslösbare Handlung. Die Infinitivregel greift hier **nicht**; „Diese Seite lesen" wäre die falsche Textsorte |
| `See also: …` | 17 (nur RAG) | **`Siehe auch: …`** | lexikalisierte Verweisform. **`siehe` ist hier KEINE Leseranrede** und kollidiert deshalb nicht mit der Sie-Regel — es ist die feste Verweisform. **HOUSE** |
| Titelsuffix `— deep dive` | 14 Seiten | **` – Vertiefung`** (mit Halbgeviertstrich **und Leerzeichen**) | bezeichnet die Intensivierung eines bereits behandelten Gegenstands, **ohne Niveau oder Reihenfolge zu behaupten** — anders als „Fortgeschritten" (Niveau) und „Teil 2" (Reihenfolge). **HOUSE für die Wortwahl.** ⚠ **Beleghinweis, weil er leicht falsch zitiert wird:** die Duden-Seite zu *Vertiefung* liefert das Synonym *Intensivierung*, ihre **Bedeutungsliste** ist aber „das Vertiefen" + „Einbuchtung, Senke". Der Sinn „zweiter, tieferer Durchgang durch denselben Stoff" steht beim **Verb**: „den Lehrstoff, das bereits Gelernte noch **vertiefen**" <https://www.duden.de/rechtschreibung/vertiefen>. **Beim Verblemma zitieren, nicht beim Substantiv.** Gestützt auf Stufe 4 durch den deutschen Hochschulgebrauch (*Vertiefungsmodul*, *Vertiefungsfach*) |
| Teiltitel `Part I — RAG` | 3 (RAG) + 5 (AI-SDLC) | **`Teil I – RAG`**, **`Teil III – Produktivbetrieb und LLMOps`** | *Teil* statt *Part*; **„und" statt „&"** (das kaufmännische Und ist im deutschen Buchtitelregister markiert); Halbgeviertstrich **mit** Leerzeichen. **HOUSE** |
| Spurenetikett der Infografikkarten | 91 Kartenstrings, alle auf **einer** Seite | **`DEMO` / `PRODUKTION`** | 4 bzw. **10 Zeichen** — gleichauf mit dem englischen Worst Case (`PRODUCTION`, 10) und damit **kein neuer** Worst Case, aber **bei 360 px zu prüfen**; Rückfall `PROD`. „BETRIEB" wäre kürzer, benennt die Spur aber allgemeiner. **HOUSE** |

> **Der Beleghinweis, der für diese ganze Tabelle gilt.** Sie ist mit einem unabhängigen Registerrichter
> (Cross-Model-Gate) erarbeitet **und dessen acht Quellen wurden anschließend einzeln abgerufen und gegen
> den ausgelieferten Seitentext geprüft** — alle acht hielten. Das ist erwähnenswert, weil dasselbe Modell
> zuvor eine Zuschreibung auf ein Glossar gestützt hatte, das den Begriff nicht enthielt. **Das
> verbleibende Risiko ist nicht die erfundene URL, sondern die Seite NEBEN der beweisenden** — genau der
> *Vertiefung*-Fall oben. **Wer eine dieser Zeilen später verteidigt, prüft den SINN, nicht die Existenz
> der Seite.**

---

## §6 Konstruktionen — wiederkehrende Satz- und Überschriftenformen dieses Kurses

> **Bedingungen, keine Ersetzungstabelle.** Jeder Eintrag nennt die englische Form, die deutschen
> **Rahmen**, **den Test, der zwischen ihnen entscheidet**, und je ein durchgearbeitetes Beispiel pro
> Zweig. **Wenn ein Eintrag anfängt, sich wie eine Nachschlagetabelle zu lesen, ist es ein schlechter
> Eintrag** — dann wird er über seine Bedingung neu geschrieben. Eine gut begründete Abweichung vom
> angebotenen Rahmen ist erwartetes Verhalten, kein Kanonverstoß.
>
> `_language.md` §9 hält die **kursunabhängigen** Konstruktionen (`N ways X does Y`, `Why X fails`,
> `X is not Y`). Hier stehen die Formen, die **dieser** Kurs trägt — und §6.1–§6.5 sind zugleich die
> Fundstelle für den AI-SDLC-Kurs (peek-don't-load), weil sie in beiden Kursen vorkommen.

### 6.1 `X vs Y` als Überschrift

Die häufigste Kontrastform des Buches: *Offline vs online eval*, *Pointwise vs pairwise evaluation*,
*Reversible vs irreversible masking*, *Reference-free vs reference-based evaluation*, *Bi-encoder vs
cross-encoder*, *Detection vs mutation*, *Deterministic vs semantic gate*.

**Der Rahmen richtet sich nicht nach den verglichenen Begriffen, sondern nach der behaupteten logischen
Beziehung.** „Oder", „gegen" und „statt" sind **keine** stilistischen Varianten von „vs." — sie **ändern
die Aussage**:

| Behauptete Beziehung | Rahmen | Durchgearbeitetes Beispiel |
|---|---|---|
| bloße **Alternative**, Entscheidungsfrage | „X oder Y" | *Reversible vs irreversible masking* → „**Reversible oder irreversible Maskierung?**" — eröffnet eine Auswahl, behauptet weder Konkurrenz noch Präferenz |
| gerichteter **Gegensatz**, Widerstreit | „X gegen Y" | *Detection vs mutation: gaming the metric* → „**Detektion gegen Mutation: Wie sich die Metrik ausspielen lässt**" — die beiden wirken hier antagonistisch aufeinander |
| kompakte, **zunächst neutrale** Gegenüberstellung | „X vs. Y" | *Pointwise vs pairwise evaluation* → „**Pointwise vs. Pairwise Evaluation**" — benennt nur die Vergleichsachse; welches Verfahren geeigneter ist, bleibt offen |
| **systematische Untersuchung** nach gemeinsamen Kriterien | „X und Y im Vergleich" | *Offline vs online eval* → „**Offline- und Online-Evaluation im Vergleich**" — der Abschnitt prüft beide an denselben Kriterien |
| **Ersetzung / Vorrang / Korrektur** einer Deutung | „X statt Y" | *Container as isolation vs security boundary* → „**Container als Isolationsgrenze statt als Sicherheitsgrenze**" — ein neutrales „vs." würde die Stoßrichtung verdecken |

**Test der Wahl:** *Was behauptet die Überschrift über das Verhältnis?* Nichts → „vs.". Eine Wahl →
„oder". Einen Konflikt → „gegen". Eine Prüfung → „im Vergleich". Ein Urteil → „statt".

**„vs." ist im Deutschen normgerecht und wird MIT Punkt geschrieben. STATUS: SETTLED.** Duden führt ein
eigenes Lemma **„vs."** („Wortart: Abkürzung … **Kurz für versus**")
<https://www.duden.de/rechtschreibung/vs_> und glossiert *versus* als „**gegen[über]; im Gegensatz zu**",
markiert *bildungssprachlich*, Präposition **mit Akkusativ** <https://www.duden.de/rechtschreibung/versus>.
Der Punkt folgt aus D 1: „Nach **Schreibabkürzungen** steht ein Punkt ‹§ 82›" — die spitzen Klammern
verweisen auf das **Amtliche Regelwerk**, die Regel steht also auf Stufe 1.
In deutscher Fachpresse ist die Form in Überschriften üblich („**Express vs. Koa**: JavaScript-Webframeworks
im Vergleich", heise), und dasselbe Haus setzt auch den Vergleichsrahmen („Python-Entwicklung: **PyCharm und
VS Code im Vergleich**"). **Beide Muster sind belegt; sie konkurrieren nicht, sie tragen verschiedene
Aussagen.**

**Achtung Ellipse — der häufigste Fehler dieser Form:** wo das Englische das Grundwort nur einmal setzt
(*Offline vs online eval*), braucht das Deutsche den **Ergänzungsstrich** → „**Offline- und
Online-Evaluation**", nicht „Offline und Online-Evaluation". Siehe §6.5.

### 6.2 `X: Y` — der Doppelpunkt-Untertitel

*Two ways to score: one answer at a time, or two head to head*, *The key tradeoff: large chunk vs. small
chunk*, *Atomic tasks: decomposition as control*, *Running agent fleets: isolation and parallelism*.

- **Rahmen A — Gegenstand + Präzisierung.** Test: *Ist Y ein Thema oder eine These?* **Thema** → „X: Y",
  klein weiter, wenn Y kein vollständiger Satz ist.
- **Rahmen B — Gegenstand + vollständige Aussage.** Ist Y die eigentliche **These**, steht dahinter ein
  vollständiger Satz und er beginnt **groß**: „Retries: **Sie** verändern die Verteilung."
- **Rahmen C — Tätigkeit + Mittel.** Trägt das Englische ein **Gerundium**, nimmt das Deutsche meist ein
  **Verb**: *Running agent fleets: isolation and parallelism* → „**Agentenflotten betreiben**: Isolation und
  Parallelität". „Der Betrieb von Agentenflotten …" ist korrekt, aber nominaler und verwaltungsnäher;
  **„Laufende Agentenflotten" ist der falsche Anschluss** an die `-ing`-Form.

### 6.3 `What X actually is` / `What "…" actually means`

*What an embedding actually is*, *What "calibrate against humans" actually means*.

- **Rahmen A — neutrale Definition: „Was unter X zu verstehen ist".** Test: wird der Begriff *definiert*
  oder sein Umfang abgegrenzt? → A.
- **Rahmen B — Korrektur eines Missverständnisses: „Was X tatsächlich bedeutet".** Nur wenn das Kapitel
  ausdrücklich gegen eine **verbreitete falsche Deutung** anschreibt: *tatsächlich* setzt einen Gegensatz
  zwischen Anschein und richtiger Bestimmung voraus.
- **Rahmen C — einordnende Handlungsüberschrift: „X richtig einordnen".** Wenn es weniger um die Definition
  als um Rolle, Abgrenzung und Konsequenzen geht.
- **Der Defekt, den dieser Eintrag verhindert: „Was X tatsächlich ist" OHNE Korrekturfolie.** Dann bildet
  *tatsächlich* nur englisches *actually* ab, und man hört das Englische mit. **Vom unabhängigen
  Registerrichter als einer von drei Übersetzungsverrätern benannt.**

### 6.4 Zählüberschrift mit Ortsangabe — `Three points where it sits`

- **„Die drei Stellen, an denen …"** — wenn die Punkte in Pipeline, Architektur oder Abbildung
  **lokalisierbar** sind. **„ansetzt" ist meist präziser als das räumlich übersetzte „sitzt".**
- **„Drei Ansatzpunkte für …"** — wenn keine Orte, sondern **Eingriffsmöglichkeiten** gemeint sind.
- **„Drei Berührungspunkte zwischen … und …"** — wenn zwei Komponenten oder Zuständigkeiten
  **aufeinandertreffen**.
- **„Drei Aspekte von …"** — wenn *where* im Englischen nur locker-metaphorisch ist.
- **Test:** *Kann ich die drei Punkte in ein Diagramm einzeichnen?* Ja → „Stellen". Nein, es sind
  Handlungsmöglichkeiten → „Ansatzpunkte". Nein, es ist nur eine Gliederung → „Aspekte".

### 6.5 Der Ergänzungsstrich in koordinierten Komposita — der häufigste Defekt dieser Klasse

Das Englische koordiniert **ohne Markierung**: *head-based and tail-based sampling*, *offline and online
eval*, *pre-filter / post-filter*, *bi-encoder and cross-encoder*, *soft cap / hard cap*, *reference-free vs
reference-based*. Das Deutsche **muss** den gemeinsamen Bestandteil mit einem **Ergänzungsstrich** anbinden:

- *head-based and tail-based sampling* → „**Head- und Tail-Sampling**" (nicht „Head und Tail Sampling")
- *pre-filter / post-filter* → „**Vor- und Nachfilterung**" (deutsch geführt) oder „**Pre- und Post-Filter**"
- *soft cap / hard cap* → „**Soft- und Hard-Cap**"
- *reference-free vs reference-based* → „**referenzfreie und referenzbasierte** Bewertung"

**Test:** teilen die beiden Glieder ein Grundwort? Dann trägt das erste den **Ergänzungsstrich**, und das
Grundwort steht nur am zweiten. Fehlt der Strich, entsteht genau die Getrenntschreibung, die das Amtliche
Regelwerk als „im Deutschen nicht normgerecht" bezeichnet (`_language.md` §1.3.3).

### 6.6 Der Schichtname als Überschrift — `Retrieval`, `Generation`, `Serving`, `Guardrails`

Die Kapitel dieses Kurses heißen nach den **Schichten** der Pipeline, und die Schichtnamen sind
**klassenverschieden** — das ist die Falle: *Retrieval*, *Generation* und *Guardrails* bleiben englisch
(§2), *Serving* ist im Deutschen **kein freistehendes Substantiv** (§3), *Evaluation* wird zu **Evaluierung**
(`_language.md` §1.1.e).

- **Test:** steht der Name in §2 (kept-EN) oder in §3/§1.1.g (deutsch geführt)? **Nachschlagen, nicht
  ableiten** — die Nachbarüberschrift entscheidet nichts.
- **Wenn der Schichtname deutsch geführt ist, wird die Überschrift umgebaut, nicht das Wort ersetzt:**
  `Serving — deep dive` → „**Bereitstellung und Betrieb – Vertiefung**", nicht „Serving – Vertiefung".
- **Die Teilüberschriften des Glossars koppeln den Schichtnamen an ein Thema** (`Ingestion — chunking`,
  `Agents — planning & loops`, `Production — serving`). Dort bleibt der Halbgeviertstrich **mit**
  Leerzeichen, und **beide** Glieder folgen ihrer eigenen Klasse: „**Ingestion – Chunking**",
  „**Agenten – Planung und Schleifen**", „**Produktivbetrieb – Bereitstellung**". ⚠ **Die Anker-IDs ändern
  sich dabei NICHT** — siehe §7.

---

## §7 Der Glossar-Vertrag — Ankerkennungen, bevor irgendjemand das deutsche Glossar schreibt

**Dieser Abschnitt entscheidet keine Termini. Er verhindert, dass die Welle, die das deutsche Glossar
schreibt, den Build zerlegt oder Links stillschweigend fehlleitet.** Er steht hier, weil er sonst in keiner
Datei stünde, die diese Welle lädt.

**1 — Die Anker sind ein locale-übergreifender VERTRAG.** Der Terme-Fuß jeder Lektion verlinkt auf
`../glossary.md#some-id`, und **denselben Link teilen alle Locales**. Eine übersetzte Überschrift
slugifiziert zu etwas ganz anderem — ein Auto-Slug kann den Anker deshalb nicht tragen.

**2 — Schreibweise: mit BACKSLASH.** Die Anker stehen in der Form `\{#id}`. Der Backslash ist **Pflicht**:
`docusaurus.config.ts` setzt `future: { v4: true }`, damit ist der MDX-1-Kompatibilitätspräprozessor für
Heading-IDs abgeschaltet, und eine nackte `{` wird als **JSX-Ausdruck** geparst — **der Build schlägt hart
fehl**. Der Backslash ist Markup, nicht Teil der ID.

**3 — Gleiche IDs, gleiche REIHENFOLGE.** `scripts/locale_parity.py` prüft die **geordnete Folge** der
expliziten Heading-IDs gegen das Englische. Nicht die Menge — die **Folge**. Der Grund steht im Skript
selbst: eine mittendrin eingefügte Zeile verschiebt jede ID darunter um eins; jede ID existiert weiter, die
Anzahl stimmt weiter, die Menge ist weiter gleich — und **jeder eingehende Link landet auf dem
Nachbareintrag**. Die lesende Person bekommt eine plausible falsche Definition, und das ist der Fehler,
den niemand meldet.

**4 — Praktische Folge.** Die deutsche Glossarseite **übersetzt die Abschnittsüberschriften, nicht die IDs**:

```
EN:  ## Ingestion — chunking \{#ingestion-chunking}
DE:  ## Ingestion – Chunking \{#ingestion-chunking}
```

*(Beachte zugleich den Strichwechsel — U+2014 → U+2013 mit Leerzeichen, `_language.md` § Typografie.)*
Ein neuer Eintrag wird **nie** nur in einer Locale eingefügt; er kommt in **alle** oder in keine.

**5 — Die 19 Anker dieses Kurses, in der verbindlichen Reihenfolge** (`docs/glossary.md`, Stand
2026-07-28), damit die Glossarwelle sie nicht aus einer womöglich veralteten Datei ableitet:

`ingestion-chunking` · `ingestion-embeddings` · `retrieval` · `generation` · `evaluation` · `guardrails` ·
`observability` · `agentic-rag` · `tools` · `planning-loops` · `multi-agent` ·
`orchestration-frameworks` · `mcp` · `real-agents` · `production-failures` · `serving` ·
`cloud-platforms` · `tooling-ecosystem` · `llmops`

**6 — Der Umfang, den diese Welle einplanen muss:** 8 901 englische Wörter, **298 fettgesetzte Lemmata**.
Jedes Lemma ist eine Termentscheidung, und **jede dieser Entscheidungen bindet Lemma UND Fließtext** —
genau die Stelle, an der das slowakische Korpus auseinanderlief (das Glossar führte Englisch, der Text
führte Slowakisch, korpusweit korrigiert in Fáza 25).

---

## §8 Phasenanhang

Chronologisches Protokoll der Entscheidungen dieses Ledgers. **Umkehrungen werden hier lesbar gehalten,
nicht überschrieben** — ein Kanon, der seine eigenen Umkehrungen still ersetzt, ist der
SK-Fáza-26-Fehlermodus.

### Phase 1 (Bootstrap) — Klassenpolitik und Startregister
Klassenpolitik übernommen aus `_language.md` §1.0 (englisch geführt mit deutschem Artikel als **Regelfall**,
invertiert gegenüber dem Slowakischen); Startregister aus den tatsächlichen Hochfrequenztermini des
englischen Quellbaums; Sense-Cards **auf Probe**; §5 leer.

### Phase 2 (2026-07-28) — Belegdurchgang, Blockstrings, Konstruktionen, Glossarvertrag
**Sechs parallele Belegbatches** (Infrastruktur/Serving, RAG/ML, Observability/Evaluation, Agenten/Tools,
Softwareprozess/Sicherheit, Verbmorphologie) plus ein Zitatprüf-Durchgang. Ergebnis für diesen Kurs:

- **Fünf zuvor offene Zeilen geschlossen**, alle fünf, weil der Beleg existierte und niemand an der
  richtigen Stelle nachgeschlagen hatte: *Retrieval* (Duden-EDV-Lemma für das **nackte** Lehnwort),
  *Log* (**zweites** Duden-Lemma, EDV), *Embedding* und *Chunk* (flexionstragende Belege), *Least
  Privilege* im Schwesterledger (BSI). **Lehre, die in den Kanon gehört: „unbelegt" hieß mehrfach
  „falsch gesucht".**
- **Vierzehn Termini gegen den Reflex umgedreht** — die deutsche Form gewinnt (`_language.md` §1.1.g). Der
  teuerste war **Endpoint → Endpunkt**, weil er im Bootstrap als HOUSE mit dem Loan gesetzt war.
- **Drei Zeilen als DISPUTED neu eröffnet**, weil die deutschen Quellen einander widersprechen:
  *Harness* (heise gegen heise), *Cold Start* (ein Artikel gegen sich selbst), *Drift* (zwei
  Duden-Lemmata, keines im ML-Sinn). **Alle drei behalten den Incumbent und ändern nichts.**
- **Vier Wörterbuchfallen neu gefunden** und in `_language.md` §1.1 in einen benannten Kasten überführt:
  *Checkpoint* (Grenzübergang), *Rollback* (Kalter Krieg), *Span* (Holzspan, Plural *Späne*),
  *Grounding* (Swissair). Zusammen mit *Log*, *Gate*, *Queue* sind es **neun**.
- **Typografie: der Gedankenstrich — entschieden in #313, hier nur belegt.** U+2013 **mit** Leerzeichen,
  U+2014 raus; die Korpusumstellung lief in #314 (21 Vorkommen), die Zählung wurde in #315 korrigiert.
  Dieser Durchgang kam **unabhängig** zum selben Ergebnis und hat die **Stufe-1-Belege nachgetragen**, die
  die ursprüngliche Entscheidung nicht führte (DIN 5008; Regelwerk § 77 mit 66 : 0). Über acht
  deutsche Quellen **gemessen**: ≈ 220 × „–", 0 × „—". Das betrifft **jeden** Seitentitel dieses Kurses.
- **§5 (Blockstrings), §6 (Konstruktionen), §7 (Glossarvertrag), §8 (dieser Anhang) angelegt.**
- **Sechs MT-Quellen disqualifiziert**, jede mit benanntem Widerspruch (siehe `_language.md` §1.1, Falle 4).
- **Die Kollokationsfalle als stehende Regel aufgenommen** (`_language.md` §1.1, Falle 3), nachgereicht aus
  dem UI-String-Durchgang (#279): **Blindbewertung und Attestierung sind zwei Gates.** Zwei flüssige
  deutsche Formulierungen hatten dort eine korrekt durchgeführte Blindbewertung gewonnen und fielen erst
  bei der Attestierung — beide waren deutsches Material auf **englischem Kollokationsgerüst**. Wer eine
  mehrwortige Wiedergabe festlegt, attestiert **die Fügung**, nicht nur das Kopfnomen.
- **Was offen bleibt und warum:** *Ground Truth* (Genus), *Grader*, *Backpressure* (Genus), *Load
  Shedding*, *Serving* (als freies Substantiv), *Release Gate*, *Guardrail* (Singular). Für alle sieben ist
  in §3 notiert, **welcher Beleg sie schließen würde**. Die deutsche Fachbuchschicht (dpunkt, Rheinwerk,
  O'Reilly DE) und die kostenpflichtigen iX-/c't-Volltexte sind die Ebene, die keiner der Durchgänge
  erreichen konnte — **dort liegen die meisten dieser sieben Antworten.**
