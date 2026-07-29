---
title: MCP und Agentenprotokolle
slug: /part-2-agents/mcp/
---

# Der Standard, der Agenten an die Außenwelt anbindet

Im [Tool-Einsatz](../tool-use/index.md) hat der Agent gelernt, Tools aufzurufen – aber jede Anbindung war Handarbeit für sich: jeder Agent an jedes Tool geklebt, mit eigens dafür geschriebenem Code. Bei einem Agenten und drei Tools geht das auf. Sobald es von beidem viele gibt, geht es nicht mehr auf. Bei M Anwendungen, die je N Tools brauchen, stehen M × N einzeln gebaute Anbindungen an – dieselbe Datenbankanbindung für jeden Agenten neu gebaut, jede API jedem Agenten neu beigebracht. Das ist **das M×N-Integrationsproblem**, und es wächst so, wie Integrationsprobleme immer wachsen: schlecht.

Der übliche Ausweg ist ein Standard. Kapseln Sie jedes Tool ein einziges Mal hinter einem Server; setzen Sie den Client ein einziges Mal um, in jeder Anwendung; danach spricht jede Anwendung mit jedem Tool, ohne dass dafür neuer Code entsteht. Aus M × N wird so **N + M** – Sie schreiben N Server und M Clients statt M × N paarweiser Anbindungen. Der Standard beschreibt sich selbst mit einem Bild: **ein USB-C-Anschluss für KI-Anwendungen**, ein Stecker also statt eines eigenen Kabels für jedes Gerät. Diese Lektion handelt von dem Protokoll, das diesen Tausch möglich macht, von der Stelle, an der es sich wirklich von den API-Dokumenten unterscheidet, die Sie schon kennen, und von der neuen Angriffsfläche, die dabei entsteht.

:::tip[▶ Video]

<YouTube id="g9JIUM0MHgQ" title="CLI vs [MCP](https://modelcontextprotocol.io): How AI Agents Choose the Right Tool for the Job — IBM Technology" />

Sehen Sie es sich vor dem Swagger-Abschnitt weiter unten an: Es stellt dieselbe Frage ohne Umschweife – wenn die Kommandozeile und die API-Spezifikation längst beschreiben, was ein Tool tut, was kommt durch MCP eigentlich hinzu? (Das Video ist auf Englisch.)

:::

## Was MCP ist

**MCP** (Model Context Protocol) ist ein offener Standard. Anthropic hat ihn Ende 2024 vorgestellt und im Dezember 2025 an die Agentic AI Foundation unter dem Dach der Linux Foundation übergeben; seither liegt die Steuerung bei einem neutralen, von der Community getragenen Gremium. Aufgebaut ist er als Client-Server-Architektur, und zwei Rollen erledigen darin die Arbeit. **Der MCP-Server** kapselt ein einzelnes Tool oder eine einzelne Datenquelle – eine Datenbank, ein Dateisystem, eine SaaS-API, ein Code-Repository – und stellt dessen Fähigkeiten einheitlich bereit; er ist ein Dienst, der Funktionen oder Daten zur Verfügung stellt. **Der MCP-Client** ist der Agent oder die Anwendung am anderen Ende: Er verbindet sich mit Servern und nutzt, was sie anbieten. Ein Server ist für viele Clients erreichbar; ein Client kann Verbindungen zu vielen Servern halten.

Mehr als eine Konvention für Tool-Calls wird MCP dadurch, dass es nicht eine, sondern drei Komponenten standardisiert:

- **Tools** – aufrufbare Funktionen, genau der Begriff aus dem Tool-Einsatz, jetzt in einheitlicher Gestalt;
- **Ressourcen** (Daten und Kontext, die der Server dem Modell zum Lesen bereitstellt) – der Inhalt einer Datei, ein Datensatz, eine Dokumentationsseite;
- **Prompts** – wiederverwendbare Vorlagen, die der Server anbietet; so liefert er nicht nur seine Aktionen mit, sondern auch den erprobten Weg, sie aufzurufen.

