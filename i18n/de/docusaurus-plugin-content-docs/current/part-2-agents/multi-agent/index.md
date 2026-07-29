---
title: Multi-Agenten-Systeme
slug: /part-2-agents/multi-agent/
---

# Mehrere spezialisierte Agenten statt eines einzelnen

Bisher hat jede Lektion *einen* Agenten gebaut: [Agentic RAG](../agentic-rag/index.md) hat ihm die Schleife gegeben, [Tool-Einsatz](../tool-use/index.md) die Tools, die er darin aufrufen kann, und [Planung und Schleifen](../planning-loops/index.md) die Fähigkeit, oberhalb dieser Schleife zu planen und rechtzeitig anzuhalten. Diese Lektion stellt eine andere Frage: Was ändert sich, wenn Sie statt eines Agenten mehrere spezialisierte einsetzen, die zusammenarbeiten?

Durch die ganze Lektion laufen zwei Fragen, und beide wiegen gleich schwer. Erstens: *warum* Sie einen Agenten überhaupt in mehrere aufteilen sollten. Zweitens: *wann nicht*. Die Disziplin aus Agentic RAG gilt unverändert weiter – die einfachste Stufe nehmen, die die Aufgabe löst. Ein Multi-Agenten-System ist die teurere Stufe und keine Belohnung dafür, etwas Beeindruckendes gebaut zu haben.

:::tip[▶ Video]

<YouTube id="kYkZI3oj2W4" title="Multi AI Agent Systems: When One AI Brain Isn't Enough — IBM Technology" />

IBM zeigt denselben Fall: wann ein einzelner Agent nicht mehr genügt und wie sich die Arbeit auf ein Team verteilt. (Das Video ist auf Englisch.)

:::

## Gründe, einen Agenten aufzuteilen

Vier Gründe, und sie ziehen nicht alle gleich stark.

**Spezialisierung.** Ein Agent mit engem Zuschnitt – eine schmale Rolle, ein darauf abgestimmter Prompt, eine Handvoll Tools – schlägt den einen Mega-Agenten, der fünfzig Tools mit sich herumschleppt. Das ist die Multi-Agenten-Fassung dessen, was der Tool-Einsatz *wenige, überschneidungsfreie Tools* nennt: Je kleiner und orthogonaler der Tool-Katalog eines Agenten ausfällt, desto seltener greift er zum falschen Tool und desto nachvollziehbarer wird sein Verhalten.

**Die Isolation der Kontexte** ist der Grund, der wirklich skaliert. Jeder Agent bekommt sein eigenes Kontextfenster, und der Orchestrator sieht von jedem Worker nur das *Ergebnis* – nicht dessen Zwischenschritte, nicht dessen rohe Tool-Ausgaben. Genau deshalb kann ein Multi-Agenten-System Arbeit übernehmen, deren vollständiger Zwischenkontext niemals in ein einziges Kontextfenster passen würde. Statt dass sich ein einziger Kontext mit dem Ballast aller füllt, behält jeder Agent den Blick auf das Stück, für das er zuständig ist.

**Modularität.** Unabhängige Agenten lassen sich getrennt bauen, testen und wiederverwenden – derselbe Grund, aus dem ein Monolith in Dienste zerlegt wird.

**Parallelität.** Mehrere Agenten bearbeiten voneinander unabhängige Teilaufgaben nebenläufig, statt sie nacheinander in einer einzigen Schleife abzuarbeiten.

## Topologien – wie die Agenten miteinander verbunden sind

Für die **Topologie** – also dafür, wie die Agenten miteinander verbunden sind – gibt es einige wenige Standardformen. Die meisten echten Systeme sind eine davon oder eine Mischung daraus.

**Orchestrator-Worker**, in vielen Frameworks auch **Supervisor** genannt. Ein führender Agent zerlegt die Aufgabe, weist jede Teilaufgabe dem spezialisierten Worker zu, der dazu passt, und fügt die Ergebnisse zu einer Antwort zusammen. Das ist die häufigste Topologie, und der Rest der Lektion stützt sich darauf.

**Die Kette (sequenziell).** In einer Kette verarbeitet jeder Agent die Ausgabe des vorherigen weiter – Autor → Lektorat → Faktenprüfung, und jede Stufe reicht ihre Arbeit an die nächste. Die Ausgabe des einen ist die Eingabe des nächsten, in fester Reihenfolge.

