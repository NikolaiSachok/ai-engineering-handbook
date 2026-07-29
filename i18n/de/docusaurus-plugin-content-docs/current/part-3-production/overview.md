---
id: overview
title: Teil III – Produktivbetrieb und LLMOps
sidebar_label: Überblick
---

# Teil III – Produktivbetrieb und LLMOps

In Teil I und Teil II ist das System entstanden: zuerst eine statische RAG-Pipeline, dann die Agenten,
die darauf aufsetzen. In Teil III geht es darum, **wie Sie es tatsächlich in den Produktivbetrieb
bringen**: Bereitstellung, Cloud-Plattformen, das Tooling-Ökosystem und der laufende Betrieb. Das ist
die Schicht, auf die es in der Praxis ankommt; in Stellenanzeigen wird sie zu einer Liste von
Werkzeugnamen. Sie trennt „läuft auf meinem Laptop“ von „läuft unter Last, lässt sich dabei
beobachten und bleibt im Kostenrahmen“.

## Was Sie hier finden

- **[Bereitstellung und Betrieb – FastAPI + Docker](./serving/index.md)** – ein Modell oder einen Agenten
  als Dienst verpacken: API, Streaming, Container, Inferenz-Engines (*inference server*).
- **[Cloud-KI-Plattformen](./cloud-platforms/index.md)** – [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service), [Amazon Bedrock](https://aws.amazon.com/bedrock/), Google Cloud Gemini
  Enterprise Agent Platform (vormals [Vertex AI](https://cloud.google.com/vertex-ai)): was sie anbieten und worin sie sich unterscheiden.
- **[Das Tooling-Ökosystem](./tooling-ecosystem/index.md)** – Evaluierung, Guardrails und Observability im
  Produktivbetrieb: was Sie messen, was Sie absichern, was Sie sehen.
- **[LLMOps – ausrollen, überwachen, Kosten](./llmops/index.md)** – das Leben des LLM-Systems nach dem Release.

## Voraussetzungen

Teil I und Teil II vollständig – Bereitstellung und laufender Betrieb setzen voraus, dass Sie den
RAG-Agenten selbst schon gebaut haben und verstehen.

:::note[Bearbeitungsstand]

Teil III ist abgeschlossen. Jede Lektion ist veröffentlicht – Bereitstellung und Betrieb,
Cloud-KI-Plattformen, das Tooling-Ökosystem und LLMOps –, und zu jeder gehört inzwischen ein zweiter,
ausführlicher Durchgang: die Vertiefung. Folgen Sie auf einer Lektionsseite dem Hinweis „Als Nächstes:
Teil 2 der Lektion“, um zur zugehörigen Vertiefung zu kommen.

:::
