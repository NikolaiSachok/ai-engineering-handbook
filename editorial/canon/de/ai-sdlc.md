# AI SDLC term ledger (DE)

The **living** term ledger for the AI SDLC course in German. It records this course's term decisions —
kept-EN vs native form, casing, bridge glosses, rejected variants — the way `canon/sk/ai-sdlc.md` does for
Slovak.

**This is a bootstrap.** It carries the class policy and a register seeded from the corpus's actual
high-frequency terms. **Terms with no attestation are marked OPEN and are not settled.**

**Load with `_language.md`.** The shared German language rules (term-direction policy, the loanword table with
gender/plural/genitive, Denglisch verb morphology, Durchkopplung, regional variance, calque templates,
verb-by-object, typography, register, bridge, bold, probation) live there and are course-independent.

> **Cross-course term consistency — peek, don't load.** Load ONLY `_language.md` + this ledger as standing
> context. For a term that plausibly overlaps the RAG course (agent, prompt, token, context, eval, guardrail,
> retrieval…), do a TARGETED, read-only lookup in `canon/de/rag.md`: if a decision exists and the sense
> matches, REUSE it verbatim and cite it. If the sense genuinely differs, FLAG for a human — do not silently
> fork. Loading a whole sibling ledger as priming context is prohibited.

---

## §1 Class policy for this course

Per `_language.md` §1.0 the German default is **English-led with a German article**. This course, however,
has a **higher share of class-3 (German-led) terms than the RAG course** — its subject matter is process,
evidence and organisation, where German has real established vocabulary (*Nachweis, Prüfung, Freigabe,
Zuständigkeit, technische Schulden*), not just borrowed tool names. That is a genuine difference between the
two ledgers and not an inconsistency.

| Class | This course's members |
|---|---|
| **1 — identifiers / branded** | `MEASURED` / `REPORTED` / `ASSERTED` (code-styled, invariant), tool names, `LOD_0/1/2` as a named product's own labels |
| **2 — English-led (default)** | Harness, Hook, Skill, Reward Hacking, Blast Radius, Policy-as-Code, Quality Gate, Least Privilege, Context Rot, Hot Set / Cold Set, Commit, Branch, Pull Request, Repository, Sandbox, Rollback, Feature Flag, Trunk-based Development, Code Review, Linting, Coverage |
| **3 — German-led (larger here than in RAG)** | see §3 below |

---

## §2 Kept-EN register — seeded

*Harness, Hook, Skill, Agent, Prompt, Kontext (dt.), Context Rot, Reward Hacking, Blast Radius, Least
Privilege, Policy-as-Code, Quality Gate, Release Gate, Stage-Gate, Hot Set / Cold Set, Commit, Branch, Merge,
Pull Request, Repository, Sandbox, Rollback, Feature Flag, Canary Release, Trunk-based Development, Code
Review, Linting, Coverage, Benchmark, Proxy-Metrik, Telemetrie (dt.), SLSA, SBOM, DORA, CI/CD, Pipeline,
Deployment, Observability, Drift, Guardrails, Human-in-the-Loop (HITL), Scaffold, Spec, Runbook,
Postmortem.*

### Kept-EN with an OBLIGATORY German gloss at first mention

| Terminus | Glosse beim ersten Vorkommen |
|---|---|
| Harness | „(das Gerüst, in dem der Agent arbeitet — Werkzeuge, Regeln, Grenzen)" — **Genus siehe §4, WEAK** |
| Hook vs. Skill | „(Hook = deterministischer Eingriff des Harness; Skill = ein Rat, den das Modell ignorieren kann)" |
| Reward Hacking | „(die geprüfte Kennzahl erfüllen, ohne die verlangte Arbeit zu tun)" — **nicht** „Belohnungs-Hacking" |
| Blast Radius | „(Reichweite des Schadens, den ein entgleister Agent anrichten kann)" |
| Least Privilege | „(nur genau die Rechte, die die Aufgabe braucht)" — deutsche Vollform siehe §4, **OPEN** |
| Policy-as-Code | „(Richtlinien als ausführbarer Code)" |
| Quality Gate | „(automatische Prüfung, die den Fortschritt blockiert)" — in deutscher CI/CD-Prosa etabliert |
| Context Rot | „(die Verfallserscheinungen langer Kontexte)" |
| Hot Set / Cold Set | „(immer geladener Kern vs. auf Abruf nachgeladener Rest)" |
| Postmortem | „(schuldfreie Nachbetrachtung eines Vorfalls)" |

