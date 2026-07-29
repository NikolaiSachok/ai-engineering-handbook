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
| **1 — exact identifiers / branded features** | English, code-styled or as a proper name; never translated, never inflected | `parallel_tool_calls`, `tool_choice`, `strict: true`, `additionalProperties`, `top_k`, `p95` / `p99`, `query:` / `passage:`, `tail_sampling`, **Structured Outputs**, **Sampling (die MCP-Fähigkeit)**, product/model names |

> **Umstellung Welle 1 (2026-07-28) — `Sampling` als MCP-Primitive wandert von Klasse 2 nach Klasse 1, und
> der Grund ist ein Beleg, der dem falschen Referenten gehörte.** Der Kanon besitzt für `Sampling` **eine**
> deutsche Attestierung (`_language.md` §1.1.e, heise) — und die gehört dem **statistischen
> Observability-Sinn**: „Metriken und Traces [kommen] in der Regel nur als Stichprobe … an (**Sampling**),
> … **das Sampling** reduziert die Datenmenge". Die MCP-Zeile und die Token-Decoding-Zeile standen in §2
> ~~**ohne eigene Attestierung** und fuhren auf diesem Beleg mit. Das ist **der `Span`-Fehler eine Etage
> höher**: korrektes Genus für den falschen Referenten.~~
> **Korrektur Welle 2 (2026-07-29): diese Begründung ist überholt, die Entscheidung nicht.** heise
> attestiert `Sampling` inzwischen **im MCP-Referenten und flektiert** („Durch den Wegfall **des Samplings**
> …"; „die bisherigen **Funktionen Roots, Sampling** und Logging"). Die MCP-Bedeutung reitet also nicht mehr
> auf fremdem Beleg – **und die befürchtete Falle existiert morphologisch gar nicht**: der Beleg ergibt
> *das Sampling, des Samplings*, **identisch** mit dem Appellativ; die beiden Sinne unterscheiden sich
> **nur im Referenten**, nicht im Genus. Klasse 1 bleibt richtig, aber als **Disambiguierungs**entscheidung
> statt als Attestierungsentscheidung: ein großgeschriebener, unflektierter Eigenname signalisiert dem Leser
> den MCP-Sinn dort, wo *des Samplings* mit dem statistischen verwechselbar wäre. (Präzedenz
> `_language.md` §1.3.1: **die Regel steht, die Begründung war falsch.**) Als **Feature-Eigenname** (wie `Roots`,
> `Elicitation`, `Structured Outputs`) ist die MCP-Fähigkeit gar kein Appellativ mehr und kollidiert nicht.
> Das Appellativ **das Sampling** behält seinen Beleg und seine §1.1.e-Zeile. Für den **Decoding**-Sinn gilt
> unverändert §3, Zeile `Sampler`: die Stufe benennen, nicht personifizieren; das Substantiv möglichst als
> Kompositum (*Top-K-Sampling*), nie nackt. Sense-Card in §4.
> ⚠ **Gemessen, nicht vermutet:** in dieser Welle kommt `sampling` **27-mal** vor und **jedes einzelne
> Vorkommen ist der statistische Sinn** (Head-/Tail-/Priority-Sampling von Traces sowie *active sampling*
> beim Labeln). Die MCP- und die Decoding-Bedeutung treten in Teil I **gar nicht** auf — die Umstellung ist
> also **Vorsorge für Teil II**, nicht Reparatur einer Welle-1-Seite. `Roots` und `Elicitation` haben
> dieselbe Gestalt, werden hier aber **ausdrücklich NICHT** umgestellt: sie kommen in dieser Welle nicht
> vor, und ein Zusammenführungsdurchgang entscheidet nichts, was er nicht gelesen hat.
> **Welle 2 (2026-07-29): beide kommen vor und werden umgestellt.** `Roots` → **Klasse 1, SETTLED** (heise
> führt es als unflektierten Eigennamen im deutschen Satz). `Elicitation` → **Klasse 1, aber HOUSE**:
> Formgleichheit mit `Roots`, **keine deutsche Attestierung im MCP-Sinn** – ausdrücklich **nicht** als
> belegt darstellen. Pflichtglosse: „(der Server fragt über den Client beim Menschen nach)"; ⛔ jede
> Wiedergabe über *Anforderung*, weil die deutsche Softwaretechnik „Requirements Elicitation =
> **Anforderungserhebung**" bereits besetzt. Register beider Zeilen: `_language.md` §1.1.c.
> ⚠ **Und die Zurückstellung von Welle 1 hat sich messbar bezahlt gemacht:** weil niemand vorgegriffen hat,
> steht die Umstellung heute auf einem **echten Beleg** statt auf einer Analogie zu `Sampling`.
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
Retrieval, Hybrid Search, Zero-Shot, Few-Shot, Faithfulness, ~~Golden Set~~, LLM-as-a-judge, ReAct, Self-RAG,
Corrective RAG (CRAG), Adaptive RAG, Plan-and-Execute, Tree of Thoughts (ToT), Graph of Thoughts (GoT), LATS,
Self-Refine, Reflexion, MemGPT, Chain-of-Thought, Chain-of-Verification (CoVe), Self-Consistency,
~~Scratchpad~~,
Context Precision, Context Recall, Reference-Free, Reference-Based, Pointwise, Pairwise, Prompt Injection,
Jailbreak, Spotlighting, Delimiting, Datamarking, Encoding, Instruction Hierarchy, PII, Red-Teaming,
Defence-in-Depth, Tool Poisoning, Rug Pull, Confused Deputy, MCP, Roots, Elicitation, stdio,
Streamable HTTP, JSON Schema, Structured Outputs, Strict Mode, Constrained Decoding, Idempotency Key,
Late Chunking (OPEN, §3),
Dry-Run, Race Condition, Tool-RAG, Lost-in-the-Middle, Human-in-the-Loop (HITL), Checkpointing, Checkpoint,
StateGraph, Store, Durable Execution, ~~Super-Step~~, Thread, A2A, Blackboard, Agent Card, TTFT, SSE,
PagedAttention, Continuous Batching, Prefill, Decode, Chunked Prefill, Prefix Caching, KV-Cache, LoRA, PEFT,
Fine-Tuning, SFT, DPO, Cold Start, Scale-to-Zero, Backpressure, Load Shedding, Admission Control,
Little's Law, Vendor-Lock-in, ~~Managed Endpoint~~, ~~Provisioned Throughput~~ → Klasse 1, ~~Instrumentation~~, OpenTelemetry
(OTel), Canary Release, Shadow Deployment, Prompt Registry, Model Pinning, Model Routing, Fallback,
LLM-Gateway, Prompt Caching, Semantic Caching, Drift, Grader, Release Gate, Dead-Letter Queue
(DLQ), SLI, SLO, SLA, IAM, Golden Signals, Soft Cap / Hard Cap, Alert, Alerting, Dashboard, Matryoshka
(MRL), MTEB, Contrastive Learning, Hard Negatives, ~~Extended Thinking~~, ~~Reasoning Effort~~,
~~Thinking Budget~~, ~~Hooks, Callbacks, Permission Modes~~ → aufgespalten, siehe den Welle-2-Kasten.*

> **Drei Streichungen aus dieser Liste, Welle 1 (2026-07-28) — sichtbar gestrichen, nicht still entfernt.**
> Ein Ledger, das seine eigenen Umkehrungen überschreibt, ist der SK-Fáza-26-Fehlermodus.
>
> - ~~**Error Budget**~~ → **das Fehlerbudget.** ⚠ **Das war ein Selbstwiderspruch INNERHALB DIESER DATEI:**
>   die Liste oben führte den Loan, während die deutsch geführte Tabelle in §2, `_language.md` §1.1.g **und**
>   §1.2 alle drei **das Fehlerbudget** setzen. Die deutsche Zeile ist die **belegte** (Computerwoche und
>   iX schreiben ausschließlich deutsch, die englische Form kommt in beiden Artikeln kein einziges Mal vor);
>   die kept-EN-Nennung war ein **Bootstrap-Rest**. **Der Widerspruch stand seit dem Bootstrap in einer
>   Datei und ist von keinem Prosa-Gate gefunden worden** — Gates lesen Sätze, nicht Register.
>   *(Batch E; Schreibung mitgezogen in `_language.md` §1.3.3.)*
> - ~~**Latency Budget**~~ → **§3, OPEN.** Die Zeile stand hier kept-EN **ohne jeden Beleg**. Der Duden führt
>   für `Budget` **keine** Bedeutung „Menge, die man gegen ein Ziel verbrauchen darf" — der SRE-Sinn ist im
>   Deutschen **nur über das Kompositum** attestiert (*das Fehlerbudget*), und für *Latenzbudget* gibt es
>   keins. **Nicht ersatzlos gestrichen, sondern nach §3 verschoben**, mit Schließbedingung und Korpusform.
>   *(Batch E.)*
> - ~~**Sampling**~~ (als MCP-Primitive) → **Klasse 1**, siehe den Kasten in §1. Das **Appellativ**
>   *das Sampling* (Observability) bleibt kept-EN und behält seine §1.1.e-Zeile. *(Batch E.)*
>
> **Neu in der Liste:** `Alerting` (das Alerting, kein Plural — flexionstragend belegt, `_language.md`
> §1.1.e) und `Late Chunking` (**mit OPEN-Marker**: die Schreibung ist durch Kanonregel entschieden, die
> Attestierung fehlt — wer den Marker abschneidet, liest die Zeile als gleichwertig zu *Late Interaction*,
> und genau das ist sie nicht).

