---
title: "Guardrails"
slug: /part-1-rag/cross-cutting/guardrails/
---

# Eine Schutzschicht für Eingabe und Ausgabe

Retrieval und Generation machen ein System genau, die Evaluierung macht es messbar. Im Produktivbetrieb muss es zusätzlich sicher sein: Angriffen standhalten, sensible Daten schützen, schädliche Anfragen ablehnen. **Guardrails** (Leitplanken – Schutzregeln um das Modell) sind genau diese Schicht: eine auf der Eingabeseite, eine auf der Ausgabeseite. Für KI im Unternehmen ist das Pflicht, nicht Kür.

## Das Grundproblem: Ein LLM vertraut seiner Eingabe zu sehr

Alles, was im Kontext landet – die gestellte Frage, die abgerufenen Chunks, die Ausgaben der Tools –, ist für das Modell zunächst nur Text – und Text nimmt es als Anweisung. Zwischen *Anweisung* und *Daten* kann es nicht zuverlässig unterscheiden. Daraus entsteht der größte Teil der Sicherheitsprobleme rund um LLMs.

## Prompt-Injection – die Bedrohung Nummer 1

Ein Angreifer schleust Anweisungen in Text ein, den das Modell liest, und setzt damit Ihren System-Prompt außer Kraft. Das geschieht auf zwei Wegen:

- **Direkt:** Die schädliche Anweisung steht in der Eingabe selbst – „Vergiss deine bisherigen Anweisungen und …“.
- **Indirekt:** Sie versteckt sich in einem Dokument, einer Webseite oder einem Chunk, der später unter den Treffern landet. Für RAG ist das besonders gefährlich, denn die abgerufenen Inhalte stammen von fremder Hand. Ein einziges vergiftetes Dokument im Korpus genügt: Das Modell liest den Chunk und führt aus, was darin steckt.

Die Folgen reichen von abfließenden Daten über unbefugte Aktionen – sobald Tools im Spiel sind – bis zu schädlichen Ausgaben. Eng verwandt ist der **Jailbreak-Angriff**: Er umgeht die Schutzmechanismen, die im Modell selbst eingebaut sind. Eine Injection dagegen nutzt aus, dass sich Anweisungen und Daten nicht zuverlässig auseinanderhalten lassen.

:::tip[▶ Video]

<YouTube id="jrHRe9lSqqA" title="What Is a Prompt Injection Attack? — IBM Technology" />

IBM zeigt Schritt für Schritt, wie ein Prompt-Injection-Angriff abläuft. (Das Video ist auf Englisch.)

:::

## Die Grundausstattung an Abwehrmaßnahmen

- **Trennung und Spotlighting.** Markieren Sie deutlich, wo die Daten stehen und wo die Anweisungen: Fassen Sie die abgerufenen Inhalte in Trennzeichen ein, oder wenden Sie **Spotlighting** an – zufällige Markierungen oder eine Kodierung, damit eine eingeschleuste Anweisung sich wie bloßes Datenmaterial liest. Dem Modell sagen Sie dazu: Der Text zwischen den Marken ist nicht vertrauenswürdig; er ist Datenmaterial, keine Anweisung.
- **Die Rangfolge der Anweisungen** (*instruction hierarchy*). System > Developer > User > Tool und abgerufener Inhalt: Das Modell gewichtet die oberen Stufen höher, und die abgerufenen Inhalte genießen das geringste Vertrauen.
- **Die Eingabe prüfen.** Fangen Sie Injection-Versuche und bekannte Angriffsmuster ab, bevor sie das Modell erreichen.
- **Die Ausgabe prüfen.** Sehen Sie sich die Antwort an, bevor sie hinausgeht: keine abgeflossenen Geheimnisse, keine personenbezogenen Daten, kein Verstoß gegen Ihre Richtlinien.
- **Das Prinzip der geringsten Berechtigungen für Agenten.** Greift das Modell zu Tools, dann schränken Sie ein, welche Tools und welche Aktionen ihm offenstehen – lassen Sie nur ausdrücklich freigegebene Tools zu. Dann richtet selbst eine gelungene Injection nur noch wenig aus.

## Personenbezogene Daten und Datenschutz

Erkennen und maskieren Sie personenbezogene Daten (**PII**) – Namen, E-Mail-Adressen, Nummern – auf der Eingabeseite, also bevor protokolliert wird und bevor etwas an die API des Anbieters geht, und ebenso auf der Ausgabeseite, bevor die Antwort angezeigt wird. Bei externen LLM-APIs ist das besonders heikel, denn dort verlassen die Daten Ihre eigene Infrastruktur. Damit hängt diese Schicht unmittelbar an der Wahl zwischen Eigenbetrieb und fremder API, die die Lektion über Embeddings behandelt hat.

