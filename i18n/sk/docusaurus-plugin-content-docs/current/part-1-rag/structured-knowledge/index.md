---
title: Štruktúrované znalosti
slug: /part-1-rag/structured-knowledge/
---

# Keď odpoveď nie je v žiadnom úryvku

Časť I doteraz na každej stránke mlčky predpokladala jedno: že znalosti prichádzajú ako **súvislý text**.
Rozparsuj dokumenty, rozdeľ ich na chunky (kúsky), chunky zaembedduj, vyhľadaj, preusporiadaj, vygeneruj. Celá pipeline je postavená na jednej stávke: že niekde v korpuse leží úryvok, ktorý po nájdení obsahuje odpoveď.

Pri veľkej časti podnikových znalostí tá stávka vychádza — preto je táto pipeline predvoľbou a preto si
zaslúžil tri lekcie. Lámu ho však tri celkom bežné otázky a každá inak:

- *„Aké riziká sa opakujú v našich desiatich tisícoch zmlúv?“* — takú odpoveď neobsahuje žiadny chunk.
  Neschováva sa v úryvku, ktorý si nevyhľadal; nikto ju nikdy nenapísal.
- *„Koľko tržieb spravil podnikový segment minulý kvartál?“* — ani toto číslo nikto nenapísal. Treba ho
  vypočítať, a to z definície „tržieb“, na ktorej sa dve oddelenia nemusia zhodnúť.
- *„Všetko, čo vieme o tomto dodávateľovi“* — dodávateľ vystupuje v šiestich rôznych zápisoch v štyroch
  systémoch a žiadny reranking z tých šiestich vecí neurobí jednu.

Odpoveď na každú z nich si žiada znalosti so **štruktúrou** — entity, vzťahy, definície — a pre každý z tých troch prípadov existuje vyzreté riešenie, ktoré nie je vektorový index. Lekcia rozoberá všetky tri a najdlhšie sa zdržiava pri otázke, kedy sa ich vôbec oplatí stavať: každé sa dobre predáva a každé býva často zlou voľbou.

:::note[Čítaj tú sekciu, ktorú potrebuješ]

