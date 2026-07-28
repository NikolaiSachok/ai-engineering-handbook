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
- **DISPUTED** — die **deutschen Quellen selbst** widersprechen einander (etwa DIN 5008 gegen Duden) und
  keine von ihnen entscheidet die Zeile. Die Incumbent-Form wird benannt und **gehalten**; nobody flips a
  DISPUTED row without new evidence.
  **Nicht mehr DISPUTED:** „externe deutsche Norm gegen projektweite Konvention". Diese Klasse ist seit
  2026-07-28 durch die **Vorrangregel** (§ Typografie) entschieden — die deutsche Norm gewinnt, und die
  Abweichung von den Schwester-Locales wird protokolliert.
- **OPEN** — no usable attestation was found. The form is *not* settled and must not be presented as canon.

A DISPUTED or OPEN row is a correct outcome. A confidently-wrong row is not.

---

## Injektionsblock (wörtlich in jeden Render-Prompt kopieren)

> Diese acht Zeilen gehören **in den Prompt**, nicht nur in den Kanon. Sie betreffen Entscheidungen, die in
> einem Korpus voller Imperative in praktisch jedem Satz wirksam werden; wer sie erst beim Lektorat anwendet,
> repariert 67 Seiten statt sie richtig zu schreiben.

1. **Anrede: „Sie", großgeschrieben — samt „Ihr/Ihre/Ihnen".** Nie „du". Nie Wechsel innerhalb einer Seite.
   **Jede Anweisung steht im Sie-Imperativ:** „Öffnen Sie die Konsole", „Prüfen Sie den Rückgabewert" — nicht
   „Öffne die Konsole". Das ist eine andere Verbform, nicht nur ein anderes Pronomen, und sie betrifft in
   einem Anleitungskorpus fast jeden Satz. **Einzige Ausnahme: die Aufschrift AUF einem Bedienelement**
   (Schaltfläche, Link-CTA, Menüeintrag, `aria-label`) steht im **Infinitiv** — „Kurs öffnen →", „Kopieren",
   „Schließen" —, weil sie die Handlung *benennt*, statt jemanden anzusprechen (§ Stimme und Anrede).
2. **Kein „man" als Leseransprache.** „Man öffnet die Konsole" ✗ → „Öffnen Sie die Konsole." Ausnahme nur für
   echte Allgemeinaussagen über die Sprache oder das Fach (§ Stimme und Anrede).
3. **Englische Fachtermini bleiben englisch** und bekommen einen **deutschen Artikel**: *der Tool-Call, das
   Tool-Result, im Strict Mode, der Idempotency-Key*. Deutsche Neuprägungen (*Werkzeugaufruf*, *strikter
   Modus*) sind **nicht** das Ziel (§1.0).
