---
title: "Ako čítať dôkazy odboru"
sidebar_position: 3
---

# Ako čítať dôkazy odboru

Lekcia 1 oprela každé číslo o stupeň dôkazu — `MEASURED`, `REPORTED`, `ASSERTED` — bez toho, aby povedala, odkiaľ ten stupeň vzniká. Toto je lekcia, ktorá ti dáva samotný nástroj: rebrík dôkazov, ktorý potom nesieš do každej ďalšej lekcie kurzu. Prichádzaš s tvrdeniami, ktoré sú skreslené — nie preto, že by ti niekto klamal, ale preto, že sekundárna vrstva odboru posúva čísla oboma smermi, ako putujú z ruky do ruky. Nadšenci ich nafukujú jedným smerom, skeptici druhým, a číslo, ktoré prejde cez desať prerozprávaní, stráca presne to, čo ho robilo užitočným. Metóda proti tomu je malá a nič oslnivá: dôjsť k pôvodnému zdroju, ohodnotiť, čo tam skutočne je, a stupeň dôkazu povedať nahlas.

## Dôkaz má tri stupne, a sláva medzi nimi nerozhoduje

Celá disciplína stojí na tom, že tieto tri stupne držíš oddelene.

- **`MEASURED`** (namerané) — kontrolovaná štúdia, telemetria, dataset alebo reprodukovateľný benchmark efekt naozaj zmeral.
- **`REPORTED`** (hlásené) — menovaný praktik alebo firma dôveryhodne opisuje vlastnú skúsenosť. Tu žije väčšina odboru.
- **`ASSERTED`** (tvrdené) — názor, marketingová veta alebo argument bez akéhokoľvek podloženia.

Dve pravidlá držia rebrík čestný. Prvé: slávne meno stupeň nezvyšuje. Sláva nie je dôkaz — „Karpathy povedal“ je `ASSERTED`, kým nenájdeš, čo naozaj odmeral. Druhé: stupeň sa pri prerozprávaní nesmie zvyšovať. Tvrdenie, ktoré desaťkrát zopakoval veľký účet, je stále len tvrdenie. Stupeň povieš slovami, ktoré si zvolíš: „randomizovaný experiment zistil“, „praktici hlásia“, „jeden vplyvný príspevok tvrdí“. Tie tri formulácie nie sú ozdoba. Sú to stupne, vyslovené nahlas.

## Skôr než tomu uveríš, spýtaj sa na menovateľa, konflikt záujmov a dátum

Keď má tvrdenie stupeň, štyri kontroly rozhodnú, či číslo prežije stret so zdrojom.

Najprv menovateľ. Tá istá telemetria Googlu dáva **28,7 %** alebo **70,6 %** pre podiel kódu napísaného AI — líšia sa len v tom, či je kopírovanie v menovateli (`MEASURED`; Google tlačí obe čísla vedľa seba, na tých istých dátach). Každý titulok „X % kódu píše AI“ je voľba menovateľa, nie fakt. Pýtaj sa, čo je dole v zlomku, skôr než zopakuješ, čo je hore.

Potom konflikt záujmov — a povedz ho v texte, nie v poznámke pod čiarou. „Výskumníci GitHubu merajú produkt GitHubu“ je súčasť zistenia, nie okrajová poznámka. Za tým stojí štrukturálne pravidlo: kto nástroj predáva, ten ho nevie nezaujato zmerať. Firma, ktorá nemá čo predať, zvykne zverejniť práve to užitočné číslo — Meta vytlačila vlastných nelichotivých **19,7 %**; vendor tlačí to lichotivé.

Potom aktuálnosť. Živé číslo býva zastarané alebo stiahnuté, a aj tak koluje ďalej. Google potichu odvolal výhodu v prepínaní kontextu z roku 2022 — pre chýbajúcu štatistickú významnosť — a webové vyhľadávanie ho v roku 2026 aj tak zopakovalo ako fakt. METR-ovo „o 19 % pomalší“ je nahradené samotným METR. Číslo neprestane putovať len preto, že prestalo byť pravdivé.

