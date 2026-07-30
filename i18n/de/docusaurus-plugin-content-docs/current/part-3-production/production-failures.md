---
id: production-failures
title: Warum KI-Systeme im Produktivbetrieb versagen
sidebar_label: Warum KI im Betrieb versagt
sidebar_position: 0
---

# Acht Situationen, in denen ein funktionierendes Demo den Produktivbetrieb nicht übersteht

Ein Demo muss ein einziges Mal gelingen, auf einem Weg, den jemand ausgesucht hat. Ein Produktivsystem muss
allein zurechtkommen, auf Wegen, die niemand vorgezeichnet hat, viele tausend Mal am Tag, während die
Leute schlafen, die es gebaut haben. Das sind zwei verschiedene technische Aufgaben, und die Liste unten ist
die Quittung dafür, nur die erste gelöst zu haben.

Lesen Sie die acht Karten als Landkarte und nicht als Warnung. Jede benennt einen Fehler, zeigt die
Architektur, die ihn verhindert, und verweist auf die Lektion, in der der Mechanismus wirklich erklärt wird.
Einige kennen Sie schon – die Qualität des Retrievals aus Teil I, den Ausfall eines Tools aus Teil II. Der
Rest ist der Gegenstand dieses Teils. Und alle acht haben eines gemeinsam: **Fast nichts
davon ist ein Fehler des Modells.** Das Modell ist das eine Bauteil, das Sie nicht geschrieben haben. Alles
darum herum haben Sie gebaut.

:::note[Woher diese Landkarte kommt]

Diese acht Fehlerbilder machen in Diskussionen über KI im Produktivbetrieb die Runde;
den Anstoß zu dieser Anordnung gab eine viel geteilte Infografik von Alex Xu (ByteByteGo). Zwei Unterschiede
sind Absicht. Jene Fassung zeigt nur die Fehler, und für ein diagnostisches Plakat ist das der ehrliche
Zuschnitt – diese Karten stellen neben jeden Fehler die **Architektur für den Produktivbetrieb**, denn zu
wissen, dass Daten unordentlich ankommen, ist nicht dasselbe wie zu wissen, was zu bauen ist. Und an drei
Stellen sind wir mit dem verbreiteten Gegenmittel nicht einverstanden: beim Drift, bei den Datensätzen für
die Evaluierung und beim Umlenken auf ein günstigeres Modell. Jeder Einwand ist dort vermerkt, wo er
auftaucht.

:::

## 1 · Das Korpus ist das Produkt

<InfoCard
  title="Das Korpus ist das Produkt"
  caption="Die Ingestion im Produktivbetrieb weist aus, was sie aufgenommen hat, was sie ausgeschlossen hat und was sie nie zu sehen bekam.">
  <Lane kind="demo" label="DEMO">
    <Node icon="documentStack" label="saubere Dokumente, eine Sorte" />
    <Flow kind="fail" />
    <Branch>
      <Node icon="database" badge="tick" label="Index" />
      <Node icon="document" badge="cross" label="unbemerkt verworfen" />
    </Branch>
  </Lane>
  <Lane kind="production" label="PRODUKTION">
    <Node icon="mixedSources" label="gemischte Quellen" />
    <Flow />
    <Node icon="chunkedPage" label="Chunking nach Layout" />
    <Flow />
    <Node icon="clipboard" label="Ingestion-Manifest" />
  </Lane>
</InfoCard>

Das Korpus für ein Demo ist ein Ordner, den jemand von Hand zusammengestellt hat: saubere, gleichartige
Dokumente, alle von einer Sorte. Im Produktivbetrieb ist es eine Mischung aus Quellen – PDFs mit
zweispaltigem Satz, Tabellen, deren Bedeutung in der Kopfzeile steckt, Wiki-Seiten, die aus einem längst
eingestellten Werkzeug halb herübergezogen wurden, und Scans. Der übliche Rat, bei der Ingestion die
Schemata zu prüfen, trifft für strukturierte Einträge zu und greift bei Dokumenten nicht, denn was
eine RAG-Antwort zerlegt, ist selten ein fehlerhaft gefülltes Feld. Es ist die **Struktur**: eine Tabelle,
die zu Prosa plattgedrückt wurde, eine Fußzeile, die an jedem Chunk klebt, und vor allem eine Chunk-Grenze,
die eine Tatsache von der Einschränkung trennt, unter der sie überhaupt gilt. „Die Tarife stiegen um 4 %“
ist nicht falsch – bis Sie es von „nur im Pilotprojekt 2019“ abschneiden.

