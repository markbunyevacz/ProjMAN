# AI Transformation Playbook
## 3 az 1-ben: PMO útmutató, Technikai támogatás, Implementációs ütemterv

---

## 1. PMO-rész: Az AI-transzformáció projektmenedzsmentje

### 1.1 PMO szerepe az AI-transzformációban

A Project Management Office (PMO) kritikus szerepet játszik az AI-transzformáció sikeres megvalósításában:

- **Stratégiai koordináció**: Az AI-bevezetés összehangolása a szervezeti célokkal
- **Kockázatkezelés**: Proaktív azonosítás és kezelés az AI-projektek kockázataihoz
- **Erőforrás-optimalizálás**: Hatékony erőforrás-allokáció az AI-iniciatívákhoz
- **Mérés és jelentéskészítés**: Folyamatos monitoring és ROI-követés
- **Change management**: Szervezeti változáskezelés támogatása

### 1.2 ROI-számítási módszertan

#### Alapképlet

```
ROI (%) = ((Megtakarítás - Befektetés) / Befektetés) × 100
```

#### Részletes ROI-modell

**1. Befektetés (Investment) kategóriák:**

- **Szoftver licenc díjak**: Agentize platform előfizetés
- **Implementációs költségek**: 
  - Konfiguráció és testreszabás: 40-80 óra × óradíj
  - Tréning és onboarding: 20-40 óra × óradíj
  - Integrációk (Jira, Excel, Teams stb.): 10-20 óra × óradíj
- **Folyamatos karbantartás**: Havonta 5-10 óra × óradíj

**2. Megtakarítás (Savings) kategóriák:**

- **Időmegtakarítás**:
  - Meeting jegyzőkönyvek automatikus generálása: 2-3 óra/hét × meeting menedzser
  - PMO riportok automatikus összeállítása: 4-6 óra/hét × PMO szakember
  - Action item tracking automatikus követése: 1-2 óra/hét × projektmenedzser
  
- **Költségcsökkentés**:
  - Adminisztratív feladatok csökkentése: 30-40% időmegtakarítás
  - Hibák csökkentése (manuális adatbevitel helyett): 20-30% csökkenés
  - Gyorsabb döntéshozatal: 15-25% időmegtakarítás

**3. Konkrét ROI-példák számokkal:**

##### Példa 1: Meeting Assistant bevezetése (50 fős csapat)

**Befektetés:**
- Agentize licenc: €500/hó × 12 hó = €6,000/év
- Implementáció: 60 óra × €100/óra = €6,000
- Tréning: 30 óra × €100/óra = €3,000
- **Összes befektetés (első év)**: €15,000

**Megtakarítás:**
- 10 meeting/hét × 2.5 óra jegyzőkönyv készítés = 25 óra/hét
- 25 óra/hét × 50 hét = 1,250 óra/év
- 1,250 óra × €80/óra (átlagos óradíj) = €100,000/év
- Action tracking automatikus: 500 óra/év × €80/óra = €40,000/év
- **Összes megtakarítás**: €140,000/év

**ROI számítás:**
```
ROI = ((€140,000 - €15,000) / €15,000) × 100 = 833%
```

**Payback period**: ~1.3 hónap

##### Példa 2: PMO Report Generator bevezetése

**Befektetés:**
- Agentize licenc: €500/hó × 12 hó = €6,000/év
- Implementáció: 50 óra × €100/óra = €5,000
- Jira/Excel integráció: 20 óra × €100/óra = €2,000
- **Összes befektetés (első év)**: €13,000

**Megtakarítás:**
- Heti PMO riport: 5 óra/hét × 50 hét = 250 óra/év
- 250 óra × €100/óra (PMO szakember) = €25,000/év
- Hibák csökkentése (manuális adatbevitel): €5,000/év
- Gyorsabb döntéshozatal: €10,000/év (értékelhetetlen, de mérhető)
- **Összes megtakarítás**: €40,000/év

