# AI SDLC term ledger (SK)

The **living** term ledger for the AI SDLC course in Slovak. It records this course's term decisions —
kept-EN vs native form, casing, bridge glosses, rejected variants — the way `rag.md` does for RAG. It grows
with the course: every new lesson seeds its new terms here and settles them during native authoring.

**Load with `_language.md`.** When authoring this course, load `_language.md` (the shared Slovak language
rules — anti-bohemism, calque templates, verb-by-object, typography, register, bridge, bold, figure
probation) **plus this ledger** as your standing context. The language rules are course-independent; the term
decisions below are this course's own.

## Governance + cross-course peek protocol

> **Cross-course term consistency — peek, don't load.** When authoring this course, load ONLY `_language.md` + this ledger as standing context. For a term that plausibly overlaps a sibling course (shared AI-engineering vocabulary — agent, prompt, token, context, eval, guardrail, retrieval…), do a TARGETED, read-only lookup in the sibling ledger(s): if a decision exists and the sense matches, REUSE it verbatim and cite it — do not re-coin. If the sense genuinely differs, FLAG for a human — do not silently fork. Never edit a frozen sibling ledger (`rag.md`). Loading a whole sibling ledger as priming context is prohibited — that is the pollution this split prevents.

## Settled terms — Part I

Settled during the Part I canon bootstrap from the **de-jargoned** EN labels (the six academic coinages were
simplified per PART-1-BRIEF's Register ruling; community terms-of-art kept as-is). Slovak developer speech
**keeps more English than Russian** — kept-EN wins wherever the community says the English word; native forms
are decided from the EN meaning, never by literal translation, and pass the anti-bohemism gate (§1.3). Suspect
collocations were **web-verified** (a pair returning only Czech hits is a bohemism → rejected). **Grade
tokens (#800, NEW DECISION):** `MEASURED` / `REPORTED` / `ASSERTED` / `UNKNOWN` appear only in
`reading-the-evidence.md` and `glossary.md`, where the ladder is the subject (kept-EN, code-styled, gloss
„(namerané / hlásené / tvrdené)"). Everywhere else the grade is carried by the wording and recorded in
`editorial/evidence/ai-sdlc/`; `scripts/evidence-ledger-check.py` fails on a returning token. Palette
(vary it, never upgrade): measured — „štúdia zistila", „namerali"; reported — „podľa jeho/jej slov",
„opisuje z vlastnej praxe", „podľa správy"; asserted — „tvrdí", „ide o argument bez merania";
unknown — „nikto to nezmeral"; vendor — „podľa údajov samotného výrobcu".

### Intro

| EN term | EN gloss | SK decision |
|---|---|---|
| Verification bottleneck | the binding constraint: generation is cheap, checking is not; throughput is gated by verification capacity. | **native — „úzke miesto overovania"** (most *(verification bottleneck)* pri prvom výskyte). `overovanie` = verification (potvrdené SK, SDLC fáza). **Web-overené / BOHEMIZMUS ZACHYTENÝ:** „úzke hrdlo" vracia prevažne české zásahy (cs.wikipedia, anycoders.cz) — **odmietnuté** ako CZ-ťahnúce; „úzke miesto" je doložene slovenské (SK slovník vývoja softvéru). Malým v tele vety. |
| The loop closes on production | the feedback edge must return from live operation to planning; ending at internal QA is a pipeline, not a loop. | **native — veta „slučka sa uzatvára na produkcii"** (nie jednoslovný termín). `slučka` = loop (REUSE `rag.md`: slučka agenta = „slučka"; „okruh" ✗ zamietnuté). „produkcia". |
| Human router | the human's role above the loop: guardrail and judgment at named checkpoints, not a stage inside it. | **figúra „človek-smerovač" — ADOPT (owner), NA SKÚŠOBNEJ DOBE.** **Vždy sa uvádza pri prvom výskyte cez natívny HITL-termín** — kept-EN „human-in-the-loop" s glosom „(schválenie človekom / človek v rozhodovacom procese)" (REUSE `rag.md`; **NIKDY „človek v slučke"**), potom figúra **„človek-smerovač"** nesie obraz (zrkadlí RU «человек-маршрутизатор»; `smerovač` = router — repurpose siete na človeka je zámerná metafora). Na skúšobnej dobe — kontroluje sa studeným prechodom. **Odmietnuté:** „človek-rozcestník" (rozcestník = pasívna smerová tabuľa, nesmeruje). |
| Substrate → **Foundation** | Part I's subject: project memory, rules-as-code, artifacts-as-the-only-interface. | **native — „základ"** (de-jargón: substrate → foundation). **Odmietnuté:** „substrát" (nepriehľadná kalka); „základňa" ako alternatíva prípustná. |
| Tier lens | the SOLOIST/SMALL-TEAM/ENTERPRISE reading applied to every mechanism. | **native — „tri úrovne zrelosti"** (soloista · malý tím · enterprise); krátka forma „tri úrovne"; `úroveň` = tier. Most *(three maturity tiers)*. **Web-overené:** „úroveň/model zrelosti" je doložene slovenské (CMM „model zrelosti", Power Platform „model zrelosti prijatia") → „tri úrovne zrelosti" znie prirodzene po slovensky, nie česky. EN-label: "the three tiers" / "the three maturity tiers" (coinage „tier lens" zrušený, zmysel zachovaný). **Odmietnuté (owner):** „optika troch úrovní" (v RU un-Russian; SK zrkadlí plain); „šošovka úrovní" (mechanický prenos). |
| Proof-vs-capability | close to production a control is about what it *prevents*; far from it, about what you can *prove*. | **NIE termín — plain phrasing** (de-jargón; „gradient" zrušený). Poviem vetou: „bližšie k produkcii je kontrola o tom, čomu zabráni; ďalej o tom, čo vieš dokázať". Nezavádzať ako pomenovaný termín. |

### The verification bottleneck

| EN term | EN gloss | SK decision |
|---|---|---|
| Proxy metric | any measured stand-in for value (merged PRs, commits, LOC, time-on-task). | **hybrid — „proxy metrika"** (kept-EN `proxy` + „metrika"). **Odmietnuté:** „náhradná metrika" (dobré ako jednorazový glos, nie termín). |
| Denominator choice | "% of code written by AI" depends entirely on the denominator; same telemetry → 28.7% vs 70.6%. | **native — „voľba menovateľa"** (`menovateľ` = denominator, SK). Most netreba. |
| Benchmark-to-production gap | the collapse from offline benchmark score to real-SDLC applied rate (Meta 68%→19.7%). | **hybrid — „priepasť medzi benchmarkom a produkciou"**; `benchmark` kept-EN + SK skloňovanie (benchmarkom). |
| Self-assessment gap | developers cannot judge AI's effect on their own speed; error ~40pp, wrong even about the sign. | **native — „skreslenie sebahodnotenia"** (`sebahodnotenie` — SK). **Odmietnuté / BOHEMIZMUS:** „sebehodnocení" (CZ tvar). |
| Tech debt on credit | velocity gained early, paid back later as sustained complexity that drives the slowdown. | **native — „technický dlh na úver"** (de-jargón: complexity debt → tech debt on credit). „technický dlh" — štandard SK; „na úver" — doložene SK. |

### Reading the evidence

| EN term | EN gloss | SK decision |
|---|---|---|
| Evidence grade / the ladder | the `MEASURED` / `REPORTED` / `ASSERTED` classification; grades inherited, never upgraded. | **native — „stupeň dôkazu" / „rebrík dôkazov"** (`rebrík` = ladder, SK). Tokeny `MEASURED` / `REPORTED` / `ASSERTED` — **kept-EN, code-styled, invariant**, ale **iba** v lekcii o čítaní dôkazov a v glosári; inde stupeň nesie formulácia (#800). Jednorazový glos „(namerané / hlásené / tvrdené)". |
| Can't-be-checked | a claim whose weakness is that nobody can check it, distinct from tested-and-failed. | **NIE termín — plain „nedá sa overiť"** (de-jargón; „nefalzifikovateľné, nie vyvrátené" zrušené). **Odmietnuté:** „nefalzifikovateľné tvrdenie" (akademizmus). |
| Citation laundering | a distorted claim passed along until it looks sourced. | **Razená figúra sa NEMANDÁTUJE (owner: DROP).** Význam sa vyjadruje **priamo**: „skreslené tvrdenie, ktoré sa opakuje, kým nevyzerá ako odkaz na štúdiu". Rodený pisateľ smie použiť idióm, iba ak je naozaj prirodzený. **Odmietnuté ako mandát:** „vypranie pôvodu". |
| Evidence that cuts against whoever published it | a result that cuts against its publisher's incentive; the strongest evidence class in a COI-heavy field. | **NIE termín — vyjadriť PRIAMO (owner: právna kalka, un-Russian; bol to aj de-jargon miss v EN — rovnaké liečenie ako citation-laundering).** Myšlienka: výsledok je nevýhodný pre samotný zdroj, a práve to mu dodáva váhu — Anthropic AI predáva, no jeho autor zverejňuje jej hranicu, takže to bolo proti ich obchodnému záujmu. Hodnotí DÔKAZ, NIE je to chvála Anthropicu — vendor-neutral (žiadne „pripísať k dobru"). Príklad: „výsledok je nevýhodný pre samotný zdroj … bolo to proti ich obchodnému záujmu, a práve preto možno meraniu veriť viac". **Odmietnuté ako termín:** „zistenie proti vlastnému záujmu", „nález proti záujmu" (kalky finding). |
| Conflict of interest, stated inline | naming the conflict of interest (who's paying) as part of the finding, not a footnote. | **native — „konflikt záujmov, uvedený priamo"** (de-jargón z positionality); `konflikt záujmov` — štandard SK. **Odmietnuté:** „pozicionalita" (nepriehľadné). |

### Preparation over model

| EN term | EN gloss | SK decision |
|---|---|---|
| Preparation-over-model | setup/scope moves agent success more than model choice (dotnet/runtime 38.1%→69%). | **native — maxima „príprava je dôležitejšia než model"**. |
| The gate-not-the-agent misread | reading a low revert/failure number as agent quality when it's a property of the review gate. | **native — „zásluha kontroly, nie agenta"** — tu `gate` = **review gate** (Sense A: proces revízie PR pred zlúčením), teda **nie „brána"**, ale „(prísna) kontrola pri revízii". Pozri **kartu významov `gate`** nižšie. |
| Controllable scope | starting agent work where the problem is bounded, with a human approval gate at the requirements boundary. | **native — „zvládnuteľný rozsah (úlohy)"**. **Odmietnuté:** „kontrolovateľný skoup" (žargón-kalka). |
| Architecture-first (with a loop) | investing in design before code, while accepting even sound architecture needs iteration. | **native — „najprv architektúra (so slučkou)"**. |
| Harness staleness | every scaffold component encodes an assumption about model limits that expires as models improve. | **kept-EN — „zastarávanie harnessu"**; `harness` kept-EN + SK skloňovanie (harnessu; §3 kept-EN termíny berú SK koncovky). Glos „harness (obväzba/lešenie agenta)" pri prvom výskyte. **Odmietnuté:** holé „lešenie" ako termín. |

### Project memory & tiering

| EN term | EN gloss | SK decision |
|---|---|---|
| Project memory | durable, agent-readable knowledge that persists across runs; the fix for agent amnesia. | **native — „pamäť projektu"** (`pamäť` — SK; **BOHEMIZMUS-strážca:** nie „paměť"). |
| Amnesia | agents retain nothing between sessions except artifacts on disk. | **native — „amnézia"** (figúra „múdry priateľ s amnéziou"). |
| Context tax / "length is a subscription" | the MEASURED >20%-per-turn cost of standing context; every line is re-sent and billed. | **native — „priebežné náklady kontextu" / „stála réžia kontextu"** — **KRITICKÝ REUSE ZÁKAZU:** SK **NESMIE** použiť figúru „daň" (`rag.md` §1.4 blocklist: „stála daň ✗ → stála réžia / priebežné náklady — figúra „daň" vyradená"). Povinná plain-dvojica „každý riadok sa účtuje v každom kroku"; „dĺžka je predplatné". `context rot` — **kept-EN**. |
| Over-compliance | agents follow instructions "thoroughly but unnecessarily," burning cost without improving outcomes. | **native — „nadmerná poslušnosť"**. **Odmietnuté:** „nad-compliance" (žargón). |
| Scar archive | the reasoning behind each locked decision, appended after every fixed bug class. | **figúra „archív jaziev" — NA SKÚŠOBNEJ DOBE**, glos pri prvom výskyte + most k odvetviu „blameless postmortem". `jazva` = scar (SK). Potvrdí/vyškrtne najbližší studený prechod. |
| Knowledge tiering | organizing memory by rate-of-change / distance-from-focus so only the relevant tier loads. | **native — „vrstvenie znalostí"** (`vrstvenie` = layering); „rozvrstvenie znalostí" alternatíva. |
| Detail tiers (map / contract / blueprint) | the three-level tiering of an artifact by its relation to the current task. | **native — „úrovne detailu (mapa / kontrakt / nákres)"** (de-jargón: „LOD" zrušený). Vlastné značky DefinitiveSpec (LOD_0/1/2) sa citujú ako názov toho nástroja, nie ako termín kurzu. **Odmietnuté:** „LOD rebrík". |
| Hot set / cold set | the always-loaded one-screen non-negotiables vs the on-demand retrieved detail. | **kept-EN, term-of-art KEEP — „hot set / cold set"** + glos „(horúca/studená sada)" pri prvom výskyte (SK drží EN pre komunitný termín). |
| Load detail on demand | loading only name+description until the body is needed, then paging it in. | **native — „načítať detail na požiadanie"** (de-jargón z progressive disclosure). **Odmietnuté:** „progresívne odhaľovanie" (okrem jedného glosovaného výskytu). |
| Artifact overload | artifacts generated faster than human review or model context can absorb, with no lifecycle discipline. | **native — „zahltenie artefaktmi"**; `artefakt` — SK. |

### Rules that hold

| EN term | EN gloss | SK decision |
|---|---|---|
| Executable rule / rules-as-code | a constraint enforced by the harness or CI which the model cannot bypass. | **native — „vykonateľné pravidlo" / „pravidlá ako kód"**. **BOHEMIZMUS-strážca:** „vykonatelné" (CZ) ✗. |
| "An instruction is not a control" | a rule stated in natural language is a suggestion, not an enforced boundary. | **native — maxima „pokyn nie je kontrola" / „pokyn nie je zábrana"** (úvodzovky/kurzíva podľa §8). |
| Hook vs skill | a hook is deterministic harness enforcement; a skill is model judgment it may ignore. | **kept-EN — „hook verzus skill"** (REUSE `rag.md`: hooks/callbacks v kept-EN registri). Glos „hook (deterministický zásah harnessu) verzus skill (rada, ktorú model môže ignorovať)". |
| The gate defines the artifact | an agent optimises exactly what you check; anything unchecked does not exist. | **native — maxima „brána určuje výsledok" / „čo kontroluješ, to dostaneš"**; `brána` — REUSE. |
| Reward hacking / gaming the gate | satisfying the checked metric without doing the requested work. | **kept-EN — „reward hacking"** (community term-of-art, KEEP) + glos „(hranie na metriku odmeny: prejsť kontrolou bez vykonania práce)". **Odmietnuté:** „hackovanie odmeny" (doslovná kalka). |
| Blast radius | the scope of damage a confused or compromised agent can reach. | **kept-EN — „blast radius"** (term-of-art, KEEP) + glos „(rozsah škôd)". **Web-overené:** natívne „polomer zásahu" v SK IT nemá doklad (vracia len bleskozvody/fyziku) → kept-EN je správne. |
| Policy-as-code | enforced-in-the-pipeline, audited rules (the enterprise form of executable rules). | **kept-EN — „policy-as-code"** (term-of-art, KEEP) + glos „(politiky ako kód)". |
| Least privilege | the agent can reach exactly the resources its task needs and no more. | **REUSE — „princíp najnižších oprávnení (least privilege)"** (`rag.md` §1.2/Fáza 4/6 — vlastnícke rozhodnutie „najnižších", nie „najmenších"; **NEOTVÁRAŤ**). |
| Drift / rule rot | the decay of a rule corpus without a staleness mechanism. | **Tri RÔZNE významy — pozri „Kartu významov: drift pravidiel" nižšie (owner).** Skrátene: „drift kontextu" (context drift) · „drift pravidiel" (pravidlá sú tie isté, drift má ich VÝKLAD kvôli context rot) · „zastarávanie pravidiel" (pravidlá ZASTARALI a treba ich zmeniť kvôli novým faktom/prístupom). Pisateľ volí podľa významu. REUSE kept-EN „drift" — `rag.md` (SK register drží „drift" kept-EN); RAG-význam (drift vstupu/modelu) je samostatný, štvrtý. |
| Consistency owner | the role accountable for reconciling a rule corpus so two files can't prescribe opposite things. | **native — „vlastník konzistencie" / „zodpovedný za konzistenciu"** (`vlastník` — SK, používa `rag.md`). |

## Karta významov: drift pravidiel (owner ruling — tri rôzne významy)

Formulácia vlastníka **doslovne** (owner ruling je v RU; SK zrkadlí významy natívne), aby pisateľ volil termín
podľa významu, nie podľa slova:

> - **„drift kontextu"** — context drift (OK as-is).
> - **„drift pravidiel"** — the rules stay the SAME but their INTERPRETATION drifts due to context rot.
> - **„zastarávanie pravidiel"** — the rules become OBSOLETE and should be CHANGED due to new facts / approaches / practices.
> These are DIFFERENT senses (interpretation-drift vs obsolescence).

Použitie v kurze:
- Lekcia 5, „hnitie pravidiel kvôli context rot" (pravidlá sa nemenili, ale model ich vykladá inak) → **„drift pravidiel"**.
- Lekcia 5, „pravidlá treba aktualizovať pre nové fakty/prístupy" → **„zastarávanie pravidiel"**.
- „drift kontextu" — samostatný význam (okno/história driftuje), nemiešať s dvoma vyššie.
- Štvrtý, RAG-význam „drift" (drift vstupu/korpusu/modelu, `rag.md`) — tiež samostatný; nezlievať s korpusom pravidiel.
- **Web-overené:** „zastarávanie" je slovenský tvar (doklad „Zastarávanie kódu"); CZ „zastarávání" ✗ odmietnuté.

## Karta významov: `gate` (owner ruling — kánon preberaj podľa VÝZNAMU, nie podľa anglického slova)

`gate` v angličtine pokrýva rôzne pojmy. Nedá sa kalkovať jedným slovom „brána": záznam kánonu nesie **významový kontext ako v tezaure** a RAG-kánon sa preberá, iba ak sa **význam zhoduje** (peek-don't-load „reuse only if the sense matches").

