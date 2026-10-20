---
title: "Architecture erosion"
sidebar_position: 2.5
---

# A sequence of reasonable fixes can dismantle the architecture

[Drift control and rule rot](./drift-and-rot.md) dealt with the decay of the rule corpus and project memory:
the instructions stop matching the system. Here the direction reverses. The decisions may still be current,
but the code stops obeying them. An agent fixes the immediate problem, the patch passes, and another boundary
quietly disappears.

[Perry and Wolf named architectural drift and architectural erosion in 1992](https://users.ece.utexas.edu/~perry/work/papers/swa-sen.pdf).
Drift comes from insensitivity to the architecture; erosion comes from violating it. The distinction matters
because drift prepares the ground for erosion: an architecture that has become less coherent and harder to see
is easier to violate next time. For agent work, treat drift as the default condition: the agent solves the local task with the context
it has now. Preserving the shape of the whole system needs an explicit mechanism.

That mechanism joins decisions to code. Keep a decision log that every fix consults, turn the structural
constraints into executable checks, and agree when repeated patching must give way to redesign. A reversed
decision stays in that log, marked superseded, so the history never passes for the current rule.

## How erosion gets in: through the small fix \{#how-erosion-gets-in-through-the-small-fix}

[Andrey Beloborodov, a practitioner who writes about running AI-first development on his own projects](https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/),
describes a project changing its rules without anyone deciding to change its architecture. Duplicates appear,
identical scenarios acquire different handling, and a fix breaks a neighbouring branch of the functionality.
These reports describe one person's experience on his own projects, not a measured comparison of development
methods.

In his account, small fixes are the easiest entry point. Each looks safe enough to skip an architecture check;
the accumulated result is a different design. His example has a recognisable sequence: an agent changes a
contract, another builds a parallel implementation, and another documents the resulting workaround. Every
individual step can look diligent.

Consider a billing module that owns invoice eligibility and a notifications module that consumes its result.
An agent repairs a missing email by copying the eligibility check into notifications. The immediate case works.
A later billing change updates only the original check, so another agent adds an exception to the copy. Nobody
proposed transferring ownership of the decision. The patches transferred it anyway.

Some re-fixing is normal, and not only for agents. A [2012 study of supplementary bug fixes by Park,
Kim, Ray and Bae](https://web.cs.ucla.edu/~miryung/Publications/msr2012-supplementarypatch.pdf), covering Eclipse JDT core,
Eclipse SWT and Mozilla, found that 22%–33% of resolved bugs involved more than one fix attempt. Only a small
share of supplementary patches resembled the initial patch, and in the two Eclipse projects 14%–15% of
supplementary-patch files neither overlapped the initial patch nor depended on it directly. A single follow-up is
ordinary even in the human baseline. What should worry you is a run of fixes in the same area — so map further
than the first diff.

:::tip[▶ Video]

<YouTube id="FgaBdwSvOGM" title="Agentic Engineering vs Software Engineering: Beyond Vibe Coding — IBM Technology" />

IBM Technology's Anna Gutowska explains how agentic systems can appear correct while making flawed decisions,
including producing architecturally poor solutions. Her account puts the bottleneck in supervising,
constraining and evaluating the work, which is exactly the missing step in the small-fix path above.

:::

## Decision before change: an ADR log that every fix consults \{#decision-before-change-an-adr-log-that-every-fix-consults}

In his [account of architectural control as a dynamic system](https://realaillusions.com/ru/materials/sovety_ai_praktika_part3/),
Beloborodov describes a project that grew to a scale he compares to a small team of 10–20 people. A described
architecture existed, yet changes and fixes were blurring it. His response was an architecture decision record,
or ADR, log: a repository file registered in every agent's settings. Agents consulted it when preparing the next
brief and when starting any change or bug fix. He reports that one coding agent was particularly prone to adding
mutually contradictory workarounds during those changes and fixes.

In his own account, proliferating exceptions and wrong programming decisions fell severalfold; he gives no
figure. Tasks spanning several blocks became cleaner. He acknowledges extra work for the agents, while arguing
that the burden was smaller than it might sound. Treat this as a mechanism worth adopting and evaluating in your
own project, not an improvement factor you can import.

His rule behind it is to record an architectural decision before changing the system to implement it. That
requires shared working artefacts: a system map, module boundaries, contracts and the decisions already taken.
He also argues for an independent critic, separate from the builder, that checks the direction of the whole
solution, including its business meaning, and he recommends a regular organisational audit of whether parallel
solutions have appeared and whether accumulated fixes have changed the project's course.

Use [Michael Nygard's 2011 pattern](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), already
introduced in [Preparation over model](../part-1-foundation/preparation-over-model.md). Each ADR has Title,
Context, Decision, Status and Consequences. Context records the forces behind the choice; Consequences records
the situation that choice creates. Number decisions sequentially without reusing numbers. A proposed decision
can become accepted, then deprecated or superseded. If you reverse it, keep the old record, mark it superseded,
and point to its replacement. This is the log's answer to memory drift: a later agent can distinguish history
from current authority.

Make the bug-fix brief ask for the governing ADR numbers and an explicit judgement about whether the proposed
fix conforms. If it needs to break an accepted decision, stop the implementation and turn the exception into a
proposal for a superseding ADR. Give each decision area an owner who accepts or rejects that proposal before
any structural change goes in.

Then give the critic the accepted log as well as the diff. In the billing example, restoring the email is only
part of the review: the critic must also check whether notifications has taken over a billing responsibility.
This applies the [plan–review–implement–critic loop](../part-2-loop/plan-review-implement-critic.md) to structural
conformance. Keep additions to the log serial, as [Running agent fleets](./agent-fleets.md) recommends for
other accretive artefacts: two agents working in parallel must not each write their own version of the same
decision.

## Architecture as executable constraints \{#architecture-as-executable-constraints}

An ADR explains why a boundary exists. A fitness function checks whether an architectural characteristic still
holds. The [Thoughtworks Technology Radar entry](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function),
drawing on Neal Ford, Rebecca Parsons and Patrick Kua's *Building Evolutionary Architectures*, describes this
as an objective assessment of architectural integrity. Existing tests, metrics and monitors can supply it;
the point is to keep checking the characteristics you chose while the system changes.

[Birgitta Böckeler's harness-engineering framing](https://martinfowler.com/articles/harness-engineering.html) calls
this an architecture fitness harness: guides and sensors that define and check the application's
architectural characteristics. Her example is a pre-commit or coding-agent hook running ArchUnit checks for
module-boundary violations. This is [Rules that hold](../part-1-foundation/rules-that-hold.md) applied to the
shape of the code. A request to respect module boundaries becomes a check that rejects a forbidden dependency.

Choose the boundaries deliberately. Perry and Wolf's building analogy distinguishes load-bearing walls from
decoration: some changes damage the structure that makes the system work. In an invented orders application,
the `orders` package must not import `ui` because domain decisions must remain independent of presentation. That
is worth a gate. Freezing every incidental package arrangement would instead make ordinary reorganisation a
policy dispute. Encode the dependency that carries the decision, and keep its rationale in the ADR.

Pick the checker for your language. [ArchUnit](https://www.archunit.org/userguide/html/000_Index.html) checks Java
architecture through ordinary unit-testing frameworks, including permitted access between layers and cycles
between slices. [Import Linter](https://import-linter.readthedocs.io/en/stable/) checks Python import contracts; its
contract types include forbidden dependencies, protected modules, layers and independence. Contracts
live in configuration and the `lint-imports` command checks them. For JavaScript and TypeScript,
[dependency-cruiser](https://github.com/sverweij/dependency-cruiser) validates dependencies against your rules and
reports violations for builds; its `--init` setup adds circular-dependency rules.

You do not have to repair an eroded system before a gate pays off. ArchUnit's
`FreezingArchRule` stores the existing violations on its first run and subsequently reports new ones. Fixed
violations disappear from the store, so they cannot return unnoticed. Use that as a ratchet: acknowledge the
baseline, prevent further erosion, and retire violations through deliberate work. Do not let the agent fixing
the code edit the frozen baseline.

[jscpd](https://github.com/kucherenko/jscpd) adds a literal duplication check, with `--threshold` controlling the
allowed duplication level across the tree. Its documentation notes that Super-Linter and MegaLinter run it with
threshold 0 by default, which fails a build on any duplication at all. Zero tolerance is defensible, but adopt
it on purpose; it does not replace the boundary rules.

Nor should clones be your only maintainability signal. As [Reading the evidence](../part-1-foundation/reading-the-evidence.md)
explains, GitClear's widely repeated duplication claim cannot be checked: it states no method and has no per-line
AI attribution. The [Carnegie Mellon difference-in-differences study](https://arxiv.org/abs/2601.13597) found the
agent-first duplication change statistically insignificant, while complexity and static-analysis warnings rose
significantly. Gate those too; copy-paste is one symptom among several.

## Which principles a machine can check \{#which-principles-a-machine-can-check}

In his practice tips, Beloborodov recommends stating YAGNI, KISS, SRP and DRY explicitly because a generic instruction
to follow best practices does not reliably produce what he wants. His interpretations are concrete: avoid
unrequested abstractions, seek the simplest implementation, keep functions focused, and reuse existing logic.
He also warns against loading every rule into configuration at once. His rule-making loop starts with a bad
result, analyses its cause, then adds a rule addressing that error.

The four principles do not become executable in the same way. Use the following split when designing the
harness. The machine column contains checks or proxies; the critic column holds the judgements those checks
cannot make.

| Principle | What a machine can check | What stays a critic's question |
|---|---|---|
| DRY | Literal clones against a duplication threshold | Does differently written code repeat the same business decision? |
| SRP | Length, cyclomatic complexity and dependency counts as proxies | Does this unit have a coherent responsibility? |
| KISS | A narrow constraint, such as a forbidden new dependency | Is there a simpler way to preserve the required behaviour? |
| YAGNI | Flag a new abstraction with a single implementation | Does a present requirement justify this abstraction? |

A single implementation is a reason to ask, and proves nothing about waste. An interface may preserve a deliberately
chosen boundary. Likewise, a short function can mix unrelated responsibilities, and splitting it to satisfy
a length limit can leave that mixing intact. A proxy catches one symptom of a principle; a passing proxy says
nothing about the rest.

DRY has the clearest computational part: a clone detector can find literal repetition. Böckeler distinguishes
that structural work from semantic judgement — what she calls inferential checking — where LLM review is
expensive and probabilistic. In the billing
example, eligibility copied and then rewritten may evade the duplication detector while preserving the same
ownership error. Ask the critic where the business decision belongs. A clean duplication report cannot answer that.

Make the computational part a gate and retain the inferential part as a critic question. Apply expensive
semantic review where the change warrants it; do not turn every commit into an unbounded architectural audit.
The point is to know which assurance you bought.

## Fix-on-fix: the signal and the redesign trigger \{#fix-on-fix-the-signal-and-the-redesign-trigger}

Beloborodov uses three consecutive edits as his warning: fixes accumulating on fixes mean it is time to return to
architectural work. Nobody has measured whether three is the right threshold. Use it as a starting value for
an agreed redesign trigger, scoped to a defined area with a visible history. It is not a universal law about
patch quality.

Make that history useful by tracking a fix-on-fix rate per module. Count a fix that touches an area another
fix touched within a chosen recent window, or link successive fixes to the same issue, as Park and colleagues
did for supplementary patches. Choose the window and definition before reading the trend. Agree the trigger
before it fires, so the next urgent bug does not become a reason to redefine the signal.

Park and colleagues' baseline is why the area and the sequence matter: a follow-up fix is common, and it often
lands beyond the first patch's neighbours. A global count would mix ordinary incomplete repairs with a local
design failure. Look for consecutive re-fixes around the same responsibility, then inspect them against the
system map and decision log. When the trigger fires, someone investigates and redesigns where needed. It does
not authorise an agent to replace the module.

On recovery, he warns against an open-ended instruction to rewrite everything properly. He argues that this produces another project with another set of problems. Start with
an audit of where debt actually blocks development, which decisions can remain, and which areas need separate
preparation before they can change. Establish the target architecture and a sequence of stages, each ending
in a working result. You are managing debt deliberately. Some of it will stay.

For the billing example, first decide where eligibility belongs and which consumers must use that contract.
Then make a stage that moves a consumer back behind the boundary and verifies its behaviour before proceeding.
A later stage can remove the redundant implementation. Keep the current decision visible throughout, and
have the critic assess each stage against it. A broad cleanup request leaves those choices to the fixer;
a staged redesign makes them reviewable before the next patch depends on them.

:::tip[▶ Video]

<YouTube id="f84XbvASkk4" title="What Is AI Code Refactoring? Agentic AI & Safe Code Changes — IBM Technology" />

IBM Technology's Martin Keen explains refactoring as changing internal structure while preserving external
behaviour, and shows the risk of vague goals such as cleaning up a whole module. His guardrail loop includes
planning, reading, searching, reporting, human approval, snapshotting, patching, verification and rollback:
the controls that make a redesign stage bounded and recoverable.

:::

## The three tiers — soloist · small-team · enterprise \{#the-three-tiers--soloist--small-team--enterprise}

**The invariant: record the decision before changing the structure, enforce its checkable boundaries, and
agree when repeated fixes require redesign.** Scale changes the ownership and the evidence required.

- **Soloist.** Keep a decision-log file the agent reads before any fix. Add one or two import or dependency
  rules for load-bearing boundaries, and count re-fixes per area by hand. *The failure it prevents:* an agent
  neatly documenting a workaround as if it were the architecture.
- **Small-team.** Assign an owner per ADR area and supersede decisions rather than deleting them. Have the
  critic check conformance against the log. Put fitness functions in CI the agents cannot edit; freeze existing
  violations and ratchet them down. Track the fix-on-fix trend per module against a trigger agreed in advance.
  *The failure it prevents:* agents building parallel implementations of the same contract.
- **Enterprise.** Make ADRs governed records linked to change records, following the [ADR library and
  change-control board](../part-1-foundation/preparation-over-model.md)
  and the [enterprise tier](./enterprise-tier/index.md). Enforce fitness functions as pipeline policy; require
  an owner-approved superseding ADR before breaking an accepted decision. That gives you the capability —
  blocking an unapproved structural change — and the proof: a trace from each change to its governing decision.
  *The failure it prevents:* architecture surviving on slides after the system has diverged from it.

## What to take away \{#what-to-take-away}

- **Small fixes can change the architecture.** Review the ownership and contracts they affect, even when the
  immediate behaviour is restored.
- **Decision before change.** Make every bug-fix brief cite governing ADRs. A necessary exception becomes a
  superseding decision before implementation, checked by someone other than the fixer.
- **Execute the load-bearing constraints.** Gate dependency boundaries, complexity and warnings alongside
  duplication. Freeze existing violations when adoption would otherwise require a wholesale cleanup.
- **Keep principles and proxies distinct.** A machine can reject a forbidden import; a critic must still
  judge whether the solution preserves the intended responsibility.
- **Track consecutive re-fixes in the same area.** Agree a redesign trigger beforehand. Three is a
  practitioner's heuristic, not a measured optimum.
- **Redesign in working stages.** Audit the debt, record the target and verify each stage. An open-ended
  rewrite request supplies none of those controls.

**[New terms](../glossary.md#architecture-erosion)**: architecture erosion / architectural drift, decision before change, ADR log, superseded ADR, fitness function, dependency rule / import contract, frozen violations, duplication gate, fix-on-fix rate, redesign trigger, redesign vs rewrite.
