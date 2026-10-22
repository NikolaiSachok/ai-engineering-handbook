---
title: Evaluation — do hĺbky
sidebar_label: "Vnútro metrík a kalibrácia sudcu"
sidebar_position: 2
---

# Keď je metrika sama sudcom, ako ju kalibruješ a na akých ľudských značkách to celé stojí

[Časť 1](./index.md) postavila rámec: vyhľadávanie a generovanie hodnoť oddelene, postav si golden set, voľný text odpovedí skóruj cez LLM-sudcu, never jeho zaujatostiam a over ho voči ľuďom, a spusti to v oboch slučkách — offline v CI aj online v produkcii.

Táto stránka to všetko predpokladá a otvára mechaniku pod tým: čo pomenované metriky naozaj počítajú, ako kalibruješ sudcu, ktorému ti Časť 1 kázala neveriť, a ako vznikajú ľudské značky, na ktorých celá tá stavba stojí.

Najprv si vymedzme jednu hranicu. Táto stránka je o meraní, nie o oprave pipeline. Páky, ktoré metrikou pohnú — lepší chunking, reranking, grounding (opretie odpovede o kontext) — patria do vrstiev [Retrieval](../../retrieval/) a [Generation](../../generation/); tu je predmetom skúmania samotný merací prístroj.

A myšlienka, na ktorej celá stránka stojí a ktorú Časť 1 iba naznačila: väčšina moderných RAG metrík je vo vnútri sama LLM-sudcom. Metrika teda dedí sudcovu omylnosť — a práve preto sú kalibrácia a ľudské značky základom každého čísla tu.

## Otvárame čierne skrinky metrík \{#opening-the-metric-black-boxes}

V Časti 1 boli názvy metrík čierne skrinky — „faithfulness“, „answer relevance“ a pár ďalších, menovky, ktorým si veril bez toho, aby si videl dovnútra. Na pokročilej úrovni potrebuješ vedieť, čo každá z nich počíta, lebo výpočet ti povie, čo dané číslo dokáže a čo nedokáže zachytiť. A každá z týchto metrík má zdokumentované slepé miesto, ktoré jej názov zakrýva.

Referenčná implementácia, o ktorej sa oplatí uvažovať, je **Ragas** — framework, ktorý zaviedol tento rozklad evaluácie RAG na pomenované, samostatne počítané metriky (Es a kol., „Ragas: Automated Evaluation of Retrieval Augmented Generation“, arXiv 2309.15217, september 2023). Že to pomenúvame, nie je formalita: tieto štyri metriky sú štandardný spôsob, akým odbor problém rozkrája — rozklad, na ktorom sa zhodol, nie súkromný recept jedného dodávateľa.

Pozeraj sa na tú štvoricu cez dve osi. **Os 1** (Časť 1 ju už načrtla): ktorú etapu metrika sleduje — context precision (presnosť kontextu) a context recall (úplnosť kontextu) hodnotia vyhľadávanie, faithfulness a answer relevance hodnotia generovanie. **Os 2** (Časť 1 ju nechala nevypovedanú, hoci v praxi rozhoduje): či metrika potrebuje referenciu — človekom napísanú správnu odpoveď — alebo si vystačí so samotnou otázkou, kontextom a odpoveďou.

| | reference-free (bez etalónu) | reference-based (s etalónom) |
|---|---|---|
| **Vyhľadávanie** | context precision (o relevantnosti rozhoduje LLM) | context recall |
| **Generovanie** | faithfulness, answer relevance | — |

Ten rozdiel poriadne zaváži. Faithfulness a answer relevance bežia na živej produkčnej prevádzke bez jedinej označkovanej odpovede; context recall bez referencie nevypočítaš vôbec. Práve táto os rozhoduje, čo kde vieš odmerať — a preto golden set dostáva na konci vlastnú sekciu.

### Faithfulness — grounding ako podiel podložených tvrdení \{#faithfulness--grounding-as-a-claim-level-ratio}

**Faithfulness** je práve to číslo, ktoré Časť 1 aj vrstva Generation stále sľubovali sformalizovať: opiera sa odpoveď o nájdený kontext, alebo sa model zatúlal späť do vlastnej pamäte? Ragas ho počíta v troch krokoch:

1. jeden LLM rozloží vygenerovanú odpoveď na **atomárne tvrdenia** — jednotlivé faktické výroky, ktoré odpoveď obsahuje;
2. druhý prechod LLM overí každé tvrdenie voči nájdenému kontextu jedinou otázkou áno/nie: dá sa toto tvrdenie odvodiť z toho, čo sme našli?;
3. z toho vezme podiel.