> **Fünf Streichungen, eine Aufspaltung und eine Anmerkung – Welle 2 (2026-07-29), RAG Teil II.**
> Wieder sichtbar gestrichen, nicht still entfernt; wieder ist die häufigste Ursache dieselbe: **eine Zeile
> stand hier als „settled kept-EN", ohne dass je etwas attestiert worden wäre.**
>
> - ~~**Scratchpad**~~ → **§3, OPEN.** Die Zeile stand hier kept-EN **ohne jeden Beleg**. Der Loan **ist**
>   im Deutschen attestiert – im **falschen Sinn**: CPU-naher Speicher, 23 de.wikipedia-Treffer, alle
>   Hardware, und *Fairchild Channel F* glossiert `scratchpad RAM` mit **Arbeitsspeicher**. Korpusform:
>   **das Arbeitsgedächtnis** (ein Referent, ein Name); Erstnennung koppelt einmal („das
>   **Arbeitsgedächtnis** – das Scratchpad aus Teil 1"). `Scratchpad` überlebt nur als Rückverweis auf
>   Teil 1 und als Kompositumsglied. ⚠ **`der Arbeitsspeicher` bleibt für RAM reserviert** und ist **nie**
>   die Wiedergabe von *working memory* – das Wort steht im selben Absatz und muss sauber getrennt bleiben.
>   *(Der Batch, der den Namen verlor, hat die Streichung gewonnen: er hatte den **Loan** studiert, während
>   der andere den **Referenten** studiert hatte. Wer den Referenten eigens studiert, schlägt wer den Loan
>   nachschlägt – die Vorrangregel aus Welle 1.)*
> - ~~**Super-Step**~~ → **§3, OPEN.** Stand kept-EN **ohne Beleg und ohne Genus**. Vier Durchgänge
>   berichten denselben Nullbefund: de.wikipedia `insource` **0**; *Bulk Synchronous Parallel* und
>   *Pregel (Framework)* haben **kein** deutsches Lemma (beide Abrufe: Seite existiert nicht); Duden `Step`
>   ist der **Steppschritt**, und `Super-Step` ist **kopffinal**, sodass die Kompositumsbildner-Ausnahme
>   nicht greift. **Dieselbe Gestalt wie ~~`Latency Budget`~~.** Korpusform: „speichert den Zustand des
>   Graphen **nach jedem Knotenübergang** (im LangGraph-Vokabular: *Super-Step*)" – das Englische einmal,
>   kursiv, artikellos, in Klammern.
> - ~~**Extended Thinking**~~, ~~**Reasoning Effort**~~, ~~**Thinking Budget**~~ → **Klasse 1.** Es sind
>   **Herstellerstellschrauben** (`thinking`, `reasoning.effort`, `thinkingBudget`), keine Appellative;
>   de.wikipedia-Attestierung **0 : 0 : 0**. Sie stehen unverändert englisch, artikellos, in Codeschrift,
>   mit Glosse bei Erstnennung. Für `Thinking Budget` gilt zusätzlich: der **appellative** Gebrauch wird
>   **umgebaut** – „wie viel **Nachdenken** eine Aufgabe bekommen darf"; ⛔ *das Denkbudget* und
>   *das Rechenbudget* (je 0 Treffer, das wäre die *Latenzbudget*-Prägung ein zweites Mal); das deutsche
>   Kompositum **das Thinking-Budget** nur dort, wo ein Artikel erzwungen ist (`_language.md` §1.1.c).
> - **Aufgespalten: ~~`Hooks, Callbacks, Permission Modes`~~.** Die drei standen gemeinsam am Ende der
>   Liste als Teil-II-Vorgriff, also als **Marken** – aber `hook` und `callback` werden im Korpus **auch
>   appellativ** gebraucht („a pre-hook that can block", „a `before_tool` callback"). Also:
>   **Klasse 1** – `Claude Code Hooks`, `ADK Callbacks`, `Permission Modes` (nur Plural; keinen Singular
>   erfinden, sondern den Wert nennen: „der Modus `plan`"). **Klasse 2, appellativ, mit neuen
>   `_language.md` §1.1.c-Zeilen** – **der Hook**, **der Callback**.
>   ⚠ **Und dabei ist eine Kanonzeile falsifiziert worden:** die `Hook`-Zeile behauptete von
>   de.wikipedia *Hook (Informatik)* „**das Lemma flektiert nie**". Es flektiert **sechsmal**, Genitiv
>   eingeschlossen – geprüft an der Quelle, die die Zeile selbst zitiert. Die Zeile steht jetzt auf
>   **SETTLED**. *(Der Gegendurchgang, der stattdessen DWDS las, fand nur den **Golf- und Boxschlag** und
>   hätte den WEAK-Status bestätigt – ein volles Paradigma für den falschen Referenten.)*
> - **Anmerkung, keine Streichung: `Soft Cap / Hard Cap`.** Der Mustername ist echt und bleibt – er ist nur
>   **nicht der Laufterm**. **Zitierform des Musternamens; im Fließtext die weiche / die harte
>   Obergrenze**; ⛔ „das Cap" / „der Cap" (**kein attestiertes Genus in diesem Sinn**, in keinem
>   Wörterbuch). Zwei Namen für einen Referenten auf einer Seite sind das *Richtungswackeln* aus §1.0, und
>   die Seite mit dem attestierten Paradigma gewinnt. Dieselbe Anmerkung gilt für §6.5, „Soft- und
>   Hard-Cap" – die **Ergänzungsstrich-Konstruktion bleibt gültig**, wo das Paar als Paar benannt wird.

> **Drei Streichungen, Welle 3 (2026-07-29), RAG Teil III — und sie stehen alle drei in EINER Zeile der
> Liste (der Produktiv-/Serving-Zeile), die diese Welle als erste tatsächlich gebraucht hat.**
> Es ist die Gestalt aus **#327, Frage 2 und 3**: *ein Terminus steht in einem Abschnitt als settled, während
> ein anderer ihn deutsch führt oder gar keine Zeile für ihn hat.* ⚠ **Und die drei Zeilen brauchen drei
> VERSCHIEDENE Auflösungen — ein pauschaler Sweep hätte eine davon falsch eingeordnet.** Das ist der Grund,
> warum #327 „Beispiel ersetzen, nicht Regel schwächen" sagt und nicht „Liste durchstreichen".
>
> - ~~**Managed Endpoint**~~ → **der Endpunkt** (§1.1.g). Der Loan stand hier settled, **ohne §1.1-Zeile** —
>   ein Zeiger auf eine leere Zelle (#327, Frage 3) —, während `endpoint → der Endpunkt` an **fünf** Stellen
>   deutsch geführt und SETTLED ist: `_language.md` §1.1 (umgedreht am 2026-07-28, Duden), §1.2, der
>   Fallenkasten, **der Injektionsblock** (Punkt 4, wörtlich in jeden Render-Prompt kopiert) und die
>   §2-Tabelle dieser Datei. Dazu das eigene Phasenprotokoll (§8): „die teuerste war **Endpoint → Endpunkt**".
>   **Fünf gegen eins, und die eine ist ein Bootstrap-Rest**, den der Umkehrungsdurchgang nicht mitgezogen
>   hat, weil er das **nackte** Substantiv drehte und niemand das **Markenkompositum** nachgesehen hat —
>   genau die Welle-1-Falle (`Budget`, `Cap`, `Signal`: Zeile fürs Kompositum, keine fürs Appellativ),
>   diesmal spiegelverkehrt.
>   ⚠ **Der Quelltext entscheidet die Klassenfrage, und zwar durch die Schreibung:** „models run as
>   **managed endpoints**" ist klein und im Plural, also ein **Appellativ**, kein Produktname.
>   **Gegenstimme im Protokoll (Slice C, run 1), und sie ist inhaltlich stark:** im deutschen IT-Markt ist
>   *Managed + Endpoint* der **stehende Name des Endpoint-Security-/MDR-Marktes**; der Slice wollte den
>   Incumbenten mit Pflichtglosse halten. **Beide Wege führen zur selben Korpusform** — „**der Endpunkt des
>   Anbieters**", nie nacktes `Managed Endpoint` —, und genau deshalb wird die kept-EN-Zeile gestrichen
>   statt gehalten: **sie lizenziert die nackte Form, die in die falsche Branche zeigt.**
> - ~~**Provisioned Throughput**~~ → **Klasse 1**, nicht deutsch geführt. **Hier wäre ein pauschaler Sweep
>   falsch gewesen.** Der Quelltext schreibt es durchgehend **groß** und als **Herstellerangebot** („Bedrock
>   as **Provisioned Throughput** and Reserved terms", „Azure sells it as PTU (**provisioned throughput
>   units**)"). Es ist ein **Produktname** wie `Golden Signals`, kein Appellativ — es kollidiert also gar
>   nicht mit `der Durchsatz`, sondern war bloß in der falschen Klasse einsortiert. Das **Appellativ** im
>   selben Absatz (klein: *provisioned throughput units*) läuft weiter über **den Durchsatz**.
> - ~~**Instrumentation**~~ → **die Instrumentierung** (§1.1.g). Der Quelltext schreibt es **klein und
>   appellativisch** (7×, u. a. als Glossarlemma in `[New terms]`), und *die Instrumentierung* steht
>   **im Injektionsblock**. Ein Terminus, den der Block namentlich als deutsch geführt aufzählt, darf nicht
>   zwei Dateien weiter als settled kept-EN stehen.
>
> **Gegen #327 protokolliert**, damit der dortige Sweep diese drei nicht neu herleitet — und mit dem Befund,
> den sie zusammen tragen: **die Prüffrage „steht der Terminus woanders anders?" reicht nicht; man muss die
> Schreibung im QUELLTEXT lesen, um zu wissen, welche der drei Auflösungen die richtige ist.**

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

> **Reparatur 2026-07-29 (Welle-1-Konsistenzdurchgang): die Glossen in dieser Tabelle standen mit
> Geviertstrich U+2014 — dem Zeichen, das § Typografie dem Korpus VERBIETET und das die Codepoint-Zählung
> zurückweist.** §2 weist die Renderer an, diese Zeichenketten **wörtlich** zu übernehmen; der Kanon hat also
> jedem Renderer aufgetragen, einen verbotenen Codepoint auszuliefern. **Fünf Glossen sind auf `–` (U+2013,
> mit Leerzeichen) korrigiert** — `Guardrails`, `Backpressure`, `Confused Deputy`, `Faithfulness`,
> `Alerting` —, dazu die `Groundedness`-Glosse in `_language.md` §1.1.b und die `Harness`-Glosse in
> `ai-sdlc.md` §2.
>
> ⚠ **Alle sechs Renderer der Welle haben den Strich selbstständig korrigiert**, unabhängig voneinander: die
> dreizehn ausgelieferten Seiten führen **0× U+2014**. Das ist der Beleg dafür, dass der Kanon der defekte
> Teil war, nicht die Prosa — und es ist derselbe Befund wie bei `Golden Set` weiter unten: **wo ein Register
> und sechs unabhängige Renderer auseinandergehen, ist das Register der Verdächtige.**
>
> ⚠ **Ausdrücklich NICHT angetastet, und die Abgrenzung ist die eigentliche Entscheidung:**
> (a) die **Metaprosa** dieser Redaktionsdateien — das ist §8 §O und Issue #318, eine **locale-weite
> redaktionelle** Frage, die dieser Durchgang nicht an sich zieht;
> (b) **Zitate aus Quellen** (die BSI-Sätze in `_language.md` §1.1.f, der englische Quelltextausschnitt in
> §3 `verbosity bias`) — **ein Zitat zu glätten fälscht den Beleg**, und das Register lebt von seinen Belegen;
> (c) die Stellen, an denen der Geviertstrich **selbst der Gegenstand** ist („—" als genanntes Zeichen).
>
> **Die Regel, die daraus folgt und die künftige Zeilen bindet: eine Zeichenkette, die §2 zum wörtlichen
> Übernehmen freigibt, ist ein AUSGELIEFERTER String und untersteht der Typografie — auch wenn sie in einer
> Redaktionsdatei steht.**

| Terminus | Glosse beim ersten Vorkommen |
|---|---|
| Fine-Tuning | „(Nachtrainieren des Modells)" |
| Guardrails | „(Leitplanken – Schutzregeln um das Modell)" — Bild bei heise belegt |
| Grounding | „(Rückbindung der Antwort an den Kontext)" |
| Store | „(Langzeitspeicher des Frameworks)" |
| Scale-to-Zero | „(Herunterskalieren auf null Instanzen)" |
| Backpressure | „(Gegendruck – Schutz vor Überlast)" |
| Load Shedding | „(gezieltes Abwerfen von Last)" |
| Zero-Shot | „(ohne Trainingsbeispiele)" |
| Race Condition | „(Fehler durch unkontrolliertes Timing zweier nebenläufiger Zugriffe)" — **nicht** „Wettlaufsituation" als Terminus |
| Confused Deputy | „(getäuschter Stellvertreter – eine privilegierte Komponente wird zum Missbrauch ihrer **eigenen** Rechte verleitet)" *(Welle 2, 2026-07-29: an die ausgelieferte Fassung angeglichen. §2 gibt diese Zeichenkette zum wörtlichen Übernehmen frei, also durfte sie nicht von der ausgelieferten Seite abweichen – und die ausgelieferte gewinnt, weil sie besser liest und veröffentlicht ist.)* |
| Rug Pull | „(Austausch eines Tools nach der Freigabe)" |
| Dry-Run | „(Probelauf ohne Wirkung)" |
| ~~Golden Set~~ → **der Goldstandard** | ~~„(handgeprüfter Referenzdatensatz)"~~ — **GESTRICHEN, siehe den Kasten unter dieser Tabelle.** Die Glosse überlebt als Apposition zum deutschen Terminus: „der **Goldstandard** (*golden set*) – der handgeprüfte Referenzdatensatz" |
| LLM-as-a-judge | „(ein Modell bewertet die Ausgabe eines anderen)" |
| **Faithfulness** *(neu, Welle 1)* | „**(Quellentreue – wie treu die Antwort den herangezogenen Quellen bleibt, ohne unbelegte Informationen hinzuzufügen)**" |
| **Groundedness** *(neu, Welle 1)* | dieselbe Glosse; **nur als Kompositumsglied** — „die Groundedness-Metrik", „der Groundedness-Wert". ⛔ „das/die Groundedness" mit Artikel |
| **Alerting** *(neu, Welle 1)* | „(Alarmierung – die Regeln, nach denen ein Alarm ausgelöst wird)"; danach kept-EN weiterlaufen |

> **Vierte Streichung aus §2 — Welle-1-Konsistenzdurchgang (2026-07-29), in der Form der
> `Error-Budget`-Streichung, weil es derselbe Fehlertyp ist: ein Selbstwiderspruch INNERHALB DIESER DATEI.**
>
> - ~~**Golden Set**~~ → **der Goldstandard.** ⚠ Der Loan stand **zweimal** in §2 — in der
>   settled-kept-EN-Liste **und** in der Glossentabelle darüber —, während die **deutsch geführte Tabelle
>   derselben §2** und `_language.md` §1.1.b beide **der Goldstandard** setzen: Duden, Bedeutung 2, volles
>   Paradigma, mit der ausdrücklichen Notiz „**‚Golden Set' hat praktisch keine deutsche Attestierung**".
>   **Drei Zeilen gegen zwei — und die zwei waren die belegten.**
> - **Die Welle hatte die Frage längst entschieden, bevor sie jemand stellte: `Goldstandard` 29×,
>   `Golden Set` 0×** — fünf Seiten, sechs Renderer, kein einziger Rückfall.
> - **Die Glosse ist nicht verloren, sie dreht sich um.** Klasse 3 heißt „deutscher Terminus im Fließtext,
>   englisches Original einmal in Klammern"; die Korpusform ist **„der Goldstandard (*golden set*) – der
>   handgeprüfte Referenzdatensatz"**, und `cross-cutting/evaluation/index.md` schreibt sie bereits so.
> - ⚠ **Was NICHT mitgestrichen wird:** `Ground Truth` bleibt **OPEN** (`_language.md` §1.1.b). Die Welle
>   verwendet es artikelfrei („als Ground Truth dienen", „die Ground-Truth-Labels") — genau das, was die offene
>   Zeile vorschreibt. **Eine Streichung entscheidet die Nachbarzeile nicht mit.**

> **Wie die `Faithfulness`-Zeile hierher kam — eine Gate-6.5-Entscheidung, ausdrücklich protokolliert.**
> Batch A fand beim Attestieren von `groundedness` zwei unabhängige deutsche Quellen, die **dieselbe**
> Glosse setzen: heise („**Quellentreue (Faithfulness)**: Wie treu bleibt die generierte Antwort den
> bereitgestellten Quelldokumenten, ohne unbelegte Informationen hinzuzufügen?") und die Juristische
> Fakultät der HHU Düsseldorf („Wie gut passen die generierten Ergebnisse zu den zitierten Dokumenten
> (**Quellentreue**)?"). `Faithfulness` stand in §2 als **settled kept-EN ohne Glosse**; Batch A hat die
> Frage **eskaliert statt §2 anzufassen** — das war richtig, und hier ist die Antwort:
>
> **Die Zeile wird NICHT umgedreht, sie bekommt eine Glosse.** Die Klasse bleibt 2 (kept-EN mit deutschem
> Artikel); sie wandert nur aus der glossenlosen Liste in diese Tabelle. Grund: die beiden Quellen
> **glossieren** den englischen Terminus, sie **ersetzen** ihn nicht — genau die Brückenrichtung aus §7.
>
> ⚠ **Und die Doppelglossen-Sorge, die Batch A mitgemeldet hat, ist geprüft und aufgelöst:** `Grounding` →
> „(Rückbindung der Antwort an den Kontext)" und `Faithfulness/Groundedness` → „(Quellentreue)" sind
> **nicht zwei Wörter für einen Referenten**. *Grounding* ist der **Vorgang** (die Antwort an den Kontext
> binden), *Faithfulness/Groundedness* ist die **gemessene Eigenschaft**. Sense-Card in §4 — sie steht
> dort, weil genau diese Unterscheidung ohne sie beim nächsten Durchgang wieder eingeebnet würde.

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
| **die Kosinus-Ähnlichkeit** | cosine similarity | de.wikipedia-Lemmatitel; **8 : 0** gegen *Cosinus-*; heise + INNOQ. „Cosine Similarity" in deutscher Prosa **nie** *(Welle 1)* |
| **der Dienst** | service | ⚠ `der Service` hat in **beiden** Wörterbüchern ein volles Paradigma und in **keinem** unseren Sinn. Loan nur im Kompositum (*Microservice*) *(Welle 1)* |
| **die Reihenfolge** · **das Ranking** · **der Rang** | ordering · ranking · rank | drei Referenten, drei Wörter. ⛔ *die Anordnung* (Duden-Sinn 2 = **Verfügung**) *(Welle 1)* |
| **die Passage / der Textabschnitt** | passage | Duden-Sinn 4; *Textpassage*, wo `Passage` sonst ortshaft läse. **Nicht** synonym mit *Chunk* — §4 *(Welle 1)* |
| **das Bewertungsraster** | rubric | ⛔ **die Rubrik** — kein Bewertungssinn in Duden **oder** DWDS *(Welle 1)* |
| **die Regression** *(mit Pflichtglosse)* | regression (Softwaretest) | „eine Regression (eine durch eine Änderung verursachte Verschlechterung)". ⛔ das Verb *regredieren* *(Welle 1)* |
| **die Kalibrierung**; kalibrieren | calibration | ⚠ **nur** der Judge-Sinn. *RRF needs no calibration* → **die Score-Normierung** *(Welle 1)* |
| **der Schwellenwert** | threshold | ⛔ *die Schwelle* für einen Zahlenwert (Eisenbahnschwelle) *(Welle 1)* |
| **die Übereinstimmung zwischen den Annotatoren** | inter-annotator agreement | Umschreibung ist die Korpusform; *IAA* einmal einführen; Überschrift: *die Interrater-Reliabilität* *(Welle 1)* |
| **die Schwärzung / die Maskierung** | redaction / masking | BSI. ⛔ *die Redaktion*; ⚠ *Anonymisierung* für *redaction* ist **sachlich falsch** *(Welle 1)* |
| **die Erfolgsrate der Angriffe (ASR)** | attack success rate | BSI: fünf Vorkommen, und `Angriffserfolgsrate` **0×** im selben Dokument *(Welle 1)* |
| **die Metadaten** *(nur Plural)* | metadata | Duden: **Pluralwort**. *metadata filtering* → **verbal**: „nach Metadaten filtern" *(Welle 1)* |
| **das Verfahren** | technique | ⛔ *die Technik* — im Deutschen zuerst die Technologie *(Welle 1)* |
| **die Domäne** | domain | ⛔ *die Domain*. Der AD-Sinn steckt im deutschen Wort; die **Fügung** entschärft ihn *(Welle 1)* |
| **die Chunk-Größe** | chunk size / chunk length | ⚠ **Genuswechsel:** *der* Chunk → **die** Chunk-Größe. **Eine** Benennung, obwohl das Englische zwischen *size* und *length* wechselt *(Welle 1)* |
| **die Normierung**; normieren | normalisation | **WEAK.** ⛔ *die Normalisierung* als bloßes Substantiv; Ausnahme **L2-normalisiert** *(Welle 1)* |
| **die Deduplikation**; deduplizieren | deduplication | volles Duden-Paradigma für Substantiv **und** Verb; Anweisungsform „Duplikate entfernen" *(Welle 1)* |
| **der Widerspruch**; widersprechen **+ Dativ** | conflict | ⛔ *der Konflikt* für zwei Quellen — im Deutschen zwischenmenschlich, mit **Parteien** *(Welle 1)* |
| **das Perzentil** | percentile | `das 95. Perzentil` (Ziffer, Punkt, Leerzeichen). `p95` bleibt Klasse 1 *(Welle 1)* |
| **die Obergrenze / das Limit** | cap | ⛔ „das Cap" nackt. *A budget is a cap* → „**Ein Budget ist eine Obergrenze**" *(Welle 1)* |
| **mehrsprachig** | multilingual | Duden definiert *multilingual* über das deutsche Wort; als Modellnamensteil unangetastet *(Welle 1)* |
| **die Rechteausweitung** | privilege escalation | de.wikipedia-Lemma; ⛔ *eskalieren* für „stufenweise zunehmen" *(Welle 1)* |

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
| **Gate (IT-Sinn)** | Wörterbuchgenus *das Gate* betrifft den Flughafen-Sinn. **BLEIBT OPEN — bestätigt und verschärft im Piloten 2026-07-28:** der einzige echte bloße Plural (`Interne Gates` / `Externe Gates`, de.wikipedia *Quality Gate*) steht **anaphorisch nach eingeführtem `Quality Gate`** und zeigt kein Genus; ⚠ **und die lebendige Falle ist nicht der Flugsteig, sondern das LSTM-Gate** (`_language.md` §1.1, Fallenkasten). Ausführlich im Nachtrag unter der Tabelle | nur im festen Kompositum: **das Quality Gate** (heise-belegt, frisch nachgeprüft); **Release Gate** ist im Deutschen **OPEN**. Für den eingefügten Check: „eine **Prüfung vorschalten**"; für *to gate*: „**nur nach Freigabe zulassen**"; wo der strukturelle Punkt gebraucht wird: **der Kontrollpunkt** |
| **Sampler** | **NEU OPEN 2026-07-28 (DE-Pilot).** Duden **und** DWDS führen ausschließlich Musiksinne (die Sampler-CD, das Sampling-Instrument); **kein einziger deutscher Satz** mit `der Sampler` im LLM-Sinn, in keiner Flexion | **die Stufe benennen, nicht personifizieren.** Deutsche Prosa schreibt den Kanon-Regelfall *Substantiv englisch (`das Sampling`), Verb deutsch (`auswählen`)*: „Greedy Decoding **wählt** das Token mit der höchsten Wahrscheinlichkeit **aus**" (heise), „Top-K Sampling: aus den k wahrscheinlichsten Token **auswählen**" (Fraunhofer IESE). ⛔ *abtasten* ist auf die Signalverarbeitung festgelegt |
| **Bestätigungsschritt** | **NEU OPEN 2026-07-28 (DE-Pilot).** Nur Übersetzungsspeicher und Hersteller-UI-Doku → disqualifiziert | **„eine ausdrückliche Bestätigung", „eine Rückfrage"** |
| **Orchestrierungsschicht** | **NEU OPEN 2026-07-28 (DE-Pilot).** Null native Treffer; heise greift stattdessen zum englischen **Orchestration-Layer** | **die Steuerungsschicht** (de.wikipedia *Schichtenarchitektur*, flektiert belegt und dort ausdrücklich mit *Orchestrierung* zusammengestellt) |
| **Ground Truth (Genus)** | **NEU 2026-07-28.** Kein deutscher Satz weist dem Ausdruck einen Artikel zu; *die* (nach *die Wahrheit*) und *der* (nach *der Grund*) sind **beide** begründbar | **artikelfrei verwenden** („als Ground Truth dienen", „die Ground-Truth-Labels") oder auf **der Goldstandard** ausweichen (Duden-belegt). *Grundwahrheit* wird in der deutschen Wissenschaftsprosa selbst infrage gestellt |
| **Recall / Precision (Richtung)** | **NEU 2026-07-28 — DISPUTED, die deutschen Quellen widersprechen einander.** de.wikipedia führt *Trefferquote* / *Genauigkeit*, das Fraunhofer IKS behält *Precision, Recall, Accuracy, F1-Score* englisch | **Incumbent kept-EN halten.** Zusatzgrund: „Genauigkeit" ist auch die übliche Wiedergabe von *accuracy* — eine deutsch geführte Metriktabelle kollidiert mit sich selbst. Einmal glossieren, dann artikelfrei |
| **Backpressure (Genus)** | **NEU 2026-07-28.** In **jedem** nativen Beleg **artikellos** verwendet | artikellos schreiben oder umformulieren („die Flusskontrolle") |
| **Load Shedding** | **NEU 2026-07-28.** *Lastabwurf* ist ein starkes deutsches Wort — **aber ausschließlich für Stromnetz und Kraftwerk**; die deutsche IT-Fachpresse verwendet **weder** die deutsche **noch** die englische Form und hat für diesen Vorgang **kein Wort** | den Vorgang beschreiben: „Anfragen gezielt abweisen", „Last gezielt abwerfen" |
| **Serving (als freies Substantiv)** | **NEU 2026-07-28.** Der Loan überlebt nur in englischen Komposita (*Serving Endpoints*); „das Serving von Modellen" hat null Attestierung | **die Bereitstellung / der Betrieb** |
| **Grader** | **NEU 2026-07-28 — zero German attestation at any tier** für die KI-Evaluationsbedeutung | **der Bewerter / das Bewertungsmodell / die Bewertungsinstanz** |
| **Cold Start** | **NEU 2026-07-28 — DISPUTED.** Ein einziger deutscher Artikel schreibt auf derselben Seite *Kaltstart* **und** *Cold-Start*; erschwerend ist *Kaltstart* im Deutschen zusätzlich mit dem **Motoren**- und dem **Rechenzentrums**-Sinn besetzt | Incumbent **der Cold-Start** halten, nichts ändern |
| **Drift (Genus)** | **NEU 2026-07-28 — DISPUTED.** Duden hat *die* Drift (Strömung) **und** *der* Drift (Motorsport), **keines im ML-Sinn** | Incumbent **der Drift**; **möglichst das Kompositum schreiben** — *die Datendrift*, *der Modelldrift*, *der Konzeptdrift* sind besser belegt |
| **„AI delta" → „KI-Delta"** | Autorenfigur, im Deutschen nicht geprüft. **BLEIBT OPEN — und der Pilot durfte sie nicht bestätigen:** jeder belegte deutsche Sinn von `Delta` ist eine **messbare Zahldifferenz** (DWDS „Lücke, Differenz", Beleg aus dem Haushaltskontext; daneben Buchstabe, NATO-Alphabet, Flussdelta, Virusvariante, Börsen-Delta), unsere Verwendung ist **qualitativ**. **Kanonregel angewandt: der Durchgang, der einen Terminus prägt, darf nicht der sein, der ihn bestätigt** | auf Probe; im Zweifel schlichte Prosa — **die Korpusform des Piloten:** „Hier liegt der entscheidende Unterschied zur gewöhnlichen API-Entwicklung." |
| **„token tax"** | im Russischen bestätigt, im Slowakischen **gestrichen** | **nicht übernehmen**; „die laufenden Kosten der Tool-Beschreibungen" |
| **Latency Budget / Latenzbudget** | **NEU OPEN 2026-07-28 (Welle 1) — und diese Zeile ist eine UMKEHRUNG:** sie stand in §2 als settled kept-EN, **ohne jeden Beleg**. Der Duden führt für `Budget` **keine** Bedeutung „Menge, die man gegen ein Ziel verbrauchen darf"; der SRE-Sinn ist im Deutschen **nur über das Kompositum** attestiert (*das Fehlerbudget*, Computerwoche + iX) — für *Latenzbudget* existiert keins | **umbauen**: „**Für die Latenz gilt eine Obergrenze von …**", „**das vorgegebene Latenzziel**". ⛔ „das Latency Budget" mit deutschem Artikel. **Was es schließen würde:** ein flektierter deutscher Satz bei heise/iX/INNOQ/dpunkt mit *Latenzbudget* oder mit artikeltragendem *Latency Budget* |
| **Tail-Latenz / „the tail"** | **NEU OPEN 2026-07-28 (Welle 1).** Für *Tail-Latenz* stammen die **einzigen** deutschsprachigen Treffer von `beefed.ai`, einer KI-generierten Content-Farm — vom Auftrag **ausdrücklich disqualifiziert, nicht abgewertet**; *der Schwanz der Verteilung* nur aus derselben Quelle. `Tail` ist im Deutschen schlicht **nicht angekommen** — es gibt nichts zu verwechseln, weil es nichts gibt | **die Perzentilform** (`_language.md` §1.1.e): „die Latenz im **95. Perzentil**", „der **p95-Wert** der Latenz", am klarsten „**die langsamsten 5 % der Anfragen**"; für „the tail" umschreiben: „**der obere Rand der Verteilung**", „**die seltenen, langsamen Anfragen**". ⛔ **die Ausreißer** — das ist eine **sachliche** Verfälschung, keine stilistische. **Was es schließen würde:** ein flektierter Satz bei heise/iX/c't/INNOQ/dpunkt oder ein de.wikipedia-Lemma; für „the tail" ein deutsches SRE-Fachbuch mit einem stehenden Substantiv |
| **Alert Fatigue / Alarmmüdigkeit** | **NEU OPEN 2026-07-28 (Welle 1) — und es ist ein REGISTER-, kein Bedeutungsproblem, was die seltenere und genauso teure Sorte ist.** *Alarmmüdigkeit* ist attestiert (Charité, Institut für Medizinische Informatik) und der Mechanismus ist **identisch** mit unserem — aber das Wort ist im Deutschen fest in der **Intensivmedizin** verankert; ein deutscher Entwickler liest Stationsalltag, nicht SRE. Strukturell dieselbe Lage wie **`Lastabwurf`**, nur ist dort das Fach fremd und hier **benachbart**. ⚠ Aussagekräftiger Nullbefund: ein deutscher Fachtext über genau dieses Problem enthält `Alarmmüdigkeit` **null Mal** — und ist zusätzlich eine wortgleich auf fünf Seiten stehende **Pressemitteilung**, zählt also nur als Nullbefund | **das Phänomen beschreiben, nicht benennen**: „wer zu viel alarmiert, wird nicht mehr gehört", „zu viele Alarme stumpfen ab", „die Zuständigen gewöhnen sich an die Alarme und übersehen den einen, der zählt". Wo ein Terminus unvermeidlich ist: kept-EN **`Alert Fatigue`, artikelfrei**, mit deutscher Umschreibung in Klammern. **Was es schließen würde:** **ein** flektierter Satz bei heise/iX/c't/INNOQ/dpunkt/Rheinwerk mit *Alarmmüdigkeit* **oder** *Alert Fatigue* über **Bereitschaftsdienst/On-Call** — einer reicht, die Wortbildung ist unstrittig, nur der Registertransfer ist offen |
| **burn-rate alerting** | **NEU OPEN 2026-07-28 (Welle 1).** Für *Burn Rate* liefert die Herstellerlokalisierung „die **Brennrate** des Fehlerbudgets" (Google Cloud de) — und Google Cloud de ist in genau diesem Themenfeld bereits **disqualifiziert** (`_language.md` §1.1, Falle 4) | **umbauen**: „**Alerts auf die Burn Rate**", „**wenn die Burn Rate steigt, …**". **Was es schließen würde:** ein deutscher Satz bei heise/iX/INNOQ/dpunkt mit **flektierter** *Burn Rate* oder mit einer deutschen Vollform, die **nicht** *Brennrate* ist |
| **staleness / freshness (Index-Aktualität)** | **NEU OPEN 2026-07-28 (Welle 1) — keine Attestierung auf einer zulässigen Stufe.** Alle Treffer der gezielten Suche waren SEO-Agenturseiten, Anbieter-Glossare, KI-generierte Wissensseiten und Google-Cloud-Lokalisierung; diese Klassen sind ausdrücklich disqualifiziert. ⛔ *die Frische* ist im Deutschen auf **Lebensmittel** festgelegt und liest sich sofort übersetzt; ⛔ *die Veraltung*, *der Veraltungsgrad*, *der Aktualitätsrückstand* sind **Prägungen ohne Beleg** — der „súbeh"-Fehlermodus | **den Zustand als Nebensatz schreiben, nicht als Substantiv**: „**wie aktuell der Index ist**", „**veraltete Einträge**", „**der Index hinkt der Quelle hinterher**", „**seit der letzten Indexierung geänderte Dokumente**". *die Aktualität* ist ein gewöhnliches deutsches Wort und **darf im Satz vorkommen** — festgelegt wird die **Fügung** nicht. **Was es schließen würde:** ein Satz bei heise/iX/c't/INNOQ/dpunkt/Rheinwerk oder ein de.wikipedia-Lemma, in dem *Aktualität* einen **Index, Datenbestand oder Cache im Genitiv regiert** — oder ein deutsches Substantiv für *staleness*, das nicht erst für diesen Anlass gebildet wurde |
| **answer relevance** | **NEU OPEN 2026-07-28 (Welle 1) — und die Nullbefunde sind ordentlich erhoben.** Verworfen: `myscale.com/blog/de` (MT-Lokalisierung des englischen Originals), `innowise.com/de` (MT-Signal: „**Ein guter** „LLM-as-a-judge"-**Modell**"), Fraunhofer IESE (**404 beim Abruf** — der Treffer stammte aus einer Suchvorschau und zählt deshalb **nicht**). ⚠ **Gegenläufiges Signal, ehrlich vermerkt:** heise **verdeutscht** die Schwestermetrik (*Quellentreue (Faithfulness)*) — *die Antwortrelevanz* wäre also nicht abwegig, sie ist nur **unbelegt** | **Incumbent kept-EN halten, artikelfrei** und vorzugsweise als Kompositumsglied: „der **Answer-Relevance-Wert**", „die **Answer-Relevance-Metrik**" (Durchkopplung, §1.3.3). Beim ersten Vorkommen glossieren: „(wie gut die Antwort die gestellte Frage trifft)". ⚠ **§2 führt drei der vier RAGAS-Metriken** (Faithfulness, Context Precision, Context Recall) — **die vierte wird dort ergänzt, sobald diese Zeile schließt, und vorher nicht.** **Was es schließen würde:** **ein einziger** deutscher Satz bei heise/iX/dpunkt/Fraunhofer/INNOQ oder in deutscher Hochschullehre, der die RAGAS-Metrik benennt — artikeltragend englisch („**die** Answer Relevance liegt bei …") oder deutsch („**die Antwortrelevanz** misst …") |
| **Inter-Annotator-Agreement (Genus des Loans)** | **NEU OPEN 2026-07-28 (Welle 1).** Der Loan ist in deutscher Wissenschaftsprosa belegt — aber **ausnahmslos artikellos bzw. als Klammereinschub**; **kein kasusmarkierter Beleg** | **die attestierte Umschreibung verwenden**: „die **Übereinstimmung zwischen den Annotatoren**" (*zwischen* + Dativ), Kürzel **IAA** einmal einführen; als **Überschrift** ist **die Interrater-Reliabilität** zulässig (de.wikipedia-Lemma). **Was es schließen würde:** ein deutscher Satz bei heise/iX/dpunkt oder in einem Hochschulskript mit **kasusmarkiertem** „das/der Inter-Annotator-Agreement" |
| **verbosity bias · self-preference / self-enhancement bias** | **NEU WEAK 2026-07-28 (Welle 1) — und das ist eine Gate-6.5-Entscheidung gegen die Zurückhaltung des Batches, deshalb steht sie hier vollständig.** Batch A hat das Bildungsmuster auf **Stufe 1** belegt (BSI-Bias-Whitepaper: geschlossenes Kompositum, deutsches Erstglied, englisches Original in Klammern — *Repräsentationsbias*, *Messungsbias*, *Präsentationsbias*, *Auswahlbias* u. a., 16 Geschwister) und die beiden Wörter **bewusst nicht geprägt**, weil es ihre Vorkommen nicht zählte. **Gezählt (2026-07-28): `verbosity bias` 4×, `self-preference` 6× + `self-enhancement` 2×** — beide liegen also über der Nachtragsschwelle und **müssen** eine Wiedergabe haben. **Das Muster lizenziert die FORM, nicht das WORT:** die konkreten Komposita sind **unattestiert** | **der Ausführlichkeitsbias (Verbosity Bias)** · **der Selbstbevorzugungsbias (Self-Preference Bias)** — Genus und Genitiv vom belegten Grundwort (*der Bias*, *des Bias*, §1.1.a). **Die Klammer mit dem englischen Original ist PFLICHT, nicht Zierrat** — sie ist das, was eine musterlizenzierte Prägung tragbar macht, und die BSI macht es selbst so. Wo der Quelltext das Wort **ohne** „bias" verwendet („**Self-preference** — the judge rating outputs in its own style"), **nicht substantivieren, sondern den Satz bauen**: „das Modell **bevorzugt Antworten im eigenen Stil**", „die **Bevorzugung längerer Antworten**". **Was es schließen würde (WEAK → SETTLED):** ein deutscher Satz bei heise/iX/dpunkt/Fraunhofer/BSI mit **einem der beiden Komposita flektiert** |
| **fusion (bloßes Substantiv im IR-Sinn)** | **NEU OPEN 2026-07-28 (Welle 1).** Kein deutschsprachiger T1–T5-Beleg für `Fusion`/`fusionieren` mit **zwei Rangfolgelisten** als Objekt. ⚠ **Der Nullbefund, der die Zeile trägt:** INNOQ — ein deutsches Haus, genau unsere Drucklatte — schrieb seinen RRF-/Hybrid-Search-Artikel **nur auf Englisch**. Duden führt vier Sinne, **keinen** über Listen oder Rangfolgen; der Leitsinn ist die **Unternehmensfusion**, sodass ein kalt eingeführtes „die Fusion" im Suchkapitel kaufmännisch liest, bevor es technisch liest | **`RRF` / `Reciprocal Rank Fusion` bleiben kept-EN** (bereits settled, nicht wieder aufmachen). Für den **Vorgang** ausschreiben: „**die Zusammenführung der beiden Ergebnislisten**"; Verb **zusammenführen**; die beiden Familien: „**die score-basierte** vs. **die rangbasierte Zusammenführung**"; *the fused order* → „**die resultierende Reihenfolge**". ⛔ *die Verschmelzung* (Dudens eigenes Definitionswort für den Fusions-/Kernsinn — importiert den falschen Rahmen), *die Rangfusion* (keine Attestierung). **Was es schließen würde:** ein nativer deutscher Satz mit artikeltragendem oder flektiertem `Fusion`/`fusionieren`, dessen Objekt **zwei Trefferlisten** sind („bei der Fusion der beiden Trefferlisten"); eine deutsche Wiedergabe von RRF als „reziproke Rangfusion" schlösse sie sofort |
| **packing / context packing** | **NEU OPEN 2026-07-28 (Welle 1) — ehrlicher Nullbefund, kein Achselzucken:** `Context Packing`, `Kontext-Packing`, `die Kontextpackung` und „gepackte Chunks" ergaben **null** T1–T5-Treffer. ⛔ *die Packung* ist Duden-fest auf Verpackung und den medizinischen Wickel — „die Kontextpackung" wäre komisch. **Die Abwesenheit eines deutschen Substantivs IST der Befund** | **kein Substantiv prägen — den Vorgang verbal schreiben**: „…und **übergibt diese als Kontext an das Modell**" (INNOQ), „die ausgewählten Chunks **in den Prompt aufnehmen**", „**das Kontextfenster füllen**", wo das Budget der Punkt ist. Als **Überschrift** nach §6.2 Rahmen C umbauen: „**Einen langen Kontext zusammenstellen**", nicht „Long-Context-Packing". *the packed chunks* → „die **aufgenommenen** / **übergebenen** Chunks". **Was es schließen würde:** ein T1–T5-Satz mit artikeltragendem „das Context Packing" / „das Kontext-Packing" oder ein etabliertes deutsches Substantiv. Bis dahin ist die Verbalkonstruktion **kein Notbehelf, sondern das Ruling** (Präzedenz: `Gate`, `Load Shedding`) |
| **parametric knowledge / parametric memory** | **NEU OPEN 2026-07-28 (Welle 1) — das Adjektiv ist einwandfreies Deutsch, der TERMINUS ist unattestiert.** de.wikipedia `insource:"parametrisches Wissen"` → **0 Treffer**; `insource:"parametrische" insource:"Sprachmodell"` → **0**. ⚠ Und `parametrisch` ist nicht *falsch*, sondern **besetzt**: die dominante deutsche Kollokation ist **parametrische vs. nichtparametrische Statistik** — und die liegt in unserer Nachbarschaft, sodass ein Evaluationskapitel mit „parametrisch" den Leser zu **verteilungsfreien Tests** einlädt; dazu parametrisches CAD und der parametrische Equalizer. „Parametrisches Wissen" liest sich als *Wissen parametrischer Art* | **umschreiben**: „**das im Modell gespeicherte Wissen**", „**das Wissen in den Gewichten des Modells**" (Fraunhofer IESE: „den Ursprung der Halluzinationen **in den Gewichten des Modells** zu verstehen"); als Kurzanapher „**das Modellwissen**"; der Kontrast der Welle → „**Wissen aus dem Kontext gegen Wissen aus den Gewichten**". Muss der englische Terminus erscheinen, **einmal in Klammern als Englisch**: „das im Modell gespeicherte Wissen (*parametric knowledge*)". ⛔ *das parametrische Gedächtnis* — Kalk **und** eine Prägung **auf einer offenen Zeile** (§4, `Speicher`: *Gedächtnis* ist dort OPEN); genau der SK-„súbeh"-Fehler. ⚠ **`die Wissensbasis` hier NICHT wiederverwenden** — sie bezeichnet in diesem Korpus die **abgerufene** Seite, und die Gleichsetzung zerstört exakt den Gegensatz, auf dem die Lektion steht. **Was es schließen würde:** ein heise-/iX-/Fraunhofer-/INNOQ-/BSI-Satz mit flektiertem „parametrisches Wissen" / „des parametrischen Wissens" im LLM-Sinn |
| **Late Chunking (Attestierung)** | **NEU OPEN 2026-07-28 (Welle 1) — die SCHREIBUNG ist entschieden, die ATTESTIERUNG fehlt, und die Zeile steht hier, damit niemand das eine für das andere hält.** de.wikipedia `insource:"Late Chunking"` → **0 Treffer**. Die einzige deutschsprachige Quelle (`jina.ai/de`) **disqualifiziert sich auf der eigenen Seite**: Überschrift „**Spätes Chunking** in Embedding-Modellen mit langem Kontext", Fließtext durchgehend „**Late Chunking**" — eine Seite, zwei Wiedergaben desselben Terminus; dazu „die **Late Chunking**-Strategie" (undurchgekoppelt, §1.3.3-widrig) und „**Cosinus**-Ähnlichkeit" gegen die 8 : 0-Zählung | **das Late Chunking, des Late Chunkings** — getrennt und großgeschrieben (Adj+Subst), Genus **geerbt von `das Chunking`**; im Kompositum durchgekoppelt: **das Late-Chunking-Verfahren**. ⚠ **Es erbt von `Late Interaction` die FORM, nicht den STATUS.** ⛔ *spätes Chunking* — behauptet Verspätung **in der Zeit** statt Nachordnung **in der Pipeline**, und ist nur von der disqualifizierten Quelle lizenziert. Erstnennung mit Glosse: „(das Dokument zuerst vollständig einbetten und die Chunks erst danach aus den Token-Embeddings herausschneiden)". **Was es schließen würde:** ein artikeltragender deutscher Satz bei heise/iX/INNOQ/Fraunhofer/dpunkt („beim **Late Chunking** …", „**des Late Chunkings**") oder ein de.wikipedia-Lemma |
| **knowledge conflict / context–memory conflict** | **NEU OPEN 2026-07-28 (Welle 1).** Kein deutscher RAG-/LLM-Fachtext **benennt** das Phänomen; *Wissenskonflikt* und *Kontext-Gedächtnis-Konflikt* sind unbelegt. ⚠ Zusätzlich sperrt das Deutsche selbst: **alle drei Duden-Bedeutungen von `Konflikt` haben PARTEIEN** (streitende Auffassungen mit Zerwürfnis, bewaffnete Auseinandersetzung, innerer Zwiespalt) — **zwei Quellen streiten nicht, sie stimmen nicht überein** | **umschreiben, nicht prägen**: „**der Widerspruch zwischen abgerufenem Kontext und Modellwissen**". Für den allgemeinen Fall gilt die settled Zeile: Verb **widersprechen + DATIV** („Das widerspricht **dem** höherrangigen Ziel."), reziprok „die Quellen widersprechen **einander**"; Adjektiv **widersprüchlich** / attributiv **sich widersprechend**; Substantiv **der Widerspruch**. ⚠ **„mit etwas in Konflikt geraten" ist im Duden als „gegen etwas verstoßen" glossiert** — wer „das Ergebnis gerät mit dem Kontext in Konflikt" schreibt, sagt auf Deutsch *es verstößt gegen den Kontext*. Das ist eine andere Aussage. ⛔ *konfligieren* (bildungssprachlich), *kollidieren* (kollokiert mit Regeln, Terminen, Fahrzeugen). **Was es schließen würde:** ein deutscher RAG-/LLM-Fachtext, der das Phänomen mit einem **flektierten** Substantiv benennt |
| **der Metadatenfilter (Kompositum)** | **NEU OPEN 2026-07-28 (Welle 1) — und der Nullbefund ist aussagekräftig, kein Fehlen:** **jede** geprüfte deutsche Quelle greift für diesen Referenten zur **Verbalphrase**, nicht zum Kompositum | **verbal**: „**nach Metadaten filtern**", „**die Metadaten zum Filtern verwenden**" (heise); als Ding: „**Filterkriterien für die Metadaten**" (heise). Falls unvermeidbar **der Metadatenfilter** (Genus vom Kopfnomen *der Filter*) — **HOUSE, nicht belegt**. **Was es schließen würde:** ein nativer deutscher Satz bei heise/iX/INNOQ/Fraunhofer mit **flektiertem** *Metadatenfilter* („**der** Metadatenfilter", „**des** Metadatenfilters") |
| **size ↔ length (terminologische Trennung)** | **NEU OPEN 2026-07-28 (Welle 1).** **Keine** geprüfte deutsche Quelle unterscheidet die beiden terminologisch; die einzige, die die Größe überhaupt benennt, verwendet *Länge* **anaphorisch für dieselbe Größe** | **die Trennung nicht nachbauen**: eine Benennung — **die Chunk-Größe** —, auch wo das Englische *length* schreibt. *answer length* → **die Länge der Antwort**; *maximum input length* → **eine Obergrenze für die Eingabelänge**. **Was es schließen würde:** ein deutscher Fachtext, der *size* und *length* für dieselbe Domäne **terminologisch unterscheidet** |
| **parametric override** | **NEU OPEN 2026-07-28 (Welle 1).** Kein deutscher Satz aus heise/iX/Fraunhofer/BSI benennt mit einem **Substantiv**, dass ein Modell sein parametrisches Wissen dem gelieferten Kontext vorzieht | **den Nebensatz schreiben**: „**wie oft sich das Modell über den gelieferten Kontext hinwegsetzt**" (*sich hinwegsetzen* **über + Akk.**) oder „wie oft das im Modell gespeicherte Wissen den Kontext **verdrängt**". ⛔ *der Override* als Loan (kein Genus auf irgendeiner Stufe). **Was es schließen würde:** ein deutscher Fachsatz, der das Phänomen mit einem Substantiv benennt |
| **refusal rate** | **NEU OPEN 2026-07-28 (Welle 1).** *die Verweigerungsrate* und *die Ablehnungsrate* sind morphologisch einwandfrei und **beide unbelegt** | **Korpusform: „der Anteil verweigerter Antworten"** in der Dashboard-Aufzählung. ⚠ Hinweis für die Suche: die BSI zeigt das produktive Muster („**die Erfolgsrate** komplexer Angriffe") — falls je ein Beleg auftaucht, wird er vermutlich „**die Rate verweigerter Antworten**" lauten, nicht das Kompositum. **Was es schließen würde:** ein deutscher Satz aus heise/iX/BSI/Fraunhofer, der eine **gemessene Rate von Modellverweigerungen** mit einem Substantiv benennt |
| **denylist / blocklist** | **NEU OPEN 2026-07-28 (Welle 1) — bewusst NICHT vorentschieden:** beide kommen in dieser Welle **nicht vor**, und ein Zusammenführungsdurchgang entscheidet nichts, was er nicht gelesen hat. ⛔ *die Sperrliste* ist zudem besetzt (deutsches Standardwort für die **Certificate Revocation List**), *die Negativliste* stammt aus einem **BSI-Dokument von 2009** mit Vor-Umbenennungs-Vokabular | für `allowlist` gilt die WEAK-Zeile in `_language.md` §1.1.f (Plural und Komposita ja, artikeltragender Singular nein). Für die beiden anderen: **erst zählen, dann entscheiden** |
| **Golden Signals** | **NEU markiert 2026-07-28 (Welle 1): der Incumbent bleibt, aber als HOUSE, nicht als belegt.** Auf **keiner** Quellenstufe wurde eine deutsche Attestierung gefunden — weder für den Loan noch für eine deutsche Form. Die Zeile stand in §2, als wäre sie belegt | **kept-EN, im Plural und mit deutschem Artikel: „die Golden Signals"**, einmal glossiert („Latenz, Traffic, Fehler, Sättigung"). ⛔ **„die goldenen Signale"** — das übersetzt einen Eigennamen. **Was es schließen würde:** ein deutscher Satz bei heise/iX/INNOQ/dpunkt mit `Golden Signals` **oder** einer deutschen Vollform |
| **Scratchpad (als freies deutsches Substantiv)** | **NEU OPEN 2026-07-29 (Welle 2) – und diese Zeile ist eine UMKEHRUNG:** sie stand in §2 als settled kept-EN, **ohne jeden Beleg**. Der Loan **ist** attestiert, aber im **falschen Sinn**: 23 de.wikipedia-Treffer, allesamt **CPU-naher Speicher**, und *Fairchild Channel F* glossiert `scratchpad RAM` ausgerechnet mit **Arbeitsspeicher** – dem Wort, das im selben Absatz für RAM reserviert ist | **das Arbeitsgedächtnis** ist die Korpusform (ein Referent, ein Name); Erstnennung koppelt einmal: „das **Arbeitsgedächtnis** – das Scratchpad aus Teil 1". `Scratchpad` nur als **Rückverweis auf Teil 1** und als **Kompositumsglied**. ⛔ „das Scratchpad" mit deutschem Artikel im Fließtext. **Was es schließen würde:** ein flektierter deutscher Satz bei heise/iX/c't/INNOQ/dpunkt mit artikeltragendem `Scratchpad` **im Agenten-/LLM-Referenten**, nicht im Mikrocontroller |
| **Super-Step (Genus)** | **NEU OPEN 2026-07-29 (Welle 2) – zweite UMKEHRUNG derselben Gestalt**, und der Nullbefund ist von **vier** Durchgängen unabhängig erhoben: de.wikipedia `insource` **0**; *Bulk Synchronous Parallel* und *Pregel (Framework)* haben **kein deutsches Lemma** (beide Abrufe: Seite existiert nicht); Duden `Step` ist „frühere Schreibung für **Stepp**", der Steppschritt, also **kein Rechensinn und keine Genusquelle**; und `Super-Step` ist **kopffinal**, sodass die Kompositumsbildner-Ausnahme (`_language.md` §1.1) nicht greift | **umbauen:** „speichert den Zustand des Graphen **nach jedem Knotenübergang** (im LangGraph-Vokabular: *Super-Step*)" – das Englische **einmal**, kursiv, artikellos, in Klammern. ⛔ „der/das Super-Step". **Was es schließen würde:** ein deutscher Satz mit `der`/`das Super-Step` **im markierten Kasus**, oder ein de.wikipedia-Lemma zu Pregel oder BSP |

> **Nachtrag aus dem Piloten „Tool-Einsatz" (2026-07-28) — warum `Gate` OPEN bleibt, ausführlich.** Die Zeile
> ist nicht aus Trägheit offen; dieser Durchgang hat sie **verschärft** und dabei die Gestalt der Ausnahme
> benannt.
>
> **Neue Evidenz, ehrlich gewogen:** de.wikipedia *Quality Gate* enthält ein echtes bloßes `Gates` —
> „**Interne Gates** überprüfen interne Anforderungen … **Externe Gates** prüfen …" —, aber **im Plural,
> anaphorisch und erst nachdem `Quality Gate` auf derselben Seite eingeführt ist**. Es zeigt kein Genus und
> lizenziert keinen kalt eingeführten Singular. **Der aussagekräftige Nullbefund:** der heise-Artikel
> *Test-Governance die funktioniert* behandelt genau diesen Begriff und enthält **null** Treffer für
> *Kontrollpunkt*, *Prüfpunkt*, *Prüfschritt*, *Schranke* — er schreibt kept-EN „**Quality Gates**" bzw.
> schlicht „**statische Prüfungen**". **Deutsch hat für diesen Sinn kein bloßes Substantiv.**
>
> **Verworfene Kandidaten, jeder mit Grund:** *Kontrollinstanz* (DWDS-Kollokationen durchweg
> institutionell-politisch: „demokratisch, parlamentarisch, staatlich"; zusätzlich kollidiert *Instanz* =
> Objektinstanz), *Prüfinstanz* (dieselbe Kollision), *Prüfstelle* (Duden: eine **Institution**, TÜV-artig),
> *Schranke* (Schlagbaum; zusätzlich *obere/untere Schranke* in der Mathematik), *Prüfschritt* (unbelegt).
>
> **Bestbelegter Herausforderer, trotzdem nicht sauber:** *der Prüfpunkt* (drei unabhängige Quellen,
> zweifach genusmarkiert) — **ist aber Microsofts deutsches Wort für den Hyper-V-Snapshot**. Der Incumbent
> **der Kontrollpunkt** wird gehalten; der ausgelieferte String „Gestaffelte Kontrollpunkte" wird **nicht**
> für einen Seitwärtszug angefasst.
>
> **Korpusform:** „eine **Prüfung vorschalten**" (DWDS *vorschalten* Sinn 2: „vorab, vor etwas anderem
> stattfinden lassen") für den eingefügten Check; „**nur nach Freigabe zulassen**" für das Verb *to gate*.
> ⛔ *absichern* (Duden: gegen Unfälle sichern — **kein** Freigabesinn), ⛔ *unter Genehmigungsvorbehalt
> stellen* (Baurecht-Register).
>
> ***Was die Zeile schließen würde:*** ein nativer deutscher Satz (heise/iX/INNOQ/dpunkt/BSI) mit einem
> bloßen, kasusmarkierten Singular-`Gate` für einen Kontrollpunkt **ohne** *Quality*/*Stage*/*Release*
> davor.
>
> **Unberührt geblieben sind `Load Shedding`, `Backpressure`, `Ground Truth`, `Grader`, `Serving`,
> `Release Gate` und `Guardrail` (Singular) — ⚠ und das ist selbst ein Befund.** Von den fünf Zeilen, die der
> Auftrag zum Piloten als „landen zuerst auf dir" benannt hatte (`Guardrail`-Singular, bloßes `Gate`, `Log`,
> `Queue`, die Partizipien), kam **genau eine** (`Gate`) im Text tatsächlich vor. Siehe §8, Phase 3.

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
  **Vierter Zweig, ergänzt Welle 1 (2026-07-28):** *eine durch eine ÄNDERUNG verursachte Verschlechterung*
  → **die Regression** — mit **Pflichtglosse** beim ersten Vorkommen einer Seite, weil der deutsche Leser
  sonst die Statistik mitliest (`_language.md` §1.1.b). Die Zusatzfrage lautet damit: *Ist es überhaupt
  ein Fehler — oder ist es messbar schlechter geworden, ohne dass etwas kaputt ist?* Der Korpus nennt
  ausdrücklich Modellwechsel, Korpus-Reingest und Eingabedrift als Ursachen; **nicht jede Regression ist
  ein Defekt im Code**, deshalb ⛔ *der Regressionsfehler* als Oberbegriff.
  **Fünfter Zweig, und der teuerste — Welle-1-Konsistenzdurchgang (2026-07-29): `retrieval failure` /
  `generation failure`, das diagnostische Rückgrat von Teil I.**
  **Korpusform: „das Fehlerbild des Retrievals" und „das Fehlerbild der Generation".**
  Diese Karte hatte die Entscheidung bereits getroffen; niemand hatte sie angewandt. **Das Paar ist eine
  KATEGORIE, kein Vorfall** — der Überblick führt es als die *zwei* Ursachen ein, in die jede schlechte
  Antwort zerfällt —, und der Zweig *Kategorie → das Fehlerbild / die Fehlerklasse* steht seit dem Bootstrap
  oben in dieser Karte.
  ⚠ **Gezählt, nicht geschätzt: die dreizehn Seiten trugen SIEBEN Namen für dieses eine Paar** —
  *Fehler des Retrievals* (ausgerechnet auf der Seite, die es **definiert**), *Versagen des Retrievals* (4×),
  *Fehler im Retrieval* (3×), *Fehlerquote des Retrievals*, *die Quote*, *Fehler der Generation* (3×),
  *Fehler in der Generation* (3×). **Und daneben stand auf zwei Seiten, unabhängig voneinander, bereits
  `Fehlerbild` als Anapher für genau dieses Paar** („die Aufschlüsselung der **Fehlerbilder** aus dem
  Überblick", „das direkteste Maß für das **Fehlerbild**, das Teil 1 benannt hat"). **Der Korpus hatte die
  Antwort also selbst gefunden, zweimal, ohne dass eine Zeile sie festhielt.**
  - **`versagen` bleibt — als VERB, und das ist keine Konzession.** „dass das Retrieval seltener
    **versagt**", „Mit jeder Stufe **versagt** das Retrieval seltener" sind attestiert (`_language.md` §9.2,
    heise) und bleiben unangetastet. Gestrichen ist allein die **Nominalisierung als Klassenname**: *das
    Versagen des Retrievals* benennt ein **Ereignis des Zusammenbrechens** (Organversagen, menschliches
    Versagen), nicht eine Diagnosekategorie — dasselbe Wort, andere Wortart, anderer Referent.
  - **Die RATE heißt nicht *die Fehlerquote des Retrievals*, sondern wird verbal gebaut:** „**wie oft das
    Retrieval versagt**", „um wie viel **seltener das Retrieval damit versagt**". Danach darf „die Quote" als
    Anapher stehen — aber erst danach.
  - **`die Fehlerklasse` wird NICHT mitgestrichen und ist keine Dublette.** Sie benennt eine Klasse **in einer
    Taxonomie**, eine Ebene unter dem Paar: die vier Reparaturfälle in `generation/index.md`, „die schlechteste
    Fehlerklasse, die sich ausliefern lässt". **Frage vor dem Schreiben:** *Meine ich eine der ZWEI
    Diagnosekategorien dieses Teils — oder irgendeine Fehlerkategorie?*
  - ⛔ *der Retrieval-Fehler* · ⛔ *der Generierungsfehler* — sie lesen sich als **ein einzelner Vorfall** und
    fallen damit auf den ersten Zweig dieser Karte zurück.
  - ⚠ **Warum `Fehlerbild` und nicht `Fehlerklasse` für das Paar:** der Überblick rahmt den ganzen Teil
    **diagnostisch** („Bestimmen Sie die Ursache, bevor Sie den Fehler beheben"), und ein *Fehlerbild* ist
    genau das, was man diagnostiziert. Die beiden Seiten, die von sich aus so schrieben, taten es in derselben
    Rahmung — **Usus und Sense-Card zeigen hier in dieselbe Richtung, und das ist der Grund, warum die Zeile
    nicht DISPUTED ist.**
  - ⚠ **Bindet Teil II und Teil III.** Das Paar ist das diagnostische Rückgrat des ganzen Kurses, nicht nur
    von Teil I; jede spätere Welle, die es erwähnt, schreibt **dieselben zwei Zeichenketten**.
- **`Suche` / `Retrieval` / `Recherche`** — *retrieval* (die Schicht/der Terminus) vs. *search* (die
  Handlung) vs. *search over a tree* (der algorithmische Durchlauf). Vorschlag: Terminus → **Retrieval**;
  Handlung → **suchen / die Suche**; Baum-/Graphdurchlauf → **die Suche im Suchraum / das Durchsuchen**.
  **Auf Probe.**
- **`Bewertung`** — *evaluation* (die Disziplin) vs. *score* (die Zahl) vs. *rating*. Vorschlag: Disziplin →
  **die Evaluation**; Zahl → **der Score**; „Bewertung" nicht für die Zahl. **Auf Probe.**
  **Erweitert Welle 1 (2026-07-28) — und die Erweiterung ist zugleich die ANTWORT auf eine Prüffrage an
  Gate 6.5: hat die `Bewertungs-`Familie inzwischen zwei Wörter für einen Referenten?** Sie hat es
  **nicht**. ~~Sechs Referenten, sechs Namen~~ **acht Referenten, acht Namen** *(Welle 2, 2026-07-29)*,
  keine Überschneidung:
  - die **Disziplin** → **die Evaluierung / die Evaluation** (`_language.md` §1.1.e)
  - die **Zahl** → **der Score** — ⛔ nie „die Bewertung" für die Zahl
  - das **Kriterienwerk**, gegen das bewertet wird → **das Bewertungsraster** *(rubric, neu)*
  - die **bewertende Instanz** → **der Bewerter / das Bewertungsmodell / die Bewertungsinstanz** *(grader)*
  - der **Spruch** des Judges über eine Antwort → **das Urteil** *(verdict, neu)* — „zu demselben Urteil
    kommen"
  - die **zusammengezogene Empfehlung** am Absatzende → **das Fazit** *(verdict im zweiten Korpussinn, neu)*
  - die **Tätigkeit** des Bewertens → **die Bewertung** *(grading, neu Welle 2)* – „die **Bewertung jedes
    Hops**", „**pro Hop bewerten**". ⚠ Das ⛔ dieser Karte gilt **nur für die Zahl**: *die Bewertung* darf
    nicht der Name des **Scores** sein, wohl aber der Name der **Handlung**. Beide Sätze zusammen sind die
    Karte, nicht nur der zweite.
  - die **Heuristik, die Knoten eines Suchbaums bewertet** (ToT/LATS, *state evaluator*) → **die
    Bewertungsfunktion** *(neu Welle 2)* – de.wikipedia *Minimax-Algorithmus*, exakt unser Referent.
    ⛔ **der Evaluator** (kein Duden-, kein DWDS-Lemma; im Deutschen die **Person** der Programmevaluation)
    – er wäre der **vierte** Name für eine bewertende Komponente neben *Judge*, *Bewerter* und *Kritiker*.
    §1.1.g führt die Zeile.
  
  ⚠ **Wie die beiden Zeilen hierhergekommen sind, und es ist die Lehre der Welle in Kleinform: zwei Batches
  haben unabhängig „den siebten Referenten" gemeldet.** Jeder war für sich richtig, beide zusammen waren
  falsch – dieselbe arithmetische Kollision, die Welle 1 in §1.1.g getroffen hat, eine Etage tiefer.
  **Die Zahl in einer Sense-Card („sechs Referenten, sechs Namen") IST eine Zählung**, auch wenn sie nicht
  wie eine aussieht; die Batches hatten ausdrücklich darauf verzichtet, Tabellenzahlen fortzuschreiben –
  und es ist trotzdem passiert, an der Stelle, die niemand für eine Zählung hielt.
  
  **Frage vor dem Schreiben:** *Meine ich das Fach, die Zahl, das Regelwerk, wer bewertet, den Spruch über
  eine Antwort oder die Schlussfolgerung des Abschnitts?* ⚠ Das Bewertungsraster ist das **Kriterienwerk**,
  nicht die Zahl — die alte Kartenregel wird davon **nicht** verletzt.
- **`Schicht`** — *layer* (Pipelinestufe des Buches) vs. *layer* (Verteidigungsschicht). Vorschlag: bei
  Verwechslungsgefahr nie nackt — **die Pipelinestufe** vs. **die Verteidigungsschicht**. **Auf Probe.**
- **`Speicher`** — *memory* (Agentengedächtnis) vs. *storage* (Ablage) vs. *cache*. Vorschlag: Gedächtnis →
  **das Gedächtnis / die Memory** (OPEN), Ablage → **der Speicher**, Zwischenspeicher → **der Cache**.
  **OPEN — nicht entschieden.**
  ⚠ **Welle 1:** *parametric memory* darf diese offene Zeile **nicht stillschweigend schließen** — die
  Wiedergabe ist „das im Modell gespeicherte Wissen" (§3), **nicht** „das parametrische Gedächtnis".

**Neu in Welle 1 (2026-07-28) — sechs Karten, jede aus einer Kollision, die ein einzelner Belegdurchgang
nicht sehen konnte:**

- **`Chunk` / `Passage` / `Textabschnitt`** — **der englische Quelltext verwendet *chunk* und *passage*
  nahezu austauschbar; das Deutsche erzwingt die Unterscheidung**, und wer sie einebnet, verliert die
  Pipeline-Logik der Lektion.
  **Frage vor dem Schreiben:** *Rede ich über das, was die Ingestion ERZEUGT — oder über das, was der
  Retriever/Reranker BEWERTET?*
  - das Artefakt der Ingestion (Segmentierung, Overlap, Größe) → **der Chunk**, *des Chunks*, *die Chunks*
  - die Texteinheit, die abgerufen und bewertet wird → **die Passage**, *der Passage*, *die Passagen*;
    **die Textpassage**, wo `Passage` sonst ortshaft läse (Ladenpassage)
  - dort, wo die **Segmentgrenze** selbst der Punkt ist → **der Textabschnitt**
  - ⚠ **Genuswechsel im Kompositum, den ein späterer Durchgang sonst „korrigiert":** *der* Chunk, aber
    **die** Chunk-Größe (das Kopfnomen trägt das Genus).
  - ⛔ *der Absatz* — behauptet eine typografische Grenze, die der Chunker nicht respektieren muss.
  - Die Codepräfixe `query:` / `passage:` sind **Klasse 1**: nie übersetzen, nie flektieren.

- **`Aussage` / `Behauptung` / `Zeugenaussage`** — für *claim* (25 Vorkommen), und die Zweiteilung ist
  **belegt, nicht erfunden** (de.wikipedia *Faktencheck* prüft „**die Aussage**" und reserviert
  „**Behauptungen**" für die ungeprüfte Meldung).
  **Frage vor dem Schreiben:** *Behaupte ich schon etwas über den Wahrheitswert?*
  - nein, neutrale Einheit → **die Einzelaussage / die atomare Aussage / die Aussagen der Antwort** —
    **nie das nackte „die Aussage"** neben *Quelle* und *prüfen*, sonst liest der Gerichtssinn mit
  - ja, ausdrücklich unbelegt („an unsupported claim", „the model asserts") → **die Behauptung**
  - ⛔ **die Zeugenaussage** — und der Grund ist nicht Geschmack: `Behauptung` **trägt das Urteil im Wort**
    (DWDS „aber **unbewiesene** Meinungsäußerung"), sodass *supported claims / total claims* als
    „gestützte unbewiesene Meinungsäußerungen" gelesen würde — ein Widerspruch in sich.
  - ⛔ „durch die Quelle **gedeckt**" → „**durch die Quelle belegt**" / „**stützt sich auf** die Quelle".

- **`Sampling`** — drei Sinne, ein Wort, **und der Beleg gehört nur einem davon**.
  **Frage vor dem Schreiben:** *Meine ich das Aufzeichnen einer Teilmenge, die MCP-Fähigkeit oder die
  Tokenauswahl?*
  - **statistisch / Traces** (der einzige Sinn, für den der Kanon eine deutsche Attestierung besitzt) →
    **das Sampling**, *des Samplings*; **die Stichprobe** ist das **Ergebnis** (die behaltene Teilmenge),
    nicht das Verfahren. In einer Lektion, die MCP oder Decoding berührt, **nie nackt**, sondern als
    durchgekoppeltes Kompositum: **das Trace-Sampling**, **das Head-based Sampling**, **das Tail-based
    Sampling**; koordiniert nach §6.5 „**Head- und Tail-Sampling**".
  - **MCP-Fähigkeit** → **Klasse 1**, Eigenname, unübersetzt und unflektiert (§1).
  - **Tokenauswahl beim Decoding** → §3, Zeile `Sampler`: **die Stufe benennen, nicht personifizieren**;
    Verb **auswählen**; das Substantiv möglichst als Kompositum (*Top-K-Sampling*), nie nackt.
  - ⚠ **Für Teil I ist das Vorsorge:** alle 27 Vorkommen dieser Welle sind der statistische Sinn.

- **`Feedback` / `Rückmeldung`** — **eine Richtungskarte, kein Bedeutungsproblem**, und das macht sie
  gefährlicher: *Rückmeldung* ist keine falsche Übersetzung (der Duden glossiert *Feedback* selbst so),
  **aber in nativer deutscher IT-Prosa zeigt der Pfeil in die andere Richtung**.
  **Frage vor dem Schreiben:** *Wer schickt an wen?*
  - Nutzer → System → **das Feedback / das Nutzerfeedback**
  - System → Nutzer → **die Rückmeldung**
  - Beleg, der beides in **einem** Satz verteilt: „Geben die Nutzenden **Feedback** …, bekommen sie eine
    visuelle **Rückmeldung** über die Aktivierung." (informatik-aktuell)
  - ⚠ In einem Observability-Kapitel, dessen ganzer Punkt die **Herkunft eines Signals** ist, ist die
    Verwechslung ein **Sachfehler**. ⛔ *das Feedbacksignal* → „ein Signal aus dem Nutzerfeedback".
  - ⚠ Offen und **bewusst nicht hier entschieden:** ob der Korpus *Nutzerfeedback* oder
    *Nutzenden-Feedback* schreibt, entscheidet `_language.md` § Gendern, nicht diese Karte. Incumbent:
    **das Nutzerfeedback**.

- **`Alerting` / `Benachrichtigung`** — **zwei Stufen einer Kette, nicht zwei Wörter für eine Sache**;
  heise trennt sie in einem Satzpaar.
  **Frage vor dem Schreiben:** *Rede ich über die REGEL, die auslöst — oder über die ZUSTELLUNG danach?*
  - Regel + Auslösung → **das Alerting** („Für Alerting legen Administratoren fest, in welchen Fällen ein
    Alarm ausgelöst wird"); **die Alarmierung** nur als **Glosse** beim ersten Vorkommen, nie als Laufterm
    (sonst liest sich der Absatz wie ein Leitstellenprotokoll)
  - Zustellung an die Zuständigen → **die Benachrichtigung / benachrichtigen** („Das Benachrichtigen der
    zuständigen Personen übernehmen häufig externe Tools")
  - das einzelne Ereignis → **der Alert** (§1.1.a) bzw. **der Alarm**, der **ausgelöst** wird
  - ⚠ Wer *alerting* mit *Benachrichtigung* wiedergibt, verliert **genau die Unterscheidung, die die
    Lektion trägt**.

- **`Grounding` / `Groundedness` / `Faithfulness`** — die Karte, die verhindert, dass ein späterer
  Durchgang die beiden Glossen für Dubletten hält (Batch A hat die Frage an Gate 6.5 eskaliert; §2 trägt
  die Entscheidung, hier steht die Abgrenzung).
  **Frage vor dem Schreiben:** *Rede ich über den VORGANG oder über die gemessene EIGENSCHAFT?*
  - der Vorgang, die Antwort an den Kontext zu binden → **Grounding**, Glosse „(Rückbindung der Antwort an
    den Kontext)"
  - die gemessene Eigenschaft und ihre Metrik → **Faithfulness / Groundedness**, Glosse
    „(Quellentreue …)" — *Groundedness* **nur als Kompositumsglied** (*die Groundedness-Metrik*), weil
    das nackte Lehnwort **kein attestiertes Genus** hat
  - ⚠ **Quellentreue ist nicht Faktentreue:** der Korpus sagt ausdrücklich, eine Antwort könne
    **quellentreu und trotzdem falsch** sein. ⛔ *die Faktentreue* misst Wahrheit, nicht Stützung.
  - ⛔ *die Rückbindung* als **Metrikname** — sie ist und bleibt die Glosse für *Grounding*.

**Neu in Welle 2 (2026-07-29) – eine Karte, und sie entscheidet nichts Neues: sie AKTIVIERT eine Bedingung,
die der Kanon seit Welle 1 mit sich führt:**

- **`Protokoll`** – *communication protocol* gegen *audit trail*, zwei Referenten, die in Teil II auf
  derselben Seite stehen.
  **Frage vor dem Schreiben:** *Rede ich über eine Vereinbarung zwischen zwei Seiten – oder über eine
  Aufzeichnung?*
  - die Vereinbarung → **das Protokoll**, *die Protokolle*, *des Protokolls*. **Auf Protokoll- und
    Agentenseiten (Teil II) heißt `das Protokoll` ausschließlich das Kommunikationsprotokoll**, gemessen
    47 : 0 für den Netzsinn in dieser Materie.
  - die Aufzeichnung → dort **die Protokollierung** bzw. **das Log** (`_language.md` §1.1.e).
  - ⚠ **Außerhalb dieses Kontexts bleibt die §2-Zeile („die Protokollierung / das Protokoll" für *audit
    trail*) unverändert gültig** – vor allem in `ai-sdlc.md`. **Die Zeile wird nicht gestrichen, sie wird
    durch diese Karte geschützt:** sie trug die Bedingung „nur ohne Verwechslungsgefahr mit dem
    Netzwerkprotokoll" von Anfang an, und Teil II ist der Ort, an dem die Bedingung **feuert**.
  - ⛔ die Genitivfügung „**das Protokoll der Sitzung**" – Duden-Bedeutung 1 von `Protokoll` ist die
    **Sitzungsniederschrift**, und *Sitzung* ist in Teil II unser eigenes Wort für *session*. Beide Wörter
    sind unsere; die Fügung gehört jemand anderem.
  - ⛔ *das Prüfprotokoll*, ⛔ *der Prüfpfad* (§1.1.f, umsatzsteuerrechtlich besetzt).

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
| `**[New terms](../../glossary.md#…)**` | 61 (beide Kurse), davon 35 mit `../../` | **`**[Neue Begriffe](../../glossary.md#tools)**`** — Label deutsch, **Termliste vorerst englisch** | **HOUSE, DE-Pilot 2026-07-28.** Die Liste spiegelt die **Glossar-Lemmata**, und das deutsche Glossar ist noch nicht geschrieben. Ein Flip hier allein würde Fußzeile und Glossar auseinanderlaufen lassen — genau der Defekt, den das slowakische Korpus in Fáza 25 korpusweit korrigieren musste. **Der Flip gehört in die Glossarwelle, nicht hierher** (§7) |
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
- *soft cap / hard cap* → „**Soft- und Hard-Cap**" ⚠ *(Welle 2, 2026-07-29: die Ergänzungsstrich-Konstruktion bleibt gültig, wo das Paar **als Paar benannt** wird – `Soft Cap / Hard Cap` ist die **Zitierform des Musternamens**. Der Laufterm im Fließtext ist **die weiche / die harte Obergrenze**; ⛔ „das Cap" / „der Cap", kein attestiertes Genus in diesem Sinn. Siehe die Anmerkung in §2.)*
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

### 6.7 Vier Konstruktionen aus Welle 1, die jede Seite von Teil I trifft

*Neu 2026-07-28. Jede stammt aus einem Belegdurchgang, und drei davon sind Fehler, die eine Seite
**fließend** begehen kann — deshalb stehen sie hier und nicht nur in einer Termzeile.*

**(a) `three costs` — das Pluraletantum blockiert den ZÄHLER, nicht das Verb.**
`Kosten` hat keinen Singular, auf den ein Kardinale referieren könnte. „Es fallen Kosten an" ✅ —
„**Drei Kosten** fallen an" ⛔. **Die Reparatur ist ein Zählwort oder ein Satzumbau, nicht ein anderes
Verb:** „**drei Kostenblöcke**" (belegt) · „drei Kostenarten" · „drei Posten" · „**An drei Stellen
entstehen Kosten.**" · „**Die Kosten haben drei Quellen.**"
**Test:** *Steht eine Zahl unmittelbar vor `Kosten`?* Dann umbauen. — ⚠ Wer aus diesem Befund
„*anfallen* ist verboten" macht, repariert das falsche Wort.

**(b) `X attacks that problem` — das ist NICHT `angreifen`.**
Die Welle enthält 54 Sicherheitsangriffe **und drei Stellen, an denen `attack` „ein Problem angehen"
heißt** („Two techniques from 2024 **attack** that loss", „Late chunking **attacks** it by inverting the
order of operations", „Contextual retrieval **attacks** the same disease at index time").
→ „**gehen dagegen an**", „**setzen dort an**", „**greifen das Problem auf**".
**Test:** *Ist das Subjekt ein Angreifer — oder ein Verfahren?* Verfahren → nie `angreifen`. In einem Buch,
dessen übrige Vorkommen Sicherheitsangriffe sind, wäre das ein **Lesefehler**, kein Stilfehler.

**(c) Das englische Verb, für das es kein deutsches gibt — umbauen, nicht entlehnen.**
Diese Welle liefert das Muster dreimal: `to threshold`, `to redact` (im schmalen Listensinn), `to cap`.
Deutsch bildet an dieser Stelle **eine Relativkonstruktion oder ein Funktionsverbgefüge**:
- *a score you can threshold* → „ein Score, **auf den sich ein Schwellenwert anwenden lässt**"
- *a number you threshold on* → „ein Konfidenzwert, **über den ein Schwellenwert entscheidet**"
- *X overrides Y* → „X **setzt** Y **außer Kraft**" (Satzklammer!)
- *cap it with `max_tokens`* → „**Begrenzen Sie die Ausgabe mit `max_tokens`.**"
⛔ *thresholden*, *alerten*, *trunkieren* (letzteres **nicht** mangels Beleg, sondern **wegen** eines
Belegs im falschen Sinn — `_language.md` §1.3.2).
**Test:** *Habe ich gerade ein englisches Verb mit deutscher Endung gebildet?* Dann steht die Antwort in
§1.3.2, und sie lautet fast immer: den Satz umbauen.

**(d) Ordinalzahl + Bezugswort — `das 95. Perzentil`.**
Ziffer, **Punkt**, Leerzeichen, Bezugswort (Duden: „In Ziffern geschriebene Ordnungszahlen erhalten einen
Punkt"). ⛔ „das 95te Perzentil", „das 95-te Perzentil". `p95` / `p99` bleiben **Klasse 1**, klein und
englisch; mit Artikel durchgekoppelt: **der p95-Wert**. Prozentangaben folgen der Typografiezeile:
`5 %`, nicht `5%`. ⚠ **Umbruchschutz (U+00A0) zwischen „95." und „Perzentil" ist HOUSE** — eine Regel
dafür wurde ausdrücklich gesucht und **nicht gefunden**.

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

### Phase 3 (2026-07-28) — Pilot „Tool-Einsatz"

*Beide Seiten der Lektion, durch den vollen Gate-Stack. Protokolliert in der Form des slowakischen
Fáza-2b/3/4-Eintrags, weil dieser Eintrag die einzige ehrliche Vergleichsbasis dafür ist, was ein Pilot
kostet.*

**Das Playbook hatte drei Zusatzrunden nach dem Piloten eingeplant — 2b Re-Edit, 2c Methodenwechsel auf
Rekonstruktion aus der Proposition, 2d Politur —, weil das Slowakische genau die gebraucht hat. Eingetreten
ist das so nicht, aber auch nicht andersherum, und die Unterscheidung ist der eigentliche Befund:**

- **2b ist eingetreten und war substanziell.** Drei Kaltlesungen plus ein Cross-Model-Registerrichter
  haben eine echte Reparaturrunde erzwungen (§I–§K). **Der Pilot ist nicht durchgerutscht.**
- **2c ist NICHT eingetreten.** Der Wechsel der *Methode* — weg vom Wortersatz, hin zum Neubau aus dem Sinn —
  musste nicht erst gelernt werden. `_language.md` §1.4 sagt seit dem Bootstrap: *„Die Reparatur ist nie ein
  Wortersatz, sondern ein Neubau aus dem Sinn."* Das Slowakische hat diesen Satz mit einer verlorenen Runde
  bezahlt; das Deutsche hat ihn geerbt, und die Renderer-Briefe haben ihn **wörtlich** mitgegeben. Die
  2b-Reparatur lief von Anfang an propositionsbasiert.
- **Das ist der Beleg dafür, dass der Port funktioniert — und zugleich die Grenze dessen, was dieser Pilot
  beweisen kann: er zeigt, dass eine BEKANNTE Falle vermeidbar ist, nicht dass es keine unbekannten mehr
  gibt.** §I–§N sind die unbekannten, die er gefunden hat.

**Die Kosten sind trotzdem angefallen, und zum Teil an ganz anderer Stelle.** Statt „drei Runden
Prosareparatur" kostete der Pilot:

1. eine **Terminologierunde vor der Prosa**, die fünfmal so groß ausfiel wie geplant (§A);
2. zwei **Infrastrukturreparaturen**, ohne die der Pilot gar nicht durch die Gates gepasst hätte (§B);
3. eine **Abstimmungsrunde zwischen parallelen Belegdurchgängen**, für die es im Gate-Stack keinen Schritt
   gibt (§D);
4. **eine Prosareparaturrunde (2b)** — genau die eingeplante, in vollem Umfang (§I–§L). *(Ein Größenvergleich
   mit der slowakischen Runde wird hier bewusst NICHT behauptet: dafür fehlt eine gemeinsame Messgröße.)*

---

#### §A Die OPEN-Zeilen, mit denen gerechnet wurde, sind fast alle NICHT aufgetreten

Der Auftrag benannte vorab, was „zuerst auf dem Piloten landet": **`Guardrail` im Singular, bloßes
`Gate`, die IT-Sinne von `Log` und `Queue`, und die Partizipien von `embedden`/`chunken`/`refactoren`/
`stubben`**. Gemessen am tatsächlichen Text beider Seiten:

| vorhergesagte OPEN-Zeile | Vorkommen im Piloten |
|---|---|
| `Guardrail` (Singular) | **0** |
| `Log` (IT-Sinn) | **0** |
| `Queue` (IT-Sinn) | **0** |
| `embedden` / `chunken` / `refactoren` / `stubben` | **0** |
| bloßes `Gate` | **3** ✅ |

**Eine von fünf.** Und die Zeilen, die tatsächlich unvermeidbar waren, standen im Kanon **gar nicht** —
nicht als OPEN, sondern überhaupt nicht:

| Terminus | Vorkommen (beide Seiten) | Zeile im Kanon vorher |
|---|---:|---|
| `retry` / `retries` / `retrying` | **28** | keine |
| `schema` | **37** | *Schema* vorhanden, das Umfeld nicht |
| `validation` / `validate` | **14** | keine |
| `idempotency` / `idempotent` | **12** | nur *Idempotency-Key* als Beispielwort |
| `runtime` | **9** | keine (nur *Laufzeitfehler* als Glossbeispiel) |
| `timeout` | **4** | keine |
| `backoff` | **3** | keine |
| `fan-out` / `fan-in` | **3** | keine |
| `loadout` | **4** | keine |
| `namespacing` | **1** | keine |

**Die Diagnose, und sie gilt für die restlichen 65 Seiten:** das kept-EN-Register wurde aus einem
**Terminusinventar** gesetzt — 123 Lehnwortzeilen, 38 Verbzeilen, 161 Kursbegriffe, aus Glossarlemmata
und Kapitelüberschriften gewonnen. Laufender Text braucht aber nicht die Schlagwörter, sondern das
**Bindegewebe**: *retry, timeout, backoff, side effect, namespace, batch, grammar, overhead, validation*.
Keines davon ist ein Glossarlemma, weil keines ein Lehrbegriff des Kurses ist — und genau deshalb fehlten
sie alle.

> **Regel für die Wellen 4–11: das Register jeder Welle wird aus einer FREQUENZZÄHLUNG über den
> laufenden englischen Text der Welle geseedet, nicht aus dem Glossar.** Ein Kanon mit 161
> Morphologiezeilen hat das häufigste Substantiv seiner ersten Seite nicht gekannt. Das ist kein
> Versäumnis der Bootstrap-Durchgänge, sondern eine Eigenschaft der Quelle, aus der sie geschöpft haben.

#### §B Zwei Gates konnten den Piloten strukturell nicht annehmen

Beide wurden empirisch gefunden — indem die englischen Seiten testweise als `i18n/de/**` abgelegt und die
Gates laufen gelassen wurden, **bevor** eine Zeile Deutsch geschrieben war.

**B1 — `scripts/locale_parity.py`, Dateimengenprüfung.** Sobald `current/` existiert, verglich das Skript
die volle Dateimenge und meldete jede noch nicht übersetzte Seite als Defekt. Für eine *released* Locale
ist das richtig; für eine *unreleased* ist Teilübersetzung der **Normalzustand**. Das Skript kannte diese
Asymmetrie bereits — `missing_translation()` wendet sie auf einen ganz fehlenden Kurs an —, nur nicht eine
Ebene tiefer. **Wirkung ohne Fix: die Locale wäre „alles oder nichts" gewesen**, und der Pilot hätte den
Gate nie grün bekommen. **Fix:** fehlende Seiten sind in einer unreleased Locale informativ, nicht fatal;
die Gegenrichtung (eine Seite ohne englische Quelle) bleibt in **jeder** Locale ein harter Fehler — das ist
die Hälfte, die nicht fail-open gehen darf.

**B2 — `scripts/i18n-link-check.sh`, Toleranzregel.** Der Gate tolerierte einen kaputten Link nur, wenn die
**Quellseite** eine noch nicht übersetzte EN-Fallback-Seite ist. Die erste übersetzte Lektion einer Locale
verlinkt aber zwangsläufig auf noch nicht übersetzte Geschwister und ein noch nicht übersetztes Glossar —
und Docusaurus kann `.md`-Links nicht über die Grenze zwischen Fallback- und Übersetzungsbaum auflösen. Der
Gate versprach im eigenen Kopfkommentar, er „pflege sich selbst, während Locales sich füllen"; **tatsächlich
tat er das nur bei 0 % und bei 100 %.** **Fix:** die Toleranz urteilt jetzt über das **Paar** aus Quelle und
Ziel — toleriert wird, wenn die Quelle in einer unreleased Locale liegt **und das ZIEL dort noch nicht
übersetzt ist**. Sobald das Ziel existiert, muss der Link auflösen; ein falscher Glossar-Anker auf eine
bereits übersetzte Seite fällt weiter durch, also bleibt genau die Klasse scharf, für die der Gate
geschrieben wurde (#307). Der Selbsttest wuchs von 9 auf 19 Fälle, davon 10 neue Paarfälle.

> **Die verallgemeinerbare Lehre:** beide Gates waren gegen den **Endzustand** einer Locale geschrieben und
> gegen den **Anfangszustand** ungetestet — und ein Gate, das den Zielzustand prüft, sieht wie ein
> funktionierender Gate aus, solange niemand den Übergang fährt. Das ist derselbe Fehlertyp wie #307, nur
> eine Ebene höher: **der Pilot ist der erste Moment, in dem die Gates selbst geprüft werden, und er muss
> vor der Prosa gefahren werden, nicht nach ihr.**

#### §C Blindbewertung und Attestierung — die Reihenfolge hat sich zum dritten Mal bezahlt gemacht

Der Kanon führt zwei Fälle, in denen eine ordentlich durchgeführte Blindbewertung flüssiges Deutsch auf
englischem Kollokationsgerüst prämiert hat („aus Grundprinzipien", „die sie ehrlich halten"). **Dieser Pilot
liefert den dritten, und diesmal war es kein Kollokations-, sondern ein Attestierungsfehler.**

Der cross-family-Blindrichter kürte für die Schema-Überschrift **„Constrained Decoding: der Sampler schließt
ungültige Token aus"** und begründete es mit **präziser Agenszuweisung** — ein sauber benannter
sprachlicher Grund, formal ein gültiges Urteil. **`der Sampler` ist im Deutschen für diesen Sinn
nirgends belegt:** Duden und DWDS führen ausschließlich Musiksinne (die Sampler-CD, das
Sampling-Instrument), und in deutscher LLM-Prosa existiert kein einziger flektierter Beleg. Was deutsche
Fachprosa schreibt, ist die kanoneigene Regel: **Substantiv englisch (`das Sampling`), Verb deutsch
(`auswählen`)** — heise: „Greedy Decoding **wählt** das Token mit der höchsten Wahrscheinlichkeit **aus**".

Der Zweitplatzierte („Das Schema wird zur Grammatik", Abstand KNAPP) ist durchgehend belegt und wurde
nachgerückt. **Die Regel „der billigere Gate läuft zuletzt" hat also erneut genau das gefangen, wofür sie
existiert — und der Richter hat den Fehler nicht etwa schlampig gemacht, sondern mit einem korrekten
linguistischen Argument über ein Wort, das es im Deutschen nicht gibt.**

#### §D Der Gate-Stack hat keinen Abstimmungsschritt — und brauchte einen

Die Attestierung lief in **fünf parallelen Batches**. Zwei Ergebnisse widersprachen sich an der Naht, und
**jeder Batch hatte für sich recht**:

1. **`write tools` / `read tools`.** Batch B belegte das deutsche *Gerüst* („rein **lesende** Services",
   „eine **schreibende** Transaktion", „**schreibenden** Zugriff") und schlug „schreibende **Werkzeuge**"
   vor. Batch C maß im selben Zeitraum `Tools` : `Werkzeuge` ≈ **15 : 2–3** in nativer deutscher Agentenprosa
   und bestätigte die Kanonentscheidung, dass `Tool` englisch bleibt. **Auflösung: attestiertes
   Partizipialgerüst behalten, Kopfnomen des Korpus einsetzen → „schreibende Tools" / „lesende Tools".**
2. **`runtime` im Fan-out-Satz.** Batch C schrieb im Musterbeispiel „**Die Laufzeitumgebung** verteilt die
   Aufrufe …". Batch E, das genau diesen Referenten untersuchte, verbietet das: `Laufzeitumgebung` ist die
   JVM/CLR-Klasse Wirtsplattform, `Laufzeit` ist ein **kategorialer** falscher Freund (alle neun
   DWDS-Bedeutungen sind Zeitdauern, auch die Informatik-Bedeutung). **Auflösung: Batch E gewinnt** —
   „**Ihre Anwendung** verteilt die Aufrufe …".

> **Regel: Parallelisierte Belegdurchgänge brauchen einen Abstimmungsschritt, und der gehört in den
> Gate-Stack.** Der Ertrag der Parallelisierung ist real; ihr Preis ist, dass kein Batch die Nachbarn sieht.
> Ohne den Abstimmungsschritt wäre **beides** in die Prosa gegangen — ein Kopfnomen gegen die
> Korpusentscheidung und ein falscher Referent —, und beide hätten jede Flüssigkeitsprüfung überlebt.
> *(Als Gate-Schritt eingetragen im `de-locale-playbook.md` §4, zwischen Gate 6 und Gate 7.)*

#### §E Der Kanon braucht eine Klasse, die er nicht hat

`Retry` und `Backoff` haben **kein attestiertes Genus als freies Substantiv** und treten trotzdem völlig
unauffällig als erstes Kompositumsglied auf: `das Retry-Budget` ✅ / `ein Retry` ⛔; `die Backoff-Strategie`
✅ / `das Backoff` ⛔. Die §1.1-Tabelle kennt nur „englisch geführt" und „deutsch geführt" — dieser dritte
Zustand hat keine Spalte. Der Grund ist grammatisch: **im Kompositum trägt das Kopfnomen das Genus**, das
Lehnwort braucht also keins. Praktische Folge für jeden Nachtrag: **wer kein flexionstragendes Beispiel
findet, trägt nicht „OPEN, Wort meiden" ein, sondern prüft zuerst die Kompositumsverwendung.**
*(Als Kasten in `_language.md` §1.1 aufgenommen; die Nachtrag-Regel in §1.1.g verweist darauf.)*

#### §F Die Fallenliste wächst von neun auf sechzehn — und eine Falle ist von neuer Art

Neu belegt: `Time-out` (Duden: **Sport**, „Auszeit", kein EDV-Sinn), `transient` (DWDS: **Signalphysik**;
das Informatikbeispiel ist das **Java-Schlüsselwort**), `Grundlast` (**Stromnetz**), `Sampler`/`sampeln`
(**Musik**), `wohlgeformt` (Duden: **ästhetisch**, „wohlgeformte Hände"), `Loadout` (**Gaming**), `Fan-out`
(**Digitaltechnik** *Ausgangslastfaktor* **und** **Offsetdruck**) *(Schreibung Welle 2 korrigiert: `out` ist kein
Substantiv, § 45 E1 greift nicht; `_language.md` §1.1, Fallenkasten)*.

**Die neue Art ist `Gate`.** Der Kanon führte es als Flughafen-Falle. Die *lebendige* Kollision ist eine
andere: de.wikipedias LSTM-Artikel flektiert **das Input Gate**, **das Forget Gate**, **des Forget Gates**.

> **Eine Falle IM eigenen Fachgebiet ist gefährlicher als eine ferne.** Das Flughafen-`Gate` hilft bloß
> nicht weiter. Das LSTM-`Gate` **liefert korrektes Genus für den falschen Referenten** — genau der
> `Span`-Fehler, nur eine Etage näher am Text. Wer in einer LLM-Lektion „das Gate" schreibt, landet beim
> Leser nicht am Flugsteig, sondern am Vergessens-Tor eines rekurrenten Netzes.

#### §G Was der Auftrag als Struktur behauptete und was der Gate wirklich prüft

Der Auftrag verlangte **„byte-identische Code-Fences"**. `scripts/locale_parity.py` prüft das **nicht**: es
vergleicht **Fence-Anzahl pro Sprache** und zählt inhaltliche Abweichungen als `tolerated`. Das ist auch
richtig so — Mermaid-Labels folgen der Seitensprache (Kanon §3), nur die Protokollartefakte `tool call:` /
`tool result:` und Codebezeichner bleiben englisch. **Wer die strengere Fassung geglaubt hätte, hätte die
Diagrammbeschriftungen englisch gelassen und damit eine echte Regel verletzt, um eine erfundene
einzuhalten.** Für den Rest gilt die Auftragsbeschreibung wörtlich: Dateimenge, H1/H2-Folge, Komponentenzahl,
Zahlentoken und — hier nicht einschlägig, weil beide Seiten keine haben — die **geordnete** Folge expliziter
Heading-IDs.

#### §H Eine Gate-5-Zeile ist durch die eigene Inventarliste gefallen

Die Liste der load-bearing strings wurde von Hand zusammengestellt und enthielt **17 von 18** — die
Überschrift des Validierungsabschnitts fehlte und wäre ungeprüft in die Seite gegangen. Sie wurde
nachträglich einzeln durch Generierung und Blindbewertung geschickt.

> Das ist wörtlich die stehende Regel des Kanons, angewandt auf den Kanonanwender: **„eine Flächenangabe
> wird ausgezählt, nicht übernommen."** Drei Durchgänge in Folge haben sich jetzt an genau diesem Punkt
> geirrt (Playbook §7.7, die Gedankenstrich-Zeile, diese Liste). **Der Fehlertyp ist nicht die Ausnahme,
> sondern der Normalfall** — und die Konsequenz für die Wellen ist, die Strings pro Seite **aus der Datei zu
> greppen**, statt sie aufzuschreiben.

#### §I Die Prosa-Gates haben echte Defekte gefunden — der Pilot ist nicht durchgerutscht

Gates 2/3/4 haben eine **substanzielle** Reparaturrunde erzwungen: **drei Kaltlesungen** (zwei auf
Verstehen, eine ausdrücklich auf Natürlichkeit) plus der **Cross-Model-Registerrichter**. Das ist die
scheduled-2b-Runde des Playbooks, und sie war nötig. Die Klassen, geordnet nach Ertrag:

1. **Wörter, die auf den falschen Pfad führen** (§J) — die wertvollste Klasse, weil der Satz danach
   grammatisch tadellos ist und trotzdem etwas anderes sagt.
2. **Nicht-native Wortbildung.** `bedeutungsnah` — durchsichtig gebaut, sofort verständlich und **kein
   etabliertes deutsches Wort**; eine Kaltleserin benannte genau diese Stelle als den Punkt, an dem sie an
   der Muttersprachlichkeit zweifelte. Es stand auf **beiden** Seiten an strukturell paralleler Position,
   was es als feste Ersatzform für ein englisches Wort ohne deutschen Einwortpartner entlarvt. →
   „semantisch ähnlich" / „inhaltlich ähnlich".
3. **Kollokationen auf englischem Gerüst** — „ein kleinerer Satz an Tools", „die erste Anfrage zahlt
   Latenz", „Diese Seite nimmt vier Fragen dazu", „Drei Kosten fallen an" (`Kosten` ist ein Plurale tantum
   und lässt sich nicht zählen), „das tragende Wort" (*load-bearing*, im Deutschen sind Wände tragend, nicht
   Wörter), „durch die Konstruktion des Verfahrens" (*by construction*). **Jede einzelne dieser Fügungen
   hätte eine Flüssigkeitsprüfung überstanden — genau Falle 3 aus `_language.md` §1.1.**
4. **Korrekte Wörter, die kein deutscher Entwickler sagt** — `Handlung` für *action* (das hat ein Roman),
   `Auflagen` für *requirements* (behördlich), `Parole` für *slogan*, `annehmbare Argumente` (= erträglich,
   nicht zulässig), „je Antwort/je Aufruf" statt „pro" (DIN-Register).
5. **Ein Versprechen ohne Einlösung.** Die Beschriftung „Die Parallelität, als Befund mit Datum." kündigt ein
   Datum an, und es folgt keines. Beide Leser haben es unabhängig markiert.

**Was ausdrücklich NICHT angetastet wurde:** die Stellen, die die dritte Leserin als unverwechselbar
deutsch hervorhob („einander ins Gehege kommen", „macht aus einer kurzen Störung einen Ausfall", „Es erzeugt
Text, und dabei bleibt es."). **Eine Reparaturrunde, die diese glattzieht, hat die Seite schlechter
gemacht, nicht besser** — das gehört als Regel in jeden Reparaturbrief.

#### §J Die wertvollste Klasse: das Wort, das den Leser auf den falschen Pfad schickt

Kein Gate der Ebene 1 sieht diese Klasse, weil jeder einzelne Satz korrekt ist. Gefunden hat sie die
Kaltlesung — und der teuerste Fall hat **beide** Kaltleser unabhängig voneinander entgleisen lassen:

- **`zusammenfassen` für *batching*** (Seite 2, ~4 Vorkommen). Im Deutschen heißt `zusammenfassen`
  **zuerst *summarize*** — in einem Text über Sprachmodelle die schlechtestmögliche Kollision. „Anthropic
  Claude fasst standardmäßig zusammen:" wurde gelesen als *„Claude fasst standardmäßig zusammen"*.
  Erschwerend: dieselbe Seite verwendet später **`Batch`** für dieselbe Sache, es konkurrieren also zwei
  Termini und der ältere ist der mehrdeutige. **Regel: nie nackt — „fasst die Aufrufe zu einem Batch
  zusammen", und `Batch` ist ab dem ersten Vorkommen das tragende Substantiv.**
- **`unterstellt`** — gemeint war *setzt voraus*; gelesen wurde erst *unterordnen*, dann der
  vorwurfsvolle Sinn (*jemandem etwas unterstellen*). Die Kursivsetzung machte es schlimmer: sie
  signalisiert „hier liegt die Bedeutung" und zeigt auf die falsche. → „setzt das Modell voraus".
- **`Die Überführung`** als nackte Beschriftung eines Aufzählungspunktes — landet auf dem forensischen Sinn (*jemanden überführen*).
  Das **Verb** ist im Kontext einwandfrei („in eine Grammatik überführen"), das isolierte Substantiv nicht.
  → „Die Umwandlung des Schemas beim ersten Aufruf."
- **`Bestand`** beim ersten Vorkommen — gelesen als *Fortbestand* („dafür sorgen, dass es weiter besteht"),
  **was den Satz in sein Gegenteil verkehrt**. Klar wird es erst beim zweiten Vorkommen. → beim ersten Mal
  explizit: „den Tool-Bestand".
- **`über sie schließen`** — **eine Konstruktion, die es im Deutschen nicht gibt.** Das Deutsche hat
  `auf etwas schließen` und `Schlüsse über etwas ziehen`; `über etwas schließen` ist die Blaupause einer
  anderen Sprache. Es war zugleich der Satz, an dem die Leserin am längsten hängenblieb.

> **Die Lehre für die Wellen:** ein Wort, dessen häufigster Sinn im Zielfach *daneben* liegt, ist gefährlicher
> als ein falsches Wort — denn es wird nicht als Fehler gelesen, sondern als Aussage. **Das ist die
> Falscher-Sinn-Falle (§1.1, Falle 1) auf der Ebene des laufenden Textes statt der Termzeile**, und nur eine
> Kaltlesung findet sie.

#### §K Die Überschriften waren die schwächste Schicht — und das ist die Schicht, die Gate 5 schützen soll

Die dritte Kaltlesung war ausdrücklich auf **Natürlichkeit** angesetzt, nicht auf Verstehen. Ihr
Gesamturteil: *„deutlich über dem Übersetzungsdurchschnitt"* — **und die schwächste Schicht sind die
Überschriften und die Merksätze**, also genau die Strings, die Gate 5 vorab abgesichert hatte.

**Der Befund, der ins Gate-Design gehört: der Blindrichter und die naive Kaltleserin sind über
Überschriften systematisch verschiedener Meinung.** Der Richter prämiert **Nominalstil und
Informationsstruktur** — beides korrekte deutsche Überschriftentugenden; dieselbe Überschrift nennt die
Leserin **gestelzt**. Beide urteilen zutreffend über verschiedene Größen, und **keiner von beiden ist als
Alleinentscheider richtig**.

**Und eine Klasse sieht Gate 5 grundsätzlich nicht: die Eigenschaft der FOLGE.** Die Leserin benannte den
Listicle-Rhythmus — **drei gezählte Überschriften hintereinander** („Der Tool-Call in vier Schritten",
„Vier Fehlerbilder …", „Drei Kosten …") — und, in derselben Kategorie, **einen Referenten mit vier Namen**
(`Bestand`, `Satz an Tools`, `Tool-Liste`, `Tool-Katalog`). Jede einzelne Zeichenkette ist einwandfrei;
defekt ist erst die Reihe.

> **Gate-Design-Befund, protokolliert:** **Gate 5 beurteilt Zeichenketten in Isolation und kann eine
> Eigenschaft der Seite grundsätzlich nicht sehen.** Nach Gate 5 muss deshalb eine **Seitenkonsistenzprüfung**
> laufen: Überschriftenfolge als Ganzes, ein Referent = ein Name, kein Metronom aus Pointen (auf Seite 2
> endeten **elf Absätze in Folge** auf einen kurzen Merksatz — jeder für sich gut, zusammen eine Maschine).
> *(Als Amendment zu Gate 5 im `de-locale-playbook.md` §4 eingetragen.)*

#### §L Dreimal hat ein Zitat das Ohr eines Prüfers überstimmt — und das ist kein Streit, sondern die Regel

Die dritte Leserin schlug drei Änderungen vor, die **abgelehnt** wurden. Sie stehen hier vollständig, weil
eine stille Ablehnung genau der Verlust wäre, gegen den dieser Anhang existiert. **Alle drei gehen in das
Leserpaket (#278), nicht in einen stillen Flip.**

1. **„Prinzip der geringsten Berechtigungen" → „Prinzip der geringsten Rechte".** **Abgelehnt.** Die Form
   ist **BSI IT-Grundschutz ORP.4.A2**, wörtlich per `pdftotext | grep` nachgeprüft: „(Prinzip der
   geringsten Berechtigungen, englisch Least Privileges …)". Die Hausaufteilung des Kanons weist genau
   diese Form dem **berechtigungsvergebenden** Text zu, und um solchen handelt es sich hier. **Das Ohr eines
   naiven Lesers schlägt keinen Stufe-1-Beleg — das ist der SK-Fáza-26-Fehlermodus in umgekehrter
   Richtung.** Die Zeile trägt ohnehin ihre eigene DISPUTED-Notiz zu *minimalen Rechte*.
2. **`title: Tool-Einsatz` → „Tool Calling" / „Werkzeuge aufrufen".** **Abgelehnt.** Es ist das
   **ausgelieferte** Sidebar-Kategorielabel, und es hat eine Cross-Model-Blindbewertung auf `Nominalstil`
   mit **KNAPPEM** Abstand gewonnen — unter der stehenden Regel „knapper Abstand ⇒ Incumbent halten". Der
   Einwand (englisches `Tool-Call` neben eingedeutschtem `-Einsatz`) ist real und wird protokolliert;
   **ein Flip braucht einen Beleg, kein Ohr.**
3. **„Zeitbeschränkung" → „Timeout".** **Teilweise abgelehnt.** Die deutsche Zweiteilung ist attestiert und
   gewollt: `die Zeitbeschränkung` = der konfigurierte Grenzwert, `die Zeitüberschreitung` = der ausgelöste
   Fehler, `das Timeout` = überall zulässig. Die Leserin hat aber recht, dass die **Fehlertaxonomie-Zeile**
   die präzise Unterscheidung nicht braucht. **Auflösung: die Zweiteilung bleibt, wo Präzision der Punkt
   ist; in der Taxonomiezeile steht „Timeout".**

#### §M Der Pilot hat einen Defekt in der ENGLISCHEN Quelle gefunden — und ihn nicht repariert

Beide Kaltleser blieben unabhängig voneinander an derselben Stelle stehen: der Anthropic-`tool_choice`-
Passage. Englisch heißt es sinngemäß, Claude setze parallele Aufrufe ab, wann immer eine Anfrage davon
profitiert — und, zwei Sätze später, **„mit `tool_choice` vom Typ `auto` ruft das Modell höchstens ein Tool
pro Antwort auf"**. **Wörtlich gelesen widersprechen sich beide Sätze, weil `auto` der Default ist.**

**Das Deutsche ist quellentreu; die Unklarheit sitzt oben.** Die fehlende Bedingung zu ergänzen („wenn
dieser Schalter gesetzt ist") würde eine Tatsache behaupten, **die die Quelle nicht hergibt**. Deshalb:
**als Quelldefekt gemeldet, nicht still repariert.** Beide Leser sagten übereinstimmend, dies sei die eine
Stelle, an der sie das Falsche gebaut hätten.

> **Die Lehre:** die Sekundärlocale ist ein **Prüfinstrument für das Englische**. Ein Kaltleser ohne
> Quellzugang stolpert über genau die Sätze, die im Original mehrdeutig sind — und **eine treue Übersetzung
> macht die Mehrdeutigkeit sichtbar, statt sie zu glätten.** Glätten wäre der Defekt.

#### §N Zwei Methodenbefunde über die Gates selbst — beide über die Eingabe, nicht über das Urteil

**N1 — ein Gate gegen ein noch entstehendes Artefakt gefahren.** Eine mechanische Prüfung lief gegen eine
Datei, die ein Agent gerade noch schrieb, und meldete einen Defekt, den es nicht gab. **Regel: ein
Artefakt, das noch entsteht, wird nicht geprüft.** Der Gate hat nicht falsch geurteilt — er hat
über einen Zwischenstand geurteilt, und ein Zwischenstand ist kein Prüfgegenstand.

**N2 — die Eingabeaufbereitung des Registerrichters hat Defekte fabriziert.** Dem Richter wurden Sätze vorgelegt, die
die Extraktion bei **300 Zeichen** abschnitt. Ergebnis: **elf „Satzabbruch"-Urteile**, die sämtlich
Artefakte der Extraktion waren und nichts über den Text sagten. **Der Richter hat das Muster selbst
markiert** — was ihn entlastet und die Aufbereitung belastet.

> **Regel, die beide teilen: die Eingabevorbereitung eines Gates IST Teil des Gates.** Ein sauberes Urteil
> über eine kaputte Eingabe ist ein kaputtes Gate. Beim Aufsetzen jedes Gates wird deshalb erst die
> **Eingabe** geprüft (vollständig? fertig? unverstümmelt?), dann das Urteil.

#### §O Ein Befund, der hier NUR protokolliert und ausdrücklich NICHT entschieden wird

**Die Metaprosa dieses Kanons schließt deutsche Anführungen mit einem ASCII-`"` (U+0022).** Ausgezählt am
2026-07-28 — Codepoints statt Zeichen benannt, damit die Zählung nachprüfbar bleibt, ohne sich selbst zu
verfälschen: `_language.md` **833×** U+201E (öffnend) gegen **0×** U+201C (schließend); `rag.md` 136 : 0;
`ai-sdlc.md` 169 : 0. *(Stand **vor** den Nachträgen dieser Phase; die neuen Zeilen folgen derselben
Hauspraxis und erhöhen die linke Zahl, nicht die rechte — die rechte bleibt bei allen drei Dateien null.)* **Das ausgelieferte Korpus macht es richtig** — der slowakische Lektionsbaum steht bei
339 : 339, und die beiden deutschen Pilotseiten bei 11 : 11. Betroffen ist also **nur die Metaprosa der
Redaktionsdokumente**, kein einziger Leser-sichtbarer String.

**Das ist formgleich mit der offenen Frage in #318** (bindet die Gedankenstrich-Regel die *eigene* Metaprosa
des Kanons? — `_language.md` führte am 2026-07-28 **608** Geviertstriche U+2014, die es dem Korpus verbietet). **Deshalb wird hier
nichts geändert:** es ist eine **locale-weite redaktionelle Entscheidung**, keine Pilotentscheidung, und sie
gehört nach #318. Der Pilot liefert nur die Zählung, damit die Entscheidung dort auf Zahlen und nicht auf
einem Eindruck getroffen wird.

---

### Phase 4 (2026-07-28) — Welle 1, Belegdurchgang vor der Prosa (RAG Teil I)

*Fünf parallele Attestierungsbatches über die 13 englischen Dateien unter `docs/part-1-rag/` (A Evaluation
und Messung · B Retrieval-Mechanik · C Sicherheit und Datenschutz · D Inhalt und Daten · E Observability
und Betrieb), danach **ein** Zusammenführungsdurchgang (Gate 6.5) über alle fünf Ledger gleichzeitig.
**Kein Renderdurchgang, keine Prosa** — dieser Eintrag protokolliert, was das Register vor der ersten
deutschen Seite gekostet und erbracht hat.*

#### Die Zahlen, gemessen und nicht geschätzt

- **59 Kopfwörter** haben die fünf Batches beurteilt. **Sieben** davon hatten bereits eine Kanonzeile —
  und bei **dreien** (`Budget`, `Cap`, `Signal`) betraf die vorhandene Zeile nur das **Markenkompositum**
  (*Error Budget*, *Soft Cap / Hard Cap*, *Golden Signals*), **nicht das Appellativ**, das die Prosa
  tatsächlich braucht. **Zweiundfünfzig Kopfwörter waren neu.**
- **Rund 45 Zeilen sind SETTLED** (mehrere davon mit ausdrücklich WEAK oder OPEN markiertem Teilzweig),
  **18 Zeilen stehen OPEN** — jede mit ihrer Schließbedingung in §3 —, **kein einziger neuer
  DISPUTED-Fall.** Die bestehenden DISPUTED-Zeilen (*Recall/Precision*, *Cold Start*, *Drift*, *Harness*,
  *API*, die Formwahl bei *Least Privilege*) sind **unberührt geblieben**.
- **Der Kanon ist an fünf Stellen gewachsen, deren Zählung im Text steht und deshalb mitgezogen werden
  musste:** der Fallenkasten von **sechzehn auf einundzwanzig**, §1.1.g von **vierzehn auf achtzehn**, und
  — weil Punkt 4 des Injektionsblocks jene achtzehn **aufzählt** — auch der Block, der **wörtlich in jeden
  Render-Prompt** kopiert wird.

#### Was die Prosa an Register verlangt hat, das die Glossar-Saat nicht enthielt

Das Startregister (§2) ist aus den **Hochfrequenztermini des englischen Quellbaums** gezogen worden, also
aus dem, was eine Terminologieliste sieht. **Was es nicht sah, ist das Bindegewebe:** `cost` (57),
`attack` (54), `masking` (29), `parsing` (29), `claim` (25), `metadata` (25), `budget` (23), `sampling`
(27 — und, gezählt, **alle 27 im statistischen Sinn**), `passage` (17), `fusion` (17), `refusal` (15),
`length` (15), `paper` (15). **Das sind keine Fachbegriffe, das sind die Wörter, mit denen ein Fachtext
Sätze baut** — und genau sie hatten keine Zeile. Der Befund ist deshalb nicht „das Register war
unvollständig", sondern schärfer: **ein aus Termfrequenz gezogenes Register erfasst systematisch nicht,
was ein Kapitel FLIESSEND macht.**

#### Sechs Kollisionen, die kein einzelner Batch sehen konnte

**Alle sechs sind von der Gestalt, für die Gate 6.5 existiert: jede Seite war für sich richtig.**

1. **`Normierung` (B) gegen `Score-Normalisierung` (A).** Batch B hat den Referenten **eigens studiert**
   und ruled `die Normierung` (WEAK, mit protokollierter Gegenevidenz); Batch A schrieb beim Ruling zu
   `calibration` **im Vorbeigehen** „die **Score-Normalisierung**" in ein durchgearbeitetes Beispiel.
   → **B gewinnt** nach der Vorrangregel *wer den Referenten eigens studiert hat, schlägt wer ihn beiläufig
   verwendet*. **Beide Seiten bleiben stehen:** A's **Aufspaltung** (Judge-Kalibrierung ≠
   Score-Skalierung) war die eigentliche Einsicht und wird übernommen — nur das Wort wechselt.
   **Korpusform: „RRF braucht keine Score-Normierung."**
2. **Die Glosse für `Faithfulness`.** Batch A fand zwei unabhängige deutsche Quellen, die die Metrik mit
   **Quellentreue** glossieren, und hat die Frage **eskaliert, statt §2 anzufassen** — richtig, denn §2
   führte `Faithfulness` als settled kept-EN **ohne** Glosse. → **Die Zeile wird nicht umgedreht, sie
   bekommt eine Glosse** und wandert aus der glossenlosen Liste in die Glossentabelle. Die mitgemeldete
   Doppelglossen-Sorge ist geprüft und **aufgelöst**: *Grounding* ist der **Vorgang**,
   *Faithfulness/Groundedness* die gemessene **Eigenschaft** — Sense-Card in §4.
3. **`Error Budget` — ein Selbstwiderspruch INNERHALB dieser Datei.** §2 führte den Loan als settled
   kept-EN, während die deutsch geführte Tabelle **derselben Datei** sowie `_language.md` §1.1.g und §1.2
   **das Fehlerbudget** setzen. → **Der Loan wird gestrichen**, sichtbar und mit Grund; die deutsche Zeile
   ist die belegte (Computerwoche und iX schreiben ausschließlich deutsch), die kept-EN-Nennung war ein
   Bootstrap-Rest. **Im selben Zug `Latency Budget`:** stand kept-EN **ohne jeden Beleg** → nach §3, OPEN,
   mit Schließbedingung. ⚠ **Der Widerspruch stand seit dem Bootstrap in einer Datei und ist von keinem
   Prosa-Gate gefunden worden — Gates lesen Sätze, nicht Register.**
4. **`Sampling` fuhr auf einem Beleg mit, der einem anderen Referenten gehört.** Die einzige deutsche
   Attestierung des Kanons (§1.1.e, heise) belegt den **statistischen** Sinn; die MCP-Zeile und die
   Decoding-Zeile in §2 standen unbelegt daneben. **Das ist der `Span`-Fehler eine Etage höher: korrektes
   Genus für den falschen Referenten.** → Sinn (iii) behält den Beleg; die **MCP-Fähigkeit wird Klasse 1**
   (Eigenname); der Decoding-Sinn läuft über die bestehende `Sampler`-Zeile; Sense-Card in §4.
   ⚠ **Der Auftrag hatte die Lage umgekehrt vermutet** — die Beleglage fiel andersherum aus.
5. **`der Dienst` — und die Zählung, die vier Batches gleichzeitig fortschrieben.** Batch E fand eine
   §1.1.g-Zeile, die **fehlte**, obwohl der Kanon längst so schreibt (§1.4, §9.3, § Gendern). ⚠ **Die
   eigentliche Kollision war arithmetisch: DREI Batches meldeten unabhängig „damit wächst §1.1.g auf
   fünfzehn"** (B für *Kosinus-Ähnlichkeit*, D für *mehrsprachig*, E für *der Dienst*), Batch C reichte
   *die Schwärzung* nach. **Jede Meldung war für sich richtig und alle vier zusammen falsch.** →
   **vierzehn → achtzehn**, in der Tabelle **und** im Injektionsblock. **Ebenso doppelt belegt war der
   Fallenkasten:** B beanspruchte Platz **17** für `Trunkierung`, E denselben Platz für `Service`. →
   beide sind gültige Fallen, der Kasten geht auf **einundzwanzig**.
6. **`verbosity bias` / `self-preference bias` — hier hat Gate 6.5 GEGEN die Zurückhaltung eines Batches
   entschieden, und das steht ausdrücklich so da.** Batch A belegte das Bildungsmuster auf **Stufe 1**
   (BSI: geschlossenes Kompositum, deutsches Erstglied, englisches Original in Klammern, 16 Geschwister)
   und **prägte die beiden Wörter bewusst nicht**, weil es ihre Vorkommen nicht besaß. Der
   Zusammenführungsdurchgang hat gezählt — **`verbosity bias` 4×, `self-preference` 6× + `self-enhancement`
   2×** —, beide liegen über der Nachtragsschwelle und **müssen** eine Wiedergabe haben. →
   **Das Muster lizenziert die FORM, nicht das WORT:** *der Ausführlichkeitsbias (Verbosity Bias)*,
   *der Selbstbevorzugungsbias (Self-Preference Bias)*, **WEAK**, mit **pflichtiger** englischer Klammer —
   und wo der Quelltext ohne „bias" auskommt, wird **nicht substantiviert, sondern der Satz gebaut**.
   **Batch A's Abstinenz bleibt als Gegenstimme im Protokoll**, weil sie methodisch richtig war.

#### Fünf Befunde, die den eigenen Vorhandensvermutungen eines Batches widersprochen haben

*Diese Liste steht hier, weil ein Ledger, das nur seine Ergebnisse zeigt, seine teuerste Arbeit verbirgt.*

- **`die Schwärzung` war als REJECTED geschrieben**, bevor die BSI-Handreichung auftauchte: **weder Duden
  noch DWDS führen unseren Sinn** (nur „schwarz färben", der fotografische Sinn und, süddeutsch-salopp,
  „schmuggeln"). **Die Stufe-1-Domänenquelle überschreibt die Wörterbuchlücke** — die `Log`-Lehre
  („‚unbelegt' hieß mehrfach ‚falsch gesucht'") ein zweites Mal bestätigt.
- **`kalibrieren` hätte scheitern können:** Duden führt **nur** messtechnische Sinne. Gerettet hat die
  Zeile **DWDS-Sinn 2** — die andere Hälfte der Lehre: *eine Falle in EINEM Wörterbuch heißt nicht, dass
  das ANDERE den richtigen Sinn nicht führt.*
- **`überschreiben` ist NICHT einfach falsch**, und das wäre beinahe so protokolliert worden: dieselbe BSI
  verwendet es für *override*. Der Kanon übernimmt es trotzdem nicht — **aber beide Befunde stehen im
  Eintrag**, damit niemand später den zweiten „entdeckt" und die Zeile für nachlässig hält.
- **Bei `domain` saß die Falle nicht, wo der Auftrag sie vermutete.** Erwartet war „Domain heißt zuerst
  Internetdomain"; **der gefährlichere Zwilling steckt im deutschen Wort** (Windows-/AD-Domäne). Der
  Ausweg auf *Domäne* wehrt den Netzsinn also gar nicht ab — **die Fügung tut es.**
- **Bei `Kosten` hatte der Kaltleser recht und die Diagnose war falsch.** Das Pluraletantum blockiert
  **den Zähler, nicht das Verb**: „Es fallen Kosten an" ist einwandfrei, „drei Kosten" ist es nicht. **Wer
  daraus „*anfallen* ist verboten" macht, repariert das falsche Wort.**
- *(Kleiner, aber teuer:* **`Dashboard` fehlte nicht — es stand im falschen Unterabschnitt.** Die Zeile
  ist seit dem Bootstrap in §1.1.a korrekt und vollständig; wer eine Observability-Seite rendert, lädt
  aber §1.1.e und findet sie dort nicht. Repariert mit einem **Querverweis**, nicht mit einem Umzug —
  Verschieben bräche bestehende Verweise, ohne etwas zu entscheiden.*)

#### Eine neue Klasse, die der Fallenkasten nicht hatte

Die einundzwanzig Kastenzeilen enden alle mit „Wort nicht verwenden". **Welle 1 hat eine zweite Klasse
sichtbar gemacht, deren Konsequenz „Wort verwenden, aber nie nackt" lautet:** `Kandidat` (Wörterbücher
kennen nur Personen), `Passage` (Ladenpassage), `Aussage` (Zeugenaussage), `Verweigerung` (Kriegsdienst —
eine **Dominanzfalle**, kein falscher Sinn), `Domäne` (AD-Domäne). Bei allen fünf trägt **die Fügung** den
Referenten, nicht das Lemma. **Sie in den Kasten zu schreiben hieße, fünf Wörter zu verbieten, für die es
keinen Ersatz gibt — und der nächste Durchgang erfände einen.** Die Trennung *verbieten* gegen *binden*
ist deshalb selbst die Entscheidung; sie steht als eigener Unterkasten in `_language.md` §1.1.
`Alarmmüdigkeit` schließt die Klasse als **Grenzfall** ab: dort hilft keine Kollokation, weil das Problem
das **Register** ist (Intensivmedizin) — die Zeile bleibt OPEN.

#### Was dieser Durchgang NICHT konnte

- **Er sieht nur Widersprüche.** Was ein einzelner Batch für sich falsch beurteilt hat, findet er nicht —
  das ist die eingebaute Grenze von Gate 6.5 und keine Nachlässigkeit dieses Laufs.
- **Er hat nicht nachrecherchiert.** Wo zwei Ledger eine Frage offen ließen, steht die Zeile **OPEN mit
  gehaltenem Incumbenten**; das ist das korrekte Ergebnis, nicht ein Patt.
- **Die deutsche Fachbuchschicht (dpunkt, Rheinwerk, O'Reilly DE) und die kostenpflichtigen iX-/c't-
  Volltexte blieben wieder unerreichbar** — dieselbe Feststellung wie in Phase 2, und dort liegen
  weiterhin die meisten der offenen Antworten.
- **Achtzehn OPEN-Zeilen sind kein Restposten, sondern die Arbeitsliste der nächsten Welle.** Sechs davon
  (`Alert Fatigue`, `Tail-Latenz`, „the tail", `Latenzbudget`, `staleness/freshness`, `burn-rate
  alerting`) betreffen **eine einzige Seite** — die Observability-Vertiefung. Wer sie rendert, rendert
  eine Seite, deren Kernvokabular im Deutschen **nicht existiert**, und muss durchgehend umschreiben.
  Das gehört in den Renderbrief, nicht in eine Fußnote.

---

### Phase 5 (2026-07-29) — Welle 1, Seiten- und Wellenkonsistenz NACH der Prosa (RAG Teil I)

*Ein Durchgang über alle dreizehn ausgelieferten deutschen Seiten unter `part-1-rag/`, nachdem sechs Renderer
sie parallel geschrieben hatten. **Das ist die Schicht, die das Playbook nach dem Piloten eingezogen hat:
Gate 5 beurteilt Zeichenketten in Isolation und kann eine Eigenschaft der SEITE oder der WELLE grundsätzlich
nicht sehen** (§8 Phase 3 §K, Amendment in `de-locale-playbook.md` §4). Kein Renderdurchgang, keine neue
Recherche — gezählt, geruled, angewandt, protokolliert.*

#### Der Befund, der alles andere erklärt

**Jeder Renderer hat innerhalb seiner Lektion sauber gearbeitet. Es gibt in dieser Welle keine einzige
Kollision INNERHALB einer Seite. Alle liegen ZWISCHEN den Seiten** — und keine einzelne Instanz ist ein
Fehler: jede Zeichenkette für sich ist einwandfreies Deutsch, jede war lokal die richtige Wahl. **Defekt ist
erst die Menge.** Das ist dieselbe Gestalt wie bei Gate 6.5 eine Etage tiefer (dort kollidieren
Attestierungsbatches, hier Renderer), und es ist der Grund, warum ein Konsistenzdurchgang **zählen** muss und
nicht lesen kann: ein Prüfer, der die Seiten nacheinander liest, sieht auf jeder Seite ein stimmiges Bild.

#### Die teuerste Kollision: EIN Referent, SIEBEN Namen

`retrieval failure` / `generation failure` ist das diagnostische Rückgrat, das der Überblick aufspannt; es
kehrt auf mindestens acht Seiten wieder. Es trug **sieben** deutsche Namen: *Fehler des Retrievals*
(ausgerechnet auf der Seite, die den Terminus **definiert**), *Versagen des Retrievals* (4×), *Fehler im
Retrieval* (3×), *Fehlerquote des Retrievals*, *die Quote*, *Fehler der Generation* (3×), *Fehler in der
Generation* (3×). **Der Pilot hatte vier Namen für einen Referenten; eine Welle mit sechs parallelen
Renderern kommt auf sieben — die Zahl skaliert mit der Zahl der Autoren, nicht mit der Zahl der Seiten.**

**Geruled: `das Fehlerbild des Retrievals` / `das Fehlerbild der Generation`** — Begründung, Abgrenzung gegen
`die Fehlerklasse` und der Verbleib des Verbs `versagen` stehen in der `Fehler`-Sense-Card (§4), wo die
Entscheidung hingehört. ⚠ **Der eigentliche Befund über die Methode ist ein anderer:** die Karte hatte die
Antwort seit dem Bootstrap („Kategorie → das Fehlerbild"), und **zwei Seiten hatten sie unabhängig
voneinander bereits angewandt**, ohne dass eine Zeile sie festhielt. **Der Kanon war nicht unvollständig — er
war unangewandt.** Ein Register beantwortet keine Frage, die niemand ihm stellt; deshalb muss der
Konsistenzdurchgang die Karte **gegen die gezählten Namen halten** und nicht darauf warten, dass ein Renderer
nachschlägt.

#### Zwei Kanonzeilen haben einander widersprochen — und beide Male gewann die, die ein System bildet

1. **`top-K` gegen `Top-k`.** §3 und § Typografie setzen `top-K`, §1.1.b setzte `Top-k`. **Die §1.1.b-Zeile
   ist gestrichen** (sichtbar, mit Begründung, wie die `Error-Budget`-Streichung). Entschieden hat nicht die
   Mehrheit der Fundstellen, sondern dass die eine Seite ein **System** ist — dieselbe Positionsregel trägt
   `vLLM` und `promptfoo`, und das große `K` bindet an `Recall@K` — während die andere sich **selbst als
   „Usus-Beobachtung, keine Norm"** deklarierte. **Eine Zeile, die ihre eigene Beweislast benennt, hat den
   Streit vorentschieden.**
2. **`Golden Set` gegen `der Goldstandard` — innerhalb DERSELBEN Datei**, zum zweiten Mal nach `Error Budget`.
   §2 führte den Loan zweimal, die deutsch geführte Tabelle derselben §2 und `_language.md` §1.1.b setzten den
   deutschen Terminus. **Die Welle hatte längst abgestimmt: 29 : 0.** Streichung in §2.

> **Die Lehre, die aus beiden zusammen folgt und die über diese Welle hinausreicht: wenn ein Register und
> sechs unabhängige Renderer auseinandergehen, ist das REGISTER der Verdächtige.** Beim Geviertstrich (unten)
> war es genauso: sechs Renderer haben denselben Kanonfehler unabhängig voneinander korrigiert. **Der Korpus
> ist ein Prüfinstrument für den Kanon, nicht nur umgekehrt.**

#### Der Kanon hat jedem Renderer aufgetragen, einen verbotenen Codepoint auszuliefern

**§2 gibt seine Pflichtglossen zum wörtlichen Übernehmen frei — und schrieb fünf davon mit U+2014**, dem
Geviertstrich, den § Typografie dem Korpus verbietet und den die Codepoint-Zählung zurückweist. Repariert
sind die fünf plus `Groundedness` (`_language.md`) und `Harness` (`ai-sdlc.md`).
**Die Regel, die daraus wird: eine Zeichenkette, die der Kanon zum wörtlichen Übernehmen freigibt, ist ein
AUSGELIEFERTER String und untersteht der Typografie — auch wenn sie in einer Redaktionsdatei steht.**
⚠ **Ausdrücklich nicht angetastet:** die **Metaprosa** der Kanondateien (das ist §8 §O und #318, eine
locale-weite redaktionelle Frage) und **Zitate aus Quellen** — ein Zitat zu glätten fälscht den Beleg.
**Die Grenze zwischen beidem zu ziehen war die eigentliche Arbeit dieser Zeile**, nicht das Ersetzen.

#### Was der Durchgang an neuen Zeilen erzwungen hat — und woran man sie erkennt

**Siebzehn neue §1.1-Zeilen**, und **keine einzige** entstand aus einer Prägung: jede hält fest, was die
Renderer bereits einstimmig geschrieben hatten, ohne nachschlagen zu können — `die Quellenangabe` (21× auf
einer Seite allein 18×), `die Prüffrage` (7×), `die Modellbeschreibung` (2× wortgleich),
`referenzfrei/referenzbasiert` (8×), `Faithfulness` **artikelfrei** (32× ohne einen einzigen Artikel),
`Late Interaction` (6× ohne Artikel). **Das ist das Muster, das die Zeilen belastbar macht: sechs Renderer,
die dieselbe Lösung finden, ohne voneinander zu wissen, sind eine Messung — kein Konsens.**
⚠ Und der Umkehrschluss steht mit im Register: **`labeln` bleibt OPEN**, obwohl eine Seite „gelabelte Daten"
schreibt. **Ein Konsistenzdurchgang schließt keine offene Zeile** — die Stelle ist gemeldet, nicht geändert.

#### Zwei Fallen, die der Fallenkasten nicht hatte, und beide sind vom Typ „richtig, aber nie nackt"

- **`die Generation`** — der gesetzte Schichtname, aber im Deutschen zuerst die **Alterskohorte**. Damit
  gehört er in die Klasse von `Bestand`, `Kandidat`, `Passage`, `Aussage`, `Domäne`, die Welle 1 aufgemacht
  hat. Dazu kam ein zweiter Name für dieselbe Stufe (`die Generierung`, 3× auf einer Seite, u. a. im
  Diagramm) — **vereinheitlicht auf `Generation`**.
- **`das Korpus`** — das Genus wechselte zwischen den Seiten, also genau das, was §1.1 als lautestes
  Maschinenübersetzungs-Signal führt. ⚠ **Und der Beweis stand schon im Text:** dieselben Seiten, die „**den**
  gesamten Korpus" schrieben, schrieben den Plural „Unternehmen**skorpora**" — *Korpora* ist der Plural des
  **Neutrums**. **Ein Text kann seinen eigenen Fehler beweisen, wenn man ihn zählt statt liest.**

#### Zwei Entscheidungen, die Teil II und Teil III BINDEN

1. **`sidebar_label: Teilübersicht` → `Überblick`.** *Teilübersicht* ist **keine attestierte deutsche Form**,
   sondern eine Prägung, und sie decodiert zweideutig: „Übersicht über den Teil" **oder** „teilweise
   Übersicht" — und ein Sidebar-Label hat keinen Kontext, der die falsche Lesart abwehrt. Ihr Renderer hatte
   das gemeldet; ausgeliefert wurde sie trotzdem, weil eine andere Seite sie in der Prosa aufgriff. **Genau
   dieser Mechanismus ist die Gefahr: ein gemeldeter Defekt zementiert sich, sobald eine Nachbarseite ihn
   zitiert.** ⇒ **Die Übersichtsseite jedes Teils trägt `sidebar_label: Überblick`**, und die Prosa verweist
   auf sie als **„der Überblick zu Teil I/II/III"** — eine Fügung, die zugleich sagt, *welches* Dokument
   gemeint ist.
2. **`Teil I` (der Buchteil) gegen `Teil 1` (die erste Hälfte einer Lektion).** Der Unterschied war
   **römisch gegen arabisch und sonst nichts** — er verschwindet beim Lautlesen, und **zwei von drei
   Kaltlesern sind darüber gestolpert**; auf der Observability-Vertiefung standen beide auf einer Seite und
   meinten zwei verschiedene Dokumente. ⇒ **Konvention: die erste Nennung je Seite wird ausgeschrieben —
   „[Teil 1 der Lektion](./index.md)"** (die Formulierung, die der ausgelieferte Sidebar-Hinweis „Als
   Nächstes: **Teil 2 der Lektion**" ohnehin schon verwendet), danach kurz „Teil 1"; **der Buchteil heißt
   römisch und wird, wo er quer verweist, als „der Überblick zu Teil I" benannt.**

#### Was dieser Durchgang NICHT konnte — und was er ausdrücklich nicht angefasst hat

- **Er sieht nur Mengen.** Was ein einzelner Renderer für sich falsch entschieden hat, findet er nicht; das
  ist die eingebaute Grenze, dieselbe wie bei Gate 6.5.
- **Er hat nicht nachrecherchiert.** Wo kein Beleg vorlag, steht die Zeile **HOUSE** oder **OPEN** mit
  gehaltenem Incumbenten und benannter Schließbedingung — nie eine Prägung.
- **Er hat gutes Deutsch stehen lassen, auch wo es die Einheitlichkeit stört.** `der Zielkonflikt` bleibt
  neben `die Abwägung`, weil er eine **schärfere** Aussage macht (zwei Ziele stehen gegeneinander) und echtes
  Fachvokabular ist. **§8 §I gilt auch für einen Konsistenzdurchgang: eine Runde, die das glattzieht, macht
  den Korpus schlechter.**
- **Er hat einen Quelldefekt gemeldet statt repariert:** `maskieren` ist auf der Guardrails-Vertiefung
  zugleich der **Oberbegriff** und **einer seiner vier eigenen Operatoren** — dieselbe Mehrdeutigkeit trägt
  das englische Original. **Das ist §M, und die Regel gilt unverändert: die Sekundärlocale macht die
  Mehrdeutigkeit sichtbar, sie glättet sie nicht.**
- **Offen an die nächste Welle:** die Observability-Übersicht definiert die Evaluierung als „offline, auf
  einem Datensatz", während drei Argumente der Vertiefung auf einer unglossierten **Online-Evaluierung**
  aufsitzen. Das ist ein **wellenweiter** Riss, der in die Evaluierungslektion hineinreicht — er gehört
  dorthin und nicht in einen lokalen Flicken.

---

### Phase 6 (2026-07-29) – Welle 2, Belegdurchgang vor der Prosa (RAG Teil II)
#### Eine Anweisung des Gates war falsch, und die Dateigrenze hat sie abgefangen

Gate 6.5 hat als Reparatur **O.29** verlangt, auf der Observability-Vertiefung von Teil I
`Werkzeugkatalog` durch `Tool-Katalog` zu ersetzen – gestützt auf eine Zählung: einmal
`Werkzeugkatalog` gegen zweimal `Tool-Katalog` im ausgelieferten Korpus. Der ausführende Agent hat die
Zeile **nicht angefasst**, weil der Pfad außerhalb seiner erlaubten Dateiliste lag, und den Fall gemeldet
statt ihn zu erledigen.

**Das war der Glücksfall, denn die Anweisung war sachlich falsch.** Der Satz lautet: „Um den
**Werkzeugkatalog** geht es hier ebenfalls nicht, der steht in [Teil III]" – und Teil III ist die Lektion
über das **Werkzeug-Ökosystem** (Ragas, DeepEval, LangSmith …). Das englische Original schreibt an genau
dieser Stelle „the tool catalogue, which is Part III". Gemeint ist der Katalog der **Produkte**, nicht der
Katalog der Tools, die ein Agent registriert hat. **Zwei Referenten, zwei Namen – korrekt so.** Die
Ersetzung hätte sie zu einem verschmolzen, also genau den Defekt erzeugt, gegen den dieser ganze Durchgang
gebaut ist.

**Die Lehre ist doppelt.** Erstens: **eine Zählung sieht Mengen, keine Referenten** – das ist dieselbe
eingebaute Grenze wie in Phase 5, hier aber mit umgekehrtem Vorzeichen. Dort hat das Zählen einen Defekt
gefunden, den Lesen übersehen hätte; hier hat es einen Defekt *erfunden*, den Lesen sofort ausräumt. **Wer
eine gezählte Abweichung repariert, muss den Satz gelesen haben.** Zweitens, und das ist die
Prozesslehre: **die Dateigrenze war als Sicherung gegen Scope-Creep gedacht und hat stattdessen einen
Inhaltsfehler abgefangen.** Eine Begrenzung, die den Ausführenden zum Melden statt zum Erledigen zwingt,
erzeugt genau den Moment, in dem die Anweisung noch einmal geprüft wird.


*Sechs Slices über die englischen Dateien unter `docs/part-2-agents/` (A Schleife und Steuerung ·
B Planung · C Gedächtnis und Zustand · D Multiagentensysteme und Graph · E MCP und Agentenprotokolle ·
F Tools, Sicherheit und Bewertung) – **und jeder Slice lief ZWEIMAL, unabhängig**. Zwölf Blätter, danach
**ein** Zusammenführungsdurchgang (Gate 6.5) über alle zwölf gleichzeitig. Kein Renderdurchgang, keine
Prosa. Das bindende Blatt ist `WAVE2-TERMS.md`: **226 Zeilen über rund 191 Kopfwörter**, davon **213
anwendbar** und **13 OPEN**; **null DISPUTED sind stehen geblieben**.*

#### Was das Doppeln gekauft hat – und was es nicht kaufen kann

**102 der 226 Zeilen tragen `AGREED ×2`**, also: beide Durchgänge eines Slices sind unabhängig zum selben
Ruling gekommen. Das ist die stärkste Evidenzklasse dieses Durchgangs und **es gibt sie nur, weil doppelt
gelaufen wurde**. **40 Zeilen sind RESOLVED** – dort haben die beiden Durchgänge einander widersprochen und
dieser Gate hat entschieden.

**Alle sechs Slices haben mindestens einen frontalen Widerspruch produziert; der Auftrag hatte mit drei
gerechnet.** Und sie lagen nicht gleichverteilt: **in vier von sechs Fällen traf der Widerspruch die
folgenreichste Zeile des Slices** – `trajectory` (55–60 Sätze), `reflection` (die zentrale Unterscheidung
der Lektion), `session` (querschnittig), `state machine` (der Rahmen der Graphlektion). Ein einzelner Lauf
hätte jedes Mal eine selbstsichere, ordentlich zitierte, **falsche** Zeile ausgeliefert.

Die drei frontalen Widersprüche, die dieser Eintrag namentlich festhält:

1. **`reflection` / `self-critique`.** Der eine Durchgang ⛔te *die Reflexion* (strukturelles Argument: der
   String ist im selben Kapitel ein Klasse-1-Eigenname) und setzte *die Selbstkritik*; der andere ⛔te *die
   Selbstkritik* (Registerargument: das DWDS-Wortprofil ist *schonungslos, harsch, zerknirscht*) und hielt
   *die Reflexion*. **Beide Argumente sind richtig und handeln von verschiedenen Dingen.** Entschieden,
   nicht gemittelt: die gemessene Eigenschaft des **deutschen Wortes** schlägt die HOUSE-Zeile ohne
   Domänenbeleg – und das strukturelle Problem wird durch die **Umbaulösung** des Verlierers gelöst, nicht
   durch sein Wort. Ergebnis: Begriff → **die Reflexion**; Framework → **`Reflexion`** in Codeschrift mit
   Apposition; der unterscheidende Merksatz wird **umgebaut, nicht übersetzt**; ⛔ *die Selbstkritik*.
2. **`trajectory`.** *der Pfad* gegen *der Verlauf*, beide gut belegt. Entschieden hat **keine Beleglage,
   sondern das Ledger**: `der Verlauf` ist in der **Nachbarlektion** bereits für die Gesprächshistorie
   ausgegeben – ein deutsches Wort für zwei englische Referenten auf benachbarten Seiten ist genau der
   Defekt, für den dieser Gate existiert. Dazu absorbiert `der Pfad` die Korpusüberschrift „Grading the
   whole **path**". **Keiner der beiden Durchgänge konnte das sehen; ein Batch sieht seine Nachbarn nicht.**
3. **`Multiagentensystem`.** Hier waren sich die beiden Durchgänge **uneinig darüber, ob es überhaupt einen
   Widerspruch gibt**: der eine las die Zeile als lebendigen Selbstwiderspruch, der andere wies nach, dass
   §1.3.3 die Hausform **namentlich** führt und die Zeile also stimmig ist. **Der zweite hat recht** – und
   trotzdem wird die Zeile geändert. **Denn dieselbe Zeile ist jetzt von zwei unabhängigen Prüfern als
   Widerspruch gelesen worden, und das ist ein Befund über die DARSTELLUNG der Tabelle, nicht über die
   Regel.** Repariert ist deshalb die **Terminus-Spalte**, nicht das Ruling; die Zitation von §1.3.3 bleibt
   stehen, ergänzt um die ehrliche Klarstellung, dass die Durchkopplung eine **Korpuskonsistenz-Entscheidung
   ist und keine Regelfolge** (§ 44 betrifft englische Wortgruppen, § 45(2) erlaubt sie bloß). Daraus die
   allgemeine Lesart, die über diese Zeile hinausgeht: **in einer §1.1-Zeile ist die Terminus-Spalte nicht
   das Ruling – das steht in der Beleg-Spalte, und wo beide auseinandergehen, ist die Spalte der Defekt.**

#### Der größte strukturelle Befund: das MCP-Register gab es nicht

`_language.md` §1.1 hatte **keine einzige** Zeile für `Server`, `Client`, `Host`, `Protokoll`, `Session`,
`Transport`, `SDK`, `Registry`, `Capability`, `Ressource`, `Primitiv`, `Agent Card`. Und die **acht
MCP-Termini, die `rag.md` §2 seit dem Bootstrap als settled kept-EN führt** – `stdio`, `Streamable HTTP`,
`SSE`, `A2A`, `Agent Card`, `Roots`, `Elicitation`, `MCP` –, hatten **ebenfalls keine Registerzeile**,
obwohl §2 mit eigenen Worten verlangt, dass ein Terminus **vor seinem zweiten Vorkommen** eine §1.1-Zeile
bekommt. **Die gesamte MCP-Oberfläche war unregistriert an dem Tag, an dem Teil II zu rendern begann.**

**Das ist Welle 1s teuerster Befund, eine Sektion weiter: „unangewandt, nicht unvollständig."** Die
Entscheidung existierte; die Anwendung fehlte. In Welle 1 war es eine Sense-Card, die seit dem Bootstrap die
Antwort hatte und die niemand aufschlug; hier ist es ein Ledger, das auf ein anderes Ledger zeigt.
**Die prozedurale Folgerung ist schärfer als die Wiederholung: ein Verweis von einem Register auf ein
anderes braucht eine Prüfung, dass der Verweis auflöst.** Ein Zeiger auf eine leere Zelle sieht genauso aus
wie ein Zeiger auf eine gefüllte.

Der Zuwachs, gezählt: **37 neue §1.1-Zeilen** (14 MCP · 7 Multiagenten/Graph · 7 Tools/Sicherheit/Bewertung ·
6 Gedächtnis/Zustand · 2 Planung · 1 Schleife) – **mehr als ein Drittel davon ist die eine fehlende
Oberfläche.**

#### Die Eingabe dieses Gates war defekt, auf zwei unabhängige Arten

**Und beide sahen aus wie ein sauberes Ergebnis.**

1. **Eine Regex, die jede Flexionsform ausschloss.** Das Term-Muster des Konkordanz-Extraktors trug ein
   abschließendes `(?![a-z])`, wodurch **jeder Plural und jede flektierte Form per Konstruktion verloren
   ging**. Gemessen: `primitive` stand mit **3 Sätzen**, der Quellbaum hat **22** – und **keiner der drei**
   trägt die MCP-Bedeutung, an der die Zeile hängt; `loop` stand mit **156** und ist **183**; `step` 70 →
   **103**; `budget` 43 → **55**; `checkpoint` 15 → **23**; `thread` 17 → **23**; `state` 59 → **62**.
2. **Fehlende Abschnitte.** Mehrere Termini der Auftragsblätter hatten in der Konkordanzdatei **überhaupt
   keinen Abschnitt**: `dry run` (der Korpus schreibt `dry-run`, und der Terminus steht **fettgedruckt auf
   einer ausgelieferten Seite**), `permission mode` (4 Vorkommen), `tool result` (11), `toolset` (17),
   `capstone` (13), `sensitive action` (6), `interpose` (4); ein anderer Slice vermisste sieben eigene
   (`checkpointing`, `short-term memory`, `parametric memory`, `compact`, `session`, `context window`,
   `summarise the history`); ein dritter neun (`agent loop`, `retrieval loop`, `turn`, `non-termination`,
   `iteration limit` u. a.).

**Ein abschneidender Extraktor erfindet Urteile; ein verengender erfindet ABWESENHEITEN – und das ist
schwerer zu sehen, weil nichts kaputt aussieht.** Ein zu kurzer Satz sieht kurz aus. Eine Zahl „156" und
eine Überschrift, die schlicht fehlt, sehen beide **richtig** aus. Welle 1 hatte den abschneidenden Fall
protokolliert; **er ist nicht behoben, er hat nur die Gestalt gewechselt.**

**Wer es unabhängig gefunden hat – und wer nicht:** Slice A fand die **abgeschnittenen Listen** selbst
(„14 von 156 gezeigt, `… (142 more)`") und leitete daraufhin jeden Referenten neu aus `docs/part-2-agents/`
ab; **die Regex fand A nicht** und sagt das ausdrücklich, weil eine plausible Zahl kein Signal gibt. Slice E
fand die **Regex** und die fehlenden Abschnitte (von 21 Konkordanzabschnitten waren zwei nachweislich
unvollständig, sieben Auftragstermini fehlten ganz). Slice F fand die **fehlenden Abschnitte** über einen
Gegengrep. Slice C bekam eine korrigierte Konkordanz und hat seinen Durchgang daraufhin **angehängt statt
eingearbeitet** – sichtbar, mit den bewegten Zählungen, nach derselben Regel, nach der dieses Register
streicht.

**Mehrere Rulings dieses Durchgangs existieren nur, weil ein Slice die Quelle selbst nachgegrept hat** –
`der Loop-Back-Kante`, `Event Loop`, `LoopAgent`, die `plain/opaque/free-running`-Varianten, `dry-run`, und
`die Komponente` für MCPs Primitive: Letzteres wäre an drei Sätzen entschieden worden, von denen **keiner**
den MCP-Referenten trägt. **Ein Gate ist nur so gut wie seine Eingabe, und die Eingabe ist Teil des Gates.**

#### Umkehrungen und Streichungen, jede einzeln benannt

- **`rag.md` §2, fünf Streichungen:** ~~`Scratchpad`~~ und ~~`Super-Step`~~ nach §3 als **OPEN** (beide
  standen kept-EN **ohne jeden Beleg** – dieselbe Gestalt wie ~~`Latency Budget`~~ in Welle 1);
  ~~`Extended Thinking`~~, ~~`Reasoning Effort`~~, ~~`Thinking Budget`~~ nach **Klasse 1**
  (Herstellerstellschrauben, keine Appellative).
- **`rag.md` §2, eine Aufspaltung:** ~~`Hooks, Callbacks, Permission Modes`~~ → Klasse 1
  (`Claude Code Hooks`, `ADK Callbacks`, `Permission Modes`) **plus** zwei appellative Klasse-2-Zeilen
  (*der Hook*, *der Callback*).
- **`rag.md` §2, eine Anmerkung statt einer Streichung:** `Soft Cap / Hard Cap` bleibt als **Zitierform des
  Musternamens**; der Laufterm ist **die weiche / die harte Obergrenze**.
- **Drei Kanonbegründungen sind falsifiziert worden, und in allen drei Fällen hat das Ruling überlebt und
  nur der Grund gewechselt.** (a) Die `Hook`-Zeile behauptete „das Lemma flektiert nie" – es flektiert
  **sechsmal**, Genitiv eingeschlossen, **in der Quelle, die die Zeile selbst zitiert**; die Zeile geht von
  WEAK auf **SETTLED**. (b) Die `Orchestrator`-Zeile behauptete, **kein** obliquer Kasus sei in einer
  Nicht-MT-Quelle belegt – Dativ und Akkusativ sind es jetzt; der Genitiv bleibt erschlossen, die Zeile
  bleibt ehrlich. (c) Der `Sampling`-Kasten in §1 stützte sich darauf, die MCP-Bedeutung fahre auf fremdem
  Beleg mit – sie tut es nicht mehr, und die befürchtete Falle existiert **morphologisch gar nicht**;
  Klasse 1 steht weiter, aber als **Disambiguierungs**entscheidung.
  **Das Muster ist die eigentliche Lehre: prüfe die BEGRÜNDUNG einer Zeile, bevor du ihre HEDGE erbst** –
  die Hedge ist das, was die nächste Welle daran hindert, die Zeile zu verbessern.
- **Zwei Bannzeilen wurden eingegrenzt statt umgekehrt:** `die Standardisierung` war für den statistischen
  Rahmen verboten und ohne Geltungsbereich formuliert (Teil II braucht das Wort in einer Lektionsüberschrift);
  die `Orchestrator`-Einschränkung war für den **Laufzeit**-Referenten der Tool-Use-Lektion geschrieben und
  hätte in Teil II „Ihre Anwendung zerlegt die Aufgabe" erzeugt, wo der Korpus einen **Agenten** meint.
- **Der Fallenkasten wächst von einundzwanzig auf siebenundzwanzig** (`Trajektorie`, `Transport`,
  `Supervisor`, `persistieren`, `Resümee`, `Step`), die Pflicht-Kollokations-Klasse um **siebzehn**, und
  **§1.1.g von achtzehn auf zweiundzwanzig** (*die Fähigkeit*, *das Transportprotokoll*, *die
  Vertrauensgrenze*, *der Bewerter / die Bewertungsfunktion*) – **in der Tabelle UND im Injektionsblock,
  Punkt 4, weil der die Zahl aufzählt und wörtlich in jeden Render-Prompt kopiert wird.**
  ⚠ **Die Zahlen wurden EINMAL berechnet, von diesem Gate, aus der Vereinigung aller zwölf Blätter.**
  Mehrere Batches haben ausdrücklich darauf verzichtet, Totale fortzuschreiben – und die Kollision ist
  **trotzdem** passiert, eine Etage tiefer: **zwei Batches meldeten unabhängig „den siebten Referenten" der
  `Bewertung`-Sense-Card.** Beide hatten recht, beide zusammen nicht; die Antwort ist **acht**.
  **Eine Zahl in Kanonprosa ist eine geteilte veränderliche Variable, auch wenn sie nicht wie eine Zählung
  aussieht.** „Sechs Referenten, sechs Namen" ist eine Zählung.
- **Zwei neue Fehlerklassen, beide ausdrücklich außerhalb der Zählung:** die **Registerfalle** (Definition
  richtig, Wortprofil falsch – `Alarmmüdigkeit`, `Selbstkritik`: mit zwei Mitgliedern ist es eine Klasse,
  keine Anekdote) und die **Eigennamen-Kollision** (`die Reflexion` gegen `Reflexion`). Letztere ist der
  interessanteste Befund der Welle: **die vier Fallen prüfen Lemma gegen Referent; keine prüft Appellativ
  gegen Eigennamen** – und keine Attestierung findet sie, nur das Lesen des Quellsatzes. Ihre Reparatur ist
  auch kein Wort, sondern ein **umgebauter Satz**, wofür ein Termledger keine Spalte hat.

#### Was dieser Durchgang NICHT konnte

- **Er sieht nur Widersprüche – und nach dem Doppeln trägt ein GETEILTER Irrtum die selbstsicherste
  Beschriftung auf dem Blatt.** Was beide Durchgänge eines Slices **gleich** falsch beurteilt haben, geht
  hier unbemerkt durch und heißt dann `AGREED ×2`. **102 der 226 Zeilen tragen dieses Etikett, und keine
  davon ist gegen irgendetwas anderes geprüft worden als gegen den zweiten Lauf.** Doppeln erhöht den Preis
  eines geteilten Irrtums; es beseitigt ihn nicht. **Der nächste Gate im Stapel darf `AGREED ×2` nicht als
  „geprüft" lesen.** Zwei Kandidaten zuerst, beide auf **je einer** deutschen Quelle: `das
  Arbeitsgedächtnis` im CS-Sinn und `der Subagent`.
- **Er kann eine Attestierung nicht prüfen.** Jede Zählung, jedes Zitat und jeder Nullbefund der zwölf
  Blätter ist auf Treu und Glauben übernommen. Die Blätter selbst berichten **fünf** Werkzeugfehler, die
  **wie ein Nullbefund aussehen**: Rate-Limit, Bezahlschranken-Anreißer, falsche Sprachfassung, fehlender
  Konkordanzabschnitt – und, der schlimmste, eine **Suchzusammenfassung, die einen plausiblen Satz zitiert,
  den es auf der Seite nicht gibt.** Ein Teil der Nullbefunde in der Vereinigung ist also mit Sicherheit
  keiner.
- **Er kann Natürlichkeit nicht beurteilen.** Nichts hiervon hat ein deutscher Muttersprachler gelesen; jede
  RESOLVED-Zeile ist eine Beleg- und Ledgerentscheidung, keine Ohrentscheidung. **Zuerst vor Gate 7
  gehören:** `die Teilaufgabe` (die knappste Entscheidung der Welle, gegen eine Domänenregistermessung),
  `die Reflexion` samt umgebautem Merksatz (ein Satz, kein Wort), `die Komponente` für MCPs Primitive (beide
  Durchgänge haben gemessen – und Verschiedenes gemessen), `der Pfad` in seiner Bindung (eine gebundene
  Fügung muss Wiederholung überstehen) und `die weiche / die harte Obergrenze`.
- **Drei Dinge sind bewusst nicht entschieden worden.** (a) **`control layer`** steht **OPEN**, weil
  `die Steuerungsschicht` bereits an *orchestration layer* vergeben ist; **ob ein deutsches Wort zwei
  englische Termini tragen darf, ist eine Kanonpolitikfrage** und gehört zu §3, nicht zu einer Termzeile.
  (b) `die API` (Genus) und die Formwahl bei `Least Privilege` bleiben **DISPUTED mit gehaltenem
  Incumbenten** und werden nicht neu aufgerollt. (c) Die **Defekte der englischen Quelle** – zehn bestätigte
  plus sieben im Nachtrag, darunter `call` mit drei Objekten und `capability` mit fünf – **sind keine
  Termentscheidungen und wurden nicht als solche behandelt**; die Reparatur gehört nach EN und von dort in
  alle vier Locales (§8 §M).
- **Eine Messung konnte nicht abgeschlossen werden.** Mehrere Blätter melden Zählungen, die sie wegen
  Rate-Limit oder Bezahlschranke nicht nehmen konnten (`mehrschrittig`, `Handlungsspielraum`,
  `Rückwärtskante`, `Kontextüberlastung`). Sie stehen im bindenden Blatt als **NICHT GEMESSEN**, nie als
  Null. **Ein späterer Durchgang soll sie nehmen, nicht erben.**
