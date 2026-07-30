#!/usr/bin/env python3
"""Build the Sol (cross-model) register-gate prompt for ONE German page, PROGRAMMATICALLY
FROM THE SHIPPED FILE, into an owner-scoped, page-named path.

Every rule in here was bought with a defect:

  * Wave 1 refused ~1/3 of Sol's replacements as enterprise-German flattening.
    Wave 2 refused ZERO -- because the prompt FORBIDS proposing replacements at all.
    THE LEVER IS THE PROMPT, NOT THE REVIEWER. Do not relax this into "suggest a fix".
  * Wave 2 required every quote to be VERBATIM from the file and invalidated any verdict
    whose quote was not. Result: ~450 verdicts, zero fabricated citations.
  * A verdict without a linguistically NAMED TELL is discarded. The named tell is what
    makes the gate falsifiable and what lets an orchestrator who does not speak German
    adjudicate at all.
  * The prompt goes in ON STDIN (`codex exec -s read-only - < prompt.txt`). As an
    argument it hangs.
  * The output path carries the PAGE SLUG. A /tmp collision once overwrote one
    renderer's prompt with another's and returned 24 confident verdicts about a
    different lesson.

Usage: solprompt.py <de-page-path> <slug>  > .scratch-dewave3/sol/PROMPT-<slug>.txt
"""
import sys, pathlib, re

page = pathlib.Path(sys.argv[1])
slug = sys.argv[2]
text = page.read_text(encoding="utf-8")

print(f"""Du bist ein einsprachig deutscher Registerprüfer. Du liest ausschließlich Deutsch.
Es gibt keinen englischen Quelltext, und du fragst nicht danach.

Der Text unten ist EINE Seite eines deutschen Fachhandbuchs über KI-Engineering
(Druckniveau: dpunkt, Rheinwerk, O'Reilly Deutschland, heise/iX). Er wendet sich mit
„Sie" an eine Leserin oder einen Leser mit Entwicklungshintergrund.

WICHTIG, damit du nicht das Falsche prüfst:
Englische Fachbegriffe sind in diesem Buch ABSICHT und KEIN Fehler. Deutsche
Fachprosa schreibt „das Embedding", „der Prompt", „das Retrieval", „der Tool-Call",
„die Guardrails". Ein Anglizismus ist hier per Hausregel kein Defekt. Prüfe NICHT die
Wortwahl englischer Termini. Prüfe, ob das DEUTSCHE drumherum klingt wie von einem
deutschen Fachautor geschrieben.

=== DEINE AUFGABE ===

Gib Urteile über einzelne PASSAGEN ab. Für jede Passage genau drei Dinge:

  1. ZITAT — die betroffene Stelle, WÖRTLICH und ZEICHENGENAU aus dem Text unten
     kopiert. Nicht gekürzt, nicht geglättet, nicht normalisiert.
  2. URTEIL — genau eines von: NATIV / VERDÄCHTIG / ÜBERSETZT
  3. BEFUND — der sprachlich BENANNTE Grund. Nenne das Phänomen beim Namen:
     Satzklammer, Verbzweitstellung, Verbletztstellung im Nebensatz, Rektion/Kasus,
     Genus eines Lehnworts, Nominalstil, Denglisch-Partizip, von-Genitiv statt
     Kompositum oder echtem Genitiv, englische Wortstellung, Kollokationsbruch,
     Funktionsverbgefüge, falsche Präposition, Tempusfehler, Kongruenzfehler,
     Registerbruch, feste Wendung mit falscher Bedeutung.

=== DREI VERBOTE, DIE DIESES GATE DEFINIEREN ===

  A. SCHLAGE KEINE ERSETZUNG VOR. Keine Verbesserung, keine Alternative, kein
     „besser wäre …". Du DIAGNOSTIZIERST. Wer repariert, entscheidet später jemand
     anderes. Ein Urteil, das eine Ersetzung enthält, wird verworfen.
  B. KEIN URTEIL OHNE BENANNTEN BEFUND. „Klingt holprig", „unnatürlich",
     „nicht idiomatisch" sind KEINE Befunde. Ohne einen sprachlich benannten Befund
     wird das Urteil verworfen.
  C. KEIN ZITAT, DAS NICHT WÖRTLICH IM TEXT STEHT. Deine Zitate werden maschinell
     gegen den Text geprüft. Ein Zitat, das nicht zeichengenau vorkommt, macht das
     ganze Urteil ungültig. Wenn du dir bei einem Zeichen unsicher bist, zitiere
     kürzer — lieber fünf sichere Wörter als zwölf rekonstruierte.

=== WORAUF ES BEI DIESEM DURCHGANG BESONDERS ANKOMMT ===

Der teuerste Fehler dieses Projekts war bisher NICHT ein falsches Wort. Er war eine
FLÜSSIGE deutsche Fügung, die auf einer englischen Kollokation gebaut war — richtiges
Register, richtige Domäne, und trotzdem falsch, weil die deutsche Wendung im
Deutschen etwas anderes bedeutet oder eine feste Redewendung anstößt. Beispiele der
Fehlerklasse (nicht unbedingt in diesem Text): „auf der Leitung" für ein
Datenformat — korrekt gebaut und stößt „auf der Leitung stehen" an; „einen Plan
fahren"; „Vertrauen erteilen".

Solche Stellen findet KEINE Wortliste und KEIN Wörterbuch. Nur ein deutsches Ohr.
Achte deshalb ausdrücklich auf:
  — Verb + Objekt: nimmt dieses Verb im Deutschen wirklich dieses Objekt?
  — Präposition + Kasus: regiert die Präposition hier wirklich diesen Fall?
  — feste Wendungen, die die Fügung ungewollt anstößt;
  — Nominalisierungen, die ein deutscher Autor als Nebensatz schriebe;
  — Sätze, deren Bau der englischen Reihenfolge folgt, obwohl jedes Wort deutsch ist.

Ein Text kann fehlerfrei sein. „Diese Seite ist durchgehend nativ" ist ein
zulässiges und erwartetes Ergebnis. Erfinde keine Beanstandungen, um etwas zu liefern.
Nenne aber, wo du unsicher bist, ausdrücklich VERDÄCHTIG statt ÜBERSETZT.

Arbeite den Text von oben nach unten durch. Überschriften, Aufzählungen, Tabellen und
die Beschriftungen in den Diagrammen gehören dazu.

=== TEXT (Seite: {slug}) ===

{text}
=== ENDE DES TEXTES ===

Gib jetzt deine Urteile aus, eines pro Block, im Format:

ZITAT: <wörtlich>
URTEIL: <NATIV|VERDÄCHTIG|ÜBERSETZT>
BEFUND: <benanntes sprachliches Phänomen + kurze Begründung>
""")