Schlimmer noch: Ein strenger Validierer schadet *unbemerkt*. Er verwirft die Dokumente,
die nicht in das Schema passen, der Index sieht anschließend gesund aus, und das Modell antwortet aus
einem unvollständigen Korpus – mit Überzeugung, denn niemand hat ihm gesagt, dass ein Drittel des
Ausgangsmaterials nie angekommen ist. Die Architektur für den Produktivbetrieb ist deshalb keine strengere
Prüfung, sondern ein **Manifest**: Die Ingestion weist aus, was sie *aufgenommen* hat, was sie
*ausgeschlossen hat und warum* und wo ihre *blinden Flecken* liegen – als Artefakt der Erstellung, das man
lesen kann. Ein ausgeschlossenes Dokument ist eine Entscheidung; ein ausgeschlossenes Dokument, das
niemand benennen kann, ist ein Defekt. Die Mechanik – das Parsing, das Layout, die Verfahren für das
Chunking, die Metadaten – steht in der Lektion zur [Ingestion](../part-1-rag/ingestion/index.md).

## 2 · Das Retrieval braucht das Recht, Nein zu sagen

<InfoCard
  title="Das Retrieval darf die Antwort verweigern"
  caption="Eine Untergrenze für die Relevanz hinter dem Reranking, und ein Generator, der „kein Kontext“ antworten darf.">
  <Lane kind="demo" label="DEMO">
    <Node icon="retrieval" label="top-K, immer" />
    <Flow kind="fail" />
    <Node icon="speechBubble" badge="bang" label="sicher, aber falsch" />
  </Lane>
  <Lane kind="production" label="PRODUKTION">
    <Node icon="sortedList" label="Reranking" />
    <Flow />
    <Node icon="gauge" label="Score-Untergrenze" />
    <Flow />
    <Branch>
      <Node icon="speechBubble" badge="tick" label="belegte Antwort" />
      <Node icon="speechBubbleEmpty" badge="tick" label="oder „kein Kontext“" />
    </Branch>
  </Lane>
</InfoCard>

Dieser Fehler kostet Teams die meiste Zeit, weil das System an jeder Stelle gesund aussieht. Nichts wirft
einen Fehler. Der Dienst antwortet mit 200. Es kommen einfach die falschen Chunks an, und das Modell tut,
wofür es gebaut ist – es schreibt eine flüssige Antwort aus allem, was es bekommen hat.

Das Retrieval getrennt von der Generation zu bewerten, ist die eine Hälfte der Aufgabe, die Diagnose; Teil
I begründet sie: Ohne diese Trennung unterscheiden Sie einen Fehlgriff des Retrievals nicht von einem
Modell, das guten Kontext übergangen hat, und Sie verbringen zwei Wochen damit, an einem Prompt zu feilen,
um einen Fehler in der Indexierung zu beheben. Was der Produktivbetrieb zusätzlich braucht, ist die
Möglichkeit, die Antwort zu verweigern, und genau die haben die meisten Demos nicht einmal im Entwurf. Ein
Demo gibt **immer top-K** zurück – top-K ist ein Ausschnitt und kein Urteil, und ein Ranking nach
Ähnlichkeit liefert seine fünf besten Kandidaten, ob nun einer davon Ihre Frage betrifft oder keiner.
**Setzen Sie eine Score-Untergrenze hinter der Stufe an, deren Scores etwas bedeuten.** Die zusammengeführten
Scores einer hybriden Suche – das Ranking aus der dichten und das aus der lexikalischen Suche, in einem
zusammengefasst – sind nicht auf eine vergleichbare Skala kalibriert, ein Schwellenwert auf einem solchen
Score ist deshalb annähernd willkürlich; der Score eines Cross-Encoder-Rerankers ist der, für den Sie eine
Untergrenze wirklich festlegen können. Oberhalb der Untergrenze ist die Antwort **belegt** – jede Aussage
stützt sich auf eine Passage, die die Hürde genommen hat. Unterhalb davon gibt das Retrieval **absichtlich
eine leere Menge zurück**, und der Generator sagt, dass ihm der stützende Kontext fehlt, statt aus einer
schwachen Ausbeute etwas Plausibles zusammenzusetzen.

