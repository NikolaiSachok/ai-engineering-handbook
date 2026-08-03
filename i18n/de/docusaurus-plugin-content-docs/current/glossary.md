---
id: glossary
title: Glossar
sidebar_position: 5
---

# Glossar

Einheitliche Definitionen der Begriffe, auf die die Seiten dieses Handbuchs verweisen. Jeder Begriff wird hier
genau einmal bestimmt. Die Liste wächst, während wir die Schichten der Reihe nach durchgehen. Wo hinter den
Formeln und der Geschichte eines Begriffs eine kanonische Quelle steht, folgt der Definition ein Verweis
(↗ Wikipedia für die Klassiker, ↗ arXiv für Verfahren aus einem Paper).

<a id="ingestion-chunking"></a>

## Ingestion – Chunking \{#ingestion-chunking}

**Chunk** – ein Fragment eines Dokuments, die Einheit, in der indexiert wird. Er ist zugleich die Einheit der
Suche und die Einheit dessen, was das Modell zu sehen bekommt.

**Overlap** (*chunk overlap*) – ein gemeinsames Textstück zwischen benachbarten Chunks. Es rettet eine
Tatsache, die genau auf die Schnittkante gefallen ist: Sie überlebt in mindestens einem der beiden Nachbarn
unversehrt, sofern sie kürzer ist als die Überlappung. Üblich sind etwa 10–20 % der Chunk-Größe.

**Rekursiv oder strukturell** (*recursive / structural chunking*) – an natürlichen Grenzen schneiden, und zwar
hierarchisch (Abschnitte → Absätze → Sätze), sodass die Chunk-Grenzen mit den Gedankengrenzen zusammenfallen.
Der Standardfall in der Praxis.

**Semantisch** (*semantic chunking*) – die Chunk-Grenze liegt dort, wo die Ähnlichkeit benachbarter Sätze
scharf abfällt (ein Themenwechsel). Teurer, dafür handelt jeder Chunk am Ende von einer Sache.

**Chunk-Metadaten** (*chunk metadata*) – die Daten, die einem Chunk angehängt werden: Quelle, Titel,
Überschriftenpfad, Datum, Zugriffsrechte. Sie speisen das Filtern, die Quellenangaben und die
Zugriffssteuerung.

**Parent-Document- bzw. Small-to-Big-Retrieval** – über kleine, scharfe Chunks suchen, dem Modell aber das
größere übergeordnete Textstück rund um den Treffer vorlegen. Das Verfahren trennt die zwei Rollen eines
Chunks: Suche und Kontext.

**Parsing der Dokumente** (*document parsing / layout-aware extraction*) – ein rohes Dokument (PDF, Scan,
HTML) in strukturierten Text verwandeln, der die Lesereihenfolge, die Tabellen und die Hierarchie der
Überschriften bewahrt. Ein Parsing, das die Struktur zuerst erkennt, bestimmt die Regionen der Seite und die
Lesereihenfolge, bevor es den Text herauszieht – anders als ein flacher `extract_text`-Abzug.

