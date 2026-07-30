# LEDGER-E — binding ledger, slice E (release, gating, versioning, incidents) · RAG Teil III

**Gate 6.5, stage 1.** Inputs read in full: `OUT-E-run1.md` (215 lines), `OUT-E-run2.md` (195 lines),
`dewave3-concord-E.txt`, `REFERENTS-baseline-verdicts.md`, the shipped German corpus (27 pages,
`i18n/de/…/current/**`), `editorial/canon/de/{_language.md,rag.md,ai-sdlc.md}`.

> **What this pass added that neither run had.** I re-counted the contested families over the English
> source myself and hand-classified all 29 `snapshot` occurrences from the concordance. Three results
> change rulings: (1) the `snapshot` sense split is **10 restorable : 19 dated picture** — run 2 exact,
> run 1 wrong, **and the brief's framing wrong in the opposite direction**; (2) the countable *a deploy*
> is **already shipped as „ein Deployment"** in the delivered German, which decides a frontal run1↔run2
> contradiction; (3) `die CI` is **CORPUS PRECEDENT over 4 occurrences on 3 pages**, not the 2 pages run 2
> claimed and not the unattested house form run 1 claimed.

---

## 1 · Binding table

Class: 1 = identifier/untouchable · 2 = kept-EN loan · 3 = German-led (first-mention gloss) · 4 = fully German.

