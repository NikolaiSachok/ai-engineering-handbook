---
title: Ingestion
slug: /part-1-rag/ingestion/
---

# Von Dokumenten zu einem durchsuchbaren Index

Die Ingestion ist die vorgelagerte Hälfte von RAG: alles, was mit Ihren Dokumenten geschieht, **bevor** die
erste Frage überhaupt gestellt wird. Alles, was später durchsucht wird, entsteht hier. Die Kette:
Dokumente parsen → **Chunking** → Metadaten → in eine Vektordatenbank einbetten.

Diese Seite behandelt **Chunking** und **Embedding-Modelle**, die beiden Säulen der Ingestion. Das Parsing
der Dokumente gehört in den zweiten Durchgang, die Vertiefung dieser Schicht; siehe den Hinweis am Ende der
Seite.

:::info[So lesen Sie diese Seite]

Jedes Thema steht zuerst so da, „wie es in der Branche üblich ist“. Alles, was an einem bestimmten Projekt
hängt (Strata-RAG), ist in eigene Fallstudienseiten ausgelagert – damit sich die Theorie nicht mit
Implementierungsdetails vermischt.

:::

---

## Chunking

### Warum ein Dokument überhaupt zerlegt werden muss

Das naive Rezept lautet: „Zerlegen Sie das Dokument in Chunks.“ Aber *warum* zerlegen – und warum ist das die Stelle,
an der zuerst alles schiefgeht?

Zwei voneinander unabhängige Zwänge erzwingen die Zerlegung:

1. **Ein Embedding-Modell presst ein ganzes Textstück in einen einzigen Vektor.** Je größer und je bunter
   dieses Stück, desto mehr mittelt der Vektor die Unterschiede weg. Der Vektor eines Absatzes über einen einzigen
   Gedanken ist scharf. Der Vektor eines vollständigen Handbuchs von 40 Seiten ist eine verwaschene Wolke,
   die zu *jeder* konkreten Frage schlecht passt.
2. **Ein Chunk ist zugleich die Einheit der Suche und die Einheit dessen, was das Modell zu sehen bekommt.**
   Gesucht wird über Chunks, und die gefundenen Chunks sind es, die dem Modell vorgelegt werden. Behalten
   Sie das für den ganzen Abschnitt im Kopf: Ein Chunk spielt zwei Rollen gleichzeitig, und die beiden
   stellen entgegengesetzte Anforderungen an seine Größe.

### Die zentrale Abwägung: großer Chunk oder kleiner Chunk

Alles in diesem Abschnitt läuft auf eine einzige Tabelle hinaus:

| | Chunk zu **groß** | Chunk zu **klein** |
|---|---|---|
| Wirkung auf das Embedding | Der Vektor wird unscharf → er passt schlecht zu einer konkreten Frage | Der Vektor ist scharf |
| Wirkung auf den Kontext des Modells | Viel Rauschen, das Relevante geht darin unter (der **Lost-in-the-Middle**-Effekt: Anfang und Ende eines langen Kontexts nimmt das Modell besser wahr als die Mitte), teuer in Token | Die Bedeutung geht verloren – der Chunk ergibt für sich genommen keinen Sinn |
| Typisches Fehlerbild | Sie bekommen etwas grob zum Thema, aber die Tatsache, die Sie brauchten, ist darin verdünnt | Sie bekommen einen Chunk, der für sich genommen nichts bedeutet |

Das klassische Beispiel für einen zu kleinen Chunk ist der verlorene **Bezug**. Ein Satz aus einem Bericht:

> „Im dritten Quartal ist er um 20 % gewachsen.“

Als eigenständiger Chunk ist das wertlos: *Was* ist „er“? Das Quartal welchen Jahres? Das Embedding eines
solchen Satzes passt zu nichts Sinnvollem, und selbst wenn es doch auftaucht, kann das Modell nichts damit
anfangen. Der Kontext („er“ = der Umsatz der Sparte X für 2025) ist im Nachbarabsatz geblieben, und der hat
es nicht in diesen Chunk geschafft.

Deshalb scheitert der Ansatz „einfach alle N Zeichen schneiden“ – und deshalb sind klügere Strategien
entstanden.

### Chunking-Strategien (von einfach bis ausgefeilt)

1. **Feste Größe.** Alle N Token oder Zeichen schneiden – die Grundlage, auf der alles Weitere aufbaut.
   Einfach, schnell, reproduzierbar. Der Nachteil: Es wird blind geschnitten, mitten im Satz, mitten in der
   Tabelle.
