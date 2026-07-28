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

---

## §3 Terms still OPEN — not settled, do not present as canon

These need either an attestation or a cold read before they become rules. **Until then: avoid the word or
paraphrase.** Writing a plausible-sounding German form here is exactly the failure the Slovak locale hit with
„súbeh" — a coinage that passed one reviewer and was later struck as semantically wrong.

| Terminus | Warum offen | Vorläufige Behandlung |
|---|---|---|
| **Guardrail (Singular)** | kein stabiler deutscher Singularusus für den KI-Sinn belegbar | nur im Plural *Guardrails* verwenden; Singular umformulieren |
| **Retrieval (Genus)** | kein artikelführender Beleg gefunden; de.wikipedia führt *Information Retrieval* ohne Artikel | Hausform *das Retrieval* (`_language.md` §1.1) — als HOUSE, nicht als Norm zitieren |
| **Embedding (Genus)** | Beleglage entscheidet nicht (*zum Embedding* schließt nur Femininum aus) | Hausform *das Embedding*; Plural *die Embeddings* ist belegt |
| **Chunk (Genus)** | nur der Plural *die Chunks* ist belegt | Hausform *der Chunk* |
| **Log (IT-Sinn)** | der Wörterbucheintrag ist der **seemännische** (*das Log*, Plural **„Loge"**) — als Beleg für den IT-Sinn **unbrauchbar** | *die Logs*, *die Logdatei*, *das Protokoll* verwenden; den DWDS-Eintrag **nicht** als Beleg zitieren |
| **Queue (IT-Sinn)** | Wörterbuch kennt nur Billardstock und (veraltet) Warteschlange von Personen | Hausform *die Queue*; wo möglich *die Warteschlange* |
| **Gate (IT-Sinn)** | Wörterbuchgenus *das Gate* betrifft den Flughafen-Sinn | nur im festen Kompositum: **das Quality Gate**, **das Release Gate** |
| ~~Tool Call / Tool Result — Schreibung~~ | **GESCHLOSSEN im Bootstrap.** Amtliches Regelwerk § 45 E1 entscheidet: Substantiv+Substantiv aus dem Englischen wird **zusammen oder mit Bindestrich** geschrieben, getrennt ist nicht normgerecht | **der Tool-Call, das Tool-Result, die Prompt-Injection** — siehe `_language.md` §1.3.3. Die in der Fachpresse verbreitete Getrenntschreibung ist genau die vom Regelwerk als „im Deutschen nicht normgerechte Getrenntschreibung" bezeichnete |
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

## §5 Repeated exact strings

Empty at bootstrap. Recurring block strings (admonition headings, the "What you take away" section title,
video-caption wording, part-opener boilerplate) are settled the first time a German page needs them and are
recorded here verbatim so they never drift.