**ROI számítás:**
```
ROI = ((€40,000 - €13,000) / €13,000) × 100 = 208%
```

**Payback period**: ~4 hónap

##### Példa 3: Kombinált bevezetés (Meeting Assistant + PMO Report Generator)

**Befektetés:**
- Agentize licenc: €800/hó × 12 hó = €9,600/év
- Implementáció: 100 óra × €100/óra = €10,000
- Tréning és integráció: 50 óra × €100/óra = €5,000
- **Összes befektetés (első év)**: €24,600

**Megtakarítás:**
- Meeting Assistant: €140,000/év
- PMO Report Generator: €40,000/év
- Szinergia hatások: €20,000/év (jobban koordinált projektek)
- **Összes megtakarítás**: €200,000/év

**ROI számítás:**
```
ROI = ((€200,000 - €24,600) / €24,600) × 100 = 713%
```

**Payback period**: ~1.5 hónap

### 1.3 ROI-követés és jelentéskészítés

**Havi mérési pontok:**
- Aktuális időmegtakarítás (órákban)
- Költségcsökkentés (EUR-ban)
- Felhasználói elégedettség (1-5 skála)
- Hibák száma (előtte/utána összehasonlítás)

**Negyedéves jelentés:**
- ROI újraszámítás
- Payback period frissítés
- Ajánlások a következő negyedévre

---

## 2. Agentize technikai támogatás leírása

### 2.1 Mi az Agentize?

Az Agentize egy AI-agent alapú platform, amely automatizálja a projektmenedzsment és üzleti folyamatok kulcsfontosságú feladatait. A platform moduláris architektúrával rendelkezik, lehetővé téve a szervezeti igényekhez igazított testreszabást.

### 2.2 Technikai támogatás típusai

#### 2.2.1 Implementációs támogatás

- **Konfiguráció**: Agentize platform beállítása a szervezeti igényekhez
- **Integrációk**: Kapcsolódás meglévő rendszerekhez (Jira, Excel, Microsoft Teams, Slack)
- **Testreszabás**: Workflow-k és automatizálások létrehozása

#### 2.2.2 Tréning és onboarding

- **Adminisztrátor tréning**: Platform kezelés, konfiguráció módosítások
- **Felhasználói tréning**: Napi használat, best practices
- **Dokumentáció**: Részletes útmutatók és FAQ-k

#### 2.2.3 Folyamatos támogatás

- **Technikai support**: Email és chat támogatás (8-17h munkaidőben)
- **Rendszeres frissítések**: Új funkciók és javítások
- **Performance monitoring**: Rendszer teljesítmény követése

### 2.3 Use case-ek részletes leírása

#### Use Case 1: Meeting Assistant

**Funkciók:**
- **Automatikus jegyzőkönyv generálás**: Meeting audio/video feldolgozása, kulcsfontosságú pontok kiemelése
- **Action item tracking**: Automatikus action item azonosítás és hozzárendelés
- **Következő lépések generálása**: AI-alapú ajánlások a meeting után
- **Integráció**: Microsoft Teams, Zoom, Google Meet támogatás

**Workflow támogatás:**

1. **Meeting előtt**:
   - Meeting agenda automatikus előkészítése (előző meetingek alapján)
   - Résztvevők értesítése

2. **Meeting alatt**:
   - Valós idejű jegyzetelés (opcionális)
   - Kulcsfontosságú pontok azonosítása

3. **Meeting után**:
   - Automatikus jegyzőkönyv generálás (5-10 perc)
   - Action item-ek kiemelése és hozzárendelése
   - Következő meeting időpont javaslat

**Időmegtakarítás:**
- **Előtte**: 2-3 óra/manuális jegyzőkönyv készítés
- **Utána**: 10-15 perc ellenőrzés és finomhangolás
- **Megtakarítás**: ~2.5 óra/meeting

