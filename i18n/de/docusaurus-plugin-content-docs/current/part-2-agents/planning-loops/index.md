---
title: Planung und Schleifen
slug: /part-2-agents/planning-loops/
---

# Die Schleife auf das Ziel ausrichten – und dafür sorgen, dass sie endet

In [Agentic RAG](../agentic-rag/index.md) haben Sie die Schleife bekommen: `reason → decide → act → observe`,
und sie dreht sich, bis das Modell selbst entscheidet, dass es so weit ist. In [Tool-Einsatz](../tool-use/index.md)
kam dazu, dass jede Aktion in dieser Schleife ein Tool-Call ist – das Modell formuliert die Absicht, Ihr Code
setzt den Aufruf ab. Der Agent hat also Bewegungsfreiheit und einen Vorrat an Aktionen. Eine Frage blieb dabei
offen: Wie entscheidet der Agent bei einer Aufgabe über *viele* Schritte, in welcher Reihenfolge er sie abarbeitet –
und was bringt die Schleife dazu, **anzuhalten**? Um die Schicht, die die Schleife steuert und beendet, geht es
in dieser Lektion.

Die ganze Lektion in einem Satz: Agentic RAG hat dem Agenten eine Schleife gegeben; hier geht es darum, sie auf
das Ziel auszurichten und so zu begrenzen, dass sie tatsächlich endet.

:::tip[▶ Video]

<YouTube id="D37Ijn2o5U0" title="Why Agentic AI Fails: Infinite Loops, Planning Errors, and More — IBM Technology" />

Das Video nimmt die ganze Lektion von den Fehlern her: die konkreten Arten, auf die eine Schleife
schiefgeht – Endlosschleifen und Planungsfehler –, und warum erst die Freiheit, die Reihenfolge selbst zu
bestimmen, sie möglich macht.
(Das Video ist auf Englisch.)

:::

## Aufgabenzerlegung – vom Ziel zu den Schritten

**Die Aufgabenzerlegung** (task decomposition) bedeutet, das Ziel in Teilaufgaben zu zerlegen, die der Agent
einzeln abarbeiten kann. Eine echte Anfrage – „Diese beiden Berichte abgleichen und die Abweichungen
markieren“ – ist kein einzelner Tool-Call. Sie ist eine Folge: den ersten laden, den zweiten laden, beide
nebeneinanderlegen, Feld für Feld vergleichen, einsammeln, was nicht zusammenpasst. Irgendwie muss der Agent
vom Ziel zu dieser Folge kommen.

Das geschieht auf zwei Arten. **Ausdrücklich**: Der Agent schreibt vorab einen Plan – eine Aufgabenliste – und
arbeitet ihn ab. **Implizit**: Nichts wird aufgeschrieben, der Plan *entsteht* Schritt für Schritt, während der
Agent in der Schleife überlegt. Die implizite Variante ist genau die Standardschleife aus Agentic RAG, nur ohne
Plan auf dem Papier.

Ein ausgeschriebener Plan bringt zwei handfeste Dinge. Er gibt dem Modell ein Gerüst, an dem es sich beim
Überlegen entlanghangelt – ein aufgeschriebener Plan hält es weit besser auf Kurs, als wenn es das Ganze im
Kopf behalten muss. Und er gibt *Ihnen* etwas, woran Sie den Fortschritt ablesen können: An der Liste sehen
Sie, welche Teilaufgaben erledigt sind und welche nicht. Der zweite Punkt wiegt schwerer, als er klingt;
merken Sie ihn sich.

## Zwei Strategien für die Reihenfolge der Schritte

Sobald Sie zerlegen, gibt es zwei Arten, das Ergebnis in eine Reihenfolge zu bringen. Sie ziehen in
entgegengesetzte Richtungen.

**ReAct** (Reasoning + Acting) verschränkt beides: Der Agent überlegt einen Schritt, handelt, beobachtet,
überlegt den nächsten. Der Plan steht nie vorab fest – er entsteht Schritt für Schritt und passt sich jeder
Beobachtung an. Das ist genau die Standardschleife aus Agentic RAG. Seine Stärke ist die Beweglichkeit: Er
reagiert auf das, was er tatsächlich sieht, nicht auf das, was er vorher vermutet hat. Seine Schwäche zeigt
sich bei langen Aufgaben. Ohne festen Plan kann er abschweifen, sich im Kreis drehen oder das Ziel aus den
Augen verlieren – jeder Schritt ist eine frische lokale Entscheidung, und nichts hält den roten Faden.