Tri hlavné sekcie stoja samostatne a nemajú medzi sebou poradie čítania. Ak sa rozhoduješ, či vôbec štruktúru
extrahovať, začni [tromi druhmi štruktúry](#three-kinds-of-structure) — slovník, taxonómia, ontológia. Ak od
teba niekto žiada znalostný graf, choď na [kedy sa graf oplatí postaviť](#when-a-graph-earns-its-build-cost).
Ak ide o čísla a dashboardy, choď na [sémantickú vrstvu](#the-semantic-layer-names-two-different-things).
[Záverečná sekcia](#which-of-the-three-you-actually-need) je rozhodnutie, ktoré ich spája.

:::

## Tri druhy štruktúry a zvyčajne vyhrá tá najlacnejšia \{#three-kinds-of-structure}

Tieto tri pojmy sa neustále zamieňajú. Keď ich od seba oddelíš, väčšina nejasností zmizne.

| | Čo to je | Čo umožňuje |
|---|---|---|
| **Riadený slovník (controlled vocabulary)** | pevný zoznam povolených termínov | extraktor prestane vymýšľať názvy |
| **Taxonómia (taxonomy)** | hierarchia nad tými termínmi | zoskupovať výsledky na nadradených úrovniach, dediť vlastnosti, pýtať sa na širšie aj užšie pojmy |
| **Ontológia (ontology)** | triedy, vlastnosti a obmedzenia medzi nimi | validovať dáta a odvodzovať fakty, ktoré nikto nevyslovil |

**Väčšina tímov, ktoré hovoria, že potrebujú ontológiu, potrebuje riadený slovník.** Povedz to zadávateľovi
včas: rozdiel medzi tými dvoma artefaktmi je zhruba rozdiel medzi jedným popoludním a trvalým personálnym
záväzkom.

Riadený slovník rieši najznámejší problém štruktúrovanej extrakcie. Necháš model vytiahnuť vzťahy z troch
tisícok dokumentov. Model to zvládne plynulo, ale nejednotne: v jednom dokumente označí vzťah človeka k firme
ako `works_for`, v ďalšom ako `employed_by`, v treťom ako `is_employee_of`. Nič po prúde ich nespojí, lebo pre
akýkoľvek dopyt sú to tri nesúvisiace predikáty. V jednotlivom dokumente sa model nepomýlil — medzi dokumentmi
ho však nič neobmedzovalo. Podaj mu uzavretý zoznam povolených typov vzťahov a problém zmizne, za cenu
napísania toho zoznamu.

### Kde sa schéma naozaj vyplatí

Schéma sa vypláca na troch oddelených miestach. Vedz, za ktoré z nich platíš:

**Extrakcia.** Daj modelu vopred sadu tried a vlastností a prestane vymýšľať. To je problém `works_for`
z odseku vyššie a práve tu vracia najlacnejšia štruktúra najviac.

**Validácia.** Vrstva obmedzení vie odmietnuť extrahované tvrdenie, ktoré schéme odporuje — hranu zamestnania
mieriacu na dokument namiesto organizácie, dátum mimo povoleného rozsahu. Tak vznikne deterministická brána nad pravdepodobnostným producentom — presne taký mechanizmus odporúča v kurze AI SDLC lekcia [vrstvené brány a rozmanitosť mechanizmov](/ai-sdlc/part-3-verification/layered-gates). Schéma je to, čo takú
bránu vôbec *umožňuje*, lebo brána potrebuje niečo, voči čomu bude kontrolovať.

**Dopyt.** Ak chceš otázku priradiť k pojmu, a nie k úryvku, potrebuješ model pojmov. To je druhý význam
[sémantickej vrstvy](#the-semantic-layer-names-two-different-things): otázka sa cez ňu priradí k pojmu
v doménovom modeli.

### Doménová schéma nie je schéma odpovede

S JSON Schema si sa v tejto príručke už stretol — obmedzuje *tvar odpovede modelu*: povinné polia, povolené
hodnoty enumu, parsovanie, ktoré buď prejde, alebo neprejde. Ontológia obmedzuje *tvar sveta, o ktorom tá
odpoveď hovorí*.

Na papieri vyzerajú podobne, no sú to úplne odlišné artefakty. Schéma odpovede patrí k promptu, mení sa spolu
s ním a vlastní ju ten, kto vlastní danú funkciu. Doménový model patrí organizácii, mení sa vtedy, keď sa mení
biznis, a prežije každý prompt, ktorý ho kedy čítal. Zameň jedno za druhé a doménový model ti skončí verziovaný
vedľa promptovej šablóny — takto sa firma dozvie, že jej definíciu „zákazníka“ prepísala jazyková korektúra.

### Rozumné východisko a test, kedy ho opustiť

Väčšine systémov s LLM dá JSON Schema a k nej validátor ten istý praktický úžitok za zlomok ceny: uzavretú
množinu typov a cestu, ktorou sa neplatný výstup odmietne. Nie je to horšia možnosť, za ktorú by si sa mal ospravedlňovať — väčšinu času je to správna odpoveď. [Formálny stack](./deep-dive.md#the-formal-stack-by-purpose)
— RDF, OWL, SHACL, SPARQL — sa oplatí za podmienok, ktoré vieš pomenovať: potrebuješ odvodzovať fakty, ktoré
nikto nevyslovil; musíš zabezpečiť interoperabilitu so štandardným slovníkom, ktorý v tvojom odvetví už existuje; alebo schému predpísal regulátor a súlad s ňou je povinný.

Rozhodujú dve nákladové položky a ani jednu dodávatelia na slajde neuvádzajú. Po prvé, ontológia si vyžaduje
trvalú údržbu ľuďmi s odborným úsudkom — nie je to práca, ktorú si naplánuješ do kalendára. Druhá položka je
ostrejšia: *zlá ontológia je horšia než žiadna.* Keď schéma chýba, extraktor vyrobí neporiadok, ktorý ako
neporiadok aj vyzerá. Keď je schéma zlá, extraktor musí zaraďovať nesprávne — a nesprávne zaradené dáta
vyzerajú *čisto*: prejdú validáciou, spoja sa, vykreslia sa v dashboarde a sú chybné spôsobom, na ktorý žiadna
kontrola po prúde nie je nastavená.

Pri rozhodovaní o štruktúre sa preto nepýtaj, či bude systém upratanejší. Pýtaj sa: *vieš pomenovať dopyt, na
ktorý dnes odpovedať nevieš a s touto štruktúrou by si vedel?* Ak nie, staviaš kvôli poriadku — a poriadok
neprežije prvé odovzdanie údržby ďalšiemu človeku.

## Kedy sa znalostný graf oplatí postaviť \{#when-a-graph-earns-its-build-cost}

Znalostný graf (knowledge graph) drží entity ako uzly a vzťahy medzi nimi ako hrany; buď ich z korpusu
vytiahne model, alebo ich niekto zostaví ručne. **GraphRAG** je vyhľadávanie nad takým grafom a ako vlastné
meno je to referenčná implementácia od Microsoftu. Začni od toho, čo už vieš, lebo prvý argument, ktorý za
znalostné grafy zvyčajne zaznie — že riešia multi-hop otázky —, má v tomto kurze lepšiu a lacnejšiu odpoveď
inde.

*„Kto vedie oddelenie, ktoré vydalo smernicu X?“* vyzerá ako otázka na prechod grafom. Nie je. Rozlož ju na
dve obyčajné vyhľadania — nájdi oddelenie, ktoré X vydalo, potom nájdi jeho vedúceho — a odpovie na ňu
statická pipeline, ktorú už máš. To je [agentic RAG](../../part-2-agents/agentic-rag/index.md) a nepotrebuje
ani extrakčný prechod, ani schému, ani údržbu. Ak návrh na graf stojí hlavne na multi-hop otázkach, ešte
nenašiel svoj dôvod.

Ten dôvod existuje a je ním iná trieda otázok.

### Tri triedy otázok a rozhoduje len jedna

**Lokálna — okolie entity.** *„Čo vieme o tomto dodávateľovi a s čím je prepojený?“* Graf tu pomôže. Pomôže
však aj rozklad otázky a aj dobre odfiltrované vektorové vyhľadávanie nad dokumentmi označkovanými tým
dodávateľom. Prínos je však malý a sám osebe celý ten aparát neodôvodní.

**Globálna — celý korpus.** *„Aké témy sa opakujú v týchto desiatich tisícoch dokumentov?“* *„Ktoré riziká sa
objavujú vo viac než jednej rodine zmlúv?“* Vyhľadávanie nad chunkami na to odpovedať nevie. Vyhľadávanie
predpokladá, že odpoveď v korpuse leží a tvojou úlohou je nájsť ju; tu niet čo nájsť. Odpoveďou je *zhrnutie
korpusu* a musí vzniknúť skôr, než sa ktokoľvek opýta. Práve táto trieda otázok stavbu ospravedlní. Je to aj
to, o čom je pôvodná práca o GraphRAG — konvenčný RAG podľa jej autorov „zlyháva na globálnych otázkach
mierených na celý textový korpus“ ([Edge a kol., *From Local to Global*](https://arxiv.org/abs/2404.16130)).

**Tá istá entita v rôznych zdrojoch.** Jedna organizácia ako `Acme Corp`, `Acme Corporation`, `ACME Corp.`
a k tomu preklep. V grafe sa tento problém stane viditeľným — a práve tam sa práca na grafe potichu mení na
[stotožňovanie entít](./deep-dive.md#entity-resolution), inú disciplínu s iným rozpočtom.

### Náklady sú rozhodovacie kritériá, nie výhrady

**Extrakcia je prechod LLM cez celý tvoj korpus** a podľa toho je aj drahá. Najjasnejšie dostupné číslo pochádza
z nadväzujúcej práce samotného Microsoft Research:
[LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)
vznikol práve preto, aby sa vyhol vstupným nákladom na indexovanie pri plnej stavbe, a jeho indexovanie sa
uvádza ako „identické s vektorovým RAG a na úrovni 0,1% nákladov plného GraphRAG“. Obrátene to znamená, že plná stavba stojí rádovo tisícnásobok toho, čo obyčajné zaembeddovanie toho istého korpusu. To je
číslo, ktoré patrí do návrhu.

**Extrakcia halucinuje hrany.** Vzťah, ktorý model odvodil, no žiadny dokument ho neuvádza, bude v grafe
vyzerať presne ako ten uvedený. Nesprávne fakty v korpuse dávajú v grafe generovanom LLM chybné trojice —
dokladá to práca [*Less is More: Denoising Knowledge Graphs for RAG*](https://arxiv.org/html/2510.14271v1),
ktorá rozoberá, ako populárne systémy narábajú so šumom z extrakcie. Vektorová cesta obdobu tejto chyby
nemá: vyhľadaný chunk je chunk, ktorý existuje.

**Graf zastaráva ako každý odvodený artefakt.** Naozaj ťažkou časťou je prírastková aktualizácia nad meniacim
sa korpusom a je to ten istý argument, aký táto príručka už vedie o zamrznutých váhach modelu — pozri
[LLMOps](../../part-3-production/llmops/deep-dive.md). Graf postavený raz a nikdy neprestavaný je momentka,
ktorá sa kazí odo dňa, keď je hotová.

**Hodnotiť graf nie je to isté ako hodnotiť vyhľadávanie.** Recall@K nad chunkami ti nepovie nič o tom, či sú
extrahované vzťahy *pravdivé*. Potrebuješ presnosť extrakcie voči označkovanej vzorke a hodnotenie odpovedí od
začiatku do konca na tých typoch otázok, ktoré vie obslúžiť jedine graf. Aparát na to má
[lekcia o evaluácii](../cross-cutting/evaluation/index.md); podrobnosti sú v prehĺbení.

### Kedy graf nestavať

Malý korpus. Otázky tvaru vyhľadaj a vráť. Dáta, ktoré sa menia rýchlejšie, než ich stihneš znova extrahovať.
A to, čo o tom v praxi rozhodne: nikto sa nezaviazal držať extrakčnú schému správnu. Bez takého majiteľa sa
vina zvalí na technológiu namiesto na personálne rozhodnutie, ktoré to spôsobilo.

Bežná produkčná podoba — ak je graf vôbec opodstatnený — nie je graf namiesto vektorov. Sú to vektory na
vyhľadanie, graf na štruktúru a router (smerovač), ktorý rozhodne, kam ktorá otázka pôjde: presne ten aparát
smerovania, aký už stavia [prehĺbenie vrstvy Retrieval](../retrieval/deep-dive.md).

## Sémantická vrstva pomenúva dve rôzne veci \{#the-semantic-layer-names-two-different-things}

Toto slovné spojenie treba v lekcii vysvetliť najmä preto, že má dva významy, ktoré sa v podnikových diskusiách nevedomky zamieňajú. Reálne sú obe.

**Vrstva metrík (metrics layer).** Modelovacia vrstva nad dátovým skladom — dbt Semantic Layer, Cube, LookML
a im podobné —, v ktorej je metrika zadefinovaná *raz*: čo znamenajú „tržby“, aké spojenia tabuliek z toho
vyplývajú, ktoré filtre sú prípustné, akými dimenziami sa dá rezať. Každý konzument si potom vypýta metriku,
namiesto aby si ju znova poskladal v SQL. [dbt](https://docs.getdbt.com/docs/build/about-metricflow) opisuje
problém, ktorý tým rieši, ako „viacero analytikov pracujúcich nad tými istými dátami, každý s vlastným
spôsobom dopytovania“, z čoho plynie „zmätok, nekonzistentnosti a bolenie hlavy pri správe dát“.

**Sémantická vrstva nad jazykovou vrstvou.** V konverzačnej AI: asistent priradí výpoveď používateľa
k **doménovému pojmu** — entite, vzťahu, zámeru —, a nie k úryvku textu. Odpoveď potom vychádza z doménového
modelu, a nie z toho, čo retriever náhodou vrátil.

Súvisia spolu v tom, že obe nahrádzajú výklad podľa okamžitej potreby spoločným modelom. Nie sú tou istou
vrstvou, nemajú spoločné nástroje a zvyčajne ich vlastnia rôzne tímy. Povedz hneď v prvej vete, ktorú z nich
myslíš, a zvyšok rozhovoru pôjde ľahšie.

### Text-to-SQL: výber namiesto odvodzovania

Pre text-to-SQL je dôležitý prvý z tých dvoch významov, teda vrstva metrík — a je to v celej lekcii
najjasnejší prípad toho, ako štruktúra mení náročnosť úlohy.

Vektorové top-K nevie počítať. Agregačné otázky — súčty, pomery, „koľko“, „oproti minulému kvartálu“ —
si popri významovom vyhľadávaní vyžadujú aj štruktúrovanú cestu. Zjavný spôsob, ako ju postaviť, je nechať model písať SQL
nad tvojím dátovým skladom. Ak model pracuje priamo so surovou schémou, musí celý dopyt **odvodiť**: uhádnuť
spojenia tabuliek, tipnúť si, ktorý zo štyroch dátumových stĺpcov je ten biznisový, a poradiť si s hodnotami
v takom formáte, v akom ich zdrojový systém nechal. [BIRD](https://bird-bench.github.io/) je benchmark
postavený práve okolo veľkých, realistických a neupratovaných databáz, v ktorých si hodnoty „zachovávajú svoj
pôvodný a často ‚špinavý‘ formát“. Ľudskí dátoví inžinieri na ňom dosahujú presnosť vykonania (execution accuracy) 92,96%, kým najlepší systém v rebríčku 81,95% (obe hodnoty tak, ako ich k septembru 2025 uvádza rebríček).
Na realistických schémach je teda chybný takmer každý piaty dopyt — a chybný SQL dopyt sa neohlási, vráti
číslo.

Namier ten istý model na sémantickú vrstvu a jeho práca sa zmení. Už dopyt neodvodzuje — *vyberá* definovanú metriku a príslušné dimenzie. To je oveľa menšie rozhodnutie z uzavretého zoznamu a mení sa s ním aj
to, ako sa pokazí: zlý *výber* namiesto zlého *odvodenia*. Nesprávny výber sa dá odhaliť, lebo vieš ukázať,
ktorú metriku model zvolil; jemne zlé spojenie tabuliek ukázať nevieš.
[Cube](https://docs.cube.dev/docs/introduction) vedie tento argument pre agentov priamo: bez sémantickej
vrstvy „agenti píšuci SQL nad dátovým skladom skončia pri nekonzistentných metrikách a neriadenom prístupe“.

Vrstva prináša ešte jednu výhodu a je dôležitejšia, než na prvé počutie znie: keďže cez ňu prechádza každý
dopyt, presúva sa miesto, kde sa politika vynucuje. Cube to formuluje tak, že dopyt „sa overí voči dátovému
modelu a deterministicky sa naň uplatnia prístupové politiky ešte pred tým, než sa dostane do dátového
skladu“. Je to ten istý princíp, na ktorom trvá prehĺbenie vrstvy Retrieval —
[preosej pred vyhľadávaním, nikdy nefiltruj až potom](../retrieval/deep-dive.md) —, len prichádza zo
štruktúrovanej strany.

### Prečo podniky chcú odpovede priradené k pojmom

Priradenie k pojmu prináša dve veci, ktoré citácia úryvku nedá. **Konzistentnosť**: dve formulácie tej istej otázky systém priradí k tomu istému pojmu, a teda vráti rovnakú odpoveď. **Auditovateľnosť**: vieš ukázať,
*ktorý* pojem bol priradený a prečo. Citácia ti povie, ktorý text model čítal; nepovie ti, ako tomu textu
porozumel.

Doménový model, ku ktorému sa otázka priraďuje, nie je nič iné než [ontológia](#three-kinds-of-structure)
z prvej sekcie — a preto sú „potrebujeme ontológiu“ a „potrebujeme sémantickú vrstvu“ tak často tá istá
požiadavka, ktorá prichádza z dvoch oddelení.

### Čo sémantická vrstva stojí a kedy ju vynechať

Sémantická vrstva je najprv vyjednávanie o definíciách a až potom technický artefakt — a drahé je práve to
vyjednávanie. Dve oddelenia, ktoré „aktívneho zákazníka“ definujú inak, sa musia zastaviť a niekto
s právomocou musí rozhodnúť. Samotné modelovanie zaberie týždeň; dohoda môže trvať štvrťrok. Potom sa definície
rozchádzajú, takže ich musí niekto natrvalo vlastniť. Metrika, ktorá potichu zmení význam, je horšia než
žiadna metrika — z toho istého dôvodu, pre ktorý je zlá ontológia horšia než žiadna.

**Kedy ju nestavať:** jeden tím, hŕstka metrík, žiadny spor o definície medzi oddeleniami. Vtedy by vrstva iba
zvyšovala réžiu a prácu odvedie dobre zdokumentovaná sada pohľadov (views). Test je konkrétny — *dali už
niekedy dvaja ľudia na tú istú otázku rôzne čísla?* Ak nie, niet čo zosúlaďovať a nemá zmysel zavádzať riadenie definícií pre spor, ktorý nemáš.

## Slovník, graf alebo sémantická vrstva: čo naozaj potrebuješ \{#which-of-the-three-you-actually-need}

Tri sekcie sú tri odpovede na jednu otázku: *kde v tvojich znalostiach žije štruktúra a kto ju udržiava?*

- Ak ti extraktor vymýšľa názvy, potrebuješ **riadený slovník** — a potrebuješ ho tento týždeň.
- Ak sú tvoje otázky o korpuse ako celku, a nie o čomkoľvek v ňom, potrebuješ **graf** a k nemu majiteľa jeho
  schémy; bez toho majiteľa nepotrebuješ ani jedno.
- Ak sú tvoje otázky aritmetické a dvaja ľudia sa o tú aritmetiku hádajú, potrebuješ **sémantickú vrstvu** —
  a ťažká je tá hádka, nie modelovanie.
- Ak ťa nevystihuje ani jedno, správnou architektúrou je pipeline Ingestion → Retrieval → Generation
  a štruktúrovaná obchádzka je náklad bez návratnosti.

Ontológia, graf aj sémantická vrstva majú jeden spoločný režim zlyhania: každá sa pokazí ticho a vierohodne.
Zlá ontológia prejde validáciou. Zastaraný graf vráti neaktuálne vzťahy bez náznaku neistoty. Metrika s rozídenou definíciou sa bez varovania vykreslí v dashboarde. Ani jedna nevyhodí chybu. Každá z nich potrebuje menovaného majiteľa a kontrolu, ktorá by ju
zachytila.

## Čo si odniesť z lekcie

- Pipeline Časti I predpokladá, že odpoveď v nejakom úryvku existuje; ten predpoklad rúcajú tri triedy otázok
  a každá má inú štruktúrovanú odpoveď.
- Riadený slovník, taxonómia a ontológia sú tri rôzne záväzky — väčšine žiadostí o ontológiu vyhovie riadený
  slovník a testom pre krok ďalej je pomenovať dopyt, na ktorý dnes odpovedať nevieš.
- JSON Schema s validátorom je pre väčšinu tímov rozumné východisko; formálny stack sa oplatí pri odvodzovaní faktov,
  interoperabilite so štandardmi a regulovanom súlade.
- Doménová schéma nie je schéma odpovede: iní majitelia, iné tempo zmien — a keď ich zameníš, definície
  biznisu ti skončia vnútri promptu.
- Grafy neospravedlnia multi-hop otázky, na tie stačí rozklad otázky; ospravedlnia ich globálne otázky nad
  celým korpusom, na ktoré neodpovedá žiadny jednotlivý chunk.
- Pri stavbe grafu musí LLM prejsť celým korpusom, extrakcia vie vymyslieť neexistujúce hrany a hotový graf
  zastaráva — v praxi však rozhodne to, či niekto vlastní extrakčnú schému.
- „Sémantická vrstva“ pomenúva aj vrstvu metrík nad dátovým skladom, aj priraďovanie k pojmom v konverzácii;
  povedz najprv, ktorú z nich myslíš.
- Nad sémantickou vrstvou model vyberá zadefinovanú metriku namiesto toho, aby dopyt odvodzoval. Tým sa
  rozhodnutie zmenší, chyba sa stane viditeľnou a prístupové politiky sa uplatnia skôr, než sa niekto dotkne
  dátového skladu.

**[Nové pojmy](../../glossary.md#structured-knowledge)**: controlled vocabulary, taxonomy, ontology, RDF,
OWL 2, SHACL, SPARQL, knowledge graph, GraphRAG, entity resolution, semantic layer, metrics layer,
text-to-SQL.

---

:::note[Ďalej — druhá časť lekcie]

**[Extrakcia, schémy a dopytovanie](./deep-dive.md)** — ako graf naozaj vzniká (šesť fáz indexovania,
hierarchické zhlukovanie Leidenovým algoritmom a štyri metódy dopytovania), prečo je stotožňovanie entít tou
časťou, ktorá sklame, ako graf hodnotiť, keď metriky vyhľadávania neplatia, formálny stack vysvetlený podľa
účelu a čo text-to-SQL kazí a sémantická vrstva odstraňuje.

Pozri aj: odkiaľ chunky pochádzajú — [Ingestion](../ingestion/index.md); aparát smerovania, ktorý táto lekcia
preberá — [prehĺbenie vrstvy Retrieval](../retrieval/deep-dive.md); multi-hop bez grafu —
[Agentic RAG](../../part-2-agents/agentic-rag/index.md).

:::
