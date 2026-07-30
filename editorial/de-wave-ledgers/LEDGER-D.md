# LEDGER-D — Gate 6.5, Stufe 1 · Slice D (Geld: cost, price, spend, budget, Hebel)

Reconciliation of `OUT-D-run1.md` + `OUT-D-run2.md` against the **shipped German corpus** (27 pages,
Teile I + II) and the **German canon** (`_language.md` §1.1, `rag.md` §2/§3). Both runs read in full
before a line was written.

---

## 0. The finding that reorders this whole slice — read it before the table

**Both runs declared a canon gap that does not exist.** Run 2 states it explicitly: *„Es gibt für diese
Slice nichts wiederzuverwenden — kein einziger Terminus dieser Slice hat irgendwo im Kanon eine Zeile,
außer `Fehlerbudget` und `Provisioned Throughput`."* Run 1 built a 21-row „Kanon-Lückenliste" on the
same premise.

`_language.md` §1.1 in fact carries **four SETTLED rows squarely inside slice D**, plus three more that
bind it:

| Canon row | Line | What it already rules |
|---|---|---|
| **Stellschraube** | `_language.md:1084` | SETTLED, DWDS Sinn 2, Verben *drehen/justieren*. **„Das ist die deutsche Wiedergabe für *the knobs that control this*."** ⛔ *die Knöpfe* |
| **Kosten** | `_language.md:1088` | SETTLED, Pluraletantum, Zählersperre; **singularisches *the cost of X* → `der Preis` oder `die Kosten für X`**; *cost driver* → **der Kostentreiber** |
| **Obergrenze / Limit** (cap) | `_language.md:1089` | SETTLED; *to cap* → **begrenzen / eine Obergrenze setzen**; ⛔ **deckeln** (Politikregister), ⛔ *kappen*, ⛔ „das Cap" nackt |
| **Budget** | `_language.md:1090` | SETTLED Paradigma / WEAK freies Substantiv; **„das Kompositum trägt den Sinn"** — *Fehlerbudget*, *Retry-Budget*, **`das Token-Budget`**; ⛔ *budgetiert*; ⛔ *das Latency Budget* |
| Durchsatz · Throughput | `:1051` · `:1382` | **der Durchsatz**, SETTLED, Duden mit EDV-Sinn — the head noun behind #327 |
| das Fehlerbudget | `rag.md:336` | Klasse 3, SETTLED |
| Latency Budget / Latenzbudget | `rag.md:433` | **OPEN**, Welle-1-Umkehrung |

Three consequences, all of which change rulings below:

