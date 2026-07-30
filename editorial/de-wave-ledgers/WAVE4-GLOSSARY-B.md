# WAVE4-GLOSSARY-B.md — the binding term-direction mapping for the German glossary, slice B

**Issue #283, reconciliation pass, slice B: the LAST NINE sections of `docs/glossary.md`** —
`\{#multi-agent}` through `\{#llmops}`, **141 bold headwords**. Slice A (a peer agent) holds the first ten.

**This sheet is not a translation.** It is the mapping the rendering agents obey: per headword, the class,
the German headword form, its grammatical information, the evidence, and the evidence class. Where the
evidence does not decide, the row says `none` and lands in the flag list (§11). **An unfilled cell is a
finding, not a failure.**

**The rule that governs every row (project canon, #328): where the canon is silent or disagrees with the
shipped corpus, the SHIPPED CORPUS wins, and its evidence class is `corpus precedent`, not `attestation`.**
Seven rows below overrule a canon line on exactly that ground and say so (§11.3).

**Nothing else was written, edited, staged or committed.** No git command was run.

---

## 0. Scope correction, read this first

The brief says "the last 10 sections". `docs/glossary.md` has **19** sections, not 20:

```
$ grep -n '^## ' docs/glossary.md | wc -l
19
```

The first ten (`ingestion-chunking` … `planning-loops`) are slice A's. **Mine are the remaining NINE**
(`multi-agent`, `orchestration-frameworks`, `mcp`, `real-agents`, `production-failures`, `serving`,
`cloud-platforms`, `tooling-ecosystem`, `llmops`). The nine heading lines are at 565, 608, 650, 711, 738,
792, 900, 979, 996 — which is what the brief actually enumerated. **10 + 9 = 19, so nothing is unowned**;
the count in the brief's prose is off by one, the line list is right. Recorded because the next wave will
read the prose, not the line numbers.

---

## 1. Method and the two instruments that would have misled me

### 1.1 The counting command

Every count in this sheet comes from this, run at the repo root:

```bash
DE=i18n/de/docusaurus-plugin-content-docs/current

# occurrences in RUNNING GERMAN PROSE (footer lines excluded, see §1.2)
grep -rhI --include='*.md' -- '<PAT>' $DE | grep -v '\[Neue Begriffe\]' \
  | grep -o -- '<PAT>' | wc -l

# the files
grep -rlI --include='*.md' -- '<PAT>' $DE
```

Notation in the evidence cells: **`KORPUS(n / f)`** = n occurrences in running German prose across f files.
Inline-code spans (`` `StateGraph` ``) are counted separately and marked `Codeschrift`.

I did **not** trust `scripts/locale-review/concord.py`. The brief warns it once undercounted every
concordance by missing stem-changing inflections (`cache` 35→66); I therefore grepped **stems**, not full
words (`Übergabe` not `Übergaben`, `Parallelität` not `Datenparallelität`), and cross-checked every
non-trivial ruling against a printed context window rather than a number. Two rulings changed as a direct
result: `Daten-Parallelität` (a full-word grep on `Datenparallel` returns **0**; the corpus writes
`Daten-Parallelität`) and `semantischer Cache` (a full-word grep returns **0**; the corpus writes
„einem **semantischen** Cache").

### 1.2 ⚠ The instrument that WOULD have misled me — the `[Neue Begriffe]` footers

**Every lesson page ends with an English, lowercase term list.** Example, `part-2-agents/multi-agent/deep-dive.md:124`:

```
**[Neue Begriffe](../../glossary.md#multi-agent)**: FIPA ACL, contract net protocol, blackboard,
A2A (Agent2Agent), multi-agent debate, trajectory stitching.
```

A case-insensitive grep for an English loan therefore returns hits that are **not German prose**. Three
headwords in my slice were saved only by this exclusion:

| Loan | naive `grep -roi` | in German prose | what the corpus actually writes |
|---|---:|---:|---|
| `handoff` | 2 | **0** (1 is the code identifier `handoff()`) | **die Übergabe** (28) |
| `sub-agent` | 1 | **0** | **der Subagent** (11) |
| `trajectory` | 2 | **0** | no noun at all — a construction |

WAVE3-TERMS §6 records this carve-out for the two `tooling-ecosystem` pages only. **It is corpus-wide**
(`grep -c 'Neue Begriffe' $DE -r` hits every lesson page), and the failure mode is the inverse of the one
the ledger names: *a non-zero on the loan that is not a non-zero in prose*. See Lessons.

### 1.3 Class notation

`1` = identifier / product name (English, code-styled or as a proper name, never inflected) · `2` = kept-EN
loan with a German article, headword leads English with a German gloss · `3` = German-led, headword leads
German with the English original alongside · `4` = fully German, no English needed.

---

## 2. `## Agents – Multi-Agenten-Systeme` \{#multi-agent} — 11 headwords

| EN headword | Cl. | German headword form | Artikel / Plural / Genitiv | Evidence | Ev. class |
|---|---|---|---|---|---|
| **Multi-agent system** | 3 | **das Multi-Agenten-System** | das / die Multi-Agenten-Systeme / des Multi-Agenten-Systems | KORPUS(39 / 13) — the single most cross-cutting term of the section; shipped page `title: Multi-Agenten-Systeme`; `Multiagenten…` 0 · canon `_language.md` §1.1.c row (identical) | corpus precedent + canon |
| **Orchestrator / supervisor** | 2 | **der Orchestrator / der Supervisor** | Orchestrator: der / die Orchestratoren / des Orchestrators · Supervisor: der / die Supervisors / des Supervisors | KORPUS Orchestrator(43 / 6), case-marked („der Span **des Orchestrators**", „**Orchestratoren** über **Orchestratoren**") · Supervisor(5 / 3), always as the alias („in vielen Frameworks auch **Supervisor** genannt") · canon §1.1.c both rows | corpus precedent + canon |
| **Worker / sub-agent** | 2 | **der Worker / der Subagent** | Worker: der / die Worker (Nullplural), Dat. Pl. **den Workern** / des Workers · Subagent: der / **die Subagenten** / **des Subagenten** (n-Deklination) | KORPUS Worker(71 / 8) · Subagent(11 / 4), case-marked („für jeden Aufruf **eines Subagenten**") · canon §1.1.c · WAVE3 W3-5 upgrades `Worker` genitive/dative to SHIPPED | corpus precedent + canon + ledger |
| **Handoff** | 3 | **die Übergabe** | die / die Übergaben / der Übergabe | KORPUS(28 / 8) („Arbeit durch **die Übergabe** an…", „Ein Worker liest **eine Übergabe** falsch") · `Handoff` **0** in prose · **canon `_language.md` §1.1.c says `Handoff` = OPEN** | **corpus precedent — canon is silent, the corpus decides** |
| **Agent chain** | 3 | **die Kette (sequenziell)** | die / die Ketten / der Kette | KORPUS — the bold named form „**Die Kette (sequenziell).**" (H3, `multi-agent/i`), „das Team als … als **Kette**", „**die Kette** (jeder Agent verarbeitet die vorherige Ausgabe weiter)" · `Agentenkette` 0 | corpus precedent |
| **Critic / debate** | 3 | **der Kritiker-Agent / die Debatte** | Kritiker-Agent: der / die -en / des -en · Debatte: die / die Debatten / der Debatte | KORPUS Kritiker(2 / 1) („ein **Kritiker-Agent** hält dagegen") · Debatte(9 / 2), bold H3 „**Die Debatte zwischen Agenten.**" · `Critic` 0 in prose | corpus precedent |
| **FIPA ACL** | 1 | **FIPA ACL**, unverändert | artikellos, unflektiert | KORPUS(5 / 1) („**FIPA** – die Foundation for Intelligent Physical Agents", „**FIPA ACL** hat diese Teile schon 2002 benannt") | corpus precedent |
| **Contract net protocol** | 2 | **das Contract Net**; ausgeschrieben **das Contract-Net-Protokoll** | das / – / des Contract Net | KORPUS(5 / 1) („**Das Contract Net** (Reid G. Smith …)", „**Das Contract Net** von weiter oben") · `Kontraktnetz` 0 · canon §1.1.c row (identical, incl. the compound) | corpus precedent + canon |
| **Blackboard** | 2 | **das Blackboard** | das / die Blackboards / des Blackboards | KORPUS(16 / 2), case-marked in three cases („eben **dem** Blackboard", „zum gemeinsam**en** Blackboard", „**Das** Blackboard zieht Ballast an") · canon §1.1.c | corpus precedent + canon |
| **Multi-agent debate** | 3 | **die Multi-Agenten-Debatte** | die / die -n / der -Debatte | KORPUS („Bei der **Multi-Agenten-Debatte** schlagen mehrere Instanzen desselben Modells…", „die **Multi-Agenten-Debatte** kaufen Qualität"; `Debatten-Topologie` 1) | corpus precedent |
| **Trajectory stitching** | — | **KEIN deutscher Terminus. Konstruktion:** „**die Kennung des Gesprächs oder der Aufgabe** durch jede Nachricht ziehen, sodass sich die Spans zu **einem** Eltern-Kind-Trace zusammensetzen" | — (no noun) | `Trajectory` / `Trajektorie` **0** in prose (both loan hits are the English footer) · `Korrelations-ID`, `Korrelationskennung` 0 · the referent IS present — „eine gemeinsame Kennung: **die Kennung des Gesprächs oder der Aufgabe**" (2), „der Span des Orchestrators als Elternknoten, der Span jedes Workers darunter" · no ledger row, no canon row | **none → §11.2** |

⚠ **`die Tafel` (2, `multi-agent/d`) is the IMAGE, not the term** — „Stellen Sie sich ein Team vor einer
echten **Tafel** vor". The term is `das Blackboard`. Do not promote the picture to a headword.

---

## 3. `## Agents – Orchestrierungs-Frameworks` \{#orchestration-frameworks} — 13 headwords

| EN headword | Cl. | German headword form | Artikel / Plural / Genitiv | Evidence | Ev. class |
|---|---|---|---|---|---|
| **Orchestration framework** | 2 | **das Orchestrierungs-Framework** | das / die Orchestrierungs-Frameworks / des Orchestrierungs-Frameworks | KORPUS(13 / 8), shipped page `title: Orchestrierungs-Frameworks`; „Sie greifen zu **einem Orchestrierungs-Framework**" · `Orchestrierungsframework` (closed) 0 · head noun canon §1.1.a `das Framework` | corpus precedent + canon |
| **Agent as a graph / state machine** | 3 | **der Agent als Graph, als Zustandsautomat** | Zustandsautomat: der / die Zustandsautomaten / des Zustandsautomaten (n-Deklination) | KORPUS(6 / 2), case-marked („Machen Sie **einen Zustandsautomaten** daraus", „Für **den Zustandsautomaten** aus dem vorigen…") · `Zustandsmaschine` 0 · H2 „der Agent als Graph, als Zustandsautomat" | corpus precedent |
| **Node / edge** | 4 | **der Knoten / die Kante** | Knoten: der / die Knoten / des Knotens · Kante: die / die Kanten / der Kante | KORPUS Knoten(61 / 7), Kante(22 / 3) („Aus den Schritten werden **Knoten**", „einfache Kanten und bedingte Kanten") | corpus precedent |
| **Checkpointing** | 2 | **Checkpointing**, artikellos oder im Kompositum | **kein Artikel erfinden** | KORPUS(3 / 2), **all three article-less** („Persistenz und **Checkpointing**", „Tracing, Streaming und **Checkpointing**") · canon §1.1.d row says exactly „artikellos oder im Kompositum" | corpus precedent + canon |
| **State graph (StateGraph)** | 1 | **`StateGraph`**, Codeschrift, unverändert | artikellos | KORPUS: 2 tokens, **both in code spans** („modelliert einen Agenten als `StateGraph`") · `Zustandsgraph` 0 | corpus precedent |
| **Conditional edge** | 3 | **die bedingte Kante** | die / die bedingten Kanten / der bedingten Kante | KORPUS(4 / 1) („einfache Kanten und **bedingte Kanten**, die anhand des Zustands…") | corpus precedent |
| **Checkpointer** | 2 | **der Checkpointer** | der / die Checkpointer (Nullplural) / **des Checkpointers** | KORPUS(12 / 2), case-marked („der Zustand **des Checkpointers**", „**keinen** Checkpointer") · canon §1.1.d | corpus precedent + canon |
| **Checkpoint backend** | 2 | **das Checkpoint-Backend** | das / die Checkpoint-Backends / des Checkpoint-Backends | KORPUS („was Durable Execution und **die Checkpoint-Backends** darunter wirklich sind" 2; „**kein** Backend für Dauerhaftigkeit") · canon §1.1.d | corpus precedent + canon |
| **Thread (thread_id)** | 2 | **der Thread**; die Kennung **`thread_id`** (Klasse 1) | der / die Threads / des Thread[s] | KORPUS(18 / 4), case-marked („was **ein Thread** ist", „innerhalb **eines einzelnen Threads**", „die **keinen** Thread teilen") · canon §1.1.a · ⚠ W3-5 downgrades the canon's Duden citation to **SETTLED (Paradigma) / WEAK (Referent)** — the paradigm holds, the IT sense is not in Duden | corpus precedent + canon (referent WEAK) |
| **Durable execution** | 2 | **Durable Execution**, artikellos; **Pflichtglosse bei Erstnennung**: „(dauerhafte Ausführung – ein Durchlauf setzt nach einem Absturz beim letzten gesicherten Schritt fort)" | **kein Artikel** | KORPUS(7 / 2) incl. `sidebar_label: "Graphen und Durable Execution"`; the gloss ships verbatim at `orchestration-frameworks/d` · canon §1.1.d „artikellos" | corpus precedent + canon |
| **Framework long-term memory / store** | 2 | **der Store**, **Pflichtglosse** „(Langzeitspeicher des Frameworks)" | der / die Stores / des Stores | KORPUS(7 / 1), case-marked („nennt LangGraph **den Store**", „zu **einem** thread-übergreifenden **Store**", „**keinen** Store") · canon §1.1.d · rag.md §2 gloss table carries **the identical string** — and it ships | corpus precedent + canon |
| **Declarative vs imperative agent definition** | 3 | **deklarative gegen imperative Agentendefinition**; Adjektive **deklarativ / imperativ** | – (adjectives) | KORPUS: the take-away writes „**deklarative gegen imperative Agentendefinition**" verbatim; `deklarativ*`(10 / 2), `imperativ*`(9 / 2), bold H3s „**Imperativ** heißt…", „**Deklarativ** heißt…" | corpus precedent |
| **Human-in-the-loop (HITL)** | 2 | **der Human-in-the-Loop (HITL)** | **der** / – / des Human-in-the-Loop | KORPUS(12 / 7), **article-bearing masculine in four independent files**: „Darüber sitzt **der Human-in-the-Loop (HITL)**" (of/i), „**der** Human-in-the-Loop" (tool-use/d, mcp/d, planning-loops/d), „einen Human-in-the-Loop" (of/d) · **canon has NO §1.1 row** — only the §1.3.3 Durchkopplung list (`:1724`) | **corpus precedent — canon has no gender, the corpus supplies it** |

---

## 4. `## Agents – MCP und Agentenprotokolle` \{#mcp} — 18 headwords

| EN headword | Cl. | German headword form | Artikel / Plural / Genitiv | Evidence | Ev. class |
|---|---|---|---|---|---|
| **MCP (Model Context Protocol)** | 2 | **MCP**; ausgeschrieben **das Model Context Protocol** | das MCP / – / des MCP | canon §1.1.c row (identical) · KORPUS: `MCP` is everywhere, almost always as a compound former (`MCP-Server`, `MCP-Client`, `MCP-Registry`) | canon + corpus precedent |
| **MCP server** | 2 | **der MCP-Server** | der / die MCP-Server (Nullplural) / des MCP-Servers | KORPUS(20 / 5) — the highest-frequency `MCP-` compound · canon §1.1.c `Server` row prescribes „Erstnennung **der MCP-Server**" | corpus precedent + canon |
| **MCP client** | 2 | **der MCP-Client** | der / die MCP-Clients / des MCP-Clients | KORPUS(9 / 3) · canon §1.1.c `Client` | corpus precedent + canon |
| **MCP resources** | 2 | **die MCP-Ressourcen** (Pl.); Laufterm **die Ressourcen** | die (Pl.) / — / der Ressourcen | KORPUS `Ressource*`(25 / 6) — running prose uses the **bare** German plural („**Tools**, **Ressourcen** und **Prompts**"). `MCP-Ressourcen` itself **0** | corpus precedent for the head noun; **the `MCP-` compound is unattested → §11.2** |
| **MCP prompts** | 2 | **die MCP-Prompts** (Pl.); Laufterm **die Prompts** | die (Pl.) / — / der Prompts | KORPUS bare `Prompts` in the triad, `MCP-Prompts` **0** · canon §1.1.a `der Prompt` | corpus precedent for the head noun; **the `MCP-` compound is unattested → §11.2** |
| **M×N integration problem** | 3 | **das M×N-Integrationsproblem** | das / – / des M×N-Integrationsproblems | KORPUS(3 `M×N` + 4 `Integrationsproblem` / 2) — „Das ist **das M×N-Integrationsproblem**" (bold, `mcp/i`). ⚠ Keep the **multiplication sign U+00D7**, not `x` | corpus precedent |
| **A2A (Agent2Agent)** | 2 | **A2A**, artikellos; **das A2A-Protokoll** | bare A2A artikellos · das A2A-Protokoll / – / des A2A-Protokolls | KORPUS `A2A`(25 / 7), `Agent2Agent`(2 / 2) · canon §1.1.c row (identical) | corpus precedent + canon |
| **MCP host** | 2 | **der MCP-Host**; Laufterm **der Host** | der / die Hosts / des Hosts | KORPUS: **`MCP-Host` 0**; the bare **`der Host`** is the delivered form and is fully case-marked („**Der Host** ist die LLM-Anwendung", „innerhalb **des Hosts**", „**Ein Host** hält mehrere Clients") · canon §1.1.c `der Host` with Pflichtglosse | corpus precedent for `der Host`; **the `MCP-` compound is unattested → §11.2** |
| **Capability negotiation** | 3 | **die Aushandlung der Fähigkeiten** | die / – / der Aushandlung | KORPUS: „das SDK übernimmt … **die Aushandlung der Fähigkeiten**" (verbatim), „der Version und **Fähigkeiten** über JSON-RPC 2.0 **aushandelt**", „ihre Protokollversion und ihre **Fähigkeiten** aus[tauschen]" · `Fähigkeitsaushandlung` 0 · `Capability` **0** — ⛔ per `_language.md` §1.1.g (`die Fähigkeit`, nicht `die Capability`) | corpus precedent + canon §1.1.g |
| **Roots** | 1 | **Roots**, artikellos, unflektiert | – | KORPUS(5 / 1) · canon §1.1.c „artikellos, unflektiert" | corpus precedent + canon |
| **Sampling** | 1 | **Sampling** (die MCP-Fähigkeit) — Klasse 1 als **Disambiguierungs**entscheidung | das Sampling / die Samplings / des Samplings | KORPUS(41 / 8), of which **10 are the MCP referent** (`mcp/d`) and 19 the statistical Observability sense (`observability/d`) · canon `rag.md` §1 box: class 1 for the MCP primitive, the Observability appellative stays class 2 §1.1.e | corpus precedent + canon |
| **Elicitation** | 1 | **Elicitation**, artikellos, unflektiert | – | KORPUS(7 / 2) · canon §1.1.c „artikellos, unflektiert" | corpus precedent + canon |
| **Streamable HTTP** | 2 | **Streamable HTTP**, artikellos („über Streamable HTTP") | **kein Artikel** | KORPUS(11 / 3), all article-less · canon §1.1.c „artikellos" | corpus precedent + canon |
| **MCP registry** | 2 | **die MCP-Registry** | **die** / die Registries / der Registry | KORPUS `MCP-Registry`(2 / 1) + bare `Registry`(10 / 4), feminine and case-marked („über **eine** Registry", „In **einer** Registry gelistet zu sein") · canon §1.1.c `die Registry` · W3-28 upgrades it to corpus-attested | corpus precedent + canon + ledger |
| **Server discovery** | — | **KEIN deutscher Terminus. Konstruktion:** H2 „**Einen Server zu finden heißt nicht, ihm zu vertrauen**"; auf Ökosystemebene „**findet ein Client über eine Registry heraus, welche Server es überhaupt gibt**"; beim Verbindungsaufbau „**findet ein Client die Fähigkeiten eines bestimmten Servers über den Handshake**" | — (no noun) | `Serverfindung`, `Serversuche`, `Server-Findung`, `Entdeckung` **all 0** · ⚠ **`Discovery` occurs once and it is the WRONG referent** — „mit **der Discovery über OpenID Connect**" (OIDC discovery, `mcp/d`). A loan count of 1 here is a measurement of a different word | **none → §11.2**; ⚠ wrong-referent trap recorded |
| **Tool poisoning** | 2 | **das Tool-Poisoning** | das / kein Plural / des Tool-Poisonings | KORPUS(7 / 4) · canon §1.1.c | corpus precedent + canon |
| **Rug pull** | 2 | **der Rug-Pull** (durchgekoppelt), Pflichtglosse „(Austausch eines Tools nach der Freigabe)" | der / die Rug-Pulls / des Rug-Pulls | KORPUS **hyphenated 4 (`mcp/d`) : spaced 2 (`guardrails/d`)** — „**Der Rug-Pull** (Austausch eines Tools nach der Freigabe)" ships the canon gloss verbatim · canon §1.1.c `der Rug-Pull` + §1.3.3 (Subst.+Subst. → Bindestrich) | corpus precedent (majority) + canon; **shipped inconsistency → §11.1** |
| **Confused deputy** | 2 | **der Confused Deputy**, Pflichtglosse „(getäuschter Stellvertreter – eine privilegierte Komponente wird zum Missbrauch ihrer **eigenen** Rechte verleitet)" | der / die Confused Deputies / des Confused Deputy | KORPUS(5 / 2) + `getäuschter Stellvertreter`(2 / 2) · canon §1.1.c + rag.md §2 gloss table (aligned to the shipped page in wave 2) | corpus precedent + canon |

---

## 5. `## Agents – echte Agenten (Abschluss dieses Teils)` \{#real-agents} — 7 headwords

**All seven are class 1 vendor dials.** `rag.md` §2 struck `Extended Thinking`, `Reasoning Effort` and
`Thinking Budget` from the kept-EN list into class 1 in wave 2 (de.wikipedia attestation 0 : 0 : 0), and split
`Hooks / Callbacks / Permission Modes` into class 1 (branded) + class 2 (appellative). The corpus obeys.

| EN headword | Cl. | German headword form | Artikel | Evidence | Ev. class |
|---|---|---|---|---|---|
| **Extended thinking** | 1 | **Extended Thinking** / `thinking`-Blöcke, artikellos, Codeschrift für den Parameter | artikellos | KORPUS: `Extended Thinking` **0**, `erweitertes Denken` **0**; the page renders the referent as `thinking`-Blöcke (2 code tokens, `real-agents`) and appellatively as **das Nachdenken**(11 / 1 in `real-agents`) · canon §1.1.d „artikellos, Codeschrift" | canon + corpus precedent (referent) |
| **Interleaved thinking** | 1 | **Interleaved Thinking**, artikellos; appellativ **das Nachdenken zwischen den Tool-Calls** | artikellos | KORPUS: `Interleaved Thinking` **0**; `verschränkt*`(9 / 4) is the corpus's adjective for *interleaved* (also used for chunked prefill in `serving/d`) · no ledger row, no canon row for this exact term | **thin: canon+ledger silent, only the adjective is corpus-attested → §11.2** |
| **Reasoning effort** | 1 | **`reasoning.effort`**, Codeschrift, artikellos; appellativ „**wie viel Nachdenken** eine Aufgabe bekommen darf" | artikellos | KORPUS: `Reasoning Effort` **0**, `Denkaufwand` **0**; `Reasoning`(13 / 10) only as a compound former · canon §1.1.d „artikellos, Codeschrift"; `rag.md` §2 wave-2 strike | canon + corpus precedent |
| **Thinking budget** | 1 | **`thinkingBudget`**, Codeschrift; wo ein Artikel erzwungen ist **das Thinking-Budget** | das (nur im Kompositum) | KORPUS: `Thinking-Budget` **0**, `Denkbudget` **0** (⛔ per `rag.md` §2 — the `Latenzbudget` coinage failure a second time) · canon §1.1.d row | canon; **corpus has zero → §11.2** |
| **Claude Code hooks** | 1 | **Claude Code Hooks**; appellativ **der Hook** | Claude Code Hooks artikellos · der Hook / die Hooks / des Hooks | KORPUS `Hooks`(12 / 4) + 2 code tokens; `Claude Code Hooks` as a full string **0** · canon §1.1.c `der Hook` (SETTLED after wave 2 falsified the „flektiert nie" claim) | canon + corpus precedent (appellative) |
| **ADK callbacks** | 1 | **ADK-Callbacks** (durchgekoppelt); appellativ **der Callback** | ADK-Callbacks Pl. · der Callback / die Callbacks / des Callbacks | KORPUS `ADK-Callbacks`(3 / 1) — **hyphenated as delivered** · `Callback*`(6 / 1) · canon §1.1.c `der Callback` | corpus precedent + canon |
| **Permission modes** | 1 | **Permission Modes**, nur Plural, artikellos; den Wert nennen: „der Modus `plan`" | nur Plural; **keinen Singular erfinden** | KORPUS(3 / 1) · canon §1.1.c „nur Plural, artikellos"; `rag.md` §2 wave-2 split | corpus precedent + canon |

---

## 6. `## Production – warum KI-Systeme im Produktivbetrieb versagen` \{#production-failures} — 14 headwords

**The whole page is the authority and it is a single file** (`part-3-production/production-failures.md`, 412
lines). It is also the section where the German is most heavily **construction-led**: five of the fourteen
referents have no German noun at all, and that is the delivered decision, not a gap in the render.

| EN headword | Cl. | German headword form | Artikel / Plural / Genitiv | Evidence | Ev. class |
|---|---|---|---|---|---|
| **Score floor / relevance floor** | 3 | **die Score-Untergrenze** / **die Untergrenze für die Relevanz** | die / die -n / der -grenze | KORPUS `Score-Untergrenze`(3 / 1) incl. a Mermaid/InfoCard label and the bold rule „**Setzen Sie eine Score-Untergrenze hinter der Stufe an, deren Scores etwas bedeuten.**"; `Untergrenze`(8 / 2); the InfoCard caption writes „Eine **Untergrenze für die Relevanz** hinter dem Reranking" · WAVE3 §2 `floor` → die Untergrenze, §8 D-2 | corpus precedent + ledger |
| **Ingestion manifest** | 2/3 | **das Ingestion-Manifest**; Laufterm **das Manifest** | **das** (⚠ nicht korpusbelegt) / die Manifeste / des Manifest[e]s | KORPUS `Ingestion-Manifest`(1 / 1, an InfoCard label) + bare `Manifest`(2 / 1) — but **every token is article-less or nominative** („sondern ein **Manifest**"), so the corpus does **not** decide the gender · no ledger row, no canon row | **corpus precedent for the WORD, `none` for the GENUS → §11.2** |
| **Blind spot (ingestion)** | 4 | **der blinde Fleck**, meist Plural **die blinden Flecken** | der / die blinden Flecken / des blinden Flecks | KORPUS(2 in `production-failures` + 1 in `evaluation/d`) („wo ihre *blinden Flecken* liegen", „und die **blinden Flecken**") | corpus precedent |
| **Frozen regression set** | 3 | **der eingefrorene Regressionsdatensatz**; anaphorisch **ein eingefrorener Datensatz** | der / die -sätze / des -satzes | KORPUS: „Ein **eingefrorener Regressionsdatensatz** beantwortet die Frage…" (bold, verbatim) + „dafür ist ein **eingefrorener Datensatz** da" + take-away „ein **eingefrorener** für die Regressionen" · ⚠ WAVE3 §0 notes the ban rule `einfrieren` was **narrowed** because it was too wide — the participle is licensed, the bare verb is not | corpus precedent + ledger |
| **Rotating live-sampled set** | 3 | **der wechselnde Datensatz aus dem laufenden Verkehr** | der / die -sätze / des -satzes | KORPUS verbatim: „Ein **wechselnder Datensatz aus dem laufenden Verkehr** beantwortet die Frage…" (bold) + take-away „ein **wechselnder** aus dem laufenden Verkehr" · ⛔ `rotierend` **0** · `der Verkehr` per X-7 (`Traffic` 0 as a running term) | corpus precedent + ledger |
| **Benchmark familiarity** | 3 | **die Vertrautheit mit dem Maßstab** | die / – / der Vertrautheit | KORPUS verbatim, bold: „misst irgendwann nicht mehr die Qualität, sondern die **Vertrautheit mit dem Maßstab** selbst" · ⚠ **the corpus renders *benchmark* as `der Maßstab`(18 / 7), not as `Benchmark`(5 / 4)** — do not reintroduce the loan in this headword | corpus precedent |
| **Audit-grade logging** | 3 | **die Protokollierung für ein Audit** | die / die -en / der Protokollierung | KORPUS: „ob Sie jemandem eine **Protokollierung für ein Audit** schulden" (take-away), „Eine **Protokollierung**, die auf die Fehlersuche zugeschnitten ist, ist keine Protokollierung, die auf den Nachweis zugeschnitten ist", `Audit`(5 / 2) · ⛔ `Prüfpfad` (canon §1.1.f: a VAT-law term) · ⛔ `revisionssicher` **0** | corpus precedent + canon |
| **Cost per accepted answer** | 3 | **die Kosten für eine angenommene Antwort** | die Kosten (Pluraletantum) / — / der Kosten | KORPUS verbatim as an H2 („**Die Einheit sind die Kosten für eine angenommene Antwort**") + bold in prose + take-away · canon §1.1.a `die Kosten` Pluraletantum, ⛔ a numeral immediately before it | corpus precedent + canon |
| **Retry tax** | 3 | **die Mehrkosten der Wiederholungen** | die (Pl.) / — / der Mehrkosten | KORPUS(2 / 1) bold („diesen Abstand fressen die **Mehrkosten der Wiederholungen**") · **⚠ the English survives inside the image `alt` text**: „der Abstand ist als **retry tax** beschriftet, also als Mehrkosten der Wiederholungen" — a bound bilingual gloss, not a regression · ⛔ `die Retry-Steuer` (W3-15) | corpus precedent + ledger |
| **Drift response ladder** | — | **KEIN deutscher Terminus. Konstruktion (Reihenfolge als Satz):** H2 „**Indexieren Sie neu, bevor Sie neu trainieren**"; „fangen Sie weit unterhalb des Modells an: **neu indexieren und neu in Chunks aufteilen, die Mischung der Suchverfahren anpassen, den Prompt überarbeiten – und erst dann** …" | — | ⛔ **the `Leiter`/`Sprosse` word field is OCCUPIED by two other referents**: `Leiter`(12 / 4) and `Sprosse`(9 / 3) are the guardrails escalation ladder (`guardrails/d` 6+7) and the tuning ladder in `cloud-platforms/d`. A `Drift-Leiter` coinage would be the third sense of one word inside one Part · `der Drift`(10 / 3), canon §1.1.e Incumbent, DISPUTED gender held | **none for the noun; corpus precedent for the construction → §11.2** |
| **Corpus as a release** | 4 | **das Korpus ist ein Release** (Satz, kein Kompositum) | Korpus: das / die Korpora / des Korpus · Release: **das** Release | KORPUS bold, twice: „**Das Korpus ist ein Release**" (take-away) and H2 „Der Prompt und **das Korpus sind Releases**"; plus the section-1 H2 „**Das Korpus ist das Produkt**" · `das Release` genus = WAVE3 §8 D-4 (Neutrum, a house decision) | corpus precedent + ledger |
| **Permission-aware retrieval** | 3 | **ein Retrieval, das die Berechtigungen kennt** | — (relative clause) | KORPUS bold, verbatim: „**Ein Retrieval, das die Berechtigungen kennt**, ist kein Merkmal, das Sie später ergänzen" · ⛔ `berechtigungsbewusst` **0** (a calque of *-aware*) · `die Zugriffssteuerung`(15 / 6) is the neighbouring settled term and must **not** be substituted here — it is *access control*, not the filter | corpus precedent |
| **Cross-lingual retrieval gap** | — | **KEIN deutscher Terminus. Konstruktion:** H3 „**Nur eine Sprache.**" + „übersehen einschlägige englische Dokumente, sobald die Frage in einer anderen Sprache eintrifft, und der Fehler bleibt unbemerkt: **weniger Treffer, alle plausibel**" | — | `Cross-Lingual` **0**; `sprachübergreifend`(7 / 2) exists but **only in Part I** (`ingestion/d` 6, `retrieval/d` 1) and never as a name for this gap · `mehrsprachig` is the canon §1.1.g form for *multilingual* and is used for the users, not the gap | **none → §11.2** |
| **Graceful degradation (tools)** | — | **KEIN deutscher Terminus. Konstruktion:** „**Liefern Sie absichtlich eine schlechtere Antwort, statt gar keine**" + „die Nutzer halten das für einen Defekt und nicht für Langsamkeit" | — | `Degradation` **0**, `geordnete Verschlechterung` **0** · ⚠ WAVE3 W3-15 adds `graceful shutdown` → „das geordnete Herunterfahren" as a new OPEN row — **a different referent**; do not borrow it here · `die Fallback-Antwort`(1 / 1) is the mechanism, not the property | **none → §11.2** |

---

## 7. `## Production – Bereitstellung und Betrieb` \{#serving} — 31 headwords

This is the densest kept-EN section, and it is also where the corpus **overrules the canon three times on
spelling** (`Prefix-Caching`, `der Cold-Start`, `Reinforcement-Fine-Tuning` — the last one in §8). Every
kept-EN row below was checked individually; four of the assumed-kept-EN terms are in fact German-led or
construction-led in the delivered German (`Serving`, `Admission control`, `Load shedding`, `Data parallelism`).

| EN headword | Cl. | German headword form | Artikel / Plural / Genitiv | Evidence | Ev. class |
|---|---|---|---|---|---|
| **Serving** | 3 | **die Bereitstellung** (Vorgang/Disziplin) / **der Betrieb** (laufender Dienst) | die Bereitstellung / die -en / der Bereitstellung · der Betrieb / – / des Betriebs | KORPUS `Bereitstellung`(41 / 15); shipped titles „**Bereitstellung und Betrieb** – FastAPI + Docker" and „Bereitstellung und Betrieb – Vertiefung", used as the lesson's name in **9 cross-references** · **canon §1.1.d: `Serving` = OPEN als freies Substantiv**; `rag.md` §2 German-led row „die Bereitstellung / der Betrieb"; „das Serving" mit deutschem Artikel unbelegt · ⚠ WAVE3 §1.5 keeps three referents apart: **die Auslieferung** (act of delivering) · **das Deployment** (one countable deploy) · **die Bereitstellung** (the process/discipline) | corpus precedent + canon |
| **Inference** | 3 | **die Inferenz** | die / die Inferenzen / der Inferenz | KORPUS(36 / 8) · canon §1.1.g German-led row, Injektionsblock point 4 („die Inferenz", nicht „die Inference") | corpus precedent + canon §1.1.g |
| **Inference server** | 2 | **die Inferenz-Engine**, Erstnennung mit Klammerglosse *(inference server)* | **die** / die Inferenz-Engines / der Inferenz-Engine | KORPUS(22 / 5) — „eine **Inferenz-Engine** (*inference server*) auf Ihren eigenen GPUs" ships the parenthesis verbatim; **`Inferenzserver` 0** · X-1 (collision resolved for A) · ⚠ WAVE3 §9 keeps the row OPEN, incumbent held: heise + iX are **one** Stilfamilie counted twice | corpus precedent + ledger (OPEN, incumbent held) |
| **SSE (Server-Sent Events)** | 2 | **SSE**, artikellos; ausgeschrieben **die Server-Sent Events** | artikellos; ausgeschrieben Pl. | KORPUS `SSE`(12 / 5), `Server-Sent Events`(1 / 1) · canon §1.1.c | corpus precedent + canon |
| **Time-to-first-token (TTFT)** | 2 | **das Time-to-First-Token (TTFT)** | **das** / – / des Time-to-First-Tokens | KORPUS(7 / 3), neuter and case-marked: „sondern **das Time-to-First-Token (TTFT)**", „Spürbar ist **das TTFT**" · ⚠ **capitalisation differs from the English page**: the corpus writes `Time-to-First-Token` (capital F, capital T), the English glossary writes `Time-to-first-token`. **Keep the corpus capitalisation in the German headword** — it is the delivered form and § 45 E1 licenses it | corpus precedent |
| **Streaming** | 2 | **das Streaming** | das / – / des Streamings | KORPUS(18 / 8), neuter attested („**das Streaming** über SSE", „**das Streaming** zum Nutzer", dative „beim Streaming") | corpus precedent |
| **Continuous batching** | 2 | **das Continuous Batching** (gespreizt, Adj+Subst) | **das** / – / des Continuous Batching | KORPUS(10 / 4), neuter and case-marked in another file: „**Das Continuous Batching** liegt im GPU-Scheduler", „nicht mit **dem Continuous Batching** aus Bereitstellung und Betrieb" · `Batching`(13 / 4); ⚠ WAVE3 §7 downgrades `das Batching` to **HOUSE** (both runs applied the same `-ing` rule) — but the **compound** is corpus-attested, so this row stands on the corpus | corpus precedent |
| **PagedAttention** | 1 | **PagedAttention**, unverändert | artikellos | KORPUS(4 / 2) | corpus precedent |
| **Cold start** | 2 | **der Cold-Start** (durchgekoppelt) | der / die Cold-Starts / des Cold-Starts | KORPUS **`Cold-Start` 13 (3 files) : `Cold Start` 0 : `Kaltstart` 0** · canon §1.1.d Incumbent + W3-8 (the canon spells it three ways in three places; the corpus settles it) · `rag.md` §3: DISPUTED, incumbent held | corpus precedent + canon (W3-8 delta confirmed shipped) |
| **OpenAI-compatible API** | 3 | **die OpenAI-kompatible API** | die / die APIs / der API | KORPUS `OpenAI-kompatible API`(4 / 3) + `OpenAI-kompatibl*`(6 / 5) · canon §1.1.a `die API` (DISPUTED, feminine incumbent held) | corpus precedent + canon |
| **ASGI workers** | 2 | **die ASGI-Worker** (Pl.) | der ASGI-Worker / die ASGI-Worker (Nullplural) / des ASGI-Workers | KORPUS(3 / 2) — „starten Sie mehrere **ASGI-Worker** – eigenständige Kopien des ASGI-Servers (uvicorn)" · canon §1.1.d `Worker`; W3-38 „verwenden, aber nie nackt" (bare `Worker` reads as a person) | corpus precedent + canon |
| **uvloop** | 1 | **`uvloop`**, Codeschrift/kleingeschrieben, unverändert | artikellos | KORPUS(1 / 1) | corpus precedent (thin: 1 token) |
| **Threadpool offloading** | — | **KEIN deutscher Terminus für *offloading*. Konstruktion:** „eine gewöhnliche `def`-Pfadoperation läuft **in einem anyio-Threadpool** … und nicht im Event-Loop"; die Regel heißt im Korpus **die Threadpool-Regel** | Threadpool: der / die Threadpools / des Threadpools | KORPUS `Threadpool`(2 / 1) — both tokens · `auslagern`/`ausgelagert` **0 in Part III** (2 tokens exist in `planning-loops/d`, a different referent) · ⚠ WAVE3 §7 marks `der Threadpool` as `AGREED ×2` on **one informatik-aktuell pattern read twice** | corpus precedent for `Threadpool`; **`none` for *offloading* → §11.2** |
| **Backpressure** | 2 | **Backpressure**, artikellos; **Pflichtglosse** „(Schutz vor Überlast – der Empfänger bremst den Sender)" | **kein Artikel erfinden** | KORPUS(5 / 3) — and the **corrected gloss ships verbatim** at `serving/d` · ⛔ `Gegendruck` **0** · **⚠ the canon `rag.md` §2 gloss table still says „(Gegendruck – Schutz vor Überlast)"** — W3-10 proposes the change, the corpus has already made it. **Rule for the corpus** | **corpus precedent — overrules the canon gloss, see §11.3** |
| **Load shedding** | — | **KEIN deutscher Substantiv. Verbale Konstruktion:** „**Anfragen gezielt abweisen**"; Mermaid „**Abweisen – sofort `429` / `503` + `Retry-After`**" und „**Last abweisen: `429` / Producer drosseln / Worker-Pool vergrößern**" | — | KORPUS `Load Shedding` **0**, `Lastabwurf` **0**; the verb `abweis*`(4 / 3) carries it · canon §1.1.d `Load Shedding` = **OPEN** · WAVE3 §9: describe the action; ⛔ `der Lastabwurf` (69 : 0 — power grid **and** aviation, W3-13) | **corpus precedent for the construction; the noun is OPEN** |
| **Admission control** | — | **KEIN deutscher Terminus. Korpusform: `die Annahme` als Mechanismusname in Fügung** — „das Rate Limit je Nutzerkonto …, jetzt **in die Annahme eingebaut** statt nachträglich angeschraubt"; Mermaid „**Annahme – Obergrenze `max_num_seqs`**" | die Annahme / die -n / der Annahme | KORPUS `Admission Control` **0**; `grep -ci admission editorial/canon/de/_language.md` = **0** · canon `rag.md` §2 still lists it as settled kept-EN — **W3-9 moves it to §3 (OPEN)** · ⚠ **`die Annahme` is occupied on the neighbouring page**: „ruht auf einer unausgesprochenen **Annahme**" (`serving/i`) = *assumption*. Two referents, one word, one lesson | **corpus precedent (construction); referent collision → §11.1** |
| **Little's Law** | 1 | **Little's Law**, unverändert, artikellos | artikellos | KORPUS(2 / 1) — „Warum das so früh greift, sagt **Little's Law**: L = λW" · ⚠ `rag.md` §2 lists it settled kept-EN **with no §1.1 row** (W3-7, the thirteen-pointer-at-an-empty-cell class) — harmless here because it is article-less in both tokens | corpus precedent |
| **Iteration-level scheduling** | 3 | **das Scheduling auf Iterationsebene** | das / – / des Schedulings | KORPUS(3 / 1) verbatim, bold once: „Continuous Batching ist in Wahrheit **Scheduling auf Iterationsebene**" · kept-EN head `Scheduling` + German prepositional phrase | corpus precedent |
| **Prefill / decode** | 2 | **Prefill** / **Decode**, Kompositumsbildner, **kein freier Artikel** | **kein Artikel erfinden** | KORPUS `Prefill`(6 / 2), `Decode`(5 / 2), all as compound formers or bare („bei jedem **Decode-Schritt**") · canon: **no §1.1 row for either** (W3-7) · WAVE3 §9 OPEN, closes when a German house prints „des Prefills" / „beim Prefill" with an article | corpus precedent + ledger (OPEN) |
| **Chunked prefill** | 2 | **Chunked Prefill** (gespreizt — `Chunked` ist ein Adjektiv, § 37 E4) | artikellos | KORPUS(2 / 1) · W3-6 explicitly keeps `Chunked`, `Continuous`, `Late` spaced because they ARE adjectives | corpus precedent + ledger |
| **Prefix caching** | 2 | **das Prefix-Caching** (durchgekoppelt — `prefix` ist ein Substantiv, § 45 E1) | das / – / des Prefix-Cachings | KORPUS **`Prefix-Caching` 3 : `Prefix Caching` 0** · **⚠ the canon `rag.md` §2 lists it SPACED**; W3-6 proposes the hyphen, the corpus already ships it. **Rule for the corpus** | **corpus precedent — overrules the canon spelling, see §11.3** |
| **Quantisation** | 3 | **die Quantisierung** | die / die -en / der Quantisierung | KORPUS(4 / 2) · canon §1.1.g + Injektionsblock point 4; ⚠ **nicht** `Quantifizierung` (a real false friend) | corpus precedent + canon §1.1.g |
| **KV-cache quantisation** | 3 | **die Quantisierung des KV-Caches** (Genitivfügung, kein Kompositum) | die / – / der Quantisierung | KORPUS verbatim, bold: „Eine eigene Achse ist die **Quantisierung des KV-Caches**" · **`KV-Cache-Quantisierung` 0** — the corpus deliberately does not compound it · `KV-Cache`(19 / 2); head noun canon §1.1.a `der Cache`, Gen. `des Caches` | corpus precedent |
| **Tensor parallelism** | 3 | **die Tensor-Parallelität** | die / – / der Tensor-Parallelität | KORPUS(4 / 1) incl. a Mermaid subgraph („Tensor-Parallelität – innerhalb eines Knotens") · WAVE3 §9: hyphenate all three sharding compounds **uniformly**, HOUSE | corpus precedent + ledger (HOUSE) |
| **Pipeline parallelism** | 3 | **die Pipeline-Parallelität** | die / – / der Pipeline-Parallelität | KORPUS(4 / 1) incl. a Mermaid subgraph | corpus precedent + ledger (HOUSE) |
| **Data parallelism** | 3 | **die Daten-Parallelität** | die / – / der Daten-Parallelität | KORPUS(2 / 1) — „**Daten-Parallelität** ist ein anderes Werkzeug für ein anderes Problem", „vollständige Kopien nach dem Muster der **Daten-Parallelität**". ⚠ **A full-word grep on `Datenparallel*` returns 0** — this row is the concrete instance of the concord bug the brief warns about | corpus precedent + ledger (HOUSE) |
| **MIG (Multi-Instance GPU)** | 1 | **MIG (Multi-Instance GPU)**, unverändert | artikellos | KORPUS(2 / 1) | corpus precedent (thin: 2 tokens) |
| **GPU time-slicing** | 2 | **das GPU-Time-Slicing** | **das** (⚠ nach der `-ing`-Regel, nicht korpusbelegt) / – / des GPU-Time-Slicings | KORPUS(2 / 1) — „**GPU-Time-Slicing** verschränkt stattdessen die Arbeit auf derselben GPU" (nominative, no article) and „mit MIG oder **Time-Slicing**" (prepositional) · `Zeitscheib*` **0** · no canon row | **corpus precedent for the WORD, `none` for the GENUS → §11.2** |
| **KEDA** | 1 | **KEDA**, unverändert | artikellos | KORPUS(1 / 1) — „[KEDA], **einen** ereignisgetriebenen **Autoscaler**" (the article belongs to `Autoscaler`, masculine) · WAVE3 §9 `autoscaling` regraded to *one house, real evidence* (ADDENDUM A3) | corpus precedent (thin: 1 token) |
| **KServe** | 1 | **KServe**, unverändert | artikellos | KORPUS(1 / 1) | corpus precedent (thin: 1 token) |
| **Serverless GPU** | 2 | **Serverless GPU**, artikellos, gebunden; verbal „**skaliert im Leerlauf auf null**" | **kein Artikel erfinden** | KORPUS `Serverless`(8 / 4), always bound (`Serverless GPU`, `das Serverless-Angebot`, „echtem Serverless für GPUs") · ⛔ `serverlos` **0** · WAVE3 §9 OPEN: de.wikipedia's `serverlos` is **17 of 18 peer-to-peer** · ⚠ §7: `die GPU` is the wave's highest-exposure THIN×2 row (80 occurrences, all evidence de.wikipedia, 0 shipped) | corpus precedent + ledger (OPEN) |

---

## 8. `## Production – Cloud-KI-Plattformen` \{#cloud-platforms} — 24 headwords

| EN headword | Cl. | German headword form | Artikel / Plural / Genitiv | Evidence | Ev. class |
|---|---|---|---|---|---|
| **Managed endpoint** | 3 | **der verwaltete Endpunkt** | der / die verwalteten Endpunkte / des verwalteten Endpunkts | KORPUS `Endpunkt*`(26 / 7); „Modelle als **verwaltete Endpunkte**"(2), „laufen auf den **verwalteten Endpunkten**"(1); **`Managed Endpoint` 0, `Managed` 0** · `rag.md` §2 struck the kept-EN row in wave 3 (five canon locations lead `der Endpunkt`); X-13 measured `verwaltet` **9 : 0**; W3-42 records four slices confirming with no dissent | corpus precedent + canon + ledger |
| **Model catalogue** | 3 | **der Modellkatalog** — **gebunden, nie nackt** | der / die Modellkataloge / des Modellkatalog[e]s | KORPUS(4 / 2) — „der zweite ist der **Modellkatalog** – welche Modelle Ihnen diese Plattform als verwaltete Endpunkte …" · canon §1.1.a `der Katalog` · ⚠ W3-38: `Modellkatalog` bare is dangerous — **10 of 10 de.wikipedia hits are vehicle brochures** | corpus precedent + canon + ledger (binding obligation) |
| **Data residency** | 2 | **die Data Residency**, kept-EN, **Pflichtglosse bei Erstnennung**; im Fließtext **der Speicherort** | Data Residency: **die** (fem.), artikellos in Subjektstellung · Speicherort: der / die -e / des Speicherorts | KORPUS `Data Residency`(7 / 2) at term-level positions (H2, the contrast, „eine Zusage zur…") **and** `Speicherort`(20 / 3) in running prose — exactly the split WAVE3 §8 D-1 decided, **now shipped** · ⛔ `Datenresidenz` **0** · ⛔ `die Datenhoheit` belongs only to the sovereignty branch (SC-M2) | **corpus precedent — D-1 upgrades from DECIDED to shipped** |
| **Provisioned throughput** | 1 | **Provisioned Throughput**, unverändert (Herstellerangebot) | artikellos | KORPUS(6 / 2) incl. `PTU-Endpunkte`, `PTU-Kapazität` · `rag.md` §2 moved it to class 1 in wave 3; the **appellative** in the same paragraph runs over `der Durchsatz` (canon §1.1.a) | corpus precedent + canon |
| **Batch mode** | 2/3 | **der Batch-Tarif** (*batch tier*), Klammerpflicht bei Erstnennung | der / die Batch-Tarife / des Batch-Tarif[e]s | KORPUS(15 / 5) — the ledger's THIN×2 row is now the **best-shipped** term in the money field · ⛔ `Batch-Modus` **0**, ⛔ `die Preisstufe` (X-12: 95 hits, all Verkehrsverbund fare zones), ⛔ `die Stapelverarbeitung`, ⛔ `der Batch-Betrieb` (§8 D-3) · ⚠ the corpus's own warning must stay readable: „Verwechseln Sie **den Batch-Tarif** nicht mit dem **Continuous Batching**" | **corpus precedent — D-3's THIN×2 label can be retired for the German form (15 : 0); the external attestation question stays open** |
| **Managed RAG** | 2/3 | **ein verwaltetes RAG-Angebot** (*managed RAG*); kompakt **das Managed-RAG-Angebot** | das / die -e / des -Angebot[e]s | KORPUS `RAG-Angebot`(7 / 2) + `verwaltetes RAG`(3 / 2); **`Managed RAG` 0** · X-17: `Stufe` is occupied 55× as *rung/stage*, `Ebene` 35× — ⛔ `die Managed-RAG-Stufe` · `RAG` ships 124× and **never** with an article | corpus precedent + ledger |
| **Vendor lock-in** | 2 | **Vendor-Lock-in**, artikellos | **kein Artikel erfinden** | KORPUS(3 / 3) — „Schutz vor **Vendor-Lock-in**" · WAVE3 §9 OPEN (Artikel) · ⚠ W3-42 flags the tension: the term carries `Vendor` while the head noun's own answer is `der Anbieter` (38 : 0). **Reported, not litigated** | corpus precedent + ledger (OPEN) |
| **Fine-tuning** | 2 | **das Fine-Tuning**, Pflichtglosse „(Nachtrainieren des Modells)" | das / die Fine-Tunings / des Fine-Tunings | KORPUS(33 / 6) · canon §1.1.b + rag.md §2 gloss table | corpus precedent + canon |
| **LoRA / PEFT** | 1 | **LoRA / PEFT**, unverändert, **Nullglosse** (Eigennamen) | artikellos; **der LoRA-Adapter** im Kompositum | KORPUS `LoRA`(11 / 2), `PEFT`(3 / 2) — „einen kleinen **LoRA-Adapter** über eingefrorenen Basisgewichten" · `rag.md` §2 „bare names take a ZERO gloss" | corpus precedent + canon |
| **DPO (Direct Preference Optimization)** | 1 | **DPO**, unverändert | artikellos | KORPUS(5 / 2) | corpus precedent |
| **Reinforcement fine-tuning (RFT)** | 2 | **das Reinforcement-Fine-Tuning (RFT)** (durchgekoppelt) | das / – / des Reinforcement-Fine-Tunings | KORPUS **hyphenated 3 (`cloud-platforms/d`) : spaced 1 (`llmops/d`)**; `RFT`(5 / 2) · § 45 E1 (Subst.+Subst.) supports the majority | corpus precedent (majority) + canon; **shipped inconsistency → §11.1** |
| **Model distillation** | 2/3 | **die Distillation**; als Angebotsname **Model Distillation** | **die** / die -en / der Distillation | KORPUS(3 / 1) — „darüber **die Distillation** und ganz oben das fortgesetzte Vortraining", „**Model Distillation** (ein Lehrermodell versieht die Daten für ein kleineres Schülermodell mit Labels)" · ⛔ `Destillation` **0** (the chemistry word), ⛔ `Distillierung` **0** · no canon row | corpus precedent (thin: 3 tokens, 1 file) |
| **Continued pre-training** | 3 | **das fortgesetzte Vortraining** (*continued pre-training*) | das / – / des Vortrainings | KORPUS(2 / 1) verbatim **with the italic English in parentheses** — the class-3 form the canon prescribes · ⛔ `Pre-Training` **0**, ⛔ `Weiterführendes Vortraining` **0** | corpus precedent |
| **Managed agent runtime** | 3 | **die verwaltete Agenten-Laufzeitumgebung**; Anapher **die Umgebung** | die / die -en / der Agenten-Laufzeitumgebung | KORPUS(4 / 2) · X-11 + W3-2/W3-4 · ⛔ **`die Agentenlaufzeit`** — a canon coinage with de.wikipedia insource **0**, and it is **SHIPPED once**, at `part-2-agents/mcp/deep-dive.md:15` („eine Entwicklungsumgebung, eine Chat-App, eine **Agentenlaufzeit**"), leaked out of the canon's own `Host` Pflichtglosse. **W3-4 predicted the mechanism; this is the live instance** → §11.1 | corpus precedent + ledger |
| **FinOps** | 2 | **FinOps**, artikellos | **kein Artikel erfinden** | KORPUS(8 / 3), all article-less · WAVE3 §8 D-6 names this the `Backpressure`/`FinOps`/`Chargeback` class | corpus precedent + ledger |
| **Cost modelling** | 3 | **die Kostenmodellierung** | die / die -en / der Kostenmodellierung | KORPUS(1 / 1) — „FinOps (der Aufbau der Preise je Plattform, …)" list item „**Kostenmodellierung**" · no canon row, no ledger row | corpus precedent (thin: 1 token) |
| **Unit economics** | 3 | **die Stückkosten** (des Features) | die (Pl.) / — / der Stückkosten | KORPUS(2 / 1) — „auf die **Stückkosten des Features** – die Kosten pro Anfrage, pro aktiven Nutzer, pro ausgeliefertem Feature" · ⛔ `Unit Economics` **0** · WAVE3 §9 OPEN, incumbent = exactly this construction | corpus precedent + ledger (OPEN) |
| **Committed-use discount** | 3 | **der Rabatt für eine zugesagte Nutzung** | der / die Rabatte / des Rabatt[e]s | KORPUS `Rabatt*`(7 / 4); **two forms for one referent**: „Rabatte **für eine zugesagte Nutzung**"(2, `llmops/d`) vs „Rabatte **bei fester Abnahmezusage**"(1, `cloud-platforms/i`) · ⛔ `Committed-Use` **0** | corpus precedent (majority 2 : 1); **shipped inconsistency → §11.1** |
| **Context caching** | 2 | **das Context-Caching** | **das** / – / des Context-Cachings | KORPUS(1 / 1) — „**Das Context-Caching** von Gemini berechnet zwischengespeicherte Eingabe mit etwa 10 % der regulären Eingabe" — **article-bearing neuter, so the genus IS decided** · ⛔ `Kontext-Caching` **0** · distinct from `das Prompt-Caching`(8 / 5) | corpus precedent (thin: 1 token, but case-marked) |
| **Cross-region egress** | 3 | **der Egress zwischen Regionen** | der / – / des Egress | KORPUS `Egress`(5 / 3) — „der **Egress zwischen Regionen**"(3) · ⛔ **`regionsübergreifend`** (X-10: both runs counted the same 10 de.wikipedia hits; the run that **read** them found all ten are urban planning / demography / tourism, zero IT; 0 in the shipped German) · rebuild „zwischen Regionen" / „über Regionsgrenzen hinweg" | corpus precedent + ledger |
| **Multi-cloud gateway** | 3 | **das Gateway über mehrere Clouds hinweg** | das Gateway / die Gateways / des Gateways | KORPUS: H2 „**Anbieterunabhängig bleiben – das Gateway über mehrere Clouds hinweg**", bold in prose, plus the take-away and `cloud-platforms/i` („das Gateway-Muster über mehrere Clouds hinweg") · ⛔ `Multi-Cloud-Gateway` **0** · Mermaid label „**LLM-Gateway / Router**" (cp/d) | corpus precedent |
| **Digital sovereignty** | 3 | **die digitale Souveränität** | die / – / der Souveränität | KORPUS `Souveränität`(11 / 2) — „**Die digitale Souveränität** stellt eine härtere Frage als die **Data Residency**"; the section thesis ships verbatim: „Die Frage nach dem Ort ist eine Frage der Geografie, **die Souveränität eine Frage der Macht**" · `sidebar_label: "Kosten, Agenten und Souveränität"` · SC-M2 | corpus precedent + ledger |
| **Sovereign cloud** | 3 | **die souveräne Cloud** (Adjektiv klein und flektiert) | die / die souveränen Clouds / der souveränen Cloud | KORPUS(2 / 2) + inflected genitive plural „die Regionen **souveräner Clouds**" and „in einer bestimmten Region **einer souveränen Cloud**" · ⚠ **WAVE3 §9 says „BSI never writes `souveräne Cloud`" and asks for one register per page; the shipped German writes it anyway.** Rule for the corpus. ⛔ **`die souveräne Region`** stays banned (X-16 — de.wikipedia's one hit is constitutional geography) → „eine Region in einer souveränen Cloud" | **corpus precedent — overrules the ledger's caution, see §11.3** |
| **Air-gapped** | 3 | **physisch getrennt** (Adjektiv); Erstnennung „vollständig physisch getrennte Bereitstellungen (*air-gapped*)"; im Kompositum **die Air-Gap-Variante** | Adjektiv; Air-Gap im Kompositum nur | KORPUS `physisch getrennt*`(6 / 1) + the italic English gloss once + `Air-Gap-Variante`(1 / 1); **`Air Gap` as a free noun 0**, `luftdicht` 0 · canon/WAVE3 §9 `Air Gap` OPEN (Genus), incumbent = `physisch getrennt` + the compound | corpus precedent + ledger (OPEN) |

---

## 9. `## Production – das Tooling-Ökosystem` \{#tooling-ecosystem} — 4 headwords

**This is the section the brief flags as the corpus-beats-canon test case, and it holds.** The canon's own
metaprose (`rag.md` §8, Phase 6) wrote `das Werkzeug-Ökosystem`; the shipped German writes
`Tooling-Ökosystem` **3 : 0** and uses it in two live navigational links. W3-29 files the canon repair.

| EN headword | Cl. | German headword form | Artikel / Plural / Genitiv | Evidence | Ev. class |
|---|---|---|---|---|---|
| **Instrumentation** | 3 | **die Instrumentierung** | die / die -en / der Instrumentierung | KORPUS(6 / 3); **`Instrumentation` 0 in German prose** · canon §1.1.g + Injektionsblock point 4; `rag.md` §2 struck the kept-EN row in wave 3 · ⚠ **carve-out**: the lowercase English `instrumentation` in the `[Neue Begriffe]` footers of **both** `tooling-ecosystem` pages (`index.md:194`, `deep-dive.md:144`) is **not** a regression — WAVE3 §6 releases it until the glossary wave. **This wave IS the glossary wave: those footers now become translatable, and a checker will read them as fresh regressions unless the render brief says otherwise** → §11.4 | corpus precedent + canon §1.1.g |
| **OpenTelemetry GenAI conventions** | 2/3 | Laufform **die GenAI-Konventionen von OpenTelemetry**; Zitierform **einmal** „die GenAI Semantic Conventions von OpenTelemetry"; Versionszitat `Semantic Conventions v1.41.x` | die (Pl.) / — / der GenAI-Konventionen | KORPUS `GenAI-Konventionen`(6 / 3) : `GenAI Semantic Conventions`(2 / 2) : `semantische Konventionen` 0 · W3-32: **five names ship across Parts I/II** — the owning page uses the running form three times incl. its take-away, and it is the only variant that inflects as German. **Part III must not add a sixth** | corpus precedent + ledger (binding) |
| **Safety classifier** | 3 | **der Klassifikator für Sicherheitsrisiken**, kurz **der Klassifikator** | der / die Klassifikatoren / des Klassifikators | KORPUS(13 / 6) — bold and verbatim: „Die zweite Bauform ist **der Klassifikator für Sicherheitsrisiken**"; also `Klassifikatormodell*` · ⛔ `Sicherheitsklassifikator` **0** · WAVE3 §9 listed this as OPEN with exactly this incumbent — **it now ships, so the row upgrades** | **corpus precedent — upgrades the ledger's OPEN row** |
| **Red-teaming** | 2 | **das Red-Teaming**; Durchlauf **der Red-Teaming-Durchlauf** | das Red-Teaming / kein Plural / des Red-Teamings · der Durchlauf / die -läufe / des -laufs | KORPUS `Red-Teaming`(25 / 4) · W3-28 upgrades the genus from HOUSE (`-ing` rule) to **corpus-attested Neutrum** („**ein ernsthaftes** Red-Teaming" + two genitives) · X-5: ⛔ `Red-Team-Läufe`, ⛔ `Red-Teaming-Läufe`, ⛔ `Red-Team-Durchläufe` — the attested compound family is `Red-Teaming-` and the head noun is `Durchlauf` | corpus precedent + ledger |

---

## 10. `## Production – LLMOps` \{#llmops} — 19 headwords

| EN headword | Cl. | German headword form | Artikel / Plural / Genitiv | Evidence | Ev. class |
|---|---|---|---|---|---|
| **LLMOps** | 2 | **LLMOps**, artikellos | **kein Artikel erfinden** | KORPUS(27 / 11) — **no article-bearing token in the whole corpus**: „**LLMOps** ist der Name, den die Branche dieser Disziplin gegeben hat", „der Teil **von LLMOps**", „was **LLMOps** von MLOps erbt", compound `die LLMOps-Lektion`, `eine LLMOps-Praxis` · shipped titles „LLMOps – ausrollen, überwachen, Kosten", „LLMOps – Vertiefung" | corpus precedent; **genus not decided and not needed** |
| **Canary release** | 2 | **das Canary Release** (gespreizt) | das / die Canary Releases / des Canary Release[s] | KORPUS(10 / 3) · canon §1.1.d row · ⚠ W3-22 asks for ONE ruling over the `Canary Release / Shadow Deployment / Prompt Registry / Quality Gate / Release Gate` family; the shipped German is **not uniform** (see the `Prompt registry` row below) → §11.1 | corpus precedent + canon |
| **Shadow deployment** | 2 | **das Shadow Deployment** (gespreizt) | das / die Shadow Deployments / des Shadow Deployments | KORPUS(3 / 2) · ⛔ `Schatten*` **0** · head noun canon §1.1.a `das Deployment` | corpus precedent + canon |
| **Prompt registry** | 2 | **die Prompt-Registry** (durchgekoppelt) | **die** / die Prompt-Registries / der Prompt-Registry | KORPUS **hyphenated 2 : spaced 0** · **⚠ the canon `rag.md` §2 lists `Prompt Registry` SPACED** while it lists `Canary Release` spaced too — and the corpus ships one of each. § 45 E1 (`Prompt` is a noun) supports the hyphen here and § 37 E4 (`Canary` is an adjective) supports the space there, so **the shipped asymmetry is CORRECT, not a defect** — which is exactly what W3-22 could not decide from inside a slice. Record it as resolved by the corpus | **corpus precedent — resolves W3-22 for these two members, see §11.3** |
| **Model pinning** | 2/3 | **das Model-Pinning**; verbal **die Modellversion festlegen** | das / – / des Model-Pinnings | KORPUS `Model-Pinning`(2 / 2) + „**Legen Sie die Modellversion fest**" (bold, `production-failures`), „**Modell festgelegt**" (InfoCard label), `festgelegt`(26 / 15) · WAVE3 §4 binds both halves | corpus precedent + ledger |
| **Model routing** | 3 | **das Routing über Modelle hinweg** | das Routing / – / des Routings | KORPUS(6 / 4) — „die Hebel bei den Kosten: das **Routing über Modelle hinweg**" · **`Modell-Routing` 0** · ⚠ **the canon `rag.md` §2 carries `Model Routing` kept-EN and §1.3.3's citation paragraph carries `Model-Routing`; the corpus writes neither.** Rule for the corpus | **corpus precedent — overrules the canon term, see §11.3** |
| **Fallback** | 2 | **Fallbacks** (Pl.), artikellos, Kompositumsbildner: **die Fallback-Kette**, **die Fallback-Antwort** | **kein Artikel erfinden**; Plural **Fallbacks** | KORPUS(8 / 4) incl. the H3 „**Fallbacks und das Gateway**", the Mermaid label „LLM-Gateway: Routing, Fallbacks, Budgets", `die Fallback-Kette`(2), `die Fallback-Antwort`(1) — **no article-bearing singular anywhere** · §8 D-6: `rag.md` §2 carries it as settled kept-EN **with no §1.1 row** (W3-7's thirteenth pointer at an empty cell); genus stays **OPEN** · sense split: „LoRA macht **den Rollback** fast kostenlos" is the rollback path, **not** the routing chain | corpus precedent + ledger (OPEN Genus) |
| **LLM gateway** | 2 | **das LLM-Gateway** | das / die LLM-Gateways / des LLM-Gateways | KORPUS `LLM-Gateway`(8 / 3) + bare `Gateway`(≈20, `cloud-platforms/d` + `llmops`) — „am **LLM-Gateway** aus Teil 1", „das **AI Gateway** von Azure API Management" (class-1 product name) · ⚠ WAVE3 §9 notes `gateway` occurs **31×** in the same file set and is the delivered incumbent — the reason bare `Gate` stays OPEN | corpus precedent |
| **Prompt caching** | 2 | **das Prompt-Caching** (durchgekoppelt) | das / – / des Prompt-Cachings | KORPUS(8 / 5) — „das **Prompt-Caching** (das statische Präfix zuerst)", „die Faktoren **des Prompt-Cache**" | corpus precedent |
| **Semantic caching** | 2/3 | Vorgang **das semantische Caching**; das Ding **der semantische Cache** | Caching: das / – / des Cachings · Cache: der / die Caches / **des Caches** | KORPUS `semantisches Caching`(3 / 2) — „über das **semantische Caching**", „Beim **semantischen Caching** sparen Sie Kosten" — and `semantischer Cache`(1, inflected: „samt einem **semantischen Cache**") · ⛔ `der Semantik-Cache` · WAVE3 §2 rules `der semantische Cache` **HOUSE** (ruled by no slice); the head noun is canon §1.1.a `der Cache` · ⚠ **the corpus keeps process and thing apart — do not collapse them** | corpus precedent + ledger (HOUSE) |
| **Drift** | 2 | **der Drift**; vorzugsweise das Kompositum **der Eingabedrift · der Korpusdrift · der Modelldrift** | der / die Drifts / des Drifts | KORPUS(10 / 3) · canon §1.1.e Incumbent, `rag.md` §3 **DISPUTED** (Duden has *die* Drift = current and *der* Drift = motorsport, neither in the ML sense) · W3-21: all three compounds **masculine**, and strike the canon's false „besser belegt" claim (de.wikipedia insource = 0 for all three) | corpus precedent + canon (DISPUTED, incumbent held) |
| **Grader** | 3 | **der Bewerter** | der / die Bewerter (Nullplural) / **des Bewerters** | KORPUS(16 / 3), 5 in `llmops/d` alone — „bei dem das Belohnungssignal von einem **Bewerter** kommt, den Sie selbst festlegen", „**der Bewerter** bepunktet sie" · **`Grader` 0** · ⚠ **canon `rag.md` §2 lists `Grader` as settled kept-EN while §3 and §1.1.e hold it OPEN with `der Bewerter` as the Korpusform** — W3-26 scopes §2 to the API name (`model graders`). Rule for the corpus | **corpus precedent — resolves a canon self-contradiction, see §11.3** |
| **Showback** | 2 | **Showback**, artikellos | **kein Artikel erfinden**; „beim Showback" | KORPUS(3 / 1), all article-less — „**Showback** berichtet jedem Team … den eigenen Verbrauch", „**Showback** ist das Fundament" · WAVE3 §9 OPEN (Genus) | corpus precedent + ledger (OPEN) |
| **Chargeback** | 2 | **Chargeback**, artikellos; **das Chargeback-Verfahren** im Kompositum | **kein Artikel erfinden** | KORPUS(5 / 1), all article-less — „**Chargeback** geht weiter und bucht die Kosten … auf die Gewinn- und Verlustrechnung", „Wird per **Chargeback** abgerechnet" · WAVE3 §9 OPEN (Genus) | corpus precedent + ledger (OPEN) |
| **Release gate** | 3 | **die Freigabe vor dem Release** — eine Zeichenkette | die / die -n / der Freigabe | KORPUS(3 / 2) incl. the H2 „**Die Freigabe vor dem Release und der Weg zurück**" · **`Release Gate` 0**; `insource:"Release Gate"` = 0 and `insource:"Release-Gate"` = 0 (W3-23) · ⚠ `rag.md` §2 lists it settled kept-EN while §1.1.f and `ai-sdlc.md` hold it **OPEN, zero attestation** — W3-23 strikes the §2 line as a bootstrap remnant. Rule for the corpus · the counted sense `gate` → **die Prüfung / die Prüfungen** („**Nicht jede Prüfung kostet gleich viel.**", `production-failures`) | **corpus precedent — resolves a canon self-contradiction, see §11.3** |
| **Error budget policy** | 3 | **die Richtlinie zum Fehlerbudget** | die / die -n / der Richtlinie | KORPUS(4 / 2) bold — „an die eine Organisation gebunden ist: die **Richtlinie zum Fehlerbudget**", „**Eine Richtlinie zum Fehlerbudget** ist eine schriftliche Vereinbarung, unterschrieben vor jedem Vorfall" · ⛔ `Fehlerbudget-Richtlinie` **0**, ⛔ `Richtlinie für das Fehlerbudget` **0** · head noun canon §1.1.e/§1.1.g `das Fehlerbudget` (⛔ *Error Budget*, struck from §2 in wave 1) | corpus precedent + canon §1.1.g |
| **Release freeze** | 3 | **der Stopp aller Releases** | der / – / des Stopps | KORPUS(3 / 1) bold once — „Das ist **der Stopp aller Releases**, und die Richtlinie muss zu jeder Handlung den Verantwortlichen benennen"; anaphorically **der Stopp** („die Befugnis, **den Stopp** auszusprechen", „Ohne unterschriebene Richtlinie ist **der Stopp** ein Vorschlag") · ⛔ `Release-Freeze`, `Release-Stopp`, `Freigabestopp`, `Freeze` **all 0** | corpus precedent |
| **Job queue** | 2 | **die Job-Queue** | die / die Job-Queues / der Job-Queue | KORPUS(3 / 1) + Mermaid „**Job-Queue<br/>(Backpressure: laufende Arbeit begrenzen)**" · X-4: **`die Queue` 45 of 45**, ⛔ bare `die Warteschlange` in Part III, ⛔ `die Warteschlangentiefe` / `Queue-Tiefe` (queue depth → **die Länge der Queue**) · `job` → **der Job**, Erstnennung gebunden „ein Job – eine Arbeitseinheit, die die Queue trägt" (§4) | corpus precedent + ledger + canon §1.1.d |
| **Dead-letter queue (DLQ)** | 2 | **die Dead-Letter-Queue (DLQ)** (durchgekoppelt) | die / die Dead-Letter-Queues / der Dead-Letter-Queue | KORPUS `Dead-Letter-Queue`(3 / 1) + `DLQ`(4 / 1) + Mermaid „**Dead-Letter-Queue<br/>(Alarm bei Wachstum)**" · canon §1.1.d row (identical, hyphenated) | corpus precedent + canon |

---

## 11. The flag list — what I did NOT silently decide

### 11.1 Inconsistent in the SHIPPED corpus (referent-inventory defects)

| # | Term | The split, measured | Ruling | Note |
|---|---|---|---|---|
| **F-1** | `rug pull` | **`Rug-Pull` 4** (`part-2-agents/mcp/deep-dive.md`) **: `Rug Pull` 2** (`part-1-rag/cross-cutting/guardrails/deep-dive.md`) | **`der Rug-Pull`** — majority + canon §1.1.c + §1.3.3 | **Shipped Part I defect. Report, do not repair here** — same shape and same handling as W3-30/W3-31 |
| **F-2** | `reinforcement fine-tuning` | **`Reinforcement-Fine-Tuning` 3** (`cloud-platforms/d`) **: `Reinforcement Fine-Tuning` 1** (`llmops/d`) | **`das Reinforcement-Fine-Tuning`** — majority + § 45 E1 | Both inside Part III, i.e. inside this wave's own delivery |
| **F-3** | `committed-use discount` | „Rabatte **für eine zugesagte Nutzung**" 2 (`llmops/d`) : „Rabatte **bei fester Abnahmezusage**" 1 (`cloud-platforms/i`) | **`der Rabatt für eine zugesagte Nutzung`** — majority | Two paraphrases, no coinage on either side, so the cost of the split is only inconsistency |
| **F-4** | `die Annahme` — **two referents, one word, one lesson** | *admission control* („in **die Annahme** eingebaut", `serving/d`) vs *assumption* („eine unausgesprochene **Annahme**", `serving/i`) | Keep the construction; **never let `die Annahme` stand alone as the admission-control term** — always „in die Annahme eingebaut", „Annahme – Obergrenze `max_num_seqs`" | The `Sprosse`/`Leiter` shape (F-5) one lesson over. No gate reads for it |
| **F-5** | `die Leiter` / `die Sprosse` — **three referents competing** | guardrails escalation ladder (`guardrails/d` 6+7), tuning ladder (`cloud-platforms/d` 4+1), and the *drift response ladder* would be a third | **Do not coin `die Drift-Leiter`.** Use the corpus's sequence-as-a-sentence | Recorded so a later sweep does not "unify" the metaphor |
| **F-6** | `Canary Release` spaced vs `Prompt-Registry` hyphenated | `Canary Release` 10 spaced, `Shadow Deployment` 3 spaced, `Prompt-Registry` 2 hyphenated, `MCP-Registry` 2 hyphenated | **Both are right** — `Canary`/`Shadow` are adjectives (§ 37 E4), `Prompt`/`MCP` are nouns (§ 45 E1) | **This resolves W3-22 for four of its five members.** `Quality Gate` / `Release Gate` stay unresolved because both ship 0 times |
| **F-7** | `die Agentenlaufzeit` — **a banned canon coinage that SHIPPED** | 1 token, `part-2-agents/mcp/deep-dive.md:15` | ⛔. Use **`die Agenten-Laufzeitumgebung`** (4 / 2 in Part III) | The canon's own `Host` Pflichtglosse (`_language.md` §1.1) instructs renderers to write it. **W3-4 predicted the mechanism; this is the live instance.** The glossary must not inherit it |

### 11.2 No corpus occurrence AND no ledger/canon row — genuinely undecided at render time

Seven referents and two genders. **Each has a corpus-attested construction, which is the ruling until
something closes the row** — none of them needs a coinage to ship.

| # | Headword | What is missing | Corpus-attested construction to ship | What would close it |
|---|---|---|---|---|
| **U-1** | **Trajectory stitching** | no German noun anywhere; no ledger row; no canon row | „**die Kennung des Gesprächs oder der Aufgabe** durch jede Nachricht ziehen, sodass sich die Spans zu einem Eltern-Kind-Trace zusammensetzen" | a German source naming the practice with an inflected noun |
| **U-2** | **Server discovery** | `Serverfindung`/`Serversuche`/`Entdeckung` all 0; ⚠ the one `Discovery` token is **OIDC discovery**, a different referent | H2 „**Einen Server zu finden heißt nicht, ihm zu vertrauen**"; „findet ein Client **über eine Registry** heraus, welche Server es überhaupt gibt" | an inflected German noun for the ecosystem-level lookup |
| **U-3** | **Drift response ladder** | no noun; and the `Leiter`/`Sprosse` field is occupied twice (F-5) | „neu indexieren und neu in Chunks aufteilen, die Mischung der Suchverfahren anpassen, den Prompt überarbeiten – **und erst dann** an die Gewichte" | — (prefer the sentence permanently; a heading coinage is the least reversible place) |
| **U-4** | **Cross-lingual retrieval gap** | `Cross-Lingual` 0; `sprachübergreifend` exists **only in Part I** and never names this gap | H3 „**Nur eine Sprache.**" + „weniger Treffer, alle plausibel" | a German source naming the recall loss |
| **U-5** | **Graceful degradation (tools)** | `Degradation` 0, `geordnete Verschlechterung` 0; ⚠ W3-15's „das geordnete Herunterfahren" is *graceful shutdown*, a **different** referent | „**Liefern Sie absichtlich eine schlechtere Antwort, statt gar keine**" | a German source naming the property |
| **U-6** | **Threadpool offloading** (the *offloading* half) | `auslagern` 0 in Part III | „läuft **in einem anyio-Threadpool** … und nicht im Event-Loop"; die **Threadpool-Regel** | a German source naming the act |
| **U-7** | **Interleaved thinking** | the term is 0; only the adjective `verschränkt` is attested, and it also does duty for *chunked prefill* | „**das Nachdenken zwischen den Tool-Calls**"; kept-EN `Interleaved Thinking` article-free if the term is unavoidable | one case-marked German token |
| **U-8** | **das Ingestion-Manifest** — GENUS only | the word ships (1 label + 2 prose) but **every token is article-less or nominative** | Ship the word; if an article is forced, **do not invent one in the glossary** — write „ein **Manifest**, das ausweist …" | one case-marked token |
| **U-9** | **das GPU-Time-Slicing** — GENUS only | 2 tokens, neither article-bearing; no canon row. The `das` above is derived from the `-ing` rule, which WAVE3 §7 explicitly labels **one derivation counted twice, not two data points** | „**GPU-Time-Slicing** verschränkt die Arbeit auf derselben GPU"; „mit MIG oder **Time-Slicing**" | one case-marked token |

**Also thin, but decided by a single case-marked token — flagged so nobody reads the ruling as strong:**
`das Context-Caching` (1 token, but article-bearing, so the genus IS decided) · `die Distillation` (3 tokens,
1 file) · `die Kostenmodellierung` (1 token) · `uvloop`, `KEDA`, `KServe` (1 token each, all class 1, so no
German decision is at risk) · `MIG` (2 tokens).

Three headwords are `MCP-` compounds the corpus never writes, while their head nouns are fully attested:
**`der MCP-Host`** (bare `der Host` case-marked ×3), **`die MCP-Ressourcen`**, **`die MCP-Prompts`**. The
`MCP-` pattern itself is corpus-attested three times over (`MCP-Server` 20, `MCP-Client` 9, `MCP-Registry` 2)
and Durchkopplung is obligatory (§1.3.3), so the compound is safe — but **its evidence class is *pattern +
head noun*, not corpus precedent for the compound.** Stated so the render does not over-claim.

### 11.3 Where the ledger or canon disagrees with the shipped corpus — I rule for the CORPUS, explicitly

| # | Term | Canon / ledger says | Shipped corpus says | Ruling | Filed as |
|---|---|---|---|---|---|
| **C-1** | `Backpressure` gloss | `rag.md` §2 gloss table: „(Gegendruck – Schutz vor Überlast)" | „(**Schutz vor Überlast – der Empfänger bremst den Sender**)", `serving/d` | **the corpus gloss** | W3-10 (already proposed) |
| **C-2** | `prefix caching` spelling | `rag.md` §2 kept-EN list: `Prefix Caching`, **spaced** | `Prefix-Caching` **3 : 0** | **hyphenated** | W3-6 (already proposed) |
| **C-3** | `model routing` | `rag.md` §2 kept-EN `Model Routing`; §1.3.3 citation form `Model-Routing` | **`das Routing über Modelle hinweg` 6 : 0** | **the German construction** | **NEW — not in WAVE3's canon delta** |
| **C-4** | `grader` | `rag.md` §2: settled kept-EN `Grader` · §3 + §1.1.e: OPEN, Korpusform `der Bewerter` | **`der Bewerter` 16 : `Grader` 0** | **`der Bewerter`**; §2's entry scopes to the API name | W3-26 (already proposed) |
| **C-5** | `release gate` | `rag.md` §2: settled kept-EN · §1.1.f + `ai-sdlc.md`: OPEN, zero attestation | **`die Freigabe vor dem Release` 3 : `Release Gate` 0** | **the German string** | W3-23 (already proposed) |
| **C-6** | `sovereign cloud` | WAVE3 §9: BSI never writes `souveräne Cloud`; pick one register per page | **`die souveräne Cloud` 2, inflected in the genitive plural** | **`die souveräne Cloud`** (⛔ `die souveräne Region` stands) | **NEW — a ledger caution the corpus has overtaken** |
| **C-7** | the Adj+Subst / Subst.+Subst. family | W3-22 asks for ONE ruling over five terms and holds the incumbents | `Canary Release` + `Shadow Deployment` **spaced**; `Prompt-Registry` + `MCP-Registry` **hyphenated** | **the asymmetry is correct** — adjective → space, noun → hyphen | **NEW — resolves W3-22 for four of five members; `Quality Gate` / `Release Gate` stay open (both ship 0)** |
| **C-8** | `handoff` | canon `_language.md` §1.1.c: **OPEN** | **`die Übergabe` 28 / 8 files** | **`die Übergabe`** | **NEW — canon-silent row the corpus has already decided** |
| **C-9** | `Human-in-the-Loop` genus | canon has **no §1.1 row** (only the §1.3.3 Durchkopplung list) | **masculine, article-bearing in four independent files** | **`der Human-in-the-Loop`** | **NEW — canon-silent row the corpus has already decided** |
| **C-10** | `admission control` | `rag.md` §2: settled kept-EN | **0 in the corpus; `die Annahme` in Fügung** | construction; the noun is OPEN | W3-9 (already proposed) |
| **C-11** | `batch tier` label | WAVE3 §8 D-3: `der Batch-Tarif` is the wave's **THIN×2** row | **15 occurrences, 5 files** | **the German form is no longer thin**; only the *external attestation* question remains open | **NEW — a label the corpus has outgrown** |
| **C-12** | `safety classifier` | WAVE3 §9: **OPEN**, incumbent `der Klassifikator für Sicherheitsrisiken` | **it ships, bold, as the section's second Bauform** | **upgrade the row from OPEN to corpus precedent** | **NEW** |
| **C-13** | `Data Residency` / `der Speicherort` | WAVE3 §8 D-1: **DECIDED** (a judgement call with a stated cost of being wrong) | **the split ships exactly as decided** — 7 term-level : 20 running-prose | **upgrade from DECIDED to shipped** | **NEW** |
| **C-14** | `Werkzeug-Ökosystem` (canon metaprose) | `rag.md` §8 Phase 6: „Teil III ist die Lektion über das **Werkzeug-Ökosystem**" | **`Tooling-Ökosystem` 3 : 0**, incl. the page title and two live navigational links | **`das Tooling-Ökosystem`** | W3-29 / X-15 (already proposed) |

**Nine of these fourteen are already on WAVE3's canon-delta list; five are new** (C-3, C-6, C-7, C-8, C-9,
plus the three re-gradings C-11/C-12/C-13). They are **reported, not applied** — nothing in `editorial/canon/`
was touched.

### 11.4 A defect class this wave creates and no current gate would catch

**The `[Neue Begriffe]` footers become translatable the moment the German glossary exists, and nothing marks
that transition.** Today every German lesson page ends with the **English** term list, and WAVE3 §6 carve-out
#2 explicitly licenses that „until the glossary wave". This *is* the glossary wave. So:

- if the footers stay English, `instrumentation` in `tooling-ecosystem/{index,deep-dive}.md` remains a
  licensed exception — but a term checker run **after** the glossary ships will read it, and the other ~30
  footers, as fresh regressions of `die Instrumentierung`, `die Übergabe`, `der Bewerter` and so on;
- if the footers are translated, **every count in every previous ledger silently changes**, because the
  footers were the excluded set (§1.2).

**Recommendation: decide the footer question in the same PR as the glossary, and state the decision in the
render brief.** Either way the deterministic gate needs to know which set it is excluding. Neither
`banscan.py` nor `locale_parity.py` can see this — one reads sentences, the other reads heading ids.

---

## 12. Section headings — proposed German, from the shipped lesson titles

**Method: no coining.** Each descriptor is lifted from the shipped German page's own `title:` / H1 /
`sidebar_label`, per the brief. RU and SK both keep the English lesson-family prefix and translate only the
trailing descriptor; German does the same **and swaps the dash**: `—` (U+2014) → **`–` (U+2013) with
spaces**, per `_language.md` § Typografie and the worked example in `rag.md` §7 point 4.

| # | English heading | **Proposed German heading** | Source of the descriptor |
|---:|---|---|---|
| 11 | `## Agents — multi-agent systems` | `## Agents – Multi-Agenten-Systeme` | `multi-agent/index.md` → `title: Multi-Agenten-Systeme` |
| 12 | `## Agents — orchestration frameworks` | `## Agents – Orchestrierungs-Frameworks` | `orchestration-frameworks/index.md` → `title: Orchestrierungs-Frameworks` |
| 13 | `## Agents — MCP and agent protocols` | `## Agents – MCP und Agentenprotokolle` | `mcp/index.md` → `title: MCP und Agentenprotokolle` |
| 14 | `## Agents — real agents (capstone)` | `## Agents – echte Agenten (Abschluss dieses Teils)` | `real-agents.md` → `title: Echte Agenten – …`; `part-2-agents/overview.md` writes „über **die echten Agenten**"; **`der Abschluss dieses Teils` is a shipped cross-page string, 11 tokens in 9 files** ⚠ see note |
| 15 | `## Production — why AI fails in production` | `## Production – warum KI-Systeme im Produktivbetrieb versagen` | **canon precedent, `_language.md` §9.2, verbatim** — „Warum KI-Systeme im Produktivbetrieb versagen" ✓, and it is the shipped `title:`. **Do not re-coin; do not substitute `scheitern`/`ausfallen`/`fehlschlagen`** (§9.2 rules the five verbs apart and this one is a mechanism failing to deliver its expected function) |
| 16 | `## Production — serving` | `## Production – Bereitstellung und Betrieb` | `serving/index.md` → `title: "Bereitstellung und Betrieb – FastAPI + Docker"`; the lesson is named this way in **9 cross-references**. ⚠ Do **not** carry the „– FastAPI + Docker" tail into the glossary heading (a second dash in one heading) |
| 17 | `## Production — cloud platforms` | `## Production – Cloud-KI-Plattformen` | `cloud-platforms/index.md` → `title: Cloud-KI-Plattformen`; W3-41 also binds the `_category_.json` label „Cloud-KI-Plattformen" (⛔ „Cloud-AI-…") |
| 18 | `## Production — the tooling ecosystem` | `## Production – das Tooling-Ökosystem` | `tooling-ecosystem/index.md` → `title: Das Tooling-Ökosystem`; X-15 / W3-29 / W3-41. ⛔ `Werkzeug-Ökosystem`, ⛔ `Tool-Ökosystem` |
| 19 | `## Production — LLMOps` | `## Production – LLMOps` | `llmops/index.md` → `title: "LLMOps – ausrollen, überwachen, Kosten"`; the bare name is the form used in all 11 files. ⚠ Do not carry the tail |

⚠ **Heading 14 is the one place I coined a bracket rather than lifted one.** The shipped title is „Echte
Agenten – Claude, OpenAI, Gemini", which has no equivalent of „(capstone)"; RU/SK write „(завершающий урок)" /
„(záverečná lekcia)" = *(closing lesson)*. I chose **„(Abschluss dieses Teils)"** because that exact string
ships 11 times as the cross-page name for this page. **Alternative if the render prefers the RU/SK shape:
„(Abschlusslektion)" — but that word is 0 in the corpus, so it is a coinage and would enter „auf Probe"
per `_language.md` §6.** Prefer the shipped string.

**Capitalisation.** The descriptor after the dash follows German orthography, not the English page's
lowercase: nouns are capitalised (`Multi-Agenten-Systeme`, `Bereitstellung und Betrieb`), a leading article or
adverb is not (`das Tooling-Ökosystem`, `warum KI-Systeme …`, `echte Agenten`). This matches RU/SK, which also
lowercase the leading word of the descriptor.

---

## 13. Anchors — the exact strings, in the binding order

Both forms per section, **the HTML anchor first, then a blank line, then the heading**. The `\{#id}` form
carries a **literal backslash**: `docusaurus.config.ts` sets `future: { v4: true }`, the MDX-1 heading-id
preprocessor is therefore off, and a bare `{` is parsed as JSX — **the build fails hard**. The backslash is
markup, not part of the id. `scripts/locale_parity.py` asserts the **ordered sequence** of explicit heading
ids against English, so these nine must appear in exactly this order, after slice A's ten.

```
<a id="multi-agent"></a>
## Agents – Multi-Agenten-Systeme \{#multi-agent}

<a id="orchestration-frameworks"></a>
## Agents – Orchestrierungs-Frameworks \{#orchestration-frameworks}

<a id="mcp"></a>
## Agents – MCP und Agentenprotokolle \{#mcp}

<a id="real-agents"></a>
## Agents – echte Agenten (Abschluss dieses Teils) \{#real-agents}

<a id="production-failures"></a>
## Production – warum KI-Systeme im Produktivbetrieb versagen \{#production-failures}

<a id="serving"></a>
## Production – Bereitstellung und Betrieb \{#serving}

<a id="cloud-platforms"></a>
## Production – Cloud-KI-Plattformen \{#cloud-platforms}

<a id="tooling-ecosystem"></a>
## Production – das Tooling-Ökosystem \{#tooling-ecosystem}

<a id="llmops"></a>
## Production – LLMOps \{#llmops}
```

**Ordered id sequence for slice B** (verified against `grep -n '^## ' docs/glossary.md`, positions 11–19 of 19):

`multi-agent` · `orchestration-frameworks` · `mcp` · `real-agents` · `production-failures` · `serving` ·
`cloud-platforms` · `tooling-ecosystem` · `llmops`

⚠ These are the last nine of the **19** ids `rag.md` §7 point 5 lists as the binding order. **Translate the
heading text, never the id**, and never insert an entry in one locale only — §7 point 3's failure mode is
that every id below the insertion still exists, the count still matches, the *set* still matches, and every
inbound link lands on the neighbouring entry. The reader gets a plausible wrong definition and nobody
reports it.

---

## 14. External references — all verified, none translated

`↗ [Wikipedia]` / `↗ [arXiv]` / vendor-site links are **English sources and are not translated**; the link
text stays as on the English page. **All twelve in slice B resolve.** Verified per repo convention (never cite
a link from memory) with:

```bash
curl -sSL -o /dev/null -w '%{http_code} %{url_effective}' --max-time 25 -A 'Mozilla/5.0' '<URL>'
```

| Section | Link | HTTP | Note |
|---|---|---:|---|
| multi-agent | `en.wikipedia.org/wiki/Foundation_for_Intelligent_Physical_Agents` | 200 | — |
| multi-agent | `en.wikipedia.org/wiki/Contract_Net_Protocol` | 200 | — |
| multi-agent | `en.wikipedia.org/wiki/Blackboard_system` | 200 | — |
| multi-agent | `arxiv.org/abs/2305.14325` | 200 | multi-agent debate |
| mcp | `modelcontextprotocol.io` (×2) | 200 | redirects to `/docs/2026-07-28/getting-started/intro` — a **dated docs path**, so the bare host is the right thing to cite; do not pin the redirect target |
| mcp | `a2a-protocol.org` | 200 | — |
| mcp | `registry.modelcontextprotocol.io` | 200 | — |
| serving | `en.wikipedia.org/wiki/Server-sent_events` | 200 | — |
| serving | `arxiv.org/abs/2309.06180` | 200 | PagedAttention |
| serving | `en.wikipedia.org/wiki/Little%27s_law` | 200 | keep the `%27` escape |
| tooling-ecosystem | `github.com/open-telemetry/semantic-conventions-genai` | 200 | extra check, because GitHub 200s are not proof of a live repo: `api.github.com/repos/…` → `full_name: open-telemetry/semantic-conventions-genai`, `archived: false`, `pushed_at: 2026-07-29`. **Real and active.** No redirect, so it is not a renamed repo |
| llmops | `martinfowler.com/bliki/CanaryRelease.html` | 200 | — |

**404s: none.** The `arxiv.org/abs/2406.12045` link on line 561 (`pass^k`) belongs to slice A's
`planning-loops` section and was not checked here.

---

## 15. What this pass could not do

1. **The corpus can convict, not acquit** — the ledger's own limit, and it binds this sheet harder, because
   **57 of my 141 rows rest on `corpus precedent` as their primary evidence.** Where the shipped German is
   wrong, my grep agrees with it confidently. F-1 and F-7 are the two places I caught it; there will be others.
2. **No native ear read any of these forms.** I checked distribution, inflection and referent — not idiom.
   The highest residual risk, in order: „**die Vertrautheit mit dem Maßstab**", „**der Rabatt für eine
   zugesagte Nutzung**", „**das Scheduling auf Iterationsebene**", „**die Aushandlung der Fähigkeiten**",
   „**der Stopp aller Releases**".
3. **I did no new lexicographic research.** Every external attestation cited here comes through
   `WAVE3-TERMS.md` or `editorial/canon/de/`. The two counter-checks WAVE3 §12.2 names as most valuable
   (`der Perimeter`, `die GPU`) are still owed, and `die GPU` sits in my `Serverless GPU` row.
4. **I did not measure the 360 px Mermaid label budget.** Several bound German strings in my sections are
   longer than their English originals („Annahme – Obergrenze `max_num_seqs`", „Dead-Letter-Queue<br/>(Alarm
   bei Wachstum)"). That belongs at the render gate; WAVE3 §5 says which labels.
5. **Slice A's ten sections are untouched**, including terms that also occur in mine (`Drift`, `Guardrails`,
   `Observability`, `Trace`, `Span`, `Goldstandard`, `Evaluierung`). If slice A rules any of those
   differently, **the collision is real and needs a stage-2 gate over the two sheets** — exactly the shape
   WAVE3 §1 exists for. I have flagged the overlap rather than reaching into their slice.
6. **The genus of `LLMOps` is not decided and I did not decide it.** 27 occurrences, 11 files, **zero
   article-bearing tokens.** Every one of them is a subject, a compound former, or governed by a preposition.
   That is not an accident to repair; it is a form that works, and inventing „das LLMOps" for one glossary
   headword would create the incumbent retroactively — the `Eval` failure mode from W3-27.

---

## Lessons

**What the corpus told me that the canon did not.**

- **Nine of my headwords are decided in the shipped German and nowhere else.** `die Übergabe` (canon:
  `Handoff` = OPEN, corpus: 28 in 8 files), `der Human-in-the-Loop` (canon: no gender row at all, corpus:
  masculine and article-bearing in four independent files), `das Routing über Modelle hinweg`, `die souveräne
  Cloud`, `der Klassifikator für Sicherheitsrisiken`, `der Stopp aller Releases`, `die Richtlinie zum
  Fehlerbudget`, `das Context-Caching`, `die Quantisierung des KV-Caches`. **The pattern: the canon records
  the terms somebody argued about, and the corpus records the terms somebody had to write.** A term that
  never caused an argument has no canon row and 28 corpus tokens — and reading only the canon makes it look
  undecided when it is the best-evidenced row on the sheet.
- **`AGREED ×2`'s failure signature has a corpus-side twin, and it is worse.** The ledger warns that two runs
  agreeing on a verdict while disagreeing on the measurement means the agreement is about instinct. The
  corpus version: **a form that ships in one file, twice, and nowhere else** reads exactly like a form that
  ships everywhere, because both are "corpus precedent". `die Distillation` (3 tokens, 1 file) and
  `der Batch-Tarif` (15 tokens, 5 files) carry the same label and are not the same claim. I added file counts
  to every cell for this reason; a bare occurrence count hides single-file rows.
- **Three canon deltas WAVE3 proposed are already shipped, which changes what they are.** W3-6
  (`Prefix-Caching` hyphenated), W3-8 (`der Cold-Start`) and W3-10 (the `Backpressure` gloss) are not
  proposals any more — the renderers made those calls independently and the pages went out. Same finding as
  wave 1's dash correction: **where a register and six independent renderers diverge, the register is the
  suspect.** The delta list should distinguish *proposed* from *already true in the output*, or someone will
  "apply" a change that is a no-op and log it as work.

**The instrument that misled me, and it was not the one I was warned about.**

- I was told to distrust `concord.py` for undercounting stem-changing inflections. That warning paid off
  exactly once (`Daten-Parallelität`: a full-word grep on `Datenparallel*` returns **0**, the corpus writes
  it hyphenated). **The instrument that nearly cost me three rulings was plain `grep -i`, because of the
  `[Neue Begriffe]` footers.** Every German lesson page ends with an English lowercase term list, so
  `grep -roi handoff` returns 2 and both are English. Three of my headwords — `handoff`, `sub-agent`,
  `trajectory` — would have been ruled kept-EN on footer hits. **WAVE3 §6 records this carve-out for two
  pages; it is corpus-wide.** The general form: *the corpus contains a copy of the source-language term list,
  so any loan-word census over the target locale double-counts its own input.*
- **And the mirror-image trap fired too, in the other direction.** WAVE3 §10.3 warns *a zero on the loan is
  not a zero on the referent* — `Managed` 0 does not mean the concept is absent, the German writes
  `verwaltet` 9. My slice produced the **non-zero** version: `Discovery` occurs once in the MCP deep-dive and
  it is **OpenID Connect discovery**, not server discovery. A count of 1 on the right string measuring the
  wrong referent is the `Span`/`Sampling` error one floor down, and the only defence is printing the context
  window instead of the number. I printed context for every non-trivial row and it changed four rulings.

**Defect classes no current gate would catch.**

- **The footer transition (§11.4).** The `[Neue Begriffe]` footers are English *by a license that expires
  when the German glossary ships* — and nothing anywhere encodes the expiry. After this wave, a term checker
  will read ~30 footers as fresh regressions of `die Instrumentierung`, `die Übergabe` and `der Bewerter`; if
  instead the footers get translated, every count in every earlier ledger silently shifts, because the
  footers were the excluded set. `banscan.py` reads sentences and `locale_parity.py` reads heading ids;
  neither can see a licensed exception whose license ran out. **A carve-out with a stated expiry condition
  and no gate that watches for it is a scheduled defect.**
- **One German word doing three jobs inside one Part, where each job is in a different file.** `die Annahme`
  = *admission control* (`serving/d`) and *assumption* (`serving/i`), one lesson apart. `die Leiter` /
  `die Sprosse` = the guardrails escalation ladder, the tuning ladder, and — if anyone coins
  `die Drift-Leiter` — the drift response ladder. Every gate this project runs is **per page**: the cold
  read, the register pass, the naturalness gate. **A word-field collision that never puts two senses on one
  page is invisible to all of them, and it is the reader who pays**, because the reader meets both pages in
  one sitting. What would catch it is a per-**Part** referent inventory keyed on the German word, not on the
  English term — the inverse of how every ledger in this directory is indexed.
- **A canon block released for verbatim reuse is an unversioned code path into the output.** `die
  Agentenlaufzeit` is banned (de.wikipedia insource 0), and it **shipped** at
  `part-2-agents/mcp/deep-dive.md:15`, because the canon's `Host` Pflichtglosse instructs renderers to copy
  that exact string. W3-4 identified the mechanism; the token is still in the delivered locale. Wave 1 found
  the identical shape with the forbidden em dash in five glosses. **Twice is a pattern: strings the canon
  releases for verbatim copying need to be gated as shipped output, which §2's own rule already says —
  „eine Zeichenkette, die §2 zum wörtlichen Übernehmen freigibt, ist ein AUSGELIEFERTER String" — and
  nothing enforces it.** A grep of the ban list over the canon's own release-for-copy blocks would have
  caught both.
- **Off-by-one in a brief's prose against its own line numbers.** The brief said "the last 10 sections" and
  then listed nine heading lines; the file has 19 sections, so 10 + 9 is exactly right and the prose is
  wrong. Harmless here because the line list was authoritative and I checked. **It would not have been
  harmless if I had trusted the word "10" and reached back into slice A's `planning-loops`** — two agents
  ruling the same section, which is the collision this whole two-slice split exists to avoid. Same class as
  „never cite an issue number from memory": **a count in prose is a shared mutable variable, and the brief
  is not exempt from its own rule.**
