# Részletes Implementációs Terv - UI Funkciók Kivezetése

## 1. Áttekintés

### 1.1 Cél
A teljes funkcionalitás UI-ra kivezetése, beleértve:
- Meeting Assistant: Teams ID, kapcsolók, email preview, action items UI
- PMO Report Generator: Dinamikus Jira lista, Excel upload, recipients, letöltés
- Globális: Last errors panel, Status részletek expand/collapse

### 1.2 UI Struktúra Döntés
**NEM használunk füleket a fő szinten**, mert:
- A jelenlegi 2 kártya struktúra (Meeting/PMO) jól működik
- A funkciók tabbed interface-ben jelennek meg **kártyán belül**
- Globális elemek (errors, status) panelként/jelzőként

**UI Struktúra:**
```
┌─────────────────────────────────────┐
│  Header: ProjMAN AI Agents          │
├─────────────────────────────────────┤
│  Integrációk állapota (expandable)  │
│  Last Errors Panel (collapsible)    │
├─────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐ │
│  │ Meeting      │  │ PMO Report   │ │
│  │ [Tabs]       │  │ [Tabs]       │ │
│  │ - Input      │  │ - Config     │ │
│  │ - Results    │  │ - Preview    │ │
│  │ - Actions    │  │ - Download   │ │
│  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────┘
```

## 2. Backend API Endpointok

### 2.1 GET /api/v1/jira/projects
**Cél:** Jira projektek dinamikus listázása

**Request:**
- Nincs (opcionális query param: `search`)

**Response:**
```json
{
  "projects": [
    {
      "key": "PROJ-1",
      "name": "Project One",
      "lead": "John Doe",
      "projectType": "software"
    }
  ],
  "total": 10
}
```

**Integráció:**
- Használja: `core/integrations.py` → `JiraIntegration.fetch_project_data()`
- Új metódus: `list_projects()` a `JiraIntegration` osztályban

### 2.2 POST /api/v1/files/upload
**Cél:** Excel fájl feltöltés és feldolgozás

**Request:**
- `file`: multipart/form-data (Excel fájl)
- `purpose`: "pmo_report" | "meeting_data"

**Response:**
```json
{
  "file_id": "uuid",
  "filename": "budget.xlsx",
  "url": "http://minio:9000/agentize/reports/budget.xlsx",
  "size": 12345,
  "processed": false,
  "message": "File uploaded successfully"
}
```

**Integráció:**
- Használja: `core/storage.py` → `StorageService.upload_file()`
- Excel parsing: `pandas` library (hozzáadni `requirements.txt`-hez)

### 2.3 GET /api/v1/logs/recent
**Cél:** Utolsó hibák/logs lekérése

**Request:**
- Query param: `limit` (default: 5), `level` (ERROR, WARNING, INFO)

**Response:**
```json
{
  "logs": [
    {
      "timestamp": "2025-01-15T10:30:00Z",
      "level": "ERROR",
      "message": "Jira API call failed",
      "module": "api.main"
    }
  ],
  "total": 5
}
```

**Integráció:**
- Python logging handler: In-memory buffer (max 100 entries)
- Új modul: `core/logging_handler.py`

### 2.4 POST /api/v1/meetings/send-test-email
**Cél:** Teszt email küldés

**Request:**
```json
{
  "recipient": "test@example.com",
  "subject": "Test Email",
  "html_content": "<html>...</html>"
}
```

**Response:**
```json
{
  "sent": true,
  "message": "Email sent successfully"
}
```

**Integráció:**
- Használja: `core/integrations.py` → `EmailService.send_email()`

### 2.5 GET /api/v1/reports/download/{format}
**Cél:** Riport letöltés különböző formátumokban

**Request:**
- Path param: `format` (html, excel, pdf)
- Query param: `report_id`

**Response:**
- File download (Content-Disposition header)
- Vagy JSON error ha nincs report_id

**Integráció:**
- Használja: `agents/pmo_report_generator.py` → `generate_html_report()`, `export_to_excel_format()`
- PDF: `reportlab` vagy `weasyprint` library (hozzáadni `requirements.txt`-hez)

