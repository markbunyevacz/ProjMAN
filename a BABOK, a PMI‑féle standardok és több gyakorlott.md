<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# a BABOK, a PMI‑féle standardok és több gyakorlott BA‑módszertan is javasol konkrét heurisztikákat arra, hogyan lehet hiányzó attribútumokat következetesen „kibontani” a forrásanyagból. Összegyűjtöttem a legrelevánsabb irányelveket:

BABOK (IIBA Business Analysis Body of Knowledge)
Requirements Analysis and Design Definition – Specify and Model Requirements (4.2)
Követel a követelésekről „gazdag attribútumkészletet” (prioritás, forrás, állapot, kapcsolatok). A BABOK kifejezetten bátorítja:
szabálykatalógusok használatát (pl. domain szabály → kategória besorolás),
pattern alapú felismerést (use case sablonok, user story minták),
metaadatok beemelését (dokumentum author, időbélyegek) a stakeholder‑trackinghez.
Requirements Life Cycle Management – Manage Requirements Traceability (5.1)
Cél az, hogy minden elemhez kapcsolt legyen a „source” (szerző, stakeholder), a „status”, a „priority”, és ezek összeköthetők legyenek projektszintű célokkal. Ha az adat hiányzik:
definíció szerint lehet „Derived or Assumed”, de ezt explicit módon jelölni kell,
kötelező egy „validation check” (Grounding vagy Review) későbbi ellenőrizhetőségre.
Elicitation and Collaboration – Conduct Elicitation (4.3)
A BABOK itt említi a document analysis technikát: a dokumentumok feljegyzéseiből, sablonjaiból, formázásából következtetünk hiányzó információkra. Tipikus heurisztikák:
„due date” → dátumminták keresése határidő kulcsszavakkal („deadline”, „complete by”, „határidő”, „vigyázat dátumdöfés”),
„cost” → valuta + számtalálatok, becsült ráfordítás (órák, FTE), budget sorok,
„category/prioritás” → kulcsszavak („critical”, „must”, „nice to have”), MoSCoW térkép, folyamat-lépcső.
PMI (PMBOK, PMI-ACP)
Product Backlog / Requirements Attributes
A PMBOK (Requirements Management plan) előírja, hogy minden backlog elemhez legyen prioritás, státusz, forrás, becsült erőforrás/ráfordítás. Ha nincs:
Használhatók Scoring Models (szövegből kinyert kockázat/érték score),
WSJF (Weighted Shortest Job First) vagy Value vs. Effort heurisztika: a dokumentumban szereplő érték-növekedés vs. ráfordítás említésekből becsülhető.
Agile (PMI-ACP, SAFe gyakorlat)
Gyakorlatban sok csapat a „Definition of Ready” részeként heurisztikákat használ:
ha nincs explicit határidő, legalább olyan szintű részletesség deriválható, hogy „Q3 release”→ kvartális határidő;
ha nincs költség, legalább „effort t-shirt size” (S/M/L) becslés a dokumentumban található részletek (összetettség, interfészek) alapján;
vendor/szerző: stakeholder mátrix vagy dokumentum metaadat, email aláírás, szerzői mező.
Gyakorlati heurisztikák (a fenti szabványokra támaszkodva)
Az alábbi logikák könnyen automatizálhatók, miközben összhangban vannak a standardokkal:
Kategória (MoSCoW / domain)
Szöveges kulcsszavak: must, critical, blocking → „Must have”; optional, later → „Could have”.
Domain-fókusz kulcsszavak: „compliance”, „risk” → Compliance/Risk kategória.
Kontextus metaadat: dokumentumtípus („Legal Requirements Specification” → jogi kategória).
Prioritás
Kulcsszó leképezés (BABOK Minták): urgent, immediately → High; should, preferred → Medium; optional, nice to have → Low.
Ha semmi sincs: MoSCoW-besorolás átemelése a prioritás mezőbe.
Szállító / Szerző
Dokumentum metaadat (core_props.author, last_modified_by) → BABOK „source” attribútum.
Stakeholder-mátrix (ha az analízismodul már kiemelte a szerzőköt): stakeholders[0].organization.
Határidő
Regex: dátum + „deadline”, „due”, „delivery” kulcsszó ugyanabban a mondatban.
Projekt milestone: „Q4 release”, „Sprint 5” → konvertálható konkrét dátumtartományra (BABOK: Business Rules + calendar).
Ha semmi: PMI javaslat szerint „unset” státusz, de explicit jelölve (pl. dueDate: null, dueStatus: "not set").
Költség
Valuta + szám, ráfordítás kulcsszavak („USD”, „Ft”, „FTE”, „person-hours”).
Dokumentum mérete (pl. BABOK felismeri a „Function Points”, „Story Points” becslést).
Ha van compliance scoring vagy MoSCoW pontszám, átszámítható effort‑heurisztikára (pl. 80% compliance → magas költség).
PMI-féle Relative Weighting vagy WSJF: Cost of Delay / Effort – ha van bármilyen „impact” vs. „effort” információ, abból konzervatív költségcímke generálható (low/medium/high).
Létrehozva / Frissítve
Word metaadat (created, modified), PDF/Excel tulajdonságok.
Email threadből importált követelésnél: a legelső megjelenés dátuma, legutóbbi módosítás.
Ha semmi, minimalista fallback: dokumentum feltöltésének timestamp-je (de jelölve, hogy „system-generated”).
Ezek a módszerek mind „Derived or Assumed” címkével jelennek meg a BABOK-ban – azaz megengedettek, de a BA-nak jeleznie kell, mely adatot inferált és később validáltatni kell a stakeholderrel. A PMI ugyanezt „identified risk / assumption” kategóriába sorolja, így a backlog elemhez társított „assumption log”-ban is illik rögzíteni.
Összességében tehát a szabványok nemcsak engedik a heurisztikus derivációt, hanem kifejezetten javasolják, feltéve hogy:
dokumentáljuk a módszert (szabálykészlet, kulcsszó térkép),
jelöljük az inferred mezőket (pl. _derived: true, confidence: 0.6),
tervbe vesszük a validációt (review, stakeholder megerősítés).
Ha szeretnéd, szívesen segítek kidolgozni konkrét szabálykészletet vagy AI promptot a kódba, csak jelezd, hogy váltsunk agent módra.

