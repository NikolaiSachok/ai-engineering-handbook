---
title: Retrieval
slug: /part-1-rag/retrieval/
---

# Den passenden Kontext zur Frage finden

Nach der Ingestion liegen die Chunks bereits in einer Vektordatenbank. Die naive Fassung des Retrievals geht so: die Frage einbetten und die K nächsten Vektoren nach der Kosinus-Ähnlichkeit zurückgeben. Das ist ein Anfang, keine fertige Lösung. Aufgabe der Retrieval-Schicht ist es, aus „den nächstgelegenen Vektoren“ Ergebnisse zu machen, die wirklich zur Sache gehören, richtig geordnet sind und nichts enthalten, was die fragende Person nicht sehen darf.

Behalten Sie den Rahmen aus dem Überblick zu Teil I: **Das Fehlerbild des Retrievals** liegt vor, wenn der benötigte Chunk unter den zurückgegebenen Treffern gar nicht vorkommt. Die ganze Schicht läuft darauf hinaus, diesen Fall seltener zu machen.

:::tip[▶ Video]

<YouTube id="T-D1OfcDW1M" title="What is Retrieval-Augmented Generation (RAG)? — IBM Technology" />

Der große Bogen: wie die Suche den Kontext in die Generation einspeist. (Das Video ist auf Englisch.)

:::

## Warum die naive Vektorsuche über top-K nicht reicht

Bei echten Fragen zeigt das naive Schema „die K nächsten Vektoren“ gleich mehrere Schwächen auf einmal.

Das **Dense Retrieval** (die dichte Vektorsuche) erfasst die Bedeutung, verfehlt aber exakte Token: Fehlercodes, Teilenummern, Namen, Abkürzungen. Zur Frage „Fehler X-42“ fördert es den richtigen Chunk unter Umständen nie zutage, während eine Suche nach dem exakten Wort ihn sofort findet. Dazu kommt, dass die Wörter der Frage nicht die Wörter des Dokuments sind – und dass von Zugriffsrechten in diesem Schema überhaupt keine Rede ist. Auf die naive Suche gehören deshalb mehrere Schichten.

Es sind vier: die Frage umformulieren, die blinden Flecken der Suche ausgleichen, die Reihenfolge korrigieren und den Suchraum auf das begrenzen, was zulässig ist.

## Die Frage umformulieren, bevor gesucht wird

Die Frage, die jemand eintippt, ist selten die beste Frage, mit der sich suchen lässt. Ein paar günstige Aufrufe an das Sprachmodell – von hier an kurz **LLM** – *vor* dem Retrieval sorgen dafür, dass der benötigte Chunk spürbar häufiger überhaupt gefunden wird. Diese Vorstufe heißt im Englischen **query transformation**, und sie hat drei gängige Formen.

- **Das Auflösen von Bezügen.** Was im Text nur „das“ oder „er“ heißt, bekommt seinen Namen zurück. Im Chat führt daran kein Weg vorbei: „und was kostet das?“ bedeutet ohne den Gesprächsverlauf nichts – Sie formulieren die Frage so um, dass sie für sich steht: „Was kostet Produkt X?“
- **Multi-Query.** Mehrere Umformulierungen derselben Frage erzeugen, mit jeder einzeln suchen, die Ergebnisse zusammenführen.
- **HyDE** (*hypothetical document embeddings*). Das Modell eine hypothetische Antwort skizzieren lassen, diese einbetten und damit suchen. Ein grob entworfener Antworttext liegt im Vektorraum oft näher am gesuchten Chunk als eine kurze Frage.

## Hybride Suche – Dense Retrieval plus Stichwortsuche

Hier liegt der mit Abstand größte Fortschritt gegenüber der naiven Suche. Am Werk sind zwei Mechanismen mit entgegengesetzten Stärken:

| | **Dense (Vektorsuche)** | **Sparse / Stichwortsuche (BM25)** |
|---|---|---|
| Was es erfasst | Bedeutung, Synonyme, Umschreibungen | exakte Wörter: Codes, Namen, Teilenummern, seltene Fachbegriffe |
| Wo es blind ist | exakte Token, die das Modell kaum gewichtet | Synonyme und Bedeutung – es zählt nur die wörtliche Übereinstimmung |

Die **hybride Suche** (*hybrid search*) lässt beide Verfahren laufen und führt ihre Scores zusammen – gewichtet oder über **Reciprocal Rank Fusion (RRF)**. Jedes Verfahren gleicht den blinden Fleck des anderen aus, und damit ist beantwortet, warum ein Vektor allein nicht reicht.

Nehmen Sie die Frage „Wie setze ich ein Passwort zurück?“ Das Dense Retrieval findet über die Bedeutung das Dokument „Zugang zum Konto wiederherstellen“; BM25 findet dagegen das Dokument, das wörtlich „Passwort zurücksetzen“ heißt. Zusammen liefern sie, was jedes für sich verfehlt hätte.