*faithfulness = supported claims / total claims*, na škále 0 až 1.

Ragas to ukazuje na príklade: na otázku „Kde a kedy sa narodil Einstein?“ môže odpoveď tvrdiť dve veci — miesto a dátum „14. marca 1879“. Ak kontext podporuje miesto, ale nie dátum, jedno z dvoch tvrdení je podložené a faithfulness je 1/2 = 0,5.

```mermaid
flowchart TB
    A["Vygenerovaná odpoveď"] --> D["Rozlož na atomárne tvrdenia<br/>(LLM rozoberie odpoveď)"]
    D --> V["Over každé tvrdenie voči nájdenému kontextu<br/>(dá sa odvodiť? áno / nie)"]
    V --> R["Faithfulness = podložené tvrdenia / všetky tvrdenia"]
```

A tu je to slepé miesto: faithfulness meria opretie o kontext, nie správnosť. Tvrdenie verne opreté o nesprávny kontext dostane rovnú 1,0 — metrike stačí, že odpoveď vieš vystopovať k tomu, čo sa našlo, aj keď to, čo sa našlo, je nezmysel. A keďže metrika je sama LLM-pipeline (najprv rozlož, potom over), jej číslo nesie aj vlastné chyby sudcu: pokazený rozklad alebo nesprávne posúdené odvodenie posunie skóre, hoci samotná odpoveď je v poriadku.

Faithfulness teda zachytí halucináciu aj prebitie kontextu parametrickou pamäťou — zlyhanie, pred ktorým varovala vrstva Generation. Nesprávnu, ale poctivo podloženú odpoveď však prepustí rovno cez sito. Zaceliť túto medzeru je úloha pre referenciu — o tom nižšie.

### Ako answer relevance ide od odpovede späť k otázke \{#how-answer-relevance-runs-the-question-backwards}

**Answer relevance** meria to, čoho sa faithfulness vôbec nedotkne: či odpoveď naozaj rieši položenú otázku — je k veci a je úplná? Správnosť (correctness) je pritom samostatná os, ktorú zámerne necháva na pokoji.

Ragas ju počíta tak, že otázku spätne zostrojí z odpovede: z vygenerovanej odpovede necháš LLM napísať N umelých otázok (predvolene tri), na ktoré by tá odpoveď bola dobrou odpoveďou. Každú vygenerovanú otázku aj tú pôvodnú zaembedduješ (prevedieš na vektor) a vezmeš **kosínusovú podobnosť** (cosine similarity) každej vygenerovanej k pôvodnej. Answer relevance je priemer týchto podobností.

```text
answer relevance = (1/N) · Σ cos(E_gen_i, E_orig)
```

Intuícia: z naozaj relevantnej odpovede vieš pôvodnú otázku zrekonštruovať — vygeneruješ otázku a skončíš presne tam, odkiaľ si vyšiel, teda pri vysokom kosínuse. Vyhýbavá, natiahnutá alebo polovičná odpoveď plodí otázky, ktoré sa rozídu inam, a priemerná podobnosť klesne. Preto rovnako trestá neúplnosť aj rozvláčnosť — vata rozriedi signál, ktorý by inak ukazoval späť na otázku.

Aj tu ostáva slepé miesto, čestná hranica hodnotenia bez etalónu: answer relevance výslovne neposudzuje faktickú správnosť; je to zhoda v zámere, nič viac. Postav ju vedľa faithfulness a máš celý dosah reference-free hodnotenia: faithfulness potvrdí, že odpoveď je podložená, answer relevance potvrdí, že je k veci. Správnosť je tretia vec a nedosiahne na ňu ani jedna z nich — na tú treba referenciu, známu správnu odpoveď alebo človeka. Žiadna vychytralosť bez etalónu tú medzeru nezacelí; je štrukturálna.

### Prečo context precision záleží na poradí \{#why-context-precision-cares-about-rank-order}

**Context precision** sa presúva na stranu vyhľadávania a kladie ostrejšiu otázku než „koľko z vrátených chunkov bolo relevantných?“. Pýta sa, či sú tie relevantné zoradené navrchu. Je citlivá na poradie, čo obyčajný podiel relevantných nie je.

Počíta sa ako vážený priemer po pozíciách. Na každej pozícii k je Precision@k podiel relevantných spomedzi prvých k vrátených chunkov; každú pozíciu zvážiš tým, či je chunk, ktorý na nej sedí, sám relevantný, sčítaš to po pozíciách a vydelíš celkovým počtom relevantných položiek v top-K (K najlepších).