Now I have comprehensive research. Let me generate a summary document to provide to the user.

# A BABOK és PMI Standardok Heurisztikus Követelményattribútum-Kibontásának Komplex Elemzése

Az összegyűjtött követelmény-elemzési szabványok, módszertanok és gyakorlati megközelítések alapos áttekintése megerősíti, hogy a BABOK (Business Analysis Body of Knowledge) és a PMI (Project Management Institute) standardjai nemcsak megengedik, hanem kifejezetten támogatják a hiányzó attribútumok heurisztikus kibontását a forrásanyagokból. Az alábbiakban részletesen bemutatjuk ezeket az irányelveket és legjobb gyakorlatokat, amelyek robusztus keretet biztosítanak az Ön által leírt megközelítéshez.

## BABOK Követelmény-attribútumok és Származtatási Elvek

A BABOK v3 a **Requirements Analysis and Design Definition** (Követelmény-elemzés és Tervezési Definíció) tudásterületében kifejezetten foglalkozik a követelmények attribútumainak rögzítésével és kezelésével. A **Specify and Model Requirements** (7.1) feladat világosan előírja, hogy minden követelményhez dokumentálni kell a releváns attribútumokat, még akkor is, ha azokat közvetlenül nem adták meg a stakeholderek.[^1][^2][^3][^4]

### Követelmény-attribútumok Szabványa

A BABOK szerint minden követelményhez kapcsolódnia kell egy "gazdag attribútumkészletnek", amely tartalmazza:[^5][^6][^1]

- **Egyedi azonosító (ID)**: Minden követelmény követhetőségéhez
- **Leírás**: A követelmény szöveges kifejezése
- **Forrás (Source)**: Ki vagy mi szolgáltatta a követelményt
- **Tulajdonos (Owner)**: Ki felelős a követelményért
- **Prioritás (Priority)**: Értékelési skála (általában 1-5)
- **Állapot (Status)**: Életciklus státusz (tervezett, elemzett, jóváhagyott, megvalósított)
- **Kategória/Típus**: Funkcionális, nem-funkcionális, átmeneti stb.
- **Dátumok**: Létrehozás, módosítás dátumai
- **Indoklás (Rationale)**: Miért szükséges ez a követelmény
- **Kapcsolatok**: Más követelményekhez, tervezési elemekhez való kapcsolódások


### Származtatott Követelmények ("Derived or Assumed")

A BABOK kifejezetten elismeri a **származtatott követelmények** (derived requirements) koncepcióját a **Requirements Life Cycle Management** (5.1) fejezetben. Amikor egy attribútum nem áll közvetlenül rendelkezésre, az analizta:[^7][^1]

1. **Származtathatja** más forrásokból (dokumentum metaadat, kontextus, domain szabályok)
2. **Feltételezhet** ésszerű alapon (amely később validálásra kerül)
3. **Explicit módon jelölni kell** ezeket "_derived: true" vagy hasonló mezőkkel[^1][^7]
4. **Dokumentálni kell a módszert**, ahogyan az attribútumot megállapították
5. **Validációt kell tervezni** a stakeholderekkel való későbbi ellenőrzésre[^8][^9]

A **Validate Requirements** (7.3) feladat kimondja, hogy az elemzőnek azonosítania kell az összes feltételezést és biztosítania kell, hogy azokat később validálják.[^9][^10]

## PMI Követelmény-nyomonkövetési Mátrix és Attribútumkezelés

A PMI PMBOK útmutatója a **Requirements Traceability Matrix** (RTM - Követelmény-nyomonkövetési Mátrix) révén még részletesebb útmutatást ad az attribútumokra.[^6][^11][^12][^5]

### RTM Kötelező Attribútumai

A PMI szerint minden követelménynek tartalmaznia kell:[^13][^11][^5][^6]