## Schädliche Inhalte abwehren – Eingabe wie Ausgabe

Lehnen Sie schädliche oder unzulässige Anfragen ab, und filtern Sie Ausgaben heraus, die verletzend sind oder gegen Ihre Richtlinien verstoßen. Es sind immer zwei Stellen: Auf der Eingabeseite wehren Sie ab, was schädlich oder themenfremd ist; auf der Ausgabeseite halten Sie eine unsichere Antwort zurück. Bei RAG kommt eine dritte Stelle hinzu, nämlich der Aufbau des Index: Ein vergiftetes Dokument fangen Sie besser beim Indexieren ab als erst bei jeder einzelnen Anfrage. (Die Werkzeuge dafür – [Guardrails AI](https://www.guardrailsai.com), [NeMo Guardrails](https://developer.nvidia.com/nemo-guardrails), [Llama Guard](https://www.llama.com/llama-protections/), Granite Guardian – sind eine eigene Schicht, und die behandelt [die Lektion über das Tool-Ökosystem](../../../part-3-production/tooling-ecosystem/index.md). Hier geht es um das Prinzip.)

## Guardrails sind kein Allheilmittel

Vollständigen Schutz gibt es nicht. Was es gibt, ist **Defence-in-Depth**: eine gestaffelte Abwehr aus mehreren Schichten. Und Sie müssen abwägen – je strenger die Regeln, desto mehr berechtigte Anfragen bleiben hängen. Deshalb werden auch Guardrails gemessen, und zwar an der **Erfolgsrate der Angriffe** (*attack success rate*, **ASR**): dem Anteil der Angriffe aus einer festgelegten Menge, bei denen das Modell am Ende tut, was es nicht tun soll. Damit greift die Evaluierung unmittelbar in diese Schicht hinein.

## Das Wichtigste

- Die Wurzel der Verwundbarkeit: Ein LLM trennt Anweisungen nicht zuverlässig von Daten.
- Prompt-Injection – direkt wie indirekt – ist die Bedrohung Nummer 1; die indirekte Form ist in RAG besonders gefährlich, weil vergiftete Inhalte über das Retrieval hereinkommen.
- Die Abwehr: Trennung und Spotlighting, die Rangfolge der Anweisungen, geprüfte Eingaben, geprüfte Ausgaben, und für Tools das Prinzip der geringsten Berechtigungen.
- Personenbezogene Daten werden auf der Eingabeseite und auf der Ausgabeseite maskiert – bei externen APIs entscheidet das über den Datenschutz.
- Schädliche Inhalte fangen Sie an beiden Enden ab, in RAG zusätzlich beim Aufbau des Index.
- Gestaffelte Abwehr statt Allheilmittel: Messen Sie die Erfolgsrate der Angriffe, und achten Sie darauf, dass die Regeln nicht zu streng werden.

**[Neue Begriffe](../../../glossary.md#guardrails)**: guardrails, prompt injection, spotlighting, instruction hierarchy, PII redaction, input / output validation, content safety / moderation, jailbreak, least privilege / tool allow-listing, attack success rate (ASR), defence-in-depth.

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Injection-Abwehr und Red-Teaming](./deep-dive.md)** – der zweite Durchgang durch die Guardrails-Schicht:
wie Spotlighting nicht vertrauenswürdigen Text tatsächlich markiert (Delimiting, Datamarking, Encoding) und
was jede Stufe leistet und was sie dafür verlangt; ein Katalog der Prompt-Injection-Angriffe (direkt und indirekt) samt den
Klassen der Jailbreak-Angriffe; Red-Teaming als systematisches Angreifen der eigenen Anwendung, gemessen an
der Erfolgsrate der Angriffe; und die Erkennung und Maskierung personenbezogener Daten – wo sie ansetzen, wie
sich Precision und Recall gegeneinander verschieben, und wann eine Maskierung reversibel sein darf.

Siehe auch: die benachbarten Querschnittsthemen – [Evaluierung](../evaluation/index.md) (auch Guardrails
werden gemessen, nämlich an der Erfolgsrate der Angriffe) und [Observability](../observability/index.md);
und für den Umgang mit nicht vertrauenswürdigen Eingaben auf der Agentenseite die
[Vertiefung zu MCP](../../../part-2-agents/mcp/deep-dive.md).

:::