4. **Ein Anglizismus ist hier KEIN Defekt — daraus folgt aber NICHT, dass das englische Wort gewinnt.**
   Die slowakische Regel „Anglizismus = Fehler" gilt im Deutschen ausdrücklich **nicht** (§1.0, Kasten).
   **Vierzehn Termini führt das Deutsche belegt selbst** und ein flüssig schreibendes Modell macht sie
   zuverlässig falsch: *der Endpunkt* (nicht „Endpoint"), *die Inferenz*, *der Durchsatz*, *die
   Quantisierung*, *die Instrumentierung*, *das Fehlerbudget*, *die Vektordatenbank*, *das Kontextfenster*,
   *die Wissensbasis*, *die Halluzination*, *das Geheimnis* (secret), *die Funktionstrennung*, *das
   Betriebshandbuch*, *das Prinzip der geringsten Berechtigungen*. **Die vollständige Liste mit Belegen
   steht in §1.1.g — vor dem ersten Rendern lesen.**
5. **Genus, Plural und Genitiv jedes Lehnworts stehen in §1.1.** Innerhalb einer Seite darf kein Wackeln
   auftreten (*der Cache* … *das Cache*) — das ist das lauteste Maschinenübersetzungs-Signal überhaupt.
6. **Durchkopplung:** mehrgliedrige englische Fügungen werden im deutschen Satz durchgekoppelt —
   *Machine-Learning-Modell*, *Prompt-Injection-Angriff*, *Retrieval-Qualität*. „Prompt Injection Angriff" ✗.
7. **Typografie:** „…" primär, ‚…' verschachtelt, **niemals »…«** und niemals «…»; **ß** (bundesdeutsch, kein
   Schweizer ss); Dezimalkomma; **Gedankenstrich `–` (U+2013) MIT Leerzeichen — nie `—` (U+2014)**;
   Bis-Strich kompress; **Prozentzeichen mit schmalem geschützten
   Zwischenraum** und Tausendergliederung ebenso — **10–20 %**, `28,7 %`, `1 000 000` (nicht „20%",
   nicht „1.000.000"). Das weicht bewusst von EN/RU/SK ab (§ Typografie, Vorrangregel).
   **Und: der Gedankenstrich ist der Halbgeviertstrich MIT Leerzeichen — `Teil I – RAG`,
   `Retrieval – Vertiefung`. Der Geviertstrich „—" der englischen Seite wird NICHT übernommen**
   (§ Typografie, Gedankenstrich-Zeile). Über acht deutsche Quellen gemessen: ≈ 220 × „–", 0 × „—".
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

- **Lektionen stehen im „Sie"** — „behalten Sie im Kopf", „wenn Sie ausrollen", „Sie bekommen". Nie „du",
  nie Wechsel innerhalb einer Seite. Die Höflichkeitsform und ihre Possessiva werden **immer
  großgeschrieben**: *Sie, Ihnen, Ihr, Ihre*.

  **Die Anrede entscheidet mit über die Verbform, nicht nur über das Pronomen.** Jede Anweisung steht im
  **Sie-Imperativ**: „Öffnen Sie die Konsole", „Prüfen Sie den Rückgabewert", „Geben Sie eine Meldung
  zurück" — nicht „Öffne …", „Prüfe …", „Gib …". Weil dieser Korpus überwiegend aus Anweisungen besteht,
  ist das die **breiteste** Fläche dieser Entscheidung; ein einziger stehengebliebener du-Imperativ mitten
  in einer Sie-Seite ist derselbe Registerbruch wie ein wackelndes Genus (§1.1).

  **Geltungsbereich.** Die Regel gilt für **Korpusprosa** — Lektionen, Glossar, Blockstrings, Kartenlabels,
  UI-Strings. Redaktionsdokumente wie dieses hier sprechen die **schreibende Instanz** an, nicht die
  lesende; ihre Imperative („Vermeide scharfe Ausschläge", „Trage eine Zeile nach") sind **keine**
  Korpusprosa und werden nicht mitgezogen.

  > **STATUS: SETTLED — Eigentümerentscheid vom 2026-07-28, auf der Beleglage.** Diese Zeile stand bis dahin
  > als `du` und als DISPUTED, *gegen* die eigene Beleglage. Die Beleglage hat entschieden; die Zeile ist
  > jetzt die **belegte** Wahl, nicht mehr die trotzige.
  >
  > **Jede öffentlich lesbare deutsche Fachbuchquelle, die geprüft wurde, verwendet
  > `Sie`:** Rheinwerk-Openbook („Vor dem Lesen sollten **Sie** sich überlegen, welche Fragen das Kapitel
  > beantworten soll", <https://openbook.rheinwerk-verlag.de/javainsel/00_002.html>); zwei dpunkt-Leseproben
  > (76× *Sie/Ihnen* gegen 1× *du*; 35× *Sie* gegen 0× *du*); der GNOME-Übersetzungsleitfaden („Der Anwender
  > wird … **grundsätzlich in der Höflichkeitsform** angesprochen", <https://wiki.gnome.org/de/UebersetzungsRichtlinien>);
  > der Microsoft-Lokalisierungsleitfaden, der `du` ausdrücklich Leserinnen und Lesern **unter 18** vorbehält.
  > Der tekom-Fachartikel bestätigt zwar einen `du`-Trend, rät aber genau in diese Richtung: „Mit dem Sie
  > macht man im Zweifelsfall nichts Grundsätzliches verkehrt … Ein falsch verwendetes Du kann aber durchaus
  > zu Irritationen führen." (<https://technischekommunikation.info/fachartikel/sprache/gerne-per-du-1272/>)
  >
  > **Der Befund, der die Gegenrechnung zusammenbrechen ließ:** die drei angeblich unabhängigen Kronzeugen
  > für ein `du` sind **eine** Stilfamilie, nicht drei Datenpunkte — dpunkt betreut seit 2015 das
  > deutschsprachige O'Reilly-Programm und gehört zu Heise Medien
  > (<https://www.heise.de/news/dpunkt-verlag-uebernimmt-deutschsprachiges-O-Reilly-Programm-2622415.html>).
  > Damit stand einer einhelligen Sie-Beleglage kein zweiter Strang gegenüber, sondern derselbe Strang
  > dreimal gezählt.
  >
  > **Was das SETTLED hier bedeutet — und was nicht.** Die Belege sind **Verlagsusus**, keine Duden- oder
  > Regelwerksregel; eine öffentlich lesbare **Buch**-Autorenrichtlinie mit Anrederegel existiert bei keinem
  > der Verlage (das bleibt OPEN). SETTLED steht deshalb dafür, dass die Quellen einander **nicht
  > widersprechen** und die Entscheidung getroffen ist — nicht dafür, dass ein Normgeber sie vorschreibt.
  >
  > **Der tragende Grund ist die fehlende Kontrollinstanz.** Der deutschen Locale fehlt der native
  > Korrekturleser; der Eigentümer liest Russisch und Slowakisch, sein Deutsch ist ~A1. Wenn niemand hören
  > kann, ob ein unkonventionelles Register als *informell und modern* oder als *fremd* ankommt, gewinnt der
  > belegte Verlagsusus gegen jede Erwägung von Korpussymmetrie. Ein deutscher Entwickler erwartet in einem
  > Fachhandbuch das `Sie`.
  >
  > **Vermerkt wird ab jetzt die Divergenz zu RU und SK, nicht die zur deutschen Fachprosa.** Russisch führt
  > «ты», Slowakisch „ty" — das Deutsche weicht davon **bewusst** ab. Die Gleichlage der Anrede über alle
  > Locales war das Argument für `du`; sie ist eine Konsistenzerwägung und wiegt weniger als der attestierte
  > Usus der Zielsprache. Wer diese Divergenz später „glattzieht", macht die Entscheidung rückgängig — sie
  > ist keine Unachtsamkeit. *(Dieselbe Sorte Divergenz wie bei §3 „KI statt AI": das Deutsche folgt seiner
  > eigenen belegten Praxis, wo RU und SK anders verfahren.)*
  >
  > **Wiedereröffnungsbedingung.** Eine bindende Hausrichtlinie eines Verlags, die `du` vorschreibt; oder ein
  > nativer Leserbefund (Gate 7, `de-pilot-naturalness-check`), der das `Sie` für dieses Publikum als
  > distanziert markiert. **Kein Flip ohne Eigentümerentscheid** — in beide Richtungen.

  **Ausnahme innerhalb der UI-Strings: Bedienelementbeschriftungen stehen im INFINITIV.** Die Grenze läuft
  nicht zwischen Prosa und UI, sondern **innerhalb** der UI-Strings — zwischen zwei Textsorten:

  | Textsorte | Form | Beispiele |
  |---|---|---|
  | **Handlungsanweisung** — ein Satz, der die lesende Person anspricht (Fließtext, Fehlermeldung, Hinweis, leerer Zustand) | **Sie-Imperativ** | „Öffnen Sie die Konsole.", „Bitte melden Sie sich an, um fortzufahren.", „Prüfen Sie den Rückgabewert." |
  | **Bedienelementbeschriftung** — die Aufschrift **auf** einem Bedienelement: Schaltfläche, Link-CTA, Menüeintrag, Tab, Karteikartenreiter, `aria-label` | **Infinitiv** | „Kurs öffnen →", „Lehrplan ansehen →", „Kopieren", „Schließen", „Mehr lesen" |

  **Zwei Unterfälle, die keine sind.** *Nacktes Verb* („Speichern") und *Verb mit Objekt* („Kurs öffnen")
  sind dieselbe Form — keine geprüfte Quelle unterscheidet sie, und beide stehen überall nebeneinander
  (KERN: „Speichern" und „Modal schließen"). Und ein **navigierender** CTA darf statt des Infinitivs auch
  eine **bloße Präpositionalphrase ganz ohne Verb** tragen: „Zum Angebot", „Zum Girokonto", „In den
  Warenkorb" — auf bahn.de, telekom.de, dkb.de, heise.de und rheinwerk-verlag.de gleichermaßen belegt. Die
  Wahl steht also zwischen **Infinitiv und Präpositionalphrase**; ein Imperativ ist in keinem der beiden
  Unterfälle vorgesehen.

  **Der Grund ist kein Höflichkeitsgrund, sondern ein grammatischer.** Eine Beschriftung ist **an niemanden
  gerichtet** — sie **benennt** die Handlung, die das Element auslöst, so wie eine Überschrift ihren
  Abschnitt benennt. Der Sie-Imperativ macht aus dem Namen eine Aufforderung und damit aus dem Knopf einen
  Satz („Öffnen Sie den Kurs →" auf einer anklickbaren Karte). Die Anrede wird dadurch **nicht** aufgeweicht:
  sobald ein UI-String ein Satz an die lesende Person ist, gilt lückenlos der Sie-Imperativ.

  > **STATUS: SETTLED.** Der stärkste Beleg ist **projektintern und liegt bereits im Build**: die
  > deutschen Docusaurus-Theme-Strings (`@docusaurus/theme-translations/locales/de`), aus denen dieses
  > Projekt **74 von 85 `code.json`-Schlüsseln** automatisch befüllt, treffen **in derselben Datei, von
  > denselben deutschen Autoren** genau diese Unterscheidung:
  >
  > - Bedienelemente im **Infinitiv** — `theme.CodeBlock.copy` = „**Kopieren**",
  >   `theme.CodeBlock.copyButtonAriaLabel` = „**In die Zwischenablage kopieren**",
  >   `theme.AnnouncementBar.closeButtonAriaLabel` = „**Schließen**",
  >   `theme.BackToTopButton.buttonAriaLabel` = „**Zurück nach oben scrollen**",
  >   `theme.ErrorPageContent.tryAgain` = „**Nochmal versuchen**", `theme.blog.post.readMore` = „**Mehr lesen**".
  > - Prosa-Sätze im **Sie-Imperativ** — `theme.NotFound.p2` = „**Bitte kontaktieren Sie** den Besitzer der
  >   Seite … und **teilen Sie** ihm mit, dass der Link nicht mehr funktioniert."; `theme.NotFound.p1` =
  >   „Wir konnten nicht finden, wonach **Sie** gesucht haben."
  >
  > Das ist die entscheidende Kombination: **dieselben Autoren, dieselbe Datei, Sie in der Prosa und
  > Infinitiv auf den Knöpfen.** Die Verbform der Beschriftung ist also **unabhängig** von der Anrede des
  > Fließtextes. Und `theme.blog.post.readMore` („Mehr lesen") ist exakt dieselbe Textsorte wie
  > `landing.cta.open` — stünde daneben „Öffnen Sie den Kurs →", wäre der Registerbruch **auf einer
  > Bildschirmseite sichtbar**.
  >
  > ⚠️ **Einschränkung zu diesem Beleg — das `de`-Theme-Paket ist ein Zeuge für das REGISTER, nicht für die
  > KORREKTHEIT.** Eine Prüfung des ausgelieferten Pakets beim Bau von #279 ergab: **16 der 74**
  > automatisch befüllten Schlüssel kommen unübersetzt auf Englisch zurück, drei weitere sind fehlerhaft —
  > darunter „**Dokumentation Seiten**" (ein Deppenleerzeichen, also genau der Fehler, den §1.3.3 verbietet)
  > und „**Ein doc getaggt**" (unübersetztes kleingeschriebenes Substantiv plus Denglisch-Partizip).
  > **Das entwertet die Belegkraft oben nicht** — die zitierten Schlüssel („Kopieren", „Schließen",
  > „Mehr lesen", „Bitte kontaktieren Sie …") sind einwandfreies Deutsch, und die Beobachtung ist ohnehin
  > eine über die **Wahl der Verbform**, nicht über sprachliche Fehlerfreiheit. Aber: **das Paket darf nie
  > als Autorität für eine Schreibung zitiert werden**, nur als Zeugnis dafür, welche Form deutsche Autoren
  > in dieser Textsorte greifen. Wer eine Schreibung daraus übernimmt, importiert mit einiger
  > Wahrscheinlichkeit einen Defekt. *(Befund: `de-ui-strings`, #279/#310.)*
  >
  > **Der Satz, der die Regel ausspricht** (Sheeren Münch-Schmitt, Lokalisierungsfachfrau,
  > <https://lingdrafts.hypotheses.org/2190>): „Übrigens: **Schaltflächen enthalten praktisch immer eine
  > Handlungsaufforderung. Daher werden sie üblicherweise nicht substantivisch, sondern verbal ausgedrückt –
  > aber nicht im Imperativ, sondern im Infinitiv.**" Entscheidend ist die Begründungsrichtung: **gerade
  > weil** die Beschriftung eine Handlungsaufforderung ist, steht sie trotzdem **nicht** im Imperativ. Das
  > „nicht im Imperativ" ist unqualifiziert — es schließt den Imperativ als solchen aus, nicht nur den
  > du-Imperativ.
  >
  > **Microsoft-Lokalisierungsleitfaden de-DE** (offiziell, 77 S.): enthält **keine** ausgesprochene Regel,
  > **zeigt** die Trennung aber in den eigenen normativen Beispielen, in denen `(+)` die korrekte deutsche
  > Zielform markiert — „(+) **Klicken Sie** im Menü Datei auf **Öffnen**." und „**Klicken Sie auf**
  > ‚Abbrechen', um zu Ihrer Arbeit zurückzugehen …": Sie-Imperativ in der Prosa, Infinitiv auf dem
  > Bedienelement, in einem Satz.
  >
  > **Mozilla-l10n-Styleguide DE** (<https://mozilla-l10n.github.io/styleguides/de/>) — „Stattdessen wird der
  > **Infinitiv** verwendet" (Beispiel „XYZ anzeigen statt Zeige XYZ"); und, für diese Frage wichtiger als
  > die du-Hälfte: „Des Weiteren sollte ein ‚Sie' **grundsätzlich aber auch gemieden** und nur in Fällen
  > verwendet werden, **in denen es einer direkten Ansprache des Nutzers bedarf**." Eine Knopfbeschriftung
  > ist kein solcher Fall.
  >
  > **Das Argument, das die Gegenhypothese ausschließt — die Paarung hält in BEIDE Richtungen.** Würde die
  > Beschriftung der Anrede folgen, müssten du-Seiten „Speichere" und „Melde dich an" zeigen und Sie-Seiten
  > „Buchen Sie" und „Erfahren Sie mehr". **Beides kommt in der geprüften Stichprobe kein einziges Mal vor:**
  > - *Sie in der Prosa → Infinitiv auf den Knöpfen:* Microsoft de-DE, bahn.de („Profitieren Sie von …" neben
  >   „Deutschland-Ticket buchen"), telekom.de, heise.de („Geben Sie uns Bescheid." neben „Jetzt anmelden").
  > - *du in der Prosa → Infinitiv auf den Knöpfen:* der KERN-UX-Standard („**Nutze** Icons in Buttons nur
  >   dann …", „**Achte** …", „**Verwende** …") beschriftet seine eigenen Knöpfe „Speichern", „Abbrechen",
  >   „Bearbeiten", „Modal schließen"; ebenso dkb.de („**Nutze** den Sommer …" neben „Zum Girokonto").
  > - *beide Anreden auf einer Seite → dieselben Infinitive:* rheinwerk-verlag.de.
  >
  > Über sechs deutschsprachige Seiten hinweg: **Sie-Imperativ als Knopfbeschriftung = 0, du-Imperativ als
  > Knopfbeschriftung = 0.** Der Infinitiv ist **anredeneutral** — er benennt die Handlung, statt jemanden
  > anzusprechen, trägt deshalb gar keine Höflichkeitsmarkierung und überlebt jedes umgebende Register
  > unverändert. Genau das macht die Regel sicher kodifizierbar.
  >
  > **Was hier NICHT als Beleg zählt — dreimal.**
  > 1. Die Schwester-Locales schreiben ihre CTAs zwar ebenfalls im Infinitiv („Открыть курс →",
  >    „Otvoriť kurz →"), aber beide führen «ты»/„ty" — dort war der Infinitiv **keine**
  >    Höflichkeitsentscheidung und trägt für diese Frage nichts bei.
  > 2. Der **KERN-UX-Standard schreibt den Infinitiv nicht vor** — eine Prüfung der Seite ergab nur die
  >    Forderung nach knappen, eindeutigen Handlungslabels. Er zählt hier **als Usus, nicht als Vorschrift**;
  >    eine Berufung auf ihn als Regelquelle wäre eine Überdehnung.
  > 3. Die deutsche Microsoft-Learn-Seite zum *Windows Admin Center UI style guide* passt inhaltlich perfekt,
  >    trägt aber `ms.translationtype: MT` — maschinell übersetzt. Aus „Create/Delete/Add" entstehen
  >    mechanisch deutsche Infinitive; der Beleg wäre zirkulär. **Nach der MT-Signal-Prüfung verworfen**
  >    (§ Sprachpaar und Rolle der Locale).
  >
  > **Restschwäche, ehrlich benannt.** Es wurde **kein** Unternehmensstandard gefunden, der wörtlich sagt
  > „nie den Sie-Imperativ auf einer Schaltfläche"; die Mozilla-Regel nennt ausdrücklich nur den
  > du-Imperativ, und der unqualifizierte Satz stammt aus einem Fachblog, nicht aus einer Firmennorm. Das
  > Verbot ruht also auf der **Konvergenz** aus Münch-Schmitt, den Microsoft-Beispielen und dem
  > ausnahmslosen Befund über sechs Seiten. Ungeprüft blieben SAP Fiori DE, der Apple-Styleguide DE und der
  > Styleguide der Bundesregierung. Das ist eine Lücke in der **Zitierbarkeit**, kein Widerspruch in der
  > Beleglage: **nichts Geprüftes weist in die andere Richtung.**
  >
  > **Verhältnis zur Vorrangregel (§ Typografie).** Dies ist **kein** Fall der Vorrangregel: hier kollidiert
  > keine projektweite Konvention mit einer deutschen Norm. Der Geltungsbereich hatte die beiden Textsorten
  > schlicht nicht unterschieden, weil „UI-Strings" als **ein** Eimer notiert war. Diese Zeile teilt den
  > Eimer; die Anrede-Entscheidung vom 2026-07-28 bleibt unangetastet.

- **Das unpersönliche „man" ist im deutschen Doku-Reflex der Default — und im Korpus als Leseransprache
  verboten.** Es ist die dritte Anziehungskraft, die das Russische und das Slowakische gar nicht kennen: Es
  ist überhaupt keine Anrede — weder „Sie" noch „du" —, und ein Absatz driftet lautlos hinein und wieder
  heraus. Diese Drift ist der eigentliche Defekt, nicht das Wort. **Der Wechsel auf „Sie" macht diese Falle
  nicht kleiner:** „man" liegt registerlich näher an der Höflichkeitsform als am „du" und wirkt deshalb
  unauffälliger, während es dieselbe Uneindeutigkeit über den Handelnden erzeugt.

  **Verboten** ist „man" überall dort, wo **die lesende Person die handelnde ist** — in Anweisungen,
  Empfehlungen, Arbeitsschritten, Warnungen:

  | ✗ „man" | ✓ Neubau | Funktion |
  |---|---|---|
  | Man öffnet die Konsole. | Öffnen Sie die Konsole. | konkrete Leserhandlung → Sie-Imperativ |
  | Man prüft den Rückgabewert. | Prüfen Sie den Rückgabewert. | Anweisung → Sie-Imperativ |
  | Man speichert die Daten im Index. | Die Daten werden im Index gespeichert. | Vorgang, Handelnder unwichtig → Passiv |
  | Man kann drei Fälle unterscheiden. | Es lassen sich drei Fälle unterscheiden. | unpersönliche Möglichkeit |
  | Beim Reranking bewertet man neu. | Beim Reranking werden die Treffer neu bewertet. | echte Prozessbeschreibung |

  **Erlaubt — und nur hier** — ist „man" für **echte Allgemeinaussagen über die Sprache, das Fach oder eine
  Definition**, wo die Leseranrede sachlich falsch wäre: „Unter einem Agenten versteht man hier …", „Im
  Deutschen setzt man in diesem Fall einen Bindestrich."

  > **STATUS: HOUSE — ausdrücklich eine Redaktionsregel, KEINE deutsche Norm.** Die Recherche fand **keine
  > einzige** deutsche Quelle, die „man" in Anleitungs- oder Fachprosa untersagt — die englische Intuition,
  > „one" sei schlechter Stil, hat im Deutschen kein Gegenstück. Es gibt sogar das **Gegenteil**: das
  > Arbeitshandbuch „Bürgernahe Verwaltungssprache" des Bundesverwaltungsamts **empfiehlt** „man" als Mittel
  > gegen das Passiv — „Verwenden Sie dazu unbestimmte Subjekte (z. B. **man**, jemand, wer, es)"
  > (<https://www.bva.bund.de/SharedDocs/Downloads/DE/Oeffentlichkeitsarbeit/Buergernahe_Verwaltungssprache_BBB.pdf>);
  > und heise verwendet es unmarkiert („Werte definiert **man** mit def.").
  >
  > Was der Beleglage standhält, ist die **engere** Regel, und genau die gilt hier: **kein „man" für einen
  > Schritt, den die lesende Person ausführen soll** — Handlungsschritte stehen im **Sie-Imperativ**
  > („Prüfen Sie …", „Öffnen Sie …"), damit der Handelnde eindeutig ist. Der Rest ist Registerdisziplin:
  > „man" driftet aus der „Sie"-Ansprache heraus und wieder hinein, und diese Drift liest sich als
  > Maschinenausgabe.
  >
  > Der unabhängige Register-Gegencheck (ein zweites Modell als nativer Registerrichter) lehnte ein
  > ausnahmsloses Verbot mit demselben Grund ab: die Leseranrede und „man" sind semantisch nicht
  > austauschbar (Leseransprache vs. generische Referenz); ein Totalverbot erzwingt unidiomatisches Passiv,
  > überladene Substantivierungen oder eine Anrede, die der lesenden Person Handlungen unterstellt, die sie
  > nicht ausführt. **Die Regel lautet deshalb: „man" ist ein Defekt, außer es lässt sich mit dem
  > Definitionsrahmen begründen** — die Beweislast liegt beim „man", nicht bei der Anrede. *(Der Gegencheck
  > lief gegen die damalige `du`-Fassung; sein Argument ist von der Wahl der Anredeform unabhängig und
  > trägt unter „Sie" unverändert.)*

- **Autoren-„wir" nur dosiert** und nur als Rahmen des gemeinsamen Wegs („Schritt für Schritt geben wir dem
  Modell mehr Freiheit") sowie für Vorbehalte zum Umfang des Materials; **nie in Anweisungen an den Leser**.

- **Drucklatte — Register mit benannten Vorbildern.** Ziel ist Prosa, die eine erfahrene deutschsprachige
  Entwicklerin als *von einer Kollegin geschrieben* akzeptiert: das Register von **dpunkt, Rheinwerk,
  O'Reilly Deutschland, heise/iX/c't** — sachlich, dicht, ohne Aufgeregtheit, mit Fachwörtern statt
  Umschreibungen. **Ausdrücklich NICHT: Enterprise-Marketing-Deutsch** („ganzheitliche Lösungen", „nahtlose
  Integration", „zukunftssicher", „Mehrwert schaffen", Nominalstil, werbender Anpreisungston —
  „Entdecken Sie jetzt die Vorteile …"). **Der Defekt ist der Werbeduktus, nicht die Höflichkeitsform:** das
  „Sie" ist genau die Anrede, die dpunkt, Rheinwerk und O'Reilly Deutschland selbst verwenden (§ Stimme und
  Anrede), und darf deshalb **nie** als Marketingsignal geflaggt werden. Genau in
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
ständig vor (*Nutzer, Entwickler, Reviewer, Autor, Angreifer, Betreiber, Prüfer*), und sie müssen **einmal,
bewusst** entschieden werden. Ein unentschiedenes Korpus wackelt, und deutsche Leser lesen Wackeln als
Maschinenausgabe.

> **Korrigierte Begründung (2026-07-28, mit dem Anredewechsel).** Eine frühere Fassung dieses Abschnitts
> stützte sich darauf, dass die „du"-Anrede „den größten Teil davon konstruktiv abräumt". **Diese Begründung
> ist hinfällig** und wird hier nicht stillschweigend ersetzt, sondern benannt: die Höflichkeitsform räumt
> Agensnomen **nicht** ab, wie es eine Ansprache in der zweiten Person Singular für einen Teil der Fälle tat.
> Sie war ohnehin nur dort richtig, wo der Satz die **lesende Person** meinte — nie für *der Betreiber*, *der
> Angreifer*, *der Prüfer*, *der Autor*, die den Korpus tatsächlich füllen und über die in der dritten Person
> gesprochen wird. **Die Leiter unten steht deshalb auf eigenen Füßen** (vier unabhängige Belegstränge, siehe
> unten), und die **vier Fälle, in denen die Umformulierung scheitert, tragen jetzt mehr Gewicht, nicht
> weniger** — sie sind häufiger, weil die Anrede weniger wegnimmt.

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
jede schreibende Instanz neu improvisiert.** Sie sind **die tragenden Fälle dieses Abschnitts**: seit die
Anrede „Sie" lautet, nimmt sie der Leiter nichts mehr ab, und diese vier treten entsprechend häufiger auf.

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

> ### Vorrangregel — bei Kollision gewinnt die deutsche Norm
>
> **STATUS: SETTLED — Eigentümerentscheidung 2026-07-28.** Sie gilt für die ganze Locale, nicht nur für die
> zwei Zeilen, an denen sie gefunden wurde.
>
> **Die Regel.** Wo eine **projektweite Konvention** (aus EN/RU/SK übernommen) mit einer **belegten
> deutschen Norm** zusammenstößt, **gewinnt die deutsche Norm** — und die Abweichung von den
> Schwester-Locales wird in der betroffenen Zeile **ausdrücklich protokolliert**, statt stillschweigend
> absorbiert zu werden.
>
> **Grund — es ist derselbe Grund wie bei der Anrede.** Am 2026-07-28 hat der Eigentümer die Anrede genau so
> entschieden: „du" war die Gleichlage mit «ты» und „ty", „Sie" ist das, was das deutsche Fachverlagswesen
> tatsächlich belegt. Er hat die belegte Norm über die Locale-Symmetrie gestellt — **weil es in diesem Projekt
> keinen deutschen Muttersprachler gibt, der hören könnte, ob eine unkonventionelle Wahl als bewusst oder als
> fremd ankommt** (§ Sprachpaar und Rolle der Locale: „für das Deutsche bürgen nur die Gates"). Eine
> Konvention, die für das Russische und das Slowakische richtig ist, wird durch den Import ins Deutsche nicht
> richtig — sie wird nur **unhörbar** falsch. Enges Prozentzeichen ist dieselbe Frage in anderer Gestalt und
> bekommt dieselbe Antwort.
>
> **Was dabei aufgegeben wird — ehrlich benannt.** Die **visuelle Gleichlage über die Locales** ist ein
> echter Wert und wird hier wissentlich eingetauscht, nicht übersehen: dieselbe Zahl sieht auf der deutschen
> Seite ab jetzt anders aus als auf der englischen, russischen und slowakischen, und ein späterer
> Konsistenzlauf **wird** versuchen, das zu „reparieren". Der Gegenwert: auf dem Bildschirm ist immer nur
> **eine** Locale sichtbar — die Norm dagegen ist für jeden deutschen Leser in **jedem** Satz sichtbar. Wer
> eine solche Zeile später zurückdreht, dreht eine Eigentümerentscheidung zurück und braucht dafür einen
> Beleg, nicht ein Konsistenzgefühl.
>
> **Was die Regel *nicht* tut.** Sie entscheidet keine Zeile, in der sich die **deutschen Quellen
> untereinander** widersprechen (DIN 5008 gegen Duden, Norm gegen Buchsatz). Solche Zeilen bleiben DISPUTED
> oder werden mit Angabe des Registers entschieden — und der unterlegene Beleg bleibt im Text stehen.

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
  **Gegen die Vorrangregel geprüft (2026-07-28): keine Kollision.** Die Gleichlage mit dem Slowakischen ist
  hier **nicht** der einzige Träger — „…" ist unabhängig davon die Form, die das Amtliche Regelwerk 2024 in
  seinen eigenen Beispielen setzt (§ 79, siehe Zeile oben). Es wird also **keine** deutsche Norm gegen eine
  Projektkonvention eingetauscht; die Konvention und die primär belegte Form fallen zusammen, und »…« bleibt
  eine legitime, aber nicht gewählte Alternative. Nur deshalb darf diese Zeile HOUSE bleiben.
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

- **Tausendergliederung: schmaler geschützter Zwischenraum (U+202F)**, nicht der Punkt — `10 000`,
  `1 000 000`; und **vierstellige Zahlen werden nicht gegliedert** (`5423`, nicht „5 423").
  **STATUS: SETTLED (2026-07-28, Vorrangregel oben) — vorher DISPUTED.** Hier sagen **DIN und Duden
  dasselbe**, es gibt also gar keinen deutschen Quellenstreit:
  - DIN 5008:2020, Abschnitt 11.2: „**Zahlen mit mehr als drei Stellen links oder rechts des Kommas werden
    mithilfe eines ganzen Leerschritts – vom Komma ausgehend – in dreistellige Gruppen gegliedert.**"
    Beispiele der Norm: `7 654 321,08 CHF`, `0,373 18 g`
    (<https://journalismusausbildung.de/din-5008-zahlen/>).
  - Duden: „Ganze Zahlen mit 5 oder mehr Ziffern werden von der Endziffer aus **durch Zwischenräume** in
    dreistellige Gruppen gegliedert" — `34 500`, `600 000`, `3 134 512`
    (<https://www.duden.de/sprachwissen/rechtschreibregeln/zahlen-und-ziffern>).
  **Vierstellige Zahlen:** DIN stellt frei („Bei vierstelligen Zahlen ist neben der Schreibung mit
  Zwischenraum bzw. ganzem Leerschritt auch die ohne möglich"), Duden gliedert erst ab **fünf** Ziffern. Der
  Korpus nimmt die ungegliederte Form — sie ist unter **beiden** Quellen zulässig.
  **Einzige Ausnahme, und sie kommt aus der Norm selbst — Geldbeträge:** „Bei Geldbeträgen können aus
  Sicherheitsgründen auch Punkte zur Gliederung verwendet werden" (`5.340 EUR`, `7.893.432 EUR`). Nur dort
  ist der Punkt richtig.
  **Was aufgegeben wird, benannt:** die **Drucklatte setzt durchgehend den Punkt** — dpunkt/O'Reilly `4.319`,
  Rheinwerk `12.000`, heise `100.000`, und die de-DE-Locale aller Systeme tut es auch. Das ist verbreitete
  deutsche **Praxis**, aber keine Norm; und im Korpus kollidiert sie zusätzlich mit dem englischen
  Dezimalpunkt, der in Code und Zahlenbeispielen auf derselben Seite steht. Die Norm entscheidet, der
  Praxis-Dissens bleibt hier stehen.
  **Zur Breite des Zwischenraums — ehrlich, weil die Norm hier wörtlich etwas anderes sagt:** DIN schreibt
  für die Tausendergliederung einen **ganzen** Leerschritt vor (Schreibmaschinen- und
  Textverarbeitungskontext); im Satz sähe der wie eine Wortlücke aus. Der Korpus setzt deshalb die
  **typografische Realisierung** derselben Gliederungsregel: schmaler **geschützter** Zwischenraum U+202F.
  Fällt der aus, ist U+00A0 der Rückfall — **nie** ein normales Leerzeichen (Umbruchrisiko), **nie** der
  Punkt außerhalb von Geldbeträgen, **nie** ungegliedert (`137813` ist unter beiden Quellen falsch).
  **Wiederaufnahme:** eine bindende Verlagshausregel; der Renderer gibt U+202F unzuverlässig aus; oder die
  Zahl steht als Code, Datenbankwert oder API-Literal — dann bleibt die Quellform unverändert.

- **Prozentzeichen mit schmalem geschützten Zwischenraum: `20 %`, `10–20 %`, `28,7 %`.**
  **STATUS: SETTLED (2026-07-28, Vorrangregel oben) — vorher DISPUTED mit „eng" als Incumbent.**
  > **Entscheidungsgeschichte — diese Zeile wurde umgedreht, und das Protokoll sagt es.**
  > Ursprünglich **eng (`20%`)**, auf Korpuskonsistenz mit EN/RU/SK; der Kanon nannte das selbst „den
  > auffälligsten bewussten Normbruch des deutschen Kanons". Die Zeile stand außerdem **im Widerspruch zum
  > Playbook** (`de-locale-playbook.md` §7.5), das schon `20 %` festgelegt hatte — welches Dokument gewann,
  > hing davon ab, welches ein Renderer zuerst las. **Umgedreht auf `20 %` durch den Eigentümer am
  > 2026-07-28**, auf genau den Beleg, den die eng-Zeile bereits gegen sich selbst notiert hatte. Ein Kanon,
  > der seine eigenen Umkehrungen stillschweigend überschreibt, ist der SK-Fáza-26-Fehlermodus; deshalb steht
  > die alte Entscheidung hier lesbar über der neuen.
  **Beleglage — die deutschen Quellen sind sich hier einig, sie spalten sich nicht:**
  - DIN 5008:2020, Abschnitt 10.7 („Prozent- und Promillezeichen"): „**Prozent- und Promillezeichen sind
    durch einen Leerschritt von der zugehörigen Zahl zu trennen.**" Für Textverarbeitungssysteme schreibt die
    Norm ausdrücklich „**einen kleineren Zwischenraum (Festabstand)**" vor — das ist genau U+202F — und:
    „Die Trennung von Zahl und Prozent- bzw. Promillezeichen am Zeilenende sollte vermieden werden"
    (<https://journalismusausbildung.de/din-5008-prozent-und-promillezeichen/>).
  - Duden (Rechtschreibung, 24. Aufl.): Wert und Einheit getrennt — „5 Prozent oder 5 %".
  - typolexikon: „Zwischen Zahl und Prozentzeichen wird **immer** ein Leerraumzeichen gesetzt"
    (<https://www.typolexikon.de/prozentzeichen/>).
  - korrekturen.de: „**Anders als teilweise im Englischen** werden im Deutschen Maßeinheiten und Symbole
    stets mit Abstand vor oder hinter die Zahl gestellt: € 25, **80 %**, 3 t Gewicht."
  Die enge Schreibung ist ein **Import aus der englischen Typografie** — die letzte Quelle sagt das
  wörtlich.
  **Ableitungen bleiben eng** (das ist keine Ausnahme *vom* Beleg, sondern steht in ihm): `20%ig`
  (Duden D 30.1 führt `75%ig`), alternativ ausgeschrieben `20-prozentig`; und `die 5-%-Klausel` (das
  Amtliche Regelwerk 2024 führt `5-%-Klausel` unter „fünf"). DIN: „Das Leerzeichen entfällt bei
  Ableitungen — *Der 8%ige Umsatzrückgang …*"
  **Abweichung von den Schwester-Locales, protokolliert:** EN, RU und SK schreiben im gesamten Korpus eng,
  und die slowakische Locale hat 2026-07 ausdrücklich von „geschütztes Leerzeichen" auf „eng" umgestellt
  (`canon/sk/_language.md`). **Diese Konvention trägt nicht ins Deutsche.** Eine typografische Konvention ist
  eine Eigenschaft der **Locale**, nicht des Korpus. Wer die deutsche Seite später „auf eng vereinheitlicht",
  dreht eine Eigentümerentscheidung zurück.
  **Wiederaufnahme:** nur für Code, UI-Strings und wörtlich zitierte fremdsprachige Passagen — dort bleibt die
  Quellform stehen — sowie für echte Ableitungen und Zusammensetzungen. **Gleichlage mit den anderen Locales
  ist ausdrücklich kein Wiederaufnahmegrund.**

- **Bereiche mit Bis-Strich (Halbgeviert, en dash), ohne Leerzeichen**: `10–20 %`, `9–11 Uhr`.
  **STATUS: SETTLED nach Register (2026-07-28) — vorher DISPUTED.** Hier spalten sich die deutschen Quellen
  **wirklich**, und beide Seiten stehen deshalb im Protokoll:
  - **Kompress:** Duden setzt vor und nach dem Bis-Zeichen kein Leerzeichen — „Vor und nach dem bis-Zeichen
    steht gemäß zum Beispiel Duden **kein Leerzeichen**: 24.–25. Oktober"
    (<https://blog.leo.org/2020/10/23/das-bis-zeichen-und-seine-laenge/>); korrekturen.de setzt es ebenso
    („bis-Zeichen (»Öffnungszeiten 9–11 Uhr«)"); die Gesellschaft für deutsche Sprache bestätigt die Form
    ausdrücklich als zulässig: „Der Bis-Strich **darf auch kompress gesetzt werden**, also ohne Leerzeichen"
    (<https://gfds.de/strichlaengen/>). Auch der klassische Buchsatz und DIN 5008 Anhang F (der Anhang für
    typografisch gehobene Publikationen) setzen kompress.
  - **Mit Leerzeichen:** der **normative Teil** von DIN 5008 („24. – 25. Oktober", „Montag – Donnerstag").
  **Der Kanon nimmt kompress**, und zwar **nicht** wegen der Gleichlage mit den anderen Locales, sondern weil
  DIN 5008 die Geschäftskorrespondenz und Textverarbeitung regelt, während dies ein **gesetztes Buch** ist —
  genau der Fall, für den Anhang F geschrieben wurde, und der Fall, den Duden und korrekturen.de beschreiben.
  Dass es zufällig auch die Form der Schwester-Locales ist, ist ein Nebeneffekt, kein Grund; die Zeile stünde
  genauso da, wenn RU und SK es anders machten. **Die Vorrangregel greift hier nicht** — sie entscheidet nur
  Norm gegen Projektkonvention, nicht deutsche Quelle gegen deutsche Quelle.
  **Harte Unterregel, nicht optional:** Wort und Strich werden nie gemischt — „von 8 bis 20 Uhr" ✓,
  „von 8–20 Uhr" ✗.
  **Wiederaufnahme:** eine bindende Verlagshausregel; oder der Korpus wechselt in ein
  Korrespondenz-/Formularregister, für das DIN 5008 normativ ist.

- **Gedankenstrich: Halbgeviertstrich `–` (U+2013) MIT Leerzeichen auf beiden Seiten.**
  „Teil I – RAG", „Teil III – Produktivbetrieb und LLMOps", „Serving – FastAPI und Docker".
  **Der Geviertstrich `—` (U+2014) ist im Deutschen falsch** — er ist die englische und spanische Konvention
  und wird hier **nie** gesetzt, auch nicht als Trenner zwischen Label und Titel, auch nicht mitten im Satz.
  **STATUS: SETTLED.**
  - de.wikipedia, *Halbgeviertstrich*: „Der Gedankenstrich wird in deutschen Texten typografisch als
    **Halbgeviertstrich** realisiert" und „Der Gedankenstrich wird auf beiden Seiten durch ein **Leerzeichen**
    (oder einen Zeilenumbruch) vom Umgebenden getrennt"; zum Englischen ausdrücklich abgegrenzt: „Im
    Englischen wird als Gedankenstrich oft auch der **Geviertstrich** ( — ) … verwendet."
    (<https://de.wikipedia.org/wiki/Halbgeviertstrich>)
  - de.wikipedia, *Geviertstrich*: im Deutschen „**kaum verwendet**"; als Gedankenstrich dient er „in
    verschiedenen Sprachen wie dem **Englischen und dem Spanischen**".
    (<https://de.wikipedia.org/wiki/Geviertstrich>)
  - typolexikon, *Gedankenstrich*: „In der Typografie wird ein Gedankenstrich auch als **Halbgeviertstrich**
    bezeichnet"; für den Parenthesestrich „**Vor und nach dem Gedankenstrich wird ein Leerraumzeichen
    gesetzt**". (<https://www.typolexikon.de/gedankenstrich/>)

  > **Das ist ein Fall der Vorrangregel, und zwar der bisher größte nach Fläche.** Der Geviertstrich steht in
  > diesem Korpus nicht aus deutschem Anlass, sondern **geerbt aus dem englischen Quelltext**, und RU und SK
  > haben ihn mitgeerbt: `Часть I — RAG`, `Časť I — RAG`. Genau die Konstellation, für die die Vorrangregel
  > geschrieben wurde — projektweite Konvention gegen belegte deutsche Norm → **die deutsche Norm gewinnt**,
  > und die Divergenz zu RU/SK wird hier protokolliert statt stillschweigend absorbiert. Wer sie später
  > „glattzieht", macht die Entscheidung rückgängig.
  >
  > **Verhältnis zur Bis-Strich-Zeile — kein Widerspruch, zwei verschiedene Striche.** Beide sind derselbe
  > Codepoint `–` (U+2013); sie unterscheiden sich **nur durch die Leerzeichen**, und das ist Absicht:
  > **Bis-Strich kompress** (`10–20 %`, ein Bereich), **Gedankenstrich gespreizt** (`Teil I – RAG`, ein
  > Einschub oder Trenner). Wer die beiden Zeilen nebeneinander liest und einen Fehler vermutet, hat die
  > Funktion verwechselt, nicht den Kanon.
  >
  > **Herkunft dieser Zeile.** Aufgeworfen von der `de-ui-strings`-Instanz beim Bau von `i18n/de/**` (#279),
  > die den Wert **nicht** eigenmächtig geflippt hat, weil der Kanon ihn nicht entschied — richtig gehandelt:
  > eine locale-weite typografische Festlegung ist eine Kanonentscheidung, keine JSON-Entscheidung.
  > **Der Befund ist zugleich eine Lücke im Sweep:** `de-locale-playbook.md` §7.7 gibt an, jeden aus RU/SK
  > geerbten typografischen Wert geprüft zu haben, und führt diesen nicht auf. Ein Sweep, der sich für
  > vollständig erklärt, ist damit nachweislich unvollständig gewesen — die Lehre gilt allgemein: **ein
  > Vollständigkeitsanspruch ist selbst eine Behauptung und trägt keinen Beleg.**

  **Betroffene Flächen — umgestellt in #314, Endstand 21 Vorkommen** (`i18n/de/**`, ausgezählt, nicht
  geschätzt):

  - **8** `Teil N — …`-Kategorielabel in den Sidebars (5 `aiSdlcSidebar`, 3 `handbookSidebar`)
  - **8** Kopien davon im Footer (`link.item.label.Part…`)
  - **2** weitere Label desselben Musters: `Serving — FastAPI und Docker`, `LLMOps — Bereitstellung,
    Überwachung, Kosten`
  - **3** satzinterne Vorkommen: `landing.hero.tagline`, der RAG-Blurb **und die
    generated-index-Beschreibung von `Cross-cutting`**

  > **Belegnachtrag aus dem Termledger-Durchgang (#275/#276), 2026-07-28 — nur Evidenz, keine Neuentscheidung.**
  > Diese Zeile war **schon entschieden**, als der Termledger-Durchgang unabhängig auf dasselbe Ergebnis
  > stieß. Die Entscheidung oben bleibt unangetastet; hier stehen nur die Quellen, die sie **noch nicht**
  > führte — sie heben sie von „drei Tier-3-Belegen" auf **Stufe 1**:
  >
  > - **DIN 5008 (Stufe 1, und die einzige Quelle, die den Glyphen VORSCHREIBT):** „Der Gedankenstrich wird
  >   standardmäßig mit einem **Halbgeviertstrich** dargestellt. **Vor und nach dem Gedankenstrich steht ein
  >   Leerzeichen.** Folgt anschließend ein Satzzeichen, entfällt die Leerstelle nach dem zweiten
  >   Gedankenstrich." **Der Geviertstrich ist in DIN 5008 gar nicht vorgesehen.**
  > - **Amtliches Regelwerk § 77 (Stufe 1) regelt die FUNKTION, nicht den Glyphen** — es kontrastiert den
  >   Gedankenstrich nur gegen das **Divis** („Der Gedankenstrich ist **länger**. Divis: - Gedankenstrich: –").
  >   **Es schreibt den Halbgeviertstrich also nicht vor, es führt ihn vor:** im gesamten § 77-Abschnitt
  >   stehen **66 × U+2013 und 0 × U+2014**.
  > - **Gesellschaft für deutsche Sprache:** „Der Langstrich (Halbgeviertstrich) kommt – wie beispielsweise
  >   in diesem Satz – seiner Aufgabe als Gedankenstrich bei Einschüben nach." <https://gfds.de/strichlaengen/>
  > - **Gemessen statt charakterisiert:** über acht deutsche Quellen (heise-Startseite und heise/developer,
  >   ein iX-Artikel, Rheinwerk-Startseite, gfds.de, typolexikon.de, der § 77-Abschnitt, eine
  >   Universitätsseite) wurden die Codepoints gezählt — **≈ 220 × U+2013, 0 × U+2014**. *(dpunkt.de
  >   antwortete mit 403 und ist nicht enthalten.)* Die Verlage setzen die Form **in genau unserer
  >   Titelkonstruktion**: „Passkeys in der Praxis **–** Teil 1", „Won't fix! **–** Teil 5: …" (heise
  >   developer), „SAP HANA & S/4HANA **–** Entwicklung" (Rheinwerk).
  >
  > **Zwei Präzisierungen, die die Zeile schärfer machen, ohne sie zu ändern:**
  >
  > 1. **Verboten oder nur unüblich? Präzise: nur unüblich — und das trägt hier trotzdem.** **Kein** deutscher
  >    Beleg *verbietet* U+2014; § 77 regelt die Funktion. Aber DIN 5008 **zählt die zulässigen Formen auf und
  >    enthält ihn nicht**, und die deutschen Quellen ordnen ihn dem Englischen zu. Der Unterschied ist
  >    wichtig, damit niemand die Zeile mit einem Normverstoß begründet, den es nicht gibt.
  > 2. **Der eigentlich verräterische Punkt ist die Spationierung, nicht der Glyph.** Die **englische**
  >    Konvention setzt den Geviertstrich **kompress** (`word—word`). Ein `Titel — Untertitel` mit **vollen
  >    Leerzeichen um einen Geviertstrich** ist **weder die deutsche noch die englische Form** — es ist das
  >    Muster maschinell erzeugten Englischs. Genau dieses Signal darf diese Locale nicht senden.
  >
  > **Randfall aus § 77 E2**, der in der Lektionsprosa vorkommen wird: folgt auf den schließenden
  > Gedankenstrich ein **Komma**, steht es **eng am Strich** — „Sie wundern sich – so schreiben Sie **–,**
  > dass ich Ihnen so selten schreibe." (Beispiel des Regelwerks), also `–,` ohne Zwischenraum dazwischen.
  >
  > **Und ein Nachtrag, der die Bis-Strich-Zeile oben STÜTZT statt sie aufzumachen:** die dort protokollierte
  > Spaltung (Duden kompress gegen den *normativen* Teil von DIN 5008) löst die GfdS auf — „Der Bis-Strich
  > **darf auch kompress gesetzt werden** … Wenn Sie den Langstrich so setzen, folgen Sie … auch dem
  > **(nicht normativen) Anhang F** der besagten DIN 5008, die zu typografisch anspruchsvollen Textwerken
  > Bezug nimmt." **Die kompresse Bis-Strich-Regel wird damit nicht wieder aufgemacht.**

  Und, ungleich größer als alle 21: **die gesamte noch ungeschriebene deutsche Lektionsprosa**, für die diese
  Zeile ab jetzt gilt.

  > **Diese Aufzählung stand hier zuerst falsch — und das gehört ins Protokoll, weil es dieselbe Lehre ist,
  > die der Kasten darüber dem §7.7-Sweep vorhält, eine Ebene tiefer.** Die erste Fassung nannte „acht,
  > acht, **zwei** satzinterne" und ließ `Serving`, `LLMOps` und die `Cross-cutting`-Beschreibung ganz aus:
  > **20 statt 21, und die Gliederung an zwei Stellen daneben.** Ich hatte aus der Meldung abgeschrieben,
  > die die Zeile ausgelöst hat, statt selbst zu zählen. Gefunden wurde der Fehler nur, weil die
  > `de-ui-strings`-Instanz beim Umstellen **jede Nachricht mit U+2014 enumeriert hat, statt meine Liste
  > abzuarbeiten**.
  >
  > **Die Regel, die daraus folgt und für jede „betroffene Flächen"-Angabe in diesem Kanon gilt:** eine
  > Flächenangabe wird **ausgezählt, nicht übernommen** — und wer sie abarbeitet, enumeriert das Muster
  > selbst, statt der Liste zu vertrauen. Eine Liste im Kanon ist ein **Hinweis auf die Größenordnung**, nie
  > die Arbeitsgrundlage. Zwei Sweeps in Folge haben sich in genau diesem Punkt geirrt (§7.7 des Playbooks
  > und diese Zeile); der Fehlertyp ist also nicht die Ausnahme, sondern der Normalfall.

- **Geschütztes Leerzeichen zwischen Zahl und Einheit** (128 GB, 8 GPU, 24 h), damit der Wert nicht am
  Zeilenende abreißt. **STATUS: SETTLED** für das Leerzeichen („Einheiten werden **immer** mit einem
  Leerzeichen zwischen dem Zahlenwert und der Einheit geschrieben"), WEAK für die Art des Leerzeichens.
  Innerhalb einer abgekürzten Einheit steht **nie** ein Leerzeichen. Sonderfälle: **Temperatur** `8 °C`
  (Zwischenraum, dann Gradzeichen direkt an der Einheit), **Winkel** `45°` (kein Zwischenraum) — korrekturen.de
  nennt den Winkelgrad ausdrücklich als „die einzige Ausnahme … 45° (aber: 45 °C)".
  **Das Prozentzeichen fällt unter dieselbe Regel** und bekommt denselben schmalen geschützten Zwischenraum
  (`20 %`) — siehe die Prozent-Zeile oben. *(Diese Stelle sagte bis 2026-07-28 das Gegenteil; sie wurde mit
  der Prozent-Umkehrung nachgezogen.)*
- **Wie der schmale Zwischenraum in den Quelldateien steht.** In dieser Kanondatei und in allen Beispielen
  oben steht an den betreffenden Stellen ein **normales Leerzeichen** — eine Regelsammlung, in der das
  entscheidende Zeichen unsichtbar ist, kann niemand prüfen. Im **gesetzten Korpus** (`i18n/de/**`) steht
  dort U+202F, ersatzweise U+00A0. Wer eine Regel aus dieser Datei kopiert, kopiert also die *Form*, nicht
  das Byte.

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
  Tool-Definition, im Strict Mode, das Constrained Decoding, der Idempotency-Key, der Dry-Run*. Beim
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
*Idempotency-Key*. Ein deutscher Prägungssatz (*Werkzeugaufruf*, *strikter Modus*, *eingeschränkte
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

> ### Die vier Fallen, an denen diese Tabelle gebaut wurde — lesen, bevor Sie eine Zeile nachtragen
>
> **Falle 1 — der Wörterbucheintrag im FALSCHEN SINN.** Ein Lemma zu finden ist nicht dasselbe wie einen
> Beleg zu finden. Die Belegdurchgänge zu diesem Kanon sind daran **neunmal** hängengeblieben, und jedes
> Mal hätte die Zeile **tadellos zitiert und trotzdem falsch** dagestanden. **Stand seit dem Piloten
> „Tool-Einsatz" (2026-07-28): sechzehn** — die neun des Belegdurchgangs (Phase 2) plus **sieben neue**,
> unten mit Datum markiert. Die Zahl „neun" bleibt hier stehen, damit der Zuwachs lesbar ist:
>
> | Wort | Wörterbuchsinn / falscher Referent | unser Sinn |
> |---|---|---|
> | `Log` (DWDS) | seemännisch, Fahrtmessgerät, Plural **Loge** | Protokolldatei — **aber der Duden hat ein ZWEITES Lemma im richtigen Sinn**, siehe unten |
> | `Gate` | Flughafen-Gate — **und seit 2026-07-28 kommt der gefährlichere Zwilling dazu:** ⚠ **NICHT nur das Flughafen-Gate.** de.wikipedia *Long short-term memory* flektiert **das Input Gate**, **das Forget Gate**, **des Forget Gates** — ein attestiertes, genusmarkiertes **LSTM-Gate** | der Kontrollpunkt im Ablauf |
> | `Queue` | Billardstock; veraltet Personenschlange | Nachrichten-/Job-Warteschlange |
> | `Checkpoint` (Duden **und** DWDS) | Kontrollpunkt an Grenzübergängen | gespeicherter Modell-/Ablaufzustand |
> | `Rollback` | Kalter Krieg, „Zurückdrängung des Kommunismus"; „Rückschritt" | Zurücksetzen einer Transaktion/Version |
> | `Container` | Transportbehälter | Prozessisolation |
> | `Span` | Holzspan, Plural **Späne** | Teilstück eines Trace |
> | `Grounding` | Grounding **der Swissair**; Wellness-„Erden" | Rückbindung an den Kontext |
> | `scoren` / `pushen` / `pullen` / `instrumentieren` | Sport / salopp+Drogenjargon / Rudern+Reiten+Golf / Orchester | siehe §1.3.2 |
> | `Time-out` (Duden) *(neu 2026-07-28)* | **Sport**: „Auszeit" — der Eintrag hat **gar keinen** EDV-Sinn | die Zeitschranke / der Zeitfehler |
> | `transient` (DWDS) *(neu 2026-07-28)* | **Signalphysik** („die Transiente betreffend"); das DWDS-Informatikbeispiel ist das **Java-Schlüsselwort** (nicht serialisiert) | der vorübergehende Fehler |
> | `Grundlast` (DWDS) *(neu 2026-07-28)* | **Stromnetz** („ständig zur Verfügung stehende Energiemenge"), historisch Grundlasten auf einem Grundstück | die laufenden Kosten eines Mechanismus |
> | `Sampler` / `sampeln` (Duden + DWDS) *(neu 2026-07-28)* | **Musik**: die Sampler-CD, das Sampling-Instrument; „einen Sampler zusammenstellen" | die Auswahlstufe der Dekodierung |
> | `wohlgeformt` (Duden + DWDS) *(neu 2026-07-28)* | **ästhetisch**: „wohlgeformte Hände", „eine wohlgeformte Vase" | syntaktisch regelkonform |
> | `Loadout` *(neu 2026-07-28)* | **Gaming**: die vor der Mission gewählte Waffen-/Ausrüstungsauswahl | die dynamisch geladene Tool-Menge |
> | `Fan-Out` *(neu 2026-07-28)* | **Digitaltechnik**: *Ausgangslastfaktor*; **und** der *Fan-Out-Effekt* im **Offsetdruck** | das nebenläufige Verteilen von Aufrufen |
> | ⛔ `Auffächerung` *(kein Lehnwort — der verworfene deutsche Kandidat, zählt nicht zu den sechzehn)* | **Themengliederung** („klar gegliedert ausbreiten"); die einzige Fan-Out-Verbindung ist der **Druck**-Sinn | — (nicht verwenden) |
>
> > **Die Lehre, die diese sieben hinzufügen — und sie schärft die alte Regel, statt sie zu wiederholen:**
> > **Eine Falle IM eigenen Fachgebiet ist gefährlicher als eine ferne.** Das Flughafen-`Gate` hilft bloß
> > nicht weiter; das **LSTM-`Gate`** liefert **korrektes Genus für den falschen Referenten** — genau der
> > `Span`-Fehler, nur eine Etage näher am Text. Wer in einer LLM-Lektion „das Gate" schreibt, landet beim
> > Leser nicht am Flugsteig, sondern am Vergessens-Tor eines rekurrenten Netzes.
>
> **Drei dieser Fallen wurden am 2026-07-28 unabhängig nachgeprüft und halten wörtlich:** Duden
> `Checkpoint` führt als **einzige** Bedeutung „Kontrollpunkt an Absperrungen, Grenzübergängen" — **kein
> EDV-Sinn**, obwohl das volle Paradigma dasteht; Duden `Rollback` führt **nur** „Zurückdrängung des
> Kommunismus …" und „Rückfall, Rückschritt" — **kein Datenbank- oder Deployment-Sinn**; DWDS `Attest` führt
> **ausschließlich** „ärztliche Bescheinigung". **Alle drei würden eine tadellos zitierte, belegfreie Zeile
> ergeben.**
>
> **Zwei Lehren daraus, beide teuer erkauft.** (a) **Eine Suchergebnis-Vorschau, die einen Eintrag
> beschreibt, ist nicht der Eintrag** — die Duden-Seite zu `Rollback` wurde in einem Snippet mit einem
> Datenbanksinn beschrieben, den sie nicht enthält. (b) **Eine Falle in EINEM Wörterbuch heißt nicht, dass
> das ANDERE den richtigen Sinn nicht führt** — genau das ist bei `Log` passiert (DWDS seemännisch, Duden
> hat ein separates EDV-Lemma) und bei `Agent` (Duden kennt **keinen** Softwaresinn, DWDS führt ein
> eigenes Homograph ²Agent). Wer nur eine Quelle prüft, bekommt beide Male das falsche Ergebnis.
>
> **Falle 2 — „Deutsch behält das Englische" ist KEINE Regel.** §1.0 sagt richtig, dass ein Anglizismus
> hier kein Defekt ist. Daraus folgt **nicht**, dass der Loan gewinnt. Die Belegdurchgänge haben
> **vierzehn** Termini gefunden, bei denen die deutsche Form **entscheidend gewinnt** — sie stehen unten
> gesammelt in §1.1.g, weil ein flüssig schreibendes Modell sie **zuverlässig falsch** macht. Das
> beobachtete Muster (Heuristik, keine Regel — sie ersetzt keinen Beleg):
>
> - Deutsch gewinnt bei **Messgrößen und Vorgängen**: *Durchsatz, Latenz, Inferenz, Quantisierung,
>   Instrumentierung, Fehlerbudget, Endpunkt*.
> - Englisch hält bei **Dingen, auf die man zeigen kann**: *Container, Queue, Deployment, Rollback,
>   Worker, Feature Flag, Cache*.
> - Englisch hält fast geschlossen bei **`-ing`-Nominalisierungen**: *Chunking, Grounding, Fine-Tuning,
>   Reranking, Monitoring, Sampling, Tracing* — diese Familie ist deutschen Konkurrenten praktisch
>   verschlossen.
> - **Das Substantiv bleibt englisch, das Verb wird deutsch** (§1.2, §1.3.2): *das Embedding* /
>   *vektorisieren*, *das Chunking* / *unterteilen*, *der Trace* / *nachverfolgen*, *das Code-Review* /
>   *prüfen*. Wer das Verb mitentlehnt, schreibt übersetztes Englisch.
>
> **Falle 3 — die KOLLOKATION, die flüssig klingt und englisch gebaut ist.** Diese Falle liegt **hinter**
> allen anderen, weil sie jede Flüssigkeitsprüfung überlebt. Beim Rendern der UI-Strings (#279) gewannen
> **zwei** deutsche Formulierungen eine ordentlich durchgeführte Blindbewertung — vier divergente
> syntaktische Strategien, verdeckte Kandidaten, benannter linguistischer Grund — und fielen erst bei der
> Attestierung:
>
> - **„aus Grundprinzipien"** — attestiert **nur als Verbergänzung**, nie als bloßes Attribut.
> - **„die sie ehrlich halten"** — im Deutschen **gar nicht** vorhanden; der Duden führt
>   `jemanden **für** ehrlich halten` — **andere Rektion, andere Bedeutung**.
>
> Beides ist flüssiges Deutsch auf einem **englischen Kollokationsgerüst**. Daraus folgt eine stehende
> Regel für dieses Register:
>
> > **Blindbewertung und Attestierung sind zwei verschiedene Gates, und Flüssigkeit verdeckt genau das,
> > was die Attestierung findet. Wer eine MEHRWORTIGE deutsche Wiedergabe festlegt, attestiert die
> > KOLLOKATION — nicht nur das Kopfnomen.** Verlangt wird ein **realer deutscher Satz**, der die Fügung
> > enthält, samt Rektion und Kasus. Ein Kopfnomen, das im Wörterbuch steht, sagt nichts darüber, ob es in
> > **dieser** Fügung, mit **dieser** Präposition, in **dieser** Funktion vorkommt.
>
> Das ist die Falle, für die dieser Locale **kein** natives Korrektiv hat: eine englisch gebaute deutsche
> Kollokation liest sich für jeden Nicht-Muttersprachler — und für jedes Modell, das sie erzeugt hat —
> einwandfrei.
>
> **Falle 4 — die Herstellerlokalisierung.** Die MT-Signal-Prüfung (§ Sprachpaar) hat in diesen
> Durchgängen konkret disqualifiziert: **Microsoft Learn de-de** (rendert *grounding* auf **einer** Seite
> als *Erddaten*, *Erdung*, *Grundlagedaten*, *Volldokumentgrundung* **und** unübersetzt; erklärt sich in
> den eigenen Metadaten als `ms.translationtype: MT`), **Splunk de_de** (*die* Trace neben *der* Span auf
> derselben Seite), **Google Cloud de gegen AWS de** (*Beobachtbarkeit* als Laufterm gegen unübersetztes
> *Observability*), **Microsoft/AWS/IBM zu Dead-Letter Queue** (vier Übersetzungen, drei Hersteller, einer
> widerspricht sich selbst), **Atlassian de** (nachgewiesene MT-Signale), **alphaXiv-DE** und
> **KI-generierte Glossar-Contentfarmen** (`feed2content.ai` u. a.).
> **Die Prüfung ist eine Konsistenzprüfung, kein Herstellerbann:** die deutsche AWS-Builders-Library-Seite
> zu *Lastabwurf* ist in sich stimmig und wurde deshalb als **schwacher** Beleg behalten, nicht verworfen.

> ### Ein Lehnwort kann als KOMPOSITUMSBILDNER überleben und als freies Substantiv unbrauchbar sein
>
> *(Neu aus dem Piloten „Tool-Einsatz", 2026-07-28. Die vier Fallen oben werden dadurch **nicht** umnummeriert
> — dies ist keine fünfte Falle, sondern eine Klasse, die der Tabelle fehlt.)*
>
> Die Tabelle in §1.1 kennt zwei Zustände: englisch geführt oder deutsch geführt. **Dieser Durchgang hat
> einen dritten gefunden**, und zwar zweimal unabhängig: **`Retry`** und **`Backoff`** haben **kein
> attestiertes Genus als freies Substantiv**, treten aber völlig unauffällig als erstes Glied eines
> Kompositums auf. `das Retry-Budget` ✅ / `ein Retry` ⛔; `die Backoff-Strategie` ✅ / `das Backoff` ⛔.
>
> Der Grund ist grammatisch, nicht zufällig: **im Kompositum trägt das Kopfnomen das Genus**, das Lehnwort
> braucht also gar keins. Genau deshalb ist eine Zählung „kommt 6-mal vor" wertlos, solange man nicht zählt,
> **wie oft es mit eigenem Artikel** vorkommt — bei `Backoff` war die Antwort null.
>
> **Praktische Regel für Nachträge:** Wer für ein Lehnwort kein flexionstragendes Beispiel findet, trägt
> nicht „OPEN, Wort meiden" ein, sondern prüft, ob die **Kompositumsverwendung** belegt ist — dann ist das
> Wort im Korpus brauchbar, nur nicht als nacktes Substantiv.
>
> ⚠ **Dieser Kasten schränkt die Nachtrag-Regel am Ende von §1.1.g ein** — dort steht „Wer keinen Beleg
> findet, trägt OPEN ein und umgeht das Wort". Das gilt weiter für das **nackte** Substantiv; die
> Kompositumsverwendung wird **vorher** geprüft, nicht mit umgangen.

### §1.1.a Grundvokabular — im Wörterbuch entschieden

| Terminus | Artikel | Plural | Genitiv Sg. | Status / Beleg |
|---|---|---|---|---|
| Cache | **der** Cache | die Caches | des Cache**s** | SETTLED — Duden: „der Cache; Genitiv: des Cache, Plural: die Caches" <https://www.duden.de/rechtschreibung/Cache>. DWDS druckt „Cache(s)" — **Hausform mit -s**, damit sie zu allen übrigen Zeilen passt. |
| Prompt | **der** Prompt | die Prompts | des Prompts | SETTLED — Duden und DWDS führen beide **nur Maskulinum**: „der Prompt; Genitiv: des Prompts, Plural: die Prompts" <https://www.duden.de/rechtschreibung/Prompt>. Ein vereinzeltes „das Prompt" kommt in freier Wildbahn vor und ist **kein** Vorbild. |
| Token | **das** Token | **die Token** | des Tokens | **SETTLED (2026-07-28) — vorher DISPUTED, und die Gegenevidenz war die falsche.** Duden: „das oder der Token; Genitiv: des Tokens, Plural: die Token[s]" <https://www.duden.de/rechtschreibung/Token>, richtiger Sinn (EDV + Sprachwissenschaft). **Ein Wörterbuch, das beide Genera lizenziert, ist kein Quellenstreit** — es ist eine Wahl, und die trifft der Kanon. Die frühere Notiz „die KI-Fachprosa neigt zum Maskulinum" hält der **flexionstragenden** Evidenz nicht stand: heise schreibt „**ein einzelnes nächstes** Token", „nur **ein einzelnes** Token" (neutrale starke Endung; maskulin wäre *ein einzelner nächster Token*) <https://www.heise.de/hintergrund/Speculative-Decoding-Wie-Multi-Token-Prediction-LLMs-beschleunigt-11332677.html>. **Plural umgestellt auf die unmarkierte Form „die Token"** — so durchgängig bei heise („mehrere **Token** vorhersagt", „ein Kontextfenster von 64.000 **Token**"); *Tokens* ist Duden-Nebenform. |
| Agent | **der** Agent | die Agenten | **des Agenten** | SETTLED — **aber nicht über den Duden.** Duden führt für *Agent* **keinen** Softwaresinn (Spion, Handelsvertreter, Künstleragent) — die frühere Zitierung war die Falle aus dem Kasten oben. **DWDS führt ein eigenes Homograph ²Agent** im richtigen Sinn: „Computerprogramm, das unabhängig von Benutzereingriffen abläuft, selbstständig Entscheidungen trifft …", markiert *Informations- und Telekommunikationstechnik* <https://www.dwds.de/wb/Agent>. n-Deklination in beiden Quellen. de.wikipedia führt **Software-Agent** und **KI-Agent** als eigene Lemmata. **n-Deklination: „des Agents" ✗, „dem Agent" ✗** — der voraussichtlich häufigste Flexionsfehler dieses Korpus. ⚠ **Präzisierung 2026-07-28:** „n-Deklination in beiden Quellen" ist zu knapp — DWDS druckt unter ²Agent **zwei** Paradigmen nebeneinander, und `des Agents` gehört zum Untersinn *installierte Client-/Daemon-Software*. Die Korpusregel ändert sich dadurch **nicht**, ihre Begründung schon; siehe §1.3.1. |
| Kontext | **der** Kontext | die Kontexte | des Kontext[e]s | SETTLED — Duden <https://www.duden.de/rechtschreibung/Kontext> |
| KI | **die** KI | die KIs | der KI | SETTLED — Duden: „die KI; Genitiv: der KI, Plural: die KIs" <https://www.duden.de/rechtschreibung/KI> |
| API | **die** API | die APIs | der API | **DISPUTED** — DWDS führt **zwei** Einträge: Neutrum als Haupteintrag („das API; Genitiv: API(s)") und Femininum **umgangssprachlich markiert** <https://www.dwds.de/wb/API>; kein Duden-Lemma. **Incumbent: die API**, weil die deutsche Vollform *die Programmierschnittstelle* feminin ist und die Fachprosa dem folgt. Der Konflikt steht hier, damit ihn niemand für ein Versehen hält. |
| Pipeline | **die** Pipeline | die Pipelines | der Pipeline | SETTLED — Duden: „die Pipeline; Genitiv: der Pipeline, Plural: die Pipelines" <https://www.duden.de/rechtschreibung/Pipeline> (CI/CD-Sinn bei heise belegt) |
| Index | **der** Index | die Indizes | des Index[es] | SETTLED (Genus) / Plural gespalten — Duden: „der Index; Genitiv: des Index[es], Plural: die Indexe und Indizes, auch: Indices" <https://www.duden.de/rechtschreibung/Index>; DWDS reiht *Indizes* zuerst. **Hausform: Indizes.** |
| Batch | **der** Batch | die Batches | des Batch**s** | SETTLED (Genus gespalten) — Duden: „der oder das Batch; Genitiv: des Batchs, Plural: die Batches" <https://www.duden.de/rechtschreibung/Batch>. **Hausform: der Batch.** Achtung Genitiv: *des Batchs*, nicht „des Batches". **Nachtrag DE-Pilot (2026-07-28) — Korpusformen, und eine abgelehnte Herabstufung.** Der Pilot brachte diese Zeile als **WEAK** ein (de.wikipedia *Stapelverarbeitung* führt nur „**Die** Batch-Jobs", also Genus am Kopfnomen *Jobs*; artikeltragend nur KrautPress: „**einen** Batch-Request", „**im** Batch"). **Die Herabstufung wird nicht übernommen:** das Paradigma steht im Duden, und die Pilotbelege widersprechen ihm nicht, sie stützen es bloß schwächer. WEAK gilt allein für die **Fügung**, nicht für Genus/Plural/Genitiv. **Korpusform für den Vorgang: „zu einem Batch zusammenfassen", „gemeinsam in einem Batch absetzen"** (Verb `batchen` = OPEN, §1.3.2). ⚠ **Und `zusammenfassen` darf in dieser Bedeutung nie nackt stehen** — in einem Text über Sprachmodelle liest es sich zuerst als *summarize*; beide Kaltleser des Piloten sind unabhängig voneinander darüber gestolpert. Das Objekt muss mit: „fasst die Aufrufe zu einem Batch zusammen". |
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
| Latenz | **die** Latenz | die Latenzen | der Latenz | **SETTLED — Beleg 2026-07-28 nachgetragen** (die Zeile behauptete SETTLED ohne Quelle). Duden führt den IT-Sinn **ausdrücklich** als Bedeutung 4, *Fachsprache*: „Zeit zwischen einem Ereignis und der darauf folgenden Reaktion; **Verzögerungszeit**" <https://www.duden.de/rechtschreibung/Latenz>. Dudens Deklinationstabelle zeigt **nur Singularformen**; den Plural liefert DWDS („Nominativ Plural: **Latenzen**", <https://www.dwds.de/wb/Latenz> — dort allerdings **ohne** den IT-Sinn). **Zwei Quellen, zwei Hälften: Duden die Bedeutung, DWDS der Plural.** In der Praxis dominiert das Kompositum („**Anfragelatenz**"). |
| Durchsatz | **der** Durchsatz | die Durchsätze | des Durchsatzes | SETTLED — Duden, mit EDV-Sinn: „Zahl der pro Zeiteinheit verarbeiteten Anweisungen oder übertragenen Daten" <https://www.duden.de/rechtschreibung/Durchsatz> |
| Tool-Definition | **die** Tool-Definition | die Tool-Definitionen | der Tool-Definition | **WEAK — herabgestuft von SETTLED (2026-07-28), und zugleich erstmals belegt.** Das **Kopfprinzip** (das deutsche Grundwort *Definition* bestimmt Genus und Flexion) ist ein **morphologisches Argument, kein Beleg** — die Zeile stand als SETTLED ohne Quelle. **Der Beleg existiert jetzt:** eine dpunkt-Ausgabe eines LLM-Anwendungsbuchs führt „**Richtlinien für Tooldefinitionen**" als Kapitelüberschrift und — **innerhalb desselben Bandes uneinheitlich** — „Richtlinien für **Tool-Definitionen**" sowie „**Tooldefinitionen**" im Register. Ehrlich dazu: das ist eine **übersetzte** deutsche Ausgabe, also lektoriertes deutsches Verlagswesen, keine originär deutsche Prosa. **Die frühere Feststellung „zero German attestation" für diesen Terminus ist damit widerlegt** — anders als bei *Tool-Result*. |
| Prompt-Injection | **die** Prompt-Injection | die Prompt-Injections | der Prompt-Injection | SETTLED (Kopfprinzip + § 45 E1) — Grundwort *Injection* feminin; im Fachjournalismus feminin belegt („Eine Prompt Injection in einem Repository …", heise). **Schreibung mit Bindestrich, siehe §1.3.3** — die dort verbreitete Getrenntschreibung ist die vom Regelwerk ausdrücklich als nicht normgerecht bezeichnete. |
| Commit | **der** Commit | die Commits | des Commits (*regelhaft*) | **WEAK** — kein Duden-/DWDS-Lemma. Das Maskulinum trägt nicht der Nominativsatz, sondern das **anaphorische Pronomen** bei de.wikipedia: „Commit ist ein Ausdruck aus der Softwaretechnik … **Er** wird sowohl im Zusammenhang mit der Persistierung …" <https://de.wikipedia.org/wiki/Commit>; heise flektiert: „**Jeder** Commit erhält eine eindeutige Kennung", „auf **den aktuellsten** Commit", „**Die** Commits bilden eine verknüpfte Liste". **Genitiv ehrlich: heise schreibt auch unflektiert „zur Referenzierung *eines Commit*"** — *des Commits* ist Hausform, nicht durchgängig belegt. |
| Harness | **der** Harness (Incumbent) | die Harnesses | des Harness | **DISPUTED (2026-07-28) — und der Widerspruch sitzt IM Beleg, nicht zwischen zwei Recherchen.** Kein Wörterbucheintrag. Maskulin, zweifach kasusmarkiert: „sowohl für **den** Coding-Harness von Claude Code als auch für **den** Harness des eigenen Agenten" (heise) <https://www.heise.de/news/Claude-Code-in-der-Praxis-eigenen-KI-Chat-Agenten-in-fuenf-Sessions-entwickeln-11353330.html>. **Derselbe Verlag schreibt in seinem eigenen Erklärstück dreimal NEUTRUM:** „Dazu braucht es **das Harness**", „… ist **das Harness**", „angetrieben **vom Harness**" <https://www.heise.de/hintergrund/Kurz-erklaert-Agent-Harness-11330445.html>. Beide Sätze sind nachgeprüft und stehen wörtlich da. **Incumbent *der Harness* wird gehalten**, kein Flip ohne nativen Check (→ Leserpaket). Wo es unsicher wirkt: als Kompositum umgehen („das Agentengerüst"). **Nicht verwechseln:** de.wikipedias Lemma **Test-Harnisch** („bzw. **Testrahmen**") ist der *Test*-Harness der Qualitätssicherung — ein **anderer Referent** als der Agenten-Harness und deshalb **kein** Konkurrent für diese Zeile. |
| Embedding | **das** Embedding | die Embeddings | des Embeddings | **WEAK (2026-07-28, hochgestuft von HOUSE)** — kein Duden-/DWDS-Lemma, aber flexionstragend belegt: „**Ein längeres** Embedding hingegen enthält zusätzliche Information" (neutrale starke Endung; maskulin wäre *ein längerer*) und „die Dimension **des Embeddings**" <https://www.herr-rau.de/wordpress/2025/06/llm-grundlagen-teil-3-ueber-embedding.htm>; heise behält den Loan („Zum Speichern und Suchen **der Embeddings**"). Die deutsche Prägung *Worteinbettung* ist ein de.wikipedia-Lemma, bleibt aber auf das klassische Wort-Embedding beschränkt und ist **nicht** die Korpusform. **Bloßes „Einbettungen" für Embeddings erschien nur auf der disqualifizierten Microsoft-Seite.** |
| Chunk | **der** Chunk | die Chunks | des Chunks | **WEAK (2026-07-28, hochgestuft von HOUSE)** — de.wiktionary führt „**der** Chunk, Genitiv **des Chunks**, Plural **Chunks**" — allerdings im **psycholinguistischen** Sinn („Block sprachlicher Information … Kurzzeitgedächtnis"); benachbarter Sinn, die Morphologie überträgt sich, das steht hier ausdrücklich. Im RAG-Sinn maskulin flexionstragend: „**Ein** Chunk ist **ein segmentierter** Daten- oder Textblock". Deutsche Wörter (*Textabschnitt*, *Abschnitt*) erscheinen als **Glosse neben** dem Loan („die Chunks, also die generierten kleineren Textabschnitte"), nie als Terminus. *Textbaustein*, *Fragment*: keine Attestierung in diesem Sinn. |
| Chunking | **das** Chunking | (kein Plural) | des Chunkings | HOUSE (-ing-Nominalisierung → Neutrum, analog *das Training*) |
| Reranking | **das** Reranking | (kein Plural) | des Rerankings | HOUSE (wie *Chunking*) |
| Grounding | **das** Grounding | (kein Plural) | des Groundings | HOUSE (wie *Chunking*) |
| Fine-Tuning | **das** Fine-Tuning | die Fine-Tunings | des Fine-Tunings | HOUSE (wie *Chunking*) |
| Retrieval | **das** Retrieval | (Plural strittig) | **des Retrievals** | **SETTLED (2026-07-28) — vorher HOUSE „Genus unbelegt". Der Beleg existierte; niemand hatte das nackte Lehnwort nachgeschlagen, nur die Fügung *Information Retrieval*.** Duden, Fachgebiet **EDV**: „**das Retrieval; Genitiv: des Retrievals, Plural: die Retrievals**", Bedeutung „Kurzform für Information-Retrieval" <https://www.duden.de/rechtschreibung/Retrieval>. Artikeltragend im RAG-Sinn: „**Das Retrieval** der für die Anfrage relevanten Dokumente" <https://blog.mayflower.de/20544-rag-reranker.html>. **Zum Plural bleibt ein echter Quellenstreit:** DWDS überschreibt den Eintrag „Retrieval, **das oder der**" und markiert „wird nur im Singular verwendet" <https://www.dwds.de/wb/Retrieval>. Genus: Duden ist eindeutig, DWDS lässt beides — der Kanon nimmt das Neutrum. Plural im Korpus **vermeiden**. |
| Trace | **der** Trace | die Traces | des Traces (*regelhaft abgeleitet*) | **WEAK (2026-07-28, hochgestuft von HOUSE)** — kein Wörterbucheintrag; maskulin flexionstragend bei INNOQ: „**Jeder** Trace besitzt eine ID", „**ein neuer** Trace" <https://www.innoq.com/de/articles/2023/03/microservices-tracing/>. de.wikipedia hat native Lemmata (*Ablaufverfolgung* für die Tätigkeit, *Ablaufprotokoll* für das Artefakt) und **räumt selbst ein, dass der Loan die übliche Bezeichnung ist**: „ein Ablaufprotokoll …, **das auch im Deutschen meist als *Trace* bezeichnet wird**". **Disqualifiziert:** Splunk de_de schreibt „**eine** Trace" bei gleichzeitig maskulinem *Span* auf derselben Seite (MT-Signal). |
| Span | **der** Span | die Spans | **des Spans** (belegt) | **WEAK (2026-07-28)** — maskulin und genitivbelegt bei INNOQ: „innerhalb **eines laufenden Spans**", „**einen neuen** Span", „**den** Kind-Span". **⚠ Wörterbuchfalle, nachgeprüft 2026-07-28:** Dudens *Span* hat **zwei** Bedeutungen, und **keine** ist unsere — „kleines, als Abfall entstehendes Stückchen des bearbeiteten Materials" (Holzspan) und, landschaftlich-veraltet, „mit jemandem einen Span haben" (Streit). Grammatik dort: „der Span; Genitiv: des Spanes, Spans, **Plural: die Späne (meist im Plural)**". **Das Genus stimmt zufällig; der Plural darf auf keinen Fall übernommen werden.** IT-Plural ist **die Spans**. |
| ~~Endpoint~~ → **Endpunkt** | **der** Endpunkt | die Endpunkte | des Endpunkt[e]s | **UMGEDREHT auf German-led, SETTLED (2026-07-28) — vorher „der Endpoint", HOUSE.** Siehe §1.1.g. Duden führt *Endpunkt* <https://www.duden.de/rechtschreibung/Endpunkt>; heise schreibt in **jedem** geprüften Register *Endpunkt*, auch im ML-Serving-Kontext: „lässt sich mit KServe **ein Endpunkt** bereitstellen" (Artikeltitel: „… **Modellendpunkte** erstellen"). Die Treffer für *der Endpoint* in deutscher Prosa sind fast alle der **Endgeräte**-Sinn der IT-Sicherheit (*Endpoint Detection and Response*) — ein anderer Begriff. |
| Payload | **OPEN (Artikel)** → deutsch: **die Nutzlast / die Nutzdaten** | die Payloads | — | **DISPUTED für das Lehnwort, German-led als Kanonform.** **Weder Duden noch DWDS haben ein Lemma** (beide 404). de.wikipedias Lemma ist **Nutzdaten** („Als Nutzdaten (englisch *payload*) bezeichnet man …"), der Artikel verwendet auch *die Nutzlast*; heise schreibt „JSON **Nutzlast** (Body) kreieren". Das Lehnwort zirkuliert als *der*, *die* **und** *das* — keine Quelle der Stufen 1–3 weist ein Genus zu. **Korpusform: die Nutzlast** (ein Datenpaket) bzw. **die Nutzdaten** (der Inhalt); „Payload" nur artikellos in Codenähe. |
| Worker | **der** Worker | **die Worker** (nicht *Workers*) | des Workers (*regelhaft abgeleitet*) | **WEAK (2026-07-28, hochgestuft von HOUSE)** — akkusativmarkiert bei heise: „**einen** Worker Thread zu initiieren", „**Den** Code für **den** Worker Thread" <https://www.heise.de/blog/Features-von-uebermorgen-Worker-Threads-in-Node-js-4354189.html>. Nullplural nach der `-er`-Analogie (*der Server / die Server*, Duden: *der Container / die Container*) — **„die Workers" ✗**. *Arbeitsprozess* als Nebenläufigkeitsterminus: **keine deutsche Attestierung auf irgendeiner Stufe**. |
| Branch | **der** Branch | **die Branches** | des Branches (*regelhaft*) | **WEAK (2026-07-28, hochgestuft von HOUSE)** — kein Wörterbucheintrag; de.wikipedia (*Versionsverwaltung*) glossiert: „Ein *Branch*, **zu Deutsch Zweig**, ist eine Verzweigung zu einer neuen Version"; heise flektiert maskulin: „auf einen einzelnen langlebigen Branch: **den** Main Branch". **„die Branchs" hat null Attestierung.** ⚠ **Kollision, die man kennen muss:** das Deutsche hat bereits **die Branche** (Wirtschaftszweig, Plural *Branchen*) — im Plural unterscheidbar, im Singular eine echte Lesefalle. |
| Repository | **das** Repository | **die Repositorys** | des Repositorys | **WEAK — und hier lauert ein Kanon-Bug, der ausdrücklich benannt wird.** Der Duden lemmatisiert **die lateinische Form mit eigener EDV-Bedeutung**: „**das Repositorium**; Genitiv: des Repositoriums, Plural: **die Repositorien**", Bedeutung 2 „Ort zur Speicherung von Daten in der EDV und im Internet" <https://www.duden.de/rechtschreibung/Repositorium>. DWDS hat **weder** *Repository* **noch** *Repositorium*. Für das **Lehnwort** trägt die `-y → -ys`-Regel des Amtlichen Regelwerks (*Baby/Babys*, *Party/Partys*) plus nativer Usus: „**Der HEAD-Pointer des Repositorys**" und die Schlagzeile „… **Repositorys** über Kommandozeile bearbeiten" (heise). **Der Fehler wäre nicht die Wahl, sondern die Mischung:** *die Repositorien* ist der Plural von **Repositorium**, nicht von *Repository*. **Ein Lemma wählen und nur dieses flektieren** — der Korpus nimmt das Lehnwort. *(Die Duden-Seite zu `Repository` selbst antwortete dreimal mit 403 und wird deshalb **nicht** zitiert; die Zeile trägt auch ohne sie.)* |
| Trade-off | **der** Trade-off | die Trade-offs | des Trade-offs | HOUSE (kein Wörterbucheintrag) |
| Tool | **das** Tool | die Tools | des Tools | HOUSE |
| Tool-Call | **der** Tool-Call | die Tool-Calls | des Tool-Calls | HOUSE (Genus vom Grundwort *Call*) — **Schreibung**: § 45 E1, siehe §1.3.3. Die im Fachjournalismus verbreitete Getrenntschreibung „Tool Calls" ist **nicht** normgerecht. |
| Tool-Result | **das** Tool-Result | die Tool-Results | des Tool-Results | **HOUSE — und das Deutsche hat hier NICHTS, worauf man sich stützen könnte: zero German attestation at any tier.** Gesucht wurde nach `Tool Result`, `Tool-Result`, `Tool-Ergebnis`, `Toolergebnis`, `Werkzeugergebnis`, `Ergebnis des Tool-Aufrufs`, `Rückgabe des Werkzeugs` — in Wörterbüchern, bei heise/iX, im Volltext einer deutschen dpunkt-Ausgabe und im BSI-Bestand. **Die einzigen deutschen Treffer stammten von Microsoft Learn de-de und sind disqualifiziert** (Falle 4). **Das Deutsche muss hier also WÄHLEN, und die Wahl lässt sich nicht aus dem Usus abschreiben, weil es keinen gibt.** Der Kanon wählt das Neutrum nach dem Kopfprinzip (*das Result*) und nach der Gleichlage mit *der Tool-Call*. **Das steht hier ausdrücklich, damit niemand diese Zeile später für belegt hält.** *(Kontrast: die Nachbarzeile* Tool-Definition *ist inzwischen belegt — die beiden sind NICHT gleich gelagert.)* |
| **Log** | **das** Log | die Logs | des Logs | **SETTLED (2026-07-28) — vorher „HOUSE mit Warnung", und die Warnung war halb richtig.** DWDS führt tatsächlich nur den **seemännischen** Sinn („Messgerät zur Feststellung der Fahrgeschwindigkeit eines Schiffes", Plural **Loge**) <https://www.dwds.de/wb/Log> — **aber der Duden hat ein zweites, eigenes Lemma im richtigen Sinn:** „**Log**, Substantiv, Neutrum, Gebrauch: **EDV**, des Logs, Plural: **die Logs**, Kurzform für Logdatei, Logfile" <https://www.duden.de/rechtschreibung/Log_EDV>. Ebenso Duden **das Logfile**; de.wikipedia **Logdatei** („auch Protokolldatei"). **Hausaufteilung:** *die Logdatei* für die Datei, *das Log / die Logs* für die Signalklasse (die Observability-Triade heißt in deutscher Fachprosa durchgängig „Logs, Metriken und Traces"), *das Protokoll* nur ohne Verwechslungsgefahr mit dem **Netzwerk**protokoll — genau dieses Homonym ist der Grund, warum die Fachpresse *Log* vorzieht. |
| **Queue** | **die** Queue | die Queues | der Queue | **WEAK (2026-07-28, hochgestuft von HOUSE) — die Wörterbuchfalle bleibt bestehen, der Usus ist jetzt belegt.** Duden/DWDS kennen nur **Billardstock** und die veraltete Personenschlange; der Message-Queue-Sinn steht in **keinem** Wörterbuch. Das Femininum ist aber in nativer Fachprosa zweifelsfrei: „aus **der** Queue entfernt" (informatik-aktuell, Kafka), „entkoppelt RabbitMQ den Publisher nochmals von **der** eigentlichen Queue", „Verfügt hingegen jeder Consumer über **eine eigene** Queue" (heise, AMQP) <https://www.heise.de/developer/artikel/Message-Queues-mit-AMQP-und-Node-js-2099074.html>. Nützlicher Zufall: auch das Wörterbuch-Femininum gehört zum Personen-Schlange-Sinn, das Genus kollidiert also nicht. **Aufteilung nach Sinn:** *die Warteschlange* für die **Datenstruktur** (de.wikipedia-Lemma: „In der Informatik bezeichnet eine Warteschlange (englisch *queue*) eine häufig eingesetzte Datenstruktur"), *die Queue* für die konkrete Broker-/Job-Queue. |
| **Dead-Letter Queue (DLQ)** | **die** Dead-Letter-Queue | die Dead-Letter-Queues | der Dead-Letter-Queue | **WEAK — und es gibt keine native deutsche Form.** Feminin belegt bei ORDIX (deutsches IT-Haus): „muss **die** Dead Letter Queue überwacht werden", „Retry Topics und **Dead Letter Queues** in Apache Kafka" <https://blog.ordix.de/resilienz-in-apache-kafka-mit-dead-letter-queues>. **Deutsche Formen existieren nur in Herstellerlokalisierungen und widersprechen einander** — Microsoft „Warteschlangen für unzustellbare Nachrichten" **und** „Dead-Letter Warteschlangen", AWS „Warteschlangen mit unzugestellten Nachrichten", IBM „dead-letter-Warteschlangen": vier Übersetzungen, drei Hersteller, einer widerspricht sich selbst → **disqualifiziert**. Kein de.wikipedia-Lemma. |
| **Guardrail** | **kein deutscher Singular; Plural: die Guardrails** | die Guardrails | — | **WEAK für den Plural, OPEN für den Singular (2026-07-28) — die frühere Notiz „nirgends belegt, auch nicht bei der BSI" ist FALSCH und wird hier korrigiert.** Die BSI-Handreichung zu LLM-Gegenmaßnahmen enthält *Guardrail* dreimal — aber **ausschließlich innerhalb englischer Maßnahmennamen** („HIG: Human Input Guardrail / **Menschliche Filterung der Eingabe**"), nie flektiert, nie mit deutschem Artikel <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KI/Evasion-Angriffe_auf_LLMs-Gegenmassnahmen.pdf>. **Der Kern des Rulings hält also: kein Genus ist attestiert**, und die BSI übersetzt selbst mit **Filterung**, nicht mit *Leitplanke*. Das native Bild **Leitplanken** ist im KI-Governance-Sinn belegt („… die **Leitplanken** setzen, Ergebnisse prüfen und Trade-offs verantworten", informatik-aktuell) — **immer im Plural**; ein „die Leitplanke" für diesen Sinn wurde auf keiner Stufe gefunden. **Regel: nur im Plural schreiben** („Guardrails", Glosse „(Leitplanken)"); Singular **nicht erfinden**, sondern umformulieren („eine Guardrail-Regel", „ein Schutzfilter"). |
| **Gate** | **OPEN als Einzelwort** | die Gates | — | OPEN — der Wörterbucheintrag „das Gate" betrifft den **Flughafen-Sinn** (DWDS). Im Deutschen ist fast nur das feste Kompositum belegt: **das Quality Gate** ist in deutscher CI/CD-Prosa etabliert (heise/iX) <https://www.heise.de/ratgeber/Shift-Left-Secure-by-Design-und-agile-Entwicklung-4613935.html?seite=4>. Nacktes „das Gate" für den Kontrollpunkt **nicht** setzen; siehe die Sense-Card `gate` im Kurs-Ledger. **⚠ Nachtrag DE-Pilot (2026-07-28): die lebendige Kollision ist nicht der Flugsteig, sondern das LSTM-Gate** — siehe den Fallenkasten oben und `rag.md` §3. |
| **Timeout** | **das** Timeout | die Timeouts | des Timeouts | **SETTLED für Form und Genus (Duden „Time-out, Timeout, das"), Sinn erst auf Stufe 3.** ⚠ **Der Duden-Eintrag ist mit *Sport* markiert und führt als einzige Bedeutung „Auszeit" — er belegt das Lemma, NICHT unseren Sinn.** Den EDV-Sinn trägt de.wikipedia *Timeout (Netzwerktechnik)*: „**Das Timeout** bezeichnet in der Programmierung und Netzwerktechnik entweder die Zeitspanne … oder den Fehler selbst". ⚠ **Deutsche Zweiteilung, die das Englische nicht kennt** — dieselbe Quelle sagt es ausdrücklich: „Diese Zweideutigkeit existiert im Deutschen nicht, hier wird zwischen *Zeitbeschränkung* und *Zeitüberschreitung* unterschieden." **die Zeitbeschränkung** = der eingestellte Grenzwert, **die Zeitüberschreitung** = der ausgelöste Fehler. *Zeitüberschreitung* für einen konfigurierten Wert ist ein **Bedeutungsfehler**, keine Stilfrage. *(DE-Pilot 2026-07-28.)* |
| **Overhead** | **der** Overhead | die Overheads | des Overheads | **SETTLED (Genus).** Duden und DWDS beide **Maskulinum**; informatik-aktuell flexionstragend: „**Der Overhead** … wird **er** dennoch sichtbar", „**im Overhead** dieser Mechanismen". ⚠ **Zweistufige Attestierung, ehrlich vermerkt:** der *Wörterbuch*-EDV-Sinn ist „zusätzlich benötigte Daten" (Protokollbytes), nicht „laufender Aufwand"; unser Sinn ruht auf Duden-Sinn *Verwaltung/Gemeinkosten* **plus** dem informatik-aktuell-Usus. Niemand darf DWDS allein dafür zitieren. *(DE-Pilot 2026-07-28.)* |
| **Granularität** | **die** Granularität | die Granularitäten | der Granularität | **SETTLED, und ausnahmsweise auf Stufe 1.** DWDS: „Grad der Teilbarkeit". Die Adjektive sind **kein** Kunstwort: de.wikipedia „**eine feingranulare** Architektur", „**grobgranularen** Architekturen"; **BSI Zero Trust** liefert sogar den Komparativ — „Berechtigungen möglichst **feingranular** vergeben", „ist **feingranularer** durchgesetzt". *(DE-Pilot 2026-07-28.)* |
| **Validierung** | **die** Validierung | die Validierungen | der Validierung | **SETTLED.** DWDS-Sinn 2 trägt den IT-Untersinn: „Überprüfung der formalen Korrektheit und Integrität von Daten". **Rektion attestiert: `gegen` + Akkusativ** — informatik-aktuell: „die Daten … live **gegen das Datenschema validiert**". **Die zwei Ebenen heißen im Deutschen `technisch` ↔ `fachlich`**, und INNOQ definiert beide im Fließtext: „**technischen Validierungen** wie ‚dieser Wert muss eine Zahl sein'" gegen „**fachlichen Validierungen** wie ‚in Zustand XY muss Objekt A eine Beziehung zu B haben'". ⛔ *schemabasierte Prüfung*, *Validierung auf Schemaebene* sind Neuprägungen. *(DE-Pilot 2026-07-28.)* |
| **Endlosschleife** | **die** Endlosschleife | die Endlosschleifen | der Endlosschleife | **SETTLED.** DWDS-Lemma mit eigenem EDV-Sinn und flektierten Belegen aus *Die Zeit* und *c't*: „dass Anwendungen **in einer Endlosschleife landeten**". Rektion: **in + Dativ**. Die Ausstiegsbedingung heißt **die Abbruchbedingung** (de.wikipedia: „Fehlerhafte Abbruchbedingungen verursachen häufig unbeabsichtigte Endlosschleifen"). Gehört sachlich zur Retry-Familie in §1.1.d, steht aber hier, weil das **Wörterbuch** sie entscheidet. *(DE-Pilot 2026-07-28.)* |
| **Stellschraube** | **die** Stellschraube | die Stellschrauben | der Stellschraube | **SETTLED — und die Übertragung ist LEXIKALISIERT, kein Bild aus zweiter Hand.** DWDS-Sinn 2 wörtlich: „Einflussgröße, durch deren flexible Anwendung ein Vorgang oder ein Ergebnis gezielt verändert und angepasst werden kann". Attestierte Verben: **drehen** („an allen Stellschrauben drehen"), **justieren**. Das ist die deutsche Wiedergabe für *the knobs that control this*. ⛔ *die Knöpfe* ist ein Kalk — ein Knopf wird gedrückt, nicht graduell verstellt. *(DE-Pilot 2026-07-28.)* |

### §1.1.b RAG, Modelle, Evaluation

| Terminus | Artikel | Plural | Genitiv Sg. | Status / Beleg |
|---|---|---|---|---|
| Reranker | **der** Reranker | die Reranker | **des Rerankers** (belegt) | **WEAK** — genitivmarkiert: „**Der Einsatz eines Rerankers** …", „**Der** Reranker analysiert jedes Dokument" <https://blog.mayflower.de/20544-rag-reranker.html>. *Reranking* als artikeltragendes Substantiv wurde **nicht** gefunden → **das Reranking** bleibt HOUSE (`-ing`-Analogie). **Hausschreibung: *Reranking*, nicht *Re-Ranking*** — die Fachprosa mischt beides in einem Artikel, der Korpus wählt eine Form. *Neubewertung* ist die **Glosse**, *Nachsortierung* hat **keine deutsche Attestierung**. |
| Vektordatenbank | **die** Vektordatenbank | die Vektordatenbanken | der Vektordatenbank | **WEAK — sauberer German-led-Sieg**, siehe §1.1.g. de.wikipedia-Lemma **Vektordatenbank**, das der Artikel durchgängig verwendet <https://de.wikipedia.org/wiki/Vektordatenbank>; heise ebenso, bis in die Überschrift („Moderne **Vektordatenbanken** im Marktüberblick"). **„Vector Database" nie in deutscher Prosa schreiben.** |
| Wissensbasis / Wissensdatenbank | **die** Wissensbasis / **die** Wissensdatenbank | die Wissensbasen / -datenbanken | der Wissensbasis | **WEAK (Usus) + HOUSE (Aufteilung).** de.wikipedia-Lemma ist **Wissensdatenbank**; *Wissensbasis* ist der etablierte Terminus wissensbasierter Systeme („Inferenzmaschine und **Wissensbasis** sind die beiden zentralen Komponenten"). Beide zirkulieren in RAG-Prosa, oft in einem Satz. **Hausaufteilung (keine Quelle unterscheidet sie):** *die Wissensbasis* = das abstrakte Wissen, über das ein System schließt; *die Wissensdatenbank* = der konkrete gespeicherte Bestand. **„Knowledge Base" in deutscher Prosa: verloren, nicht verwenden.** |
| Kontextfenster | **das** Kontextfenster | die Kontextfenster | des Kontextfensters | **WEAK — German-led**, §1.1.g. heise definiert es so: „**Das Kontextfenster**: Die Menge an Eingabetext, die das Modell zu einem bestimmten Zeitpunkt betrachten kann"; im Nachrichtenteil durchgängig („ein Kontextfenster von 64.000 Token"). Genus/Plural folgen automatisch aus *das Fenster*. **„Context Window" außerhalb von Herstellerdoku nicht gefunden.** |
| Halluzination | **die** Halluzination | die Halluzinationen | der Halluzination | **SETTLED — German-led, mit eigener KI-Bedeutung im Duden.** Bedeutung 2, markiert *künstliche Intelligenz*: „durch KI erzeugte, nicht auf Fakten oder realen Daten basierende falsche, jedoch glaubhaft erscheinende Information" <https://www.duden.de/rechtschreibung/Halluzination>. Eigenes de.wikipedia-Lemma *Halluzination (Künstliche Intelligenz)*. **„die Hallucination": keine deutsche Attestierung auf irgendeiner Stufe.** Verb *halluzinieren* ist Duden- und DWDS-belegt. |
| Goldstandard | **der** Goldstandard | die Goldstandards | des Goldstandards | **SETTLED** — Duden, Bedeutung 2: „dem erreichten wissenschaftlichen, technischen Stand entsprechende Vorgehensweise, [medizinische] Methode o. Ä." <https://www.duden.de/rechtschreibung/Goldstandard>. **Die Korpusform für *golden set / golden dataset*** — deutsche Prosa schreibt *Golden Dataset (Goldstandard-Datensatz)*; **„Golden Set" hat praktisch keine deutsche Attestierung.** |
| **Ground Truth** | **OPEN** | — | — | **OPEN — und bewusst nicht geraten.** Kein deutscher Satz weist dem Ausdruck einen Artikel zu. *die* (nach *die Wahrheit*) und *der* (nach *der Grund*) sind **beide** begründbar — genau die Signatur einer Zeile, die man nicht ausfüllt. *Grundwahrheit* existiert, wird in der deutschen Wissenschaftsprosa aber selbst infrage gestellt (DH-Konferenzbeitrag: „**Ground Truth: Grundwahrheit oder Ad-Hoc-Lösung?**"). **Praxis: artikelfrei verwenden** („als Ground Truth dienen", „die Ground-Truth-Labels") oder auf **Goldstandard** ausweichen. *Was es entscheiden würde:* ein Satz mit „die/der Ground Truth" bei heise, iX oder dpunkt. |
| **Recall / Precision** | **DISPUTED — artikelfrei verwenden** | — | — | **DISPUTED — die deutschen Quellen widersprechen einander.** *Deutsche Seite (Stufe 3):* de.wikipedia führt die deutschen Termini und setzt das Englische in Klammern — „**Die Trefferquote** gibt den Anteil … an" (*recall*), „**Die Genauigkeit** beschreibt …" (*precision*) <https://de.wikipedia.org/wiki/Beurteilung_eines_binären_Klassifikators>. *Englische Seite (Stufe 4, modernes ML):* das Fraunhofer-Institut IKS behält alle vier Metriknamen englisch — „Maschinelles Lernen wird häufig durch Metriken wie **Accuracy, Precision, Recall und F1-Score** bewertet." **Incumbent (kept-EN) wird gehalten**, mit einem inhaltlichen Zusatzgrund: „**Genauigkeit**" ist im Deutschen auch die übliche Wiedergabe von *accuracy*, eine deutsch geführte Metriktabelle kollidiert also mit sich selbst. Einmal glossieren „(dt. Trefferquote / Genauigkeit)", dann artikelfrei (*der Recall-Wert*, *die Precision-Kurve*). |
| Top-k | — (Variablenausdruck) | — | — | **HOUSE — Schreibung, nicht Genus.** Deutsche RAG-Prosa schreibt die Variable **klein und durchgekoppelt**: „die **Top-k-Dokumente**", „**des k-Werts**", „ein höherer **top-k-Wert**". **Hausform: `Top-k` allein, `Top-k-Dokumente` / `Top-k-Wert` im Kompositum, nie „Top k Dokumente".** Am Satzanfang groß (§ Typografie). *(Die Durchkopplungsbegründung folgt §1.3.3; die Kleinschreibung des `k` ist eine Usus-Beobachtung, keine Norm.)* |
| **Grammatik** (formal) | **die** Grammatik | die Grammatiken | der Grammatik | **SETTLED auf Stufe 3/4 — nicht auf Stufe 1/2.** Weder Duden noch DWDS führen einen formalsprachlichen Sinn. de.wikipedia: „eine **kontextfreie Grammatik** … ist **eine formale Grammatik**"; LMU-Skript *Formale Sprachen und Komplexität* mit vollem Paradigma. **`kontextfrei` ist ein Wort** — 51 : 0 gegen „kontext-frei". Verb: **überführen / transformieren** („das Schema **in eine Grammatik überführen**"); ⛔ **„eine Grammatik kompilieren" = 0 Belege**. ⚠ Das **Substantiv** *die Überführung* nicht als Etikett verwenden — isoliert liest es forensisch („jemanden überführen"); der Kaltleser des Piloten ist genau dort gelandet. Nackt: **die Umwandlung**. *(DE-Pilot 2026-07-28.)* |
| **wohlgeformt** | Adjektiv | — | — | **SETTLED auf Stufe 3/4 — und Stufe 1/2 belegt den FALSCHEN Sinn.** Duden `wohlgeformt` führt **ausschließlich** „von guter, vollkommener Form; ästhetisch ansprechend geformt" („sein Kopf ist wohlgeformt"). Der formalsprachliche Sinn steht bei de.wikipedia (*Syntax*, *XML*) und in Hochschulmaterial: „Ein XML-Dokument heißt **wohlgeformt** …, wenn es alle XML-Regeln einhält." Zusammenschreibung: 51 : 0. ⚠ **Der Gegenpol ist im Deutschen schon vergeben:** das etablierte Paar ist *wohlgeformt ↔ **gültig/valide***, und *gültig* heißt dort **schemakonform**. Wo unser Text *well-formed ↔ correct* meint, muss der Gegenpol **„fachlich richtig"** heißen — sonst liest ein XML-kundiger Leser das Gegenteil. *(DE-Pilot 2026-07-28.)* |
| **Prompt-Engineering** | **das** Prompt-Engineering | — | des Prompt-Engineerings | **SETTLED.** heise-Ratgeber: „**Prompt-Engineering** … ist die Kunst … eine Anweisung so zu formulieren"; im selben Text „Diese Anweisung, **der Prompt**". Keine Glosse nötig; *Promptdesign* markiert heise selbst als „seltener". *(DE-Pilot 2026-07-28.)* |

### §1.1.c Agenten und Tools

| Terminus | Artikel | Plural | Genitiv Sg. | Status / Beleg |
|---|---|---|---|---|
| Hook | **der** Hook (Hausform) | die Hooks | des Hooks | **WEAK — Genus NICHT attestiert.** de.wikipedia-Lemma **Hook (Informatik)**: „Hook (englisch für Haken, auch **Einschubmethode** genannt) bezeichnet in der Programmierung eine Schnittstelle …" <https://de.wikipedia.org/wiki/Hook_(Informatik)> — das Lemma flektiert nie. Agentensinn bei heise nur im Plural („Skills und **Hooks** automatisieren …"). Maskulinum als **Analogie** (`-er`/einsilbige englische Sachnomina, *der Haken*), nicht als Beleg. |
| Skill | **der** Skill (Hausform) | die Skills | des Skills | **WEAK — Genus nicht attestiert.** Zwei heise-Belege, beide Plural, beide im Agentensinn: „**Skills** und Hooks automatisieren …", „aus Werkzeugen, Kontext, **Skills** und Regeln" <https://www.heise.de/hintergrund/Kurz-erklaert-Agent-Harness-11330445.html>. *die Fähigkeit* existiert, aber nur im allgemeinen Sinn — **kein** Konkurrent für das gepackte Anweisungsbündel. |
| Checkpoint | **der** Checkpoint | die Checkpoints | des Checkpoints | **WEAK — und eine Musterfalle.** Duden **und** DWDS haben das Lemma („der Checkpoint; des Checkpoints; die Checkpoints") — aber **nur im Sinn „Kontrollpunkt an Absperrungen, Grenzübergängen"** <https://www.duden.de/rechtschreibung/Checkpoint>. Der ML-Sinn ist **nur im Fachjournalismus** belegt (heise: *Checkpoints* für gespeicherte Modellgewichte). **Das Genus ist morphologische Übertragung aus dem Grenzsinn, nicht Beleg für unseren.** Eine Zeile, die den Duden hier für den ML-Sinn zitierte, sähe tadellos aus und wäre belegfrei. |
| Multiagentensystem | **das** Multiagentensystem | die Multiagentensysteme | des Multiagentensystems | **WEAK — beide Schreibungen sind attestiert, der Kanon wählt.** de.wikipedia-Lemma ist die **geschlossene** Form: „Bei einem **Multiagentensystem** oder MAS handelt es sich um ein System aus mehreren … Software-Agenten" <https://de.wikipedia.org/wiki/Multiagentensystem>, und das Lemma nennt *Multi-Agenten-System* **nicht** als Variante. Die durchgekoppelte Form ist im Fachjournalismus trotzdem normal („**Multi-Agenten-Systeme** setzen auf Zusammenarbeit statt zentrale Steuerung", heise). **Hausform: *Multi-Agenten-System*** — sie fügt sich in die Durchkopplungslinie des Korpus (§1.3.3) ein; die Lemmaform bleibt als Nebenform zulässig und wird in Zitaten nicht angetastet. |
| **Handoff** | **OPEN** | — | — | **OPEN — keine Attestierung auf irgendeiner Stufe.** *(Ein Suchtreffer schien „Handoffs (Übergaben)" zu zeigen; beim tatsächlichen Abruf der Seite war weder *Handoff* noch *Übergabe* vorhanden — die Zeile steht deshalb leer statt mit einem Phantombeleg.)* **Korpusform: die Übergabe** („die Übergabe an den nächsten Agenten"). *Was es entscheiden würde:* ein flektierter deutscher Satz bei heise/iX/dpunkt oder ein de.wikipedia-Agentenlemma. |
| **Blast Radius** | **OPEN** | — | — | **OPEN.** Keine Attestierung auf den Stufen 1–5. Vorhanden sind nur Übersetzungsmedien und Herstellerblogs; **Mimecast DE rendert *Explosionsradius*** — ein wörtlicher Kalk mit MT-Signatur, **disqualifiziert**. ⚠ **Namenskollision:** die deutsche Sicherheitspresse verwendet „Blast-RADIUS" massiv für eine RADIUS-Protokollschwachstelle — jede Suche ist davon verseucht. **Korpusform: die Schadensreichweite** bzw. Glosse „(Reichweite des Schadens, den ein entgleister Agent anrichten kann)". |
| Orchestrator / Orchestrierung | **der** Orchestrator / **die** Orchestrierung | die Orchestratoren / -ungen | des Orchestrators | **SETTLED (Verb) / WEAK (Substantive)** — Duden hat für *orchestrieren* eine ausdrückliche **EDV**-Bedeutung: „(mehrere informationstechnologische Einzelvorgänge zu einem Geschäftsprozess) miteinander verknüpfen, kombinieren" <https://www.duden.de/rechtschreibung/orchestrieren>. de.wikipedia verwendet beide Substantive („**Ein Orchestrator** übernimmt Planung, Softwarewerkzeug-Auswahl und autonome schrittweise Ausführung"). **Nachtrag DE-Pilot (2026-07-28) — die Flexion ist schwächer belegt als der Nominativ.** Sinnidentisch und nativ ist nur der **Nominativ** (informatik-aktuell: „**Der Orchestrator** legt die Reihenfolge fest, in der die Microservices aufgerufen werden"); **ein obliquer Kasus konnte in KEINER Nicht-MT-Quelle belegt werden** — das Paradigma oben ist insoweit **erschlossen**. Praktische Folge: *der Orchestrator* ist das **Eskalationswort für die Koordination selbst** (Fan-out/Fan-in, Reihenfolge), **nicht** die Standardwahl für den Laufzeit-Referenten — dort steht **Ihre Anwendung / Ihr Code**. ⛔ **`die Orchestrierungsschicht` = OPEN** (null native Treffer; heise greift zum englischen *Orchestration-Layer*) → **die Steuerungsschicht**, siehe `rag.md` §3. |
| **Seiteneffekt** | **der** Seiteneffekt | die Seiteneffekte | des Seiteneffekt(e)s | **SETTLED nach gemessenem Usus: 16 : 2 : 0** (Seiteneffekt : Nebeneffekt : Nebenwirkung) über 24 deutsche CS-Quellen. DWDS-Korpusbeleg im richtigen Sinn, akkusativmarkiert: „sie hat **einen Seiteneffekt**". ⚠ **Nebenwirkung ist der falsche Freund** — DWDS-Sinn 2 „unerwünschte zusätzliche Wirkung eines Medikaments", alle Belege pharmazeutisch. ⚠ *Nebeneffekt* schwächt ab (Duden: „weniger wichtiger … Effekt") und ist für ein Tool, das Geld abbucht, sachlich falsch. **Gegenstimme protokolliert:** de.wikipedias Lemma ist *Wirkung (Informatik)* und nennt *Seiteneffekt* puristisch eine „Rückübersetzung" — das ist eine Sprachkritik, kein Usus, und der Usus steht 16 : 0 dagegen. ⚠ **Belegstufe ehrlich:** die DWDS-*Seite* führt das Wort, der **Eintrag** tut es nicht (der Grammatikblock ist dort „computergeneriert") — die Korpussätze sind der Beleg, der Kasten darüber nicht. *(DE-Pilot 2026-07-28.)* |
| **Idempotenz** | **die** Idempotenz | — | der Idempotenz | **SETTLED.** de.wikipedia führt Mathematik **und** Informatik in einem Lemma, inkl. unseres Retry-Sinns: „eine Operation so häufig wiederholt oder erneut versucht werden kann wie notwendig, ohne unbeabsichtigte Auswirkungen zu verursachen". Flexionstragend bei informatik-aktuell („durch **die** vorhandene Idempotenz"), JAX.de („Eigenschaft **der** Idempotenz"). Adjektiv **idempotent**. ⚠ Duden hat keinen brauchbaren Eintrag, DWDS „nicht genügend Daten" — die Zeile steht auf Stufe 3+5, nicht auf Stufe 2. *(DE-Pilot 2026-07-28.)* |
| **Idempotency-Key** | **der** Idempotency-Key | die Idempotency-Keys | des Idempotency-Keys | **HOUSE.** *Idempotenzschlüssel* = **0 Belege**, *Idempotency Key* = 0 Belege in deutscher Fachprosa (24 Quellen geprüft, englisches Zwillingswort mitgegrept). Genus per attestiertem Kopfnomen: heise „**einen eigenen** API-Key … **Dieser** API-Key" → `-Key` ist maskulin. Schreibung durchgekoppelt, passend zum HTTP-Header `Idempotency-Key`. ⚠ **MDN de disqualifiziert** — „Diese Seite wurde automatisch aus dem Englischen übersetzt." Es war der einzige direkte Genusbeleg. ⚠ **Schreibungskorrektur, mitgezogen am 2026-07-28:** der Injektionsblock und §1.0 führten den Terminus als „der Idempotency Key" **getrennt** — das ist nach dem eigenen § 45 E1 (§1.3.3) im deutschen Satz **nicht normgerecht**; beide Stellen stehen jetzt mit Bindestrich. Die **Zitierform** in `rag.md` §2 bleibt getrennt, weil jene Liste ausdrücklich Zitierform ist. *(DE-Pilot 2026-07-28.)* |
| **Namensraum** | **der** Namensraum | die Namensräume | des Namensraums / -raumes | **SETTLED.** de.wikipedia: „**Der Namensraum** (englisch *namespace*) ist ein Begriff aus der Programmierung"; beide Genitivvarianten im Artikel belegt. ⚠ **`das Namespacing` = 0 Vorkommen** — die `-ing`-Nominalisierung überlebt hier **nicht** ins Deutsche (die Ausnahme zur `-ing`-Heuristik in Falle 2 oben). Für den Vorgang eine **Verbalphrase**: „nach Namensräumen gruppieren". *(DE-Pilot 2026-07-28.)* |

### §1.1.d Betrieb, Serving, Infrastruktur

| Terminus | Artikel | Plural | Genitiv Sg. | Status / Beleg |
|---|---|---|---|---|
| Rate Limit | **das** Rate Limit | die Rate Limits | des Rate Limits | **WEAK — und der deutsche Konkurrent steht auf einer HÖHEREN Stufe.** heise, artikeltragend: „GitHub führt … **ein Rate Limit** für die Audit-Log-API ein", „Derzeit ist **das Rate Limit** unabhängig von der Komplexität" <https://www.heise.de/news/GitHub-fuehrt-im-August-Rate-Limit-fuer-die-Audit-Log-API-ein-9207335.html>; ebenso „**das Rate Limiting**". **Gegenlage:** de.wikipedias Lemma heißt **Durchsatzratenbegrenzung** und der Artikel verwendet ausschließlich die deutsche Form. Der Kanon nimmt den Loan, **weil die deutsche Form außerhalb ihres eigenen Enzyklopädieeintrags nirgends vorkommt** — aber die Zeile ist ehrlich WEAK, nicht settled. *Ratenbegrenzung* ist nur bei MDN de und Microsoft Learn de-de belegt → **disqualifiziert** (Microsoft behält `rate-limit` auf der eigenen Azure-Seite englisch). |
| Rollback | **das** Rollback | die Rollbacks | des Rollback[s] | **WEAK für den IT-Sinn / SETTLED für das Paradigma.** ⚠ **Dudens drei Bedeutungen sind Kalter Krieg und „Rückschritt" — kein EDV-Sinn** <https://www.duden.de/rechtschreibung/Rollback>; das Paradigma („das Rollback, des Rollback[s], die Rollbacks") ist dort aber verbindlich. Der IT-Sinn steht auf Stufe 3 **mit demselben Genus**: „**Das** Rückgängigmachen der Effekte einer Transaktion wird als **Rollback** … bezeichnet", „bei **einem** Rollback" <https://de.wikipedia.org/wiki/Transaktion_(Informatik)>. *Zurückrollen* ist als Nominalisierung belegt, aber kein Terminus; *Rücknahme*, *Wiederherstellung*: keine Attestierung. |
| Canary Release | **das** Canary Release | die Canary Releases | des Canary Release[s] | **WEAK** — neutrum, dreifach artikeltragend bei informatik-aktuell: „**das** Konzept **des Canary Releasing**", „**Das** Canary Releasing ist gewissermaßen die Weiterentwicklung von Blue-/Green-Deployments", „**Das** Canary Releasing ermöglicht … ein reibungsloses Zurückrollen". heise attributiv: „Chrome jetzt auch für Android als **Canary-Release** verfügbar". **„Kanarienvogel-Release": keine deutsche Attestierung auf irgendeiner Stufe** — der Vogel erscheint nur als Etymologie-Nebensatz. |
| **Cold Start** | **der** Cold-Start (Incumbent) | die Cold-Starts | des Cold-Starts (belegt) | **DISPUTED — und der Widerspruch steht in EINEM deutschen Artikel.** openknowledge.de schreibt auf derselben Seite „die Dauer eines »**Kaltstarts**«" **und** „die tatsächliche Dauer eines **Cold-Starts**" **und** „einen **Cold-Start** zu vermeiden" <https://www.openknowledge.de/von-less-server-zu-serverless-eine-reise-durch-die-cloud/>. Erschwerend: *Kaltstart* ist im Deutschen **zweifach besetzt** — de.wikipedia führt den **Motorensinn**, und heise verwendet es prominent für den **Rechenzentrums-Kaltstart** (Black Start), einen dritten Sinn. Drei heise-Serverless-Artikel enthalten **weder** *Cold Start* **noch** *Kaltstart*. **Incumbent halten, nichts ändern.** |
| **Backpressure** | **OPEN (Artikel)** | — | — | **OPEN — in jedem nativen Beleg ARTIKELLOS.** informatik-aktuell: „Flow Control durch **non-blocking Back Pressure**" — Massenbegriff ohne Artikel. Dieselbe Quelle liefert einen vierten deutschen Kandidaten, den niemand vorgeschlagen hatte: „nicht-blockierendem **Rückdruck**" (ein einziges Vorkommen). *Gegendruck* und *Rückstau* stammen aus einer KI-generierten Glossar-Contentfarm → **disqualifiziert**. **Praxis: artikellos verwenden** („Backpressure greift, wenn …") oder umformulieren („die Flusskontrolle", „die Regelung der Datenrate"). *Was es entscheiden würde:* ein Satz mit „der/das Backpressure" bei heise/iX/dpunkt/Rheinwerk. |
| **Load Shedding** | **OPEN** | — | — | **OPEN — und die Überraschung fällt andersherum aus, als der Auftrag erwartete.** *Lastabwurf* ist ein starkes, etabliertes deutsches Wort — de.wikipedia führt es **zweimal**, beide Male **Stromnetz/Kraftwerk**, kein IT-Lemma. Und die deutsche Fachpresse übernimmt **weder** *Lastabwurf* **noch** *Load Shedding*: heise- und informatik-aktuell-Resilienzartikel zählen Retries, Fallbacks und Circuit Breaker auf und haben für diesen Vorgang **kein Wort**. Einzige IT-Verwendung: die deutsche AWS-Builders-Library-Seite („Ziel **des Lastabwurfs** ist es, die Wartezeit … gering zu halten") — in sich stimmig, deshalb **nicht disqualifiziert**, aber eine einzelne Herstellerseite. **Korpusform: den Vorgang beschreiben** („Anfragen gezielt abweisen", „Last gezielt abwerfen"). |
| Feature Flag | **das** Feature Flag | die Feature Flags | des Feature Flags | **WEAK — pronominal gesichert.** heise: „**Ein Feature Flag, das** ursprünglich für Testzwecke existierte …" — das Relativpronomen *das* pinnt das Neutrum; derselbe Artikel: „weil **das Flag** dort nicht korrekt gesetzt war" <https://www.heise.de/hintergrund/Aus-Softwarefehlern-lernen-Teil-5-440-Millionen-Dollar-Verlust-in-Minuten-10748532.html>. Das Synonym **Feature Toggle** liefert den Genitiv: „die Aktivierung … **eines Feature Toggles**" (informatik-aktuell). *Schalter* wird nur als **Glosse** gebraucht; *Feature-Schalter* und *Funktionsschalter*: **keine deutsche Attestierung**. |
| Kill Switch | **der** Kill-Switch | die Kill-Switches | des Kill-Switches (*regelhaft*) | **WEAK — mit einer belegten deutschen Alternative.** heise, unmarkiert und artikeltragend: „**Ein zentraler Kill-Switch** schützt vor irreversiblen Schäden." In der KI-Politikberichterstattung steht der Loan **in Anführungszeichen** und im selben Text greift der Autor zum deutschen Wort: „bringen »**Notausschalter**« ins Spiel", „in Form **eines Notausschalters**" <https://www.heise.de/news/Gegen-die-Apokalypse-Wissenschaftler-fordern-Kill-Switch-fuer-KI-9631689.html>. ⚠ **de.wikipedias Lemma *Kill-Switch* ist Tontechnik** (Momentan-Stummschaltung) — kein Beleg für unseren Sinn. |
| Serving | **OPEN als freies Substantiv** | — | — | **OPEN.** Der Loan überlebt im Deutschen **nur in englischen Komposita** („Serving Endpoints", „Serving Logs" bei heise). „**das Serving** von Modellen" mit deutschem Artikel: **keine Attestierung auf irgendeiner Stufe**. Was deutsche Prosa tatsächlich schreibt, ist ein Verb oder ein schlichtes Substantiv: „lässt sich … **ein Endpunkt bereitstellen**", „**die Bereitstellung** trainierter Modelle für Inferenz", Artikeltitel „KI-Modelle produktiv **betreiben**". **Korpusform: die Bereitstellung / der Betrieb**; *Serving* nur in festen englischen Fügungen. |
| **Wiederholung** (retry) | **die** Wiederholung | die Wiederholungen | der Wiederholung | **SETTLED.** Das zählbare Ding heißt im Deutschen *Wiederholung*: informatik-aktuell „auf drei **Wiederholungen** beschränken"; heise glossiert das englische Wort ausdrücklich als Jargon: „und *retry*, **Wiederholung** einer Operation". Verb: **wiederholen** (INNOQ: „Requests zu **wiederholen**"). ⛔ *Wiederholungsversuch* verworfen — DWDS-Belege ausschließlich außerhalb der Informatik. ⛔ *retryen* = 0 Belege auf allen Stufen. *(DE-Pilot 2026-07-28.)* |
| **Retry** (bloßes Lehnwort) | **OPEN (Genus)**, Plural **DISPUTED** | — | — | **OPEN — nur als Kompositumsglied verwenden.** Kein flexionstragender Singular auf irgendeiner Stufe. Der Plural widerspricht sich **innerhalb eines Hauses**: INNOQ schreibt „Retrys" im einen und „Retries" im anderen Artikel. **Regel: nie „ein Retry", immer „die Wiederholung" — `Retry-` bleibt aber als Kompositumsbildner zulässig** (*das Retry-Budget*); siehe den Kasten „Ein Lehnwort kann als KOMPOSITUMSBILDNER überleben" oben. *(DE-Pilot 2026-07-28.)* |
| **Backoff** | **der** Backoff (bloß) | — | des Backoffs | **WEAK — und die Zählung ist der eigentliche Befund.** In de.wikipedias *Binary Exponential Backoff* kommt das Wort **6-mal** vor und **kein einziges Mal** als artikeltragendes Appellativ: es lebt im Eigennamen und im Kompositum („**das** Backoff-**Verfahren**" — *das* gehört zu *Verfahren*, ein Scheingenus). Maskulin belegt nur bei Microsoft Learn (`ms.translationtype: **HT**`, menschlich übersetzt, in sich stimmig → als schwacher Beleg behalten): „(**der** exponentielle Backoff)", „mit **exponentiellem** Backoff". **Korpusform: das Kompositum** — *die Backoff-Strategie*, *die Wartezeit*. ⛔ „exponentielles Backoff" = 0 Belege. *(DE-Pilot 2026-07-28.)* |
| **Race Condition** | **die** Race Condition | die Race Conditions | der Race Condition | **SETTLED.** de.wikipedia-Lemma ist *Wettlaufsituation* mit Weiterleitung von *Race Condition*; femininer Beleg samt Verb: „dass **eine Race Condition entsteht**". **Das deutsche Wort benennt den FEHLER, nicht die Nebenläufigkeit** (Kategorien: Programmfehler, Fehlermanagement) — die slowakische Falle („súbeh" = Nebenläufigkeit) greift im Deutschen also nicht. Verb: **entstehen**. ⛔ „es kommt zu einem Wettlauf", „die Zugriffe geraten in einen Wettlauf" = 0 Belege, englisches Gerüst. *(DE-Pilot 2026-07-28.)* |

### §1.1.e Observability und Messgrößen

| Terminus | Artikel | Plural | Genitiv Sg. | Status / Beleg |
|---|---|---|---|---|
| Observability | **die** Observability | (kein Plural) | der Observability | **WEAK — und der deutsche Konkurrent verhält sich lehrreich.** Femininum belegt: „Um **eine gute** Observability zu erreichen …" (objektkultur), „Observability dient aber nicht nur zur Fehlererkennung. Viel mehr will **sie** …" (heise). **Die Beobachtbarkeit ist gut belegt — aber strukturell IMMER als Einführungsglosse:** „Observability – oder auf Deutsch *Beobachtbarkeit* – beschreibt die Fähigkeit …", und danach läuft der Text wieder mit *Observability*. **Genau dieses Muster baut der Korpus nach: einmal glossieren, dann kept-EN weiterlaufen** (§7 Brückenrichtung). **Disqualifiziert:** Google Cloud de führt *Beobachtbarkeit* als Laufterm, AWS de lässt *Observability* unübersetzt — zwei Herstellerlokalisierungen, die einander widersprechen. |
| Monitoring | **das** Monitoring | die Monitorings | des Monitorings | **SETTLED** — Duden, richtiger Sinn: „[Dauer]beobachtung [eines bestimmten Systems]" <https://www.duden.de/rechtschreibung/Monitoring>. *die Überwachung* wird in deutscher Prosa **kontrastiv** eingesetzt („Reaktive Überwachung" vs. „Proaktive Ursachenanalyse"), nicht als Ersatz. |
| Metrik | **die** Metrik | die Metriken | der Metrik | **SETTLED (Morphologie) / WEAK (IT-Sinn).** ⚠ Dudens *Metrik* ist **Verslehre und Musik** <https://www.duden.de/rechtschreibung/Metrik> — die Morphologie überträgt sich gefahrlos (dasselbe Wort), die Bedeutung liefert Stufe 3: „Eine **Softwaremetrik**, oder kurz **Metrik**, ist eine … Funktion, die eine Eigenschaft von Software in einen Zahlenwert … abbildet" <https://de.wikipedia.org/wiki/Softwaremetrik>. |
| Telemetrie | **die** Telemetrie | (Plural meiden) | der Telemetrie | **SETTLED (Genus) / WEAK (Softwaresinn).** Duden: feminin, „Übertragung von Messwerten …; Fernmessung" <https://www.duden.de/rechtschreibung/Telemetrie> — der Softwaresinn ist eine **Dehnung**, die die deutsche Fachprosa aber genau so vollzieht („Die Fähigkeit, diese Daten über mehrere Systeme hinweg zu erfassen, wird als **Telemetrie** bezeichnet"). **Praxis: fast immer das Kompositum *die Telemetriedaten*** („zum Erfassen von **Telemetriedaten** wie Logs, Metriken und Traces", heise). Plural *die Telemetrien* regelhaft ableitbar, **nicht belegt** → meiden. |
| Sampling | **das** Sampling | die Samplings | des Samplings | **WEAK — und der beste Fund dieser Gruppe.** heise, artikeltragend **im Observability-Sinn**: „Metriken und Traces [kommen] in der Regel nur als Stichprobe … an (**Sampling**), … **das Sampling** reduziert die Datenmenge" <https://www.heise.de/news/Drei-Fragen-und-Antworten-Observability-fuer-bessere-Einblicke-und-Vorhersagen-9439537.html> — derselbe Satz zeigt, dass *Stichprobe* die **Erklärung** ist, nicht der Ersatz. ⚠ Dudens *Sampling* ist der **Musiksinn** — er liefert Morphologie, nicht Bedeutung. **Head-based / tail-based bleiben englisch** („Tail-based Sampling"): für eine übersetzte Form gibt es **keine deutsche Attestierung**. |
| Instrumentierung | **die** Instrumentierung | die Instrumentierungen (*regelhaft*) | der Instrumentierung | **WEAK — German-led, und zwar klar**, §1.1.g. Vier unabhängige Belege (heise ×3, INNOQ): „die Qualität **der Instrumentierung**", „**Auto-Instrumentierung** deckt Dependencies … ab", „Normierungen … für **die Instrumentierung** von Apps". **Das englische *Instrumentation* erscheint im Deutschen nur als Teil von Eigennamen/API-Namen** („Instrumentation API"), nie als freies Substantiv. |
| **Drift** | **der** Drift (Incumbent) | die Drifts | des Drifts | **DISPUTED.** Duden hat **zwei** Lemmata, **keines im ML-Sinn**: *die* Drift (Strömung, ozeanographisch, Plural *Driften*) und *der* Drift (Motorsport). Deutsche ML-Prosa spaltet sich: die stärkste einzelne Fachquelle (Vogel IT-Medien) ist durchgehend **maskulin** („**der** Model Drift", „**ein** Konzeptdrift"), andernorts steht ein rückverweisendes feminines Pronomen. **Incumbent *der Drift* halten** — Begründung: das maskuline Duden-Lemma ist das *moderne technische*, das feminine das seemännisch-ozeanographische. **Praxis: möglichst das Kompositum schreiben** — *die Datendrift*, *der Modelldrift*, *der Konzeptdrift* sind besser belegt als das bloße Wort. Der `drift`-Sense-Card im AI-SDLC-Ledger bleibt davon unberührt. |
| Fehlerbudget | **das** Fehlerbudget | die Fehlerbudgets | des Fehlerbudget[e]s | **WEAK — German-led**, §1.1.g. **Zwei unabhängige deutsche Fachhäuser schreiben durchgängig *Fehlerbudget*:** Computerwoche („So managen Sie SLOs und **Fehlerbudgets**") — die englische Form kommt im ganzen Artikel **kein einziges Mal** vor — und iX 9/2017 („Definierte **Fehlerbudgets** schaffen Freiräume …"). Der Loan lebt in der Beraterprosa weiter, verliert aber auf der höheren Quellenstufe. |
| SLA / SLO | **das** SLA / **das** SLO | die SLAs / die SLOs | des SLAs / des SLOs | **WEAK — weniger gespalten als erwartet, beide Neutrum.** de.wikipedia: „**Ein** Service-Level-Agreement (SLA …)", „**eines SLA**" <https://de.wikipedia.org/wiki/Service-Level-Agreement> — **beachte die Lemmaschreibung mit Bindestrichen**, wenn ausgeschrieben. SLO artikeltragend: „**Ein** Service Level Objective (SLO) ist ein messbares Ziel", „**Ein gutes SLO** ist realistisch …". |
| **SLI** | **das** SLI (Hausform) | die SLIs | des SLIs | **OPEN — kein artikeltragender Beleg gefunden**, nur artikellose Aufzählungen („Service Level Indicators (SLI) und Service Level Objectives (SLO) legen fest, …", iX 9/2017). **Die Falle ist echt:** das Kopfnomen *der Indikator* spräche für **der** SLI, während die Dreiergruppe für **das** spricht. **Hausform *das SLI* ist Paradigmenausgleich innerhalb der Gruppe (das SLA / das SLO / das SLI), keine Kopfnomen-Ableitung und kein Beleg** — das steht hier ausdrücklich. *Was es entscheiden würde:* ein Satz „das SLI ist …" / „der SLI wird …" in iX, c't, INNOQ oder einem deutschen SRE-Fachbuch. |
| Evaluierung / Eval | **die** Evaluierung / **das** Eval (Hausform) | die Evaluierungen / die Evals | der Evaluierung / des Evals | **SETTLED (Evaluierung) / HOUSE (Eval).** **Die vermutete österreichische Markierung von *Evaluierung* existiert nicht** — Duden und DWDS führen *Evaluation* und *Evaluierung* als **synonym und unmarkiert**; markiert ist allein *Evaluation* als *bildungssprachlich* <https://www.duden.de/rechtschreibung/Evaluierung>. In deutscher KI-Prosa **dominiert *Evaluierung*** („LLMs als Tools zur **Evaluierung** von RAG-Systemen", ORDIX; „Eine **Evaluierung** auf deutsche Benchmarks", ontolux). Das zählbare *Eval* verwendet heise nur **großgeschrieben-abkürzungsartig und ohne Artikel** („Large Language Models testen mit **EVALs**") — **das Genus ist nicht belegt**; *das Eval* ist Analogie zu *das Log / das Tool / das Setup / das Update*. **Hausaufteilung: *die Evaluierung* für den Vorgang, *das Eval / die Evals* nur für den zählbaren Testfall.** |
| **Grader** | **der** Grader (Hausform) | die Grader | des Graders | **OPEN — zero German attestation at any tier** für die KI-Evaluationsbedeutung. Was deutsche Prosa stattdessen bildet: **die Bewertungsinstanz**, **der KI-Bewerter**, **das Bewertungsmodell**. **Korpusform: der Bewerter / das Bewertungsmodell.** Wird der Loan als API-Name gebraucht, gilt die Hausform oben — **Analogie** zu englischen `-er`-Agensnomina mit Nullplural (*der Router / die Router*), **kein Beleg**. |

### §1.1.f Softwareprozess, Sicherheit, Governance

**Diese Gruppe verhält sich anders als alle anderen — hier hat das Deutsche echtes eigenes Vokabular**
(*Prüfung, Freigabe, Nachweis, Zuständigkeit, Funktionstrennung*), und die **BSI** ist als Stufe-1-Quelle
tatsächlich ergiebig. Fünf von zwanzig geprüften Zeilen sind deutsch geführt (§1.1.g).

| Terminus | Artikel | Plural | Genitiv Sg. | Status / Beleg |
|---|---|---|---|---|
| Merge (Substantiv) | **der** Merge | die Merges (*regelhaft*) | des Merge / Merges (schwankend) | **WEAK** — das deutsche Substantiv **wird** verwendet: „Wer veranlasst **den Merge** nach Abnahme?", „bei dem Versuch **eines Merge** des Features in den Main Branch" (heise). de.wikipedia glossiert die Handlung deutsch: „was als *Merging*, **zu deutsch verschmelzen**, bezeichnet wird". *Zusammenführung* als Terminus: **keine Attestierung** — als **Verb** ist *zusammenführen* dagegen DWDS-Synonym zu *mergen* (§1.3.2). |
| Pull Request | **der** Pull Request | die Pull Requests | des Pull Requests (*regelhaft*) | **WEAK** — „Wie viele Reviewer müssen **den Pull Request** genehmigen?", „die Bearbeitung von **Pull Requests**", attributiv durchgekoppelt „**Pull-Request-Workflows**" (heise). **Merge Request** (GitLab) hat **keine** eigenständige deutsche Attestierung → dasselbe Paradigma **per Analogie** (HOUSE). |
| Code-Review | **das** Code-Review (Hausform; *der* zulässig) | die Reviews | des Reviews | **SETTLED für die Varianz, HOUSE für die Wahl — und „die Code-Review" fällt raus.** de.wikipedia-Lemma *Review (Softwaretest)* sagt es wörtlich: „**Der oder das Review** ist eine statische Testmethode …" <https://de.wikipedia.org/wiki/Review_(Softwaretest)> — die Quelle lizenziert *der* **und** *das* und **schließt *die* aus**. Hausform **das Code-Review** (Analogie *das Interview*). *Quelltextprüfung*, *Codeprüfung*, *Programmdurchsicht*: im Lemma nicht vorhanden, **nicht etabliert**. |
| Testabdeckung / Code Coverage | **die** Testabdeckung / **die** Code Coverage | die Testabdeckungen | der Testabdeckung | **SETTLED (deutsches Lemma) — beide Formen sind korrektes Deutsch.** de.wikipedia-Lemma **Testabdeckung**, das *Codeabdeckung* gleichwertig verwendet und „Test Coverage bzw. Code Coverage" glossiert. heise verwendet den Loan **feminin**: „**Eine** besonders verführerische Metrik … ist **die Code Coverage**". **Hausform: die Testabdeckung** als Lemma, *die Code Coverage* im laufenden Fachtext zulässig. |
| Statische Code-Analyse / **Linter** | **die** statische Code-Analyse / **Linter: OPEN** | — | der statischen Code-Analyse | **SETTLED (Begriff) / OPEN (das Agensnomen).** de.wikipedia: „**Statische Code-Analyse** … ist ein statisches Software-Testverfahren", und: „In Anlehnung an das klassische Programm *Lint* wird der Vorgang auch als **linten** bezeichnet." **Das Verb ist etabliert (§1.3.2), das Substantiv *Linter* hat keinen Genusbeleg** — OPEN. *Was es entscheiden würde:* ein Satz mit Artikel auf *Linter* in c't/iX oder einem deutschen Fachbuch. |
| Quality Gate | **das** Quality Gate | die Quality Gates | des Quality Gates (*regelhaft*) | **SETTLED (Usus, frisch nachgeprüft)** — „**Quality Gates** in der Entwicklung helfen beim Prüfen der Einhaltung von Qualitätsanforderungen"; „SonarQube … erlaubt es, auf Projektebene unabhängige **Quality Gates** anzulegen" <https://www.heise.de/ratgeber/Shift-Left-Secure-by-Design-und-agile-Entwicklung-4613935.html?seite=4>. Neutrum aus deutscher PM-Prosa („**Ein** Qualitygate **ist ein** bestimmter Zeitpunkt …"). **Dass *Qualitätstor* NICHT etabliert ist, sagt die deutsche Quelle selbst**: „Qualitygates (**deutsch in etwa**: Qualitätstore)" — „in etwa" ist das Eingeständnis. **Stage-Gate** ist als **der Stage-Gate-Prozess** etabliert; **Release Gate: OPEN**, keine deutsche Attestierung. |
| **Secret** → **das Geheimnis** | **das** Geheimnis | die Geheimnisse | des Geheimnisses | **SETTLED — German-led, Stufe 1, und die Vermutung im Auftrag war falsch.** Das BSI-Grundschutz-Baustein zu Secrets Management verwendet **Geheimnis** als laufendes deutsches Substantiv genau für den Zugangsdaten-Sinn: „Bei den zu verwaltenden **Geheimnissen** handelt es sich zum Beispiel um vertrauliche Umgebungsvariablen, Datenbankanmeldeinformationen, API-Schlüssel …" <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Hilfsmittel/Benutzerdefinierte_BS/BS_Secrets_Management_mit_Hashicorp_Vault.pdf>. **Zählung im ganzen Baustein: *Geheimnis* 5×, *Zugangsdaten* 0×, *Anmeldedaten* 0×, *Credential* 0×.** Englisches *Secret* kommt 17× vor, davon **16× im festen Kompositum „Secrets Management"** — „**das Secret**" mit deutschem Artikel: **null Attestierung auf Stufe 1**. **Korpusform: das Geheimnis; kept-EN nur im festen Terminus *Secrets Management*.** |
| **Least Privilege** → **das Prinzip der geringsten Berechtigungen** / **der minimalen Rechte** | **das** Prinzip | — | des Prinzips | **SETTLED German-led (Stufe 1) — DISPUTED, WELCHE deutsche Form. Diese Zeile war seit dem Bootstrap OPEN, weil die BSI nie geprüft worden war. Sie ist jetzt geprüft.** IT-Grundschutz-Kompendium **ORP.4.A2** (Edition 2023): „Benutzendenkennungen und Berechtigungen DÜRFEN NUR aufgrund des tatsächlichen Bedarfs … vergeben werden (**Prinzip der geringsten Berechtigungen**, englisch Least Privileges und **Erforderlichkeitsprinzip**, englisch Need-to-know)." BSI-Positionspapier **Zero Trust** (04.07.2023): „… welches im Kern auf dem **Prinzip der minimalen Rechte** (engl. „Least Privileges") … basiert." **Beide Dokumente führen den Begriff IMMER mit einer deutschen Vollform ein und stellen das Englische in die Klammer** — die Richtung ist damit entschieden. **Welche Vollform, entscheidet die BSI nicht: sie widerspricht sich zwischen den eigenen Dokumenten** → DISPUTED, und beide bleiben stehen. **Hausaufteilung nach Registerlage:** *Prinzip der geringsten Berechtigungen* im Berechtigungs-/Compliance-Text (die normative Kompendiumsformulierung), *Prinzip der minimalen Rechte* im Architektur-/Zero-Trust-Text. **Keine dritte Form erfinden.** Nebenfund, wertvoll: **Erforderlichkeitsprinzip** ist die BSI-Form für *need-to-know*. |
| **Separation of Duties** → **die Funktionstrennung** | **die** Funktionstrennung | (Plural meiden) | der Funktionstrennung | **SETTLED — German-led, Stufe 1 + Fachverband.** BSI ORP.4 (2023) trägt es im Anforderungstitel: „**ORP.4.A4 Aufgabenverteilung und Funktionstrennung**", und: „… SOLLTE **den Grundsatz der Funktionstrennung** unterstützen." de.wikipedias Lemma **Funktionstrennung** glossiert **beide** englischen Varianten: „(englisch *segregation of duties* oder *separation of duties*; abgekürzt SoD)" <https://de.wikipedia.org/wiki/Funktionstrennung>; es ist zugleich der Terminus der Wirtschaftsprüfung (IDW). *Aufgabentrennung* und *Trennung der Zuständigkeiten* kommen im Lemma **nicht** vor → **nicht etabliert**. |
| **Provenance** | **die** Provenance | — | der Provenance | **ENTSCHIEDEN IN #313 — nicht hier. Siehe `canon/de/ai-sdlc.md` §4a; diese Zeile verweist nur und ergänzt Belege.** Kanon: **kept-EN „die Provenance"** + Glosse „(Herkunft und Nachweiskette eines Artefakts)", Kurzlabel **„Herkunft"**; *Herkunftsnachweis*, *Provenienz* bloß und *Datenherkunft* abgelehnt, *Datenprovenienz* OPEN. **Der Termledger-Durchgang kam unabhängig zum selben Ergebnis** und trägt drei Belege nach, die #313 nicht führt — sie stehen in §4a des Ledgers. |
| **Audit** | **das** Audit (*der* Duden-Nebenform) | die Audits | des Audits | **SETTLED — Stufe 1 und Stufe 2. Dies ist eine NEUE Zeile: #313 hat *Prüfpfad* ausdrücklich „nicht berührt", also ist hier nichts überschrieben, sondern erstmals geprüft.** BSI IT-Grundschutz-Baustein **DER.3.1 „Audits und Revisionen"**: „**Audits und Revisionen** sind grundlegend für jedes erfolgreiche Managementsystem für Informationssicherheit (ISMS)"; Flexion direkt aus dem BSI-Fließtext: „Vorbereitung **eines Audits**", „Bei **einem Audit** MUSS das Auditteam prüfen …", „… die **das Audit** oder die Revision leitet." **Zählung im Baustein: Audit 140×, Revision 70×, Prüfung 27× — *Prüfpfad* 0×, *Nachvollziehbarkeit* 0×, *Protokollierung* 0×.** Duden: „das, auch: der Audit; Genitiv: des Audits, Plural: die Audits", Gebrauch *Wirtschaft*, „[unverhofft durchgeführte] Überprüfung, Revision"; DWDS nennt das Neutrum zuerst. **Hausform: das Audit**, korpusweit gehalten. **Kosten, benannt:** das nackte *Audit* bezeichnet die **Prüfung**, nicht den aufbewahrten **Pfad** — dieselbe Unschärfe trägt aber auch das englische Label. |
| **SBOM** | **die** SBOM | die SBOMs | **der** SBOM | **SETTLED — Stufe 1, und die Zählung ist eindeutig.** BSI **TR-03183-2** (deutsche Fassung): „**Eine SBOM** ist ein maschinenverarbeitbares Dokument und entspricht einer elektronischen Stück-/Teileliste"; „… eines Abgleichs **der SBOM** des Produktes mit Schwachstelleninformationen" <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR03183/BSI-TR-03183-2.pdf>. **Volltextzählung der TR: 35 feminine Marker, 0 maskuline oder neutrale.** Femininum vermutlich nach *die Liste / die Stückliste*. |
| **Audit Trail** | kept-EN, artikelfrei — deutsch: **die Protokollierung** | — | — | **SETTLED für die deutsche Form, OPEN für ein Genus des Lehnworts — und ⚠ WÖRTLICHE FALLE AUF STUFE 1, die gefährlichste dieses Durchgangs.** *Prüfpfad* ist **kein** IT-Begriff, sondern ein **umsatzsteuerrechtlicher Terminus**: § 14 Abs. 1 UStG: „… innerbetriebliche Kontrollverfahren …, die einen **verlässlichen Prüfpfad zwischen Rechnung und Leistung** schaffen können" <https://www.gesetze-im-internet.de/ustg_1980/__14.html>. Er bezeichnet die belegbare Verbindung zwischen **Rechnung und erbrachter Leistung**, nicht ein manipulationssicheres Ereignisprotokoll. **Revisionssicherheit** benennt eine **Eigenschaft** der Archivierung nach GoBD, nicht das Artefakt. **Ein Kanon, der *audit trail* als *Prüfpfad* wiedergibt, importiert Steuerrecht in ein Observability-Kapitel.** Korpusform: **die Protokollierung / das Protokoll**, oder *Audit Trail* als Loan stehen lassen. *(Alle Quellen, die „Audit Trail = Prüfpfad" gleichsetzen, waren DMS-Herstellerglossare unterhalb Stufe 5.)* |
| **Attestation** | **OPEN** | — | — | **OPEN — und *Attest* ist eine totale Falle.** DWDS *Attest*: „das Attest", **einzige Bedeutung „ärztliche Bescheinigung"** <https://www.dwds.de/wb/Attest>. DWDS *Attestierung* existiert als Stichwort, aber **ohne Definition**, und im Kontext von Rechten/Anerkennung, nicht von signierten Metadaten. Für den in-toto-/Sigstore-Sinn: **zero German attestation at any tier**. **Kept-EN *Attestation*, niemals *Attest*.** *Was es entscheiden würde:* ein dpunkt-/Rheinwerk-Titel zu Supply-Chain-Security oder ein c't-/iX-Beitrag mit *Attestierung* oder *Bescheinigung* auf einem signierten Metadatenobjekt. |
| Mutationstest | **der** Mutationstest | die Mutationstests | des Mutationstests (*regelhaft*) | **WEAK — und die belegte Schreibung ist die unschönere.** Es gibt **kein** eigenes de.wikipedia-Lemma; die attestierte Form steht in *Dynamisches Software-Testverfahren*: „Der **Mutationen-Test** ist keine Testtechnik im engeren Sinne, sondern ein Test der Leistungsfähigkeit anderer Testmethoden …" <https://de.wikipedia.org/wiki/Dynamisches_Software-Testverfahren>. **Hausform: *Mutationstest*** (glattes Kompositum) — regelhaft, aber **nicht belegt**; das steht hier ausdrücklich. |
| technische Schulden | **die** technischen Schulden (Plural) | — | technischer Schulden | **SETTLED — German-led, Plural zuerst.** de.wikipedia-Lemma: „**Technische Schulden** oder Technische Schuld (englisch *technical debt*) ist eine in der Informatik gebräuchliche Metapher …" <https://de.wikipedia.org/wiki/Technische_Schulden>. Genitiv Plural nativ belegt (heise-Titel „Qualitätsinvestitionen statt **technischer Schulden**"). Beide Numeri sind lizenziert; **der Korpus nimmt den Plural.** |
| **Runbook** → **das Betriebshandbuch** | **das** Betriebshandbuch | die Betriebshandbücher | des Betriebshandbuchs | **SETTLED — German-led, Stufe 1, mit eigener amtlicher Abkürzung.** BSI OPS.1.1.1 *Allgemeiner IT-Betrieb* (2023): „Ein **Betriebshandbuch (BHB)** beschreibt je IT-Komponente alle relevanten Maßnahmen und Daten, die für den Betrieb … notwendig sind"; „… als Teil **des Betriebshandbuchs** definiert werden" <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/04_OPS_Betrieb/OPS_1_1_1_Allgemeiner_IT_Betrieb_Edition_2023.pdf>. **Volltextzählung des Bausteins: *Betriebshandbuch* 4×, *Runbook* 0×.** |
| **Postmortem** | **OPEN (Artikel)**; Hausform *das Post-Mortem* | die Post-Mortems | — | **OPEN.** heise verwendet es durchgängig **artikellos** und in Komposita (*Post-Mortem-Kultur*, *Blameless-Post-Mortem-Protokoll*, iX-Titel „Post mortem"); **kein geprüfter Text hängt einen Artikel daran**. *Nachbetrachtung* / *Post-Mortem-Analyse*: keine Attestierung. Hausform **das Post-Mortem** ist **Analogie** (*das Protokoll*, *das Review* — der Neutrum-Default für nominalisierte englische Ereignisnomina), **kein Beleg**; das steht hier ausdrücklich. |
| Sandboxing | **kein Substantiv — verbal umschreiben** | — | — | **OPEN als Substantiv.** *die Sandbox* ist DWDS-settled (§1.1.a) — **„Sandboxing" kommt im de.wikipedia-Sandbox-Artikel gar nicht vor.** Deutsche Prosa verwendet **Verben**: *isolieren*, *abschirmen*, „vom Rest des Systems **abgeschirmt**". **Korpusform: „in einer Sandbox ausführen" / „abschotten"**, nicht „das Sandboxing". |

### §1.1.g **Wo die deutsche Form gewinnt — der Abschnitt, den ein flüssiges Modell zuverlässig falsch macht**

**Das ist die wertvollste Tabelle dieses Kanons.** §1.0 sagt richtig, dass ein Anglizismus im Deutschen kein
Defekt ist. Ein schreibendes Modell macht daraus die Regel „also nimm das englische Wort" — und liegt dann
bei **vierzehn** Termini falsch, jedes Mal in eine Richtung, die sich flüssig und selbstsicher anfühlt. Die
folgenden Zeilen sind **belegt**, nicht gewählt; jede steht mit ihrem Beleg oben in §1.1.a–f.

> **Nachprüfung der drei folgenreichsten Zeilen (2026-07-28).** Weil diese Tabelle Bootstrap-Entscheidungen
> umdreht, wurden die drei teuersten Belege **nicht** aus dem Rechercheprotokoll übernommen, sondern
> einzeln nachgeholt: Duden `Retrieval` („Substantiv, Neutrum · Gebrauch: **EDV** · das Retrieval; Genitiv:
> des Retrievals"), Duden `Log_EDV` (ein **eigenes Lemma** mit Querverweis „Wort mit gleicher Schreibung"
> auf das seemännische `Log_Seewesen`) und das BSI-Zero-Trust-Papier („welches im Kern auf dem **Prinzip
> der minimalen Rechte** (engl. „Least Privileges") … basiert" — und, im selben Dokument,
> „nach dem **Prinzip der geringsten Rechte**", was die DISPUTED-Markierung der Formwahl trägt).
> **Alle drei halten wörtlich.**
> **Methodischer Nebenbefund, der es wert ist, weitergegeben zu werden:** der Abruf des BSI-PDFs meldete
> „Phrasen nicht gefunden", während `pdftotext` dieselbe Datei in einer Sekunde sauber las. **Ein
> Werkzeugfehler beim Abruf sieht genauso aus wie ein Nullbefund** — bei PDFs also extrahieren und greppen,
> nicht abrufen und fragen.

| ✗ Der Reflex nimmt | ✓ Der Beleg sagt | Kürzeste Begründung |
|---|---|---|
| der Endpoint | **der Endpunkt** | heise schreibt in **jedem** Register *Endpunkt*, auch beim ML-Serving. „der Endpoint" ist im Deutschen fast nur der **Endgeräte**-Sinn der IT-Sicherheit |
| Inference | **die Inferenz** | Duden-Lemma; heise durchgängig „**Inferenz**-Engine", „LLM-**Inferenz**" |
| Throughput | **der Durchsatz** | Duden mit ausdrücklichem **EDV**-Sinn; „der Throughput" in deutscher ML-Prosa **nicht gefunden** |
| Quantization | **die Quantisierung** | Duden, richtiger Sinn; heise-Titel „Wie **Quantisierung** große Sprachmodelle verkleinert". ⚠ **nicht** *Quantifizierung* |
| Instrumentation | **die Instrumentierung** | vier unabhängige Belege; *Instrumentation* lebt im Deutschen nur noch in API-Eigennamen |
| Error Budget | **das Fehlerbudget** | zwei unabhängige Fachhäuser (Computerwoche, iX) schreiben ausschließlich deutsch |
| Vector Database | **die Vektordatenbank** | de.wikipedia-Lemma + heise bis in die Schlagzeile; **„Vector Database" nie schreiben** |
| Context Window | **das Kontextfenster** | heise definiert und verwendet es; der Loan erscheint nur in Herstellerdoku |
| Knowledge Base | **die Wissensbasis / Wissensdatenbank** | deutscher Terminus wissensbasierter Systeme; der Loan verliert deutlich |
| hallucination | **die Halluzination** | Duden führt eine **eigene KI-Bedeutung**; „die Hallucination" hat null Attestierung |
| Least Privilege · Separation of Duties · Secret · Runbook | **Prinzip der geringsten Berechtigungen / minimalen Rechte** · **die Funktionstrennung** · **das Geheimnis** · **das Betriebshandbuch** | **allesamt Stufe 1 (BSI)** — im Sicherheits- und Governance-Vokabular hat das Deutsche eigene, normativ gesetzte Wörter, und die BSI stellt das Englische konsequent in die Klammer |

> **Und die Gegenrichtung, damit daraus keine Anglizismus-Jagd wird (§1.0 verbietet die):** die deutschen
> Konkurrenten, die **verloren** haben und deshalb **nicht** verwendet werden — *Nachsortierung* (Reranking),
> *Rückbindung* (Grounding), *Feature-Schalter* (Feature Flag), *Kanarienvogel-Release*, *Arbeitsprozess*
> (Worker), *Qualitätstor* (Quality Gate), *Aufgabentrennung*, *Prüfpfad* (Audit Trail — sogar
> **sinnfalsch**, s. o.), *Zusammenführung* (Merge), *Quelltextprüfung* (Code-Review). Für jedes dieser
> Wörter wurde aktiv gesucht; **keines** ist in seinem Sinn attestiert. Ein Lektor, der sie einsetzt,
> „verbessert" belegte Fachsprache in unbelegte Neuprägung.

**Nachtrag-Regel.** Jeder neue englische Terminus, der im Korpus zum zweiten Mal vorkommt, bekommt **vor**
seinem zweiten Vorkommen eine Zeile in dieser Tabelle. Wer keinen Beleg findet, trägt **OPEN** ein und
umgeht das Wort, statt einen Artikel zu erfinden — ein erfundener Artikel wird im nächsten Absatz von einem
anderen erfundenen Artikel abgelöst, und genau das ist der Defekt, den diese Tabelle verhindert.

**Ergänzung 2026-07-28 (DE-Pilot), ein Schritt VOR dem OPEN-Eintrag:** Wer kein flexionstragendes Beispiel
findet, prüft **zuerst die Kompositumsverwendung** — ein Lehnwort kann als Kompositumsbildner völlig
brauchbar und als freies Substantiv unbelegt sein (`das Retry-Budget` ✅ / `ein Retry` ⛔). Siehe den Kasten
„Ein Lehnwort kann als KOMPOSITUMSBILDNER überleben" am Anfang von §1.1. Erst wenn auch das Kompositum
unbelegt ist, steht die Zeile auf **OPEN**.

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
| überwachen | to monitor | „monitoren" ✗ als Terminus; das **Substantiv** *das Monitoring* bleibt kept-EN (§1.1.e) |
| **der Endpunkt** | endpoint | **kein „der Endpoint"** — §1.1.g. Der Loan ist im Deutschen fast nur der Endgeräte-Sinn der IT-Sicherheit |
| **die Inferenz** | inference | Duden-Lemma; im ML-Sinn durchgängig in deutscher Fachprosa |
| **die Quantisierung**; quantisieren | quantization | ⚠ **nicht** *Quantifizierung* — anderer Begriff |
| **die Instrumentierung** | instrumentation | der Loan lebt im Deutschen nur in API-Eigennamen weiter |
| **das Fehlerbudget** | error budget | zwei deutsche Fachhäuser schreiben ausschließlich deutsch |
| **die Vektordatenbank** | vector database | „Vector Database" in deutscher Prosa **nie** schreiben |
| **das Kontextfenster** | context window | — |
| **die Wissensbasis / die Wissensdatenbank** | knowledge base | Wissensbasis = das abstrakte Wissen, Wissensdatenbank = der gespeicherte Bestand (Hausaufteilung) |
| **die Halluzination**; halluzinieren | hallucination | Duden führt eine eigene KI-Bedeutung |
| **die Nutzlast / die Nutzdaten** | payload | das Lehnwort hat **kein** Wörterbuchlemma und kein stabiles Genus (§1.1.a) |
| **das Geheimnis** | secret (Zugangsdatum) | **BSI-Form**; kept-EN nur im festen Terminus *Secrets Management* |
| **die Funktionstrennung** | separation of duties | BSI + Wirtschaftsprüfung; *Aufgabentrennung* ist nicht etabliert |
| **das Prinzip der geringsten Berechtigungen** / **der minimalen Rechte** | least privilege | BSI führt den Begriff immer deutsch ein; **welche** Form, ist DISPUTED (§1.1.f) |
| **das Betriebshandbuch (BHB)** | runbook | BSI-Terminus mit eigener amtlicher Abkürzung |
| ⚠ **NICHT deutsch geführt: *provenance* ist kept-EN — „die Provenance"** | provenance | **Diese Zeile stand kurzzeitig als „der Herkunftsnachweis" und ist FALSCH gewesen.** #313 hat den Terminus entschieden: kept-EN **die Provenance**, Kurzlabel **„Herkunft"**; *Herkunftsnachweis* ist **abgelehnt**. Vollständig in `canon/de/ai-sdlc.md` §4a |
| **das Audit** | audit | ⚠ **nicht *Prüfpfad*** (§ 14 UStG-Terminus, §1.1.f) |
| **die statische Code-Analyse**; linten | static analysis; to lint | das **Verb** *linten* ist de.wikipedia-belegt; das Substantiv *Linter* ist OPEN |
| **die Testabdeckung** | test/code coverage | *die Code Coverage* im laufenden Fachtext zulässig |
| **die Protokollierung / das Protokoll** | audit trail | ⚠ **nie** *Prüfpfad* — das ist ein umsatzsteuerrechtlicher Terminus (§1.1.f) |
| **technische Schulden** | technical debt | Plural ist die Korpusform |
| **die Bereitstellung / der Betrieb** | serving | „das Serving" mit deutschem Artikel ist unbelegt |
| **der Bewerter / das Bewertungsmodell** | grader | der Loan hat null deutsche Attestierung |

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

> **Amendment 2026-07-28 (DE-Pilot „Tool-Einsatz") — die Regel steht, die BEGRÜNDUNG war falsch.**
>
> **Die alte Begründung, absichtlich lesbar gelassen:** „des Agents" galt hier als **Flexionsfehler** — als
> eine Form, die es im Deutschen **nicht gibt**. Das ist widerlegbar, und eine Regel, die auf einer
> widerlegbaren Begründung ruht, fällt mit ihr: genau der **SK-Fáza-26-Fehlermodus**, weshalb die alte
> Fassung hier stehen bleibt statt ersetzt zu werden.
>
> **Die Form gibt es — sie gehört nur zu einer ANDEREN Lesart.** DWDS führt ein zweites, informatisches
> Homograph **²Agent** und druckt **zwei Paradigmen nebeneinander**: `des Agent(s)` / `die Agents`
> [ˈɛɪ̯ʤɛnt] **und** `des Agenten` / `die Agenten` [aˈgɛnt]. Die eigenen Belege spalten sich sauber nach
> Untersinn: die `Agents`-Formen stehen bei **installierter Client-/Daemon-Software** („Die Installation
> **des Agents** ist für alle Versionen gleich"), der autonome, schlussfolgernde Agent nimmt die
> n-Deklination.
> In de.wikipedias *Software-Agent* steht `Agenten` **26-mal** gegen `Agents` **7-mal**, und alle sieben
> `Agents` stehen in **englischen Literaturtiteln**, keiner im deutschen Fließtext.
>
> ⇒ **Korpusregel unverändert: `des Agenten`, `die Agenten`.** Neue Begründung: *„des Agents" ist die Form
> der **anderen** Lesart (installierter Software-Agent), nicht ein Flexionsfehler* — nicht mehr „die Form
> gibt es nicht". Praktischer Gewinn: Wer die Form in einer Quelle findet, weiß jetzt, **warum** sie dort
> richtig und hier falsch ist, statt die Regel für widerlegt zu halten.

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
| debuggen | **debuggt** (kein `ge-`) | SETTLED — Duden <https://www.duden.de/rechtschreibung/debuggen>; DWDS setzt dieselbe Form („debuggt, debuggte, hat debuggt") und markiert **„gedebuggt" ausdrücklich als „ungewöhnl."** — die Betonungsregel (§1.3.2 Regel 2) greift hier, *de-BUGG-en* ist nicht erstbetont | zulässig |
| streamen | **gestreamt** | SETTLED — Duden <https://www.duden.de/rechtschreibung/streamen> | zulässig |
| forken | **geforkt** | SETTLED — DWDS <https://www.dwds.de/wb/forken> | zulässig |
| pushen | **gepusht** | SETTLED (Form) / **WEAK (Git-Sinn) — Falscher-Sinn-Falle bestätigt**: Duden markiert alle Bedeutungen als *salopp* („ein neues Album pushen") bzw. *Jargon* („mit harten Drogen handeln") und kennt **keinen** Git-Sinn <https://www.duden.de/rechtschreibung/pushen> | zulässig im Git-Kontext, sonst meiden; neutral: **„hochladen / an das entfernte Repository übertragen"** |
| indexieren | **indexiert** (kein `ge-`) | SETTLED — Duden <https://www.duden.de/rechtschreibung/indexieren> | bereits deutsch |
| skalieren | **skaliert** (kein `ge-`) | SETTLED — Duden <https://www.duden.de/rechtschreibung/skalieren> | bereits deutsch |
| **releasen** | **releast** / released (stummes -e → § 21 E2); **kein `ge-`** (re-LEA-sen) | SETTLED — Duden führt das volle Lemma: „releast, releaste, hat releast/released", Glosse **„veröffentlichen; ein Release vornehmen"** <https://www.duden.de/rechtschreibung/releasen>; DWDS-Lemma ebenfalls vorhanden | **im Korpus: „veröffentlicht"** (Dudens eigene Glosse); *releast* zulässig |
| **patchen** | **gepatcht** — „gepatched" ✗ (kein stummes -e) | SETTLED — Duden, ausdrücklich **EDV**: „die in einem Programm enthaltenen Fehler beheben" <https://www.duden.de/rechtschreibung/patchen>; DWDS mit c't-Beleg | etabliert, zulässig |
| **taggen** | **getaggt** — „getagged" ✗ | SETTLED — Duden, ausdrücklich **EDV**: „(einen Text) mithilfe von Tags strukturieren" <https://www.duden.de/rechtschreibung/taggen>; DWDS mit Zeit-Beleg | etabliert, zulässig |
| **quantisieren** | **quantisiert** (kein `ge-`) | SETTLED — DWDS: „quantisiert, quantisierte, hat quantisiert", Marker *Physik, Nachrichtentechnik* <https://www.dwds.de/wb/quantisieren>; ML-Sinn bei heise belegt („auf lediglich vier Bit **quantisiert**") | **die Korpusform**. **„quantifizieren" ✗** — anderer Begriff, klassischer falscher Freund |
| **instrumentieren** | **instrumentiert** (kein `ge-`) | SETTLED (Form) / **WEAK (Observability-Sinn) — Falscher-Sinn-Falle**: das DWDS-Lemma ist **musikalisch** („einen Kompositionsentwurf für die Orchesterinstrumente ausarbeiten") <https://www.dwds.de/wb/instrumentieren>. Der IT-Sinn ist nur bei heise belegt („Spring Sleuth instrumentiert viele Standardbibliotheken") | zulässig; Substantiv **die Instrumentierung** ist bei heise gut belegt |
| **mocken** | (gemockt) | **WEAK — und der Wörterbuchbefund taugt nicht als Beleg.** DWDS kennt **kein** gegenwartssprachliches Verb *mocken* (nur *der Mocken* = „süddeutsch, mundartlich Brocken"; ein Verb *mocken* „schleichen, lauern" steht nur bei Grimm). Der IT-Sinn erscheint bei heise **in Anführungszeichen** („externe Abhängigkeiten … »gemockt« werden sollten") — das ist Distanzierung, kein etablierter Usus | **im Korpus: „nachgebildet / simuliert"** bzw. „einen Mock bereitstellen"; de.wikipedia meidet das Verb ebenfalls („Mock-Objekt, auch **Attrappe**") |
| **linten** | (gelintet) | **WEAK (Infinitiv) — de.wikipedia sagt es ausdrücklich**: „Davon abgeleitet hat sich das Verb **linten** (englisch *to lint*) für das Durchführen der statischen Code-Analyse etabliert" <https://de.wikipedia.org/wiki/Lint_(Programmierwerkzeug)>. **Nur der Infinitiv ist belegt**; *gelintet* ist regelhaft abgeleitet, nicht belegt | Infinitiv zulässig; für das Partizip **„statisch geprüft" / „einer statischen Codeanalyse unterzogen"** |
| **tracen** | — | **OPEN — kein Wörterbucheintrag** (DWDS 404, kein Duden-Lemma). Die deutsche Fachpresse **meidet das Verb** und schreibt deutsch: „Aufrufe … **nachverfolgen**", „alle Abschnitte des Aufrufbaums **protokolliert**" (heise). de.wikipedia-Lemma: **Ablaufverfolgung** | **im Korpus: „nachverfolgt / protokolliert"**; die Substantive *der Trace*, *das Tracing* bleiben kept-EN |
| **scoren** | (gescort / gescored) | **SETTLED für die Form, FALSCHER SINN für unsere Verwendung.** Duden **und** DWDS führen **ausschließlich den Sportsinn**: „einen Punkt, ein Tor o. Ä. erzielen", Beleg „für die Bayern scorte der eingewechselte Spieler" <https://www.duden.de/rechtschreibung/scoren>. **Kein Evaluationssinn in Tier 1–2.** Der einzige Treffer im ML-Sinn stammt von Microsoft Learn de-de → **disqualifiziert** | **im Korpus: „bewertet"** bzw. „einen Score berechnen". Das Substantiv *der Score* bleibt kept-EN |
| **reviewen** | (reviewt) | **OPEN — kein Wörterbucheintrag** (Duden 404; DWDS leitet auf *revieren* um). Der heise-Fachartikel über Pull-Request-Workflows benutzt das Verb nirgends, sondern „**prüft**" / „**überprüft**". **Merke:** *review* endet **nicht** auf stummes -e → „reviewed" wäre selbst als Hausform unzulässig (§ 21 E2) | **im Korpus: „geprüft / begutachtet"** bzw. „ein Code-Review durchführen" |
| **batchen** | — | **OPEN — zero German attestation at any tier** (DWDS 404; de.wikipedia-Lemma ist **Stapelverarbeitung** und enthält das Verb nicht). Die einzigen Treffer für *gebatcht* stammen aus herstellerlokalisierter Doku → **disqualifiziert** | **im Korpus: „gebündelt / stapelweise verarbeitet"** |
| **refaktorisieren** | **refaktorisiert** (kein `ge-`) | SETTLED — die deutsche Form lautet **refaktorisieren**, nicht „refaktorieren" und nicht „refactoren"; heise verwendet sie („statt wild drauf los zu refaktorisieren") | **die Korpusform** |
| **embedden** | — | **OPEN** — kein Duden-, DWDS- oder Wiktionary-Eintrag | **im Korpus: „eingebettet"**; das Substantiv bleibt *das Embedding*. „geembeddet" **nicht** schreiben |
| **chunken** | — | **OPEN** — kein Wörterbucheintrag | **im Korpus: „aufgeteilt / zerlegt / unterteilt"**; das Substantiv bleibt *das Chunking*. „gechunkt" **nicht** schreiben |
| **refactoren** | — | **OPEN** — kein Wörterbucheintrag | ersetzt durch **refaktorisieren** |
| **stubben** | — | **OPEN** — kein Wörterbucheintrag | „einen Stub bereitstellen" |
| **pullen** | (gepullt) | **OPEN für den Git-Sinn — und mit Warnung** | ⚠ **meiden**: die Wörterbuchbedeutungen sind nautisch, reiterlich, Golf — und „salopp, derb Wasser lassen" (DWDS). Im Korpus: **„abrufen / holen"** |

> **Belastbarkeit, ehrlich.** Anders als beim Genus ist diese Achse überwiegend **kodifiziert** — die meisten
> Zeilen stehen so im Duden, im DWDS oder im amtlichen Wörterverzeichnis. Die OPEN-Zeilen (*embedden,
> chunken, refactoren, stubben, tracen, reviewen, batchen*) haben **gar keine** lexikografische Deckung;
> deshalb weicht der Korpus dort auf das deutsche Verb aus. Das ist **keine Anglizismus-Jagd**
> (§1.0 verbietet die), sondern die Vermeidung einer Form, für die es keine Norm gibt und über die deshalb
> jede Seite anders entscheiden würde.
>
> **Das Muster, das dieser Durchgang sichtbar gemacht hat, und es ist das wichtigste Ergebnis der ganzen
> Tabelle: Das Deutsche behält das SUBSTANTIV und verdeutscht das VERB.** *Chunking* bleibt, aber man
> **unterteilt**. *Embedding* bleibt, aber man **vektorisiert**. *Code-Review* bleibt, aber man **prüft**.
> *Trace* bleibt, aber man **verfolgt nach**. *Score* bleibt, aber man **bewertet**. Das betrifft **acht**
> der geprüften Verben und ist keine Stilpräferenz, sondern der belegte Usus der Fachpresse: wer das Verb
> mitentlehnt, schreibt übersetztes Englisch, wo Fachprosa steht. **§1.2 hält die Gegenstücke** —
> die Tabelle dort ist nicht die Ausnahme zu dieser hier, sondern ihre andere Hälfte.
>
> **Und die Falscher-Sinn-Falle sitzt bei den Verben genauso wie bei den Substantiven:** *scoren* (Sport),
> *pushen* (salopp + Drogenjargon), *pullen* (Rudern, Reiten, Golf, derb), *instrumentieren* (Orchester),
> *mocken* (bei Grimm „schleichen, lauern"; im Gegenwartsdeutsch gar nicht mehr lemmatisiert),
> *stubben* (Forst: der Baumstumpf). **Ein Duden-Treffer auf den Infinitiv ist kein Beleg für unsere
> Bedeutung.**

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
| `What is important to understand is that …` | „Was wichtig zu verstehen ist, ist, dass …" | „**Entscheidend ist, dass …**" / „Dabei ist Folgendes wichtig: …" / „Sie müssen zwei Fälle unterscheiden: …" |
| `Once the agent receives the data, …` | „Einmal der Agent die Daten erhält, …" | „**Sobald** der Agent die Daten erhält, …" / „Nachdem der Agent die Daten erhalten hat, …" (*einmal* leitet keinen finiten Nebensatz ein) |
| `This allows the model to call the tool` | „Das erlaubt dem Modell, **um** das Tool aufzurufen" | „**Dadurch kann** das Modell das Tool aufrufen." / „Das ermöglicht es dem Modell, das Tool aufzurufen." (*erlauben/ermöglichen* regieren den reinen *zu*-Infinitiv; *um zu* ist final) |
| `By using a re-ranker, …` | „Durch Verwenden eines Re-Rankers …" | „Durch **den Einsatz** eines Re-Rankers …" / „Wenn Sie einen Re-Ranker einsetzen, …" |
| `different than expected` | „unterschiedlich als erwartet" | „Das Ergebnis **weicht von** der Erwartung **ab**." / „… fällt **anders aus als** erwartet." |
| `ends up calling the tool twice` | „Der Agent endet damit, das Tool zweimal aufzurufen" | „**Schließlich** ruft der Agent das Tool zweimal auf." / „Infolgedessen …" |
| `You want to validate the answer` | „Sie wollen die Antwort validieren" | „Sie **sollten** die Antwort prüfen." / „Prüfen Sie die Antwort, bevor Sie sie weiterverarbeiten." (*you want to* ist Empfehlung, nicht Wille) |
| `supports calling external tools` | „unterstützt das Aufrufen externer Tools" | „**kann** externe Tools aufrufen" / „unterstützt Aufrufe externer Tools" |
| `The request comes with three parameters` | „Die Anfrage kommt mit drei Parametern" | „Die Anfrage **enthält** drei Parameter." |
| `is responsible for generating the answer` | „ist verantwortlich für das Erzeugen der Antwort" | „Das Modell **erzeugt** die Antwort." / „Für die Antwortgenerierung ist das Modell **zuständig**." (*verantwortlich* aktiviert Haftung) |
| `This results in a wrong answer` | „Dies resultiert **in** einer falschen Antwort" | „**Dadurch entsteht** eine falsche Antwort." / „Das **führt zu** …" (*resultieren* regiert *aus*, nicht *in*) |
| `Receiving the request, the agent checks the cache` | „Die Anfrage empfangend, prüft der Agent den Cache" | „**Nachdem** der Agent die Anfrage empfangen hat, prüft er den Cache." (englische `-ing`-Nebensätze werden im Deutschen zu Temporal-, Kausal- oder Modalsätzen) |
| `The prompt is generated by the agent` | „Der Prompt wird durch den Agenten erzeugt" | „**Der Agent erzeugt den Prompt.**" — Passiv nur zur Agensausblendung oder für eine andere Thema-Rhema-Gliederung, nicht als Standardform |
| lange Linksattribute | „die durch das Modell nach dem Abruf aus der Datenbank erzeugte Antwort" | „die Antwort, **die** das Modell nach dem Datenbankabruf erzeugt" — Relativsatz statt überladenes Vorfeld |

**Unterklammerte Hauptsatzketten — flaggen, aber mit Bedacht.** Eine Folge kurzer, je für sich korrekter
Hauptsätze ist **kein sicheres** Übersetzungsindiz: in Anleitungen und Warnungen ist sie idiomatisch
(„Starten Sie den Dienst. Prüfen Sie das Protokoll."). **Verdächtig wird sie, wenn logisch abhängige Aussagen nur
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
- `Sie wollen` (als Empfehlung — die Anrede ist richtig, das Verb ist der Kalk: gemeint ist *sollten*)
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
  Wiederholungen bereits eingeführter Termini — auch nicht im Abschnitt „Was Sie mitnehmen" (die
  Zusammenfassung zeichnet nicht erneut aus, was im Text schon ausgezeichnet ist). Ein klauselanger Merksatz
  kommt in Anführungszeichen oder Kursive, nicht in Fettdruck.

---

## §9 Konstruktionen (Angebot an den Schreibenden, keine Regel)

Das Register in §1.0–§1.2 hält **Termini**. Dieser Abschnitt hält **Konstruktionen**: wiederkehrende
englische Satzformen, die sonst jedes Mal neu entschieden werden — typisch in der Überschrift, auf die ~1 %
der Tokens und ~1 % der Aufmerksamkeit entfallen.

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
