# RAG kánon — dodatok (živý)

`canon/sk/rag.md` je **zmrazený**. Všetky rozhodnutia RAG-kurzu prijaté **po** zmrazení žijú tu. Načítavaj
spolu s `_language.md` a `rag.md` (loading contract v `editorial/style-canon.md`).

Prvé naplnenie: dávka `part-1-rag/structured-knowledge` (#405/#406/#407), lokalizačná fáza, 2026-08-03.

## 1a. Termíny dávky `structured-knowledge` (2026-08) — statusy

Pravidlo „no self-blessing" (`style-canon.md`): termín vymyslený alebo prvýkrát zaťažený v tom istom prechode
vstupuje **NA SKÚŠOBNÚ DOBU** a nepatrí do žiadneho do-not-flag zoznamu. Skúšobnú dobu sníma **iný** prechod —
chladné čítanie čerstvým recenzentom alebo míľnikový prechod.

| Termín (EN) | Slovenské znenie | Odborový termín alebo coinage | Status |
|---|---|---|---|
| controlled vocabulary | riadený slovník | odborový (knihovníctvo, metadáta) | SETTLED |
| taxonomy | taxonómia | odborový | SETTLED |
| ontology | ontológia | odborový | SETTLED |
| knowledge graph | znalostný graf | odborový | SETTLED |
| graph extraction | extrakcia grafu | odborový | SETTLED |
| entity resolution | stotožňovanie entít | odborový (MDM, e-Government) | SETTLED |
| over-/under-merging | prílišné / nedostatočné zlučovanie | opisné | NA SKÚŠOBNEJ DOBE |
| extraction precision | presnosť extrakcie | odborový | SETTLED |
| semantic layer | sémantická vrstva | odborový (dbt / Cube / LookML) | SETTLED |
| metrics layer | vrstva metrík | odborový | SETTLED |
| semantic model | sémantický model | odborový | SETTLED |
| measure / dimension / entity | miera / dimenzia / entita | odborový (BI) | SETTLED |
| community report | správa o komunite | opisné | NA SKÚŠOBNEJ DOBE |
| community detection | detekcia komunít | odborový | SETTLED |
| shapes graph / data graph / validation report | graf tvarov / dátový graf / validačná správa | odborový (W3C SHACL) | SETTLED |
| context distillation | kontextová destilácia | odborový | SETTLED |
| correlated error | korelovaná chyba | odborový (štatistika) | SETTLED |

**Ponechané v angličtine** (§7 `_language.md` — pre tieto neexistuje ustálený slovenský tvar alebo je preklad
zavádzajúci): RDF, OWL 2, SHACL, SPARQL, GraphRAG, TextUnit, local / global / DRIFT / basic search, Meta API,
text-to-SQL, BIRD.

### 1a.1 Tri rozhodnutia s externým dôkazom, nie s intuíciou

Kánon žiada, aby nový alebo sporný termín stál na **externom zdroji**, nie na uchu modelu. Tri z vyššie
uvedených ho majú a ten dôkaz sa zapisuje sem, aby ho nikto nemusel hľadať znova:

- **`stotožňovanie entít`** (entity resolution) — §54a zákona o e-Governmente používa «stotožnenie údajov»;
  ÚGKK SR ten istý tvar; MDM článok ANASOFT-u píše doslova «deduplikácia, stotožňovanie a obohacovanie
  záznamov». Je to presne tá disciplína, ktorú anglická stránka pomenúva (record linkage / MDM), v odbornom
  registri a so zákonným ukotvením. **Pozor:** «rozlíšenie entít» je nesprávne — *rozlíšenie* môže v slovenčine
  znamenať pravý opak zlučovania, o ktoré tu ide.
- **`znalostný graf`** — používa ho repozitár slovenskej štátnej správy `slovak-egov/centralny-model-udajov`
  («RDF znalostný graf»).
- **`riadený slovník`** — doložené na slovenských knihovnícko-metadátových zdrojoch (InfoLib, euroekonom.sk).
  Český tvar je `řízený slovník`, takže slovenské znenie je zároveň správne z hľadiska antibohemizmovej brány.

## 2a. Krížne odkazy medzi kurzami — jeden tvar pre všetky lokality

**Pravidlo:** odkazuj holým `/ai-sdlc/part-3-verification/layered-gates`, **bez** prefixu lokality — rovnako
ako v anglickom zdroji.

`baseUrl` lokalizovanej zostavy **už obsahuje** segment lokality (`/ai-engineering-handbook/sk/`), takže
absolútna markdown-cesta sa sama zmení na `/ai-engineering-handbook/sk/ai-sdlc/…` a čitateľ zostáva v
slovenčine. Overené zostavením všetkých štyroch lokalít 2026-08-03: `href` vo vygenerovanom HTML je
`/ai-engineering-handbook/sk/ai-sdlc/part-3-verification/layered-gates` a cieľová trasa existuje.

:::danger[Tu sa už raz pomýlilo — nezopakuj to]

Prvý návrh tejto sekcie hovoril opak („daj `/sk/ai-sdlc/…`"). Je to **nesprávne** a **rozbíja to zostavu**:
`npm run build` spadne s `Docusaurus found broken links`, lebo cesta ukáže na neexistujúcu trasu. Chyba
vznikla ako vierohodná úvaha o tom, ako sa skladá `baseUrl`, poslala sa ďalej ako fakt a naraz sa dostala do
troch lokalít. **Pravidlo o odkazoch overuje zostava, nie úvaha** — jeden `npm run build` odpovie za minútu.

:::

## 9a. ✅ VYRIEŠENÉ 2026-08-08 — dedené defekty, ktoré lokalizačný prechod nemal právo opraviť

Oba našiel render dávky `structured-knowledge`; oba sú **staršie ako táto dávka** a sú prierezové, takže
nepatrili do lokalizačného PR. Zapísané, aby sa nestratili — **a presne preto sa aj vyriešili.**
Oba uzavreté v prechode #431/#432; **rozhodnutia žijú v `_language.md` §Typografia a §1.1**, nie tu. Táto
sekcia ostáva ako záznam nálezu.

**Čo prechod pridal k pôvodnému hláseniu — obe čísla boli podcenené:**

- **Vnorená úvodzovka nebola jediná obeť.** Oprava kánonu odhalila **20 živých ASCII zatváracích úvodzoviek**
  v už nasadenej slovenskej próze kurzu **AI-SDLC** (`glossary.md` 2×, `rules-that-hold.md` 18×) — otvorené
  správne cez `„` (U+201E), zatvorené cez ASCII `"` (U+0022). Kurz RAG bol čistý. Pravidlo teda nebolo len
  *neotestované* v kánone; v druhom kurze sa **rozišlo s korpusom** a nič to nemeralo. Doplnená brána
  `scripts/sk-typography-check.py` (v CI), aby sa to už nedalo zopakovať.
- **Rod `pipeline`: nie 6 proti 7, ale 18 proti 21.** Pôvodný počet videl len stránky, ktoré mal render pred
  sebou, a **kurz AI-SDLC nevidel vôbec**. *Počet, ktorý zozbieral jeden prechod, je vzorka, nie census.*
  Rozhodnutie (ženský rod, s dokladom z JÚĽŠ) je v `_language.md` §1.1.

Pôvodné znenie nálezu:

- **Znak vnorenej úvodzovky v `_language.md` §Typografia je poškodený.** Sekcia predpisuje `‚…'` so
  **zatváracím ASCII apostrofom (U+0027)**. To si protirečí s tou istou sekciou, ktorá `"…"` odmieta, a súbor
  sám dokumentuje, že časti boli znovu odvodené z recenzií s rozbitým kódovaním. Žiadna staršia stránka v
  `i18n/sk` vnorenú úvodzovku nepoužila, takže pravidlo nikdy nebolo vyskúšané — prvé stránky, ktoré ho
  vyskúšali, sú z tejto dávky a použili **‚…' (U+201A … U+2018)**, čo nezávislý recenzent potvrdil.
  *Riadok kánonu treba opraviť.* **Poučenie na zapamätanie: štýlové pravidlo, ktoré ešte nikto nepoužil, nie je
  ustálené — je neotestované, a prvá stránka, ktorá ho použije, je jeho test.**
- **Rod slova `pipeline` je v korpuse rozdvojený.** Mužský 6× (`statický`, `statického`, `funkčný`,
  `Štandardný`, `zabalil`), ženský 7× (`statická`×3, `pevná`, `pevnú`, `celou`, `Celá`) — vrátane nadpisu
  `## Celá pipeline` v `retrieval/index.md` proti `statický pipeline` v `part-1-rag/overview.md`. Nové stránky
  použili **mužský rod**, lebo sa viažu na `intro.md` a `part-1-rag/overview.md`. Zjednotenie korpusu je práca
  pre consistency-editora, nie pre render lokality.

## 1b. Dávka `part-2-agents/orchestration-frameworks` — oprava faktu o prerušení (lokalizácia, 2026-08-07)

Prechod zosynchronizoval do ru/sk/de opravu: prerušený uzol LangGraphu **nepokračuje** tam, kde sa zastavil,
ale vykoná sa nanovo od prvého riadka. V tom istom prechode sme vlastnú nálepku krížového odkazu **zaviedli aj
stiahli** — druhý riadok tabuľky je tu práve preto, aby sa stiahnutý tvar nevrátil.

| Termín (EN) | Slovenské znenie | Status |
|---|---|---|
| `idempotency-key discipline` — nálepka krížového odkazu na `../tool-use/deep-dive.md` | **zásada kľúča idempotencie** | SETTLED. Zložené z inkumbenta `rag.md` §1 „kľúč idempotencie (idempotency key)". Hlavové podstatné meno **`zásada`** je korpusové: `multi-agent/index.md` prekladá tú istú anglickú konštrukciu ako „zásada z používania nástrojov". ⛔ **`disciplína`** — v korpuse vyhradená pre *odbor* („hodnotiaca disciplína", „disciplína návrhu"); samostatne sa číta ako sebadisciplína |
| ~~`at-most-once discipline`~~ — „zásada vykonania operácie najviac raz", potom „zásada „účinok nanajvýš raz"" | **OBE STIAHNUTÉ 2026-08-07** | Dôvod **nie je štylistický, ale adresný: nálepka pomenovala pojem, ktorý cieľová stránka nepoužíva.** `../tool-use/deep-dive.md` učí **idempotenciu** a **kľúč idempotencie**; reťazec „at-most-once" sa na nej nevyskytuje v žiadnej lokalite. Náhrada — riadok vyššie. Tým padla aj otvorená otázka `najviac` / `nanajvýš`: slovo je zo stránky preč |

**Pravidlo, kvôli ktorému je druhý riadok zapísaný.** Nálepka krížového odkazu sa stavia z **termínu, ktorý na
cieľovej stránke doslova stojí**. Poradie výberu ostáva: inkumbent (register §1, cieľová stránka, glosár) — a
až keď inkumbent neexistuje, nový tvar. Pre cudzí pojem nerazí nový termín.
