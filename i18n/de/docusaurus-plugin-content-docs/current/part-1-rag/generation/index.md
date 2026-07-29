---
title: Generation
slug: /part-1-rag/generation/
---

# Aus dem Kontext eine belegte Antwort formulieren

Das Retrieval hat guten Kontext übergeben – freigegeben in dem Sinne, dass der Fragende ihn auch sehen darf. Jetzt folgt das **G** in RAG: Das Modell muss daraus eine Antwort formulieren – **aus genau diesem Kontext**. Erinnern Sie sich an den Rahmen aus dem Überblick zu Teil I: **Das Fehlerbild der Generation** liegt vor, wenn der Chunk, den Sie brauchten, *im* Kontext stand und die Antwort trotzdem falsch war. Das Modell hat ihn übergangen, verstümmelt oder mit einer eigenen Vermutung vermischt. In dieser Schicht geht es darum, genau das zu verhindern.

## Der Kern der Sache: aus dem Kontext antworten, nicht aus dem eigenen Wissen

Ein LLM trägt **das im Modell gespeicherte Wissen** (*parametric knowledge*) mit sich – alles, was es beim Training aufgenommen hat. Ohne eine ausdrückliche Einschränkung greift es bereitwillig auf das Wissen in seinen Gewichten zurück: möglicherweise veraltet, möglicherweise falsch und mit Sicherheit nicht aus Ihren Dokumenten. RAG will das Gegenteil und bindet das Modell an den Kontext, den Sie ihm liefern: aktuell, freigegeben, überprüfbar. Generation heißt in dieser Schicht also nicht, das Modell frei laufen zu lassen, sondern es an die Quellen gebunden zu halten.

:::tip[▶ Video]

<YouTube id="cfqtFvWOfg0" title="Why Large Language Models Hallucinate — IBM Technology" />

Warum ein Modell überhaupt anfängt, Dinge zu erfinden. (Das Video ist auf Englisch.)

:::

## Den Prompt bauen und den Kontext zusammenstellen

Wie Sie den Prompt zusammensetzen, ist die halbe Miete. Der Grundaufbau: ein System-Prompt, die abgerufenen Chunks – deutlich abgesetzt – und die eigentliche Frage. Das Zusammenstellen dieses Kontexts (*context packing*) geht an drei Stellen am häufigsten schief:

- **Den Kontext ausdrücklich abgrenzen.** Markieren Sie, wo die Quellen anfangen und wo sie aufhören, damit das Modell die Daten, aus denen es antworten soll, von den Anweisungen unterscheiden kann. Das ist zugleich die erste Verteidigungslinie gegen eine **Prompt-Injection** – mehr dazu in der Schicht Guardrails.
- **Die Reihenfolge: der Lost-in-the-Middle-Effekt.** Anfang und Ende eines langen Kontexts nimmt ein Modell besser wahr; was in der Mitte vergraben liegt, geht ihm verloren. Daraus folgt die Regel: Kippen Sie nicht 50 Chunks hinein, sondern übergeben Sie eine Handvoll der besten – dafür sorgt das Reranking – und legen Sie die wichtigsten an die Ränder.
- **Metadaten für die Quellenangaben.** Quelle und Abschnitt, beim Chunking angehängt, wandern mit in den Prompt – sonst hat die Antwort nichts, worauf sie verweisen könnte.

:::tip[▶ Video]

<YouTube id="1c9iyoVIwDs" title="4 Methods of Prompt Engineering — IBM Technology" />

Wie sich ein Prompt aufbauen lässt. (Das Video ist auf Englisch.)

:::

## Grounding-Anweisungen – der wichtigste Hebel gegen Halluzinationen

Der stärkste Hebel ist zugleich der einfachste: ausdrückliche Grenzen im Prompt. Eine **Grounding**-Anweisung (Rückbindung der Antwort an den Kontext) sagt dem Modell genau zwei Dinge: Es soll **ausschließlich** aus dem bereitgestellten Kontext antworten, und wenn die Antwort dort nicht steht, soll es das offen sagen, statt sie zu erfinden. Diese eine Anweisung senkt den Anteil der Halluzinationen spürbar, weil sie dem Modell die Erlaubnis nimmt, die Antwort aus dem eigenen Wissen aufzufüllen.

## Quellenangaben

