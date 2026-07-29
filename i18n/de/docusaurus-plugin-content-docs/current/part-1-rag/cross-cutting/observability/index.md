---
title: Observability
slug: /part-1-rag/cross-cutting/observability/
---

# Dem System im Produktivbetrieb bei der Arbeit zusehen

Die Evaluierung sagt Ihnen, ob das System gut ist – offline, auf einem Datensatz. Die **Guardrails**
(Leitplanken – Schutzregeln um das Modell) sorgen dafür, dass es sicher bleibt. **Die Observability** – auf
Deutsch die Beobachtbarkeit – zeigt, was das System im Produktivbetrieb an echten Anfragen tatsächlich tut.
Ohne sie bleiben die Probleme des Produktivbetriebs unsichtbar: Sie wissen nicht, *warum* eine bestimmte
Antwort schlecht ausgefallen ist, was aus der Vektordatenbank geholt wurde, was sie gekostet hat und wie lange
sie gebraucht hat.

## Was Sie schon kennen – und was an KI-Systemen neu ist

Die drei Säulen der Observability – **Traces, Metriken, Logs** – kennen Sie aus der gewöhnlichen
Softwareentwicklung bereits. In dieser Lektion geht es um den Unterschied: Was ändert sich, wenn Sie statt
eines gewöhnlichen Dienstes ein LLM- oder RAG-System beobachten?

## Warum ein LLM-System schwerer zu beobachten ist

Zwei Dinge kommen zusammen: Das System antwortet nicht deterministisch, und das Modell ist eine Blackbox. Eine
schlechte Antwort aus dem Produktivbetrieb lässt sich ohne die vollständige Aufzeichnung nicht nachstellen,
und dazu gehört alles: wie die Abfrage lautete – auch in ihrer umformulierten Fassung –, welche Chunks
zurückkamen und mit welchem Score, welcher Prompt an das Modell ging, was es zurückgab, welche Tools der
Agent aufrief. Gewöhnliche Software ist deterministisch, dort gibt es einen Stacktrace. Eine LLM-Anwendung
braucht die Aufzeichnung des **gesamten Wegs, auf dem die Antwort zustande kam**.

## Der Trace durch die Pipeline – der zentrale Baustein

Ein **Trace** ist genau diese Aufzeichnung: eine einzelne Anfrage, vollständig festgehalten auf ihrem Weg
durch die Pipeline. Abfrage → umformulierte Abfrage → Chunks samt Score → Reranking → der abgeschickte
Prompt → die Ausgabe des Modells → bei einem Agenten zusätzlich jeder Schritt und jeder Tool-Call. Jeder
dieser Schritte ist ein **Span**. Damit beantwortet der Trace die Frage, um die sich jede Fehlersuche dreht:
Warum ist aus genau dieser Abfrage genau diese Antwort geworden?

## Was Sie protokollieren – die RAG-Besonderheiten

- **Die abgerufenen Chunks und ihre Scores** – war der richtige dabei? Das hängt unmittelbar an der
  Retrieval-Evaluierung.
- **Der endgültige Prompt** – das, was das Modell tatsächlich gesehen hat.
- **Die rohe Ausgabe des Modells**, dazu die Nachverarbeitung.
- Bei Agenten **der vollständige Trace aus Schritten und Tool-Calls**.
- Pro Schritt: Latenz, Zahl der Token, Kosten, Modellversion.

## Kosten und Latenz sind keine Nebensache

Anders als bei einer gewöhnlichen Anwendung kostet hier jede Anfrage Geld – in Token –, und die Aufrufe des
Modells sind langsam. Die Observability muss deshalb den Preis pro Anfrage und die Latenz pro Schritt
ausweisen, vor allem für Generation und Reranking. Erst dann fallen die Anfragen auf, die teuer oder langsam
sind, und Sie können gegensteuern: ein Cache, ein günstigeres Modell, weniger Chunks im Prompt.

## Feedback: Die Observability liefert der Evaluierung neue Fälle

