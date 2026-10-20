---
title: "Atomárne úlohy: dekompozícia ako nástroj kontroly"
sidebar_position: 2
---

# Jednotka dekompozície je jednotkou kontroly

[Prvá lekcia](./vision-to-stages.md) dala každej etape podmienku dokončenia, ktorú si môžeš overiť. Táto lekcia sa venuje *veľkosti* etapy — a veľkosť nie je otázkou úhľadnosti. Agenta dokážeš kontrolovať len s takou podrobnosťou, s akou rozdelíš prácu. Ak úlohu nemožno overiť na jedno prečítanie, už si nad ňou stratil kontrolu. Nie preto, že ju agent určite nezvládne, ale preto, že nedokážeš zistiť, či ju zvládol. Atomicita určuje rozpočet na overovanie; nie je len otázkou poriadkumilovnosti.

## Dekompozícia je kontrola

Čím je jednotka menšia, tým dôkladnejšiu kontrolu okolo nej môžeš vytvoriť. Trojriadkovú zmenu si dokážeš prečítať celú a uistiť sa o jej správnosti; pri tisícriadkovej zmene môžeš iba namátkovo skontrolovať niekoľko miest a dúfať. Medzi týmito krajnosťami sa kontrola oslabuje plynulo: každý riadok, ktorý nedokážeš udržať v hlave, je riadok, ktorému dôveruješ namiesto toho, aby si ho skontroloval. Každá hranica medzi jednotkami je miestom, kde sa môžeš zastaviť a výsledok overiť. Počet hraníc preto určuje, koľkokrát môžeš zachytiť problém skôr, než sa prenesie do ďalšej jednotky a ešte sa zhorší. Spôsob, akým prácu rozdelíš, teda *určuje*, koľko kontroly si nad ňou zachováš. Kontrolu, ktorej sa vzdáš pri dekompozícii, už v ďalších krokoch nezískaš späť.

## Správna veľkosť má dolnú aj hornú hranicu

Ak zvolíš príliš veľkú jednotku, podmienka dokončenia sa rozostrí: jednotku nedokážeš overiť na jeden raz, takže „hotovo“ sa opäť zmení na „vyzerá to ako hotové“. To je pasca kontroly založenej na úsudku, pred ktorou varovala Prvá lekcia. Ak prácu rozdelíš na príliš malé jednotky, objavia sa iné náklady: každá drobná jednotka stále potrebuje vlastné zadanie, vlastný výsek kontextu aj samostatné odovzdanie výsledku. Od určitého bodu stojí koordinácia častí viac, než sa ich rozdelením ušetrí. Ideál leží medzi týmito krajnosťami: **najväčšia jednotka, ktorú ešte dokážeš overiť na jedno prečítanie.** Do každej hranice vlož čo najviac práce, no neprekroč množstvo, ktoré vieš skutočne skontrolovať. To je celá optimalizácia.

## Príliš jemná dekompozícia je samostatný spôsob zlyhania