- **Sense A — review gate** — proces revízie PR pred zlúčením (kontext `dotnet/runtime`, Lekcia 3). → **nie „brána"**, ale opisne: „(prísna) kontrola pri revízii", „kontrola zmien pred zlúčením". Maxima misread: „zásluha kontroly, nie agenta".
- **Sense B — verification / pipeline gate** — štrukturálny kontrolný bod, ktorý blokuje postup a zachytáva triedy chýb (Intro; Lekcia 1 „automatická brána (build/testy)"; Časť III „viacúrovňové brány", escape ledger). → **„brána"** (ustálený obraz). Pri písaní Časti III zvážiť „brána" vs komunitný „gate".
- **Sense C — requirements sign-off / stage-gate** — schválenie požiadaviek človekom pred nákladnou realizáciou. → „schválenie požiadaviek" / kept-EN „stage-gate"; nie „brána".

## Vlastníkom rozhodnuté sporné termíny (denník)

- **Human router — ADOPT.** Figúra „človek-smerovač" prijatá (na skúšobnej dobe), s povinným uvedením cez
  human-in-the-loop pri prvom výskyte. Pozri riadok Intro.
- **Citation laundering — DROP.** Razená figúra zrušená; význam sa vyjadruje priamo. Pozri riadok „Reading the evidence".
- **Tier lens → „tri úrovne zrelosti" (owner).** „optika troch úrovní" zrušená; krátka forma „tri úrovne". Web-overené ako prirodzené SK (model/úroveň zrelosti). EN vyrovnaný na "the three tiers / three maturity tiers"; RU — «три уровня зрелости». Riadky Intro aj nadpis úrovní v Lekcii 1 aktualizované.
- **Against-interest finding — DROP termínu (owner).** Právna kalka zrušená vo všetkých troch jazykoch; význam sa vyjadruje priamo a vendor-neutral (hodnotí dôkaz, nie chvála Anthropicu). Pozri riadok „Reading the evidence".
- **Intro disclaimer „not a boast" — DROP v RU/SK (owner, 2026-07-20), ZÁMERNÉ rozídenie s EN.** EN veta z „Why a
  loop, not a pipeline": „It is worth flagging as a correction, not a boast". V EN znie prirodzene; v RU/SK nie:
  plochý technický register nerobí silné tvrdenia, ktoré by bolo treba dementovať, a samotná zmienka o
  „chvastaní" *znie* ako chvastanie. Rozhodnutie vlastníka: disclaimer NEPREKLADAŤ, ale vypustiť — obe vety sa
  zvinú do „Kurz sa tento nedostatok snaží napraviť" / «Курс старается исправить этот недостаток». EN si „not a
  boast" zámerne ponecháva. **Pri RE-RENDERI intra disclaimer NEVRACAJ** — je to stance-veta, nie fakt (pozri
  pravidlo „stance vs information"). Tiež „Väčšina/Most" → „Mnohé/Многие" (owner). PR #203.
