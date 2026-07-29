#!/usr/bin/env python3
"""The course list — read from docusaurus.config.ts, never restated.

Why this exists. A course is three names that must agree: its URL prefix (`routeBasePath`,
e.g. `/rag-agents`), its English content dir (`docs/`, `docs-<id>/`) and its i18n dir
(`i18n/<loc>/docusaurus-plugin-content-docs[-<id>]/`). Two gates need to travel between
them — scripts/i18n-link-check.sh maps a broken page's URL back to a translation file, and
scripts/locale_parity.py walks each English tree against its translated counterpart — and
both used to carry their own copy of the table. That is one hard-coded special case per
course per gate, and it is a bug with a delay fuse: #307 was exactly this, a mapping that
knew only about the first course and silently classified the entire second one as
untranslated.

So the table is DERIVED here, from the `COURSES` array in docusaurus.config.ts, using the
same two construction rules the config itself applies:

  * the FIRST course is the preset docs instance (`id: 'default'`): content in `docs/`,
    i18n in the UN-suffixed `docusaurus-plugin-content-docs/`;
  * every other course is a `@docusaurus/plugin-content-docs` entry: content in
    `docs-<id>/` (the config writes ``path: `docs-${c.id}/` ``), i18n in
    `docusaurus-plugin-content-docs-<id>/` (Docusaurus' own per-instance dir naming).

Adding a third course therefore needs no edit here and none in either gate.

Parsing is deliberately strict, in the spirit of `released_locales()` in locale_parity.py:
if the constant moves or changes shape this ABORTS rather than returning a short or empty
list, because a silently short list is a fail-OPEN — an unrecognised course would become a
blanket exemption in the link gate and an unchecked tree in the parity gate.

Usage:
    from courses import courses                 # -> list[Course]
    python3 scripts/courses.py                  # TSV: basePath<TAB>docsDir<TAB>i18nDir<TAB>locales
"""

from __future__ import annotations

import os
import re
import sys
from typing import NamedTuple

CONFIG = "docusaurus.config.ts"

# The preset (first) docs instance. Docusaurus names its i18n dir without an id suffix and
# defaults its content path to `docs/`; both are unique to this id.
DEFAULT_INSTANCE_ID = "default"
I18N_DIR_PREFIX = "docusaurus-plugin-content-docs"


class Course(NamedTuple):
    id: str        # docs-plugin instance id ('default' = the preset instance)
    base: str      # routeBasePath with no slashes, e.g. 'rag-agents' — the URL segment
    docs_dir: str  # English content dir, e.g. 'docs' / 'docs-ai-sdlc'
    i18n_dir: str  # per-locale dir under i18n/<loc>/, e.g. 'docusaurus-plugin-content-docs'
    # Locale codes the course CLAIMS — its `locales` field in the config. A course is not
    # necessarily translated everywhere the SITE is: scope is per course, so a gate must
    # ask the course rather than assume the site-wide answer. Parsed strictly and never
    # defaulted (see _abort below): an empty or unreadable declaration would make every
    # locale a blanket exemption, which is the fail-open the field was added to close.
    locales: tuple[str, ...]


def _abort(message: str) -> "None":
    sys.exit(
        f"courses.py: ERROR — {message} The course table is derived from {CONFIG}; a gate "
        "cannot honestly run on a partial one, so it refuses to run rather than pass "
        "silently. Fix the parse in courses.py."
    )


def courses(config_path: str = CONFIG) -> list[Course]:
    """Every course declared in docusaurus.config.ts, in declaration order."""
    if not os.path.isfile(config_path):
        _abort(f"{config_path} not found (run from the repo root).")
    with open(config_path, encoding="utf-8") as fh:
        text = fh.read()

    block = re.search(r"const\s+COURSES\s*:\s*Course\[\]\s*=\s*\[(.*?)\n\];", text, re.S)
    if not block:
        _abort("could not find the `const COURSES: Course[] = [ … ];` array.")
    body = block.group(1)

    # Read `id` first, then the `basePath` belonging to the SAME object — i.e. the first one
    # appearing before the next `id:`. Two independent findall() lists would silently pair the
    # wrong values the day a course object writes its fields in another order.
    starts = [m for m in re.finditer(r"^\s*id:\s*'([\w-]+)',", body, re.M)]
    if not starts:
        _abort("the COURSES array declares no `id:` field.")

    out: list[Course] = []
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(body)
        chunk = body[m.end():end]
        bp = re.search(r"^\s*basePath:\s*'([^']*)',", chunk, re.M)
        if not bp:
            _abort(f"course '{m.group(1)}' declares no `basePath:`.")
        cid = m.group(1)
        base = bp.group(1).strip("/")
        if not base:
            _abort(f"course '{cid}' has an empty basePath; a course must own a URL prefix.")

        loc = re.search(r"^\s*locales:\s*\[([^\]]*)\],", chunk, re.M)
        if not loc:
            _abort(
                f"course '{cid}' declares no `locales:`. Every course states which locales it "
                "claims; there is no default, because the default would be 'all of them' — the "
                "assumption per-course locale scope exists to remove."
            )
        claimed = tuple(re.findall(r"['\"]([\w-]+)['\"]", loc.group(1)))
        if not claimed:
            _abort(f"course '{cid}' has an empty `locales:` list; it must claim at least 'en'.")
        if "en" not in claimed:
            _abort(
                f"course '{cid}' does not claim 'en'. The English tree is the source every "
                "other locale is compared against, so every course has one."
            )

        suffix = "" if cid == DEFAULT_INSTANCE_ID else f"-{cid}"
        out.append(
            Course(
                id=cid,
                base=base,
                docs_dir="docs" if cid == DEFAULT_INSTANCE_ID else f"docs-{cid}",
                i18n_dir=f"{I18N_DIR_PREFIX}{suffix}",
                locales=claimed,
            )
        )

    bases = [c.base for c in out]
    if len(set(bases)) != len(bases):
        _abort(f"two courses share a basePath ({sorted(bases)}); the URL prefix must be unique.")
    return out


if __name__ == "__main__":
    for c in courses():
        print(f"{c.base}\t{c.docs_dir}\t{c.i18n_dir}\t{','.join(c.locales)}")