## 3. Frontend Módosítások

### 3.1 Meeting Assistant Kártya

**Tabbed Interface:**
- **Input Tab:**
  - Meeting Transcript (textarea)
  - Meeting Title (input)
  - Participants (input)
  - **ÚJ:** Teams Meeting ID (input)
  - **ÚJ:** Checkbox: "Create Jira tickets"
  - **ÚJ:** Checkbox: "Send email notifications"
  - Process Meeting gomb

- **Results Tab:**
  - Meeting Minutes (JSON/HTML preview)
  - **ÚJ:** Email HTML Preview (iframe vagy div)
  - **ÚJ:** "Send Test Email" gomb
  - **ÚJ:** "Download HTML" gomb

- **Action Items Tab:**
  - Action items lista (táblázat)
  - **ÚJ:** "Create Jira Tickets" gomb (minden action item-hez)
  - **ÚJ:** Jira ticket ID-k megjelenítése

**CSS:**
```css
.tabs {
  display: flex;
  border-bottom: 2px solid #e0e0e0;
  margin-bottom: 1rem;
}
.tab {
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  border-bottom: 2px solid transparent;
}
.tab.active {
  border-bottom-color: #667eea;
  color: #667eea;
}
.tab-content {
  display: none;
}
.tab-content.active {
  display: block;
}
```

### 3.2 PMO Report Generator Kártya

**Tabbed Interface:**
- **Configuration Tab:**
  - Report Period (start/end)
  - Report Type (select)
  - **ÚJ:** Jira Projects (multi-select dropdown - dinamikus Jira-ból)
  - **ÚJ:** Excel Files (file input - multiple)
  - **ÚJ:** Recipients (input - comma separated)
  - **ÚJ:** Checkbox: "Send email"
  - Generate Report gomb

- **Preview Tab:**
  - HTML Report Preview (iframe)
  - Warnings/Info blokkok
  - **ÚJ:** "Refresh Preview" gomb

- **Download Tab:**
  - **ÚJ:** "Download HTML" gomb
  - **ÚJ:** "Download Excel" gomb
  - **ÚJ:** "Download PDF" gomb (ha implementálva)
  - **ÚJ:** "Email Report" gomb

**Dinamikus Jira Projects:**
- Betöltés: Oldal betöltésekor `/api/v1/jira/projects` hívás
- Multi-select dropdown vagy checkbox lista
- Fallback: Ha Jira nincs konfigurálva, szövegmező (jelenlegi)

### 3.3 Globális Elemek

**Last Errors Panel:**
```html
<div class="errors-panel" id="errorsPanel">
  <h3 onclick="toggleErrors()">⚠️ Last Errors (5) <span class="toggle-icon">▼</span></h3>
  <div class="errors-content" style="display: none;">
    <div class="error-item">
      <span class="error-time">2025-01-15 10:30</span>
      <span class="error-level">ERROR</span>
      <span class="error-message">Jira API call failed</span>
    </div>
  </div>
</div>
```

**Status Expand/Collapse:**
```html
<div class="integration-item" data-integration="jira">
  <span class="integration-name">Jira</span>
  <span class="integration-status">✅ Konfigurálva</span>
  <button class="expand-btn" onclick="toggleDetails('jira')">›</button>
</div>
<div class="integration-details" id="jiraDetails" style="display: none;">
  <p>URL: https://company.atlassian.net</p>
  <p>Ping: 120ms</p>
  <p>Last Code: 200</p>
</div>
```

## 4. Integrációk és Függőségek

### 4.1 Új Python Könyvtárak
```txt
pandas>=2.0.0          # Excel fájl feldolgozás
openpyxl>=3.1.0        # Excel olvasás/írás
python-multipart>=0.0.6  # File upload FastAPI-hoz
reportlab>=4.0.0       # PDF generálás (opcionális)
```

### 4.2 Meglévő Integrációk Használata
- `core/integrations.py` → JiraIntegration, EmailService, TeamsIntegration
- `core/storage.py` → StorageService (file upload)
- `core/database.py` → DatabaseService (logs tárolás - opcionális)
- `agents/pmo_report_generator.py` → Excel export formátum