```text
Context Precision@K = Σ_k (Precision@k · v_k) / (total relevant items in top-K)
```

kde v_k je 1, keď je chunk na pozícii k relevantný, a 0 inak. Vezmi K = 2: relevantný chunk a za ním nerelevantný. Pri v = [1, 0] je skóre (1 × 1 + 0,5 × 0) / 1 = 1,0. Prehoď ich: pri v = [0, 1] je skóre (0 × 0 + 0,5 × 1) / 1 = 0,5. Nič nepribudlo ani neubudlo, zmenilo sa len poradie. Rozhoduje pozícia v poradí.

Toto je práve tá metrika, ktorá odmeňuje prácu rerankera z vrstvy Retrieval: dostať správne chunky do množiny je nevyhnutné, ale context precision skóruje až ich poradie — teda či naozaj skončia navrchu.

### Context recall — tá jediná, čo potrebuje etalón \{#context-recall-is-the-one-that-needs-a-reference}

**Context recall** kladie otázku, na ktorej pri vyhľadávaní záleží najviac: priniesli sme späť všetko, čo správna odpoveď potrebuje? Je to najpriamejšia miera zlyhania vyhľadávania, ktoré Časť 1 pomenovala — potrebný chunk, čo sa nikdy nedostal do výsledkov.

Lenže odpovedať na otázku „vyhľadali sme všetko potrebné?“ si žiada vedieť, čo „všetko potrebné“ vlastne je, a tá znalosť nie je zadarmo: toto je tu jediná **reference-based** metrika — jediná, čo potrebuje referenčnú odpoveď. Počíta sa opäť cez LLM: referenčnú odpoveď (etalón) rozložíš na tvrdenia a pri každom overíš, či sa dá pripísať nájdenému kontextu; z toho vezmeš podiel.

*context recall = supported reference claims / total reference claims*

Časť 1 nazvala recall „hlavnou metrikou pre RAG“ a toto je dôvod: nízky context recall znamená, že generovanie fyzicky nemá ako odpovedať, nech je model akokoľvek dobrý — dôkaz jednoducho nemá pred sebou. A práve táto závislosť od referenčnej odpovede je aj dôvod, prečo golden set nie je pre stranu vyhľadávania luxus navyše: bez neho túto metriku vôbec nevypočítaš.

Odstúp o krok a všimni si vzor v tej štvorici — v ňom je celá pointa. Tri z nich — faithfulness, answer relevance, context recall — sú samy malé LLM-pipeline, ktoré rozkladajú, overujú alebo generujú. *Metrika je sudca.* Číslo (skóre), ktoré ti Ragas vráti, je teda dôveryhodné presne natoľko, nakoľko je dôveryhodný LLM, čo ho počíta — a tým sa „ver metrike“ mení na „ver sudcovi“. Lenže sudcovi, ako Časť 1 povedala bez okolkov, sa na slovo veriť nedá. Ďalšia otázka je preto nevyhnutná: ako kalibruješ sudcu, ktorému ti kázali neveriť?

## Kalibrácia sudcu, ktorému nemáš veriť \{#calibrating-the-judge-you-were-told-to-distrust}

Časť 1 dala pokyn — sudca má zaujatosti, over ho voči ľuďom — ale nechala ho ako číre „čo“. Táto sekcia je „ako“: zaujatosti majú mená aj mechanizmy, existujú dva protokoly skórovania s odlišnými profilmi zlyhania a „over ho voči ľuďom“ je konkrétny postup podložený číslom.

Vychádzame tu z práce, ktorá LLM-as-a-judge ustanovila ako metódu a spísala jej spôsoby zlyhania (Zheng a kol., „Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena“, arXiv 2306.05685, jún 2023).

### Zaujatosti majú mená a každá má svoju nápravu \{#the-biases-have-names-and-each-has-a-mitigation}

**Zaujatosť podľa poradia** (position bias) — sudca uprednostní odpoveď, ktorú vidí ako prvú alebo na pevnom mieste, bez ohľadu na to, ktorá je naozaj lepšia. Náprava je mechanická: každé párové porovnanie spusti v oboch poradiach a víťazstvo počítaj len vtedy, keď verdikt prežije prehodenie. Ak sa s obráteným poradím obráti aj víťaz, rozhodlo poradie, nie kvalita, a výsledok je šum.

**Zaujatosť voči dĺžke** (verbosity bias) — dlhšiu, rozvinutejšiu odpoveď hodnotí vyššie, aj keď tá dĺžka navyše nepridáva nič správne; vata sa číta ako dôkladnosť. Naprávaš ju hodnotiacimi kritériami (rubric), ktoré skórujú obsah, nie objem, a dávaš pozor na príznak: skóre, ktoré kopíruje dĺžku odpovede, je skóre, čo meria nesprávnu vec.