A predovšetkým: choď k pôvodnému zdroju. Vo výskume pre tento kurz chybovali úryvky z vyhľadávania znova a znova — vymýšľali desatinné miesta, menili percentá na počty, pripisovali reálne čísla nesprávnej štúdii. Náprava nebola lepší úryvok. Bolo to otvoriť samotnú štúdiu.

## Percentuálny bod nie je percento

Jedna kontrola dáva kurzu právo učiť zvyšok — a je to práve tá, ktorú väčšina médií pokazí. Keď porozumenie klesne zo **67 %** na **50 %** (`MEASURED`), je to pokles o **17 percentuálnych bodov** — relatívne o štvrtinu — nie „o 17 % menej“. Chyba sebahodnotenia u METR je **40 percentuálnych bodov**, nie „40 %“. A relatívny nárast nie je podiel: „**+31,3 %** viac pull requestov sa zlúči bez revízie“ neznamená, že 31 % pull requestov ostáva bez revízie. Sú to dve rôzne veličiny. Pomýliť si ich je presne tá nedbalosť, proti ktorej táto lekcia stojí — pomýliš si to raz, a strácaš právo o téme učiť.

## Najcitovanejšie číslo žánru sa nedá overiť

Skús tie štyri kontroly na najcitovanejšom čísle žánru „AI škodí kvalite kódu“: duplicita blokov vraj vzrástla o **81 %** od roku 2023, kopírovanie z **9,4 %** na **15,7 %**. Číslo pochádza od GitClearu, vendora, ktorý predáva analýzu kvality kódu. Prejdi štyri kontroly a rozpadne sa ti v rukách. Autor nie je uvedený. Stránka nemá dátum. Korpus je súkromný, takže ho nikto zvonka nezreprodukuje. Metóda nie je opísaná, kontroly žiadne — a nosná chyba: nikde nie je uvedené, ktoré riadky naozaj napísala AI. Je to časový rad za obdobie, keď stúpalo osvojenie AI, nie porovnanie AI-kódu s kódom bez AI. Dokonca aj vlastné číslo rozsahu driftuje medzi vydaniami — 153 miliónov riadkov, potom 211 miliónov zmenených riadkov, potom 623 miliónov analyzovaných zmien, zakaždým iná jednotka. Nespájaj ich do jedného trendu.

Tu je jemný bod, a je to celá lekcia. Slabina GitClearu nie je, že ho niekto vyvrátil. Päť cielených vyhľadávaní nenašlo ani jednu vierohodnú metodologickú námietku — žiaden rozbor, žiadnu neúspešnú replikáciu, nič. Slabina je, že sa to nedá overiť. Nie je čo reprodukovať. Je to iné a tichšie zlyhanie než mýliť sa, a je bežnejšie.

Čestná verzia toho istého tvrdenia pritom prežíva. Jediný nezávislý kauzálny test — párovaná difference-in-differences štúdia z Carnegie Mellon (porovnanie vývoja liečenej a kontrolnej skupiny), 401 liečených repozitárov proti 606 kontrolným — dáva duplicitu **+7,92 %**, a nie je to štatisticky významné, v agent-prvých repozitároch; **−0,94 %**, tiež nevýznamné, v IDE-prvých. Silne významné sú naopak zložitosť (**+34,85 %**) a upozornenia statickej analýzy (**+17,73 %**). Takže „AI zhoršuje udržiavateľnosť“ platí — ale cez zložitosť, nie cez klony. Najcitovanejšie číslo žánru je to, ktoré sa nereplikuje; skutočné zistenie je to tiché vedľa neho. A stupeň: napriek všetkým tým desatinným miestam je GitClear `REPORTED`, nie `MEASURED` — časový rad za obdobie osvojenia nie je meranie účinku AI.

## Sekundárna vrstva skresľuje na obe strany

GitClear nie je výnimka, je to typ. Vo výskume pre tento kurz sa podobne rozpadlo šesť ďalších tvrdení — a bod nikdy nie je „títo ľudia klamú“. Je to prežitie, nie veda. Presne preto kurz chodí k pôvodným zdrojom.

