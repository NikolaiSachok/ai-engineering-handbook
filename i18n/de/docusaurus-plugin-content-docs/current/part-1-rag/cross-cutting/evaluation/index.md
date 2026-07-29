---
title: "Evaluierung"
slug: /part-1-rag/cross-cutting/evaluation/
---

# Qualität messen statt raten

Mehrfach ist in diesem Teil die Auskunft „das misst eine Metrik“ gefallen – beim Chunking, beim Retrieval,
beim Reranking und bei **Faithfulness** (Quellentreue – wie treu die Antwort den herangezogenen Quellen
bleibt, ohne unbelegte Informationen hinzuzufügen). Die **Evaluierung** ist die Antwort auf das *Wie*. Sie
ist kein Randthema: Ohne sie stellen Sie die Pipeline blind ein – andere Chunk-Größe, anderer Prompt, anderer
Reranker, und hinterher „fühlt es sich besser an“. Eine Evaluierung macht aus dem „fühlt sich besser an“ eine
Zahl. Genau das trennt ein System im Produktivbetrieb von einer Vorführung, und genau danach wird im
Vorstellungsgespräch am hartnäckigsten gefragt.

## Das Grundprinzip: Retrieval und Generation getrennt messen

Die Aufschlüsselung der Fehlerbilder aus dem Überblick zu Teil I wird hier zum Arbeitsmittel. Die beiden Stufen
gehen auf verschiedene Weise kaputt und werden mit verschiedenen Hebeln repariert – deshalb müssen sie auch
getrennt gemessen werden.

| | **Retrieval-Metriken** – haben wir die richtigen Chunks gefunden? | **Generation-Metriken** – ist die Antwort gut, gemessen am gelieferten Kontext? |
|---|---|---|
| Was sie messen | Ob der benötigte Chunk in den Ergebnissen gelandet ist – und auf welchem Rang | Ob die Antwort auf dem Kontext ruht und die gestellte Frage wirklich beantwortet |
| Die wichtigsten | **Recall@K** (für RAG die zentrale Größe), Precision@K, MRR, nDCG | **Faithfulness**, **Answer-Relevance**, Korrektheit |

Warum Recall@K die zentrale Größe ist: Fehlt der benötigte Chunk in den Ergebnissen, kann die Generation die
Frage schlicht nicht richtig beantworten. Auf der ersten Stufe wiegt Recall schwerer als Precision – was dort
verloren geht, holt keine spätere Stufe zurück.

## Ohne Datensatz keine Evaluierung

Messen setzt eine Referenz voraus: Fragen, dazu entweder die passenden Chunks oder die richtige Antwort. Das
ist der **Goldstandard** (golden set) – der handgeprüfte Referenzdatensatz. Sie bauen ihn von Hand oder
synthetisch: Ein LLM erzeugt aus dem Korpus Frage-Antwort-Paare, ein Mensch liest sie gegen. Ein kleiner,
sauberer Datensatz schlägt einen großen, verrauschten. Genau hier sparen Teams am häufigsten – und ohne
Referenz bricht die ganze Evaluierung in sich zusammen.

## LLM-as-a-judge: frei formulierten Text bewerten

Antworten sind frei formulierter Text; mit einem exakten Abgleich kommen Sie da nicht weit. Für die Qualität
der Generation – Faithfulness und Answer-Relevance – ziehen Sie deshalb **ein zweites Modell als Judge** heran
(LLM-as-a-judge: ein Modell bewertet die Ausgabe eines anderen). Es bewertet die Antwort anhand eines
**Bewertungsrasters** oder vergleicht sie mit einer Referenz und vergibt einen Score. Der Kniff skaliert
menschliches Urteilsvermögen auf Tausende von Beispielen – eines der wichtigsten Verfahren der
Generation-Evaluierung und eine Standardfrage im Vorstellungsgespräch.

:::tip[▶ Video]

<YouTube id="trfUBIDeI1Y" title="LLM as a Judge: Scaling AI Evaluation Strategies — IBM Technology" />

Wie ein LLM-Judge eine Antwort bewertet. (Das Video ist auf Englisch.)

:::

Ein Judge ist nicht neutral, und Sie sollten wissen, nach welcher Seite er kippt: Da ist der **Positionsbias** – von zwei
Antworten bevorzugt er die erste; da ist der **Ausführlichkeitsbias** (Verbosity Bias) – länger liest sich
als besser; und da ist die Neigung, **Antworten im eigenen Stil** höher zu bewerten (Self-Preference).
Daraus folgen zwei Regeln: Geben Sie ihm ein klares Bewertungsraster vor, und kalibrieren Sie ihn **anhand
menschlicher Labels**, bevor Sie ihm trauen.

