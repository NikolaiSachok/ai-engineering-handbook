# Language canon (DE) — course-independent language rules

Shared German language rules that hold across every course in this language — voice & register, gendering,
typography, the term-direction policy, the **loanword-interference gate**, the EN→DE calque templates,
verb-by-object, the bridge-direction rule, the bold budget, and the probation rule for coined figures **and
coined terms**. They are **course-independent**: load this file whichever course you are authoring, alongside
that course's term ledger (`rag.md`, `ai-sdlc.md`).

This is the **bootstrap** of the German canon, not a finished canon. It mirrors the *shape* of the Slovak
canon (`canon/sk/_language.md`) and **not** its decisions — German is not Slovak with different endings, and
in the one place where the two languages look most alike (the term-direction policy) they point in **opposite
directions**. Read §1.0 before anything else.

**Honesty grading.** Every ruling below carries one of five English status tokens so the owner — whose German
is ~A1 and who therefore cannot check the German itself — can read the confidence without reading the German:

- **SETTLED** — a top-tier source (Duden, the Amtliches Regelwerk, DWDS, IDS/grammis) states it outright.
- **WEAK** — attested only in professional tech journalism (heise/iX/c't) or a single de.wikipedia headword,
  with no dictionary entry. Usable, but it deserves a second independent source before being defended as a rule.
- **HOUSE** — no external norm decides it; this is a deliberate editorial ruling for corpus consistency. The
  reason is always given.
- **DISPUTED** — sources genuinely conflict, or an external norm conflicts with a project-wide convention.
  The incumbent form is named and **held**; nobody flips a DISPUTED row without new evidence.
- **OPEN** — no usable attestation was found. The form is *not* settled and must not be presented as canon.

A DISPUTED or OPEN row is a correct outcome. A confidently-wrong row is not.

---

## Injektionsblock (wörtlich in jeden Render-Prompt kopieren)

> Diese acht Zeilen gehören **in den Prompt**, nicht nur in den Kanon. Sie betreffen Entscheidungen, die in
> einem Korpus voller Imperative in praktisch jedem Satz wirksam werden; wer sie erst beim Lektorat anwendet,
> repariert 67 Seiten statt sie richtig zu schreiben.

1. **Anrede: „du", klein.** Nie „Sie". Nie Wechsel innerhalb einer Seite.
2. **Kein „man" als Leseransprache.** „Man öffnet die Konsole" ✗ → „Öffne die Konsole." Ausnahme nur für
   echte Allgemeinaussagen über die Sprache oder das Fach (§ Stimme und Anrede).
3. **Englische Fachtermini bleiben englisch** und bekommen einen **deutschen Artikel**: *der Tool-Call, das
   Tool-Result, im Strict Mode, der Idempotency Key*. Deutsche Neuprägungen (*Werkzeugaufruf*, *strikter
   Modus*) sind **nicht** das Ziel (§1.0).
4. **Ein Anglizismus ist hier KEIN Defekt.** Die slowakische Regel „Anglizismus = Fehler" gilt im Deutschen
   ausdrücklich **nicht** (§1.0, Kasten).
5. **Genus, Plural und Genitiv jedes Lehnworts stehen in §1.1.** Innerhalb einer Seite darf kein Wackeln
   auftreten (*der Cache* … *das Cache*) — das ist das lauteste Maschinenübersetzungs-Signal überhaupt.
6. **Durchkopplung:** mehrgliedrige englische Fügungen werden im deutschen Satz durchgekoppelt —
   *Machine-Learning-Modell*, *Prompt-Injection-Angriff*, *Retrieval-Qualität*. „Prompt Injection Angriff" ✗.
7. **Typografie:** „…" primär, ‚…' verschachtelt, **niemals »…«** und niemals «…»; **ß** (bundesdeutsch, kein
   Schweizer ss); Dezimalkomma; Bis-Strich kompress und Prozent eng: **10–20%**.
8. **Drucklatte:** dpunkt, Rheinwerk, O'Reilly Deutschland, heise/iX. **Nicht** Enterprise-Marketing-Deutsch —
   genau das Register, in das ein Modell rutscht, wenn man ihm „professionelles Deutsch" sagt.

---

## Sprachpaar und Rolle der Locale

Deutsch ist eine **präsentationsreife Sekundär-Locale**, die **aus dem englischen Sinn neu geschrieben** wird,
niemals Satz für Satz übersetzt. Die englische Seite ist kanonisch (`docs/`), Russisch und Slowakisch sind
parallele Locales.

**Die entscheidende Einschränkung: der Autor kann das Deutsche nicht korrigieren.** Für das Russische bürgten
„die Gates plus das letzte Auge des Autors"; für das Deutsche bürgen **nur die Gates**. Das hebt die Latte für
die Gates, es senkt sie nie für den Text. Praktisch heißt das: **jede Festlegung braucht im Moment der
Festlegung einen zitierbaren Beleg**, keinen Eindruck — und wo die Belege nicht entscheiden, steht DISPUTED
oder OPEN, nicht eine hübsch klingende Erfindung.

**MT-Signal-Prüfung bei Belegen.** Lokalisierte Herstellerdokumentation (Microsoft Learn de-de, Cloud-Docs
der großen Anbieter) ist **kein** Beleg für nativen Usus, wenn dieselbe Firma sich auf ihren anderen
deutschen Seiten selbst widerspricht. Widerspruch innerhalb eines Anbieters = Maschinenübersetzung →
Beleg verwerfen und das im Kanon vermerken.

**Das deutsche Zusatzproblem ist nicht die Schwestersprache, sondern die Lehnwortschicht.** Slowakisch hat
das Tschechische, das ein Modell einmischt; Deutsch hat nichts Vergleichbares. An seiner Stelle steht die
**Interferenzkontrolle** (§1.3) mit drei Prüfungen in der Reihenfolge ihres erwarteten Ertrags:
Lehnwortgenus und Denglisch-Morphologie (§1.3.1–§1.3.2, im Voraus entscheidbar), englische Satzstellung
(§1.4), und regionale Varianz (§1.3.4 — der nächste strukturelle Verwandte des Bohemismus-Tests: eine Form,
die in einer benachbarten Standardvarietät völlig korrekt und für die gewählte trotzdem falsch ist).

---

## Stimme und Anrede