1. Pipeline, ktorý sa pri rozbore ukázal byť len diagramom — proces nakreslený ako slučka so spätnou väzbou, ktorá v skutočnosti nemala žiadnu spätnú hranu.
2. „Kompilátor špecifikácií“, ktorý je v skutočnosti systémovým promptom na 70 KB. Za produktom stojí repozitár bez kódu — štyri textové súbory — a „kompilátor“ je len prompt, ktorý káže chatbotu tvrdiť, že je kompilátor. Vynucovanie zdvorilosťou.
3. Vlna CVE pripísaná jednému AI-nástroju — „27 na účet Claude Code“ — čo pri rozbore meria iba to, ktorý nástroj podpisuje svoje commity. Claude Code podpisuje predvolene, väčšina nástrojov nie. Číslo počíta odtlačky prstov, nie chyby.
4. Najcitovanejšia maxima odboru — „myslenie môžeš outsourcovať, porozumenie nie“ — pripísaná Karpathymu, ktorý sa výslovne odvoláva na tweet, čo sa mu páčil, a autorstvo si nikdy nenárokuje. Pripísať mu ju je presne to zlyhanie z tretej ruky, ktorému táto lekcia bráni.
5. Odvolané číslo Googlu — stiahnuté v roku 2022 pre chýbajúcu štatistickú významnosť — a v roku 2026 vrátené ako aktuálny fakt živým webovým vyhľadávaním.
6. „97,9 %“ od OpenAI — reťazec, ktorý sa nenachádza ani v štúdii, ani v blogu, na ktoré sa odvoláva. Niet za ním vety a menovateľ sa cestou zmenil z „aktívnych pracovníkov“ na „zamestnancov“.

Šesť rôznych zlyhaní, no nie jeden mechanizmus. Štyri z nich sú skreslené tvrdenie, ktoré sa opakuje, kým nevyzerá ako odkaz na štúdiu. Zvyšné dve — diagram bez spätnej väzby a prompt vydávaný za kompilátor — sú artefakt s nesprávnym menom, nie skreslené tvrdenie. Každý z týchto bodov by prežil sebavedomé spísanie. Ani jeden neprežil prečítanie pôvodného zdroja.

:::tip[▶ Video]

<YouTube id="-dAmqHFWzyg" title="Top 5 AI Myths — IBM Technology" />

IBM v krátkom videu prechádza päť „všeobecne známych“ tvrdení o AI, ktoré neprežijú pozorný pohľad — presne ten istý reflex, aký táto lekcia cvičí, len o pole vedľa. (Video je v angličtine.)

:::

## Niekoľko čísel, ktoré si možno už nosíš

Zopár skreslených tvrdení je bežných natoľko, že sa oplatí pomenovať ich a odložiť.

Číslo „**441,5 %** viac času na revíziu“ je od Faros AI, nie od DORA — a vedľa neho stojace „**+31,3 %**“ je relatívny nárast podielu pull requestov bez revízie, nie 31-percentný podiel.

„Stanfordská štúdia 100 000 vývojárov“ nemá publikovaný článok. Čísla kolujú cez prednášky a slajdy, metóda nie je zverejnená. Cituj ju, ak vôbec, ako „stanfordská skupina hlási — v prednáškach, nie v publikovanom článku“.

„Copilot zrýchli vývojárov o 55 %“ — to sú výskumníci GitHubu, na produkte GitHubu, na jednej hračkárskej úlohe o HTTP serveri, z roku 2023. Marketingový artefakt, nie zistenie o tvojej práci.

„Schopnosti AI sa zdvojnásobia každých 7 mesiacov“ je zaokrúhlenie vlastného fitu METR — **207 dní** — a revízia METR z roku 2026 dáva nedávne tempo **131 dní**. Je to regresia cez dvanásť modelov na úlohách, ktoré METR sám nazýva „nenáročné na trest“ a „statické“. Cituj ten fit; necituj ho ako zákon.

## Zistenie povieš čestne, len keď mu pridáš populáciu a proxy

Zlyhanie je na oboch stranách rovnaké: reálne číslo, zbavené svojej populácie a svojho proxy. Náprava je tvar vety. Povedz číslo, a potom pridaj to, čo prerozprávanie zvyčajne zahodí — na kom sa meralo, aké proxy zastupovalo hodnotu, kto platil, a či je to ešte aktuálne. Napríklad: „Naprieč desiatkami tisíc inžinierov Microsoftu, porovnávaných každý sám so sebou, prinieslo osvojenie CLI agenta približne o 24 % viac zlúčených pull requestov za štyri mesiace — a zlúčený pull request nie je tá hodnota, ktorú prináša.“ Jedna veta, a nesie číslo, populáciu, proxy aj konflikt záujmov naraz.