Beim Transportprotokoll bleibt es bewusst unspektakulär. Ein Server auf Ihrem eigenen Rechner spricht über `stdio`, ein entfernter Server über **Streamable HTTP**. Die drei Komponenten bleiben in beiden Fällen dieselben – wo der Server läuft, ist eine Frage der Bereitstellung und ändert nichts an dem, was der Client zu sehen bekommt.

## Tools bauen und Agenten bauen – zwei getrennte Aufgaben

Es geht bei alledem nicht um Ordnungsliebe. MCP trennt zwei Aufgaben voneinander, die bis dahin aneinanderhingen: Tools zu bauen und Agenten zu bauen. Sie schreiben einen MCP-Server ein einziges Mal, und jeder MCP-Client kann ihn benutzen – über Anwendungen, Frameworks und Modelle hinweg, ohne Code für die einzelne Anbindung. Die Anbindung an Ihr Ticketsystem ist dann nicht mehr etwas, das jedes Agententeam für sich neu umsetzt, sondern etwas, das ein Team einmal ausliefert und an das sich alle anderen anschließen.

Das ist kein Merkmal des Protokolls, sondern eine Wirkung im ganzen Ökosystem: der Gewinn aus N + M, in menschlichen Maßstäben ausgedrückt. Ein Tool, das für eine Anwendung gebaut wurde, lässt sich von jeder anderen weiterverwenden – so wie ein USB-C-Gerät an jedem Rechner funktioniert. Sichtbar wird der Wert nicht im ersten Projekt, sondern im zweiten, dritten und zehnten, das den Server wiederverwendet, statt ihn noch einmal zu bauen.

## Worin sich MCP von Swagger/OpenAPI und von `--help` auf der Kommandozeile unterscheidet

Ein Einwand verdient es hier, ernst genommen zu werden, denn er kommt in jedem fachlichen Gespräch früher oder später: *„MCP ist doch nur Swagger für LLMs. Es klebt Beschreibungen an die Endpunkte, damit ein Modell sie lesen kann. OpenAPI haben wir seit zehn Jahren.“* Der Einwand ist berechtigt, und ihn ehrlich zu beantworten ist der schnellste Weg zu verstehen, was MCP ist – und was nicht.

Fangen Sie mit dem Zugeständnis an, denn der wahre Teil daran ist wirklich wahr. OpenAPI und Swagger tragen längst Bedeutung: Jeder Endpunkt kann ein `summary` und eine `description` haben, jeder Parameter eine Notiz dazu, was er bedeutet. Der `--help`-Text auf der Kommandozeile leistet dasselbe. Und Sie *können* ein LLM unmittelbar aus einer OpenAPI-Spezifikation heraus steuern: Bilden Sie jeden Endpunkt auf eine Tool-Definition ab, geben Sie dem Modell die Beschreibungen mit – und der Satz aus dem Tool-Einsatz, dass eine Beschreibung ein Prompt ist, gilt dort Wort für Wort. Der Unterschied liegt also ausdrücklich *nicht* darin, dass MCP Bedeutung trägt und die anderen nicht. Wer behauptet, Swagger könne keine Bedeutung transportieren, irrt sich – und wenn Sie ihm glauben, fällt der Rest dieses Abschnitts in sich zusammen.

Die wirklichen Unterschiede sind vier, und in keinem geht es darum, ob Beschreibungen vorhanden sind:

1. **Ein Protokoll für die Laufzeit, keine Dokumentation für den Entwurf.** Ein MCP-Client findet die Fähigkeiten eines Servers zur Laufzeit und spricht sie über ein einheitliches Protokoll an – der Agent fragt den Server, was er anbietet, und ruft es dann im laufenden Betrieb auf. OpenAPI und `--help` beschreiben eine API im Voraus: Erst liest jemand die Beschreibung, dann programmiert er gegen sie. Das eine verarbeitet ein laufender Agent, das andere ist Dokumentation für einen Menschen, der eine Anbindung baut. Der Unterschied liegt darin, **wer** liest und **wann** – nicht darin, ob Bedeutung vorhanden ist.