**Példa használati eset:**
```
Hétfői projekt státusz meeting (1 óra)
→ Meeting Assistant automatikusan generál jegyzőkönyvet
→ 3 action item azonosítva és hozzárendelve
→ Jira ticket-ek automatikusan létrehozva
→ Csapat értesítve email-ben
Időmegtakarítás: 2.5 óra
```

#### Use Case 2: PMO Report Generator

**Funkciók:**
- **Adatgyűjtés**: Automatikus adatgyűjtés Jira, Excel, és más forrásokból
- **Adatelemzés**: AI-alapú trend elemzés és kockázat azonosítás
- **Riport generálás**: Vezetői összefoglaló automatikus létrehozása
- **Vizualizáció**: Grafikonok és diagramok generálása

**Workflow támogatás:**

1. **Adatgyűjtés** (automatikus):
   - Jira projekt státuszok lekérése
   - Excel táblázatok feldolgozása
   - KPI-k számítása

2. **Adatelemzés** (AI-alapú):
   - Trend azonosítás (pl. késések, túlköltések)
   - Kockázat értékelés
   - Ajánlások generálása

3. **Riport generálás**:
   - Vezetői összefoglaló (1-2 oldal)
   - Részletes adatok (melléklet)
   - Vizualizációk

**Időmegtakarítás:**
- **Előtte**: 5-6 óra/heti PMO riport manuális összeállítása
- **Utána**: 30-45 perc ellenőrzés és finomhangolás
- **Megtakarítás**: ~5 óra/hét

**Példa használati eset:**
```
Heti PMO riport összeállítása
→ Agentize automatikusan lekéri az adatokat Jira-ból
→ Excel táblázatok feldolgozása
→ AI elemzi a trendeket és kockázatokat
→ Vezetői összefoglaló generálása (PDF)
→ Email küldés a vezetőségnek
Időmegtakarítás: 5 óra/hét
```

#### Use Case 3: Kombinált workflow (Meeting + PMO)

**Integrált folyamat:**

1. Meeting Assistant generál jegyzőkönyvet és action item-eket
2. Action item-ek automatikusan Jira ticket-ekké alakulnak
3. PMO Report Generator követi a ticket-ek státuszát
4. Heti riport tartalmazza a meeting eredményeket és action item státuszokat

**Színergia hatások:**
- Jobban koordinált projektek
- Gyorsabb döntéshozatal
- Teljesebb áttekintés

### 2.4 Technikai követelmények

**Minimális követelmények:**
- Internet kapcsolat
- Microsoft Teams / Zoom / Google Meet hozzáférés
- Jira API hozzáférés (PMO Report Generator esetén)
- Excel fájlok hozzáférése (opcionális)

**Biztonsági szempontok:**
- Adatok titkosítása (átvitel és tárolás során)
- GDPR megfelelőség
- Szervezeti adatok védelme

### 2.5 Technikai specifikáció és implementáció

#### 2.5.1 AI Agent architektúra

**AI Agent definíció:**
Az AI agent egy autonóm szoftver entitás, amely:
- **Érzékelés (Perception)**: Külső adatok feldolgozása (meeting audio, Jira API, Excel fájlok)
- **Döntéshozatal (Decision Making)**: AI-alapú elemzés és következtetés
- **Cselekvés (Action)**: Automatikus feladatok végrehajtása (jegyzőkönyv generálás, riport készítés)
- **Visszacsatolás (Feedback Loop)**: Eredmények értékelése és finomhangolás

**Agent komponensek:**
1. **Input Handler**: Adatok fogadása és előfeldolgozása
2. **AI Engine**: OpenRouter + Haiku 4.5 integráció
3. **Task Executor**: Feladatok végrehajtása
4. **Output Generator**: Eredmények formázása és küldése
5. **State Manager**: Agent állapot kezelése

#### 2.5.2 Infrastruktúra követelmények

**Szükséges szolgáltatások:**

1. **AI Szolgáltató: OpenRouter**
   - API endpoint: `https://openrouter.ai/api/v1/chat/completions`
   - Model: `anthropic/claude-3.5-haiku` (Haiku 4.5)
   - API kulcs: Környezeti változóban tárolva (`OPENROUTER_API_KEY`)
   - Rate limiting: 100 kérés/perc (default)