Z tohto tvaru vyplýva päť pravidiel. Nikdy neuvádzaj číslo produktivity bez jeho proxy a populácie. Percentuálne body drž oddelene od percent. Konflikt záujmov pomenuj priamo v texte. Keď sa zdroj sám zrieka vlastného výsledku, začni práve tým. A uprednostni zistenie, ktoré je nevýhodné pre toho, kto ho zverejnil — Anthropic zverejňuje náklad vlastného nástroja, OpenAI sťahuje vlastný benchmark. Výsledok, ktorý škodí záujmu vlastného autora, je najsilnejší dôkaz, aký môže odbor plný konfliktov záujmov ponúknuť.

## Tri úrovne zrelosti: soloista · malý tím · enterprise

Hodnotenie dôkazov je univerzálna zručnosť; menia sa len stávky.

- **Soloista.** Mechanizmus je osobný návyk: skôr než začneš konať podľa čísla, dovedieš ho k pôvodnému zdroju. Čomu to bráni: premrhať víkend stavaním na čísle, ktoré sa rozsype, len čo otvoríš zdroj.
- **Malý tím.** Mechanizmus je otázka „odkiaľ to vieme?“ ako stály zvyk revízie návrhu — a odkazy na pôvodné zdroje v rozhodovacom dokumente, nie na blogy vendorov. Čomu to bráni: tímovému štandardu, voľbe frameworku alebo politike testovania, postavenej na čísle, ktoré nikto nepreveril.
- **Enterprise.** Mechanizmus je latka dôkazu pre rozhodnutia o nástrojoch — obstarávanie číta pôvodné zdroje, nie prezentácie vendorov. Čomu to bráni: nastaviť politiku pre tisíce ľudí podľa zle prečítanej štúdie. Tu platí to, čo si kurz opakuje najčastejšie: čím ďalej je rozhodnutie od samotnej práce, tým viac sa zlé prečítanie stáva dôkazom, na ktorý sa spoliehajú ostatní. Len čo sa „štúdia hovorí X“ dostane do štandardu, každý nižšie v procese zdedí chybu bez toho, aby zdroj kedy videl.

## Čo si odniesť z lekcie

- Ohodnoť každé tvrdenie — `MEASURED`, `REPORTED`, `ASSERTED` — a pri prerozprávaní stupeň nezvyšuj. Sláva nie je dôkaz.
- Čítaj na menovateľa, konflikt záujmov a aktuálnosť čísla; a keď máš pochybnosť, otvor pôvodný zdroj. Úryvky z vyhľadávania chybovali znova a znova. Štúdie nie.
- Percentuálne body nie sú percentá a relatívny nárast nie je podiel. Pomýliš si to a strácaš právo o téme učiť.
- Najcitovanejšie číslo žánru býva to, ktoré sa nedá overiť, nie to, ktoré je dokázané. Tvrdenie GitClearu o duplicite sa nereplikuje; čestné zistenie — udržiavateľnosť klesá cez zložitosť, nie cez klony — stojí ticho vedľa.
- Zistenie formuluj s jeho populáciou, proxy, konfliktom záujmov a aktuálnosťou. Uprednostni výsledok, ktorý je nevýhodný pre toho, kto ho zverejnil.

**Nové termíny:** stupeň dôkazu (rebrík `MEASURED` / `REPORTED` / `ASSERTED`), konflikt záujmov uvedený priamo, zistenie nevýhodné pre toho, kto ho zverejnil, cesta k pôvodnému zdroju.

---

Rebrík — `MEASURED` / `REPORTED` / `ASSERTED` — je nástroj, ktorý Lekcia 1 už použila a odteraz ho nesieš do každej ďalšej. Tá istá disciplína, dôjsť k pôvodnému zdroju namiesto sekundárneho prerozprávania, sa v Lekcii 3 vracia pri číslach, ktoré si o sebe hlásia priamo samotné AI-laby.
