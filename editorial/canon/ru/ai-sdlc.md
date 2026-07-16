# AI SDLC term ledger (RU/EN)

The **living** term ledger for the AI SDLC course in RU/EN. It records this course's term decisions —
kept-EN vs native form, casing, bridge glosses, rejected variants — the way `rag.md` does for RAG. It grows
with the course: every new lesson seeds its new terms here and settles them during native authoring.

**Load with `_language.md`.** When authoring this course, load `_language.md` (the shared RU/EN language
rules) **plus this ledger** as your standing context. The language rules are course-independent; the term
decisions below are this course's own.

## Governance + cross-course peek protocol

> **Cross-course term consistency — peek, don't load.** When authoring this course, load ONLY `_language.md` + this ledger as standing context. For a term that plausibly overlaps a sibling course (shared AI-engineering vocabulary — agent, prompt, token, context, eval, guardrail, retrieval…), do a TARGETED, read-only lookup in the sibling ledger(s): if a decision exists and the sense matches, REUSE it verbatim and cite it — do not re-coin. If the sense genuinely differs, FLAG for a human — do not silently fork. Never edit a frozen sibling ledger (`rag.md`). Loading a whole sibling ledger as priming context is prohibited — that is the pollution this split prevents.

## Terms to settle

The AI SDLC term set, seeded from the course skeletons — the native writers' term to-do list. Each RU
decision is **TBD (decide during authoring)**: settle it natively from the EN meaning (never by translation),
enter the kept-EN-vs-native call + the bridge gloss, and cite any RAG-canon reuse per the peek protocol
above. Do **not** pre-fill translations here.

### Intro

| EN term | EN gloss | RU decision |
|---|---|---|
| Verification bottleneck | the binding constraint in agent-built software: generation is cheap, checking is not; throughput is gated by review/verification capacity, not by model capability. | **TBD** (decide during authoring) |
| The loop closes on production | the design principle that the feedback edge (incidents, telemetry, drift) must return from live operation to planning; a scheme that ends at internal QA is a pipeline, not a loop. | **TBD** (decide during authoring) |
| Human router | the human's role above the loop: guardrail and judgment at named checkpoints, not a stage inside it. | **TBD** (decide during authoring) |
| Substrate | Part I's subject: project memory, rules-as-code, and artifacts-as-the-only-interface — what must be true before any agent writes a line. | **TBD** (decide during authoring) |
| Tier lens | the SOLOIST/SMALL-TEAM/ENTERPRISE reading applied to every mechanism; "practice constant, mechanism scales." | **TBD** (decide during authoring) |
| Proof-vs-capability gradient | the further a control sits from the blast radius the more it is about *proof*; the closer, the more it is about *capability*. | **TBD** (decide during authoring) |

### The verification bottleneck

