#!/usr/bin/env python3
"""Extract every translatable label from every ```mermaid fence, and make it gateable.

WHY THIS EXISTS. Mermaid is the one text unit a prose gate does not read as prose. It
sits inside a fence, so the typography census, the register pass and the cold read all
skip it -- while the READER sees it rendered on the page like any other text. Two
independent signals landed on it in this wave:

  * slice F: BOTH waves' `golden set` regressions, and both of its own riskiest
    occurrences, are in Mermaid labels;
  * the term pass: Mermaid is an UNCOUNTED translatable surface -- 89 label-bearing
    lines across 8 files, being translated correctly BY ACCIDENT, and recorded nowhere
    in the playbook.

So the labels get pulled out and run through the SAME term binding, the SAME census and
the SAME Sol pass as prose. Cheaper than another cold read, and it closes the surface
both regressions came through.

WHAT IS AND IS NOT A LABEL. Node IDs (`A`, `REDIS`, `WP`) never change and are class 1.
Translated prose is: node label text, subgraph titles, edge labels, and -- the shape no
flowchart regex matches -- in a `sequenceDiagram`, the text after `:` and the alias
after `as`. A label extractor that only handles flowcharts silently under-reports the
one sequence diagram in this corpus by eleven lines.

usage: mermaid_gate.py labels <file|dir> ...     # the inventory, per file
       mermaid_gate.py solprompt <file> <slug>   # a Sol prompt over THIS page's labels
"""
import pathlib, re, sys, json, collections

# ---- extraction ---------------------------------------------------------------------

def fences(text):
    out, cur, inside = [], [], False
    for ln in text.split("\n"):
        s = ln.strip()
        if s.startswith("```"):
            if not inside and s[3:].strip().lower() == "mermaid":
                inside, cur = True, []
            elif inside:
                out.append(cur); inside = False
            continue
        if inside:
            cur.append(ln)
    return out

LABEL_PATTERNS = [
    # flowchart node labels: A["…"]  A[…]  A(…)  A{…}  A{{…}}  A[(…)]  A>…]
    (r'\[\(\s*"?(?P<t>[^"\]\)]+?)"?\s*\)\]', "node"),
    (r'\{\{\s*"?(?P<t>[^"\}]+?)"?\s*\}\}', "node"),
    (r'\[\s*"(?P<t>[^"]+?)"\s*\]', "node"),
    (r'\[\s*(?P<t>[^"\[\]|]+?)\s*\]', "node"),
    (r'\(\s*"(?P<t>[^"]+?)"\s*\)', "node"),
    (r'\{\s*"(?P<t>[^"]+?)"\s*\}', "node"),
    (r'\{\s*(?P<t>[^"\{\}|]+?)\s*\}', "node"),
    # edge labels:  -->|"…"|   -->|…|   -- "…" -->   -- … -->
    (r'\|\s*"?(?P<t>[^"|]+?)"?\s*\|', "edge"),
    (r'--\s*"(?P<t>[^"]+?)"\s*--?>', "edge"),
    # subgraph titles: subgraph X["…"]  /  subgraph "…"  /  subgraph Name
    (r'^\s*subgraph\s+\w*\s*\[\s*"?(?P<t>[^"\]]+?)"?\s*\]', "subgraph"),
    (r'^\s*subgraph\s+"(?P<t>[^"]+?)"', "subgraph"),
    # sequenceDiagram: `participant A as Label` and `A->>B: message` and `Note over A: text`
    (r'^\s*(?:participant|actor)\s+\w+\s+as\s+(?P<t>.+?)\s*$', "participant"),
    (r'^\s*Note\s+(?:over|left of|right of)\s+[^:]+:\s*(?P<t>.+?)\s*$', "note"),
    (r'^\s*\w+\s*-?-?>>?\+?-?\s*\w+\s*:\s*(?P<t>.+?)\s*$', "message"),
]

SKIP = re.compile(r'^(flowchart|graph|sequenceDiagram|classDiagram|stateDiagram|end|direction|click|style|classDef|linkStyle|autonumber|%%)', re.I)

def labels_of(text):
    found = []
    for block in fences(text):
        for raw in block:
            line = raw.rstrip()
            if not line.strip() or SKIP.match(line.strip()):
                continue
            seen_here = set()
            for pat, kind in LABEL_PATTERNS:
                for m in re.finditer(pat, line, re.M):
                    t = m.group("t").strip().strip('"')
                    if not t or t in seen_here:
                        continue
                    # Node IDs (`A`, `REDIS`, `WP`) are class 1 and never labels -- but they
                    # are only ever written OUTSIDE the brackets, so anything captured here
                    # is a label by construction. An earlier version of this skipped any
                    # all-caps token as "probably an id" and therefore silently dropped
                    # `G[GPU]`, whose id is `G` and whose LABEL is `GPU`. That single
                    # false negative is the whole reason this extractor is checked against
                    # an independently measured count instead of trusted.
                    if re.fullmatch(r'[A-Za-z]', t):
                        continue
                    seen_here.add(t)
                    found.append((kind, t, line.strip()))
    return found

