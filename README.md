# ProjMAN
## AI Transformation Documentation & Tools

Ez a repository az AI-transzformációhoz szükséges dokumentációkat és eszközöket tartalmazza, különösen az Agentize platform bevezetéséhez.

---

## 📚 Dokumentáció

### 1. AI Transformation Playbook (`docs/ai-transformation-playbook.md`)

Egy átfogó útmutató az AI-transzformációhoz, amely három fő részből áll:

- **PMO-rész**: Projektmenedzsment útmutató konkrét ROI-számításokkal
  - PMO szerepe az AI-transzformációban
  - Részletes ROI-számítási módszertan
  - Konkrét példák számokkal (Meeting Assistant, PMO Report Generator, kombinált)

- **Agentize technikai támogatás**: Részletes leírás use case-ekkel
  - Technikai támogatás típusai
  - Meeting Assistant use case (jegyzőkönyv + action tracking)
  - PMO Report Generator use case (Excel/Jira → vezetői összefoglaló)
  - Workflow támogatás és időmegtakarítás
  - **Technikai specifikáció és implementáció** (OpenRouter + Haiku 4.5)

- **90 napos implementációs ütemterv**: Feltételezett ütemterv
  - 1-30 nap: Igényfelmérés, pilot bevezetés
  - 31-60 nap: Testreszabás, tréning, finomhangolás
  - 61-90 nap: Teljes körű bevezetés, mérés, visszacsatolás

### 2. Proof of Value Kit (`docs/proof-of-value-kit.md`)

Bemutató anyagok és útmutatók az első ügyféltalálkozóhoz:

- **Meeting Assistant**: 
  - Funkciók és képességek
  - Demo script és videó útmutatók
  - Lépésről lépésre beállítási útmutató képernyőképekkel
  - Gyakori problémák és megoldások

- **PMO Report Generator**:
  - Funkciók és képességek
  - Demo script és videó útmutatók
  - Lépésről lépésre beállítási útmutató képernyőképekkel
  - Gyakori problémák és megoldások

- **Kombinált használat**: Integrált workflow és színergia hatások
- **Ügyféltalálkozó előkészítés**: Checklist és demo prezentáció struktúra
- **Demo adatok és folyamatok**: Teljes demo környezet setup és scriptek

### 3. Success Metrics Framework (`docs/success-metrics-framework.md`)

Az AI-bevezetés mérési módszertana:

- **Mérési módszertan**: Filozófia, szintek (operatív, taktikai, stratégiai)
- **KPI-k**: 
  - Időmegtakarítás metrikák
  - Költségcsökkentés metrikák
  - Minőségi metrikák (felhasználói elégedettség, pontosság)
  - Üzleti hatás metrikák (döntéshozatal, projekt teljesítmény)
- **Mérési gyakoriság és adatforrások**: Automatikus és manuális adatforrások
- **Mérési eszközök és sablonok**: Felmérések, nyilvántartások, jelentések
- **Adatelemzés és jelentéskészítés**: Havi, negyedéves, éves jelentések

---

## 🛠️ Eszközök

### ROI Kalkulátor Sablon (`tools/roi-calculator-template.md`)

Részletes útmutató az ROI-kalkulátor sablon használatához:

- **Excel/Google Sheets sablon struktúra**: Befektetés, Megtakarítás, ROI számítás, Összefoglaló munkalapok
- **Lépésről lépésre kitöltés**: Minden kategória részletes útmutatással
- **Példa számítások**: Kis és nagy projektekre
- **Sablon létrehozása**: Excel és Google Sheets útmutatók
- **Használati tippek**: Ügyféltalálkozókon való használathoz

### ROI Kalkulátor CSV sablonok

Kész CSV fájlok az Excel/Google Sheets importáláshoz:

- `tools/roi-calculator-investment.csv`: Befektetés kategóriák
- `tools/roi-calculator-savings.csv`: Megtakarítás kategóriák
- `tools/roi-calculator-summary.csv`: ROI számítás és összefoglaló

### Demo Környezet

Teljes demo környezet a Proof of Value bemutatáshoz:

- **Docker Compose** (`docker-compose.demo.yml`): PostgreSQL, Redis, MinIO
- **Demo adatok** (`demo_data/`): Meeting transcript, Jira adatok, Excel struktúra
- **Scriptek** (`scripts/`): Adatbetöltés és demo futtatás
- **Screenshots** (`screenshots/`): Placeholder mappák a képernyőképekhez

### NotebookLM Integráció

NotebookLM-hez optimalizált dokumentumok automatizáláshoz:

- **VIDEO_SCRIPTS.md**: Részletes videó scriptek a 4 demo videóhoz
- **SCREENSHOT_GUIDE.md**: Képernyőképek készítési útmutatója (13 screenshot)
- **INTEGRATION_GUIDE.md**: Teljes fejlesztési útmutató (API, integrációk, kód)
- **README.md**: NotebookLM használati útmutató

---

## 📁 Projekt struktúra