2. **Overlap.** Benachbarte Chunks überlappen einander – ein gleitendes Fenster. Fällt eine Tatsache genau
   auf die Schnittkante, überlebt sie in mindestens einem der beiden Nachbarn unversehrt, sofern sie kürzer
   ist als die Überlappung. Ein billiges Mittel gegen halbierte Tatsachen, bezahlt mit doppeltem Text.
   Angewendet wird es fast immer, zusätzlich zu jeder anderen Strategie; üblich sind etwa 10–20 % der
   Chunk-Größe.
3. **Rekursiv oder strukturell.** **Der Standardfall in der Praxis**, der Kompromiss, der einfach ist und
   fast immer trägt: Statt blind zu schneiden, wird an natürlichen Grenzen geschnitten, und zwar
   hierarchisch – zuerst nach Abschnitten, dann, wenn ein Stück immer noch zu groß ist, nach Absätzen, dann
   nach Sätzen. So fallen die Chunk-Grenzen mit den Gedankengrenzen zusammen.
4. **Semantisch.** Hier entscheiden die Embeddings der einzelnen Sätze über die Grenze: Solange benachbarte
   Sätze einander im Sinn nahe sind, bilden sie einen Chunk; ein scharfer Abfall der Ähnlichkeit zeigt einen
   Themenwechsel an, also eine Grenze. So entstehen Chunks, die möglichst genau von einer Sache handeln. Der
   Nachteil: Es ist teurer, weil schon beim Zerlegen eingebettet werden muss, und es verdient seinen Preis
   nicht immer.
5. **An der Dokumentstruktur orientiert.** Bei Dokumenten aus dem Unternehmen – Richtlinien, Verträgen,
   Tabellen – entscheidet oft genau das über die Qualität. Maßgeblich sind die Auszeichnungen im
   Quelldokument: Überschriften, Tabellen, Codeblöcke. Eine Tabelle wird nicht Zeile für Zeile zerschnitten,
   Code nicht mitten in einer Funktion auseinandergerissen, und der **Überschriftenpfad** („Kapitel 3 ›
   Abschnitt 2 › Auszahlungsbedingungen“) wandert in die Metadaten des Chunks.

:::tip[Eine allgemeingültige Chunk-Größe gibt es nicht]

Sie hängt vom Dokumenttyp ab (dichter Rechtstext ≠ lockerer Chatverlauf) und vom Fragetyp (eine punktgenaue
Tatsache ≠ die Bitte, eine ganze Richtlinie zu erklären). Die Chunk-Größe wird deshalb nicht geraten,
sondern **gemessen**: Vergleichen Sie die Varianten in einer Evaluierung des Retrievals und sehen Sie sich
die Metriken an. Das ist die Brücke zur Schicht [Evaluierung](../cross-cutting/evaluation/index.md):
Chunking ist nichts, was man einmal einstellt und dann vergisst, sondern ein Parameter, den Sie anhand von
Metriken immer wieder anpassen.

:::

### Chunk-Metadaten – was ein Chunk außer seinem Text noch mitträgt

Ein Chunk ist nicht nur Text. Sie hängen ihm **Metadaten** an: die Quelle (Datei oder URL), den Titel, den
Überschriftenpfad, das Datum, die Version und – im Unternehmen entscheidend – die **Zugriffssteuerung**, also
wer ihn sehen darf. Drei Gründe, das genau hier festzulegen:

- **Filtern:** „nur in Dokumenten nach 2024 suchen“ oder „nur im Bereich Personal“ – dazu **filtern Sie
  zusätzlich zur Vektorsuche nach Metadaten**.
- **Quellenangaben:** Damit eine Antwort auf Abschnitt 2 der Urlaubsregelung verweisen kann, muss dieser
  Verweis von Anfang an mit dem Chunk mitreisen.
- **Zugriffssteuerung:** In einem Unternehmenssystem darf jemand aus dem Marketing in einer Antwort keinen
  Ausschnitt aus der Gehaltsliste zu sehen bekommen. Die Berechtigungen werden auf der Ebene des einzelnen
  Chunks geprüft, und die nötige Angabe dazu steht in den Metadaten.

**Das Entscheidende:** Metadaten werden beim Chunking festgelegt. Was Sie dort nicht angehängt haben, steht
später nirgends mehr zur Verfügung.

### Ein Ausblick: Ein Chunk hat zwei Rollen, und sie lassen sich trennen

Ein Chunk ist die Sucheinheit, und derselbe Chunk wird dem Modell vorgelegt – dabei muss es sich gar nicht
um dasselbe Textstück handeln. Die [Vertiefung zum Retrieval](../retrieval/deep-dive.md) führt die Idee aus: Sie können über kleine,
scharfe Chunks *suchen* (ein gutes Embedding) und dem Modell ein größeres übergeordnetes Textstück rund um
den Treffer *vorlegen* (der volle Kontext). Diese Verfahrensfamilie
heißt *Parent-Document*- bzw. *Small-to-Big-Retrieval*. Für den Moment genügt es zu wissen, dass sich die
zwei Rollen eines Chunks trennen lassen.

