---
title: Smerovanie medzi modelmi — náklady a latencia celého dopytu
sidebar_label: Smerovanie medzi modelmi
sidebar_position: 3
---

# Smerovanie medzi modelmi — náklady a latencia celého dopytu

Keď zveríš 70% dopytov menšiemu modelu, ešte z toho nevyplýva 70% úspora. A ak jeho odpoveď pred zobrazením skontroluješ, kontrola môže spotrebovať čas, ktorý máš vyhradený na prvý token. **Model routing (smerovanie medzi modelmi)** sa oplatí až vtedy, keď celý postup súčasne spĺňa požiadavky na kvalitu, cenu aj latenciu.

Táto lekcia rozvíja [smerovanie medzi modelmi v LLMOps](./index.md#route-between-models). Všetky ceny, časy a počty v nasledujúcich výpočtoch sú vymyslené vstupy na vysvetlenie postupu: nejde o merania ani o cenník poskytovateľa.

## Vybrať model vopred alebo skontrolovať hotovú odpoveď? \{#choose-before-generation-or-check-after-it}

Začni údajmi, ktoré už aplikácia má. Používateľ zvolil konkrétnu akciu v rozhraní; vyhľadávanie vrátilo určitý počet úryvkov; chýbajú citácie alebo si zdroje odporujú. K dispozícii môžeš mať aj rozdiel medzi skóre výsledkov vyhľadávania. Použitie týchto údajov si po vyhľadávaní nevyžaduje ďalšie volanie modelu. Samotné vyhľadávanie však má svoju cenu.

Takéto príznaky ešte neurčujú náročnosť dopytu. Dva úryvky si môžu protirečiť a dvadsať úryvkov môže opakovať jediný fakt. Aj rozdiel medzi skóre musíš kalibrovať pre konkrétny vyhľadávač a populáciu dopytov.

Samostatná predikcia odpovedá na inú otázku: zvládne tento dopyt lacnejší model v požadovanej kvalite? Router (smerovač) môže používať pravidlo, klasifikátor alebo LLM. Pri učení potrebuje reprezentatívne označené príklady a oddelenú testovaciu sadu pre skutočnú dvojicu modelov a tvoje úlohy. Výsledky sa nemusia preniesť na inú dvojicu ani na iné dopyty. Náklady a čas klasifikátora patria do porovnania.

Pri výbere vopred smerovač vyberie model a ten vygeneruje odpoveď. **Model cascade (kaskáda modelov)** postupuje inak: najprv vygeneruje odpoveď lacný model, potom ju systém skontroluje a pri nevyhovujúcom výsledku zavolá silnejší model. **Escalation rate (miera eskalácie)**, označená `r`, je podiel dopytov vstupujúcich do tejto kaskády, pri ktorých sa zavolá ďalšia úroveň. Ak niektoré dopyty idú priamo na silnejší model, do menovateľa tejto miery nepatria.

| Návrh | Za čo platíš | Dôsledok chybného výberu |
| --- | --- | --- |
| Výber vopred | Smerovač a jedno generovanie vybraným modelom | Slabá odpoveď môže zostať nepovšimnutá, ak nemáš kontrolu alebo audit. |
| Kaskáda | Vždy lacné generovanie a kontrola; pri eskalácii aj silnejší model | Odhalenú slabú odpoveď môžeš nahradiť, ak ešte zostáva čas. |

Od eskalácie podľa kvality odlišuj **fallback (záložnú cestu)** pri chybe služby alebo obmedzení počtu volaní, napríklad chybe 429. Rozhodnutie použiť iný model má v týchto prípadoch iný dôvod.

Ani jeden návrh nezaručuje správnu odpoveď. Verifier (overovač), ktorý posudzuje kvalitu výsledku, môže prijať zlú odpoveď aj odmietnuť dobrú. Silnejší model môže zopakovať tú istú chybu a chýbajúce dôkazy vo vyhľadanom kontexte nevyrieši ani jeden postup. Platná schéma či existencia citovaného dokumentu ešte neznamená, že zdroj podporuje tvrdenie. Kontrolu kalibruj na príkladoch označených človekom a audituj prijaté aj odmietnuté odpovede; metodiku rozoberá [prehĺbenie evaluácie](../../part-1-rag/cross-cutting/evaluation/deep-dive.md).

Nahradiť odpoveď môžeš iba pred jej zobrazením alebo pred nezvratnou operáciou v externom systéme. Ak používateľ nemá výmenu vidieť, priebežne generovaný text zadržiavaj. Kaskádu obmedz na odpovede alebo pred operáciami s vedľajšími účinkami vyžaduj schválenie. Aj výber modelu vopred môže dopĺňať kontrola a náprava; možnosť odhaliť chybu závisí od celého návrhu.

## Podiel dopytov a podiel výdavkov počítaj zvlášť \{#compute-request-mix-and-spend-separately}

Predstav si 100 dopytov troch druhov. Pri každom druhu porovnaj vybraný model s použitím silného modelu na rovnakú prácu. Dĺžka vstupu aj výstupu sa medzi druhmi môže líšiť. Nasledujúce dolárové sumy sú hypotetické:

| Druh úlohy | Počet | Vybraný model: $/dopyt | Iba silný model: $/dopyt | Vybraný model: spolu $ | Iba silný model: spolu $ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Vyhľadanie údaja | 70 | 0,001 | 0,010 | 0,070 | 0,700 |
| Syntéza | 25 | 0,006 | 0,020 | 0,150 | 0,500 |
| Dlhý text | 5 | 0,050 | 0,050 | 0,250 | 0,250 |
| Spolu | 100 | — | — | 0,470 | 1,450 |

Úspora je `(1.450 − 0.470) / 1.450`, približne 67,6%. Vyhľadanie údaja tvorí 70% dopytov, ale iba `0.070 / 0.470`, približne 14,9% výdavkov pri smerovaní. Každý z týchto podielov má iný menovateľ.

Ak klasifikátor spotrebuje ďalších 0,001 $ na každý zo 100 dopytov, pripočítaš 0,100 $. Celkom zaplatíš 0,570 $ a úspora klesne na približne 60,7%.

Pre jednoduchú kaskádu označ náklad na generovanie malým modelom `Cs`, na kontrolu `Cv` a na dodatočné volanie veľkého modelu `Cl`. Pri pevných nákladoch na jednotlivé kroky je očakávaný náklad na dopyt vstupujúci do kaskády:

`E[C] = Cs + Cv + r × Cl`

Pri hypotetických hodnotách `Cs = 0.002`, `Cv = 0.001`, `Cl = 0.010` a `r = 0.20` vyjde 0,005 $ — polovica z 0,010 $ za samotný silný model. Náklady sa vyrovnajú pri:

`r = (Cl − Cs − Cv) / Cl = 0.70`

Ak eskaluješ 80% dopytov, zaplatíš priemerne 0,011 $, teda viac než pri priamom použití silného modelu. Pri eskalácii platíš za obe generovania; neznamená to však automaticky presne dvojnásobnú cenu.

Tento výpočet predpokladá pevné náklady. Ak na silnejší model postupujú najmä dlhšie dopyty, použi priemerný náklad jeho volania podmienený tým, že dopyt eskaloval. Započítaj aj smerovač, opakované pokusy, opätovne posielaný kontext, ďalšie kontroly a nástroje, ak ich používaš. Dopyty, ktoré kaskádu obchádzajú, zahrň do celku samostatne s príslušnou váhou. Porovnávaj rovnaké úlohy pri rovnakej požadovanej kvalite: lacnejšie nesprávne odpovede nie sú dôkazom úspory.

## Dve generovania menia percentil času odozvy celého dopytu \{#a-two-pass-path-changes-the-percentile}

**TTFT (time-to-first-token — čas do prvého tokenu)** u poskytovateľa meria čas po prvý token na jeho rozhraní. Používateľ však čaká až na prvý token, ktorý mu aplikácia skutočne sprístupní. Do tohto času patrí vyhľadávanie, smerovanie, čakanie vo frontoch aj kontroly, ktoré blokujú zobrazenie. Čas do dokončenia celej odpovede je ďalšia metrika. Keď text zadržiavaš až do výsledku kontroly, dobré TTFT poskytovateľa sa používateľovi nemusí prejaviť. Rozlíšenie metrík vysvetľuje [lekcia o servingu](../serving/index.md).

Pri sériovej kaskáde so zadržaným výstupom čakáš pri prijatej odpovedi na generovanie malým modelom a kontrolu. Pri eskalovanom dopyte sa pripočíta čas generovania veľkým modelom a záverečných kontrol blokujúcich zobrazenie. Najprv spočítaj skutočný uplynutý čas v každom trace, teda zázname priebehu jedného dopytu. Až z týchto celkov vypočítaj percentil. Súčet p95 jednotlivých spanov nie je p95 celého dopytu: jednotlivé percentily môžu patriť iným dopytom a záleží aj na koreláciách a na tom, ktoré dopyty eskalujú.

V ďalšom hypotetickom príklade trvá generovanie malým modelom vždy 450 ms a kontrola 100 ms. Generovanie veľkým modelom so záverečnou kontrolou pridá vždy 1200 ms. Ostatná réžia je nulová. Prijatú odpoveď preto zobrazíš po 550 ms, eskalovanú po 1750 ms. Zo 100 časov zoradených vzostupne vezmi pre p95 hodnotu na 95. mieste — konvenciu nearest-rank.

| Miera eskalácie | Dopyty s časom 550 ms | Dopyty s časom 1750 ms | p95 | Podiel dopytov dokončených do 800 ms |
| --- | ---: | ---: | ---: | ---: |
| 4% | 96 | 4 | 550 ms | 96% |
| 5% | 95 | 5 | 550 ms | 95% |
| 6% | 94 | 6 | 1750 ms | 94% |

Pri takto úplne oddelených časoch oboch vetiev sa p95 presunie na pomalú vetvu, keď jej podiel prekročí 5%. Pri presne 5% ostáva podľa zvolenej konvencie na rýchlej vetve. Interpolácia alebo iné meracie okno môže hraničný výsledok zmeniť. Aj pri 4% však používatelia s eskalovanými dopytmi čakajú 1750 ms; p95 nesľubuje čas každému jednotlivému používateľovi.

Všeobecnejšie označ `Fa(t)` podmienenú distribučnú funkciu času prijatých dopytov a `Fe(t)` podmienenú distribučnú funkciu času eskalovaných dopytov. Druhá zahŕňa celú sériovú cestu, nielen volanie veľkého modelu. Distribučná funkcia celku je:

`F(t) = (1 − r) × Fa(t) + r × Fe(t)`

Cieľ „aspoň 95% dopytov do termínu“ spĺňaš práve vtedy, keď `F(deadline) ≥ 0.95`. Ak sa časy vetiev prekrývajú alebo má aj rýchla vetva dlhý chvost, 5% nie je univerzálne bezpečná hranica eskalácie. Meraj celé tracy pod záťažou: pri rastúcom `r` môžu spoločné fronty a protitlak spomaliť aj prijaté dopyty. Meranie rozoberá [observability — prehĺbenie](../../part-1-rag/cross-cutting/observability/deep-dive.md), fronty a riadenie záťaže [serving — prehĺbenie](../serving/deep-dive.md).

Jednou možnosťou je synchrónne kontrolovať rýchlu úroveň, ak sa kontrola podľa meraní zmestí do časového rozpočtu, a pomalú úroveň auditovať asynchrónne, ak je zostávajúce riziko, že používateľ dostane chybnú odpoveď, prijateľné. Asynchrónny audit však už zobrazenú chybu nezastaví. Povinné bezpečnostné kontroly pred zobrazením zachovaj. Ak požadovanú kvalitu do termínu nevieš overiť, systém má odpoveď odmietnuť alebo odložiť. Panel metrík nenahrádza požiadavku zachytiť chybu pred zobrazením.

## Spravuj všetky pravidlá smerovania, nielen prah \{#operate-the-policy-not-just-the-threshold}

Prísnejší prah kontroly môže zvýšiť `r` a pomôcť nahradiť chybné odpovede. Zlepšenie kvality však musíš preukázať meraním. Pre jednotlivé druhy úloh a úrovne modelov sleduj mieru eskalácie, chyby medzi prijatými odpoveďami, nesprávne prijatia aj odmietnutia overovačom, výslednú kvalitu, náklad na úspešne vybavený dopyt, TTFT z pohľadu používateľa aj čas dokončenia.

Keď `r` rastie, preskúmaj zmeny vstupov, vyhľadávania, overovača a malého modelu. Nezmierňuj prah iba preto, aby si znížil výdavky. Politiku prehodnocuj podľa nových dôkazov a zmien závislostí; neexistuje všeobecné pravidlo, že po štvrťroku prestane platiť.

Konfiguráciu verziuj a umožni jej načítanie za behu. Má určovať prípustné úrovne modelov, pravidlá pre jednotlivé druhy úloh, prahy, termíny, limity výdavkov aj postup pri vypršaní času na kontrolu. Pred použitím ju validuj a uplatni ju naraz, aby nevznikla zmes dvoch verzií. Do každého tracu zaznamenaj verziu konfigurácie a dôvod výberu. Zmenu over na oddelenej testovacej sade a potom na malej časti produkčnej premávky so sledovaním kvality. Predchádzajúcu konfiguráciu maj pripravenú na rollback.

Každú úroveň musíš vedieť samostatne vypnúť. Vypnutie úrovne malého modelu znamená obísť generovanie týmto modelom aj jeho kontrolu. Pri vypnutí silnej úrovne výslovne urči, ako sa systém zachová, napríklad či odpoveď odmietne alebo odloží. Rovnako urč bezpečný postup pri výpadku overovača. Ohranič počet pokusov aj celkový čas, aby systém neeskaloval donekonečna. Presmerovanie mení zaťaženie aj výdavky cieľovej úrovne; over jej kapacitu a rozpočet. Pri zhoršení podmienok sa systém má riadiť známou politikou s jasnými limitmi.

## Čo si odniesť z lekcie \{#what-to-take-away}

- Začni príznakmi, ktoré už máš. Ak predikuješ, či lacný model úlohu zvládne, vyhodnoť túto predikciu na svojich modeloch a dopytoch.
- Započítaj každé generovanie a každú kontrolu. Podiel dopytov má iný menovateľ než podiel výdavkov.
- Percentily počítaj z časov celých dopytov. Samotná miera eskalácie nedokazuje, že splníš limit latencie.
- Odhalenú chybu môžeš napraviť pred zobrazením odpovede alebo nezvratnou operáciou. Audituj aj prijaté odpovede a pre výpadky urč správanie s jasnými limitmi.

**[Nové pojmy](../../glossary.md#llmops)**: Model cascade (kaskáda modelov), Escalation rate (miera eskalácie).

Pozri aj: [smerovanie medzi modelmi v LLMOps](./index.md#route-between-models) a [evaluácia — prehĺbenie](../../part-1-rag/cross-cutting/evaluation/deep-dive.md).