Der letzte Schritt gelingt nur einem Generator, der die Antwort auch verweigern kann – dafür argumentiert
die [Generation](../part-1-rag/generation/index.md) ausführlich, und das
[Retrieval](../part-1-rag/retrieval/index.md) liefert die hybride Suche und das Reranking, ohne die eine
sinnvolle Untergrenze gar nicht möglich ist. Das Demo antwortet auf alles. Das Produktivsystem darf Nein
sagen.

## 3 · Ein Datensatz für die Evaluierung genügt nicht

<InfoCard
  title="Zwei Datensätze, nicht einer"
  caption="Jeder beantwortet eine andere Frage: Läuft noch, was vorher lief? Und passt meine Evaluierung noch zur Wirklichkeit?">
  <Lane kind="demo" label="DEMO">
    <Node icon="clipboard" label="Datensatz, Woche 1" />
    <Flow kind="fail" />
    <Node icon="dashboard" badge="bang" label="falsche Sicherheit" />
  </Lane>
  <Lane kind="production" label="PRODUKTION">
    <Merge>
      <Node icon="clipboard" badge="padlock" label="fester Datensatz" />
      <Node icon="speechBubbleGroup" label="Stichprobe aus dem Verkehr" />
    </Merge>
    <Flow />
    <Node icon="scales" label="ehrliches Bild der Qualität" />
  </Lane>
</InfoCard>

Testfälle aus der ersten Woche beschreiben, wie sich das Team vorgestellt hat, dass Leute fragen. Nach
einem halben Jahr im Produktivbetrieb wissen Sie, wie sie tatsächlich fragen, und in dieser Lücke fängt
ein grünes Dashboard an zu lügen. Der übliche Rat lautet, wöchentlich eine Stichprobe aus dem laufenden
Verkehr zu ziehen und sie als Maßstab zu nehmen – und hier steht unser erster Einwand, denn den festen
Datensatz zu *ersetzen* tauscht eine Blindheit gegen eine andere. Ein Maßstab, der sich jede Woche ändert,
sagt Ihnen nicht, ob die Änderung dieser Woche etwas zerlegt hat, das letzte Woche lief; dafür ist ein
eingefrorener Datensatz da.

Behalten Sie beide. Ein **eingefrorener Regressionsdatensatz** beantwortet die Frage „Läuft noch, was vorher
lief?“, und um sie zu beantworten, muss er stillstehen. Ein **wechselnder Datensatz aus dem laufenden
Verkehr** beantwortet die Frage „Passt meine Evaluierung noch zur Wirklichkeit?“, und dafür muss er sich
bewegen. Für den Wechsel gibt es einen zweiten Grund, und er kommt von der anderen Seite: Ein fester Maßstab,
gegen den ein Team Monate lang optimiert, misst irgendwann nicht mehr die Qualität, sondern die **Vertrautheit
mit dem Maßstab** selbst. Beide Datensätze brauchen Labels, und das ist der Teil, für den niemand ein Budget
einplant; die [Evaluierung](../part-1-rag/cross-cutting/evaluation/index.md) sagt es unverblümt: kein
Datensatz, keine Evaluierung.

## 4 · Grün und korrekt sind nicht dasselbe

<InfoCard
  title="Grün heißt nicht korrekt"
  caption="Verfügbarkeit ist eine Eigenschaft des Dienstes. Korrektheit ist eine Eigenschaft der Antwort.">
  <Lane kind="demo" label="DEMO">
    <Node icon="cloud" badge="tick" label="200 OK" />
    <Flow kind="fail" />
    <Node icon="speechBubble" badge="bang" label="falsche Antwort" />
  </Lane>
  <Lane kind="production" label="PRODUKTION">
    <Node icon="traceSpans" label="Trace der Pipeline" />
    <Flow />
    <Node icon="scales" label="Judge auf einer Stichprobe" />
    <Flow />
    <Node icon="gauge" badge="tick" label="Qualitätsalarm" />
  </Lane>
</InfoCard>