- **observability — REUSE RAG-kánon, sense-scoped (owner 2026-07-20).** Koncept/termín = **„pozorovateľnosť" /
  kept-EN „observability"** (ako v `rag.md`; RU zrkadlí «наблюдаемость»/«observability»). **„monitoring" IBA pre
  bežný zmysel** „sledovať produkciu / dashboardy", NIE ako názov konceptu. Dôvod: (1) konzistencia s RAG kurzom
  na tom istom webe; (2) zachovať rozdiel monitoring (známe signály/dashboardy, known-unknowns) vs observability
  (vlastnosť — klásť ľubovoľné otázky, unknown-unknowns), na ktorom stojí kľúčový insight lekcie OPERATE
  („nefunkčný systém nevytvára žiadne dáta"). SK OPS-blok mermaid v intre je už „pozorovanie" (akt) — správne,
  nemení sa. (RU-strana: OPS-blok „прод + наблюдаемость" → „прод + мониторинг", lebo tam je EN sloveso "observe".)


## Pilot Intro+L1 — rozhodnutia tohto behu (2026-07-16)

- **Separation of duties — „oddelenie právomocí"** (native; most *(separation of duties)* pri prvom výskyte). Podnikový princíp nezávislej revízie „kritik nie je autor" na enterprise úrovni Lekcie 1. Zrkadlí RU «разделение обязанностей». (Alternatíva „oddelenie zodpovedností" prípustná; „segregácia povinností" odmietnutá ako kalka.)
- **Priemyselné štandardy (enterprise):** pevné názvy/veľké písmená — „SLSA Source L4 „Two-Party Review"" (OpenSSF), „DORA RTS, čl. 17" (EU 2024/1774, nezávislosť schvaľujúcej a vykonávajúcej funkcie). Stupeň: `MEASURED` pre výskum schvaľovania zmien + nariadené regulátorom.
- **Figúry — verdikt:** „chrbtica práce" (spine) — POTVRDENÁ (natívny idióm, dekóduje pri prvom kontakte). „niť, nie etapa" — PONECHANÁ NA SKÚŠOBNEJ DOBE (dekóduje, ale opiera sa o následný obraz tkania; najbližší milestone potvrdí/vyškrtne). „technický dlh na úver" — POTVRDENÁ.
- **blast radius:** stránky používajú natívne „miesto škody (blast radius)"; ledger drží kept-EN „blast radius (rozsah škôd)" ako kotvu — SPORNÉ, ponechané na rozhodnutie vlastníka (naivný čitateľ „miesto škody" dekóduje bezchybne).

## Issues #792/#793 — critic diversity and seams (2026-10-20) — NEW DECISIONS, PROBATION

| EN term | sense | SK decision + bridge + rejected variants |
|---|---|---|
| correlated error | Models tend to make the same mistakes, including across families; added coverage means errors only the second reviewer catches. | **NEW DECISION, PROBATION — „korelované chyby“**; prvý definujúci výskyt v lekcii: „korelované chyby (correlated errors)“. Množné číslo pomenúva opakujúcu sa zhodu chýb. Pôvodný most „(correlated error)“ odmietnutý pre nezhodu čísla so slovenským termínom. Odmietnuté „závislé chyby“: zamieňa koreláciu s neurčitou závislosťou. |
| critic lens | The reviewer's stated question plus the inputs needed to answer it, deliberately chosen to elicit different findings. | **NEW DECISION, PROBATION — „uhol pohľadu kritika“**; most „(critic lens)“. Otázka aj potrebné vstupy sú povinnou súčasťou definície. Odmietnuté „šošovka kritika“ (doslovný obraz) a „optika kritika“ (menej priame než bežné slovenské pomenovanie; iný koncept „tier lens“ už kánon rieši bez „optiky“). |
| seam | A junction between decomposed work units where modules, contracts, data or user scenarios must agree. | **NEW DECISION, PROBATION — „styčné miesto“**; most „(seam)“. Odmietnuté samostatné „styk“ (bez kontextu mnohoznačné), „spoj“ (evokuje hotové fyzické spojenie), „rozhranie“ (zužuje význam na interface) a „šev“ (textilná metafora). Cielený náhľad do `rag.md`: záznamy „seam“ pri grafe a odovzdávaní telemetrie majú iný kontext; tu ide o vzťah jednotiek dekompozície. |
| consumer-driven contract test | Consumer expectations become checks run on every provider build, blocking a breaking change before shipment. | **NEW DECISION, PROBATION — „kontraktový test riadený konzumentom“**; most „(consumer-driven contract test)“ pri prvom výskyte v lekcii. „Konzument“ označuje službu využívajúcu kontrakt poskytovateľa. Odmietnuté „spotrebiteľský test“: môže znamenať test produktu pre spotrebiteľov a stráca väzbu na kontrakt. |
| characterization (golden) test | Records existing observed behaviour as a baseline, without asserting its correctness; a person accepts or rejects later changes. | **NEW DECISION, PROBATION — „charakterizačný test“**; prvý most „(characterization test, golden master)“ s odkazom na Wikipediu už na slovenskom termíne. Pôvodný tvar „charakterizačný (golden) test“ s ďalším mostom „(characterization test / golden master)“ odmietnutý: dve zátvorky za sebou trieštia prvé uvedenie pojmu. `Golden master` zostáva kept-English v moste; nejde o `golden set` („etalónová sada“) z `rag.md`, ale o test správania existujúceho kódu. Odmietnuté „zlatý test“: nejasné hodnotenie kvality testu namiesto pomenovania metódy. |
| the four defences against regression | Documentation, a directive protecting working code and contracts, role separation and tests, attributed to the practitioner; the course classifies their mechanisms. | **NEW DECISION, PROBATION — „štyri obrany proti regresii“**. Anglický most netreba: opisný názov sa hneď rozvedie na štyri položky. „Regresia“ nadväzuje na zavedené „regresné hodnotenie“ / „regresia kvality“ v `rag.md`, tu konkrétne porušenie predtým funkčného správania. Odmietnuté „štyri regresné obrany“: nejasná väzba prídavného mena. |

Oprava po recenzii, round 1: nové heslá glosára majú veľké začiatočné písmeno; položky riadka „Nové pojmy“ zostávajú malé, inak sú totožné. Pre kontrolórov používaj „kontrolóri založení na LLM“, nie „modeloví kontrolóri“: „modelový“ môže znamenať vzorový. „Styčné miesto“ zachovaj aj v zhrnutí, nie holé „styk“. Pri štyroch obranách výslovne uveď „nezávislé oddelenie rolí“.

Spresnenie po druhom redakčnom kole: všetkých šesť nových hesiel glosára začína veľkým písmenom; položky „Nové pojmy“ sú totožné po prevode na malé písmená. Čiarka do hesla ani položky nepatrí: rozdelila by jeden pojem na viac položiek. Heslá s malým začiatočným písmenom a položky s veľkým sú odmietnuté pre nesúlad s úpravou glosára a zoznamov. Prvý výskyt na každej stránke a v hesle o štyroch obranách je „Andrej Beloborodov“; samotné „Beloborodov“ pri prvom výskyte je odmietnuté. Titul pred menom („praktik Andrej Beloborodov“ za EN „Practitioner Andrey Beloborodov“) je odmietnutý ako kalka: zdroj sa uvádza celým menom. Tam, kde EN uvádza prístavok („Andrey Beloborodov, a practitioner who…“), SK ho zachováva ako „Andrej Beloborodov, praktik, ktorý…“ alebo vzťažnou vetou s rovnakým významom (pozri Issue #798 a #799). „Charakterizačné (golden) porovnanie“ v lekcii o bránach označuje porovnanie správania pri refaktoringu, nie nový pojem; holé „golden porovnanie“ je odmietnuté pre slabšiu väzbu na „charakterizačný test“. Percentá sa podľa `_language.md` píšu bez medzery („60%“); „60 %“ je odmietnuté pre rozpor s projektovou konvenciou. Register zostáva „ty“ aj v celom bode pre malý tím: „Dohodni si … urč … pridaj“; „Dohodnite … určte … pridajte“ je odmietnuté ako vykanie.

## Issues #794/#795 — observability, rollout and document status (2026-10-20) — NEW DECISIONS, PROBATION

| EN term | sense | SK decision + bridge + rejected variants |
|---|---|---|
| telemetry done-condition | The telemetry signal set, including the business signal, belongs in the task's done-condition; the critic checks that the system emits it. | **NEW DECISION, PROBATION — „telemetria ako podmienka dokončenia“**. Bez mosta: obe slová sú už v kánone. |
| black-box probe | A scheduled check that walks a user journey from outside the service network. | **NEW DECISION, PROBATION — „syntetická sonda zvonku (black-box probe)“**; v próze ďalej „sonda“. SRE pojem „black-box monitoring (monitoring zvonku)“ sa pripisuje knihe SRE, rovnako ako white-box. |
| heartbeat | A periodic signal from an inner component; separate liveness check, not proof that the journey works. | **NEW DECISION, PROBATION — „heartbeat (pravidelný signál života)“**, kontrola „živosti (liveness)“. „Životnosť“ odmietnutá: znamená trvanlivosť. Samostatné heslo glosára nemá. |
| symptom-based alerting | Page a person on symptoms that hurt users now or are about to and that need human judgement. | **NEW DECISION, PROBATION — „alerting na príznaky (symptom-based alerting)“**; page = „alert na privolanie človeka (page)“. |
| shadow verification (shadow run) | The candidate path runs on real inputs beside the control path, outputs are compared, users keep the control result; side effects are off. | **NEW DECISION, PROBATION — „tieňové overovanie (shadow run)“**, jednotne aj v próze. „Tieňový beh“ odmietnutý ako druhý názov pre to isté. |
| artefact promotion (build once) | Build once, promote the same artefact identified by digest through staging to production; keep the previous one for rollback. | **NEW DECISION, PROBATION — „posun artefaktu medzi prostrediami (build once)“**. „Presun“ odmietnutý: konzistentne „posun“. |
| user report (sensor of last resort) | A logged user report; a confirmed defect goes into the escape ledger, a report that beat every alert reveals a missing signal. | **NEW DECISION, PROBATION — „hlásenie od používateľa (posledná poistka pri odhaľovaní zlyhaní)“**. „Snímač poslednej záchrany“ odmietnutý ako kalk. Hlásenie chýbajúci signál *odhaľuje*: opis, nie pokyn. |
| document status (as-is / target / experiment / superseded) | A first-line marker: the document describes the working system, an intended state, an experiment, or history. | **NEW DECISION, PROBATION — „stav dokumentu (súčasný stav / cieľový stav / experiment / nahradené)“**. „Nahradené“ zodpovedá SETTLED „nahradené rozhodnutie“. |
| flag debt | The upkeep cost of a flag and the code branches it keeps alive. | **NEW DECISION, PROBATION — „dlh z flagov (flag debt)“**. |
| release flag / kill-switch flag | Release flag: owner, description and removal date. Long-lived kill-switch flag: owner and periodic review, no expiry. | **NEW DECISION, PROBATION — „flag na sprístupnenie (release flag)“, „flag núdzového vypínača“**. Glosy „(ops toggle)“, „(deploy grant)“ a „flag na sprístupnenie je krátkodobý“ odmietnuté: anglický text ich nemá. |

Požiadavka „vlastník“ patrí kurzu, nie Beloborodovovi: ten uvádza opis a dátum odstránenia. Prvá zmienka na stránke: „Andrej Beloborodov“. Bez autorského „my“; závery kurzu sú označené ako závery kurzu.

## Issue #798 — architecture erosion (2026-10-20) — NEW DECISIONS, PROBATION

| EN term | sense | SK decision + bridge + rejected variant |
|---|---|---|
| architecture erosion / architectural drift | Perry and Wolf's two terms (1992) for the decay of code structure: erosion violates the architecture, drift is insensitivity to it. Not the rule-corpus drift of the drift-and-rot lesson. | **NEW DECISION, PROBATION — „erózia architektúry / architektonický drift“**; most „(architecture erosion / architectural drift)“. Lekcia výslovne odlišuje tento drift od driftu a zastarávania pravidiel. |
| decision before change | Record the architectural decision first, change the system second; a fix that must break an accepted decision becomes a proposal for a new one. | **NEW DECISION, PROBATION — „rozhodnutie pred zmenou“**. |
| ADR log | The in-repo log of ADRs (Nygard's format), consulted on every task brief and every bug fix. | **NEW DECISION, PROBATION — „denník architektonických rozhodnutí“**; most „(ADR log)“ v glosári aj pri prvom výskyte v texte. Odmietnuté „register ADR“ (evokuje úradnú evidenciu). |
| superseded ADR | A record of a decision replaced by a later one, kept with status `superseded` and a pointer to its replacement. | **NEW DECISION, PROBATION — „nahradený záznam ADR“**; most „(superseded ADR)“. „Nahradené rozhodnutie (superseded decision)“ sa v tejto lekcii nepoužíva: je to heslo sekcie o drifte a iný pojem (rozhodnutie v pamäti projektu, nie záznam denníka ADR). |
| fitness function | An objective integrity assessment of an architectural characteristic (Ford, Parsons, Kua). | **NEW DECISION, PROBATION — „fitness funkcia“** (kept-EN prvý člen, bez spojovníka). Zvolený tvar rozpoznateľný podľa anglického termínu; „funkcia vhodnosti“ sa podľa úzu neoverovala — preveriť pri ukončení PROBATION. |
| dependency rule / import contract | An executable statement of which modules may depend on which, checked in the build; the rule is the subject, the tools are examples. | **NEW DECISION, PROBATION — „pravidlo závislostí / kontrakt importov“**. „Vykonateľné“ ostáva podľa riadku Executable rule. |
| frozen violations | Violations stored on a rule's first run (`FreezingArchRule`); new ones fail, old ones are removed as planned work, so the list only shrinks. | **NEW DECISION, PROBATION — „zmrazené porušenia“**. Ratchet sa opisuje („jednosmerné sprísňovanie“), nie prekladá. |
| duplication gate | A check that fails the build when duplication exceeds a set threshold (`jscpd --threshold`). | **NEW DECISION, PROBATION — „kontrola duplicít“**. Odmietnutá „brána duplicít“ (kalk gate). |
| fix-on-fix rate | The share of fixes that repair the result of an earlier fix in the same area. | **NEW DECISION, PROBATION — „podiel opakovaných opráv“**. Odmietnuté „miera opráv opráv“ (zhluk genitívov). |
| redesign trigger | An agreed-in-advance threshold (Beloborodov: three consecutive fixes on fixes) that starts an audit and redesign; nobody has measured the right threshold. | **NEW DECISION, PROBATION — „spúšťač prepracovania návrhu“**. Odmietnutý „trigger redizajnu“ (redizajn = vizuálny dizajn). |
| redesign vs rewrite | Redesign: debt audit, target architecture, staged move with working results. Rewrite: the open brief "rewrite it all properly". | **NEW DECISION, PROBATION — „prepracovanie návrhu verzus prepis“**; bez čiarky, jedna položka „Nové pojmy“. |

Heslá glosára začínajú veľkým písmenom; položky „Nové pojmy“ sú s nimi totožné po zmene prvého písmena na malé. Prvá zmienka: „Andrej Beloborodov, praktik, ktorý…“, ďalej „Beloborodov“ alebo zámeno. Rozsahy percent „22–33%“. „Niekoľkonásobne“ bez čísla. Opakovaný reťazec „*Akému zlyhaniu to predchádza:*“ sa nemení.

## Issue #797 — existing codebase (2026-10-20) — NEW DECISIONS, PROBATION

| EN term | sense | SK decision + bridge + rejected variants |
|---|---|---|
| existing codebase (brownfield) | Already running code, often partly agent-written, knowledge scattered across chats, wikis and heads; the loop is installed around it, not before it. | **NEW DECISION, PROBATION — „existujúca kódová základňa“**; most „(brownfield)“ pri prvom definujúcom výskyte. Odmietnuté „existujúci projekt“ ako heslo (v próze prípustné) a „legacy“ ako termín (hodnotí kód ako zlý). |
| audit before refactor | Before changing anything: what works, what blocks development, what is risky, what to do, how to check; never the brief "rewrite it all properly". | **NEW DECISION, PROBATION — „audit pred refaktoringom“**. Citované zadanie je „prepíš všetko poriadne“, rovnako ako v lekcii o erózii architektúry (#798); tá istá rada Beloborodova má v kurze znieť rovnako. Odmietnuté „refaktorizácia“ (český sklon). |
| independent multi-model audit | Same fixed areas, several independent models; divergent verdicts read as different things checked, not averaged. | **NEW DECISION, PROBATION — „nezávislý audit viacerými modelmi“**. Odmietnuté „multimodelový audit“ (znie ako multimodálny) a „Rozdielne verdikty znamenajú…“ (tvrdenie namiesto čítania). Sloveso „nepriemeruj“, nie „nespriemerúvaj“. |
| audit dimensions (13) | The unchanged checklist areas. | **NEW DECISION, PROBATION — „13 oblastí auditu“**; opakovaný audit „opakovaný audit v rovnakých oblastiach“. Odmietnuté „dimenzie“ (kalk). |
| verification pack | Checks known to actually work, each with a known pass meaning, plus a basic CI gate for new work. | **NEW DECISION, PROBATION — „overovacia sada“**; most „(verification pack)“ v lekcii. Odmietnuté „verifikačný balík“ (kalk z package). |
| single source of truth (rebuilt from the code) | Project documentation next to the code, reconciled with the implementation, split into history, target state and experiments. | **NEW DECISION, PROBATION — heslo „Jediný zdroj pravdy (obnovený z kódu)“**; v próze „jediný zdroj pravdy (single source of truth)“ s jedinou zátvorkou — dve zátvorky za sebou sú odmietnuté z rovnakého dôvodu ako pri charakterizačnom teste. |
| the new-chat test | A fresh agent without chat history asked about last week's architecture decisions; no answer from the repo = memory still lives in old chats. | **NEW DECISION, PROBATION — „test nového chatu“**. Odmietnuté „test čerstvého rozhovoru“. |
| characterization test | — | **REUSE (#792/#793) — „charakterizačný test“**; most na tejto stránke „(characterization test)“ bez golden master, ako v EN. |
| light loop | task → acceptance criteria → implementation → independent critique → check → result. | **NEW DECISION, PROBATION — „odľahčená slučka“**. Odmietnuté „ľahká slučka“ (= jednoduchá). |
| roll-forward | Fixing by deploying forward instead of reverting. | **NEW DECISION, PROBATION — „nasadenie opravy namiesto vrátenia (roll-forward)“**. Odmietnuté „rolovanie vpred“. |
| baseline | Before/after measure on a named proxy metric with a stated denominator. | **NEW DECISION, PROBATION — „východiskové meranie (baseline)“**, nie tučne (nie je heslo tejto lekcie). Odmietnuté „základná čiara“ (kalk). |
| bounded change class | A change type with a mechanical done-condition (e.g. a migration). | **NEW DECISION, PROBATION — „presne vymedzený typ zmien“**. Pôvodný kandidát „ohraničená trieda zmien“ odmietnutý ako ťažký kalk. |
| experience report | The genre of the Google report, not a research study. | **NEW DECISION, PROBATION — „správa o skúsenostiach (experience report), nie výskumná štúdia“**. |

Opakujúce sa reťazce: označenie zlyhania je `*Akému zlyhaniu to predchádza:*` (39 výskytov v korpuse, väčšinový tvar) a záverečný nadpis `## Čo si odniesť` (21 : 7); tvary „Zlyhanie, ktorému to predchádza:“ a „Čo si z toho odniesť“ sú v tejto lekcii odmietnuté. Meno: „Andrej Beloborodov“ pri prvom výskyte, ďalej skloňované priezvisko. H1 bez koncovej bodky (markdownlint MD026): „Kód už máš, slučku ešte nie“.

## Issue #799 — the model is a dependency (2026-10-20) — NEW DECISIONS, PROBATION

| EN term | sense | SK decision + bridge + rejected variant |
|---|---|---|
| model snapshot vs moving alias | A snapshot is a fixed version; an alias points at a version the supplier may replace. The ID format does not tell which. | **NEW DECISION, PROBATION — „snapshot modelu verzus pohyblivý alias“**. |
| model pinning | Choosing a snapshot in config and recording its ID on each agent change. | **NEW DECISION, PROBATION — „pripnutie modelu (model pinning)“**. |
| re-qualification | Checking a candidate before a staged rollout: repeated regression cases, unchanged judge, first-pass success. | **NEW DECISION, PROBATION — „opätovné preverenie (re-qualification)“**. |
| item-level regression | A previously passing case fails consistently beyond run-to-run variance; a higher average can hide it. | **NEW DECISION, PROBATION — „regresia v jednotlivých prípadoch (item-level regression)“**. |
| deprecation notice period | Time from announcement to retirement for qualifying and migrating. | **NEW DECISION, PROBATION — „lehota pred vyradením (deprecation notice period)“**. retirement — „vyradenie“; deprecation pages — „vyradenia modelov“; deprecated ID — „identifikátora určeného na vyradenie“, „endpointy určené na vyradenie“. Odmietnuté „vyradzovať“: nie je slovenský tvar (bohemizmus podľa *vyřazovat*); nedokonavý vid je „vyraďovať“. |
| auto-upgrade | The platform replaces the deployed version itself. | **NEW DECISION, PROBATION — „automatický upgrade (auto-upgrade)“**. |
| tested exit / fallback provider | Another supplier or a self-hosted model behind the same client, run on a schedule against the regression set. | **NEW DECISION, PROBATION — „vyskúšaná možnosť odchodu / záložný poskytovateľ“**; v texte „Vyskúšaná možnosť odchodu (tested exit)“. Supplier je všade „poskytovateľ“; „dodávateľ“ len v hesle vendor-portable memory. |
| vendor-portable memory | Rules, decisions and briefs in repository files, not in chat history. | **NEW DECISION, PROBATION — „pamäť nezávislá od dodávateľa (vendor-portable memory)“**. |
| data terms | Dated terms of one supplier and tier: training, retention, residency, personal data. | **NEW DECISION, PROBATION — „podmienky nakladania s dátami“**; heslo je bez zoznamu v zátvorke (v hesle nie je čiarka ani „ · “); v texte most „(data terms)“. tier — „plán predplatného“; odmietnuté „verzia (predplatného / služby)“: na stránke o verziách modelov falošný priateľ. Paid — „platené služby“. |
| routing by break-even | Assigning a model to a task class by first-pass success and the price inequality. | **NEW DECISION, PROBATION — „smerovanie podľa hranice rentability (routing by break-even)“**. Nadpis sekcie „…podľa nákladov na prijatú zmenu“ (jednotka lekcie o nákladoch). |
| DPA / ZDR | Data processing addendum; zero retention by separate arrangement. | **NEW DECISION, PROBATION — „dodatok o spracúvaní osobných údajov (data processing addendum, DPA)“; „Zero data retention (ZDR), teda nulové uchovávanie dát“**, ďalej ZDR. „Dohodovať“ odmietnuté (bohemizmus) → „dojednáva“. |
| Modified Retention amendment | The supplier's amendment name. | **NEW DECISION, PROBATION — „dodatok Modified Retention“**; holá anglická fráza v slovenskej syntaxi odmietnutá. |
| data at rest | Stored data, as opposed to processing. | **NEW DECISION, PROBATION — „uložené dáta“**. |
| GA / preview | Model classes in published notice policies. | **NEW DECISION, PROBATION — „modely vo všeobecnej dostupnosti (GA)“, „predbežné verzie (preview)“**, ďalej „GA“, „preview“. Dve glosy „teda … teda“ v jednej vete odmietnuté. |
| suspension | The supplier suspends an account. | **NEW DECISION, PROBATION — „pozastavenie účtu“, „pozastavený účet“; „zablokované účty“** (v citácii praktika). |
| consumer vs commercial terms | Personal subscription terms vs business terms. | **NEW DECISION, PROBATION — „spotrebiteľské podmienky“; „obchodné podmienky“, „komerčné služby“**. |

Riadok zdrojov: „Zdroje (prečítané v októbri 2026): OpenAI [názov](url), bez dátumu; …“; dátumy v zdrojoch a tabuľkách ISO. Položky „Nové pojmy“ malým písmenom, oddelené „, “, bez čiarky vnútri, s bodkou na konci. Bez autorského „my“ (napr. „Pri rešerši pre tento kurz … sa nenašlo…“). From time to time = „občas“, nie „pravidelne“ (regularly).