# ---- modes --------------------------------------------------------------------------


# ---- the Mermaid-label prompt -------------------------------------------------------
# Kept as a module-level constant at column 0 so the emitted German is EXACTLY this text.
# Indenting a prompt into a function body changes every line the model reads, and THE
# LEVER IS THE PROMPT — a whitespace-shifted prompt is a different gate.
PROMPT_TEMPLATE = """\
Du bist ein einsprachig deutscher Registerprüfer. Du liest ausschließlich Deutsch.
Es gibt keinen englischen Quelltext, und du fragst nicht danach.

Unten stehen die BESCHRIFTUNGEN aus den Diagrammen EINER Seite eines deutschen
Fachhandbuchs über KI-Engineering (Druckniveau: dpunkt, Rheinwerk, O'Reilly Deutschland,
heise/iX). Es sind keine Fließtextsätze, sondern Knotenbeschriftungen, Kantenbeschriftungen
und Titel — also KURZE Fügungen, die im gerenderten Diagramm für sich allein stehen.

WICHTIG, damit du nicht das Falsche prüfst:
Englische Fachbegriffe sind in diesem Buch ABSICHT und KEIN Fehler. Prüfe NICHT die
Wortwahl englischer Termini. Prüfe das DEUTSCHE drumherum.

Und beachte die Textsorte: Eine Beschriftung darf verknappt sein. Ein fehlender Artikel
oder ein Nominalstil, der in einem Fließtextsatz ein Befund wäre, ist in einer
Diagrammbeschriftung normal. Beanstande NICHT die Kürze als solche.

WORAUF ES HIER ANKOMMT: Genau diese Zeilen sind der Ort, an dem in zwei früheren Wellen
gestrichene Termini zurückgekehrt sind — weil eine Beschriftung in einem Codeblock steht
und deshalb von jeder Prosaprüfung übersprungen wird, während die Leserin sie gerendert
sieht. Achte deshalb auf:
  — feste Wendungen, die die Fügung ungewollt anstößt;
  — Verb + Objekt und Präposition + Kasus, die es im Deutschen nicht gibt;
  — englische Wortstellung in einer deutschen Fügung;
  — uneinheitliche Benennung: bezeichnen zwei Beschriftungen DASSELBE mit verschiedenen
    Wörtern? Das ist hier der teuerste Fehler, und du siehst alle Beschriftungen der
    Seite auf einmal — als Einzige.

=== DREI VERBOTE, DIE DIESES GATE DEFINIEREN ===

  A. SCHLAGE KEINE ERSETZUNG VOR. Du DIAGNOSTIZIERST. Ein Urteil, das eine Ersetzung
     enthält, wird verworfen.
  B. KEIN URTEIL OHNE BENANNTEN BEFUND. „Klingt holprig" ist KEIN Befund. Nenne das
     Phänomen: Kollokationsbruch, Rektion/Kasus, Genus, Nominalstil, Durchkopplung,
     englische Wortstellung, feste Wendung mit falscher Bedeutung, Kongruenz, Register.
  C. KEIN ZITAT, DAS NICHT WÖRTLICH UNTEN STEHT. Deine Zitate werden maschinell geprüft.

„Alle Beschriftungen sind nativ" ist ein zulässiges und erwartetes Ergebnis. Erfinde
keine Beanstandungen.

=== BESCHRIFTUNGEN (Seite: {slug}) ===

{body}
=== ENDE ===

Gib jetzt deine Urteile aus, eines pro Block, im Format:

ZITAT: <wörtlich>
URTEIL: <NATIV|VERDÄCHTIG|ÜBERSETZT>
BEFUND: <benanntes sprachliches Phänomen + kurze Begründung>
"""


def build_prompt(labels, slug):
    """The Sol prompt over ONE page's Mermaid labels."""
    body = "\n".join(f"{i:3}. {t}" for i, (_, t, _) in enumerate(labels, 1))
    return PROMPT_TEMPLATE.format(slug=slug, body=body)


# ---- modes --------------------------------------------------------------------------

def resolve(args):
    targets = []
    for a in args:
        q = pathlib.Path(a)
        targets += sorted(q.rglob("*.md")) if q.is_dir() else [q]
    return targets