**Plan-and-Execute** geht den anderen Weg: erst die ganze Schrittfolge planen, dann ausführen. Das ist
strukturierter und billiger – Sie denken *einmal* über den Plan nach, statt bei jedem Schritt neu von vorn
anzufangen, und das zahlt sich bei langen, strukturierten Aufgaben aus. Der Preis ist Starrheit. Ein vorab
festgelegter Plan kann in dem Moment falsch sein, in dem die Wirklichkeit von ihm abweicht. Brauchbar ist
Plan-and-Execute deshalb nur *mit* einem Mechanismus zum Umplanen: Schlägt ein Schritt fehl oder widerspricht
eine Beobachtung dem Plan, muss der Agent den Plan überarbeiten können, statt blind weiterzulaufen. Dieser
Mechanismus hat einen Namen – **die Umplanung** (re-planning) –, und ohne ihn ist Plan-and-Execute eine Falle.

Der Gegensatz in einem Satz: ReAct gewinnt an Beweglichkeit, Plan-and-Execute an Struktur und Sparsamkeit.

In der Praxis entscheiden Sie sich selten für eine der beiden allein. Sie kombinieren: die groben Schritte
vorab planen, jeden Schritt mit einer lokalen ReAct-Schleife ausführen und umplanen, sobald ein Schritt
fehlschlägt. Der Plan hält den Zusammenhang, die innere Schleife sorgt für Beweglichkeit im Kleinen, und die
Umplanung ist das Gelenk zwischen beiden.

## Das zentrale Fehlerbild – eine Schleife, die nicht richtig endet

Das ist das Fehlerbild dieser ganzen Schicht: **Die Schleife endet nicht richtig.** Geben Sie dem Agenten die Freiheit, die
Reihenfolge selbst zu bestimmen, dann kann er dort versagen, wo eine starre Pipeline es nie könnte – ein fester
Weg `retrieve → generate` endet immer, weil es nirgendwo sonst hingeht. Eine Schleife dagegen muss sich für
das Ende *entscheiden*. Genau diese Entscheidung ist das Neue, das misslingen kann.

Sie misslingt in drei Gestalten:

- **Sie hält nie an.** Der Agent ruft immer weiter Tools auf und kommt nie zu dem Schluss, dass er fertig ist.
- **Sie wiederholt dieselbe erfolglose Aktion.** Dieselbe Abfrage, derselbe fehlschlagende Aufruf, derselbe
  Fehler – wieder und wieder, ohne dass etwas vorangeht.
- **Sie entfernt sich vom Ziel.** Jeder Schritt ist für sich plausibel, und trotzdem entfernt sich der Agent
  langsam von dem, worum er eigentlich gebeten wurde.

Exotisch ist keine der drei. Alle drei sind der Preis für die Freiheit, die Agentic RAG eingeführt hat –
dieselbe Freiheit, mit der die Schleife Fragen über mehrere Hops beantworten kann, lässt sie auch leerlaufen.

## Verteidigung in Schichten

Gegen eine Schleife, die nicht anhält, gibt es keinen einzelnen Schalter. Sie legen die Verteidigung in Schichten
übereinander: unten die schwächste und zugleich unnachgiebigste, oben die klügste.

**Budgets und Limits.** Eine harte Obergrenze – für Schritte, Tool-Calls, Tokens, Kosten oder die verstrichene
Zeit. Ist sie erreicht, hält die Schleife an, gleichgültig was das Modell „will“. Im Produktivbetrieb ist das
nicht verhandelbar. Sie ist die Sicherung, die das Ende auch dann garantiert, wenn jede klügere Verteidigung
versagt, und sie ist der Grund, warum ein entlaufener Agent Sie einen begrenzten Betrag kostet statt eines
unbegrenzten.

**Die Schleifenerkennung.** Achten Sie darauf, ob der Agent dieselbe Aktion wiederholt – derselbe Aufruf,
dieselben Argumente, dasselbe Ergebnis –, und greifen Sie dann ein, statt ihn weiterlaufen zu lassen. Das
greift bei der zweiten Gestalt, bevor das Budget einschreiten muss.

**Eine Abbruchbedingung.** Legen Sie fest, was „fertig“ überhaupt heißt, und schreiben Sie es aus. Üblich ist
ein Tool zum Beenden, das das Modell aufruft, um sich für fertig zu erklären – statt „Bin ich fertig?“ als
vages Urteil stehen zu lassen, das das Modell in jedem Schritt neu fällt und in jedem Schritt falsch fällen
kann.

