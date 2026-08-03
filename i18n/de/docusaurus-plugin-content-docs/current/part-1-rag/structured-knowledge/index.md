---
title: Strukturiertes Wissen
slug: /part-1-rag/structured-knowledge/
---

# Wenn die Antwort in keiner Passage steht

Teil I hat auf jeder Seite etwas vorausgesetzt und es nie ausgesprochen: dass Ihr Wissen als **Prosa** ankommt. Dokumente parsen, in Chunks zerlegen, die Chunks einbetten, suchen, neu ordnen, antworten. Die ganze Pipeline ist eine Wette darauf, dass es irgendwo im Korpus eine Passage gibt, die die Antwort enthält, sobald man sie nur findet.

Für einen großen Teil des Wissens im Unternehmen geht diese Wette auf. Deshalb ist die Pipeline der Regelfall, und deshalb hat sie drei Lektionen verdient. An drei gewöhnlichen Fragen versagt sie trotzdem, und an jeder auf andere Weise:

- *„Welche Risiken tauchen in unseren zehntausend Verträgen immer wieder auf?“* – kein Chunk enthält diese Antwort. Sie versteckt sich nicht in einer Passage, die Sie nicht abgerufen haben; sie ist nie aufgeschrieben worden.
- *„Wie viel Umsatz hat das Enterprise-Segment im letzten Quartal gemacht?“* – auch diese Antwort hat niemand aufgeschrieben. Sie muss berechnet werden, und zwar auf der Grundlage einer Definition von „Umsatz“, über die zwei Abteilungen womöglich uneins sind.
- *„Alles, was wir über diesen Lieferanten wissen“* – der Name des Lieferanten steht in sechs Schreibweisen über vier Systeme verteilt, und kein noch so gutes Reranking macht aus diesen sechs Dingen ein Ding.

Jede dieser Fragen verlangt Wissen mit **Struktur** – Entitäten, Beziehungen, Definitionen –, und für jede gibt es eine ausgereifte Antwort, die kein Vektorindex ist. Diese Lektion behandelt alle drei und verweilt vor allem bei der Frage, wann sich ihr Aufbau überhaupt lohnt: Jede wird kräftig beworben, und jede ist häufig die falsche Wahl.

:::note[Lesen Sie den Abschnitt, den Sie brauchen]

