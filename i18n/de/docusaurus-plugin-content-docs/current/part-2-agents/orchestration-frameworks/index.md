---
title: Orchestrierungs-Frameworks
slug: /part-2-agents/orchestration-frameworks/
---

# Was ein Framework der selbst gebauten Schleife voraushat

Die bisherigen Lektionen haben Agenten aus Grundbausteinen aufgebaut: die Schleife in [Agentic RAG](../agentic-rag/index.md),
die Tools, die sie aufruft, in [Tool-Einsatz](../tool-use/index.md), die Planung und das Anhalten dieser Schleife in
[Planung und Schleifen](../planning-loops/index.md), und Agententeams in der Lektion
[Multi-Agenten-Systeme](../multi-agent/index.md). In der Praxis schreiben Sie das nicht alles selbst. Sie greifen zu einem
**Orchestrierungs-Framework** – [LangChain](https://www.langchain.com), [LangGraph](https://www.langchain.com/langgraph),
[LlamaIndex](https://www.llamaindex.ai) und deren Nachbarn. Diese Lektion behandelt, was ein Framework über die selbst
gebaute `while`-Schleife hinaus wirklich beiträgt, damit Sie eines auswählen und gut einsetzen können: nicht nachbauen,
was es Ihnen ohnehin gibt, und sich nicht hinter ihm verstecken, sobald etwas schiefgeht.

Deshalb sei der Zuschnitt offen benannt. Diese Seite setzt die Grundbausteine der vorangegangenen Lektionen voraus und
behandelt nur das, was ein Framework darüber hinaus beiträgt – sie ist weder ein Framework-Tutorial von Grund auf noch ein
Rundgang durch eine API. Es geht um die Philosophien und die Grenzen: wofür diese Bibliotheken da sind, wo sie sich
bezahlt machen und wo sie mehr kosten, als sie einsparen. Anleitungen mit Code stehen hier keine.

:::tip[▶ Video]

<YouTube id="ZVPlLaehjLk" title="Agentic AI Frameworks Explained: Workflows, Multi-Agent, & Production — IBM Technology" />

IBMs Landkarte desselben Geländes – wie sich Frameworks in Workflow-, Multi-Agenten- und Betriebsfragen aufteilen – ist
eine gute Orientierung, bevor es darum geht, was jede Schicht Ihnen einbringt. (Das Video ist auf Englisch.)

:::

## Der Boilerplate-Code, den Sie sonst selbst schreiben

Beginnen Sie mit der ehrlichen Frage: Was schreiben Sie selbst, wenn Sie das Framework weglassen? Wer ein paar Agenten
von Grund auf gebaut hat, kennt die Antwort: immer wieder dieselbe Mechanik, und davon eine ganze Menge.

Die Schleife kommt zuerst: der Zyklus `nachdenken → entscheiden → handeln → beobachten`, der so lange läuft, bis der Agent
selbst befindet, dass er fertig ist. Dann die Verdrahtung um die Tool-Calls herum – die Schemata, die das Modell liest, die
Zuordnung, die einen Tool-Namen auf die richtige Funktion abbildet, und die Formatierung, die jedes Ergebnis wieder in den
Gesprächsverlauf einfügt. Anspruchsvoll ist daran nichts, fummelig ist beides, und Sie schreiben es jedes einzelne Mal neu.

Darauf sitzt, was mit dem Agenten mitwächst:

- **Zustand und Gedächtnis** über die Schritte hinweg, damit der Agent noch weiß, was er vor drei Antworten getan hat.
- Ein Kontrollfluss, der wirklich etwas kann – Verzweigungen, Wiederholungen, Schleifen und die Pausen, in denen ein
  Mensch eingreift.
- Die Orchestrierung mehrerer Agenten: die Übergaben und das Routing zwischen ihnen, die Topologien aus der Lektion
  über [Multi-Agenten-Systeme](../multi-agent/index.md) – also die Art, wie die Agenten miteinander verbunden sind.
- Der Rest, der zum Produktivbetrieb gehört – Tracing-Hooks, Streaming, Persistenz und Checkpointing.

Nichts davon ist der interessante Teil Ihres Agenten. Es ist der Boilerplate-Code darunter. Das Kernversprechen eines
Frameworks lautet, dass es diese Mechanik ein für alle Mal und überall gleich mitbringt, damit in Ihrem Code das Verhalten steht
und nicht die Verdrahtung.

## Die zentrale Abstraktion: der Agent als Graph, als Zustandsautomat

Hinter den Markennamen kommen die meisten Frameworks bei einem Gedanken zusammen, und LangGraph spricht ihn am klarsten aus:
Modellieren Sie den Agenten als **Graphen**, als **Zustandsautomaten**. Aus den Schritten werden **Knoten** – das Modell
aufrufen, ein Tool aufrufen, eine Entscheidung treffen –, und aus dem Kontrollfluss werden **Kanten** dazwischen – darunter auch
solche, die zurückführen, damit der Zyklus weiterlaufen kann, bis eine Bedingung erfüllt ist.

Und genau darauf kommt es bei dieser Umdeutung an: Die selbst gebaute Schleife ist ein `while`-Block – undurchsichtig, während
sie läuft, und alles oder nichts, wenn sie scheitert. Machen Sie einen Zustandsautomaten daraus, dann wird sie zu etwas,
das Sie einsehen, anhalten und wieder aufnehmen können. Sie bekommen Checkpoints, auf die Sie zurückgehen können, Knoten,
an denen ein Mensch freigibt, bevor es weitergeht, Wiederholungen, die auf einen einzelnen Schritt begrenzt sind, und
Verzweigungen, die deterministisch sind, statt in der frei laufenden Schleife des Modells vergraben zu liegen. In einem
Satz liegt hier der entscheidende Unterschied: Der Graph macht aus einer undurchsichtigen Schleife eine Maschine, die
sich steuern, einsehen und wieder aufnehmen lässt.

## Das Feld, nach Schichten sortiert

Die Framework-Landschaft wirkt überfüllt, bis Sie sie danach sortieren, was das jeweilige Werkzeug eigentlich sein will.
Drei grobe Schichten.

Die **Integrationsschicht** besteht aus breiten Bibliotheken fertiger Anbindungen – an Modelle, an Tools, an Datenquellen
–, damit Sie die Adapter nicht von Hand schreiben. Hier wohnt LangChain, und ebenso LlamaIndex, das stärker auf Daten und
RAG hin ausgerichtet ist. Lautet Ihr Problem „den Agenten an fünfzehn verschiedene Dienste anschließen“, dann kaufen Sie auf
dieser Schicht ein.

Auf der Schicht für **Kontrollfluss und Zustand** ist der Graph zu Hause: LangGraph und Microsoft
Agent Framework, Microsofts Eintrag mit Ausrichtung auf das Unternehmensumfeld. Für den Zustandsautomaten aus dem vorigen
Abschnitt ist diese Schicht zuständig.

Die **Multi-Agenten-Schicht** verpackt die Topologien aus der Lektion über Multi-Agenten-Systeme.
[CrewAI](https://www.crewai.com) gliedert die Arbeit in rollenbasierte „Crews“ aus Agenten mit fest zugewiesenen
Aufgaben; [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) liefert vorgefertigte
Orchestrierungen für mehrere Agenten mit, geerbt von [AutoGen](https://github.com/microsoft/autogen) – Agenten, die sich
miteinander unterhalten. Wenn das, was Sie modellieren wollen, wirklich ein Team *ist*, fangen Sie hier an.

Ein Vorbehalt, und er wiegt schwerer als die Einteilung. Diese Grenzen verwischen – LangChain kann auch Kontrollfluss,
die Frameworks schreiben einander die guten Einfälle innerhalb von ein bis zwei Releases ab, und das ganze Ökosystem ist
schnell in Bewegung: Microsoft Agent Framework 1.0 (allgemein verfügbar seit April 2026) hat
[Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) und AutoGen aufgesogen, beide stehen inzwischen im
Wartungsmodus. Lesen Sie die drei Schichten als Momentaufnahme von Philosophien, nicht als haltbare Rangliste. Lernen Sie
die Kategorien; die Versionsnummern haben sich verschoben, bevor Sie ausliefern.

## Wiederkehrende Muster im Alltag

In der täglichen Arbeit kommen immer wieder dieselben wenigen Formen vor, und wer sie beim Namen kennt, braucht aus der
Dokumentation eines Frameworks kaum mehr.

Die Grundform ist ein Graph aus **Tool-Knoten mit bedingten Kanten** – der Agent ruft ein Tool auf, und eine Kante
entscheidet anhand des Ergebnisses, wohin es als Nächstes geht. Für den Regelfall liefern die meisten Frameworks
einen **vorgefertigten ReAct-Agenten** (Reasoning + Acting) mit: fertig verdrahtet, Sie instanziieren ihn, statt den
Graphen selbst zusammenzusetzen.

Die Persistenz taucht als **Checkpointer** auf – eine Komponente, die den Zustand sichert, sodass ein Durchlauf angehalten
und später wieder aufgenommen werden kann, und die getrennte Threads getrennt hält, damit zwei Gespräche nicht
ineinanderlaufen. Darüber sitzt der **Human-in-the-Loop (HITL)**: ein Knoten, an dem die Schleife anhält, damit ein
Mensch freigibt, und der danach genau dort fortsetzt, wo sie stehengeblieben ist. Das ist der Human-in-the-Loop aus
[Planung und Schleifen](../planning-loops/index.md), jetzt zu einem vollwertigen Knoten im Graphen befördert statt zu
einem Knopf, den jemand von Hand drückt.

Für Teams reicht Ihnen das Framework ein fertiges **Supervisor**- oder **Crew**-Konstrukt – den Orchestrator aus der
Lektion über Multi-Agenten-Systeme, vorgefertigt, sodass Sie die Topologie konfigurieren statt sie zu programmieren. Und
durch alles hindurch läuft die **Tracing-Anbindung**, [LangSmith](https://www.langchain.com/langsmith) als naheliegendes
Beispiel: die Schicht für Observability (Beobachtbarkeit), mit der Sie sehen, was der Graph tatsächlich getan hat. Das
ist der Gegenstand von [Teil III](../../part-3-production/overview.md), und hier ist die Stelle, an der diese Schicht andockt.

## Wann besser nicht – und was es kostet

Ein Framework ist nicht umsonst, und die Kosten sind das Spiegelbild des Nutzens.

Am schärfsten ist der **Preis der Abstraktion**. Ein Framework verbirgt den Prompt und den Kontrollfluss – genau das, was
Sie wollten, bis zu dem Moment, in dem etwas schiefgeht und Sie sich *durch* Schichten fremden Codes hindurch auf die
Fehlersuche machen. Für einen einfachen Agenten sind eine schlichte Schleife und der native Tool-Einsatz des Anbieters
klarer, kürzer und weit leichter zu debuggen als dasselbe Verhalten, durch ein Graph-Framework gefädelt. Die Abstraktion
verdient ihren Preis erst, wenn es echte Komplexität zu bändigen gibt.

Zwei weitere stehen daneben. **Bewegung im Ökosystem** heißt, dass sich die APIs und die gerade gesegneten Muster von
Release zu Release verschieben; der idiomatische Code von heute ist die Altlast, von der Sie nächstes Jahr wegmigrieren.
Und die Abstraktionen eines Frameworks zu übernehmen ist ein Abwägen zwischen **Portabilität und Vendor-Lock-in** – je
mehr Sie sich auf seine Konstrukte stützen, desto enger sind Sie daran gekoppelt.

Die Regel ist deshalb eine Regel über die Reihenfolge. Verstehen Sie zuerst die Grundbausteine aus den vorangegangenen
Lektionen; greifen Sie dann zu einem Framework, um Boilerplate-Code loszuwerden, nie um sich das Verständnis dessen zu
ersparen, was er tut. Holen Sie ein Graph-Framework herein, wenn Sie wirklich steuerbare komplexe Abläufe brauchen –
Checkpoints, Human-in-the-Loop, Verzweigungen, die Koordination mehrerer Agenten. Für einen einfachen Agenten nehmen Sie
das SDK des Anbieters direkt und lassen die Schicht weg.

## Wo diese Lektion anschließt

Nichts in dieser Lektion ist ein neuer *Begriff*. Frameworks ändern die Gedanken der vorangegangenen Lektionen nicht –
die Schleife, die Tools, die Planung, die Topologien für mehrere Agenten. Sie verpacken sie und geben sie Ihnen zurück,
abzüglich des Boilerplate-Codes. Und weil sie dieselben Grundbausteine verpacken, stecken sie unmittelbar in der Schicht
für Observability und Evaluierung, die [Teil III](../../part-3-production/overview.md) aufgreift: Der Graph, den Sie hier
gebaut haben, ist genau das, was Sie dort tracen und messen werden.

## Das Wichtigste

- Ein Orchestrierungs-Framework nimmt Ihnen den Boilerplate-Code ab, den Sie sonst um die eigene Schleife herum
  schreiben: die Mechanik der Schleife, die Verdrahtung der Tool-Calls, Zustand und Gedächtnis, den Kontrollfluss, die
  Übergaben zwischen Agenten und am Ende noch Tracing, Streaming und Checkpointing.
- Die zentrale Abstraktion, bei der die meisten Frameworks zusammenkommen, ist der Agent als Graph, als Zustandsautomat:
  Knoten (Modell aufrufen, Tool aufrufen, entscheiden) und Kanten (Kontrollfluss, die zurückführenden eingeschlossen).
  Der entscheidende Unterschied ist, dass daraus statt einer undurchsichtigen `while`-Schleife eine Maschine wird, die
  sich steuern, einsehen und wieder aufnehmen lässt.
- Sortieren Sie das Feld nach Schichten – Integration (LangChain, LlamaIndex), Kontrollfluss und Zustand (LangGraph,
  Microsoft Agent Framework), mehrere Agenten (CrewAI und die Orchestrierungen des Microsoft Agent Framework) –, aber
  behandeln Sie es als Momentaufnahme: Die Grenzen verwischen, und das Ökosystem ist in Bewegung. Lernen Sie die
  Kategorien, nicht die Versionsnummern.
- Der Preis ist die Abstraktion: Ein Framework verbirgt Prompt und Kontrollfluss, also suchen Sie Fehler durch Schichten
  fremden Codes hindurch. Für einen einfachen Agenten ist eine schlichte Schleife mit nativem Tool-Einsatz klarer.
- Die Regel: zuerst die Grundbausteine. Ein Framework nimmt Ihnen Boilerplate-Code ab, es ersetzt nicht das Verständnis
  – ein Graph-Framework für steuerbare komplexe Abläufe, für einen einfachen Agenten das SDK des Anbieters direkt.

**[Neue Begriffe](../../glossary.md#orchestration-frameworks)**: orchestration framework, agent as a graph / state machine, node / edge, checkpointing, human-in-the-loop (HITL).

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Graphen und Durable Execution](./deep-dive.md)** – ein konkreter LangGraph-Graph, Knoten für Knoten durchgegangen,
Durable Execution und die Checkpoint-Backends dahinter, das frameworkeigene Gedächtnis gegen die Konstrukte für mehrere
Agenten gestellt, deklarative gegen imperative Agentendefinition und Tracing und Evaluierung auf Framework-Ebene.

Siehe auch: wie sich diese Konstrukte über Claude, OpenAI und Gemini abbilden –
[der Abschluss dieses Teils](../real-agents.md); die allgemeine Schicht für Schleifensteuerung und Budgets, die ein
Framework verpackt – [Planung und Schleifen](../planning-loops/index.md); die Standardprotokolle unterhalb der
Transportschicht – [MCP und Agentenprotokolle](../mcp/index.md).

:::