2. **Komponenten für Sprachmodelle, nicht nur Aktionen.** OpenAPI und die Kommandozeile beschreiben aufrufbare Aktionen und sonst nichts. Für MCPs Ressourcen (Kontext zum Lesen) und Prompts (Vorlagen zum Wiederverwenden) hat weder das eine noch das andere eine Entsprechung – in OpenAPI gibt es kein Konstrukt für „Hier ist ein Dokument, das dem Modell im Kontext stehen soll“ oder „Hier ist die erprobte Vorlage für diesen Vorgang“. MCP standardisiert Kontext und Vorlagen gleichrangig neben den Aktionen.

3. **Ein einziger, einheitlicher Client.** Jeder MCP-Client spricht mit jedem MCP-Server. Es gibt keinen eigenen Client je API und keinen Adapter je Framework. Hier wird der Gewinn aus N + M greifbar: Was Sie sonst auf der Client-Seite für jede API neu schreiben würden, schrumpft auf eine einzige Umsetzung des Protokolls.

4. **Eine Sitzung, und sie läuft in beide Richtungen.** MCP ist eine zustandsbehaftete Sitzung und kein Stapel voneinander unabhängiger Aufrufe nach dem Muster Anfrage/Antwort. Ein Server kann dem Client von sich aus Aktualisierungen schicken, und über **Sampling** kann er das Modell *des Clients* bitten, etwas für ihn zu erzeugen – eine Fähigkeit, die in beide Richtungen wirkt und für die eine statische API-Spezifikation keine Ausdrucksform hat.

Und nun die ehrliche Einschränkung, denn in einem Punkt trifft der Einwand zu. In der Praxis sind MCP-Server für ein Modell tatsächlich meist besser lesbar als eine rohe OpenAPI-Ausgabe – aber aus handwerklichen Gründen, nicht weil das Protokoll mehr könnte. MCP-Server werden von vornherein für Agenten geschrieben: Ihre Beschreibungen sind als Prompts formuliert (die Disziplin aus dem Tool-Einsatz, dass eine Beschreibung ein Prompt ist), und sie bieten einen bewusst zugeschnittenen, kleinen Tool-Katalog an statt jedes Endpunkts, den eine API zufällig besitzt (die Regel „wenige Tools, und keine, die sich überschneiden“). Ein von Hand geschriebener MCP-Server lässt sich von einem Modell meist besser bedienen als eine automatisch erzeugte Swagger-Datei mit 200 Endpunkten. Das ist aber ein Unterschied in der Entwurfspraxis und nichts, was OpenAPI nicht ausdrücken könnte. Swagger kann jede Bedeutung transportieren, die auch MCP transportiert; MCP-Server werden nur eben üblicherweise so geschrieben, dass ein Modell sie verarbeitet. Halten Sie beides auseinander: „auf einen Agenten zugeschnitten“ ist eine Gewohnheit beim Schreiben, keine Eigenschaft des Protokolls.

## MCP vs. A2A – von Agent zu Tool, von Agent zu Agent

MCP standardisiert eine Achse: vom Agenten zum Tool, vom Agenten zu den Daten. Über eine zweite Achse sagt es nichts – die von Agent zu Agent, also genau die Verständigung, die Sie ab dem Moment brauchten, in dem Sie [Multi-Agenten-Systeme](../multi-agent/index.md) gebaut haben. Wenn ein Agent an einen anderen übergibt, welches Protokoll trägt diese Übergabe? MCP ist dafür nicht gemacht; es verbindet einen Agenten mit seinen Tools, nicht mit einem Gegenüber.