- **Egyedi azonosító**: Egyértelmű követhetőséghez
- **Szöveges leírás**: A követelmény világos kifejezése
- **Indoklás**: Miért került be (rationale for inclusion)
- **Forrás**: Honnan származik (stakeholder, dokumentum, szabályozás)
- **Tulajdonos**: Ki felelős érte
- **Prioritás**: Általában 1-5 vagy High/Medium/Low skálán
- **Verzió**: Változáskövetéshez
- **Jelenlegi státusz**: Active, Cancelled, Deferred, Added, Approved, Assigned, Completed
- **Dátum**: Létrehozás és módosítás dátumai
- **Nyomonkövetési linkek**: Előre és hátra irányuló kapcsolatok


### Assumption Log és Hiányzó Adatok Kezelése

A PMI bevezeti az **Assumption Log** (Feltételezési Napló) fogalmát, amely a **Develop Project Charter** folyamat kimenetele. Ez a dokumentum rögzíti:[^14][^15][^16][^17]

- Minden **feltételezést** (assumption) - ami igaz**nak vélt**, de még nem megerősített tényező
- Minden **korlátozást** (constraint) - megkötést a megoldásra
- A feltételezés **kockázati szintjét** és **bizonytalanságát**
- A **validációs státuszt**: megerősítve, validálásra vár, vagy megcáfolva[^15][^16][^14]

Amikor egy követelményattribútum hiányzik, a PMI szabvány szerint:

1. **Dokumentálni kell feltételezésként** az Assumption Log-ban
2. **Kockázati értékelést** kell végezni (mivel a feltételezések bizonytalanságot hordoznak)
3. **Validációs tervet** kell készíteni a feltételezés ellenőrzésére
4. **Kapcsolatot** kell létrehozni a követelmény és a feltételezés között[^16][^17][^14][^15]

## Gyakorlati Heurisztikák Szabványalapú Megközelítése

### MoSCoW Prioritizálási Keretrendszer

A MoSCoW módszer az egyik legszélesebb körben elfogadott heurisztikus prioritizálási technika, amelyet mind a BABOK, mind az Agile (PMI-ACP) gyakorlatok támogatnak:[^18][^19][^20][^21][^22][^23]

**Must Have**: Kritikus, projekt sikeréhez elengedhetetlen

- Kulcsszavak: "critical", "must", "mandatory", "essential", "required", "blocking"
- Heurisztika: Ha a dokumentum compliance, regulatory vagy legal kontextusban említi → Must Have

**Should Have**: Nagyon fontos, de nem blokkoló

- Kulcsszavak: "should", "important", "preferred", "expected"
- Heurisztika: Ha a business value magas, de van workaround → Should Have

**Could Have**: Kívánatos, de opcionális

- Kulcsszavak: "could", "nice to have", "optional", "if time permits", "enhancement"
- Heurisztika: Ha a dokumentum "future release" vagy "phase 2" kontextusban említi → Could Have

**Won't Have (this time)**: Most nem implementált

- Kulcsszavak: "later", "future", "not in scope", "deferred", "out of scope"
- Heurisztika: Explicit kizárás vagy későbbi fázisra halasztás → Won't Have

A BABOK kifejezetten ajánlja a MoSCoW használatát a **Prioritize Requirements** tevékenységnél.[^20][^23][^18]

### WSJF (Weighted Shortest Job First) Értékelési Heurisztika

A SAFe (Scaled Agile Framework) által bevezetett WSJF módszer matematikai alapokon nyugvó prioritizálást tesz lehetővé:[^24][^25][^26][^27][^28]

**WSJF Formula**: Cost of Delay / Job Duration

**Cost of Delay** = Business Value + Time Criticality + Risk Reduction/Opportunity Enablement

**Heurisztikák dokumentumból való származtatásra**:

1. **Business Value** → Kulcsszavak: "revenue", "customer satisfaction", "competitive advantage", "market share"
2. **Time Criticality** → Dátumok, határidők: "Q3 release", "by year-end", "regulatory deadline"
3. **Risk Reduction** → "compliance", "security", "risk mitigation", "vulnerability"
4. **Job Duration** → Komplexitás mutatók: interfészek száma, függőségek, technikai összetettség[^26][^27][^28][^24]

Ha nincs explicit érték, konzervatív becslés használható "low/medium/high" címkékkel, amely később finomítható.[^27][^26]

## Attribútum-specifikus Heurisztikák

### Kategória Származtatása

**Domain szabályok alapján**:[^29][^30][^1]

- "compliance", "regulatory", "legal", "GDPR" → Compliance kategória
- "performance", "scalability", "latency" → Non-Functional/Performance
- "user interface", "workflow", "process" → Functional
- "data migration", "training", "cutover" → Transition

**Dokumentumtípus alapján**:[^31][^32]

- Legal Requirements Specification → Legal kategória
- Technical Design Document → Technical követelmények
- User Story → Functional követelmények


### Prioritás Heurisztikái

**Explicit kulcsszavak**:[^23][^18][^20]

