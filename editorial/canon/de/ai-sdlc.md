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
| Harness | „(das Gerüst, in dem der Agent arbeitet – Werkzeuge, Regeln, Grenzen)" — **Genus siehe §4, WEAK** |
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
| ~~die Trennung der Zuständigkeiten~~ → **die Funktionstrennung** | separation of duties | **ABGELÖST 2026-07-28.** Diese Zeile ließ „eine Seite sich entscheiden" — genau das Wackeln, das der Kanon verhindern soll. Die Belege entscheiden es jetzt korpusweit: **BSI ORP.4.A4** trägt *Funktionstrennung* im Anforderungstitel, das de.wikipedia-Lemma glossiert **beide** englischen Varianten darunter, und es ist zugleich der Terminus der Wirtschaftsprüfung. **„Trennung der Zuständigkeiten" ist nicht etabliert** und wird nicht mehr verwendet. Siehe die Tabelle unten |
| die Zuständigkeit für Konsistenz | consistency owner | — |
| die Überlastung durch Artefakte | artifact overload | — |
| „Eine Anweisung ist keine Kontrolle." | "An instruction is not a control." | Merksatz. Beachte `_language.md` §9.3 — hier trägt die bloße Kopula, weil beide Größen gleichartig sind |
| „Was Sie prüfen, das bekommen Sie." | "The gate defines the artifact." | Merksatz; **nicht** „Das Gate definiert das Artefakt" (Kalke). Anrede nachgezogen mit dem Sie-Ruling (`_language.md` § Stimme und Anrede, 2026-07-28) — der Merksatz stand zuvor im „du" |

**Neu aufgenommen im Belegdurchgang 2026-07-28 — deutsch geführt, jede Zeile auf Stufe 1 oder 2 belegt.**
Dieser Kurs ist genau der, in dem der Reflex „Deutsch behält das Englische" am häufigsten scheitert: das
Sicherheits- und Governance-Vokabular ist im Deutschen **normativ gesetzt**, und die BSI stellt das
Englische konsequent in die Klammer.

