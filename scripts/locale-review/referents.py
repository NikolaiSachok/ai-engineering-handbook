#!/usr/bin/env python3
"""Referent inventory: candidate 'one referent, several names' collisions.

Measured history of this instrument:
  wave 1 consistency pass: found ONE referent under SEVEN names (`retrieval failure`),
    invisible to reading because each page was internally coherent. Counting found it.
  wave 2 baseline: 6 candidates, 0 real. `Schritt` 24 vs `Stufe` 31 is TWO REFERENTS,
    not two names. So is `Werkzeugkatalog` vs `Tool-Katalog`.
  wave 2 post-render: 14 flags, 1 real (a `Golden Sets` regression of a struck term) --
    and one false flag was caused by a plural-tolerant regex matching a genitive singular.

⇒ THE RULE THIS TOOL ENCODES: a count sees quantities, not referents. So it never
   asserts a merge. It prints, for every variant, a SENTENCE per occurrence, and the
   human/agent reading it decides what each occurrence REFERS TO before any merge is
   ordered. An instruction to merge that was not preceded by reading a sentence is how
   wave 2's gate ordered a wrong repair on a 1:2 count.
"""
import re, sys, pathlib, json, collections

def units(md):
    lines = md.split("\n")
    out, i, infence, lang = [], 0, False, None
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            out.append(lines[i]); i += 1
        i += 1
    for ln in lines[i:]:
        s = ln.strip()
        if s.startswith("```"):
            if not infence: infence, lang = True, s[3:].strip().lower()
            else: infence, lang = False, None
            continue
        if infence:
            if lang == "mermaid": out.append("[mermaid] " + s)
            continue
        if not s: continue
        if s.startswith(("|", "#", "-", "*", ":::", "<")):
            out.append(s); continue
        out += [p.strip() for p in re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ\"„'`*\[(])", s) if p.strip()]
    return out

# German inflectional endings a noun variant may legitimately carry. Matching the bare string
# only would MISS every case-marked occurrence — and a case-marked form is the strongest
# evidence this project has (a marked genitive outranks any number of nominative article
# counts). But tolerating the endings silently is what produced a false flag once: a
# plural-tolerant pattern matched a GENITIVE SINGULAR and the row was reported as a 1:2
# plural split. So the ending is tolerated AND the surface form actually matched is PRINTED
# next to every occurrence. The reader can then see `…katalogs` and not mistake it for a plural.
ENDINGS = ("es", "en", "er", "em", "s", "e", "n")


def variant_pattern(v):
    alts = sorted({v + e for e in ENDINGS} | {v}, key=len, reverse=True)
    return re.compile(r"(?<![A-Za-zÄÖÜäöüß])(" + "|".join(re.escape(a) for a in alts)
                      + r")(?![A-Za-zÄÖÜäöüß])", re.I)


def main(groups_path, roots):
    groups = json.loads(pathlib.Path(groups_path).read_text(encoding="utf-8"))
    corpus = []
    for root in roots:
        p = pathlib.Path(root)
        files = sorted(p.rglob("*.md")) if p.is_dir() else ([p] if p.is_file() else None)
        if files is None:
            print(f"FAIL: source path does not exist: {root}")
            print("      A referent inventory over zero files reports every variant absent,")
            print("      which fabricates the very absence this tool exists to detect.")
            return 2
        for f in files:
            for u in units(f.read_text(encoding="utf-8")):
                corpus.append((str(f), u))
    if not corpus:
        print("FAIL: the paths given yielded no text units — a tool failure, not a clean run.")
        return 2

    for gname, variants in groups.items():
        print(f"\n{'#'*100}\n# GROUP: {gname}")
        print("# A COUNT SEES QUANTITIES, NOT REFERENTS. Read every sentence below and decide what")
        print("# each occurrence REFERS TO before proposing any merge. Do not merge on a count.")
        print("# The [surface form] beside each hit is what actually matched: a genitive singular")
        print("# is NOT a plural, and reading it as one has already caused one wrong repair.\n")
        tot, forms_seen = {}, {}
        for v in variants:
            p = variant_pattern(v)
            hits = []
            forms = collections.Counter()
            for f, u in corpus:
                m = p.search(u)
                if m:
                    hits.append((f, u, m.group(1)))
                    forms[m.group(1)] += 1
            tot[v] = len(hits)
            forms_seen[v] = dict(forms)
            print(f"  ## «{v}» — {len(hits)} unit(s) · surface forms: {dict(forms) or 'NONE'}")
            for f, u, surface in hits:
                print(f"     [{pathlib.Path(f).parent.name}/{pathlib.Path(f).name}] "
                      f"[{surface}] {u}")
            if not hits:
                print("     (none)")
            print()
        print(f"  COUNTS: {tot}")
        print(f"  SURFACE FORMS: {forms_seen}")
        print("  VERDICT: ____ (one referent -> merge, naming the winning string | several "
              "referents -> KEEP BOTH, naming each referent | not comparable)")
    return 0


def self_test():
    fails = []

    def check(label, got, want):
        if got == want:
            print(f"  ok   {label} -> {got!r}")
        else:
            print(f"  FAIL {label} -> got {got!r}, want {want!r}")
            fails.append(label)

    print("referents --self-test")
    p = variant_pattern("Werkzeugkatalog")
    check("the bare form matches", bool(p.search("Der Werkzeugkatalog steht dort.")), True)
    m = p.search("Der Inhalt des Werkzeugkatalogs steht dort.")
    check("a GENITIVE SINGULAR is found at all", bool(m), True)
    check("and its surface form is reported, so it cannot pass as a plural",
          m.group(1) if m else None, "Werkzeugkatalogs")
    m2 = p.search("Zwei Werkzeugkataloge existieren.")
    check("a plural is found", m2.group(1) if m2 else None, "Werkzeugkataloge")
    check("a longer compound is NOT a hit (word boundary holds)",
          bool(p.search("Der Werkzeugkatalogeintrag steht dort.")), False)

    print("  -- the unit splitter")
    doc = ('---\ntitle: T\n---\n\n# Eine Überschrift\n\n'
           'Ein Satz. Noch ein Satz.\n\n| eine | Tabellenzeile |\n\n'
           '```python\nx = "kein Text"\n```\n\n'
           '```mermaid\nflowchart TD\n  A["Eine Beschriftung"]\n```\n')
    u = units(doc)
    check("a code fence contributes nothing", any("kein Text" in x for x in u), False)
    check("a mermaid fence IS a translatable surface",
          any("Eine Beschriftung" in x for x in u), True)
    check("a table row is one unit", sum(1 for x in u if x.startswith("|")), 1)
    check("two sentences are two units", sum(1 for x in u if "Satz" in x), 2)

    check("a mistyped source path exits 2 rather than reporting every variant absent",
          main(str(pathlib.Path(__file__).parent / "referent-groups.de.json"), ["/nope/nope"]), 2)

    print()
    if fails:
        print(f"referents --self-test: FAIL ({len(fails)}): {'; '.join(fails)}")
        return 1
    print("referents --self-test: PASS")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2:]))