| EN term | EN gloss | RU decision |
|---|---|---|
| Proxy metric | any measured stand-in for value (merged PRs, commits, LOC, characters, time-on-task); throughput is measurable, value is not, and the two must never be equated. | **TBD** (decide during authoring) |
| Denominator choice | the observation that "% of code written by AI" figures depend entirely on what sits in the denominator; the same telemetry yields wildly different headlines (28.7% vs 70.6%). | **TBD** (decide during authoring) |
| Benchmark-to-production gap | the collapse from offline benchmark score to real-SDLC applied rate (Meta's 68%→19.7%, ~3.5×); benchmark numbers do not survive contact with a real SDLC. | **TBD** (decide during authoring) |
| Self-assessment gap | developers cannot judge AI's effect on their own speed; measured error ~40 percentage points, wrong even about the sign. | **TBD** (decide during authoring) |
| Complexity debt (on credit) | velocity gained early, paid back later as sustained complexity/warning increases that drive the eventual slowdown. | **TBD** (decide during authoring) |

### Reading the evidence

| EN term | EN gloss | RU decision |
|---|---|---|
| Evidence grade / the ladder | the `MEASURED` / `REPORTED` / `ASSERTED` classification applied to every claim; grades are inherited and never upgraded. | **TBD** (decide during authoring) |
| Unfalsifiable-not-refuted | a claim whose weakness is that nobody can check it (private corpus, no method), distinct from a claim that has been tested and failed. | **TBD** (decide during authoring) |
| Citation laundering | the drift by which an assertion, a vendor figure, or a misattributed quote acquires the authority of a study as it passes through secondary sources. | **TBD** (decide during authoring) |
| Against-interest finding | a result that cuts against its publisher's incentive (Anthropic publishing a skill cost, OpenAI retiring its own benchmark); the strongest evidence class in a field full of COI. | **TBD** (decide during authoring) |
| Positionality (named COI) | stating the conflict of interest inline as part of the finding, not in a footnote. | **TBD** (decide during authoring) |

### Preparation over model

| EN term | EN gloss | RU decision |
|---|---|---|
| Preparation-over-model | the finding that setup/scope moves agent success more than model choice (dotnet/runtime: 38.1%→69%). | **TBD** (decide during authoring) |
| The gate-not-the-agent misread | reading a low revert/failure number as agent quality when it is a property of the review gate that produced it. | **TBD** (decide during authoring) |
| Controllable scope | starting agent work where the problem is bounded and knowable, with declared inputs/outputs and a human approval gate at the requirements boundary. | **TBD** (decide during authoring) |
| Architecture-first (with a loop) | investing in design before code, while accepting that even sound-looking architecture needs iteration — which is why the loop exists. | **TBD** (decide during authoring) |
| Harness staleness | the property that every scaffold component encodes an assumption about model limits that expires as models improve; preparation must be re-reviewed, not set once. | **TBD** (decide during authoring) |

### Project memory & tiering

| EN term | EN gloss | RU decision |
|---|---|---|
| Project memory | durable, agent-readable knowledge that persists across runs; the fix for agent amnesia. | **TBD** (decide during authoring) |
| Amnesia (the smart friend with amnesia) | the property that agents retain nothing between sessions except the artifacts on disk; anything that must survive must be pinned or re-injected. | **TBD** (decide during authoring) |
| Context tax / "length is a subscription" | the MEASURED >20%-per-turn cost of standing context; every line is re-sent and billed on every turn, so the file must earn its length. | **TBD** (decide during authoring) |
| Over-compliance | the measured mechanism by which extra written artifacts hurt: agents follow instructions "thoroughly but unnecessarily," burning cost without improving outcomes. | **TBD** (decide during authoring) |
| Scar archive | the reasoning behind each locked decision, appended after every fixed bug class; the highest-value section of any project memory because it stops re-litigating decided tradeoffs. | **TBD** (decide during authoring) |
| Knowledge tiering | organizing project memory by rate-of-change / distance-from-focus so only the relevant tier is loaded (type→roster→item; blueprint→contract→map). | **TBD** (decide during authoring) |
| LOD ladder (map / contract / blueprint) | the three-level tiering of an artifact by its relation to the current task; independently mirrored by Anthropic Skills' activation/reference/deep-dive. | **TBD** (decide during authoring) |
| Hot set / cold set | the always-loaded one-screen non-negotiables vs the on-demand retrieved detail. | **TBD** (decide during authoring) |
| Progressive disclosure | loading only an artifact's name+description until its body is needed, then paging it in; the retrieval half of tiering. | **TBD** (decide during authoring) |
| Artifact overload | the central unsolved failure mode of spec-driven work: artifacts generated faster than human review or model context can absorb, with no lifecycle discipline. | **TBD** (decide during authoring) |

### Rules that hold

| EN term | EN gloss | RU decision |
|---|---|---|
| Executable rule / rules-as-code | a constraint enforced by the harness or CI (hook, lint rule, grep, gate), which the model cannot bypass — as opposed to prose it is asked to obey. | **TBD** (decide during authoring) |
| "An instruction is not a control" | the principle that a rule stated in natural language (a freeze, an "ask me first," a "don't") is a suggestion, not an enforced boundary. | **TBD** (decide during authoring) |
| Hook vs skill | a hook is deterministic harness enforcement (runs regardless of the model); a skill is model judgment (advice it may ignore). Security/correctness failures must be hooks. | **TBD** (decide during authoring) |
| The gate defines the artifact | an agent optimises exactly what you check, so anything unchecked does not exist; "the agent grading its own homework" is not verification. | **TBD** (decide during authoring) |
| Reward hacking / gaming the gate | the measured behavior of satisfying the checked metric without doing the requested work (retrieving rather than deriving; suppressing a symptom to make a test pass). | **TBD** (decide during authoring) |
| Blast radius | the scope of damage a confused or compromised agent can reach; controls are placed relative to it. | **TBD** (decide during authoring) |
| Policy-as-code | enforced-in-the-pipeline, audited rules (the enterprise form of executable rules). | **TBD** (decide during authoring) |
| Least privilege | the agent can reach exactly the resources its current task needs and no more (five distinct scopes: repo, CI token, cloud IAM, tool allow-list, network egress). *(SK canon: `princíp najnižších oprávnení` — owner ruling, do not reopen; RU RAG canon mirrors it as `принцип наименьших привилегий`, `rag.md` §7 — peek and reuse if the sense matches.)* | **TBD** (decide during authoring) |
| Drift / rule rot | the decay of a rule corpus without a staleness mechanism: duplicated constants diverge, copied reference code goes stale, rules whose framework changed survive, and seams between files contradict. | **TBD** (decide during authoring) |
| Consistency owner | the person/role accountable for reconciling a rule corpus so two authoritative files cannot prescribe opposite things. | **TBD** (decide during authoring) |