| Kanon | Original | Beleg / Hinweis |
|---|---|---|
| **das Prinzip der geringsten Berechtigungen** / **der minimalen Rechte** | least privilege | **BSI**, siehe §4. Registerabhängige Hausaufteilung; **keine dritte Form** |
| **das Erforderlichkeitsprinzip** | need-to-know | **BSI** ORP.4.A2, wörtlich |
| **die Funktionstrennung** | separation of duties / segregation of duties | **BSI** ORP.4.A4 („Aufgabenverteilung und **Funktionstrennung**"); de.wikipedia-Lemma glossiert **beide** englischen Varianten; zugleich der Terminus der Wirtschaftsprüfung (IDW). *Aufgabentrennung* und *Trennung der Zuständigkeiten* sind **nicht etabliert** — die frühere §3-Zeile „die Trennung der Zuständigkeiten" wird damit **abgelöst** |
| **das Geheimnis / die Geheimnisse** | secret (Zugangsdatum) | **BSI**-Baustein *Secrets Management*: „Bei den zu verwaltenden **Geheimnissen** handelt es sich zum Beispiel um vertrauliche Umgebungsvariablen, Datenbankanmeldeinformationen, API-Schlüssel …". **Zählung im Baustein: Geheimnis 5×, Zugangsdaten 0×, Anmeldedaten 0×, Credential 0×.** „das Secret" mit deutschem Artikel: **null Attestierung auf Stufe 1**. Kept-EN nur im festen Terminus **Secrets Management** |
| **das Betriebshandbuch (BHB)** | runbook | **BSI** OPS.1.1.1 mit eigener amtlicher Abkürzung; **Volltextzählung: Betriebshandbuch 4×, Runbook 0×** |
| ⚠ **NICHT hier — `provenance` ist kept-EN „die Provenance"** | provenance | **Diese Zeile stand kurzzeitig als „der Herkunftsnachweis" und war falsch.** Entschieden in **§4a**: kept-EN **die Provenance** + Glosse, Kurzlabel **„Herkunft"**; *Herkunftsnachweis* **abgelehnt**. §4a trägt auch die Belege des Termledger-Durchgangs |
| **das Audit** | audit | ⚠ **nicht *Prüfpfad*** — § 14 UStG-Terminus. Entschieden in **§4b** (BSI DER.3.1: Audit 140×, Prüfpfad 0×) |
| **die Protokollierung / das Protokoll** | audit trail | ⚠ **niemals *Prüfpfad***: das ist ein Terminus aus § 14 Abs. 1 **UStG** („ein verlässlicher **Prüfpfad zwischen Rechnung und Leistung**") und bezeichnet die Verbindung zwischen Rechnung und erbrachter Leistung. Ein Kanon, der *audit trail* so wiedergibt, importiert Steuerrecht in ein Observability-Kapitel |
| **die statische Code-Analyse**; **linten** | static analysis; to lint | de.wikipedia: „In Anlehnung an das klassische Programm *Lint* wird der Vorgang auch als **linten** bezeichnet"; das Substantiv *Linter* bleibt OPEN (§4) |
| **die Testabdeckung** | test coverage / code coverage | de.wikipedia-Lemma, das *Codeabdeckung* gleichwertig verwendet. *die Code Coverage* (feminin, heise) im laufenden Fachtext zulässig |
| **das Fehlerbudget** | error budget | Computerwoche und iX schreiben **ausschließlich** deutsch |
| **die Instrumentierung** | instrumentation | der Loan lebt im Deutschen nur noch in API-Eigennamen (*Instrumentation API*) |
| **das Code-Review** (Hausform; *der* zulässig, **„die" ✗**) | code review | de.wikipedia-Lemma *Review (Softwaretest)*: „**Der oder das Review** ist eine statische Testmethode" — die Quelle lizenziert *der* und *das* und **schließt *die* aus**. *Quelltextprüfung* / *Codeprüfung*: nicht etabliert |
| **technische Schulden** (Plural) | technical debt | de.wikipedia-Lemma nennt den **Plural zuerst**; Genitiv Plural nativ belegt („statt **technischer Schulden**", heise) |
| **der Mutationstest** | mutation testing | ⚠ die attestierte Schreibung ist **Mutationen-Test** (de.wikipedia, *Dynamisches Software-Testverfahren*); *Mutationstest* ist die glattere Hausform, **regelhaft, nicht belegt** |

---

## §4 Nicht entschieden — OPEN und DISPUTED

**Zwei verschiedene Zustände, und die Unterscheidung ist ab 2026-07-28 scharf:** **OPEN** heißt *kein
brauchbarer Beleg gefunden* — jede Zeile nennt deshalb, **welcher Beleg sie schließen würde**. **DISPUTED**
heißt *die deutschen Quellen widersprechen einander* — dort wird der Incumbent **benannt und gehalten**, und
nichts geändert. Geschlossene Zeilen bleiben **durchgestrichen** stehen, damit die Umkehrung lesbar ist.

| Terminus | Warum offen | Vorläufige Behandlung |
|---|---|---|
| **Harness (Genus)** | **JETZT DISPUTED, nicht mehr bloß WEAK (2026-07-28) — und der Widerspruch sitzt IM Beleg.** Die heise-Belege sind nachgeprüft und stehen wörtlich da („für **den** Coding-Harness … als auch für **den** Harness des eigenen Agenten"). **Derselbe Verlag schreibt im eigenen Erklärstück dreimal Neutrum:** „Dazu braucht es **das Harness**", „… ist **das Harness**", „angetrieben **vom Harness**" <https://www.heise.de/hintergrund/Kurz-erklaert-Agent-Harness-11330445.html>. Zwei frühere Recherchen fanden je **eine** Hälfte und verallgemeinerten | **Incumbent *der Harness* halten**, kein Flip ohne nativen Check → Leserpaket (#278). Bei Zweifel als Kompositum umgehen („das Agentengerüst"). **Nicht verwechseln:** de.wikipedias **Test-Harnisch** / *Testrahmen* ist der **Test**-Harness der QS — ein anderer Referent, kein Konkurrent |
| ~~**Least Privilege — deutsche Vollform**~~ | **GESCHLOSSEN 2026-07-28 — German-led SETTLED auf Stufe 1; DISPUTED nur noch, WELCHE deutsche Form.** Die BSI wurde jetzt geprüft. **IT-Grundschutz-Kompendium ORP.4.A2 (Edition 2023):** „(**Prinzip der geringsten Berechtigungen**, englisch Least Privileges und **Erforderlichkeitsprinzip**, englisch Need-to-know)". **BSI-Positionspapier Zero Trust (04.07.2023):** „… im Kern auf dem **Prinzip der minimalen Rechte** (engl. „Least Privileges") … basiert". **Beide Dokumente führen den Begriff IMMER mit deutscher Vollform ein und stellen das Englische in die Klammer** — die Richtung ist entschieden. Welche Vollform, entscheidet die BSI nicht: sie widerspricht sich zwischen den eigenen Dokumenten | **Hausaufteilung nach Registerlage:** *Prinzip der geringsten Berechtigungen* im Berechtigungs-/Compliance-Text (normative Kompendiumsformulierung), *Prinzip der minimalen Rechte* im Architektur-/Zero-Trust-Text. **Keine dritte Form erfinden.** Kept-EN *Least Privilege* bleibt als Klammerglosse zulässig. **Nebenfund:** *need-to-know* = **Erforderlichkeitsprinzip** (BSI) |
| **project memory** | „Projekterinnerung" vs. „Projektgedächtnis" — kein Beleg entscheidet | „das dauerhafte Projektwissen" umschreiben |
| **Attestation** (signierte Nachweise) | **NEU 2026-07-28 — zero German attestation at any tier** für den in-toto-/Sigstore-Sinn. ⚠ **totale Falle:** DWDS *Attest* hat als **einzige** Bedeutung „ärztliche Bescheinigung"; *Attestierung* existiert als Stichwort **ohne Definition** | kept-EN **Attestation**, **niemals *Attest***. *Was es schließen würde:* ein dpunkt-/Rheinwerk-Titel zu Supply-Chain-Security oder ein c't-/iX-Beitrag mit *Attestierung* auf einem signierten Metadatenobjekt |
| **Release Gate** | **NEU 2026-07-28.** *Quality Gate* und *Stage-Gate* sind belegt (§3), **Release Gate ist es nicht** | *das Freigabe-Gate* **nicht** prägen; umschreiben („die Freigabe vor dem Release") oder kept-EN mit Glosse |
| **Linter** (das Agensnomen) | **NEU 2026-07-28.** Das **Verb** *linten* ist de.wikipedia-belegt („hat sich das Verb **linten** … etabliert"), das **Substantiv** hat keinen Genusbeleg | **die statische Code-Analyse** für den Begriff, **linten** für das Verb; *Linter* artikelfrei oder als Werkzeugname |
| **Postmortem (Artikel)** | **NEU 2026-07-28.** heise verwendet es durchgängig **artikellos** und in Komposita (*Post-Mortem-Kultur*, *Blameless-Post-Mortem-Protokoll*); **kein geprüfter Text hängt einen Artikel daran** | Hausform **das Post-Mortem** ist **Analogie** (*das Protokoll*, *das Review*), **kein Beleg** — das steht hier ausdrücklich. Wo möglich umformulieren |
| **Sandboxing** (als Substantiv) | **NEU 2026-07-28.** *die Sandbox* ist DWDS-settled — **„Sandboxing" kommt im de.wikipedia-Sandbox-Artikel gar nicht vor**; deutsche Prosa verwendet Verben (*isolieren*, *abschirmen*) | **„in einer Sandbox ausführen" / „abschotten"**, nicht „das Sandboxing" |
| **Blast Radius** | **NEU 2026-07-28 — keine Attestierung auf den Stufen 1–5.** ⚠ **Namenskollision:** die deutsche Sicherheitspresse verwendet „Blast-RADIUS" massiv für eine RADIUS-Protokollschwachstelle. Der einzige deutsche Renderer ist *Explosionsradius* auf einem Herstellerblog → **disqualifiziert** | kept-EN mit Glosse, oder **die Schadensreichweite** |
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

> **Unabhängige Bestätigung + drei Belege nach (Termledger-Durchgang #275/#276, 2026-07-28).** Dieser
> Durchgang hatte `provenance` parallel und **ohne Kenntnis von #313** attestiert und kam zum **gleichen
> Ergebnis**: *Herkunftsnachweis* raus, Kurzlabel *Herkunft*. Die Entscheidung oben bleibt; hier stehen nur
> die Belege, die sie noch nicht führte:
>
> 1. **Das DWDS-Kollokationsprofil, das die Dominanz misst statt sie zu behaupten:** *Ausfuhrgenehmigung,
>    Fleisch, Lebensmittel, Rindfleisch, **Strom**, **Ökostrom**, fälschungssicher, lückenlos*
>    (<https://www.dwds.de/wb/Herkunftsnachweis>). **Null Software.**
> 2. **de.wikipedia führt `Herkunftsnachweis` als BEGRIFFSKLÄRUNGSSEITE** mit drei Bedeutungen —
>    Ursprungszeugnis, Warenverkehrsbescheinigung, Energiewirtschaft — und **keinem** IT-Sinn.
> 3. **Der stärkste Einwand kommt aus der IT selbst, und er fehlte bisher:** der deutsche **elektronische
>    Rechtsverkehr** besetzt genau dieses Kompositum bereits — **VHN, „vertrauenswürdiger
>    Herkunftsnachweis"**, der Nachweis, dass eine Nachricht aus einem bestimmten Postfach stammt. Ein
>    deutscher Enterprise-Leser hat für das Wort also **schon einen IT-Referenten — einen anderen**.
>
> **Eine Präzisierung zur Einordnung, die die Entscheidung nicht ändert.** Die Überschrift nennt es einen
> „gefangenen falschen Freund"; genauer ist es **keine Falle vom Typ `Log`/`Gate`/`Queue`**. Dort ist der
> Wörterbuchsinn ein **anderer Begriff** (Schiffslog, Flughafen-Gate, Billardstock). Hier ist der Wortsinn
> **richtig** — dokumentarischer Herkunftsnachweis — und das Kompositum sauber gebildet; falsch ist nur, dass
> drei institutionalisierte Domänen den Ausdruck besetzen. Das ist eine **Dominanzfalle**. Der Unterschied
> ist praktisch: gegen eine Dominanzfalle hilft **disambiguierender Kontext**, gegen einen falschen Sinn
> hilft gar nichts. **Für ein nacktes Label — den Fall, um den es ging — bleibt das Urteil identisch.**
>
> **Und ein Befund zur Rollenverteilung, den eine Registerzeile nicht fassen kann:** deutsche
> Lieferkettenprosa verteilt **einen** Begriff auf **drei** Rollen. **Als SLSA-Kategoriename bleibt der Loan
> englisch** — heise: „Informationen über den **Ursprung (Provenance)** des Codes", „die Kategorien Source,
> Build und **Provenance**". **Im Kompositum steht die lateinische Form** — „SLSA-Provenienz",
> „Provenienz-Nachweise", „die Provenienz von Builds". **Frei und in Überschriften steht das deutsche
> Wort** — Schlagzeile eines deutschen Sicherheitsmagazins: „Software-Lieferkette: **Herkunft** ohne
> Sicherheitsgarantie". **Das stützt die Entscheidung oben genau: kept-EN als Terminus, „Herkunft" als
> Label.** Es erklärt zugleich, warum *Provenienz* als **Terminus** abgelehnt und im **Kompositum** trotzdem
> belegt ist — kein Widerspruch, sondern zwei Rollen.
>
> **Ein Nullbefund, der ausdrücklich NICHTS beweist — und die Lehre daraus.** **BSI TR-03183-2**
> (Cyber-Resilienz, Teil 2: SBOM) ist die naheliegende Stufe-1-Quelle und wurde volltextgegreppt:
> *Provenienz* 0, *Provenance* 0, *Herkunft* 0, *Herkunftsnachweis* 0, *Nachvollziehbarkeit* 0, *Ursprung* 0,
> *SLSA* 0, *in-toto* 0, *Sigstore* 0 — nur *Lieferkette* 2×. **Das ist KEIN Beleg gegen irgendeine Form:
> die englische Fassung derselben Richtlinie hat `provenance` ebenfalls 0×.** Das Dokument behandelt den
> Begriff schlicht nicht. **Regel daraus, allgemein: bevor ein Nullbefund als Evidenz zählt, wird die
> Quelle in der AUSGANGSSPRACHE gegengegreppt** — sonst wird aus „das Dokument sagt dazu nichts" ein
> erfundenes „das Dokument lehnt es ab".

**Sichtbare Fläche — erledigt.** Das in #310 ausgelieferte Label
`Enterprise-Reifegrad: Prüfpfad, Herkunftsnachweis, Vorgaben` trug die abgelehnte Form und lautet seit **#314**
`Enterprise-Reifegrad: Prüfpfad, **Herkunft**, Vorgaben`. `Prüfpfad` (*audit trail*) und `Vorgaben` (*policy*)
waren nicht berührt und bleiben. Im gesamten `i18n/de/**` steht seither **kein** „Herkunftsnachweis" mehr
(ausgezählt).

---

## §4b Entscheidung: `audit` → **das Audit**. Und `Prüfpfad` muss raus — es ist Steuerrecht

> **Verhältnis zu §4a, ausdrücklich, damit hier nichts stillschweigend überschrieben wird.** §4a stellt fest,
> `Prüfpfad` sei „nicht berührt" gewesen und bleibe. **Das war keine Entscheidung über den Terminus, sondern
> eine Feststellung über den Umfang jenes Durchgangs** — geprüft wurde `provenance`, nicht `audit`. Dieser
> Abschnitt prüft ihn erstmals, und er kommt zu einem anderen Ergebnis. **Der Beleg dafür ist Stufe 1 und
> wurde direkt am Gesetzestext nachgeschlagen, nicht aus einem Rechercheprotokoll übernommen.**

**Kanon: `audit` → das Audit** (kept-EN, §1.0 Klasse 2), Plural *die Audits*, Genitiv *des Audits*.

**`Prüfpfad` ✗ — ABGELEHNT, und zwar nicht als Stilfrage.** Es ist ein **umsatzsteuerrechtlicher Terminus**.
§ 14 Abs. 1 UStG, wörtlich: „Dies kann durch jegliche innerbetriebliche Kontrollverfahren erreicht werden,
die einen **verlässlichen Prüfpfad zwischen Rechnung und Leistung** schaffen können."
(<https://www.gesetze-im-internet.de/ustg_1980/__14.html>) Er bezeichnet die belegbare Verbindung zwischen
**Rechnung und erbrachter Leistung** — nicht ein manipulationssicheres Ereignisprotokoll. **Ein Kanon, der
*audit* so wiedergibt, importiert Steuerrecht in ein Governance-Kapitel.**

Und das Wort hat kaum lexikalischen Stand: **Duden 404**, kein Eintrag; **DWDS**: „Ihre Anfrage Prüfpfad ist
nicht in unseren gegenwartssprachlichen lexikalischen Quellen vorhanden" — die dort angezeigte Flexion ist
ausdrücklich als **(computergeneriert)** markiert. Im BSI-Baustein zu Audits kommt es **0×** vor.

**Der Ersatz ist Stufe 1 und wird von der BSI selbst geführt.** IT-Grundschutz-Baustein **DER.3.1 „Audits und
Revisionen"**: „**Audits und Revisionen** sind grundlegend für jedes erfolgreiche Managementsystem für
Informationssicherheit (ISMS)." Flexion direkt aus dem BSI-Fließtext: „Vorbereitung **eines Audits** oder
einer Revision"; „Bei **einem Audit** MUSS das Auditteam prüfen …"; „Es SOLLTE eine Person benannt werden,
die **das Audit** oder die Revision leitet."
**Termzählung im Baustein: Audit 140×, Revision 70×, Prüfung 27× — Prüfpfad 0×, Nachvollziehbarkeit 0×,
Protokollierung 0×.**
**Duden** stützt das Genus: „das, auch: der Audit; Genitiv: des Audits, Plural: die Audits", Gebrauch
*Wirtschaft*, „[unverhofft durchgeführte] Überprüfung, Revision"; **DWDS nennt das Neutrum zuerst**.
→ **Hausform: das Audit**, korpusweit gehalten (Duden lizenziert beide Genera; der Kanon wählt).

**Was das kostet, benannt.** Das nackte *Audit* bezeichnet die **Prüfung**, nicht den aufbewahrten **Pfad**.
Dieselbe Unschärfe trägt aber das englische Label `audit` genauso — und die registergerechten deutschen
Wörter für die Spur (*Protokollierung*, *Revisionssicherheit*) sind für ein Sidebar-Label weder kurz noch
neutral genug. Für den **Audit Trail** als Artefakt bleibt es bei **die Protokollierung / das Protokoll**
(§3).

> **Sichtbare Fläche — NICHT erledigt, und das ist der Punkt.** Das Label lautet nach #314
> `Enterprise-Reifegrad: **Prüfpfad**, Herkunft, Vorgaben`. Empfohlen:
> **`Enterprise-Reifegrad: Audit, Herkunft, Vorgaben`** — gleiche Länge, kein Wachstum des Labels.
> **Der Termledger-Durchgang hat `i18n/**` nicht angefasst** (sein Diff liegt vollständig in `editorial/`);
> die Umstellung gehört zur String-Pflege und ist gemeldet.
> **Zusatzbedingung für die Neufassung:** die englische Seite baut auf einem Gegensatz auf — „**Audit**
> records the act; **provenance** records the lineage of the thing produced" —, den das Label erhalten muss.
> *Prüfpfad* zerstört ihn doppelt: es bezeichnet weder den Vorgang noch die Abstammung.

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

## §7 Wiederkehrende Blockstrings

**Die korpusweiten Blockstrings (`## Das Wichtigste`, `:::note[Als Nächstes: Teil 2 der Lektion]`,
`:::tip[▶ Video]`, `(Das Video ist auf Englisch.)`, `:::note[Bearbeitungsstand]`,
`:::note[Voraussetzungen]`, `:::info[So lesen Sie diese Seite]`, `Siehe auch: …`, das Titelsuffix
` – Vertiefung`, die Teiltitel `Teil I – …`) sind in `canon/de/rag.md` §5 mit Begründung und Status
entschieden und gelten UNVERÄNDERT auch hier.** Das ist ein zulässiger gezielter Nachschlag
(peek-don't-load, siehe Kopf dieser Datei): die Strings sind kursübergreifend identisch, der Sinn stimmt
überein, sie werden **wörtlich wiederverwendet und zitiert**, nicht neu geprägt.

**Nur dieser Kurs hat zusätzlich:**

| EN (Quelle) | Vorkommen | **Deutsch — verbindlich** | Begründung / Status |
|---|---|---|---|
| `:::note[Field note]` | 4 (nur hier) | **`:::note[Aus der Praxis]`** | kennzeichnet Herkunft und Erfahrungscharakter natürlicher als das wenig etablierte Kompositum „Praxisnotiz". **HOUSE** |
| Teiltitel `Part I — The Foundation` … `Part V — Scale & Governance` | 5 | **`Teil I – Das Fundament`**, **`Teil II – Die Schleife`**, **`Teil III – Überprüfung`**, **`Teil IV – Die Plattform`**, **`Teil V – Skalierung und Governance`** | *Teil* statt *Part*; **„und" statt „&"**; **Halbgeviertstrich mit Leerzeichen**, nicht der Geviertstrich der englischen Seite (`_language.md` § Typografie). „Die Schleife" ist zugleich der Kursterminus für *the loop* (§8.5). **HOUSE** |

> **Merksätze werden zu Blockstrings, sobald sie zweimal vorkommen.** Dieser Kurs arbeitet mit kurzen
> apodiktischen Merksätzen („Eine Anweisung ist keine Kontrolle.", „Was Sie prüfen, das bekommen Sie."). Sie
> stehen in §3 und werden **wörtlich** wiederverwendet — nicht jedes Mal neu formuliert. Siehe §8.4 für den
> Test, mit dem ein neuer Merksatz gebaut wird.

---

## §8 Konstruktionen — wiederkehrende Satz- und Überschriftenformen dieses Kurses

> **Bedingungen, keine Ersetzungstabelle.** Jeder Eintrag nennt die englische Form, die deutschen
> **Rahmen**, **den Test, der zwischen ihnen entscheidet**, und je ein durchgearbeitetes Beispiel.
> Liest sich ein Eintrag wie eine Nachschlagetabelle, ist er schlecht und wird über seine Bedingung neu
> geschrieben.
>
> `_language.md` §9 hält die kursunabhängigen Konstruktionen. **`canon/de/rag.md` §6 hält `X vs Y`, den
> Doppelpunkt-Untertitel, `What X actually is`, die Zählüberschrift mit Ortsangabe und den
> Ergänzungsstrich** — diese Formen kommen in **beiden** Kursen vor und sind **dort** entschieden
> (peek-don't-load). Hier stehen nur die Formen, die dieser Kurs allein trägt.

### 8.1 `X over Y` — die Priorisierungsaussage

Nur dieser Kurs hat sie: *Preparation over model*, *Architecture-first with a loop*.
Es ist **keine** Gegenüberstellung (dafür `rag.md` §6.1), sondern eine **Rangbehauptung** — und das Deutsche
muss den Rang **ausdrücklich machen**, weil es die englische Präposition *over* in dieser elliptischen
Rangform **nicht produktiv verwendet**.

- **Rahmen A — vollständige These: „X ist wichtiger als Y".** Test: soll die Überschrift eine begründbare
  Behauptung formulieren statt eines Schlagworts? → *Preparation over model* → „**Vorbereitung ist wichtiger
  als die Modellwahl**". *(Der semantische Kopf muss präzisiert werden: gemeint ist nicht „das Modell" als
  Gegenstand, sondern seine Wahl bzw. seine weitere Optimierung.)*
- **Rahmen B — nominaler Prioritätsrahmen: „Vorrang für X".** Test: ist Y aus dem Kapitelkontext bereits
  eindeutig und kann ohne Informationsverlust entfallen? → „**Vorrang für die Vorbereitung**".
- **Rahmen C — Ersetzung: „X statt Y".** Test: soll Y tatsächlich **zurückgedrängt** werden? →
  „Vorbereitung statt weiterer Modelloptimierung".

> **✗ „Vorbereitung über Modell" — der stärkste Übersetzungsverräter dieses Kurses.** Er übernimmt *over*
> als Rangoperator; das Deutsche kennt *über* räumlich, thematisch und in festen Fügungen, aber nicht in
> dieser elliptischen englischen Prioritätsform. **STATUS: HOUSE** — Registerurteil des unabhängigen
> Cross-Model-Gates, kein Wörterbucheintrag entscheidet es. Der Grund ist trotzdem prüfbar: die Form bildet
> sich 1:1 auf den englischen Satz zurück (das §1.4-Kriterium).

### 8.2 `Rules that hold` — der englische Relativsatz als Überschrift

- **Rahmen A — restriktiver Relativsatz: „Regeln, die Bestand haben".** Test: wird aus einer größeren Menge
  gerade die **Teilmenge** bezeichnet, die sich dauerhaft bewährt? → A.
- **Rahmen B — nominale Verdichtung: „Beständige Regeln" / „Tragfähige Regeln".** Test: ist die gemeinte
  Eigenschaft **eindeutig** und ohne Verlust in einem Adjektiv ausdrückbar? Zeitliche Dauer → *beständig*;
  praktische Belastbarkeit → *tragfähig*.
- **Wahl ohne weiteren Kontext: „Regeln, die Bestand haben".** Englisches *hold* kann *gelten*, *zutreffen*,
  *Bestand haben* oder *sich bewähren* heißen; der Relativsatz lässt das Geltungskriterium ergänzen.
- **✗ „Regeln, die halten"** — mechanische Übertragung der Polysemie von *hold*. Deutsches *halten* verlangt
  in dieser Bedeutung eine andere Konstruktion („das Argument **hält** der Prüfung **stand**").
  **Zweiter der drei benannten Übersetzungsverräter.**

### 8.3 `From X to Y` — der Entwicklungspfad

*From vision to verifiable stages.*

- **„Von X zu Y"** — wenn X und Y **Anfangs- und Endpunkt einer konzeptionellen Entwicklung** sind:
  „**Von der Vision zu überprüfbaren Etappen**".
- **„X in Y überführen"** — wenn das Kapitel erklärt, wie die lesende Person den Ausgangszustand **aktiv
  transformiert**; dann greift der Sie-Imperativ: „Überführen Sie die Vision in überprüfbare Etappen."
- **„Der Weg von X zu Y"** — wenn der ganze Übergangsprozess systematisch beschrieben wird.
- **Wortwahl:** *Etappen* hebt den gegliederten Weg hervor; *Stufen* legt eine feste Hierarchie oder
  Reifeabfolge nahe und bleibt deshalb den **Reifegraden** vorbehalten (§3). **✗ „verifizierbare Stufen"** —
  grammatisch möglich, aber stark von *verifiable stages* geprägt; je nach Sachverhalt „überprüfbare
  Etappen", „prüfbare Zwischenergebnisse" oder „nachprüfbare Prozessschritte".

### 8.4 Der Merksatz (`The gate defines the artifact.`)

Dieser Kurs arbeitet mit **kurzen apodiktischen Merksätzen** als Überschrift und als Kastenzeile. Sie sind
die dichteste Übersetzungsfalle des Kurses, weil ein wörtlich übertragener Merksatz **grammatisch tadellos**
ist und trotzdem englisch klingt.

- **Test 1 — trägt der deutsche Satz dieselbe Behauptung, wenn man ihn ohne den englischen daneben liest?**
  *The gate defines the artifact* → „Das Gate definiert das Artefakt" ✗: nacktes *Gate* ist im Deutschen
  nicht gesetzt (§4, §5), und *definieren* ist hier zu schwach für eine Kausalbehauptung. → „**Was Sie
  prüfen, das bekommen Sie.**" ✓ — dieselbe Kausalität mit deutschen Mitteln.
- **Test 2 — steht ein Inferenzverb, wo das Englische mit einer bloßen Kopula auskommt?** Vergleiche
  `_language.md` §9.3: „Grün ist nicht richtig" ✗ → „**Grün heißt nicht korrekt**" ✓.
- **Test 3 — Anrede.** Ein Merksatz mit Leseranrede steht im **Sie** („Was Sie prüfen …"), nie im
  unpersönlichen „man".
- **Ein Merksatz, der zweimal vorkommt, ist ein Blockstring** → §7, und wird ab dann **wörtlich**
  wiederverwendet.

### 8.5 Aufzählende Prozessüberschriften — `Plan, review, implement, critic`

Das Englische reiht **bloße Verbstämme**. Das Deutsche hat drei Rahmen, und die Wahl ist eine Sachaussage
über die Struktur des Kapitels:

- **Substantivreihe** — wenn die Glieder **Phasen mit Namen** sind: „**Planen, Prüfen, Umsetzen,
  Kritisieren**" (substantivierte Infinitive, alle groß).
- **Zyklusbezeichnung** — wenn der Text die Reihe als **einen** Gegenstand behandelt. Der Kurs nennt sie
  ohnehin *the loop* → „**die Schleife**"; also „die Schleife aus Planen, Prüfen, Umsetzen und Kritisieren".
- **Rollenreihe** — wenn die Glieder **Rollen** und nicht Tätigkeiten sind (das ist hier für *critic* der
  Fall): dann wird die Rolle benannt, nicht die Tätigkeit — „der Kritiker" bzw. kept-EN „der Critic".
- **Test:** *Kann ich vor jedes Glied „die Phase des …" setzen?* Ja → Substantivreihe. Nein, es sind
  handelnde Instanzen → Rollenreihe.

### 8.6 `X-first` (`Architecture-first`, `Plan-first review`)

Englisches `-first` ist ein produktives Suffix; das Deutsche hat **kein** Gegenstück und muss den Rang
ausschreiben — dieselbe Falle wie §8.1.

- **Als Überschrift: „zuerst X"** → „**Zuerst die Architektur**" (so bereits in §3).
- **Attributiv im Satz:** Durchkopplung mit ausgeschriebenem Rang — „ein **architekturzentriertes**
  Vorgehen", „die **vorgeschaltete** Planprüfung". **Nicht** „Architektur-first".
- **✗ „Architektur-zuerst"** als Kompositum: eine Nachbildung der englischen Wortbildung, kein deutsches
  Wort.

---

## §9 Der Glossar-Vertrag — Ankerkennungen, bevor irgendjemand das deutsche Glossar schreibt

**Die Regeln sind identisch mit `canon/de/rag.md` §7 und werden dort begründet** (Backslash-Pflicht wegen
`future.v4: true`, geordnete ID-Gleichheit in `scripts/locale_parity.py`, Übersetzen der Überschrift ohne
Antasten der ID). **Hier stehen nur die Zahlen dieses Kurses.**

Die **22 Anker dieses Kurses, in der verbindlichen Reihenfolge** (`docs-ai-sdlc/glossary.md`, Stand
2026-07-28):

`verification-bottleneck` · `reading-the-evidence` · `preparation-over-model` ·
`project-memory-and-tiering` · `rules-that-hold` · `vision-to-stages` · `atomic-tasks` ·
`artifacts-as-interface` · `plan-review-implement-critic` · `roles-and-the-human` · `layered-gates` ·
`escape-ledger` · `detection-vs-mutation` · `review-at-volume` · `secrets` ·
`least-privilege-and-sandboxing` · `environments-migrations-and-real-data` ·
`observability-rollout-and-the-kill-switch` · `running-agent-fleets-isolation-and-parallelism` ·
`drift-control-and-rule-rot` · `cost-and-the-economics-of-agent-work` ·
`the-enterprise-tier-audit-provenance-and-whats-required`

**Beachte:** mehrere dieser IDs enthalten genau die Konstruktionen, die §8 entscheidet
(`preparation-over-model` → §8.1, `rules-that-hold` → §8.2, `vision-to-stages` → §8.3,
`detection-vs-mutation` → `rag.md` §6.1). **Die deutsche Überschrift folgt §8, die ID bleibt englisch und
unverändert** — das ist kein Widerspruch, sondern der Vertrag.

**Umfang für die Glossarwelle:** 5 818 englische Wörter, **170 fettgesetzte Lemmata**. Jede Lemmaentscheidung
bindet **Lemma UND Fließtext**.

---

## §10 Phasenanhang

**Umkehrungen werden hier lesbar gehalten, nicht überschrieben.**

### Phase 1 (Bootstrap)
Klassenpolitik mit **höherem Klasse-3-Anteil als im RAG-Kurs** (Prozess, Nachweis, Organisation — dort hat
das Deutsche echtes eigenes Vokabular); Startregister; Sense-Cards `gate` und `drift`; §4 mit sieben offenen
Zeilen, darunter **Least Privilege**, ausdrücklich weil die BSI nie geprüft worden war.

### Phase 2 (2026-07-28) — Belegdurchgang, Blockstrings, Konstruktionen, Glossarvertrag
Sechs parallele Belegbatches plus ein Zitatprüf-Durchgang. Ergebnis für diesen Kurs:

- **Least Privilege geschlossen — auf Stufe 1, genau da, wo der Bootstrap gesagt hatte, dass man nachsehen
  muss.** Die Richtung ist **German-led SETTLED**; DISPUTED ist nur noch, **welche** deutsche Vollform,
  und zwar weil die **BSI sich zwischen ihren eigenen zwei Dokumenten widerspricht** (ORP.4.A2: *Prinzip
  der geringsten Berechtigungen*; Zero-Trust-Positionspapier: *Prinzip der minimalen Rechte*). Beide bleiben
  stehen, registerabhängig aufgeteilt. **Nebenfund: *Erforderlichkeitsprinzip* für *need-to-know*.**
- **Fünf weitere Zeilen deutsch geführt entschieden, alle auf Stufe 1:** *Secret* → **das Geheimnis**
  (die im Auftrag geäußerte Vermutung, *Geheimnis* sei „schlecht", ist durch die BSI widerlegt — *Zugangsdaten*
  kommt im maßgeblichen Baustein **null**mal vor), *Separation of Duties* → **die Funktionstrennung**
  (löst die frühere §3-Zeile „die Trennung der Zuständigkeiten" ab), *Runbook* → **das Betriebshandbuch**,
  *SBOM* → **die SBOM** (35 : 0 in der BSI-TR). *(Der Durchgang hatte zusätzlich* Provenance *→ „der
  Herkunftsnachweis" gesetzt — **diese Zeile ist zurückgenommen**: #313 hatte den Terminus parallel
  entschieden (kept-EN **die Provenance**, Kurzlabel **„Herkunft"**), und die eigene Nachrecherche kam
  unabhängig zum selben Ergebnis. Belege nachgetragen in §4a.)*
- **Harness von WEAK auf DISPUTED hochgestuft** — nicht weil ein neuer Beleg fehlt, sondern weil **derselbe
  Verlag sich selbst widerspricht** (*den Harness* gegen *das Harness*). Zwei frühere Durchgänge hatten je
  eine Hälfte gefunden und verallgemeinert; **der Streit lag nie zwischen den Recherchen, sondern in der
  Quelle**. Incumbent gehalten, Zeile geht ins Leserpaket (#278).
- **`audit` erstmals geprüft — und der ausgelieferte String trägt eine Stufe-1-Falle.** #313 hatte
  *Prüfpfad* ausdrücklich „nicht berührt"; das war eine Umfangs-, keine Termentscheidung. Geprüft ergibt
  sich: **das Audit** (BSI DER.3.1, Audit 140× : Prüfpfad 0×; Duden/DWDS Neutrum zuerst), und *Prüfpfad* ist
  ein **umsatzsteuerrechtlicher** Terminus. Das Label lautet nach #314 weiterhin
  „Enterprise-Reifegrad: **Prüfpfad**, Herkunft, Vorgaben" → empfohlen
  „**Enterprise-Reifegrad: Audit, Herkunft, Vorgaben**". Vollständig in **§4b**. **Der
  Termledger-Durchgang hat `i18n/**` nicht angefasst**; die Umstellung ist gemeldet.
- **Eine wörtliche Falle auf Stufe 1 gefunden — die gefährlichste des Durchgangs:** *Prüfpfad* für
  *audit trail* ist ein Terminus aus **§ 14 UStG** und bezeichnet die Verbindung zwischen Rechnung und
  Leistung. Er ist nicht bloß unüblich, er ist **falsch**.
- **Vier neue OPEN-Zeilen ehrlich eröffnet statt gefüllt:** *Attestation* (⚠ *Attest* = ärztliche
  Bescheinigung), *Release Gate*, *Linter*, *Postmortem* (Artikel), *Sandboxing* (als Substantiv),
  *Blast Radius*. Für jede ist notiert, **welcher Beleg sie schließen würde** — bei vier von ihnen ist es
  dieselbe Ebene: **deutsche Fachbücher (dpunkt, Rheinwerk, O'Reilly DE) und die kostenpflichtigen
  iX-/c't-Volltexte**, die kein Durchgang erreichen konnte.
- **§7 (Blockstrings), §8 (Konstruktionen), §9 (Glossarvertrag), §10 (dieser Anhang) angelegt.**
- **Typografie kursweit betroffen:** der Gedankenstrich ist ab jetzt U+2013 **mit** Leerzeichen; die fünf
  Teiltitel dieses Kurses sind in §7 entsprechend festgelegt.
