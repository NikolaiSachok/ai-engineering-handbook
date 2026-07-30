# LEDGER-C — Gate 6.5 stage 1, slice C (Plattform · Souveränität · Residenz · Mandanten)

Reconciles `OUT-C-run1.md` and `OUT-C-run2.md` (both read in full), against the **27 shipped German
pages** (issue #328), the referent baseline, and `editorial/canon/de/{_language.md,rag.md,ai-sdlc.md}`.
No new lexicographic research. Every count marked `CORPUS(n)` is **my own** measurement over
`i18n/de/docusaurus-plugin-content-docs/current/**`, not copied from either sheet.

---

## 0. The three findings that change how this slice should be read

**(1) The slice's declared doubling blind spot is dissolved, not confirmed — by a source neither run
pointed its method at.** Both runs worried that `Anbieter` rests on BSI documents they both read, so an
`AGREED ×2` would only re-report the regulator's register. **The shipped German answers the row
independently: `Anbieter` 38, `Provider` 0** (the single `Provider` is inside the OTel attribute name
`gen_ai.*`, class 1 — baseline, verified). And it is not a bare count: **10 genitives (`des Anbieters`),
3 dative plurals (`den Anbietern`), 22 article-bearing occurrences across 8 pages**, and the referent is
*ours*, verbatim: „die API **des Anbieters**", „Hat **der Anbieter** das Modell stillschweigend auf eine
neue Version umgestellt", „das SDK **des Anbieters**", „**beim Anbieter** zwischengespeichert".
⇒ `Anbieter` is **CORPUS PRECEDENT(38)**, *not* `THIN×2`. It was never a gap; it was an unrecorded ruling.

**(2) One row IS `THIN×2`, and it is `Perimeter`.** It rests on exactly one document — the BSI Zero-Trust
position paper — for genus, register *and* referent. Corpus: 0. Neither run produced a single heise/iX/c't
sentence with `der Perimeter`. DWDS licenses **both** m and n and therefore decides nothing. And the two
runs, reading *the same PDF*, report **28** vs **34** occurrences: the doubling did not even reproduce the
measurement, let alone corroborate the source. `AGREED ×2` here is worth less than one heise sentence.

**(3) The corpus overturns a collocation both runs got wrong — and run 2 cited a corpus quote that does
not exist.** Run 2 bans `pro` („⛔ *pro Projekt* im Fließtext — `je` ist die Korpusform, vgl. „je Anfrage""),
and run 1 writes „Kosten **je Anfrage**", „Kontingente **je Region und Modell**". Measured over the shipped
German: **`pro Anfrage` 6 · `je Anfrage` 0.** The string run 2 cites as the corpus form is absent from the
corpus. The corpus is not "je wins" — it **splits by what is being counted**: `pro` for a rate per *event*
(`pro Anfrage` 6, `pro Aufruf` 4, `pro Schritt` 4, `pro Feld` 2, `pro Antwort` 2), `je` for a share per
*partition or unit of content* (`je Chunk` 3, `je Token` 3, `je Dokument` 2, `je Sprache`, `je Anwendung`,
`je Teilaufgabe`). Slice C's highest-frequency collocation — *cost per request* — therefore ships as
**„die Kosten pro Anfrage"**, while *per tenant / per region / per project* ship as **„je Mandant"**,
**„je Region"**, **„je Projekt"**.

---

## 1. Binding table

Class: 1 = identifier/untouchable · 2 = kept-EN loan · 3 = German-led (gloss at first mention) · 4 = fully German.

| Terminus | German | Kl. | Status | Artikel / Plural / Genitiv | Kollokation | ⛔ verworfen | Evidenzgrad |
|---|---|---|---|---|---|---|---|
| **platform** (Appellativ) | **die Plattform**; Erstnennung gebunden **die KI-Plattform** / **die Cloud-Plattform** | 3 | **BOUND** | die Plattform · die Plattformen · der Plattform | „**die Plattform liefert Modelle aus**"; „**auf einer Plattform laufen**"; die Plattform-Guardrails (durchgekoppelt) · **die Plattformwahl** (dt. Erstglied, zusammen) | ⛔ *das Portal* · ⛔ *die Umgebung* (im Korpus für *environment*, 5×) · ⛔ *die Platform* · ⛔ **`Cloud-AI-Plattform`** (§3: **KI**, nicht AI) | CORPUS(1) + RECONCILED (run 2's 3-Sinn-Spaltung gewählt) |
| **platform** (Eigenname) | *Gemini Enterprise Agent Platform*, *Google Cloud Platform* — unverändert, unflektiert | **1** | **BOUND** | — | Artikel + Flexion tragen die Unterscheidung, nicht die Großschreibung | ⛔ Übersetzung von Produktnamen | AGREED×2 |
| **provider** · **vendor** | **der Anbieter** — *ein Referent, ein Name* | 3 | **CORPUS PRECEDENT** | der Anbieter · die Anbieter (Nullplural), Dat. Pl. **den Anbietern** · **des Anbieters** | „**die API des Anbieters**"; „**beim Anbieter**"; „**den Anbieter wechseln**"; „**vom Anbieter betrieben**"; *provider-agnostic* → „**anbieterunabhängig**" | ⛔ **der Provider** (Duden + DWDS: der **ISP**) · ⛔ *der Dienstleister* · ⛔ **der Betreiber** (KI-VO: das sind **Sie**) · ⛔ *der Hersteller* (Kanon: Herstellerdoku) · ⛔ *der Verkäufer*, *der Lieferant* | **CORPUS(38)** — 22 artikeltragend, 10 Genitive, 3 Dat. Pl., 8 Seiten |
| **managed** (attributiv) | **kept-EN, unflektiert, großgeschrieben, nur als Erstglied**; vor engl. Grundwort gespreizt, vor dt. Grundwort **durchgekoppelt** | 2 | **BOUND** | kein eigener Artikel — **Genus vom Kopfnomen** | „**Managed Services**" · „**die Managed-RAG-Stufe**" · „**das Managed-Service-Angebot**"; Prädikat → „**vom Anbieter betrieben**" | ⛔ *gemanagt* (Duden: umgangssprachlich) · ⛔ *verwaltet* (Herstellerlokalisierung; `Verwaltung` = IAM) · ⛔ *betreut* · ⛔ „Managed Plattform" (Deppenleerzeichen) | AGREED×2 (~140 bzw. 106 de.wikipedia-Treffer gegen 0:1:2) |
| **managed service** | **der Managed Service** | 2 | **BOUND** | der Managed Service · die Managed Services · des Managed Service[s] | „die Guardrails **als Managed Services** beziehen" | ⛔ *der verwaltete Dienst* · ⛔ *der Managed Dienst* · ⛔ „der Service" nackt (bleibt verboten; hier steht er **gebunden**) | AGREED×2 + Kanonlizenz (`_language.md` §1.1.d, `Service`-Zeile) |
| **managed endpoint** | **der Endpunkt des Anbieters**; Erstnennung „…laufen als **vom Anbieter betriebene Endpunkte** (*managed endpoints*)" | 3 | **BOUND — bereits entschieden** (`rag.md` §2, gestrichen gegen #327) | der Endpunkt · die Endpunkte · des Endpunkts | „**einen Endpunkt bereitstellen**"; „das Modell **läuft hinter einem Endpunkt des Anbieters**" | ⛔ **nacktes `Managed Endpoint`** · ⛔ *der Managed-Endpunkt* (Hybrid, §1.0 Glossreinheit) | **RESOLVED** (Streichkasten) + **CORPUS(6)**: `Endpunkt` 6 : `Endpoint` 0 |
| **managed RAG** | **`Managed RAG` artikellos** in Subjektstellung; sonst gebunden **die Managed-RAG-Stufe**, *das Managed-RAG-Angebot* | 2 | **OPEN** (incumbent held: artikellos + gebunden; **schließt**, wenn ein deutscher Fachsatz `RAG` oder `Managed RAG` einen Artikel anhängt) | **kein Artikel erfinden** | „**Jede Plattform verkauft außerdem eine Managed-RAG-Stufe.**" | ⛔ **„das Managed RAG"** mit eigenem Artikel | **RECONCILED (run1 vs run2, ich wähle run 1).** Run 2 leitet `das` vom „bereits gesetzten `das RAG`" ab — **diese Zeile existiert nicht**: im ausgelieferten Korpus trägt `RAG` **nie** einen Artikel (124 Vorkommen, alle Komposita oder artikellos), im Kanon gibt es keine Genuszeile. |
| **perimeter** | **der Perimeter** | 2 | **THIN×2** | der Perimeter · die Perimeter · **des Perimeters** | „**hinter dem Perimeter**"; „**innerhalb / außerhalb des Perimeters**"; „**den Perimeter verlassen**"; **der Perimeterschutz** | ⛔ *die Vertrauensgrenze* (= *trust boundary*, Welle 2) · ⛔ *die Sicherheitsgrenze* (= *security boundary*, Pilot) · ⛔ *die Netzgrenze* (= *network boundary*) · ⛔ *das Firmennetz*, *die Umfriedung* · ⚠ **Duden hat kein Lemma `Perimeter`** — nicht zitieren · ⚠ DWDS-Wortprofil ist **schweizerisch-raumplanerisch** (§1.3.4) | **THIN×2** — eine einzige BSI-PDF trägt Genus, Register *und* Referent; Korpus 0; keine Fachpresse; die beiden Läufe zählen **dieselbe** Datei als 28 bzw. 34 |
| **region** | **die Region**; **Erstnennung gebunden: die Cloud-Region** | 3 | **BOUND** | die Region · die Regionen · der Region | „**in derselben Region halten**"; „**in der gewählten Cloud-Region**"; „**an die Region binden**"; „**Kontingente gelten je Region und je Modell**"; *cross-region* → **regionsübergreifend** / **zwischen Regionen**; *in-region* → **in derselben Region** | ⛔ **„Daten in der Region halten"** — „in der Region" ist die stehende deutsche Wendung für *im Umland* · ⛔ *die Zone* (im Korpus Azure „Data Zone", Klasse 1) · ⛔ *das Gebiet*, *der Raum* | **RECONCILED (run1 vs run2, ich wähle run 2)** — run 1 schreibt die Fügung, die run 2 als Fehllesung nachweist. + **CORPUS(3)**: `Regionen` ist im ausgelieferten Deutsch bereits für **Layout-Regionen** vergeben (`ingestion/deep-dive.md`) → Bindung, keine Umbenennung |
| **data residency** | **⚖ ENTSCHEIDUNG OFFEN — siehe §7.1.** Vorläufig: **`Data Residency`** kept-EN, artikellos, **Pflichtglosse bei Erstnennung**, danach **Konstruktion** | 2 | **OPEN (incumbent held: keine)** — Feld ohne Incumbent | **kein Artikel** bis zur Entscheidung | „**Data Residency – die Zusage darüber, wo die Inferenz stattfindet**"; „*global* heißt ausdrücklich: **keine Zusage über den Ort**"; „**die Daten an eine Region binden**" | ⛔ **die Datenhoheit** (= *sovereignty*; kollabiert genau die Unterscheidung) · ⛔ *die Datenhaltung* (das Speichern) · ⛔ *die Datenlokalisierung* (staatliche Auflage, anderer Handelnder) · ⛔ *der Datenstandort* · ⛔ *die Residenz* nackt (Fürstensitz) | **RECONCILED-PENDING-RULING** — run 1 setzt *die Datenresidenz*, run 2 ⛔-t genau das; **beide lesen dieselbe Zählung (1 de.wikipedia-Artikel) gegensätzlich** |
| **residency** (bloß) | **Konstruktion, kein Substantiv**: „die Zusage über den Ort", „wo die Inferenz stattfindet" | 3 | **OPEN (incumbent held: kein Substantiv; schließt mit einem flektierten deutschen Substantiv, das einen Datenbestand im Genitiv regiert)** | — | „**der Regler zwischen Ort und Kapazität**"; „**tauscht die Zusage über den Ort gegen Kapazität**"; *AI residency* → „**wo das Modell rechnet**" | ⛔ *die Residenz*, *die Ansässigkeit* · ⛔ **die KI-Residenz** (Prägung auf einer offenen Zeile) | AGREED×2 (beide OPEN, beide bauen um) |
| **sovereignty** | **die digitale Souveränität** | 3 | **BOUND** | die Souveränität · kein Plural · der Souveränität | „digitale Souveränität **ermöglichen / gewährleisten**"; **das Souveränitätsversprechen**, **die Souveränitätsgarantie**; **die Datenhoheit** nur *innerhalb* dieses Feldes für die Kontrollfrage | ⛔ *die Datensouveränität* (eigener Gaia-X-Begriff, im Korpus nicht vorhanden) · ⛔ *die Selbstbestimmtheit* · ⛔ *die Hoheit* nackt · ⛔ *die Datenhoheit* **als Kanonkopf** | AGREED×2 mit **unabhängiger Tier-3/Tier-5-Stütze** (de.wikipedia-Lemma *Digitale Souveränität*, 130 Artikel; heise ×3 in run 1, BSI-Presse in beiden) — **nicht THIN** |
| **sovereign** (Appellativ) | **souverän**, klein und flektiert | 3 | **BOUND** | die souveräne Cloud · eine souveräne Region · ein souveräner Endpunkt · souveräne Umgebungen | „**per Richtlinie an einen souveränen Endpunkt binden**"; „**In souveränen Umgebungen hinken die Spitzenmodelle hinterher.**" | ⛔ *hoheitlich* (Verwaltungsrecht) · ⛔ *unabhängig* (verliert die Rechtsdimension) · ⚠ **nie auf Personen/Teams** — dort heißt *souverän* „gelassen, überlegen" | AGREED×2 (run 1 SETTLED, run 2 WEAK; ich nehme run 1's Grad, weil nur run 1 flektierte Fachpressesätze vorlegt) |
| **sovereign** (Produktname) | *AWS European Sovereign Cloud*, *Microsoft Sovereign Cloud* — unübersetzt | **1** | **BOUND** | Artikel **die** (vom deutschen Kopf *die Cloud*), Name unverändert | „**die AWS European Sovereign Cloud**" (BSI wörtlich) | ⛔ „die europäische souveräne Cloud von AWS" · ⛔ *Sovereign-Cloud-Angebote* (mischt Name und Appellativ) → „**Angebote für souveräne Clouds**" | AGREED×2 |
| **tenancy** → **tenant** (`tenancy` 0, `tenant` 6) | **der Mandant**; *multi-tenant* → **mehrmandantenfähig** / **der Mehrmandantenbetrieb**; *per-tenant* → **je Mandant** | 3 | **CORPUS PRECEDENT** | der Mandant · die Mandanten · **des Mandanten** (n-Deklination) | **Die ausgelieferte Kette ist wiederzuverwenden, nicht neu zu bauen:** „Versehen Sie die Spans **mit dem Feature, dem Mandanten, der Route und dem Modell**" (`observability/deep-dive.md`) — Teil III schreibt dieselbe Kette. „**Warteschlangen je Mandant**"; „**Sicherheit im Mehrmandantenbetrieb**" | ⛔ *der Mieter* · ⛔ *der Nutzer* (der Korpus trennt beide im selben Satz) · ⛔ „des Mandants" · ⚠ nie „der Mandant" **nackt bei Erstnennung** (Duden-Leitsinn: Anwaltsmandant) | **CORPUS(3)** + AGREED×2 |
| **private endpoint** | **der private Endpunkt** (Adjektiv klein, flektiert) | 3 | **BOUND** | die privaten Endpunkte | „**Private Endpunkte: Der Verkehr zum Modell verlässt nie das eigene Netz.**"; *private connectivity* → „die private Anbindung" | ⛔ *das Private Endpoint* als Appellativ (Azure-Produktname bleibt Klasse 1) | **abgeleitet aus CORPUS(6)** (`Endpunkt` 6 : `Endpoint` 0) — nicht HOUSE, wie run 1 meinte |
| **egress** | **kein freies Substantiv — nur Kompositumsbildner: die Egress-Kosten, die Egress-Gebühren** | 2 | **BOUND (WEAK)** | kein Artikel auf `Egress` allein | „**Egress-Kosten zwischen Regionen**"; „**Daten, die eine Region oder eine Cloud verlassen, werden berechnet**" | ⛔ **der Datenabfluss** — die BSI verwendet das Wort für den **Sicherheitsvorfall**; wer *egress* so überträgt, macht aus einem Rechnungsposten eine Datenpanne · ⛔ *der/das Egress* nackt · ⛔ *die Ausleitung*, *der Datenausgang*, *die Datenausfuhr* | **RECONCILED (run1 vs run2, ich wähle run 2).** Run 1 stellt die Zeile OPEN, weil `insource:"Egress-Gebühren"` = 0 — und formuliert als Schließbedingung „ein Satz bei heise/iX/c't … mit einem deutschen Substantiv für die **Gebühr**". Run 2 legt genau den vor (heise-Schlagzeile „Gegen Amazon und **Egress-Gebühren**"). **Run 1's eigene Schließbedingung schließt die Zeile** — de.wikipedia war das falsche Korpus für einen Handelsterm. ⚠ Korpus: `egress` = 13 Treffer, **alle 13 sind `Regression`** — verifizierter Nullbefund, dieselbe Teilzeichenkettenfalle wie im Quelltext |
| **landing zone** | — | — | **kommt nicht vor (0, beidseitig verifiziert) — bewusst nicht vorentschieden** | — | — | — | AGREED×2 (Nullbefund) |
| **vendor lock-in** | **Vendor-Lock-in**, **artikellos** | 2 | **OPEN (Artikel; incumbent held: artikellos)** — schließt mit einem kasusmarkierten „der/das Vendor-Lock-in" bei heise/iX/INNOQ/dpunkt | **kein Artikel erfinden** | **Der Korpussatz existiert bereits:** „ein Abwägen zwischen **Portabilität und Vendor-Lock-in**" (`orchestration-frameworks/index.md`) — Schreibung *und* Artikellosigkeit sind ausgelieferte Praxis; *lock-in avoidance* → „**Vermeidung von Vendor-Lock-in**" | ⛔ „der/das Vendor-Lock-in" · ⛔ *Vendor Lock-In*, *Vendor Lock-in* (Getrenntschreibung; § 44(1)) | **CORPUS(1)** + §1.3.3 + AGREED×2 |
| **lock-in** (bloß) | Zustand → **der Lock-in-Effekt**; im Fließtext besser die **Konstruktion**: **die Bindung an einen Anbieter / an eine Plattform** | 2/3 | **BOUND** | der Lock-in-Effekt · die Lock-in-Effekte · des Lock-in-Effekt[e]s | „**Sie binden sich enger an den Anbieter.**"; „**Die Bindung entsteht am Zubehör, nicht am Endpunkt.**"; **die Wechselkosten**, **der Anbieterwechsel** | ⛔ „der Lock-in" nackt · ⛔ *die Kundenbindung* (Anbietersicht, positiv) · ⛔ *die Anbieterbindung* (1 Treffer) · ⛔ **die Herstellerabhängigkeit als Laufterm** — wer „Anbieter" sagt und „Hersteller-…" schreibt, hat zwei Namen für eine Firma | AGREED×2 (de.wikipedia-Lemma *Lock-in-Effekt*, maskulin, Definition nennt **Anbieter** und **Wechselkosten**) |
| **portable** (Adjektiv) | **umbauen**: „**wechselbar bleiben**", „**sich die Portabilität bewahren**", „**den Wechsel offenhalten**" | 3 | **OPEN (incumbent held: die Substantiv-/Verbalkonstruktion)** | — | H2 *Staying portable* → „**Die Portabilität wahren**" oder „**Den Wechsel offenhalten**" | ⛔ *tragbar* (physisch) · ⛔ *übertragbar* (kollidiert mit *transferable* und der DSGVO-*Datenübertragbarkeit*) · ⛔ **„portabel bleiben"** — behauptet, das System sei tragbar | **RECONCILED (run1 vs run2, ich wähle run 2).** Run 1 lässt „portabel bleiben" als WEAK zu und räumt im eigenen §6.4 ein, dass genau seine mehrwortigen Prägungen den Kaltlese-Durchgang brauchen |
| **portability** (0 im Quelltext, im Deutschen gebraucht) | **die Portabilität** | 3 | **CORPUS PRECEDENT** | die Portabilität · Plural meiden · der Portabilität | „die Portabilität **gewährleisten / sicherstellen / wahren**"; „**seinen eigenen Preis bei der Portabilität**" (Korpus wörtlich) | — | **CORPUS(2)** (`orchestration-frameworks/index.md`, `real-agents.md`) + BSI (C5 §5.10 „Portabilität und Interoperabilität"; OPS.2.2.A15) |
| **catalogue** (a) *model catalogue*, 11× | **der Modellkatalog — nie nackt bei Erstnennung**; sicherste Erstform **„der Katalog der Modelle, die eine Plattform ausliefert"** | 3 | **BOUND** | der Katalog · die Kataloge · des Katalog[e]s | „**der Katalog umfasst / enthält**"; „**ein Modell in den Katalog aufnehmen**"; „**ein Modell aus dem Katalog nehmen**" (= *retire a model*); *catalogue breadth* → „**Breite des Katalogs**" | ⛔ **nacktes „der Modellkatalog"** — 10 von 10 de.wikipedia-Treffern sind **Fahrzeugprospekte** · ⛔ *die Modellpalette*, *das Modellangebot* (erst recht Automobilwörter) · ⛔ *die Liste*, *das Verzeichnis*, *die Sammlung* (Kanon) · ⛔ **„im Katalog blättern"**, „einen Katalog herausbringen" (DWDS-Wortprofil ist buchhaft) | **CORPUS(41)** für `Katalog` + Kanonzeile §1.1 + AGREED×2 für den Fahrzeugbefund |
| **catalogue** (b) *injection catalogue*, 2× | **der Injection-Katalog** (Kanonform, unverändert) | 3 | **BOUND** | der Injection-Katalog | beide Vorkommen sind Rückverweise auf die Guardrails-Vertiefung — **die dortige Benennung gilt** | ⛔ Neubenennung | Kanon §1.3.3 + AGREED×2 |
| **catalogue** (c) *Werkzeugkatalog* | **`tooling-ecosystem` MUSS das Wort `Werkzeugkatalog` mindestens einmal aufgreifen** | 3 | **BINDING (Querverweis-Pflicht)** | der Werkzeugkatalog | Der ausgelieferte deutsche Text **verlinkt bereits hierher**: „Um **den Werkzeugkatalog** geht es hier ebenfalls nicht, der steht in [Teil III](…/part-3-production/tooling-ecosystem/…)" | ⛔ **`Tool-Katalog` in Teil III** — das ist Teil II's Referent (die Tools, die ein Agent registriert hat); der Zeichenkettenbefund ist beidseitig 0 | **CORPUS(1)** — ein **lebender** Zeiger; ohne Aufgriff zeigt er auf eine leere Zelle |
| **self-host / self-hosted / self-hosting** | Substantiv **der Eigenbetrieb** (**gebunden**, Objekt im Genitiv/mit *von*) · Verb **selbst betreiben** · attributiv **selbst betrieben** / **im Eigenbetrieb** | 3 | **CORPUS PRECEDENT** | der Eigenbetrieb · Plural meiden · des Eigenbetrieb[e]s | **Korpus wörtlich:** „**API oder Eigenbetrieb**" (2×), „die Wahl zwischen **Eigenbetrieb und fremder API**". Gebunden: „**der Eigenbetrieb großer Sprachmodelle**", „**der Eigenbetrieb von Langfuse**". Verbal: „**das Modell auf eigenen GPUs betreiben**" | ⛔ *selbstgehostet* (Denglisch-Partizip) · ⛔ *die Selbstbeherbergung*, *das Selbsthosten* · ⛔ *das Self-Hosting* **mit deutschem Artikel** (kein Artikelbeleg auf irgendeiner Stufe) · ⚠ **⛔ *der lokale Betrieb* dort, wo der Korpus *local/dev* meint** (Ollama) — dort „**auf dem eigenen Rechner**" | **CORPUS(3)** — **RECONCILED (run1 vs run2, ich wähle run 2)**, s. §3.1 |
| **self-hosting** (Überschrift/Substantiv) | **Überschrift umbauen, nicht übersetzen**: „**Langfuse selbst betreiben: kein einzelner Container**"; Sidebar „**Selbst betreiben und verdrahten**" | 3 | **BOUND** | — | „**Selbst zu betreiben ist ein Preis, den Sie für Kontrolle und Ort zahlen.**" | ⛔ *das Self-Hosting* mit Artikel · ⛔ *die Eigenbeherbergung* | AGREED×2 (Präzedenz `packing`, `Gate`, `Load Shedding`: die Verbalkonstruktion **ist** das Ruling) |
| **open weights** → **open-weight** (3×, attributiv) | Erstnennung **„ein Modell mit offenen Gewichten"**; kompakt danach **das Open-Weight-Modell** | 2/3 | **OPEN (incumbent held: die Umschreibung)** — schließt mit einem heise-/iX-/Fraunhofer-Satz, der `Open-Weight-Modell` als stehenden Terminus führt | das Open-Weight-Modell · die Open-Weight-Modelle | „**oft ein älteres Modell oder eines mit offenen Gewichten**" | ⛔ **`Open-Weight` freistehend** — 8 von 8 de.wikipedia-Treffern sind die **Kampfsport-Gewichtsklasse** · ⛔ *quelloffenes Modell* (sachlich falsch: offene Gewichte ≠ offener Quelltext) · ⛔ *das Open-Weights-Modell* (Plural-s im Erstglied) | RECONCILED (die Umschreibung von run 2 ruht auf der gesetzten Kanonwahl „**das Wissen in den Gewichten des Modells**"; die Kompaktform von run 1 bleibt als Anapher). ⚠ **Zählung: run 1 = 3, run 2 = 2; meine Messung = 3.** Run 1 hat recht |
| **open source** | **Open Source**, artikellos, zwei Wörter, groß · im Kompositum **Open-Source-Bibliothek / -Werkzeug / -Lizenz** | 2 | **BOUND** | artikellos | „**Open Source heißt volle Kontrolle und Ihr Betriebsaufwand.**"; „**eine Open-Source-Bibliothek mit RAG-Metriken**" | ⛔ **`quelloffen` in jedem Satz, der die OSI-/*source-available*-Unterscheidung zieht** — auf **beiden** Seiten (s. §2.3) · ⛔ *frei* (Free Software ist ein dritter Begriff) · ⛔ *offener Quellcode* als Terminus | **AGREED×2 auf die Einsicht, RECONCILED auf die Regel** (run 1 verbietet es für *source-available*, run 2 für *open source* im Kontrastsatz — beide Hälften gelten) + **CORPUS(3)** `quelloffen` (alle außerhalb des Kontrasts) : `Open Source` **0** |
| **enterprise** (a) Handelnder | **das Unternehmen**, meist **Ihr Unternehmen** | 3 | **BOUND** | das Unternehmen · die Unternehmen · des Unternehmens | „**Davon hängt ab, ob Ihr Unternehmen zustimmen darf.**" | ⛔ *die Unternehmung* (veraltet) · ⛔ *der Konzern* (setzt Größe voraus) · ⛔ *die Firma* (unter der Drucklatte) | **CORPUS(22 : 0)** |
| **enterprise** (b) attributiv | **eindeutschen**: *enterprise agreement* → **der Rahmenvertrag** · *enterprise plans* → **die Unternehmenstarife** · *enterprise features* → **die Funktionen für Unternehmenskunden** · *enterprise AI offerings* → **die KI-Angebote für Unternehmen** | 3 | **BOUND** | — | — | ⛔ **die Enterprise-Angebote / Enterprise-Tarife** — das ist **Enterprise-Marketing-Deutsch**, das `_language.md` §1.1 (Drucklatte) und §-Kasten **namentlich ausschließen** · ⛔ *das Enterprise* mit Artikel | **RECONCILED (run1 vs run2, ich wähle run 2) — und eine Kanonregel entscheidet es**, nicht mein Geschmack: run 1 will `Enterprise-` durchkoppeln, germanisiert aber im eigenen Beispiel („*enterprise agreement* → **der Rahmenvertrag**"). ⚠ **`Enterprise-Reifegrad` (`ai-sdlc.md`) ist ein ANDERER Referent** (der dritte Reifegrad) und wird **nicht geforkt** — run 1's Flag bleibt gültig |
| **enterprise** (c) Eigenname | *Gemini **Enterprise** Agent Platform* — unangetastet | **1** | **BOUND** | — | — | — | AGREED×2 |
| **account** → **accounting** (5×; bloßes `account` = 0) | **die Kostenerfassung**; besser **verbal**: „**Token und Latenz pro Anfrage erfassen**" · *accountability* (1×) → **die Rechenschaftspflicht** | 3 | **BOUND** | die Kostenerfassung · der Kostenerfassung | „**Haken für die Kostenerfassung: Eingabe- und Ausgabe-Token protokollieren.**"; Korpus wörtlich: „**dafür müssen Sie die Kosten zuordnen**" | ⛔ **die Abrechnung als Laufterm** — DWDS-Wortprofil „Tag der Abrechnung", „Abrechnung mit …" (Vergeltung); in einem Kapitel über Ausfälle ein Registerausschlag. **Nur gebunden zulässig: „die Token-Abrechnung"** · ⛔ *das Accounting* (= Buchhaltung) · ⛔ *die Buchführung* | **RECONCILED (run1 vs run2, ich wähle run 2)** — run 1's Kopfwahl *die Abrechnung* ist run 2's ⛔, und der Grund ist ein gemessenes Wortprofil, kein Geschmack. ⚠ **`das Konto` ist im Korpus für den UI-Sinn belegt** („Zugang zum **Konto** wiederherstellen") — falls `account` je auftaucht |
| **project** | **das Projekt** | 3 | **BOUND** | das Projekt · die Projekte · des Projekt[e]s | „**je Projekt und Team**" (die Fügung mit *Team* entschärft die Lesart „Arbeitsvorhaben") | ⛔ **`projected` → „projizierte Kosten"** — im Deutschen optisch/geometrisch; der Zähler hat `projected` unter `project` mitgezählt → „**die voraussichtlichen Kosten pro Anfrage**" | AGREED×2 (der Wert der Zeile ist der Sense-Split) |
| **cloud** *(nicht auf der Termliste — 96 Vorkommen, 0 Incumbent; s. §7.3)* | **die Cloud**; Komposita **die Cloud-Region**, **die Cloud-Plattform**, **der Cloud-Anbieter** | 2 | **OPEN (incumbent held: keine; Duden trägt die Zeile, der Korpus nicht)** | die Cloud · die Clouds · der Cloud | „**die KI-Plattform Ihres Cloud-Anbieters**"; „**in der Cloud, die Sie ohnehin nutzen**" | ⛔ *die Wolke* · ⛔ *Cloud-AI-…* (§3: KI) | **CORPUS(0 appellativ)** — die einzige Nennung ist der Eigenname „Google Cloud Next". Run 2 meldet die fehlende §1.1-Zeile; run 1 nicht |

---

## 2. Sense cards

Jede Karte: **die Frage vor dem Schreiben** + **ein fertiger deutscher Satz pro Zweig**.

### 2.1 `residency` gegen `sovereignty` — die Unterscheidung, auf der der ganze Abschnitt steht

**Frage: Geht es um einen ORT oder um MACHT?**

- **Ort** → **die Zusage über den Ort** (Terminusname `Data Residency`, artikellos, einmal glossiert).
  „**Data Residency ist die Zusage darüber, wo die Inferenz stattfindet.**"
- **Macht / Jurisdiktion** → **die digitale Souveränität**.
  „**Die Frage nach dem Ort ist eine Frage der Geografie, die Souveränität eine Frage der Macht.**"
- **Der Abschluss, der im Deutschen fertig bereitliegt:**
  „**Souverän ist nicht, wessen Daten in der EU liegen, sondern wer im Streitfall bestimmen kann, was mit ihnen geschieht.**"
- **Die dritte Stufe, die der Korpus selbst aufmacht** (*AI residency ≠ data residency*):
  „**Und wo die Daten liegen, sagt noch nicht, wo das Modell rechnet**: auch mit GPUs in der Region können Prompts, Telemetrie und Ausgaben die Region verlassen.**"**

⚠ **`die Datenhoheit` gehört ausschließlich in den Souveränitätszweig** — als das Wort für die
Kontrollfrage („wer die Datenhoheit hat"), **nie** im Ortszweig. Sie im Residenzabsatz zu verwenden
kollabiert genau die Unterscheidung, um derentwillen der Abschnitt existiert.
⚠ **Nie beide Wörter am selben Kopfnomen.** *Souveränität* ist im Deutschen politisch-rechtlich stärker
besetzt als das englische *sovereignty* — ein Vorteil, solange die Residenzstelle nicht ebenfalls
„souverän" heißt.

### 2.2 `perimeter` — eine Zone, kein Gerät, keine Linie

**Frage: (a) der umschlossene Bereich, den Daten nicht verlassen dürfen, (b) das Gerät an der Grenze,
oder (c) die Linie, an der das Vertrauen endet?**

- **(a) Zone — alle 10 Korpusvorkommen** → **der Perimeter**.
  „**Was Sie kaufen, ist das Modell hinter dem Perimeter Ihrer Cloud: IAM, Abrechnung, Netz, Audit.**"
  „**Die Standardwahl, wenn die Daten den Perimeter nicht verlassen dürfen.**"
- **(b) Gerät an der Grenze** — kommt nicht vor; wenn doch: **die Perimeterkomponente**, nie „der Perimeter".
- **(c) Vertrauenslinie** → **die Vertrauensgrenze** (Welle 2). **Getrennt halten.**

**Der Satz, der beide braucht und den ein Zusammenlegen zerstört:**
„**Innerhalb des Perimeters liegt trotzdem eine Vertrauensgrenze – abgerufene Inhalte sind auch dort nicht
vertrauenswürdig.**"
**Vier Referenten, vier Namen:** *trust boundary* → die Vertrauensgrenze · *security boundary* → die
Sicherheitsgrenze · *perimeter* → der Perimeter · *network boundary* → die Netzgrenze.
**Der Prüfsatz:** „hinter dem Perimeter" ✓ / „hinter der Vertrauensgrenze" ✗ — der Perimeter ist ein **Ort**,
die Vertrauensgrenze eine **Relation**.
⚠ **Ehrlich vermerkt (run 1, und run 2 unterschlägt es):** der Korpus dehnt *perimeter* über das Netz hinaus
(IAM, Abrechnung, Audit), die BSI verwendet es netzzentriert. Das **englische Original dehnt genauso** — die
Dehnung ist also treu, kein Übersetzungsfehler; aber sie ist der Grund, warum diese Zeile `THIN×2` bleibt.

### 2.3 `open source` gegen `source-available` — der Satz, der kippt

**Frage: Zieht derselbe Absatz eine Abgrenzung gegen *source-available* / ELv2?**

- **Ja (Tooling-Ecosystem, index + deep-dive):** dann heißt *open source* **Open Source** und sonst nichts,
  und `quelloffen` darf auf **keiner** Seite des Kontrasts stehen.
  „**Phoenix erscheint unter ELv2 – der Quelltext ist einsehbar, die Lizenz ist aber keine
  Open-Source-Lizenz im Sinne der OSI.**"
  **Warum:** `quelloffen` sagt wörtlich *die Quelle ist offen* — das ist die **Definition von
  source-available**. Als Wiedergabe von *open source* macht es den unterscheidenden Satz zur Tautologie;
  als Wiedergabe von *source-available* löscht es die Grenze, gegen die der Korpus argumentiert.
- **Nein (Serving, Cloud-Platforms, LLMOps):** dort ist **quelloffen** der ausgelieferte Incumbent (3×) und
  bleibt es. „**vLLM ist der quelloffene Standard für GPU-Serving.**"
- **Kompositum immer durchgekoppelt:** *Open-Source-Bibliothek*, *Open-Source-Werkzeug*, *Open-Source-Lizenz*.

### 2.4 `self-host` — welcher Gegenstand wird selbst betrieben?

**Frage: ein MODELL auf eigenen GPUs, oder ein WERKZEUG im eigenen Perimeter?** Das Verb ist beide Male
dasselbe; das **Objekt** entscheidet den Satz.

- **Modell:** „**Am einen Ende steht der Eigenbetrieb: ein Inferenzserver auf Ihren eigenen GPUs.**"
- **Werkzeug:** „**Langfuse selbst zu betreiben ist der Preis, den Sie für Kontrolle und Ort zahlen.**"
- **Attributiv:** „**ein selbst betriebener Proxy**", „**die im Eigenbetrieb laufende Instanz**".
- **Die Achse, die der Korpus schon benannt hat:** „**API oder Eigenbetrieb**".
- ⚠ **Nicht** *lokaler Betrieb*, wo der Korpus *local/dev* meint (Ollama) → „**auf dem eigenen Rechner**".

### 2.5 `managed` — Erstglied oder Prädikat?

**Frage: Steht `managed` in einem Produktkategorienamen, oder sagt der Satz aus, dass jemand anderes den
Betrieb übernimmt?**

- **Kategoriename, englischer Kopf → gespreizt, unflektiert:**
  „**Das Modell läuft als Managed Service in der Cloud, die Sie ohnehin nutzen.**"
- **Kategoriename, deutscher Kopf → durchgekoppelt, das Deutsche trägt Genus und Flexion:**
  „**Jede Plattform verkauft außerdem eine Managed-RAG-Stufe: die Pipeline aus Teil 1, fertig verdrahtet.**"
- **Aussage → deutsches Prädikat mit dem Anbieter als Agens:**
  „**Wer die Plattform betreiben lässt, gibt Kontrolle ab.**" · *the managed version* → „**die vom Anbieter
  betriebene Fassung**".

### 2.6 `catalogue` — drei Kataloge, drei Namen, und einer ist auf Deutsch ein Autoprospekt

**Frage: ein Katalog **wovon**?**

| Referent | Deutsch | Wo |
|---|---|---|
| die Modelle, die eine Plattform ausliefert | **der Modellkatalog** — nie nackt bei Erstnennung | `cloud-platforms/*`, 11× |
| die gesammelten Injection-Muster | **der Injection-Katalog** (Kanonform) | `tooling-ecosystem/deep-dive.md`, 2× |
| das Werkzeug-Ökosystem, auf das Teil I zeigt | **der Werkzeugkatalog** — **muss einmal aufgegriffen werden** | `tooling-ecosystem/index.md` |

Erstnennung: „**Der Modellkatalog einer Plattform – welche Modelle sie Ihnen über einen Endpunkt ausliefert –
ist die erste Kategorie.**" Danach anaphorisch „**der Katalog**".
Knappe Alternative: „**der Katalog der Modelle, die eine Plattform ausliefert**".
⛔ **`Tool-Katalog` kommt in Teil III nicht vor und darf hier nicht eingeführt werden** (beidseitig 0 gegrept).

### 2.7 `platform` — Appellativ, SaaS-Produkt oder Eigenname?

**Frage: die Sorte Produkt, ein Werkzeugprodukt, oder ein Markenname?**

- **Cloud-KI-Angebot** → **die KI-Plattform / die Cloud-Plattform**.
  „**Zwischen beiden liegt die Möglichkeit, um die es in dieser Lektion geht: die KI-Plattform Ihres Cloud-Anbieters.**"
- **Werkzeugprodukt** (LangSmith, Langfuse, Phoenix) → ebenfalls **die Plattform**, aber gebunden:
  „**die Plattformen für Observability**".
- **Eigenname** → unverändert, unflektiert, Klasse 1: „**… die Gemini Enterprise Agent Platform.**"

⚠ Appellativ und Eigenname stehen im Korpus **in einem Absatz** („two of the three platforms were renamed").
Die Unterscheidung trägt **Artikel und Flexion**, nicht die Großschreibung — das Deutsche schreibt ohnehin
alles groß.

### 2.8 `pro` gegen `je` — die Verteilungspräposition (Korpusbefund, §0.3)

**Frage: zähle ich eine Rate pro EREIGNIS oder einen Anteil je PARTITION?**

- **Ereignis** (Anfrage, Aufruf, Schritt, Antwort) → **pro**.
  „**Eine Obergrenze für den Preis pro Anfrage.**" · „**prüft die voraussichtlichen Kosten pro Anfrage**".
- **Partition / Inhaltseinheit** (Mandant, Region, Projekt, Modell, Sprache) → **je**.
  „**Warteschlangen je Mandant**" · „**Kontingente gelten je Region und je Modell**" · „**je Projekt und Team**".

---

## 3. RUN DISAGREEMENTS — beide Seiten, meine Auflösung, mein Grund

### 3.1 `self-host` / **`der Eigenbetrieb`** — die frontale Umkehrung, und sie trifft die teuerste Zeile des Slices

- **Run 1:** ⛔, ausdrücklich „**die teuerste ⛔ dieses Blattes**". Begründung: `Eigenbetrieb` ist
  kommunalrechtlich vergeben (de.wikipedia-Lemma: Organisationsform eines kommunalen Unternehmens;
  `insource` = **789**, dominiert von Stadtwerken). „Langfuse im Eigenbetrieb" sage auf Deutsch *Langfuse als
  kommunales Unternehmen*. Korpusform: *der Betrieb auf eigener Hardware* / *selbst betreiben*.
- **Run 2:** das **Ruling**. Begründung: der ausgelieferte Korpus führt es (2×), heise trägt es **in unserer
  Domäne** und flexionstragend („**Der Eigenbetrieb** großer Sprachmodelle ist längst kein Hexenwerk mehr").
  Räumt die Dominanzfalle ausdrücklich ein und bindet statt zu verbieten.
- **Meine Auflösung: run 2, und der Korpus entscheidet es, nicht das Argument.** Meine Messung: `Eigenbetrieb`
  = **3** (nicht 2), auf **zwei** Seiten, und eine davon ist **laufende Prosa, ungebunden**:
  „Damit hängt diese Schicht unmittelbar an der Wahl zwischen **Eigenbetrieb und fremder API**"
  (`guardrails/index.md`); dazu zweimal das Merksatz-Label „**API oder Eigenbetrieb**" (`ingestion/index.md`).
  Run 1's ⛔ verlangt also die Reparatur dreier ausgelieferter Sätze auf zwei Seiten — und liefert dafür eine
  Zählung, die das **falsche Register** misst: 789 Treffer in einem Enzyklopädiekorpus voller Kommunalartikel
  sagen nichts über die deutsche IT-Fachpresse, in der heise das Wort im Titelsatz eines LLM-Artikels führt.
  **Was von run 1 bindend bleibt:** die Bindungspflicht (die run 2 ohnehin selbst aufstellt) und die
  ⚠-Kollision *lokaler Betrieb* ↔ *local/dev*, die run 2 nicht hat.
- ⚠ **Unaufgelöste Restspannung, ehrlich vermerkt:** der Korpus liefert die **nackte** Form einmal aus, die
  Regel verlangt Bindung. Auflösung: **je Lektion einmal gebunden einführen, danach anaphorisch nackt** —
  das ist mit dem ausgelieferten Satz vereinbar, ohne ihn zu brechen.

### 3.2 `data residency` — dieselbe Zählung, gegensätzlich gelesen

- **Run 1:** **die Datenresidenz** (Klasse 3, WEAK), gestützt auf einen heise-**Blog**, der das Wort an Ort und
  Stelle definiert; räumt ein: de.wikipedia = **1** Artikel.
- **Run 2:** ⛔ **die Datenresidenz als Kopfterm** — „ein einziger enzyklopädischer Treffer, sonst nur
  disqualifizierte Klassen; das ist die `súbeh`-Lage mit einem Feigenblatt". Setzt stattdessen kept-EN
  **`Data Residency`** + BSI-C3A-Laufform **die Lokalisierung der Daten**.
- **Meine Auflösung: keine von beiden bindend — die Zeile geht an §7.1.** Run 2's Alternative fällt
  unabhängig durch: **`Lokalisierung` = 0 im ausgelieferten Korpus**, und in einem Handbuch, das in vier
  Sprachen erscheint, ist `Lokalisierung` **zuerst l10n** (run 2 warnt selbst davor und schlägt es trotzdem
  vor). Zudem benennt BSI's `Lokalisierung` die **Auswahloption der Kundin** („ob sie eine Lokalisierung in
  Deutschland fordern"), nicht die **Zusage des Anbieters** — ein Referentenwechsel, keine Übersetzung.
  Vorläufig gilt die Konstruktion; die Kopfnomenfrage muss geruled werden.

### 3.3 `egress` — run 1's eigene Schließbedingung ist von run 2 erfüllt worden

- **Run 1:** **OPEN**, kein Substantiv prägen; misst `insource:"Egress-Gebühren"` = **0**; nennt als
  Schließbedingung „ein Satz bei heise/iX/c't/INNOQ/dpunkt mit … einem deutschen Substantiv für die **Gebühr**".
- **Run 2:** **die Egress-Kosten / die Egress-Gebühren** als Kompositumsbildner; legt eine heise-Schlagzeile
  („Gegen Amazon und **Egress-Gebühren**") und Computerwoche („**Egress-Kosten**") vor.
- **Meine Auflösung: run 2.** Es ist kein Widerspruch, sondern ein **Korpusfehler in run 1**: de.wikipedia ist
  das falsche Korpus für einen Cloud-Handelsterm; die Fachpresse ist es. Run 1 hat die richtige Frage gestellt
  und im falschen Regal gesucht. **Status WEAK bleibt** — zwei Quellen, davon eine Computerwoche, für ein
  ganzes Wortfeld. Beide Läufe konvergieren unabhängig auf ⛔ *der Datenabfluss*, und run 1 liefert dafür den
  **Tier-1-Gegenbeleg** (die BSI verwendet das Wort für die Datenpanne) — das ist die stärkste ⛔ des Blattes.

### 3.4 `region` — run 1 schreibt die Fügung, die run 2 als Fehllesung nachweist

- **Run 1:** „*in-region* → **in der Region halten**", „**Daten in der Region festhalten**", „Daten aus
  Residenzgründen **in der Region festhalten**".
- **Run 2:** „**„in der Region" ist im Deutschen die stehende Wendung für *in der näheren Umgebung / im
  Umland*.** „Daten **in der Region** halten" liest zuerst als *im Umland lassen*." → „in derselben Region",
  „in der gewählten Cloud-Region".
- **Meine Auflösung: run 2**, und die Kollision ist im Korpus belegt: `Regionen` ist im ausgelieferten
  Deutsch bereits vergeben — an die **Layout-Regionen eines Dokuments** (3×, `ingestion/deep-dive.md`:
  „Layouterkennung: **Regionen** + Lesereihenfolge"). **Binden statt umbenennen**: in Teil III bei Erstnennung
  **die Cloud-Region**.

### 3.5 `account` — run 1's Kopfwort ist run 2's ⛔

- **Run 1:** **die Abrechnung** (der Vorgang) / *die Verbrauchserfassung*.
- **Run 2:** **die Kostenerfassung**; ⛔ *die Abrechnung* als Laufterm, weil das DWDS-Wortprofil „Tag der
  Abrechnung" / „Abrechnung mit …" (Vergeltung) trägt — Registerausschlag in einem Ausfall-/Postmortem-Kapitel.
- **Meine Auflösung: run 2.** Der Grund ist ein gemessenes Wortprofil, nicht Geschmack; und der Korpus stützt
  die **Verbalform**: „dafür müssen Sie **die Kosten zuordnen**". *die Abrechnung* bleibt **gebunden** zulässig
  („die Token-Abrechnung").

### 3.6 `enterprise` attributiv — und eine Kanonregel, nicht ich, entscheidet es

- **Run 1:** **Enterprise-** durchgekoppelt (*die Enterprise-Angebote*, *die Enterprise-Tarife*), WEAK/HOUSE.
- **Run 2:** eindeutschen (*die Unternehmenstarife*, *die Funktionen für Unternehmenskunden*), HOUSE, gestützt
  auf Korpus `Unternehmen` 22 : `Enterprise` 0.
- **Meine Auflösung: run 2** — und zwar, weil `_language.md` §1.1 die Drucklatte definiert als „dpunkt,
  Rheinwerk, O'Reilly Deutschland, heise/iX. **Nicht Enterprise-Marketing-Deutsch**". „Die Enterprise-Tarife"
  ist genau das. **Run 1 germanisiert im eigenen Beispiel** (*enterprise agreement* → „der Rahmenvertrag",
  ausdrücklich ⛔ „das Enterprise-Agreement") — die Zeile widerspricht sich intern.
  ⚠ **Run 1's Querverweis bleibt gültig und ist wertvoll:** `ai-sdlc.md` führt `Enterprise` kept-EN für den
  **Reifegrad** — anderer Referent, **nicht forken, nicht angleichen**.

### 3.7 `managed RAG` — run 2 erfindet einen Artikel und beruft sich dabei auf eine Zeile, die es nicht gibt

- **Run 1:** ⛔ „das Managed RAG" mit eigenem Artikel; nur gebunden (*die Managed-RAG-Stufe*).
- **Run 2:** **das Managed RAG**, „Genus vom Kopf `das RAG` (kept-EN, `rag.md` §2)".
- **Meine Auflösung: run 1.** Geprüft: im ausgelieferten Deutsch kommt `RAG` **124×** vor und **nie mit
  Artikel** (alles Komposita — `RAG-System`, `RAG-Index`, `RAG-Problem` — oder artikellos „für RAG"); im Kanon
  gibt es **keine** Genuszeile für `RAG`. Run 2 leitet aus einer leeren Zelle ab — genau der #327-Fehlermodus.

### 3.8 `portable` (Adjektiv)

- **Run 1:** „**portabel bleiben**" WEAK zugelassen. **Run 2:** ⛔ — *portabel* ist im Alltag der tragbare
  Gegenstand; „portabel bleiben" behauptet, das System sei tragbar.
- **Meine Auflösung: run 2.** Run 1 stuft die eigene Adjektivzeile selbst als WEAK ein und räumt in seinem
  §6.4 ein, dass genau seine mehrwortigen Prägungen den Kaltlese-Durchgang brauchen. Das Substantiv ist
  unstrittig und **korpusbelegt (2×)**.

### 3.9 Zählungen, bei denen die Läufe auseinandergehen

| Größe | Run 1 | Run 2 | Meine Messung | Folge |
|---|---|---|---|---|
| `open-weight` im Quelltext | **3** | 2 | **3** | run 1 hat recht; die Zeile beschreibt drei Stellen, nicht zwei |
| `Perimeter` im BSI-Zero-Trust-PDF | 28 | 34 | *(nicht nachgeprüft — Webquelle)* | **dieselbe Datei, zwei Zahlen.** Der Kern des `THIN×2`-Befunds: die Verdopplung reproduziert nicht einmal die Messung |
| `Eigenbetrieb` im ausgelieferten Deutsch | — | 2 | **3** | run 2 unterzählt; der dritte Treffer ist der **ungebundene** Prosabeleg und damit der wichtigste |
| `vendor` im Quelltext | nicht geruled | 21 (16 außerhalb Codefences) | **20** | run 1 hat den Terminus gar nicht abgedeckt; run 2's Zusammenlegung auf `der Anbieter` ist eine Regelanwendung („ein Referent, ein Name") und wird übernommen |
| `self-host*` | 20 conc. / 23 roh | **23** (`self-hostable` fehlt in der Konkordanz) | *(Konkordanz zeigt 20)* | run 2's Oberflächeninventar ist gründlicher; die Konkordanz **unterzählt** |

### 3.10 Wo beide Läufe zusammen falsch liegen (nur der Korpus findet es)

- **`pro` / `je`** — s. §0.3. Run 2 zitiert „vgl. je Anfrage" als Korpusform; die Zeichenkette **existiert im
  ausgelieferten Deutsch nicht** (`pro Anfrage` 6 : `je Anfrage` 0). Run 1 schreibt dieselbe Fügung ohne
  Falschzitat. **Eine Verdopplung, die denselben Fehler zweimal meldet, sieht aus wie Bestätigung** — genau
  die Gestalt, vor der der Slice selbst gewarnt hat, nur an einer Stelle, die keiner der beiden Läufe für
  riskant hielt.
- **`Cloud`** — 96 Vorkommen in Teil III, **0 appellative Nennungen** im ausgelieferten Deutsch (die einzige
  ist der Eigenname „Google Cloud Next"), **keine §1.1-Zeile**. Run 2 meldet die Kanonlücke, run 1 gar nichts;
  **keiner** von beiden erkennt, dass damit ein weiteres Wortfeld ohne Incumbent vorliegt (§7.3).

---

## 4. VOCABULARY FOOTPRINT

Flach, dedupliziert — jedes deutsche Inhaltswort aus meinen Beispielsätzen und Sense-Cards:

Abrechnung · Anbieter · Anbieterwechsel · anbieterunabhängig · Angebot · Anfrage · Anbindung · Audit ·
Aufruf · Ausgabe · Bindung · binden · Betrieb · betreiben · betrieben · Cloud · Cloud-Anbieter ·
Cloud-Plattform · Cloud-Region · Container · Datenhoheit · Eigenbetrieb · Eingabe · einsehbar · Endpunkt ·
erfassen · Fassung · Feature · festlegen · GPU · Geografie · Gewichte · halten · Inferenz · Injection-Katalog ·
Instanz · Jurisdiktion · Katalog · Kapazität · KI-Angebot · KI-Plattform · Kontingent · Kontrolle · Kosten ·
Kostenerfassung · Latenz · Lektion · Lizenz · Macht · Mandant · Mehrmandantenbetrieb · mehrmandantenfähig ·
Modell · Modellkatalog · Netz · Ort · Perimeter · Perimeterschutz · Pipeline · Plattform · Portabilität ·
Preis · Projekt · Prompt · Proxy · Quelltext · Rahmenvertrag · Rechenschaftspflicht · Rechner · Region ·
regionsübergreifend · Richtlinie · Route · Schnittstelle · Sicherheit · Sitzungsisolation · souverän ·
Souveränität · Souveränitätsversprechen · Spitzenmodell · Standardwahl · Stufe · Team · Telemetrie · Token ·
Token-Abrechnung · Umgebung · Unternehmen · Unternehmenskunde · Unternehmenstarif · Vergleich · Verkehr ·
verdrahtet · verlassen · Vertrauensgrenze · vertrauenswürdig · voraussichtlich · Warteschlange · Wechsel ·
wechselbar · Wechselkosten · Werkzeug · Werkzeugkatalog · Zusage · zuordnen

⚠ **Kollisionskandidaten, die Stufe 2 prüfen muss** (Wörter, die andere Slices für andere Referenten
brauchen könnten): **Umgebung** (*environment* — im ausgelieferten Deutsch 5×), **Stufe** (*tier*),
**Route** (Observability), **Warteschlange** (*queue*, Slice-übergreifend), **Kontingent** (*quota*, von
keinem Slice geruled), **Instanz**, **Fassung** (*version*), **Schnittstelle** (*interface* / *wire*),
**Kontrolle**, **Ort**.

---

## 5. SPREAD — Vorkommen über die 10 Teil-III-Dateien

| Terminus | n | Dateien | Verteilung |
|---|---|---|---|
| **platform** | 111 | **10 / 10** | cloud-platforms/index 42 · cp/deep 13 · tooling/index 12 · llmops/deep 7 · llmops/index 5 · tooling/deep 5 · overview 4 · serving/index 3 · serving/deep 1 · prod-failures 1 |
| **provider** | 52 | **6** | llmops/deep 13 · serving/index 11 · llmops/index 11 · cp/deep 9 · serving/deep 3 · cp/index 2 |
| **managed** | 47 | **5** | cp/index 22 · cp/deep 11 · tooling/deep 6 · tooling/index 4 · llmops/deep 1 |
| **self-host\*** | 20 (23 mit `self-hostable`) | **5** | tooling/deep 9 · cp/index 4 · cp/deep 3 · serving/index 2 · tooling/index 2 |
| **open source** | 15 | **5** | tooling/index 8 · tooling/deep 3 · serving/index 2 · cp/deep 1 · llmops/index 1 |
| **enterprise** | 15 | **4** | cp/index 9 · cp/deep 2 · tooling/index 2 · overview 1 |
| **perimeter** | 10 | **4** | cp/index 4 · cp/deep 3 · tooling/deep 2 · tooling/index 1 |
| **region** | 24 | **4** | cp/deep 9 · cp/index 8 · llmops/deep 2 · llmops/index 1 |
| **residency** | 30 | **3** | cp/index 12 · cp/deep 12 · tooling/deep 1 |
| **catalogue** | 13 | **3** | cp/index 10 · tooling/deep 2 · cp/deep 1 |
| **egress** | 6 | **3** | cp/deep 3 · llmops/deep 2 · cp/index 1 |
| **lock-in** | 8 | **3** | cp/index 4 · cp/deep 3 · llmops/deep 1 |
| **project** | 4 | **3** | tooling/deep 2 · cp/index 1 · llmops/deep 1 |
| **sovereignty / sovereign** | 12 / 14 | 2 / 2 | fast ganz in cp/deep (8 / 10) |
| **managed RAG** · **managed endpoint** · **data residency** | 12 · 3 · 5 | 2 · 2 · 2 | nur cloud-platforms |
| **account(ing)** | 5 | 2 | serving/index 4 · tooling/index 1 |
| **managed service** · **private endpoint** · **vendor lock-in** · **portable** | 1 · 1 · 2 · 4 | je 1 | — |
| **tenancy** · **landing zone** · **open weights** · **portability** | 0 | 0 | Nullbefunde (aber `tenant` 6, `open-weight` 3) |

**Terme über ≥3 Dateien — hier muss EINE Zeichenkette zentral entschieden werden, sonst driften die
Renderer auseinander:**
`platform` (10) · `provider` (6) · `managed` (5) · `self-host` (5) · `open source` (5) · `enterprise` (4) ·
`perimeter` (4) · `region` (4) · `residency` (3) · `catalogue` (3) · `egress` (3) · `lock-in` (3) ·
`project` (3).
⚠ **`platform` steht in allen zehn Dateien** und ist damit der einzige Terminus dieses Slices, dessen
Fehlwahl jede Seite von Teil III berührt.
⚠ **`residency`** konzentriert sich auf **zwei** Seiten — das macht die §7.1-Entscheidung billig zu
implementieren und teuer zu verschieben: sie betrifft 24 von 30 Vorkommen in einer einzigen Lektion.

---

## 6. CANON DELTA — gemeldet, nicht editiert

| # | Datei / Abschnitt | Heute | Vorschlag | Grund |
|---|---|---|---|---|
| C-1 | `_language.md` §1.1.d + **neue §1.1.g-Zeile** | keine `Anbieter`-Zeile; `Provider` kommt im Kanon **0×** vor | **der Anbieter · die Anbieter · des Anbieters**, Dat. Pl. *den Anbietern*; §1.1.g: **`der Provider` → `der Anbieter`** | **CORPUS(38 : 0)**, 22 artikeltragend, Referent verifiziert. Der Reflex greift zum Loan, und der Loan hat in **beiden** Wörterbüchern ein volles Paradigma im **falschen** Sinn (ISP) — die `Service`-Gestalt |
| C-2 | `_language.md` §1.1.a | keine `Plattform`-Zeile | **die Plattform · die Plattformen · der Plattform**; Erstnennung gebunden (KI-/Cloud-Plattform) | 111 Vorkommen in **allen zehn** Dateien; Duden Bedeutung 4 mit EDV-Marke; ausgeliefert bisher nur 1× |
| C-3 | `_language.md` §1.1.a | **keine `Cloud`-Zeile** | **die Cloud · die Clouds · der Cloud** | 96 Vorkommen in Teil III, **0 appellative Nennungen** im ausgelieferten Deutsch. Ohne Zeile erfindet jeder Renderer den Artikel neu |
| C-4 | `_language.md` §1.1.f | keine `Perimeter`-Zeile | **der Perimeter · die Perimeter · des Perimeters** — **mit `THIN×2`-Marker** und dem Vermerk „Duden hat kein Lemma; nicht zitieren" | Der Marker ist der eigentliche Vorschlag: ohne ihn liest die nächste Welle die Zeile als gleichwertig zu `Souveränität` |
| C-5 | `_language.md` §1.1.f | keine `Souveränität`-Zeile | **die (digitale) Souveränität · kein Plural · der Souveränität**; ⛔ *die Datensouveränität* | BSI-Definition wörtlich + de.wikipedia-Lemma + heise; **das einzige der fünf Nullfelder mit unabhängiger Tier-3/5-Stütze** |
| C-6 | `_language.md` §1.1.d | keine `Mandant`-Zeile | **der Mandant · die Mandanten · des Mandanten** (n-Deklination); *multi-tenant* → **mehrmandantenfähig** | CORPUS(3) inkl. der wiederzuverwendenden Aufzählungskette; BSI C5 *Mandantentrennung* |
| C-7 | `_language.md` §1.1.d | keine `Region`-Zeile | **die Region · die Regionen · der Region**, **Erstnennung `die Cloud-Region`**, ⛔ „in der Region halten" | Zwei Referenten (Cloud-Region ↔ Layout-Region, 3× ausgeliefert) + die Idiomfalle |
| C-8 | `_language.md` §1.1.f | keine `Portabilität`-Zeile | **die Portabilität · der Portabilität**; Adjektiv **OPEN** (⛔ „portabel bleiben") | CORPUS(2) + BSI C5 §5.10 als amtlicher Abschnittstitel |
| C-9 | `_language.md` §1.1.d | keine `Eigenbetrieb`-Zeile | **der Eigenbetrieb · des Eigenbetrieb[e]s**, **„nie nackt bei Erstnennung"**-Klasse; ⚠ DWDS trägt nur den Kommunal-/Wirtschaftssinn | CORPUS(3); die Zeile muss die Dominanzfalle **mitliefern**, sonst wird die Bindung wegredigiert |
| C-10 | `_language.md` §1.1.f | `Vendor-Lock-in` steht in §1.3.3 (Schreibung), **kein Register** | Registerzeile: **Artikel OPEN → artikellos verwenden**; zusätzlich **der Lock-in-Effekt · die Lock-in-Effekte · des Lock-in-Effekt[e]s** | CORPUS(1) artikellos; kein Beleg hängt je einen Artikel an — die `Retry`/`Backoff`-Klasse |
| C-11 | `_language.md` §1.1.d | keine `Egress`-Zeile | **kein freies Substantiv; nur Kompositumsbildner** (die Egress-Kosten / -Gebühren), **WEAK**; ⛔ *der Datenabfluss* mit dem BSI-Grund | Ohne die ⛔ wird aus einem Rechnungsposten eine Datenpanne |
| C-12 | `_language.md` §1.1.d | `Managed Service` ist in der `Service`-Zeile **lizenziert**, hat aber keine eigene Zeile | **der Managed Service · die Managed Services · des Managed Service[s]**; dazu die **`Managed`-Schreibregel** (Erstglied, unflektiert; vor dt. Grundwort durchgekoppelt) | Die Lizenz ohne Register lässt Genus und Schreibung offen |
| C-13 | `_language.md` §1.1 (Querverweis, **keine Verschiebung**) | die `Katalog`-Zeile steht im Register-Block bei `Signal`/`Registry` | **Querverweis aus §1.1.d** | Die Zeile ist vollständig und korrekt — sie ist nur **für eine Cloud-Seite nicht auffindbar**. Dieselbe Gestalt wie `Dashboard` |
| C-14 | `rag.md` §2 / §3 | — | **`Data Residency` als OPEN-Zeile aufnehmen** mit der §7.1-Entscheidung und ihrer Schließbedingung | Sonst prägt der erste Renderer den Kopfterm des am stärksten tragenden Abschnitts |
| C-15 | `rag.md` §2, Streichkasten Welle 3 (**Dissens, nicht Umkehr**) | `~~Managed Endpoint~~` → *der Endpunkt* | **Kein Änderungsantrag.** Vermerkt: Slice C's Gegenstimme (Incumbent mit Pflichtglosse halten) ist bereits protokolliert, und sie ist **korpusseitig widerlegt**: `Endpunkt` 6 : `Endpoint` 0 im ausgelieferten Deutsch. Ich ziehe den Dissens hiermit zurück | Die Streichung ist richtig; ich melde nur, dass sie jetzt auch **Korpusdeckung** hat, die der Kasten nicht zitiert |
| C-16 | `_language.md` §1.3.x (Kollokation) | keine Regel | **`pro` für Raten pro Ereignis · `je` für Anteile je Partition** — mit den Korpuszahlen | Verhindert die Wiederholung von §0.3; und korrigiert ein **Falschzitat**, das sonst als Korpusform weiterläuft |
| C-17 | `rag.md` §8 / Renderer-Injektionsblock | — | **Bindend: `tooling-ecosystem` greift `Werkzeugkatalog` mindestens einmal auf; `Tool-Katalog` kommt in Teil III nicht vor** | Der ausgelieferte deutsche Text **verlinkt bereits** mit diesem Wort hierher. Ohne Aufgriff zeigt ein Verweis auf eine leere Zelle |
| C-18 | `docs/part-3-production/**/_category_.json` (5 Labels) | „Cloud AI platforms", „Part III — Production & LLMOps", „LLMOps — deploy, monitor, cost", „Serving — FastAPI + Docker", „The tooling ecosystem" | Deutsche Fassungen: **„Cloud-KI-Plattformen"** (⛔ „Cloud-AI-…", §3), **„Werkzeug-Ökosystem"**; Gedankenstriche als `–` | Nur das erste Label ist Slice-C-Material; ich melde es, weil es ein **ausgelieferter, sichtbarer String** ist, den die Konkordanz nicht sieht. ⚠ Die U+2014-Frage in den Labels ist im Kanon bereits protokolliert — **kein neuer Befund** |

---

## 7. NEEDS A DECISION, NOT MORE RESEARCH

### 7.1 ⚖ `residency` — der Kopfterm des tragendsten Abschnitts (DIE Entscheidung dieses Slices)

**Die Lage.** Drei Kandidaten, alle drei geprüft, alle drei mit einem benannten Defekt. Weitere
Attestierung hilft nicht: beide Läufe haben dieselbe Zählung erhoben (**1** de.wikipedia-Artikel) und
gegensätzlich gelesen; das ist keine Wissenslücke, sondern eine Wertungsfrage.

| | Vorschlag | Trägt | Bricht |
|---|---|---|---|
| **A** (run 1) | **die Datenresidenz** | ein heise-Beleg, der das Wort *definiert*; morphologisch transparent; hält Residenz ↔ Souveränität lexikalisch getrennt | **1** de.wikipedia-Artikel; heise-**Blog**, nicht iX/c't; eine Prägung auf der am stärksten tragenden Zeile — der `súbeh`/`Latenzbudget`-Fehlermodus |
| **B** (run 2) | kept-EN **`Data Residency`** + Laufform **die Lokalisierung der Daten** | BSI C3A auf Stufe 1 | **`Lokalisierung` = 0 im Korpus**; in einem **viersprachigen** Handbuch liest es zuerst als **l10n**; und BSI's `Lokalisierung` benennt die **Auswahloption der Kundin**, nicht die **Zusage des Anbieters** — ein Referentenwechsel |
| **C** (meine Empfehlung) | **`Data Residency` als kept-EN Terminusname, artikellos, Pflichtglosse bei Erstnennung — und im Fließtext die Konstruktion** („die Zusage darüber, wo die Inferenz stattfindet", „an eine Region binden", „keine Zusage über den Ort") | die Präzedenzklasse des Kanons (`Load Shedding`, `packing`, `Gate`, `staleness`): **keine Attestierung auf zulässiger Stufe → Konstruktion, nicht Prägung**; hält die Souveränitätsunterscheidung intakt, weil nichts Schwaches gegen ein starkes Wort gestellt wird | **wortreicher** — eine Nebensatzkonstruktion statt eines Substantivs, über die 24 `residency`-Vorkommen der Cloud-Platforms-Lektion |

**Meine Empfehlung: C.**
Der zusätzliche Grund, der nicht in der Tabelle steht: *die Souveränität* ist im Deutschen ein **starkes,
130-fach belegtes** Wort. Ein schwaches, frisch geprägtes Substantiv daneben verliert den Wettstreit
**innerhalb des Satzes** — der Leser löst das unbekannte `Datenresidenz` über das bekannte `Souveränität`
auf und kollabiert genau die Unterscheidung, um derentwillen der Abschnitt geschrieben ist. Eine
Konstruktion kann das nicht: sie **sagt**, was gemeint ist.

**Kosten, wenn ich falsch liege.** C's Fehlermodus ist **Wortreichtum** — der deutsche Text bekommt pro
Vorkommen einen Nebensatz mehr. Das ist unschön und **reparierbar**, sobald ein Beleg auftaucht.
A's Fehlermodus ist **semantisch und selbstverstärkend**: eine Prägung wird Kanonkopf, jeder folgende
Renderer wiederholt sie, und sie steht auf der Zeile, deren Verwechslung mit *sovereignty* der Abschnitt
ausdrücklich verhindern will. B's Fehlermodus ist **ein Homonym im eigenen Haus**: ein Handbuch mit einer
Lokalisierungspipeline verwendet „Lokalisierung" für eine Datenortszusage. **Ich empfehle die
zurücknehmbare Verlustart.**

**Schließbedingung für ein Upgrade auf A:** *ein* flektierter Satz bei heise/iX/c't/INNOQ/dpunkt oder in
einem BSI-/DIN-Dokument, in dem **`Datenresidenz` einen Datenbestand im Genitiv regiert**. Dann wird C zu A,
ohne dass ein einziger Satz semantisch umgebaut werden muss — das ist der zweite Grund für C.

### 7.2 ⚖ `Perimeter` — halten oder auf Konstruktion umstellen?

Die Zeile ist `THIN×2`: eine BSI-PDF trägt Genus, Register und Referent; Korpus 0; keine Fachpresse; die
beiden Läufe zählen dieselbe Datei verschieden. **Meine Empfehlung: halten** (`der Perimeter`), weil (i) die
BSI-Belege kasusmarkiert und in unserem Sachgebiet sind, (ii) es **keinen** Ersatz gibt, der nicht mit
*Vertrauensgrenze* / *Sicherheitsgrenze* / *Netzgrenze* kollidiert, und (iii) der Terminus in **vier**
Dateien steht — eine Umstellung auf Konstruktionen berührt vier Seiten. **Kosten, wenn ich falsch liege:**
das Wort trägt ohne technischen Kontext eine **schweizerisch-raumplanerische** Färbung (DWDS-Wortprofil:
*Schutzgebiet, Moorlandschaft, Gestaltungsplan*, §1.3.4); die Kollokationen der Zeile („hinter dem Perimeter
Ihrer Cloud", „den Perimeter verlassen") entschärfen das, ein nacktes „der Perimeter" in einer Überschrift
nicht. **Konkrete Auflage, wenn gehalten wird:** in Überschriften gebunden schreiben
(„**hinter dem Perimeter der Plattform**"), nie freistehend. **Der Gegencheck, der sie schließen würde:**
eine heise/iX/c't-Volltextzählung `Perimeter` mit deutschem Artikel — *nicht* ein zweites Lesen der BSI.

### 7.3 ⚖ `Cloud` — ein Wortfeld ohne Incumbent, das die Termliste nicht kennt

96 Vorkommen in Teil III, **0** appellative im ausgelieferten Deutsch, **keine** §1.1-Zeile. Es steht auf
keiner Slice-Termliste dieser Welle und ist damit ein **Loch zwischen den Slices**. Duden trägt die Zeile
(feminin, EDV-Marke), also ist es keine Forschungsfrage — es ist eine **Zuweisungsfrage**.
**Empfehlung: `die Cloud · die Clouds · der Cloud` zentral setzen, bevor Teil III gerendert wird.**
**Kosten, wenn nicht:** zehn Dateien erfinden den Artikel unabhängig; das ist die Gestalt, die bei
`Laufzeit` fünf ausgelieferte Seiten gekostet hat.
⚠ **Arithmetik-Hinweis, ohne neuen Wert:** dieser Befund berührt **die im Auftrag genannte Zahl der
Wortfelder ohne Incumbent** — Delta **+1** (`Cloud`). Den neuen Wert bildet Stufe 2 aus der Vereinigung.

### 7.4 ⚖ `air-gapped` (8×) — von keinem Slice geruled

Beide Läufe melden es unabhängig als **außerhalb ihrer Termliste**, und beide sagen, der
Souveränitätsabschnitt braucht es („fully air-gapped deployments", „air-gapped GDC"). Es ist keine
Forschungsfrage, sondern eine **Zuweisung**: entweder wird es Slice C nachgereicht oder es fehlt beim
Rendern. **Empfehlung: Slice C zuschlagen** — es steht in denselben Absätzen wie `sovereign` und `Perimeter`.
Ebenso, aus demselben Grund unentschieden und im selben Absatz: `quota` (*Kontingent*?),
`committed-use discount`, `FinOps`, `unit economics`, `multi-cloud gateway`, `trusted cloud`, `Hyperscaler`
(Genus), `CLOUD Act`, `SecNumCloud`, `C5`.

---

## 8. WHAT THIS PASS COULD NOT DO

1. **Ich habe keine der Webquellen nachgeprüft.** Alle BSI-, Duden-, DWDS-, de.wikipedia- und
   heise-Zahlen in §1 stammen aus den Blättern. Wo die Läufe dieselbe Quelle verschieden zählen
   (`Perimeter` 28 vs 34), habe ich das **protokolliert, nicht aufgelöst** — Gate 6.5 attestiert nicht neu.
   Verifiziert habe ich ausschließlich: den **ausgelieferten deutschen Korpus**, den **Quelltext von Teil III**,
   den **Kanon** und die **Konkordanz**.
2. **`Datenresidenz` bleibt ohne zweite Quelle.** Ich habe keine gesucht (Auftragsgrenze) und kann deshalb
   nicht sagen, ob run 1's Blogbeleg allein steht. §7.1 empfiehlt daher die Form, die **ohne** eine zweite
   Quelle auskommt — und die sich nachträglich billig upgraden lässt.
3. **Kein nativer Ohrenprüfer.** Die Fügungen, die dieser Ledger neu bindet — „**die Portabilität wahren**",
   „**den Wechsel offenhalten**", „**die Zusage über den Ort**", „**der Eigenbetrieb großer Sprachmodelle**",
   „**Warteschlangen je Mandant**" — sind gegen Beleg und Korpus geprüft, aber **eine englisch gebaute
   deutsche Kollokation überlebt genau diese Prüfung**. Sie brauchen den Kaltlese-Durchgang.
4. **Der Data Act (VO (EU) 2023/2854) ist in beiden Läufen ungelesen** (EUR-Lex lieferte beiden leere
   Antworten). Er ist die naheliegendste Stufe-1-Quelle für **genau die drei schwächsten Zeilen dieses
   Slices**: `Egress` (Entgelte), `Vendor-Lock-in` (Artikel) und `Portabilität`/`Anbieterwechsel`. Wer ihn
   über einen anderen Amtsblatt-Spiegel beschafft, sollte die drei Zeilen erneut aufmachen.
5. **Ich sehe keinen Defekt, den Korpus und Kanon teilen.** Der `#328`-Grep ist stark, wo eine Kanonregel
   dem ausgelieferten Text widerspricht (so fiel `pro`/`je`), und **blind**, wo beide dasselbe falsch machen.
   Bei `Anbieter` habe ich Referenten gelesen, nicht nur gezählt; bei `Katalog`, `Portabilität` und `Mandant`
   ebenfalls — bei `quelloffen` **nicht vollständig** (3 Treffer gelesen, aber ich habe nicht geprüft, ob
   irgendeine ausgelieferte Seite den OSI-Kontrast implizit zieht).
6. **Cross-Slice-Positionen dieses Slices, Zusammenführung bei Stufe 2:** `Laufzeit`/`runtime` — nicht meine
   Zeile, aber `Managed Runtime` fällt unter meine `Managed`-Schreibregel (Erstglied unflektiert; das
   **Grundwort** entscheidet Slice A). `snapshot` — berührt mich nicht. `lever`/`Hebel`, `queue`
   (**meine Fügung: „Warteschlangen je Mandant"**), `budget` — meine Sätze verwenden `Warteschlange` und
   `Kontingent`; beides gehört anderen Slices, ich beanspruche keine Bindung.
7. **Nicht entschieden, absichtlich:** alles unter §7.4. Ein Durchgang entscheidet nichts, was er nicht als
   Auftrag gelesen hat.