- "urgent", "immediately", "ASAP", "critical path" → High Priority (4-5)
- "important", "should", "needed" → Medium Priority (2-3)
- "optional", "nice to have", "enhancement" → Low Priority (1)

**Implicit mutatók**:

- Compliance/szabályozási említés → automatikusan High
- "Future phase" említés → automatikusan Low
- Stakeholder szintje (CEO vs. end-user kérés) → befolyásolja a prioritást


### Szállító/Szerző Kibontása

**Dokumentum metaadat** (BABOK Document Analysis technika):[^32][^31]

- Microsoft Office: `core_props.author`, `core_props.last_modified_by`
- PDF: `/Author`, `/Creator` mezők
- Email: Feladó mező, aláírás elemzése

**Szövegkontextus**:

- "As requested by [Name]" → Stakeholder azonosítása
- "[Organization] requires..." → Szervezet származtatása
- Email thread elemzése → Stakeholder mátrix építése[^33][^34][^35]


### Határidő Heurisztikái

**Regex minták** (BABOK Document Analysis):[^31][^1]```
(deadline|due date|deliver by|complete by|határidő).{0,20}(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})

```

**Projekt milestone kapcsolatok**:

- "Q1 2024", "Sprint 5", "Release 3.0" → Projekt tervből származtatható dátum
- "Before go-live", "Post-migration" → Mérföldkőhöz kötött

**Implicit határidők**:

- Regulatory requirement → Szabályozás hatályba lépési dátuma
- Compliance követelmény → Audit dátum vagy jelentési határidő[^6][^1]

### Költség/Effort Becslés

**Direkt mutatók**:[^24][^26][^27]

- Valuta + szám: "USD 50,000", "€25K", "1.5M Ft"
- Ráfordítás: "40 person-hours", "3 FTE", "2 month effort"
- Story Points vagy Function Points említése

**Indirekt complexity heurisztikák**:

- Interfészek száma (több interfész → magasabb költség)
- Függőségek száma más követelményektől
- Technikai komplexitás kulcsszavak: "integration", "real-time", "distributed"
- BABOK Compliance scoring: Magas compliance → Magas validációs költség[^36]

### Létrehozás/Módosítás Dátumai

**Elsődleges források**:[^5][^1]

- Dokumentum fájl tulajdonságok: Created Date, Modified Date
- Verziókezelő rendszer: Git commit timestamp, SVN revision date
- Email thread: Első említés dátuma, utolsó válasz dátuma

**Fallback megoldás**:

- Ha semmi sem elérhető: Dokumentum feltöltésének rendszer-timestampje
- **Kötelező jelölés**: `dateSource: "system-generated"` vagy `confidence: "low"`[^1]

## Automatizálási Támogatás: NLP és ML Heurisztikák

Modern követelménykezelő rendszerek egyre inkább alkalmazzák a Natural Language Processing (NLP) és Machine Learning (ML) technikákat a heurisztikus attribútum-kibontásra.[^37][^38][^39][^40][^41][^42][^36]

### Named Entity Recognition (NER) Követelményekhez

**Személyek, szervezetek, dátumok azonosítása**:[^43]

```python
# Példa: SpaCy NER használata
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("The Finance Department requires implementation by Q3 2024")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")
# Output: Finance Department - ORG, Q3 2024 - DATE
```


### Supervised Learning Osztályozás

Több tanulmány kimutatja, hogy ML módszerek 90%+ pontosságot érnek el követelmények osztályozásában:[^39][^40][^41][^42][^44][^45]

- **Multinomial Naive Bayes**: Legjobb általános teljesítmény FR/NFR osztályozásra
- **Support Vector Machine (SVM)**: Jó pontosság kis adathalmazon
- **Neural Networks**: Kiváló nagy adathalmazokon (>100K példa)
- **Active Learning**: Csak 50%-a az adathalmaznak szükséges ugyanazon teljesítményhez[^39]


### LLM-alapú Attribútum Extrakció

A GPT-4 és hasonló nagy nyelvi modellek kiemelkedő eredményeket mutatnak:[^46][^47][^36]

- **91% F1-Score** attribútum-érték párok kinyerésére
- **Különösen erős**: String wrangling (95%), Name expansion (98%)
- **Chain-of-Thought prompting**: 40%-kal jobb teljesítmény strukturált feladatoknál[^47][^48][^36]

**Prompt sablon példa követelmény-elemzésre**:[^48][^47]

```
Role: You are an expert Business Analyst following BABOK v3 standards.

Task: Extract the following attributes from the requirement text:
- Category (Functional/Non-Functional/Transition/Compliance)
- Priority (High/Medium/Low) with justification
- Stakeholder/Source
- Due Date (if mentioned)
- Cost indicators (if mentioned)

For each attribute:
1. Provide the extracted value
2. Quote the supporting text from the document
3. Assign a confidence score (0.0-1.0)
4. Mark as "derived" if inferred rather than explicit

Requirement Text: [INSERT TEXT]

Output Format: JSON
```


### Heurisztikus Szabálykészletek Implementálása