Traces aus dem Produktivbetrieb und das **Nutzerfeedback** werden zu neuen Fällen für die Evaluierung – und
zwar zu genau den schweren, an denen ein System in der Praxis scheitert. Fangen Sie eine schlechte Antwort im
Produktivbetrieb ab und nehmen Sie sie in den Goldstandard auf, dann wacht die Evaluierung von da an darüber,
dass sie nicht wiederkommt. Damit schließt sich der Kreis: Die Evaluierung misst, die Guardrails schützen, die
Observability sieht – und gibt zurück, was sie gesehen hat. Die drei Querschnittsthemen sind eine einzige
Schleife.

*(Die Werkzeuge – [LangSmith](https://www.langchain.com/langsmith), [Langfuse](https://langfuse.com), [Arize
Phoenix](https://arize.com/phoenix), [OpenTelemetry](https://opentelemetry.io) – sind eine eigene Schicht; sie
stehen in der [Lektion zum Tooling-Ökosystem](../../../part-3-production/tooling-ecosystem/index.md). Hier
geht es um das Prinzip.)*

---

Damit endet nicht nur die Lektion, sondern **Teil I**. Sein Gerüst steht jetzt: Eine schlechte Antwort
zerfällt in das Fehlerbild des Retrievals oder das Fehlerbild der Generation; die Pipeline entsteht Schicht für
Schicht – Ingestion, Retrieval, Generation –; und die Querschnittsthemen halten sie messbar, sicher und
sichtbar. In [Teil II](../../../part-2-agents/overview.md) wird diese starre Pipeline lebendig: Von da an
entscheidet das Modell über den Ablauf – und alles, was Sie sich hier an Disziplin erarbeitet haben, nehmen
Sie mit.

## Das Wichtigste

- Observability heißt: sehen, was ein laufendes LLM-System tatsächlich tut. Sie brauchen sie, weil das System
  nicht deterministisch antwortet und sich eine schlechte Antwort ohne vollständige Aufzeichnung nicht
  untersuchen lässt.
- Der zentrale Baustein ist der Trace, der eine einzelne Anfrage von Anfang bis Ende festhält, zerlegt in
  Spans: die Abfrage → das Retrieval samt Score → der Prompt → die Ausgabe → die Schritte des Agenten.
- Protokollieren Sie die RAG-Besonderheiten: Chunks mit Scores, den endgültigen Prompt, die rohe Ausgabe sowie
  Latenz, Token und Kosten pro Schritt.
- Drei Säulen: Traces – für LLM-Systeme die wichtigste Säule –, Metriken (Latenz, Kosten, Qualität) und Logs.
- Kosten und Latenz kommen zuerst: Token sind Geld, und die Aufrufe sind langsam.
- Die Observability liefert der Evaluierung neue Fälle: Was im Produktivbetrieb danebengeht, landet im
  Goldstandard – und die nächste Änderung wird an genau diesem Fall gemessen, bevor sie ausgeliefert wird.

**[Neue Begriffe](../../../glossary.md#observability)**: observability, trace / span, RAG tracing, cost per
request / token accounting, latency (p50 / p95), three pillars (metrics / logs / traces), feedback loop
(observability → eval).

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Sampling, SLOs und Budgets](./deep-dive.md)** – der zweite Durchgang durch die Observability-Schicht:
Strategien für das Trace-Sampling (Head, Tail, Priority) und der Datenschutz in den Logs (PII, Aufbewahrung);
Qualitäts-Dashboards, SLOs für ein LLM-System und die Frage, worauf ein Alert überhaupt gehört; wie sich eine
Verschlechterung aus den Traces auf ihre Ursache zurückführen lässt; und die Zählung der Token pro Anfrage
mit p50- und p95-Latenz und Kostenbudgets.

Siehe auch: die benachbarten Querschnittsthemen – [Evaluierung](../evaluation/index.md) (die Traces der
Observability werden zu neuen Fällen für die Evaluierung) und [Guardrails](../guardrails/index.md); und, für
die Observability im laufenden Produktivbetrieb, [LLMOps](../../../part-3-production/llmops/index.md).

:::