**OCR** (optische Zeichenerkennung) – maschinenlesbaren Text aus einem Bild oder einer gescannten Seite ohne
Textebene zurückgewinnen. ↗ [Wikipedia](https://en.wikipedia.org/wiki/Optical_character_recognition)

**Late Chunking** – zuerst das ganze lange Dokument durch das Embedding-Modell schicken und erst danach die
Chunk-Grenzen festlegen und die Token-Vektoren je Chunk mitteln, sodass der Vektor jedes Chunks Kontext aus
dem gesamten Dokument trägt. Verlangt ein Embedding-Modell mit großem Kontextfenster.
↗ [arXiv](https://arxiv.org/abs/2409.04701)

<a id="ingestion-embeddings"></a>

## Ingestion – Embeddings \{#ingestion-embeddings}

**Embedding** – ein Vektor, der einen Text in einem Raum darstellt, in dem geometrische Nähe Nähe in der
Bedeutung heißt.

**Der Vektorraum** (*embedding space*) – der Raum, in den ein Modell Texte abbildet; die Suche schrumpft damit
darauf zusammen, die Punkte zu finden, die dem Vektor der Frage am nächsten liegen.

**Bi-Encoder** – kodiert die Frage und den Chunk getrennt in zwei Vektoren und vergleicht sie über ihren
Abstand. Schnell – die Vektoren der Chunks werden einmal berechnet, beim Indexieren. Das Rückgrat der
Vektorsuche.

**Cross-Encoder** – gibt das Paar „Frage + Chunk“ gemeinsam in das Modell und liefert eine einzige
Relevanzzahl zurück. Genauer als ein Bi-Encoder, aber langsamer (der Score lässt sich nicht vorab berechnen).
Im Einsatz beim Reranking.

**Die Dimensionszahl** (*dimensionality*) – die Länge eines Embedding-Vektors (etwa 384 / 768 / 1536). Mehr
Dimensionen sind ausdrucksstärker, kosten aber Speicher, Suchgeschwindigkeit und Geld.

**Die Kosinus-Ähnlichkeit** (*cosine similarity*) – die Nähe, gemessen über den Winkel zwischen zwei Vektoren;
sie berücksichtigt die Richtung und ignoriert die Länge. Die Standardwahl; bei normierten Vektoren fällt sie
mit dem Skalarprodukt zusammen. ↗ [Wikipedia](https://en.wikipedia.org/wiki/Cosine_similarity)

**Für das Retrieval trainiert (retrieval-optimiert)** – Modelle, die auf Paaren aus Frage und Passage
trainiert wurden und nicht auf allgemeiner Satzähnlichkeit. Sie erwarten oft ein Präfix `query:` /
`passage:`. Im Englischen heißen sie *retrieval-optimised* oder *asymmetric embeddings*.

**Mehrsprachige Embeddings** (*multilingual embeddings*) – Embedding-Modelle, die über mehrere Sprachen hinweg
arbeiten; für mehrsprachige Inhalte im Unternehmen entscheidend.

**API oder Eigenbetrieb** (*self-hosted vs. API embeddings*) – die Wahl zwischen einem offenen Modell auf der
eigenen Infrastruktur (die Daten bleiben im Haus) und einer proprietären API (einfacher, dafür verlassen die
Daten das Haus, und pro Aufruf fallen Kosten an).

**Fine-Tuning** (Nachtrainieren des Modells) – ein vortrainiertes Embedding-Modell durch Contrastive Learning
auf Tripeln aus Frage, passender Passage und unpassender Passage an eine Domäne anpassen; getragen wird es von
den Hard Negatives. Es erzwingt, das ganze Korpus neu einzubetten, denn Frage und Dokument müssen von
derselben Modellversion kodiert sein.

**Matryoshka Representation Learning (MRL)** – Embeddings so trainieren, dass die Information von grob nach
fein in ineinandergeschachtelte Präfixe gepackt wird, sodass ein Vektor auf weniger Dimensionen gekürzt werden
kann und brauchbar bleibt – ein Regler zwischen Größe und Genauigkeit, ohne neu einzubetten.
↗ [arXiv](https://arxiv.org/abs/2205.13147)

<a id="retrieval"></a>

## Retrieval \{#retrieval}

**Dense Retrieval** (die dichte Vektorsuche) – die Suche über Embedding-Vektoren; sie erfasst die Bedeutung
und Synonyme und ist blind für exakte Token.

**top-K** – die Anzahl der nächstgelegenen Kandidaten, die die erste Stufe der Suche zurückgibt (üblich sind
50 bis 100, noch vor dem Reranking).

**Die Frage umformulieren** (*query transformation*) – die Frage vor der Suche umbauen: umschreiben,
Multi-Query, HyDE.

**Multi-Query** – mehrere Umformulierungen derselben Frage erzeugen, mit jeder einzeln suchen und die
Ergebnisse zusammenführen.

**HyDE** (*hypothetical document embeddings*) – eine hypothetische Antwort erzeugen, sie einbetten und damit
suchen: Sie liegt oft näher am benötigten Chunk als eine kurze Frage.
↗ [arXiv](https://arxiv.org/abs/2212.10496)

**BM25 / die Stichwortsuche** (*sparse retrieval*) – die klassische Suche über die wörtliche Übereinstimmung
von Wörtern (Termfrequenzen). Sie erfasst exakte Token und ist blind für Synonyme.
↗ [Wikipedia](https://en.wikipedia.org/wiki/Okapi_BM25)

**Die hybride Suche** (*hybrid search*) – Dense Retrieval und Stichwortsuche zusammen laufen lassen und ihre
Scores zusammenführen. So gleicht jedes Verfahren den blinden Fleck des anderen aus.

**Reciprocal Rank Fusion (RRF)** – ein Weg, die Ergebnisse mehrerer Suchen über ihre Ränge in der jeweiligen
Liste zusammenzuführen, ohne die unterschiedlichen Skalen ihrer Scores in Einklang bringen zu müssen.
↗ [SIGIR'09](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf)

**Die score-basierte Zusammenführung / die Score-Normierung** (*score fusion / score normalisation*) –
Retriever über ihre rohen Scores zusammenführen: jeden auf einen gemeinsamen Bereich normieren (Min/Max,
Z-Score) und danach gewichtet summieren. Die Größenordnung der Scores bleibt erhalten, doch das Verfahren ist
anfällig für Ausreißer und für die von Frage zu Frage verschobene Verteilung – die score-basierte Alternative
zur rangbasierten RRF.

**Reranking** – die top-K-Kandidaten mit einem Cross-Encoder neu bewerten und neu sortieren, sodass die besten
nach oben steigen. Die zweite Stufe; sie arbeitet an der Precision.

**LLM-Reranker** – ein Reranking, bei dem ein allgemeines LLM per Prompt über die Relevanz urteilt –
pointwise, pairwise oder listwise. Zero-Shot und über Anweisungen steuerbar, dafür teuer, latenzstark und ohne
deterministisches Ergebnis, verglichen mit einem eigens dafür trainierten Cross-Encoder.

**Das zweistufige Schema** (*two-stage retrieval*) – zuerst günstig und breit für den Recall (Bi-Encoder oder
hybride Suche), danach teuer und genau für die Precision (Cross-Encoder). Das kanonische Schema des
Retrievals.

**Late Interaction / ColBERT** – Frage und Dokument in Vektoren je Token kodieren, die Dokumentseite vorab
berechnen und erst zum Zeitpunkt der Bewertung mit MaxSim punkten: für jedes Token der Frage die größte
Kosinus-Ähnlichkeit zu einem beliebigen Token des Dokuments, summiert über die Token der Frage. Der Abgleich
Token für Token bleibt damit erhalten wie bei einem Cross-Encoder, und dennoch bleibt die Dokumentseite
vorberechenbar und ein ganzes Korpus durchsuchbar; bezahlt wird das mit Speicher – ein Vektor je Token.
↗ [arXiv](https://arxiv.org/abs/2004.12832)

**Die Multi-Vector-Darstellung** (*multi-vector retrieval*) – ein Chunk wird durch viele Vektoren dargestellt,
einen je Token, statt durch einen einzigen; das ist die Darstellung, über der Late Interaction sucht.

**Das Contextual Retrieval** – jedem Chunk vor dem Einbetten und dem Indexieren mit BM25 einen kurzen, vom
Modell erzeugten Vorspann voranstellen, der ihn im Gesamtdokument verortet, sodass der Chunk Kontext trägt,
den ein nackter Chunk weggeworfen hätte; das Prompt-Caching macht das Erzeugen billig.
↗ [Anthropic](https://www.anthropic.com/news/contextual-retrieval)

**Das Routing der Frage** (*query routing*) – die vorab getroffene Entscheidung darüber, wo und wie eine Frage
gesucht wird: welcher Index oder welche Sammlung, ob überhaupt abgerufen wird, Dense Retrieval oder hybride
Suche, welcher Ausschnitt nach Metadaten. Der Anfang des Trichters – bei falscher Route fällt die Antwort
endgültig aus der Kandidatenmenge.

**Nach Metadaten filtern** (*metadata filtering*) – die Suche über die Felder eines Chunks einschränken:
Datum, Abteilung, Dokumenttyp, Sprache.

**Pre-Filter / Post-Filter** – ob ein Prädikat für Metadaten oder Berechtigungen vor der Vektorsuche greift
(nur Vektoren, die es erfüllen, werden überhaupt Kandidaten – richtig, und für die Zugriffssteuerung Pflicht,
doch ein sehr scharfer Filter arbeitet gegen den ANN-Index) oder erst danach (schnell, doch ein sehr scharfer
Filter kann weniger als K Ergebnisse übrig lassen, manchmal gar keines).

**Die Zugriffssteuerung (ACL)** (*access control*) – Chunks nach den Berechtigungen aussortieren, bevor
Ergebnisse herausgehen, sodass niemand etwas erhält, worauf er keinen Anspruch hat. Eine
Sicherheitsanforderung, keine Option.

**Recall@K / Precision@K** – Metriken der Suche: der Anteil der benötigten Dokumente, die in den top-K
gelandet sind (Recall), und der Anteil der relevanten unter den zurückgegebenen (Precision).
↗ [Wikipedia](https://en.wikipedia.org/wiki/Precision_and_recall)

**nDCG** (normalized discounted cumulative gain) – eine Ranking-Metrik, die nicht nur berücksichtigt, ob die
relevanten Dokumente gefunden werden, sondern auch, an welcher Position sie stehen (weiter oben zählt mehr).
↗ [Wikipedia](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)

**MRR** (mean reciprocal rank) – der Kehrwert der Position des ersten relevanten Treffers, gemittelt über die
Fragen. ↗ [Wikipedia](https://en.wikipedia.org/wiki/Mean_reciprocal_rank)

<a id="generation"></a>

## Generation \{#generation}

**Grounding** (Rückbindung der Antwort an den Kontext) – die Antwort an den gelieferten Kontext binden und
nicht an das im Modell gespeicherte Wissen.

**Die Grounding-Anweisung** (*grounding instructions*) – dem Modell ausdrücklich sagen, dass es ausschließlich
aus dem Kontext antworten und offen sagen soll, wenn die Antwort dort nicht steht. Der wichtigste Hebel gegen
Halluzinationen.

**Einen langen Kontext zusammenstellen** (*context packing*) – wie die abgerufenen Chunks im Prompt
zusammengesetzt werden: die Quellen abgrenzen, sie ordnen, die wenigen besten auswählen.

**Lost-in-the-Middle** – ein Modell nutzt Information, die in der Mitte eines langen Kontexts vergraben liegt,
schlechter als das, was am Anfang und am Ende steht. ↗ [arXiv](https://arxiv.org/abs/2307.03172)

**Die Quellenangabe** (*citations / attribution*) – zu jeder Einzelaussage der Antwort angeben, woher sie
stammt; das macht die Antwort nachprüfbar und dämmt das Erfinden ein.

**Die Antwortverweigerung** (*refusal / abstention*) – ein ordentliches „Ich weiß es nicht“, wenn der Kontext
nicht ausreicht; besser als ein selbstsicher vorgetragener Fehler.

**Faithfulness / Groundedness** (Quellentreue) – eine Metrik dafür, wie weit die Antwort tatsächlich auf den
herangezogenen Quellen ruht und nicht auf dem Wissen des Modells; im weiteren Verlauf steht dafür durchgehend
Faithfulness.

**Das im Modell gespeicherte Wissen** (*parametric knowledge*) – alles, was das Modell beim Training
aufgenommen hat und in seinen Gewichten trägt; RAG drängt es bewusst zurück, damit der Kontext den Vorrang
hat. Kurz auch: das Modellwissen.

**Die Halluzination** (*hallucination*) – eine selbstsicher vorgetragene Tatsache, die in den Quellen nicht
steht oder falsch ist.

**Self-Consistency** – statt eines einzigen Durchlaufs der Chain-of-Thought mit Greedy Decoding mehrere
Lösungswege erzeugen und die Endantwort per Mehrheitsentscheid ermitteln; das greift nur dort, wo die Antwort
ein diskreter, abstimmbarer Wert ist. ↗ [arXiv](https://arxiv.org/abs/2203.11171)

**Chain-of-Verification (CoVe)** – eine Schleife der Selbstprüfung: eine Erstantwort entwerfen, Prüffragen
planen, sie *unabhängig* von diesem Entwurf beantworten (damit das Modell den eigenen Fehler nicht
durchwinken kann) und den Entwurf zuletzt gegen die Prüfungen überarbeiten.
↗ [arXiv](https://arxiv.org/abs/2309.11495)

**Der Widerspruch zwischen abgerufenem Kontext und Modellwissen** (*knowledge conflict, context–memory
conflict*) – der abgerufene Kontext widerspricht der Vorannahme des Modells; das Modell hält sich nicht immer
an den Kontext, besonders dann nicht, wenn die Vorannahme fest sitzt oder der Kontext unplausibel wirkt. Ob es
das getan hat, misst Faithfulness.

**Die Gestaltung der Antwort** (*answer-shaping*) – Format, Ton und Länge der Antwort steuern. Ein echter
Qualitätshebel, aber dem Grounding nachgeordnet: Die Gestaltung darf niemals eine Quellenangabe, einen
Vorbehalt oder eine ehrliche Antwortverweigerung fallen lassen.

<a id="structured-knowledge"></a>

## Strukturiertes Wissen \{#structured-knowledge}

**Das kontrollierte Vokabular** (*controlled vocabulary*) – eine feste Liste zugelassener Bezeichnungen. Die
günstigste Struktur, die es gibt, und die, die einen Extraktor daran hindert, für dieselbe Beziehung drei
Namen zu erfinden.

**Die Taxonomie** (*taxonomy*) – eine hierarchische Gliederung der Bezeichnungen eines Vokabulars; sie bringt
Aggregation, Vererbung und Fragen nach Ober- und Unterbegriffen.

**Die Ontologie** (*ontology*) – Klassen, Eigenschaften und die Einschränkungen, denen sie unterliegen: ein Modell der
Domäne statt einer Liste ihrer Etiketten. Sie bringt Validierung und die Ableitung von Fakten, die niemand
hingeschrieben hat, zum Preis dauerhafter menschlicher Pflege.

**RDF** – das Modell der Tripel: Jeder Fakt ist ein Subjekt, ein Prädikat und ein Objekt.

**OWL 2** – die Ontologiesprache des W3C mit formal definierter, modelltheoretischer Bedeutung; sie ist es,
die maschinelles Schlussfolgern möglich macht. Ihre **Profile** (EL, QL, RL) tauschen Ausdrucksstärke gegen
Berechenbarkeit, und eines davon zu wählen ist eine echte Ingenieursentscheidung.

**SHACL** – eine Sprache zur Validierung von RDF: Ein **Shapes-Graph** nennt die Bedingungen, ein
**Datengraph** wird dagegen geprüft, und heraus kommt ein **Validierungsbericht**. Der deterministische
Kontrollpunkt, den ein probabilistischer Extraktor passieren muss.

**SPARQL** – die Abfragesprache für RDF; sie gleicht Muster auf einem gerichteten, beschrifteten Graphen ab,
auch über relationale Daten, die eine Zwischenschicht als RDF zeigt.

**Der Knowledge Graph** (Wissensgraph) – Entitäten als Knoten und Beziehungen als Kanten, aus einem Korpus
herausgezogen oder von Hand gepflegt.

**GraphRAG** – das Retrieval über einen Knowledge Graph, der aus Ihren Dokumenten gebaut wurde; als Eigenname
Microsofts Referenzimplementierung.

**Die Extraktion des Graphen** (*graph extraction*) – der Durchlauf des Sprachmodells, der aus Chunks Entitäten,
Beziehungen und Covariates macht. Die teure Phase, und die, die darüber entscheidet, ob weiter hinten
überhaupt etwas stimmt.

**TextUnit** – GraphRAGs Name für einen Quell-Chunk, die Einheit, über die die Extraktion läuft. Seine Größe
ist eine Entwurfsentscheidung und keine bloße Voreinstellung: Größere Einheiten bedeuten weniger Aufrufe und
mehr Entitäten je Aufruf – und eine geringere Wahrscheinlichkeit, dass das Modell dem richtigen Paar auch die richtige Beziehung
zuschreibt.

**Covariates / die Extraktion der Aussagen** (*covariate / claim extraction*) – Aussagen über Tatsachen, jede
mit einem bewerteten Status und einer Zeitangabe; in GraphRAG optional und standardmäßig aus, weil sie erst
mit an die eigene Domäne angepassten Prompts nützlich wird.

**Die Bildung von Communitys / der hierarchische Leiden-Algorithmus** (*community detection / hierarchical
Leiden*) – die rekursive Gruppenbildung, die Entitäten zu ineinandergeschachtelten Communitys zusammenfasst,
sodass Zusammenfassungen auf mehreren Ebenen entstehen.

**Der Community-Report** – die beim Aufbau erzeugte Zusammenfassung einer Community, mit einer knappen
Übersicht und ihren wichtigsten Entitäten, Beziehungen und Aussagen. Das ist es, was für eine Frage an das
ganze Korpus tatsächlich gelesen wird.

**Local Search** – eine Abfragemethode des Graphen: die Nachbarschaft einer Entität, kombiniert mit den
Roh-Chunks. Der Graph liefert die Struktur, die Belege liefert nach wie vor die Prosa.

**Global Search** – Map-Reduce über jeden Community-Report, für Fragen an das Korpus als Ganzes. Je Abfrage
teuer – und zugleich die Methode, die den Aufbau eines Graphen überhaupt rechtfertigt.

**DRIFT Search** – Kontext aus den Communitys, in eine lokale Abfrage eingefaltet, damit sie breiter ansetzt.

**Die Duplikaterkennung** (*entity resolution*) – die Entscheidung, dass `Acme Corp` und `Acme Corporation`
ein Knoten sind. Der Schritt, der am ehesten enttäuscht, weil die verbreiteten Systeme für Graph-RAG über den
Vergleich der Zeichenketten zusammenführen.

**Zu viel und zu wenig zusammenführen** (*over-merging / under-merging*) – die beiden Richtungen desselben
Fehlers: Verschiedene Entitäten zu verschmelzen erfindet Verbindungen, eine Entität zu zerfasern verdeckt
sie. Geben Sie beides getrennt an; eine einzelne Zahl für die Genauigkeit lässt das eine im anderen
verschwinden.

**Precision auf den extrahierten Tripeln** (*extraction precision*) – der Anteil der extrahierten Tripel, die
gegen ihren Quelltext wahr sind, gemessen an einer gelabelten Stichprobe. Das Maß für Richtigkeit, das die
Metriken des Retrievals nicht liefern können.

**Die semantische Schicht** (*semantic layer*) – zwei verschiedene Dinge unter einem Namen. Das eine ist die
**Kennzahlenschicht** (*metrics layer*): eine Modellierungsebene über einem Warehouse, in der eine Kennzahl
einmal definiert wird, mit ihren Verknüpfungen, ihren zulässigen Filtern und ihren Dimensionen. Das andere ist
die semantische Schicht über der sprachlichen Schicht – eine Äußerung wird einem Begriff der Domäne
zugeordnet statt einer Passage, damit Antworten widerspruchsfrei und nachprüfbar werden.

**Das semantische Modell** (*semantic model*) – die Modellierungseinheit einer Kennzahlenschicht; sie erklärt
die Bestandteile darunter und die Kennzahlen, die darauf aufbauen.

**Measure / Dimension / Entität** – die Bestandteile eines semantischen Modells: die Größen, die Arten, sie zu
schneiden, und die Schlüssel, über die verknüpft wird.

**Die Meta API** – der Endpunkt einer semantischen Schicht, über den ein Agent herausfindet, was abfragbar
ist. Die strukturierte Entsprechung eines Tool-Schemas: Sie beseitigt das Fehlerbild, bei dem ein Modell eine
Kennzahl erfindet, die vernünftig klingt und gar nicht existiert.

**Text-to-SQL** – aus einer Frage in natürlicher Sprache SQL erzeugen. Gegen ein rohes Schema muss das Modell
die Abfrage *herleiten* – fachliche Verknüpfungen, fachliche Datumsspalten, unsaubere Werte, ungeschriebene
Regeln; gegen eine semantische Schicht *wählt* es eine definierte Kennzahl aus, eine kleinere Entscheidung,
deren Fehler sichtbar ist.

<a id="evaluation"></a>

## Evaluierung \{#evaluation}

**Die Evaluierung** (*evaluation*) – die Qualität der Pipeline mit Metriken messen statt nach Gefühl. Erst das
macht die Pipeline einstellbar.

**Das Fehlerbild des Retrievals / das Fehlerbild der Generation** (*retrieval failure / generation failure*) –
das diagnostische Rückgrat von RAG: Eine schlechte Antwort kommt in zwei Ausführungen – als *Fehlerbild des
Retrievals* (der benötigte Chunk hat es nie in die Ergebnisse geschafft) und als *Fehlerbild der Generation*
(der Chunk stand im Kontext, doch das Modell hat ihn übergangen oder verstümmelt). Der erste Schritt bei der
Fehlersuche ist die Entscheidung, welches von beiden vorliegt.

**Der Goldstandard** (*golden set*, *golden dataset*, *ground truth*) – Beispiele der Form „Frage + passende
Chunks bzw. richtige Antwort“, an denen die Metriken gerechnet werden. Sauber schlägt groß. Die geprüften
Labels, aus denen er besteht, heißen Ground Truth.

**Answer-Relevance** (wie gut die Antwort die gestellte Frage trifft) – eine referenzfreie Metrik der
Generation: Bedient die Antwort die gestellte Frage? Gerechnet wird sie, indem ein LLM aus der Antwort N
Fragen zurückgewinnt und die Kosinus-Ähnlichkeit ihrer Embeddings zur ursprünglichen Frage gemittelt wird –
*(1/N) Σ cos(E_gen_i, E_orig)*. Sie misst, ob Frage und Antwort dieselbe Absicht treffen, nicht die
Korrektheit. ↗ [arXiv](https://arxiv.org/abs/2309.15217)

**Die Korrektheit** (*correctness*) – ob die Antwort einer Referenzantwort inhaltlich entspricht.

**LLM-as-a-judge** (ein Modell bewertet die Ausgabe eines anderen) – frei formulierten Text von einem zweiten
LLM anhand eines Bewertungsrasters oder einer Referenz bewerten lassen; das trägt menschenähnliches
Urteilsvermögen in Tausende von Beispielen.

**Die Bias-Formen eines Judges** (*judge bias*) – die systematischen, nicht zufälligen Schieflagen eines
LLM-Judges, die sich deshalb über mehr Beispiele nicht herausmitteln: der Positionsbias (er bevorzugt die
zuerst gezeigte Antwort – dagegen hilft, die Reihenfolge zu tauschen und Konsistenz zu verlangen), der
Ausführlichkeitsbias (länger liest sich als besser) und Self-Preference, im Paper *self-enhancement bias*
(Ausgaben im eigenen Stil). ↗ [arXiv](https://arxiv.org/abs/2306.05685)

**Korrelierte Fehler** (*correlated error*) – zwei Modelle versagen bei denselben Eingaben aus demselben
Grund. Ein zweites Modell senkt den Fehler nur insoweit, wie seine Fehler mit denen des ersten nicht
korrelieren – und von zwei Spitzenmodellen, deren Trainingskorpora einander überlappen, ist zu
erwarten, dass sie sich genau dort am stärksten einig sind, wo ihre gemeinsamen Trainingsdaten am dünnsten
sind. Unabhängigkeit kommt aus einer anderen *Informationsquelle* – einer Prüfung gegen Belege, einer
deterministischen Zusicherung, einem ausführbaren Test, einem menschlichen Label –, nicht von einem anderen
Anbieter.

**Kontextunabhängigkeit und Unabhängigkeit der Fehlerverteilung** (*context independence vs
error-distribution independence*) – zwei Eigenschaften, die dieses Handbuch in der Evaluierung
*Unabhängigkeit* nennt. Die erste hält den Entwurf von einer prüfenden Instanz innerhalb eines Modells fern
(Chain-of-Verification). Die zweite ist die Eigenschaft über Modelle hinweg, die korrelierte Fehler
wegnehmen. Wer die erste hat, hat damit noch nicht die zweite.

**Offline und online** (*offline vs online eval*) – am Goldstandard vor der Bereitstellung messen
(Regressionen in der CI) gegenüber dem Messen im Produktivbetrieb (Nutzerfeedback, A/B-Tests).

**Auf Regressionen prüfen** (*regression eval*) – den Goldstandard in der CI laufen lassen, damit eine
Verbesserung an der einen Stelle nicht an einer anderen etwas zerbricht. Eine **Regression** ist eine durch
eine Änderung verursachte Verschlechterung.

**Der A/B-Test** (*A/B testing*) – zwei Fassungen des Systems am echten Verkehr anhand ihrer Metriken
vergleichen.

**Faithfulness** – eine referenzfreie Metrik der Generation: die Antwort in Einzelaussagen zerlegen, jede
gegen den abgerufenen Kontext prüfen und den Anteil der belegten bewerten – *Faithfulness = belegte
Einzelaussagen / Einzelaussagen insgesamt* (0–1). Sie misst das Grounding, nicht die Korrektheit – eine
Einzelaussage, die in einem falschen Kontext verankert ist, bekommt trotzdem eine glatte 1,0.
↗ [arXiv](https://arxiv.org/abs/2309.15217)

**Context-Precision** – eine Metrik des Retrievals, die die Reihenfolge einbezieht: Stehen die relevanten
Chunks oben in der Trefferliste? Ein nach Rang gewichteter Mittelwert über Precision@k – einen einzigen
irrelevanten Chunk von Rang 2 auf Rang 1 zu schieben kann den Wert von rund 1,0 auf rund 0,5 drücken.
↗ [arXiv](https://arxiv.org/abs/2309.15217)

**Context-Recall** – eine referenzbasierte Metrik des Retrievals: Hat das Retrieval alles zurückgeholt, was
die Referenzantwort braucht? Die Referenzantwort wird in Einzelaussagen zerlegt, und bewertet wird der Anteil,
den der abgerufene Kontext belegt. Das direkteste Maß für das Fehlerbild des Retrievals.
↗ [arXiv](https://arxiv.org/abs/2309.15217)

**Referenzfrei / referenzbasiert** (*reference-free vs reference-based evaluation*) – ob eine Metrik eine von
Menschen geschriebene richtige Antwort braucht. Referenzfreie Metriken (Faithfulness, Answer-Relevance) kommen
mit Frage, Kontext und Antwort aus und lassen sich deshalb an echten Anfragen rechnen; referenzbasierte
(Context-Recall, Korrektheit) brauchen eine Referenzantwort.

**Die Kalibrierung des Judges** (*LLM-judge calibration*) – die Übereinstimmung eines Judges mit menschlichen
Labels an einer zurückgehaltenen Stichprobe messen, bevor seine Zahlen im großen Maßstab gelten; starke Judges
erreichen etwa menschliches Niveau (über 80 %), kein Orakel. Neu kalibriert wird, sobald das Modell, das
Korpus oder die Verteilung der Fragen driftet. ↗ [arXiv](https://arxiv.org/abs/2306.05685)

**Pointwise / Pairwise** (*pointwise vs pairwise evaluation*) – zwei Protokolle für den Judge: Pointwise
bewertet eine einzelne Antwort für sich anhand eines Bewertungsrasters auf einer absoluten Skala (billig,
skaliert, driftet über mehrere Durchläufe); Pairwise wählt die bessere von zwei Antworten (verlässlicher für
ein Ranking, dafür O(n²) und dem Positionsbias am stärksten ausgesetzt). Referenzgestütztes Pointwise legt dem
Judge die Antwort aus dem Goldstandard mit in den Prompt. ↗ [arXiv](https://arxiv.org/abs/2306.05685)

**Die Übereinstimmung zwischen den Annotatoren (IAA)** (*inter-annotator agreement*) – das Ausmaß, in dem
unabhängige Annotatoren dieselben Labels vergeben; eine geringe Übereinstimmung ist das Signal, das
Bewertungsraster zu schärfen, und nicht, die abweichende Stimme zu überstimmen. In der Überschrift auch: die
Interrater-Reliabilität.

**Cohens Kappa** – die um den Zufall bereinigte Übereinstimmung zweier Annotatoren:
*κ = (p_o − p_e) / (1 − p_e)*, mit p_o als beobachteter und p_e als zufällig erwarteter Übereinstimmung.
↗ [Wikipedia](https://en.wikipedia.org/wiki/Cohen%27s_kappa)

**Fleiss' Kappa** – die Verallgemeinerung von Cohens Kappa auf die Übereinstimmung von mehr als zwei
Annotatoren. ↗ [Wikipedia](https://en.wikipedia.org/wiki/Fleiss%27_kappa)

**Das Active Sampling** (im maschinellen Lernen: *Active Learning*) – das knappe Budget für menschliche Labels
dort einsetzen, wo es am meisten einbringt (wo der Judge am unsichersten ist, wo Judges auseinanderlaufen oder
wo der Produktivbetrieb ein Fehlerbild gezeigt hat), statt die Labels gleichmäßig zufällig zu vergeben.

<a id="guardrails"></a>

## Guardrails \{#guardrails}

**Guardrails** (Leitplanken – Schutzregeln um das Modell) – die Schutzschicht auf der Eingabe- und der
Ausgabeseite eines LLM-Systems: gegen Angriffe, abfließende Daten und schädliche Ausgaben.

**Prompt-Injection** – Anweisungen werden in Text eingeschleust, den das Modell liest, und setzen damit den
System-Prompt außer Kraft. Direkt (in der Eingabe selbst) und indirekt (versteckt in abgerufenen Inhalten – für
RAG die gefährliche Form).

**Spotlighting** – nicht vertrauenswürdiger Inhalt wird markiert, damit das Modell ihn als Daten liest und nicht
als Anweisung. Eine Familie aus drei Verfahren auf der Ebene des Prompts, aufsteigend in Trennschärfe und
Preis: **Delimiting** (Grenzmarken um den nicht vertrauenswürdigen Text), **Datamarking** (ein
Markierungszeichen anstelle jedes Leerraums), **Encoding** (base64 / ROT13, sodass sich der Text nicht mehr als
Anweisung liest).
↗ [arXiv](https://arxiv.org/abs/2403.14720)

**Die Rangfolge der Anweisungen** (*instruction hierarchy*) – welcher Quelle das Modell zu folgen hat,
*antrainiert* und nicht bloß im Prompt vereinbart: System und Developer > User > Tool und abgerufener Inhalt.
Eine Anweisung von niedrigem Rang wird befolgt, wenn sie zum höherrangigen Ziel passt, und ignoriert, wenn sie
ihm widerspricht. ↗ [arXiv](https://arxiv.org/abs/2404.13208)

**Personenbezogene Daten (PII) erkennen und maskieren** (*PII redaction*) – auf der Eingabeseite, bevor
protokolliert wird und bevor etwas an eine externe API geht, und ebenso auf der Ausgabeseite; bei externen APIs
entscheidet das über den Datenschutz. Das Ergebnis heißt hier **die Maskierung**; für das Schreiben in den
Trace-Speicher führt die Observability-Schicht dasselbe unter **der Schwärzung**.

**Die reversible und die irreversible Maskierung** – wie gefundene personenbezogene Daten umgeformt werden.
Irreversibel – entfernen, ersetzen, maskieren, einen Hashwert bilden – zerstört das Original; reversibel –
verschlüsseln – lässt sich mit dem Schlüssel zurücknehmen. Reversible Maskierung ist Pseudonymisierung und keine
Anonymisierung, und der Schlüssel wird selbst zur Haftungsfrage.

**Die Eingabe prüfen, die Ausgabe prüfen** (*input / output validation*) – die Eingabe auf Angriffe und
Themenfremdes, die Ausgabe auf abgeflossene Geheimnisse, personenbezogene Daten und Verstöße gegen die eigenen
Richtlinien. Die Prüfung der Argumente eines Tool-Calls ist davon getrennt und heißt **die Validierung**.

**Schädliche Inhalte abwehren** (*content safety / moderation*) – auf der Eingabeseite abweisen, was schädlich
oder unzulässig ist, auf der Ausgabeseite zurückhalten, was verletzend ist oder gegen die eigenen Richtlinien
verstößt. In RAG kommt eine dritte Stelle hinzu, nämlich der Aufbau des Index.

**Jailbreak** – der Jailbreak-Angriff zielt auf das Sicherheitstraining des Modells selbst und lockt es dazu,
unzulässige Inhalte zu erzeugen. Eine Injection dagegen nutzt aus, dass eine Anwendung Anweisungen nicht
zuverlässig von Daten trennt.

**Das Prinzip der geringsten Berechtigungen** (*least privilege*) – die Menge der Tools und Aktionen, die einem
Agenten offenstehen, wird eingeschränkt, und zugelassen wird nur, was ausdrücklich freigegeben ist (*tool
allow-listing*, das Allowlisting). Dann richtet selbst eine gelungene Injection nur noch wenig aus.

**Die Erfolgsrate der Angriffe (ASR)** (*attack success rate*) – über eine festgelegte Menge von
Angriffsversuchen der Anteil derer, bei denen das Modell am Ende tut, was es nicht tun soll; die Messgröße für
die Qualität der Guardrails.

**Defence-in-Depth** – eine gestaffelte Abwehr aus mehreren Schichten: Keine Schicht ist für sich vollständig,
sie wirken zusammen.

<a id="observability"></a>

## Observability \{#observability}

**Observability** (deutsch die Beobachtbarkeit) – zu sehen, was ein laufendes System tatsächlich tut: einer
schlechten Antwort auf den Grund gehen, Kosten und Latenz messen.

**Trace / Span** – der Trace ist die vollständige Aufzeichnung einer einzelnen Anfrage auf ihrem Weg durch die
Pipeline, zerlegt in Spans, also in die einzelnen Schritte: Abfrage → Retrieval samt Scores → Prompt → Ausgabe →
die Schritte des Agenten.

**RAG-Tracing** – das Tracing der RAG-Besonderheiten: welche Chunks abgerufen wurden und mit welchem Score, der
endgültige Prompt, die rohe Ausgabe.

**Die Kosten pro Anfrage** (*cost per request / token accounting*) – Kosten und Token werden je Anfrage
mitgeführt; bei einem LLM kostet jeder Aufruf Geld. Wie gezählt wird, steht weiter unten unter **der Zählung der
Token pro Anfrage**.

**Die Latenz (p50 / p95)** – die Verzögerung nach Perzentilen; am schwersten wiegen die Schritte Generation und
Reranking.

**Die drei Säulen (Traces, Metriken, Logs)** (*three pillars*) – die drei Säulen der Observability; für ein
LLM-System ist der Trace die wichtigste.

**Die Schleife von der Observability zur Evaluierung** (*feedback loop*) – was im Produktivbetrieb danebengeht,
und das Feedback der Nutzenden werden zu neuen Fällen im Goldstandard.

**Head-based Sampling** (kurz *Head-Sampling*) – die Entscheidung über Behalten oder Verwerfen fällt am Anfang
eines Traces, auf dessen erstem Span, nach einem festen Verhältnis, das aus der Trace-ID berechnet wird. Billig
und zustandslos, aber blind dafür, wie die Anfrage ausgegangen ist – Fehlschläge lassen sich damit nicht
bevorzugt behalten.

**Tail-based Sampling** (kurz *Tail-Sampling*) – der Collector puffert jeden Span eines Traces, bis die Anfrage
abgeschlossen ist, und entscheidet erst dann anhand des vollständigen Traces: Latenz, Fehlerstatus, Attribute
der Spans. Damit lassen sich die interessanten Traces behalten, zum Preis eines Zustands im Arbeitsspeicher und
einer Lastverteilung nach Trace-ID. Die Distribution OpenTelemetry Collector Contrib bringt das als Prozessor
`tail_sampling` mit. ↗ [OpenTelemetry](https://opentelemetry.io/docs/concepts/sampling/)

**Priority-Sampling**, auch **hybrides Sampling** – 100 % der Traces behalten, die auf keinen Fall verloren
gehen dürfen (Fehler, Anfragen jenseits der Obergrenze für die Latenz, als schlecht markierte Antworten), und
von den Erfolgen der Routine nur eine niedrige Grundrate. Verbreitet ist es, beide Verfahren
hintereinanderzuschalten: zuerst das Head-, danach das Tail-Sampling.

**Das Erfassen der Nachrichteninhalte** (*message-content capture*) – der Prompt und der Ausgabetext werden im
Trace mitgeschrieben. In den GenAI-Konventionen von OpenTelemetry ist das standardmäßig abgeschaltet und muss
ausdrücklich eingeschaltet werden, wegen des Datenschutzes und der Datenmenge; die Metadaten – Modell, Zahl der
Token, Dauer – laufen dagegen von Haus aus mit.

**Die Aufbewahrungsstufe** (*retention tier*) – eine kurze TTL für die inhaltstragenden Spans, damit der rohe
Text schnell verfällt, und eine längere für die billigen Metadaten; einer der Hebel dafür, wie lange heikle
Daten im Trace-Speicher liegen.

**Die Golden Signals** – die vier Signale der Google-SRE-Schule – Latenz, Traffic, Fehler, Sättigung –, die auf
dem Dashboard eines LLM-Systems neben der Qualität als vollwertiger Achse stehen.
↗ [Google SRE](https://sre.google/sre-book/monitoring-distributed-systems/)

**SLI / SLO** – ein Service-Level-Indicator ist eine gemessene Größe: Verfügbarkeit, die Latenz im 95.
Perzentil, eine Bestehensquote für die Qualität. Ein Service-Level-Objective ist ein Ziel dafür über einen
Zeitraum. Für ein LLM-System sollte mindestens ein SLI ein Qualitäts-SLI sein, berechnet aus der
Online-Evaluierung, und nicht bloß die Verfügbarkeit.
↗ [Google SRE](https://sre.google/sre-book/service-level-objectives/)

**Das Fehlerbudget** (*error budget*) – der Abstand zwischen einem SLO und den vollen 100 %: so viel darf sich
ein Dienst an Fehlern leisten, bevor das Ziel verfehlt ist.

**Alerts auf die Burn Rate des Fehlerbudgets** (*burn-rate alerting*) – gemeldet wird, wie schnell das
Fehlerbudget verbraucht wird: Ein schnelles Abbrennen holt sofort jemanden, ein langsames Abdriften warnt nur.
Die Meldung hängt damit an der Wirkung statt an einem Schwellenwert auf jeder einzelnen Metrik.

**Wer zu viel alarmiert, wird nicht mehr gehört** (*alert fatigue*) – das Fehlerbild: Hängt an jeder Metrik ein
Alert, dann begräbt der Lärm die echte Regression, und ein wirklicher Vorfall bleibt ungelesen.

**Einen Qualitätseinbruch auf seine Ursache zurückführen** (*regression triage*) – erst erkennen, dann zuordnen:
einen statistisch belastbaren Einbruch in einer Reihe zu Qualität, Latenz oder Kosten feststellen und ihn dann
über die Spans des Traces einer Stufe und einem Änderungsereignis zuordnen – einem Deployment, einer
gewechselten Modellversion, einer erneuten Ingestion, einer verschobenen Verteilung der Eingaben.

**Die Kosten zuordnen** (*cost attribution*) – die Spans mit Feature, Mandant, Route und Modell versehen, damit
die Rechnung zeigt, welches davon das Budget verbrennt, statt nur die Gesamtsumme auszuweisen.

**Die Zählung der Token pro Anfrage** (*token accounting*) – Eingabe-Token plus Ausgabe-Token je Anfrage,
jeweils nach Modell bepreist, erfasst über die Attribute und Metriken der GenAI-Konventionen von OpenTelemetry;
die Grundlage eines Kostenbudgets.

**Eine Obergrenze für die Latenz** (*latency budget*) – Ziele für p50 und p95, dazu die Latenz nach Spans
zerlegt – Retrieval, Reranking, Generation; TTFT gegen die gesamte verstrichene Zeit –, damit eine
Überschreitung auf die langsame Stufe zeigt.

**Die weiche und die harte Obergrenze** (**Soft- und Hard-Cap**) – die Vorgabe eines Budgets in zwei Stufen: Die
weiche Obergrenze warnt – ein Alert, ein rotes Dashboard – und lässt die Anfrage durch; die harte greift zur
Laufzeit ein und weist die Anfrage ab, stuft auf ein günstigeres Modell herunter oder kürzt den Kontext.

<a id="agentic-rag"></a>

## Agenten – Agentic RAG \{#agentic-rag}

**Agentic RAG** – RAG, in dem das Retrieval kein fester Schritt der Pipeline mehr ist, sondern eine Aktion, für
die sich das Modell in einer Schleife entscheidet. Im statischen RAG hat der Code die Kontrolle, im Agentic RAG
das Modell.

**Die Schleife des Agenten** (*agent loop*) – der sich wiederholende Zyklus `nachdenken → entscheiden → handeln →
beobachten`, der sich dreht, bis das Modell selbst entscheidet, dass es für eine Antwort genug hat.

**ReAct (Reasoning + Acting)** – das Muster `nachdenken → handeln → beobachten`: Das Modell verschränkt das
Überlegen mit Aktionen, also mit Tool-Calls, und gibt das Ergebnis jeder Aktion zurück in den Kontext.
↗ [arXiv](https://arxiv.org/abs/2210.03629)

**Der Query-Router** (*routing / query router*) – der leichteste Schritt in die Autonomie: Das Modell trifft eine
einzige Entscheidung – wohin die Frage geht, in welchen Index oder an welches Tool, oder „kein Retrieval nötig“
–, und alles danach ist statisch. Nicht zu verwechseln mit dem Routing zwischen Modellen, also der Wahl, welches
Modell antwortet (Teil III).

**Das Retrieval über mehrere Hops** (*multi-hop retrieval*) – eine Antwort, die mehrere voneinander abhängige
Suchen braucht: Die nächste Abfrage entsteht aus dem Ergebnis der vorigen.

**Die Abfragen planen** (*query planning*) – eine schwierige Frage wird vorab in Teilfragen zerlegt, bevor
gesucht wird.

**Die Selbstkorrektur** (*self-correction / self-reflection*) – der Agent sieht sich das Zwischenergebnis an,
merkt, dass es danebenliegt, und formuliert die Abfrage neu oder sucht noch einmal. Sie beurteilt die Qualität
des Retrievals und bleibt damit von **der Reflexion** aus der Lektion über Planung und Schleifen getrennt, die
den ganzen Pfad beurteilt.

**Das iterative Retrieval** – in einer Schleife suchen und die Frage dabei schärfen, statt einen einzigen festen
Aufruf abzusetzen.

**Self-RAG** – dieselbe Selbstkorrektur, in trainierte Tokens verlagert: Das Modell ist darauf trainiert,
während der Generation besondere `Reflection-Tokens` einzustreuen. Sie entscheiden je Abschnitt, ob überhaupt
abgerufen wird, ob eine abgerufene Passage relevant ist und ob die Antwort von ihr getragen wird – und wie
nützlich sie ist. Diese Urteile sind in die Generation eingewoben und kein äußeres Gerüst darüber.
↗ [arXiv](https://arxiv.org/abs/2310.11511)

**Corrective RAG (CRAG)** – ein schlanker **Bewerter der abgerufenen Dokumente** bewertet sie und sortiert
seinen Konfidenzwert in drei Fächer: *korrekt* → verfeinern, also nur die relevanten Fragmente behalten;
*falsch* → verwerfen und auf eine Websuche ausweichen; *mehrdeutig* → beides verbinden. Ohne Umbau auf eine
beliebige bestehende RAG-Pipeline aufsetzbar. ↗ [arXiv](https://arxiv.org/abs/2401.15884)

**Adaptive RAG** – ein trainierter Klassifikator sagt vorher, wie komplex eine Frage ist, und leitet sie an die
billigste Strategie weiter, die noch ausreicht: gar kein Retrieval, also die Antwort aus dem im Modell
gespeicherten Wissen; ein einzelnes Retrieval; oder das volle iterative Retrieval über mehrere Schritte.
↗ [arXiv](https://arxiv.org/abs/2403.14403)

**Das Retrieval-Budget** – eine harte Obergrenze für die Retrieval-Schleife: höchstens so viele Hops, so viele
Suchen, so viele abgerufene Tokens. Sie hält die Schleife an, ganz gleich, was das Modell urteilt – das
Gegenstück zum Schrittbudget und zum Token-Budget, auf das Retrieval angewandt.

**Ausreichender Kontext** (*sufficient context*) – die Abbruchbedingung einer Retrieval-Schleife: Reicht der
Kontext schon, um zu antworten? Zu früh anzuhalten ruft zu wenig ab, und die Antwort ist nicht belegt; nie
anzuhalten ruft zu viel ab und kostet doppelt – an Anfragen und über **Lost-in-the-Middle**. Die Tokens von
Self-RAG dafür, ob eine Aussage getragen wird und wie nützlich sie ist, sind eine Möglichkeit, dieses Urteil
umzusetzen.

<a id="tools"></a>

## Agenten – Tool-Einsatz \{#tools}

**Der Tool-Einsatz**, auch **Function Calling** genannt – der allgemeine Mechanismus, mit dem das Modell eine
externe Funktion aufruft: Das Modell formuliert eine strukturierte Absicht, ausgeführt wird sie vom eigenen
Code. Das Retrieval ist davon ein Sonderfall.

**Die Tool-Definition** – ein Name, ein Beschreibungstext und ein Parameterschema (JSON Schema), die dem Modell
mitgegeben werden: das, was ihm zur Verfügung steht. Der Beschreibungstext wirkt wie ein Prompt – das Modell
wählt sein Tool danach aus.

**Der Tool-Call** – das strukturierte JSON mit dem Namen des Tools und den Argumenten, das das Modell statt
gewöhnlichen Textes oder neben ihm liefert.

**Das Tool-Result** – das Ergebnis der Ausführung eines Tools, das als eigene Nachricht an den Gesprächsverlauf
angehängt und dem Modell zurückgegeben wird.

**Die Tool-Auswahl** – die Entscheidung des Modells, welches Tool es aufruft; eine häufige Fehlerquelle, sobald
der Tool-Katalog groß wird oder sich Tools inhaltlich überschneiden.

**JSON Schema** – eine Sprache, um Struktur und Typen von Daten zu beschreiben; sie legt die zulässigen
Parameter eines Tools fest und engt ein, was das Modell überhaupt erzeugen darf.

**Die strukturierte Ausgabe** (*structured output*) – eine Ausgabe des Modells in einer vorgegebenen,
maschinenlesbaren Form – JSON nach einem Schema – statt in freiem Text; die Grundlage für verlässliche
Tool-Calls. Nicht zu verwechseln mit **Structured Outputs**, dem Namen des Features im nächsten Eintrag.

**Parallele Tool-Calls** – mehrere voneinander unabhängige Tool-Calls, die das Modell in einer einzigen Antwort
absetzt; die Anwendung verteilt sie, führt sie nebenläufig aus und führt die Ergebnisse anschließend in einer
Nachricht wieder zusammen. Zulässig ist das nur, wenn kein Aufruf das Ergebnis eines anderen braucht und keiner
dem anderen ins Gehege kommt; gesteuert wird es je Anbieter (`disable_parallel_tool_use`,
`parallel_tool_calls`).

**Constrained Decoding** – das Schema wird während der Generation erzwungen: Es wird in eine Grammatik
überführt, und in jedem Decoding-Schritt werden alle Token maskiert, die die Grammatik verletzen würden. Die
Ausgabe entspricht dem Schema damit schon vom Verfahren her und nicht erst nach einer Prüfung im Nachhinein.

**Der Strict Mode / Structured Outputs** – der ausgelieferte Schalter (`strict: true`), der das
Constrained-Decoding-Verfahren für die Argumente eines Tools einschaltet; er garantiert wohlgeformte,
schemakonforme Argumente – nicht fachlich richtige. Voraussetzung sind `additionalProperties: false` und jede
Eigenschaft unter `required`.

**Die Idempotenz / der Idempotency-Key** – ein Schreibzugriff ist idempotent, wenn er zweimal mit derselben
Eingabe dieselbe Wirkung hat wie einmal ausgeführt. Der Idempotency-Key ist ein eindeutiger Schlüssel an der
Operation, an dem der Server eine Wiederholung erkennt und sie nicht erneut ausführt – damit ist die
Wiederholung nach einer unklaren Zeitüberschreitung gefahrlos.
↗ [Wikipedia](https://en.wikipedia.org/wiki/Idempotence)

**Die dynamische Tool-Auswahl**, auch **Tool-RAG** genannt – nur die Tools abrufen und mitschicken, die zur
aktuellen Frage passen, statt bei jeder Anfrage den ganzen Tool-Katalog zu serialisieren; RAG, angewandt auf den
Katalog statt auf Dokumente. Das senkt die Kosten an Token und die Fehler bei der Tool-Auswahl, sobald der
Katalog groß ist.

**Die Validierung der Argumente** – die Argumente eines Tool-Calls werden geprüft, bevor er ausgeführt wird, und
zwar auf zwei Ebenen: **technisch** gegen das Schema (Typen, Enums, Formate) und **fachlich** auf Werte, die im
gegebenen Zusammenhang falsch sind – eine Kennung, die es nicht gibt, ein Betrag über dem Limit.

**Das Retry-Budget** – eine harte Obergrenze für Wiederholungen, pro Aufruf und pro Durchlauf. Ohne sie wird ein
Aufruf, der deterministisch fehlschlägt, zu einer Endlosschleife aus Wiederholungen. Es entspricht dem
Schrittbudget und dem Token-Budget.

<a id="planning-loops"></a>

## Agenten – Planung und Schleifen \{#planning-loops}

**Die Planung** – wie der Agent die Schritte auf ein Ziel hin in eine Reihenfolge bringt; der Plan kann vorab
feststehen oder in der Schleife von selbst entstehen.

**Die Aufgabenzerlegung** (*task decomposition*) – das Ziel wird in Teilaufgaben zerlegt, die der Agent einzeln
abarbeitet: ausdrücklich, als aufgeschriebener Plan oder Aufgabenliste, oder implizit, indem der Plan in der
Schleife von selbst entsteht.

**Plan-and-Execute** – erst die ganze Schrittfolge planen, dann ausführen und bei einem Fehlschlag umplanen;
strukturierter und billiger als ReAct, dafür starrer.

**Die Umplanung** (*re-planning*) – den Plan überarbeiten, wenn ein Schritt fehlschlägt oder eine Beobachtung
ihm widerspricht; ohne diesen Mechanismus ist Plan-and-Execute eine Falle.

**Die Reflexion** (*reflection / self-critique*) – ein eigener Schritt, in dem der Agent den Pfad beurteilt, den
sein Durchlauf bis hierher genommen hat: Komme ich voran? – und je nach Antwort entscheidet er, anzuhalten,
umzuplanen oder weiterzumachen; der wirksamste Hebel gegen das Abschweifen und gegen unbemerktes Kreisen.
Gemeint ist hier **das Prinzip**, nicht das gleichnamige Framework; dieses steht weiter unten unter
`Reflexion`, in Codeschrift.

**Die Abbruchbedingung** (*termination criterion*) – eine ausgeschriebene Bedingung dafür, was „fertig“ heißt
und die Schleife beendet; üblich ist ein Tool zum Beenden, das das Modell aufruft, um sich für fertig zu
erklären.

**Das Schrittbudget** (*step budget / iteration limit*) – eine harte Obergrenze für Schritte, Aufrufe, Tokens,
Kosten oder die verstrichene Zeit; die Sicherung, die das Ende der Schleife im Produktivbetrieb garantiert.

**Die Schleifenerkennung** (*loop detection*) – darauf achten, ob der Agent dieselbe Aktion wiederholt –
derselbe Aufruf, dieselben Argumente, dasselbe Ergebnis – und eingreifen, statt ihn im Kreis weiterlaufen zu
lassen.

**Das Arbeitsgedächtnis** (*scratchpad / working memory*) – ein Arbeitsraum, in dem der Agent nur das behält,
was zum laufenden Pfad gehört: Zwischennotizen, der Stand der erledigten Teilaufgaben. So bläht sich der Kontext
nicht auf. Es ist flüchtig und endet mit dem Durchlauf.

**Eine Schleife, die nicht richtig endet** (*non-termination*) – das Fehlerbild dieser Schicht, in drei
Gestalten: Sie hält nie an, sie wiederholt dieselbe erfolglose Aktion, oder sie entfernt sich vom Ziel. Die
Eigenschaft, dass ein Durchlauf überhaupt endet, heißt **die Terminierung**.

**Die Suche im Raum möglicher Pläne** (*plan search*), kurz **die Baumsuche** – statt sich auf einen Plan
festzulegen, einen Raum aus möglichen Plänen und Überlegungspfaden durchsuchen: mehrere nächste Schritte
erzeugen, jeden mit einer Bewertungsfunktion bewerten, die vielversprechenden Zweige mit Vorausschau expandieren
und aus Sackgassen zurücksetzen.

**Tree of Thoughts (ToT)** – überlegtes Durchsuchen der Zwischenschritte des Überlegens, der „Gedanken“: Das
Modell schlägt mögliche Gedanken vor, beurteilt jeden Zustand selbst und erkundet den Baum in der Breite oder in
der Tiefe, samt Vorausschau und Backtracking – anders als der einzelne lineare Pfad eines Chain-of-Thought.
↗ [arXiv](https://arxiv.org/abs/2305.10601)

**Graph of Thoughts (GoT)** – verallgemeinert ToT vom Baum zu einem beliebigen Graphen, sodass Gedanken nicht
nur abzweigen, sondern auch gebündelt und verschmolzen werden können. ↗ [arXiv](https://arxiv.org/abs/2308.09687)

**LATS (Language Agent Tree Search)** – Monte Carlo Tree Search über den Aktionen eines Agenten statt bloß über
seinem Überlegen, mit einer Bewertungsfunktion aus dem Sprachmodell, mit Reflexion und mit Rückmeldung aus der
Umgebung; vereint Überlegen, Handeln und Planen. ↗ [arXiv](https://arxiv.org/abs/2310.04406)

**Self-Refine** – iteratives Überarbeiten mit einem einzigen Modell und ohne Training: Dasselbe Modell erzeugt
eine Ausgabe, beurteilt sie und überarbeitet sie, in einer Schleife.
↗ [arXiv](https://arxiv.org/abs/2303.17651)

**`Reflexion`** – verbales Verstärkungslernen: Nach einem gescheiterten Versuch schreibt der Agent eine Notiz in
natürlicher Sprache darüber, was schiefgelaufen ist, legt sie in einem episodischen Speicher ab und liest sie
beim nächsten Versuch wieder – er lernt über Versuche hinweg, ganz ohne Gewichtsanpassung. **`Reflexion` ist der
Name eines Frameworks, nicht der Name des Prinzips, das es umsetzt** – im Deutschen fallen beide Wörter
zusammen, deshalb steht der Frameworkname in Codeschrift. Das Prinzip steht weiter oben als **die Reflexion**.
↗ [arXiv](https://arxiv.org/abs/2303.11366)

**Das episodische Gedächtnis** (*episodic memory*) – ein Speicher vergangener Erfahrungen des Agenten: was
geschehen ist, wann und wie es ausgegangen ist. Er überdauert den laufenden Kontext und wird abgerufen, wenn er
zu einer neuen Lage passt – anders als das Arbeitsgedächtnis, das im Kontextfenster der laufenden Aufgabe liegt.

**Das semantische Gedächtnis** (*semantic memory*) – dauerhafte Fakten, die der Agent kennt oder gelernt hat,
meist in einer Wissensbasis oder einer Vektordatenbank; langlebig, anders als das flüchtige Arbeitsgedächtnis.

***virtual context management*** (MemGPT) – eine Speicherhierarchie nach dem Vorbild eines Betriebssystems: Das
Modell behandelt das Kontextfenster als „main context“ (schnell und klein, wie RAM) und einen externen Speicher
als „external context“ (groß und langsam, wie eine Festplatte) und lagert Daten über Tool-Calls ein und aus, um
über die Grenze des Fensters hinaus zu arbeiten. ↗ [arXiv](https://arxiv.org/abs/2310.08560)

**Die Bewertung des Pfades** (*trajectory evaluation*) – den ganzen Pfad bewerten, den der Agent genommen hat,
und nicht nur seine letzte Antwort: das Ergebnis (die Erfolgsquote der Aufgabe) gegen den Ablauf (war jeder
Schritt und jeder Tool-Call tragfähig), dazu die Effizienz in Schritten und die Terminierung.

**pass^k** – der Anteil der Aufgaben, die ein Agent in *allen* k unabhängigen Versuchen löst; eine Messgröße für
die Zuverlässigkeit, die die Streuung von Durchlauf zu Durchlauf offenlegt, die ein einzelnes pass@1 verdeckt.
↗ [arXiv](https://arxiv.org/abs/2406.12045)

<a id="multi-agent"></a>

## Agenten – Multi-Agenten-Systeme \{#multi-agent}

**das Multi-Agenten-System (multi-agent system)** – mehrere spezialisierte Agenten, die zusammenarbeiten, statt dass
ein einzelner Agent alles erledigt; die Gründe dafür sind Spezialisierung, Isolation der Kontexte, Modularität und
Parallelität.

**der Orchestrator / der Supervisor** – ein führender Agent, der eine Aufgabe zerlegt, die Teilaufgaben an Worker
zuweist und deren Ergebnisse zusammenfügt; seine „Tools“ sind die Subagenten.

**der Worker / der Subagent** – ein spezialisierter Agent, der eine zugewiesene Teilaufgabe bearbeitet und ein
Ergebnis zurückgibt.

**die Übergabe (handoff)** – die Weitergabe der Kontrolle und des einschlägigen Kontexts von einem Agenten an den
nächsten; die Nachricht einer Übergabe wirkt als Prompt für den empfangenden Agenten.

**die Kette (agent chain)** – eine sequenzielle Topologie, in der jeder Agent die Ausgabe des vorherigen
weiterverarbeitet (Autor → Lektorat → Faktenprüfung).

**der Kritiker-Agent / die Debatte (critic / debate)** – eine Topologie, in der ein Kritiker-Agent oder mehrere
unabhängige Agenten die Lösungen bestreiten oder vergleichen und die Qualität über unabhängige Blickwinkel heben.

**FIPA ACL** – die von der FIPA 2002 standardisierte Agent Communication Language: Eine Nachricht ist ein
*Performativ* (ein Sprechakt – inform, request, propose, cfp …), das die Felder umschließt (sender, receiver, content,
ontology, protocol, conversation-id). Der jahrzehntealte Vorfahr der heutigen Nachrichtenschemata zwischen Agenten.
↗ [Wikipedia](https://en.wikipedia.org/wiki/Foundation_for_Intelligent_Physical_Agents)

**das Contract Net**, ausgeschrieben **das Contract-Net-Protokoll** – die Vergabe einer Aufgabe auf dem
Verhandlungsweg: Ein Manager schreibt die Aufgabe aus, unbeschäftigte Kontraktoren bewerben sich, der Manager vergibt
den Auftrag an die beste Bewerbung, der Kontraktor liefert das Ergebnis zurück (Reid G. Smith, 1980). Dynamische
Rollenverteilung, ausgedrückt als Austausch von Nachrichten.
↗ [Wikipedia](https://en.wikipedia.org/wiki/Contract_Net_Protocol)

**das Blackboard** – eine Architektur der Koordination über gemeinsames Gedächtnis: Unabhängige Spezialisten – die
Wissensquellen – lesen aus einer globalen Datenstruktur und schreiben in sie, während eine Steuerung entscheidet, wer
als Nächstes schreibt; die Agenten stimmen sich über das Blackboard ab, statt sich unmittelbar aneinander zu wenden.
Die Alternative zur Übergabe von Punkt zu Punkt. ↗ [Wikipedia](https://en.wikipedia.org/wiki/Blackboard_system)

**die Multi-Agenten-Debatte (multi-agent debate)** – mehrere Instanzen des Modells schlagen unabhängig voneinander
eine Antwort vor, kritisieren und überarbeiten dann über einige Runden hinweg und nähern sich einem Ergebnis, das
genauer und in sich stimmiger ist als ein einzelner Durchgang; die Protokollform der Topologie aus Kritiker und
Debatte. ↗ [arXiv](https://arxiv.org/abs/2305.14325)

**Trajectory stitching** – die Kennung des Gesprächs oder der Aufgabe durch jede Nachricht zwischen den Agenten
ziehen, sodass sich die lokalen Spans der einzelnen Agenten zu einem Trace aus Eltern und Kindern zusammensetzen, der
sich als Ganzes bewerten lässt; die Voraussetzung dafür, ein Team überhaupt zu evaluieren.

<a id="orchestration-frameworks"></a>

## Agenten – Orchestrierungs-Frameworks \{#orchestration-frameworks}

**das Orchestrierungs-Framework** – eine Bibliothek, die die Agentenschleife, die Verdrahtung der Tool-Calls, den
Zustand, den Kontrollfluss und die Orchestrierung mehrerer Agenten mitbringt, statt dass Sie das alles von Hand bauen:
LangChain, LangGraph, LlamaIndex, Microsoft Agent Framework (der Nachfolger von Semantic Kernel und AutoGen), CrewAI.

**der Agent als Graph, als Zustandsautomat (agent as a graph / state machine)** – den Agenten als Knoten (Modell
aufrufen / Tool aufrufen / entscheiden) und Kanten (Kontrollfluss, die zurückführenden eingeschlossen) modellieren,
sodass die Schleife einsehbar, wieder aufnehmbar und steuerbar wird.

**der Knoten / die Kante (node / edge)** – die Elemente des Graphen: Ein Knoten ist ein Schritt (Modell aufrufen /
Tool aufrufen / entscheiden), eine Kante ist der Kontrollfluss.

**Checkpointing** – den Zustand eines Agenten so sichern, dass ein Durchlauf angehalten, wieder aufgenommen und
eingesehen werden kann.

**`StateGraph`** – ein Agent, modelliert als gemeinsames getyptes Zustandsobjekt samt Knoten und Kanten; LangGraphs
konkrete Form des Gedankens vom Agenten als Graph.

**die bedingte Kante (conditional edge)** – eine Kante des Graphen, die anhand des aktuellen Zustands entscheidet,
welcher Knoten als Nächstes läuft; in ihr steckt die Verzweigung der Schleife (Tool-Call → Knoten `tools`; fertig →
`END`).

**der Checkpointer** – die Komponente, die den Zustand des Graphen nach jedem Knotenübergang (im LangGraph-Vokabular:
*Super-Step*) sichert, getrennt nach Thread, sodass ein Durchlauf wieder aufgenommen oder zurückgespult werden kann
(Zeitreise).

**das Checkpoint-Backend** – der austauschbare Speicher hinter einem Checkpointer (im Arbeitsspeicher / SQLite /
Postgres / Redis); eine Entscheidung zwischen Entwicklung und Produktivbetrieb.

**der Thread (`thread_id`)** – die Kennung, die die Checkpoint-Historie eines Gesprächs von der eines anderen trennt.

**Durable Execution** (dauerhafte Ausführung) – ein Durchlauf, der nach einem Absturz, einem Neustart oder einer
langen Pause beim letzten gesicherten Schritt fortsetzt, getragen vom Checkpointer; die Modi von `durability`
(exit / async / sync) tauschen den Zeitpunkt des Schreibens gegen Geschwindigkeit.

**der Store** (Langzeitspeicher des Frameworks) – das thread-übergreifende, dauerhafte Gedächtnis, mit Namensräumen
als Schlüssel, getrennt vom thread-gebundenen Zustand des Checkpointers, dem kurzfristigen Gedächtnis.

**deklarative gegen imperative Agentendefinition (declarative vs imperative agent definition)** – die Agenten in der
Konfiguration beschreiben (YAML/JSONC, deklarative Workflows), statt den Graphen im Code zu bauen (`add_node` /
`add_edge`).

**der Human-in-the-Loop (HITL)** – ein Haltepunkt, an dem ein Mensch freigibt oder eingreift, bevor die Schleife
weiterläuft; in einem Framework ein vollwertiger Knoten, der den Durchlauf unterbricht.

<a id="mcp"></a>

## Agenten – MCP und Agentenprotokolle \{#mcp}

**MCP (Model Context Protocol)** – ein offener Client-Server-Standard (Ende 2024 bei Anthropic entstanden, seit
Dezember 2025 ein Projekt der Agentic AI Foundation unter dem Dach der Linux Foundation), der Agenten mit Tools und
Daten verbindet; standardisiert werden Tools, Ressourcen und Prompts. Aus M × N eigens gebauten Anbindungen wird
N + M. ↗ [modelcontextprotocol.io](https://modelcontextprotocol.io)

**der MCP-Server** – kapselt ein Tool oder eine Datenquelle und stellt deren Fähigkeiten einheitlich bereit.

**der MCP-Client** – der Agent oder die Anwendung, die sich mit MCP-Servern verbindet und nutzt, was diese anbieten.

**die MCP-Ressourcen** – Daten und Kontext, die ein MCP-Server bereitstellt (ohne Gegenstück in OpenAPI oder auf einer
Kommandozeile).

**die MCP-Prompts** – wiederverwendbare Vorlagen, die ein MCP-Server anbietet.

**das M×N-Integrationsproblem (M×N integration problem)** – M Anwendungen × N Tools ergeben M × N eigens gebaute
Anbindungen; ein Standard macht daraus N + M.

**A2A (Agent2Agent)** – ein offener Standard (bei Google entstanden, im April 2025 angekündigt, seit Mitte 2025 ein
Projekt der Linux Foundation) für die Verständigung von Agent zu Agent: Agenten veröffentlichen eine Agent Card, damit
andere sie finden, und tauschen Arbeit als Tasks aus, die Messages und Artifacts tragen, über JSON-RPC. MCP führt vom
Agenten zu Tools, A2A von Agent zu Agent. ↗ [a2a-protocol.org](https://a2a-protocol.org)

**der MCP-Host**, im Fließtext **der Host** – die LLM-Anwendung (eine Entwicklungsumgebung, eine Chat-App, eine
Agenten-Laufzeitumgebung), die die MCP-Verbindungen aufbaut und einen oder mehrere Clients hält; jeder Client hält
genau eine Verbindung zu genau einem Server. Host, Clients und Server sind drei Rollen, nicht zwei.

**die Aushandlung der Fähigkeiten (capability negotiation)** – der `initialize`-Handshake, in dem Client und Server
ihre Protokollversion austauschen und erklären, welche Funktionen jede Seite unterstützt, bevor irgendeine Arbeit
beginnt.

**Roots** – eine Fähigkeit des Clients: Der Client sagt dem Server, innerhalb welcher Grenzen im Dateisystem und im
URI-Raum er arbeiten darf – ein Geltungsbereich nach dem Prinzip der geringsten Berechtigungen, den der Client
absteckt, statt ihn der Konvention zu überlassen.

**Sampling** – eine Fähigkeit des Clients, über die ein Server das Modell des Clients bitten kann, Text zu erzeugen
(der Server hat kein eigenes Modell); verlangt die ausdrückliche Zustimmung der Nutzenden und schränkt ein, wie viel
der Server vom Prompt zu sehen bekommt.

**Elicitation** – eine Fähigkeit des Clients, über die ein Server mitten in einem Vorgang fehlende Daten oder eine
Bestätigung beim Menschen einholt, und zwar über ein strukturiertes Schema, das der Client als Formular anzeigt.

**Streamable HTTP** – das Transportprotokoll für entfernte MCP-Server (es hat HTTP+SSE in der Fassung 2025-03-26
abgelöst); es verträgt mehrere Clients, erlaubt dem Server, von sich aus zu senden, und zwingt Authentifizierung und
Sichtbarkeit im Netz in den Entwurf. ↗ [modelcontextprotocol.io](https://modelcontextprotocol.io)

**die MCP-Registry** – eine Metaregistry, die die Metadaten der Server hält, nicht deren Code und nicht deren
Binärdateien, damit Clients herausfinden, welche Server es überhaupt gibt; die offizielle ist am 8. September 2025 als
Vorschau gestartet. Gelistet zu sein ist keine Prüfung.
↗ [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io)

**Server discovery** – wie ein Client die Server findet, mit denen er sich verbinden kann: auf der Ebene des
Ökosystems über eine Registry, die sagt, welche Server es überhaupt gibt, und beim Verbindungsaufbau über den
Handshake, der sagt, was ein bestimmter Server anbietet. Einen Server zu finden heißt nicht, ihm zu vertrauen.

**das Tool-Poisoning** – eine indirekte Prompt-Injection, die in der Beschreibung eines Tools steckt und die das Modell
als Anweisung liest; die folgenreichste Schwachstellenklasse auf der Client-Seite von MCP.

**der Rug-Pull** (Austausch eines Tools nach der Freigabe) – ein Server, der Verhalten oder Beschreibung eines Tools
ändert, nachdem Sie es freigegeben haben, sodass das beim Verbindungsaufbau geschenkte Vertrauen nicht mehr
beschreibt, was das Tool tut. Die Gegenmaßnahme ist, die Version jedes Servers festzuschreiben und bei jeder Änderung
neu zu prüfen.

**der Confused Deputy** (getäuschter Stellvertreter – eine privilegierte Komponente wird zum Missbrauch ihrer eigenen
Rechte verleitet) – ein klassisches Risiko im Umgang mit den OAuth-Token entfernter MCP-Server. Die Gegenmaßnahme sind
die geringsten Berechtigungen und eng gefasste Token.

<a id="real-agents"></a>

## Agenten – echte Agenten (Abschluss dieses Teils) \{#real-agents}

**extended thinking** (das ausgewiesene Nachdenken vor der Antwort) – die sichtbaren Blöcke des Nachdenkens, die ein
Modell vor seiner Antwort ausgibt; bei Claude erscheinen sie als `thinking`-Blöcke.

**interleaved thinking** (das Nachdenken zwischen den Tool-Calls) – nachdenken *zwischen* den Tool-Calls und nicht nur
vor dem ersten; bei Claude ist das auf Modellen mit adaptivem Nachdenken automatisch an.

**reasoning effort** – die Tiefe des Nachdenkens über einen abgestuften Regler steuern (OpenAIs `reasoning.effort`:
`none`/`minimal`/`low`/`medium`/`high`/`xhigh`); die Tokens des Nachdenkens selbst bleiben undurchsichtig und werden
als Ausgabe abgerechnet.

**das Thinking Budget** (`thinkingBudget`) – eine Zahl, die begrenzt, wie viel ein Modell je Anfrage nachdenkt; in
Gemini 3 weicht sie den abgestuften Stufen von `thinking_level`.

**Claude-Code-Hooks** – Ereignisse im Lebenszyklus eines Durchlaufs, an denen Sie ein eigenes Programm aufrufen
(`PreToolUse` kann einen Aufruf blockieren, dazu `PostToolUse`, `Stop` und weitere).

**ADK-Callbacks** – eine feste Matrix von Eingriffspunkten im ADK, je ein `before` und ein `after` für Agent, Modell
und Tool; gibt ein Callback ein Objekt zurück, schließt das den Aufruf kurz.

**Permission Modes** – Modi, die entscheiden, was ein Agent ohne Bestätigung tun darf (`default`, `acceptEdits`,
`plan`, `bypassPermissions` …), ausgewertet in einer festen Reihenfolge, in der eine `deny`-Regel selbst unter
`bypassPermissions` blockiert.

<a id="production-failures"></a>

## Produktivbetrieb – warum KI im Betrieb versagt \{#production-failures}

**die Score-Untergrenze / die Untergrenze für die Relevanz (score floor / relevance floor)** – ein Mindestscore, den
ein abgerufener Chunk nehmen muss, bevor er in den Kontext darf, angesetzt hinter dem Reranking: Die zusammengeführten
Scores einer hybriden Suche liegen nicht auf einer vergleichbaren Skala, ein Schwellenwert auf ihnen ist deshalb
willkürlich, während sich der Score eines Cross-Encoders gegen einen gelabelten Datensatz einstellen lässt. Unterhalb
der Untergrenze gibt das Retrieval absichtlich nichts zurück (siehe **Die Antwortverweigerung** weiter oben unter
Generation).

**das Ingestion-Manifest**, im Fließtext **das Manifest** – ein Artefakt, das ein Durchlauf der Ingestion erzeugt und
das ausweist, was aufgenommen wurde, was ausgeschlossen wurde und warum, und was der Durchlauf gar nicht sehen konnte.
Aus einem stillen Verwerfen wird damit eine Entscheidung, die sich prüfen lässt.

**der blinde Fleck (blind spot)**, meist im Plural **die blinden Flecken** – ein Teil des Korpus, den die Pipeline nie
erreicht hat: ein Format, das sie nicht unterstützt, eine Berechtigung, die ihr fehlte, eine Quelle, die niemand
eingerichtet hat. Unsichtbar, solange das Manifest ihn nicht ausweist, und zur Abfragezeit nicht davon zu
unterscheiden, dass es das Dokument gar nicht gibt.

**der eingefrorene Regressionsdatensatz (frozen regression set)** – ein Datensatz für die Evaluierung, der absichtlich
stillsteht, damit eine Änderung des Scores bedeutet, dass sich das System geändert hat. Er beantwortet die Frage
„Läuft noch, was vorher lief?“

**der wechselnde Datensatz aus dem laufenden Verkehr (rotating live-sampled set)** – ein Datensatz für die
Evaluierung, der regelmäßig aus dem echten Verkehr erneuert wird, damit er weiter dem gleicht, wie Leute tatsächlich
fragen. Er beantwortet die Frage „Passt meine Evaluierung noch zur Wirklichkeit?“ Die beiden ergänzen sich: Den
eingefrorenen durch einen wechselnden zu ersetzen, kostet die Erkennung von Regressionen.

**die Vertrautheit mit dem Maßstab (benchmark familiarity)** – der Verfall des Nutzens eines festen Maßstabs, während
ein Team über Monate dagegen optimiert; der Score steigt weiter, die Qualität nicht. Ein Argument für den Wechsel, das
neben dem Argument aus dem Drift steht.

**die Protokollierung für ein Audit (audit-grade logging)** – genug aufbewahren, lange genug und mit genug Integrität,
um Monate später nachweisen zu können, was das System für eine bestimmte Anfrage gefunden und zurückgegeben hat. Eine
andere Anforderung als die Protokollierung für die Fehlersuche, die ausführlich, aber kurzlebig ist, und eine, die
entworfen werden muss, statt sie zu erben.

**die Kosten für eine angenommene Antwort (cost per accepted answer)** – die ehrliche Einheit der Ausgaben für ein
LLM: die Kosten geteilt durch die *angenommenen* Ergebnisse und nicht durch Tokens oder Aufrufe. Näherungsweise
`attempt_cost / p`, wobei `p` die Erfolgsquote beim ersten Versuch ist.

**die Mehrkosten der Wiederholungen (retry tax)** – der Faktor, mit dem eine niedrige Erfolgsquote ein nominell
günstiges Modell belegt. Das günstigere Modell gewinnt nur, wenn
`p_cheap / p_expensive > price_cheap / price_expensive`.

**Drift response ladder** – die Reihenfolge, in der auf nachlassende Qualität in einem System mit Retrieval zu
antworten ist: neu indexieren und neu in Chunks aufteilen, dann die Mischung der Suchverfahren anpassen, dann den
Prompt überarbeiten – und erst dann an die Gewichte des Modells. Die Umkehrung des Reflexes aus MLOps, neu zu
trainieren, denn die Ursache sitzt meist im Korpus oder in den Fragen.

**das Korpus ist ein Release (corpus as a release)** – das indexierte Korpus wie Code behandeln: als versioniertes
Artefakt, das sich diffen und zurückrollen lässt, und nicht als beiläufigen Zustand, der sich unter einem festen
System still ändert.

**ein Retrieval, das die Berechtigungen kennt (permission-aware retrieval)** – das Retrieval nach den Berechtigungen
des Aufrufers filtern, damit der Index kein Dokument zitieren kann, das der Nutzer nie öffnen durfte. Eine Eigenschaft
des Index und des Abfragepfads und kein Filter, der nachträglich davorgeschraubt wird.

**Cross-lingual retrieval gap** – der stille Verlust an Treffern, wenn ein auf Englisch trainiertes Embedding-Modell
und ein ebenso trainierter Reranker in einer anderen Sprache abgefragt werden: Es kommen weniger einschlägige
Dokumente hoch, und die, die kommen, sehen plausibel aus.

**Graceful degradation (Tools)** – absichtlich eine ausdrücklich schlechtere Antwort liefern, wenn ein Tool das
Zeitlimit überschreitet oder ausfällt, statt hängen zu bleiben. Die Nutzer halten ein Hängen für einen Defekt und eine
Antwort mit Vorbehalt bloß für langsam.

<a id="serving"></a>

## Produktivbetrieb – Bereitstellung \{#serving}

**die Bereitstellung / der Betrieb (serving)** – ein Modell oder eine Pipeline als Dienst im Netz betreiben. Zwei
verschiedene Aufgaben, die nicht in einen Topf gehören: die Anwendung bereitstellen (Ihre RAG- oder Agentenpipeline
hinter einer API) und das Modell bereitstellen (die Inferenz des Sprachmodells selbst betreiben).

**die Inferenz (inference)** – das Modell berechnet im Produktivbetrieb Ausgaben aus Eingaben – der
Vorwärtsdurchlauf als Dienst, im Unterschied zum Training. Das, was Sie über die API eines Anbieters kaufen oder
auf eigenen GPUs betreiben.

**die Inferenz-Engine (inference server)** – ein eigens dafür gebauter Server für die LLM-Inferenz auf GPUs:
Continuous Batching, Verwaltung des KV-Caches, eine OpenAI-kompatible API (vLLM, SGLang, Ollama).

**SSE (Server-Sent Events)** – ein einseitig gerichteter Strom von Ereignissen über gewöhnliches HTTP; das
übliche Transportprotokoll für das Streaming von Token aus LLM-APIs.
↗ [Wikipedia](https://en.wikipedia.org/wiki/Server-sent_events)

**das Time-to-First-Token (TTFT)** – die Latenz, bis das erste gestreamte Token beim Nutzer ankommt; die Metrik
der gefühlten Latenz, die das Streaming verbessert.

**das Streaming** – Token an den Nutzer geben, sobald sie erzeugt werden, statt auf die vollständige Antwort zu
warten; der größte Hebel für die gefühlte Latenz (TTFT).

**das Continuous Batching** – das Scheduling einer Inferenz-Engine, bei dem Anfragen auf Token-Ebene in den
laufenden Batch aufgenommen werden und ihn wieder verlassen, statt auf das Ende des ganzen Batches zu warten; der
größte Hebel für den Durchsatz.

**PagedAttention** – die Verwaltung des KV-Cache-Speichers in vLLM: Der Cache wird in Seiten gehalten, wie ein
Betriebssystem den virtuellen Speicher verwaltet; das verringert die Fragmentierung und hebt den Durchsatz.
↗ [arXiv](https://arxiv.org/abs/2309.06180)

**der Cold-Start** – die Verzögerung, bis ein Container mit einem Modell überhaupt bedienen kann: Die Gewichte in
den Speicher der GPU zu laden dauert Dutzende Sekunden bis Minuten. Deshalb heißt Bereitschaft nicht „der Prozess
läuft“ – und deshalb zahlt Scale-to-Zero bei der nächsten Anfrage.

**die OpenAI-kompatible API** – der De-facto-Standard für die Schnittstelle von LLM-Endpunkten; ein einziger
Client-Dialekt spricht mit den APIs der Anbieter und mit selbst betriebenen Inferenz-Engines gleichermaßen, sodass
ein Wechsel des Backends fast nur eine geänderte URL ist.

**die ASGI-Worker (ASGI workers)** – eigenständige Betriebssystemprozesse, jeder mit einer eigenen Kopie des
ASGI-Servers (uvicorn) und einem eigenen Event-Loop, gestartet, um mehr als einen CPU-Kern zu nutzen. Die
Nebenläufigkeit kommt aus dem Event-Loop und nicht aus der Zahl der Worker; Worker bringen Kerne und decken die
kleinen rechenlastigen Anteile ab (Serialisierung, Tokenisierung, JSON).

**uvloop** – eine schnelle Implementierung des Event-Loops auf Basis von libuv, in `uvicorn[standard]` enthalten;
sie ersetzt den voreingestellten Event-Loop von asyncio und bringt mehr Tempo, ohne eine Zeile Code zu ändern.

**synchrone Arbeit auf einen Thread auslagern (threadpool offloading)** – unvermeidbar synchrone Arbeit außerhalb
des Event-Loops auf einem Thread des Pools laufen lassen (`run_in_threadpool`, `asyncio.to_thread`), damit ein
blockierender Aufruf nicht den Event-Loop blockiert und mit ihm jede nebenläufige Anfrage im Prozess.

**Backpressure (Schutz vor Überlast – der Empfänger bremst den Sender)** – die laufende Arbeit absichtlich
begrenzen: Ein Semaphor begrenzt die gleichzeitigen Generationen, eine begrenzte Queue begrenzt, wie viele warten.
So weist der Dienst überzählige Last ab, statt Arbeit anzunehmen, die er nicht zu Ende bringen kann.

**Last gezielt abweisen (load shedding)** – überzählige Anfragen sofort scheitern lassen, sobald die Queue voll
ist (`429` oder `503` mit `Retry-After`), statt sie anzunehmen: Eine Anfrage, die der Client wiederholen kann, ist
ein besseres Ergebnis als ein Dienst, der für alle zusammenbricht.

**Arbeit gar nicht erst annehmen (admission control)** – Arbeit von vornherein abweisen, deren Frist beim Client
längst abgelaufen ist, bevor sie überhaupt zum Zug kommt, statt einen Platz auf der GPU für eine Antwort zu
verbrauchen, auf die niemand mehr wartet. Die Obergrenze sitzt dabei in der Annahme selbst (`max_num_seqs`) und
nicht nachträglich davor.

**Little's Law** – die Identität L = λW: Die mittlere Nebenläufigkeit ist die Ankunftsrate mal der Verweilzeit im
System. Weil das W einer LLM-Generation Dutzende Sekunden beträgt, bedeutet schon eine niedrige Anfragerate eine
große Nebenläufigkeit. ↗ [Wikipedia](https://en.wikipedia.org/wiki/Little%27s_law)

**das Scheduling auf Iterationsebene (iteration-level scheduling)** – das Scheduling einer Inferenz-Engine
(Continuous Batching), das bei jedem Decode-Schritt neue Anfragen zulässt und fertige hinauswirft, statt einen
ganzen statischen Batch abzuwarten; eingeführt vom Orca-Paper (OSDI 2022).

**Prefill / Decode** – die zwei Phasen einer Generation mit gegenläufigen Engpässen: Prefill verarbeitet den
gesamten Prompt in einem einzigen rechenintensiven Durchlauf; Decode erzeugt pro Schritt ein Token, liest dabei
Gewichte und KV-Cache neu und wird durch die Speicherbandbreite begrenzt.

**Chunked Prefill** – das Prefill eines langen Prompts im selben Schritt mit den laufenden Decodes verschränken,
sodass ein einzelner großer Prompt nicht die Tokenerzeugung aller anderen aufhält; das erkauft einen leicht
höheren p50-Wert beim TTFT mit einem deutlich besseren p95-Wert.

**das Prefix-Caching** – den KV-Cache eines gemeinsamen Prompt-Präfixes – etwa eines gemeinsamen System-Prompts –
über Anfragen hinweg wiederverwenden, statt dieses Präfix jedes Mal neu zu berechnen.

**die Quantisierung (quantisation)** – Gewichte und wahlweise auch Aktivierungen mit geringerer Genauigkeit
ablegen: FP8, INT8 oder INT4 über AWQ und GPTQ, unterhalb der Ausgangslage FP16 oder BF16. Das spart Speicher und
hebt den Durchsatz, und es kostet etwas Qualität.

**die Quantisierung des KV-Caches (KV-cache quantisation)** – den KV-Cache selbst mit geringerer Genauigkeit
halten, etwa in FP8; damit verdoppelt sich ungefähr die Zahl der Token, die ein gegebener KV-Pool fasst, was
längere Kontexte oder mehr Nebenläufigkeit erlaubt.

**die Tensor-Parallelität (tensor parallelism)** – die Gewichtsmatrizen jeder Schicht über mehrere GPUs verteilen;
jede Schicht braucht danach ein All-Reduce, um die Teilergebnisse wieder zusammenzurechnen. Das ist
kommunikationsintensiv und verlangt eine schnelle Verbindung (NVLink) innerhalb eines Knotens.

**die Pipeline-Parallelität (pipeline parallelism)** – die Schichten in Stufen teilen und jede Stufe auf eine
andere GPU oder einen anderen Knoten legen, mit Mikro-Batches, die von Stufe zu Stufe wandern; das braucht weit
weniger Kommunikation als die Tensor-Parallelität und verträgt deshalb eine langsamere Verbindung über Knoten
hinweg, zum Preis einer Blase (*bubble*) in der Pipeline, während die Stufen sich füllen und wieder leeren.

**die Daten-Parallelität (data parallelism)** – vollständige Kopien des Modells hinter einem Load-Balancer
betreiben, für den reinen Durchsatz; das Mittel der Wahl, wenn das Modell ohnehin auf eine einzelne GPU passt –
anders als die Tensor- und die Pipeline-Parallelität, die es für Modelle gibt, die nicht passen.

**MIG (Multi-Instance GPU)** – die Zerlegung einer A100 oder H100 in der Hardware in voneinander isolierte
Instanzen, jede mit eigenem Speicher und eigener Fehlerisolation.

**GPU-Time-Slicing** – eine GPU dadurch teilen, dass die Arbeit auf ihr verschränkt wird, ganz ohne Speicher- oder
Fehlerisolation: in Ordnung für einen Entwicklungscluster, riskant im Produktivbetrieb, wo der Fehler oder die
Speicherspitze eines Mandanten auf die anderen durchschlägt.

**KEDA** – ein ereignisgetriebener Autoscaler für Kubernetes, der Lasten nach externen oder eigenen Metriken
skaliert (Länge der Queue, Token pro Sekunde, Auslastung der GPU) – anders als der voreingestellte HPA, der nur
CPU und Speicher sieht.

**KServe** – ein Baustein für die Modellbereitstellung auf Kubernetes (mit Knative), der ein Autoscaling nach den
eingehenden Anfragen bietet, einschließlich Scale-to-Zero und einer Skalierung nach Nebenläufigkeit.

**Serverless GPU** – GPU-Kapazität, sekundengenau abgerechnet, im Leerlauf auf null skaliert und ohne einen
Cluster, den Sie betreiben müssten (Modal, RunPod, Replicate, Baseten, Cloud Run mit angehängter GPU); das
zentrale Problem sind die Kosten des Cold-Starts, gemildert durch Speicherabbilder und einen Vorrat bereits
gestarteter Instanzen.

<a id="cloud-platforms"></a>

## Produktivbetrieb – Cloud-KI-Plattformen \{#cloud-platforms}

**der verwaltete Endpunkt (managed endpoint)** – ein Modell, das eine Cloud-KI-Plattform hinter Ihrem IAM, Ihrer
Abrechnung und Ihrem Netzperimeter bereitstellt: Sie rufen es auf, die Plattform betreibt es.

**der Modellkatalog (model catalogue)** – die Menge der eigenen und der fremden Modelle, die eine Plattform als
verwaltete Endpunkte bereitstellen kann (Foundry Models, der Katalog von Bedrock, Model Garden).

**Data Residency (der Speicherort)** – die Zusage, wo Anfragen verarbeitet werden, nach Region oder geografischem
Gebiet; zusammen mit der Zusage, die Daten nicht fürs Training zu verwenden, und der privaten Netzanbindung bildet
sie die Compliance-Triade.

**Provisioned Throughput (bereitgestellter Durchsatz)** – reservierte, dedizierte Modellkapazität mit planbarer
Latenz, gekauft statt der gemeinsam genutzten Token nach Verbrauch (PTU bei Azure, Provisioned Throughput bei
Vertex, der Tarif `Reserved` bei Bedrock).

**der Batch-Tarif (batch mode, batch tier)** – ein vergünstigter asynchroner Tarif für Arbeit, auf deren Antwort
niemand wartet.

**das verwaltete RAG-Angebot (managed RAG)** – die Pipeline von der Ingestion bis zum Retrieval als fertiges
Produkt der Plattform (Bedrock Knowledge Bases, Foundry IQ auf Azure AI Search, die RAG Engine von Vertex); es
tauscht die Stellschrauben gegen Geschwindigkeit.

**Vendor-Lock-in** – die Abhängigkeit, die nicht der Endpunkt selbst erzeugt – der ist oft OpenAI-kompatibel –,
sondern das, was die Plattform rundherum mitliefert: das verwaltete RAG-Angebot, die SDKs.

**das Fine-Tuning (Nachtrainieren des Modells)** – das Training eines Basismodells auf Ihren Daten fortsetzen, um
sein Verhalten zu ändern; auf den Plattformen reicht das vom überwachten Fine-Tuning (SFT) über die Verfahren mit
Präferenzdaten und Reinforcement Learning (DPO, RFT) und die Distillation bis zum fortgesetzten Vortraining. Tunen
Sie die Form – Stil, Schema, Format –, nicht Fakten, die sich ändern; dafür ist RAG da.

**LoRA / PEFT** – parametereffizientes Fine-Tuning: einen kleinen Adapter über eingefrorenen Basisgewichten
trainieren statt aller Gewichte, für einen Bruchteil an Rechenzeit und Speicher.

**DPO (Direct Preference Optimization)** – Fine-Tuning auf Paaren aus bevorzugter und abgelehnter Antwort, um die
Ausgaben eines Modells auszurichten, ohne ein eigenes Belohnungsmodell.

**das Reinforcement-Fine-Tuning (RFT)** – Fine-Tuning gegen eine Belohnungsfunktion oder einen Bewerter, der jede
Antwort bepunktet und damit das erwünschte Verhalten belohnt.

**die Distillation (model distillation)** – ein kleineres Schülermodell darauf trainieren, die Ausgaben eines
größeren Lehrermodells nachzuahmen; das kostet ein wenig Qualität und senkt die Kosten der Bereitstellung
deutlich.

**die Context-Distillation (context distillation)** – ein Modell darauf trainieren, sich so zu verhalten, als
läge ein Kontext vor – ein langer System-Prompt, eine Richtlinie, ausgearbeitete Beispiele –, ohne ihn zur
Laufzeit überhaupt mitzugeben. Sie beantwortet die Frage, wie Sie aufhören, diese Prompt-Token bei jeder
Anfrage zu bezahlen, und verlangt den üblichen Preis dieser Leiter: Das Verhalten ist danach in den Gewichten
eingefroren, eine geänderte Richtlinie heißt also erneut trainieren. Das Prompt-Caching löst dieselbe Rechnung
ohne diesen Tausch.

**das fortgesetzte Vortraining (continued pre-training)** – das Vortraining eines Basismodells auf großen
Fachdaten ohne Labels weiterführen, bevor überhaupt auf eine Aufgabe hin angepasst wird.

**die verwaltete Agenten-Laufzeitumgebung (managed agent runtime)** – ein Dienst der Plattform, der die
Agentenschleife selbst ausführt und Sitzungs- und Gedächtnispersistenz, ein Gateway für Tools und Identität,
Observability und Scale-to-Zero mitbringt (Bedrock AgentCore, Foundry Agent Service, Vertex Agent Engine) – genau
die Unterschiede gegenüber einem Agenten, den Sie selbst in einem Container betreiben.

**FinOps** – die Disziplin, die technische Entscheidungen an die Kosten in der Cloud bindet und die Ausgaben auf
eine Zahl für die Stückkosten bringt, die sich verteidigen lässt.

**die Kostenmodellierung (cost modelling)** – die Ausgaben einer Arbeitslast aus ihrer Tokenform und den
Preishebeln der Plattform abschätzen, bevor man sich auf sie festlegt.

**die Stückkosten (unit economics)** – die Kosten einer Einheit an Wert – einer Anfrage, eines aktiven Nutzers,
eines ausgelieferten Features –, die Zahl, auf die FinOps hinarbeitet.

**der Rabatt für eine zugesagte Nutzung (committed-use discount)** – ein niedrigerer effektiver Preis dafür, dass
Sie dedizierte Kapazität reservieren oder eine Nutzung über einen Zeitraum zusagen (Reservierungen von PTU bei
Azure, Reserved bei Bedrock).

**das Context-Caching** – das Zwischenspeichern eines großen, wiederverwendeten Kontexts auf der Seite des
Anbieters, das Gegenstück zum Prompt-Caching; abgerechnet wird es zu einem Bruchteil frischer Eingabe, dazu kommt
eine Gebühr für die Speicherung.

**der Egress zwischen Regionen (cross-region egress)** – die Gebühr dafür, Daten zwischen Regionen oder zwischen
Clouds zu bewegen; eine Kostenachse des Reglers zwischen Speicherort und Kapazität.

**das Gateway über mehrere Clouds hinweg (multi-cloud gateway)** – ein Router vor mehreren Anbietern oder Clouds,
der einen einzigen Schnittstellenstandard bedient, die OpenAI-kompatible API – für Unabhängigkeit, Failover, ein
Routing nach Kosten und eine zentrale Steuerung (LiteLLM, Portkey).

**die digitale Souveränität (digital sovereignty)** – die Kontrolle darüber, wer auf Ihre Daten und Arbeitslasten
zugreifen, sie betreiben und sie rechtlich herausverlangen kann und unter welcher Gerichtsbarkeit das geschieht –
Souveränität über den Betrieb, über die Daten und über die Software. Zu unterscheiden von der Data Residency, die
allein sagt, wo die Daten liegen.

**die souveräne Cloud (sovereign cloud)** – eine Cloud, die digitale Souveränität zusichern soll: über Regionen in
europäischer oder nationaler Hand, über „vertrauenswürdige Clouds“ von Partnern oder über eine vollständig
physisch getrennte Bereitstellung (AWS European Sovereign Cloud, Microsoft Sovereign Cloud, Google Distributed
Cloud).

**physisch getrennt (air-gapped)** – eine Umgebung, die vollständig vom öffentlichen Internet abgeschnitten ist,
für regulierte Arbeitslasten und für die Verteidigung; Spitzenmodelle hinken dort hinterher oder fehlen ganz.

<a id="tooling-ecosystem"></a>

## Produktivbetrieb – das Tooling-Ökosystem \{#tooling-ecosystem}

**die Instrumentierung (instrumentation)** – die Stellen im Code oder die Haken eines SDK, an denen Traces, Spans
und Metriken aus der Pipeline entstehen; die Voraussetzung für Observability.

**die GenAI-Konventionen von OpenTelemetry (OpenTelemetry GenAI conventions)** – der entstehende
anbieterneutrale Standard für die Namen von Spans und Attributen bei Modellaufrufen (Modell, Token, Tool-Calls):
einmal instrumentieren, danach exportieren, wohin Sie wollen. Mitte 2026 noch experimentell.
↗ [GitHub](https://github.com/open-telemetry/semantic-conventions-genai)

**der Klassifikator für Sicherheitsrisiken (safety classifier)** – ein kompaktes, spezialisiertes Modell, das Text
auf der Eingabe- oder auf der Ausgabeseite nach Risikokategorien bewertet (Llama Guard, Granite Guardian); es
spielt mit den Guardrails-Frameworks zusammen, die die Prüfungen orchestrieren.

**das Red-Teaming** – das eigene System absichtlich angreifen, um seine Abwehr zu messen (die Erfolgsrate der
Angriffe); als Funktion in den Werkzeugen für die Evaluierung und in den Plattformen enthalten.

<a id="llmops"></a>

## Produktivbetrieb – LLMOps \{#llmops}

**LLMOps** – die Betriebsdisziplin für Anwendungen mit Sprachmodellen: ausrollen, überwachen und die Kosten
steuern für Systeme, deren Verhalten in Prompts, Modellversionen, Indexen und Konfigurationen steckt und nicht
allein im Code. MLOps, zugeschnitten auf Anwendungen mit Basismodellen.

**das Canary Release** – einen kleinen Teil des laufenden Verkehrs auf die neue Variante lenken – Prompt, Modell,
Index – und dabei die Metriken für Qualität und Kosten beobachten; eine Regression zeigt sich an einem Bruchteil
der Nutzenden und lässt sich günstig zurücknehmen.
↗ [Martin Fowler](https://martinfowler.com/bliki/CanaryRelease.html)

**das Shadow Deployment** – die neue Variante läuft auf gespiegeltem Verkehr aus dem Produktivbetrieb, und ihre
Antworten bekommt niemand zu sehen; ein gefahrloser Vergleich der Qualität an echten Anfragen.

**die Prompt-Registry** – ein versionierter Speicher für Prompts, abgekoppelt vom Ausrollen des Codes:
Produktteams ändern Prompts, ohne Code auszuliefern, und jede Antwort aus dem Produktivbetrieb bleibt einer
genauen Prompt-Version zuzuordnen.

**das Model-Pinning (die Modellversion festlegen)** – den Produktivbetrieb auf genaue Modell-Snapshots festlegen
statt auf einen beweglichen Alias; die Aktualisierung beim Anbieter wird damit zu einem ausdrücklichen, von der
Evaluierung abgesicherten Deployment statt zu einer stillen Verhaltensänderung.

**das Routing über Modelle hinweg (model routing)** – jede Anfrage an das günstigste Modell schicken, das sie
bewältigt; der Router kann eine Regel, ein Klassifikator oder wieder ein Modell sein. Zu unterscheiden vom Routing
der Anfrage über Indexe (Teil I) und von der Auswahl eines Tools (Teil II): Hier wird entschieden, wer antwortet.

**Fallbacks** – die im Voraus festgelegten Ausweichwege – eine andere Region, ein anderer Anbieter, ein günstigeres
Modell –, auf die das System umschaltet, sobald das erste Modell einen Fehler liefert oder sein Rate Limit
erreicht ist.

**das LLM-Gateway** – die Schicht, die den Zugang zu allen Modellen hinter einer einzigen API bündelt: Routing,
Fallbacks, API-Schlüssel, Budgets und Rate Limits je Team (LiteLLM, OpenRouter).

**das Prompt-Caching** – das Zwischenspeichern des wiederkehrenden Prompt-Präfixes auf der Seite des Anbieters
(System-Prompt, Beispiele, statischer Kontext); zwischengespeicherte Eingabe-Token werden stark verbilligt
abgerechnet, weshalb Prompts vom statischen Präfix her gebaut werden.

**das semantische Caching (semantic caching)** – eine gespeicherte Antwort auf eine nahezu gleiche Frage
zurückgeben, zusammengeführt über die Ähnlichkeit der Embeddings; das spart die Kosten der ganzen Anfrage und
riskiert einen Treffer auf eine Frage, die sich nur in einer Feinheit unterscheidet. Der Speicher dahinter ist der
semantische Cache.

**der Drift** – die Welt verschiebt sich unter einer eingefrorenen Konfiguration: der Eingabedrift (der Verkehr
fragt nach neuen Dingen), der Korpusdrift (Dokumente altern) und der vorgelagerte Modelldrift (der Anbieter ändert
ein Modell ohne festgelegte Version).

**der Bewerter (grader)** – beim Reinforcement-Fine-Tuning der Bepunkter, den Sie selbst festlegen und der jeden
Antwortkandidaten bewertet; seine Punktzahl ist das Belohnungssignal, gegen das das Training optimiert.

**Showback** – jedem Team, jedem Feature oder jedem Produkt den eigenen Verbrauch berichten, während die Kosten
auf einem zentralen Budget bleiben; das Fundament von FinOps, auf das nie zu verzichten ist.

**Chargeback** – die Kosten tatsächlich auf die Gewinn- und Verlustrechnung des verbrauchenden Teams oder Produkts
buchen; das bringt mehr Verbindlichkeit als Showback und ist nur dann tragfähig, wenn der Zuordnung der Kosten zu
trauen ist.

**die Freigabe vor dem Release (release gate)** – die Prüfung der Qualität, die zwischen einer Änderung und dem
Produktivbetrieb steht: die Evaluierung in der CI, vom Release aus betrachtet, die einen Merge oder ein Deployment
anhält, dessen Metriken auf dem Goldstandard unter den Schwellenwert fallen.

**die Richtlinie zum Fehlerbudget (error budget policy)** – die vor jedem Vorfall unterschriebene Vereinbarung,
die festhält, was geschieht, wenn das Fehlerbudget aufgebraucht ist – in der Regel ein Stopp aller Releases – und
wer welche Handlung übernimmt.

**der Stopp aller Releases (release freeze)** – alle Releases anhalten, die nicht kritisch sind, P0-Behebungen und
Sicherheitspatches ausgenommen, bis ein Dienst wieder innerhalb seines SLO liegt; die letzte Steuerung, die eine
Richtlinie zum Fehlerbudget auslöst.

**die Job-Queue (job queue)** – Infrastruktur, die die Rate, mit der Arbeit ankommt, von der Rate trennt, mit der
sie abgearbeitet wird: Ein Producer stellt einen Job in die Queue und bekommt sofort eine Job-ID zurück, und ein
Pool aus Workern arbeitet die Queue asynchron ab.

**die Dead-Letter-Queue (DLQ)** – eine Nebenqueue für Jobs, die ihre Wiederholungen aufgebraucht haben; sie hält
einen Poison-Job davon ab, die Hauptqueue zu blockieren, und ihr Wachstum ist ein Signal, auf das ein Alarm
gehört.