**Self-preference** (uprednostňovanie vlastného štýlu), formálne aj self-enhancement bias — sudca dáva vyššie skóre výstupom vo vlastnom štýle, najmä tým z vlastnej modelovej rodiny. Riešenie: súď modelom z inej rodiny, než je systém, ktorý hodnotíš, alebo zmeraj odchýlku voči ľudským značkám a korekciou ju odčítaj.

Ešte jedna hranica, bez preháňania: článok upozorňuje, že LLM-sudcovia sú slabí hodnotitelia na úlohách, čo si žiadajú náročné uvažovanie alebo matematiku. Sudca je najmenej spoľahlivý presne tam, kde je úloha najťažšia — teda práve tam, kde by si sa oň najradšej oprel. Toto je **strop schopností**, nie posun jedným smerom, tak ho ber oddelene od troch zaujatostí vyššie.

Tie tri zaujatosti majú jednu vlastnosť, ktorú je ľahké pochopiť naopak: sú systematické. Náhodná chyba sa s počtom príkladov vyrovná; systematický posun nie — spusti desaťtisíc porovnaní a position bias nakloní všetkých desaťtisíc na tú istú stranu. Náprava je návrh protokolu a kalibrácia; viac dát s tým nespraví nič.

### Druhý model ešte neznamená druhý mechanizmus \{#a-second-model-is-not-automatically-a-second-mechanism}

Doteraz sme problémy sudcu opisovali ako *zaujatosti* — pomenované systematické posuny, proti ktorým existuje konkrétne opatrenie. Pod nimi leží predpoklad, ktorého sa ani jedna z tých náprav nedotkne a na ktorom stojí celý vzorec: *druhý model znižuje chybovosť len do tej miery, do akej jeho chyby nekorelujú s chybami prvého.*

Kurz AI SDLC rozvíja ten istý argument v plnom rozsahu, len o overovacích bránach, nie o modeloch. Jeho najnáročnejší stupeň existuje práve preto, aby nevznikol „dlhý reťazec s jednotvárnymi mechanizmami, určený iba na splnenie formálnych požiadaviek — šesť brán rovnakého druhu, ktoré sú slepé voči rovnakej triede chýb, a preto proti nej neposkytujú lepšiu ochranu než jediná brána“ ([vrstvené brány a rozmanitosť mechanizmov](/ai-sdlc/part-3-verification/layered-gates)). Na modely sa ten argument prenáša bez zmeny. Dva hraničné modely trénované na prekrývajúcich sa webových korpusoch a s podobnými cieľovými funkciami sú pre množstvo vstupov fakticky **jedným mechanizmom** — a čakaj, že sa najsilnejšie zhodnú práve tam, kde je ich spoločných trénovacích dát najmenej, teda presne na vstupoch, na ktorých ti systém zlyháva. Sudca odpoveď najskôr potvrdí presne tam, kde si potreboval, aby namietol.

Preto je pravidlo o inej modelovej rodine vyššie nevyhnutné, ale nie postačujúce. Odôvodňoval ho self-preference, čiže posun v *štýle*, a iný dodávateľ ho naozaj odstráni. O tom, že dve rôzne rodiny čítali ten istý internet, nehovorí nič. Nezávislosť prináša iný zdroj informácie, nie iný dodávateľ: kontrola opretá o vyhľadaný dokument, ktorý generátor nikdy nevidel, deterministická podmienka, spustiteľný test, validácia voči schéme, ľudská značka. Každý z tých mechanizmov zlyháva inak než jazykový model. Druhý API kľúč nie.

Slovo „nezávislosť“ používa táto príručka pre dve rôzne veci. Pri chain-of-verification z [prehĺbenia vrstvy Generation](../../generation/deep-dive.md) sa overovací krok k pôvodnému návrhu odpovede vôbec nedostane: to je **nezávislosť kontextu**, vnútri jedného modelu, a prináša niečo skutočné. Nie je to **nezávislosť rozdelenia chýb** naprieč modelmi. Tím, ktorý zaviedol chain-of-verification, tým vlastnosť z tejto sekcie nezískal — a práve zámena tých dvoch je to, čím systém skončí s dvomi kontrolami a jedným slepým miestom.

