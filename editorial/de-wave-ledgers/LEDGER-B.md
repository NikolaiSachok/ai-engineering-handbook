# LEDGER-B — binding ledger, slice B (queueing, load management, latency)

**Gate 6.5, stage 1 · German RAG wave 3 (Part III) · reconciles `OUT-B-run1.md` + `OUT-B-run2.md`**
Both sheets read in full (313 + 311 lines). New evidence used: the **27 shipped German pages** of Parts I+II
(issue #328), plus the live canon rows in `editorial/canon/de/_language.md` and `rag.md`. No new
lexicographic research; every web citation below is quoted from one of the two sheets and attributed.

**Arithmetic notice (brief §6):** this slice proposes **+9 rows** to `_language.md` §1.1 (`Job`, `Pool`,
`Kontingent`, `Tarif`, `Streaming`, `Nebenläufigkeit`, `Semaphor`, `Mandant`, `warten`-Rektion) and **+1
struck/moved row** (`Admission Control`, §2 → §3). **Deltas only — do not compute the new totals here.**

---

## 0. What the shipped German corpus decided before either run opened a browser

Neither run grepped the delivered locale. Ten rows of this slice are answered by it, four of them against
the sheets. Counts are over the 27 pages, case-insensitive, word-boundary-anchored where a naive substring
would lie (it does: bare `tier` returns 72 hits, of which **2** are the word — the rest are `-tieren` verbs).

| Shipped form | n | What it settles | Quoted sentence |
|---|---|---|---|
| `Obergrenze` | **41** | `bound`(a) noun and `concurrency cap` — the incumbent already exists | „Eine **Obergrenze für Wiederholungen** (**Retry-Budget**) – hart, pro Aufruf und pro Durchlauf" · „**Eine Obergrenze für die Breite** legt fest, wie viele Worker ein Orchestrator pro Schritt startet" |
| `Wiederholung` 7 · `Wiederholungen` 10 · `Wiederholungsschleife` 1 · `Wiederholungsstrategie` 1 · `Wiederholen` 1 · `wiederholen` 7 · `wiederholt` 10 | **37** | `retry` → `die Wiederholung`, closed | „die Regel, die **die Wiederholungen** an die Schreibzugriffe zurückbindet" |
| `begrenzen/begrenzt/unbegrenzt` | **28** | `bound`(a) verb + `unbounded` | „Lim[\"**begrenzt** Breite und Rekursion\"]" |
| `Zeitüberschreitung` 4 · `Timeout` 1 · `Zeitbeschränkung` **0** | — | the **error/value split, shipped and correct** — and the shipped word for the *set value* is the loan, not `Zeitbeschränkung` | „**Zeitüberschreitung** – das Tool hat **innerhalb seines Timeouts** nicht geantwortet." (Genitiv `des/seines Timeouts` attested **in our own book**) |
| `Rate Limit` **spaced** | **1** | the `rate limit` orthography dispute (§3, R7) | „Bei **transienten** Fehlern – einer Zeitüberschreitung, **einem Rate Limit**, einem `5xx` …" (Dativ ⇒ Neutrum confirmed) |
| `Quote` (= *rate*) | **1** of 3 hits is the referent | the `quota` collision, predicted by both runs, now **observed** | „Die kontextualisierten Embeddings allein senken **die Quote** um 35 % (5,7 % → 3,7 %)" |
| bare `Tier` | **2**, both **bound** | the ⛔ on appellative `Tier` — the book has never written it free | „… stehen TypeScript, Python, C# und Go als offizielle SDKs auf **Tier 1**, Java und Rust auf **Tier 2**" |
| `p50` 4 · `p95` 5 · `p99` 1 | **10** | run 2's „`p50` fehlt in `rag.md` §1" gap — shipped, class 1, closed | „Sie setzen Ziele für **p50 und p95** und zerlegen die Latenz nach Spans" |
| `TTFT` bare, unarticled | **3** | the abbreviation's treatment | „**TTFT** gegen die gesamte verstrichene Zeit" · „**Die Antwort so zu streamen, dass TTFT kurz bleibt**" |
| `Batch` masc. | **14** | `der Batch` in running German — but in the *tool-call grouping* sense, **not** the pricing sense | „fasst Aufrufe standardmäßig **zu einem Batch** zusammen" · „In **einem parallel ausgeführten Batch**" |
| `Queue` **0** · `Warteschlange` **0** | **0** | the canon's `Queue`/`Warteschlange` split has **never shipped**. Part III is its first use — the choice is cheap now and expensive later |
| `Tarif` 0 · `Betriebsart` 0 · `Abrechnung` 0 · `Kontingent` 0 · `Nebenläufigkeit` 0 · `Semaphor` 0 · `asynchron` 0 · `Backpressure` 0 | **0** | every head noun the two runs fought over is **new**. There is no incumbent to prefer, so §3's "prefer a confirmed incumbent" cannot rescue this slice — which is why the `tier`(a) row is the weakest thing here |

**Three occupancy warnings the corpus raises and neither sheet saw:**

1. **`die Stufe` is taken.** 55 word-boundary hits, all *stage / rung of complexity / pipeline step*: „Nehmen
   Sie **die einfachste Stufe**, die die Aufgabe trägt", „**die teurere Stufe**", „welche **Stufe** langsam
   war", „die **Stufe** – Retrieval oder Generation". Run 2 offered `die Stufe` as the head for `tier`(b). It
   is not free.
2. **`die Schicht` is taken** — 96 hits, and one of its shipped senses is the handbook's own curriculum
   metaphor („die **Schicht** Retrieval", „jede **Schicht** vertieft"). `tier`(d) must therefore ship the
   **compound** `die Anwendungsschicht`, never bare `die Schicht`.
3. **`Tail` already ships kept-EN in this book** — `Tail-based Sampling`, `Tail-Sampling`, and inside a German
   Mermaid label „Prüfung auf **Tail** und Vorrang". So `die Tail-Latenz` would not merely be unattested (both
   runs measured 0); it would **collide with a live token in the same book** on a different referent. Second,
   independent reason for the same ⛔. Likewise `Vorrang` is occupied („**Vorrangregel**", „Priority-Sampling")
   ⇒ ⛔ `Vorrang-Tarif`.

---

## 1. Binding table

Class: **1** identifier/untouchable · **2** kept-EN loan · **3** German-led (first-mention gloss) · **4** fully German.

| Terminus | German | Class | Status | Artikel / Plural / Genitiv | Kollokation | ⛔ rejected | Evidence grade |
|---|---|---|---|---|---|---|---|
| **queue** | **die Queue**; first mention per page „**die Queue** (Warteschlange)" | 2 | **BOUND** — all 45 Part III occurrences are the runtime object; the canon split is inert here | die / die Queues / der Queue | die Queue **abarbeiten** · die Queue **läuft voll** · **in die Queue stellen** · **aus der Queue holen** · „solange die Queue nicht leer ist" | ⛔ *das/der Queue* (full paradigm exists — for the **billiard cue**: `insource:"das Queue"` 17, `"dem Queue"` 32, all Snooker/Poolbillard, run 1) · ⛔ bare *die Schlange* (reptile, in a Python book) · ⛔ *die Warteschleife* (telephone hold music, run 2) | **RECONCILED** (run 1 retire-the-split vs run 2 keep-the-split → §3 R1) + canon row `_language.md` `Queue` WEAK, 2026-07-28 |
| **queue depth** | **die Länge der Queue** | 3 | **BOUND** (running prose) | die / die Längen / der Länge | „auf **die Länge der Queue** und die GPU-Auslastung skalieren" · Mermaid „Begrenzte Queue<br/>max. Länge D" | ⛔ *die Queue-Tiefe*, *die Warteschlangentiefe* (calques of *depth*; German measures a queue in **Länge**) | **RECONCILED** (run 1 `die Warteschlangenlänge` / run 2 `die Länge der Queue` → §3 R2). `Warteschlangenlänge` stays licensed but is not needed: both Part III hits are autoscaling signals, not queueing theory |
| **Dead-Letter Queue (DLQ)** | citation `Dead-Letter Queue`; running **die Dead-Letter-Queue**, **die DLQ** | 2 | **BOUND** | die / die -Queues / der -Queue | „die erschöpften Jobs **in die Dead-Letter-Queue routen**" · Mermaid „Dead-Letter-Queue<br/>(Alarm bei Wachstum)" | ⛔ *die Warteschlange für unzustellbare Nachrichten* — four vendor translations, three vendors, one self-contradicting → disqualified in canon | **AGREED×2**, and **stronger than either sheet said**: run 1 called the gender "inherited"; the canon row carries **independent** ORDIX attestation („muss **die** Dead Letter Queue überwacht werden") |
| **enqueue** | **(einen Job) in die Queue stellen** (in + Akk.) | 3 | **BOUND** | verb | „Der Producer **stellt einen Job in die Queue** und bekommt sofort eine Job-ID zurück." · *slow the enqueue rate* → „**die Producer drosseln**" | ⛔ **einstellen** in this referent — homograph inside this very chapter, where values are *eingestellt* (§3 R3) · ⛔ *enqueuen / geenqueued* (Denglisch verb morphology, 0 attestation, class excluded by `_language.md` §1.3.2) · ⛔ *einreihen* (reflexive, animate subject) | **RECONCILED (run 1 `stellen` vs run 2 `einstellen`; I chose `stellen`)** — 3 de.wikipedia hits for the exact Fügung vs 1, **plus** the same-page homograph argument |
| **job** | **der Job** (work unit) — first mention bound | 2 | **BOUND** (paradigm + sense) / **HOUSE** (first-mention binding) | der / die Jobs / des Jobs | „**einen Job in die Queue stellen**" · „einen Job **ausführen / abarbeiten**" · „der Job **schlägt fehl**" · **die Job-ID** · *long jobs* → „**lang laufende Jobs**" | ⛔ bare *der Job* at first mention — the DWDS Wortprofil is closed labour-market (*kündigen, verlieren, suchen*), **and the collision is in the corpus**: `overview.md` writes „the **job market**" · ⛔ *der Auftrag* — run 2 measured BSI C5: `Auftrag*` **32×, all contractual** (*Auftraggeber, Auftragsverarbeitung*); run 1 adds that it collides with *request → die Anfrage* | **AGREED×2** on DWDS Bedeutung 4 (marked *IT/Telekommunikation*) + de.wikipedia lemma `Job (EDV)`. ⚠ run 2 got **404 on Duden `/rechtschreibung/Job`** — the row stands on DWDS alone |
| **pool** | **der Pool** — **never bare, always in a compound** | 2 | **BOUND** (paradigm + sense) / **HOUSE** (compound-only rule) | der / die Pools / des Pool(e)s | **der Worker-Pool**, **der Thread-Pool**, **der KV-Cache-Pool**, **der GPU-Knotenpool** · *pool is exhausted* → „**alle Threads des Pools sind belegt**" · *scale the pool out* → „**den Worker-Pool vergrößern**" | ⛔ bare *der Pool* (DWDS Wortprofil is the swimming pool; ³Pool is billiards — two wrong referents on one lemma) · ⛔ *warme Pools* for *warm pools* → **warm gehaltene Instanzen** · ⛔ **herausskalieren** (§3 R4) | **AGREED×2** (DWDS ²Pool 4c with an IT example) — but see §3 R4, where the two sheets contradict each other **inside** this row |
| **backpressure** | **Backpressure — artikellos**; rebuild permitted: **die Flusskontrolle**, **die Regelung der Datenrate** | 2 | **OPEN (Genus) — incumbent held: artikellos; closes when** a heise/iX/dpunkt/Rheinwerk sentence writes *der/das Backpressure* with an article | — / — / — | „**Backpressure greift**, sobald die Queue voll ist." · „Die Queue ist die Stelle, **an der Sie bremsen**." · Mermaid „Job-Queue<br/>(Backpressure: laufende Arbeit begrenzen)" | ⛔ *der/das Backpressure* (no article at any tier; run 1 measured de.wikipedia `insource:"Backpressure"` = **1**, and it is **soil mechanics** — *Ödometer*) · ⛔ *der Gegendruck*, *der Rückstau* (AI content-farm glossary, disqualified in canon) · ⚠ *Rückdruck* = 1 occurrence, a footnote, never a running term | **AGREED×2** + canon row. Run 2 adds the two canon-licensed rebuilds run 1 omitted |
| **load shedding** | **describe the action — no noun**: „Anfragen gezielt abweisen" | — | **OPEN — incumbent held: describe; closes when** German trade press names the action at all | — | „Ist die Queue voll, **antwortet der Dienst sofort mit `429` oder `503`** und setzt einen `Retry-After`-Header." · Mermaid „Abweisen – sofort `429` / `503` + `Retry-After`" | ⛔ **der Lastabwurf** — `insource:"Lastabwurf"` **69 : 0 Informatik**; run 1 read the distribution and found a **sense the canon does not record: aviation** (*Transall C-160*, *Airbus A400M* — dropping cargo from a transport aircraft) · ⛔ *Load Shedding* with a German article (0) · ⛔ *die Lastabweisung*, *die Überlastabwehr* (coinages) | **AGREED×2**, counter-checked from two directions (run 1: wiki distribution; run 2: BSI C5 full text = **coverage zero, not term zero**) |
| **admission control** | **describe the mechanism — no German noun** | — | **OPEN — incumbent held: describe; closes when** a T1–T3 German source names the mechanism | — | „**Schon die Annahme prüfen:** Arbeit, deren Frist beim Erreichen ohnehin abgelaufen wäre, **gar nicht erst in die Queue stellen**." · *admission path* → „**dort, wo die Anfrage angenommen wird**" | ⛔ *die Zulassungssteuerung* / *Zugangssteuerung* / *Aufnahmesteuerung* — 0 native hits; only patent translations and dictionary portals (the translation-memory class already disqualified for `Bestätigungsschritt`) · ⛔ *die Zugangskontrolle* — collides with *access control* → **die Zugriffssteuerung** (§1.2) and re-imports the banned *kontrollieren* calque | **AGREED×2** + **canon defect**: `rag.md` §2 lists `Admission Control` as *settled kept-EN* with **no §1.1 row** (run 1 K1). → CANON DELTA 1 |
| **rate limit** | **das Rate Limit** — **spaced**; process **das Rate Limiting** | 2 | **CORPUS PRECEDENT** (spelling) / **WEAK** (the loan itself, per canon) | das / die Rate Limits / des Rate Limits | „**ein Rate Limit setzen / durchsetzen**" · „**pro Team ein eigenes Rate Limit**" · „**unter dem Rate Limit des Anbieters bleiben**" · „**Rate Limits vor das gemeinsame Kontingent setzen**" | ⛔ *die Ratenbegrenzung* (only MDN de + MS Learn de-de → §1.1 Falle 4) · ⛔ *die Durchsatzratenbegrenzung* (a de.wikipedia lemma that occurs nowhere outside its own article) | **RECONCILED (run 1 `das Rate-Limit` hyphenated vs run 2 `das Rate Limit` spaced; I chose spaced)** — §3 R7. **CORPUS(1)** + canon row, against a rule-level argument |
| **quota** | **das Kontingent** — always with a possessor attribute | 3 | **WEAK — incumbent held; closes when** a heise/iX/INNOQ/BSI sentence inflects *Kontingent* with an API allowance as its referent | das / die Kontingente / des Kontingent[e]s | „**das Kontingent des Anbieters**" · „das gemeinsame Kontingent **ausschöpfen**" · „Kontingente gelten **je Region und je Modell**" · fallback: „**wie viele Anfragen pro Minute der Anbieter zulässt**" | ⛔ **die Quote** — triple: Duden `Quote` is a **share/ratio**, not a stock; `rag.md` §4 already licenses „die Quote" as an anaphor for an **error rate**; and the shipped corpus **uses it that way** („senken **die Quote** um 35 %") · ⛔ *das Limit* here (§1.1.a reserves *Limit* for the **set** value; a quota is the **stock**) | **AGREED×2** for the ruling, but the ⛔ is now **CORPUS(1)**; the positive side is **WEAK** — Duden carries word and sense, no German IT text carries the referent |
| **retry** | noun **die Wiederholung** · verb **wiederholen** · `Retry-` only as a compound former | 3 / 1 | **CORPUS PRECEDENT** | die / die Wiederholungen / der Wiederholung | „**die Zahl der Wiederholungen begrenzen**" · „**eine Obergrenze für Wiederholungen (Retry-Budget)**" (shipped verbatim) · „nach **erschöpften Wiederholungen**" · **`Retry-After`** = class 1, code-styled | ⛔ *ein Retry* (canon `Retry` row: **OPEN (Genus)**, compound-former only) · ⛔ *retryen* · ⛔ **die Retry-Steuer / die Wiederholungssteuer** for *retry tax* — `rag.md` §3 struck the twin figure *token tax* („nicht übernehmen") ⇒ **„die Mehrkosten der Wiederholungen"**; in the image `alt` text „…, mit **den markierten Mehrkosten der Wiederholungen**" | **CORPUS(37)** — 20 noun + 17 verb forms shipped, including the exact collocation. Strongest row in the slice |
| **timeout** | set value → **das Timeout** · raised error → **die Zeitüberschreitung** · **die Zeitbeschränkung** = optional disambiguator only | 2 / 3 | **CORPUS PRECEDENT** — and this **overrides both sheets' lead form** (§3 R5) | das / die Timeouts / **des Timeouts** (shipped) | „großzügige, ausdrückliche **Timeouts** setzen, und **je Stufe** ein eigenes" · „Arbeit, die **das Timeout des Clients** ohnehin schon gerissen hat" · „**Fehler- und Zeitüberschreitungsraten**" · *graceful timeout* → „**die Zeitbeschränkung für das geordnete Herunterfahren**" | ⛔ **die Zeitüberschreitung for a configured value** — the canon calls this a **Bedeutungsfehler, not a style question**; it would be wrong 8–9 times in Part III · ⚠ DWDS `Zeitüberschreitung` has a **sport** Wortprofil (Disqualifikation, Strafe) | **CORPUS(5)** — „**Zeitüberschreitung** – das Tool hat innerhalb **seines Timeouts** nicht geantwortet" ships both halves in one sentence, genitive included. `Zeitbeschränkung` = **0 shipped** |
| **async** | keyword `async`/`await`/`asyncio` = class 1, code-styled · adjective **asynchron** · *async-first* → **von Grund auf asynchron** | 1 / 3 | **BOUND** | adjective | „ein **asynchroner** Server / Worker" · „**asynchrone** Ingestion" · „eine blockierende Operation in einem **`async`-Handler**" · „die **Ereignisschleife** blockieren" | ⛔ *das Async* as a noun (no gender at any tier) · ⛔ *asynchron-erst* (calque of *async-first*) · ⛔ *einfrieren* for a blocking call (brief §5: asserts deliberate action — a factual error) | **AGREED×2**. ⚠ `asynchron` is **0 in the shipped corpus** (which writes `nebenläufig` 18×) — the word is new, though ordinary |
| **streaming** | **das Streaming**; participle **gestreamt** | 2 | **BOUND** | das / — / des Streamings | „**Streaming über SSE**" · „die Antwort **streamen**" · „eine **gestreamte** Antwort" · **die Streaming-Antwort** | ⛔ *die Datenstromübertragung*, *das Strömen* (coinages) | **RECONCILED (run 1 SETTLED vs run 2 WEAK; I chose run 1)** — §3 R6. Run 1 quotes the **Duden noun lemma, marked EDV**; run 2 states it did not look the lemma up. Evidence beats a declared non-lookup. Corpus ships `Streaming` 4× + `gestreamt`, all article-free |
| **time to first token / TTFT** | first mention **die Zeit bis zum ersten Token** (*time-to-first-token*, **TTFT**); thereafter **TTFT**; where an article is forced **der TTFT-Wert** | 3 + 1 | **BOUND** (construction) / **WEAK** (the German full form) | der TTFT-Wert / — / des TTFT-Werts | „…**die Zeit bis zum ersten Token** – die Stille, bevor überhaupt etwas erscheint" · „**der TTFT-Wert steigt**" | ⛔ **die Zeit bis zur ersten *Antwort*** — the only German attestation (run 2: `it-kenner.heise.de`) writes *Antwort*, and in **this** lesson that is a **factual error**: the point is that the first token arrives long before the answer · ⛔ bare *das/der TTFT* (no gender attested) · ⛔ *die Erst-Token-Zeit* | **RECONCILED** — same full form both runs; run 2 supplies the attestation **and** the deliberate, argued deviation from it. Grade: **WEAK** (heise B2B/partner channel, not the newsroom) + **CORPUS(3)** for the bare abbreviation |
| **tail latency** | **die Latenz der langsamsten Anfragen** / **die Latenz im 95. Perzentil** / **der p99-Wert** | 3 | **OPEN — incumbent held: rebuild; closes when** a T1–T3 German source names the concept | — | „…und es endet damit, dass **die Latenz der langsamsten Anfragen aus dem Ruder läuft**: jenseits der Kapazität explodiert die Wartezeit in der Queue und **der p99-Wert schießt in die Höhe**." · „**die langsamsten 5 % der Anfragen**" | ⛔ **die Ausreißer** (canon: a **factual** falsification — outliers are anomalies, the tail is regular but rare) · ⛔ *die Tail-Latenz* (only German hits: an AI content farm, expressly disqualified) — **and now also because `Tail` is a live kept-EN token in this book for sampling** · ⛔ **„der p99-Wert bricht ein / fällt über die Klippe / fällt ins Bodenlose"** — §3 R8 | **RECONCILED (run 1 wrote the construction run 2 bans; I chose run 2)** + canon `rag.md` §3 |
| **percentile** | **das Perzentil**; `p50` / `p95` / `p99` class 1 | 3 / 1 | **CORPUS PRECEDENT** | das / die Perzentile / des Perzentils | „**die Latenz in den Perzentilen `p50` und `p95`**" · with an article, durchgekoppelt: **der p95-Wert** | ⛔ *das 95te / 95-te Perzentil* · ⛔ capitalised `P95` | **AGREED×2** + **CORPUS(10)** for the identifiers — which closes run 2's „`p50` missing from `rag.md` §1" gap |
| **tier** | **the loan is never written appellatively.** Per sense: (a) **der Tarif** · (b) **das Angebot** · (c) class 1 · (d) **die Anwendungsschicht** · (e) **die Modellklasse** · (f) does not occur | 3 (a,b,d,e) / 1 (c) | **BOUND for the ⛔** / per-sense below (§2) | see §2 | see §2 | ⛔ **der/das/die Tier** appellatively — **both Duden senses are the animal**; a reader meets „das Batch-Tier" as *the batch animal*. The loan survives **only bound** (`Tier 1`, `3-Tier-Architektur`) — **and that is exactly what our own corpus ships** (`Tier 1`/`Tier 2`, 2×) · ⛔ *die Tier-Stufe*, *das Tier-Modell* | **AGREED×2 on the ⛔** (Duden + de.wikipedia *Tier (Begriffsklärung)*, loan senses only bound) + **CORPUS(2)**. **Sense assignment: RECONCILED** — the two sheets built different tables (§3 R9) |
| **batch tier** | **der Batch-Tarif** (*batch tier*) — **English parenthesis obligatory at first mention** | 2/3 | **THIN×2** — see the warning below | der / die Batch-Tarife / des Batch-Tarifs | „die Arbeit **über den Batch-Tarif** laufen lassen" · „**der halb so teure Batch-Tarif**" | ⛔ *das Batch-Tier* · ⛔ *die Batch-Stufe* (`die Stufe` is occupied 55× in the shipped corpus) · ⛔ *der Batch-Betrieb* / *die Betriebsart* (§3 R9b) · ⛔ *die Stapelverarbeitung* (names the **procedure**; would flatten the distinction the corpus draws twice) | **THIN×2 / COINED (probation)** — de.wikipedia `insource:"Batch-Tarif"` = **0**; the head noun rests on **one Duden page**; the two runs coined **different** words. See the box below |