## Reranking korrigiert die Reihenfolge

Die erste Stufe – Dense Retrieval oder hybride Suche – ist auf **Recall** ausgelegt: Der benötigte Chunk soll irgendwo in die top-K geraten, wobei K bei 50 bis 100 liegt. Die Reihenfolge innerhalb dieser hundert ist allerdings grob, und in den Kontext des Modells passen nur wenige Chunks. Die zweite Stufe sorgt deshalb für **Precision**: Ein Cross-Encoder aus der [vorangegangenen Lektion](../ingestion/index.md) bewertet jeden **Kandidaten** (die Treffer der ersten Stufe) anhand der Frage neu und sortiert die Liste neu, sodass die besten nach oben steigen. Nur die wenigen besten gelangen in die Generation.

Das ist das kanonische zweistufige Schema: günstig und breit (ein Bi-Encoder oder die hybride Suche – Recall), danach teuer und genau (ein Cross-Encoder – Precision). An dieser Stelle fügen sich Bi- und Cross-Encoder aus der Lektion zur Ingestion zu einem Bild zusammen.

## Filter und Zugriffssteuerung – relevant und zugleich zulässig

Im Unternehmen beantwortet das Retrieval mehr als die Frage, ob etwas der Bedeutung nach ähnlich ist. Es beantwortet auch, was diese Person überhaupt sehen darf.

- **Nach Metadaten filtern** – nach den Feldern, die beim Chunking angehängt wurden: Datum, Abteilung, Dokumenttyp, Sprache. „Nur Personaldokumente nach 2024.“
- **Die Zugriffssteuerung (access control, ACL).** Die Berechtigungen greifen *vor* der Rückgabe, damit niemand einen Chunk erhält, auf den er keinen Zugriff hat (das Beispiel mit der Gehaltsliste aus der Lektion zur Ingestion). Das ist eine harte Anforderung: Ein System, das ein gesperrtes Dokument allein wegen seiner Relevanz herausgibt, hat einen Sicherheitsvorfall verursacht und nicht bloß einen Qualitätseinbruch. Üblich ist der Pre-Filter – erst anhand der Berechtigungen filtern, dann suchen.

## Die Pipeline im Ganzen

```text
Frage → [umformulieren] → [hybrid: dense + BM25, Filter: Metadaten + ACL]
      → Kandidaten (top-K) → [Reranking: Cross-Encoder] → die besten paar → in die Generation
```

Mit jeder Stufe versagt das Retrieval seltener. Wie viel die einzelne Stufe beiträgt, **messen** Sie: Recall@K, Precision@K, MRR, nDCG. Formal gefasst werden sie erst in der Schicht [Evaluierung](../cross-cutting/evaluation/index.md).

## Das Wichtigste

- Die naive Vektorsuche über top-K ist der Anfang, nicht das Ende.
- Die Frage selbst lässt sich vor der Suche umformulieren: Bezüge auflösen, Multi-Query, HyDE.
- Die hybride Suche aus Dense Retrieval und BM25 schließt die Kluft zwischen Bedeutung und exaktem Wort und bringt damit den mit Abstand größten Fortschritt.
- Das Reranking mit einem Cross-Encoder korrigiert die Reihenfolge: Die erste Stufe sorgt für Recall, die zweite für Precision.
- Filter und Zugriffssteuerung liefern Relevanz zusammen mit Berechtigung; die ACL ist eine Sicherheitsanforderung.

**[Neue Begriffe](../../glossary.md#retrieval)**: retrieval failure / generation failure, dense retrieval,
top-K, query transformation, multi-query, HyDE, hybrid search, BM25 / sparse retrieval, Reciprocal Rank
Fusion (RRF), reranking, two-stage retrieval, metadata filtering, access control (ACL), Recall@K, Precision@K,
nDCG, MRR.

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Zusammenführung, Ranking und Metriken](./deep-dive.md)** – der zweite Durchgang durch die Retrieval-Schicht: die Mechanik von HyDE und wann sie nach hinten losgeht, das Innere der Zusammenführung beider Ergebnislisten (Gewichtung bei RRF und Score-Normierung), die Wahl des Rerankers (Cross-Encoder gegen LLM), Parent-Document-Retrieval und Late Interaction (ColBERT), das Routing der Fragen, Pre- gegen Post-Filter und die Metriken des Rankings (nDCG, MRR) im Einzelnen.

Siehe auch: woher die Chunks kommen – [Ingestion](../ingestion/index.md); was mit dem geschieht, was Sie abrufen – [Generation](../generation/index.md); und wie die ganze Schicht gemessen wird – [Evaluierung](../cross-cutting/evaluation/index.md).

:::