**[A2A](https://a2a-protocol.org) (Agent-to-Agent)** ist die Antwort, die sich gerade herausbildet – ein Standard, den Google vorgeschlagen hat und der inzwischen unter dem Dach der Linux Foundation liegt –, und A2A ist nicht der einzige Anwärter. Die Unterscheidung, die sich zu merken lohnt, ist sauber: **MCP führt vom Agenten zu Tools und Kontext, A2A von Agent zu Agent.** Diese Ecke des Fachs bewegt sich schnell, und bis Sie das hier lesen, wird die Liste der Anwärter eine andere sein; lernen Sie deshalb die *Unterscheidung* und nicht die Namen. Die beiden Achsen gibt es wirklich, und sie bleiben; jedes einzelne Protokoll auf einer von ihnen ist eine Momentaufnahme.

## Jeder angebundene Server vergrößert die Angriffsfläche

Wer einen Agenten an einen Server anbindet, den er nicht kontrolliert, bindet ihn an Eingaben an, die er nicht kontrolliert. Ein MCP-Server ist **eine neue Angriffsfläche**. Ein bösartiger oder übernommener Server kann eine **indirekte Prompt-Injection** in die Ressourcen und Tool-Results einschleusen, die er zurückgibt – Text, den Ihr Modell als Anweisung liest; und selbst die Tool-Beschreibung ist ein Einfallstor (**Tool-Poisoning**), weil eine Beschreibung ein Prompt ist. Er kann versuchen, Daten abzuziehen, an die der Agent herankommt. Er kann die ihm erteilten Berechtigungen überschreiten und mehr tun als die eine Aufgabe, für die Sie ihn angebunden haben. Dasselbe einheitliche Protokoll, das Server so leicht anschließbar macht, macht auch einen feindlichen Server leicht anschließbar.

Die Abwehr ist die Disziplin, die Sie schon haben – nur eine Schicht weiter außen. Halten Sie sich an das **Prinzip der geringsten Berechtigungen**: pro Server ein begrenzter Tool-Katalog, nichts, was die Aufgabe nicht verlangt. Binden Sie nur Server an, die Sie geprüft haben und denen Sie vertrauen; „steht in einer Registry“ ist keine Prüfung. Verlangen Sie für **gefährliche Aktionen** die Bestätigung durch einen Menschen, damit ein übernommener Server nicht unbemerkt in Ihrem Namen handelt. Und die Guardrails aus Teil I – die Rangfolge der Anweisungen und das Spotlighting – gelten unmittelbar auch für MCP: Behandeln Sie alles, was ein Server schickt, Ressourcen wie Tool-Results, als nicht vertrauenswürdige *Daten*, über die zu urteilen ist, und nie als vertrauenswürdige *Anweisungen*, denen zu folgen ist. Eine Ressource ist Inhalt, kein Befehl – auch dann, wenn sie wie einer formuliert ist.

---

Damit ist die Lektion abgeschlossen – und mit ihr die Grundausstattung von Teil II. Angefangen hat Teil II mit einer einzigen agentischen Schleife in [Agentic RAG](../agentic-rag/index.md): Retrieval als Aktion, für die sich das Modell entscheidet. Dann kamen Tools zum Handeln hinzu ([Tool-Einsatz](../tool-use/index.md)), ein Weg, über viele Schritte zu planen und auch wirklich anzuhalten ([Planung und Schleifen](../planning-loops/index.md)), weitere Agenten, die sich die Arbeit teilen ([Multi-Agenten-Systeme](../multi-agent/index.md)), und Frameworks, um all das zu bündeln ([Orchestrierungs-Frameworks](../orchestration-frameworks/index.md)). Diese Lektion hat das letzte Stück geliefert: die Standardprotokolle, die Agenten im Produktivbetrieb an Tools und aneinander anbinden. Aus einer Schleife ist ein System geworden, das über einen gemeinsamen Stecker mit der Welt verbunden ist. Wie das alles auf laufenden Modellen von Claude, OpenAI und Gemini aussieht, zeigt [der Abschluss dieses Teils](../real-agents.md).

## Das Wichtigste

- **Das M×N-Integrationsproblem** – M Anwendungen × N Tools ergeben M × N einzeln gebaute Anbindungen – ist der Grund, warum es Standards gibt. MCP macht daraus **N + M**: jedes Tool einmal als Server kapseln, den Client einmal je Anwendung umsetzen. Das Bild dazu ist **ein USB-C-Anschluss für KI-Anwendungen**.
- **MCP** (Model Context Protocol) ist ein offener Client-Server-Standard – 2024 bei Anthropic entstanden, seit Dezember 2025 ein Projekt der Agentic AI Foundation unter dem Dach der Linux Foundation. **Der MCP-Server** kapselt ein Tool oder eine Datenquelle, **der MCP-Client** ist der Agent, der sie nutzt. Standardisiert werden drei Komponenten – **Tools**, **Ressourcen** und **Prompts** – über `stdio` (lokal) oder Streamable HTTP (entfernt).
- Der Gewinn: **Tools zu bauen und Agenten zu bauen sind mit MCP zwei getrennte Aufgaben.** Schreiben Sie einen Server einmal, und jeder Client verwendet ihn weiter – eine Wirkung im Ökosystem, kein Merkmal des Protokolls.
- MCP ist *nicht* „Swagger mit Beschreibungen“. Swagger und der `--help`-Text tragen längst Bedeutung, und ein LLM lässt sich auch aus einer OpenAPI-Spezifikation heraus steuern. Die wirklichen Unterschiede sind: Laufzeit statt Entwurfszeit, Komponenten jenseits der Aktionen (Ressourcen, Prompts), ein einziger einheitlicher Client und eine Sitzung in beide Richtungen (Sampling). MCP-Server sind für ein Modell *meist* besser lesbar – aber weil sie so geschrieben werden, nicht weil OpenAPI keine Bedeutung tragen könnte.
- **MCP führt vom Agenten zu Tools, A2A (Agent-to-Agent) von Agent zu Agent.** Zwei Achsen. Das Feld ist in Bewegung – lernen Sie die Unterscheidung, nicht die aktuellen Namen.
- Ein MCP-Server ist **eine neue Angriffsfläche**: indirekte Prompt-Injection, abgezogene Daten, überschrittene Berechtigungen. Wehren Sie sich mit dem **Prinzip der geringsten Berechtigungen**, mit ausschließlich geprüften Servern und mit einer Bestätigung durch einen Menschen für gefährliche Aktionen; behandeln Sie alles, was ein Server liefert, als nicht vertrauenswürdige Eingabe, nie als Anweisung.

**[Neue Begriffe](../../glossary.md#mcp)**: MCP (Model Context Protocol), MCP server, MCP client, MCP resources, MCP prompts, M×N integration problem, A2A (Agent-to-Agent).

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Server, Transportprotokolle und Vertrauen](./deep-dive.md)** – einen MCP-Server von Hand bauen, Sampling und Elicitation im Einzelnen, MCP-Registries und das Auffinden von Servern, die Wahl zwischen `stdio` und Streamable HTTP, die Landschaft der Agentenprotokolle im Wandel (A2A und die anderen Anwärter) und gehärtete Betriebsmuster für Server, denen Sie nicht trauen können.

Siehe auch: [der Abschluss dieses Teils](../real-agents.md), der MCP auf laufenden Modellen von Claude, OpenAI und Gemini vorführt; [Multi-Agenten-Systeme](../multi-agent/index.md) für die Achse von Agent zu Agent, die MCP offenlässt; und [Orchestrierungs-Frameworks](../orchestration-frameworks/index.md), um diese Verbindungen in eine Bibliothek zu packen.

:::
