---
title: "Slučka v existujúcom projekte"
sidebar_position: 7
---

# Kód už máš, slučku ešte nie

V I. časti zisťuješ, čo musí platiť skôr, než agent začne písať kód. Doterajšie lekcie sa venovali najmä tomu, ako pripraviť slučku ešte pred vznikom kódu. V praxi je však východisková situácia väčšinou opačná: preberáš fungujúci systém s vlastnou históriou, možno už sčasti napísaný agentmi. Poznatky o ňom sú roztrúsené po chatoch, wiki a hlavách ľudí. Potrebuješ ho meniť bez toho, aby si prišiel o to, čo už funguje.

Príkladom **existujúcej kódovej základne (brownfield)** je `dotnet/runtime`. [Stephen Toub ho označuje](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/) za *„brownfield projekt v tom najextrémnejšom zmysle“*, s *„desaťročiami histórie a miliónmi riadkov kódu“*. Vo svojom príspevku uvádza, že úspešnosť PR od agentov, ktorú na projekte zaznamenali, vzrástla z 38,1% pred prvými zmenami v nastavení na 69% po nich. Tieto zmeny rozoberá lekcia [Príprava je dôležitejšia než model](./preparation-over-model.md).

V rozbehnutom projekte však najprv potrebuješ obnoviť spoločné porozumenie systému a dôveryhodné overovanie. Až potom má takáto príprava zmysel.

## Za požiadavkou na dokumentáciu sa môže skrývať nestabilný vývoj