### 4.3 Logging Handler
Új modul: `core/logging_handler.py`
```python
class InMemoryLogHandler(logging.Handler):
    def __init__(self, max_entries=100):
        self.logs = []
        self.max_entries = max_entries
    
    def emit(self, record):
        self.logs.append({
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module
        })
        if len(self.logs) > self.max_entries:
            self.logs.pop(0)
```

## 5. Implementációs Lépések

### Fázis 1: Backend API Endpointok
1. ✅ GET /api/v1/jira/projects
2. ✅ POST /api/v1/files/upload
3. ✅ GET /api/v1/logs/recent
4. ✅ POST /api/v1/meetings/send-test-email
5. ✅ GET /api/v1/reports/download/{format}

### Fázis 2: Frontend Meeting Kártya
1. ✅ Tabbed interface létrehozása
2. ✅ Teams ID input hozzáadása
3. ✅ Kapcsolók (checkboxes) hozzáadása
4. ✅ Email preview panel
5. ✅ Action items tab és Jira ticket létrehozás

### Fázis 3: Frontend PMO Kártya
1. ✅ Tabbed interface létrehozása
2. ✅ Dinamikus Jira projects dropdown
3. ✅ Excel file upload
4. ✅ Recipients input
5. ✅ Download gombok

### Fázis 4: Globális Elemek
1. ✅ Last errors panel
2. ✅ Status expand/collapse

### Fázis 5: E2E Tesztelés
1. ✅ Meeting flow tesztelés
2. ✅ PMO flow tesztelés
3. ✅ Error handling tesztelés
4. ✅ Integrációk tesztelése (Jira, Email, Teams)

## 6. Tesztelési Terv

### 6.1 Meeting Assistant E2E Teszt
1. **Input Tab:**
   - Transcript beírása
   - Teams ID megadása (ha van)
   - Kapcsolók beállítása
   - Process Meeting gomb

2. **Results Tab:**
   - Meeting minutes megjelenítése
   - Email preview ellenőrzése
   - Test email küldés

3. **Action Items Tab:**
   - Action items lista
   - Jira ticket létrehozás

### 6.2 PMO Report Generator E2E Teszt
1. **Configuration Tab:**
   - Jira projects kiválasztása (dinamikus lista)
   - Excel fájl feltöltése
   - Recipients megadása
   - Generate Report

2. **Preview Tab:**
   - HTML report megjelenítése
   - Warnings ellenőrzése

3. **Download Tab:**
   - HTML letöltés
   - Excel letöltés

### 6.3 Error Handling Teszt
1. Jira nincs konfigurálva → Fallback demo adatok
2. Email nincs konfigurálva → Warning megjelenítése
3. Excel fájl hibás → Error message
4. API hiba → Error panel frissítése

## 7. Kockázatok és Megoldások

### 7.1 Kockázatok
- **Excel parsing komplexitás:** Különböző Excel formátumok
  - **Megoldás:** Pandas + openpyxl, error handling
- **PDF generálás:** HTML → PDF konverzió
  - **Megoldás:** reportlab vagy weasyprint, opcionális feature
- **Jira API rate limiting:** Túl sok projekt lekérés
  - **Megoldás:** Caching, pagination
- **File upload méret:** Nagy Excel fájlok
  - **Megoldás:** Max size limit, progress indicator

### 7.2 Fallback Stratégiák
- Jira nincs konfigurálva → Demo adatok (már implementálva)
- Excel nincs feltöltve → Csak Jira adatok
- Email nincs konfigurálva → Warning, de report generálás megy tovább

## 8. Következő Lépések

1. **Backend implementáció** (Fázis 1)
2. **Frontend Meeting kártya** (Fázis 2)
3. **Frontend PMO kártya** (Fázis 3)
4. **Globális elemek** (Fázis 4)
5. **E2E tesztelés** (Fázis 5)
6. **Dokumentáció frissítése**

---

**Terv készítve:** 2025-01-15
**Státusz:** Kész implementálásra

