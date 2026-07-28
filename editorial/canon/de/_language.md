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
   Tool-Result, im Strict Mode, der Idempotency Key*. Deutsche Neuprägungen (*Werkzeugaufruf*, *strikter
   Modus*) sind **nicht** das Ziel (§1.0).
4. **Ein Anglizismus ist hier KEIN Defekt.** Die slowakische Regel „Anglizismus = Fehler" gilt im Deutschen
   ausdrücklich **nicht** (§1.0, Kasten).
5. **Genus, Plural und Genitiv jedes Lehnworts stehen in §1.1.** Innerhalb einer Seite darf kein Wackeln
   auftreten (*der Cache* … *das Cache*) — das ist das lauteste Maschinenübersetzungs-Signal überhaupt.
6. **Durchkopplung:** mehrgliedrige englische Fügungen werden im deutschen Satz durchgekoppelt —
   *Machine-Learning-Modell*, *Prompt-Injection-Angriff*, *Retrieval-Qualität*. „Prompt Injection Angriff" ✗.
7. **Typografie:** „…" primär, ‚…' verschachtelt, **niemals »…«** und niemals «…»; **ß** (bundesdeutsch, kein
   Schweizer ss); Dezimalkomma; **Gedankenstrich `–` (U+2013) MIT Leerzeichen — nie `—` (U+2014)**;
   Bis-Strich kompress; **Prozentzeichen mit schmalem geschützten
   Zwischenraum** und Tausendergliederung ebenso — **10–20 %**, `28,7 %`, `1 000 000` (nicht „20%",
   nicht „1.000.000"). Das weicht bewusst von EN/RU/SK ab (§ Typografie, Vorrangregel).
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