### Das Wichtigste

- Ein Chunk ist zugleich **Sucheinheit und Lesestoff für das Modell** – zwei Rollen, deren Anforderungen an
  die Größe einander widersprechen.
- Zu groß → ein verwaschenes Embedding und Rauschen; zu klein → verlorener Kontext und verlorene Bezüge.
- Die Strategien: feste Größe → **plus Overlap** → **rekursiv (der Standardfall)** → semantisch → an der
  Dokumentstruktur orientiert.
- Die **Metadaten** (Quelle, Überschriftenpfad, Datum, Berechtigungen) werden hier festgelegt und ermöglichen später das
  Filtern, die Quellenangaben und die Zugriffssteuerung.
- Die Chunk-Größe wird **gemessen**, nicht geraten.

**[Neue Begriffe](../../glossary.md#ingestion-chunking)**: chunk, chunk overlap, recursive / structural
chunking, semantic chunking, chunk metadata, parent-document (small-to-big) retrieval.

---

## Embedding-Modelle

Die grobe Mechanik kennen Sie: Chunk → Vektor → Vektordatenbank. Hier folgen die Feinheiten, die den Unterschied
zwischen „ich habe ein Video gesehen“ und „ich verstehe, warum es so gebaut ist“ ausmachen.

### Was ein Embedding ist

Ein Embedding ist ein Vektor in einem Raum, in dem geometrische Nähe **Nähe in der Bedeutung** heißt. Das
Modell ist eine trainierte Funktion „Text → Vektor“: Texte über dieselbe Sache landen nahe beieinander,
unverwandte weit auseinander. Suchen heißt dann: die Vektoren finden, die dem Vektor der Frage am nächsten
liegen.

Daraus folgt das Wichtigste: Die Qualität des Retrievals ist durch die Qualität der Embeddings nach oben
begrenzt. Ist der Vektor des benötigten Chunks nicht in der Nähe des Fragevektors gelandet, kann ihn weiter
unten in der Pipeline fast nichts mehr retten – die hybride Suche mildert den Schlag nur ab, mehr dazu in
der Schicht Retrieval. Deshalb legt die Wahl des Modells das Fundament für das gesamte Retrieval.

:::tip[▶ Video]

<YouTube id="wgfSDrqYMJ4" title="What are Word Embeddings? — IBM Technology" />

Das Video handelt von **Wort**-Embeddings, der historischen Wurzel der Idee; in RAG betten wir ganze Chunks
ein – dasselbe Prinzip, vom Wort auf ein ganzes Textstück hochskaliert. (Das Video ist auf Englisch.)

:::

### Bi-Encoder vs. Cross-Encoder

Aus dieser einen Unterscheidung gehen sowohl die Vektorsuche als auch das Reranking hervor.

| | **Bi-Encoder** | **Cross-Encoder** |
|---|---|---|
| Wie er rechnet | Kodiert Frage und Chunk getrennt → zwei Vektoren → vergleicht sie anhand ihres Abstands | Bekommt das Paar (Frage und Chunk) zusammen → gibt eine einzige Relevanzzahl aus |
| Genauigkeit | Geringer (er sieht die Texte getrennt) | Höher (er sieht das Zusammenspiel der Wörter) |
| Geschwindigkeit | Schnell | Langsam |
| Vorberechnung | **Ja** – die Chunk-Vektoren werden einmalig beim Indexieren berechnet | **Nein** – der Score muss für jedes Paar neu berechnet werden |
| Wo er eingesetzt wird | **Vektorsuche** über die gesamte Datenbank | **Reranking** der Top-K-Treffer |

Deshalb werden beide kombiniert: Der Bi-Encoder zieht aus Millionen von Chunks schnell die Top-K-Treffer
heraus (**Recall** – wie viel von dem Gebrauchten überhaupt in die Liste kommt). Der Cross-Encoder bewertet diese Treffer anschließend neu und hebt
die wirklich passenden nach vorn (**Precision** – wie viel von dem, was in der Liste steht, wirklich passt). Genau diese Neubewertung ist das
**Reranking**. Mehr dazu in der Schicht [Retrieval](../retrieval/index.md).

### Wie Sie ein Embedding-Modell auswählen

- **Für das Retrieval trainiert (retrieval-optimiert).** Nicht jedes Modell ist für die Suche trainiert. Sie
  brauchen eines, das auf Paaren aus Frage und Passage trainiert wurde, nicht auf allgemeiner
  Satzähnlichkeit.
- **Die Dimensionszahl des Vektors** (384 / 768 / 1536 und mehr). Mit mehr Dimensionen lassen sich feinere Unterschiede
  abbilden, aber es wird teurer: Speicher, Suchgeschwindigkeit, Geld. Größer heißt nicht immer besser.
- **Sprache und Domäne.** Ein Modell, das im Englischen stark ist, kann bei russischem Text, bei
  Rechtstexten oder bei Code deutlich nachlassen. Für mehrsprachige Inhalte im Unternehmen ist das
  entscheidend.
- **Die Obergrenze für die Eingabelänge** bestimmt, bis zu welcher Chunk-Größe das Modell die Eingabe
  überhaupt annimmt. Das bindet die Modellwahl unmittelbar ans Chunking.
- **API oder Eigenbetrieb.** Eine proprietäre API (OpenAI, Cohere, Voyage) ist einfach und leistungsfähig;
  dafür verlassen Ihre Daten Ihre eigene Infrastruktur, und pro Aufruf fallen Kosten an. Offene, selbst
  betriebene Modelle (E5, BGE, gte) halten Ihre Daten im Haus – im Unternehmen oft ausschlaggebend – und kosten pro Aufruf nichts; dafür betreiben Sie die Infrastruktur selbst.

### Das Ähnlichkeitsmaß in Kürze

Die **Kosinus-Ähnlichkeit** (der Winkel zwischen zwei Vektoren; sie berücksichtigt die Richtung und
ignoriert die Länge) ist die Standardwahl. Viele Modelle liefern **normierte** Vektoren; bei ihnen fällt die
Kosinus-Ähnlichkeit praktisch mit dem Skalarprodukt zusammen. Die Regel lautet: Nehmen Sie das Maß, für das
das Modell trainiert wurde – es steht in dessen Modellbeschreibung (*model card*). Passen Maß und Modell nicht
zusammen, sinkt die Qualität.

### Zwei Fehler, die immer wieder passieren

- **Verschiedene Modelle für Fragen und für Dokumente.** Sie haben die Dokumente mit dem einen Modell
  eingebettet und die Fragen mit einem anderen → die Vektoren liegen in verschiedenen Räumen, und die Ergebnisse sind Unsinn.
  Daraus folgt: Wer das Modell wechselt, muss das gesamte Korpus neu indexieren.
- **Frage und Passage brauchen verschiedene Präfixe.** Retrieval-Modelle erwarten eine Kennzeichnung
  (`query:` / `passage:`); verwechseln Sie die beiden, sinkt die Qualität still und leise.

### Das Wichtigste

- **Bi-Encoder** (schnell, vorberechnet, also die Vektorsuche) vs. **Cross-Encoder** (genau, pro Paar,
  also das Reranking).
- Die Qualität des Retrievals ist durch die Qualität der Embeddings nach oben begrenzt.
- Bei der Auswahl zählen: retrieval-optimiert · Dimensionszahl · Sprache und Domäne · Eingabelänge ·
  **API oder Eigenbetrieb (Datenschutz)**.
- Verwenden Sie für Frage und Dokument dasselbe Modell, und achten Sie auf das Ähnlichkeitsmaß und auf die
  Präfixe.

**[Neue Begriffe](../../glossary.md#ingestion-chunking)**: embedding, embedding space, bi-encoder,
cross-encoder, dimensionality, cosine similarity, retrieval-optimised (asymmetric) embeddings, multilingual
embeddings, self-hosted vs API embeddings.

:::tip[▶ Video]

<YouTube id="t9IDoenf-lo" title="What is a Vector Database? — IBM Technology" />

Das Video führt zur nächsten Schicht hinüber: Es zeigt, wo die Chunk-Vektoren abgelegt werden und wie man
darin schnell die nächsten Nachbarn findet. (Das Video ist auf Englisch.)

:::

---

:::note[Als Nächstes: Teil 2 der Lektion]

**[Parsing und fortgeschrittene Embeddings](./deep-dive.md)** – der zweite Durchgang durch die
Ingestion-Schicht: das Parsing der Dokumente (PDF, Tabellen, HTML, OCR, Layouterkennung),
fortgeschrittenes Chunking (Late Chunking und Contextual Retrieval) und mehr zu den Embeddings selbst
(Fine-Tuning, das Kürzen der Vektoren nach Matryoshka, mehrsprachige Modelle).

Siehe auch: was mit den Chunks als Nächstes geschieht – [Retrieval](../retrieval/index.md); wie die Antwort
zusammengesetzt wird – [Generation](../generation/index.md); und wie die ganze Schicht gemessen wird –
[Evaluierung](../cross-cutting/evaluation/index.md).

:::