2. **Adatbázis:**
   - PostgreSQL 14+ vagy SQLite (fejlesztéshez)
   - Táblák:
     - `meetings`: Meeting metaadatok
     - `meeting_transcripts`: Átirat tárolás
     - `action_items`: Action item-ek
     - `reports`: Generált riportok
     - `agent_configs`: Agent konfigurációk

3. **Message Queue:**
   - Redis vagy RabbitMQ (aszinkron feldolgozáshoz)
   - Queue nevek:
     - `meeting:process`: Meeting feldolgozás
     - `report:generate`: Riport generálás

4. **File Storage:**
   - S3-kompatibilis storage (minio fejlesztéshez)
   - Bucket struktúra:
     - `meetings/audio/`: Meeting audio fájlok
     - `reports/pdf/`: Generált PDF riportok
     - `reports/excel/`: Excel exportok

5. **Integrációk:**
   - **Microsoft Teams Graph API**: Meeting adatok lekérése
   - **Jira REST API v3**: Ticket létrehozás/lekérés
   - **SMTP Server**: Email küldés

**Környezeti változók (.env):**
```bash
# AI Provider
OPENROUTER_API_KEY=sk-or-v1-...
OPENROUTER_MODEL=anthropic/claude-3.5-haiku
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/agentize
REDIS_URL=redis://localhost:6379/0

# Storage
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
S3_BUCKET=agentize

# Integrations
TEAMS_CLIENT_ID=...
TEAMS_CLIENT_SECRET=...
TEAMS_TENANT_ID=...
JIRA_URL=https://yourcompany.atlassian.net
JIRA_API_TOKEN=...
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=...
SMTP_PASSWORD=...
```

#### 2.5.3 Meeting Assistant technikai specifikáció

**Agent workflow:**

```
1. Meeting Event Trigger
   ↓
2. Audio Download (Teams API)
   ↓
3. Speech-to-Text (Whisper API vagy helyi)
   ↓
4. Transcript → AI Processing (OpenRouter/Haiku)
   ↓
5. Extract: Agenda, Key Points, Action Items
   ↓
6. Generate Meeting Minutes (Markdown → PDF)
   ↓
7. Create Jira Tickets (action items)
   ↓
8. Send Email Notifications
   ↓
9. Store Results (Database)
```

**AI Prompt struktúra (Haiku 4.5):**

```python
MEETING_ASSISTANT_SYSTEM_PROMPT = """
Te egy professzionális meeting jegyzőkönyv generáló asszisztens vagy.
Feladatod:
1. Átirat elemzése és strukturálása
2. Kulcsfontosságú pontok azonosítása
3. Action item-ek kiemelése (ki, mit, mikorra)
4. Következő lépések javaslása

Kimenet formátum (JSON):
{
  "summary": "Rövid összefoglaló (2-3 mondat)",
  "agenda_items": [
    {"topic": "...", "discussion": "...", "decisions": "..."}
  ],
  "key_points": ["...", "..."],
  "action_items": [
    {
      "id": "AI-001",
      "description": "...",
      "assignee": "név vagy email",
      "due_date": "YYYY-MM-DD",
      "priority": "high|medium|low"
    }
  ],
  "next_steps": ["...", "..."]
}
"""

MEETING_ASSISTANT_USER_PROMPT = """
Meeting átirat:
{transcript}

Meeting metaadatok:
- Dátum: {meeting_date}
- Résztvevők: {participants}
- Cím: {meeting_title}
- Időtartam: {duration} perc

Generálj jegyzőkönyvet a fenti formátumban.
"""
```

**API endpoint specifikáció:**