Andrej Beloborodov [zverejnil vlastný opis stabilizácie, ktorú viedol](https://realaillusions.com/ru/materials/ai-project-stabilization-case/). Išlo o online platformu, ktorú si majiteľ vybudoval sám s dvoma AI asistentmi. Mala vyše 100 000 riadkov TypeScriptu, niekoľko aplikácií, desiatky API trás, databázu a platby. Patrili k nej aj boti v komunikačných službách, predajné lieviky, používateľské účty, administrácia a zjednodušená vzdelávacia platforma. Projekt obsahoval vyše stovky kontrolných skriptov a už zarábal. Pri upratovaní sa preto nesmelo pokaziť nič, čo už fungovalo.

Majiteľ chcel dať do poriadku dokumentáciu, aby sa mu pohodlnejšie vyvíjalo. Za touto požiadavkou sa však skrýval nestabilný vývoj. Požiadavky a architektonické rozhodnutia zostali v niekoľkých desiatkach rozhovorov. Jeden asistent menil svoju časť bez znalosti dohody s druhým. Prestala fungovať susedná časť a jej oprava pokazila ďalšiu. Rozpadal sa samotný projekt.

Ponúkalo sa vyexportovať chaty, roztriediť priečinky, napísať spoločný pokyn pre agentov a pokračovať. Beloborodov tento postup odmietol: aj v uprataných súboroch by mohli zostať protichodné dohody bez toho, aby niekto určil, ktoré z nich zodpovedajú bežiacemu systému.

Beloborodov odporúča začať auditom, ak sa prejavujú aspoň 3 z týchto 9 varovných signálov:

- Kód píše viacero AI v rôznych chatoch.
- Chýba jediný zdroj pravdy.
- Pravidlá a ciele projektu existujú len v rozhovoroch.
- Nový agent nevidí rozhodnutia predchádzajúceho.
- Každá oprava pokazí inú funkciu.
- Testy sú zelené a nič viac o nich nevieš.
- Projekt funguje, ale bojíš sa ho meniť.
- Infraštruktúra vznikala živelne, bez návrhu.
- O chybách sa dozvedáš zo sťažností zákazníkov.

Hranica 3 z 9 je jeho orientačné pravidlo, nie overená diagnostická metóda.

Beloborodov navrhuje aj **test nového chatu**: otvor nový chat a opýtaj sa agenta na architektonické rozhodnutia z minulého týždňa. Ak nevie odpovedať alebo jeho odpoveď odporuje tvojej predstave, podľa Beloborodova pravdepodobne pracuje s vlastnou verziou projektu.

## Audit pred refaktoringom: každý model nech pracuje nezávisle

V [nadväzujúcom texte o technickom dlhu](https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/) Beloborodov odmieta postup, pri ktorom požiadaš AI, aby všetko poriadne prepísala. Výsledkom by podľa neho bol nový projekt s novými problémami. **Audit pred refaktoringom** má najprv rozlíšiť dlh, ktorý vývoj skutočne brzdí, rozhodnutia, ktoré zatiaľ môžu zostať, a časti, do ktorých sa bez osobitnej prípravy nemá zasahovať. Potom urči cieľovú architektúru a cestu k nej rozdeľ na etapy. Každá sa musí skončiť funkčným výsledkom.

Pri stabilizačnom audite preverilo niekoľko navzájom úplne nezávislých modelov **13 vopred určených oblastí**. Pri ďalšom audite ich zachovaj, aby si mohol porovnať výsledky:

1. Dokumentácia a zdroje pravdy.
2. Architektúra verzus skutočný kód.
3. Úplnosť zdrojov.
4. Reprodukovateľnosť na novom počítači.
5. Kvalita kódu a hranice komponentov.
6. Testy a to, čo naozaj overujú.
7. Bezpečnosť.
8. Platby a prideľovanie prístupu.
9. Databáza, migrácie, zálohovanie a obnova.
10. Integrácie s komunikačnými službami a úlohy na pozadí.
11. Pozorovateľnosť, nasadzovanie a vrátenie zmeny.
12. Používateľské a administrátorské postupy.
13. Pripravenosť na ďalší vývoj s AI.

Verdikty sa zásadne rozchádzali. Jeden model dal projektu 4 z 5: pochválil architektúru, ochranné skripty, pokyny pre agentov a malý počet nedokončených zástupných implementácií. Druhý označil prevádzku za nemožnú. Beloborodov tento rozdiel vysvetľoval tým, že každý model mal pre svoj verdikt reálny podklad: niektoré modely posudzovali kód, iné správanie systému v prevádzke. Jeho pravidlo: dôležitú kontrolu začni aspoň dvoma rôznymi modelmi.

**Nezávislý audit viacerými modelmi** využíva [rozmanitosť mechanizmov](../part-3-verification/layered-gates/index.md): odlišné mechanizmy odhalia odlišné druhy zlyhania. Spriemerovaním známok by si zahodil užitočnú časť nezhody. Namiesto toho zisti, čo každý model pred svojím verdiktom skutočne preveril.

Audit odhalil aj niektoré neaktuálne kontroly platieb. Niektoré kritické kontroly len hľadali reťazec pomocou grepu. Ak test nájde v zdrojovom kóde `PAID`, dokazuje len to, že tam to slovo je, nie že platba funguje. Presne tento prípad rozoberá [príklad v lekcii Detekcia verzus oprava](../part-3-verification/detection-vs-mutation.md). Takáto kontrola považuje úlohu za hotovú, keď sa objaví reťazec – a tým [brána určuje výsledok, ktorý agent vytvorí](./rules-that-hold.md).

Audit premeň na postup: čo funguje → čo brzdí vývoj → čo je rizikové → čo urobiť → ako overiť výsledok. Bez neho dostane ďalší agent aj po verdikte len vágne zadanie „prepíš všetko“.

## Pred zmenou zachyť súčasné správanie

Michael Feathers v knihe *Working Effectively with Legacy Code* zaviedol pojem **charakterizačný test** (characterization test). Vo svojom [vysvetlení charakterizačného testovania](https://michaelfeathers.silvrback.com/characterization-testing) píše: *„Účelom charakterizačného testovania je zdokumentovať skutočné správanie systému, nie overiť, či sa správa tak, ako by si si želal.“*

Skôr než existujúci kód odovzdáš agentovi, zachyť testami, čo robí dnes. Aj správanie, ktoré možno neskôr označíš za chybné. Keď charakterizačný test prestane prechádzať, upozorní na zmenu správania. Pri kontrole neúspešného testu potom musíš výslovne rozhodnúť, či sa má pôvodné správanie zachovať.

Napríklad test platobného postupu môže vykonať platbu a následne overiť prístup. Tým preverí väzbu medzi zaplatením a pridelením prístupu. Hľadanie reťazca s platobným stavom ju nepreverí nikdy. Zachovaj aj kontroly scenárov v susedných častiach systému. Beloborodov vo svojom texte o technickom dlhu definuje regresiu ako pokazenie funkcie, ktorá už fungovala.

Kritické kontroly založené na grepe nahraď testami správania a súčasné správanie zachyť charakterizačnými testami. Oba kroky zviditeľnia jeho zmeny. Agent optimalizuje presne to, čo kontroluješ. Ak súčasné správanie nezachytáva žiadny test, regresiu nemusí odhaliť ani agent, ani jeho brána.

Plán obnovy zahŕňal aktualizovanú **overovaciu sadu (verification pack)** – súbor skutočne funkčných kontrol – a základnú automatickú bránu v CI pre nové funkcie. Predtým, než sa na sadu spoľahneš, zisti, čo každá kontrola vykoná a čo znamená jej úspešný výsledok. Kontrolóra oddeľ od implementácie podľa hranice opísanej v lekcii [Detekcia verzus oprava](../part-3-verification/detection-vs-mutation.md).

## Zdroj pravdy obnovuj podľa kódu

Plán dokumentácie sa začal opisom skutočného stavu projektu a prostredia. Všetka projektová dokumentácia mala byť pri kóde, bez rozporov, s oddelenou históriou, cieľovým stavom a experimentmi. Plán vykonal samotný majiteľ podľa Beloborodovových pokynov. Spúšťal skripty, ktoré Beloborodov pripravil na presun dokumentov z chatov do repozitára.

Oddelenie histórie, zámerov a experimentov má praktický dôvod. Nový agent nesmie zamietnutý návrh čítať ako pokyn. Želaná architektúra sa nesmie tváriť ako tá, ktorá je nasadená.

**Jediný zdroj pravdy (single source of truth)** obnovuj z kódu: musí zodpovedať implementácii. O tom, čo systém robí dnes, rozhoduje kód. Oblasť auditu „Architektúra verzus skutočný kód“ ti ukáže, ktorým dokumentom nemáš veriť. Dokumentáciu preto zosúlaď s implementáciou. Do písomnej pamäti ulož to, čo z kódu nevyčítaš: rozhodnutia a ich dôvody, cieľový stav a označenie experimentov. Ako túto pamäť vrstviť a načítavať, vysvetľuje lekcia [Pamäť projektu a vrstvenie znalostí](./project-memory-and-tiering.md).

Lákavou skratkou je nechať agenta zhrnúť staré chaty do nového súboru pravidiel. Gloaguen a kolegovia z ETH Zurich v [štúdii kontextových súborov repozitárov](https://arxiv.org/abs/2602.11988) porovnávali tri varianty: agent bez kontextového súboru, so súborom vytvoreným LLM a so súborom od vývojára. Kontextové súbory zvýšili náklady na inferenciu v priemere o viac než 20%. Vplyv na úspešnosť úloh bol okrajový: pri generovaných súboroch mierne záporný, pri súboroch od vývojárov mierne kladný, no ani v jednom smere nebol štatisticky významný. (Čísla pochádzajú z aktuálnej revízie článku; skoršie revízie uvádzali iné hodnoty.) Autori navrhujú generované súbory zatiaľ vynechať. Ručne písané odporúčajú obmedziť na to, čo programovací agent potrebuje a v README nenájde, napríklad osobitné konvencie či nefunkčné požiadavky.

Kurz tento záver rozširuje aj na sumarizáciu starých chatov: aj takto vznikne generovaný kontextový súbor. Z prehľadnejšieho dokumentu ešte nevyplýva, že jeho obsah zodpovedá kódu. Z rozhovorov obnov rozhodnutia, over ich platnosť podľa implementácie a zachovaj dôvody. Z celého archívu rozhovorov však nerob trvalé pokyny.

Test nového chatu tu použi ako akceptačnú kontrolu. Novému agentovi daj prístup k repozitáru, bez histórie starých chatov, a opýtaj sa ho na nedávne architektonické rozhodnutia. Musí odpovedať z podkladov v repozitári a odlíšiť existujúci stav od zamýšľaného. Ak stále potrebuješ nájsť ten správny starý rozhovor, spoločnú pamäť si ešte neobnovil.

## Obnov slučku, odstráň zistené riziká a zopakuj audit

Prvá fáza plánu obnovy mala znovu umožniť kontrolované zmeny. Obsahovala šesť položiek:

- Opísať skutočný stav projektu a prostredia.
- Presunúť všetku projektovú dokumentáciu ku kódu a odstrániť rozpory.
- Oddeliť v dokumentácii históriu, cieľový stav a experimenty.
- Aktualizovať overovaciu sadu.
- Pridať základnú automatickú bránu v CI pre nové funkcie.
- Zaviesť odľahčenú slučku: úloha → akceptačné kritériá → implementácia → nezávislá kritika → kontrola → výsledok.

Je to najmenšia podoba cyklu [Plán, kontrola, implementácia, kritik](../part-2-loop/plan-review-implement-critic.md). Pri odovzdávaní práce používaj [artefakty ako rozhranie](../part-2-loop/artifacts-interface.md), aby sa každá úloha aj jej výsledok dali skontrolovať.

Druhá fáza plánu sa zameriavala na riziká zistené auditom. Mala zabezpečiť platby a prideľovanie prístupu a nahradiť kritické kontroly založené na grepe testami správania. Zahŕňala aj bezpečné zmeny databázy so záznamom migrácií a kontrolu externých integrácií. Komponenty mali tvoriť nedeliteľné celky a chyby mali zostať izolované. Išlo o ohraničené opravy s overiteľným výsledkom.

Zvyšok druhej fázy plánu sa týkal prevádzky: pozorovateľnosti a alertingu, overiteľného nasadzovania a scenárov vrátenia zmeny aj nasadenia opravy namiesto vrátenia (roll-forward). Plán vyžadoval overiť obnovu zálohy do prázdnej databázy ešte pred záverečnou kontrolou pripravenosti na produkciu. Existencia zálohy ešte nezaručuje, že ju dokážeš obnoviť. Jednotlivé postupy nájdeš v lekciách [Prostredia, migrácie a reálne dáta](../part-4-platform/environments-migrations-data.md) a [Pozorovateľnosť, nasadzovanie a núdzový vypínač](../part-4-platform/observability-rollout.md).

Opakovaný audit repozitára ukázal, že zistené problémy boli odstránené a projekt bol dostatočne stabilný na ďalší vývoj. Zásadou je **opakovaný audit v rovnakých oblastiach**. S novým zoznamom kontrol by si odpovedal na nové otázky a o tých pôvodných by si sa nič nedozvedel. Z prípadu si preto vezmi 13 oblastí auditu, nie verdikt jediného modelu.

:::tip[▶ Video]

<YouTube id="kY7ak0p4tZM" title="How to use Generative AI for App Modernization" />

Video IBM Technology sa venuje využitiu generatívnej AI pri modernizácii existujúcich aplikácií. Táto lekcia vysvetľuje predpoklad takejto práce: čo preveriť auditom a ktoré správanie zachytiť testami ešte pred zmenou.

:::

## Vo veľkej organizácii začni v malom a audítora vyber mimo tímu

V zrelom repozitári nie je pocit rýchlosti dobrým kritériom na zavádzanie AI. [Randomizovaný experiment METR z roku 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) sledoval 16 skúsených vývojárov pri 246 úlohách vo veľkých open-source repozitároch, do ktorých roky prispievali. [Repozitáre mali v priemere približne 10 rokov a vyše 1 100 000 riadkov kódu](https://arxiv.org/abs/2507.09089). Účastníkom trvala práca s AI o 19% dlhšie, hoci pred experimentom očakávali zrýchlenie o 24% a aj po ňom verili, že ich AI zrýchlila o 20%.

Samotný METR už tieto výsledky označuje za zastarané. V [aktualizácii z februára 2026](https://metr.org/blog/2026-02-24-uplift-update/) uvádza, že AI dnes vývojárov pravdepodobne zrýchľuje viac. Pre výberové skreslenie sú dôkazy o veľkosti tohto nárastu len veľmi slabé. Starší výsledok preto posudzuj s ohľadom na podmienky, v ktorých experiment prebehol. Ukazuje však, prečo presvedčenie skúsených vývojárov nenahradí východiskové meranie: ich dojem a výsledok experimentu sa rozchádzali aj v tom, či AI prácu zrýchlila alebo spomalila.

AI zavádzaj po jednotlivých tímoch. Priprav východiskové meranie (baseline) a porovnaj stav pred zavedením a po ňom. Výslovne pomenuj proxy metriku aj jej menovateľ: na akú jednotku práce sa údaj vzťahuje. Pilot migrácií môže sledovať napríklad čas na jednu migráciu; takýto výsledok sa nesmie potichu zmeniť na tvrdenie o celkovej produktivite vývoja. Túto disciplínu vysvetľujú lekcie [Ako posudzovať dôkazy](./reading-the-evidence.md) a [Úzke miesto overovania](./verification-bottleneck.md).

Ohraničený príklad prináša Google v [správe o interných migráciách](https://arxiv.org/abs/2501.06972). Autori ju výslovne označujú za správu o skúsenostiach (experience report), nie za výskumnú štúdiu. Pri jednej z opísaných migrácií zistili, že 80% úprav kódu v začlenených zmenách vytvorila v plnom rozsahu AI. Inžinieri, ktorí túto migráciu robili, odhadli, že celkový čas bol približne o 50% kratší než pri porovnateľnej migrácii bez pomoci LLM. Ide o dva odlišné druhy dôkazu: zistený podiel úprav a odhad časovej úspory. Navyše autori z Googlu opisujú nástroje Googlu, takže majú na výsledku vlastný záujem.

Začni presne vymedzeným typom zmien, napríklad migráciou. Pri zmene s mechanicky overiteľnou podmienkou dokončenia ľahšie udržíš rozsah práce než pri otvorenom zadaní novej funkcie.

Na enterprise úrovni zver audit ľuďom mimo tímu, ktorý zmeny dodáva. Títo audítori môžu pri práci používať agentov. Audítori nesmú upravovať kód, ktorý auditujú. Takto prenesieš [detekciu oddelenú od opravy](../part-3-verification/detection-vs-mutation.md) na [enterprise úroveň](../part-5-scale-governance/enterprise-tier/index.md). Uchovávaj výsledky opakovaných auditov v rovnakých oblastiach, aby ich neskôr mohla skontrolovať aj tretia strana.

## Tri úrovne zrelosti: soloista · malý tím · enterprise

Na každej úrovni platí: **skôr než agenti začnú meniť systém, zisti, čo už existuje, a zachyť jeho súčasné správanie testami.**

- **Soloista.** Urob audit, testami zachyť správanie časti, ktorú chceš meniť, a pamäť repozitára prever testom nového chatu. Až potom obnov odľahčenú slučku. *Akému zlyhaniu to predchádza:* nový agent si z útržku rozhovoru poskladá iný projekt, zatiaľ čo sa funkčné časti nepozorovane kazia.

- **Malý tím.** Nechaj nezávislé modely auditovať rovnaké oblasti, zosúlaď dokumenty s kódom a aktualizovanú overovaciu sadu zapoj do CI. *Akému zlyhaniu to predchádza:* agenti sa riadia protichodnými dohodami a zelená kontrola zakryje regresiu v susednej funkcii.

- **Enterprise.** Pilot obmedz na presne vymedzený typ zmien a vyhodnoť ho voči východiskovému meraniu tímu. Audítorov vyber mimo tímu, ktorý zmeny dodáva; auditovaný kód neupravujú. Uchovávaj porovnateľné opakované audity. *Akému zlyhaniu to predchádza:* tím zavedie AI len preto, že sa mu zdá rýchlejšia, a vlastné tvrdenie, že chybu opravil, považuje za nezávislé overenie. Záznamy opakovaných auditov poskytujú *dôkaz*, ktorý môže neskôr preskúmať tretia strana. Naproti tomu test nového chatu na úrovni soloistu preveruje iba *schopnosť*: čo dokáže nový agent zistiť z repozitára dnes.

## Čo si odniesť

- Požiadavka na dokumentáciu môže skrývať nestabilný vývoj. Skôr než agentovi zadáš reorganizáciu alebo prepis, auditom zisti, čo bráni bezpečným zmenám.
- Zachovaj 13 oblastí stabilizačného auditu a preskúmaj rozpory medzi verdiktmi. Pochvala kódu od jedného modelu neodpovedá na otázku, či sa systém dá prevádzkovať.
- Pred zmenou zachyť skutočné správanie. Charakterizačný test upozorní na jeho zmenu; hľadanie reťazca `PAID` platobný postup neoverí.
- Spoločnú pamäť obnov podľa kódu a uchovaj rozhodnutia aj dôvody. Test nového chatu preverí, či repozitár poskytuje dosť kontextu aj bez starého rozhovoru.
- Najprv obnov odľahčenú slučku: úloha, akceptačné kritériá, implementácia, nezávislá kritika, kontrola. Potom odstráň riziká zistené auditom a zopakuj audit v rovnakých oblastiach, aby si mohol porovnať stav pred opravami a po nich.
- Zavádzanie AI rozširuj postupne, na ohraničených úlohách s výslovnými východiskovými meraniami. Vlastné odhady odlišuj od nameraných výsledkov a na enterprise úrovni oddeľ audítorov od úprav kódu, ktorý kontrolujú.

**[Nové pojmy](../glossary.md#existing-codebase)**: existujúca kódová základňa (brownfield), audit pred refaktoringom, nezávislý audit viacerými modelmi, overovacia sada, jediný zdroj pravdy (obnovený z kódu), test nového chatu, opakovaný audit v rovnakých oblastiach.