- **Lektionen stehen im „du", kleingeschrieben** — „behalte im Kopf", „wenn du ausrollst", „du bekommst".
  Nie „Sie", nie Wechsel innerhalb einer Seite. Spiegelt das russische «ты» und das slowakische „ty".

  > **STATUS: DISPUTED — und zwar gegen die Beleglage.** Das muss hier stehen, damit niemand es später für
  > eine belegte Norm hält. **Jede öffentlich lesbare deutsche Fachbuchquelle, die geprüft wurde, verwendet
  > `Sie`:** Rheinwerk-Openbook („Vor dem Lesen sollten **Sie** sich überlegen, welche Fragen das Kapitel
  > beantworten soll", <https://openbook.rheinwerk-verlag.de/javainsel/00_002.html>); zwei dpunkt-Leseproben
  > (76× *Sie/Ihnen* gegen 1× *du*; 35× *Sie* gegen 0× *du*); der GNOME-Übersetzungsleitfaden („Der Anwender
  > wird … **grundsätzlich in der Höflichkeitsform** angesprochen", <https://wiki.gnome.org/de/UebersetzungsRichtlinien>);
  > der Microsoft-Lokalisierungsleitfaden, der `du` ausdrücklich Leserinnen und Lesern **unter 18** vorbehält.
  > Der tekom-Fachartikel bestätigt den `du`-Trend und rät zugleich zur Vorsicht: „Mit dem Sie macht man im
  > Zweifelsfall nichts Grundsätzliches verkehrt … Ein falsch verwendetes Du kann aber durchaus zu Irritationen
  > führen." (<https://technischekommunikation.info/fachartikel/sprache/gerne-per-du-1272/>)
  >
  > **Zusatzbefund, der die Beleglage relativiert:** dpunkt, O'Reilly Deutschland und heise sind **eine**
  > Stilfamilie, nicht drei unabhängige Datenpunkte — dpunkt betreut seit 2015 das deutschsprachige
  > O'Reilly-Programm und gehört zu Heise Medien
  > (<https://www.heise.de/news/dpunkt-verlag-uebernimmt-deutschsprachiges-O-Reilly-Programm-2622415.html>).
  > Eine öffentlich lesbare **Buch**-Autorenrichtlinie mit Anrederegel existiert bei keinem der drei: OPEN.
  >
  > **Incumbent: `du`** — als bewusste Marken- und Korpusentscheidung, gestützt auf (1) den Registerwunsch
  > handlungsorientierter Tutorials und (2) die Gleichlage mit den beiden Schwester-Locales (RU «ты», SK „ty"),
  > die eine Übersetzung sonst schon an der Anrede erkennbar machen würde. **Kein Flip ohne Eigentümerentscheid**
  > — und wer sie verteidigt, verteidigt sie als Entscheidung, nicht als Norm.

- **Das unpersönliche „man" ist im deutschen Doku-Reflex der Default — und im Korpus als Leseransprache
  verboten.** Es ist die dritte Anziehungskraft, die das Russische und das Slowakische gar nicht kennen: Es
  liest sich weder als „du" noch als „Sie", und ein Absatz driftet lautlos hinein und wieder heraus. Diese
  Drift ist der eigentliche Defekt, nicht das Wort.

  **Verboten** ist „man" überall dort, wo **die lesende Person die handelnde ist** — in Anweisungen,
  Empfehlungen, Arbeitsschritten, Warnungen:

  | ✗ „man" | ✓ Neubau | Funktion |
  |---|---|---|
  | Man öffnet die Konsole. | Öffne die Konsole. | konkrete Leserhandlung → Imperativ |
  | Man prüft den Rückgabewert. | Prüfe den Rückgabewert. | Anweisung → Imperativ |
  | Man speichert die Daten im Index. | Die Daten werden im Index gespeichert. | Vorgang, Handelnder unwichtig → Passiv |
  | Man kann drei Fälle unterscheiden. | Es lassen sich drei Fälle unterscheiden. | unpersönliche Möglichkeit |
  | Beim Reranking bewertet man neu. | Beim Reranking werden die Treffer neu bewertet. | echte Prozessbeschreibung |

  **Erlaubt — und nur hier** — ist „man" für **echte Allgemeinaussagen über die Sprache, das Fach oder eine
  Definition**, wo „du" sachlich falsch wäre: „Unter einem Agenten versteht man hier …", „Im Deutschen setzt
  man in diesem Fall einen Bindestrich."

  > **STATUS: HOUSE — ausdrücklich eine Redaktionsregel, KEINE deutsche Norm.** Die Recherche fand **keine
  > einzige** deutsche Quelle, die „man" in Anleitungs- oder Fachprosa untersagt — die englische Intuition,
  > „one" sei schlechter Stil, hat im Deutschen kein Gegenstück. Es gibt sogar das **Gegenteil**: das
  > Arbeitshandbuch „Bürgernahe Verwaltungssprache" des Bundesverwaltungsamts **empfiehlt** „man" als Mittel
  > gegen das Passiv — „Verwenden Sie dazu unbestimmte Subjekte (z. B. **man**, jemand, wer, es)"
  > (<https://www.bva.bund.de/SharedDocs/Downloads/DE/Oeffentlichkeitsarbeit/Buergernahe_Verwaltungssprache_BBB.pdf>);
  > und heise verwendet es unmarkiert („Werte definiert **man** mit def.").
  >
  > Was der Beleglage standhält, ist die **engere** Regel, und genau die gilt hier: **kein „man" für einen
  > Schritt, den die lesende Person ausführen soll** — Handlungsschritte stehen im Imperativ, damit der
  > Handelnde eindeutig ist. Der Rest ist Registerdisziplin: „man" driftet aus der „du"-Ansprache heraus und
  > wieder hinein, und diese Drift liest sich als Maschinenausgabe.
  >
  > Der unabhängige Register-Gegencheck (ein zweites Modell als nativer Registerrichter) lehnte ein
  > ausnahmsloses Verbot mit demselben Grund ab: „du" und „man" sind semantisch nicht
  > austauschbar (Leseransprache vs. generische Referenz); ein Totalverbot erzwingt unidiomatisches Passiv,
  > überladene Substantivierungen oder ein „du", das dem Leser Handlungen unterstellt, die er nicht ausführt.
  > **Die Regel lautet deshalb: „man" ist ein Defekt, außer es lässt sich mit dem Definitionsrahmen
  > begründen** — die Beweislast liegt beim „man", nicht beim „du".

- **Autoren-„wir" nur dosiert** und nur als Rahmen des gemeinsamen Wegs („Schritt für Schritt geben wir dem
  Modell mehr Freiheit") sowie für Vorbehalte zum Umfang des Materials; **nie in Anweisungen an den Leser**.

- **Drucklatte — Register mit benannten Vorbildern.** Ziel ist Prosa, die eine erfahrene deutschsprachige
  Entwicklerin als *von einer Kollegin geschrieben* akzeptiert: das Register von **dpunkt, Rheinwerk,
  O'Reilly Deutschland, heise/iX/c't** — sachlich, dicht, ohne Aufgeregtheit, mit Fachwörtern statt
  Umschreibungen. **Ausdrücklich NICHT: Enterprise-Marketing-Deutsch** („ganzheitliche Lösungen", „nahtlose
  Integration", „zukunftssicher", „Mehrwert schaffen", Nominalstil, Sie-Ansprache mit Werbeduktus). Genau in
  dieses Register rutscht ein Modell, wenn man ihm „professionelles Deutsch" sagt — es ist die deutsche
  Entsprechung zu dem, was der slowakische Kanon als „preložený marketingový text" abweist, nur aus der
  entgegengesetzten Richtung.

- **Registerkontrolle — eine Stimme.** Die Zielstimme ist **direkt, freundlich, technisch präzise**. Vermeide
  scharfe Ausschläge zwischen drei Lagen: salopp-umgangssprachlich, übersetzt-akademisch (Nominalketten,
  „im Rahmen der Durchführung von …") und formal-technisch. Ein saloppes Bild darf einen Akzent setzen, aber
  **die tragende technische Unterscheidung muss immer auch wörtlich gesagt werden**.

---

## Gendern

Deutsch hat hier eine Achse, für die es im Russischen und Slowakischen **kein Gegenstück** gibt: *der
Entwickler* vs. *Entwickler:innen* vs. *Entwicklerinnen und Entwickler*. **Ein neutrales Default existiert
nicht** — jede explizite Strategie wird als Position gelesen. Rollenbezeichnungen kommen in diesem Korpus
ständig vor (*Nutzer, Entwickler, Reviewer, Autor, Angreifer, Betreiber, Prüfer*). Die „du"-Anrede räumt den
größten Teil davon konstruktiv ab; der Rest muss **einmal, bewusst** entschieden werden. Ein unentschiedenes
Korpus wackelt, und deutsche Leser lesen Wackeln als Maschinenausgabe.

**Entscheidung: die Rollenbezeichnung wird weggeschrieben, nicht markiert.** Leiter, in dieser Reihenfolge:

1. **Auf die Tätigkeit oder das Artefakt umstellen** — „beim Review" statt „der Reviewer"; „im Betrieb" statt
   „der Betreiber"; „bei der Abnahme" statt „der Abnehmer".
2. **Neutrale Kollektiva** — „das Team", „die Redaktion", „der Betrieb", „die Anwendung".
3. **Relativsatz mit „wer"** — „wer den Dienst betreibt, …" statt „der Betreiber …".
4. **Doppelnennung, sparsam** — „Entwicklerinnen und Entwickler" **nur dort, wo die Personengruppe selbst
   das Thema ist**, nicht als Standardform.

**Nicht verwendet werden Genderstern, Doppelpunkt und Unterstrich** im Fließtext. **STATUS: SETTLED für die
Markiertheit, HOUSE für die Entscheidung.** Der Rat für deutsche Rechtschreibung hat 2023 einen Abschnitt
„Sonderzeichen" ins Amtliche Regelwerk aufgenommen; er steht dort (S. 153) im Wortlaut:

> „Zunehmend werden bei Personenbezeichnungen orthografische Zeichen wie der Doppelpunkt (:) … oder
> Sonderzeichen wie Asterisk (\*), Unterstrich (\_) oder andere Zeichen im Wortinneren verwendet. **Diese
> Wortbinnenzeichen gehören nicht zum Kernbestand der deutschen Orthografie.**"
> <https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf>

Das Begründungspapier des Rats (Beschluss vom 15.12.2023) nennt den Grund und zugleich die vom Rat selbst
bevorzugten Mittel: „Sonderzeichen innerhalb von Wörtern beeinträchtigen die Verständlichkeit, die Lesbarkeit,
die Vorlesbarkeit und die automatische Übersetzbarkeit …"; empfohlen werden stattdessen Doppelnennung und
„Begriffe ohne geschlechtsspezifische Benennung von Personen wie Lehrpersonen, Fachkräfte, Mitglieder,
Studierende oder auch Passivkonstruktionen … **Solche Formulierungen haben keine Auswirkungen auf die
Orthografie.**"
(<https://www.rechtschreibrat.com/DOX/rfdr_PM_2023-12-20_Geschlechtergerechte_Schreibung_Erlaeuterungs-Begruendungspapier.pdf>)
Wichtig für die Einordnung: das Regelwerk bindet **Schule und öffentliche Verwaltung**, nicht Verlage — es ist
also kein Verbot, sondern ein Markiertheits-Befund.

**Belegter Verlagsusus (uneinheitlich, ehrlich vermerkt):**

- **heise** (und damit dpunkt / O'Reilly DE, siehe *Anrede*): Gendern ist **freigestellt**; wer gendert,
  nimmt **verlagsweit den Doppelpunkt** — „Wir stellen es allen frei … Der Vereinheitlichung halber haben wir
  uns beim Gender Gap auf den Doppelpunkt geeinigt – und zwar verlagsweit."
  (<https://www.heise.de/select/make/2021/3/2034509261939723212>)
- **dpunkt** (Zeitschrift): Autorinnen und Autoren frei; die **genannten Beispiele sind neutrale
  Umformulierungen** („»Mitarbeitende«, »Teilnehmende«, »alle« statt jeder oder jede") — die Redaktionsstimme
  des Dokuments selbst gendert mit Stern (<https://it-governance.dpunkt.de/pdf/Autorenrichtlinien.pdf>).
- **Microsoft** ist vom Genderstern **aktiv weggegangen**: „we have developed strategies to transition away
  from using the gender star symbol (\*) to equally inclusive alternatives … Opt for general terms that omit
  the notion of gender."
- **Beobachtete Buchprosa** (dpunkt-Leseproben): **keine** Gendersonderzeichen.

**Die rollenarme Umformulierung ist die einzige Option, die alle vier unabhängigen Belegstränge zugleich
stützen** — Rechtschreibrat, dpunkt, Microsoft und die beobachtete Buchprosa. Deshalb steht sie in diesem
Kanon oben auf der Leiter.

**Wo die Umformulierung regelmäßig scheitert — diese vier Fälle stehen hier namentlich, damit sie nicht
jede schreibende Instanz neu improvisiert:**

1. **Verantwortung** — „**Der Betreiber** haftet." (Die Rolle *ist* das Subjekt der Aussage.)
2. **Berechtigung** — „Nur **Administratoren** dürfen Schlüssel rotieren."
3. **Rollenkontrast** — „**Autor und Reviewer** müssen verschiedene Personen sein." (Der Kontrast *ist* der
   Inhalt; „beim Review" löscht ihn.)
4. **Definierte Rahmenwerksrollen** — *Product Owner*, *Scrum Master*, *Data Protection Officer*: feste
   Bezeichnungen, die nicht umformuliert werden.

In allen vier Fällen gilt das generische Maskulinum. Für eine **konkrete, benannte Person** gilt deren
tatsächliche Form.

> **Der Restfall.** Wenn die Leiter 1–4 versagt und eine Rollenbezeichnung im Singular stehen *muss*, gilt
> das **generische Maskulinum** als Rückfall — es ist die **sichere, nicht die unsichtbare** Wahl (für einen
> Teil der Leserschaft trägt es inzwischen ein eigenes Signal). Das deckt sich mit dem Auftrag an diesen Kanon
> und liegt **innerhalb** dessen, wovor der Register-Gegencheck gewarnt hat: er riet von einem **systematischen** generischen
> Maskulinum ab, nicht von ihm als Rückfall. Sonderzeichen bleiben in jedem Fall draußen. **Sollte das
> Projekt je gendern wollen, ist der Doppelpunkt die belegte deutsche IT-Konvention** (heise) — dann aber
> korpusweit und einmalig entschieden.

---

## Typografie

- **Deutsche Anführungszeichen „…"** (unten öffnend, oben schließend), verschachtelt ‚…'.
  **STATUS: SETTLED** — so gesetzt im Amtlichen Regelwerk 2024, § 79: „Steht innerhalb einer Anführung eine
  weitere Anführung, steht die weitere Anführung in der Regel in **halben** Anführungszeichen … „Das ist wohl
  ganz unangebracht, ‚Eile mit Weile' von mir zu verlangen.""
  (<https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf>)

- **»…« wird in diesem Korpus nicht verwendet — obwohl es vollwertiges Deutsch ist.**
  **STATUS: HOUSE, und zwar gegen eine ernstzunehmende Gegenevidenz.** Die nach innen zeigenden Guillemets
  sind **gleichrangig normgerecht** (Gallmann, Univ. Jena: „Guillemets, deutsch: »Beispiel«" neben
  „Gänsefüßchen, deutsch: „Beispiel"", <http://gallmann.uni-jena.de/Ortho/V_Anfuehrung_Skript.pdf>), und
  **dpunkt setzt in seinen eigenen Richtlinien durchgehend »…«**. Es wird berichtet, dass Duden Bd. 9 die
  Gänsefüßchen der Hand-/Maschinenschrift und die Guillemets dem **Buchdruck** zuordnet — **WEAK**, nur über
  de.wikipedia belegt, **nicht** als Duden-Zitat verwenden. Ein Verbot des Mischens ist **nirgends belegt**
  (OPEN); „ein System pro Text" ist hier also eine gewählte Konvention.
  **Grund für die Wahl:** Gleichlage mit der slowakischen Locale, die ebenfalls „…" führt — ein Wechsel des
  Anführungssystems zwischen zwei Locales desselben Buches wäre eine sichtbare Inkonsistenz. Genau deshalb
  steht das Verbot **namentlich**: ein Modell wird »…« erzeugen, weil es korrekt ist.
  Ebenfalls draußen: russische «…», englische gerade "…", und die **schweizerischen** «…» (§1.3.4).
  Anführungszeichen stehen **ohne** Leerzeichen am Text (nie französisch « … »).

- **ß, nicht durchgängig ss.** **STATUS: SETTLED**, Amtliches Regelwerk 2024, § 25: „Für das scharfe
  (stimmlose) [s] nach langem Vokal oder Diphthong wird ß geschrieben, wenn im Wortstamm kein weiterer
  Konsonant folgt. — Maß, Straße, groß, außen, beißen, heißen — Ausnahme: aus".
  § 25 E2 nennt die Schweizer Ausnahme ausdrücklich: „In der Schweiz und in Liechtenstein kann **immer** ss
  geschrieben werden: Straße – Strasse." → jedes `Strasse`, `gross`, `heisst`, `Fussnote` ist ein
  **Schweizer Tell** und wird korrigiert (§1.3.4).
  § 25 E3 für Versalien: „Bei Schreibung mit Großbuchstaben ist neben der Verwendung des Großbuchstabens **ẞ**
  auch die Schreibung SS möglich."

- **Dezimalkomma**: 0,5; 0,36; 28,7 — nie „0.5". **STATUS: SETTLED.**

- **Tausendergliederung: schmaler geschützter Zwischenraum**, nicht der Punkt — `10 000`, `1 000 000`; und
  **vierstellige Zahlen werden nicht gegliedert** (`5423`, nicht „5 423").
  **STATUS: DISPUTED.** Norm-Seite: DIN 5008:2020 („Zahlen mit mehr als vier Stellen sollten … durch je ein
  Leerzeichen in dreistellige Gruppen gegliedert werden — 15 976 Messebesucher") und Duden („Ganze Zahlen mit
  5 oder mehr Ziffern werden … durch Zwischenräume in dreistellige Gruppen gegliedert",
  <https://www.duden.de/sprachwissen/rechtschreibregeln/zahlen-und-ziffern>). Praxis-Seite: die de-DE-Locale
  aller Systeme und die verbreitete Fachprosa verwenden den **Punkt** (`120.000`). **Incumbent: Zwischenraum**
  — er kollidiert nicht mit dem englischen Dezimalpunkt, der im Korpus in Code und Zahlenbeispielen vorkommt.
  Ausnahme laut DIN: **Geldbeträge** werden „aus Sicherheitsgründen mit dem Punkt" gegliedert (`51.397,30 €`).

- **Prozentzeichen eng am Zahlwert: 10–20%, 28,7%.**
  **STATUS: DISPUTED — bewusste Abweichung von der deutschen Norm.** Die Norm ist eindeutig und lautet
  **`20 %` mit Zwischenraum**: DIN 5008:2020 „**Vor dem Prozentzeichen wird ein Leerzeichen gesetzt.** Das
  Leerzeichen entfällt bei Ableitungen. — 3 % Skonto — Aber: 14 prozentig"; ebenso typolexikon: „Zwischen
  Zahl und Prozentzeichen wird **immer** ein Leerraumzeichen gesetzt". Die enge Schreibung ist ein Import aus
  der englischen Typografie.
  Dagegen steht die **projektweite Konvention**: EN, RU und SK schreiben im gesamten Korpus eng (`20%`), und
  die slowakische Locale hat 2026-07 ausdrücklich von „geschütztes Leerzeichen" auf „eng" umgestellt, weil die
  alte Regel dem eigenen Korpus widersprach. **Incumbent: eng** — Korpuskonsistenz schlägt hier die
  Einzelsprachnorm, weil dieselbe Zahl auf vier Sprachseiten identisch aussehen soll.
  **Dieser Konflikt ist der auffälligste bewusste Normbruch des deutschen Kanons.** Er steht hier, damit ihn
  niemand für ein Versehen hält; ein Flip auf `20 %` ist eine Eigentümerentscheidung und müsste **korpusweit**
  erfolgen. Unabhängig davon gilt die Ableitungsregel: `20%ig`, `die 5-%-Klausel`.

- **Bereiche mit Bis-Strich (Halbgeviert, en dash), ohne Leerzeichen**: `10–20%`.
  **STATUS: DISPUTED, mit begründetem Incumbent.** Der **normative Teil** von DIN 5008 setzt Leerzeichen
  („Montag – Donnerstag"); der **klassische Buchsatz und DIN 5008 Anhang F** (der Anhang für typografisch
  gehobene Publikationen) setzen kompress. Die Gesellschaft für deutsche Sprache bestätigt beides: „Der
  Bis-Strich **darf auch kompress gesetzt werden**, also ohne Leerzeichen" (<https://gfds.de/strichlaengen/>).
  **Incumbent: kompress** — ein Buch ist genau der Fall, für den Anhang F geschrieben wurde, und es ist die
  Form der übrigen Locales.
  **Harte Unterregel, nicht optional:** Wort und Strich werden nie gemischt — „von 8 bis 20 Uhr" ✓,
  „von 8–20 Uhr" ✗.

- **Geschütztes Leerzeichen zwischen Zahl und Einheit** (128 GB, 8 GPU, 24 h), damit der Wert nicht am
  Zeilenende abreißt. **STATUS: SETTLED** für das Leerzeichen („Einheiten werden **immer** mit einem
  Leerzeichen zwischen dem Zahlenwert und der Einheit geschrieben"), WEAK für die Art des Leerzeichens.
  Innerhalb einer abgekürzten Einheit steht **nie** ein Leerzeichen. Sonderfälle: **Temperatur** `8 °C`
  (Zwischenraum, dann Gradzeichen direkt an der Einheit), **Winkel** `45°` (kein Zwischenraum).
  Beim Prozentzeichen gilt nach der Zeile oben **kein** Zwischenraum.
- **Großschreibung am Satzanfang für Termini, die sonst klein gesetzt werden**: „top-K" im Satzinneren, aber
  „Top-K ist die Zahl der Fragmente, die das Retrieval zurückgibt." Ebenso „vLLM", „promptfoo" — den Satz
  lieber umbauen, als eine erzwungene Kleinschreibung an den Anfang zu stellen.

---

## §1.0 Dreiklassige Termpolitik — **invertiert gegenüber dem Slowakischen**

Jeder Fachterminus gehört in genau eine von drei Klassen, und die **Richtung** (englisch geführt vs. deutsch
geführt) wird **einmal** entschieden und gilt für den ganzen Korpus. **Richtungswackeln innerhalb einer Seite
ist ein Defekt** — dieselbe Seite darf nicht einmal „strikter Modus" und einmal „Strict Mode" als Namen des
Terminus schreiben.

- **Klasse 1 — exakte Bezeichner und Produktnamen:** englisch, in Codeschrift oder als Eigenname, nie
  übersetzt: `parallel_tool_calls`, `tool_choice`, `strict: true`, `additionalProperties`, **Structured
  Outputs** (Feature-Name), Produkt- und Modellnamen.
- **Klasse 2 — englische Fachtermini, mit deutschem Artikel geführt (der REGELFALL):** der englische Term
  bleibt stehen und wird **deutsch flektiert und durchgekoppelt** — *der Tool-Call, das Tool-Result, die
  Tool-Definition, im Strict Mode, das Constrained Decoding, der Idempotency Key, der Dry-Run*. Beim
  **ersten Vorkommen auf einer Seite** einmal ein kurzer deutscher Glossierungszusatz in Klammern, danach
  nackt.
- **Klasse 3 — deutsch geführte Termini (die AUSNAHME):** ein Terminus wird nur dann deutsch geführt, wenn
  die deutsche Form in der Fachsprache **wirklich die übliche ist** — *das Modell, der Kontext, die Anfrage,
  die Antwort, der Fehler, der Ausfall, die Latenz, der Durchsatz, die Berechtigung*. Der englische Ausdruck
  steht dann einmal in Klammern (Brückenrichtung, §7). Jede Klasse-3-Zuordnung ist eine **bewusste, im
  Ledger begründete** Entscheidung, nicht der Default.

**Warum das genau umgekehrt zum Slowakischen ist.** Der slowakische Kanon hat für *tool definition*, *tool
call*, *tool result*, *strict mode*, *constrained decoding*, *idempotency key* und *dry-run* **slowakisch
geführte** Formen festgelegt, weil die slowakische Entwicklersprache dort wirklich heimische Wörter benutzt.
Die deutsche Praktikerprosa tut das **nicht**: sie sagt *Tool-Call*, *Strict Mode*, *Constrained Decoding*,
*Idempotency Key*. Ein deutscher Prägungssatz (*Werkzeugaufruf*, *strikter Modus*, *eingeschränkte
Dekodierung*) ist grammatisch einwandfrei und vollständig dekodierbar — und liest sich **exakt wie die
übersetzte Marketingprosa, die die Drucklatte abweist**, nur aus der Gegenrichtung. Deshalb ist die
kept-EN-Liste im Deutschen um ein Vielfaches länger als im Slowakischen.

> ### Die Regel „ein Anglizismus ist ein Defekt" wird NICHT übernommen
>
> Der russische Kanon führt Anglizismen als benannten Defekt; der slowakische führt Bohemismen so. **Für das
> Deutsche gilt beides nicht.** Ein englischer Fachterminus in deutscher Fachprosa ist hier **kein Fehler,
> kein Stilbruch und kein Übersetzungssignal** — er ist der Normalfall des Registers, in dem dieses Buch
> geschrieben ist.
>
> Das steht hier ausdrücklich, weil ein wohlmeinender Lektor die Regel sonst aus dem Nachbarkanon
> **re-importiert** und dabei systematischen Schaden anrichtet: Er ersetzt fünfzig eingeführte englische
> Termini durch grammatisch korrekte deutsche Neuprägungen, und der Text liest sich danach übersetzt statt
> nativ. **Wer Anglizismen im Deutschen jagt, jagt hier das Falsche.** Was stattdessen gejagt wird, steht in
> §1.3 (Lehnwortmorphologie, Durchkopplung, regionale Varianz) und §1.4 (englischer Satzbau).
>
> Was weiterhin ein Defekt ist: **ein englischer Terminus ohne deutschen Artikel und ohne Flexion**
> („nach Tool Call kommt Tool Result" ✗ → „nach dem Tool-Call kommt das Tool-Result"), ein **undurchgekoppelter**
> Mehrwortbegriff (§1.3.3), und ein **wackelndes Genus** (§1.1).

**Glossreinheit.** Der Glossierungszusatz in Klammern bei einem englisch geführten Terminus ist **reines
Deutsch**, der englische Zusatz bei einem deutsch geführten Terminus ist **reines Englisch** — nie ein
Hybrid: „der Dry-Run (Probelauf ohne Wirkung)" ✓, „Laufzeitfehler (runtime error)" ✓, „(Runtime-Fehler)" ✗.

---

## §1.1 Kept-EN-Register — Genus, Plural, Genitiv

**Dies ist der größte Abschnitt, den das Deutsche gegenüber dem Russischen und Slowakischen hinzufügt, und
der einzige ohne Vorlage.** Russisch und Slowakisch weisen das Genus morphologisch aus der Endung zu; keiner
der beiden Kanons braucht deshalb eine solche Tabelle. Deutsch verlangt zu **jedem** Substantiv einen Artikel,
und der native Usus ist bei einem Teil dieser Wörter echt gespalten. **Wackeln innerhalb einer Seite ist das
lauteste denkbare Maschinenübersetzungs-Signal** — lauter als eine ungeschickte Wortwahl, weil kein Mensch,
der Deutsch als Erstsprache schreibt, denselben Begriff auf derselben Seite mit zwei Artikeln versieht.

Regel: **die hier eingetragene Form gilt**, auch wenn die Alternative ebenfalls korrekt ist. Wo die
Alternative korrekt ist, steht sie in der Spalte „Nebenform" — als Erlaubnis für Zitate, nicht als Wahl.

| Terminus | Artikel | Plural | Genitiv Sg. | Status / Beleg |
|---|---|---|---|---|
| Cache | **der** Cache | die Caches | des Cache**s** | SETTLED — Duden: „der Cache; Genitiv: des Cache, Plural: die Caches" <https://www.duden.de/rechtschreibung/Cache>. DWDS druckt „Cache(s)" — **Hausform mit -s**, damit sie zu allen übrigen Zeilen passt. |
| Prompt | **der** Prompt | die Prompts | des Prompts | SETTLED — Duden und DWDS führen beide **nur Maskulinum**: „der Prompt; Genitiv: des Prompts, Plural: die Prompts" <https://www.duden.de/rechtschreibung/Prompt>. Ein vereinzeltes „das Prompt" kommt in freier Wildbahn vor und ist **kein** Vorbild. |
| Token | **das** Token | die Tokens | des Tokens | **DISPUTED** — Duden: „das oder der Token; Genitiv: des Tokens, Plural: die Token[s]" <https://www.duden.de/rechtschreibung/Token>; DWDS ebenfalls beide Genera. **Gegenevidenz:** die deutsche KI-Fachprosa neigt zum Maskulinum (de.wikipedia, *Large Language Model*: „Ein Token ist eine Zeichenkette …", „Jeder Token wird dann zum Embedding"). **Incumbent: das Token / die Tokens** (Duden nennt das Neutrum zuerst). Kein Flip ohne nativen Check. |
| Agent | **der** Agent | die Agenten | **des Agenten** | SETTLED (Morphologie) — Duden: „der Agent; Genitiv: des Agenten, Plural: die Agenten" <https://www.duden.de/rechtschreibung/Agent>. **n-Deklination: „des Agents" ✗, „dem Agent" ✗** — der voraussichtlich häufigste Flexionsfehler dieses Korpus. Duden führt den Software-Sinn nicht; er erbt die Deklination (de.wikipedia *Softwareagent*: „Als Software-Agent … bezeichnet man ein Computerprogramm"). |
| Kontext | **der** Kontext | die Kontexte | des Kontext[e]s | SETTLED — Duden <https://www.duden.de/rechtschreibung/Kontext> |
| KI | **die** KI | die KIs | der KI | SETTLED — Duden: „die KI; Genitiv: der KI, Plural: die KIs" <https://www.duden.de/rechtschreibung/KI> |
| API | **die** API | die APIs | der API | **DISPUTED** — DWDS führt **zwei** Einträge: Neutrum als Haupteintrag („das API; Genitiv: API(s)") und Femininum **umgangssprachlich markiert** <https://www.dwds.de/wb/API>; kein Duden-Lemma. **Incumbent: die API**, weil die deutsche Vollform *die Programmierschnittstelle* feminin ist und die Fachprosa dem folgt. Der Konflikt steht hier, damit ihn niemand für ein Versehen hält. |
| Pipeline | **die** Pipeline | die Pipelines | der Pipeline | SETTLED — Duden: „die Pipeline; Genitiv: der Pipeline, Plural: die Pipelines" <https://www.duden.de/rechtschreibung/Pipeline> (CI/CD-Sinn bei heise belegt) |
| Index | **der** Index | die Indizes | des Index[es] | SETTLED (Genus) / Plural gespalten — Duden: „der Index; Genitiv: des Index[es], Plural: die Indexe und Indizes, auch: Indices" <https://www.duden.de/rechtschreibung/Index>; DWDS reiht *Indizes* zuerst. **Hausform: Indizes.** |
| Batch | **der** Batch | die Batches | des Batch**s** | SETTLED (Genus gespalten) — Duden: „der oder das Batch; Genitiv: des Batchs, Plural: die Batches" <https://www.duden.de/rechtschreibung/Batch>. **Hausform: der Batch.** Achtung Genitiv: *des Batchs*, nicht „des Batches". |
| Alert | **der** Alert | die Alerts | des Alerts | SETTLED (Genus gespalten) — Duden: „der oder das Alert; Genitiv: des Alerts, Plural: die Alerts" <https://www.duden.de/rechtschreibung/Alert>. **Hausform: der Alert.** |
| Cluster | **der** Cluster | die Cluster | des Clusters | SETTLED — Duden: „der, (auch:) das Cluster; Genitiv: des Clusters, Plural: die Cluster" <https://www.duden.de/rechtschreibung/Cluster>. **Hausform: der Cluster.** |
| Container | **der** Container | die Container | des Containers | SETTLED — Duden <https://www.duden.de/rechtschreibung/Container> |
| Thread | **der** Thread | die Threads | des Thread[s] | SETTLED — Duden <https://www.duden.de/rechtschreibung/Thread> |
| Schema | **das** Schema | die Schemata | des Schemas | SETTLED — Duden: „das Schema; Genitiv: des Schemas, Plural: die Schemen, Schemata, Schemas" <https://www.duden.de/rechtschreibung/Schema>. **Hausform: Schemata** (so auch in der deutschen Fachprosa: „typisierte Funktionen und Zod-Schemata", heise). |
| Score | **der** Score | die Scores | des Scores | SETTLED — Duden, und bereits im richtigen Sinn: „Zahlenwert, Messwert z. B. eines Tests" <https://www.duden.de/rechtschreibung/Score> |
| Framework | **das** Framework | die Frameworks | des Frameworks | SETTLED — Duden **und** DWDS stimmen überein <https://www.duden.de/rechtschreibung/Framework> |
| Dashboard | **das** Dashboard | die Dashboards | des Dashboards | SETTLED — Duden <https://www.duden.de/rechtschreibung/Dashboard> |
| Sandbox | **die** Sandbox | die Sandboxen | der Sandbox | SETTLED — DWDS: „Substantiv (Femininum) · Nominativ Plural: Sandboxen/Sandboxes" <https://www.dwds.de/wb/Sandbox>. **Hausform: die Sandboxen.** |
| Deployment | **das** Deployment | die Deployments | des Deployments | SETTLED — DWDS <https://www.dwds.de/wb/Deployment> |
| Latenz | **die** Latenz | die Latenzen | der Latenz | SETTLED — Duden (Genus) + DWDS (Plural) |
| Durchsatz | **der** Durchsatz | die Durchsätze | des Durchsatzes | SETTLED — Duden, mit EDV-Sinn: „Zahl der pro Zeiteinheit verarbeiteten Anweisungen oder übertragenen Daten" <https://www.duden.de/rechtschreibung/Durchsatz> |
| Tool-Definition | **die** Tool-Definition | die Tool-Definitionen | der Tool-Definition | SETTLED (Kopfprinzip) — das deutsche Grundwort *Definition* bestimmt Genus und Flexion des Determinativkompositums |
| Prompt-Injection | **die** Prompt-Injection | die Prompt-Injections | der Prompt-Injection | SETTLED (Kopfprinzip + § 45 E1) — Grundwort *Injection* feminin; im Fachjournalismus feminin belegt („Eine Prompt Injection in einem Repository …", heise). **Schreibung mit Bindestrich, siehe §1.3.3** — die dort verbreitete Getrenntschreibung ist die vom Regelwerk ausdrücklich als nicht normgerecht bezeichnete. |
| Commit | **der** Commit | die Commits | des Commits | **WEAK** — kein Duden-/DWDS-Lemma; maskulin belegt über de.wikipedia („Ein Commit …") <https://de.wikipedia.org/wiki/Commit>. Plural und Genitiv sind **regelhaft abgeleitet**, nicht belegt. |
| Harness | **der** Harness | die Harnesses | des Harness | **WEAK** — kein Wörterbucheintrag; maskulin zweifach kasusmarkiert in deutscher Fachpresse belegt: „sowohl für **den** Coding-Harness von Claude Code als auch für **den** Harness des eigenen Agenten" (heise) <https://www.heise.de/news/Claude-Code-in-der-Praxis-eigenen-KI-Chat-Agenten-in-fuenf-Sessions-entwickeln-11353330.html>. Wo es unsicher wirkt: als Kompositum umgehen („das Agentengerüst"). |
| Embedding | **das** Embedding | die Embeddings | des Embeddings | **HOUSE** (Plural belegt, **Genus nicht**) — Beleg schließt nur Femininum aus („Jeder Token wird dann **zum** Embedding", de.wikipedia); Plural belegt („Als Embeddings werden Vektoren bezeichnet"). Genus aus der Analogie *das Training, das Ranking*. Die deutsche Prägung *Worteinbettung* existiert (de.wikipedia), gehört ins enzyklopädisch-mathematische Register und ist **nicht** die Korpusform. |
| Chunk | **der** Chunk | die Chunks | des Chunks | **HOUSE** (Plural belegt, Genus nicht) — „Die einzelnen Chunks werden mittels Tokenisierung in Token zerlegt" (de.wikipedia, *Retrieval-Augmented Generation*) |
| Chunking | **das** Chunking | (kein Plural) | des Chunkings | HOUSE (-ing-Nominalisierung → Neutrum, analog *das Training*) |
| Reranking | **das** Reranking | (kein Plural) | des Rerankings | HOUSE (wie *Chunking*) |
| Grounding | **das** Grounding | (kein Plural) | des Groundings | HOUSE (wie *Chunking*) |
| Fine-Tuning | **das** Fine-Tuning | die Fine-Tunings | des Fine-Tunings | HOUSE (wie *Chunking*) |
| Retrieval | **das** Retrieval | (meist kein Plural) | des Retrievals | **HOUSE — Genus unbelegt.** Es wurde kein artikelführender Beleg gefunden; de.wikipedia führt *Information Retrieval* artikellos. Als Hausform verwenden, **nicht** als Norm zitieren. |
| Trace | **der** Trace | die Traces | des Traces | HOUSE (kein Wörterbucheintrag) |
| Span | **der** Span | die Spans | des Spans | HOUSE (kein Wörterbucheintrag) |
| Endpoint | **der** Endpoint | die Endpoints | des Endpoints | HOUSE (kein Wörterbucheintrag) |
| Payload | **die** Payload | die Payloads | der Payload | HOUSE (kein Wörterbucheintrag) |
| Worker | **der** Worker | die Worker | des Workers | HOUSE (kein Wörterbucheintrag) |
| Branch | **der** Branch | die Branches | des Branches | HOUSE (kein Wörterbucheintrag) |
| Repository | **das** Repository | die Repositorys | des Repositorys | **WEAK** — Duden-Seite lieferte 403, DWDS kein Lemma; Neutrum belegt über „in **einem** Repository" (heise). Plural und Genitiv regelhaft abgeleitet. |
| Trade-off | **der** Trade-off | die Trade-offs | des Trade-offs | HOUSE (kein Wörterbucheintrag) |
| Tool | **das** Tool | die Tools | des Tools | HOUSE |
| Tool-Call | **der** Tool-Call | die Tool-Calls | des Tool-Calls | HOUSE (Genus vom Grundwort *Call*) — **Schreibung**: § 45 E1, siehe §1.3.3. Die im Fachjournalismus verbreitete Getrenntschreibung „Tool Calls" ist **nicht** normgerecht. |
| Tool-Result | **das** Tool-Result | die Tool-Results | des Tool-Results | HOUSE |
| **Log** | **das** Log | die Logs | des Logs | **HOUSE mit Warnung.** Der Wörterbucheintrag ist der **seemännische** („das Log … Plural: **Loge**", Messgerät für die Schiffsgeschwindigkeit, DWDS) und taugt **nicht** als Beleg für den IT-Sinn — insbesondere ist „Loge" **nicht** der IT-Plural. Wer belegen will, schreibt **die Logdatei / das Protokoll**. |
| **Queue** | **die** Queue | die Queues | der Queue | **HOUSE mit Warnung.** Die Wörterbucheinträge betreffen den **Billardstock** (Neutrum/Maskulinum) und eine veraltete Personen-Warteschlange (Femininum). Der Message-Queue-Sinn ist **unbelegt**. Wo möglich: **die Warteschlange**. |
| **Guardrail** | **OPEN (Singular)** | die Guardrails | **OPEN** | OPEN — für den jungen KI-Sinn ist kein stabiler deutscher Singularusus belegbar. **Bis zur Klärung: nur im Plural** („Guardrails", Glosse „(Leitplanken)"); heise belegt *Leitplanken* als natives Bild <https://www.heise.de/news/Nvidias-Open-Source-Toolkit-soll-Leitplanken-fuer-Chatbots-bieten-8983722.html>. Singular **nicht erfinden**. |
| **Gate** | **OPEN als Einzelwort** | die Gates | — | OPEN — der Wörterbucheintrag „das Gate" betrifft den **Flughafen-Sinn** (DWDS). Im Deutschen ist fast nur das feste Kompositum belegt: **das Quality Gate** ist in deutscher CI/CD-Prosa etabliert (heise/iX) <https://www.heise.de/ratgeber/Shift-Left-Secure-by-Design-und-agile-Entwicklung-4613935.html?seite=4>. Nacktes „das Gate" für den Kontrollpunkt **nicht** setzen; siehe die Sense-Card `gate` im Kurs-Ledger. |

**Nachtrag-Regel.** Jeder neue englische Terminus, der im Korpus zum zweiten Mal vorkommt, bekommt **vor**
seinem zweiten Vorkommen eine Zeile in dieser Tabelle. Wer keinen Beleg findet, trägt **OPEN** ein und
umgeht das Wort, statt einen Artikel zu erfinden — ein erfundener Artikel wird im nächsten Absatz von einem
anderen erfundenen Artikel abgelöst, und genau das ist der Defekt, den diese Tabelle verhindert.

---

## §1.2 Deutsch geführte Formen (Klasse 3)

Diese Termini stehen im Lektionstext **deutsch**; beim ersten Vorkommen auf einer Seite steht der **englische
Originalausdruck in Klammern** (umgekehrte Brückenrichtung, §7).

| Kanon | Original | Abgelehnt / Hinweis |
|---|---|---|
| das Modell | model | „das Model" ✗ (= Fotomodell/Datenmodell-Anglizismus) |
| der Kontext | context | — |
| die Anfrage | request | „der Request" ist zulässig, wenn ausdrücklich das Protokollobjekt gemeint ist |
| die Abfrage | query (SQL, Suche) | nicht mit *Anfrage* mischen: Abfrage = an einen Index/eine Datenbank |
| die Frage | query (Nutzerfrage) | — |
| die Antwort | answer / response | — |
| der Fehler | error | — |
| der Ausfall; ausfallen | outage; to go down | Verfügbarkeit, **nicht** semantische Korrektheit (§9.2) |
| die Latenz / der Durchsatz | latency / throughput | — |
| die Berechtigung; die Zugriffssteuerung | permission; access control | „Zugriffskontrolle" ist Kalke von *control* → Steuerung |
| die Bereitstellung; bereitstellen, ausrollen | deployment; to deploy | das Substantiv *Deployment* bleibt kept-EN (§1.1); das **Verb** wird deutsch |
| protokollieren | to log | „loggen" nur im saloppen Nebensatz, nie als Terminus |
| zwischenspeichern | to cache | das Substantiv *Cache* bleibt kept-EN |
| auslösen | to trigger | „triggern" nur salopp |
| einbetten | to embed | das Substantiv *Embedding* bleibt kept-EN; „embedden" ✗ |
| überwachen | to monitor | „monitoren" ✗ als Terminus |

> **Muster, das diese Tabelle trägt:** im Deutschen ist häufig **das Substantiv englisch und das Verb
> deutsch** — *das Embedding* / *einbetten*, *der Cache* / *zwischenspeichern*, *das Deployment* /
> *bereitstellen*, *das Log* / *protokollieren*. Das ist kein Widerspruch, sondern der belegte Usus: das
> Substantiv ist der Terminus, das Verb ist gewöhnliche Prosa. Wer beides angleicht — „geembeddet",
> „gecachet", „gedeployt" —, schreibt Jargon, wo Fachprosa steht (§1.3.2).

---

## §1.3 Die Interferenzkontrolle (der deutsche Gegenpart zum Anti-Bohemismus)

Das Slowakische hat mit dem Anti-Bohemismus sein tragendes Artefakt: eine **benannte, immer eingeschaltete
Prüfung** gegen eine fast identische Schwestersprache, die Modelle einmischen. **Deutsch hat keine solche
Schwestersprache** — die Stelle bleibt trotzdem nicht leer. Sie wird gefüllt mit den drei Prüfungen, die im
Deutschen den größten Ertrag bringen, in dieser Reihenfolge. Die ersten beiden haben gegenüber dem
Bohemismus-Test einen **Vorteil**: sie sind **im Voraus entscheidbar** — man kann sie einmal festlegen,
statt sie auf jeder Seite neu zu erkennen.

### §1.3.1 Lehnwortgenus und -flexion

Siehe §1.1. Die Prüfung lautet: **Steht jedes englische Substantiv auf dieser Seite mit dem Artikel, den §1.1
festlegt — und mit demselben auf der ganzen Seite?** Zwei Genera für einen Begriff auf einer Seite: Defekt.
Ein Genus, das §1.1 nicht kennt: Zeile nachtragen oder Wort umgehen. Häufigster Einzelfehler:
**„des Agents" statt „des Agenten"** (n-Deklination).

### §1.3.2 Denglisch-Verbmorphologie

Eine **Korrektheits-Achse, keine Geschmacksachse**: Partizip II und Hilfsverb jedes entlehnten Verbs werden
**einmal** festgelegt, sonst entscheidet jede der 67 Seiten neu. **Und hier gibt es, anders als beim Genus,
eine echte Entscheidungsprozedur** — zwei Regeln entscheiden fast alles im Voraus:

> **Regel 1 — `-t` oder `-ed`? Amtliches Regelwerk 2024, § 21 E2.**
> „In zwei Fallgruppen ist im Partizip II auch die der Herkunftssprache entsprechende Flexionsendung **-ed**
> zulässig. (1) bei Verben, **deren Infinitiv im Englischen auf ein stummes e endet**: getimt/getimed,
> gelikt/geliked, gefakt/gefaked … **Aber:** Sind die Partizipien flektiert oder gesteigert, ist in beiden
> Fällen **ausschließlich die deutsche Endung zulässig**: eine gefakte Nachricht."
> <https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf> (S. 44)
>
> Daraus folgt deterministisch: englischer Infinitiv auf stummes **-e** (*cache, route, parse, merge*) → `-t`
> **und** `-ed` zulässig. **Kein** stummes -e (*deploy, download, commit, trigger*) → **`-ed` ist schlicht
> falsch**. **Attributiv gebeugt → immer `-t`** („der gecachte Wert", „geparster Code").
>
> **Regel 2 — `ge-` oder nicht? Betonung entscheidet** (IDS/grammis): „Das Partizipialpräfix ge- wird nicht
> gesetzt bei: Verben ohne Initialbetonung" <https://grammis.ids-mannheim.de/progr@mm/5210>. Daher
> *de-PLOY-en* → **deployt**, *com-MIT-ten* → **committet**, *de-BUGG-en* → **debuggt**, und alle
> `-ieren`-Verben → **indexiert, skaliert, refaktorisiert** (nie „geindexiert").

Alle folgenden Verben bilden das Perfekt mit **haben** und sind **nicht trennbar** (auch *downloaden* nicht:
„ich downloade", nicht „ich loade down").

| Infinitiv | Partizip II | Status / Beleg | Korpusregel |
|---|---|---|---|
| downloaden | **downgeloadet** / **gedownloadet** — „gedownloaded" ✗ | SETTLED — Regelwerk-Wörterverzeichnis S. 187: „downloaden downloadete, downgeloadet/gedownloadet § 21(2)" | **im Korpus: „heruntergeladen"** — der Korpus umgeht die Doppelform |
| uploaden | **geuploadet** (auch upgeloadet) | SETTLED — DWDS <https://www.dwds.de/wb/uploaden> | **im Korpus: „hochgeladen"** |
| prompten | **gepromptet** | SETTLED — Duden: „promptet, promptete, hat gepromptet" <https://www.duden.de/rechtschreibung/prompten> | zulässig; für die tatsächliche Prompt-Interaktion |
| cachen | **gecacht** / gecached; attributiv nur **gecachte** | SETTLED — DWDS: „cacht, cachte, hat gecacht/gecached", ausdrücklich unter „§ 21 (E2.1)" <https://www.dwds.de/wb/cachen> | **im Korpus: „zwischengespeichert"**; das Substantiv bleibt *der Cache*. **„gecachet" ✗** |
| deployen | **deployt** (kein `ge-`, kein `-ed`) | SETTLED — DWDS <https://www.dwds.de/wb/deployen>; iX: „Ist die Anwendung erfolgreich deployt …" | **im Korpus: „bereitgestellt" / „ausgerollt"** — aber *deployen* ist in deutscher Fachpresse etabliert und **kein** Fehler |
| committen | **committet** (kein `ge-`) | SETTLED (Form) — Duden: „committet sich, committete sich, hat sich committet" <https://www.duden.de/rechtschreibung/committen>. **OPEN für den Git-Sinn:** die Wörterbücher lexikalisieren nur das reflexive „sich committen" | Git-Kontext zulässig; alternativ „eingecheckt / übernommen" |
| mergen | **gemergt**; prädikativ auch **gemerged** | SETTLED — DWDS: „hat gemergt/gemerged … bei **prädikativem Gebrauch** auch … gemerged" <https://www.dwds.de/wb/mergen> | Git-Kontext zulässig; sonst „zusammengeführt" |
| triggern | **getriggert** | SETTLED — Duden <https://www.duden.de/rechtschreibung/triggern> | **im Korpus: „ausgelöst"** |
| loggen | **geloggt** | SETTLED — DWDS, dessen eigene Glosse „protokollieren" lautet <https://www.dwds.de/wb/loggen> | **im Korpus: „protokolliert"** |
| parsen | **geparst** / geparsed; attributiv nur **geparster** | SETTLED — Duden: „du hast geparst oder geparsed; aber **nur geparster Code**" <https://www.duden.de/rechtschreibung/parsen> | etabliert, zulässig |
| mappen | **gemappt** | SETTLED — Duden <https://www.duden.de/rechtschreibung/mappen> | **im Korpus: „abgebildet" / „zugeordnet"** |
| routen | **geroutet** / gerouted; attributiv **geroutete** | SETTLED — Duden <https://www.duden.de/rechtschreibung/routen> | **im Korpus: „weitergeleitet"** |
| monitoren | **gemonitort** | SETTLED — **Duden führt das Verb als volles Lemma**: „monitort, monitorte, hat gemonitort" <https://www.duden.de/rechtschreibung/monitoren> | **im Korpus: „überwacht"** — als **Stilentscheidung**, nicht als Korrektheitsfrage. *gemonitort* ist korrektes Deutsch, nur stilistisch markiert |
| rendern | **gerendert** | SETTLED — Duden <https://www.duden.de/rechtschreibung/rendern> | etabliert, zulässig |
| debuggen | **debuggt** (kein `ge-`) | SETTLED — Duden <https://www.duden.de/rechtschreibung/debuggen> | zulässig |
| streamen | **gestreamt** | SETTLED — Duden <https://www.duden.de/rechtschreibung/streamen> | zulässig |
| forken | **geforkt** | SETTLED — DWDS <https://www.dwds.de/wb/forken> | zulässig |
| pushen | **gepusht** | SETTLED (Form) / WEAK (Git-Sinn) — Duden markiert alle Bedeutungen als *salopp/Jargon* und kennt **keinen** Git-Sinn | zulässig im Git-Kontext, sonst meiden |
| indexieren | **indexiert** (kein `ge-`) | SETTLED — Duden <https://www.duden.de/rechtschreibung/indexieren> | bereits deutsch |
| skalieren | **skaliert** (kein `ge-`) | SETTLED — Duden <https://www.duden.de/rechtschreibung/skalieren> | bereits deutsch |
| **refaktorisieren** | **refaktorisiert** (kein `ge-`) | SETTLED — die deutsche Form lautet **refaktorisieren**, nicht „refaktorieren" und nicht „refactoren"; heise verwendet sie („statt wild drauf los zu refaktorisieren") | **die Korpusform** |
| **embedden** | — | **OPEN** — kein Duden-, DWDS- oder Wiktionary-Eintrag | **im Korpus: „eingebettet"**; das Substantiv bleibt *das Embedding*. „geembeddet" **nicht** schreiben |
| **chunken** | — | **OPEN** — kein Wörterbucheintrag | **im Korpus: „aufgeteilt / zerlegt / unterteilt"**; das Substantiv bleibt *das Chunking*. „gechunkt" **nicht** schreiben |
| **refactoren** | — | **OPEN** — kein Wörterbucheintrag | ersetzt durch **refaktorisieren** |
| **stubben** | — | **OPEN** — kein Wörterbucheintrag | „einen Stub bereitstellen" |
| **pullen** | (gepullt) | **OPEN für den Git-Sinn — und mit Warnung** | ⚠ **meiden**: die Wörterbuchbedeutungen sind nautisch, reiterlich, Golf — und „salopp, derb Wasser lassen" (DWDS). Im Korpus: **„abrufen / holen"** |

> **Belastbarkeit, ehrlich.** Anders als beim Genus ist diese Achse überwiegend **kodifiziert** — die meisten
> Zeilen stehen so im Duden, im DWDS oder im amtlichen Wörterverzeichnis. Die vier OPEN-Zeilen (*embedden,
> chunken, refactoren, stubben*) haben **gar keine** lexikografische Deckung; deshalb weicht der Korpus dort
> auf das deutsche Verb aus. Das ist **keine Anglizismus-Jagd** (§1.0 verbietet die), sondern die Vermeidung
> einer Form, für die es keine Norm gibt und über die deshalb jede Seite anders entscheiden würde.

### §1.3.3 Durchkopplung

Drei Regelstellen entscheiden alles, und sie hängen davon ab, **wie viele Teile** die Fügung hat und **welcher
Wortart** die Teile angehören. Die Unterscheidung ist tragend — wer nur „immer Bindestrich" merkt, schreibt in
der Hälfte der Fälle etwas Falsches.

**(a) Drei oder mehr Teile, oder eine Wortgruppe als Bestandteil → Durchkopplung ist PFLICHT (§ 44).**

> „**§ 44** Ein Bindestrich wird gesetzt **zwischen allen Bestandteilen** mehrteiliger Zusammensetzungen, in
> denen eine **Wortgruppe** oder eine Zusammensetzung mit Bindestrich auftritt … (1) … `Ad-hoc-Bildung,
> De-facto-Anerkennung, Erste-Hilfe-Lehrgang`"
> — Amtliches Regelwerk 2024, S. 71. Dass § 44 **verbindlich** ist, sagt die Vorbemerkung (3), S. 69:
> „Gruppen, in denen der Bindestrich gesetzt werden **muss** (§ 40 bis § 44 …)".
> Und Vorbemerkung (2): „Die Schreibung mit Bindestrich bei **Fremdwörtern** … folgt den für das Deutsche
> geltenden Regeln." <https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf>

Im amtlichen Wörterverzeichnis direkt belegt: „Open Source § 37 E4 … **Open-Source-Software § 44(1)**",
„**Gender-Pay-Gap § 44(1)**", „**Open-End-Diskussion § 44(1)**". **Die Asymmetrie ist gewollt: *Open Source*
allein, *Open-Source-Software* durchgekoppelt.**

**(b) Zwei Teile, Substantiv + Substantiv → zusammen ODER mit Bindestrich; getrennt ist FALSCH (§ 45 E1).**

> „**E1:** Aus anderen Sprachen stammende Verbindungen aus **Substantiv + Substantiv**, die sich im Deutschen
> grammatisch wie Zusammensetzungen verhalten, werden **zusammengeschrieben**; als Variante ist die
> verdeutlichende Schreibung mit Bindestrich möglich: `Midlifecrisis/Midlife-Crisis,
> Shoppingcenter/Shopping-Center`. In etlichen Fällen von Entlehnungen aus dem Englischen … **wird bevorzugt
> mit Bindestrich geschrieben:** `Desktop-Publishing, Facility-Management`" — Regelwerk 2024, S. 73.

→ **`Tool-Call` ✓ (Hausform), `Toolcall` ✓ (zulässig), `Tool Call` ✗.** Dasselbe für *Tool-Result*,
*Prompt-Injection*, *Tool-Definition*, *Retrieval-Qualität*, *Chunking-Strategie*.

**(c) Zwei Teile, Adjektiv + Substantiv → darf getrennt bleiben (§ 37 E4), Großschreibung nach § 55(3).**

> „Aus dem Englischen stammende Bildungen aus **Adjektiv + Substantiv** können zusammengeschrieben werden,
> wenn der Hauptakzent auf dem ersten Bestandteil liegt, also `Happyend` oder `Happy End` … **aber nur
> `Corporate Identity`, `Social Media`**" — Regelwerk 2024, S. 62. Das Wörterverzeichnis ordnet
> „**Deep Learning § 37 E4, § 55(3)**" genau hier ein.

→ **`das Dense Retrieval`, `das Constrained Decoding`, `die Hybrid Search`, `Machine Learning`** dürfen
getrennt und großgeschrieben stehen. **Sobald sie ein Kompositum anführen, greift wieder § 44(1):**
`Dense-Retrieval-Verfahren`, `Constrained-Decoding-Strategie`, `Machine-Learning-Modell`.

#### Warum „Prompt Injection Angriff" nicht bloß unschön, sondern falsch ist

Das Regelwerk selbst benennt das Phänomen und markiert es prescriptiv (S. 47):

> „In der Getrennt- und Zusammenschreibung von substantivischen Zusammensetzungen aus dem Englischen
> überwiegt in vielen Fällen auch nach 20 Jahren im deutschen Wortschatz **die im Deutschen nicht
> normgerechte Getrenntschreibung**."

Und das Grundprinzip, Teil B Vorbemerkung (1), S. 55: „Handelt es sich um die Bestandteile von Wortgruppen,
so schreibt man sie getrennt. **Handelt es sich um die Bestandteile von Zusammensetzungen, so schreibt man
sie zusammen.**" (Populär: das „Deppenleerzeichen",
<https://de.wikipedia.org/wiki/Leerzeichen_in_Komposita>.)

**Praktische Folge für diesen Kanon:** deutsche Fachpresse schreibt vielfach „Tool Calls" und „Prompt
Injection" getrennt — das ist **genau die Getrenntschreibung, die das Regelwerk als nicht normgerecht
bezeichnet**. Der Korpus folgt der Norm, nicht der Gewohnheit, und tut es **einheitlich**.

#### Verbindliche Schreibungen für dieses Korpus

Nach Häufigkeit im Textbestand:

- **Machine-Learning-Modell** (allein: *Machine Learning*), **Large Language Model** — als ganz englische
  Fügung, oder deutsch **großes Sprachmodell**; das Mischwort „Large-Language-Modell" **meiden**
- **Prompt-Injection**, **Prompt-Injection-Angriff**, **Prompt-Injection-Schutz**
- **Tool-Call**, **Tool-Result**, **Tool-Definition**, **Tool-Auswahl**, **Tool-Call-Ergebnis**
- **Retrieval-Qualität**, **Retrieval-Schicht**, **Chunking-Strategie**, **Embedding-Modell**
- **Golden Set** (Adj+Subst, § 37 E4) — aber **Golden-Set-Pflege**
- **Quality Gate**, **Release Gate** (Adj+Subst) — aber **Quality-Gate-Regel**
- **Error-Budget**, **Blast-Radius**, **Cold-Start**, **Dead-Letter-Queue**, **Vendor-Lock-in**
- **Multi-Agenten-System**, **Agentic RAG**, **Human-in-the-Loop**, **Least-Privilege-Prinzip**
- **Open Source** — aber **Open-Source-Projekt** (amtlich belegt), **End-to-End-Test**

**Getrennt bleibt der englische Ausdruck** außerdem:

- als fremdsprachiges **Zitatwort** (§ 21 E1: „Bei Zitatwörtern gilt die englische Schreibung"): „Die
  Spezifikation nennt das *tool call*."
- als **Produkt- oder Eigenname** in der amtlich festgelegten Herstellerschreibung: **Structured Outputs**,
  **Model Armor**, **GitHub Actions**
- als **Codebezeichner**: `tool_call`, `ToolCall`, `parallel_tool_calls`
- in einem **vollständig englischen** Satz, Tabellenfeld oder Diagrammlabel

### §1.3.4 Regionale Varianz (CH / AT)

Der strukturelle Verwandte des Bohemismus-Tests: eine Form, die in einer **benachbarten Standardvarietät
völlig korrekt** und für die gewählte trotzdem falsch ist. Der Korpus ist **bundesdeutsch**.

**Die zwei Tells, die in einem IT-Text mehr wiegen als jedes einzelne Wort — beide nicht-lexikalisch:**

1. **Schweizer Zahlenformat.** `1'250'254.99` — Apostroph als Tausendertrenner, **Punkt** als Dezimaltrenner.
   Das ist sofort schweizerisch. Bundesdeutsch: Dezimalkomma, Gliederung nach § Typografie.
2. **Schweizer Anführungszeichen** «Beispiel» (nach **außen** zeigend) gegenüber deutschen »Beispiel« (nach
   **innen**). Gallmann führt beide als getrennte Systeme
   (<http://gallmann.uni-jena.de/Ortho/V_Anfuehrung_Skript.pdf>). Der Korpus verwendet ohnehin „…".

Die lexikalischen Fälle — Duden markiert die regionale Zuordnung jeweils auf der Lemmaseite:

| Vermeiden | Kanon | Duden-Markierung / Grund |
|---|---|---|
| `ss` statt `ß` (Grösse, ausserhalb, heissen, Fussnote) | Größe, außerhalb, heißen, Fußnote | Regelwerk § 25 E2: „In der Schweiz und in Liechtenstein kann immer ss geschrieben werden" |
| **das** Mail / ein Mail | **die** E-Mail / die Mail | Duden: „die Mail … (auch, besonders süddeutsch, **österreichisch, schweizerisch:**) das Mail" <https://www.duden.de/rechtschreibung/Mail> |
| Jänner | Januar | „**österreichisch**, seltener süddeutsch" <https://www.duden.de/rechtschreibung/Jaenner> |
| Feber | Februar | „**österreichisch**, besonders Amtssprache" <https://www.duden.de/rechtschreibung/Feber> |
| allfällig | etwaig / eventuell / gegebenenfalls | „besonders **österreichisch, schweizerisch**" <https://www.duden.de/rechtschreibung/allfaellig> |
| Unterbruch | Unterbrechung / Ausfall | „**schweizerisch**" <https://www.duden.de/rechtschreibung/Unterbruch> |
| Pendenz / pendent | offener Punkt / offene Aufgabe / To-do | „**schweizerisch**" <https://www.duden.de/rechtschreibung/Pendenz> |
| Traktandum | Tagesordnungspunkt | „**schweizerisch**" <https://www.duden.de/rechtschreibung/Traktandum> |
| parkieren | parken | „**schweizerisch**" <https://www.duden.de/rechtschreibung/parkieren> |
| Spital | Krankenhaus | „**österreichisch, schweizerisch**, landschaftlich, sonst veraltet" <https://www.duden.de/rechtschreibung/Spital> |
| österreichisches Fugen-s: **Fabriks**arbeiter, **Zugs**verkehr, **Aufnahms**prüfung | Fabrikarbeiter, Zugverkehr, Aufnahmeprüfung | „**österreichisch**" <https://www.duden.de/rechtschreibung/Fabriksarbeiter> — im Fachtext betrifft es Komposita wie *Zugriffsberechtigung* nicht, aber das Muster ist zu kennen |
| Beistrich | Komma | Austriazismus |

> **Grenze der Prüfung.** International etablierte IT-Termini (*Server, Repository, Commit*) sind **nicht**
> deshalb regional, weil eine Schweizer oder österreichische Publikation sie verwendet. Bereinigt werden nur
> **belegte Varianten**, nie pauschal englischer Fachwortschatz — sonst kippt diese Prüfung in genau die
> Anglizismus-Jagd, die §1.0 verbietet.

---

## §1.4 Kalkenschablonen EN→DE (worauf der Kalken-Durchgang grept)

Das Gegenstück zu §1.3, aber die Quelle ist die **englische Satzstruktur**. Das sind **grammatisch korrekte
deutsche Sätze, die englischer Bau in Verkleidung sind**: eine Rückübersetzung bildet sie 1:1 auf den
englischen Satz ab. Die deutschen Verräter sind **syntaktisch**, nicht lexikalisch — anders als im
Slowakischen, wo die Wortstellung frei ist und der Kalk sich an Kollokationen zeigt.

**Die Reparatur ist nie ein Wortersatz, sondern ein Neubau aus dem Sinn** (wer — tut was — unter welcher
Bedingung — mit welchem Ergebnis).

| Englische Struktur | Kalk im Deutschen (✗ — flaggen) | Reparaturrichtung (aus dem Sinn neu bauen) |
|---|---|---|
| `The model can call any external function` | „Das Modell kann rufen jede externe Funktion" | **Satzklammer schließen**: „Das Modell kann jede registrierte Funktion **aufrufen**." Das finite Modalverb besetzt die linke Klammer, der Infinitiv die rechte, das Objekt steht im Mittelfeld. Je nach Sinn: Fähigkeit („kann … aufrufen"), Berechtigung („darf … zugreifen"), Architektur („stehen … als Tools zur Verfügung") |
| `The error is returned to the model` | „Der Fehler wird zurückgegeben zum Modell" | „Der Fehler wird **an das Modell** zurückgegeben." — besser aktiv und rollenklar: „Das Tool meldet dem Modell den Fehler." / „Schlägt der Aufruf fehl, erhält das Modell die Fehlerdetails." (*zum* statt *an* ist zusätzlich die falsche Präposition beim kommunikativen Empfänger) |
| `the definition of the tool` | „die Definition von dem Tool" | **Kompositum oder Genitiv**: „die **Tool-Definition**" (fester Fachbegriff) / „die Definition **des Tools**" (ein bestimmtes Tool). Nicht jedes *of* in ein Kompositum pressen: bei erweitertem Bezug bleibt der Genitiv („die Definition des vom Agenten verwendeten Tools"). **Dieser Fehler ist in diesem Korpus der häufigste.** |
| `is running / is processing` | „ist am Laufen", „ist gerade am Verarbeiten" | Deutsches Präsens trägt den Verlauf schon: „Der Dienst läuft." / „Der Dienst verarbeitet gerade die Anfrage." / „Die Verarbeitung läuft noch." Der Am-Progressiv ist nicht falsch, aber regional und im Schriftdeutsch markiert |
| `does not call the tool` (Skopus verrutscht) | „Das Modell **nicht** ruft das Tool auf", „ruft nicht auf das Tool" | *nicht* steht an der **Skopusgrenze**: Satznegation „ruft das Tool **nicht auf**"; Objektkontrast „ruft **nicht das Tool**, sondern die lokale Funktion auf"; Modalität „**muss** das Tool **nicht** aufrufen" (kein Zwang) vs. „**darf** das Tool **nicht** aufrufen" (Verbot). **Test:** eine *sondern*-Fortsetzung bilden — passt keine, ist es Satznegation |
| `What X changes is …` / `It is X that …` | „Was X ändert, ist …", „Es ist X, das …" | Deutscher Spaltsatz nur bei **echtem Kontrastfokus** („Nicht das Modell ändert den Zustand; es ist das Tool, das ihn ändert"). Ohne ausgeschlossene Alternative: direkt sagen — „Das Modell erzeugt eine Anfrage." **Test:** lässt sich „nicht A, sondern X" bilden? Wenn nein, ist der Spaltsatz nur englische Verpackung |
| `What is important to understand is that …` | „Was wichtig zu verstehen ist, ist, dass …" | „**Entscheidend ist, dass …**" / „Dabei ist Folgendes wichtig: …" / „Du musst zwei Fälle unterscheiden: …" |
| `Once the agent receives the data, …` | „Einmal der Agent die Daten erhält, …" | „**Sobald** der Agent die Daten erhält, …" / „Nachdem der Agent die Daten erhalten hat, …" (*einmal* leitet keinen finiten Nebensatz ein) |
| `This allows the model to call the tool` | „Das erlaubt dem Modell, **um** das Tool aufzurufen" | „**Dadurch kann** das Modell das Tool aufrufen." / „Das ermöglicht es dem Modell, das Tool aufzurufen." (*erlauben/ermöglichen* regieren den reinen *zu*-Infinitiv; *um zu* ist final) |
| `By using a re-ranker, …` | „Durch Verwenden eines Re-Rankers …" | „Durch **den Einsatz** eines Re-Rankers …" / „Wenn du einen Re-Ranker einsetzt, …" |
| `different than expected` | „unterschiedlich als erwartet" | „Das Ergebnis **weicht von** der Erwartung **ab**." / „… fällt **anders aus als** erwartet." |
| `ends up calling the tool twice` | „Der Agent endet damit, das Tool zweimal aufzurufen" | „**Schließlich** ruft der Agent das Tool zweimal auf." / „Infolgedessen …" |
| `You want to validate the answer` | „Du willst die Antwort validieren" | „Du **solltest** die Antwort prüfen." / „Prüfe die Antwort, bevor du sie weiterverarbeitest." (*you want to* ist Empfehlung, nicht Wille) |
| `supports calling external tools` | „unterstützt das Aufrufen externer Tools" | „**kann** externe Tools aufrufen" / „unterstützt Aufrufe externer Tools" |
| `The request comes with three parameters` | „Die Anfrage kommt mit drei Parametern" | „Die Anfrage **enthält** drei Parameter." |
| `is responsible for generating the answer` | „ist verantwortlich für das Erzeugen der Antwort" | „Das Modell **erzeugt** die Antwort." / „Für die Antwortgenerierung ist das Modell **zuständig**." (*verantwortlich* aktiviert Haftung) |
| `This results in a wrong answer` | „Dies resultiert **in** einer falschen Antwort" | „**Dadurch entsteht** eine falsche Antwort." / „Das **führt zu** …" (*resultieren* regiert *aus*, nicht *in*) |
| `Receiving the request, the agent checks the cache` | „Die Anfrage empfangend, prüft der Agent den Cache" | „**Nachdem** der Agent die Anfrage empfangen hat, prüft er den Cache." (englische `-ing`-Nebensätze werden im Deutschen zu Temporal-, Kausal- oder Modalsätzen) |
| `The prompt is generated by the agent` | „Der Prompt wird durch den Agenten erzeugt" | „**Der Agent erzeugt den Prompt.**" — Passiv nur zur Agensausblendung oder für eine andere Thema-Rhema-Gliederung, nicht als Standardform |
| lange Linksattribute | „die durch das Modell nach dem Abruf aus der Datenbank erzeugte Antwort" | „die Antwort, **die** das Modell nach dem Datenbankabruf erzeugt" — Relativsatz statt überladenes Vorfeld |

**Unterklammerte Hauptsatzketten — flaggen, aber mit Bedacht.** Eine Folge kurzer, je für sich korrekter
Hauptsätze ist **kein sicheres** Übersetzungsindiz: in Anleitungen und Warnungen ist sie idiomatisch
(„Starte den Dienst. Prüfe das Protokoll."). **Verdächtig wird sie, wenn logisch abhängige Aussagen nur
deshalb getrennt bleiben, weil das Englische unabhängige Sätze verwendet** — Ursache, Bedingung und Zweck
bleiben unmarkiert, bekannte Information wird immer wieder zum neuen Satzsubjekt, alles trägt denselben
Rang:

> ✗ „Das Modell ruft das Tool auf. Das Tool gibt Daten zurück. Das Modell verwendet die Daten. Es erzeugt
> eine Antwort."
> ✓ „Das Modell ruft zunächst das Tool auf. Dessen Rückgabe übernimmt es in den Kontext, aus dem es die
> Antwort erzeugt."

Die Abhilfe ist **nicht „längere Sätze", sondern eine erkennbare Hierarchie** aus Hauptaussage, Bedingung,
Folge und Zweck. *(Der Auftrag an diesen Kanon führte diese Kette als verlässliches Indiz; der Register-Gegencheck widerspricht
mit benanntem Grund. Hier steht deshalb die eingeschränkte Fassung — **STATUS: DISPUTED**, Incumbent: nur
flaggen, wenn die logischen Relationen fehlen.)*

**Verbotene Satzskelette (Grep-Liste).** Vor der Veröffentlichung wird der fertige deutsche Text gegen diese
Zeichenfolgen gegrept; **kein Treffer passiert**. Die Reparatur ist nie ein Wortersatz im Inneren der
Schablone — der Satz wird aus der Proposition neu gebaut:

- `Was ... ist, ist` (englischer Spaltsatz)
- `Es ist ... , das` / `Es ist ... , der`
- `ist am Laufen` / `ist am Verarbeiten` / `ist gerade am`
- `Einmal der` / `Einmal das` / `Einmal die` (am Satzanfang, für *once*)
- `, um ... zu` nach *erlauben* / *ermöglichen*
- `resultiert in`
- `unterschiedlich als`
- `endet damit, ... zu`
- `Du willst` (als Empfehlung)
- `ist verantwortlich für das`
- `kommt mit` (für *comes with*)
- `Durch Verwenden`
- `von dem Tool` / `von der Definition` (analytischer *of*-Genitiv, wo Kompositum oder Genitiv gehört)
- `zurückgegeben zum` / `gesendet zum` (Nachfeld + falsche Präposition)

---

## §1.5 Verb nach Objekt

Im Englischen steht überall *the model emits / issues / produces X*. Dasselbe deutsche Verb auf jedes Objekt
gemalt ist die **stärkste überlebende Übersetzungsspur** — im Slowakischen war es „vydať", und dort war die
Form sogar schon als gesetzter Autorenstil ratifiziert worden, bevor sie widerrufen wurde. Genau deshalb steht
diese Tabelle im Bootstrap und nicht in einer späteren Phase.

**Das Verb wird nach dem OBJEKT gewählt, nicht nach dem englischen Original.** Wiederholtes „Das Modell gibt
… aus" wird automatisch geflaggt.

| Objekt | Idiomatische Verben | Passt NICHT | Grund |
|---|---|---|---|
| Text | erzeugen, generieren, formulieren | auslösen | *auslösen* setzt einen Folgevorgang in Gang, bringt kein Produkt hervor |
| strukturierte Ausgabe | erzeugen, liefern, zurückgeben | formulieren | strukturierte Daten werden nicht sprachlich formuliert; *zurückgeben* nur bei Aufruf-/Antwortrelation |
| Tool-Aufruf | das Tool **aufrufen**, den Aufruf **erzeugen/initiieren**, den Aufruf **absetzen** | entscheiden | eine Entscheidung *führt zu* einem Aufruf; der Aufruf selbst wird nicht „entschieden" |
| Anfrage / Request | senden, stellen, absetzen, übermitteln | ausgeben | *stellen* für die kommunikative Bitte, *senden/absetzen* im Protokollkontext |
| Absicht / Entscheidung | Absicht äußern, formulieren; Entscheidung **treffen, fällen** | ausgeben, emittieren | Entscheidungen sind Akte, keine Datenprodukte — außer man spricht ausdrücklich über ihre serialisierte Form |
| Ergebnis | liefern, zurückgeben, berechnen, erzeugen | absetzen, stellen | *absetzen* ist eine gerichtete Kommunikationshandlung, kein Hervorbringen |
| Fehler | melden, zurückgeben, verursachen, protokollieren | entscheiden, begehen | Diagnose (*melden*), Schnittstelle (*zurückgeben*) und Entstehung (*verursachen*) sind verschiedene Rollen |
| Log-Eintrag | schreiben, erzeugen, protokollieren | auslösen | ein Ereignis *löst* einen Eintrag *aus*; die protokollierende Instanz *schreibt* ihn |
| Kennzahl / Score | berechnen, ermitteln, liefern; einen Score **vergeben** | formulieren | Kennzahlen entstehen durch Messung, nicht durch Formulierung |
| Warnung / Alert | ausgeben, melden, erzeugen; Alarm **auslösen** | berechnen | eine Warnung ist eine Mitteilung, ein Alarm ein ausgelöster Zustandswechsel |

> **„ausgeben" ist rationiert.** Es ist das technische Oberverb für die **sichtbare oder maschinenlesbare
> Bereitstellung** von Output — „Text auf der Konsole ausgeben", „Daten als JSON ausgeben", „eine Warnung
> ausgeben" ✓. Es ist **kein** neutrales Verb für jede Hervorbringung: „eine Entscheidung ausgeben", „eine
> Absicht ausgeben", „eine Anfrage ausgeben", „einen Tool-Aufruf ausgeben" ✗.
>
> **„emittieren" ist im allgemeinen Handbuchtext verboten.** Es ist standardsprachlich auf Aussendung/Abgabe
> spezialisiert (Strahlung, Wertpapiere, Signale). Als Universalübersetzung von *emit/issue* ist es
> unidiomatisch — im Telemetriekontext („ein Event emittieren") ist es tolerierter Fachjargon, sonst nicht.

---

## §3 Schreibung und Register

- **KI, nicht AI** — im deutschen Fließtext heißt das Fach **KI**: *KI-System, KI-Modell, KI-gestützt,
  KI-Entwicklung*. **STATUS: SETTLED** (Duden führt das Lemma *die KI*
  <https://www.duden.de/rechtschreibung/KI>; heise verwendet durchgehend *KI*).
  **Bewusste Divergenz von RU und SK**, die beide „AI" lateinisch führen: das Russische und das Slowakische
  haben kein etabliertes heimisches Kürzel mit dieser Verbreitung, das Deutsche hat es. **„AI" bleibt** nur
  in festen englischen Namen (Kurstitel, Produktnamen, `AI SDLC`). Die Autorenfigur „AI delta" ist im
  Deutschen **OPEN** — Vorschlag „KI-Delta", **auf Probe** (siehe Figuren).
- **top-K** — lateinisch, kleines „t" im Satzinneren und in Diagrammen; am Satzanfang „Top-K".
- **Recall@K / Precision@K** — groß, wie im Glossar; zu unterscheiden von *Context Recall / Context Precision*.
- **LLM-as-a-judge** — nur die volle Form (nicht „LLM-as-judge").
- **lost-in-the-middle** — durchgekoppelt in allen Positionen.
- **nDCG, MRR, RRF, BM25, ACL, HyDE, ReAct, TTFT, SSE, SLA, IAM, OTel, LLMOps, FinOps** — feste Schreibung
  wie hier.
- **vLLM** — kleines „v" in allen Positionen; **promptfoo** — kleines „p", nie am Satzanfang (Satz umbauen);
  **Ragas** — nur der erste Buchstabe groß (nicht „RAGAS"); **SGLang, PagedAttention** — wie hier.
- **KV-Cache** — lateinisches „KV", Bindestrich, *Cache* (kept-EN, §1.1). Genus wie *der Cache*.
- **p50 / p95 / p99** — kleines lateinisches „p".
- **ReAct** wird aufgelöst als **Reasoning + Acting** (die Beobachtung ist die Rückkopplung des Zyklus, kein
  Teil des Akronyms).
- **Produkt-, Framework- und Modellnamen** sind Eigennamen und bleiben unverändert: LangChain, LangGraph,
  LlamaIndex, Semantic Kernel, AutoGen, CrewAI, LangSmith, FastAPI, Pydantic, Kubernetes, Helm, vLLM, SGLang,
  Ollama, Hugging Face, Bedrock, Vertex AI, Azure OpenAI, Ragas, DeepEval, promptfoo, Langfuse, NeMo
  Guardrails, Llama Guard, Model Armor, Presidio, LiteLLM, ClickHouse, PostgreSQL, Redis, Claude, GPT, Gemini.
- **Beschriftungen in Mermaid-Diagrammen:** Namen von Protokollartefakten bleiben englisch („tool call: …",
  „tool result: …"); gewöhnliche Wortbeschriftungen folgen der Sprache der Seite und beginnen groß
  („Entscheidung", „Modell", „Antwort").

---

## §7 Brückenrichtung (bridge rule)

Die Richtung ist im Deutschen **spiegelverkehrt zum Slowakischen im Volumen**, nicht im Prinzip: weil die
allermeisten Termini englisch geführt sind (§1.0), ist die **häufigste** Brücke „englischer Terminus →
deutsche Glosse".

- **Glossar (Lemma):** englisch geführter Terminus → **fettes englisches Lemma + deutsche Glosse in
  Klammern**, wo sie etwas hinzufügt („**Dense Retrieval (dichte Vektorsuche)**"); nackte Namen ohne Glosse
  (BM25, ColBERT, HyDE, MRR …). Deutsch geführter Terminus → englischer Originalausdruck in Klammern
  („**Zugriffssteuerung (access control, ACL)**").
- **Lektionen (Fließtext):** kanonische Form nach §1.0/§1.1; die Brücke steht **beim ersten Vorkommen auf
  der Seite** (auf langen Seiten Auffrischung beim ersten Vorkommen in einem neuen großen Abschnitt).
- **Brückendichte:** nie zwei Brücken desselben Terminus innerhalb eines Bildschirms; eine kurze Seite kommt
  mit einer Brücke pro Terminus aus. Ein deutscher Terminus, der den Originalausdruck wörtlich spiegelt
  (Zugriffssteuerung ↔ access control), braucht höchstens eine.
- Die Videobeschreibung (`:::tip[▶ Video]`) zählt **nicht** als erstes Vorkommen; ebenso wenig eine
  **Ankündigungsliste** der Themen einer Seite vor deren Behandlung.

---

## §8 Fettdruck (Auszeichnungsbudget)

- **Budget:** nicht mehr als ~0,36 fette Abschnitte pro Zeile Prosa (dasselbe wie RU/EN/SK). Fett ist ein
  **Navigationswerkzeug, keine Intonation**.
- **Ausgezeichnet wird:** der Terminus-Anker beim ersten definierenden Vorkommen (meist zusammen mit der
  Brücke), der Kopf eines Definitionslistenpunkts, die seltene einzelne Merksatz-These einer Seite.
- **Nicht ausgezeichnet wird:** rhetorische Betonung mitten im Satz, ganze Sätze und mehrgliedrige Klauseln,
  Wiederholungen bereits eingeführter Termini — auch nicht im Abschnitt „Was du mitnimmst" (die
  Zusammenfassung zeichnet nicht erneut aus, was im Text schon ausgezeichnet ist). Ein klauselanger Merksatz
  kommt in Anführungszeichen oder Kursive, nicht in Fettdruck.

---

## §9 Konstruktionen (Angebot an den Schreibenden, keine Regel)

Das Register in §1.0–§1.2 hält **Termini**. Dieser Abschnitt hält **Konstruktionen**: wiederkehrende
englische Satzformen, die sonst jedes Mal neu entschieden werden — typisch in der Überschrift, auf die ~1%
der Tokens und ~1% der Aufmerksamkeit entfallen.

> **Status dieser Einträge.** Es sind **Startvorschläge für den Schreibenden, keine Substitution und kein
> Verbot.** Die richtige Fassung hängt davon ab, welchen Gedanken der Satz trägt; jeder Eintrag hält deshalb
> die **Bedingung der Wahl** zwischen den Rahmen fest, nicht ein Paar „englisch → deutsch". Eine gut
> begründete Abweichung vom angebotenen Rahmen ist **erwartetes Verhalten**, kein Kanonverstoß; eine
> unbegründete Abweichung ist ein gewöhnlicher Defekt. **Wenn ein Eintrag anfängt, sich wie eine
> Nachschlagetabelle zu lesen, ist es ein schlechter Eintrag — dann wird er über seine Bedingung neu
> geschrieben.**
>
> Das ist **nicht** das Gegenstück zu §1.4. §1.4 zählt Formen auf, die **geflaggt** werden; §9 bietet Rahmen
> an, zwischen denen **entschieden** wird.

### 9.1 `N ways X does Y`

- **Rahmen „N Wege / N Möglichkeiten, X zu tun"** passt, wenn es einen **Handelnden oder eine steuerbare
  Instanz** gibt, die zwischen Verfahren wählt: „Fünf Wege, einen RAG-Index zu aktualisieren."
- **Rahmen „N Arten, auf die X geschieht"** passt, wenn **Erscheinungsformen desselben Vorgangs** gezählt
  werden, nicht wählbare Verfahren. („Arten, auf die …" macht die modale Relation expliziter als „Arten,
  wie …".)
- **Rahmen „N Situationen / N Szenarien, in denen X geschieht"** passt, wenn die Gliederung den **Umständen**
  folgt, unter denen das Ereignis eintritt. *Situation* für reale Betriebslagen, *Szenario* für modellierte
  oder hypothetische Konstellationen — **Szenario ersetzt nicht routinemäßig jedes reale Beispiel**.
- **Rahmen „N Gründe, warum X geschieht"** passt, wenn jeder Listenpunkt eine **Kausalfrage** beantwortet.
  Er behauptet mehr als *Situation* oder *Art*.
- **Test der Wahl — nicht am grammatischen Subjekt, sondern an der semantischen Klasse der Aufzählung.**
  Frage: *Was sind die N Listenelemente?* Wählbare Verfahren → **Wege/Möglichkeiten**. Erscheinungsformen →
  **Arten/Formen**. Umstände → **Situationen**. Entworfene Konstellationen → **Szenarien**. Kausale
  Erklärungen → **Gründe/Ursachen**. Zusatzprobe: *Wer kann sich dafür entscheiden, X auf diese Weise zu
  tun?* — liefert die Frage keinen natürlichen Akteur, scheiden *Wege/Möglichkeiten* aus.
- **Präzedenz (2026-07, `part-3-production/production-failures`):** *Eight ways a working demo dies in
  production*. „Acht Wege, auf denen ein Demo stirbt" ✗ — das Demo wählt nicht zwischen acht Verfahren, den
  Produktivbetrieb nicht zu überstehen; die Metapher ist zudem stark markiert und dicht an der englischen
  Bildlichkeit. Die acht Punkte sind Betriebskonstellationen, keine Verfahren und keine sauberen
  Scheiternstypen → **„Acht Situationen, in denen ein funktionierendes Demo den Produktivbetrieb nicht
  übersteht"** ✓. Falls das Kapitel tatsächlich Ursachen analysiert, ist **„Acht Gründe, warum …"** die
  bessere Wahl. — Dieselbe Wahl fiel unabhängig im Russischen (`способов` → `сценариев`) und im Slowakischen
  (`spôsobov` → `situácií`).

### 9.2 `Why X fails`

Das Deutsche unterscheidet hier **fünf** Verben, nicht zwei. Die Wahl ist eine Sachaussage, keine Stilfrage.

- **versagen** — eine Instanz erbringt die **erwartete Funktion oder Leistung nicht**. Duden: „das
  Geforderte, Erwartete nicht tun, leisten können" und „plötzlich aufhören zu funktionieren, nicht mehr seine
  Funktion erfüllen" (*der Motor versagte, die Bremsen versagten*)
  <https://www.duden.de/rechtschreibung/versagen>. Für Software fachsprachlich belegt und **nicht** zu
  dramatisch (heise: „wenn das System versagt").
- **scheitern** — ein **zielgerichtetes Vorhaben** erreicht sein Ziel nicht. Duden: „ein angestrebtes Ziel
  … nicht erreichen"; typische Subjekte *Versuch, Plan, Projekt, Vorhaben*
  <https://www.duden.de/rechtschreibung/scheitern>. Also: *Projekt*, *Einführung*, *Migration*, *Einsatz*.
- **fehlschlagen** — ein **einzelner, abschließbarer Vorgang** endet ohne Erfolg: „Der Tool-Aufruf schlägt
  fehl.", „Die Authentifizierung schlägt fehl." Für ein dauerhaft betriebenes Gesamtsystem unidiomatisch.
- **ausfallen** — eine zuvor verfügbare Einheit ist **nicht mehr verfügbar**: „Der Datenbankserver fällt
  aus." Betrifft **Verfügbarkeit, nicht Korrektheit** — ein System kann verfügbar sein und trotzdem falsch
  antworten (genau die Unterscheidung, auf der §9.3 steht).
- **nicht funktionieren** — die neutrale Oberform; gut für eine einführende Überschrift, für die Diagnose
  meist zu unspezifisch. **kaputtgehen** ist umgangssprachlich und kein Kanonverb.
- **Test der Wahl:** *Was genau erreicht sein Ziel nicht?* Eine erwartete **Funktion** → versagen. Ein
  **Vorhaben** → scheitern. Ein **einzelner Vorgang** → fehlschlagen. Die **Verfügbarkeit** → ausfallen.
- **Präzedenz:** *Why AI systems fail in production* → **„Warum KI-Systeme im Produktivbetrieb versagen"** ✓
  (ein Mechanismus mit erwarteter Funktion). Für ein Kapitel über Organisation, Einführung und Betriebskonzept
  wäre **„Warum KI-Projekte im Produktivbetrieb scheitern"** richtig. Vergleiche mit dem Demo aus §9.1: dort
  ging es nicht um die Störung eines Mechanismus, sondern um Umstände — deshalb wechselte dort der ganze
  Rahmen.

### 9.3 `X is not Y`

- **Bloße Kopula „X ist nicht Y" / „X ist kein Y"** trägt, wenn der Satz unmittelbar eine **Klassifikation
  oder begriffliche Gleichsetzung** verneint und X und Y **gleichartig** sind: „Ein Vektorindex ist keine
  Wissensbasis."
- **„X bedeutet / heißt noch nicht Y"** — wenn X ein **Indikator, Zeichen oder beobachteter Zustand** ist,
  aus dem der Leser vorschnell Y ableiten könnte. *bedeuten* perspektiviert X als Zeichen, *heißen* liegt
  näher an der erläuternden Fachprosa.
- **„Aus X folgt nicht Y"** — wenn es ausdrücklich um eine **ungültige Inferenz** geht (X wird als Evidenz
  für Y benutzt).
- **Zwei parallele Aussagesätze** — wenn die beiden Größen **verschiedenen Bezugsebenen oder Trägern**
  angehören. Für Lehrtext oft stärker als die Negation, weil es nicht nur sagt, was falsch ist, sondern die
  richtige Ontologie liefert.
- **Test der Wahl:** (1) Bestreite ich „X gehört zur Klasse Y"? → bloße Kopula. (2) Bestreite ich „X ist ein
  Zeichen für Y"? → *bedeutet/heißt nicht*. (3) Bestreite ich „X ist ein hinreichender Grund für Y"? → *aus X
  folgt nicht*. (4) Muss ich erst erklären, worauf X und Y sich beziehen? → parallele Aussagesätze.
- **Substantivierte Adjektive.** „Grün ist nicht richtig" ist grammatisch möglich, semantisch aber instabil
  (*Grün* kann Farbe, Statusklasse oder UI-Zustand meinen). Als Überschrift trägt die Ellipse:
  **„Grün heißt nicht korrekt"** ✓. Im Fließtext wird sie aufgelöst: „Eine grüne Statusanzeige bedeutet
  nicht, dass die Antwort korrekt ist." — Zum Vergleich: im Russischen scheiterte genau dieser String ohne
  Inferenzverb („Зелёный — ещё не верный") und musste auf „ещё не значат" umgeschrieben werden; im
  Slowakischen ging er durch, **weil** das Inferenzverb dort schon stand.
- **Präzedenz:** *Uptime is not correctness* → als pointierte Überschrift **„Verfügbarkeit ist nicht
  Korrektheit"** ✓ (zwei Eigenschaften einer Art); im Fließtext aufgelöst als
  **„Verfügbarkeit ist eine Eigenschaft des Dienstes. Korrektheit ist eine Eigenschaft der Antwort."** —
  dieselbe Zweisatz-Lösung, die im Russischen und Slowakischen gewählt wurde.

---

## Figuren und Termini auf Probe (§6)

**Russische und slowakische Autorenfiguren werden nicht übernommen.** Die geschützten Figuren der anderen
Locales sind sprachgebundene Neuprägungen — russische bzw. slowakische Wörter in einem russischen bzw.
slowakischen Rahmen, keine übertragbaren Bedeutungen. Das Deutsche **übersetzt sie nicht**; es baut eigene
schlichte Prosa. **In der ersten Phase haben nackte Wörter Vorrang vor geprägten Figuren.**

**Jede geprägte deutsche Figur betritt den Kanon AUF PROBE.** Bis ein Kaltdurchgang sie beim Erstkontakt
bestätigt, steht sie mit dem Vermerk „(auf Probe)" und Prüfende behandeln sie **wie gewöhnlichen Text**. Erst
der nächste Kaltdurchgang oder Milestone-Durchgang bestätigt sie (eine naive, einsprachig deutsche Leserin
dekodiert sie beim ersten Kontakt ohne die englische Seite) oder streicht sie (dann wandert sie zu den
abgelehnten Varianten). Eine deutsche Figur wird **nicht** dadurch bestätigt, dass sie im Russischen
funktioniert — jede Sprache prüft für sich.

> **Die Probezeit gilt hier auch für TERMINI, nicht nur für Figuren.** Im Slowakischen sind mehrere heimische
> Prägungen durch **einen** Prüfer gekommen und wurden später als **semantisch falsch** gestrichen — „súbeh"
> für *race condition* ist der Musterfall: das Wort bedeutet Nebenläufigkeit, nicht den Fehler, und keine
> Glosse rettet ein falsches Wort als Namen einer Fehlerklasse. Im Deutschen ist dieselbe Falle wegen §1.0
> zwar seltener (deutlich weniger heimische Prägungen), aber gefährlicher, wenn sie zuschlägt: eine
> grammatisch tadellose deutsche Neuprägung wirkt für einen einzelnen Prüfer sofort plausibel. Deshalb gilt:
> **Ein neu geprägter deutscher Terminus ist „auf Probe", bis ein Kaltdurchgang oder ein Beleg ihn
> bestätigt — nicht, bis ein Prüfer ihn durchgewinkt hat.**

**Offene Figuren-Fragen dieses Bootstraps** (nichts davon ist gesetzt):

- **„AI delta" → „KI-Delta"** — auf Probe, siehe §3.
- **Guardrails / „Leitplanken"** — das native Bild ist bei heise belegt, aber als **Terminus** bleibt
  *Guardrails* kept-EN (§1.1); „Leitplanken" ist die **Glosse**, nicht der Kanonname. Der Singular ist OPEN.
- **„token tax" / „Token-Steuer"** — im Russischen bestätigt, im Slowakischen **ausdrücklich gestrichen**
  („daň" wurde ausgemustert). Für das Deutsche **nicht übernehmen**, bis ein eigener Kaltdurchgang darüber
  entschieden hat; bis dahin schlichte Prosa („die laufenden Kosten der Tool-Beschreibungen").