```python
POST /api/v1/meetings/process
{
  "meeting_id": "teams-meeting-id",
  "audio_url": "https://...",
  "participants": ["user1@company.com", "user2@company.com"],
  "meeting_title": "Heti projekt státusz",
  "meeting_date": "2025-01-15T10:00:00Z"
}

Response:
{
  "meeting_id": "uuid",
  "status": "processing|completed|failed",
  "minutes_url": "https://.../minutes.pdf",
  "action_items": [...],
  "jira_tickets": ["JIRA-123", "JIRA-124"]
}
```

**Adatmodell (SQL):**

```sql
CREATE TABLE meetings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    external_id VARCHAR(255) UNIQUE, -- Teams meeting ID
    title VARCHAR(500),
    date TIMESTAMP,
    duration_minutes INTEGER,
    participants JSONB, -- ["email1", "email2"]
    audio_url TEXT,
    transcript TEXT,
    status VARCHAR(50), -- pending, processing, completed, failed
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE meeting_minutes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    meeting_id UUID REFERENCES meetings(id),
    summary TEXT,
    agenda_items JSONB,
    key_points JSONB,
    action_items JSONB,
    next_steps JSONB,
    minutes_pdf_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE action_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    meeting_id UUID REFERENCES meetings(id),
    description TEXT,
    assignee_email VARCHAR(255),
    due_date DATE,
    priority VARCHAR(20),
    jira_ticket_id VARCHAR(100),
    status VARCHAR(50), -- open, in_progress, completed
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### 2.5.4 PMO Report Generator technikai specifikáció

**Agent workflow:**

```
1. Schedule Trigger (Cron: heti/havi)
   ↓
2. Data Collection:
   - Jira API: Projektek, ticket-ek, státuszok
   - Excel Files: Költségvetés, erőforrások
   ↓
3. Data Aggregation & Validation
   ↓
4. AI Analysis (OpenRouter/Haiku):
   - Trend elemzés
   - Kockázat azonosítás
   - Ajánlások generálása
   ↓
5. Generate Report:
   - Executive Summary (AI generált)
   - Charts/Graphs (matplotlib/plotly)
   - Detailed Data (tables)
   ↓
6. Export: PDF + Excel
   ↓
7. Email Distribution
   ↓
8. Store Results
```

**AI Prompt struktúra (Haiku 4.5):**

```python
PMO_REPORT_SYSTEM_PROMPT = """
Te egy PMO riport generáló asszisztens vagy.
Feladatod:
1. Projekt adatok elemzése (Jira + Excel)
2. Trend azonosítás (késések, túlköltések, erőforrás problémák)
3. Kockázatok prioritizálása
4. Vezetői összefoglaló írása (1-2 oldal, executive summary)

Kimenet formátum (JSON):
{
  "executive_summary": {
    "overview": "Rövid áttekintés (1 bekezdés)",
    "key_metrics": {
      "total_projects": 15,
      "on_track": 10,
      "at_risk": 3,
      "delayed": 2,
      "budget_variance": "+5%"
    },
    "critical_risks": [
      {
        "project": "Projekt neve",
        "risk": "Kockázat leírása",
        "impact": "high|medium|low",
        "mitigation": "Javasolt megoldás"
      }
    ],
    "recommendations": ["...", "..."]
  },
  "detailed_analysis": {
    "trends": ["...", "..."],
    "resource_allocation": {...},
    "budget_analysis": {...}
  }
}
"""