| Terminus | German | Class | Status | Artikel/Plural/Genitiv | Kollokation | ⛔ rejected | Evidence grade |
|---|---|---|---|---|---|---|---|
| **release** (42) | **das Release** | 2 | **BOUND** (genus = house choice, stated) | das Release · die Releases · des Releases | „von Release zu Release verfolgen"; „Das Korpus ist ein Release."; Verb → **veröffentlichen** | ⛔ *der Release* (DWDS licenses both — this is a **choice**, not a source conflict; Neutrum first at DWDS, and every neighbour is Neutrum: *das Deployment*, *das Canary Release*) · ⛔ **die Freigabe** for the *thing* released (reserved for the `gate` field, see below — two referents, one word) · ⛔ *die Veröffentlichung* as the noun for the artefact | `RECONCILED (run1 had NO ROW for the slice's highest-count term; run2 ruled it; I adopt run2)` + `CORPUS(3 — plural only: „ein bis zwei Releases", „von Release zu Release"; genus NOT corpus-decided)` |
| **release gate** (7, 3 files) | **„die Freigabe vor dem Release"** — ONE string | 3 | **OPEN (incumbent held: the paraphrase; closes when a native DE sentence from heise/iX/INNOQ/dpunkt/BSI carries a case-marked bare singular `Gate` without *Quality/Stage/Release* in front)** | — (construction, not a noun) | „**Die Freigabe vor dem Release** prüft die Qualität, nicht nur die Kosten." · criteria referent → **die Freigabekriterien** · `pre-release gates` → „**Prüfungen vor dem Release**" | ⛔ *das Freigabe-Gate* (`ai-sdlc.md` §127 forbids coining it) · ⛔ *das Release Gate* with a German article (0 attestation, both runs, `insource:"Release Gate"` = 0 **and** `insource:"Release-Gate"` = 0) · ⛔ *das Release-Tor*, *das Freigabetor*, *die Freigabeschranke* | `AGREED×2` on OPEN + `CANON-VERBATIM` (`ai-sdlc.md` §4). ⚠ run1's alternates *das Freigabeverfahren / die Freigabekriterien* rest **entirely on BSI OPS.1.1.6** → `THIN` (single regulator doc, single run) |
| **gate** (31 bare + 1 `gated`, 5 files) | **OPEN — ships a CONSTRUCTION SET, never a word.** See SC-6 | 2 (bound `Quality Gate` only) / 3 (rest) | **OPEN (incumbent held: no bare `Gate`; closes as above)** | `das Quality Gate · die Quality Gates · des Quality Gates` only | fixed term → **das Quality Gate**; counted object → **die Prüfung / die Prüfungen**; inserted check → **„eine Prüfung vorschalten"**; verb *to gate* → **„nur nach Freigabe zulassen"** / Mermaid **„gibt das Deployment frei"**; structural point → **der Kontrollpunkt** (last resort) | ⛔ **das Gate** bare — `gateway` occurs **31× in the same file set** and the delivered German already writes `Gateway`; a `Gate`-shaped word collides on the page. Two attested technical twins, not one: LSTM (`das Input Gate`) **and** semiconductor (`des Gates` = 35 de.wikipedia hits, Transistor/MOSFET) · ⛔ *Kontrollinstanz*, *Prüfinstanz*, *Prüfstelle*, *Schranke*, *Prüfschritt* (canon, `rag.md` §3) · ⛔ **der Prüfpunkt** — **now doubly blocked**: Microsoft's German for the Hyper-V *snapshot*, and this slice binds `der Snapshot` · ⛔ *der Synchronisationspunkt* (attested at de.wikipedia *Quality Gate*, but it names *synchronising*, not *blocking* — a sideways move against a held incumbent) | `AGREED×2` + `CANON-VERBATIM` + `CORPUS(delivered: „nur nach Freigabe zulassen" ×1 and „Schalten Sie eine Prüfung vor" ×1, both verbatim in `part-2-agents/tool-use/deep-dive.md`; `die Prüfung` 19×; bare `Gate` **0×** vs `Gateway` 3× in the shipped 27 pages)` |
| **gate**, sense *licence-gated* (1) | **lizenzpflichtig** | 4 | **BOUND** | adj. | „Langfuse ist quelloffen (MIT-Kern; **einige Unternehmensfunktionen sind lizenzpflichtig**)" | ⛔ carrying the release-gate vocabulary into this sentence — it is a **different referent** (licensing, not control flow) | `RECONCILED (run1-only find; run2 missed it; verified by my grep: `\bgated\b` = 1, `tooling-ecosystem/index.md`)` |
| **gating** (0) | — | — | **NULL, triple-verified** | — | — | — | `AGREED×2` + my grep = 0 |
| **canary** (12, 3 files) | **das Canary Release** (canon spelling **held** for wave 3) | 2 | **BOUND with a spelling reservation → CANON DELTA §6.2** | das Canary Release · die Canary Releases · des Canary Release[s] | „**Ein Canary Release schickt einen Teil des Verkehrs auf die neue Fassung.**" · anaphoric bare `canary` (5×) → repeat the term or **„der Testlauf auf einem Teil des Verkehrs"** · „a failing canary" → „**ein Canary Release, das durchfällt**" · das Canary Release **löst den Rollback aus** | ⛔ *der/das Canary* bare (no genus) · ⛔ *Kanarienvogel-Release* (0 attestation; the bird appears only as etymology) · ⛔ *das Kanarienvogel-Verfahren* | `CANON(_language.md §1.1.d, WEAK)` + `RECONCILED (run1 held canon spelling, run2 re-spelled to `Canary-Release`; I hold the incumbent and file the delta — a spelling flip mid-wave puts two spellings on one page)` |
| **shadow deployment** (2, 1 file) | **das Shadow-Deployment** + mandatory first-mention gloss | 2 | **BOUND** (genus inherited, not invented) | das Shadow-Deployment · die Shadow-Deployments · des Shadow-Deployments | Gloss: „(**Schattenbetrieb** – die neue Fassung läuft mit, ohne dass ihre Antworten ausgeliefert werden)" · „Ein Shadow-Deployment **läuft mit**; seine Antworten **werden nicht ausgeliefert**." · list → „**Canary Release, Shadow-Deployment oder A/B-Test**" (§6.5 Ergänzungsstrich does **not** apply — no shared Grundwort) | ⛔ **der Schattenbetrieb as the running term** — the `Lastabwurf` shape: strong German word, but the attested domain is plant/machine commissioning (DGUV, Bahn-Online), not software delivery. As a **gloss** yes, as a terminus no · ⛔ *das Schattendeployment*, *die Schattenauslieferung* | `AGREED×2 (genus from `das Deployment`, DWDS)` + `RECONCILED (run2's de.wikipedia *Probebetrieb* citation licenses the gloss; run1 had no source for it)`. Loan itself: `insource:"Shadow Deployment"` = 0 |
| **rollout / roll out** (1 + 5) | Verb **ausrollen**; the **noun is avoided** | 3 | **BOUND (verb) / OPEN (noun — closes when a DE trade sentence inflects `der/das Rollout` about *software*, not an aircraft)** | — | „### Roll out gradually" → „**Schrittweise ausrollen**" (§6.2 Rahmen C) · „**Rollen Sie schrittweise aus.**" · „The rollout patterns come straight from release engineering" → „**Die Muster für das schrittweise Ausrollen stammen direkt aus dem Release-Engineering.**" | ⛔ *der Rollout* / *das Rollout* as a running term — genus **split** (de.wikipedia `der` 99 : `das` 46) **and** the dominant referent is **aviation** (Boeing 747, C-130, STS-126: rolling the aircraft out of the hangar). A cold „der Rollout" in the serving chapter reads as a hangar exit · ⛔ *die Ausrollung* | `AGREED×2` + `CANON(§1.2)`. `RECONCILED (run1's „Muster für das schrittweise Ausrollen" chosen over run2's „Muster der Auslieferung" — the latter loses *gradual*, which is the whole referent, and squats on `Auslieferung`)` |
| **rollback** (13, 3 files) | Noun **das Rollback**; verb **zurückrollen** (Deployment) / **zurücksetzen** (Prompt, Version) | 2 (noun) / 4 (verb) | **BOUND** | das Rollback · die Rollbacks · des Rollback[s] | **Blockstring:** `rollback path` (4×) → **„der Rollback-Pfad"**: „**Jedes Artefakt braucht einen Rollback-Pfad.**" · „Das Canary Release **löst den Rollback aus**." · `auto-rolls-back` → „**rollt automatisch zurück**" · „Ein Prompt **wird zurückgesetzt**, indem man den Commit zurücknimmt." | ⛔ *die Zurückdrängung*, *der Rückschritt* (Duden's senses are the Cold War) · ⛔ **das Zurückrollen as a NOUN terminus** (`_language.md` §1.1.d) — the **verb** is licensed, the noun is not · ⛔ *die Rücknahme*, *die Wiederherstellung* | `CANON SETTLED (paradigm) / WEAK (IT sense)` + `RECONCILED (run2 found the Deployment-sense verb attested **inside the canon's own citation** — informatik-aktuell: „ein reibungsloses **Zurückrollen**"; run1 had only *zurücksetzen*. Both are kept, split by object.)` ⚠ run2's „der Weg zurück" is a fine one-off prose variant but **not** the blockstring: 4 occurrences across 3 files need one compound, not a paraphrase that drifts |
| **promotion / promote** (7, 4 files) | **four branches — see SC-4** | 3 | **BOUND (a) via corpus / HOUSE (b,c,d)** | — | (a) **zu einem Fall im Goldstandard aufsteigen** (intr.) / **einen Trace in den Goldstandard übernehmen** (tr.) · (b) **auf `exception` hochstufen** · (c) **auf 100 % ausweiten** · (d) **zur Regel erheben** | ⛔ **promoten** (Duden: advertising/marketing — „ein Album promoten"; same shape as *pushen*, *scoren*) · ⛔ *die Promotion* (German: first the doctorate, then sales promotion) · ⛔ **befördern** (Duden referents are **persons** by rank and **goods** by transport) · ⛔ *hochstufen* for branch (a) — that is branch (b)'s scale, not a change of dataset | (a) `CORPUS(1, verbatim)` — `part-1-rag/cross-cutting/observability/deep-dive.md`: „**Sie steigen zu neuen Fällen im Goldstandard auf**"; also „aus dem Produktivbetrieb in den Goldstandard". (b,c,d) `RECONCILED (run1 found FOUR senses, run2 only two; I verified all four exist — `Auto-promote → 100%` Mermaid label and „promoted from a tactic to a rule" are real. Run1 wins the inventory, run2 wins the German for (a).)` |
| **freeze / frozen** (16 + 11, 4 files) | **five branches — see SC-2.** Terminus **der Release-Freeze** | 2 (terminus) / 4 (rest) | **BOUND**, one branch is a **factual**, not stylistic, constraint | der Release-Freeze · die Release-Freezes · des Release-Freezes | (i) „**Ist das Budget aufgebraucht, werden alle Änderungen und Releases eingefroren – außer P0-Korrekturen und Sicherheits-Patches.**" · (ii) event loop → **lahmlegen / blockieren** · (iii) **der eingefrorene Regressionsdatensatz** · (iv) **eingefrorene Basisgewichte** · (v) wordplay kept | ⛔ **einfrieren for the event-loop sense** — the most expensive line of the slice. Duden's **transitive** *einfrieren* = „auf dem augenblicklichen Stand **belassen**", i.e. a **deliberate** hold; „der Aufruf friert die Event-Loop ein" therefore asserts an intentional shutdown — in the same lesson block as the Release-Freeze, which *is* one. A **factual** error · ⛔ *die/das Freeze* (all evidence masculine) · ⛔ *das Einfrieren* as the terminus name · ⛔ *der Auslieferungsstopp*, *das Moratorium* (coinage / politics-law register) | `RECONCILED (run1 = 2 heise articles, one from 1999 → WEAK; run2 found the de.wikipedia **lemma `Code-Freeze`**, masculine and thrice case-marked, plus Duden `einfrieren` and `lahmlegen` verbatim → stronger. I take run2's evidence and run1's five-branch card.)` + `CORPUS(1: „stabil genug, um darauf zu bauen, und noch nicht **eingefroren**")`. `Release Freeze` itself: `insource:` = 0 → the compound genus is **inherited**, stated as such |
| **pin / pinned / pinning / re-pin / unpinned** (**37**, 4+ files) | Verb + running term **die Modellversion festlegen**; noun **das Model-Pinning** | 3 (verb) / 2 (noun) | **BOUND — and the strongest corpus find in the slice** | das Model-Pinning · *kein Plural* · des Model-Pinnings | „### Pin the model" → „**Die Modellversion festlegen**" · „**Legen Sie exakte Modellversionen fest.**" · `unpinned alias` → „**ein Alias ohne festgelegte Version**" · `re-pin` → „**erneut festlegen**" / „**auf die vorherige Version zurücksetzen**"; Mermaid `Repin previous` → „**Vorgänger wieder festlegen**" · `a pinned artefact` → „**ein Artefakt mit festgelegter Version**" · region sense → **in der Region halten** / **an einen souveränen Endpunkt binden** · feature-set sense → **bindet Sie an** | ⛔ **pinnen / gepinnt** as the running term (Duden `pinnen`: „mit Pinnen, Stecknadeln … befestigen" *umgangssprachlich* + **Medizin** „nageln" — no software sense). run2's heise **blog** attestation („Versionen exakt pinnen") does not overturn the dictionary gap, and the same page supplies the German („exakte Versionsnummern eingesetzt"). Admissible **only** where the English term is being named · ⛔ *anheften*, *anpinnen*, *festnageln* · ⛔ *das Pinning* bare | `CORPUS(2, and it is decisive)` — Part I observability deep-dive: „einer geänderten **Festlegung der Modellversion**" and „(**Die Modellversion so festzulegen**, dass der Anbieter sie nicht unter Ihnen wegziehen kann, ist eine LLMOps-Praxis; sie gehört in die [Lektion zu LLMOps](…/part-3-production/llmops/index.md).)" — **Part I names the practice in German and forward-references THIS lesson by link.** Renaming it in Part III breaks a shipped forward reference. Count `37` verified by my own grep (run2 exact; run1's 32 wrong; concordance's 20 undercounts) |
| **snapshot** (29, **9 of 10 files — widest spread in the wave**) | **TWO referents, two words — see SC-1.** (A) **der Snapshot** · (B) **die Momentaufnahme** | 2 (A) / 4 (B) | **BOUND** | (A) der Snapshot · die Snapshots · des Snapshots — (B) die Momentaufnahme · die Momentaufnahmen · der Momentaufnahme | (A) **einen Snapshot erstellen / wiederherstellen / zurückspielen**; card label `corpus snapshot` → **„Korpus-Snapshot"** (15 chars) · (B) **etwas als Momentaufnahme behandeln / lesen**; „Names are snapshots" → „**Namen sind Momentaufnahmen.**" | ⛔ **one word for both senses** — `llmops/deep-dive.md` carries both on one page („a dated snapshot to re-check" / „restoring the previous snapshot"). „die Momentaufnahme wiederherstellen" ✗ (you do not restore a picture); „einen Snapshot der Produktnamen erstellen" ✗ (claims you can roll the name-state back) · ⛔ **der Prüfpunkt** in either branch · ⛔ *der Schnappschuss* (DWDS sense 2 = photography) · ⛔ *die Sicherung* (= backup) · ⛔ **der Checkpoint** as a synonym — see the boundary in SC-1 | (A) `AGREED×2` on `DWDS Bed. 3 [ITK]` with a **full paradigm in our referent** — rare in this project. (B) `CORPUS(5)` — `die Momentaufnahme` shipped 5× across 4 pages in exactly this sense. Sense split **10 : 19**, hand-counted by me from the concordance: `RECONCILED (run2 exact; run1 said 12 : 17; the task brief said the 29 are “overwhelmingly a pinned model version”, which is wrong — see §3.1)` |
| **prompt registry** (3) | **die Prompt-Registry** | 2 | **BOUND** | die Prompt-Registry · **die Prompt-Registries** · der Prompt-Registry | First-mention gloss: „(**das versionierte Verzeichnis der Prompts**)" · „Eine Prompt-Registry **hält** die Prompt-Versionen." · „re-pinning the registry version" → „**die Version in der Registry wieder festlegen**" | ⛔ *das Prompt-Register* (German `Register` = index/registry office/organ stop/linguistic register — wrong frame; the delivered locale did not pick it although it lies close) · ⛔ *die Prompt-Verwaltung* as the terminus (it is the **function**) · ⛔ *die Prompt Registry* un-hyphenated | `CANON SETTLED (§1.1 `Registry` row: die Registry / **die Registries** / der Registry)` + `CORPUS(8 sentences, case-marked incl. Dativ „in einer Registry")`. ⚠ **run2 proposed the plural `die Registrys` as a house guess — that is a REGRESSION against an existing canon row. Run1 cited the canon correctly; run1 wins.** |
| **version / versioned** (30, 6 files) | **die Version**; `versioned` → **versioniert**; `version control` → **die Versionsverwaltung** | 3 | **BOUND** | die Version · die Versionen · der Version | „in **der Versionsverwaltung** halten" · „the index has to be versioned" → „**der Index muss versioniert sein**" · „an exact prompt version" → „**eine exakte Prompt-Version**" | ⛔ *die Versionierung* for *version control* (it names the **process**, not the system) · ⛔ *die Versionskontrolle* (calque of *control*; canon blocks the same pattern at *Zugriffskontrolle*) · ⛔ **„die Version des Vorfalls"** in any form — Duden's own example under `Version` sense 2 is „eine neue Version **des Vorfalls** tauchte auf" (= a *telling* of events), and **both words are bound termini in this slice**. Rebuild wherever they meet · ⛔ *die Fassung* as the running term for software versions | `AGREED×2` + `Duden/de.wikipedia`. The `Version`+`Vorfall` collision is `RECONCILED (run2-only find, verified, adopted)` |
| **versioning** (0) | — | — | **NULL, triple-verified** | — | concept ships as `versioned` ×3 and `version control` ×1–2 | — | `AGREED×2` + my grep = 0 |
| **deprecation / deprecate** (2) | Verb **abkündigen**, Part. II **abgekündigt**; noun **die Abkündigung** — never bare | 4 | **BOUND (WEAK), with a named register trap** | die Abkündigung · die Abkündigungen · der Abkündigung | **Bind the phrase: „die Abkündigung eines Modells"**, never bare `die Abkündigung`. Prefer the participle. „Providers deprecate and retire models" → „**Anbieter kündigen Modelle ab und schalten sie später ab.**" · „OpenAI distinguishes deprecation from shutdown" → „**Abkündigung und Abschaltung sind zweierlei.**" | ⛔ *die Deprecation*, *deprekieren*, *deprecaten* (0 attestation, Denglisch verb morphology) · ⛔ *missbilligen* (the literal Duden sense of *deprecate* — wrong sense) · ⛔ *für veraltet erklären* as the terminus (a claim about state, not an announcement) · ⛔ *die Einstellung* (too general) | `RECONCILED (run1 explicitly DECLINED to attest and left the row unfilled; run2 attested it — de.wikipedia *macOS* case-marked, `insource:"abgekündigt"` = 94 articles, `"Abkündigung"` = 64. Run2 wins by producing evidence where run1 produced none.)` ⚠ run2's measured register trap is real: 4 of the top 5 `Abkündigung` hits are **ecclesiastical** (parish announcements) — the `Alarmmüdigkeit` class, a **word-profile** trap, defused by the binding phrase |
| **Deprecated** (status label, 1) | **untranslated**, glossed once | **1** | **BOUND** | — | „Active, Legacy, Deprecated, Retired" → **unverändert**; gloss once: „(aktiv · Altbestand · abgekündigt · abgeschaltet)" | ⛔ translating the label — it is a **provider status string** in a lifecycle list, `_language.md` §1.0 class 1 | `RECONCILED (run1-only find; run2 missed the label entirely. Verified: `llmops/index.md` „Active, Legacy, Deprecated, Retired — with at least 60 days' notice".)` |
| **artefact** (17, 3 files) + `deployable` (5) | **das Artefakt** | 3 | **BOUND (paradigm) / WEAK (software referent)** | das Artefakt · die Artefakte · des Artefakt[e]s | **Blockstring:** *the deployable artefact* (5×, incl. 2 take-aways) → **„das auslieferbare Artefakt"** — one string, everywhere · „**Jedes Artefakt braucht einen Rollback-Pfad.**" · `five-artefact deploy` → „**das Deployment aus fünf Artefakten**" | ⛔ *Fünf-Artefakt-Deployment* (three-member coinage, unattested) · ⛔ *das Erzeugnis*, *das Build-Ergebnis*, *das Bauergebnis* (coinages beside an established canon word) · ⛔ *das Build-Artefakt* as the umbrella (only one of our five is built) | `CORPUS(2: „Ein Artefakt, und jede Frage des Produktivbetriebs hängt daran")` + `Duden paradigm` + `CANON (ai-sdlc.md §3/§4a)`. ⚠ **In-field trap, run2-only and worth keeping:** Duden sense 4 is *Elektronik: **Störsignal*** — in a chapter about GPUs, serving and metrics „das Artefakt" can read as *measurement artefact*. The binding phrase defuses it |
| **CI** (18, 4 files) | **die CI** | 2 | **CORPUS PRECEDENT** (upgraded from both runs) | die CI · — · der CI; preferred compound **die CI-Pipeline** | **Blockstring: „in der CI"** · „offline **in der CI** und online im Produktivbetrieb" · `eval in CI` → „**die Evaluierung in der CI**" (head noun owned by the eval slice — see §8.4) · heading „Deploy — CI/CD when the artefact isn't just code" → „**Bereitstellen – CI/CD, wenn das Artefakt nicht nur Code ist**" | ⛔ *das CI* (collides with **Corporate Identity**, the dominant German referent of the abbreviation) · ⛔ *der CI* · ⛔ *die kontinuierliche Integration* as the running term (the loan is established; §1.0 forbids the anglicism hunt) | `CORPUS(4)` — **4 occurrences on 3 independent pages**, every one Dativ feminine: `part-2-agents/real-agents.md`, `…/evaluation/deep-dive.md` ×2, `…/evaluation/index.md`. `RECONCILED (run1 called it HOUSE/unattested, run2 claimed 2 pages; both undercount. This is a delivered ruling, not a house form.)` |
| **CD** (1, only in `CI/CD`) | **`CI/CD`**, uninflected, never alone | 2 | **BOUND** | — | compounds hyphenated: **die CI/CD-Pipeline**, **der CI/CD-Prozess** | ⛔ **die CD** alone (the German referent is the audio disc — the loudest collision in the slice) | `AGREED×2` + `CANON (ai-sdlc.md §2 kept-EN list)` |
| **deploy** (30, 9 files) | **three branches — see SC-5** | 2/3 | **BOUND — and the countable branch is CORPUS PRECEDENT** | — | process/discipline → **die Bereitstellung** · **countable event → „ein Deployment"** · verb → **bereitstellen / ausrollen** · `adk deploy` → class 1, untouched | ⛔ **„ein Deploy"** — German has no short noun; the word exists only as a verb stem · ⛔ *deployen* as the running term (canon §1.3.2 sets „bereitgestellt / ausgerollt") | `CORPUS(4) — DECIDES A FRONTAL RUN DISAGREEMENT.` The delivered German already writes the countable: „am Status **eines Deployments**", „Hat **ein Deployment** die Prompt-Vorlage geändert?", „einem Deployment, einer geänderten Festlegung der Modellversion", Mermaid „(ein Deployment)". And it reserves **die Bereitstellung** for the process (5×: „eine Frage der Bereitstellung", „vor der Bereitstellung", „Lektion über Bereitstellung und Betrieb"). **Run1's „Eine Änderung an einem davon ist ein Deployment." is corpus-correct; run2's „… ist eine Bereitstellung." is not.** |
| **deployment** (14, 6 files) | (a) **das Deployment** · (b) **die bereitgestellte Instanz** · (c) **die Betriebsumgebungen** | 2 (a) / 3 (b,c) | **BOUND** | das Deployment · die Deployments · des Deployments | (b) „a fine-tuned deployment bills per token" → „**die bereitgestellte Instanz rechnet pro Token ab**" · (c) `air-gapped deployments` (6× in cloud-platforms) → „**vollständig abgeschottete Betriebsumgebungen**" | ⛔ **(b) rendered as `Deployment`** — „das Deployment rechnet pro Token ab" claims the **process** costs money; the referent is the **running instance**. A factual error, not a style one · ⛔ (c) *abgeschottete Deployments* (the referent is an **installation**) | `CANON SETTLED (§1.1.a, DWDS)` + `RECONCILED (run2 caught (b) as a factual error and is right; run1 wanted `das Deployment` + a gloss, which leaves the false predicate standing. (c) is run1-only and correct — verified, 6 occurrences.)` |
| **drift** (18 prose + 1 icon prop, 4 files) | **der Drift** (DISPUTED incumbent, **not reopened**); prefer the **verb**; compounds all **masculine** | 2 | **DISPUTED (incumbent held) + CANON DELTA §6.1** | der Drift · die Drifts · des Drifts | **der Eingabedrift · der Korpusdrift · der Modelldrift** (all masculine; head noun rules) · heading „### Drift — three flavours" → „**Drift – drei Ausprägungen**" (article-less, then compounds) · „Drift is answered by re-indexing" → „**Auf Drift antwortet man mit erneutem Indexieren**" · verb → „**das Korpus driftet**", „eine Zahl, **die nicht in die falsche Richtung driften darf**" · `driftCurves` = icon identifier, **class 1, not translated** | ⛔ **„die Datendrift"** — the canon prints one feminine and two masculine articles for the **same head noun** in one line; §1.1 calls exactly that the loudest MT signal · ⛔ *die Drift* (incumbent is masculine) · ⛔ *die Abweichung* (measures against a spec, not against time) · ⛔ *das Abdriften* as a terminus | `DISPUTED, held` + `CORPUS: the NOUN has never shipped (0 in 27 pages); the VERB has (driften/driftet/wegdriften/Abdriften, 5 sentences). Part III is the first place the noun is unavoidable.` Compounds: `COINED (probation)` — run2 measured `insource:` = **0** for `Datendrift`, `Modelldrift`, `Konzeptdrift`, `Eingabedrift`, `Korpusdrift`; the canon's „besser belegt" claim does not hold |
| **regression** (15 nominal + **5 verbal**, 5 files) | **die Regression** with a mandatory first-mention gloss | 3 | **BOUND — CORPUS PRECEDENT, and the gloss is a blockstring** | die Regression · die Regressionen · der Regression | **Blockstring, shipped twice word-for-word:** „die echte **Regression** (**eine durch eine Änderung verursachte Verschlechterung**)" · „eine Regression **abfangen / erkennen / zuordnen**" · `frozen regression set` → „**der eingefrorene Regressionsdatensatz**" | ⛔ **regredieren** (Duden: psychology and law only) — **and this is exactly where the concordance's dropped verb forms bite**: „can regress quality" → „**kann die Qualität verschlechtern**"; „if the new tune regresses" → „**wenn die neue Fassung schlechter abschneidet**"; Mermaid `Regresses?` → „**Verschlechterung?**" · ⛔ *der Regressionsfehler* as the umbrella · ⛔ *Regressionstriage* | `CORPUS(11+, gloss shipped verbatim ×2)` + `CANON SETTLED`. `RECONCILED (run1 alone caught that the concordance drops the 5 VERBAL occurrences — verified: `\bregress(es\|ed)?\b` = 5. Run2 read 15 and missed them.)` ⚠ In Part III `regression` stands next to statistics vocabulary („policy-gradient update") — the gloss is not a formality here |
| **incident** (7, 3 files) | **der Vorfall** | 3 | **BOUND — Stufe 1 + corpus** | der Vorfall · die Vorfälle · des Vorfalls | „signed before any incident, not during it" → „**vor jedem Vorfall unterschrieben, nicht während eines Vorfalls**" · „a production incident waiting for its first legitimate user" → „**ein Vorfall im Produktivbetrieb, der auf seinen ersten legitimen Nutzer wartet**" · „Provider outages and 429s aren't incidents; they're weather." → „**Ausfälle beim Anbieter und 429er sind keine Vorfälle, sondern Wetter.**" | ⛔ *der Incident* with a German article (the Stufe-1 source uses the loan **only in the family title**) · ⛔ *die Störung* — 13 : 117 against at BSI, and in German ITIL a **narrow** term (the reported outage); the corpus also means quality incidents without an outage · ⛔ *der Zwischenfall* (accident/diplomacy register) · ⛔ *der Produktionsvorfall* (coinage; the **phrase** carries it: *Vorfall im Produktivbetrieb*) | `UNION — stronger than either run alone.` run1: BSI DER.2.1 full-text **Vorfall/Vorfälle 117 : Störung 13 : Incident 10** (all ten in the family title). run2: Duden `Vorfall` full paradigm in the right sense. Me: `CORPUS(2 bare: „in die ein Vorfall gehört", „so bleibt ein wirklicher Vorfall eine Stunde lang unbemerkt" + 2 compounds: Datenschutzvorfall, Sicherheitsvorfall)`. ⚠ run2's measured dominance trap (Duden's `Vorfall` word profile is politically loaded) is real → never as the lone first word of a heading |
| **runbook** (3, 1 file) | **das Betriebshandbuch (BHB)** | 3 | **BOUND — MUST NOT REGRESS** | das Betriebshandbuch · die Betriebshandbücher · des Betriebshandbuchs | ⚠ **needs a SENTENCE, not a swap.** The English has a copula („the incident loop **is** a runbook") and „Die Schleife ist ein Betriebshandbuch" is a category error. Bind: „**Im Produktivbetrieb steht sie im Betriebshandbuch – als feste Abfolge, die eine Kollegin nachts um drei abarbeiten kann.**" · heading „### The incident loop, now a runbook" → „**Die Schleife bei einem Vorfall – jetzt im Betriebshandbuch**" | ⛔ *das Runbook* · ⛔ *das Ablaufhandbuch*, *die Handlungsanweisung* (coinages beside an officially set form) | `CANON SETTLED, Stufe 1 (BSI OPS.1.1.1: Betriebshandbuch 4 : Runbook 0)` + `AGREED×2`. `RECONCILED (run2's copula catch adopted; run1's straight swap would have shipped the category error.)` ⚠ honest referent note, no ⛔: BSI's *Betriebshandbuch* is a **document per IT component**, our runbook a **procedure**. The stretch is real; the canon already decided it; nothing new is coined here. **`Betriebshandbuch` is 0× in the shipped RAG corpus** — it lives in the AI-SDLC canon, so Part III is its first RAG-course use |
| **on-call** (0) | — | — | **NULL, triple-verified** | — | `Bereitschaft`/`pager`/`rotation` also 0 | — | `AGREED×2` + my grep = 0. The `Bereitschaftsdienst` question is **not raised** by Part III |
| **postmortem** (0) | — | — | **NULL, triple-verified** | — | — | — | `AGREED×2` + my grep = 0. The OPEN row (`_language.md` §1.1.f, `ai-sdlc.md` §4) is **neither closed nor burdened** by this wave |
| **AI delta** (6, 3 files, **H2 on two pages**) | **OPEN as a word — ships a BOUND CONSTRUCTION.** Head noun **der Unterschied** + obligatory `zu`-complement at first mention per page. See SC-7 | 3 | **OPEN (incumbent held: the construction; closes when a German trade sentence inflects `Delta` for a QUALITATIVE difference — „des KI-Deltas", „ein qualitatives Delta")** | — | **The three binding strings:** heading 1 → „**Docker – wo der Unterschied wirklich liegt**" · heading 2 → „**Was sich mit der KI ändert: Artefakt und Test**" · definition line → „**Der Unterschied zur gewöhnlichen Anwendung: was sich ändert, sobald ein Sprachmodell im Spiel ist.**" · counting anaphora → „**Der zweite Unterschied** ist der Zugriff auf die GPU." / „**Der dritte** ist der Cold-Start." · plural → „**Die Unterschiede bei Gewicht, GPU-Zugriff und Cold-Start**" | ⛔ **das KI-Delta** — 0 attestation; every attested German sense of `Delta` is a letter, a place, a virus or a **measurable numeric difference** (DWDS: Buchstabe, NATO-Alphabet, Flussmündung, SARS-CoV-2-Variante, Börsen-Delta); ours is qualitative · ⛔ *der KI-Unterschied*, *die KI-Differenz*, *das KI-Spezifikum*, *der KI-Zuschlag* (coinages) · ⛔ **„einen/den Unterschied machen"** — **Duden marks the collocation itself as a calque**: under `Unterschied` sense 1, „das macht keinen Unterschied **(umgangssprachlich; … nach englisch *it makes no difference*)**". Colloquial **and** flagged as an anglicism. So „der Unterschied, den die KI macht" falls too · ⛔ **bare `der Unterschied`** at first mention — in a book full of comparisons the `zu`-complement must be there | `AGREED×2 on OPEN` + `CANON-VERBATIM (rag.md §3 pilot corpus form: „Hier liegt der entscheidende Unterschied zur gewöhnlichen API-Entwicklung.")`. ⚠ **The task brief's line „KI-Delta with Durchkopplung" contradicts BOTH sheets AND the canon** — see §7.1. If stage 2 nonetheless closes the row toward the loan, the **exact string is `das KI-Delta`** (Durchkopplung per § 45 E1; the canon already writes the candidate hyphenated) — but it would be a coinage on zero evidence |
| **delta** (bare, 8 free-standing of 14, 5 files) | **der Unterschied** (countable) | 3 | **BOUND (construction)** | der Unterschied · die Unterschiede · des Unterschieds | „Line them up and the durable teaching point is the delta" → „…ist **der Unterschied**, nicht die Funktionsliste." (the reference is covered by the preceding clause — the `zu` obligation binds at **first mention**) | as above | `AGREED×2` |
| **change** (59, 8 files) | **die Änderung**; verb **ändern / sich ändern** | 3 | **BOUND — CORPUS PRECEDENT** | die Änderung · die Änderungen · der Änderung | „Every change … runs the golden set" → „**Jede Änderung** an Prompt, Modell, Index oder Config läuft gegen den Goldstandard." · „a prompt change is a cost change" → „**Eine Änderung am Prompt ist eine Änderung an den Kosten.**" (parallelism kept) · Mermaid `Change` → „**Änderung**" | ⛔ *der Change* (loan; the German ITIL *Change* is a narrower process object) · ⛔ **„Eine Prompt-Änderung ist eine Kosten-Änderung"** — noun chain on an English frame, §1.4 · ⛔ *die Veränderung* as the terminus — reserve the pair: **die Änderung** = what you do · **die Veränderung** = what happens to the world underneath | `CORPUS(several, incl. the Regression gloss „eine durch eine Änderung verursachte Verschlechterung" ×2 verbatim)` + `AGREED×2`. Count **59** (concordance + run2 + my grep); run1's 63 is wrong |

---

## 2 · Sense cards

Every card ships a **question to ask before writing** and **a worked German sentence per branch**.

### SC-1 · `snapshot` — 29 occurrences, 9 of 10 files, TWO referents

**Question before writing:** *Kann ich diesen Zustand zurückspielen — oder sage ich nur, dass dieses Bild altern wird?*

| Branch | n (hand-counted by me from the concordance) | Ruling | Worked German sentence |
|---|---|---|---|
| (A) restorable saved state — index, corpus, memory, DB | **10** | **der Snapshot** · des Snapshots · die Snapshots | „**Der Index rollt nur zurück, indem Sie den vorherigen Snapshot wiederherstellen – und eine erneute Ingestion, die an Ort und Stelle überschreibt, hat keinen Snapshot mehr, den sie wiederherstellen könnte.**" · „**Der Index muss versioniert sein: ein benannter Snapshot, den Sie wieder festlegen können.**" · card label → „**Korpus-Snapshot**" |
| (B) dated picture that will age — product names, rosters, prices, tool lists | **19** | **die Momentaufnahme** · der Momentaufnahme · die Momentaufnahmen | „**Alles Folgende ist eine Momentaufnahme von Mitte 2026; wie in Teil 1 sind die Produktnamen datiert, und was bleibt, ist die Kategorie darunter.**" · „**Namen sind Momentaufnahmen.**" · „**Behandeln Sie jede Produktbezeichnung als Momentaufnahme.**" |
| (C) micro-referent, 1×: a provider issuing **date-stamped model versions** | **1** (inside the 10) | neither — it is a **version**, not a picture and not a restore point | „…, veröffentlicht Ersetzungszuordnungen und gibt **datierte Versionsstände** aus – oft mit dem Datum in der Kennung." |

**Why the split holds and is not ornament.** `llmops/deep-dive.md` uses **both** senses: „a dated snapshot to
re-check" and „it rolls back only by restoring the previous snapshot". One German word for both puts two
referents under one terminus **on a single page** — the direction-wobble of §1.0, one storey down.

**And branch (B) is the majority AND already shipped.** `die Momentaufnahme` occurs **5×** across 4 delivered
pages in exactly this sense („behandeln Sie die Einteilung als Momentaufnahme, die bereits altert").
Part III's dominant `snapshot` sense is therefore **not a gap to fill but a ruling to apply**.

**Boundary to `Checkpoint` — mandatory, because the corpus ships `Checkpoint` 31×:**
- **der Snapshot** = restorable copy of a **data state** (index, corpus, database, VM, memory).
- **der Checkpoint** (kept-EN, `rag.md` §2) = saved **run or training state** (a `Durchlauf` resuming; a training checkpoint).
- Part III has exactly one occurrence that tests the line: „it pauses at the cap and emits **a deployable checkpoint**" (Azure RFT) → „**ein auslieferbarer Checkpoint**", **not** *Snapshot*.
- **Test:** *Wurde etwas GESPEICHERT, um weiterzurechnen (Checkpoint) — oder KOPIERT, um zurückzukönnen (Snapshot)?*

### SC-2 · `freeze` / `frozen` — five branches, two of which must never touch

**Question before writing:** *Hört hier absichtlich etwas auf (Prozess) — oder bleibt hier ungewollt etwas stehen (Technik)?*

| Branch | n | Ruling | Worked German sentence |
|---|---|---|---|
| (i) release freeze — the org stops shipping | ~10 | **der Release-Freeze**; verb **einfrieren + Akk.** | „**Ist das Budget aufgebraucht, werden alle Änderungen und Releases eingefroren – außer P0-Korrekturen und Sicherheits-Patches.**" · „**Wer den Freeze ausruft, muss in der Richtlinie namentlich benannt sein.**" |
| (ii) event loop — a blocking call halts everything | 3 | **lahmlegen** / **blockieren** — ⛔ *einfrieren* | „**Ein blockierender Aufruf in einem `async def`-Handler legt die gesamte Event-Loop lahm – und mit ihr jede gleichzeitige Anfrage in diesem Prozess.**" |
| (iii) the standing-still eval set | ~5 | attributive **eingefroren** | „**Ein eingefrorener Regressionsdatensatz beantwortet die Frage ‚Habe ich kaputt gemacht, was funktioniert hat?' – und dafür muss er stillstehen.**" |
| (iv) frozen weights (LoRA) | 3 | **eingefrorene Basisgewichte**; *frozen at training time* → **zum Trainingszeitpunkt festgeschrieben** | „**LoRA trainiert einen kleinen Adapter über eingefrorenen Basisgewichten.**" |
| (v) the wordplay (frozen config ↔ frozen behaviour) | 1 | keep the repetition | „**Eine eingefrorene Konfiguration bedeutet noch kein eingefrorenes Verhalten, weil die Welt darunter sich bewegt.**" |

⚠ **The expensive error this card prevents — and it is factual, not stylistic.** Duden's **transitive**
`einfrieren` means „auf dem augenblicklichen Stand **belassen**" (examples: „ein Projekt, die Preise
einfrieren"), Perfekt with **hat**. „Der Aufruf friert die Event-Loop ein" therefore asserts a **deliberate**
shutdown — precisely what the organisation does at a Release-Freeze, defined in the same lesson block. Duden's
*intransitive* sense („der Rechner ist eingefroren") does fit, but it is intransitive with **sein** and carries
no object.

⚠ **And the valency flips.** The English is intransitive at (i) („all changes and releases **freeze**"); German
is not. Use the **passive** („alle Änderungen und Releases **werden eingefroren**") or name the agent („die
Organisation **friert** alle Releases **ein**"). „Releases frieren ein" ✗ — then something turns to ice.

Branch (iv) keeps *eingefroren* because it sits in a different chapter and the ML collocation is standard —
but **on a page that also carries branch (i), switch (iv) to *festgeschrieben***.

### SC-3 · `pin` — 37 occurrences, three referents, two of them in the same book

**Question before writing:** *Lege ich eine VERSION fest, halte ich DATEN an einem Ort, oder BINDE ich jemanden an eine Auswahl?*

| Branch | n | Ruling | Worked German sentence |
|---|---|---|---|
| (a) fix a version (model, index, prompt registry) | ~32 | **die Modellversion festlegen**; noun **das Model-Pinning** (kept-EN, glossed) | „**Legen Sie exakte Modellversionen fest. Anbieter kündigen Modelle ab und schalten sie ab; ein Alias ohne festgelegte Version ändert das Verhalten ohne Ihr Zutun.**" · „**Model-Pinning** (das Festlegen auf eine exakte Modellversion) macht aus dieser Überraschung wieder eine Entscheidung." · „**Bleibt der neue Tune zurück, legen Sie wieder den Vorgänger fest.**" |
| (b) hold data in a region | 2 | **in der Region halten** / **an einen souveränen Endpunkt binden** | „**Daten aus Gründen der Datenresidenz in der Region zu halten, kann den Zugriff auf günstigere regionsübergreifende Kapazität kosten.**" |
| (c) tie you to a feature set | 1 | **binden an + Akk.** | „**Es bindet Sie an den kleinsten gemeinsamen Nenner, sodass das native Prompt-Caching eines Anbieters hinter der einheitlichen Schnittstelle wegfallen kann.**" |

**Why (a) is not a choice:** the delivered Part I writes the practice in German **and links this lesson by
name** — „(Die Modellversion so **festzulegen**, dass der Anbieter sie nicht unter Ihnen wegziehen kann, ist
eine LLMOps-Praxis; sie gehört in die *Lektion zu LLMOps*.)" A Part III that renames it breaks a forward
reference that has already shipped.

**One referent, two shipped German verbs (resolved):** Part I writes **festlegen** (model version), Part II
writes **festschreiben** („Geprüfte Server mit **festgeschriebener** Version … **schreiben Sie eine Version
fest**", MCP deep-dive). Part III takes **festlegen** — the Part I sentence names Part III as the home of the
practice and hands over the label with it. `festschreiben` stays correct in its Part II sentence (different
object, different lesson) and is **not** imported.

### SC-4 · `promote` — four branches, one English word, ⛔ *promoten* in all four

**Question before writing:** *Wandert etwas in einen anderen BESTAND, auf eine höhere STUFE, auf mehr TRAFFIC, oder von einer Praxis zu einer REGEL?*

- **Bestand** (5×): „promote this bad trace to an eval case" → button label, infinitive: „**Trace in den Goldstandard übernehmen**"; in prose, the shipped intransitive: „**Die Traces, an denen sich eine Regression zeigt, steigen zu neuen Fällen im Goldstandard auf.**"
- **Stufe** (2×): „start on `noop` …, then promote to `exception` / `fix`" → „zuerst auf `noop` …, dann **auf `exception` bzw. `fix` hochstufen**."
- **Traffic** (1×): „the change auto-promotes to full traffic" → „**Die Änderung wird automatisch auf den vollen Traffic ausgeweitet.**"; Mermaid `Auto-promote → 100%` → „**Automatisch auf 100 % ausweiten**" (percent sign with a narrow no-break space, § Typografie).
- **Regel** (1×): „model-tier routing **promoted from a tactic to a rule**" → „**das Routing nach Modellklasse, vom Kniff zur Regel erhoben**."

### SC-5 · `deploy` / `deployment` — the countable *a deploy* is the whole decision

**Question before writing:** *Rede ich über den VORGANG, über EIN Auslieferungsereignis, oder über eine bereitgestellte INSTANZ beim Anbieter?*

- **Vorgang / Disziplin** → **die Bereitstellung** (shipped 5×): „**Wo der Server läuft, bleibt eine Frage der Bereitstellung.**"
- **Ein Ereignis** (~21×; English shortens *deployment* → *a deploy*) → **das Deployment**, shipped countable: „**Jede Änderung an einem der fünf Artefakte ist ein Deployment.**" · „**Ein Alias ohne festgelegte Version ist ein Deployment, das Sie nicht eingeplant haben.**" ⛔ „ein Deploy".
- **Anbieterinstanz** (Azure/Bedrock) → **die bereitgestellte Instanz**: „**Die bereitgestellte Instanz eines nachtrainierten Modells rechnet pro Token ab, dazu kommt eine Stundengebühr.**" ⛔ „das Deployment rechnet ab" (asserts the *process* costs money).
- `air-gapped deployments` (6×) → **die vollständig abgeschotteten Betriebsumgebungen** — third referent, third word.
- Compound: „the deploy checklist" → „**die Checkliste für das Deployment**" (⛔ „im Deployment-Checkliste", a run2 typo worth not inheriting).

### SC-6 · `gate` — three uses, three constructions, none of them a word

**Question before writing:** *Nenne ich den festen Terminus, zähle ich Prüfungen, oder ist `gate` hier ein Verb?*

- **fester Terminus** (`quality gate`) → **das Quality Gate**; in a compound **die Quality-Gate-Regel**.
- **gezähltes Objekt** („Gates are not equally expensive", „a pipeline needs gates between the steps") → **die Prüfung / die Prüfungen**: „**Nicht jede Prüfung kostet gleich viel.**" · heading: „**Zwischen den Schritten steht je eine Prüfung**".
- **eingefügter Check** („put corpus updates through the same gate") → **eine Prüfung vorschalten** (canon Korpusform; shipped verbatim as „Schalten Sie eine Prüfung vor, die die Argumente ansieht"): „**Schicken Sie Korpus-Aktualisierungen durch dieselbe Prüfung wie alles andere.**"
- **Verb** (`gates the deploy`, 2× Mermaid edge label) → Mermaid, short: „**gibt das Deployment frei**"; in prose: „**lässt die Bereitstellung nur nach Freigabe zu**" (canon Korpusform, shipped verbatim in `tool-use/deep-dive.md`).
- **struktureller Punkt**, where a noun is unavoidable → **der Kontrollpunkt** (canon incumbent) — ⚠ **use last**: it is **0×** in the shipped 27 RAG pages; its only delivered occurrence is the AI-SDLC UI heading „Gestaffelte Kontrollpunkte", a different course.
- **Verb-nach-Objekt (§1.5):** eine Prüfung **schaltet man vor**; eine Prüfung **blockiert** den Merge (`blockieren` is shipped: „Ein Hook, der *blockiert*"); ein Deployment **wird freigegeben**. ⛔ „das Gate **feuert**", ⛔ „durch das Gate **gehen**".

### SC-7 · `AI delta` — a heading on two pages; the ruling is a construction with a mandatory complement

**Question before writing:** *Wovon unterscheidet sich das hier? — und steht dieser Bezugspunkt im Satz?*

- **Heading, „where it is"** → „**Docker – wo der Unterschied wirklich liegt**".
- **Heading, „what it consists of"** → „**Was sich mit der KI ändert: Artefakt und Test**".
- **Definitionszeile** („AI delta: what changes when an LLM is in the loop") → „**Der Unterschied zur gewöhnlichen Anwendung: was sich ändert, sobald ein Sprachmodell im Spiel ist.**"
- **Negation** („there is no AI delta to speak of") → „**Dann gibt es keinen nennenswerten Unterschied zur gewöhnlichen Anwendung.**"
- **Zählende Anapher** → „**Der zweite Unterschied ist der Zugriff auf die GPU.**" · „**Der dritte ist der Cold-Start.**"
- **Comparison anchors Part III supplies itself:** „zur gewöhnlichen API-Entwicklung", „zum klassischen DevOps", „zum gewöhnlichen Docker-Betrieb", „zur gewöhnlichen Warteschlange".
- ⛔ „**den Unterschied machen**" — Duden marks the phrase itself as a calque (*nach englisch it makes no difference*), so the obvious rendering „der Unterschied, den die KI macht" falls with it. Use „**Der Unterschied entsteht erst, wenn das Modell im Container liegt.**"

---

## 3 · RUN DISAGREEMENTS

Both positions recorded; my resolution and the reason follow each.

**3.1 · `snapshot` sense split — and the brief is wrong too (the slice's most consequential row).**
run1: 12 restorable : 17 dated picture. run2: 10 : 19, hand-counted. The **task brief** asserts a third thing:
that Part III's 29 are „overwhelmingly a **pinned model version**".
**Resolution: run2, verified independently.** I classified all 27 concordance units myself: (A) restorable =
**10** (`corpus snapshot` label, „snapshot the corpus", memory snapshot ×2, cold-start snapshots, index
snapshot, timestamped snapshots, „the previous snapshot" ×2, „a named snapshot you can re-pin"); (B) dated
picture = **19**. The brief's framing does not survive the text: **exactly one** occurrence is the
pinned-model-version referent („issues timestamped snapshots — often with the date in the id"), and it is a
version, not a picture. **The outcome the brief wanted is unchanged — two referents, never collapsed — but the
dominance flips, and that matters: the majority sense is the one the corpus has already shipped 5× as
`die Momentaufnahme`.** The stronger evidence lands on the bigger half.

**3.2 · The countable *a deploy* — a frontal contradiction, settled by the shipped corpus.**
run1: „Eine Änderung an einem davon ist **ein Deployment**." run2: „Jede Änderung an einem der fünf Artefakte
ist **eine Bereitstellung**." Both call their own line the lesson's core sentence.
**Resolution: run1.** The delivered German already uses the **countable** `ein Deployment` (4 occurrences:
„am Status eines Deployments", „Hat ein Deployment die Prompt-Vorlage geändert?", „einem Deployment", Mermaid
„(ein Deployment)") and reserves **die Bereitstellung** for the process/discipline (5 occurrences). run1 called
the countability „the real decision of this row, and it is new" — it is **not new, it is shipped**, which is the
issue-#328 shape a third time.

**3.3 · `die CI` — both runs undercount their own strongest evidence.**
run1: „HOUSE — der Incumbent steht im Kanon, ein Beleg für das nackte Kürzel fehlt." run2: „WEAK — Genus
ausgeliefert, **zwei Seiten**."
**Resolution: CORPUS PRECEDENT(4).** Four occurrences of „in der CI" on **three independent pages**
(`part-2-agents/real-agents.md`; `…/evaluation/deep-dive.md` ×2; `…/evaluation/index.md`), every one Dativ
feminine. This is a delivered ruling, not a house form and not two pages.

**3.4 · `pin` family size.** run1: 32. run2: 37. Concordance: 20.
**Resolution: 37 (run2), verified by my grep** (`pins?` 10 · `pinned` 7 · `pinning` 10 · `re-pins?` 3 ·
`re-pinning` 4 · `unpinned` 3). run1 was right that the extractor drops participles but produced its own wrong
total. `re-pin` and `unpinned` carry half the rollback section's argument.

**3.5 · Which counts the concordance actually drops.** run1 found 19 dropped occurrences and listed them
(`pinned` 7, `unpinned` 3, `regress*` 5, `deployable` 5, `promoted` 2, `Deprecated` 1, `gated` 1,
`redeployment` 1); run2 found the `pin` gap but read `regression` as 15 and missed the five verbal forms — the
exact five where the canon's ⛔ on *regredieren* bites.
**Resolution: run1's defect report is adopted; run1's corrected totals are not.** My greps: `gates?` **31**
(not run1's 32 — `gated` is a separate, non-release sense), `changes?` **59** (not 63), pin family **37**
(not 32), `regress(es|ed)` **5** ✅, `deployable` **5** ✅, `gated` **1** ✅.

**3.6 · `deprecation`.** run1 declined to attest and left the row WEAK-with-no-source, saying so honestly.
run2 attested `die Abkündigung / abkündigen / abgekündigt` (de.wikipedia *macOS*, case-marked; 94 articles with
`abgekündigt`) **and** measured the register trap (4 of the top 5 `Abkündigung` hits are ecclesiastical).
**Resolution: run2.** A row with evidence beats a row with a declared blank — and run2's own trap-measurement
is what makes it safe to use (bind the phrase, prefer the participle).

**3.7 · `Deprecated` as a status label.** run1 spotted that `Active, Legacy, Deprecated, Retired` is a
provider **status list** (class 1, untranslated) — a different class from the verb. run2 missed it entirely.
**Resolution: run1.** Verified in `llmops/index.md`.

**3.8 · `Prompt-Registry` plural.** run1 cited the canon row (`die Registries`, SETTLED). run2 proposed
`die Registrys` as an admitted house guess.
**Resolution: run1 — and run2's proposal is a regression against an existing canon row.** Flagging it because
„I am guessing and I say so" is not a licence to overwrite a settled line.

**3.9 · `Canary Release` spelling.** run1 kept the canon's spread `das Canary Release`. run2 re-spelled to
`das Canary-Release`, arguing § 45 E1 (Subst.+Subst.) and pointing at the hyphenated heise citation **inside
the same canon row**.
**Resolution: hold the incumbent for wave 3, file the delta (§6.2).** run2's argument is good and may well
win — but a spelling flip decided inside one slice puts two spellings of a 12-occurrence term on the same page
set. This is a canon-level orthography question spanning `Canary Release`, `Shadow-Deployment`,
`Prompt-Registry`, `Quality Gate` and `Release Gate`; it must be settled once, above the slice.

**3.10 · `gate` — do the runs actually disagree?** No. run1: „OPEN bleibt — Incumbent gehalten"; run2:
„BLEIBT OPEN — Teil III schließt die Zeile nicht und erzwingt sie auch nicht." Per the brief's default that is
**OPEN with the incumbent held**, and both runs ship constructions. They differ only in inventory: run1 has the
`licence-gated` sense (run2 missed it); run2 has the counted-object branch `die Prüfung/die Prüfungen` and the
new-and-rejected candidate *der Synchronisationspunkt* (run1 missed both). **The union is the ruling.**

**3.11 · `rollback` verb.** run1: only *zurücksetzen*. run2: *zurückrollen* **oder** *zurücksetzen*, and found
that the Deployment-sense verb is attested **inside the canon's own citation** („ein reibungsloses
**Zurückrollen**", informatik-aktuell, in the `Canary Release` row).
**Resolution: both, split by object** — *zurückrollen* for a deployment, *zurücksetzen* for a prompt or a
version. run2's find is genuinely new evidence about an existing canon line.

**3.12 · The shared blind spot both runs named, in different places.** run1: „`Freeze`, `CI`, `Model Pinning` —
bei allen dreien ist die naheliegende Recherche dieselbe; zwei übereinstimmende WEAK-Zeilen sind **nicht** eine
SETTLED-Zeile." run2: „wenn ein Sinn im **englischen Quelltext** mehrdeutig ist … produzieren zwei unabhängige
Läufe **denselben** Fehler mit doppelter Zuversicht" (its example: „stopped at the gate" — merge or
deployment?; it ruled *both* rather than deciding).
**Resolution: both warnings stand and are carried into §7.** Note that two of run1's three (`CI`, `pinning`)
were in fact closed by the *corpus*, not by more web research — which is the general lesson.

---

## 4 · VOCABULARY FOOTPRINT

Flat, deduplicated list of every German content word appearing in this ledger's worked sentences and sense
cards. Stage 2 uses it for cross-slice collision detection.

`Abfolge` · `Abkündigung` · `abkündigen` · `abgekündigt` · `abgeschottet` · `abschalten` · `Abschaltung` ·
`Alias` · `Anbieter` · `Anfrage` · `Artefakt` · `Ausfall` · `ausrollen` · `ausweiten` · `auslieferbar` ·
`ausliefern` · `Auslieferung` · `Basisgewichte` · `Bereitstellung` · `bereitstellen` · `bereitgestellt` ·
`Betriebshandbuch` · `Betriebsumgebung` · `binden` · `blockieren` · `Canary Release` · `Checkliste` ·
`Checkpoint` · `Cold-Start` · `Config` · `Datenresidenz` · `Datensatz` · `Deployment` · `Drift` · `driften` ·
`durchfallen` · `eingefroren` · `einfrieren` · `Endpunkt` · `Ereignis` · `erheben` · `Event-Loop` ·
`Evaluierung` · `Fassung` · `festlegen` · `Festlegung` · `festgeschrieben` · `Freeze` · `Freigabe` ·
`freigeben` · `Freigabekriterien` · `Funktionsliste` · `Gateway` · `Goldstandard` · `GPU` · `halten` ·
`hochstufen` · `Index` · `Ingestion` · `Instanz` · `Kategorie` · `Kennung` · `Kniff` · `Konfiguration` ·
`Kontrollpunkt` · `Korpus` · `Kosten` · `lahmlegen` · `laufen` · `lizenzpflichtig` · `Merge` · `Modell` ·
`Modellklasse` · `Modellversion` · `Model-Pinning` · `Momentaufnahme` · `Nenner` · `Produktbezeichnung` ·
`Produktivbetrieb` · `Prompt` · `Prompt-Registry` · `Prüfung` · `Quality Gate` · `Regressionsdatensatz` ·
`Regression` · `Release` · `Release-Freeze` · `Richtlinie` · `Rollback` · `Rollback-Pfad` · `Routing` ·
`Schattenbetrieb` · `Schnittstelle` · `Shadow-Deployment` · `Sicherheits-Patch` · `Snapshot` · `Sprachmodell` ·
`stillstehen` · `Traffic` · `Trace` · `übernehmen` · `Unterschied` · `Verhalten` · `Veränderung` · `Version` ·
`Versionsstand` · `Versionsverwaltung` · `versioniert` · `veröffentlichen` · `Verkehr` · `verschlechtern` ·
`vorschalten` · `Vorfall` · `Vorgänger` · `Warteschlange` · `Wetter` · `wiederherstellen` · `Zugriff` ·
`zurückrollen` · `zurücksetzen` · `zurückspielen` · `Änderung`

⚠ **Cross-slice collision candidates I can already see from my own list** (stage 2 decides, not me):
`die Prüfung` (slice E's counted `gate` **and** likely the eval/guardrails slices' `check`/`validation`);
`die Evaluierung` (head noun owned by the eval slice — my „Eval in der CI" borrows it);
`die Instanz` (my `deployment` sense (b) vs any object-instance use);
`der Durchlauf` (I do **not** write it, but SC-1's Checkpoint boundary leans on it — 54× shipped, must not regress);
`die Warteschlange`, `das Budget`, `der Hebel`, `die Laufzeit` (declared cross-slice in the brief; my only
contact is the AI-delta anchor „zur gewöhnlichen Warteschlange" and the Freeze branch (i) mention of a budget);
`die Fassung` (I use it for *tune/version* in two rejected-verb rewrites while ⛔-ing it as the terminus for
`version` — stage 2 should confirm that split reads as deliberate);
`festlegen` (this slice binds it for `pin`; if another slice binds it for `set`/`define`, they collide).

---

## 5 · SPREAD (from the concordance; per Part III file)

Terms spanning **≥3 files need ONE binding string decided centrally** — marked ★.

| Terminus | n | files | distribution |
|---|---|---|---|
| ★ **snapshot** | 29 | **9** | cloud-platforms/deep-dive 7 · serving/deep-dive 4 · llmops/deep-dive 4 · cloud-platforms/index 3 · production-failures 2 · tooling-ecosystem/index 2 · tooling-ecosystem/deep-dive 2 · llmops/index 2 · serving/index 1 |
| ★ **deploy** | 30 | **9** | llmops/index 13 · llmops/deep-dive 5 · tooling-ecosystem/deep-dive 3 · cloud-platforms/deep-dive 2 · tooling-ecosystem/index 2 · overview 1 · production-failures 1 · serving/deep-dive 1 · cloud-platforms/index 1 |
| ★ **change** | 59 | **8** | llmops/deep-dive 17 · llmops/index 14 · production-failures 8 · serving/index 6 · cloud-platforms/deep-dive 4 · tooling-ecosystem/deep-dive 4 · serving/deep-dive 2 · cloud-platforms/index 2 |
| ★ **release** | 42 | **6** | llmops/deep-dive 19 · production-failures 8 · llmops/index 7 · overview 1 · tooling-ecosystem/index 1 · tooling-ecosystem/deep-dive 1 |
| ★ **version** | 30 | **6** | llmops/index 11 · llmops/deep-dive 8 · production-failures 7 · serving/deep-dive 1 · cloud-platforms/deep-dive 1 · tooling-ecosystem/deep-dive 1 |
| ★ **deployment** | 14 | **6** | cloud-platforms/deep-dive 6 · production-failures 2 · llmops/index 2 · serving/deep-dive 1 · cloud-platforms/index 1 · llmops/deep-dive 1 |
| ★ **gate** | 31 | **5** | llmops/deep-dive 13 · production-failures 9 · llmops/index 5 · tooling-ecosystem/index 2 · tooling-ecosystem/deep-dive 2 — ⚠ **`gateway` = 31 in the same file set** |
| ★ **regression** | 15 (+5 verbal) | **5** | llmops/deep-dive 6 · llmops/index 4 · production-failures 3 · tooling-ecosystem/index 1 · tooling-ecosystem/deep-dive 1 |
| ★ **delta** | 14 | **5** | serving/index 6 · llmops/index 3 · cloud-platforms/deep-dive 2 · llmops/deep-dive 2 · serving/deep-dive 1 |
| ★ **promote** (+promotion) | 7 | **4** | tooling-ecosystem/deep-dive 3 · llmops/deep-dive 2 · tooling-ecosystem/index 1 · llmops/index 1 |
| ★ **pin** / **pinning** | 20 in concordance, **37 with participles** | **4** | llmops/deep-dive 8 · llmops/index 5 · cloud-platforms/deep-dive 3 · production-failures 2 · tooling-ecosystem/deep-dive 1 |
| ★ **drift** | 18 (+1 icon prop) | **4** | production-failures 8 · llmops/index 7 · llmops/deep-dive 2 · tooling-ecosystem/deep-dive 1 |
| ★ **CI** | 18 | **4** | tooling-ecosystem/index 5 · tooling-ecosystem/deep-dive 5 · llmops/index 5 · llmops/deep-dive 3 |
| ★ **freeze** | 16 | **3** | llmops/deep-dive 11 · serving/deep-dive 2 · serving/index 1 |
| ★ **frozen** | 11 | **3** | production-failures 5 · llmops/deep-dive 4 · llmops/index 1 |
| ★ **rollback** | 13 | **3** | llmops/deep-dive 8 · production-failures 4 · llmops/index 1 |
| ★ **canary** | 12 | **3** | llmops/index 6 · llmops/deep-dive 4 · production-failures 2 |
| ★ **artefact** | 17 | **3** | llmops/deep-dive 10 · llmops/index 6 · production-failures 1 |
| ★ **incident** | 7 | **3** | llmops/index 3 · llmops/deep-dive 3 · tooling-ecosystem/deep-dive 1 |
| ★ **release gate** | 7 | **3** | llmops/deep-dive 5 · tooling-ecosystem/deep-dive 1 · llmops/index 1 |
| ★ **AI delta** | 6 | **3** | serving/index 4 (incl. 1 H2) · llmops/index 1 (H2) · llmops/deep-dive 1 |
| prompt registry | 3 | 2 | llmops/index 2 · llmops/deep-dive 1 |
| roll out | 5 | 2 | llmops/index 4 · production-failures 1 |
| shadow deployment | 2 | 1 | llmops/index 2 |
| rollout (noun) | 1 | 1 | llmops/index 1 |
| runbook | 3 | 1 | llmops/index 3 |
| deprecation / deprecate | 2 | 1 | llmops/index 2 |
| CD | 1 | 1 | llmops/index 1 (only inside `CI/CD`) |
| gating · versioning · on-call · postmortem | 0 | 0 | true zeros, triple-verified |

**21 of this slice's terms span ≥3 files.** The ones where a drifting string would be most visible, in order:
`snapshot` (9 files, two referents), `deploy` (9), `change` (8), `release` (6), `gate` (5, beside 31 `gateway`).

---

## 6 · CANON DELTA (reported, never edited)

**6.1 · `_language.md` §1.1.e / `rag.md` §3 — the `Drift` compounds carry two genders in one line.**
*Current:* „Incumbent **der Drift**; möglichst das Kompositum schreiben — *die Datendrift*, *der Modelldrift*,
*der Konzeptdrift* sind besser belegt."
*Proposed:* „…— **der Datendrift**, **der Modelldrift**, **der Konzeptdrift**", and strike „besser belegt".
*Reason:* the head noun is `Drift` in all three; one feminine and two masculine articles for one head noun is
the wobble §1.1 names as the loudest MT signal — **inside the canon, in one line**. And run2's measurement
kills the „besser belegt" clause: de.wikipedia `insource:` = **0** for `Datendrift`, `Modelldrift`,
`Konzeptdrift`. Both runs reached this independently (run1 K-2, run2 K1). This is a **presentation defect**, not
a reopening of the DISPUTED `der` vs `die` row — `der` stands either way.

**6.2 · `_language.md` §1.3.3 — orthography of the Subst.+Subst. loans, one decision needed for five terms.**
*Current:* §1.3.3 lists „**Quality Gate**, **Release Gate** (Adj+Subst) — aber **Quality-Gate-Regel**"; §1.1.d
prints „**das Canary Release**" spread.
*Issues, both raised independently:* (i) `Quality`/`Release` are English **nouns** in attributive position, so
the governing rule is **§ 45 E1**, not § 37 E4 — the *classification* is wrong even if the *decision* stands
(run1 K-3); (ii) §1.1.d's own heise citation is hyphenated („als **Canary-Release** verfügbar"), and §1.1's
`MCP` row already writes **die MCP-Registry** durchgekoppelt, so the canon is internally inconsistent
(run2 K2).
*Proposed:* rule the family **once** — `Canary Release`, `Shadow Deployment`, `Prompt Registry`,
`Quality Gate`, `Release Gate` — and, whichever way it goes, re-label `Quality Gate`/`Release Gate` as a
**stated exception with a reason** rather than a rule consequence.
*Reason:* five terms, 12+2+3+n occurrences, several spanning ≥3 files. Deciding it inside a slice guarantees two
spellings on one page. **This ledger holds the incumbents unchanged pending that decision.**

**6.3 · `Release Gate` sits on an OPEN list and on a binding-spellings list at the same time.**
`_language.md` §1.1.f and `ai-sdlc.md` §4/§127 say **OPEN, no German attestation**; `rag.md` §2 carries
`Release Gate` in the settled kept-EN list; `_language.md` §1.3.3 prescribes its **spelling** as binding.
*Proposed:* strike or footnote the `rag.md` §2 entry as a bootstrap remnant.
*Reason:* the `Golden Set` / `Error Budget` / `Scratchpad` shape — same terminus, settled in one file, OPEN in
another. Two ledgers plus `insource:"Release Gate"` = 0 **and** `insource:"Release-Gate"` = 0 outweigh a
bootstrap list line. (run1 K-4; run2 recorded the same null independently.)

**6.4 · `_language.md` §1.1 Fallenkasten — the `Gate` trap box names one technical twin; there are two.**
*Current:* the live collision is „das Input Gate / das Forget Gate" (LSTM).
*Proposed:* add the **semiconductor** twin: de.wikipedia `insource:"des Gates"` = 35, `insource:"das Gate"` = 85,
head articles *Transistor*, *MOSFET*, *Feldeffekttransistor*, *Flash-Speicher* — a fully inflected,
gender-marked `das Gate` in electronics, with the larger count.
*Reason:* it strengthens the OPEN verdict rather than weakening it, and Part III adds a **third**, closer
collision the box does not know: `gateway` occurs **31×** in the same files, and the delivered German already
writes `Gateway` (bare `Gate` is 0× in the shipped 27 pages). That is a Part-III-specific reason the row must
stay open, and it is stronger than the LSTM argument because both words live in **this** lesson.

**6.5 · Missing §1.1 rows — the canon has no line for terms Part III uses heavily.**
No row exists for: **Release** (42), **Snapshot** (29), **Momentaufnahme** (5 shipped), **Artefakt** (17),
**CI** (18), **Vorfall/Incident** (7), **Freeze / Release-Freeze** (27), **Version** (30),
**Shadow-Deployment**, **Model-Pinning**, **Abkündigung**.
*Proposed rows* (article · plural · genitive · evidence · status):

| Terminus | Artikel | Plural | Genitiv Sg. | Attestierung | Status |
|---|---|---|---|---|---|
| **Snapshot** | **der** Snapshot | die Snapshots | des Snapshots | DWDS Bed. 3 [ITK], full paradigm **in our referent**; 17 case-marked de.wikipedia hits, all IT, none fem./neut. | **SETTLED** |
| **Momentaufnahme** (`snapshot` sense B) | **die** Momentaufnahme | die Momentaufnahmen | der Momentaufnahme | Duden, incl. the transferred example sentence; **5× shipped** | **SETTLED (CORPUS)** |
| **Release** | **das** Release | die Releases | des Releases | DWDS full paradigm **with a marked ITK sub-sense**; genus is a **choice** (DWDS licenses both) | **SETTLED (paradigm) / HOUSE (genus)** |
| **Artefakt** | **das** Artefakt | die Artefakte | des Artefakt[e]s | Duden paradigm; 2× shipped; ⚠ Duden sense 4 = *Störsignal (Elektronik)* → bind the phrase | **SETTLED (paradigm) / WEAK (software referent)** |
| **CI** | **die** CI | — | der CI | **4 shipped occurrences on 3 pages, all Dativ feminine**; compound *die CI-Pipeline* (heise) | **CORPUS PRECEDENT** |
| **Vorfall** | **der** Vorfall | die Vorfälle | des Vorfalls | BSI DER.2.1 (117 : 13 : 10) + Duden paradigm + 2× shipped | **SETTLED, Stufe 1** |
| **Release-Freeze** | **der** Release-Freeze | die Release-Freezes | des Release-Freezes | genus **inherited** from the attested `der Code-Freeze` (de.wikipedia lemma, thrice case-marked); `Release Freeze` itself = 0 hits | **HOUSE (analogy — stated)** |
| **Version** | **die** Version | die Versionen | der Version | Duden sense 3; ⚠ ⛔ collocation „die Version des Vorfalls" | **SETTLED** |
| **Shadow-Deployment** | **das** Shadow-Deployment | die Shadow-Deployments | des Shadow-Deployments | genus inherited from `das Deployment` (DWDS); loan itself 0 hits; gloss from de.wikipedia *Probebetrieb* | **WEAK (loan) / SETTLED (genus)** |
| **Model-Pinning** | **das** Model-Pinning | *kein Plural* | des Model-Pinnings | `-ing` → Neutrum, no plural: **rule** from §1.1.f (`Spotlighting` row) | **HOUSE (rule-derived)** |
| **Abkündigung / abkündigen** | **die** Abkündigung | die Abkündigungen | der Abkündigung | de.wikipedia *macOS* case-marked; `abgekündigt` 94 articles; ⚠ ecclesiastical word profile → bind the phrase | **WEAK** |

**6.6 · `_language.md` §1.1.b (`Regression`) writes „in der CI" but §1.1 has no `CI` row.**
*Reason:* the **phrase** is decided, the **abbreviation** has no entry — the `Budget`/`Cap`/`Signal` shape in
reverse. §6.5 supplies the row, now with corpus evidence rather than a house guess.

**6.7 · Dissent on record, not a request (per §5 of the brief).** `Managed Endpoint`,
`Provisioned Throughput` and `Instrumentation` are taken as given. No dissent from this slice.

---

## 7 · NEEDS A DECISION, NOT MORE RESEARCH

**7.1 · `AI delta`: the brief instructs „KI-Delta with Durchkopplung"; both sheets and the canon rule the
opposite.** `rag.md` §3 says **BLEIBT OPEN** and gives the pilot's corpus form as plain prose
(„Hier liegt der entscheidende Unterschied zur gewöhnlichen API-Entwicklung"); both runs ⛔ `das KI-Delta` on
zero attestation, with run2 adding that Duden marks the obvious fallback („einen Unterschied machen") as an
explicit calque.
**My recommendation: bind the CONSTRUCTION** (§SC-7), keep the term OPEN. **If stage 2 overrules and wants the
loan, the exact binding string is `das KI-Delta`** (Durchkopplung per § 45 E1; the canon already writes the
candidate hyphenated) — I record the string so the instruction can be executed without a second round trip.
**Cost of being wrong in my direction:** two H2 headings and one definition line read as ordinary German prose
instead of naming a coined figure the book elsewhere treats as a term; a reader loses the label but loses no
meaning. **Cost of being wrong the other way:** a coined term on zero attestation, on a heading, on two pages —
the `Latenzbudget` failure mode a third time, and headings are the least reversible place to put a coinage.

**7.2 · The orthography family (§6.2).** Nobody can research this further; § 45 E1 and the canon's own list
point opposite ways and both are already documented. **Recommendation: hyphenate the Subst.+Subst. loans
(`Canary-Release`, `Shadow-Deployment`, `Prompt-Registry`) and keep `Quality Gate` / `Release Gate` spread as a
named, reasoned exception** (they are in a binding-spellings list and `Quality Gate` is the established
kept-EN form). **Cost of being wrong:** cosmetic per instance, cumulative across 5 terms and ~20 occurrences —
and inconsistency here is exactly the signal §1.1 warns about.

**7.3 · `der Kontrollpunkt` as the noun fallback for `gate`.** It is the canon incumbent but has **0**
occurrences in the shipped 27 RAG pages; its only delivery is an AI-SDLC UI heading. **Recommendation: keep it
as the incumbent, use it last**, and prefer the shipped constructions (`die Prüfung`, `eine Prüfung
vorschalten`, `nur nach Freigabe zulassen`). **Cost of being wrong:** if Part III leans on it, the RAG course
introduces a structural noun the reader has met nowhere in Parts I–II.

**7.4 · `das Release` genus.** DWDS licenses **both** Neutrum and Maskulinum; the shipped corpus is silent (all
3 occurrences are article-less). This is a **choice**, and it must be made once for a 42-occurrence term across
6 files. **Recommendation: Neutrum** — DWDS lists it first, and every neighbouring term is Neutrum
(`das Deployment`, `das Canary Release`, `das Rollback`). **Cost of being wrong:** none semantically, but a
mid-course flip would be visible on six pages.

**7.5 · `Snapshot` and `Momentaufnahme` on the same page.** They meet in `llmops/deep-dive.md` and in
`production-failures.md`. The split is right; whether the two read well side by side is a **cold-reader**
question, not an attestation question. **Recommendation: ship the split, flag both pages for the cold read.**

**7.6 · The `frozen regression set` / `eval gate` head nouns cross the slice boundary.** I ruled the
**adjectives and constructions** („der eingefrorene Regressionsdatensatz", „die Evaluierung in der CI") and
deliberately left the **head nouns** (`Goldstandard`, `Evaluierung`, `Eval-Satz`) to the eval slice. My
sentences are built so that only the head noun swaps if that slice rules otherwise.

---

## 8 · WHAT THIS PASS COULD NOT DO

1. **It did no new lexicographic research, by design.** Every external attestation here comes from one of the
   two runs. Where the two disagreed about a source's strength I weighed the sources they quoted; I did not
   fetch a third.
2. **It could not counter-check the BSI-only rows with a heise/iX/c't full-text count.** Two rows lean on a
   single regulator document — run1's `das Freigabeverfahren` / `die Freigabekriterien` (BSI OPS.1.1.6) — and
   are labelled `THIN` rather than settled. `der Vorfall` also rests partly on BSI, but it carries a Duden
   paradigm and 2 shipped occurrences besides, so it is not thin.
3. **It could not verify run2's quotations verbatim in every case.** Spot-checking against the shipped corpus
   found run2's Part II `festschreiben` citation **paraphrased**, not quoted („Schreiben Sie die Version jedes
   Servers fest, den Sie anbinden…" vs the actual „…schreiben Sie eine Version fest und prüfen Sie bei jeder
   Aktualisierung erneut"). Content unaffected, but run2's quote marks are not always literal; treat its
   external quotations with the same caution.
4. **It could not settle the corpus counts run2 reported for the delivered German.** run2 said `Gateway` 8×,
   `Registry` 7×, `CI` on 2 pages; I measure `Gateway` **3**, `Registry` **8 sentences**, `CI` **4 on 3 pages**.
   The *directions* all hold; the numbers in run2's sheet should not be quoted downstream.
5. **It did not measure the card/Mermaid labels against the 360 px label budget.** „feste Modellversion",
   „Korpus-Snapshot", „eingefrorener Regressionsdatensatz", „Automatisch auf 100 % ausweiten" are all longer
   than their English originals. That belongs at a rendering gate.
6. **It cannot resolve genuine ambiguity in the English source.** run2 flagged one instance („stopped at the
   gate" — merge or deployment? the sentence names both) and ruled *both*. Two blind runs reading one ambiguous
   source produce the same reading with doubled confidence; a third read of the same sentence does not help.
   That one needs the English author, not a German attestation.
7. **It could not test whether the `gate` construction set stays consistent across 31 occurrences in 5 files.**
   Shipping constructions instead of a word is the right ruling and the harder one to hold; only the rendered
   pages will show whether five files converge on the same four constructions.
8. **Two rows remain honestly OPEN and should not be read as failures:** `gate` (with `release gate`) and
   `AI delta`. Both have stated closing conditions, both hold their incumbent, and both now ship worked
   sentences rather than a placeholder — which is the difference between an open row that renders and an open
   row that gets dodged.