Po nepríjemnom prekvapení máme sklon deliť prácu čoraz jemnejšie, akoby menšie jednotky boli vždy bezpečnejšie. Nie sú — a náklady takéhoto prístupu sú zmerané. Keď ETH Zurich [poskytol agentom viac písomného kontextu ku každej úlohe, dodatočné artefakty výsledkom *uškodili*](https://arxiv.org/abs/2602.11988): úspešnosť klesla a náklady na jeden krok vzrástli o viac než 20%, pretože agent prejavoval nadmernú poslušnosť a dôkladne, no zbytočne dodržiaval všetko, čo dostal. Jemnejšia dekompozícia vedie presne týmto smerom: viac jednotiek znamená viac zadaní, viac kontextu opakovane posielaného pri každom kroku a viac artefaktov, ktorých vzájomný súlad treba udržiavať. Takto sa zadnými dverami pod heslom „jednoducho to rozdeľ ešte viac“ vracia typické zlyhanie z Časti II — **zahltenie artefaktmi**. Krivka nákladov má svoje minimum. Nájdi ho; nesnaž sa dostať na nulu.

## Niekto musí udržať celok

Aj po rozdelení práce musia jednotlivé časti vytvoriť jeden celok a niekto musí mať naďalej prehľad o celku, kým sa časti dokončujú. Osvedčený model vyzerá takto: orchestrátor udržiava plán a kontext, zatiaľ čo dočasní vykonávatelia dostanú vždy jednu atomárnu úlohu, splnia ju a namiesto celého záznamu svojej práce vrátia skrátený výsledok. Anthropic, predajca modelu, nameral, že jeho [multiagentový výskumný systém prekonal jedného agenta o 90,2%](https://www.anthropic.com/engineering/multi-agent-research-system) vo vlastnom internom výskumnom teste. Zároveň však upozorňuje, že programovanie sa paralelizuje omnoho ťažšie, takže tento údaj naň nemožno preniesť. Všímaj si štruktúru, nie číslo: úlohou orchestrátora *je* overovanie. Uchováva podmienky dokončenia a porovnáva s nimi každý vrátený výsledok. Vykonávatelia tvoria; orchestrátor rozhoduje, čo sa považuje za dokončené.

Takto dostáva overiteľná etapa z Prvej lekcie správnu veľkosť. Etapa je atomárna, keď ju dokážeš overiť na jeden raz — je dosť malá na to, aby bola kontrola skutočná, a dosť veľká na to, aby hranica opodstatnila svoje režijné náklady. Ak ju zväčšíš, stratíš overiteľnosť; ak ju zmenšíš, zaplatíš za zahltenie. Túto hranicu stanovuješ pri dekompozícii a práve vtedy ju ešte môžeš stanoviť lacno.

## Každým rozdelením vzniká styčné miesto

Keď prácu rozdelíš, jednotlivé časti sa kontrolujú ľahšie, no musíš preveriť aj to, ako spolu fungujú. Každý vykonávateľ vidí iba svoj kontext a orchestrátor porovnáva každý výsledok s podmienkou dokončenia danej úlohy. Ani jedna z týchto kontrol však neoveruje vzťah medzi dvoma jednotkami. **Styčné miesto (seam)** je spojenie medzi jednotkami, na ktorom musia byť zladené moduly, kontrakty, dáta alebo používateľské scenáre. Pri každom rozdelení preto počítaj aj s kontrolou každého nového styčného miesta.

[Andrej Beloborodov](https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/) zo svojej praxe uvádza, že práve na styčných miestach vzniká najviac chýb v prevádzke, lebo agent vidí len obmedzený kontext. Kontraktové testy a parity/golden testy uprednostňuje pred kontrolami samotnej upravovanej časti. End-to-end scenárov (E2E) ponecháva málo, pretože sú pre AI náročné. Odporúčanie tohto kurzu: obmedz E2E testy na kritické používateľské cesty.

Kontrolu vyber podľa toho, čo sa má na styčnom mieste zachovať:

- **Na hranici služby alebo tímu** použi [kontraktový test riadený konzumentom](https://martinfowler.com/articles/consumerDrivenContracts.html) (consumer-driven contract test). Očakávania každého konzumenta sa premietnu do kontrol spúšťaných pri každom builde poskytovateľa. Zmena, ktorá by konzumentovi niečo pokazila, zastaví build poskytovateľa ešte pred nasadením.
- **Pri refaktoringu** použi [charakterizačný test](https://en.wikipedia.org/wiki/Characterization_test) (characterization test, golden master). Zaznamená dnešné správanie a porovná s ním neskoršie výstupy. Zachytáva, čo kód robí, nie čo by robiť mal. Správnosť teda nie je zaručená, preto o prijateľnosti zistenej zmeny rozhoduje človek.

Pre používateľa je to obyčajná regresia: po zmene prestane fungovať niečo, čo predtým fungovalo. Beloborodov v [opise regresií](https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/) pripisuje regresie lokálnym opravám, ktoré menia spoločné komponenty, API kontrakty alebo dátové štruktúry bez ohľadu na súvisiace scenáre. Uvádza štyri obrany proti regresii:

- **Dokumentácia** — pred zmenou zapíš, ako sa existujúci kód používa a aké kontrakty plní.
- **Direktíva** — prepisovanie funkčného kódu alebo zmena používaného kontraktu vyžaduje samostatné rozhodnutie.
- **Oddelenie rolí** — nezávislý kritik overí, či zmena zasahuje do už vytvoreného kódu a či tento kód zostáva funkčný.
- **Testy** — overuj aj susednú funkcionalitu a fungujúce scenáre, nielen upravenú časť.

V členení tohto kurzu sú prvé tri obrany založené na úsudku: závisia od toho, čo si agent prečíta a čo posúdi kontrolór. Testy poskytujú výpočtovú kontrolu. Z direktívy sa stane výpočtová kontrola až [vynútením](../part-1-foundation/rules-that-hold.md), napríklad hookom alebo pravidlom v CI, ktoré zablokuje neschválenú úpravu kontraktu.

:::tip[▶ Video]

<YouTube id="kYkZI3oj2W4" title="Multi AI Agent Systems: When One AI Brain Isn't Enough — IBM Technology" />

IBM ukazuje rozdelenie medzi orchestrátora a vykonávateľov ako architektúru. Porovnaj ho s varovaním v tejto lekcii: rovnaké rozdelenie, ktoré ti umožňuje overovať jednotlivé časti, zároveň prináša náklady na koordináciu. Preto ich porovnaj s použitím jediného agenta, ktorého celý výstup by si ešte dokázal skontrolovať sám.

:::

## Tri úrovne zrelosti: soloista · malý tím · enterprise

Na každej úrovni platí rovnaké pravidlo: **prácu dokážeš kontrolovať len s takou podrobnosťou, s akou ju dekomponuješ.** Mení sa len to, čo tvorí hranicu.

- **Soloista.** Rozdeľ prácu na časti, ktoré dokážeš prečítať naraz; hranicou je tvoja vlastná pozornosť. Vypíš si styčné miesta, ktoré rozdelením vytvoríš, a každému priraď kontrolu. *Akému zlyhaniu to predchádza:* zmena je príliš veľká na kontrolu, no napriek tomu ju schváliš, pretože opätovné čítanie by už vyžadovalo viac práce než dôvera.
- **Malý tím.** Dohodni si hranice úloh vopred a každej jednotke urč vlastníka; hranicou je pull request, ktorý možno reálne skontrolovať. Tam, kde sa práca odovzdáva medzi vlastníkmi, pridaj kontraktové testy. *Akému zlyhaniu to predchádza:* veľkosť jednotky sa riadi sebadôverou autora a na kontrolu sa dostane zmena, ktorú v skutočnosti nikto nedokáže preveriť.
- **Enterprise.** Dekompozícia sa stáva súčasťou pipeline — veľkosť jednotiek sa prispôsobuje nezávislej kontrole a auditu, nie pohodliu. Kontraktové testy umožňujú kontrolu naprieč tímami: žiadny tím nevidí obe strany, no každý môže svoju časť overiť podľa rovnakého kontraktu. *Akému zlyhaniu to predchádza:* práca sa zoskupí do takých veľkých balíkov, že preukázateľne nezávislá kontrola sa zmení na formálne odklepnutie.

## Čo si z toho odniesť

- Prácu dokážeš kontrolovať len s takou podrobnosťou, s akou ju dekomponuješ. Jednotka, ktorú nemožno overiť na jedno prečítanie, predstavuje kontrolu, ktorú si už stratil. Dekompozícia je posledným miestom, kde si ju ešte môžeš lacno zachovať.
- Veľkosť prispôsob kontrole: zvoľ najväčšiu jednotku, ktorú ešte dokážeš overiť na jeden raz. Pri väčšej sa stav „hotovo“ zakladá len na úsudku; pri menšej režijné náklady na koordináciu pohltia samotnú prácu.
- Príliš jemná dekompozícia je skutočné zlyhanie, nie bezpečná predvolená voľba. Viac jednotiek znamená viac zadaní, viac opakovane posielaného kontextu a viac artefaktov, ktorých súlad treba udržiavať — odtiaľ pochádza zmeraný nárast nákladov na krok o viac než 20%. Krivka nákladov má svoje minimum.
- Keď prácu rozdelíš, nechaj plán a podmienky dokončenia u orchestrátora, zatiaľ čo dočasní vykonávatelia mu vracajú skrátené výsledky. Úlohou orchestrátora je overovať, nie tvoriť.
- Pri rozdelení práce počítaj s kontrolou každého styčného miesta; podmienky dokončenia jednotlivých jednotiek vzťahy medzi nimi nepokrývajú. Kontraktové testy preveria spoločné očakávania, charakterizačné testy doterajšie správanie a E2E testy kritických ciest overia, že spojené časti spolu fungujú.

**[Nové pojmy](../glossary.md#atomic-tasks)**: atomárna úloha, dekompozícia ako nástroj kontroly, príliš jemná dekompozícia, orchestrátor a dočasní vykonávatelia, styčné miesto, kontraktový test riadený konzumentom, charakterizačný test, štyri obrany proti regresii.