**Hierarchisch.** Orchestratoren über Orchestratoren: ein Orchestrator, dessen Worker selbst Orchestratoren eigener Teams sind. Das ist das Orchestrator-Muster über mehrere Ebenen hinweg, für Aufgaben, die einem einzelnen flachen Team zu groß sind.

**Die Debatte zwischen Agenten.** Ein erzeugender Agent schlägt etwas vor, ein **Kritiker-Agent** hält dagegen – oder mehrere Agenten erarbeiten unabhängig voneinander Lösungen, und die beste wird ausgewählt. Unabhängige Blickwinkel machen das Ergebnis besser, und zwar aus demselben Grund, aus dem Gutachten verblindet werden: Ein Blick von außen findet, was eine einzelne Kette sich bereitwillig schönredet.

## Nachrichten und Übergaben zwischen den Agenten

Agenten verständigen sich über Nachrichten. Der Vorgang, der tatsächlich Arbeit weitergibt, ist die **Übergabe an den nächsten Agenten**: Sie gibt die Kontrolle weiter *und mit ihr* den Kontext, auf den es ankommt.

Die Entwurfsentscheidung, an der alles hängt, ist die Frage, *welcher Kontext* bei jeder Übergabe mitreist. Bekommt der empfangende Agent zu wenig, kann er die Aufgabe nicht erledigen. Bekommt er zu viel, wächst der Kontext, bis er das Kontextfenster sprengt, und der Worker verliert den Faden. Das ist die Multi-Agenten-Fassung des Satzes aus dem Tool-Einsatz, dass eine Tool-Definition ein Prompt ist – hier lautet er: *die Nachricht einer Übergabe ist ein Prompt*. Sie muss genau das tragen, was der nächste Agent zum Handeln braucht, und nichts darüber hinaus.

## Auch der Orchestrator ist nur ein Agent

Es liegt nahe, den Orchestrator für eine neue Art von Komponente zu halten. Das ist er nicht. Ein **Orchestrator** ist ein Agent, der drei längst bekannte Aufgaben zugleich erledigt:

- **Die Aufgabenzerlegung** – das Ziel in Teilaufgaben zerlegen, die Lektion über die Planung unmittelbar angewandt.
- **Das Routing** – jede Teilaufgabe dem richtigen Worker zuweisen. Das ist der Router aus Agentic RAG, nur weist er jetzt eine Teilaufgabe einem *Agenten* zu statt eine Abfrage einem Tool oder einem Index.
- **Die Synthese** – die Ergebnisse der Worker zur endgültigen Antwort zusammenfügen.

Seine ‚Tools‘ sind die Subagenten. Das ist der ganze Trick: begrifflich nichts Neues, nur die früheren Bausteine, jetzt auf Agenten angewandt statt auf Funktionen.

## Was es kostet und wann es sich nicht lohnt

Alles bisher war der Fall *dafür*. Jetzt die ehrliche Bremse, denn Multi-Agenten-Systeme sind die Stelle, an der Teams zu viel Geld ausgeben.

**Kosten und Latenz vervielfachen sich.** N Agenten bedeuten größenordnungsmäßig das N-Fache an Modellaufrufen gegenüber einem einzelnen Agenten. Das ist ein Sprung nach oben, bei den Kosten wie bei der Latenz – umsonst ist das nicht.

**Fehler pflanzen sich fort.** Der Fehler eines Agenten vergiftet alles, was danach kommt. Nichts dient allen als Ground Truth, also nimmt der nächste Agent in der Reihe ein falsches Zwischenergebnis schlicht als Tatsache.

**Die Koordination kostet extra.** Agenten können aneinander vorbeireden, dieselbe Arbeit doppelt tun oder sich gegenseitig blockieren, während jeder auf den anderen wartet.

**Fehlersuche und Evaluierung werden schwerer.** Der Pfad, den ein Durchlauf genommen hat, verteilt sich jetzt über mehrere Agenten, und die Observability muss die Teile zu einem zusammenhängenden Trace *zusammensetzen*. Das verschärft den Punkt aus Planung und Schleifen, dass Sie den ganzen Pfad verfolgen müssen – jetzt liegt er nicht einmal mehr an einer Stelle.

Daraus die Regel. Ein einzelner, gut entworfener Agent gewinnt meistens. Greifen Sie erst dann zu mehreren, wenn es echte Spezialisierung zu nutzen gibt, wenn der Kontext in kein einziges Kontextfenster passt oder wenn sich Teilaufgaben wirklich parallel bearbeiten lassen – dieselbe Disziplin wie in Agentic RAG: die einfachste Stufe nehmen, die die Aufgabe löst.

