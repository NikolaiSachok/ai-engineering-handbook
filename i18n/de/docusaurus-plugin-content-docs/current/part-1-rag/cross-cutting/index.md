---
title: "Querschnittsthemen"
slug: /part-1-rag/cross-cutting/
---

# Was zu keiner einzelnen Stufe gehört

Ingestion, Retrieval und Generation haben ihren Platz in der Pipeline — den Moment, in dem sie
stattfinden. Drei Dinge haben diesen Platz nicht. Man kann nicht auf den Schritt zeigen, in dem ein
System verlässlich, sicher oder nachvollziehbar wird: Diese Eigenschaften stecken entweder in jeder
Stufe, oder sie fehlen überall. Genau deshalb sind es Querschnittsthemen und nicht eine vierte,
fünfte und sechste Stufe.

Es sind zugleich die drei, die eine Demo von einem Produktivsystem trennen. Darum stehen sie am Ende
von Teil I — und darum wird im Vorstellungsgespräch am hartnäckigsten danach gefragt.

## Was darin steckt

- **[Evaluierung](./evaluation/index.md)** — woran Sie erkennen, dass das System funktioniert,
  statt es zu glauben. Retrieval und Generation gehen auf verschiedene Weise kaputt und lassen sich
  mit verschiedenen Hebeln reparieren, also werden sie auch getrennt gemessen. Damit fängt man an:
  Ohne Zahl ist jede weitere Änderung an der Pipeline eine Vermutung, die sich besser anfühlt.
- **[Guardrails](./guardrails/index.md)** — wie Sie es sicher halten. Ein Modell kann Anweisung und
  Daten nicht zuverlässig auseinanderhalten; alles, was in den Kontext gerät, ist deshalb etwas, dem
  es folgen könnte. Guardrails sind genau die Schicht auf der Eingabe- und der Ausgabeseite, die
  davon ausgeht.
- **[Observability](./observability/index.md)** — wie Sie sehen, was das System tut, sobald echte
  Nutzer es haben. Traces, Spans und Sampling machen aus „die Qualität ist gefallen“ ein „sie ist
  *hier* gefallen, *seit diesem Zeitpunkt*, wegen *dieser* Änderung“ — und die fehlgeschlagenen
  Traces, die dabei auffallen, werden zu neuen Fällen für die Evaluierung.

Jedes der drei Themen ist eine Lektion plus **Deep Dive**: Die Lektion liefert das Arbeitsmodell, der
Deep Dive geht eine Ebene tiefer zu den Mechanismen und den Fehlerbildern. Der Hinweis „Weiter —
Teil 2 der Lektion“ steht am Fuß jeder Lektionsseite.

Die Reihenfolge ist kein Zufall. Die Evaluierung steht zuerst, weil Guardrails und Observability
Signale erzeugen, die ohne Vergleichsmaßstab wertlos sind. Die Observability steht zuletzt, weil sie
den Kreis schließt: Woran das System im Produktivbetrieb scheitert, wird zu dem, was die Evaluierung
als Nächstes prüft.
