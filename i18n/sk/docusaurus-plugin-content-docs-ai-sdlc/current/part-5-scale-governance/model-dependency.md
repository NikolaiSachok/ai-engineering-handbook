---
title: "Model ako závislosť: pripnutie, upgrady, odchod a podmienky pre dáta"
sidebar_position: 3.5
---

# Model je závislosť a o jeho vydaniach rozhoduje niekto iný

[Lekcia o nákladoch](./cost-economics/index.md) vyčíslila cenu modelu. II. a III. časť zaviedli brány na kontrolu jeho výstupov. Zostáva však samotný model ako závislosť, ktorú ovláda poskytovateľ. Pri pripnutej knižnici si termín upgradu vyberáš ty a testy spustíš skôr, než sa zmena dostane k používateľom. Pri modeli sa signatúra volania nemusí zmeniť vôbec, zatiaľ čo sa jeho odpovede zmenia podľa harmonogramu poskytovateľa. Nezávisíš od signatúry, ale od správania modelu. API tak môže ďalej vracať kód 200, hoci pracovný tok, ktorý ho používa, už nefunguje.

Môžeš prísť aj o samotný prístup. Andrej Beloborodov, ktorý pri vývoji od začiatku využíva AI a verejne o tejto práci píše, uvádza zablokované účty medzi dôvodmi, prečo používa viacero asistentov. V [jeho príspevku](https://realaillusions.com/ru/materials/threads-sovety-ai-praktika/) (po rusky) označuje poskytovateľa za „nepredvídateľného partnera“ (preložené z ruštiny, rovnako ako jeho ďalšie citáty na tejto stránke). Jeho asistenti zdieľajú jeden repozitár aj znalostnú bázu, takže keď sa jeden model správa zle, Beloborodov sa v susednom paneli editora prepne k inému asistentovi.

## Pripnutie obmedzuje, čo sa môže zmeniť

Identifikátor modelu môže označovať **snapshot modelu**, teda pevne určenú verziu, alebo **pohyblivý alias**, ktorého cieľovú verziu poskytovateľ smie zmeniť. **Pripnutie modelu (model pinning)** znamená, že v konfigurácii zvolíš konkrétny snapshot. Obmedzíš tým zmeny spôsobené presunom aliasu. Identifikátor snapshotu zaznamenaj pri každej zmene kódu, ktorú vytvorí agent: patrí do [priradenia agenta a modelu](./enterprise-tier/index.md).

Tabuľky citujú stránky poskytovateľov prečítané v októbri 2026: ide o datované príklady, nie o porovnanie ani odporúčanie.

| Služba | Snapshot: čo zaručuje pevný identifikátor | Alias: ako sa mení cieľ |
|---|---|---|
| OpenAI API | OpenAI uvádza, že snapshot pevne určuje verziu, a odporúča ho pripnúť, pretože na rovnaký prompt môžu rôzne snapshoty reagovať inak. | Na citovaných stránkach nie je uvedené, ako sa aliasy presúvajú. |
| Anthropic API | Podľa Anthropic zostávajú váhy aj konfigurácia pevné počas celej životnosti identifikátora. Od generácie 4.6 sú snapshotmi aj identifikátory bez dátumu. | Pri modeloch pred 4.6 odkazujú aliasy na najnovší datovaný snapshot danej vedľajšej verzie. |
| Google Gemini API | Google uvádza, že stabilné modely sa zvyčajne nemenia. | Alias `latest` priebežne ukazuje na stabilné, preview aj experimentálne vydania. Zmeny aliasu `latest`, ktoré narušia kompatibilitu, Google oznamuje e-mailom dva týždne vopred. |

Zdroje (prečítané v októbri 2026): OpenAI [stránka modelu](https://developers.openai.com/api/docs/models/gpt-4o) a [referencia](https://developers.openai.com/api/reference/overview), bez dátumu; Anthropic [identifikátory modelov](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions), bez dátumu; Gemini [modely](https://ai.google.dev/gemini-api/docs/models), aktualizované 2026-10-19.

Pripnutie nezabráni vyradeniu modelu, presmerovaniu identifikátora určeného na vyradenie na nástupcu ani zmenám infraštruktúry. Stránka spoločnosti Anthropic o identifikátoroch sama upozorňuje, že aktualizácie infraštruktúry občas spôsobia drobné rozdiely v správaní aj pri nezmenenom identifikátore a váhach. Anthropic vo vlastnej [správe o incidente](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) zo 17. septembra 2025 uvádza, že chyba v smerovaní požiadaviek podľa kontextového okna zasiahla 31. augusta v najviac postihnutej hodine 16% požiadaviek na Sonnet 4. Preto aj po pripnutí ďalej [sleduj kvalitu v produkcii](../part-4-platform/observability-rollout.md): infraštruktúra môže naďalej meniť výstupy.

## Upgrade preveruj na nemenných prípadoch a s nemenným hodnotiteľom

[Chen, Zaharia a Zou](https://arxiv.org/abs/2307.09009v3) v článku na arXiv opisujú kontrolovanú štúdiu, v ktorej presnosť GPT-4 pri rozlišovaní prvočísel a zložených čísel klesla z 84% v marci 2023 na 51% v júni 2023. Tretia revízia článku z októbra 2023 dospela k záveru, že tá istá služba sa môže za krátky čas podstatne zmeniť. [Ma, Yang a Kästner](https://arxiv.org/abs/2311.11123) v kontrolovanej prípadovej štúdii zistili, že pri aktualizáciách API sa 10,9% jednotlivých predikcií pri detekcii toxicity zmenilo zo správnych na nesprávne. Aktualizácie za aliasom `gpt-3.5-turbo` neboli oznámené, takže vývojári, ktorí ho volali, ich nemohli vopred otestovať.

Preprint [Xu a Wu](https://arxiv.org/abs/2608.17719) pochádza z augusta 2026. Autori v ňom spustili 900 položiek z benchmarkov na každom modeli 50-krát, a to pri troch dvojiciach verzií pred upgradom a po ňom. Prechod z GPT-5.4 na GPT-5.5 zvýšil celkové skóre náročného matematického benchmarku Omni-MATH o 7,3 percentuálneho bodu. Zlepšilo sa aj celkové skóre IFBench, ktorý overuje dodržiavanie pokynov, no 8,3% jeho položiek sa preukázateľne zhoršilo. Novší model ich pri opakovaných behoch riešil správne menej často, a podľa štatistických testov štúdie sa tento rozdiel nedal vysvetliť šumom vzorkovania. Celkové skóre teda zakrylo zmeny oboma smermi.

Tieto práce skúmali klasifikačné úlohy a benchmarky. Pri rešerši pre tento kurz v októbri 2026 sa nenašlo žiadne zverejnené meranie regresií programovacích agentov po upgrade modelu.

Pred prechodom spusti kandidáta vo vlastnom harnesse. **Opätovné preverenie (re-qualification)** využíva minulé zlyhania a [úniky premenené na regresné prípady](../part-3-verification/escape-ledger.md), aby odhalilo, čo upgrade pokazí.

1. Nemeň [LLM v úlohe hodnotiteľa](../part-3-verification/layered-gates/index.md). Ak naraz vymeníš generujúci model aj hodnotiteľa, nezistíš, či skóre stúplo vďaka lepším výstupom alebo miernejšiemu posudzovaniu. Nového hodnotiteľa prever samostatne na verdiktoch, ktoré potvrdil človek.
2. Spúšťaj prípady opakovane na oboch verziách. Odlíšiš tak trvalé zmeny od bežného kolísania odpovedí.
3. Porovnávaj prípad po prípade. Zlepšenia inde môžu zakryť **regresiu v jednotlivých prípadoch (item-level regression)**: začne zlyhávať prípad, ktorý predtým prechádzal.
4. Zmeraj úspešnosť prvého pokusu `p` na reprezentatívnej vzorke každej triedy úloh. Regresné prípady odhaľujú poškodené správanie; na reprezentatívnej práci odhadneš `p` bez toho, aby v nej neúmerne prevážili minulé zlyhania.
5. Nasadzuj postupne, aby si obmedzil rozsah možných následkov. Znova preskúmaj [predpoklady zabudované do harnessu](../part-1-foundation/preparation-over-model.md): po upgrade už staré provizórne riešenia nemusia byť potrebné.

Beloborodov podľa svojich slov občas [prehadzuje roly modelov, ktoré píšu a kontrolujú kód](https://realaillusions.com/ru/materials/sovety_ai_praktika_part3/), aby zistil, „kto otupel“. Ak pri takejto neformálnej kontrole opakovane spúšťaš tie isté prípady, získaš výsledky, ktoré sa dajú preskúmať.

:::tip[▶ Video]

<YouTube id="4gC3oueK9Gc" title="Building Trustworthy AI: Avoid Model Drift & Unsafe Outputs — IBM Technology" />

Video IBM Technology opisuje validáciu výstupov, sledovanie driftu a filtre po nasadení. Vysvetľuje monitorovanie, ktoré potrebuješ aj po pripnutí modelu.

:::

## Odchod má termín

Po ohlásení vyradenia máš **lehotu pred vyradením (deprecation notice period)** na preverenie nástupcu a migráciu. Niektoré platformy používajú aj **automatický upgrade (auto-upgrade)**, takže ti môžu vymeniť verziu skôr, než jej nástupcu preveríš. Zverejnené pravidlá rozlišujú modely vo všeobecnej dostupnosti (GA) a predbežné verzie (preview).

| Služba | Oznámenie vopred: uvedené minimum podľa triedy modelu | Vyradenie alebo upgrade: postup a príklad |
|---|---|---|
| OpenAI API | OpenAI uvádza pre GA najmenej 6 mesiacov a pre špecializované modely najmenej 3 mesiace. Pri preview môže byť lehota oveľa kratšia, napríklad dva týždne. Ak ide o bezpečnosť alebo o súlad s predpismi, oznámi to s čo najväčším primeraným predstihom. | Príklad `o3-2025-04-16`: oznámenie 2026-06-11, vypnutie 2026-12-11. Automatická náhrada nie je uvedená. |
| Anthropic API | Anthropic uvádza pre verejne vydané modely najmenej 60 dní. Partnerské platformy určujú vlastné harmonogramy. | Príklad `claude-opus-4-1-20250805`: oznámenie 2026-06-05, vyradenie 2026-08-05. Automatická náhrada neprebehne; požiadavky na vyradený model zlyhajú. |
| Google Gemini API | Google pre stabilné modely uvádza oznámenie vopred bez minimálnej lehoty. Oznámené dátumy sú najskoršie možné: vyradenie môže prísť neskôr. Pre preview platia najmenej dva týždne. | Niektoré stabilné endpointy určené na vyradenie automaticky presmerujú požiadavky na nástupcu. Vypnuté endpointy prestanú byť dostupné. |
| Microsoft Foundry | Microsoft uvádza pre GA najmenej 60 dní a pre preview najmenej 30 dní; v núdzových situáciách sa lehota môže skrátiť. | Nasadenia typu Standard pri vyradení automaticky prejdú na novšiu verziu. S nastavením `NoAutoUpgrade` namiesto toho prestanú fungovať. |

Zdroje (prečítané v októbri 2026): OpenAI [vyradenia modelov](https://developers.openai.com/api/docs/deprecations), bez dátumu; Anthropic [vyradenia modelov](https://platform.claude.com/docs/en/about-claude/model-deprecations), bez dátumu; Gemini [vyradenia modelov](https://ai.google.dev/gemini-api/docs/deprecations), aktualizované 2026-10-20, a modely uvedené vyššie; Microsoft [vyradenia modelov](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements), 2026-07-24.

Na platforme Foundry nastavenie `OnceNewDefaultVersionAvailable` prevedie nasadenia typu Standard na novšiu verziu už pri určení novej predvolenej verzie. Nasadenia typu Provisioned automatickým upgradom neprechádzajú. Preview verzie sa povinne prevádzajú na novšiu verziu s oznámením najmenej 30 dní vopred.

Spomedzi modelov GA a stabilných modelov v tabuľke je najkratšia uvedená minimálna lehota 60 dní, a to pre verejne vydané modely Anthropic a pre modely GA od Microsoftu. Google pre stabilné modely minimum neuvádza; pri preview sú minimá ešte kratšie. Ak začneš s preverovaním a migráciou až po oznámení a potrebuješ na ne viac času, než zostáva do vyradenia, nestihneš ich. Stihneš to iba vtedy, ak kandidátov preveruješ priebežne, ešte pred oznámením.

Pri pozastavení prístupu môžeš prísť aj o tento čas na prípravu. Dve zverejnené ustanovenia ukazujú dôvody aj podmienky oznámenia.

| Služba | Pozastavenie alebo ukončenie: dôvody a oznámenie |
|---|---|
| Anthropic API | Anthropic môže prístup pozastaviť, ak sa odôvodnene domnieva alebo určí, že nastala niektorá z uvedených podmienok. Patria medzi ne napríklad porušenie podmienok, zákonný zákaz či podstatný nárast nákladov na poskytovanie služby. Zaväzuje sa vynaložiť primerané úsilie na písomné oznámenie. |
| Google Gemini API | Google môže prístup pozastaviť bez oznámenia, ak sa odôvodnene domnieva, že boli porušené podmienky. Podľa §8(a) môže tiež kedykoľvek z akéhokoľvek dôvodu ukončiť poskytovanie API alebo zmluvný vzťah. |

Zdroje (prečítané v októbri 2026): Anthropic [obchodné podmienky](https://www.anthropic.com/legal/commercial-terms), platné od 2025-06-17; Google [podmienky API](https://developers.google.com/terms), upravené 2021-11-09.

**Vyskúšaná možnosť odchodu (tested exit)** si vyžaduje jedného klienta pre všetky volania modelu a konfiguráciu, v ktorej je zapísaný poskytovateľ aj model. Cez toho istého klienta pravidelne spúšťaj regresné prípady so záložným poskytovateľom alebo modelom prevádzkovaným vo vlastnej infraštruktúre. Úspešnosť prvého pokusu záložného modelu meraj samostatne: iný model má vlastné náklady na prijatú zmenu. Podobne ako [obnovu zálohy](../part-4-platform/environments-migrations-data.md) musíš aj prechod nacvičiť, aby si odhalil jeho zlyhania.

## Bez pamäti projektu sa odchádza ťažko

V [ďalšom príspevku](https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/) Beloborodov píše, že ľudia za ním najčastejšie prichádzajú so stratou kontextu. Potrebu uchovávať znalosti o projekte mimo chatov si podľa neho ľudia niekedy uvedomia „prudko a bolestivo“ — napríklad pri zablokovaní účtu.

Znalosti, ktoré existujú iba v histórii chatu, sú závislé od prístupu k účtu. S účtom stratíš aj ich. Pravidlá, rozhodnutia, poznámky k architektúre a zadania preto uchovávaj ako [pamäť projektu](../part-1-foundation/project-memory-and-tiering.md) v súboroch repozitára alebo v úložisku znalostí. Tak vzniká **pamäť nezávislá od dodávateľa (vendor-portable memory)**: náhradný asistent ju prečíta aj bez pôvodného účtu.

## Podmienky pre dáta určuje účet

Ak vložíš firemný kód do osobného chatu, vzťahujú sa naň spotrebiteľské podmienky tvojho osobného predplatného. Keď prompty opustia tvoj počítač, **podmienky nakladania s dátami (data terms)** určujú ich použitie na tréning, dobu uchovávania aj miesto spracovania. **Dodatok o spracúvaní osobných údajov (data processing addendum, DPA)** vymedzuje, ako poskytovateľ spracúva osobné údaje v tvojom mene.

Pri každej službe a jej konkrétnom pláne predplatného zisti štyri veci: či poskytovateľ trénuje na tvojich dátach, ako dlho dáta uchováva, kde ich spracúva a ktorý DPA sa uplatňuje. Použitie na tréning a uchovávanie sú dve samostatné otázky.

| Služba | Použitie na tréning | Uchovávanie |
|---|---|---|
| OpenAI API | OpenAI dáta na tréning nepoužíva, pokiaľ na to nedáš súhlas. | Záznamy na monitorovanie zneužívania uchováva najviac 30 dní, ak zákon nevyžaduje dlhšie obdobie. Stav Responses sa predvolene uchováva 30 dní; niektoré endpointy uchovávajúce stav držia dáta, kým ich nevymažeš. |
| Anthropic (komerčné služby) | Anthropic dáta zákazníkov predvolene vylučuje z tréningu; spätná väzba alebo súhlas môžu použitie na tréning umožniť. Obchodné podmienky osobitne zakazujú trénovať na zákazníckom obsahu služieb. | Vstupy a výstupy API vymaže do 30 dní. Medzi výnimky patria ZDR, vynucovanie Usage Policy a zákonné požiadavky. |
| Anthropic (spotrebiteľské služby) | Podľa aktualizácie podmienok vyžaduje tréning súhlas používateľa. | Pri povolenom tréningu sa nové alebo obnovené chaty a programovacie relácie uchovávajú päť rokov; inak zostáva pôvodných 30 dní. Aktualizácia sa nevzťahuje na komerčné služby. |
| Google Gemini API | Google v bezplatných službách používa vstupy a výstupy na vývoj a zlepšovanie produktov; môže ich kontrolovať človek. V platených službách sú zo zlepšovania produktov vylúčené. | V oboch prípadoch uchováva prompty, kontext a výstupy 55 dní na vynucovanie pravidiel a plnenie zákonných povinností sprístupniť údaje. |
| Google Vertex AI | Google dáta zákazníka bez predchádzajúceho súhlasu alebo pokynu zákazníka na tréning nepoužíva. | Cache vymaže do 24 hodín; ukladanie do cache možno vypnúť. Prompty môže zaznamenávať na odhaľovanie zneužívania; doba uchovávania nie je uvedená. |
| Microsoft Foundry | Microsoft dáta bez súhlasu alebo pokynu na tréning nepoužíva. | Dáta funkcií, ktoré uchovávajú stav, aj nahrané dáta drží, kým ich zákazník nevymaže. Existuje aj úložisko na monitorovanie zneužívania s kontrolou človekom; doba uchovávania nie je uvedená. |

Zdroje (prečítané v októbri 2026): OpenAI [kontrola dát](https://developers.openai.com/api/docs/guides/your-data), bez dátumu, pravidlo pre tréning od 2023-03-01; Anthropic [tréning](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training), zobrazuje 2026-08-18, a [uchovávanie](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data), 2026-07-01, obchodné podmienky uvedené vyššie, [aktualizácia spotrebiteľských podmienok](https://www.anthropic.com/news/updates-to-our-consumer-terms), 2025-08-28; Gemini [podmienky](https://ai.google.dev/gemini-api/terms), platné od 2026-03-23, aktualizované 2026-04-28, a [pravidlá používania](https://ai.google.dev/gemini-api/docs/usage-policies), 2026-06-09; Vertex [ZDR](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/vertex-ai-zero-data-retention), 2026-10-15; Foundry [ochrana dát](https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy), 2026-05-18.

Zero data retention (ZDR), teda nulové uchovávanie dát, má vlastné podmienky oprávnenosti a výnimky. Rezidenciu dát over samostatne.

| Služba | Zero data retention | Rezidencia dát / DPA |
|---|---|---|
| OpenAI API | OpenAI vyžaduje schválenie a splnenie ďalších požiadaviek; oprávnenosť sa líši podľa endpointu. Aj pri ZDR zostávajú označené obrazové a súborové vstupy uložené na kontrolu; niektoré funkcie uchovávajú stav aplikácie. | Spracovanie v regióne tam, kde je podporované. V regiónoch určených iba na uloženie môže spracovanie aj dočasné uloženie prebehnúť mimo regiónu. Rezidencia dát mimo USA vyžaduje schválenie monitorovania zneužívania a dodatok Modified Retention. DPA nie je na citovanej stránke uvedený. |
| Anthropic (komerčné služby) | ZDR dojednáva Anthropic s každou organizáciou zvlášť cez obchodné oddelenie. Označený obsah môže uchovávať až dva roky; niektoré modely bez osobitného povolenia vyžadujú 30-dňové uchovávanie. Oprávnenosť sa líši podľa funkcie; funkcie uchovávajúce stav sú vylúčené a zákon môže vyžadovať uchovávanie. | Inferencia pri modeloch 4.6+ iba v USA alebo globálne; iba USA za 1,1× cenu. Geografická oblasť uloženia pracovného priestoru je USA. Obchodné podmienky zahŕňajú DPA. |
| Anthropic (spotrebiteľské služby) | Nie je uvedené. | Rezidencia dát ani DPA nie sú uvedené. |
| Google Gemini API | Nie je uvedené. | Google môže zaznamenané dáta platených služieb dočasne ukladať alebo držať v cache v ktorejkoľvek krajine, kde Google alebo jeho zástupcovia prevádzkujú zariadenia. Záväzok k rezidencii dát nie je uvedený. Na platené služby sa vzťahujú podmienky pre sprostredkovateľa. |
| Google Vertex AI | Podľa Google dosiahne zákazník ZDR vlastnou konfiguráciou, s výnimkou zaznamenávania na odhaľovanie zneužívania. Grounding with Google Search uchováva záznamy najviac tri dni a toto ukladanie nemožno vypnúť. | Uložené dáta zostávajú vo vybranej lokalite. Endpointy viazané na jurisdikciu alebo lokalitu držia spracovanie ML v danej jurisdikcii; globálny endpoint môže spracúvať kdekoľvek bez záruky rezidencie dát. Stránka ZDR odkazuje na Cloud Data Processing Addendum (CDPA) od Google. |
| Microsoft Foundry | Microsoft na žiadosť umožňuje úpravu monitorovania zneužívania. | Spracovanie v geografickej oblasti určenej zákazníkom s výnimkou nasadení Global/DataZone. Uložené dáta zostávajú v geografickej oblasti zákazníka. Stránka odkazuje na DPA. |

Zdroje (prečítané v októbri 2026): OpenAI kontrola dát, Anthropic aktualizácia spotrebiteľských podmienok, Gemini podmienky, Vertex ZDR a Foundry ochrana dát uvedené vyššie; Anthropic [ZDR](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) a [rezidencia dát](https://platform.claude.com/docs/en/manage-claude/data-residency), bez dátumu; Vertex [rezidencia dát](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency), 2026-10-15; DPA: [Anthropic](https://www.anthropic.com/legal/data-processing-addendum), Google [podmienky pre sprostredkovateľa](https://business.safety.google/processorterms/), Google Cloud [CDPA](https://cloud.google.com/terms/data-processing-addendum), [Microsoft](https://aka.ms/DPA), dátumy týchto dokumentov nie sú na citovaných nadradených stránkach uvedené.

Lekcie o [secrets](../part-4-platform/secrets.md) a [prostrediach](../part-4-platform/environments-migrations-data.md) obmedzovali, čo smie vstúpiť do kontextu. Pri dátach, ktoré sa k poskytovateľovi dostanú, zaznamenaj príslušné podmienky a pri ich zmene si ich znova prečítaj.

## Smeruj podľa nákladov na prijatú zmenu

Lacnejší model sa oplatí len vtedy, keď mu úspešnosť prvého pokusu klesne pomerne menej, než mu klesne cena. Ak stojí polovicu, ale úspešnosť má nižšiu než polovičnú, prijatá zmena vyjde drahšie. **Smerovanie podľa hranice rentability (routing by break-even)** vychádza z podmienky `p_cheap / p_expensive > price_cheap / price_expensive`, rozobranej v [prehĺbení o nákladoch](./cost-economics/deep-dive.md).

Meraj `p` pre každú triedu úloh na reprezentatívnej práci. Do rozhodnutia započítaj aj ľudskú revíziu neúspešných pokusov: môže tvoriť väčšinu účtu. Požiadavky na dáta môžu samostatne odôvodniť model vo vlastnej infraštruktúre bez ohľadu na výsledok tohto porovnania. Každá ďalšia cesta však znamená ďalší model na pripnutie, životný cyklus na sledovanie a podmienky na prečítanie.

:::tip[▶ Video]

<YouTube id="pePAAGfh-IU" title="How to Pick the Right AI Foundation Model — IBM Technology" />

Martin Keen vo videu IBM Technology predstavuje šesť krokov výberu modelu aj náklady nesprávneho výberu. Uplatni tento postup na každú triedu úloh, ktorú smeruješ na konkrétny model.

:::

## Tri úrovne zrelosti: soloista · malý tím · enterprise

Invariant platí na každej úrovni: **pripni verziu, ktorú používaš, preveruj každú jej zmenu a dokáž, že vieš odísť.**

- **Soloista.** Pripni model v konfigurácii a pamäť projektu ulož do repozitára. Pred upgradom znova spusti minulé zlyhania; skontroluj lehoty pred vyradením aj podmienky účtu. *Akému zlyhaniu to predchádza:* pozastavený účet odnesie aj kontext projektu alebo alias prejde na model, ktorý si nikdy netestoval.
- **Malý tím.** Zaveď jedného klienta pre všetky volania modelu, upgrady preveruj opakovanými behmi a záložnú cestu pravidelne skúšaj. Pre každú triedu úloh meraj úspešnosť prvého pokusu a pri každej službe zaznamenaj záväzky týkajúce sa dát. *Akému zlyhaniu to predchádza:* o vyradení sa dozvieš z chýb v produkcii alebo nasadíš upgrade, ktorého lepší priemer zakryl poškodené prípady.
- **Enterprise.** V evidencii modelov uchovávaj verziu, poskytovateľa, región, podmienky, lehotu oznámenia a vlastníka. Zabezpeč DPA aj záväzky k rezidencii dát a uchovávaniu; ponechaj dôkazy o preverení aj vyskúšanom odchode. *Akému zlyhaniu to predchádza:* zákazník sa opýta, kam išli dáta a ktorý model vytvoril zmenu, no nikto nevie odpovedať.

## Čo si odniesť

- Pripnutie obmedzuje zmeny cez alias. Vyradenie, presmerovanie na nástupcu a infraštruktúru neovláda, preto zachovaj priradenie agenta a modelu aj sledovanie kvality.
- **Hodnotiteľa nemeň.** Miernejšie posudzovanie sa potom nemôže vydávať za zlepšenie generujúceho modelu.
- Minulé zlyhania odhaľujú regresie, na vzorke reprezentatívnej práce odhadneš `p` pre smerovanie. Potrebuješ oboje.
- **Skúšaj odchod a pamäť uchovávaj v repozitári.** Pri pozastavení účtu sa k histórii chatov nemusíš dostať; pri vyradení zostane pracovný tok bez funkčnej cesty, ak nemá preverenú náhradu.
- Záväzky k dátam určuje služba a plán predplatného daného účtu. Zaznamenaj podmienky aj ich dátum.
- Do nákladov pri smerovaní započítaj ľudskú revíziu neúspešných pokusov. Lacnejšie tokeny môžu stáť viac ľudského času.

**[Nové pojmy](../glossary.md#the-model-is-a-dependency-pinning-upgrades-exit-and-data-terms)**: snapshot modelu verzus pohyblivý alias, pripnutie modelu (model pinning), opätovné preverenie (re-qualification), regresia v jednotlivých prípadoch (item-level regression), lehota pred vyradením (deprecation notice period), automatický upgrade (auto-upgrade), vyskúšaná možnosť odchodu / záložný poskytovateľ, pamäť nezávislá od dodávateľa (vendor-portable memory), podmienky nakladania s dátami (použitie na tréning · uchovávanie · zero data retention · rezidencia dát · DPA), smerovanie podľa hranice rentability (routing by break-even).