:::tip[▶ Video]

<YouTube id="dAE7OFm9oek" title="Can You Trust an AI to Judge Fairly? Exploring LLM Biases — IBM Technology" />

Die Bias-Formen eines Judges – und wie weit Sie ihm trauen dürfen. (Das Video ist auf Englisch.)

:::

## Offline und online – zwei Schleifen

- **Offline:** Sie schicken den Goldstandard vor der Bereitstellung durch die Pipeline, in der CI. Das sind
  die Unit-Tests eines RAG-Systems – sie fangen eine **Regression** (eine durch eine Änderung verursachte
  Verschlechterung) ab, bevor sie ausgeliefert wird: „X verbessert, dabei stillschweigend Y kaputtgemacht“.
- **Online:** Sie messen im Produktivbetrieb – **Nutzerfeedback** (Daumen hoch, Daumen runter), implizite
  Signale, A/B-Tests. Echte Fragen bringen ans Licht, woran der Goldstandard nicht gedacht hat.

## Die Evaluierung treibt die Entwicklung

Daraus entsteht die Schleife, die die Pipeline überhaupt erst einstellbar macht: etwas ändern → Evaluierung
laufen lassen → Metriken vergleichen → behalten oder verwerfen. Damit schließen sich alle früheren Stellen,
an denen es „hier wird gemessen“ hieß, zu einem Vorgang zusammen – im Englischen heißt dieser Zuschnitt
*eval-driven development*. Und weil die CI dabei auf Regressionen prüft, geht eine Verbesserung an der einen
Stelle nicht auf Kosten einer anderen.

## Metriken zeigen, wo Sie ansetzen müssen

Der praktische Hauptnutzen: Die Evaluierung zeigt, auf welcher Stufe der Fehler sitzt.

| Symptom | Diagnose | Wo Sie ansetzen |
|---|---|---|
| Antwort falsch, der benötigte Chunk war **nicht** in den Ergebnissen | Fehlerbild des Retrievals → Recall@K zu niedrig | Chunking / hybride Suche / Reranking |
| Antwort falsch, der benötigte Chunk stand aber **im Kontext** | Fehlerbild der Generation → Faithfulness zu niedrig | Grounding (Rückbindung der Antwort an den Kontext) / Prompt |

## Das Wichtigste

- Eine Evaluierung macht aus „fühlt sich besser an“ eine Zahl; erst dadurch wird die Pipeline einstellbar,
  und erst dadurch unterscheidet sich ein System im Produktivbetrieb von einer bloßen Vorführung.
- Retrieval und Generation werden getrennt gemessen – sie gehen auf verschiedene Weise kaputt.
- Retrieval: Recall@K als zentrale Größe, dazu Precision@K, MRR und nDCG. Generation: Faithfulness,
  Answer-Relevance, Korrektheit.
- Ohne Goldstandard geht nichts – Frage plus passende Chunks oder richtige Antwort; sauber schlägt groß.
- Ein Judge bewertet frei formulierten Text anhand eines Bewertungsrasters. Rechnen Sie mit seinen
  Bias-Formen und kalibrieren Sie ihn anhand menschlicher Labels.
- Offline fängt die CI Regressionen ab; online liefern Nutzerfeedback und A/B-Tests das, was der
  Goldstandard nicht abgedeckt hat.
- Die Metriken sagen Ihnen, auf welcher Stufe Sie ansetzen müssen.

**[Neue Begriffe](../../../glossary.md#evaluation)**: evaluation, golden set / golden dataset / ground truth, answer relevance,
correctness, LLM-as-a-judge, judge bias, offline vs online eval, regression eval, A/B testing.

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Innenleben der Metriken und Judge-Kalibrierung](./deep-dive.md)** – der zweite Durchgang durch die
Evaluierungsschicht: wie die Metriken im Ragas-Stil tatsächlich berechnet werden (Faithfulness,
Answer-Relevance, Context-Precision und Context-Recall), wie ein LLM-Judge anhand menschlicher Labels
kalibriert wird und woher seine Bias-Formen kommen (Position, Ausführlichkeit, Self-Preference; Pointwise
gegen Pairwise), und wie ein Goldstandard von Hand entsteht – Übereinstimmung zwischen den Annotatoren und
Active Sampling.

Siehe auch: die Schichten, die die Evaluierung misst – [Retrieval](../../retrieval/index.md) und
[Generation](../../generation/index.md); und die benachbarten Querschnittsthemen –
[Guardrails](../guardrails/index.md) und [Observability](../observability/index.md).

:::
