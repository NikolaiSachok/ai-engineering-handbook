---
id: overview
title: Teil I – RAG
sidebar_label: Überblick
---

# Teil I – RAG

RAG (Retrieval-Augmented Generation) lässt ein Sprachmodell aus **Ihren** Dokumenten antworten statt aus
dem, was es sich im Training gemerkt hat. Bevor es eine Antwort erzeugt, sucht das System die passenden
Stellen in Ihren Daten heraus und gibt sie dem Modell als Kontext mit. Teil I behandelt diesen Weg als
**statische Pipeline**: eine feste Schrittfolge, für jede Frage dieselbe.

Durch den ganzen Teil zieht sich ein diagnostisches Prinzip: Bestimmen Sie die Ursache, bevor Sie den
Fehler beheben. Eine schlechte Antwort hat eine von zwei Ursachen. **Das Fehlerbild des Retrievals** liegt
vor, wenn die Stelle, die Sie brauchten, gar nicht erst in den Ergebnissen gelandet ist. **Das Fehlerbild
der Generation** liegt vor, wenn diese Stelle zwar abgerufen wurde, das Modell sie aber übergangen oder
verstümmelt hat. Fast jede Entscheidung in der Pipeline zielt auf eines dieser beiden Fehlerbilder, und der erste
Schritt ist immer derselbe: feststellen, welches der beiden vorliegt.

## Was Sie hier finden

- **[Ingestion](./ingestion/index.md)** – die Aufbereitung der Dokumente im Voraus: Chunking, Embeddings und Metadaten. Hier entscheidet sich, wie gut die Suche überhaupt werden kann.
- **[Retrieval](./retrieval/index.md)** – wie aus den nächstgelegenen Vektoren wirklich relevante Treffer
  werden: die Frage umformulieren, hybride Suche, Reranking, Filter und Zugriffssteuerung.
- **[Generation](./generation/index.md)** – wie die Antwort an den abgerufenen Kontext zurückgebunden wird:
  Grounding, Quellenangaben, eine ehrliche Antwortverweigerung statt einer Erfindung.
- **Querschnittsthemen** – was sich keinem einzelnen Schritt zuordnen lässt:
  [Evaluierung](./cross-cutting/evaluation/index.md) (woran Sie erkennen, dass das System funktioniert),
  [Guardrails](./cross-cutting/guardrails/index.md) (die Leitplanken, die es absichern),
  [Observability](./cross-cutting/observability/index.md) (woran Sie sehen, was es im Produktivbetrieb
  tut).

## Voraussetzungen

Sie sollten mit Sprachmodellen allgemein vertraut sein und in groben Zügen wissen, was ein Prompt, ein
Kontext und ein Embedding sind. Vertiefte Mathematik brauchen Sie nicht – wir erklären von Grund auf.

:::note[Bearbeitungsstand]

Teil I liegt in seiner Grundfassung vollständig vor – jede Lektion ist veröffentlicht: Ingestion,
Retrieval, Generation und die Querschnittsthemen (Evaluierung, Guardrails, Observability). 🚧 Ein zweiter
Durchgang steht noch aus, der jede Schicht vertieft; die Themen dafür stehen auf den Lektionsseiten unter
„Als Nächstes: Teil 2 der Lektion“.

:::