Jedes gewohnte Signal kann gesund sein, während das System falsch antwortet. Die Latenz ist in Ordnung, die
Fehlerquote liegt bei null, der Pod läuft – und die Antworten sind mit Überzeugung falsch, denn kein
gewöhnlicher Monitor hat eine Meinung zum *Inhalt* einer 200. Eine grüne Statusanzeige bedeutet nicht, dass
die Antwort korrekt ist: Verfügbarkeit ist eine Eigenschaft des Dienstes, Korrektheit eine Eigenschaft der
Antwort, und aus der ersten folgt die zweite nicht.

Zwei Dinge schließen die Lücke. Ein **Trace**, der den ganzen Weg einer Anfrage aufzeichnet – die Frage,
welche Chunks zurückkamen und mit welchen Scores, den Prompt in der Form, in der er abgeschickt wurde, die
Antwort, die Tokens –, denn ohne die Kennungen der Chunks rekonstruieren Sie nicht einmal, *warum* eine
Antwort falsch war. Und ein **unabhängiger Judge auf einer Stichprobe des laufenden Verkehrs**, damit die
Qualität eine überwachte Metrik mit Schwellenwert und Alarm ist und nicht etwas, das Sie aus einem Ticket
der Kundenbetreuung erfahren. Das ist die
[Observability](../part-1-rag/cross-cutting/observability/index.md) und die Schleife, in der sie die
Evaluierung speist.

Eine Sache entwerfen Sie besser bewusst, statt sie zu erben: Eine Protokollierung, die auf die Fehlersuche
zugeschnitten ist, ist keine Protokollierung, die auf den Nachweis zugeschnitten ist. Für die Fehlersuche
brauchen Sie die letzten Tage so genau, wie Sie sich das leisten können. Für ein **Audit** dagegen – etwa
in einer regulierten Branche, bei einer bestrittenen Antwort oder wenn ein Kunde fragt, was Ihr System ihm
im März gesagt hat – müssen Sie *Monate später* noch nachweisen können, was gefunden und was zurückgegeben
wurde. Das ist eine Anforderung an Aufbewahrung und Integrität und keine Einstellung für die
Ausführlichkeit. Entscheiden Sie, welches von beiden Sie bauen, bevor ein Prüfer es für Sie entscheidet.

## 5 · Die Einheit sind die Kosten für eine angenommene Antwort

<Infographic
  src="/img/infographics/production-failures/05-cost.webp"
  alt="Drei Versuche mit dem günstigen Modell gegen einen Versuch mit dem teuren Modell; der Abstand ist als retry tax beschriftet, also als Mehrkosten der Wiederholungen"
  caption="Ein günstigeres Modell gewinnt nur, wenn sein Vorsprung bei der Erfolgsquote größer ist als der Abstand beim Preis."
/>

Kosten, die in einem Demo wie ein Rundungsfehler aussehen, wachsen im Produktivbetrieb an drei Stellen
gleichzeitig: Agenten wiederholen ihre Versuche, Dialoge schicken bei jeder Replik ihre ganze Geschichte
erneut, und Nutzer kleben ganze Dokumente in ein Feld, das Sie für einen Satz bemessen haben. Das erneute
Senden wird am häufigsten übersehen: Ein zustandsloses Modell liest bei jeder Replik die ganze Mitschrift
neu, also kostet eine Aufgabe, die doppelt so lange läuft, ungefähr das Vierfache. Zu beschneiden, was im
Kontext mitfährt, ist der wirksamste Hebel, den Sie haben. Ein stabiles Präfix des Prompts, das sich cachen
lässt, hilft mehr als jeder Wechsel auf ein anderes Modell.

Damit kommt der zweite Einwand: „Überlassen Sie die Routine einem kleineren Modell“ ist ein Rat mit einer
Bedingung, und die Bedingung wird meist weggelassen. Es zählen die **Kosten für eine angenommene Antwort**
und nicht die Kosten je Token. Ein günstigeres Modell, das drei Versuche braucht, während das teure mit
einem auskam, ist damit nicht günstiger – diesen Abstand fressen die **Mehrkosten der Wiederholungen**:

```text
cost_per_accepted ≈ attempt_cost / p          (p = Erfolgsquote beim ersten Versuch)

Das günstigere Modell gewinnt nur, wenn:
    p_cheap / p_expensive  >  price_cheap / price_expensive
```