> ### ⚠ `der Batch-Tarif` — the slice's own declared blind spot, carried forward unflattened
>
> Run 2 pre-registered the failure mode in its own sheet: *„wenn Run 1 zu demselben Wort gekommen ist, ist das
> kein Beleg, sondern derselbe blinde Fleck zweimal — beide Durchgänge lesen dieselbe Duden-Seite."*
> **Run 1 did not come to the same word** (it chose `der Batch-Betrieb`). So this row does not even have the
> false comfort of agreement:
> - What the two runs **do** agree on is a **null**: German has **no attested noun** for a cloud pricing tier.
>   Run 1: `insource:"Preisstufe" insource:"Cloud"` = 0. Run 2: `insource:"Preisstufe"` = 95, all
>   **Verkehrsverbund** fare zones; `insource:"Tarifstufe"` = 17, all **tax brackets / local transit**;
>   `insource:"Batch-Tarif"` = 0.
> - The positive side rests on **`_language.md`'s tier-1 shape with a tier-2 body**: one Duden entry for
>   `Tarif` („festgesetzter Preis; Entgelt, Gebühr für etwas (z. B. für die Inanspruchnahme von
>   Dienstleistungen)", example „für Großkunden gilt ein besonderer, **verbilligter Tarif**") plus a
>   §1.3.3 spelling licence for the compound. **That is one source. Label: `THIN×2`, not `AGREED×2`.**
> - **Why I still bind it over run 1's `der Batch-Betrieb`:** run 1 rejected `die Stapelverarbeitung`
>   precisely because it *„benennt das Verarbeitungsverfahren und würde genau die Unterscheidung einebnen,
>   die der Korpus zweimal ausdrücklich zieht"* — and then chose `Betrieb`/`Betriebsart`, which has the same
>   defect: it names a **mode of operation**, not a **price**, while the corpus says in as many words that
>   „batch mode is a **pricing** tier at the API level". The choice is settled by an internal contradiction in
>   run 1, **not by evidence**. Additionally `Betrieb` is occupied in the shipped corpus (12×, *Produktivbetrieb*).
> - **Closing condition:** any T1–T3 German source (heise/iX/c't/INNOQ/dpunkt/Rheinwerk/BSI) that inflects a
>   noun for a cloud **pricing** tier. A renderer that finds one should report it, not adopt it silently.

| Terminus | German | Class | Status | Artikel / Plural / Genitiv | Kollokation | ⛔ rejected | Evidence grade |
|---|---|---|---|---|---|---|---|
| **interactive tier** | **does not exist** — the corpus contrast is adjectival, **interaktiv ↔ Batch** | 3 | **NULL FINDING, verified twice** | — | „**Arbeit, die warten kann, soll nicht den interaktiven Preis zahlen.**" · „**nicht interaktive** Lasten" (two words, `nicht` uninflected — precedent *nicht vertrauenswürdig*) · „Nicht alle Arbeit mit dem Modell ist **interaktiv**." | ⛔ inventing „die interaktive Stufe" / „der interaktive Tarif" — the English source has no such term, and a merge pass must not decide what is not there | **AGREED×2** (`grep -roi "interactive tier"` = 0 in both runs; counter-probe `interactive` = 3, all adjectival). ⚠ `interaktiv` = **0 in the shipped corpus** — new but ordinary |
| **batch API** | **die Batch-API**; vendor names class 1 (`die Azure Batch API`) | 2 / 1 | **DISPUTED (inherited)** — the gender hangs on the `API` row, which `_language.md` §1.1.a carries as DISPUTED with incumbent **die**. **Do not reopen here.** | die / die Batch-APIs / der Batch-API | „**die Batch-API des Anbieters**" · „Wenn **die Batch-API passt** – unabhängige Anfragen, Ergebnisse innerhalb eines Tages –, **nehmen Sie sie**" | ⛔ *das Batch-API* (would break the incumbent inside one page — the loudest MT signal) · ⛔ *die Batch API* spaced (§ 45 E1: noun+noun ⇒ hyphen) · ⛔ *die Stapel-API* | **AGREED×2** on substance (run 1 labelled it WEAK, run 2 DISPUTED — the same thing said twice) |
| **wait / waiting** | verb **warten**, **`auf` + Akk. obligatory when the subject is a thing that can be *maintained*** · attribute **wartend** · nominalisation **das Warten** | 3 | **BOUND**, with the rection rule refined against the corpus (§3 R10) | verb / — / — | „**Der Dienst wartet die meiste Zeit auf das Modell.**" · „**hunderte wartende Anfragen** verschränken" · title formula, 3× in the corpus, never varied: „**die Arbeit, die warten kann**" | ⛔ **die Wartung** as the nominalisation — `die Wartung` is exclusively *maintenance*, and the shipped corpus proves the field is live (`Wartungsmodus`) · ⛔ objectless „der Dienst/der Server/der Worker wartet" | **RECONCILED** — run 1 found the noun trap, run 2 found the Duden Bedeutung 2 verb trap; the corpus then narrowed run 2's blanket rule (it ships objectless `wartet` 4× — with subjects like *Aufruf*, *Durchlauf*, *Halluzination*, none maintainable) |
| **bounded / bound** | four senses, four constructions — see §2 | 3 | **BOUND for (a), (c), (d)** / **OPEN for (b), partially closed** | — | see §2 | ⛔ **„die Nebenläufigkeit binden"** — the most expensive calque in this slice: German *binden* = *tie/oblige*, not *limit*; „die Arbeit binden" reads as *contractually obliging the work*. Fluent German on an English collocation skeleton — the wave-2 *auf der Leitung* shape · ⛔ *eine gebundene Queue* (meaningless) · ⛔ *E/A-gebunden, I/O-lastig, speicherbandbreitenbegrenzt* (0/0/0/0, run 2) | **CORPUS(28)** for (a) (`begrenzen`/`begrenzt`/`unbegrenzt`) + **RECONCILED** for (b) — run 2's measurement `insource:"rechenintensiv"` = **54** closes *compute-bound* alone (§3 R11) |
| **concurrency cap / ceiling** (the corpus head is **not** *limit*) | **die Obergrenze für die Nebenläufigkeit** | 3 | **CORPUS PRECEDENT** for `Obergrenze` / **BOUND** for the compound | die Obergrenze / die Obergrenzen / der Obergrenze; **die Nebenläufigkeit**, Pl. avoid | „**eine Obergrenze für die Nebenläufigkeit setzen**" · „**je Mandant eine eigene Obergrenze**" · Mermaid „Semaphor – Obergrenze für die Nebenläufigkeit: N" · **der Semaphor**, des Semaphors, die Semaphore | ⛔ *das Concurrency-Limit* (no gender attested; and §1.1.a reserves *Limit* for the **set** value — a compound would create a second name for one referent) · ⛔ *die Parallelität* as the running term — de.wikipedia carries it as a **variant of the same lemma**, and Part III needs *Parallelität* for **tensor/pipeline/data parallelism** in the same lesson · ⛔ *die Gleichzeitigkeit* | **AGREED×2** + **CORPUS(41)** for `Obergrenze für` + Akk. `concurrency limit` itself = **0 occurrences, verified twice**; the corpus writes `concurrency cap` (2), `Concurrency caps` (1), `concurrency ceiling` (1) |
| **drain** | (a) a queue → **abarbeiten** · (b) in-flight connections at SIGTERM → **zu Ende bedienen** · (c) a pipeline bubble → **leerlaufen** | 3 | **BOUND** (three senses, three verbs) — no noun | verb | (a) „**Ein Pool von Workern arbeitet die Queue ab**, so schnell, wie Hardware und die Rate Limits des Anbieters es erlauben." · (b) „Bei `SIGTERM` soll der Server **keine neuen Verbindungen mehr annehmen und die laufenden zu Ende bedienen**." · *drain window* → „**das Zeitfenster für das geordnete Herunterfahren**" | ⛔ **die Queue leeren / entleeren / abfließen lassen** — says *discard the contents*, the opposite of working it off; container-and-plumbing register · ⛔ **drainieren / die Drainage** — Duden: **medicine** (wound drainage) and **agriculture** (land drainage). ⚠ run 2 flags honestly that it never fetched the `drainieren` lemma; run 1 did — the ⛔ is **attested**, not HOUSE · ⛔ *der Drain* | **RECONCILED** — run 1 found 2 senses, run 2 found 3 (the pipeline bubble); I keep 3. **CORPUS(2)** for `abarbeiten` („einzeln **abarbeiten**") + Duden `abarbeiten` Bedeutung 1.2 |
| **shed** | **abweisen** (+ Akk.) as the running verb; „**Last abwerfen**" only where the canon gloss is quoted | 3 | **BOUND** (verb) / **OPEN** (noun — see `load shedding`) | verb | „**Überschüssige Anfragen weisen Sie mit `429` und `Retry-After` ab.**" · „Wenn das Alter des ältesten Jobs eine Schwelle überschreitet, **weisen Sie Last ab**." · Mermaid „Abweisen – sofort `429` / `503` + `Retry-After`" | ⛔ *abwerfen* as the **running** verb (drags in `Lastabwurf` ⇒ power grid + aviation, 69 : 0) · ⛔ *abwerfen* **without** *Last* (aircraft/ballast) · ⛔ *abstoßen* (organ rejection / divestment), *ausschleusen* (logistics/medicine) | **RECONCILED (run 1 banned *abwerfen* outright, run 2 licensed it from `rag.md` §3; I split it)** — §3 R12 |
| **priority** | **class 1, unflected**: **die Stufe `Priority`**, **der Tarif `Priority`** | 1 | **BOUND** | — | „**Vertex bietet Provisioned Throughput über `Standard`, einen etwa 1,8-fach teureren Tarif `Priority` und einen etwa halb so teuren `Flex-Batch`.**" | ⛔ *die Prioritätsstufe*, *der Vorrang-Tarif* — that **translates a proper name** (precedent: ⛔ „die goldenen Signale" for `Golden Signals`), and `Vorrang` is already occupied in the shipped corpus by **Priority-Sampling** („bei einer **Vorrangregel**") | **AGREED×2** — both occurrences are vendor price-tier names (Bedrock „Reserved, Priority, Standard, Flex"; Vertex „a roughly 1.8× Priority tier"). `priority queue` = **0**, verified ⇒ `Vorrangwarteschlange` is **not decided here** |

**Held over, reported not decided (they belong to other slices, but this slice's sentences need them):**
`der Worker` (shipped 43×, kept-EN), `der Producer` / `der Consumer` (0 shipped — Mermaid labels), `der Mandant`
(*tenant*; shipped 3×, n-declension `des Mandanten`), `der Semaphor` (0 shipped), `graceful shutdown`
(**OPEN**, incumbent held: „**das geordnete Herunterfahren**"), `poison job` (⛔ *der Giftjob*, ⛔ any
*Vergiftung* wording — that would import the **security** frame of `Tool Poisoning` / `poisoned documents`;
running form „**ein Job, der immer wieder scheitert und die Queue verkeilt**").

---

## 2. Sense cards

Each card gives **the question to ask before writing** and **a worked German sentence per branch**. A sense
split that ships only a word gets dodged; one that ships a sentence survives contact with prose.

### 2.1 `tier` — 30 occurrences, six referents, and the loan is unwritable in all six

> **Question before writing: am I talking about a PRICE, an OFFERING, a PRODUCT NAME, an ARCHITECTURE LAYER,
> a MODEL CLASS, or a MATURITY LEVEL? And the answer is never „Tier".**

The pre-decision that governs all six: `das Tier` is the everyday German word for **animal**, learned before
school. This is not the `Log` / `Service` shape (a loan whose dictionary sense is merely wrong) — the string
collides with core vocabulary. „das Batch-Tier" reads as *the batch animal*. The loan survives **only bound**
(`Tier 1`, `3-Tier-Architektur`) — the Kompositumsbildner class — **and that is precisely how our own shipped
corpus uses it** („SDKs auf **Tier 1**, Java und Rust auf **Tier 2**"), a form Part III never needs.

| # | Referent (English surface) | ~n | German head | **Worked sentence** | Status |
|---|---|---|---|---|---|
| **(a)** | **price / billing** — *batch tier, pricing tier, half-price tier, the cheapest tier the platform will sell you, service tier, committed-use tiers* | ~16 | **der Tarif** | „**Batch ist der günstigste Tarif, den die Plattform Ihnen verkauft** – rund der halbe Preis gegen ungefähr 24 Stunden Vorlauf." · „Für unabhängige Anfragen mit Ergebnissen binnen eines Tages nehmen Sie die Batch-API des Anbieters: sie läuft über **den halb so teuren Batch-Tarif** (*batch tier*), und Sie müssen keine Worker betreiben." | **THIN×2** (see box in §1) |
| **(b)** | **offering / packaged product** — *the managed RAG tier, the packaged grounding tier, managed tiers, Developer tier, serverless tier, a third tier* | 7 | **das Angebot** (preferred) — ⛔ bare **die Stufe** | „Jede Plattform verkauft außerdem **ein verwaltetes RAG-Angebot** – die Pipeline aus Teil I als fertigen Dienst." · „Viele Teams wachsen aus **dem verwalteten Angebot** heraus oder behalten es nur für Ingestion und Ablage." | **RECONCILED** — run 1 chose `das Angebot`, run 2 offered `die Stufe / die Ebene / das Angebot`. The corpus decides: `Stufe` is occupied **55×** as *rung/stage* („nehmen Sie **die einfachste Stufe**"), `Ebene` **35×** as *abstraction level*, `Angebot` **1×**. The least-occupied word wins |
| **(c)** | **vendor price-tier names** — *Reserved, Priority, Standard, Flex, Flex-Batch, Developer, Global Standard* | 5 | **class 1** — the name stays English and unflected; a German head noun carries article and case | „… nachdem Bedrock seine Preise im November 2025 in **die Stufen `Reserved`, `Priority`, `Standard` und `Flex`** umgebaut hat." — here *die Stufen* is only the counting frame, **not** the terminus | **BOUND** (class 1) |
| **(d)** | **architecture layer** — *a stateless app tier plus an async worker* | 1 | **die Anwendungsschicht** — the **compound**, never bare `die Schicht` | „Was bleibt, ist die **Form**: **eine zustandslose Anwendungsschicht** plus ein asynchroner Worker, ein OLTP-Speicher für die Konfiguration, ein OLAP-Speicher für die Telemetrie, **eine Queue zur Entkopplung der Ingestion** und Objektspeicher für die Rohdaten." | **BOUND** — de.wikipedia *Schichtenarchitektur* („einzelne Aspekte … werden konzeptionell **einer Schicht** (engl. *tier* oder *layer*) zugeordnet") — the §1.1.g signature: German lemma, English in the bracket |
| **(e)** | **model class in routing** — *model-tier routing* | 1 | **die Modellklasse** | „Das Zweite ist **das Routing nach Modellklasse**, von der Taktik zur Regel erhoben: billiger Verkehr geht per Voreinstellung an ein billiges Modell, das Spitzenmodell muss begründet angefordert werden." | **BOUND** (ordinary German compound; `Modellklasse` = 0 in the shipped corpus, so no collision) |
| **(f)** | **maturity level** — *maturity tiers, enterprise tier* | **0 in Part III** | **der Reifegrad** — **DO NOT IMPORT** | (reference only: `ai-sdlc.md` „die drei **Reifegrade** (Einzelperson · kleines Team · Enterprise)", shipped as `Enterprise-Reifegrad`) | **DECIDED NOT TO REUSE.** Verified twice: `maturity tier` = 0, `enterprise tier` = 0 in Part III. Run 1 logged it as a peek-don't-load reuse; run 2 checked the sense and found it is a **maturity** referent, not a price or an offering. Recorded so a later pass does not read the absence as a gap |

**The corpus's own collision warning must *carry* the distinction in German, not merely repeat it** — in
English `batch` collides with `batching`; in German nothing collides once (a) and the kept-EN term stand side
by side:

> „Die Warnung aus Teil 1 ist es wert, wiederholt zu werden, weil das Wort kollidiert: **dieses Batch ist ein
> Abrechnungstarif auf API-Ebene, nicht das `Continuous Batching` aus der Serving-Lektion** — das ist ein
> GPU-Scheduler, der etwas völlig anderes tut."

### 2.2 `queue` — 45 occurrences, four referents, and the canon split does not bite here

> **Question before writing: am I pointing at a concrete thing in the running system, or talking about the
> FIFO principle? And: is it even a noun?**

| Referent | n | German | **Worked sentence** |
|---|---|---|---|
| **concrete runtime object** — Redis queue, ingestion queue, event queue, job queue, DLQ, per-tenant queues, **and the in-process bounded queue behind the semaphore** | **45 of 45** | **die Queue** | „Das Gegenmittel ist **Backpressure**: Begrenzen Sie die Nebenläufigkeit bewusst mit einem Semaphor, der die gleichzeitigen Generierungen deckelt, und stellen Sie **eine begrenzte Queue mit einer festen Höchstlänge** dahinter." · „**Die Job-Queue** trennt die Rate, mit der Arbeit ankommt, von der Rate, mit der sie verarbeitet wird." |
| **the data structure / the FIFO principle** | **0 in Part III** | **die Warteschlange** (de.wikipedia lemma) | „Eine **Warteschlange** arbeitet nach dem Prinzip *first in, first out*." — recorded so the branch is not deleted as unused; **it has no Part III occurrence** |
| **verb** *to queue* | 2 | **sich stauen** / **warten** | „Unter Last versagt es subtiler: der Pool ist erschöpft, und **weitere Anfragen stauen sich und warten auf einen freien Thread**." |
| **`queueing delay`** | 2 | **die Wartezeit in der Queue** | „Jenseits der Kapazität explodiert **die Wartezeit in der Queue**." |

**Mermaid labels are translated prose, not an English diagram** ⇒ German (§1.3.3's last bullet does **not**
apply). The five labels, bound:

```
SEM["Semaphor – Obergrenze für die Nebenläufigkeit: N"] --> Q{"Begrenzte Queue<br/>max. Länge D"}
Q -->|"Queue voll"| SHED["Abweisen – sofort 429 / 503 + Retry-After"]
P["Producer<br/>einstellen → Job-ID"] --> Q["Job-Queue<br/>(Backpressure: laufende Arbeit begrenzen)"]
WP -->|"Wiederholungen aufgebraucht"| DLQ["Dead-Letter-Queue<br/>(Alarm bei Wachstum)"]
Q -.->|"Alter des ältesten Jobs hoch"| SHED["Last abweisen: 429 / Producer drosseln / Worker-Pool vergrößern"]
```

⚠ The third label keeps the English operation name in the producer box only because `enqueue` is the
**operation name** there; in prose the verb is „in die Queue **stellen**". If the label is read as prose,
render it `P["Producer<br/>in die Queue stellen → Job-ID"]`. **Flagged, not silently varied.**

### 2.3 `job` — three referents, and two of them are not jobs

> **Question before writing: can I put this thing in a queue?**

| Referent | n | German | **Worked sentence** |
|---|---|---|---|
| **yes — a unit of work** | ~32 | **der Job** (bind at first mention) | „**Ein Job** – eine Arbeitseinheit, die die Queue trägt – läuft bei einem LLM Sekunden bis Minuten, nicht Millisekunden, und das dehnt das Zeitfenster, in dem ein Worker mitten in der Bearbeitung sterben kann." |
| **no — a responsibility** (*that is RAG's job*, *dataset quality stays your job*, *one word, two jobs*) | ~11 | **die Aufgabe** / **zuständig sein** | „Wissen aktuell zu halten ist **die Aufgabe des Retrievers**, und keine noch so gute Feinabstimmung ersetzt eine neue Ingestion." · „‚Serving' verbirgt **zwei verschiedene Aufgaben**, und sie zu vermischen ist der schnellste Weg, sich in diesem Thema zu verlieren." |
| **no — the labour market** (`overview.md`: „the **job market** names by tool") | 1 | **der Arbeitsmarkt** | „**Der Arbeitsmarkt** benennt diese Rollen nach Werkzeugen." |

⚠ **This third branch is the whole reason the first-mention binding is mandatory.** Run 2 collapsed it into
sense (b); run 1 kept it separate and is right — the collision is not hypothetical, it is printed on the
first page of the part.

### 2.4 `bound / bounded` — 27 + 6 occurrences, four referents, four constructions

> **Question before writing: am I setting an UPPER LIMIT, naming the BOTTLENECK, staking out a SCOPE, or
> OBLIGING somebody?**

| # | Referent | n | German | **Worked sentence** |
|---|---|---|---|---|
| **(a)** | set an upper limit — *bound concurrency, bound the retry count, bounded queue, unbounded concurrency, bounding the in-flight work* | ~14 | **begrenzen / beschränken** (+ Akk.); adjective **begrenzt / unbegrenzt**; noun **die Obergrenze** | „**Begrenzen Sie sie** mit einem Semaphor und **einer begrenzten Queue**, weisen Sie den Überschuss mit `429` und `Retry-After` ab, und setzen Sie **die Obergrenze** an der knappen GPU oder dem Anbieter-Slot, nicht an der billigen Verbindung." · „**Unbegrenzte Nebenläufigkeit** zerlegt einen LLM-Dienst auf drei Arten gleichzeitig." |
| **(b)** | name the bottleneck — *I/O-bound, compute-bound, memory-bandwidth-bound, resource-bound* | 9 | **no compound — say the bottleneck in a clause.** *compute-bound* alone has a German word | „**Prefill** verarbeitet den ganzen Prompt in einem Durchgang und ist **rechenintensiv**." · „**Decode** gibt pro Schritt ein Token aus, liest dabei jedes Mal Gewichte und KV-Cache neu und **wird durch die Speicherbandbreite begrenzt**." · „Die Last **wartet fast nur auf Ein- und Ausgabe** – deshalb passt ein von Grund auf asynchrones FastAPI dazu." · „Diese Arbeit ist **durch die verfügbaren Ressourcen begrenzt** und langsam." |
| **(c)** | stake out a scope — *profiles bounded to US, EU, or APAC* | 1 | **beschränkt auf** (+ Akk.) | „… Profile, die **auf die USA, die EU oder APAC beschränkt** sind, gegen globale Profile" |
| **(d)** | oblige — *a decision an organisation is bound by* | 1 | **binden — and ONLY here** | „Dieser Abschnitt besitzt das, was aus diesen Zahlen eine Entscheidung macht, **an die sich eine Organisation bindet**: die **Fehlerbudget-Richtlinie**." |

⚠ **(b) remains OPEN as terminology, but is now partially closed.** Run 2 measured
`insource:"rechenintensiv"` = **54** ⇒ *compute-bound* **does** have a German adjective and should use it.
`insource:"I/O-lastig"` / `"E/A-lastig"` / `"ein-/ausgabelastig"` / `"speicherbandbreitenbegrenzt"` = **0 / 0
/ 0 / 0** ⇒ those three stay clauses. *Closing condition:* an inflected sentence at heise/iX/c't/INNOQ/dpunkt
with a German adjective for *I/O-bound* or *memory-bandwidth-bound*.

### 2.5 `timeout` — two referents, and Part III hits both

> **Question before writing: is it the value that was set, or the error that fired?**

| Referent | n | German | **Worked sentence** |
|---|---|---|---|
| **the configured value** | 8–9 | **das Timeout** (shipped incumbent); **die Zeitbeschränkung** only where a sentence must contrast value against error | „Setzen Sie ausdrückliche, großzügige **Timeouts**, und setzen Sie sie **je Stufe**: ein Retrieval-Aufruf und ein Modellaufruf verdienen unterschiedliche." · „… Arbeit, die **das Timeout des Clients** ohnehin schon gerissen hat, gar nicht erst in die Queue stellen." |
| **the raised error** | 1–2 | **die Zeitüberschreitung** | „Das klassische Panel trägt weiter: Latenzperzentile (`p50`/`p95`), **wie oft Fehler und Zeitüberschreitungen auftreten**, …" |

⚠ The two runs split 9/1 and 8/2 on the counts (the disputed unit is *„no timeout … just hangs"*). **The
count does not change the rule** — classification is per occurrence — but it is recorded because a renderer
that mechanically writes „Zeitüberschreitung" is wrong eight or nine times, which the canon calls a
**Bedeutungsfehler, not a style question**.

### 2.6 `drain` — five occurrences, three referents, three verbs

> **Question before writing: is a STORE being worked off, is in-flight work being FINISHED, or is a pipeline
> RUNNING EMPTY?**

| Referent | n | German verb | **Worked sentence** |
|---|---|---|---|
| work a queue off | 3 | **abarbeiten** (+ Akk.) | „**Ein Pool von Workern arbeitet die Queue ab**, so schnell, wie Hardware und die Rate Limits des Anbieters es erlauben." · „**Langfuse Worker** – ein asynchroner Worker, der **die Ereignis-Queue abarbeitet** und Hintergrund-Jobs erledigt." |
| finish in-flight work (SIGTERM, orderly shutdown) | 1 + *drain window* | **zu Ende bedienen** (connections) / **zu Ende bearbeiten** (jobs) | „Bei `SIGTERM` soll der Server **keine neuen Verbindungen mehr annehmen und die laufenden zu Ende bedienen** – innerhalb eines Timeouts, das kürzer sein kann als ein LLM-Stream." · *drain window* → „**das Zeitfenster für das geordnete Herunterfahren**" |
| a pipeline bubble empties | 1 | **leerlaufen** | „Die Pipeline **füllt sich und läuft wieder leer**." |

---

## 3. RUN DISAGREEMENTS

Every place the two blind runs differ, both positions, my resolution and its reason. **Reversals are recorded,
not overwritten.**

**R1 — `queue`: retire the canon split, or keep it? (the slice's largest row, 45 occurrences, a whole
section, five Mermaid labels)**
*Run 1:* **retire it.** Its K4 shows the split's own cited source does not support a referent boundary:
de.wikipedia's `Message Queue` is a **redirect to `Warteschlange (Datenstruktur)`** (API-checked);
`Nachrichtenwarteschlange` and `Message-Queue` do not exist; the data-structure page itself writes „Gibt **die
Queue** als Text zurück"; and broker prose writes both words on one page (adesso: „reiht sie **in eine
Warteschlange** ein" beside „holt sich … **aus der Queue**"). Proposed the bridge pattern — gloss once, then
kept-EN — status **SETTLED**.
*Run 2:* **keep it, rename its criterion.** Status **WEAK**. Its Kollision 6: the strongest German source for
a *concrete* job queue writes `Warteschlange` (iX/heise on Slurm: „stellt es die Anfrage automatisch **in die
Warteschlange**"), while heise/AMQP writes `Queue` 8× and `Warteschlange` 0×. So the boundary is not
concrete-vs-abstract but **broker/messaging register vs scheduler/everyday register**. Explicitly declined to
propose a flip.
*My resolution:* **the operative instruction is identical either way — `die Queue`, 45 of 45** — because run
2 itself verifies the data-structure branch has **zero** Part III occurrences. So I bind `die Queue`
everywhere, adopt run 1's **first-mention bridge gloss** („die Queue (Warteschlange)"), and adopt run 2's
**corrected criterion** for the canon row. I do **not** flip the canon row from a slice: run 1's redirect
finding is the strongest single argument in either sheet and goes to **CANON DELTA 3** as a report.
*Why:* the shipped corpus has **`Queue` 0 / `Warteschlange` 0** — the split has never been exercised, so
nothing is being protected by keeping it and nothing is being broken by not using it. Deciding the canon
question is stage 2's call, not this slice's.

**R2 — `queue depth`.** Run 1: **die Warteschlangenlänge**, SETTLED on 8 de.wikipedia hits in queueing theory
(*Random early detection*, *Kendall-Notation*, *Pollaczek-Chintschin-Formel*). Run 2: **die Länge der Queue**,
with the same 8 hits cited only to kill *Queue-Tiefe*.
*Resolution: `die Länge der Queue`.* Both Part III occurrences are **autoscaling signals**, not queueing-theory
quantities, and after `die Queue` is introduced a switch to `Warteschlangen-` is exactly the
Richtungswackeln §1.0 forbids. `die Warteschlangenlänge` stays licensed for a queueing-theory passage — Part
III has none. *Cost of being wrong:* nil; both are transparent.

**R3 — `enqueue`: `stellen` or `einstellen`?** Run 1: **in die Queue stellen** (de.wikipedia: „Jobs in die
Queue **zu stellen**" *At (Unix)*, „wird **in die Queue gestellt**" *Neighbor Discovery Protocol*, „**stellt
sie in die Queue**" *HotSpot*; plus one *einstellt*). Run 2: **in die Queue einstellen** (de.wikipedia
*Warteschlange (Datenstruktur)*: „So können **Aufgaben eingestellt** werden"; iX/Slurm).
*Resolution: `in die Queue stellen`.* Two reasons: 3 direct attestations of the exact Fügung against 1; and —
the decisive one, which neither sheet raised — **`einstellen` is a homograph inside this very chapter**, where
values are *eingestellt* („das eingestellte Timeout", §2.5) and where `einstellen` additionally means *cease*
and *hire*. Run 2's own `job` row writes „einen Job **einstellen**", which in a German operations chapter can
read as *hire someone*. *Cost of being wrong:* low; `einstellen` remains attested and would not be an error,
only a second name.

**R4 — `pool`, inside one row, the two sheets contradict each other: `herausskalieren`.** Run 1 uses it twice
as a worked collocation („der Worker-Pool wird **herausskaliert**", „den Worker-Pool **herausskalieren**").
Run 2 lists **⛔ *herausskalieren* (Kalk von *scale out*)** and gives „**den Worker-Pool vergrößern**".
*Resolution: run 2.* `herausskalieren` is an unattested morpheme-by-morpheme calque of *scale out* — the
`enqueuen`/`alerten` class the canon excludes wholesale. **Run 1 shipped it in two worked sentences**, i.e.
exactly where the wave-2 finding says renderers copy from. Also: run 1 wrote *warmgehaltene Instanzen* (one
word), run 2 *warm gehaltene Instanzen* (two) — **two words is right**; Duden's univerbated *warmhalten* is
the figurative „sich jemanden warmhalten".

**R5 — `timeout`: which German leads for the configured value?** Both runs led with **die Zeitbeschränkung**
(canon `_language.md` §1.1.a prescribes the two-way split and names *Zeitbeschränkung* for the set value).
*Resolution: neither — the corpus overrules both.* The shipped German writes „Zeitüberschreitung – das Tool
hat innerhalb **seines Timeouts** nicht geantwortet": the **loan** carries the configured value (genitive
attested), and `Zeitbeschränkung` has **0 shipped occurrences** anywhere in 27 pages. Per brief §3, where
canon metaprose and shipped forms disagree, the corpus wins. **`das Timeout` leads; `die Zeitbeschränkung` is
the disambiguator; `die Zeitüberschreitung` is strictly the error.** *Cost of being wrong:* low —
`Zeitbeschränkung` stays canon-licensed, so a later reversal costs a find-and-replace, not a re-argument.

**R6 — `streaming`: SETTLED or WEAK?** Run 1: **SETTLED**, quoting the Duden noun lemma with **Gebrauch EDV**
(„Datenübertragungsverfahren, bei dem die Daten **bereits während der Übertragung** angesehen oder angehört
werden können"). Run 2: **WEAK**, stating in its own row „**kein Substantivlemma nachgeschlagen, das steht
hier ausdrücklich**", carrying the gender only from the `-ing` family rule.
*Resolution: run 1, SETTLED → BOUND.* This is the cleanest reconciliation in the slice: one run retrieved the
entry, the other declared it had not looked. Present evidence beats a declared non-lookup. Run 1's honest
caveat is preserved: Duden's example gloss is medial („angesehen oder angehört"), but the **head** of the
definition is *Datenübertragungsverfahren*, which carries our token sense.

**R7 — `rate limit`: `das Rate-Limit` (hyphen) or `das Rate Limit` (spaced)? — the row this task flagged as
needing ONE binding string across 6 files.**
*Run 1 (K2):* **hyphen.** `_language.md` §1.3.3 quotes the Amtliches Regelwerk **§ 45 E1** („Aus anderen
Sprachen stammende Verbindungen aus **Substantiv + Substantiv** … werden zusammengeschrieben; als Variante ist
die verdeutlichende Schreibung mit Bindestrich möglich") and calls the spaced form „im Deutschen nicht
normgerecht". `rate` is a noun ⇒ § 45 E1 applies, not § 37 E4. Canon precedent: *Prompt-Injection*,
*Tool-Call*, *Dead-Letter-Queue*. Proposed correcting §1.1.d.
*Run 2:* **spaced.** Canon row §1.1.d holds unchanged.
*And run 2 contradicts itself:* its `batch API` row writes „⛔ **die Batch API** getrennt (§1.3.3, **nicht
normgerecht**)" — applying the very rule to `Batch-API` that it declines to apply to `Rate Limit`, one row
away.
*Resolution: **`das Rate Limit`, spaced** — the corpus wins over the rule.* The shipped German prints „einer
Zeitüberschreitung, **einem Rate Limit**, einem `5xx`" (dative ⇒ neuter confirmed, spacing confirmed), and the
canon row prints the same. Per brief §3, a shipped form beats canon metaprose; here shipped form **and** the
term row agree against a general orthography rule, and changing an already-delivered string on a rule
argument is the more expensive error. **Run 1's argument is not refuted, it is outranked** — it goes to
**CANON DELTA 4** as a reported tension for the orthography owner, **explicitly not to be applied in wave 3**.
*Cost of being wrong:* one string across 6 files, mechanically fixable — but if the hyphen were adopted now,
Part III would contradict a shipped Part II sentence, which is the loud MT signal §1.1 warns about.

**R8 — `tail latency`: which direction does p99 move? (run 1 wrote the construction run 2 bans)**
*Run 1's worked sentence:* „**der p99-Wert fällt über die Klippe**" and „die langsamsten Anfragen **brechen
vollends weg**".
*Run 2:* ⛔ „der p99-Wert **bricht ein** / **fällt ins Bodenlose**" — in English the **curve** falls off a
cliff; in German the **value** is the subject, and the value **rises**. „einbrechen" asserts the opposite of
the sentence.
*Resolution: run 2.* „**der p99-Wert schießt in die Höhe**" / „**die Latenz der langsamsten Anfragen läuft
aus dem Ruder**". This is a **factual inversion, not a style preference** — the same class as the brief's
`einfrieren` and `die Decke` examples, and it passes every fluency check. Run 1's „brechen vollends weg" is
also rejected: it reads as *the requests fail*, when the English says their latency degrades.

**R9 — `tier`: two different sense tables.**
(a) *Count:* both landed on **30** and both flagged the brief's 28 as wrong; run 2 documents why a naive
`grep -i tier` says 37 (**`frontier` 6×**). Agreed.
(b) *Sense (a), the price track:* run 1 → **der Batch-Betrieb / die Betriebsart / die Abrechnungsart**
(HOUSE); run 2 → **der Tarif / der Batch-Tarif** (WEAK, Klammerpflicht). **Resolved for `der Tarif`** on run
1's own internal contradiction (it rejects `Stapelverarbeitung` for naming the procedure, then picks
`Betriebsart`, which also names the procedure) plus corpus occupancy (`Betrieb` 12× as *Produktivbetrieb*).
**Labelled `THIN×2`** — see the box in §1. This is the row most likely to be reversed.
(c) *Sense (b):* run 1 → `das Angebot / der verwaltete Dienst`; run 2 → `die Stufe / die Ebene / das
Angebot`. **Resolved for `das Angebot`** on corpus occupancy (`Stufe` 55×, `Ebene` 35×, `Angebot` 1×).
(d) *Sense (d):* both → `die Schicht` / `die Anwendungsschicht`. **Refined to the compound only** — bare `die
Schicht` is the handbook's own curriculum word (96 shipped hits).
(e) *Sense (f), maturity:* run 1 imported `ai-sdlc.md`'s `Reifegrad` as a peek-don't-load reuse with the
honest note that it does not occur in Part III; run 2 verified `maturity tier` = 0 and `enterprise tier` = 0
and ruled **do not import**. **Resolved: do not import**, and log the check so a later pass does not read the
absence as a gap. Substantively the two agree; run 2's framing is the safer record.

**R10 — `wait`: which trap, and how wide is the rule?** Run 1 found the **noun** trap (`die Wartung` =
maintenance ⇒ nominalise as `das Warten`). Run 2 found the **verb** trap (Duden `warten` Bedeutung 2 „(an
etwas) Arbeiten ausführen, die zur Erhaltung der Funktionsfähigkeit … notwendig sind") and proposed a blanket
**Pflichtrektion `auf` + Akk.**
*Resolution: both traps are real; run 2's rule is narrowed by the corpus.* The shipped German ships
objectless `wartet` four times — „der erste Aufruf mit einem neuen Schema **wartet**", „der Durchlauf
**wartet**", „eine Halluzination **wartet**" — and in none of them can the subject be *maintained*. It also
ships `Wartungsmodus`, so the maintenance field is live. **Binding rule: `auf` + Akk. is obligatory whenever
the subject is a thing that can be maintained (Dienst, Server, Instanz, Worker, Pool, Maschine); elsewhere
the objectless verb is fine.** That is narrower than run 2 and wider than run 1, and it is the only version
consistent with what the book already prints.

**R11 — `-bound` family: coin nothing, or use `rechenintensiv`?** Run 1: no German word for any member;
rebuild all four as clauses („**durch die Rechenleistung begrenzt**"). Run 2: measured
`insource:"rechenintensiv"` = **54** ⇒ *compute-bound* has a word; the other three are 0.
*Resolution: run 2 for compute-bound, run 1 for the rest.* „**Prefill ist rechenintensiv, Decode wird durch
die Speicherbandbreite begrenzt**" is also the better parallel, which the prefill/decode contrast needs.

**R12 — `shed`: is „Last abwerfen" a running verb or a one-time gloss?** Run 1: ⛔ *abwerfen* in running text
entirely (it drags in `Lastabwurf` ⇒ power grid + aviation, 69 : 0); the canon gloss may stand **once** as an
explanation. Run 2: uses „Last abwerfen" as a collocation, citing `rag.md` §3, which prints it as a Korpusform.
*Resolution: split them.* The **running verb is `abweisen`** (requests and excess load alike); „Last
abwerfen" is licensed **only where the canon gloss is being quoted**, at most once per page; **the noun `der
Lastabwurf` is banned outright**, which both runs agree on. This preserves run 1's drag argument without
overriding a canon-printed string.

**R13 — counts.** `queue` 45 (concordance) vs 46 (run 2's `\bqueue(s|ing|d)?\b`): run 2 identified the exact
cause — the surface form **`queued`** („Async **queued** ingestion absorbs spikes") is missing from the
concordance's header tally although **the text unit is printed**. Not a fabricated absence; a header defect.
`pool` 15 vs 19, `async` 19 vs 27, `streaming` 15 vs 16, `rate limit` 11 vs 10 — all the same shape
(inflected/compound forms in or out). **Binding for downstream counting: use the concordance's unit counts**
(`queue` 45, `job` 44, `tier` 30, `rate limit` 11, `pool` 15), and note run 1's finding that the brief's own
numbers were wrong for `job` (27 → 44) and `tier` (28 → 30). `job` at 44 is the **second-densest** head term
of the slice, which neither the brief nor the canon reflected.

**R14 — `Backpressure` gloss.** Run 1: the `rag.md` §2 gloss „(Gegendruck – Schutz vor Überlast)" **stays a
gloss**. Run 2 (Kollision 1): §2's mandatory gloss contains *Gegendruck*, which `_language.md` §1.1.d
**disqualifies** as coming from an AI-generated glossary content farm — a contradiction inside the canon, on a
string §2 releases for verbatim shipping. **Verified directly:** `rag.md` line 262 prints the gloss; line 1255
of `_language.md` prints the disqualification. *Resolution: run 2.* A disqualified source must not carry a
shipped string. Proposed replacement, terminology-free because a gloss **explains** and does not **name**:
**„(Schutz vor Überlast – der Empfänger bremst den Sender)"**. → CANON DELTA 2. Run 1's counter-position is
recorded: *Gegendruck* is an ordinary German word and inside a gloss is not a coinage — but whoever takes that
line must **change §1.1.d, not ignore it**.

---

## 4. VOCABULARY FOOTPRINT

Flat, deduplicated list of every German content word appearing in the worked sentences and sense cards above.
Stage 2 uses this to detect cross-slice collisions. **Bold = already occupied in the shipped German corpus
with a count; a collision here is a real one, not a hypothetical.**

`abarbeiten` · `abweisen` · `Abrechnungstarif` · `Alarm` · `Anbieter` **(38)** · `Anfrage` **(59)** ·
`Ankunftsrate` · `Annahme` · `Angebot` **(1)** · `Anwendungsschicht` · `Arbeit` **(103)** · `Arbeitsmarkt` ·
`Arbeitseinheit` · `asynchron` · `Aufgabe` · `Backpressure` · `Batch` **(14)** · `Batch-Tarif` · `Bearbeitung`
· `bedienen` · `begrenzen` **(28)** · `begrenzt` · `beschränkt` · `binden` · `bremsen` · `Dead-Letter-Queue` ·
`Dienst` **(12)** · `drosseln` · `Ereignisschleife` · `erschöpft` · `Fehlerbudget-Richtlinie` · `Flusskontrolle`
· `Frist` **(1)** · `Generierung` · `geordnet` · `gestreamt` **(1)** · `GPU-Auslastung` · `Herunterfahren` ·
`Höchstlänge` · `Ingestion` · `Instanz` **(4)** · `interaktiv` · `Job` · `Job-ID` · `Kontingent` · `Länge` ·
`Last` **(5)** · `Latenz` **(52)** · `leerlaufen` · `Mandant` **(3)** · `Mehrkosten` · `Modellklasse` ·
`Nebenläufigkeit` · `Obergrenze` **(41)** · `Perzentil` **(1)** · `Preis` · `Producer` · `Queue` ·
`Rate Limit` **(1)** · `rechenintensiv` · `Ressource` **(21)** · `Schicht` **(96)** · `Semaphor` ·
`Speicherbandbreite` · `stauen` · `stellen` · `Streaming` **(4)** · `Stufe` **(55)** · `Tarif` · `Timeout`
**(1)** · `Verbindung` **(19)** · `verkeilen` · `vergrößern` · `warm gehalten` · `warten` **(7)** · `Wartezeit`
· `Wiederholung` **(37)** · `Worker` **(43)** · `Zeitfenster` **(1)** · `Zeitüberschreitung` **(4)** ·
`zustandslos`

**Collision candidates I am handing to stage 2 (highest first):**
1. **`die Stufe`** — I use it only as a **counting frame** for vendor price names („die Stufen `Reserved`,
   `Priority` …"). It is occupied **55×** as *rung of complexity / pipeline stage*. If another slice binds
   `Stufe` as a terminus, mine must be re-worded, not theirs.
2. **`die Schicht`** — occupied **96×**, including the handbook's curriculum metaphor. I use only the
   compound `die Anwendungsschicht`. Slice A/C's `layer`/`Orchestrierungsschicht` work touches this.
3. **`die Obergrenze`** — I bind it for `concurrency cap`; it is already the shipped rendering of `cap` **and**
   (per the referent baseline) of `Latency Budget`'s neighbourhood, 41 hits. Three referents are converging on
   one word. **Worth a stage-2 look** even though each use is individually right.
4. **`die Wartezeit` / `warten`** — mine is queueing delay; slice-neutral, but the `auf`-rection rule (§3 R10)
   must not be re-stated more widely by another slice.
5. **`Latenz`** (52), **`Budget`** (67) — cross-slice, stated, not decided here.
6. **`der Tarif`** — 0 shipped, so **no collision today**; but if another slice renders *plan*, *pricing*,
   *rate card* or *SKU* it will land here. Flagged pre-emptively.

---

## 5. SPREAD (from the concordance, per Part III file)

Terms in **≥3 files need ONE binding string decided centrally** — named in bold.

| Terminus | occ | files | Which |
|---|---|---|---|
| **`tier`** | 30 | **7** | production-failures · serving/deep-dive · cloud-platforms/{index,deep-dive} · tooling-ecosystem/deep-dive · llmops/{index,deep-dive} |
| **`job`** | 44 | **7** | overview · serving/index · cloud-platforms/deep-dive · tooling-ecosystem/{index,deep-dive} · llmops/{index,deep-dive} |
| **`rate limit`** | 11 | **6** | serving/{index,deep-dive} · cloud-platforms/{index,deep-dive} · llmops/{index,deep-dive} |
| **`queue`** | 45 | **5** | serving/{index,deep-dive} · tooling-ecosystem/deep-dive · llmops/{index,deep-dive} |
| **`bound`** | 27 | **5** | serving/{index,deep-dive} · cloud-platforms/index · llmops/{index,deep-dive} |
| **`retry`** | 15 | **5** | production-failures · serving/{index,deep-dive} · cloud-platforms/index · llmops/deep-dive |
| **`streaming`** | 15 | **5** | overview · serving/{index,deep-dive} · cloud-platforms/index · llmops/index |
| **`wait`** | 18 | **5** | serving/{index,deep-dive} · tooling-ecosystem/deep-dive · llmops/{index,deep-dive} |
| **`quota`** | 10 | **4** | serving/{index,deep-dive} · cloud-platforms/{index,deep-dive} |
| **`timeout`** | 10 | **4** | production-failures · serving/{index,deep-dive} · llmops/index |
| **`async`** | 19 | **4** | serving/{index,deep-dive} · tooling-ecosystem/deep-dive · llmops/deep-dive |
| **`batch tier`** | 9 | **4** | production-failures · cloud-platforms/deep-dive · llmops/{index,deep-dive} |
| **`pool`** | 15 | **3** | serving/deep-dive · cloud-platforms/index · llmops/deep-dive |
| **`backpressure`** | 7 | **3** | serving/{index,deep-dive} · llmops/deep-dive |
| **`waiting`** | 10 | **3** | serving/{index,deep-dive} · tooling-ecosystem/deep-dive |
| **`bounded`** | 6 | **3** | serving/deep-dive · cloud-platforms/index · llmops/deep-dive |
| **`drain`** | 5 | **3** | serving/deep-dive · tooling-ecosystem/deep-dive · llmops/deep-dive |
| `batch API` | 6 | 2 | cloud-platforms/deep-dive · llmops/deep-dive |
| `shed` | 6 | 2 | serving/deep-dive · llmops/deep-dive |
| `enqueue` | 4 | 2 | serving/deep-dive · llmops/deep-dive |
| `load shedding` | 3 | 2 | serving/deep-dive · llmops/deep-dive |
| `priority` | 2 | 2 | cloud-platforms/{index,deep-dive} |
| `admission control` | 2 | 1 | serving/deep-dive |
| `time to first token` | 2 | 1 | serving/index |
| `tail latency` | 1 | 1 | serving/deep-dive |
| `percentile` | 1 | 1 | llmops/index |
| `interactive tier` · `concurrency limit` | 0 | 0 | verified twice — do not create |

**`rate limit` is the one this task singled out, and it is the worst-shaped: 11 occurrences, 6 files, and the
two runs disagreed on the string.** Binding: **`das Rate Limit`, spaced, neuter, plural `die Rate Limits`,
process `das Rate Limiting`** (§3 R7). `tier` (7 files) and `job` (7 files) also need central strings and have
them above.

---

## 6. CANON DELTA — report only; **the canon was not edited**

| # | File · section | Current text | Proposed | Reason |
|---|---|---|---|---|
| **1** | `rag.md` §2, "Settled as kept-EN (class 2)", line 102 | `… Backpressure, Load Shedding, **Admission Control**, …` | **Move `Admission Control` to §3 (OPEN)** with the closing condition and the descriptive corpus form | §2's own preamble requires every listed term to have a `_language.md` §1.1 row before its second use. **There is no `Admission Control` row** (verified: `grep -ci admission _language.md` = 0), and there is nothing to add — no de.wikipedia lemma (404), and *Zulassungssteuerung*/*Zugangssteuerung* exist only in patent translations and dictionary portals. Same shape as the already-reversed `Latency Budget`, `Scratchpad`, `Super-Step`. The term occurs **2×** in Part III, i.e. over the threshold. *(run 1, K1)* |
| **2** | `rag.md` §2, mandatory-gloss table, line 262 | `\| Backpressure \| „(Gegendruck – Schutz vor Überlast)" \|` | `\| Backpressure \| „(Schutz vor Überlast – der Empfänger bremst den Sender)" \|` | `_language.md` line 1255 **disqualifies** *Gegendruck* (AI-generated glossary content farm). §2 releases this string for verbatim shipping, so a disqualified source would carry a delivered string. A gloss **explains**; it must not **name**. *(run 2, Kollision 1; verified against both files)* — **dissent recorded:** run 1 holds the gloss is fine because *Gegendruck* is ordinary German; that position requires **changing §1.1.d**, not ignoring it |
| **3** | `_language.md` §1.1.d `Queue` row + `rag.md` §3 `Queue (IT-Sinn)` row | „*die Warteschlange* für die **Datenstruktur** (de.wikipedia-Lemma), *die Queue* für die konkrete Broker-/Job-Queue" | Either **retire the split** (bridge pattern: gloss once, then kept-EN) **or** restate its criterion as **broker/messaging register vs scheduler/everyday register** | The split's cited source does not carry a referent boundary: `Message Queue` **redirects** to `Warteschlange (Datenstruktur)`; the data-structure page itself writes „**die Queue**"; broker prose uses both words on one page. Meanwhile the strongest German source for a *concrete* job queue (iX/Slurm) writes `Warteschlange`. **Zero Part III impact either way** (all 45 are the runtime object) and **zero shipped impact** (`Queue` 0, `Warteschlange` 0 in the delivered locale) — which is why it is cheap to decide now. *(run 1 K4 + run 2 Kollision 6)* |
| **4** | `_language.md` §1.1.d `Rate Limit` row vs §1.3.3 (§ 45 E1) | §1.1.d prints **„das Rate Limit"** (spaced); §1.3.3 calls spaced noun+noun „im Deutschen nicht normgerecht" | **Report the tension; do NOT change the string in wave 3.** Either add an explicit exception note to §1.1.d, or plan a coordinated re-spelling that also touches the **shipped** Part II sentence | The delivered locale prints „einem **Rate Limit**". Changing it on a rule argument would make Part III contradict a shipped Part II sentence — the loud MT signal §1.1 warns about. **The rule argument stands unrefuted** (`rate` is a noun ⇒ § 45 E1, and the canon hyphenates the twins *Prompt-Injection*, *Tool-Call*, *Dead-Letter-Queue*); it is outranked, not answered. *(run 1 K2; run 2 applies the same rule to `Batch-API` one row away — an internal inconsistency worth fixing whichever way it goes)* |
| **5** | `_language.md` §1.1 — **9 missing rows** | — | Add: **`Job`** (der, die Jobs, des Jobs — DWDS Bed. 4, marked IT; ⚠ Duden `/Job` 404, DWDS carries it alone) · **`Pool`** (der, die Pools, des Pool(e)s — DWDS ²Pool 4c; HOUSE: compound-only) · **`Kontingent`** (das, die Kontingente, des Kontingent[e]s — WEAK, no IT referent) · **`Tarif`** (der, die Tarife, des Tarif[e]s — Duden Bed. 1; **THIN×2** for the compound) · **`Streaming`** (das, —, des Streamings — Duden, Gebrauch EDV) · **`Nebenläufigkeit`** (die — de.wikipedia lemma; the canon already *uses* the word in the `Race Condition` row) · **`Semaphor`** (der, die Semaphore, des Semaphors — WEAK, plural regular) · **`Mandant`** (der, die Mandanten, **des Mandanten**, n-decl. — BSI C5 „Cloud-Kunden (**Mandanten**)", shipped 3×) · **`warten`** → §1.5 (rection rule, §3 R10) | Every one is used ≥2× in Part III and has **no** row. `Streaming` is additionally missing from `rag.md` §2. **Delta: +9 rows to §1.1 and +1 to §1.5 — do not compute the new totals** |
| **6** | `rag.md` §1, class-1 identifier list | lists `p95` / `p99` | add **`p50`** | Part III writes `p50`, and the **shipped corpus already ships it 4×** („Ziele für **p50 und p95**"). Same class, same treatment. Trivial. *(run 2)* |
| **7** | `rag.md` §3 — new OPEN rows | — | Add **`graceful shutdown / graceful timeout`** (incumbent: „das geordnete Herunterfahren"; 0 attestation found across heise/iX/INNOQ/informatik-aktuell/de.wikipedia in run 1's three targeted searches) and **`retry tax`** (⛔ *die Retry-Steuer*; running form „die Mehrkosten der Wiederholungen" — the `token tax` precedent, §3 „nicht übernehmen"). `retry tax` is **bold-marked and also inside an image `alt` text** in Part III, so it needs a decision, not silence | *(run 1 §4; run 2 Kollision 4)* |
| **8** | `_language.md` §1.1.d `Load Shedding` row | records *Lastabwurf* as power grid / power plant | add the **aviation** sense | Run 1 read the full distribution of `insource:"Lastabwurf"` (69 hits) and found *Transall C-160* and *Airbus A400M*, where `Lastabwurf` is **dropping cargo from a transport aircraft**. A second wrong referent the canon does not record |

---

## 7. NEEDS A DECISION, NOT MORE RESEARCH

| Row | The decision | My recommendation | Cost of being wrong |
|---|---|---|---|
| **`tier` sense (a) — the price track (~16 occurrences, 4 files)** | German has **no attested noun**. Somebody must pick between two coinages: `der Tarif`/`der Batch-Tarif` or `der Batch-Betrieb`/`die Betriebsart`. Three independent measurements found zero (`Preisstufe`+Cloud 0; `Tarifstufe` 17, all tax/transit; `Batch-Tarif` 0) | **`der Tarif` / `der Batch-Tarif` (*batch tier*)**, English parenthesis obligatory at first mention. `Tarif` says *price*, which is what the corpus insists the thing is; `Betrieb` says *mode of operation*, which is the distinction the corpus explicitly draws **against** | **Moderate.** ~16 occurrences across 4 files, plus a heading. A reversal is a mechanical replace, but a wrong choice makes the corpus's own „this is a **pricing** tier, not Continuous Batching" warning unintelligible in German. **This is the slice's THIN×2 row — treat a later reversal as expected, not as a failure** |
| **`queue` — canon split: retire or rename?** | Neither run would flip a canon row unilaterally, and both are right not to. But leaving it as-is means the next pass applies a criterion whose own source does not support it | **Restate the criterion** (broker/messaging vs scheduler register) rather than retire the split, and note that Part III does not exercise it | **Low today, rising.** Zero Part III and zero shipped impact — but the next German content that has a real data-structure passage will decide it by accident |
| **`rate limit` spelling** | Spaced (shipped + canon row) vs hyphenated (§ 45 E1 + canon's own twin-term precedent). Both sides are documented; no further attestation will resolve an orthography rule | **Ship spaced now** (§3 R7); file the rule tension for a coordinated pass that would also touch delivered Part II text | **Low but visible.** 11 occurrences, 6 files. The expensive error is not the spacing — it is Part III disagreeing with a shipped Part II sentence |
| **`Backpressure` gloss (`rag.md` §2 vs `_language.md` §1.1.d)** | A canon-internal contradiction on a string released for verbatim shipping. One of the two must move | **Replace the gloss** with a naming-free explanation: „(Schutz vor Überlast – der Empfänger bremst den Sender)" | **Low.** One string; but leaving a disqualified source attached to a delivered gloss is exactly the provenance failure the leak/quality discipline exists to prevent |
| **`Admission Control`: §2 kept-EN or §3 OPEN?** | Nothing further to attest — 404 on the lemma, and the only German candidates are translation-memory class | **Move to §3 OPEN**, ship the descriptive construction | **Low.** 2 occurrences, 1 file |
| **`timeout`: loan or `die Zeitbeschränkung` as the lead form?** | The canon prescribes the German; the delivered corpus uses the loan. Both are canon-licensed, so this is a house call, not an evidence question | **`das Timeout` leads** (corpus precedent, genitive attested in our own book) | **Low.** Fully mechanical either way; the only hard rule — never `Zeitüberschreitung` for a set value — is unaffected |

---

## 8. WHAT THIS PASS COULD NOT DO

1. **No new lexicographic research, by design.** Every dictionary quote, `insource:` count and URL above is
   **reproduced from one of the two sheets and attributed**. I verified none of them at the source. If run 1
   or run 2 misread a Duden entry, this ledger inherits the error — and run 1 documents that it caught itself
   nearly doing exactly that (a search-result summary claimed a heise article contained „Gold-Tier" /
   „Silver-Tier"; the direct fetch did **not** contain the passage, and citing it would have made the `Tier`
   row look impeccably sourced **and wrong**).
2. **The corpus grep can prove presence, not absence of a *sense*.** `Queue` 0 / `Warteschlange` 0 tells me
   the split never shipped; it cannot tell me whether Part I/II ever *needed* it and worked around it.
3. **`der Batch-Tarif` remains a coinage on probation.** Two runs, zero attestation, two different words. My
   resolution rests on a **semantic argument and a self-contradiction in run 1**, not on evidence. Labelled
   `THIN×2` throughout so no downstream pass reads it as settled.
4. **No native-speaker ear.** The three collocations most likely to be wrong are, in order: „weitere Anfragen
   **stauen sich**", „**die Queue abarbeiten**", „**der p99-Wert schießt in die Höhe**" — the class that
   fluency hides. Each is checked against a fixed German idiom; none has been heard by a native speaker.
5. **Two paywalls are still shut** (run 2): the iX benchmark „Inferenz-Engines vLLM, SGLang und NIM im
   Vergleich" and the iX Slurm article — German original prose on exactly throughput, latency, batching and
   streaming. For `queue depth`, `in-flight`, `Nebenläufigkeit` and `TTFT` that would have been the decisive
   source. No German book full text (dpunkt/Rheinwerk) was available to either run.
6. **Cross-slice terms are stated, not merged**, per the brief: `Laufzeit`/`runtime`, `snapshot`,
   `lever`/`Hebel`, `budget`, `Semaphor` genus, `Handler` genus, `Producer`/`Consumer` genus, `poison` /
   `poisoning`, and the `API` gender that `die Batch-API` inherits. Stage 2 merges them.
7. **I did not verify the concordance against the English source.** Run 2 found one header-tally defect
   (`queued` missing from the `queue` surface-form line, unit still printed); I carried its counts forward
   without re-deriving them.
8. **Where I chose against a run, I chose once and said why.** Twelve resolutions in §3 are decisions, not
   findings. The four with the largest undercovered share are, in order: **`der Batch-Tarif`** (THIN×2),
   **`das Kontingent`** (Duden carries word and sense, no German IT text carries the referent),
   **`das Angebot`** for `tier`(b) (chosen on corpus occupancy, not on attestation), and the
   **`warten`-rection rule** (narrowed from run 2 on four shipped sentences — a small sample).