---

## §3 German-led (class 3) — this course

| Kanon | Original | Hinweis / Abgelehnt |
|---|---|---|
| der Engpass der Überprüfung; **kurz: der Prüf-Engpass** | verification bottleneck | *Engpass* ist der etablierte deutsche Terminus für *bottleneck*; „Flaschenhals" ist bildlich möglich, aber im Fachtext markiert. **Auf Probe** |
| die Schleife schließt sich in der Produktion | "the loop closes on production" | Satz, kein Einwortterminus |
| die Projekterinnerung / das Projektgedächtnis | project memory | **OPEN — zwei Kandidaten, kein Beleg.** Bis zur Entscheidung: „das dauerhafte Projektwissen" |
| ausführbare Regeln; Regeln als Code | executable rules; rules-as-code | — |
| der Nachweisgrad; die Nachweisleiter | evidence grade / the ladder | Tokens `MEASURED` / `REPORTED` / `ASSERTED` bleiben kept-EN, code-styled, mit einmaliger Glosse „(gemessen / berichtet / behauptet)" |
| die Wahl des Nenners | denominator choice | „% des von KI geschriebenen Codes" hängt vollständig vom Nenner ab |
| technische Schulden **auf Kredit** | tech debt on credit | „technische Schulden" ist der etablierte deutsche Terminus (auch „technische Schuld" Singular) |
| die Selbsteinschätzungslücke | self-assessment gap | **Auf Probe** — alternativ schlicht: „Entwickler können ihre eigene Beschleunigung nicht beurteilen" |
| der beherrschbare Zuschnitt | controllable scope | **Auf Probe** |
| zuerst die Architektur | architecture-first | — |
| die Amnesie | amnesia | im Deutschen unmittelbar dekodierbar |
| die Wissensschichtung | knowledge tiering | **Auf Probe**; „Schichtung des Wissens" als Auflösung |
| die Detailstufen (Karte / Kontrakt / Bauplan) | detail tiers (map / contract / blueprint) | — |
| die drei Reifegrade (Einzelperson · kleines Team · Enterprise) | the three maturity tiers | „Reifegrad" ist im deutschen Prozessvokabular etabliert (CMMI-Rezeption). **Enterprise** bleibt kept-EN |
| die übermäßige Folgsamkeit | over-compliance | **Auf Probe**; „gründlich, aber unnötig" als Auflösung |
| die Trennung der Zuständigkeiten | separation of duties | „Funktionstrennung" ist die in der Wirtschaftsprüfung übliche Form — beide zulässig, **eine Seite entscheidet sich** |
| die Zuständigkeit für Konsistenz | consistency owner | — |
| die Überlastung durch Artefakte | artifact overload | — |
| „Eine Anweisung ist keine Kontrolle." | "An instruction is not a control." | Merksatz. Beachte `_language.md` §9.3 — hier trägt die bloße Kopula, weil beide Größen gleichartig sind |
| „Was Sie prüfen, das bekommen Sie." | "The gate defines the artifact." | Merksatz; **nicht** „Das Gate definiert das Artefakt" (Kalke). Anrede nachgezogen mit dem Sie-Ruling (`_language.md` § Stimme und Anrede, 2026-07-28) — der Merksatz stand zuvor im „du" |

---

## §4 Terms still OPEN — not settled