Der halbe Preis bringt nichts, wenn die Zuverlässigkeit unter der Hälfte liegt. Messen Sie `p` für jede
Route, bevor Sie einer Einsparung glauben. [LLMOps](./llmops/index.md) behandelt die Hebel – das Routing, das
Caching, den Batch-Tarif, Budgets, die den Verbrauch wirklich stoppen –, und der Kurs zum AI-SDLC rechnet
dieselbe Arithmetik für eine andere Einheit aus: für die Kosten einer angenommenen Änderung am Code.

## 6 · Indexieren Sie neu, bevor Sie neu trainieren

<InfoCard
  title="Zuletzt neu trainieren"
  caption="Der Drift sitzt meist im Korpus oder in den Fragen, nicht in den Gewichten.">
  <Lane kind="demo" label="DEMO">
    <Node icon="driftCurves" label="Drift erkannt" />
    <Flow kind="fail" />
    <Node icon="chip" badge="refresh" label="Modell neu trainieren" />
  </Lane>
  <Lane kind="production" label="PRODUKTION">
    <Node icon="database" badge="refresh" label="neu indexieren" rank="1" />
    <Flow />
    <Node icon="sliders" label="Mischung der Suche" rank="2" />
    <Flow />
    <Node icon="codeFile" label="Prompt" rank="3" />
    <Flow />
    <Node icon="chip" label="Gewichte zuletzt" rank="last" />
  </Lane>
</InfoCard>

Die Qualität lässt nach, ohne dass ein Deployment stattfindet. Nutzer bringen neues Vokabular mit, die
Dokumente darunter ändern sich, und ein beim Anbieter betriebenes Modell, dessen Version Sie nicht
festgelegt haben, wird unbemerkt ausgetauscht. Das ist der dritte Einwand und der schärfste: Der gewohnte
Reflex ist, ein erneutes Training anzustoßen, sobald der Drift einen Schwellenwert überschreitet – eine
Antwort aus MLOps, übertragen auf ein System, in dem die Gewichte fast nie das Problem sind.

In einem System mit Retrieval kommt der Drift meist vom Korpus oder von den Fragen, und deshalb fangen Sie weit
unterhalb des Modells an: neu indexieren und neu in Chunks aufteilen, die Mischung der Suchverfahren
anpassen, den Prompt überarbeiten – und erst dann überlegen, ob Sie an die Gewichte gehen, was für die
meisten Teams ohnehin nur das nächste Release des Anbieters bedeutet und keinen eigenen Trainingsdurchlauf.
Drei Arten von Drift und wie Sie jede beobachten, stehen in [LLMOps](./llmops/index.md). Die brauchbare
Folgerung: **Das Korpus ist ein Release** – es braucht eine Version, einen Diff und einen Rollback, genau wie
der Code.

## 7 · Der Prompt und das Korpus sind Releases

<InfoCard
  title="Prompt und Korpus sind Releases"
  caption="Alles, was das Verhalten ändert, braucht eine Version und einen Weg zurück.">
  <Lane kind="demo" label="DEMO">
    <Node icon="codeFile" label="Prompt im Code" />
    <Flow kind="fail" />
    <Node icon="cloud" badge="bang" label="jede Änderung live" />
  </Lane>
  <Lane kind="production" label="PRODUKTION">
    <Merge>
      <Node icon="document" badge="tag" label="Prompt-Konfig" />
      <Node icon="chip" badge="tag" label="Modell festgelegt" />
      <Node icon="database" badge="tag" label="Snapshot des Korpus" />
    </Merge>
    <Flow />
    <Node icon="branchSplit" label="Canary Release, Rollback" />
  </Lane>
</InfoCard>

Steckt ein Prompt im Code der Anwendung, ist das Ändern eines Satzes ein Deployment – eine Korrektur am Text
trägt damit das Risiko eines Deployments, und niemand traut sich mehr, sie als die kleine Änderung zu
behandeln, die sie ist. Lagern Sie die Prompts mit eigenen Prüfungen der Qualität in eine **Konfiguration unter
Versionsverwaltung** aus, und das Gerüst lässt sich per Diff vergleichen und zurücknehmen, statt dass Sie
bei jedem Ausrollen die Daumen drücken.