**Die Fortschrittsverfolgung.** Halten Sie das Ziel und die bereits erledigten Teilaufgaben im Kontext, damit
der Agent sieht, wo er gegenüber dem Plan steht. (Hier zahlt sich der ausgeschriebene Plan ein zweites Mal
aus.) Das ist die unmittelbare Verteidigung gegen das Abschweifen: Ein Agent, der das Ziel vor sich sieht,
verliert es seltener aus den Augen.

**Die Reflexion.** Die klügste Schicht – und einen eigenen Abschnitt wert.

## Reflexion: der wirksamste Hebel gegen Abschweifen und unbemerktes Kreisen

**Die Reflexion** (reflection / self-critique) ist ein eigener Schritt, in dem der Agent den Pfad beurteilt, den
sein Durchlauf bis hierher genommen hat. Komme ich voran? Funktioniert das überhaupt? Sollte ich den Kurs
ändern? – und je nach Antwort entscheidet er, anzuhalten, umzuplanen oder weiterzumachen.

Sie ist eine Verwandte der Selbstkorrektur aus Agentic RAG, zielt aber eine Ebene höher. Die Selbstkorrektur
dort beurteilte die *Qualität des Retrievals*: Diese Passagen passen nicht, also noch einmal suchen. Die
Reflexion hier beurteilt *den Plan und die Schleife als Ganzes* – nicht ein Retrieval, sondern den gesamten
Pfad.

Und darum wiegt sie schwerer, als es zunächst aussieht. Ein Budget *beendet* eine entgleiste Schleife nur, es
*verhindert* sie nicht. Abschweifen und unbemerktes Kreisen sind genau die beiden Fehler, die ein bloßes Budget
bereitwillig bis zur Obergrenze laufen lässt, um sie dort abzuschneiden. Die Reflexion ist die Schicht, die
merken kann, dass die Schleife entgleist ist, und die sie vor der Obergrenze wieder in die Spur bringt –
steuern statt abschneiden. Das Budget ist Ihre Garantie, dass der Agent anhält; die Reflexion ist Ihre beste
Aussicht darauf, dass er *aus dem richtigen Grund* anhält.

## Der Coding-Agent macht diese Schicht sichtbar

Wenn Sie diese Schicht mit eigenen Augen sehen wollen, nehmen Sie einen **Coding-Agenten** – einen Agenten, der
Programmieraufgaben erledigt. Geben Sie ihm eine solche Aufgabe und sehen Sie zu, wie seine ReAct-Kette
`reason → act → observe` und seine Selbstkorrekturen in der Zwischenausgabe vorbeiziehen – die Schleife, die in
Agentic RAG abstrakt blieb, steht Schritt für Schritt auf dem Bildschirm.

Schwächere oder ältere Modelle führen die Fehlerbilder besonders anschaulich vor. An einer schweren Aufgabe
drehen sie sich manchmal im Kreis – sie versuchen dieselbe kaputte Korrektur wieder und wieder, jedes Mal mit
demselben Fehler – oder sie entfernen sich von dem, worum Sie gebeten hatten. Und was tun Sie dann? Sie
unterbrechen von Hand.

Genau dieser alltägliche Reflex *ist* die Lehre. Die Unterbrechung von Hand ist ein **Human-in-the-Loop**
(HITL) als letztes Budget – Sie selbst sind die Obergrenze, die der Agent von allein nicht erreicht hat. Das
ist das konkreteste Argument dafür, warum Budgets, Reflexion und ein menschlicher Eingriff zusammen zählen:
Sie haben den Fehler bereits ablaufen sehen und nach dem Stoppknopf gegriffen.

## Was lange Pfade an Kontext kosten

Noch eine Kostenstelle, leiser als eine Schleife, die nicht anhält, aber immer vorhanden. Die Schleife füllt
den Kontext Schritt für Schritt mit Tool-Calls und deren Ergebnissen. Über einen langen Pfad hinweg heißt das:
Der Kontext wird immer voller, jede Anfrage kostet mehr, und **lost-in-the-middle** schlägt zu – das Modell
achtet am wenigsten auf die Mitte eines langen Kontexts, sodass die frühen Schritte eines Pfades genau dann aus
dem Blick geraten können, wenn der Agent sie braucht.

Die Gegenmittel gehören in den zweiten Durchgang, aber die Namen stehen schon hier: den Verlauf zusammenfassen,
während er wächst; nur das noch Relevante in einem **Arbeitsgedächtnis** (scratchpad / working memory) behalten;
und eine strukturierte Liste des bereits Erledigten führen. Das Letzte ist wieder Ihr ausgeschriebener Plan,
der sich bezahlt macht.