Az automatizált rendszerek általában 3-rétegű megközelítést használnak:[^49][^30][^29]

**1. réteg - Explicit kivonás**: Közvetlen regex és keyword matching
**2. réteg - Heurisztikus származtatás**: Szabályalapú következtetés (pl. compliance keyword → High priority)
**3. réteg - ML osztályozás**: Gépi tanulás alapú finomítás és validáció

## Dokumentálási és Validációs Követelmények

### "Derived or Assumed" Címkézés

Mind a BABOK, mind a PMI megköveteli, hogy a származtatott attribútumok explicit jelölést kapjanak:[^7][^8][^14][^15][^1]

**Minimális dokumentáció**:

```json
{
  "requirement_id": "REQ-123",
  "priority": "High",
  "priority_source": "derived",
  "derivation_method": "Compliance keyword heuristic",
  "confidence": 0.75,
  "validation_status": "pending_stakeholder_review",
  "assumption": "Regulatory requirements assumed High priority"
}
```


### Konfidencia Scoring

Bevált gyakorlat minden származtatott attribútumhoz **confidence score** hozzárendelése:[^10][^37][^36]

- **0.9-1.0**: Explicit adat forrásból (dokumentum metaadat)
- **0.7-0.89**: Erős heurisztikus bizonyíték (compliance + high priority keywords)
- **0.5-0.69**: Mérsékelt heurisztikus bizonyíték (domain kategória alapján)
- **0.0-0.49**: Gyenge vagy feltételezett adat (default értékek)

Alacsony konfidenciájú (<0.7) attribútumok prioritást kapnak a stakeholder validációnál.[^10]

### Validációs Workflow

A BABOK **Verify and Validate Requirements** (7.2, 7.3) feladatai előírják:[^8][^9][^10]

1. **Verify**: Formális ellenőrzés - jól van-e dokumentálva?
2. **Validate**: Üzleti érték ellenőrzése - helyes-e az érték?
3. **Stakeholder Review**: Származtatott attribútumok megerősítése
4. **Iteration**: Visszajelzés alapján finomítás
5. **Formal Approval**: Baselined követelmények jóváhagyása

**Validációs checklist** származtatott attribútumokhoz:[^23][^8]

- [ ] Dokumentált-e a származtatási módszer?
- [ ] Van-e confidence score?
- [ ] Azonosított-e review-ra váró státuszban?
- [ ] Stakeholder review tervezve?
- [ ] Assumption Log-ban rögzítve (ha releváns)?


## Requirements Baseline és Change Control

### Baseline Létrehozása

A PMI és BABOK egyaránt megkövetelinek a **Requirements Baseline** létrehozását, mielőtt a követelmények implementációba kerülnének:[^50][^51][^52][^53][^54]

**Baseline létrehozásának lépései**:[^51]

1. **Requirements Documentation**: Minden követelmény dokumentálva, attribútumokkal
2. **Review and Validation**: Stakeholder review, validáció
3. **Formal Approval**: Hivatalos jóváhagyás (aláírás, elektronikus jóváhagyás)
4. **Version Control**: Verzió 1.0 létrehozása és verziókezelő rendszerbe helyezése
5. **Change Management Implementation**: Change control folyamat aktiválása

**Baseline attribútumai** minden követelményre:[^52][^50][^51]

- Baseline Version (pl. v1.0)
- Baseline Date
- Approval Status
- Approved By (stakeholder lista)


### Change Control Származtatott Attribútumokra

Ha egy származtatott attribútum később módosításra kerül (pl. stakeholder validáció után):[^55][^56][^50]

1. **Change Request** létrehozása
2. **Impact Assessment**: Hatásvizsgálat (scope, schedule, cost)
3. **Change Control Board (CCB)** review
4. **Approval/Rejection** döntés
5. **Baseline Update** (ha jóváhagyott)
6. **Traceability Update**: RTM frissítése az új attribútummal

## Szabálykészlet Kidolgozása AI/Automatizációhoz

### Strukturált Heurisztikus Motor Architektúra

**Rule Engine komponensek**:

```
Input Layer:
├── Document Parser (Word, PDF, Excel, Email)
├── Metadata Extractor
└── Text Preprocessor (NLP pipeline)

Heuristic Layer:
├── Category Rules (keyword dictionaries, domain patterns)
├── Priority Rules (MoSCoW mapping, urgency detection)
├── Stakeholder Rules (NER, email parsing, org chart lookup)
├── Date Rules (regex patterns, milestone mapping)
├── Cost Rules (currency detection, effort indicators)
└── Confidence Scorer

Validation Layer:
├── Consistency Checker (cross-attribute validation)
├── Completeness Checker (required fields)
├── Quality Scorer (BABOK quality characteristics)
└── Assumption Logger

Output Layer:
├── Requirements Database
├── Traceability Matrix
├── Assumption Log
└── Validation Report
```


### Példa Szabálykészlet (Category Heuristics)