PMO_REPORT_USER_PROMPT = """
Projekt adatok (Jira):
{jira_data}

Költségvetés adatok (Excel):
{budget_data}

Időszak: {period_start} - {period_end}

Generálj PMO riportot a fenti formátumban.
"""
```

**Adatmodell (SQL):**

```sql
CREATE TABLE reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_type VARCHAR(50), -- weekly, monthly, quarterly
    period_start DATE,
    period_end DATE,
    status VARCHAR(50), -- generating, completed, failed
    pdf_url TEXT,
    excel_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE report_data (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_id UUID REFERENCES reports(id),
    source VARCHAR(50), -- jira, excel, manual
    data_type VARCHAR(50), -- projects, tickets, budget
    raw_data JSONB,
    processed_data JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE report_analysis (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_id UUID REFERENCES reports(id),
    executive_summary JSONB,
    trends JSONB,
    risks JSONB,
    recommendations JSONB,
    ai_model_version VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);
```

**API endpoint specifikáció:**

```python
POST /api/v1/reports/generate
{
  "report_type": "weekly|monthly|quarterly",
  "period_start": "2025-01-08",
  "period_end": "2025-01-14",
  "jira_projects": ["PROJ-1", "PROJ-2"],
  "excel_files": ["budget.xlsx"],
  "recipients": ["executive@company.com"]
}

Response:
{
  "report_id": "uuid",
  "status": "generating|completed",
  "pdf_url": "https://.../report.pdf",
  "excel_url": "https://.../report.xlsx"
}
```

#### 2.5.5 Implementációs útmutató junior fejlesztőnek

**1. Projekt setup:**

```bash
# Projekt struktúra
agentize-platform/
├── agents/
│   ├── meeting_assistant/
│   │   ├── __init__.py
│   │   ├── agent.py          # Fő agent logika
│   │   ├── prompts.py        # AI prompt-ok
│   │   ├── processors.py     # Audio/transcript feldolgozás
│   │   └── integrations.py  # Teams, Jira integrációk
│   └── pmo_report_generator/
│       ├── __init__.py
│       ├── agent.py
│       ├── prompts.py
│       ├── data_collectors.py # Jira, Excel adatgyűjtés
│       └── report_builder.py # PDF/Excel generálás
├── core/
│   ├── ai_client.py          # OpenRouter wrapper
│   ├── database.py           # DB kapcsolat
│   └── storage.py            # S3 fájlkezelés
├── api/
│   └── routes.py             # FastAPI endpoints
├── requirements.txt
└── .env.example
```

**2. OpenRouter integráció (core/ai_client.py):**

```python
import os
import httpx
from typing import Dict, Any, List

class OpenRouterClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.model = os.getenv("OPENROUTER_MODEL", "anthropic/claude-3.5-haiku")
        self.base_url = "https://openrouter.ai/api/v1"
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "HTTP-Referer": os.getenv("APP_URL", "http://localhost"),
                "X-Title": "Agentize Platform"
            },
            timeout=60.0
        )
    
    async def chat_completion(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 4000
    ) -> Dict[str, Any]:
        """AI kérés küldése OpenRouter-on keresztül"""
        response = await self.client.post(
            "/chat/completions",
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": temperature,
                "max_tokens": max_tokens
            }
        )
        response.raise_for_status()
        return response.json()
    
    async def extract_json(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """JSON kinyerése AI válaszból"""
        content = response["choices"][0]["message"]["content"]
        # JSON parsing (támogatja code block-ot is)
        import json
        import re
        json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        return json.loads(content)
```

**3. Meeting Assistant implementáció (agents/meeting_assistant/agent.py):**

```python
from core.ai_client import OpenRouterClient
from agents.meeting_assistant.prompts import (
    MEETING_ASSISTANT_SYSTEM_PROMPT,
    build_user_prompt
)
import json

class MeetingAssistantAgent:
    def __init__(self):
        self.ai_client = OpenRouterClient()
    
    async def process_meeting(
        self,
        transcript: str,
        meeting_metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Meeting feldolgozása és jegyzőkönyv generálása"""
        
        # 1. AI hívás
        user_prompt = build_user_prompt(transcript, meeting_metadata)
        response = await self.ai_client.chat_completion(
            system_prompt=MEETING_ASSISTANT_SYSTEM_PROMPT,
            user_prompt=user_prompt
        )
        
        # 2. JSON kinyerése
        minutes_data = await self.ai_client.extract_json(response)
        
        # 3. Action item-ek feldolgozása
        action_items = minutes_data.get("action_items", [])
        for item in action_items:
            # Jira ticket létrehozás (ha integrálva van)
            if meeting_metadata.get("create_jira_tickets"):
                await self._create_jira_ticket(item)
        
        return minutes_data
    
    async def _create_jira_ticket(self, action_item: Dict[str, Any]):
        """Jira ticket létrehozása action item-ből"""
        # Implementáció Jira API-val
        pass
```

**4. Error handling és retry logika:**

```python
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

class RobustAIClient(OpenRouterClient):
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10)
    )
    async def chat_completion_with_retry(self, *args, **kwargs):
        """Retry logikával AI hívás"""
        try:
            return await self.chat_completion(*args, **kwargs)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:  # Rate limit
                await asyncio.sleep(60)  # Várás 1 percet
                raise
            raise
```

**5. Testing:**

```python
# tests/test_meeting_assistant.py
import pytest
from agents.meeting_assistant.agent import MeetingAssistantAgent

@pytest.mark.asyncio
async def test_meeting_assistant_basic():
    agent = MeetingAssistantAgent()
    transcript = "Meeting transcript here..."
    metadata = {
        "meeting_title": "Test Meeting",
        "participants": ["user1@test.com"],
        "meeting_date": "2025-01-15"
    }
    
    result = await agent.process_meeting(transcript, metadata)
    
    assert "summary" in result
    assert "action_items" in result
    assert len(result["action_items"]) > 0
```

---

## 3. 90 napos implementációs ütemterv

### 3.1 Áttekintés

Ez az ütemterv egy tipikus 90 napos implementációs folyamatot mutat be. A tényleges időzítés függhet a szervezet méretétől, komplexitásától és egyedi igényeitől.

### 3.2 1-30. nap: Igényfelmérés és pilot bevezetés

#### 1-7. nap: Igényfelmérés és tervezés

**Célok:**
- Szervezeti igények azonosítása
- Meglévő folyamatok feltérképezése
- Pilot agent(ek) kiválasztása
- Projektcsapat összeállítása

**Tevékenységek:**
- [ ] Kick-off meeting
- [ ] Stakeholder interjúk (5-10 fő)
- [ ] Folyamatok dokumentálása
- [ ] Pilot use case kiválasztása
- [ ] Projektcsapat kijelölése (PMO, IT, felhasználók)

**Kimenetek:**
- Igényfelmérési dokumentum
- Pilot terv
- Projektcsapat lista

#### 8-15. nap: Technikai előkészítés

**Célok:**
- Agentize platform beállítása
- Integrációk előkészítése
- Teszt környezet létrehozása

**Tevékenységek:**
- [ ] Agentize fiók létrehozása
- [ ] Integrációk konfigurálása (Jira, Teams stb.)
- [ ] Teszt adatok előkészítése
- [ ] Biztonsági beállítások

**Kimenetek:**
- Működő teszt környezet
- Integrációs dokumentáció

#### 16-30. nap: Pilot agent(ek) bevezetése

**Célok:**
- Első agent(ek) működésbe helyezése
- Korai visszajelzések gyűjtése
- Alapvető problémák azonosítása

**Tevékenységek:**
- [ ] Meeting Assistant pilot (5-10 meeting)
- [ ] PMO Report Generator pilot (2-3 riport)
- [ ] Felhasználói visszajelzések gyűjtése
- [ ] Technikai problémák dokumentálása

**Kimenetek:**
- Pilot eredmények jelentése
- Visszajelzések összefoglalója
- Finomhangolási javaslatok

### 3.3 31-60. nap: Testreszabás, tréning és finomhangolás

#### 31-45. nap: Testreszabás és finomhangolás

**Célok:**
- Pilot visszajelzések alapján finomhangolás
- Workflow-k optimalizálása
- További testreszabások implementálása

**Tevékenységek:**
- [ ] Agent konfigurációk módosítása
- [ ] Workflow-k finomhangolása
- [ ] Integrációk optimalizálása
- [ ] További testreszabások (ha szükséges)

**Kimenetek:**
- Finomhangolt agent konfigurációk
- Optimalizált workflow dokumentáció

#### 46-60. nap: Tréning és onboarding

**Célok:**
- Felhasználók képzése
- Adminisztrátorok képzése
- Dokumentáció készítése

**Tevékenységek:**
- [ ] Adminisztrátor tréning (4-8 óra)
- [ ] Felhasználói tréning munkamenetek (2-3 alkalom, 2-3 óra/alkalom)
- [ ] Best practices dokumentáció
- [ ] FAQ összeállítása
- [ ] Video útmutatók készítése

**Kimenetek:**
- Képzett felhasználói bázis
- Tréning anyagok
- Dokumentáció

### 3.4 61-90. nap: Teljes körű bevezetés, mérés és visszacsatolás

#### 61-75. nap: Teljes körű bevezetés

**Célok:**
- Összes tervezett agent működésbe helyezése
- Teljes felhasználói bázis onboarding
- Folyamatos monitoring

**Tevékenységek:**
- [ ] További agent(ek) bevezetése (ha van)
- [ ] Maradék felhasználók onboarding
- [ ] Napi monitoring és támogatás
- [ ] Problémák gyors kezelése

**Kimenetek:**
- Teljes körű működés
- Felhasználói elégedettség adatok

#### 76-90. nap: Mérés és visszacsatolás

**Célok:**
- ROI mérés
- Teljesítmény értékelés
- Jövőbeli fejlesztések tervezése

**Tevékenységek:**
- [ ] ROI számítás (90 napos adatok alapján)
- [ ] KPI-k mérése
- [ ] Felhasználói elégedettség felmérés
- [ ] Visszajelzések összefoglalása
- [ ] Jövőbeli fejlesztések tervezése

**Kimenetek:**
- ROI jelentés
- Teljesítmény értékelés
- Jövőbeli roadmap

### 3.5 Kritikus sikerfaktorok

**Sikeres implementáció kulcsfontosságú tényezői:**

1. **Stakeholder engagement**: Vezetőség és kulcsfontosságú felhasználók aktív részvétel
2. **Kommunikáció**: Rendszeres kommunikáció a projektcsapat és felhasználók között
3. **Rugalmasság**: Készenlét a változtatásokra a visszajelzések alapján
4. **Támogatás**: Megfelelő technikai és felhasználói támogatás
5. **Mérés**: Folyamatos mérés és visszacsatolás

### 3.6 Kockázatok és enyhítés

**Lehetséges kockázatok:**

| Kockázat | Valószínűség | Hatás | Enyhítés |
|----------|--------------|-------|----------|
| Felhasználói ellenállás | Közepes | Magas | Korai engagement, tréning, kommunikáció |
| Technikai problémák | Alacsony | Közepes | Tesztelés, backup terv |
| Integrációs nehézségek | Közepes | Közepes | Korai tesztelés, alternatív megoldások |
| Időbeli késések | Közepes | Alacsony | Buffer idő, prioritások |
| ROI nem éri el a várakozásokat | Alacsony | Magas | Realisztikus célok, folyamatos mérés |

---

## 4. Következő lépések

### Rövid távú (0-30 nap)
1. Igényfelmérés és tervezés
2. Pilot agent(ek) kiválasztása
3. Projektcsapat összeállítása

### Közép távú (31-60 nap)
1. Testreszabás és finomhangolás
2. Tréning és onboarding
3. Dokumentáció készítése

### Hosszú távú (61-90+ nap)
1. Teljes körű bevezetés
2. ROI mérés és jelentéskészítés
3. Folyamatos fejlesztés

---

## 5. Kapcsolat és támogatás

**Technikai támogatás:**
- Email: support@agentize.com
- Chat: Agentize platformon belül
- Dokumentáció: https://docs.agentize.com

**Projektmenedzsment:**
- PMO kapcsolattartó: [név, email]
- Projektmenedzser: [név, email]

---

*Dokumentum verzió: 1.0*  
*Utolsó frissítés: 2025-01-XX*

