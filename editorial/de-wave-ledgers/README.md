# German wave ledgers

Working artefacts from the German RAG waves. They are **not** the canon — `editorial/canon/de/` is. These are
the reconciled term ledgers a wave binds its renderers to, kept because the next wave and any re-gate need them
and because they carry reasoning the canon deliberately does not.

## What is here

| file | what it is |
|---|---|
| `WAVE3-TERMS.md` | The binding ledger for RAG Part III — 749 lines. Sense cards with worked sentences, 18 resolved cross-slice collisions, 30 OPEN rows each with a closing condition. **This is what a renderer is bound to.** |
| `LEDGER-A..G.md` | The seven per-slice reconciliations behind it. Each merges two independent attestation runs, records where they disagreed and why one won. |

## Why they are in the repo

They were produced in a session scratchpad and would have been lost. Three things need them:

- **The RAG glossary (#283)** — a single 8 920-word file whose every term must be consistent with 37 shipped pages. The ledger is the only place that consistency is written down.
- **The AI-SDLC waves (#284/#285)** — they need their *own* term pass, because the vocabulary barely overlaps, but they should model its shape on this one rather than reinventing it.
- **The RU/SK re-gate (#345)** — the naturalness gate hardened between waves, so pages rendered against the earlier version carry defects the current gate catches. Knowing what was bound when is how you tell which.

## How to read them, and the limits they state about themselves

**A ruling in a ledger is not automatically in the canon.** The wave routes canon deltas separately; a row here may be a proposal that was never merged. **When they disagree, the canon wins** — and if that gap matters, fix the canon rather than the ledger.

Three limits the ledgers record about themselves, worth knowing before trusting a row:

- **`AGREED ×2` is the most confident and least verified label in them.** Its failure signature is *agreement on the verdict with disagreement on the measurement* — where two runs agree on a ruling and differ on the counts behind it, the agreement is about instinct, not evidence.
- **The corpus can convict but not acquit.** Where the shipped German is already wrong, every independent pass agrees with it confidently. Several rows rest on corpus precedent and say so.
- **The worked sentences carry defects.** At least two are known — copying a worked sentence is exactly what it is for, so read one before reusing it. This is the fifth instance in this project of *the example is the part nobody proofreads*.

Method that produced them: `editorial/de-locale-playbook.md` §13. Tooling: `scripts/locale-review/`.
