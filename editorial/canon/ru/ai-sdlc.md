# AI SDLC term ledger (RU/EN)

The **living** term ledger for the AI SDLC course in RU/EN. It records this course's term decisions —
kept-EN vs native form, casing, bridge glosses, rejected variants — the way `rag.md` does for RAG. It grows
with the course: every new lesson seeds its new terms here and settles them during native authoring.

**Load with `_language.md`.** When authoring this course, load `_language.md` (the shared RU/EN language
rules) **plus this ledger** as your standing context. The language rules are course-independent; the term
decisions below are this course's own.

## Governance + cross-course peek protocol

> **Cross-course term consistency — peek, don't load.** When authoring this course, load ONLY `_language.md` + this ledger as standing context. For a term that plausibly overlaps a sibling course (shared AI-engineering vocabulary — agent, prompt, token, context, eval, guardrail, retrieval…), do a TARGETED, read-only lookup in the sibling ledger(s): if a decision exists and the sense matches, REUSE it verbatim and cite it — do not re-coin. If the sense genuinely differs, FLAG for a human — do not silently fork. Never edit a frozen sibling ledger (`rag.md`). Loading a whole sibling ledger as priming context is prohibited — that is the pollution this split prevents.

## Settled terms — Part I

Settled during the Part I canon bootstrap from the **de-jargoned** EN labels (the six academic coinages were
simplified per PART-1-BRIEF's Register ruling; community terms-of-art kept as-is). Each decision is native
from the EN meaning — never a literal translation. Register: **practitioner** — a term a mid-level RU engineer
would not say at work is wrong. `REUSE` rows carry the RAG-canon citation; the grade tokens
`MEASURED` / `REPORTED` / `ASSERTED` stay kept-EN, code-styled, with a one-time gloss «(измерено / сообщено /
заявлено)».

### Intro

| EN term | EN gloss | RU decision |
|---|---|---|
| Verification bottleneck | the binding constraint in agent-built software: generation is cheap, checking is not; throughput is gated by review/verification capacity, not by model capability. | **native — «узкое место проверки»** (мост *(verification bottleneck)* при первом упоминании). «проверка» — практикующая, plain; «верификация» допустима как синоним в теле. Строчными в прозе. **Отвергнуто:** «бутылочное горлышко» (калька bottleneck; «узкое место» — идиоматичная русская форма). |
| The loop closes on production | the design principle that the feedback edge must return from live operation to planning; a scheme that ends at internal QA is a pipeline, not a loop. | **native — фраза «цикл замыкается на проде»** (не однословный термин). `цикл` — REUSE смысла из RAG (planning loops = «циклы»). «прод» / «продакшн» — устоявшийся dev-жаргон. **Отвергнуто:** «петля замыкается» («петля» двоится с loop-в-верёвочном смысле; «цикл» однозначнее). |
| Human router | the human's role above the loop: guardrail and judgment at named checkpoints, not a stage inside it. | **вводится как «человек-в-цикле»** (REUSE `rag.md`: «человек-в-цикле (human-in-the-loop, HITL)», строка про HITL — форма без дефисов «человек в цикле» тоже канонна), затем несёт авторский ярлык **«человек-маршрутизатор»** — фигура, **НА ИСПЫТАНИИ** (проверяется холодным прогоном как обычная калька). См. CONTESTED-заметку ниже. |
| Substrate → **Foundation** | Part I's subject: project memory, rules-as-code, artifacts-as-the-only-interface. | **native — «фундамент»** (термин де-жаргонизирован: substrate → foundation). Строчными. **Отвергнуто:** «субстрат» (непрозрачная академическая калька). |
| Tier lens | the SOLOIST/SMALL-TEAM/ENTERPRISE reading applied to every mechanism; "practice constant, mechanism scales." | **native — «оптика трёх уровней»** (соло · команда · энтерпрайз); `уровень` = tier. Мост *(tier lens)*. **Отвергнуто:** «линза уровней» (механический перенос). |
| Proof-vs-capability | close to production a control is about what it *prevents*; far from it, about what you can *prove*. | **НЕ термин — plain phrasing** (де-жаргонизировано; «градиент» снят). Выражается предложением: «ближе к проду контроль — про то, что он предотвращает; дальше — про то, что можешь доказать». Не вводить как именованный термин. |

### The verification bottleneck

| EN term | EN gloss | RU decision |
|---|---|---|
| Proxy metric | any measured stand-in for value (merged PRs, commits, LOC, time-on-task); throughput is measurable, value is not. | **гибрид — «прокси-метрика»** (kept-EN приставка `прокси` + «метрика»; устоявшаяся форма RU DevOps). **Отвергнуто:** «метрика-заместитель» (годится как разовый глосс, но не термин). |
| Denominator choice | "% of code written by AI" figures depend entirely on the denominator; same telemetry → 28.7% vs 70.6%. | **native — «выбор знаменателя»** (прозрачные математические слова). Мост не нужен. |
| Benchmark-to-production gap | the collapse from offline benchmark score to real-SDLC applied rate (Meta 68%→19.7%, ~3.5×). | **гибрид — «разрыв между бенчмарком и продом»**; `бенчмарк` kept-EN (устоявшееся). **Отвергнуто:** «оффлайн-онлайн разрыв» (мутно). |
| Self-assessment gap | developers cannot judge AI's effect on their own speed; measured error ~40pp, wrong even about the sign. | **native — «ошибка самооценки»**. **Отвергнуто:** «разрыв самооценки» (калька gap). |
| Tech debt on credit | velocity gained early, paid back later as sustained complexity/warning increases that drive the slowdown. | **native — «техдолг в кредит»** (де-жаргонизировано: complexity debt → tech debt on credit). «технический долг» / «техдолг» — устоявшееся. Мост *(tech debt on credit)*. |

### Reading the evidence

| EN term | EN gloss | RU decision |
|---|---|---|
| Evidence grade / the ladder | the `MEASURED` / `REPORTED` / `ASSERTED` classification; grades inherited, never upgraded. | **native — «уровень доказательности» / «лестница доказательности»**. Токены `MEASURED` / `REPORTED` / `ASSERTED` — **kept-EN, code-styled, инвариант**; разовый глосс «(измерено / сообщено / заявлено)» при первом появлении. **Отвергнуто:** перевод токенов в теле каждый раз (теряется единый ярлык-якорь). |
| Can't-be-checked | a claim whose weakness is that nobody can check it (private corpus, no method), distinct from tested-and-failed. | **НЕ термин — plain «это нельзя проверить»** (де-жаргонизировано; «нефальсифицируемо, но не опровергнуто» снято). **Отвергнуто:** «нефальсифицируемое утверждение» (академизм). |
| Citation laundering | a distorted claim passed along until it looks sourced. | **фигура «отмывание ссылок» — НА ИСПЫТАНИИ**, глосс при первом употреблении «искажённое утверждение, которое пересказывают, пока оно не начнёт выглядеть как исследование». **Отвергнуто:** «отмывание цитат» («цитата» двоится с прямой цитатой). Проверяется холодным прогоном. |
| Evidence that cuts against whoever published it | a result that cuts against its publisher's incentive; the strongest evidence class in a field full of COI. | **native — «свидетельство против собственного интереса»** (де-жаргонизировано из against-interest finding; юридическая по происхождению формула). **Отвергнуто:** «находка против интереса» (калька finding). |
| Conflict of interest, stated inline | naming the conflict of interest (who's paying) as part of the finding, not a footnote. | **native — «конфликт интересов, названный прямо»** (де-жаргонизировано из positionality); `конфликт интересов` (COI) — стандарт. **Отвергнуто:** «позициональность» (непрозрачно). |

### Preparation over model

| EN term | EN gloss | RU decision |
|---|---|---|
| Preparation-over-model | setup/scope moves agent success more than model choice (dotnet/runtime 38.1%→69%). | **native — максима «подготовка важнее модели»**. |
| The gate-not-the-agent misread | reading a low revert/failure number as agent quality when it's a property of the review gate. | **native — «это заслуга ворот, а не агента»**; `ворота` = gate (REUSE `rag.md`: «релизные ворота», «регрессионные ворота (quality gate)»). |
| Controllable scope | starting agent work where the problem is bounded and knowable, with a human approval gate at the requirements boundary. | **native — «управляемый объём задачи»** / «контролируемый периметр». **Отвергнуто:** «управляемый скоуп» (жаргон-калька; «объём» чище). |
| Architecture-first (with a loop) | investing in design before code, while accepting even sound architecture needs iteration. | **native — «сначала архитектура (но с циклом)»**. |
| Harness staleness | every scaffold component encodes an assumption about model limits that expires as models improve. | **kept-EN — «устаревание harness»**; `harness` kept-EN (REUSE `rag.md`: голое «harness» в теле допустимо после первого моста, рядом с «средой выполнения»). Мост «harness (обвязка агента)» при первом упоминании. **Отвергнуто:** голое «каркас» как термин (теряет kept-EN якорь). |

### Project memory & tiering

| EN term | EN gloss | RU decision |
|---|---|---|
| Project memory | durable, agent-readable knowledge that persists across runs; the fix for agent amnesia. | **native — «память проекта»**. **Отвергнуто:** «проектная память» (звучит канцелярски). |
| Amnesia | agents retain nothing between sessions except artifacts on disk. | **native — «амнезия»** (авторская фигура «умный друг с амнезией»). |
| Context tax / "length is a subscription" | the MEASURED >20%-per-turn cost of standing context; every line is re-sent and billed. | **REUSE фигуры «токенный налог»** (`_language.md` §6 / RU-канон — подтверждённая фигура «токенный налог»: постоянная плата токенами) + обязательная plain-пара «каждая строка оплачивается на каждом шаге»; «длина — это подписка, а не документ». `context rot` — **kept-EN** (глосс «гниение контекста»). |
| Over-compliance | agents follow instructions "thoroughly but unnecessarily," burning cost without improving outcomes. | **native — «избыточная исполнительность»** / «сверхусердие». **Отвергнуто:** «сверх-комплаенс» (офисный жаргон). |
| Scar archive | the reasoning behind each locked decision, appended after every fixed bug class. | **фигура «архив шрамов» — НА ИСПЫТАНИИ**, глосс при первом употреблении + мост к индустрии «безвинный разбор инцидентов (blameless postmortem)». Проверяется холодным прогоном. |
| Knowledge tiering | organizing memory by rate-of-change / distance-from-focus so only the relevant tier loads. | **native — «разбиение знаний по уровням»** / «уровневое хранение знаний»; `tiering` = «разбиение по уровням». |
| Detail tiers (map / contract / blueprint) | the three-level tiering of an artifact by its relation to the current task. | **native — «уровни детализации (карта / контракт / чертёж)»** (де-жаргонизировано: «LOD» снят). Собственные ярлыки DefinitiveSpec (LOD_0/1/2) цитируются как имя того инструмента, не как термин курса. **Отвергнуто:** «LOD-лестница». |
| Hot set / cold set | the always-loaded one-screen non-negotiables vs the on-demand retrieved detail. | **native, term-of-art KEEP — «горячий набор / холодный набор»** (прозрачно) + мост *(hot set / cold set)* при первом упоминании. |
| Load detail on demand | loading only name+description until the body is needed, then paging it in. | **native — «подгрузка деталей по требованию»** (де-жаргонизировано из progressive disclosure). **Отвергнуто:** «прогрессивное раскрытие» (кроме одного глоссированного упоминания). |
| Artifact overload | artifacts generated faster than human review or model context can absorb, with no lifecycle discipline. | **native — «перегрузка артефактами»**; `артефакт` — родное. |

### Rules that hold

| EN term | EN gloss | RU decision |
|---|---|---|
| Executable rule / rules-as-code | a constraint enforced by the harness or CI which the model cannot bypass. | **native — «исполняемое правило» / «правила как код»**. |
| "An instruction is not a control" | a rule stated in natural language is a suggestion, not an enforced boundary. | **native — максима «инструкция — это не контроль»** (в кавычках/курсиве по бюджету §8). |
| Hook vs skill | a hook is deterministic harness enforcement; a skill is model judgment it may ignore. | **kept-EN — «hook против skill»** (REUSE `rag.md`: hooks/callbacks в kept-EN реестре; skill kept-EN). Глосс «hook (детерминированный перехватчик харнесса) против skill (совет, который модель может проигнорировать)». |
| The gate defines the artifact | an agent optimises exactly what you check; anything unchecked does not exist. | **native — максима «что проверяешь, то и получаешь»** / «ворота определяют результат»; `ворота` — REUSE. |
| Reward hacking / gaming the gate | satisfying the checked metric without doing the requested work. | **kept-EN — «reward hacking»** (community term-of-art, KEEP) + глосс «игра на метрику вознаграждения: пройти проверку, не сделав работу». **Отвергнуто:** «взлом вознаграждения» (буквальная калька). |
| Blast radius | the scope of damage a confused or compromised agent can reach. | **kept-EN — «blast radius»** (term-of-art, KEEP; RU DevOps так и говорит) + глосс «радиус поражения». |
| Policy-as-code | enforced-in-the-pipeline, audited rules (the enterprise form of executable rules). | **kept-EN — «policy-as-code»** (term-of-art, KEEP) + глосс «политики как код». |
| Least privilege | the agent can reach exactly the resources its task needs and no more. | **REUSE — «принцип наименьших привилегий»** (`rag.md`: «принцип наименьших привилегий \| least privilege \| термин остаётся EN в списках, это его мост»). Не пере-чеканивать. |
| Drift / rule rot | the decay of a rule corpus without a staleness mechanism. | **REUSE «дрейф»** (`rag.md`: «дрейф \| drift») — **СМЕЩЁННЫЙ СМЫСЛ, флаг:** в RAG «дрейф» = дрейф входа/корпуса/модели; здесь смысл — расхождение/загнивание корпуса правил. Реюз «дрейф» для расхождения + **«устаревание правил»** для rule rot. **Отвергнуто:** «сдвиг» (RAG резервирует против него как термина). |
| Consistency owner | the role accountable for reconciling a rule corpus so two files can't prescribe opposite things. | **native — «ответственный за согласованность»**. |

## CONTESTED — needs owner / Codex arbitration

- **Human router → «человек-маршрутизатор» (label).** The community term «человек-в-цикле» anchors the intro
  (REUSE), but the vivid label is an author figure. Options: (a) «человек-маршрутизатор» (kept as coined
  figure, on probation); (b) keep only «человек-в-цикле» and drop the router label in RU; (c) plain
  «человек над циклом». Evidence: no community RU term for "router-as-a-person"; the figure must survive a
  cold naive-reader pass before promotion. Recommend (a) on probation.
- **Citation laundering → «отмывание ссылок» (figure).** Coinage on probation; a cold reader must decode
  «отмывание» in the laundering sense from the inline gloss, not from the EN page. If it fails the cold pass,
  fall back to the plain phrasing and drop the figure.
