---
title: "Erózia architektúry"
sidebar_position: 2.5
---

# Aj séria rozumných opráv môže rozobrať architektúru

Predchádzajúca lekcia [Kontrola driftu a zastarávanie pravidiel](./drift-and-rot.md) sa venovala pravidlám a pamäti projektu, ktoré prestávajú zodpovedať systému. Tu sa problém obracia: rozhodnutia môžu stále platiť, ale kód ich prestáva dodržiavať. Agent vyrieši aktuálny problém, oprava prejde kontrolami a pritom sa potichu stratí ďalšia hranica medzi časťami systému.

Perry a Wolf už v roku 1992 [rozlíšili dva javy](https://users.ece.utexas.edu/~perry/work/papers/swa-sen.pdf). **Architektonický drift (architectural drift)** nastáva, keď kód na architektúru neberie ohľad; **erózia architektúry (architecture erosion)**, keď ju porušuje. Na tomto rozlíšení záleží, pretože drift pripravuje pôdu pre eróziu: architektúra stráca súdržnosť, v kóde ju horšie rozoznáš a pri ďalšej zmene sa ľahšie poruší. Pojem architektonický drift tu znamená niečo iné než drift a zastarávanie pravidiel z predchádzajúcej lekcie.

Pri práci s agentmi ber architektonický drift ako samozrejmosť. Agent rieši lokálnu úlohu s kontextom, ktorý práve má. Ak má zachovať aj usporiadanie celého systému, potrebuješ na to osobitný mechanizmus.

Prepoj rozhodnutia s kódom troma spôsobmi: pri každej oprave vychádzaj z denníka rozhodnutí, štrukturálne obmedzenia over automatickými kontrolami a dohodni, kedy séria opráv vyžaduje prepracovanie návrhu. Keď rozhodnutie zmeníš, pôvodné ponechaj v denníku a označ ho ako nahradené. Ďalší čitateľ tak nebude pokladať staré rozhodnutie za platné pravidlo.

## Erózia sa začína drobnou opravou

Andrej Beloborodov [píše o tom, ako pri vývoji vlastných projektov stavia od začiatku na AI](https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/). Podľa jeho skúsenosti sa v projekte postupne menili pravidlá bez toho, aby niekto rozhodol o zmene architektúry. Objavovali sa duplicity, rovnaké situácie sa riešili rôzne a oprava pokazila susednú funkciu. Je to skúsenosť jedného človeka s vlastnými projektmi, nie merané porovnanie vývojových metód.

Beloborodov za najľahšiu cestu k takému výsledku označuje malé opravy. Každá môže pôsobiť taká neškodná, že pri nej agent vynechá kontrolu architektúry; po čase však podľa Beloborodova vznikne iný návrh. V Beloborodovovom príklade jeden agent zmení kontrakt, druhý vytvorí paralelnú implementáciu a tretí výsledné provizórne riešenie zdokumentuje. Každý krok pritom môže sám osebe pôsobiť ako výsledok starostlivej práce.

Predstav si vymyslený príklad: modul fakturácie rozhoduje, či sú splnené podmienky na vystavenie faktúry, a modul notifikácií používa jeho výsledok. Agent rieši chybu, pre ktorú neodišiel e-mail. Skopíruje kontrolu podmienok do notifikácií a konkrétny prípad začne fungovať. Pri neskoršej zmene fakturácie sa upraví iba pôvodná kontrola, preto ďalší agent pridá výnimku do kópie v notifikáciách. Opravy tak presunuli zodpovednosť za rozhodnutie inam, hoci to nikto nenavrhol.

Samotná potreba ďalšej opravy ešte neznamená problém s architektúrou a netýka sa iba agentov. Park, Kim, Ray a Bae v roku 2012 [skúmali dodatočné opravy chýb](https://web.cs.ucla.edu/~miryung/Publications/msr2012-supplementarypatch.pdf) v projektoch Eclipse JDT core, Eclipse SWT a Mozilla. Zistili, že 22–33% vyriešených chýb si vyžiadalo viac než jeden pokus o opravu. Len malá časť dodatočných opráv sa podobala pôvodnej oprave. V oboch projektoch Eclipse sa 14–15% súborov z dodatočných opráv ani neprekrývalo so súbormi pôvodnej opravy, ani od nich priamo nezáviselo.

Jedna nadväzujúca oprava je teda bežná aj pri vývoji ľuďmi. Varovným signálom je až séria opráv v tej istej oblasti. Vtedy zmapuj aj súvislosti, ktoré v prvom diffe nevidíš.

:::tip[▶ Video]

<YouTube id="FgaBdwSvOGM" title="Agentic Engineering vs Software Engineering: Beyond Vibe Coding — IBM Technology" />

Anna Gutowska vo videu IBM Technology vysvetľuje, že agentné systémy môžu pôsobiť správne, a pritom prijímať chybné rozhodnutia vrátane zlých architektonických riešení. Za úzke miesto považuje to, ako na prácu agenta dohliadať, určiť jej hranice a vyhodnotiť ju. Práve to v opísanej sérii drobných opráv chýba.

:::

## Najprv rozhodnutie, potom zmena: denník, z ktorého vychádza každá oprava

Beloborodov v [opise riadenia architektúry ako dynamického systému](https://realaillusions.com/ru/materials/sovety_ai_praktika_part3/) uvádza, že jeho projekt narástol na rozsah, ktorý prirovnáva k práci malého tímu 10–20 ľudí. Architektúru mal opísanú, no zmeny a opravy ju podľa jeho slov postupne narúšali.

Zaviedol preto **denník architektonických rozhodnutí (ADR log)**: súbor v repozitári, na ktorý odkazovali nastavenia každého agenta. Jednotlivé rozhodnutie malo podobu **záznamu architektonického rozhodnutia (architecture decision record, ADR)**. Agenti podľa jeho opisu čítali denník pri príprave ďalšieho zadania aj pred každou zmenou či opravou chyby. Jeden programovací agent bol podľa neho obzvlášť náchylný pridávať pri týchto zásahoch navzájom protichodné provizórne riešenia.

Beloborodov uvádza, že po zavedení denníka bolo výnimiek aj chybných programátorských rozhodnutí niekoľkonásobne menej; konkrétne číslo neuvádza. Podľa jeho opisu sa zlepšili aj riešenia úloh, ktoré zasahovali do viacerých blokov. Priznáva, že agentom pribudla práca, no tvrdí, že záťaž je menšia, než by sa mohlo zdať. Prevezmi tento mechanizmus, no jeho účinok si na vlastnom projekte zmeraj sám.

Beloborodovovo pravidlo znie: **rozhodnutie pred zmenou (decision before change)**. Najprv zaznamenať architektonické rozhodnutie a až potom upraviť systém tak, aby mu zodpovedal. Na to podľa neho treba spoločné pracovné artefakty: mapu systému, hranice modulov, kontrakty a prijaté rozhodnutia. Odporúča aj nezávislého kritika, oddeleného od agenta, ktorý riešenie vytvára. Kritik má posudzovať smer celého riešenia vrátane jeho biznisového zmyslu. Súčasťou Beloborodovových odporúčaní je pravidelný organizačný audit: nevznikli paralelné riešenia a nezmenili nahromadené opravy smer projektu?

Na záznamy použi [vzor Michaela Nygarda z roku 2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), ktorý už predstavila lekcia [Príprava je dôležitejšia než model](../part-1-foundation/preparation-over-model.md). Obsahuje polia `Title`, `Context`, `Decision`, `Status` a `Consequences`. V `Context` zachyť okolnosti a vplyvy, ktoré viedli k voľbe; v `Consequences` situáciu, ktorú voľba vytvorí.

Rozhodnutia čísluj postupne, čísla znovu nepoužívaj ani záznamy neprečíslovávaj. V Nygardovom vzore rozhodnutie prechádza zo stavu `proposed` do `accepted`, neskôr môže byť `deprecated` alebo `superseded`. **Nahradený záznam ADR (superseded ADR)** nechaj v denníku, označ ho stavom `superseded` a pridaj odkaz na náhradu. Tým denník rieši drift pamäti: neskorší agent rozlíši historický záznam od rozhodnutia, ktoré má dodržiavať teraz.

V každom zadaní opravy vyžaduj čísla príslušných ADR a výslovné posúdenie, či je s nimi navrhovaná oprava v súlade. Ak oprava vyžaduje porušenie prijatého rozhodnutia, zastav implementáciu a z výnimky urob návrh nového ADR, ktoré pôvodné nahradí. Každej oblasti rozhodovania prideľ vlastníka. Ten návrh prijme alebo zamietne ešte pred vykonaním štrukturálnej zmeny.

Kritikovi daj okrem diffu aj denník prijatých rozhodnutí. V príklade s fakturáciou nestačí overiť, že e-mail opäť odchádza. Kritik musí skontrolovať aj to, či notifikácie neprevzali zodpovednosť fakturácie. Takto sa slučka [Plán, kontrola, implementácia, kritik](../part-2-loop/plan-review-implement-critic.md) uplatní aj na súlad štruktúry s rozhodnutiami.

Denník dopĺňaj postupne: v jednom čase doň smie zapisovať iba jeden agent. Rovnako postupuj aj pri ostatných postupne dopĺňaných artefaktoch podľa lekcie [Flotily agentov: izolácia a paralelizmus](./agent-fleets.md). Dvaja paralelne pracujúci agenti nesmú každý zapísať vlastnú verziu toho istého rozhodnutia.

## Architektúra ako vykonateľné obmedzenia

ADR vysvetľuje, prečo hranica existuje. **Fitness funkcia (fitness function)** kontroluje, či vybraná architektonická vlastnosť naďalej platí.

[Thoughtworks Technology Radar](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function) vychádza z knihy *Building Evolutionary Architectures*, ktorej autormi sú Neal Ford, Rebecca Parsons a Patrick Kua. Fitness funkciu opisuje ako mechanizmus objektívneho hodnotenia architektonickej integrity. Fitness funkciou môže byť aj existujúci test, metrika alebo monitor. Podstatné je priebežne kontrolovať vybrané vlastnosti počas zmien systému.

Birgitta Böckeler v [texte o harness engineeringu](https://martinfowler.com/articles/harness-engineering.html) opisuje architektonický fitness harness: vodidlá a snímače, ktoré určujú a kontrolujú architektonické vlastnosti aplikácie. Ako príklad uvádza pre-commit hook alebo hook programovacieho agenta, ktorý spustí kontroly ArchUnit hľadajúce porušenia hraníc modulov.

Je to uplatnenie lekcie [Pravidlá, ktoré platia](../part-1-foundation/rules-that-hold.md) na štruktúru kódu. Z požiadavky „rešpektuj hranice modulov“ urob kontrolu, ktorá pri zakázanej závislosti neprejde.

Hranice vyberaj zámerne. Perry a Wolf prirovnávajú architektúru k budove: nosné steny majú inú úlohu než dekorácia. Niektoré zmeny poškodia práve štruktúru, vďaka ktorej systém funguje. Vo vymyslenej objednávkovej aplikácii napríklad balík `orders` nesmie importovať `ui`, pretože doménové rozhodnutia majú zostať nezávislé od prezentácie. Takú hranicu má zmysel strážiť kontrolou. Ak však zafixuješ aj rozloženie balíkov, ktoré vzniklo len náhodou, bežná reorganizácia vyvolá spor o pravidlá. Do kontroly zakóduj závislosť, v ktorej sa rozhodnutie prejavuje; zdôvodnenie uchovaj v ADR.

**Pravidlo závislostí / kontrakt importov (dependency rule / import contract)** je vykonateľné pravidlo určujúce, ktoré moduly smú závisieť od ktorých. Kontrolný nástroj si vyber podľa jazyka:

- [ArchUnit](https://www.archunit.org/userguide/html/000_Index.html) podľa dokumentácie kontroluje architektúru v Jave cez bežné frameworky na jednotkové testy. Vie overovať napríklad povolené prístupy medzi vrstvami či cykly medzi časťami systému (slices).
- [Import Linter](https://import-linter.readthedocs.io/en/stable/) kontroluje kontrakty importov v Pythone: zakázané závislosti, chránené moduly, vrstvy aj nezávislosť. Kontrakty sú v konfigurácii a overuje ich príkaz `lint-imports`.
- [dependency-cruiser](https://github.com/sverweij/dependency-cruiser) podľa dokumentácie overuje závislosti JavaScriptu a TypeScriptu voči zadaným pravidlám a hlási porušenia pri zostavení. Pri nastavení cez `--init` pridáva aj pravidlá pre kruhové závislosti.

Bránu môžeš zaviesť aj bez toho, aby si najprv upratal celý narušený systém. ArchUnit dokumentuje `FreezingArchRule`: pri prvom spustení uloží existujúce porušenia ako východiskový stav a potom hlási nové. Opravené porušenia z uloženého stavu vypadnú, takže sa nemôžu nepozorovane vrátiť. Tieto **zmrazené porušenia (frozen violations)** použi na jednosmerné sprísňovanie: zaznamenaj súčasný stav, zabráň ďalšej erózii a staré porušenia odstraňuj pri zámerných úpravách. Agentovi, ktorý opravuje kód, nedovoľ meniť uložený východiskový stav.

Na doslovne opakovaný kód slúži **kontrola duplicít (duplication gate)**, napríklad [jscpd](https://github.com/kucherenko/jscpd). Jeho parameter `--threshold` určuje povolenú mieru duplicity v celom strome. Dokumentácia jscpd uvádza, že Super-Linter a MegaLinter ho predvolene spúšťajú s prahom `0`: zostavenie tak neprejde pri akejkoľvek duplicite. Nulová tolerancia sa dá obhájiť, ale zaveď ju vedome. Pravidlá hraníc nenahradí.

Klony kódu navyše nesmú byť jediným signálom udržiavateľnosti. Ako vysvetľuje lekcia [Ako posudzovať dôkazy](../part-1-foundation/reading-the-evidence.md), často opakované tvrdenie GitClear o duplicite sa nedá overiť: chýba metodika aj priradenie jednotlivých riadkov k AI. [Štúdia Carnegie Mellon s metódou rozdielov v rozdieloch](https://arxiv.org/abs/2601.13597) zistila, že pri vývoji vedenom agentmi nebola zmena duplicity štatisticky významná. Zložitosť a počet upozornení statickej analýzy však štatisticky významne vzrástli. Zaveď kontroly aj na ne; kopírovanie kódu je len jeden z viacerých príznakov.

## Ktoré princípy dokáže skontrolovať stroj

Beloborodov vo svojich praktických odporúčaniach radí pomenovať YAGNI, KISS, SRP a DRY výslovne. Všeobecný pokyn „dodržiavaj osvedčené postupy“ podľa neho spoľahlivo neprináša to, čo potrebuje. Pod YAGNI rozumie vynechanie nevyžiadaných abstrakcií, pod KISS hľadanie najjednoduchšej implementácie, pod SRP sústredenie funkcie na jednu zodpovednosť a pod DRY opätovné použitie existujúcej logiky. Zároveň varuje pred vložením všetkých pravidiel do konfigurácie naraz. Jeho postup je opačný: zlý výsledok, rozbor príčiny a až potom pravidlo zacielené na túto chybu.

Tieto štyri princípy sa nedajú overovať automatickými kontrolami rovnakým spôsobom. Pri návrhu harnessu oddeľ strojové kontroly a zástupné ukazovatele od úsudkov, ktoré zostávajú kritikovi:

| Princíp | Čo dokáže skontrolovať stroj | Otázka pre kritika |
|---|---|---|
| DRY | Doslovné kópie kódu prekračujúce zvolený prah duplicity. | Neopakuje inak napísaný kód to isté biznisové rozhodnutie? |
| SRP | Dĺžku, cyklomatickú zložitosť a počet závislostí ako zástupné ukazovatele. | Má táto jednotka ucelenú zodpovednosť? |
| KISS | Presne vymedzené pravidlo, napríklad zákaz novej závislosti. | Dá sa požadované správanie zachovať jednoduchšie? |
| YAGNI | Novú abstrakciu s jedinou implementáciou ako podnet na posúdenie. | Odôvodňuje túto abstrakciu niektorá súčasná požiadavka? |

Jediná implementácia je dôvod na otázku, sama osebe nedokazuje zbytočnosť. Rozhranie môže zachovávať zámerne zvolenú hranicu. Podobne aj krátka funkcia môže miešať nesúvisiace zodpovednosti. Keď ju rozdelíš len kvôli limitu dĺžky, toto miešanie môže zostať. Zástupný ukazovateľ zachytí jeden príznak; úspešná kontrola ešte nepotvrdzuje dodržanie princípu.

DRY sa najľahšie kontroluje strojovo: detektor klonov nájde doslovné opakovanie. Böckeler odlišuje takéto štrukturálne kontroly od sémantického posudzovania, ktoré označuje ako kontrolu založenú na úsudku modelu (*inferential checking*). Kontrola pomocou LLM je v tomto prípade nákladná a pravdepodobnostná.

Aj kontrola podmienok na vystavenie faktúry, ktorú agent najprv skopíroval a potom prepísal, môže detektoru duplicít uniknúť. Chyba v rozdelení zodpovednosti pritom zostane. Pýtaj sa kritika, kam biznisové rozhodnutie patrí. Správa o nulovej duplicite ti na to neodpovie.

Výpočtovú časť zaraď do brány, posúdenie významu ponechaj kritikovi. Nákladnú sémantickú kontrolu sústreď tam, kde ju zmena odôvodňuje; z každého commitu nerob neohraničený audit architektúry. Pri každej kontrole si ujasni, čo jej úspešný výsledok skutočne zaručuje.

## Opravy opráv ako signál na prepracovanie návrhu

Beloborodov používa tri po sebe nasledujúce úpravy ako varovanie: keď sa opravy vrstvia na opravy, je podľa neho čas vrátiť sa k architektúre. Nikto nezmeral, či sú tri správny prah. Použi ich ako východiskovú hodnotu pre dohodnutý **spúšťač prepracovania návrhu (redesign trigger)** v určenej oblasti s dostupnou históriou. Nie je to všeobecný zákon o kvalite opráv.

Sleduj **podiel opakovaných opráv (fix-on-fix rate)** po moduloch a jeho vývoj v čase. Môžeš počítať opravy, ktoré zasiahli oblasť upravenú inou opravou v zvolenom nedávnom období. Alebo priraďuj postupné opravy k tej istej chybe, ako to robili Park a kolegovia pri dodatočných opravách. Časové okno aj definíciu zvoľ skôr, než začneš vyhodnocovať trend. Spúšťač dohodni ešte pred dosiahnutím prahu, inak sa ďalšia naliehavá chyba stane dôvodom zmeniť význam signálu.

Zistenia Parka a kolegov vysvetľujú, prečo záleží na oblasti aj poradí. Dodatočná oprava je bežná a často zasahuje aj mimo okolia pôvodnej opravy. Celkový počet za celý projekt by zmiešal obyčajné nedokončené opravy s lokálnym zlyhaním návrhu. Hľadaj preto sériu opakovaných opráv okolo tej istej zodpovednosti. Posúď ju podľa mapy systému a denníka rozhodnutí.

Po dosiahnutí prahu nechaj oblasť preskúmať a podľa potreby prepracuj návrh. Tento signál agentovi nedáva oprávnenie vymeniť celý modul. Beloborodov pri náprave varuje pred otvoreným zadaním „prepíš všetko poriadne“. Podľa neho z neho vznikne ďalší projekt s ďalšou sadou problémov.

**Prepracovanie návrhu verzus prepis (redesign vs rewrite)** rozlíš konkrétnym postupom. Začni auditom: kde technický dlh skutočne brzdí vývoj, ktoré rozhodnutia môžu zostať a ktoré oblasti potrebujú pred zmenou samostatnú prípravu. Potom urči cieľovú architektúru a postupnosť etáp, z ktorých každá skončí funkčným výsledkom. Dlh tak riadiš vedome; časť z neho zostane.

V príklade s fakturáciou najprv rozhodni, kam patrí kontrola podmienok na vystavenie faktúry a ktoré moduly majú jej výsledok používať cez príslušný kontrakt. V jednej etape presuň modul, ktorý výsledok používa, späť za dohodnutú hranicu a pred pokračovaním over jeho správanie. V neskoršej etape odstráň nadbytočnú implementáciu. Platné rozhodnutie musí byť stále dostupné a kritik voči nemu posúdi každú etapu. Pri všeobecnej požiadavke na upratanie by o smere rozhodol sám opravujúci agent. Pri etapovom postupe sa dajú rozhodnutia skontrolovať ešte predtým, než na ne nadviažu ďalšie opravy.

:::tip[▶ Video]

<YouTube id="f84XbvASkk4" title="What Is AI Code Refactoring? Agentic AI & Safe Code Changes — IBM Technology" />

Martin Keen vo videu IBM Technology vysvetľuje refaktoring ako zmenu vnútornej štruktúry pri zachovaní vonkajšieho správania. Ukazuje aj riziko neurčitých cieľov, napríklad upratania celého modulu. Jeho postup s ochrannými kontrolami má toto poradie:

1. Plánovanie.
2. Čítanie.
3. Vyhľadávanie.
4. Zhrnutie zistení.
5. Schválenie človekom.
6. Uloženie snímky stavu.
7. Úprava kódu.
8. Overenie.
9. Návrat k predchádzajúcemu stavu.

Takéto kontroly dávajú etape prepracovania návrhu jasné hranice aj možnosť návratu.

:::

## Tri úrovne zrelosti: soloista · malý tím · enterprise

**Zaznamenaj rozhodnutie pred zmenou štruktúry, vynucuj jeho overiteľné hranice a dohodni, kedy opakované opravy vyžadujú prepracovanie návrhu.** S rozsahom sa menia zodpovednosti aj dôkazy, ktoré treba predložiť.

- **Soloista.** Udržuj súbor s denníkom rozhodnutí, ktorý agent prečíta pred každou opravou. Pridaj jedno či dve pravidlá importov alebo závislostí pre nosné hranice. Opakované opravy v jednotlivých oblastiach počítaj ručne. *Akému zlyhaniu to predchádza:* agent dôsledne zdokumentuje provizórne riešenie, akoby išlo o platnú architektúru.
- **Malý tím.** Každej oblasti ADR prideľ vlastníka. Rozhodnutia nahrádzaj novými a pôvodné uchovaj. Kritik nech kontroluje súlad s denníkom. Fitness funkcie spúšťaj v CI, ktorej kontroly agenti nemôžu upravovať. Zmraz existujúce porušenia a postupne ich odstraňuj tak, aby sa opravené už nevrátili. Sleduj trend opakovaných opráv po moduloch a porovnávaj ho s prahom dohodnutým vopred. *Akému zlyhaniu to predchádza:* agenti vytvárajú paralelné implementácie toho istého kontraktu.
- **Enterprise.** Spravuj ADR ako riadené záznamy a prepoj ich so záznamami zmien. Knižnicu ADR a komisiu pre riadenie zmien opisuje lekcia [Príprava je dôležitejšia než model](../part-1-foundation/preparation-over-model.md), audit a pôvod lekcia [Enterprise úroveň: audit, pôvod a čo je povinné](./enterprise-tier/index.md). Fitness funkcie zaraď do pipeline ako povinné kontroly. Pred porušením prijatého rozhodnutia vyžaduj nahrádzajúce ADR schválené vlastníkom. Tak dokážeš zablokovať neschválenú štrukturálnu zmenu a pri každej zmene doložiť, ktoré rozhodnutie ju riadi. *Akému zlyhaniu to predchádza:* architektúra zostane len v prezentáciách a dokumentoch, hoci systém sa od nej už dávno odchýlil.

## Čo si odniesť

- **Drobné opravy môžu zmeniť architektúru.** Kontroluj zodpovednosti a kontrakty, ktorých sa dotýkajú, aj keď už pôvodné správanie funguje.
- **Najprv rozhodnutie, potom zmena.** V každom zadaní opravy odkáž na príslušné ADR. Potrebnú výnimku zaznamenaj ešte pred implementáciou ako nahrádzajúce rozhodnutie a daj ju skontrolovať niekomu inému než autorovi opravy.
- **Nosné obmedzenia overuj automatickými kontrolami.** Do brán zaraď hranice závislostí, zložitosť a upozornenia popri duplicite. Ak by zavedenie pravidla inak vyžadovalo celkové upratanie, existujúce porušenia zmraz.
- **Odlišuj princíp od zástupného ukazovateľa.** Stroj dokáže zastaviť zakázaný import; kritik musí naďalej posúdiť, či riešenie zachováva zamýšľanú zodpovednosť.
- **Sleduj série opakovaných opráv v tej istej oblasti.** Prah pre prepracovanie návrhu dohodni vopred. Tri opravy sú heuristika jedného praktika, nie namerané optimum.
- **Návrh prepracúvaj v etapách s funkčným výsledkom.** Preskúmaj dlh, zaznamenaj cieľ a over každú etapu. Otvorené zadanie na prepis neposkytuje žiadnu z týchto kontrol.

**[Nové pojmy](../glossary.md#architecture-erosion)**: erózia architektúry / architektonický drift, rozhodnutie pred zmenou, denník architektonických rozhodnutí, nahradený záznam ADR, fitness funkcia, pravidlo závislostí / kontrakt importov, zmrazené porušenia, kontrola duplicít, podiel opakovaných opráv, spúšťač prepracovania návrhu, prepracovanie návrhu verzus prepis.