```yaml
category_rules:
  compliance:
    keywords: ["GDPR", "compliance", "regulatory", "legal", "audit", "SOX", "HIPAA"]
    confidence: 0.9
    priority_override: "High"
  
  functional:
    keywords: ["user shall", "system shall", "function", "feature", "workflow"]
    confidence: 0.8
  
  non_functional:
    subcategories:
      performance:
        keywords: ["response time", "throughput", "latency", "performance"]
        confidence: 0.85
      security:
        keywords: ["authentication", "authorization", "encryption", "security"]
        confidence: 0.9
        priority_override: "High"
      usability:
        keywords: ["user interface", "UX", "accessibility", "ease of use"]
        confidence: 0.75
  
  transition:
    keywords: ["migration", "training", "cutover", "deployment", "rollout"]
    confidence: 0.8
```


### AI Prompt Sablon Heurisztikus Kibontásra

**Zero-shot + Chain-of-Thought megközelítés**:[^36][^47][^48]

```
System: You are a Business Analyst AI following BABOK v3 and PMI PMBOK standards.

Context: You are analyzing a requirement from a [DOCUMENT_TYPE] document.

Requirement Text:
"""
[REQUIREMENT_TEXT]
"""

Document Metadata:
- Author: [AUTHOR]
- Created: [DATE]
- Modified: [MODIFIED_DATE]
- Document Type: [TYPE]

Task: Extract and derive the following attributes using BABOK-compliant heuristics:

1. CATEGORY
   - Analyze keywords for: Functional, Non-Functional (Performance/Security/Usability), 
     Transition, Compliance
   - Consider document context and domain
   - Output: Category name, confidence (0-1), supporting evidence

2. PRIORITY (MoSCoW)
   - Identify urgency keywords (critical, urgent, optional, etc.)
   - Check for compliance/regulatory context (auto-High)
   - Consider "future phase" mentions (auto-Low)
   - Output: Must/Should/Could/Won't, confidence, reasoning

3. STAKEHOLDER/SOURCE
   - Extract from text ("as requested by", "required by")
   - Use document metadata (author, email sender)
   - Output: Name/Role/Organization, confidence, source

4. DUE DATE
   - Regex search for dates with deadline keywords
   - Check for milestone references (Q3, Sprint 5)
   - Output: Date or date range, confidence, source

5. COST/EFFORT INDICATORS
   - Currency + number patterns
   - Effort mentions (person-hours, FTE)
   - Complexity indicators (# of interfaces, dependencies)
   - Output: Estimated cost/effort, confidence, calculation method

For each attribute:
- If explicitly stated: confidence = 0.9-1.0, mark as "explicit"
- If derived via strong heuristic: confidence = 0.7-0.89, mark as "derived"
- If weakly inferred: confidence = 0.5-0.69, mark as "assumed"
- If missing: leave null, document in assumption log

Output Format:
```

{
"requirement_id": "auto-generated",
"attributes": {
"category": {"value": "...", "confidence": 0.x, "source": "...", "method": "..."},
"priority": {"value": "...", "confidence": 0.x, "source": "...", "method": "..."},
...
},
"assumptions": [],
"validation_needed": []
}

```
```## Összefoglalás és Implementációs Ajánlások

### Kulcsfontosságú Elvek

1. **Megengedett és támogatott**: Mind a BABOK, mind a PMI kifejezetten támogatja a heurisztikus attribútum-származtatást, feltéve hogy dokumentált és validált[^9][^7][^8][^1]

2. **Explicit jelölés kötelező**: Minden származtatott/feltételezett adat "derived" vagy "assumed" jelölést kell kapjon, confidence score-ral[^7][^36][^1]

3. **Validation tervezése**: A származtatott attribútumok stakeholder validációját előre be kell ütemezni[^8][^9][^10]

4. **Assumption Log integráció**: A feltételezéseket az Assumption Log-ban kell rögzíteni kockázatkezelési céllal[^14][^15][^16]

5. **Traceability biztosítása**: Az RTM-nek tükröznie kell a származtatási módszert és forrásokat[^11][^57][^58][^5][^6]

### Ajánlott Implementációs Folyamat

**1. Szabálykészlet Fejlesztés**
- Készítsen átfogó heurisztikus szabálykönyvet minden attribútumtípushoz
- Dokumentálja a confidence scoring logikát
- Tesztelje mintadokumentumokon és finomítsa

**2. Automatizációs Réteg**
- Implementáljon rule-based első réteget (regex, keyword matching)
- Adjon hozzá NLP/ML második réteget (NER, osztályozás)
- Opcionálisan: LLM harmadik réteg (GPT-4) komplex esetekhez

**3. Validációs Workflow**
- Confidence threshold: <0.7 → kötelező stakeholder review
- Assumption Log automatikus populálása
- Review meeting ütemezése származtatott attribútumokra

**4. Baseline és Change Control**
- Követelmények baseline-olása validáció után
- Formális change control származtatott attribútumok módosításához
- Verziókezelés és audit trail fenntartása

**5. Folyamatos Fejlesztés**
- Visszajelzések gyűjtése validációkból
- Heurisztikák finomítása a tapasztalatok alapján
- ML modellek újratanítása új adatokon