```
ProjMAN/
├── docs/
│   ├── ai-transformation-playbook.md      # AI Transformation Playbook
│   ├── proof-of-value-kit.md               # Proof of Value Kit
│   └── success-metrics-framework.md        # Success Metrics Framework
├── tools/
│   ├── roi-calculator-template.md          # ROI kalkulátor útmutató
│   ├── roi-calculator-investment.csv       # Befektetés sablon
│   ├── roi-calculator-savings.csv          # Megtakarítás sablon
│   └── roi-calculator-summary.csv         # Összefoglaló sablon
├── demo_data/
│   ├── meeting_demo_transcript.txt         # Demo meeting átirat
│   ├── meeting_request.json                 # API kérés példa
│   ├── meeting_minutes_demo.json           # Várható AI output
│   ├── jira_demo_data.json                 # Demo Jira adatok
│   ├── report_request.json                  # API kérés példa
│   ├── pmo_report_demo.json                # Várható AI output
│   └── init.sql                            # Adatbázis inicializáló script
├── scripts/
│   ├── load_demo_data.py                   # Demo adatok betöltése
│   └── demo_script.sh                      # Teljes demo folyamat
├── screenshots/
│   ├── meeting-assistant/                  # Meeting Assistant képernyőképek
│   └── pmo-report-generator/               # PMO Report Generator képernyőképek
├── notebooklm/
│   ├── VIDEO_SCRIPTS.md                   # Videó scriptek NotebookLM-hez
│   ├── SCREENSHOT_GUIDE.md                 # Screenshot útmutató NotebookLM-hez
│   ├── INTEGRATION_GUIDE.md                # Fejlesztési útmutató NotebookLM-hez
│   └── README.md                           # NotebookLM használati útmutató
├── docker-compose.demo.yml                 # Demo környezet
├── .gitignore                              # Git ignore szabályok
└── README.md                               # Ez a fájl
```

---

## 🚀 Gyors kezdés

### 1. Dokumentációk olvasása

1. Kezd az **AI Transformation Playbook**-kal a teljes áttekintésért
2. Olvasd el a **Proof of Value Kit**-et az ügyféltalálkozó előkészítéséhez
3. Ismerkedj meg a **Success Metrics Framework**-kel a mérési módszertannal

### 2. ROI kalkulátor használata

1. Olvasd el a `tools/roi-calculator-template.md` útmutatót
2. Importáld a CSV fájlokat Excel-be vagy Google Sheets-be
3. Töltsd ki a sablont az ügyfél adataival
4. Mutasd be az eredményeket az ügyféltalálkozón

### 3. Demo környezet indítása

1. **Előfeltételek:**
   ```bash
   # Docker és Docker Compose telepítve
   docker --version
   docker-compose --version
   ```

2. **Demo környezet indítása:**
   ```bash
   docker-compose -f docker-compose.demo.yml up -d
   ```

3. **Demo adatok betöltése:**
   ```bash
   python scripts/load_demo_data.py --all
   ```

4. **Demo script futtatása:**
   ```bash
   bash scripts/demo_script.sh
   ```

### 4. Ügyféltalálkozó előkészítése

1. Készítsd elő a demo környezetet
2. Gyakorold a demo scripteket
3. Ellenőrizd a videó anyagokat (amikor elkészülnek)
4. Készítsd elő a ROI kalkulátort példa adatokkal

---

## 📊 Főbb metrikák

### Meeting Assistant
- **Időmegtakarítás**: 2-3 óra/meeting → 10-15 perc ellenőrzés
- **ROI**: ~833% (50 fős csapat esetén)
- **Payback period**: ~1.3 hónap

### PMO Report Generator
- **Időmegtakarítás**: 5-6 óra/hét → 30-45 perc ellenőrzés
- **ROI**: ~208% (PMO csapat esetén)
- **Payback period**: ~4 hónap

### Kombinált bevezetés
- **Időmegtakarítás**: 7-9 óra/hét/felhasználó
- **ROI**: ~713% (kombinált használat esetén)
- **Payback period**: ~1.5 hónap

---

## ⚠️ Ismert korlátok és következő lépések

### Jelenlegi állapot

✅ **Kész:**
- Dokumentáció (80-90%)
- Demo adatok struktúra
- Docker Compose konfiguráció
- Python scriptek alap struktúra

⚠️ **Hiányzik:**
- Screenshots (13 fájl) - Placeholder mappák kész, valós képernyőképek szükségesek
- Demo videók (4 videó) - Útmutatók kész, videók készítése szükséges
- API implementáció - Specifikációk kész, kód implementálása szükséges
- Excel fájlok - Struktúra dokumentálva, valós fájlok szükségesek

### Következő lépések

1. **Screenshots készítése:**
   - Demo környezet futtatása
   - Beállítási útmutató lépéseinek követése
   - Képernyőképek készítése

2. **Demo videók készítése:**
   - Gyors bemutatás (3-5 perc) - Meeting Assistant
   - Részletes beállítás (10-15 perc) - Meeting Assistant
   - Gyors bemutatás (3-5 perc) - PMO Report Generator
   - Részletes beállítás (10-15 perc) - PMO Report Generator

3. **API implementáció:**
   - OpenRouter integráció
   - Meeting Assistant agent
   - PMO Report Generator agent
   - Integrációk (Teams, Jira, SMTP)

---

## 📝 Dokumentum verziók

- **AI Transformation Playbook**: v1.0 (2025-01-15)
- **Proof of Value Kit**: v1.0 (2025-01-15)
- **Success Metrics Framework**: v1.0 (2025-01-15)
- **ROI Kalkulátor Sablon**: v1.0

---

## 🤝 Hozzájárulás

Ez a dokumentáció és eszközök az Agentize platform bevezetéséhez készültek. Ha javaslataid vagy kérdéseid vannak, kérlek, jelezd!

---

## 📄 Licenc

MIT License - lásd a LICENSE fájlt részletekért.

---

*Utolsó frissítés: 2025-01-15*