def main(argv):
    """CLI dispatch. Importable: nothing reads sys.argv at module level, which is what
    makes the self-test possible at all."""
    if len(argv) < 2:
        print(__doc__)
        return 2
    mode = argv[1]
    targets = resolve(argv[2:3] if mode == "solprompt" else argv[2:])

    if mode == "labels":
        grand, per_file = 0, {}
        for f in targets:
            ls = labels_of(f.read_text(encoding="utf-8"))
            if not ls:
                continue
            per_file[str(f)] = ls
            grand += len(ls)
        print("# MERMAID LABEL INVENTORY — the translatable surface no prose gate reads")
        print(f"# {len(per_file)} file(s) with mermaid · {grand} label string(s)\n")
        for f, ls in per_file.items():
            kinds = collections.Counter(k for k, _, _ in ls)
            print(f"## {f}  ({len(ls)} labels · {dict(kinds)})")
            for k, t, ctx in ls:
                print(f"   [{k:11}] {t}")
            print()
        print("Every string above is READ BY THE READER and SKIPPED BY THE CENSUS, the register")
        print("pass and the cold read. Run it through the term binding and the Sol pass.")
        return 0

    if mode == "solprompt":
        if len(targets) < 1 or len(argv) < 4:
            print("usage: mermaid_gate.py solprompt <file> <slug>", file=sys.stderr)
            return 2
        page, slug = targets[0], argv[3]
        ls = labels_of(page.read_text(encoding="utf-8"))
        if not ls:
            print(f"NO MERMAID LABELS on {page} — nothing to gate.", file=sys.stderr)
            return 3
        print(build_prompt(ls, slug))
        return 0

    print(__doc__)
    return 2


# ---- self-test ----------------------------------------------------------------------
# Every case below is a REGRESSION, not an invented example.

SELF_TEST_DOC = """Prose before the fence is not a label.

```mermaid
flowchart TD
  A["Ein Knoten mit Beschriftung"] --> B[Ohne Anfuehrungszeichen]
  G[GPU] --> H{"Eine Raute"}
  B -->|"Eine Kantenbeschriftung"| G
  subgraph S["Ein Untergraph"]
    C[(Ein Zylinder)]
  end
  style A fill:#fff
```

```python
d = {"not": "a label"}
```

```mermaid
sequenceDiagram
  participant U as Die Nutzerin
  U->>S: Eine Nachricht
  Note over U: Eine Anmerkung
```
"""


def self_test():
    fails = []

    def check(label, got, want):
        if got == want:
            print(f"  ok   {label} -> {got!r}")
        else:
            print(f"  FAIL {label} -> got {got!r}, want {want!r}")
            fails.append(label)

    print("mermaid_gate --self-test")
    labels = labels_of(SELF_TEST_DOC)
    texts = [t for _, t, _ in labels]

    # THE REGRESSION THIS EXISTS FOR. An earlier extractor skipped any all-caps token as
    # "probably a node id" and therefore silently dropped `G[GPU]`, whose id is `G` and whose
    # LABEL is `GPU`. One false negative, in a surface no prose gate reads.
    check("an ALL-CAPS label is extracted (`G[GPU]`; the uppercase-node-ID heuristic ate it)",
          "GPU" in texts, True)

    check("a quoted node label", "Ein Knoten mit Beschriftung" in texts, True)
    check("an unquoted node label", "Ohne Anfuehrungszeichen" in texts, True)
    check("a diamond node label", "Eine Raute" in texts, True)
    check("an edge label", "Eine Kantenbeschriftung" in texts, True)
    check("a subgraph title", "Ein Untergraph" in texts, True)
    check("a cylinder node label", "Ein Zylinder" in texts, True)

    # A flowchart-only extractor under-reports the one sequence diagram in this corpus.
    check("a sequenceDiagram participant alias", "Die Nutzerin" in texts, True)
    check("a sequenceDiagram message", "Eine Nachricht" in texts, True)
    check("a sequenceDiagram note", "Eine Anmerkung" in texts, True)

    # Non-labels must stay out.
    check("a non-mermaid fence contributes nothing", any("a label" in t for t in texts), False)
    check("prose outside a fence contributes nothing",
          any("Prose before" in t for t in texts), False)
    check("a `style` directive is skipped", any("fill" in t for t in texts), False)
    check("a bare single-letter node id is not a label", "A" in texts, False)

    print("  -- the prompt must be emitted verbatim, at column 0")
    prompt = build_prompt(labels, "self-test")
    check("the prompt starts with the German opener, unindented",
          prompt.startswith("Du bist ein einsprachig deutscher Registerprüfer"), True)
    check("the prompt carries the slug (the collision assertion keys on it)",
          "Seite: self-test" in prompt, True)
    check("no line of the prompt was shifted by an indent",
          any(l.startswith("    Du bist") for l in prompt.split("\n")), False)
    check("the labels are numbered into the prompt", "GPU" in prompt, True)

    print()
    if fails:
        print(f"mermaid_gate --self-test: FAIL ({len(fails)}): {'; '.join(fails)}")
        return 1
    print("mermaid_gate --self-test: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main(sys.argv))
