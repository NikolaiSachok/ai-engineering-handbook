---
title: "Pozorovateľnosť, nasadzovanie a núdzový vypínač"
sidebar_position: 4
---

# Produkcia je posledná brána a musí vedieť odpovedať

Kurz sa začal [slučkou, nie pipeline](../intro.md) — a slučku z nej robí práve tá hrana, ktorá vedie z ostrej prevádzky späť k plánovaniu. Táto lekcia stavia tú hranu. Berie tri mechanizmy a každý odpovedá na inú otázku: **telemetria** rozhoduje, či vôbec *spoznáš*, že zmena je zlá, **postupné nasadzovanie** rozhoduje, *koľko ľudí* sa to dozvie skôr než ty, a **núdzový vypínač** rozhoduje, *ako rýchlo* sa to zastaví. Telemetria v tejto lekcii zahŕňa aj snímače mimo systému, pretože pri najhorších zlyhaniach zvnútra nepríde nič. Vynechaj ktorýkoľvek z nich a zo slučky zostane pipeline s optimistickým názvom.

## Niektoré triedy chýb existujú iba v produkcii

III. časť postavila [reťaz brán](../part-3-verification/layered-gates/index.md), ktorou musí zmena prejsť skôr, než niekam dopadne. Úplná byť nemôže, a nie preto, že by vznikla nedbalo: celá trieda chýb existuje iba pod skutočnou prevádzkou, skutočným rozdelením dát, na skutočných zariadeniach a pri skutočnej súbežnosti. Žiadna brána pred zlúčením ich nevníma, presne z toho mechanizmového dôvodu, ktorý tamtá lekcia pomenovala. Produkcia teda nie je „to po overení“ — produkcia je **koncová brána reťaze** a telemetria je jej mechanizmus. Nasadenie, ktoré nevieš pozorovať, je brána bez snímača.

Minimálna užitočná sada snímačov je malá a oplatí sa ju vymenovať, lebo tímy často merajú všetko a nesledujú nič:

- **Miera chýb**, podľa možnosti rozdelená podľa cesty novým kódom, aby sa regresia nestratila v priemere so zdravým menovateľom.
- **Latencia vo vysokom percentile**, nie priemer — priemer skryje práve ten chvost, kde používatelia naozaj trpia.
- **Saturácia** toho, čoho je málo: pripojení, hĺbky frontu, pamäte.
- **Jeden obchodný signál (business signal)**, ktorý by sa pohol, keby bola funkcia pokazená spôsobom, aký žiadna technická metrika nevidí — začaté platby, odoslané správy, obnovené relácie. Práve tento signál sa vynecháva najčastejšie a práve on zachytí zmenu, ktorá je technicky zdravá a funkčne na nič.

Telemetria patrí do [podmienky dokončenia](../part-2-loop/vision-to-stages.md) úlohy. Agent sa riadi zadaním; signály, ktoré v ňom chýbajú, možno vôbec nevzniknú. Urči preto sadu telemetrických signálov vrátane obchodného signálu a nechaj [kritika](../part-2-loop/plan-review-implement-critic.md) overiť, že ich systém naozaj odosiela, nielen že funkcia funguje. [Andrey Beloborodov](https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/) odhaduje, že funkčnú pozorovateľnosť nemá takmer žiadny projekt vytvorený „vibe codingom“; ani u žiadneho zo svojich klientov ju podľa vlastných slov nenašiel riadne vyriešenú. Za náročné považuje najmä rozhodnutie, čo znamená „dobré“ na hranici medzi technikou a biznisom. Túto definíciu za teba agent neurčí. Kým zadanie nevymedzí, čo znamená „dobré“, nemáš čo užitočné merať.

## Zachytávaj zlyhania sondami zvonku, alertmi a hláseniami od používateľov

Najťažšie býva zachytiť signál, ktorý sa vôbec neozve: používateľ nedokončil registráciu, nemohol zadať hodnotu alebo narazil na službu, ktorá preňho nefungovala. Ako upozorňuje Beloborodov, nefunkčný systém neposiela vôbec žiadne dáta. Kurz z toho vyvodzuje, že na internom dashboarde môže takéto ticho vyzerať ako bezchybná prevádzka. Zaznamenávaj preto zámerne aj to, čo sa nestalo: keď používateľ postup opustí, ulož posledný krok, ku ktorému sa dostal. Z „nedokončil“ tak vznikne udalosť, ktorú vieš spočítať.

