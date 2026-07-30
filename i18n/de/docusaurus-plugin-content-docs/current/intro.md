---
id: intro
title: Einführung
sidebar_position: 1
slug: /
---

# Enterprise RAG & Agents Handbook

Ein praktischer, aus den Grundprinzipien hergeleiteter Leitfaden zu RAG (Retrieval-Augmented Generation) und
Agenten im Produktivbetrieb: nicht „welche Werkzeuge es gibt“, sondern **warum** ein System so gebaut ist,
wie es ist – und wo es versagt. Das Handbuch wird fortlaufend erweitert: Es wächst Schicht für Schicht,
während der Kurs voranschreitet.

## Für wen dieses Handbuch ist

Es spielt drei Rollen gleichzeitig:

- **Kurs** – für alle, die RAG und Agenten wirklich verstehen wollen: mit dem „Warum“ und den Fehlerbildern,
  nicht nur mit einer Liste von Funktionen.
- **Nachschlagewerk des Autors** – eine dauerhafte Dokumentation der Entwurfsprinzipien und der getroffenen
  Entscheidungen.
- **Portfolio** – ein Nachweis professioneller Ingenieurspraxis: Evaluation, Guardrails, Observability,
  Entwurfsdisziplin.

Wir setzen Erfahrung voraus: Gängige Standardwerkzeuge (Vektordatenbanken, Orchestratoren) erklären wir nicht
von Grund auf – stattdessen zeigen wir das **KI-Delta**, also was sich tatsächlich ändert, wenn sie in einem
System mit einem Sprachmodell zum Einsatz kommen.

## Struktur

- **[Teil I – RAG](./part-1-rag/overview.md):** Ingestion, Retrieval, Generation und die Querschnittsthemen
  (Evaluation, Guardrails, Observability) der statischen Pipeline.
- **[Teil II – Agenten](./part-2-agents/overview.md):** Agentic RAG, Tool-Einsatz, Planung und Schleifen,
  Multi-Agenten-Systeme, Orchestrierungs-Frameworks, [MCP](https://modelcontextprotocol.io).
- **[Teil III – Produktivbetrieb und LLMOps](./part-3-production/overview.md):** Serving mit [FastAPI](https://fastapi.tiangolo.com) und Docker,
  Cloud-KI-Plattformen ([Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service), [Amazon Bedrock](https://aws.amazon.com/bedrock/), Google Cloud Gemini Enterprise Agent Platform –
  vormals [Vertex AI](https://cloud.google.com/vertex-ai)), das Tooling-Ökosystem (Evaluation, Guardrails, Observability) und LLMOps –
  Bereitstellung, Überwachung, Kosten. Das ist die Anwendungsschicht; in Stellenanzeigen erscheint sie als
  Liste von Werkzeugnamen.
- **[Glossar](./glossary.md):** einheitliche Definitionen der Begriffe, auf die die Seiten verweisen.

Jeder Teil beginnt mit einer Überblicksseite: womit er anfängt, was darin steht und was Sie vorher wissen
sollten.