### További Források és Szabványok

A következő szabványok és útmutatók nyújtanak további támogatást:

- **BABOK v3**: Fejezet 7 (Requirements Analysis and Design Definition)[^2][^3][^4][^1]
- **PMBOK Guide**: Requirements Management Plan, RTM[^11][^5][^6]
- **PMI-PBA**: Professional in Business Analysis, Requirements Baseline[^51]
- **SAFe**: WSJF prioritization, Agile requirements[^26][^27][^24]
- **ISO/IEC 29148**: Systems and software engineering - Life cycle processes - Requirements engineering

Ezek a szabványok együttesen robusztus, iparági szempontból elfogadott keretet biztosítanak a hiányzó követelményattribútumok heurisztikus kibontásához, miközben biztosítják a nyomonkövethetőséget, validálhatóságot és a projektmenedzsment bevált gyakorlatokkal való összhangot.

Ha konkrét kódimplementációra, prompt engineering sablonokra vagy specifikus szabálykészlet kidolgozására van szükség, szívesen segítek a részletesebb technikai specifikáció elkészítésében.
<span style="display:none">[^59][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^70][^71][^72][^73][^74][^75][^76][^77][^78][^79][^80][^81][^82][^83][^84][^85][^86][^87][^88]</span>

<div align="center">⁂</div>