Nič z toho nerobí sudcu nepoužiteľným — na hodnotenie voľného textu vo veľkom je sudca stále jedinou cestou. Mení to, čo z neho smieš tvrdiť. Keď sa sudca s tvojím generátorom zhodne, je to slabý dôkaz; keď sa nezhodne, je to silný dôkaz. Nezhodu používaj ako spúšťač eskalácie a v reťazci drž aspoň jednu bránu, ktorá nie je postavená na jazykovom modeli.

### Dva spôsoby skórovania: jedna odpoveď, alebo dve proti sebe \{#two-ways-to-score-one-answer-at-a-time-or-two-head-to-head}

**Pointwise** (hodnotenie jednej odpovede) podá sudcovi jednu odpoveď a pýta absolútne skóre podľa hodnotiacich kritérií, prípadne s referenciou (referenčná odpoveď sa vezie v sudcovom prompte). Je lacné, škáluje a dáva ti absolútne číslo, na ktoré vieš postaviť prah. Háčik: absolútne skóre pláva — čo dnes sudca nazve sedmičkou, o týždeň môže byť šestka, a zosúladiť tie čísla naprieč behmi je vážne ťažké.

**Pairwise** (párové porovnanie) ukáže sudcovi dve odpovede a pýta sa, ktorá je lepšia alebo či sú nerozhodné. Na zoraďovanie dvoch systémov je spoľahlivejšie — ľudia sa oveľa ochotnejšie zhodnú na „A je lepšia než B“ než na akomkoľvek absolútnom skóre, a sudcovia rovnako — a práve preto je to protokol pre A/B rozhodnutia. Má dve ceny: zoradiť veľa systémov stojí O(n²) porovnaní a je to protokol najviac vystavený position biasu — kvôli čomu preň vznikla tá náprava „prehoď poradie a žiadaj zhodu“.

Voľba teda vyplýva z otázky. Po pairwise siahni, keď sa pýtaš „prekonala verzia B verziu A?“ — výber modelu, A/B test. Po pointwise vtedy, keď potrebuješ absolútny prah „je táto odpoveď dosť dobrá?“ v CI, kde niet druhej odpovede na porovnanie. Reference-guided pointwise je stredná cesta, keď máš etalónové odpovede, ktoré sudcovi predložíš: absolútne skórovanie ukotvené v známej správnej odpovedi.

### Čo naozaj znamená „kalibrovať voči ľuďom“ \{#what-calibrate-against-humans-actually-means}

Kalibrácia je krok, ktorý sudcovej škále dodá platnosť. Skôr než jeho číslam uveríš na tisícoch príkladov, zmeriaš jeho zhodu s ľudskými značkami na vzorke — ako často sa sudca a človek zhodnú na tom istom verdikte.

Číslo, ktoré sa oplatí nosiť v hlave, určuje čestný strop: silní sudcovia (v experimentoch článku GPT-4) dosahujú nad 80% zhody s ľudskými preferenciami — zhruba toľko, koľko je zhoda medzi dvoma nezávislými ľuďmi. Čítaj to správne: sudca je tu asi taký konzistentný ako človek, nič viac. Získaš tým škálu — ten istý úsudok na ľudskej úrovni, nasadený na objem, aký by žiadny ľudský tím nezvládol.

Postup z toho vyplýva priamo: odlož si časť ľuďmi označkovaných príkladov, na nej zmeraj zhodu sudcu s človekom a pri pairwise aj konzistentnosť pri prehodení poradia. Ak zhoda prekročí tvoju latku, sudcu nasadíš na objem, aký by nijaký ľudský tím neoznačkoval. Ak neprejde, oprav hodnotiace kritériá, prepni protokol alebo vymeň model sudcu — a než mu uveríš, zmeraj to znova. Kalibruješ voči golden setu — poslednému dieliku, o ktorý sa všetko ostatné potichu opieralo.

Tri výhrady na záver:

1. absolútne skóre nekalibrovaného sudcu sú neukotvené čísla, kým ľudská vzorka nepovie inak — neber ich za bernú mincu;
2. sudca z tej istej modelovej rodiny ako hodnotený systém sa môže prevážiť na self-preference — pri každom tesnom porovnaní drž tie dva v rôznych rodinách;
3. párové zoraďovanie mnohých systémov ťahá so sebou aj nárast O(n²), aj position bias — počítaj s oboma, skôr než po ňom siahneš.

## Ľudské značky, na ktorých všetko stojí \{#the-human-labels-everything-rests-on}

Vráť sa po oboch niťach naspäť a obidve ťa dovedú na to isté miesto. Reference-based metrika (context recall) potrebuje etalónovú odpoveď; sudca, nech beží akýmkoľvek protokolom, potrebuje na kalibráciu zhodu s človekom. Oboje sa opiera o ten istý základ — ľuďmi označkovaný etalón, teda golden set.