Verlangen Sie dasselbe von allem anderen, was das Verhalten ändert, ohne den Code zu ändern: **Legen Sie
die Modellversion fest**, **nehmen Sie einen Snapshot des Korpus**, rollen Sie als Canary Release aus,
und halten Sie für jeden der drei einen eigenen Weg zurück bereit. Ein System, in dem sich Prompt, Modell und
Index jederzeit unbemerkt ändern können, hat überhaupt keinen reproduzierbaren Zustand, und das
behebt kein Test der Welt. Die Mechanik des Releases steht in [LLMOps](./llmops/index.md).

## 8 · Eine Pipeline braucht Prüfungen zwischen den Schritten

<InfoCard
  title="Die günstigste Prüfung zuerst"
  caption="Jede Stufe weist schlechte Eingaben ab, und die günstigste Prüfung läuft zuerst.">
  <Lane kind="demo" label="DEMO">
    <Node icon="chainSteps" label="keine Prüfungen" />
    <Flow kind="fail" />
    <Node icon="document" badge="crack" label="Fehler wandert weiter" />
  </Lane>
  <Lane kind="production" label="PRODUKTION">
    <Node icon="gate" label="Schema" rank="1" />
    <Flow />
    <Node icon="gate" label="Quellenangaben" rank="2" />
    <Flow />
    <Node icon="gate" label="Judge" rank="last" />
  </Lane>
</InfoCard>

In einer Pipeline über mehrere Schritte wird die erste schlechte Ausgabe zu der Eingabe, die der nächste
Schritt für vertrauenswürdig hält. Aus einem Fehlgriff des Retrievals wird eine überzeugte Zusammenfassung,
aus ihr eine Entscheidung, und bis irgendetwas auffällig aussieht, liegt der ursprüngliche Fehler mehrere
Umformungen zurück. Die Antwort darauf ist eine Prüfung zwischen den Schritten, und jede Stufe hat die Aufgabe,
schlechte Eingaben **abzuweisen**, statt aus ihnen das Beste zu machen. Eine Stufe, die nie
etwas abweist, verdeckt Fehler nur und gibt sie weiter.

Die Verfeinerung, die sich lohnt, ist die **Reihenfolge**. Nicht jede Prüfung kostet gleich viel: Eine
Prüfung des Schemas kostet Mikrosekunden, die Prüfung, ob die Antwort von den angegebenen Quellen gedeckt ist,
kostet ein Retrieval, ein Urteil durch ein Modell kostet einen Modellaufruf. Lassen Sie die günstigste
zuerst laufen, damit Sie für Fehler, die ein regulärer Ausdruck abgefangen hätte, nie den Preis eines
Judges zahlen. Dieses Argument über die Reihenfolge entwickelt die Lektion über die mehrschichtigen Prüfungen
im Kurs zum AI-SDLC in aller Ruhe; die Maschinerie auf der RAG-Seite – was Sie an der Eingabe, an der
Ausgabe und bei der Ingestion absichern – steht in der Lektion zu den
[Guardrails](../part-1-rag/cross-cutting/guardrails/index.md).

## 9 · Vier, die selten auf der Liste stehen

<InfoCard
  title="Vier, die in den Listen fehlen"
  caption="Vier Fehler, die die üblichen Listen überspringen – und der letzte fällt vor dem Modell aus.">
  <Grid tone="fail">
    <Node icon="lockOpen" label="unbegrenzte Zugriffsrechte" />
    <Node icon="document" label="vergiftete Dokumente" />
    <Node icon="globe" label="nur eine Sprache" />
    <Node icon="plug" label="unzuverlässige Tools" />
  </Grid>
</InfoCard>

Noch vier Fehler, und jeder von ihnen hat schon ein Produktivsystem zu Fall gebracht, während alle auf die acht
davor geschaut haben.

**Unbegrenzte Zugriffsrechte.** Im Demo läuft der Agent mit Anmeldedaten, die alles erlauben, und im Index
liegt jedes Dokument, das der Crawler erreichen konnte. Im Produktivbetrieb ist genau dieselbe Anordnung
ein Weg, auf dem Daten nach außen gelangen: Ein Retrieval, das nicht nach den Berechtigungen des Aufrufers
filtert, zitiert bereitwillig ein Dokument, das der Aufrufer nie öffnen durfte. **Ein Retrieval, das die
Berechtigungen kennt**, ist kein Merkmal, das Sie später ergänzen – es ändert die Form des Index.