Verlangen Sie vom Modell, zu jeder Einzelaussage anzugeben, aus welchem Chunk oder aus welcher Quelle sie stammt. Das zahlt sich doppelt aus. Erstens lässt sich die Antwort **nachprüfen**, und daraus entsteht Vertrauen. Zweitens erfindet das Modell selbst weniger: Eine Tatsache lässt sich schwerer erfinden, wenn direkt daneben eine Quelle stehen muss. Grundlage dafür sind die Metadaten, die beim Chunking angelegt wurden.

## Die Antwortverweigerung ist gewollt, keine Fehlfunktion

Das System muss „Ich weiß es nicht“ sagen dürfen – und es muss ausdrücklich dazu angewiesen werden. Eine selbstsicher formulierte falsche Antwort ist schlimmer als ein ehrliches „Das steht nicht in den Dokumenten“. Liefert das Retrieval keine Treffer, **verweigert das System die Antwort**, statt zu raten. Im Unternehmenseinsatz ist das eine Grundbedingung: Eine selbstsicher vorgetragene Antwort wird wie eine Tatsache behandelt, und ein einzelner Fehler pflanzt sich fort – bis in einen Bericht, bis in eine Entscheidung hinein.

## Faithfulness: Hier trifft die Generation auf die Messung

Auch mit Anweisungen setzt sich ein Modell gelegentlich mit seinem eigenen Wissen über den Kontext hinweg, oder es gerät ins Stolpern, wenn der Kontext dem widerspricht, was es *glaubt*. Wie weit die Antwort tatsächlich auf den Quellen ruht, lässt sich nicht erfühlen – es wird **gemessen**, mit der **Faithfulness**- bzw. **Groundedness**-Metrik (Quellentreue – wie treu die Antwort den herangezogenen Quellen bleibt, ohne unbelegte Informationen hinzuzufügen); im weiteren Verlauf steht dafür durchgehend **Faithfulness**. Genau festgelegt wird sie in der Schicht [Evaluierung](../cross-cutting/evaluation/index.md); halten Sie hier nur fest: „Das Modell verhält sich gut“ ist kein Gefühl, sondern eine Zahl.

## Das Fehlerbild der Generation beheben, Klasse für Klasse

| Fehlerklasse | Abhilfe |
|---|---|
| Der benötigte Chunk wurde übergangen | Weniger Rauschen (Reranking → wenige Chunks) plus eine Grounding-Anweisung |
| Eine Tatsache wurde erfunden | Grounding, Quellenangaben und eine erlaubte Antwortverweigerung |
| Was in der Mitte lag, ging verloren | Reihenfolge der Chunks, weniger Chunks |
| Die Antwort kam aus veraltetem Modellwissen | Harte Bindung an den Kontext, ausschließlich aus den Quellen |

## Das Wichtigste

- Generation in RAG heißt: eine Antwort **aus dem Kontext**, nicht aus dem im Modell gespeicherten Wissen.
- Beim Bau des Prompts: die Quellen ausdrücklich absetzen, den Lost-in-the-Middle-Effekt einkalkulieren, eine Handvoll der besten Chunks übergeben.
- **Grounding-Anweisungen** – nur aus dem Kontext, sonst ein offenes „Ich weiß es nicht“ – sind der wichtigste Hebel gegen Halluzinationen.
- **Quellenangaben** machen die Antwort überprüfbar und senken schon für sich genommen den Hang zur Erfindung.
- Die **Antwortverweigerung** ist normales Verhalten und keine Fehlfunktion.
- Die Treue zum Kontext wird **gemessen** – das ist die Brücke zur Evaluierung.

**[Neue Begriffe](../../glossary.md#generation)**: grounding, grounding instructions, context packing, lost-in-the-middle, citations / attribution, refusal / abstention, faithfulness / groundedness, parametric knowledge, hallucination.

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Selbstprüfung und strukturierte Ausgabe](./deep-dive.md)** – der zweite Durchgang durch diese Schicht: Schleifen zur Selbstprüfung (Chain-of-Verification, Self-Consistency), strukturierte Ausgabe sowie erzwungene und eingebettete Quellenangaben über Constrained Decoding, der Widerspruch zwischen abgerufenem Kontext und Modellwissen, das Zusammenstellen eines langen Kontexts jenseits von Lost-in-the-Middle und die Gestaltung der Antwort nach Format, Ton und Länge.

Siehe auch: was in diese Schicht hineingeht – [Retrieval](../retrieval/index.md); woher die Chunks kommen – [Ingestion](../ingestion/index.md); und wie die Quellentreue tatsächlich gemessen wird – [Evaluierung](../cross-cutting/evaluation/index.md).

:::