1. **`Stellschraube` is already spoken for — by `knob`, not by `lever`.** Both runs proposed to widen
   that row to cover `lever` as well, neither knew it was widening an existing row, and both then
   reported the resulting one-word-two-referents squeeze as a *finding* (run 1 §1 `knob`: „⚠ `lever` und
   `knob` landen auf demselben deutschen Wort"). The squeeze was self-inflicted.
2. **Run 2 breaks a SETTLED canon row twice, unflagged**: it lists **„deckeln"** among the idiomatic
   verbs for `Ausgaben` and for `Budget`. `_language.md:1089` ⛔s *deckeln* by name. Run 1 does not use it.
3. **Run 2's house spelling `Tokenbudget` (closed, from heise) is wrong twice over**: the canon writes
   **`das Token-Budget`** and the shipped corpus writes `Token-Budget` **6×** and `Tokenbudget` **0×**.

---

## 1. Binding table

Class: 1 = identifier/untouchable · 2 = kept-EN loan · 3 = German-led (gloss at first mention) · 4 = fully German.
Corpus counts are my own, measured over the 27 shipped German pages, tokenised (not `grep -c`).

| Terminus | German | Kl. | Status | Artikel / Plural / Genitiv | Kollokation | ⛔ rejected | Evidence |
|---|---|---|---|---|---|---|---|
| **lever** | **der Hebel** | 3 | **CORPUS PRECEDENT — reverses both runs** | der Hebel · die Hebel · des Hebels | „zu einem der Hebel **greifen**"; „der **wichtigste/wirksamste/stärkste** Hebel gegen X"; „**Drei Hebel** an Y"; „Sie **haben** Hebel, aber keiner ist ein Schalter" | ⛔ **„alle Hebel in Bewegung setzen"** (= sich anstrengen) · ⛔ **„am längeren Hebel sitzen"** (= im Vorteil sein) · ⛔ „den Hebel ansetzen" *als Wiedergabe des Substantivs* · ⛔ **`der Kostenhebel`** (siehe Karte 1) · ⛔ `die Stellschraube` für diesen Referenten (Kanonzeile ist für `knob` vergeben) | **CORPUS(15)** — `Hebel` 10 + `Hebeln` 1 + `Qualitätshebel` 2 + `Grundhebel` 1 (+ Verb `hebelt` 1), **8 Dateien, 3 H2-Überschriften** |
| **knob** | **die Stellschraube** (herstellerseitige Einstellung) · **der Parameter** + Klasse-1-Bezeichner | 3 / 1 | **BOUND (Kanonzeile, korrekt angewandt)** | die Stellschraube · die Stellschrauben · der Stellschraube | **an einer Stellschraube drehen** (Dat.), justieren; „Die Stellschrauben dafür sitzen **beim Anbieter**" | ⛔ *der Knopf / Drehknopf* (Kanon) · ⛔ `der Hebel` hier | **CORPUS(3) + Kanon `_language.md:1084`** — die Zeile nennt *the knobs that control this* wörtlich |
| **dial** *(6× in Teil III, nicht in D.terms)* | **der Regler** | 3 | **CORPUS PRECEDENT — reverses run 2's ⛔** | der Regler · die Regler · des Reglers | „ein Regler, **an dem Sie drehen**"; „die Länge ist ein Regler, den Sie **einstellen**"; „α ist **der Regler zwischen** X und Y" | ⛔ eine dritte Prägung erfinden; ⛔ `der Schalter` (binär) | **CORPUS(6, 4 Dateien)** — run 2 ⛔'d *der Regler* als „Audio/UI"; der Korpus fährt ihn als den graduellen Steller |
| **cost** | **die Kosten** (Pluraletantum) · Verb **kosten** · Aufwand-Sinn **der Aufwand** · Nachteils-Sinn **auf Kosten + Gen.** | 3 | **BOUND (Kanonzeile `_language.md:1088`)** | die Kosten · nur Plural · der Kosten | entstehen, anfallen, steigen; senken, reduzieren, sparen, verursachen; **„die Kosten zuordnen"** (Korpus) | ⛔ Zahl unmittelbar vor `Kosten` (`rag.md` §6.7 a) · ⛔ *die Unkosten* · ⛔ *attribuieren* → **zuordnen** | **CORPUS(60: `Kosten` 47 + Verb 13, 18 Dateien) + Kanon** |
| **price** | **der Preis** · Kennzahl **der Tokenpreis** | 3 | **CORPUS PRECEDENT** | der Preis · die Preise · des Preises | senken, drücken, anziehen; „**der Preis pro** Anfrage / pro Token"; „zum halben Preis"; „**Spitzenpreise zahlen**" | ⛔ *das Preisschild* als Metapher · ⛔ *bepreisen* **frei** (nur in der belegten Fügung, s. Evidenz) | **CORPUS(38: `Preis` 35, `Tokenpreis` 1, `Spitzenpreise` 1, `bepreist` 1; 15 Dateien)** |
| **pricing** | **kein freies Substantiv** — *pricing model* → **das Preismodell**, *pricing tier* → **die Preisstufe**, *pricing page* → **die Preisseite** | 3 | **AGREED×2, kein Korpusprüfstein** | das Preismodell · die Preismodelle · des Preismodells | „die drei Preismodelle – On-Demand, Provisioned, Batch" | ⛔ **„das Pricing"** (kein Genus, Vertriebsjargon) · ⛔ *die Preisgestaltung* als Laufterm (= Tätigkeit des Anbieters) | **AGREED×2** (beide Läufe, unabhängig, gleiche Analyse); Korpus **0** — kein Präzedenzfall in eine Richtung |
| **bill** | **die Rechnung — nie frei stehend**, immer gebunden: *die Rechnung **für** X*, *die **Monats**rechnung* | 3 | **CORPUS PRECEDENT (bestätigt run 1, korrigiert den Mechanismus)** | die Rechnung · die Rechnungen · der Rechnung | „die Rechnung **für** die Tokens läuft davon"; „**schlägt auf der Rechnung durch**"; „die **Monatsrechnung** beantwortet die Frage, …" | ⛔ **freies „die Rechnung"** im Geldsinn — der Korpus selbst benutzt es 6× im Sinn *Kalkül/Kalkulation* („die Rechnung dahinter sehen", „**die Rechnung geht nur auf, wenn** …") | **CORPUS(11)**: 9 `Rechnung` + `Monatsrechnung` + `Vorberechnung`, 7 Dateien. **3 Geld-, 6 Kalkül-Belege — die Geldbelege sind ALLE gebunden** |
| **billing** | **die Abrechnung** · Verb **abrechnen** | 3 | **AGREED×2, kein Korpusprüfstein** | die Abrechnung · die Abrechnungen · der Abrechnung | „wird **sekundengenau / stundenweise abgerechnet**" | ⛔ *fakturieren* · ⛔ *die Abrechnung* für den **Betrag** | **AGREED×2**; Korpus **0** |
| **spend** (Substantiv) | **die Kosten** (Laufterm) · **die Ausgaben** nur im eindeutig finanziellen Rahmen · Verb **ausgeben für** | 3 | **RECONCILED — beide Läufe umgekehrt; siehe Karte 2** | (wie `Kosten`) | „**die Kosten zuordnen / steuern / begrenzen**"; H2 *Governing the spend* → **„Die Kosten steuern"**; Verb: „**wir haben X ausgegeben**" (Korpus) | ⛔ **`die Token-Ausgaben`** — der Korpus schreibt **`Ausgabe-Token`** für *output tokens*; dieselben zwei Morpheme, umgedreht · ⛔ **`die KI-Ausgaben`** (liest als *KI-Ausgaben = Modellausgaben*; `Modellausgabe` ist Korpusform) · ⛔ *der Spend*, *das Spending* · ⛔ **deckeln** (Kanon `:1089`) | **CORPUS(12)**: **jedes** plurale `Ausgaben` im gelieferten Deutsch ist *output* („geprüfte Ausgaben", „Tool-Ausgaben", „schädliche Ausgaben"), **0 Geldbelege**, 7 Dateien |
| **budget** (Geld/Organisation) | **das Budget**, frei | 3 | **CORPUS PRECEDENT (freier Gebrauch als Anapher)** | das Budget · die Budgets · des Budgets | „**das Budget erschöpfen / ausschöpfen / überschreiten**"; „**Ein Budget ist eine Obergrenze**" (Korpussatz); „**das Budget verbrennen**" (Korpussatz) | ⛔ *budgetiert* / *budgetieren* (Kanon) · ⛔ **deckeln** (Kanon) | **CORPUS(57 freie Token, 13 Dateien) + Kanon `:1090`** |
| **budget** (gezählte Menge) | **das Kompositum**, bei Erstnennung; danach **das Budget** anaphorisch | 3 | **CORPUS PRECEDENT — reverses run 1's ⛔** | das Token-Budget · das Schrittbudget · das Teilbudget · das Retrieval-Budget · das Kostenbudget | „läuft in **das Schrittbudget**"; „trifft zuerst **das Token-Budget** oder **das Kostenbudget**"; „über **den Teilbudgets** steht ein Budget für die ganze Aufgabe" | ⛔ das nackte `Budget` **bei Erstnennung** einer neuen Dimension | **CORPUS**: `Schrittbudget(e)` 7 · `Token-Budget(s)` 6 · `Teilbudget(e)` 7 · `Fehlerbudget(e)` 4 · `Retrieval-Budget` 2 · `Kostenbudget(s)` 2 |
| **budget** — Schreibung | **deutsches Erstglied → geschlossen** (`Schrittbudget`, `Fehlerbudget`, `Kostenbudget`, `Teilbudget`) · **englisches Erstglied → Bindestrich** (`Token-Budget`, `Retrieval-Budget`, `Retry-Budget`) | 3 | **CORPUS PRECEDENT — reverses run 2's Hausform** | — | — | ⛔ **`Tokenbudget`** geschlossen | **CORPUS(6:0)** + Kanon `:1090` schreibt `das Token-Budget` |
| **`Latenzbudget`** | — | — | **OPEN (incumbent held: `die Obergrenze` / „Ziele für p50 und p95"; closes when a T1–T5 German source writes `Latenzbudget` in the SRE sense)** | — | Korpusform: „**Ein Budget ist eine Obergrenze**"; „**Sie setzen Ziele für p50 und p95**" | ⛔ das Latenzbudget · ⛔ *das Latency Budget* mit deutschem Artikel | **CORPUS(0)** — und das ist der Punkt: **das Muster lizenziert die Form, nicht das Wort.** Fünf Kompositumsgeschwister sind geliefert, `Latenz` + `Budget` ist das eine, das der Korpus **nicht** schreibt. Kanon `rag.md:433` bleibt unangetastet |
| **budget** (Verb) | **einplanen · veranschlagen** | 3 | **AGREED×2** | — | „**Planen Sie 2 CPU-Kerne und 4 GB RAM je Container ein.**" | ⛔ *budgetieren* (Kanon) | AGREED×2 + Kanon `:1090` |
| **error budget** | **das Fehlerbudget** | 3 | **BOUND (Kanon), CORPUS-bestätigt** | das Fehlerbudget · die Fehlerbudgets · des Fehlerbudget[e]s | „**Alerts** ergeben sich **aus dem Fehlerbudget**"; „wie schnell Sie es **verbrauchen**"; „ein schnelles **Abbrennen**" | ⛔ *das Error Budget* (Welle 1 gestrichen) | **CORPUS(4) + Kanon ×3.** ⚠ **THIN×2 auf der Attestierungsseite** — beide Läufe stützen die Zeile ausschließlich auf denselben Kanonverweis (Computerwoche + iX); run 1 misst zusätzlich `de.wikipedia insource:"Fehlerbudget"` = 0. Der *Korpus* ist hier die stärkere Evidenz als die Quellenlage |
| **burn rate** | **die Burn Rate** (feminin, mit Artikel) | 2 | **CORPUS PRECEDENT — reverses run 1, promotes run 2's fallback to incumbent** | die Burn Rate · (Plural meiden) · der Burn Rate | „**die Burn Rate des Fehlerbudgets**"; „**Alerts auf die Burn Rate**"; Verbalform „**wie schnell Sie es verbrauchen**"; Substantiv „**ein schnelles Abbrennen**" | ⛔ *die Brennrate* (disqualifizierte Quelle) · ⛔ *die Geldverbrennungsrate* (Liquiditätsreferent) · ⛔ *die Verbrauchsrate*, *die Abbrandrate* | **CORPUS(3, artikeltragend, feminin, am Fehlerbudget)**. ⚠ Die **externe** Attestierungsfrage bleibt offen (`rag.md:436`); die **gelieferte Zeichenkette** ist es nicht. Teil IIIs drei Vorkommen sind Querverweise **auf genau diese Seite** |
| **`burn` (Verb / freies Substantiv)** | **verbrauchen** · **aufzehren** · **das Budget verbrennen** | 3 | **CORPUS PRECEDENT — reverses run 1's ⛔** | — | „welches Feature **das Budget verbrennt**"; „**verbraucht** Tokens"; „der **Tokenverbrauch**" | ⛔ *abbrennen* transitiv | **CORPUS**: „das Budget **verbrennt**" (observability/deep-dive.md:81) — run 1 ⛔'d „das Budget verbrennen" ausdrücklich als „Kalk von *burn*" |
| **cheap / cheaper / cheapest** | **Referentensplit, korpusbelegt:** Preis eines Modells/Tarifs → **günstig(er)** · Verfahren/Aufwand → **billig(er)** · Anspruchsniveau → **einfach** · Aufwandsvergleich → **der geringere Aufwand** | 3 | **CORPUS PRECEDENT — reverses the blanket ⛔ of both runs; keeps their argument exactly where they aimed it** | — | **günstig:** „ein **günstigeres Modell**" (3×, Korpus), „**günstige** Aufrufe", „**günstig** und breit". **billig:** „ist **billig** und schwach", „**billig**, zustandslos", „viel **billiger** und meistens genug", „die **billigste** Strategie", „**billig** zu erkennen" | ⛔ **`günstig` für ein Verfahren** — bricht das gelieferte Antonympaar `billig ↔ teuer` (`teuer/teur-` 17 Token) · ⛔ **`billig` für ein Modell, das der Text als gleichwertig behauptet** — genau der Satz „a cheaper model must beat the price ratio"; der Korpus schreibt dort *günstiger* · ⛔ *preiswert* (Werturteil) · ⛔ *spottbillig* | **CORPUS(35)**: `billig*` **30 in 12 Dateien**, `günstig*` **5 in 3 Dateien** — und der Split ist sauber: **alle 3 Modellpreis-Belege sind `günstiger`** |
| **discount** | **der Rabatt** · Adjektiv **vergünstigt / rabattiert** · *committed-use discount* Klasse 1 + Glosse | 3 / 1 | **AGREED×2, kein Korpusprüfstein** | der Rabatt · die Rabatte · des Rabatt[e]s | „**einen Rabatt gewähren / einräumen**" (Duden) · „den Rabatt **mitnehmen**" | ⛔ *der Discount* (Handelsform) · ⛔ *diskontieren* (Wechsel-/Barwertrechnung) | **AGREED×2** (Duden `Rabatt`, volles Paradigma); Korpus **0** |
| **commitment** | **Dreiteilung:** Abnahmebindung → **die vertragliche Bindung / die Verpflichtung** · Mindestlaufzeit → **ohne Mindestlaufzeit** · Anbieterzusage → **die Zusage / die Zusicherung** | 3 | **RECONCILED (run1 vs run2, I chose run 2's three-way split)** | die Bindung / die Mindestlaufzeit / die Zusage | „Reserved-Laufzeiten: **ohne Mindestlaufzeit**, ein Monat oder sechs"; „**Alle drei geben dieselbe Zusage.**" | ⛔ **das Commitment** (DWDS: HR-Engagement, volles Paradigma **im falschen Referenten** — die `Service`-Gestalt) · ⛔ *das Bekenntnis* · ⛔ *die Verpflichtung* nackt für die Laufzeit | run 1 splits 2-way + Randfall; run 2 splits 3-way and is the only one that sees *no commitment* = **Mindestlaufzeit**, not „ohne Bindung". Korpus **0** |
| **unit economics** | **OPEN (incumbent held: der Umbau „die Stückkosten des Features – die Kosten pro Anfrage, pro aktiven Nutzer, pro ausgeliefertes Feature"; closes when a T1–T5 German source writes an article-bearing *die Unit Economics* or an established German full form)** | 3 | **OPEN — run 2's grade adopted** | die Stückkosten · nur Plural · der Stückkosten | erbt die Zählersperre von `Kosten` | ⛔ **die Unit Economics** mit deutschem Artikel · ⛔ *die Einheitsökonomie / die Einheitswirtschaftlichkeit* | **RECONCILED**: run 1 grades WEAK/SETTLED-ish, run 2 OPEN with the reason that **`Stückkosten` is the neighbour, not the translation** (it is a cost measure; *unit economics* includes the revenue side). Run 2 is right; run 1 also self-reports its only query was a tool artefact |
| **cost per accepted answer** | **die Kosten pro akzeptierte Antwort** (Akkusativ, Hausform) | 3 | **RECONCILED (run1 vs run2, I chose run 2) — run 1's blocker is a 404 artefact** | — | H2: „**Die Einheit sind die Kosten pro akzeptierte Antwort**" · Kartentitel artikellos: „**Kosten pro akzeptierte Antwort**" · Kontrast: „…, **nicht die Kosten pro Token**" · Verb im **Plural** | ⛔ „die Kosten **per** akzeptierter Antwort" · ⛔ Ziffer unmittelbar vor `Kosten` · ⛔ auf *Stückkosten* verkürzen (löscht das tragende Attribut *akzeptiert*) | run 1 builds a Genitiv detour **because `duden.de/rechtschreibung/pro` 404s**; run 2 found the right lemma (`pro_je_zu_jeweils_fuer`) and read it: **„Präposition mit Akkusativ oder Dativ", Beispiel „pro verkauftes oder verkauftem Exemplar"**. Run 1's obstacle does not exist |
| **token diet** | **OPEN (incumbent held: verbal — H3 „Token sparen", Fließtext „Tokens einsparen" / „den Prompt schlank halten"; closes when a T1–T5 source carries an established German noun for the procedure)** | — | **OPEN, AGREED×2 on the ⛔** | — | Mermaid-Knoten „Prompt assembly: token diet" → „**Prompt-Aufbau: Token sparen**" | ⛔ **die Token-Diät** — DWDS `Diät` = Schonkost, **Plural `Diäten` = Abgeordnetenbezüge**, also ein Homograph aus dem **Geld**register in einem Geldkapitel · ⛔ *die Schlankheitskur* | **AGREED×2** and independently reasoned (run 1 via the Homograph, run 2 via both DWDS frames). Both graded their own null finding as non-exhaustive — kept OPEN, not upgraded |
| **provisioned throughput** | (i) Produktname **Provisioned Throughput** artikelfrei · (ii) Appellativ **der … Durchsatz** | 1 / 3 | **RESOLVED — taken as given (#327, `rag.md` §2 struck → Klasse 1)** | (ii) der Durchsatz · die Durchsätze · des Durchsatzes | (i) „Azure verkauft es als **PTU**, Vertex als **Provisioned Throughput**" — nicht flektiert, nicht durchgekoppelt · (ii) „**dedizierter Durchsatz** für gleichmäßige Last" | ⛔ **„der Provisioned Throughput"** mit deutschem Artikel · ⛔ *der provisionierte Durchsatz* | Kanon `_language.md:1051` + `:1382`; **CORPUS(3 `Durchsatz`)**. Das Adjektiv im Appellativ ist **nicht** hier entschieden — siehe §7 |
| **dedicated** | (i) exklusiv reserviert → **dediziert** · (ii) zweckgebaut → **eigens dafür gebaut / spezialisiert** · (iii) separat → **eigen** | 3 | **AGREED×2 on the split; COINED-adjacent on the word** | Adjektiv, regelmäßig | „**dedizierte Kapazität**", „**dedizierter Durchsatz**", „**dedizierte GPU-Knotenpools**" | ⛔ **dezidiert** (DWDS: „entschieden" — **kein IT-Sinn**; grammatisch einwandfrei, semantisch falsch) · ⛔ *dediziert* für (ii)/(iii) · ⛔ **Duden/DWDS als Beleg für `dediziert` zitieren** (Duden 404, DWDS nur das gehobene Verb *dedizieren*) | **AGREED×2** — but the agreement rests on **one** de.wikipedia sentence (`Server`) for both runs, and Korpus = **0**. Labelled **THIN×2**: two reads of one source |
| **charge** (Verb) | **berechnen** · formeller **in Rechnung stellen** | 3 | **AGREED×2** | — | „**Anthropic berechnet das 1,25-Fache**" (Dezimalkomma) | ⛔ *chargen* · ⛔ *aufladen* · ⛔ *verrechnen* | AGREED×2; Korpus 0 |
| **Chargeback / Showback** *(9× in Teil III, kein Konkordanz-Kopfterm)* | **kept-EN als Mustername, Genus OPEN → artikelfrei oder im Kompositum**; der Vorgang deutsch verbalisiert | 2 | **OPEN (incumbent held: artikelfreie Konstruktion; closes when an article-bearing German sentence at T1–T5 is found)** | — · das Chargeback-Verfahren · die Showback-Auswertung | „**Showback** weist jedem Team seinen Verbrauch aus; **Chargeback** belastet die Kosten tatsächlich weiter." Korpusnah: „**die Kosten zuordnen**" | ⛔ „das Showback" mit erfundenem Artikel (die *das Feedback*-Analogie ist kein Beleg) | **AGREED×2 auf dem OPEN**, beide melden es als Konkordanzlücke. Korpus **0**. Run 2 self-grades it „nur gestreift" |
| **per-token** | **pro Token** (unflektiert) · Kennzahl **der Tokenpreis** · *per-token-per-hour* → **je Token und Stunde** | 3 | **AGREED×2, CORPUS-bestätigt** | der Tokenpreis · die Tokenpreise · des Tokenpreises | „**der Preis pro Token / pro Anfrage**"; „On-Demand **rechnet pro Token ab**" | ⛔ *per Token* (dt. *per* = Postversand/Termin) · ⛔ **tokenweise** (= sequenziell, in einem Decode-Kapitel ein Lesefehler) · ⛔ dreigliedrige Durchkopplung | **CORPUS(1: `Tokenpreis`)** + AGREED×2 |
| **economics** | **die Wirtschaftlichkeit**; „the economics come down to …" → verbal **„Wirtschaftlich entscheidet …"** | 3 | **AGREED×2, CORPUS-gestreift** | die Wirtschaftlichkeit · kein Plural · der Wirtschaftlichkeit | „die **Wirtschaftlichkeit** reservierter Kapazität"; „**Wirtschaftlich entscheidet** eine Auslastungsschwelle" | ⛔ *die Ökonomie* (Volkswirtschaft) · ⛔ *die Ökonomik* · ⛔ *die Economics* | **CORPUS(1)** + AGREED×2 |
| **free tier** | **nicht prägen** | — | **verifizierter Nullbefund ×2 — nicht entscheiden** | — | Die tatsächlichen Vorkommen: „a tier that carries no hourly fee" → „**eine Stufe ohne Stundengebühr**"; „the free levers" → „**die Hebel, die nichts kosten**" / Korpuswort **umsonst**: „ein Gateway ist **nicht umsonst**" | ⛔ *die Gratisstufe*, *das Freikontingent* — für einen Begriff geprägt, den der Text nicht enthält | **AGREED×2**, beide Läufe grepten unabhängig `free tier` + `free-tier` = 0 und lasen alle `free`-Treffer von Hand. Korpus: `umsonst` 8, `kostenlos` 3 |
| **capacity reservation** | **nicht prägen** | — | **verifizierter Nullbefund ×2 — nicht entscheiden** | — | Die Nachbarform: „monthly or annual reservations" → „**mit monatlichen oder jährlichen Reservierungen**"; Bedrock-Stufe **Reserved** bleibt Eigenname | — | **AGREED×2**; Präzedenz `denylist/blocklist` |

---

## 2. Sense cards

### Karte 1 — `lever · knob · dial`: **drei englische Wörter, drei deutsche, und der Korpus hat sie schon getrennt**

Beide Läufe haben alle drei auf **eine** Zeichenkette gelegt (`die Stellschraube`) und dann gemeldet, dass
die Zusammenlegung wehtut. Die 27 gelieferten Seiten fahren stattdessen **drei** Wörter, und die Trennachse
ist dieselbe wie im Englischen.

> **Die Frage vor dem Schreiben:**
> **1. Zeige ich auf einen *benannten Mechanismus*, den der Text als Möglichkeit anbietet — Caching, Routing,
> Batch, Quantisierung, Streaming?** → **der Hebel.**
> **2. Zeige ich auf eine *Einstellung beim Anbieter oder im Framework*, die einen Namen und einen Wert hat?**
> → **die Stellschraube** (mit Bezeichner: **der Parameter `…`**).
> **3. Zeige ich auf eine *stufenlose Größe*, die ich auf einen Wert stelle?** → **der Regler.**

- **Hebel** — *„## Cost and latency — the levers"*
  → „**## Kosten und Latenz – die Hebel**"
  *(Korpusparallele, ebenfalls H2: „**## Drei Hebel am Embedding selbst**")*
  *„Quantisation is the last lever."* → „**Die Quantisierung ist der letzte Hebel.**"
  *„Streaming is the single biggest perceived-latency lever you have."*
  → „**Streaming ist der wirksamste Hebel für die gefühlte Latenz, den Sie haben.**"
  *(Korpusparallele: „der **wirksamste Hebel** gegen Abschweifen", „der **wichtigste Hebel** gegen Halluzinationen")*
  *„so the levers actually get pulled"* → „**damit die Hebel tatsächlich benutzt werden**"
  *„the lever that moves the bill most"* → „**der Hebel mit der größten Wirkung auf die Rechnung**"
  *„leaving the free levers, batch and caching, switched off"*
  → „**die beiden Hebel, die nichts kosten – Batch und Caching –, gar nicht erst zu nutzen**"
- **Stellschraube** — *„Three knobs govern that pool."*
  → „**Drei Stellschrauben steuern diesen Pool**: `max_num_seqs` begrenzt …, `max_num_batched_tokens`
  setzt …, `gpu_memory_utilization` legt … fest."
  *„In vLLM it is the `tensor_parallel_size` knob."* → „**In vLLM ist das der Parameter `tensor_parallel_size`.**"
- **Regler** — *„a policy dial, not new code"* → „**ein Regler in der Richtlinie, kein neuer Code**"
  *„the residency-versus-capacity dial"* → „**der Regler zwischen Datenresidenz und Kapazität**"
  *(Korpusparallele: „**α ist der Regler zwischen** Bedeutung und exakter Übereinstimmung")*

**Die Idiomprüfung bleibt auf dem Protokoll, und sie war nicht falsch — sie war am falschen Ort angesetzt.**
Beide Läufe verwerfen `der Hebel` mit vier Gründen. Nach dem Korpus gilt:

| Argument der Läufe | Was davon bleibt |
|---|---|
| **(1)** „alle Hebel in Bewegung setzen" = sich mächtig anstrengen | **Bleibt vollständig — als Kollokationsverbot, nicht als Wortverbot.** Nie „alle Hebel in Bewegung setzen" für *pull all the levers*. Der Korpus schreibt „**zu einem der Hebel greifen**", und das ist genau die Fügung, die das Idiom umgeht |
| **(2)** „am längeren Hebel sitzen" = im Vorteil sein | **Bleibt** — dieselbe Klasse, dasselbe Verbot. Ein Idiom auf einem Wort verbietet die **Fügung**, nicht das Wort; sonst wäre nach derselben Regel `die Rechnung` („die Rechnung geht nicht auf") auch verboten, und die schreibt der Korpus 11× |
| **(3)** „den Hebel ansetzen" benennt *wo*, nicht *welchen Mechanismus* | **Bleibt als ⛔** für die Wiedergabe des Substantivs |
| **(4)** In einem Geldkapitel primt *der Hebel* den **Finanzhebel** (Leverage) | **Überlebt nur in einer Kompositumsform.** ⚠ **Run 1 hat dieses Argument selbst als unbelegt eingestuft** (§6.6: „die DWDS-Zeile belegt den Finanzsinn **nicht**, ich stütze mich dort auf allgemeine Sprachkenntnis"). Das war das einzige Argument mit einem *slice-spezifischen* Biss — und es ist das einzige, das sein eigener Lauf nicht tragen konnte. **Der abgeleitete Rest ist real und wird gehalten: ⛔ `der Kostenhebel`** (unbelegt **und** die eine Form, in der das Finanzbild wirklich zündet). Stattdessen: „**die Hebel an den Kosten**", „**die Hebel, die die Rechnung bewegen**" |

**Und der Preis, wenn man es anders entscheidet:** `lever` steht in **6 der 10** Teil-III-Dateien, in einer
H2. `der Hebel` steht auf **8 der 27** gelieferten Seiten, in **drei** H2-Überschriften, und die
Observability-Vertiefung enthält die Teil-III-Kollokation wörtlich — „**das Signal, zu einem der Hebel aus
Teil 1 zu greifen: ein Cache, ein günstigeres Modell, weniger Chunks im Prompt**". Das ist derselbe
Referent, dieselbe Aufzählung, und Teil III verweist auf diese Seite zurück. Ein `Stellschraube` in Teil III
erzeugt **zwei Namen für einen Referenten quer über die Teilgrenze** — der Fehler, den §1.0 „Richtungswackeln"
nennt — und macht aus einer belegten Kanonzeile (`knob`) eine überdehnte.

### Karte 2 — `spend`: **der Plural ist im Deutschen schon vergeben, und zwar an *output***

Beide Läufe legen `spend` auf **die Ausgaben (Plural)** und sichern das mit der Numerusregel ab: *Singular =
output, Plural = Geld*. Die Regel ist wörterbuchseitig richtig (DWDS: „meist im Plural") **und im gelieferten
Korpus falsch**: dort sind **alle 12** pluralen `Ausgaben` *outputs* — „geprüfte **Ausgaben**", „schädliche
**Ausgaben**", „die **Ausgaben** der Tools", „**Tool-Ausgaben**", „rohe Prompts und **Ausgaben**", in 7
Dateien, eine davon in einer H1. Geldbelege: **null**.

Und die vorgeschlagene Kompositumsform kippt vollends: der Korpus schreibt **`Ausgabe-Token`** für *output
tokens* („Die Rechnung besteht aus Eingabe-Token plus **Ausgabe-Token**"). Beide Läufe schlagen
**`Token-Ausgaben`** für *token spend* vor. Dieselben zwei Morpheme, umgedreht, im selben Kapitel.

> **Die Frage vor dem Schreiben:** *Ist das die Summe, die abfließt — oder ist es das, was ein Modell
> produziert?* Und wenn es die Summe ist: **steht Geld im Satz, oder muss der Leser es erraten?**

| Zweig | Englisch | Deutsch | Durchgearbeiteter Satz |
|---|---|---|---|
| Summe, Laufterm | „LLM spend", „steady spend", „token spend" | **die Kosten** (+ Bindung) | „**Die Kosten für LLMs haben in jeder Cloud dieselben Hebel.**" · „**Die Kosten für Tokens laufen davon, wenn niemand sie zuordnet.**" |
| Steuerung (H2) | „Governing the spend" | **„Die Kosten steuern"** | „**## Die Kosten steuern**" — korpusnah: `Kostenregeln`, `Kostenbudget`, `Kostenstelle` sind alle geliefert |
| Sichtbarkeit | „make spend visible, owned and bounded" | **zuordnen** | „**Die Kosten sichtbar machen, zuordnen und begrenzen**" *(Korpus: „dafür müssen Sie **die Kosten zuordnen**")* |
| Verb | „we spent X", „who spends what" | **ausgeben** | „…statt der nutzlosen Gesamtsumme ‚**wir haben X ausgegeben**'" *(Korpussatz, wörtlich)* |
| Substantiv `Ausgaben` | nur wo Geld im Satz steht | **die Ausgaben** | „**Die Ausgaben für KI stehen erstmals in derselben Größenordnung wie die für Infrastruktur.**" — zulässig, weil *für KI* + *Größenordnung* den Geldrahmen setzen |
| `overspend` (2×, nicht im Kopfterm) | „The overspend, when it comes …" | **der Kostenausschlag** | „**Der Kostenausschlag kommt, wenn er kommt, aus einem von drei Fehlern.**" *(Korpuswort, observability/deep-dive.md)* |

⚠ **Was diese Karte kostet, ehrlich:** Deutsch verschmilzt hier `cost` und `spend` zu einem Nomen. Die
Unterscheidung, die das Englische am Wort trägt, muss die **Kollokation** tragen: *Kosten entstehen /
fallen an* (= cost) gegen *Kosten steuern / zuordnen / begrenzen / deckeln→begrenzen* (= spend). Wer beide
Referenten mit demselben Verb baut, hat die Unterscheidung verloren — nicht am Wort, sondern im Satz.

### Karte 3 — `budget`: **Geld · Menge · Fehler · Verb — und das Kompositum ist eine Erstnennungsregel, kein Dauerzwang**

Der Kanon sagt: „das Kompositum trägt den Sinn, das nackte *Budget* trägt ihn nicht." Der Korpus schreibt
das freie `das Budget` **57×**. Beides stimmt, weil der Korpus eine Regel fährt, die die Kanonzeile nicht
ausspricht: **das Kompositum bei der Erstnennung einer Dimension, danach `das Budget` als Anapher.**

> **Die Frage vor dem Schreiben:** *Habe ich die Dimension auf dieser Seite schon benannt?*
> Nein → **Kompositum.** Ja → **das Budget** genügt.

| Zweig | Test | Deutsch | Durchgearbeiteter Satz |
|---|---|---|---|
| Geld | Lässt sich der Betrag in Euro angeben? | **das Budget**, frei | „**Kein einzelnes Team darf das Budget unbemerkt erschöpfen.**" · „**Die Budgets liegen am Gateway.**" |
| Menge, Erstnennung | Wird etwas Nicht-Geldliches gezählt? | **Kompositum** | „`max_num_batched_tokens` **setzt das Token-Budget je Schritt**." · „Eine billige, aber endlose Schleife läuft in **das Schrittbudget**." *(Korpussatz)* |
| Menge, Anapher | schon benannt? | **das Budget** | „**Ein Budget ist eine Obergrenze**, und eine Überschreitung ist das Signal, zu einem der Hebel zu greifen." *(Korpussatz)* |
| SRE | Abstand zu 100 %? | **das Fehlerbudget** | „**Eine Fehlerbudget-Richtlinie wird vor dem Vorfall unterschrieben, nicht während seiner.**" |
| Verb | steht *to budget*? | **einplanen / veranschlagen** | „**Beide Mengen brauchen Labels – und genau das plant niemand ein.**" |
| ⛔ Latenz | — | **die Obergrenze** | „**Sie setzen Ziele für p50 und p95**" / „**eine Obergrenze für die Latenz**" — **nie** *das Latenzbudget* |

⚠ **Warum `Latenzbudget` offen bleibt und nicht „durch das Muster geschlossen" wird.** Das Muster
`X + Budget` ist im gelieferten Deutsch fünffach belegt — `Schritt-`, `Token-`, `Teil-`, `Retrieval-`,
`Kosten-`. Genau das ist der Grund, aus dem die Zeile **nicht** schließt: **das Muster lizenziert die Form,
nicht das Wort.** Wären die fünf Geschwister ein Freibrief, wäre `Latenzbudget` längst geschrieben; der
Korpus schreibt an dieser Stelle stattdessen **„eine Obergrenze"**, 41 Belege in 11 Dateien. Die Abwesenheit
ist hier eine Entscheidung, keine Lücke. Schließbedingung unverändert (`rag.md` §3).

### Karte 4 — `cheap`: **der Korpus hat den Streit schon geschlichtet, und zwar zu beider Läufe halbem Recht**

Beide Läufe verbieten `billig` rundheraus, mit demselben, guten Argument: der Lehrsatz lautet *cheaper per
token ≠ worse*, und deutsches *billig* trägt „minderwertig" mit. Das gelieferte Deutsch schreibt `billig*`
**30×** in **12** Dateien — und schreibt an genau der Stelle, auf die beide Läufe zielen, **`günstiger`**.

> **Die Frage vor dem Schreiben:** *Steht da ein **Preis**, den ein Anbieter aufruft — oder ein **Verfahren**,
> das wenig Aufwand macht?*

| Zweig | Korpusstelle | Deutsch | Durchgearbeiteter Satz |
|---|---|---|---|
| Modell-/Tarifpreis | „a cheaper model", „the cheapest endpoint" | **günstig(er)** | „**Ein günstigeres Modell gewinnt nur, wenn seine Erfolgsquote den Preisabstand überbietet.**" *(Korpus: „ein Cache, **ein günstigeres Modell**, weniger Chunks im Prompt" — 3×)* |
| Verfahren / Prüfung | „the cheapest check first", „cheapest to fix", „cheap to add" | **billig(er)** | „**Zuerst die billigste Prüfung**" · „**Führen Sie sie in der Reihenfolge ihrer Kosten aus – die billigste zuerst.**" *(Korpus: „Delimiting ist **billig** und schwach"; „Head-based Sampling ist **billig** und zustandslos"; „viel **billiger** und meistens genug")* |
| Anspruchsniveau | „cheap traffic goes to a cheap model" | **einfach** + **günstig** | „**Einfache Anfragen gehen an ein günstiges Modell**, das Spitzenmodell muss begründet angefordert werden." |
| Ressource | „the waiting connection is cheap" | **kostet fast nichts** | „**Die wartende Verbindung kostet fast nichts** – und genau das verleitet dazu, mehr Arbeit anzunehmen, als der Dienst zu Ende bringen kann." |
| Aufwandsvergleich | „Blocking is the cheaper of the two" | **der geringere Aufwand** | „**Blockieren ist von beiden der geringere Aufwand.**" |

⚠ **Das zweite Argument für den Split, das keiner der Läufe hatte: das Antonym.** Der Korpus schreibt
`teuer/teur-` **17×** („**teurem** Reasoning", „die **teuren** Verfahren", „**teuer**, langsam"). Das
gelieferte Paar ist **billig ↔ teuer**. Wer *cheap* durchgehend als `günstig` rendert, während *expensive*
`teuer` bleibt, zerlegt ein Paar, das auf 27 Seiten steht — der Leser bekommt drei Wörter für zwei Pole.

⚠ **Der eine Korpus-Gegenbeleg, offen benannt:** `multi-agent/deep-dive.md` schreibt „ein **billiges** Modell
in die Worker und ein **starkes** an den Orchestrator". Dort *ist* das schwächere Modell gemeint, das
Wertungsmoment ist beabsichtigt. Er widerlegt den Split nicht — er zeigt, wo `billig` an einem Modell
korrekt ist: **wenn der Text die Schwäche mitmeint.** In Teil III meint er sie nicht.

### Karte 5 — `bill`: **der Korpus benutzt „die Rechnung" häufiger für das Kalkül als für das Geld**

Run 1 verbietet das freie `die Rechnung` und begründet es mit der Wendung „jemandes Rechnung geht nicht auf".
Der Korpus bestätigt die Diagnose und benennt den Anteil: von 11 `Rechnung`-Token sind **6 das Kalkül**
(„die Rechnung dahinter sehen", „**Die Rechnung geht nur auf, wenn** …", „Die Rechnung von Teil 1",
„die Rechnung in Token", „zahlt die umgekehrte Rechnung") und **3 das Geld** — und **alle drei Geldbelege
sind gebunden**: „die Rechnung **für** die Tokens", „die Rechnung **für** die Observability",
„die **Monats**rechnung".

> **Die Frage vor dem Schreiben:** *Steht neben `Rechnung` ein **für**-Ausdruck, ein Genitiv oder ein
> Erstglied?* Nein → umbauen; der Satz liest sonst als *Kalkül*.

- *„shows up on the bill"* → „**schlägt auf der Rechnung für die Inferenz durch**"
- *„the monthly bill collapses into one useless number"*
  → „**Die Monatsrechnung schrumpft auf eine einzige nutzlose Zahl**" *(Korpusnähe: „…statt der nutzlosen
  Gesamtsumme ‚wir haben X ausgegeben'")*
- *„## Modelling the bill"* → **umbauen**, nicht „Die Rechnung modellieren" (liest als *das Kalkül
  kalkulieren*): „**## Woraus die Rechnung entsteht**"
- *„the lever that moves the bill most"* → „**der Hebel mit der größten Wirkung auf die Rechnung**" —
  zulässig, weil der Genitiv-/Präpositionalrahmen die Geldlesart trägt

---

## 3. RUN DISAGREEMENTS

Twelve places where the two blind runs differ. Both positions kept; the losing argument is never deleted.

| # | Row | Run 1 | Run 2 | Resolution + reason |
|---|---|---|---|---|
| **D-1** | **`lever`** | `die Stellschraube`, **WEAK**, with four reasons against `der Hebel`; §6.6 self-grades reason (4) as unevidenced | `die Stellschraube`, **SETTLED**, three reasons against `der Hebel`; keeps `der Hebel` only for `leverage` | **Neither.** Both are overruled by the corpus: **`der Hebel`** (15 tokens, 8 files, 3 H2s, and the verbatim Part III collocation). Rule §3: *where canon metaprose disagrees with shipped forms, the corpus wins* — here the sheets are not even canon, and the canon's `Stellschraube` row names a **different** referent. **Both runs' idiom evidence is preserved as a collocation firewall (Karte 1), and it does real work:** it is why the German writes „zu einem der Hebel greifen" and never „alle Hebel in Bewegung setzen", and why ⛔ `der Kostenhebel` stands |
| **D-2** | **`knob`** | „⚠ `lever` und `knob` landen auf demselben deutschen Wort … müssen dieselbe Zeichenkette benutzen" | folds `dial` in too: „wer *dial* separat prägt, erzeugt zwei Namen für einen Referenten" | **Both dissolved by D-1.** Three English words, three German words, all three corpus-attested; the „one referent" premise was wrong — they are three referents that English also names separately. The canon row `_language.md:1084` says `Stellschraube` = *knob*, in those words |
| **D-3** | **`dial`** | not addressed | ⛔ *der Regler* („Audio/UI") | **Run 2 reversed.** Corpus ships `der Regler` **6× in 4 files**, always for a continuously set value, with the same verb *drehen an* („ein Regler, an dem Sie drehen"; „α ist der Regler zwischen …") |
| **D-4** | **`cheap`** | ⛔ `billig` als Laufterm — „eine **sachliche**, keine stilistische Verfälschung" | ⛔ `billig` — „derselbe Fehlertyp wie ⛔ *die Ausreißer* für *the tail*" | **Both partially reversed.** The ban is right **for the model-price sense** (corpus: `günstiger` 3/3 there) and wrong **for the procedure sense** (corpus: `billig*` 30 in 12 files, plus the shipped antonym `teuer`). Ruled as a corpus-verified split, not a ban (Karte 4) |
| **D-5** | **`spend`** | „die Ausgaben — **nur im Plural**"; ⛔ *die Ausgabe* Singular, „ein Referent-Zusammenstoß INNERHALB eines Wörterbuchlemmas"; „die Token-Ausgaben" | identical numerus split, same ⛔, same compound „die Token-Ausgaben" | **AGREED×2 and both wrong.** This is the wave-2 finding in its purest form: two blind runs converged because they read the same DWDS lemma. The corpus shows the **plural** is already the *output* plural (12/12, 7 files) and ships **`Ausgabe-Token`**, which makes `Token-Ausgaben` an indefensible minimal pair. Ruled: `die Kosten` as running term, `die Ausgaben` only inside an explicit money frame, verb `ausgeben` free (Karte 2) |
| **D-6** | **`budget`, Mengenzweig** | ⛔ *das Schrittbudget*, *das Ratenbudget* — „null Attestierung, das wäre die *Latenzbudget*-Prägung zum dritten Mal" | licenses **das Schrittbudget**, **das gemeinsame Ratenbudget** | **Run 2, on corpus evidence.** `Schrittbudget(e)` is shipped **7×**; run 1's „null Attestierung" is a fabricated absence — it never grepped the delivered locale. ⚠ Run 1's *instinct* was sound and is preserved in Karte 3: the pattern licenses the **form**, which is exactly why `Latenzbudget` stays OPEN while `Schrittbudget` is confirmed |
| **D-7** | **`budget`, Schreibung** | does not decide | **Hausform: geschlossen `Tokenbudget`** (heise), Bindestrich nur bei mehrgliedrigem Erstglied | **Run 2 reversed, twice over.** Canon `_language.md:1090` writes **`das Token-Budget`**; corpus writes `Token-Budget` **6×**, `Tokenbudget` **0×**. The real regularity is *German first element → closed; English/loan first element → hyphen*, and the corpus obeys it in all six compounds |
| **D-8** | **`burn rate`** | **kept-EN, artikellos** — „Alerts auf die Burn Rate"; the noun stays OPEN | **OPEN**, „wo ein Artikel erzwungen ist: **feminin**"; adds `Cash-Burn-Rate` as the wrong-referent counter-evidence | **Run 2's fallback promoted to incumbent by the corpus:** „**die Burn Rate des Fehlerbudgets**" — article-bearing, feminine, *at the error budget*, on the very page Part III cross-references. Run 1's „artikellos" would contradict a shipped sentence. ⚠ The **external** attestation question stays open in `rag.md` §3; the shipped **string** does not |
| **D-9** | **„das Budget verbrennen"** | ⛔ „**das Budget verbrennen**" — „Kalk von *burn*" | not addressed | **Run 1 reversed.** Corpus, observability/deep-dive.md:81: „…die Frage, welches Feature oder welcher Kunde **das Budget verbrennt**". A shipped sentence outranks a calque diagnosis |
| **D-10** | **`cost per accepted answer`** | **Genitiv** „die Kosten einer akzeptierten Antwort", *because* „die Duden-Seite zur Präposition `pro` liefert **404**, ich kann also nicht entscheiden" | **Akkusativ** „die Kosten **pro akzeptierte** Antwort", citing the actual Duden lemma `pro_je_zu_jeweils_fuer`: „Präposition mit Akkusativ oder Dativ", Beispiel „pro verkauftes oder verkauftem Exemplar" | **Run 2.** Run 1's entire construction is a detour around an obstacle that turned out to be a **wrong URL**, and run 1 says so in §6.2 („Ich habe sie **umgangen**, nicht **entschieden**"). This is the 404-is-not-a-null-finding failure mode, caught by its twin. ⚠ Run 1's Genitiv stays on the record as a permitted **anaphor** („die Kosten je akzeptierter Antwort") — it is not wrong, it was just not necessary |
| **D-11** | **`commitment`** | 2 senses + 1 Randfall; *no commitment* → „**ohne Bindung**" | 3 senses; *no commitment* → „**ohne Mindestlaufzeit**" | **Run 2.** In a Reserved-tier list („no commitment, one month, or six") the contrast is **duration**, and „ohne Bindung, mit einem Monat oder mit sechs Monaten Bindung" (run 1) says *no obligation* where the source says *no minimum term*. Both runs agree on ⛔ `das Commitment` |
| **D-12** | **canon coverage** | builds a 21-row „Kanon-Lückenliste", incl. `Kosten`, `Budget`, `Stellschraube` | states outright that only `Fehlerbudget` and `Provisioned Throughput` have canon rows | **Both wrong; see §0.** Four SETTLED §1.1 rows sit inside this slice. ⚠ **Consequence:** run 2's collocation lists for `Ausgaben` and `Budget` both contain **„deckeln"**, which `_language.md:1089` ⛔s by name. That is not a run-vs-run disagreement — it is a run-vs-canon defect, and it would have shipped |

**Where the two runs agree and I did NOT let the agreement count as verification:**
`die Ausgaben` for *spend* (D-5, reversed), `dediziert` (one de.wikipedia sentence read twice → `THIN×2`),
`das Fehlerbudget` (one canon row read twice → `THIN×2` on attestation, upheld on the corpus).

---

## 4. VOCABULARY FOOTPRINT

Flat, deduplicated German content words appearing in my worked sentences and sense cards. Stage 2 uses this
for cross-slice collisions.

Abbrennen · Abhängigkeit · Abrechnung · Anbieter · Anfrage · Antwort · Aufwand · Auslastungsschwelle ·
ausgeben · Batch · begrenzen · benutzen · billig · Bindung · Budget · Burn Rate · Cache · Caching ·
Dimension · drehen · Durchsatz · Eingabe-Token · einfach · einplanen · Einstellung · Erfolgsquote ·
erschöpfen · Fehlerbudget · Feature · Gateway · Gesamtsumme · günstig · Hebel · Kapazität · Kosten ·
Kostenausschlag · Kostenbudget · Kostenregeln · Kostenstelle · Kostentreiber · Latenz · Modell ·
Monatsrechnung · Nutzer · Obergrenze · Parameter · Preis · Preismodell · Preisseite · Preisstufe ·
Prüfung · Quantisierung · Rabatt · Rechnung · Regler · reservieren · Reservierung · Richtlinie · Routing ·
Schrittbudget · Speichergebühr · Spitzenmodell · sparen · Stellschraube · Steuerung · Streaming ·
Stückkosten · Stundengebühr · Team · teuer · Token · Token-Budget · Tokenpreis · Tokenverbrauch ·
umsonst · veranschlagen · verbrauchen · verbrennen · Verbindung · Verfahren · Wirtschaftlichkeit ·
zuordnen · Zusage · Zusicherung

⚠ **Collision candidates I can already name from inside my own slice** (stage 2 confirms or clears):
`die Ausgaben` (mine = money, corpus = *output* — **live**, see D-5) · `der Durchsatz` (slice A/E,
`throughput`) · `die Obergrenze` (slice on `cap`/`limit`) · `das Budget` (cross-slice, brief §5) ·
`der Regler` / `die Stellschraube` (whoever holds `dial`/`knob`) · `die Kosten` (everyone) ·
`die Bereitstellung` (I avoided it for *provisioned* precisely because §1.2 holds it for *deployment*) ·
`die Rechnung` (`llmops` vs any evaluation page using it for *Kalkül*) · `verbrauchen` (token vs error
budget) · `die Kostenstelle` (shipped once in a looser sense than Part III's cost-centre referent).

---

## 5. SPREAD — which of the 10 Part III files each term occurs in

| Term | n | files | Files |
|---|---|---|---|
| **cost** | 86 | **10** | all ten |
| **budget** | 49 | **8** | cloud-platforms/dd, llmops/dd, llmops/ix, overview, production-failures, serving/dd, serving/ix, tooling/dd |
| **price** | 30 | **7** | cloud-platforms ×2, llmops ×2, production-failures, serving/ix, tooling/dd |
| **bill** | 29 | **7** | cloud-platforms ×2, llmops ×2, production-failures, serving/dd, tooling/dd |
| **spend** | 25 | **7** | cloud-platforms ×2, llmops ×2, production-failures, serving/dd, tooling/dd |
| **lever** | 22 | **6** | cloud-platforms/dd, llmops ×2, production-failures, serving ×2 |
| **dedicated** | 13 | **6** | cloud-platforms ×2, serving ×2, tooling ×2 |
| **cheap + cheaper** | 49 | **5** | cloud-platforms/dd, llmops ×2, production-failures, serving/dd |
| **pricing** | 17 | 4 | cloud-platforms ×2, llmops ×2 |
| **discount** | 10 | 4 | cloud-platforms ×2, llmops ×2 |
| **billing** | 7 | 3 | cloud-platforms ×2, llmops/dd |
| error budget · commitment · knob · token diet · provisioned throughput · per-token · economics · charge | ≤10 | 2 | — |
| burn rate · unit economics · cost per accepted answer | ≤3 | 1 | — |
| capacity reservation · free tier | 0 | 0 | — |

**Terms spanning ≥3 files — ONE binding string each, decided centrally:**
`cost` (10) · `budget` (8) · `price` (7) · `bill` (7) · **`spend` (7 — the widest spread in the wave)** ·
`lever` (6) · `dedicated` (6) · `cheap` (5) · `pricing` (4) · `discount` (4) · `billing` (3).
Of these, **`spend`** and **`lever`** are the two whose binding string this ledger *changed* against both
runs; **`budget`** is the one whose spelling it changed; **`cheap`** is the one whose blanket rule it split.

---

## 6. CANON DELTA — report only, never edit

| # | File · Section | Current text | Proposed | Reason |
|---|---|---|---|---|
| **CD-1** | `_language.md` §1.1, `Stellschraube` row (`:1084`) | „Das ist die deutsche Wiedergabe für *the knobs that control this*." | Add: „**⚠ Nur für `knob`.** `lever` → **der Hebel** (Korpus: 15 Token, 8 Seiten, 3 H2, u. a. „zu einem der **Hebel** greifen"); `dial` → **der Regler** (Korpus: 6 Token). Drei englische Wörter, drei deutsche — nicht zusammenlegen." | Two independent blind runs widened this row to `lever` because it does not say it is narrow. That is the „unapplied, not incomplete" shape for the third time |
| **CD-2** | `_language.md` §1.1 — **new row** | — | **`Hebel` · der Hebel · die Hebel · des Hebels · CORPUS PRECEDENT (15 Token, 8 Seiten, 3 Überschriften).** Fügung: „zu einem der Hebel greifen", „der wirksamste/wichtigste Hebel gegen X". ⛔ „alle Hebel in Bewegung setzen", ⛔ „am längeren Hebel sitzen", ⛔ „den Hebel ansetzen" als Substantivwiedergabe, ⛔ `der Kostenhebel` | The corpus decided this ten times before the canon looked; without a row, the next renderer re-coins it |
| **CD-3** | `_language.md` §1.1 — **new row** | — | **`Regler` · der Regler · die Regler · des Reglers · CORPUS PRECEDENT (6 Token, 4 Seiten)** für `dial`. Fügung: „ein Regler, an dem Sie drehen"; „der Regler zwischen X und Y" | Run 2 ⛔'d it from the dictionary; the corpus ships it. Without a row, `dial` (6× in Part III) gets a fourth coinage |
| **CD-4** | `_language.md` §1.1 — **new row** | — | **`Ausgaben` (spend)** — **⚠ Warnzeile, keine Freigabe.** „*spend* → **die Kosten** als Laufterm; **die Ausgaben** nur im expliziten Geldrahmen. ⛔ `die Token-Ausgaben` (Korpus schreibt `Ausgabe-Token` für *output tokens*), ⛔ `die KI-Ausgaben`. Verb `ausgeben` frei." | The numerus split both runs relied on is contradicted by 12 shipped plural `Ausgaben`, all of them *outputs*. This is the highest-traffic wrong ruling in the slice (7 files) |
| **CD-5** | `_language.md` §1.1, `Budget` row (`:1090`) | „Regel: das Kompositum trägt den Sinn, das nackte *Budget* trägt ihn nicht" | Add: „**Genauer, nach dem gelieferten Korpus: Kompositum bei der Erstnennung einer Dimension, danach `das Budget` als Anapher** (Korpus: 57 freie Token, 13 Seiten — „Ein Budget ist eine Obergrenze"). **Schreibung:** deutsches Erstglied geschlossen (`Schrittbudget`, `Fehlerbudget`, `Kostenbudget`, `Teilbudget`), englisches Erstglied mit Bindestrich (`Token-Budget`, `Retrieval-Budget`, `Retry-Budget`). ⛔ `Tokenbudget` geschlossen." | The row as written forbids something the corpus does 57 times, and one run therefore proposed a spelling (`Tokenbudget`) that contradicts both the row and the corpus |
| **CD-6** | `_language.md` §1.1 — **new row** | — | **`billig / günstig`** — Referentensplit, korpusbelegt: **Preis eines Modells/Tarifs → günstig** (Korpus 3/3), **Verfahren/Aufwand → billig** (Korpus 30 Token, 12 Seiten); Antonym durchgehend **teuer**. ⛔ *preiswert* | Both runs banned `billig` outright; the shipped corpus would have to be rewritten in 12 files to comply |
| **CD-7** | `rag.md` §3, `burn-rate alerting` (OPEN) | OPEN, no German attestation | **Keep OPEN for the attestation question, and add the corpus form so no renderer re-opens the string:** „Gelieferte Form: **die Burn Rate** (feminin, artikeltragend) — „die Burn Rate **des Fehlerbudgets**", „**Alerts auf die Burn Rate**". Verbal: „wie schnell Sie es **verbrauchen**"; Substantiv „ein schnelles **Abbrennen**"." | Run 1 would have shipped an article-less form that contradicts a delivered sentence, on the strength of a null finding about *external* sources |
| **CD-8** | `rag.md` §2, Zeile 103 — **confirmation, requested** | „… Little's Law, Vendor-Lock-in, ~~Managed Endpoint~~, ~~Provisioned Throughput~~ → Klasse 1, ~~Instrumentation~~, OpenTelemetry (OTel) …" | **#327 is applied and visible; nothing further on that line is in the same shape *within slice D*.** ⚠ Two neighbours are worth a look by their owning slices, and I am **reporting, not litigating**: **(a) `Soft Cap / Hard Cap`** sits kept-EN in the same list while the canon and the corpus lead **die Obergrenze** (41 Token, 11 Seiten; „das Cap" ⛔ by `:1089`) — the §2 entry is *defensible* as the pattern's Zitierform, but the line says so nowhere; **(b) `Vendor-Lock-in`** carries *Vendor* while the corpus answer for that head noun is **der Anbieter** (21 : 0, baseline). | The brief asked me to confirm the line; these are the only two entries left with the head-noun-led-in-German shape, and both belong to other slices |
| **CD-9** | `rag.md` §2 — annotation, not a change | `Provisioned Throughput` → Klasse 1 | No dissent. Recording only that the **Appellativ** branch still needs an adjective, and this ledger does not set it — see §7 | The head noun `der Durchsatz` is settled; the modifier is not |

---

## 7. NEEDS A DECISION, NOT MORE RESEARCH

1. **The `spend` string — 7 files, and German has no second noun.** Further attestation cannot help: DWDS
   and Duden both license `die Ausgaben` for money, and the *corpus* has already spent the plural on
   *output*. Somebody must simply choose. **Recommendation: `die Kosten` as the running term, `die Ausgaben`
   only inside an explicit money frame, verb `ausgeben` unrestricted, ⛔ `Token-Ausgaben` / `KI-Ausgaben`.**
   **Cost of being wrong:** if we keep `die Ausgaben`, a reader meets „die Ausgaben des Teams" on a page that
   also says „Tool-Ausgaben" and „Ausgabe-Token"; the sentence stays fluent and means the wrong thing. If we
   take my ruling and it is wrong, we lose the English cost/spend nuance in ~25 sentences — a flattening,
   recoverable by collocation. **The asymmetry is the argument.**
2. **The adjective in `provisioned throughput` (Appellativ).** Run 2 coined **`der zugesicherte Durchsatz`**
   and then correctly refused to grade its own coinage as settled; run 1 offered **`der bereitgestellte /
   dedizierte Durchsatz`**, and *bereitgestellt* collides with `die Bereitstellung` = *deployment* (§1.2).
   Corpus: `Durchsatz` 3, always bare. **Recommendation: `der dedizierte Durchsatz`** — it is the one form a
   German source actually printed (Computerwoche), it reuses an adjective this slice already rules, and it
   does not invent a third word. **Cost of being wrong:** low; 10 occurrences in 2 files, and the product-name
   branch (Klasse 1) carries most of them.
3. **`Chargeback` / `Showback` genus.** 9 occurrences, no article-bearing German sentence at any tier, both
   runs looked. More search will keep returning English. **Recommendation: ship article-free
   („**Showback** weist jedem Team seinen Verbrauch aus; **Chargeback** belastet weiter") and use the compound
   where a case is forced („das Chargeback-Verfahren").** **Cost of being wrong:** an invented `das Showback`
   is unrecoverable once printed; article-free prose is merely stiffer.
4. **`cost per accepted answer` case, in a heading.** Duden licenses **both** Akkusativ and Dativ after `pro`.
   That is a house choice, not a research question. **Recommendation: Akkusativ throughout
   („pro akzeptierte Antwort"), Genitiv permitted as the later anaphor.** **Cost of being wrong:** zero
   grammatically; the only real cost is *inconsistency* if two pages pick differently — hence one string.
5. **`der Kostenhebel`.** With `lever` = `der Hebel`, the compound becomes tempting and it is the single form
   in which the finance-leverage reading actually bites. No corpus, no dictionary will settle it.
   **Recommendation: ⛔, rebuild as „die Hebel an den Kosten" / „die Hebel, die die Rechnung bewegen".**
   **Cost of being wrong:** a slightly longer phrase, against a term that in a chapter about bills and
   break-even reads as *Fremdkapitalhebel*.

---

## 8. WHAT THIS PASS COULD NOT DO

1. **It did no new lexicography, by design — so every dictionary claim below the corpus layer is still only
   as good as the run that made it.** Where both runs read the same source (DWDS `Stellschraube`, the single
   de.wikipedia `Server` sentence for `dediziert`, the canon row for `Fehlerbudget`), I labelled the row
   `THIN×2` rather than re-verifying it. `dediziert` in particular ships on **one** sentence, read twice.
2. **The corpus is Teile I + II only.** Part III German does not exist yet, so „CORPUS PRECEDENT" here means
   *what the delivered pages already do*, not *what Part III measured*. Two of my reversals (`spend`,
   `cheap`) rest on referent distributions in Parts I–II that Part III could genuinely shift — Part III is
   the first part where money is the **subject**, not an aside. If a later pass finds Part III forcing the
   money plural into a page that also discusses model outputs, CD-4 is the row to revisit.
3. **I could not measure the register of `der Hebel` in German IT prose**, only its frequency in our own
   corpus. The `Hebel` ruling is a **corpus** ruling, not an attestation ruling; nobody has shown a heise/iX
   sentence with `der Hebel` in this sense. The runs' idiom evidence is real and I kept it — I did **not**
   show that the idioms are dormant in technical register, I showed that our own pages write around them.
4. **The paid full-text layer is unreached, for the fourth wave running** — iX/c't archives, dpunkt,
   Rheinwerk, O'Reilly DE. That is exactly where `Unit Economics`, `Burn Rate` at the error budget,
   `Showback`/`Chargeback` and an engineering-register `Hebel`/`Stellschraube` would be decided. Run 1 names
   **iX 06/2026 „KI-Kosten im Griff"** as the perfect source for this entire slice; it is behind the paywall.
5. **I did not re-verify the concordance defects the runs reported.** Run 1 documents 17 unlisted `cheap*`
   occurrences (`cheapest` 12, `cheapness`, `cheaply`) plus three coverage gaps (`Chargeback`/`Showback`,
   `overspend`, free `burn` forms); the concordance header I read confirms the surface-form counter stops at
   `{'cheaper': 16, 'cheap': 17}`, which is consistent with run 1's account, but I checked the counter, not
   the corpus. **The `cheapest` sentences carry an infographic card title and a take-away bullet** — a
   renderer working from the concordance alone still meets them cold.
6. **Where I guess, it says so:** `der Kostenausschlag` for *overspend* is my transfer of a corpus word to a
   neighbouring referent (HOUSE, not attested for that use); „**## Woraus die Rechnung entsteht**" is my
   heading rebuild; the `billig ↔ günstig` boundary is drawn from a 30 : 5 distribution with one
   acknowledged counter-case, not from a rule anybody stated; and the claim that the corpus's `Budget` usage
   is *„Kompositum bei Erstnennung, Anapher danach"* is a pattern I read out of the sentences — the corpus
   nowhere states it.
7. **No project-wide total is computed here.** Two totals move as a result of this ledger and stage 2 owns
   the arithmetic: the count of **German-led (Klasse 3) rows** gains from `Hebel` and `Regler` (**+2**, minus
   whatever stage 2 finds already counted), and the count of **OPEN rows** is unchanged in net —
   `unit economics`, `token diet`, `Latenzbudget`, `Chargeback/Showback` stay open, `burn rate`'s *shipped
   string* closes while its *attestation row* stays open (**±0**, one row splits in two questions).