Die drei Hauptabschnitte stehen für sich, und eine Reihenfolge, in der man sie lesen müsste, gibt es nicht. Wenn Sie entscheiden, ob Sie überhaupt Struktur herausziehen sollen, beginnen Sie bei [den drei Arten von Struktur](#three-kinds-of-structure) – Vokabular, Taxonomie, Ontologie. Hat jemand einen Knowledge Graph verlangt, gehen Sie zu [wann sich sein Aufbau lohnt](#when-a-graph-earns-its-build-cost). Geht es um Zahlen und Dashboards, gehen Sie zur [semantischen Schicht](#the-semantic-layer-names-two-different-things). Der [Schlussabschnitt](#which-of-the-three-you-actually-need) ist die Entscheidung, die alle drei zusammenführt.

:::

## Drei Arten von Struktur – und meistens gewinnt die günstigste \{#three-kinds-of-structure}

Drei Dinge werden ständig miteinander verwechselt, und sie auseinanderzuhalten beseitigt den größten Teil der Verwirrung.

| | Was es ist | Was es Ihnen bringt |
|---|---|---|
| **Das kontrollierte Vokabular** | eine feste Liste zugelassener Bezeichnungen | ein Extraktor hört auf, Bezeichnungen zu erfinden |
| **Die Taxonomie** | eine hierarchische Gliederung dieser Bezeichnungen | Aggregation, Vererbung, Fragen nach Ober- und Unterbegriffen |
| **Die Ontologie** | Klassen, Eigenschaften und die Einschränkungen, denen sie unterliegen | Validierung, und die Ableitung von Fakten, die niemand hingeschrieben hat |

**Die meisten Teams, die eine Ontologie verlangen, brauchen ein kontrolliertes Vokabular.** Sagen Sie das früh, denn der Abstand zwischen diesen beiden Artefakten ist ungefähr der Abstand zwischen einem Nachmittag und einer Stelle, die dauerhaft besetzt bleiben muss.

Der Fehler, den ein kontrolliertes Vokabular behebt, ist der bekannteste der strukturierten Extraktion. Sie lassen ein Modell Beziehungen aus dreitausend Dokumenten herausziehen. Es tut das, und zwar flüssig. Im einen Dokument ist eine Person über `works_for` mit einer Firma verbunden, im nächsten über `employed_by`, im dritten kommt dieselbe Beziehung als `is_employee_of` zurück. Weiter hinten lässt sich davon nichts zusammenführen, denn für jede Abfrage sind das drei Prädikate ohne Verwandtschaft. Falsch lag das Modell in keinem einzelnen Dokument – es war nur über alle hinweg an nichts gebunden. Geben Sie ihm eine geschlossene Liste zugelassener Beziehungstypen, und das Problem verschwindet – es kostet Sie nicht mehr, als die Liste zu schreiben.

### Wo sich ein Schema wirklich auszahlt

Schemadisziplin zahlt sich an drei Stellen aus, die sich voneinander trennen lassen – und es lohnt sich zu wissen, welche der drei Sie gerade brauchen:

**Bei der Extraktion.** Geben Sie dem Modell die Klassen und Eigenschaften vorab, und es hört auf zu erfinden. Das ist das `works_for`-Problem von eben, und hier bringt die günstigste Struktur am meisten.

**Bei der Validierung.** Eine Schicht aus Bedingungen kann eine extrahierte Aussage zurückweisen, die gegen das Schema verstößt: eine Beschäftigungskante, die auf ein Dokument statt auf eine Organisation zeigt, ein Datum außerhalb des zulässigen Bereichs. Das ist ein deterministischer Kontrollpunkt, den ein probabilistischer Erzeuger passieren muss – genau die Bauform, für die der AI-SDLC-Kurs unter [layered gates and mechanism diversity](/ai-sdlc/part-3-verification/layered-gates) argumentiert (die Seite liegt nur auf Englisch vor). Ein Schema ist überhaupt erst das, was einen solchen Kontrollpunkt *möglich* macht, denn er braucht etwas, wogegen er prüfen kann.

**Bei der Abfrage.** Wenn Sie eine Frage einem Begriff zuordnen wollen statt einer Passage, brauchen Sie ein Modell der Begriffe. Das ist die [semantische Schicht](#the-semantic-layer-names-two-different-things) in ihrem zweiten Sinn, und das Domänenmodell ist das Artefakt, dem sie eine Äußerung zuordnet.

### Ein Domänenschema ist kein Antwortschema

Ein JSON Schema ist Ihnen in diesem Handbuch bereits begegnet: Es schränkt die **Form der Antwort eines Modells** ein – Pflichtfelder, zugelassene Aufzählungswerte, ein Parsen, das entweder gelingt oder scheitert. Eine Ontologie schränkt die **Form der Welt ein, von der die Antwort handelt**.

Auf dem Papier sehen die beiden ähnlich aus, und sie sind zwei ganz verschiedene Artefakte. Ein Antwortschema gehört zu einem Prompt, ändert sich mit dem Prompt und gehört dem, dem dieses Feature gehört. Ein Domänenmodell gehört der Organisation, ändert sich, wenn sich das Geschäft ändert, und überlebt jeden Prompt, in dem es je verwendet wurde. Behandeln Sie das eine wie das andere, und Ihr Domänenmodell liegt am Ende versioniert neben einer Prompt-Vorlage – so erfährt ein Unternehmen, dass seine Definition von „Kunde“ bei einer Textkorrektur verändert wurde.

### Die ehrliche Voreinstellung – und der Test, wann Sie sie verlassen

Für die meisten Systeme mit einem Sprachmodell liefert ein JSON Schema samt Validator den wirksamen Teil des Nutzens zu einem Bruchteil der Kosten: eine geschlossene Menge von Typen und einen Weg, Verstöße zurückzuweisen. Das ist keine Notlösung, für die man sich entschuldigen müsste, sondern meistens die richtige Antwort. Der [formale Unterbau](./deep-dive.md#the-formal-stack-by-purpose) – RDF, OWL 2, SHACL, SPARQL – ist den Aufwand unter Bedingungen wert, die Sie benennen können: Sie müssen Fakten ableiten, die niemand hingeschrieben hat; Sie müssen sich an ein Standardvokabular halten, das es in Ihrer Branche bereits gibt; oder eine Aufsichtsbehörde hat das Schema vorgegeben, und die Konformität steht nicht zur Wahl.

Zwei Kostenposten entscheiden das, und keiner davon steht auf einer Anbieterfolie. Der erste: Eine Ontologie wird von Menschen gepflegt, auf Dauer, und diese Pflege ist Urteilsarbeit und keine Aufgabe, die sich einplanen lässt. Der zweite wiegt schwerer: *Eine falsche Ontologie ist schlimmer als gar keine.* Wo ein Schema fehlt, erzeugt ein Extraktor ein Durcheinander, das wie ein Durcheinander aussieht. Ein falsches Schema zwingt den Extraktor, falsch einzuordnen, und falsch eingeordnete Daten sehen *sauber* aus: Sie validieren, sie lassen sich verknüpfen, sie erscheinen im Dashboard – und sie sind so falsch, dass weiter hinten keine Prüfung es bemerken kann.

Der Test für zusätzliche Struktur lautet deshalb nicht, ob damit alles ordentlicher wäre. Er lautet: *Können Sie eine Abfrage nennen, die Sie heute nicht beantworten können und die diese Struktur beantworten würde?* Wenn nicht, bauen Sie, damit es aufgeräumter aussieht – und das überlebt die erste Übergabe an eine andere zuständige Person nicht.

## Wann sich der Aufbau eines Knowledge Graphs lohnt \{#when-a-graph-earns-its-build-cost}

Ein **Knowledge Graph** (Wissensgraph) legt Entitäten als Knoten und die Beziehungen zwischen ihnen als Kanten ab – von einem Modell aus Ihrem Korpus herausgezogen oder von Hand gepflegt; **GraphRAG** ist das Retrieval über einen solchen Graphen und als Eigenname zugleich Microsofts Referenzimplementierung. Fangen Sie bei dem an, was Sie ohnehin schon können, denn auf das übliche Eröffnungsargument für einen solchen Graphen – er beantworte mehrschrittige Fragen – gibt dieser Kurs an anderer Stelle eine bessere und billigere Antwort.

*„Wer leitet die Abteilung, die Richtlinie X erlassen hat?“* sieht nach einem Durchlauf durch den Graphen aus. Ist es nicht. Zerlegen Sie die Frage in zwei gewöhnliche Abrufe – erst die Abteilung finden, die X erlassen hat, dann deren Leitung –, und die statische Pipeline, die Sie bereits haben, beantwortet sie. Das ist [Agentic RAG](../../part-2-agents/agentic-rag/index.md), und es braucht keinen Extraktionslauf, kein Schema und keine Pflege. Wenn der Hauptnutzen eines Graphenvorschlags die Mehrschrittigkeit ist, fehlt dem Vorschlag noch sein eigentlicher Grund.

Diesen Grund gibt es – nur liefert ihn eine andere Klasse von Fragen.

### Drei Klassen von Fragen – und nur eine entscheidet

**Lokal – die Nachbarschaft einer Entität.** *„Was wissen wir über diesen Lieferanten, und womit hängt er zusammen?“* Hier hilft ein Graph. Es hilft aber auch die Zerlegung der Frage, und es hilft eine gut gefilterte Vektorsuche über Dokumente, die mit dem Lieferanten verschlagwortet sind. Der Gewinn ist bescheiden, und er rechtfertigt die Maschinerie nicht.

**Global – das ganze Korpus.** *„Welche Themen wiederholen sich über diese zehntausend Dokumente hinweg?“* *„Welche Risiken tauchen in mehr als einer Vertragsfamilie auf?“* Kein Retrieval über Chunks beantwortet das. Retrieval setzt voraus, dass die Antwort im Korpus liegt und Ihre Aufgabe darin besteht, sie zu finden; hier gibt es keinen Chunk zu finden. Die Antwort ist eine *Zusammenfassung des Korpus*, und sie muss erstellt sein, bevor irgendjemand fragt. Das ist der Fall, der den Aufbau rechtfertigt. Und das ist auch das Thema des GraphRAG-Papers: Herkömmliches RAG, so seine Autoren, „scheitert an globalen Fragen, die sich an ein ganzes Textkorpus richten“ ([Edge et al., *From Local to Global*](https://arxiv.org/abs/2404.16130)).

**Dieselbe Entität aus verschiedenen Quellen.** Dieselbe Organisation als `Acme Corp`, `Acme Corporation`, `ACME Corp.` und dazu ein Tippfehler. In einem Graphen wird dieses Problem sichtbar – und hier wird aus der Arbeit am Graphen unversehens [Arbeit an der Duplikaterkennung](./deep-dive.md#entity-resolution), eine eigene Disziplin mit einem eigenen Budget.

### Die Kosten sind Entscheidungskriterien, keine Fußnoten

**Die Extraktion ist ein Durchlauf des Sprachmodells über Ihr gesamtes Korpus** und wird entsprechend bepreist. Die deutlichste verfügbare Zahl stammt aus Microsoft Researchs eigener Nachfolgearbeit: [LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) wurde eigens gebaut, um die Kosten der Indexierung im Voraus zu vermeiden, und für seine Indexierung wird angegeben, sie sei „identisch mit Vektor-RAG und 0,1 % der Kosten eines vollständigen GraphRAG“. Von hinten gelesen heißt das: Der vollständige Aufbau liegt in der Größenordnung des Tausendfachen dessen, was es kostet, dasselbe Korpus bloß einzubetten. Das ist eine Zahl für ein Angebot.

**Die Extraktion halluziniert Kanten.** Eine Beziehung, die das Modell erschlossen hat und die in keinem Dokument steht, liegt anschließend im Graphen und sieht genauso aus wie eine, die dort stand. Falsche Fakten in einem Korpus ergeben fehlerhafte Tripel in einem maschinell erzeugten Graphen, wie [*Less is More: Denoising Knowledge Graphs for RAG*](https://arxiv.org/html/2510.14271v1) belegt, während es untersucht, wie die verbreiteten Systeme mit dem Rauschen der Extraktion umgehen. Auf dem Vektorpfad gibt es dazu keine Entsprechung: Ein abgerufener Chunk ist ein Chunk, den es gibt.

**Der Graph veraltet wie jedes abgeleitete Artefakt.** Einen Graphen fortlaufend nachzuziehen, während sich sein Korpus ändert, ist der wirklich harte Teil, und es ist dasselbe Argument, das dieses Handbuch bei eingefrorenen Modellgewichten bereits vorbringt – siehe [LLMOps](../../part-3-production/llmops/deep-dive.md). Ein Graph, der einmal gebaut und nie neu gebaut wird, ist eine Momentaufnahme, die ab dem Tag ihrer Fertigstellung an Wert verliert.

**Einen Graphen zu bewerten ist nicht dasselbe wie das Retrieval zu bewerten.** Recall@K über Chunks sagt Ihnen nichts darüber, ob die herausgezogenen Beziehungen *wahr* sind. Sie brauchen Precision auf den extrahierten Tripeln, gemessen an einer gelabelten Stichprobe, und eine End-to-End-Bewertung der Antworten, und zwar für genau die Fragetypen, die nur der Graph bedienen kann. Die Lektion zur [Evaluierung](../cross-cutting/evaluation/index.md) hält die Maschinerie dafür bereit; die Einzelheiten stehen in der Vertiefung.

### Wann Sie keinen Graphen bauen sollten

Ein kleines Korpus. Fragen, die auf ein Nachschlagen hinauslaufen. Daten, die sich schneller ändern, als Sie neu extrahieren können. Und der Punkt, der es in der Praxis entscheidet: Niemand hat zugesagt, das Extraktionsschema dauerhaft zu pflegen. Ohne diese Zuständigkeit wird man den Fehlschlag der Technik anlasten statt der Personalentscheidung, die ihn verursacht hat.

Wo ein Graph überhaupt gerechtfertigt ist, ersetzt er im Produktivbetrieb üblicherweise nicht die Vektoren. Die übliche Form ist eine andere: Vektoren fürs Nachschlagen, der Graph für die Struktur, und ein Router, der entscheidet, welche Frage wohin geht – dieselbe Routing-Maschinerie, die die [Vertiefung zum Retrieval](../retrieval/deep-dive.md) bereits aufbaut.

## Die semantische Schicht bezeichnet zwei verschiedene Dinge \{#the-semantic-layer-names-two-different-things}

Dieser Ausdruck steht vor allem deshalb in dieser Lektion, weil er zwei verschiedene Dinge bezeichnet und Gespräche im Unternehmen unbemerkt zwischen ihnen hin- und herrutschen. Beide sind real.

**Die Kennzahlenschicht** (*metrics layer*). Eine Modellierungsebene über einem Warehouse – dbts Semantic Layer, Cube, LookML und Verwandte –, in der eine Kennzahl *einmal* definiert wird: was „Umsatz“ bedeutet, welche Verknüpfungen er voraussetzt, welche Filter zulässig sind, nach welchen Dimensionen er sich schneiden lässt. Jeder Abnehmer fragt danach die Kennzahl ab, statt sie in SQL nachzubauen. [dbt](https://docs.getdbt.com/docs/build/about-metricflow) beschreibt das Problem, das damit gelöst wird, als „mehrere Analysten, die an denselben Daten arbeiten und dabei jeweils ihre eigene Abfragemethode benutzen“, was zu „Verwirrung, Widersprüchen und Kopfschmerzen im Datenmanagement“ führt.

**Die semantische Schicht über der sprachlichen Schicht.** In der dialogorientierten KI: Der Assistent ordnet eine Äußerung einem **Begriff der Domäne** zu – einer Entität, einer Beziehung, einer Absicht – und nicht einer Passage. Die Antwort wird anschließend aus dem Domänenmodell erzeugt und nicht aus dem, was der Retriever gerade zurückgegeben hat.

Gemeinsam ist den beiden, dass sie eine Auslegung von Fall zu Fall durch ein gemeinsames Modell ersetzen. Dieselbe Schicht sind sie nicht, sie teilen keine Werkzeuge, und meist gehören sie verschiedenen Teams. Sagen Sie im ersten Satz, welche der beiden Sie meinen, und das übrige Gespräch wird leichter.

### Text-to-SQL: auswählen statt herleiten

Den praktischen Ertrag bringt die Kennzahlenschicht, und er ist in dieser Lektion der deutlichste Fall dafür, wie sehr Struktur ein Problem vereinfachen kann.

Ein Vektor-Top-K kann nicht zählen. Fragen nach Aggregaten – Summen, Verhältnisse, „wie viele“, „verglichen mit dem Vorquartal“ – brauchen neben dem semantischen einen strukturierten Pfad, also einen zweiten Weg neben der Vektorsuche. Am nächsten liegt es, diesen Weg von einem Modell bauen zu lassen, das SQL gegen Ihr Warehouse schreibt. Auf ein rohes Schema angesetzt, muss das Modell die ganze Abfrage **herleiten**: die Verknüpfungen erschließen, raten, welche von vier Datumsspalten das fachlich gemeinte Datum ist, mit Werten in dem Format umgehen, in dem das Quellsystem sie hinterlassen hat. [BIRD](https://bird-bench.github.io/) ist ein Benchmark, der eigens um große, realistische, unsaubere Datenbanken herum gebaut ist, in denen die Werte „ihr ursprüngliches und häufig ‚schmutziges‘ Format behalten“. Auf ihm erreichen menschliche Data Engineers 92,96 % Ausführungsgenauigkeit, das führende System 81,95 % (beides Stand der Rangliste vom September 2025). Knapp jede fünfte Abfrage geht auf realistischen Schemata daneben, und eine falsche SQL-Abfrage meldet sich nicht: Sie gibt eine Zahl zurück.

Setzen Sie dasselbe Modell auf eine semantische Schicht an, und seine Aufgabe ändert sich. Es leitet keine Abfrage mehr her, sondern *wählt* eine definierte Kennzahl und eine Menge von Dimensionen **aus**. Das ist eine viel kleinere Entscheidung, denn sie trifft eine Auswahl aus einer geschlossenen Liste, und ihr Fehlerbild ändert sich damit ebenfalls: eine falsche *Auswahl* statt einer falschen *Herleitung*. Eine falsche Auswahl lässt sich erkennen – Sie können zeigen, welche Kennzahl gewählt wurde –, eine subtil falsche Verknüpfung nicht. [Cube](https://docs.cube.dev/docs/introduction) bringt dieses Argument für Agenten ganz direkt vor: Ohne eine semantische Schicht landen „Agenten, die SQL gegen ein Warehouse schreiben, bei widersprüchlichen Kennzahlen und ungeregeltem Zugriff“.

Die Schicht bringt noch etwas Zweites, und es fällt stärker ins Gewicht, als es klingt. Weil jede Abfrage durch sie hindurchgeht, verschiebt sich der Ort, an dem die Richtlinien durchgesetzt werden – Cube formuliert es so, dass eine Abfrage „gegen das Datenmodell geprüft wird und die Zugriffsrichtlinien deterministisch auf sie angewendet werden, bevor sie das Warehouse erreicht“. Das ist dasselbe Prinzip, auf dem die Vertiefung zum Retrieval besteht – [vor der Suche filtern, nie danach](../retrieval/deep-dive.md) –, nur von der strukturierten Seite her.

### Warum Unternehmen Antworten lieber einem Begriff zuordnen

Der Weg über den Begriff bringt zwei Dinge, die eine Quellenangabe nicht bringt. **Widerspruchsfreiheit**: Dieselbe Frage, zweimal anders formuliert, wird demselben Begriff zugeordnet und bekommt damit dieselbe Antwort. **Nachprüfbarkeit**: Sie können zeigen, *welchem* Begriff sie zugeordnet wurde und warum. Eine Quellenangabe sagt Ihnen, welchen Text das Modell gelesen hat; sie sagt Ihnen nicht, wofür das Modell diesen Text genommen hat.

Hier treffen sich zwei der drei Abschnitte dieser Lektion: Das Domänenmodell, dem zugeordnet wird, ist genau [die Ontologie](#three-kinds-of-structure) – weshalb „wir brauchen eine Ontologie“ und „wir brauchen eine semantische Schicht“ so oft derselbe Wunsch sind, der aus zwei Abteilungen ankommt.

### Was eine semantische Schicht kostet – und wann Sie darauf verzichten

Eine semantische Schicht ist eine Verhandlung über Definitionen, bevor sie ein technisches Artefakt ist, und die Verhandlung ist der teure Teil. Zwei Abteilungen, die „aktiver Kunde“ verschieden definieren, müssen innehalten, und jemand mit der nötigen Befugnis muss entscheiden. Die Modellierung dauert eine Woche; die Einigung kann ein Quartal dauern. Danach driften die Definitionen, also ist jemand dauerhaft für sie zuständig. Eine Kennzahl, deren Bedeutung sich unbemerkt ändert, ist schlimmer als gar keine Kennzahl – aus demselben Grund, aus dem eine falsche Ontologie schlimmer ist als gar keine.

**Wann besser nicht:** ein Team, eine Handvoll Kennzahlen, keine Uneinigkeit zwischen Abteilungen über Definitionen. Dann ist die Schicht bloßer Formalismus, und ein gut dokumentierter Satz von Views tut es auch. Der Test ist konkret: *Haben je zwei Personen für dieselbe Frage verschiedene Zahlen vorgelegt?* Wenn nicht, gibt es noch nichts in Einklang zu bringen, und Sie würden sich Steuerungsaufwand für einen Konflikt einhandeln, den Sie gar nicht haben.

## Vokabular, Graph oder semantische Schicht: was Sie wirklich brauchen \{#which-of-the-three-you-actually-need}

Die drei Abschnitte sind drei Antworten auf eine Frage: *Wo liegt die Struktur in Ihrem Wissen, und wer pflegt sie?*

- Erfindet Ihr Extraktor Bezeichnungen, brauchen Sie ein **kontrolliertes Vokabular**, und Sie brauchen es noch diese Woche.
- Zielen Ihre Fragen auf das Korpus als Ganzes und nicht auf irgendetwas darin, brauchen Sie einen **Graphen** – und jemanden, der für sein Schema zuständig ist, sonst brauchen Sie keins von beidem.
- Sind Ihre Fragen Rechenaufgaben und zwei Leute uneins über die Rechnung, brauchen Sie eine **semantische Schicht**, und der harte Teil ist die Uneinigkeit, nicht die Modellierung.
- Trifft nichts davon auf Sie zu, ist die Pipeline aus Ingestion, Retrieval und Generation die richtige Architektur, und der Umweg über die Struktur ist ein Kostenposten ohne Ertrag.

Ontologie, Graph und semantische Schicht teilen ein Fehlerbild: Jedes von ihnen versagt lautlos und plausibel. Eine falsche Ontologie validiert. Ein veralteter Graph liefert selbstsichere Beziehungen. Eine abgedriftete Kennzahl erscheint im Dashboard. Keines wirft einen Fehler. Jedes braucht eine namentlich zuständige Person und eine Prüfung, die den Fehler auffangen würde.

## Das Wichtigste

- Die Pipeline aus Teil I setzt voraus, dass die Antwort in irgendeiner Passage steht; drei Klassen von Fragen brechen diese Voraussetzung, und jede hat eine andere strukturelle Antwort.
- Kontrolliertes Vokabular, Taxonomie und Ontologie sind drei verschiedene Verpflichtungen – die meisten Wünsche nach einer Ontologie erfüllt ein kontrolliertes Vokabular, und der Test dafür, ob Sie weitergehen sollten, ist eine Abfrage zu benennen, die Sie heute nicht beantworten können.
- Ein JSON Schema samt Validator ist die ehrliche Voreinstellung; der formale Unterbau rechtfertigt seine Kosten bei der Ableitung, bei der Interoperabilität mit Standards und bei regulatorisch vorgegebener Konformität.
- Ein Domänenschema ist kein Antwortschema: andere Zuständigkeit, andere Änderungsrate – und wer beide gleichsetzt, legt die Definitionen seines Geschäfts in einen Prompt.
- Nicht mehrschrittige Fragen rechtfertigen einen Graphen – die beantwortet die Zerlegung längst –, sondern globale Fragen an das ganze Korpus, bei denen überhaupt kein Chunk die Antwort enthält.
- Der Aufbau ist ein Durchlauf des Sprachmodells über das ganze Korpus, er kann Kanten halluzinieren, und er veraltet – in der Praxis entscheidet aber, ob jemand für das Extraktionsschema zuständig ist.
- „Semantische Schicht“ bezeichnet sowohl eine Ebene für Kennzahlen über einem Warehouse als auch das Zurückführen einer Äußerung auf einen Begriff im Dialog; sagen Sie zuerst, welche Sie meinen.
- Gegen eine semantische Schicht wählt ein Modell eine definierte Kennzahl aus, statt eine Abfrage herzuleiten. Damit wird weniger entschieden, der Fehler wird sichtbar, und die Zugriffsrichtlinien greifen, bevor das Warehouse überhaupt angefragt wird.

**[Neue Begriffe](../../glossary.md#structured-knowledge)**: controlled vocabulary, taxonomy, ontology, RDF, OWL 2, SHACL, SPARQL, knowledge graph, GraphRAG, entity resolution, semantic layer, metrics layer, text-to-SQL.

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Extraktion, Schemata und die Abfrageseite](./deep-dive.md)** – wie ein Graph tatsächlich gebaut wird (die sechs Phasen der Indexierung, die Communitys des hierarchischen Leiden-Algorithmus und die vier Abfragemethoden), warum die Duplikaterkennung der Teil ist, der enttäuscht, wie Sie einen Graphen bewerten, wenn die Metriken des Retrievals dafür nichts hergeben, der formale Unterbau nach seinem Zweck erklärt, und welche Schwierigkeiten von Text-to-SQL eine semantische Schicht wegnimmt.

Siehe auch: woher die Chunks kommen – [Ingestion](../ingestion/index.md); die Routing-Maschinerie, die diese Lektion wiederverwendet – die [Vertiefung zum Retrieval](../retrieval/deep-dive.md); Mehrschrittigkeit ohne Graphen – [Agentic RAG](../../part-2-agents/agentic-rag/index.md).

:::