| Terminus | Warum offen | Vorläufige Behandlung |
|---|---|---|
| **Harness (Genus)** | nur Fachjournalismus belegt, kein Wörterbuch: heise schreibt „den Coding-Harness", „den Harness des eigenen Agenten" → **maskulin, WEAK** | Hausform **der Harness**; bei Zweifel als Kompositum umgehen („das Agentengerüst") |
| **Least Privilege — deutsche Vollform** | drei konkurrierende Familien im deutschen Sicherheitsdeutsch (*geringste Rechte*, *minimale Rechte*, *Need-to-know*); die maßgebliche Quelle (BSI IT-Grundschutz) wurde für diesen Bootstrap **nicht** verifiziert | kept-EN **Least Privilege** + Glosse; deutsche Vollform **nicht** als Terminus setzen, bis BSI/DIN geprüft ist. *(Im Slowakischen ist genau diese Zeile seit Phase 26 DISPUTED — dieselbe Falle, andere Sprache.)* |
| **project memory** | „Projekterinnerung" vs. „Projektgedächtnis" — kein Beleg entscheidet | „das dauerhafte Projektwissen" umschreiben |
| **`gate` — Sense-Card** | drei verschiedene Begriffe unter einem englischen Wort, siehe unten | siehe Sense-Card |
| **`drift` — Sense-Card** | drei verschiedene Begriffe, siehe unten | siehe Sense-Card |
| **Scar archive / „Narbenarchiv"** | geprägte Figur, im Deutschen ungeprüft | **auf Probe**; schlicht: „das Archiv der behobenen Fehlerklassen" |
| **`provenance`** | siehe die Entscheidung direkt unter dieser Tabelle — **„Herkunftsnachweis" ist ein gefangener falscher Freund** | kept-EN **die Provenance** als Terminus; **„Herkunft"** als kurzes Label |
| **Citation laundering** | im Slowakischen und Russischen als Figur **gestrichen** (owner: DROP) | nicht prägen; direkt sagen: „eine verzerrte Behauptung, die so lange weitergereicht wird, bis sie wie eine Quellenangabe aussieht" |
| **Human router / „Mensch als Router"** | im Slowakischen „auf Probe" adoptiert; im Deutschen ungeprüft | **auf Probe**, immer zuerst über *Human-in-the-Loop* einführen |

---

## §4a Entscheidung: `provenance` — und ein gefangener falscher Freund

**Kanon: kept-EN — die Provenance** (§1.0 Klasse 2), Glosse beim ersten Vorkommen „(Herkunft und
Nachweiskette eines Artefakts)". Wo ein **kurzes Label** gebraucht wird, steht schlicht **„Herkunft"**.

> **„Herkunftsnachweis" ✗ — ABGELEHNT, und der Grund gehört ins Protokoll.** Der Tausch war naheliegend,
> grammatisch einwandfrei und wurde ohne Prägung eines neuen Wortes gemacht — trotzdem falsch, weil das Wort
> im Deutschen **bereits besetzt** ist. Duden: „[schriftlicher] Nachweis, aus welchem Gebiet, welchem Land
> eine **Ware, ein Importartikel** stammt" (<https://www.duden.de/rechtschreibung/Herkunftsnachweis>) — ein
> **Ursprungszeugnis aus Handel und Zoll**, im Alltag zusätzlich stark vom Strommarkt besetzt
> (Grünstrom-Herkunftsnachweise). Ein deutscher Leser dekodiert bei „Herkunftsnachweis" ein Zertifikat für
> eine Ware, nicht die Nachweiskette eines Build-Artefakts.
>
> **Das ist exakt die Falle, für die die Terminus-Probezeit existiert** (§ Figuren und Termini auf Probe):
> eine plausible, grammatisch tadellose deutsche Bildung, die **semantisch in eine andere Domäne zeigt** —
> derselbe Fehlertyp wie das slowakische „súbeh" für *race condition*. Keine Glosse rettet ein Wort, dessen
> Wörterbuchbedeutung woanders hingehört.

**Ebenfalls geprüft und nicht genommen:**

- **„Provenienz" bare — ABGELEHNT als Terminus.** Es bedeutet zwar das Richtige, ist aber in beiden
  Wörterbüchern **registermarkiert** — Duden „**bildungssprachlich**", DWDS „**gehoben**"
  (<https://www.dwds.de/wb/Provenienz>) — und die DWDS-Kollokationen sind durchgehend kunsthistorisch/
  archivarisch (*adelig, Echtheit, Restitution, Erhaltungszustand, lückenlos, ungeklärt*). In der Drucklatte
  dieses Korpus (dpunkt/heise) wäre es eine Stilhebung, kein Fachwort.
- **„Datenprovenienz" — OPEN, nicht ratifiziert.** Als Fachkompositum in der Forschungsdaten- und
  Data-Governance-Literatur plausibel, in dieser Sitzung aber **nicht verifiziert** (Suchbudget erschöpft).
  Nicht verwenden, bis ein Beleg vorliegt; **nicht** aus Plausibilität setzen.
- **„Datenherkunft" — VERWORFEN nach MT-Signal-Prüfung.** Der einzige Fundort war lokalisierte
  Microsoft-Learn-Dokumentation; genau die Quellensorte, die § Sprachpaar und Rolle der Locale
  disqualifiziert. *(Diese Disqualifikation stammt von `de-ui-strings` und war richtig.)*

**Sichtbare Fläche — erledigt.** Das in #310 ausgelieferte Label
`Enterprise-Reifegrad: Prüfpfad, Herkunftsnachweis, Vorgaben` trug die abgelehnte Form und lautet seit **#314**
`Enterprise-Reifegrad: Prüfpfad, **Herkunft**, Vorgaben`. `Prüfpfad` (*audit trail*) und `Vorgaben` (*policy*)
waren nicht berührt und bleiben. Im gesamten `i18n/de/**` steht seither **kein** „Herkunftsnachweis" mehr
(ausgezählt).

## §5 Sense card: `gate` (drei verschiedene Begriffe unter einem englischen Wort)

`gate` lässt sich im Deutschen **nicht** mit einem Wort kalkieren. Der Kanoneintrag trägt den **Bedeutungs-
kontext wie ein Thesaurus**; ein Eintrag aus dem RAG-Ledger wird nur übernommen, wenn **der Sinn übereinstimmt**.

- **Sinn A — review gate** — der Revisionsprozess vor dem Merge (Kontext `dotnet/runtime`). → **nicht** „Gate",
  sondern **„die Prüfung bei der Revision" / „die strenge Code-Review vor dem Merge"**. Merksatz zum Fehlschluss:
  **„Das ist das Verdienst der Prüfung, nicht des Agenten."**
- **Sinn B — verification / pipeline gate** — der strukturelle Kontrollpunkt, der den Fortschritt blockiert.
  → **„das Quality Gate"** (kept-EN, in deutscher CI/CD-Prosa etabliert) oder deutsch **„der Kontrollpunkt"**.
  Nacktes „das Gate" **nicht** verwenden (`_language.md` §1.1, OPEN).
- **Sinn C — requirements sign-off / stage-gate** — die menschliche Freigabe der Anforderungen vor teurer
  Umsetzung. → **„die Freigabe der Anforderungen"** oder kept-EN **„Stage-Gate"**; nicht „Gate".

---

## §6 Sense card: `drift` (drei verschiedene Begriffe)

Owner-Ruling aus dem slowakischen Ledger, sinngemäß übernommen (nicht wörtlich übersetzt), damit der
Schreibende **nach der Bedeutung** wählt, nicht nach dem Wort:

- **„der Kontext-Drift"** — *context drift*: das Fenster bzw. die Historie driftet.
- **„der Regel-Drift"** — die Regeln bleiben **dieselben**, aber ihre **Auslegung** driftet durch Context Rot.
- **„das Veralten der Regeln"** — die Regeln sind **überholt** und müssen wegen neuer Fakten oder Verfahren
  **geändert** werden.
- Ein **vierter**, RAG-eigener Sinn (*drift* von Eingaben/Korpus/Modell) steht in `canon/de/rag.md` und wird
  nicht mit den dreien vermischt.

Verwendung: „Regelfäule durch Context Rot" → **Regel-Drift**. „Regeln müssen für neue Fakten aktualisiert
werden" → **Veralten der Regeln**.

---

## §7 Repeated exact strings

Empty at bootstrap. Settled the first time a German page needs them, then recorded here verbatim.
