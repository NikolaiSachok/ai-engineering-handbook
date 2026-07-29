---
id: overview
title: Teil II – Agenten
sidebar_label: Überblick
---

# Teil II – Agenten

In Teil I haben Sie eine **statische Pipeline** zusammengesetzt: Eine Frage läuft einen festen Weg
entlang, `retrieve → generate`, und dieser Weg steht im Code. In Teil II geht die Kontrolle an das Modell
über. Aus der Pipeline wird eine **Schleife, die das Sprachmodell selbst antreibt**: Es entscheidet, ob es
sucht, wonach es sucht, welches Tool es nimmt und wann es aufhört. Das ist ein Agent.

Eine Linie hält den ganzen Teil zusammen: Schritt für Schritt geben wir dem Modell mehr Freiheit – von
einer einzelnen Routing-Entscheidung bis zur vollen Schleife mit Planung und mehreren Agenten –, und für
diese Freiheit zahlen wir auf jeder Stufe mit Latenz, mit Kosten und mit mühsamerer Fehlersuche. Die
Ingenieursaufgabe lautet nicht „noch agentischer“, sondern: **dem Modell nur so viel Autonomie geben, wie die
Aufgabe wirklich braucht**.

## Was Sie hier finden

- **[Agentic RAG](./agentic-rag/index.md)** – aus dem Schritt Retrieval wird eine Aktion innerhalb einer
  Schleife; dazu das Spektrum vom Router bis zur vollen Schleife.
- **[Tool-Einsatz](./tool-use/index.md)** – wie das Modell externe Funktionen aufruft: Suche, SQL, APIs,
  ein Taschenrechner.
- **[Planung und Schleifen](./planning-loops/index.md)** – ReAct (Reasoning + Acting) und
  `Plan-and-Execute`, die Aufgabenzerlegung, Abbruchbedingungen und der Weg aus einer Schleife wieder
  heraus.
- **[Multi-Agenten-Systeme](./multi-agent/index.md)** – mehrere spezialisierte Agenten, ihre Rollen, die
  Übergabe an den nächsten Agenten; dazu die Topologien – also wie die Agenten miteinander verbunden sind
  – und wann Sie einen Agenten besser nicht aufteilen.
- **[Orchestrierungs-Frameworks](./orchestration-frameworks/index.md)** – [LangGraph](https://www.langchain.com/langgraph), [LangChain](https://www.langchain.com), Microsoft Agent
  Framework, [CrewAI](https://www.crewai.com): was sie einer selbst gebauten `while`-Schleife voraushaben und wann
  Sie besser darauf verzichten.
- **[MCP und Agentenprotokolle](./mcp/index.md)** – ein standardisierter Weg, über den ein Agent an Tools
  und Daten kommt; [MCP](https://modelcontextprotocol.io) gegen [A2A](https://a2a-protocol.org).
- **[Echte Agenten – Claude, OpenAI, Gemini](./real-agents.md)** – der Abschluss dieses Teils: jede Technik
  aus Teil II, bei allen drei Anbietern durchgespielt – hinter einem Dutzend inkompatibler APIs steckt
  jedes Mal dasselbe tragfähige Verfahren.

## Voraussetzungen

Der gesamte Teil I, vor allem die Schicht **Retrieval** – der Agent ruft sie als Tool auf – und die
**Querschnittsthemen**: Evaluierung und Observability werden hier von einer guten Idee zur Pflicht.

:::note[Bearbeitungsstand]

Teil II liegt in seiner Grundfassung vollständig vor – jede Lektion ist veröffentlicht: Agentic RAG,
Tool-Einsatz, Planung und Schleifen, Multi-Agenten-Systeme, Orchestrierungs-Frameworks, MCP und der
Abschluss dieses Teils über die echten Agenten (Claude, OpenAI, Gemini). 🚧 Ein zweiter Durchgang steht
noch aus, der jede Schicht vertieft; die Themen dafür stehen auf den Lektionsseiten unter
„Als Nächstes: die Vertiefung“.

:::
