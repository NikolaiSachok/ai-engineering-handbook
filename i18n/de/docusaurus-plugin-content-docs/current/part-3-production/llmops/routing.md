---
title: Model-Routing – Kosten und Latenz der gesamten Anfrage
sidebar_label: Model-Routing
sidebar_position: 3
---

# Model-Routing – Kosten und Latenz der gesamten Anfrage

Wenn 70 % der Anfragen an ein kleines Modell gehen, sinken die Kosten deshalb noch nicht um 70 %.
Und wenn ein Modell schnell das erste Token erzeugt, kann eine nachgeschaltete Prüfung trotzdem die
für die erste sichtbare Ausgabe vorgesehene Zeit aufbrauchen. Beim
[Routing zwischen Modellen](./index.md#route-between-models) müssen Qualität, Kosten und Latenz
zusammenpassen. Entscheidend ist jeweils die gesamte Anfrage.

Alle Preise, Laufzeiten und Anteile auf dieser Seite sind frei gewählte Rechenbeispiele. Es handelt
sich weder um Anbieterpreise noch um Messwerte eines Produktivsystems.

## Vor der Generation das Modell wählen oder das Ergebnis prüfen \{#choose-before-generation-or-check-after-it}

Beginnen Sie mit Merkmalen, die Ihre Anwendung bereits kennt: der im Produkt gewählten Aktion,
der Zahl abgerufener Passagen, fehlenden Zitaten, widersprüchlichen Quellen oder dem Abstand zwischen
Retrieval-Scores. Nach dem Retrieval erfordern solche Merkmale keinen zusätzlichen Modellaufruf;
das Retrieval selbst verursacht weiterhin Kosten. Kalibrieren Sie einen Score-Abstand für den
konkreten Retriever und die jeweilige Verteilung der Anfragen. Zwei Passagen können einander
widersprechen, zwanzig können denselben Sachverhalt wiederholen. Ein Merkmal verrät nicht von selbst,
wie schwierig die Antwort für ein Modell sein wird.

Eine eigene Routing-Entscheidung sagt dagegen voraus, ob das günstige Modell die Anfrage ausreichend
gut beantworten wird. Dafür kommen Regeln, ein Klassifikator oder ein LLM infrage. Für ein gelerntes
Verfahren brauchen Sie repräsentative Labels und einen zurückgehaltenen Testsatz für das tatsächlich
eingesetzte Modellpaar und Ihre Arbeitslast. Ein Erfolg bei einem anderen Modellpaar oder anderen
Anfragen überträgt sich nicht automatisch. Die Kosten und die Laufzeit des Klassifikators gehören
zur Rechnung.

Bei der **vorab getroffenen Modellauswahl** entscheidet der Router, danach erzeugt eines der Modelle
die Antwort. Eine **Modellkaskade** (*model cascade*) beginnt dagegen mit dem günstigen Modell und
prüft dessen Ausgabe. Fällt sie durch die Qualitätsprüfung, erzeugt ein stärkeres Modell eine neue
Antwort. Die **Eskalationsrate** (*escalation rate*) `r` ist der Anteil der in diese Kaskade eintretenden
Anfragen, die die nächste Modellstufe aufrufen. Anfragen, die die Kaskade umgehen, gehören nicht in
diesen Nenner. Ein Fallback wegen eines Ausfalls oder eines Rate Limits ist etwas anderes: Er
reagiert auf die Verfügbarkeit, die Eskalation hier auf ein Qualitätssignal.

| Verfahren | Wofür Sie zahlen | Folge einer Fehlentscheidung |
|---|---|---|
| Vorab getroffene Auswahl | Router und Antwortgenerierung durch das ausgewählte Modell | Eine schwache Antwort kann ohne zusätzliche Prüfung oder Stichprobenkontrolle unbemerkt bleiben. |
| Modellkaskade | Immer Antwortgenerierung durch das günstige Modell und Prüfung; bei Eskalation zusätzlich Antwortgenerierung durch das stärkere Modell | Eine erkannte schwache Antwort lässt sich ersetzen, sofern bis zur Frist noch Zeit bleibt. |

Keines der Verfahren garantiert eine richtige Antwort. Eine Prüfinstanz, hier **Verifier** genannt,
kann schlechte Antworten akzeptieren und gute verwerfen. Auch das stärkere Modell kann denselben
Fehler machen; fehlende Belege im Retrieval ersetzen beide nicht. Ein gültiges Schema oder ein
vorhandenes Zitat zeigt noch nicht, dass die Quelle die Aussage stützt. Kalibrieren Sie die Prüfung
mit von Menschen bewerteten Fällen und kontrollieren Sie Stichproben sowohl der akzeptierten als
auch der verworfenen Antworten. Die [Vertiefung zur Evaluierung](../../part-1-rag/cross-cutting/evaluation/deep-dive.md)
beschreibt die methodischen Grundlagen.

Eine erkannte Fehlentscheidung lässt sich nur vor der sichtbaren Freigabe der Antwort oder einer
unumkehrbaren externen Aktion vollständig abfangen. Soll der Austausch der Antwort unsichtbar bleiben,
müssen Sie die Ausgabe bis zum Ende der Prüfung puffern. Beschränken Sie die Kaskade auf Antworten,
oder verlangen Sie vor Aktionen mit Nebenwirkungen eine Freigabe. Auch eine vorab getroffene
Modellauswahl kann Prüfungen und Korrekturwege vorsehen; die Sichtbarkeit von Fehlern hängt von diesen
Maßnahmen ab.

## Anfrageanteile und Kosten getrennt berechnen \{#compute-request-mix-and-spend-separately}

Vergleichen Sie dieselbe Arbeitslast einmal mit Routing und einmal ausschließlich mit dem starken
Modell. Die Anfragen dürfen je nach Klasse unterschiedlich lang sein. Für 100 Anfragen nehmen wir
folgende hypothetischen Kosten in Dollar an:

| Anfrageklasse | Anzahl | Gewähltes Modell: je Anfrage ($) | Nur starkes Modell: je Anfrage ($) | Gewähltes Modell: gesamt ($) | Nur starkes Modell: gesamt ($) |
|---|---:|---:|---:|---:|---:|
| Nachschlagen | 70 | 0,001 | 0,010 | 0,070 | 0,700 |
| Synthese | 25 | 0,006 | 0,020 | 0,150 | 0,500 |
| Lange Texte verfassen | 5 | 0,050 | 0,050 | 0,250 | 0,250 |
| Gesamt | 100 | – | – | 0,470 | 1,450 |

Die Ersparnis beträgt `(1.450 − 0.470) / 1.450`, also rund 67,6 %. Die Nachschlageanfragen machen
70 % der Anfragen aus, aber nur `0.070 / 0.470`, also rund 14,9 % der Kosten mit Routing. Die beiden
Anteile haben unterschiedliche Nenner. Kostet ein zusätzlicher Klassifikator 0,001 $ je Anfrage,
kommen für die 100 Anfragen 0,100 $ hinzu. Die Gesamtkosten steigen auf 0,570 $, die Ersparnis sinkt
auf rund 60,7 %.

Für eine Kaskade seien `Cs` die festen Kosten der Antwortgenerierung durch das kleine Modell, `Cv` die der Prüfung und `Cl`
die zusätzlichen Kosten der Antwortgenerierung durch das große Modell. Dann gilt je Anfrage, die in die Kaskade eintritt:

`E[C] = Cs + Cv + r × Cl`

Bei `Cs = 0.002`, `Cv = 0.001`, `Cl = 0.010` und `r = 0.20` ergibt sich `E[C] = 0.005`: halb so viel
wie die Antwortgenerierung durch das starke Modell allein. Kostengleichheit erreichen die beiden Varianten bei
`r = (Cl − Cs − Cv) / Cl = 0.70`. Steigt `r` auf 80 %, kostet die Kaskade 0,011 $ und damit mehr als
das starke Modell allein. Bei einer Eskalation bezahlen Sie beide Generationen; daraus folgt jedoch
kein fester Faktor zwei.

Diese Rechnung setzt feste Kosten pro Stufe voraus. Sind gerade die eskalierten Anfragen länger,
brauchen Sie für `Cl` den mittleren Preis des Aufrufs des großen Modells *unter dieser Bedingung*. Rechnen Sie
Router, Wiederholungen, erneut übertragenen Kontext, zusätzliche Prüfungen und Tools hinzu, soweit
Sie diese einsetzen. Anfragen, die die Kaskade umgehen, gehen mit ihrem eigenen Kostenanteil in die
Gesamtrechnung ein. Vergleichen Sie immer dieselbe Arbeitslast bei der geforderten Qualität.
Günstigere falsche Antworten belegen keine brauchbare Ersparnis.

## Ein zweiter Durchlauf verändert das Perzentil \{#a-two-pass-path-changes-the-percentile}

Die TTFT des Anbieters endet beim ersten von ihm erzeugten Token. Die für Nutzende sichtbare TTFT
endet erst beim ersten freigegebenen Token; dazu zählen Retrieval, Routing, Wartezeiten in Queues
und blockierende Prüfungen. Die Zeit bis zur vollständigen Antwort ist eine weitere Messgröße.
Gepufferte Ausgaben können eine gute Anbieter-TTFT vollständig verdecken. Die
[Lektion zur Bereitstellung](../serving/index.md) ordnet diese Messgrenzen ein.

Messen Sie bei einer seriellen Kaskade mit gepufferter Ausgabe zunächst die gesamte Dauer jeder
Anfrage. Eine akzeptierte Antwort erfordert die Antwortgenerierung durch das kleine Modell und die Prüfung. Eine eskalierte
Anfrage erfordert zusätzlich die Antwortgenerierung durch das große Modell und alle abschließenden blockierenden Prüfungen.
Erst über diese Gesamtdauern berechnen Sie das Perzentil. Die p95-Werte einzelner Stufen dürfen Sie
nicht einfach addieren: Sie können von unterschiedlichen Anfragen stammen; Abhängigkeiten und die
Auswahl der eskalierten Anfragen verändern die Verteilung.

Nehmen wir 100 Anfragen an: Die Antwortgenerierung durch das kleine Modell dauert immer 450 ms, die Prüfung 100 ms. Die
zusätzliche Antwortgenerierung durch das große Modell einschließlich abschließender Prüfung dauert 1200 ms. Alle übrigen
Zeitanteile setzen wir für dieses Beispiel auf null. Akzeptierte Antworten werden nach 550 ms
freigegeben, eskalierte nach 1750 ms. Für p95 verwenden wir die Nearest-Rank-Konvention: Nach dem
Sortieren der 100 Dauern zählt der 95. Wert.

| Eskalationsrate | Anfragen mit 550 ms | Anfragen mit 1750 ms | p95 | Innerhalb von 800 ms |
|---|---:|---:|---:|---:|
| 4 % | 96 | 4 | 550 ms | 96 % |
| 5 % | 95 | 5 | 550 ms | 95 % |
| 6 % | 94 | 6 | 1750 ms | 94 % |

In dieser vollständig getrennten Verteilung liegt p95 auf dem langsamen Pfad, sobald dessen Anteil
über 5 % steigt. Bei genau 5 % bleibt der 95. Wert noch auf dem schnellen Pfad. Eine interpolierte
Perzentilberechnung oder ein anderes Messfenster kann diese Grenze verschieben. Und selbst bei 4 %
warten die eskalierten Anfragen weiterhin 1750 ms: p95 garantiert keiner einzelnen Anfrage eine
bestimmte Antwortzeit.

Allgemeiner sei `Fa(t)` die bedingte Verteilungsfunktion der Gesamtdauer akzeptierter Anfragen und
`Fe(t)` die der eskalierten Anfragen, jeweils einschließlich ihres vollständigen seriellen Pfads.
Dann lautet die Verteilungsfunktion der Mischung:

`F(t) = (1 − r) × Fa(t) + r × Fe(t)`

Ein Ziel von 95 % innerhalb der Frist ist genau dann erfüllt, wenn `F(deadline) ≥ 0.95` gilt. Dafür
müssen die beiden Pfade nicht unabhängig sein. Überlappen ihre Laufzeiten oder haben bereits einige
akzeptierte Anfragen hohe Latenzen, sind 5 % Eskalation keine allgemeine sichere Obergrenze. Messen
Sie vollständige Traces unter Last: Gemeinsame Queues und Backpressure können bei steigender
Eskalationsrate auch die akzeptierten Anfragen verlangsamen. Die
[Vertiefung zur Observability](../../part-1-rag/cross-cutting/observability/deep-dive.md) behandelt die
Messung; die [Vertiefung zur Bereitstellung](../serving/deep-dive.md) behandelt den Betrieb unter Last.

Eine mögliche Aufteilung ist eine synchrone Prüfung auf der schnellen Stufe, sofern sich bei der gemessenen
Dauer das Latenzziel einhalten lässt, und eine asynchrone Stichprobenkontrolle auf der langsamen Stufe,
sofern das verbleibende Risiko bereits ausgelieferter Fehler akzeptabel ist. Eine asynchrone
Kontrolle kann eine schon ausgelieferte falsche Antwort nicht mehr zurückhalten. Vorgeschriebene
Sicherheitsprüfungen vor der Freigabe bleiben bestehen. Lässt sich die erforderliche Qualität bis zur
Frist nicht feststellen, muss das System auf eine Antwort verzichten oder die Bearbeitung
aufschieben. Ein späterer Dashboard-Befund erfüllt keine Anforderung an die Richtigkeit vor der Freigabe.

## Das gesamte Routing-Verfahren betreiben \{#operate-the-policy-not-just-the-threshold}

Ein strengerer Schwellenwert des Verifiers kann die Eskalationsrate erhöhen und mehr Fehler abfangen.
Ob dadurch die Qualität steigt, müssen Sie messen. Verfolgen Sie je Arbeitslast und Modellstufe die
Eskalationsrate, Fehler in akzeptierten Antworten, fälschliches Akzeptieren und Verwerfen durch den
Verifier, die endgültige Antwortqualität, die Kosten pro erfolgreicher Anfrage sowie die sichtbare
TTFT und die Zeit bis zur vollständigen Antwort.

Steigt die Eskalationsrate, untersuchen Sie Änderungen der Eingaben, des Retrievals, des Verifiers
und des kleinen Modells. Lockern Sie den Schwellenwert nicht allein deshalb, weil die Rechnung
wächst. Überprüfungen folgen neuen Befunden und geänderten Abhängigkeiten; ein allgemeines
vierteljährliches Ablaufdatum für eine Routing-Regel gibt es nicht.

Versionieren Sie die Konfiguration und laden Sie Änderungen ohne Neustart nach. Dazu gehören die
Zulässigkeit der Modellstufen, Regeln je Arbeitslast, Schwellenwerte, Fristen, Ausgabenobergrenzen
und das Verhalten bei einem Timeout der Prüfung. Validieren Sie die Konfiguration vor der atomaren
Übernahme. Jeder Trace hält Version und Entscheidungsgrund fest. Prüfen Sie Änderungen mit
zurückgehaltenen Testfällen und einem Canary Release mit Qualitätsmessung im laufenden Betrieb;
halten Sie die vorherige Konfiguration für einen Rollback bereit.

Jede Modellstufe braucht einen Abschalter mit festgelegten Folgen. Ist das kleine Modell deaktiviert,
entfallen die Antwortgenerierung durch dieses Modell und die anschließende Prüfung. Ist das starke Modell deaktiviert, muss ausdrücklich
feststehen, ob das System auf eine Antwort verzichtet, die Anfrage aufschiebt oder einen anderen
zulässigen Weg wählt. Auch für den Ausfall des Verifiers brauchen Sie eine explizite sichere
Reaktion. Begrenzen Sie Versuche und Gesamtdauer, damit keine endlose Eskalation entsteht.
Eine Umleitung verändert Kapazitätsbedarf und Kosten am Ziel; prüfen Sie beides, bevor Sie den
Verkehr verschieben. Der eingeschränkte Betrieb muss innerhalb bekannter Grenzen bleiben.

## Das Wichtigste \{#what-to-take-away}

- Nutzen Sie zunächst vorhandene Merkmale. Prüfen Sie anschließend anhand repräsentativer Fälle, ob
  eine eigene Vorhersage der Eignung des günstigen Modells tragfähig ist.
- Berücksichtigen Sie die Kosten jeder Antwortgenerierung und jeder Prüfung. Der Anteil einer Modellstufe an den Anfragen ist
  nicht ihr Anteil an den Kosten.
- Berechnen Sie Perzentile über vollständige Anfragen. Die Eskalationsrate allein belegt nicht,
  dass das Latenzziel eingehalten wird.
- Erkannte Fehler lassen sich vor der Freigabe oder einer unumkehrbaren Aktion abfangen. Kontrollieren
  Sie auch akzeptierte Antworten. Legen Sie zulässige Ausweichpfade für den eingeschränkten Betrieb fest
  und begrenzen Sie die Zahl der Versuche sowie die gesamte Bearbeitungszeit.

**[Neue Begriffe](../../glossary.md#llmops)**: Modellkaskade (*model cascade*), Eskalationsrate (*escalation rate*).

Weiterführend: [Routing zwischen Modellen](./index.md#route-between-models) und
[Vertiefung zur Evaluierung](../../part-1-rag/cross-cutting/evaluation/deep-dive.md).