[^1]: https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/7-requirements-analysis-and-design-definition/7-1--specify-and-model-requirements/
[^2]: https://learn.ztu.edu.ua/pluginfile.php/336274/mod_resource/content/1/BABOK_Guide_v3_Member.pdf
[^3]: https://davidodepidan.com/wp-content/uploads/2024/06/BABOK-Final-Series-6.pdf
[^4]: https://business-analysis-excellence.com/wp-content/uploads/2020/05/Week-5-Requirements-Analysis-and-Design-Study-Notes.pdf
[^5]: https://www.projectengineer.net/guide-to-requirements-management/
[^6]: https://www.managementyogi.com/2022/01/pmp-protein-requirements-management-and-requirements-traceability-matrix.html
[^7]: https://www.linkedin.com/pulse/babok-v3-terms-confuse-us-most-ln-mishra-cbap-aac
[^8]: https://www.bridging-the-gap.com/what-are-your-requirements-verification-practices-babok-6-5/
[^9]: https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/7-requirements-analysis-and-design-definition/7-3-validate-requirements/
[^10]: https://www.bridging-the-gap.com/validate-requirements-babok-6-6/
[^11]: https://www.invensislearning.com/blog/requirements-traceability-matrix/
[^12]: https://www.leancxscore.com/the-requirements-traceability-matrix-project-management-key-concepts/
[^13]: https://pmp-tools.com/2023/02/requirements-traceability-matrix.html
[^14]: https://www.reddit.com/r/pmp/comments/jul1lg/assumption_log_not_an_op_for_collect_requirements/
[^15]: https://www.linkedin.com/pulse/assumption-log-example-what-how-write-sunil-kumar-dash-itil-4--qo7fc
[^16]: https://brainsensei.com/glossary/assumption-log/
[^17]: https://www.invensislearning.com/blog/how-to-collect-requirements/
[^18]: https://www.linkedin.com/pulse/understanding-moscow-technique-business-analysis-erfan-zangeneh-cbap--vccqf
[^19]: https://xmind.com/blog/moscow-prioritization-method
[^20]: https://activecollab.com/blog/project-management/moscow-method
[^21]: https://agilemania.com/moscow-prioritization-method
[^22]: https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html
[^23]: https://babokpage.wordpress.com/reqan/
[^24]: https://www.productplan.com/glossary/weighted-shortest-job-first/
[^25]: https://productschool.com/blog/product-fundamentals/wsjf-agile
[^26]: https://www.simplilearn.com/what-is-wsjf-weighted-shortest-job-first-in-agile-article
[^27]: https://clickup.com/blog/wsjf-agile/
[^28]: https://success.atlassian.com/solution-paths/quarterly-planning-guidance-with-jira-cloud/prepare-for-a-program-increment-pi-planning-event/how-to-configure-weighted-shortest-job-first-wsjf-to-work-items
[^29]: https://www.scitepress.org/papers/2017/62804/62804.pdf
[^30]: https://www.academia.edu/34494223/Application_of_Heuristics_in_Business_Process_Models_to_Support_Software_Requirements_Specification
[^31]: http://www.bawiki.com/wiki/Document-Analysis.html
[^32]: https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-18-document-analysis/
[^33]: http://www.bawiki.com/wiki/Stakeholder-Identification.html
[^34]: https://www.bridging-the-gap.com/let-your-stakeholders-know-you-heard-them-babok-3-3-3-4/
[^35]: https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-43-stakeholder--list-map-or-personas/
[^36]: https://arxiv.org/html/2403.02130v1
[^37]: https://aclanthology.org/2025.acl-long.85.pdf
[^38]: https://dl.acm.org/doi/10.1145/1147234.1147241
[^39]: https://werpapers.dimap.ufrn.br/papers/WER2025/wer202501.pdf
[^40]: https://www.csl.mtu.edu/classes/cs4760/www/projects/s22/grad3/www/HCI_Topic_Paper_Saket.pdf
[^41]: https://ieeexplore.ieee.org/document/9307778/
[^42]: https://www.sciencedirect.com/science/article/abs/pii/S0950584922000428
[^43]: https://www.geeksforgeeks.org/nlp/information-extraction-in-nlp/
[^44]: https://dl.acm.org/doi/10.1007/s42979-025-04158-z
[^45]: https://onlinelibrary.wiley.com/doi/full/10.1155/2024/4955691
[^46]: https://www.solita.fi/blogs/unlocking-the-power-of-chatgpt-for-rapid-requirements-extraction/
[^47]: https://www.linkedin.com/pulse/prompt-engineering-automating-software-requirements-analysis-parra-7bave
[^48]: https://www.accelirate.com/prompt-engineering-guide-for-developers/
[^49]: https://thesai.org/Downloads/Volume12No10/Paper_82-Heuristic_Algorithm_for_Automatic_Extraction_Relational_Data.pdf
[^50]: https://www.projex.com/pmp-change-control/
[^51]: https://trustedinstitute.com/concept/pmi-pba/requirements-traceability-monitoring/requirements-baselining/
[^52]: https://project-management.info/performance-measurement-baseline/
[^53]: https://projectmanagementacademy.net/resources/blog/schedule-baseline/
[^54]: https://tensix.com/3-types-of-project-baseline/
[^55]: https://www.linkedin.com/pulse/change-control-project-management-important-pmp-exam-topic-bansal-3p5kc
[^56]: https://pmi.hu/en/blog/change-management-in-project-management--22524
[^57]: https://www.ketryx.com/blog/best-practices-for-maintaining-a-requirement-traceability-matrix-in-agile
[^58]: https://www.jamasoftware.com/requirements-management-guide/requirements-traceability/four-best-practices-for-requirements-traceability/
[^59]: https://techcanvass.com/blogs/types-of-requirements-as-per-babok.aspx
[^60]: https://trustedba.com/requirements-101-part-2/
[^61]: https://www.bizanalysis.org/en/quality-solution-requirements/
[^62]: https://www.watermarklearning.com/blog/babok-techniques/
[^63]: https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/
[^64]: https://fibery.io/blog/product-management/wsjf/
[^65]: https://scrum-master.org/en/what-is-wsjf-weighted-shortest-job-first-safe/
[^66]: https://www.sciencedirect.com/science/article/abs/pii/S0169023X0900144X
[^67]: https://aoteastudios.com/2012/02/the-babok-requirements-analysis/
[^68]: https://careerfoundry.com/en/blog/product-management/how-to-use-wsjf/
[^69]: https://pubmed.ncbi.nlm.nih.gov/23320748/
[^70]: https://www.modernanalyst.com/Careers/InterviewQuestions/tabid/128/ID/1364/How-is-the-Requirements-Analysis-knowledge-area-of-the-BABOK-v20-defined.aspx
[^71]: https://it.nv.gov/uploadedFiles/ITnvgov/Content/Sections/IT-Investments/Lifecycle/BABOKV1_6.pdf
[^72]: https://onlinelibrary.wiley.com/doi/full/10.1155/je/8287518
[^73]: http://acta.bibl.u-szeged.hu/30839/1/actacyb_20_3_2012_4.pdf
[^74]: https://www.sciencedirect.com/science/article/pii/S0164121224000244
[^75]: https://github.com/AleksandarMitrevski/se-requirements-classification
[^76]: https://www.perforce.com/blog/alm/agile-requirements-gathering
[^77]: https://labs.sogeti.com/requirements-management-in-safe-when-good-frameworks-go-wrong/
[^78]: https://www.testrail.com/blog/requirements-traceability-matrix/
[^79]: https://nevolearn.com/blog/scaled-agile-framework-best-practices
[^80]: https://community.atlassian.com/forums/App-Central-articles/Requirements-Management-6-Best-Practices-for-Agile-Teams/ba-p/2964897
[^81]: https://www.youtube.com/watch?v=YjE3BHP5KUo
[^82]: https://www.modernanalyst.com/Careers/InterviewQuestions/tabid/128/ID/1391/How-is-the-Solution-Assessment-and-Validation-knowledge-area-of-the-BABOK-v20-defined.aspx
[^83]: https://www.agilealliance.org/wp-content/uploads/2017/08/AgileExtension_V2-Member-Copy.pdf
[^84]: https://arxiv.org/html/2506.00058v1
[^85]: https://paginaspersonales.unam.mx/app/webroot/files/1674/general/curriculum.pdf?rand=20240706010315000000
[^86]: https://www.youtube.com/watch?v=V3gr_qf_sJg
[^87]: https://www.ai21.com/glossary/foundational-llm/automatic-prompt-engineer/
[^88]: https://www.examera.org/blog/blog075```