## Wo diese Schicht sitzt – und was sie nachgelagert kostet

Zuerst der Ort. Sie steuert und beendet die Schleife aus Agentic RAG und liegt *über* den Tools aus
Tool-Einsatz: Zerlegung und Abbruch sitzen auf der Schleife `reason → decide → act → observe`, die die Tools
aufruft. Nichts davon ersetzt jene Lektionen – es steuert, was sie gebaut haben.

Zwei nachgelagerte Folgen schärfen Punkte, die Sie schon kennen. **Observability** ist nicht mehr bloß
nützlich, sondern notwendig. Um einer Schleife, die nicht anhält, auf die Spur zu kommen, müssen Sie den
*gesamten* Pfad verfolgen – die ganze Kette der Schritte –, weil der Fehler überall darin stecken kann: eine
schlechte Zerlegung, ein falscher Schritt, eine fehlende Umplanung. Ohne den vollständigen Trace raten Sie. Und
die Evaluierung misst jetzt die Qualität des Pfades, nicht mehr bloß, ob überhaupt geantwortet wurde. Hat der
Agent das Ziel erreicht, und in wie vielen Schritten? Effizienz und Terminierung – ob der Durchlauf überhaupt
endet – gehören jetzt zur Qualität; ein Agent, der die richtige Antwort in vierzig Schritten findet, wo sechs
gereicht hätten, ist kein guter Agent.

## Das Wichtigste

- Diese Lektion ist die Schicht, die die Schleife und die Tools steuert – Zerlegung und Abbruch sitzen auf
  `reason → decide → act → observe`. Sie lenkt die Freiheit, die die früheren Lektionen dem Modell gegeben
  haben.
- Die Aufgabenzerlegung macht aus einem Ziel eine Folge von Teilaufgaben, entweder ausdrücklich (ein
  aufgeschriebener Plan, an dem Sie den Fortschritt ablesen) oder implizit (ein Plan, der in der Schleife von
  selbst entsteht). Ihn aufzuschreiben hilft dem Modell und Ihnen.
- ReAct verschränkt Überlegen und Handeln und passt sich Schritt für Schritt an; Plan-and-Execute plant vorab
  und ist bei langen, strukturierten Aufgaben billiger, braucht aber die Umplanung, um den Kontakt mit der
  Wirklichkeit zu überstehen. Reale Systeme kombinieren beides – grob planen, lokal ReAct, bei einem
  Fehlschlag umplanen.
- Das Fehlerbild dieser Schicht ist eine Schleife, die nicht richtig endet, in drei Gestalten: Sie hält nie an,
  sie wiederholt eine erfolglose Aktion, oder sie entfernt sich vom Ziel.
- Verteidigen Sie in Schichten – Budgets als nicht verhandelbare Sicherung, die Schleifenerkennung, eine
  ausgeschriebene Abbruchbedingung, die Fortschrittsverfolgung und ganz oben die Reflexion, die eine entgleiste
  Schleife verhindert, statt sie nur zu beenden. An einem Coding-Agenten sehen Sie all das gelingen und
  scheitern.
- Nachgelagert wird Observability zur Pflicht – den ganzen Pfad verfolgen, um ihn zu untersuchen –, und die
  Evaluierung misst den Pfad: ob er das Ziel erreicht hat und in wie vielen Schritten.

**[Neue Begriffe](../../glossary.md#planning-loops)**: planning, task decomposition, plan-and-execute, re-planning, reflection / self-critique, termination criterion, step budget / iteration limit, loop detection, scratchpad / working memory, non-termination.

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Baumsuche und Gedächtnis](./deep-dive.md)** – ein tieferer Durchgang durch das Steuern und Begrenzen der
Schleife: die Suche über Bäumen und Graphen von Plänen, benannte Frameworks für die Reflexion, Budget- und
Kostenregeln im Produktivbetrieb, Gedächtnisarchitekturen für lange Pfade (episodisches Gedächtnis gegen
Arbeitsgedächtnis) und Metriken, die den ganzen Pfad bewerten.

Siehe auch: die retrievalspezifische Wendung derselben Schleife – [Agentic RAG](../agentic-rag/index.md); wie
die Schleife, ihre Obergrenzen und die Erholung bei Claude, OpenAI und Gemini aussehen – [der Abschluss dieses
Teils](../real-agents.md).

:::