**Vergiftete Dokumente.** Abgerufener Text ist eine nicht vertrauenswürdige Eingabe. Ein Dokument, in dem
Anweisungen stehen, kann das Modell kapern, das es liest, und deshalb fangen Sie das am günstigsten bei der
Indexierung ab und nicht bei der Abfrage.

**Nur eine Sprache.** Ein Embedding-Modell und ein Reranker, die auf Englisch trainiert wurden, übersehen
einschlägige englische Dokumente, sobald die Frage in einer anderen Sprache eintrifft, und der Fehler bleibt
unbemerkt: weniger Treffer, alle plausibel. Sind Ihre Nutzer mehrsprachig und Ihre Evaluierung nicht, dann
haben Sie nicht das System gemessen, das Ihre Nutzer vor sich haben.

**Unzuverlässige Tools.** Die Tools fallen vor dem Modell aus. APIs antworten nicht mehr rechtzeitig, ein
MCP-Server wird neu gestartet, ein Vektorspeicher weist eine Verbindung ab – und ein Agent ohne Timeout,
ohne Wiederholung und ohne Fallback-Antwort hängt einfach – und die Nutzer halten das für einen Defekt und
nicht für Langsamkeit. Liefern Sie absichtlich eine schlechtere Antwort, statt gar keine; die Lektion über
den [Tool-Einsatz](../part-2-agents/tool-use/index.md) behandelt den ganzen Ablauf eines Aufrufs und den
Umgang mit seinen Fehlern.

## Das Wichtigste

- **Fast nichts davon ist ein Fehler des Modells.** Das Modell ist das Bauteil, das Sie nicht geschrieben
  haben; die Fehler sitzen im System darum herum.
- **Die Ingestion soll ausweisen und nicht bloß prüfen** – aufgenommen, ausgeschlossen samt Grund, und die
  blinden Flecken. Ein unbemerkt verworfenes Dokument erzeugt eine überzeugte Antwort aus einem
  unvollständigen Korpus.
- **Das Retrieval muss die Antwort verweigern können**: eine Score-Untergrenze hinter dem Reranking, eine
  absichtlich leere Menge und einen Generator, der sagt, dass ihm der Kontext fehlt.
- **Zwei Datensätze** – ein eingefrorener für die Regressionen, ein wechselnder aus dem laufenden Verkehr für
  die Wirklichkeit. Keiner ersetzt den anderen.
- **Verfügbarkeit ist nicht Korrektheit.** Nehmen Sie einen Trace mit den Kennungen der Chunks dazu und einen
  Judge auf einer Stichprobe des Verkehrs; entscheiden Sie gesondert, ob Sie jemandem eine Protokollierung
  für ein Audit schulden.
- **Die Kosten für eine angenommene Antwort** sind die Einheit: `cost ≈ attempt_cost / p`, und der
  Vorsprung eines günstigeren Modells bei der Zuverlässigkeit muss größer sein als seine Ersparnis beim
  Preis.
- **Gegen den Drift hilft zuerst ein erneutes Indexieren** und erst viel später ein erneutes Training;
  das Korpus ist ein Release, mit einer Version und einem Rollback.
- **Prompt, Modellversion und Korpus** brauchen alle drei je eine Version und einen Weg zurück, sonst
  hat das System keinen reproduzierbaren Zustand.
- **Prüfungen zwischen den Schritten, die günstigste zuerst** – jede Stufe weist schlechte Eingaben ab, statt
  sie zu verdecken und weiterzugeben.
- **Und die vier, die niemand auflistet**: unbegrenzte Zugriffsrechte, vergiftete Dokumente, eine Evaluierung
  in nur einer Sprache, unzuverlässige Tools.

Teil III liefert nun die Antworten: die [Bereitstellung](./serving/index.md) des Systems, die
[Cloud-Plattformen](./cloud-platforms/index.md), auf denen es läuft, das
[Tooling-Ökosystem](./tooling-ecosystem/index.md), das es misst und absichert, und
[LLMOps](./llmops/index.md) für sein Leben nach dem Release.

**[Neue Begriffe](../glossary.md#production-failures)**: score floor / relevance floor, ingestion manifest,
blind spot (ingestion), frozen regression set, rotating live-sampled set, benchmark familiarity, audit-grade
logging, cost per accepted answer, retry tax, drift response ladder, corpus as a release, permission-aware
retrieval, cross-lingual retrieval gap, graceful degradation (tools).