Časť 1 povedala, že ho postavíš ručne alebo synteticky a že čistý poráža veľký. Tu je, ako sa naozaj stavia do podoby, voči ktorej sa dá kalibrovať.

### Ako sa stavia golden set \{#building-the-golden-set}

Príklad v golden sete je otázka spárovaná s referenciou: relevantné chunky, správna odpoveď, alebo oboje. Vedú k nemu dve cesty.

**Ručne písané** sady, ktoré tvoria doménoví experti, majú najvyššiu kvalitu a vznikajú najpomalšie.

**Syntetické** sady necháš vygenerovať LLM — dvojice otázka–odpoveď nad tvojím korpusom — a potom postavíš k prehliadke a úprave každej dvojice **human-in-the-loop** (HITL), teda schválenie človekom. Syntetická cesta zoškáluje generovanie, ale práve tá ľudská brána mení výstup modelu na etalón: neprekontrolovaná syntetická sada je len ďalší výstup modelu preoblečený za referenciu.

Tu prestáva byť „kvalita nad objemom“ heslom a dostáva svoj dôvod. Golden set je meradlo, o ktoré sa opiera každé ostatné číslo. Chyba v meradle neostane sedieť na mieste — pokazí každú metriku počítanú voči nemu aj každého sudcu kalibrovaného voči nemu, a spraví to neviditeľne, lebo pokazené čísla stále vyzerajú ako čísla. Malá, čistá sada reprezentatívna pre doménu poráža veľkú a zašumenú preto, že šum v prístroji sa bez obmedzenia prenesie na všetko, čoho sa prístroj dotkne.

### Ako vieš, že značkám sa dá veriť: inter-annotator agreement \{#knowing-the-labels-are-trustworthy-inter-annotator-agreement}

Vnútri slova „ľuďmi označkovaný“ sa skrýva problém: ak dvaja experti prečítajú tú istú odpoveď a nezhodnú sa, či je správna, tá značka si názov etalón ešte nezaslúžila — je to mienka jedného experta.

Preto ten nesúlad zmeriaš, cez **inter-annotator agreement** (IAA), zhodu medzi anotátormi: mieru, do akej nezávislí anotátori priradia rovnaké značky. Nesú ju dve štandardné štatistiky a glosár drží ich kanonické zdroje.