V pravidelných intervaloch spúšťaj mimo siete služby syntetickú sondu zvonku (black-box probe), ktorá prejde kľúčový používateľský postup. [Kniha Google SRE](https://sre.google/sre-book/monitoring-distributed-systems/) opisuje black-box monitoring (monitoring zvonku, tak ako systém vidí používateľ) ako sledovanie príznakov: ukáže, že systém zlyháva práve teraz. Dopĺňa ho monitoringom zvnútra (white-box), o ktorý sa opiera vo väčšej miere. Vnútorné metriky môžu odhaliť blížiaci sa problém, ktorý sonda zvonku ešte nezachytí.

Alert na chýbajúci heartbeat (pravidelný signál života) je samostatná kontrola životnosti (liveness), oddelená od sondy. Komponent vnútri systému pravidelne odosiela signál; ak signál nepríde, spustí sa alert. Takáto kontrola zachytí úplné ticho. Heartbeat však dokazuje iba to, že žije komponent, ktorý ho odosiela, nie že služba obsluhuje používateľov.

Rozdeľ alerty do niekoľkých úrovní kritickosti (criticality levels). Pri alertingu na príznaky (symptom-based alerting) posielaj page (alert, ktorý zobudí človeka) iba pri príznakoch, ktoré používateľom škodia teraz alebo im čoskoro začnú škodiť a vyžadujú ľudský úsudok. Menej naliehavú prácu smeruj do ticketov; podklady na ladenie nechaj na dashboarde alebo v logoch. Kniha odporúča alerty, po ktorých môže človek konkrétne konať, a varuje, že časté budenie ľudí naučí alerty len preletieť očami alebo ignorovať aj skutočné zlyhanie. Ak na alert zakaždým reaguješ rovnakým mechanickým úkonom, tento úkon automatizuj alebo zníž kritickosť alertu.

Hlásenie od používateľa je snímač poslednej záchrany. Ten istý praktik odporúča pripraviť ho ešte pred prvým sprístupnením: namiesto e-mailovej schránky použi systém na evidenciu požiadaviek (issue tracker) a možnosť nahlásiť problém pridaj na každú stránku aj do každého kroku postupu. Zahrň hlásenia do triáže (triage) spolu s produkčnými signálmi. Potvrdená chyba *je* únik bez ohľadu na to, či ju odhalil signál alebo používateľ, a patrí do [registra únikov](../part-3-verification/escape-ledger.md) spolu s názvom brány, ktorá ju mala zachytiť. Ak hlásenie predbehlo všetky alerty, pomenuj aj chýbajúci signál. To je spätná hrana v najkonkrétnejšej podobe – prevádzka učí reťaz brán, voči čomu je slepá.

Pri triáži s pomocou agenta sa údaje zákazníkov dostávajú do kontextu modelu: tickety obsahujú mená, údaje o účtoch aj snímky obrazovky. Uplatni na agenta rovnaké [ochrany reálnych dát](./environments-migrations-data.md): citlivé údaje odstráň alebo zakry skôr, než model hlásenie uvidí, a vymedz, čo agent smie čítať.

## Postupné nasadzovanie ohraničí blast radius v počte ľudí aj v čase

Ak sa zlá zmena aj tak stane, užitočná otázka znie, koľko používateľov na ňu narazí ako prvých. Tri zásady menia sprístupnenie na riadený postup.

**Oddeľ nasadenie od sprístupnenia.** Dostať kód von a zapnúť správanie majú byť dva rôzne úkony, a presne to ti kúpi **feature flag (prepínač funkcie)**. Kód ide von vypnutý; správanie sa zapne pre 1%, potom pre 10%, potom pre všetkých. Keď je niečo zle, meníš okruh používateľov, nie nasadenie. Flag na sprístupnenie (release flag) je krátkodobý. Každý flag na sprístupnenie musí mať vlastníka, opis a dátum odstránenia. Dlhodobý flag núdzového vypínača musí mať vlastníka a pravidelnú revíziu spolu s korpusom pravidiel, nie dátum skončenia platnosti ani dátum odstránenia. Oba typy patria do [údržby flagov](../part-5-scale-governance/drift-and-rot.md).

**Ak vieš porovnať výstupy, spusti novú cestu najprv v tieňovom behu.** Pri prepísanom dopyte alebo refaktoringu kontroly oprávnení máš správnu odpoveď, s ktorou môžeš porovnávať: výstup pôvodnej cesty. Ešte predtým, než canary vystaví používateľov novej ceste (candidate), spúšťaj ju na skutočných vstupoch popri pôvodnej ceste (control) a porovnávaj výstupy. Používateľom naďalej vracaj pôvodný výsledok, kým porovnanie nepotvrdí zhodu. Pri takejto zmene teda na začiatok postupného nasadzovania pribudne tieňové overovanie (shadow run): tieňový beh → canary → zvyšovanie podielu → všetci. Knižnica [Scientist](https://github.com/github/scientist) vždy vracia výsledok `control`, popri ňom spúšťa `candidate`, porovnáva výstupy a zaznamenáva časy aj výnimky. Beloborodov na [stránke vlastného projektu](https://realaillusions.com/ru/projects/cyprus-real-estate-project/) uvádza, že jeho deduplikačná pipeline práve prechádza tieňovým overovaním a zatiaľ ju neuvádza ako súčasť reportov pre klientov. V tieňovom behu vypni vedľajšie účinky: ak obe cesty vykonajú zápis, odošlú e-mail alebo uskutočnia platbu, tá istá operácia sa vykoná dvakrát. Zápisy nahraď stubmi, ktoré nič nezapisujú alebo tieňový beh obmedz na čítanie a výpočty.

**Vrátenie zmeny musí spúšťať automat, nie človek.** Zvyšovanie podielu, ktoré postupuje podľa harmonogramu a cúva až vtedy, keď si to niekto všimne, je pomalá brána prezlečená za rýchlu. Naviaž ho na signály vyššie: prekročenie miery chýb alebo latencie ho zastaví a obráti bez čakania na niečí úsudok. Ľudský úsudok je tá vzácna vec, ktorú ti III. časť kázala [míňať zámerne](../part-3-verification/review-at-volume.md); všimnúť si pohyb metriky nie je miesto, kde ho minúť.

Existuje aj nameraný náznak, že si táto hrana pozornosť zaslúži. Správa [DORA](https://dora.dev/dora-report-2025/) z roku 2025 zistila negatívny vzťah medzi používaním AI a stabilitou dodávania — a ako zdôraznil úvod, opiera sa iba o sebahodnotenie respondentov rozsiahleho prieskumu — ide o vnímanie, nie o telemetriu. Neoprávňuje to na „AI zhoršuje tímy“. Oprávňuje presne na jedno: nestabilita, ktorú prieskum zaznamenal, sa týka práve *dodávania* — teda cesty sprístupnenia a obnovy — takže tú cestu stavaj zámerne a nespoliehaj sa, že vydrží.

:::tip[▶ Video]

<YouTube id="ztIIcXNzMN4" title="What is Site Reliability Engineering (SRE)? — IBM Technology" />

Úvod IBM do SRE — ciele úrovne služby, rozpočty chýb a spoľahlivosť ako inžiniersky cieľ namiesto zbožného priania. Čítaj ho ako slovník k automatizácii z tejto lekcie: SLO je hranica, na ktorú sa zvyšovanie podielu dá naviazať, a práve to mení „niekto si to všimne“ na mechanizmus.

:::

## Núdzový vypínač nesmie potrebovať pipeline, ktorá sa práve pokazila

Vrátenie zmeny, ktoré si žiada zelené CI, nové zostavenie a nasadenie, nie je núdzový vypínač. Je to nádej s dodacou lehotou — a zlyhá presne v situácii, pre ktorú existuje, teda keď je časťou problému sama pipeline. Vypnutie musí byť *zmena stavu*, nie *zostavenie*: prepni flag, presuň váhu premávky, vráť smerovanie. Nech je mechanizmus akýkoľvek, skúška je jediná otázka — dokáže ho jeden človek použiť za pár sekúnd bez toho, aby vznikol nový artefakt?

**Zostav raz a medzi prostrediami posúvaj ten istý artefakt.** V predprodukčnom prostredí aj v produkcii spúšťaj ten istý zostavený image s tagom odkazujúcim na commit. Pri spúšťaní ho urč digestom (nemenným odtlačkom obsahu), aby presunutie tagu (presúvateľného štítka) nezmenilo, čo beží. Nové zostavenie pre každé prostredie vytvorí iný artefakt než ten, ktorý prešiel testami. Predchádzajúci artefakt uchovaj nezmenený; vrátenie zmeny potom znamená prepnúť naň odkaz, nie ho znova zostavovať. Beloborodov k tomu odporúča aj prevádzkové návyky: skripty nasadzovania vo verzovacom systéme, bezpečne opakovateľné (idempotentné) nasadenie a záznam, kto ktorú verziu kam nasadil. Oprávnenie na nasadenie do produkcie udeľuj podľa [princípu najnižších oprávnení](./least-privilege-sandboxing/index.md) (least privilege). Vo vlastnom postupe podľa jeho opisu AI nasadzuje do testovacieho prostredia a produkciu nasadzuje sám, pretože AI s prístupom k secretom považuje za bezpečnostnú dieru. Na enterprise úrovni sa dá posúvaný artefakt overiť vďaka [záznamu o pôvode](../part-5-scale-governance/enterprise-tier/deep-dive.md) (provenance).

Flotily majú na tom vypínači ešte druhú polohu, ktorú samostatný vývojár nepozná. Zastaviť *zmenu* je vrátenie; zastaviť jej *zdroj* znamená pozastaviť agentov. Flotila, ktorá ďalej generuje nad základom, ktorý si práve vrátil, ti ten problém s chuťou postaví znova alebo naskladá ďalšiu prácu na základ, ktorému už neveríš. Runbook preto potrebuje oboje: vrátiť artefakt a zastaviť slučku, ktorá ho vyrobila — [človek-smerovač](../part-2-loop/roles-and-the-human.md) tu vykonáva zásah, ktorý sa zo svojej podstaty nedá delegovať na to, čo sa práve zastavuje.

## Tri úrovne zrelosti: soloista · malý tím · enterprise

Invariant sa nehýbe: **zmena je v produkcii pozorovateľná, k svojmu publiku sa dostáva postupne a jeden človek ju vie za pár sekúnd zastaviť bez nového zostavenia.** Škáluje sa to, koľko z toho beží bez človeka v ceste.

- **Soloista.** Sledovanie chýb, ktoré ťa naozaj zobudí, flag, ktorý zapneš najprv sebe a hŕstke známych používateľov a až potom všetkým, prepínateľný z telefónu, syntetická sonda zvonku na overenie dostupnosti kľúčového postupu a odkaz „nahlásiť problém“ na každej stránke. *Akému zlyhaniu to predchádza:* o niekoľko dní sa od používateľa dozvieš, že nové vydanie pokazilo registráciu — a potom ti hodinu trvá, kým to vrátiš.
- **Malý tím.** Dashboardy naviazané na hŕstku dohodnutých signálov, canary alebo percentuálne nasadzovanie ako predvolený postup, automatické vrátenie zmeny pri prekročení hranice, spísaný runbook, ktorý menuje, kto čo prepína, a signály uvedené v podmienke dokončenia každej úlohy, aby ich kritik mohol overiť. *Akému zlyhaniu to predchádza:* funkcia sa sprístupní bez jediného signálu alebo počas zvyšovania podielu každý predpokladá, že ten graf sleduje niekto iný.
- **Enterprise.** SLO s rozpočtami chýb, ktoré riadia tempo sprístupňovania, progresívne dodávanie s automatizovanou analýzou, auditované postupy núdzového vypnutia nacvičované ako požiarny poplach a vyhodnotenie incidentov aj triáž hlásení od používateľov, ktoré plnia register únikov pri dodržaní ochrany dát. *Akému zlyhaniu to predchádza:* schopnosť vrátiť zmenu, ktorá sa mimo prezentácie nikdy neskúšala a odhalí sa počas incidentu, pre ktorý bola napísaná.

## Čo si odniesť

- **Produkcia je koncová brána.** Niektoré chyby sa prejavia iba pod skutočnou prevádzkou a na skutočných zariadeniach. Do podmienky dokončenia úlohy zahrň niekoľko signálov vrátane obchodného a nechaj kritika overiť, že ich systém odosiela.
- **Ticho potrebuje snímač zvonku.** Sondou preveruj kľúčový používateľský postup a daj používateľom možnosť nahlásiť zlyhanie do evidencie. Interná telemetria môže stíchnuť spolu so službou; samotný heartbeat nedokazuje, že služba obsluhuje používateľov.
- **Sprístupňuj zmenu postupne a riadene.** Oddeľ nasadenie od sprístupnenia. Ak vieš porovnať výstupy, spusti novú cestu v tieňovom behu ešte pred canary. Podiel používateľov zvyšuj postupne, v tieňovom behu vypni vedľajšie účinky a zvyšovanie podielu naviaž na automatické vrátenie zmeny.
- **Núdzový vypínač je zmena stavu.** Artefakt zostav raz a ten istý posúvaj cez predprodukčné prostredie do produkcie. Predchádzajúci artefakt uchovaj nezmenený, aby si pri vrátení nemusel nič znova zostavovať. Pri flotilách pozastav aj agentov.
- **Únik učí brány.** Produkčné signály aj potvrdené hlásenia od používateľov zapisuj do toho istého registra spolu s názvom brány, ktorá chybu nezachytila. Ak hlásenie predbehne všetky alerty, zaznamenaj aj chýbajúci signál.

**[Nové pojmy](../glossary.md#observability-rollout-and-the-kill-switch)**: produkcia ako koncová brána, sada telemetrických signálov, obchodný signál, oddelenie nasadenia od sprístupnenia, feature flag, postupné nasadzovanie (canary · zvyšovanie podielu), automatické vrátenie zmeny, núdzový vypínač, pozastavenie flotily, Telemetria ako podmienka dokončenia, Syntetická sonda zvonku (black-box probe), Alerting na príznaky (symptom-based alerting), Tieňové overovanie (shadow run), Posun artefaktu medzi prostrediami (build once), Hlásenie od používateľa (snímač poslednej záchrany).