## Ein Beispiel, das Sie vermutlich schon verwendet haben

Die Redaktions- und Autorenteams, die ein Handbuch wie dieses hervorbringen, *sind* Multi-Agenten-Systeme nach dem Muster Orchestrator-Worker. Ein führender Agent – wer die Redaktion leitet oder den Text federführend schreibt – zerlegt die Arbeit und weist sie unabhängigen Spezialisten zu: dem Sprachlektorat, der naiven Erstlektüre, der Faktenprüfung, der Übersetzung. Danach fügt sie deren Berichte zu einer fertigen Seite zusammen. Dass diese Spezialisten einander nicht zu sehen bekommen, ist Absicht, und zwar aus genau dem Grund, der oben für die Debatte galt: Unabhängige Blickwinkel finden mehr als eine einzelne Prüfung, die alles nacheinander liest.

Deep-Research-Systeme haben dieselbe Gestalt. Ein führender Agent startet mehrere suchende Agenten, die parallel arbeiten; die Synthese fügt danach zusammen, was jeder von ihnen gefunden hat. Dieselbe Topologie, eine andere Aufgabe.

## Das Wichtigste

- Ein Multi-Agenten-System ist die teurere Stufe, keine Belohnung – nehmen Sie die einfachste Stufe, die die Aufgabe löst, und seien Sie ebenso bereit zu sagen, *wann nicht*, wie zu sagen, *wann doch*.
- Sie teilen einen Agenten aus vier Gründen auf: Spezialisierung (schmale Rolle, kleiner überschneidungsfreier Tool-Katalog), Isolation der Kontexte (jeder Agent sein eigenes Kontextfenster, der Orchestrator sieht nur Ergebnisse – der Grund, der wirklich skaliert), Modularität und Parallelität.
- Vier Standardtopologien: Orchestrator-Worker (ein führender Agent zerlegt, weist zu, fügt zusammen – die häufigste), die Kette (jeder Agent verarbeitet die vorherige Ausgabe weiter), die Hierarchie (Orchestratoren über Orchestratoren) und die Debatte zwischen Agenten mit einem Kritiker (unabhängige Blickwinkel machen das Ergebnis besser).
- Agenten verständigen sich über Nachrichten; eine Übergabe reicht Kontrolle und Kontext weiter, und *die Nachricht einer Übergabe ist ein Prompt* – sie trägt genau das, was der Empfänger braucht, und nicht mehr.
- Ein Orchestrator ist bloß ein Agent: zerlegen, zuweisen, zusammenfügen, mit den Subagenten als seinen Tools. Nichts Neues, nur die alten Bausteine, jetzt auf Agenten angewandt.
- Die Bremse: Kosten und Latenz vervielfachen sich (etwa das N-Fache), Fehler pflanzen sich fort, weil nichts allen als Ground Truth dient, die Koordination kostet extra, und Fehlersuche und Evaluierung werden schwerer (der Pfad muss über die Agenten hinweg zusammengesetzt werden). Ein einzelner, gut entworfener Agent gewinnt meistens.
- Eines haben Sie schon gesehen: Das Redaktions- und Autorenteam hinter einem Handbuch und Deep-Research-Systeme sind Teams nach dem Muster Orchestrator-Worker – ein führender Agent zerlegt, weist unabhängigen Spezialisten zu und fügt zusammen.

**[Neue Begriffe](../../glossary.md#multi-agent)**: multi-agent system, orchestrator / supervisor, worker / sub-agent, handoff, agent chain, critic / debate.

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Protokolle und Koordination](./deep-dive.md)** – ein tieferer Durchgang durch die Frage, wie sich ein Team aus Agenten tatsächlich abstimmt und wie Sie es funktionsfähig und bezahlbar halten: konkrete Protokolle und Nachrichtenschemata zwischen Agenten, Architekturen mit gemeinsamem Gedächtnis (das Blackboard), Muster für Rollenverteilung und Verhandlung, eine Evaluierung, die den Pfad über die Agenten hinweg zusammensetzt, und Kostenregeln für Agententeams.

Siehe auch: wie Orchestrator und isolierte Worker bei Claude, OpenAI und Gemini gebaut werden – [der Abschluss dieses Teils](../real-agents.md); die allgemeine Schicht für Schleifensteuerung und Budget, auf der diese Teams aufsetzen – [Planung und Schleifen](../planning-loops/index.md).

:::