- **Cohenova kappa** (Cohen's kappa) — zhoda medzi dvoma anotátormi opravená o náhodu. Surové percento zhody ti lichotí, lebo istá časť každej zhody padne čírou náhodou; kappa práve tú náhodou očakávanú časť odčíta.

  *κ = (p_o − p_e) / (1 − p_e)*, kde p_o je pozorovaná zhoda a p_e zhoda očakávaná náhodou.
- **Fleissova kappa** (Fleiss' kappa) rozširuje tú istú myšlienku na viac než dvoch anotátorov.

Prečo si oprava o náhodu zaslúži miesto: na binárnej značke správne/nesprávne sa dvaja anotátori zhodnú zhruba v polovici prípadov už len hodom mincou, takže „zhodli sme sa v 80% prípadov“ môže byť slabý výsledok, keď odčítaš tých približne 50%, ktoré by ti aj tak nadelila náhoda.

Nízka kappa ukazuje na hodnotiace kritériá: pokyny na značkovanie sú natoľko nejednoznačné, že ich dvaja pozorní ľudia čítajú rôzne. Náprava je pokyny zostriť a označkovať znova — brať nesúlad ako signál, ktorým je, nie prehlasovať toho, kto sa odchýlil. Je to tá istá disciplína hodnotiacich kritérií, akú si žiadal sudca v predošlej sekcii, a symetria je presná: nejednoznačné kritériá otrávia ľudské značky aj LLM-sudcu jedným a tým istým spôsobom.

### Kam míňať ľudský rozpočet, aby sa to vrátilo \{#spending-the-human-budget-where-it-pays}

Ľudské značky potrebuješ na dve rôzne úlohy. Pri **active sampling** (aktívnom vzorkovaní) vyberáš neisté odpovede, prípady, v ktorých sa sudcovia nezhodli, a nové zlyhania. Pomáhajú ti spresniť hodnotiace kritériá, doplniť golden set a zlepšiť sudcu. Ak však chceš odhadnúť, ako často systém zlyháva v celej prevádzke, potrebuješ náhodnú vzorku z presne vymedzenej populácie. Podiel chýb medzi cielene vybranými prípadmi by tento odhad skreslil. Oba účely preto rozlišuj pri výbere aj pri zobrazovaní výsledkov.

### Ponechaj si náhodnú vzorku z celej populácie \{#preserve-a-population-sample}

Predstav si, že za týždeň pribudne 56 000 záznamov a na kontrolu máš rozpočet 300 prípadov. Môžeš z neho vyhradiť 150 na rovnomerný náhodný výber zo všetkých záznamov za daný týždeň, 100 na rizikové akcie a 50 na prípady, v ktorých sa sudcovia nezhodli. Je to názorné rozdelenie rozpočtu, nie všeobecne optimálny pomer. Pri každom výbere zaznamenaj časové vymedzenie a veľkosť populácie, pravidlo výberu, vrstvu a pravdepodobnosť zaradenia do vzorky. Odstráň duplicity medzi skupinami tak, aby si náhodnú časť potichu nenahradil prípadmi vybranými podľa spúšťacej podmienky. Kontroluj úspešné aj neúspešné prípady. Náhodná časť ti umožní odhadnúť chybovosť v populácii; cielené časti pomôžu nájsť chyby na opravu.

Aj stratifikovaným výberom môžeš odhadovať chybovosť v celej populácii. V každej vrstve vyberaj náhodne a jej nameranú chybovosť váž podielom tejto vrstvy v populácii. Ak rizikové prípady tvoria 10% prevádzky, ich chybovosť má váhu 0,1, aj keby si im venoval polovicu kontrol. Prostý priemer zo skontrolovaných prípadov by ich zastúpenie nadhodnotil. Ak nepoznáš pravdepodobnosti výberu ani nemáš zachovanú náhodnú časť, uvádzaj len chybovosť cielenej vzorky. Rovnako postupuj pri [prioritne uchovávaných tracoch](../observability/deep-dive.md#you-cannot-keep-every-trace): prednostné ukladanie chýb pomáha pri ladení, ale z takýchto záznamov bez váženia neurčíš chybovosť celej prevádzky.

### Zachytiť chybu a presne odhadnúť chybovosť sú dve rôzne úlohy \{#detection-is-different-from-precise-estimation}

Pri *n* nezávislých náhodných výberoch s rovnakou pravdepodobnosťou zlyhania *p* je pravdepodobnosť, že zachytíš aspoň jedno zlyhanie, `1 − (1 − p)^n`. Tento binomický model je užitočnou aproximáciou, ak vzorka tvorí malú časť populácie. Pre výber bez vrátenia z konečnej populácie je presným modelom hypergeometrické rozdelenie. Záznamy z toho istého incidentu, od toho istého zákazníka alebo vytvorené podľa rovnakej šablóny môžu spolu súvisieť; rovnaký počet takýchto záznamov poskytuje menej nezávislých informácií.

Ak je skutočná chybovosť 1%, pri 200 kontrolách očakávaš v priemere dve zlyhania a pravdepodobnosť zachytenia aspoň jedného je **86,6%**. Chybu teda vieš zachytiť pomerne často, no jej početnosť odhadneš nepresne. Ak nájdeš presne 2 chyby z 200, približný 95% Wilsonov interval spoľahlivosti je **0,27%–3,57%**. Ani nulový počet nájdených chýb nedokazuje nulovú chybovosť. Ak chceš mať pri zadanej chybovosti 95% pravdepodobnosť zachytenia aspoň jednej chyby, vypočítaj `n ≥ ln(0.05) / ln(1 − p)` a zaokrúhli nahor: pri 1% potrebuješ **299** kontrol, pri 0,25% ich potrebuješ **1 197**. Pri 300 kontrolách a chybovosti 0,25% je pravdepodobnosť zachytenia **52,8%** — chybu môžeš nájsť, ale nemôžeš sa na to spoľahnúť.

Interval spoľahlivosti vyjadruje neistotu odhadu spôsobenú výberom vzorky. Pri opakovanom vzorkovaní by postup na výpočet 95% intervalu zahrnul pevnú skutočnú chybovosť približne v 95% prípadov. Pri malom počte chýb použi Wilsonov alebo exaktný binomický interval namiesto symetrickej aproximácie normálnym rozdelením. Napríklad 28 chýb zo 400 kontrol znamená 7%, s približným 95% Wilsonovým intervalom **4,89%–9,93%**. Samotné bodové odhady okolo 6%, 7% a 8% z oddelených vzoriek tejto veľkosti ešte nedokazujú trend. Pred porovnaním verzií si urči najmenšiu zmenu, ktorú potrebuješ zachytiť, hladinu významnosti a štatistickú silu testu; podľa nich vypočítaj potrebnú veľkosť vzorky. Vzorec pre zachytenie aspoň jednej chyby rieši inú otázku. Ak verzie skúšaš na rovnakých vstupoch, porovnávaj spárované prípady a toto párovanie zohľadni aj pri analýze.

Vopred si stanov aj obdobie kontroly a pravidlo vyhlásenia poplachu. Ak denne opakuješ test, kým niektorý interval nezačne vyzerať znepokojivo, zvyšuješ pravdepodobnosť falošného poplachu. Použi porovnanie v určenom čase alebo sekvenčný postup, ktorý s opakovaným sledovaním počíta. Interval pritom zachytáva iba neistotu z výberu vzorky. Aj úzky interval môže zavádzať, ak bol výber skreslený, ľudia pri značkovaní prehliadli chyby alebo vzorka nezodpovedá populácii, o ktorej chceš rozhodovať.

Cielené značkovanie využi na opravy a prípady zlyhania po vyriešení nezhôd medzi anotátormi uchovaj ako nemenné regresné prípady. Na kalibráciu sudcu si odlož samostatnú ľuďmi označkovanú vzorku. Sleduj na nej zhodu sudcu s ľuďmi aj zastúpenie jednotlivých tried zlyhaní a obnov ju, keď sa zmení model, hodnotiace kritériá, korpus alebo požiadavky z produkcie. [Lekcia o kapacite ľudskej kontroly](/ai-sdlc/part-3-verification/review-at-volume#budget-reviewer-minutes-before-routing-work) pridáva ďalšiu podmienku: aj štatisticky užitočnú vzorku musí mať kto a kedy skontrolovať.

## Čo si odniesť z lekcie \{#what-to-take-away}

- Štyri metriky Ragas prestanú byť čiernymi skrinkami, len čo uvidíš ich aritmetiku: faithfulness je podiel podložených tvrdení zo všetkých; answer relevance je priemerný kosínus medzi pôvodnou otázkou a otázkami, ktoré z odpovede zregeneruje LLM; context precision je presnosť vážená poradím; context recall je podiel podložených referenčných tvrdení zo všetkých.
- Organizujú ich dve osi — etapa (vyhľadávanie verzus generovanie) a bez etalónu verzus s etalónom. Faithfulness a answer relevance nepotrebujú etalónovú odpoveď a bežia na živej prevádzke; context recall bez referencie nevypočítaš.
- Tri zo štyroch metrík sú samy LLM-pipeline, takže metrika je sudca a dedí jeho omylnosť — a to je celý dôvod, prečo kalibrácia nie je nadštandard.
- Metriky bez etalónu ťa dovedú len po istú hranicu: faithfulness potvrdí „podložené“, answer relevance potvrdí „k veci“, správnosť nepotvrdí ani jedna. Na tú treba referenciu alebo človeka.
- Zaujatosti sudcu sú systematické, takže viac príkladov ich nevymyje: position bias (spusti obe poradia a žiadaj zhodu), verbosity bias aj self-preference si každá pýta protokol alebo kalibračnú nápravu.
- Pod pomenovanými zaujatosťami leží predpoklad, ktorého sa ani jedna z nich nedotkne: druhý model pomôže len vtedy, keď jeho chyby nekorelujú s chybami prvého — a dva hraničné modely trénované na prekrývajúcich sa korpusoch majú k jednému mechanizmu blízko. Nezávislosť preto prináša iný zdroj informácie (opretá kontrola, test, schéma, človek), nie iný dodávateľ.
- Pairwise zoradí dva systémy spoľahlivejšie, ale stojí O(n²) a je najviac vystavené position biasu; pointwise ti dá absolútny prah do CI; tak či onak kalibruješ voči ľuďom a sudca triedy GPT-4 sa zastaví zhruba na ľudskej úrovni zhody — nad 80%, nie na úrovni orákula.
- Golden set je meradlo, na ktorom všetko stojí: meraj zhodu medzi anotátormi kappou opravenou o náhodu, rozdeľ vzácny ľudský rozpočet medzi cielené hľadanie chýb a náhodný audit a prekalibruj, keď sa posunie model, korpus alebo otázky.

**[Nové pojmy](../../../glossary.md#evaluation)**: context precision, context recall, faithfulness, answer relevance, reference-free vs reference-based, LLM-judge calibration, position bias, verbosity bias, self-preference / self-enhancement bias, pointwise vs pairwise, inter-annotator agreement (Cohen's kappa, Fleiss' kappa), active sampling / active learning, population audit, confidence interval, detection probability, correlated error, context independence vs error-distribution independence.
