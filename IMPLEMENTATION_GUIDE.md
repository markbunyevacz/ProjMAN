# Implementation Guide
## ProjMAN AI Agents - Complete Implementation Documentation

**Version:** 1.0  
**Date:** 2025-11-14  
**Author:** ProjMAN Development Team

---

## Table of Contents

1. [Overview](#1-overview)
2. [Architecture](#2-architecture)
3. [Installation](#3-installation)
4. [Configuration](#4-configuration)
5. [Usage Examples](#5-usage-examples)
6. [API Reference](#6-api-reference)
7. [Integration Guide](#7-integration-guide)
8. [Testing](#8-testing)
9. [Deployment](#9-deployment)
10. [Troubleshooting](#10-troubleshooting)

---

## 1. Overview

### 1.1 Purpose

This guide provides complete implementation documentation for the ProjMAN AI agents:
- **Meeting Assistant**: Automated meeting documentation and action item tracking
- **PMO Report Generator**: Automated executive reporting from project data

### 1.2 What's Included

**Implemented Components:**
- ✅ Meeting Assistant Python implementation
- ✅ PMO Report Generator Python implementation
- ✅ OpenRouter API integration
- ✅ JSON input/output handling
- ✅ Email notification generation
- ✅ HTML report generation
- ✅ Jira export format
- ✅ Error handling and retry logic

**Documentation:**
- ✅ Comprehensive analysis document
- ✅ Structured deliverables summary
- ✅ Implementation guide (this document)
- ✅ Agent-specific README

### 1.3 Prerequisites

**Required:**
- Python 3.8 or higher
- OpenRouter API key (get from https://openrouter.ai/)
- Internet connectivity

**Optional (for integrations):**
- Jira API access
- Microsoft Teams API access
- SMTP server for email notifications
- PostgreSQL database (for production)

---

## 2. Architecture

### 2.1 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Applications                      │
│  (Meeting platforms, Jira, Excel, Email clients)            │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    ProjMAN AI Agents                         │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │  Meeting Assistant   │  │ PMO Report Generator │        │
│  │                      │  │                      │        │
│  │ - Transcript process │  │ - Data collection    │        │
│  │ - Minutes generation │  │ - Trend analysis     │        │
│  │ - Action extraction  │  │ - Report generation  │        │
│  └──────────┬───────────┘  └──────────┬───────────┘        │
│             │                          │                     │
│             └──────────┬───────────────┘                     │
│                        ▼                                     │
│              ┌──────────────────┐                           │
│              │  OpenRouter API  │                           │
│              │ Claude 3.5 Haiku │                           │
│              └──────────────────┘                           │
└─────────────────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   Data Storage Layer                         │
│  (PostgreSQL, Redis, File System)                           │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Component Architecture

**Meeting Assistant:**
```
Input (JSON) → Prompt Builder → OpenRouter API → Response Parser → Output (JSON)
                                                                    ↓
                                                          Email Generator
                                                          Jira Exporter
```

**PMO Report Generator:**
```
Input (JSON) → Prompt Builder → OpenRouter API → Response Parser → Output (JSON)
                                                                    ↓
                                                          HTML Generator
                                                          Excel Exporter
```

### 2.3 Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| Language | Python | 3.8+ | Core implementation |
| AI API | OpenRouter | Latest | AI model access |
| AI Model | Claude 3.5 Haiku | Latest | Natural language processing |
| HTTP Client | requests | 2.31.0+ | API communication |
| Date/Time | python-dateutil | 2.8.2+ | Date parsing |
| Database | PostgreSQL | 14+ | Data storage (optional) |
| Queue | Redis | 7+ | Async processing (optional) |

---

## 3. Installation

### 3.1 Basic Installation

**Step 1: Clone the repository**
```bash
git clone https://github.com/markbunyevacz/ProjMAN.git
cd ProjMAN
```

**Step 2: Install dependencies**
```bash
cd agents
pip install -r requirements.txt
```

**Step 3: Set up environment variables**
```bash
export OPENROUTER_API_KEY="your-api-key-here"
```

### 3.2 Virtual Environment Setup (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r agents/requirements.txt
```

### 3.3 Docker Installation (Optional)

```bash
# Build Docker image
docker build -t projman-agents .

# Run with environment variables
docker run -e OPENROUTER_API_KEY="your-key" projman-agents
```

### 3.4 Verification

Test the installation:
```bash
cd agents
python -c "from meeting_assistant import MeetingAssistant; print('Meeting Assistant OK')"
python -c "from pmo_report_generator import PMOReportGenerator; print('PMO Report Generator OK')"
```

---

## 4. Configuration

### 4.1 Environment Variables

**Required:**
```bash
OPENROUTER_API_KEY="sk-or-v1-..."  # Your OpenRouter API key
```

**Optional:**
```bash
# API Configuration
OPENROUTER_MODEL="anthropic/claude-3.5-haiku"  # AI model to use
OPENROUTER_TIMEOUT=60  # API timeout in seconds
OPENROUTER_MAX_RETRIES=3  # Number of retry attempts

# Database (for production)
DATABASE_URL="postgresql://user:pass@localhost/projman"

# Redis (for async processing)
REDIS_URL="redis://localhost:6379/0"

# Email (for notifications)
SMTP_HOST="smtp.gmail.com"
SMTP_PORT=587
SMTP_USER="your-email@gmail.com"
SMTP_PASSWORD="your-password"

# Jira (for integration)
JIRA_URL="https://yourcompany.atlassian.net"
JIRA_API_TOKEN="your-jira-token"
JIRA_PROJECT_KEY="PROJ"
```

### 4.2 Configuration File (Optional)

Create `config.json`:
```json
{
  "openrouter": {
    "model": "anthropic/claude-3.5-haiku",
    "timeout": 60,
    "max_retries": 3
  },
  "meeting_assistant": {
    "default_priority": "medium",
    "action_item_prefix": "AI-"
  },
  "pmo_report": {
    "risk_threshold": 0.7,
    "budget_variance_threshold": 0.1
  }
}
```

---

## 5. Usage Examples

### 5.1 Meeting Assistant - Basic Usage

**Python API:**
```python
from agents import MeetingAssistant

# Initialize
assistant = MeetingAssistant()

# Prepare meeting data
meeting_data = {
    "meeting_id": "meeting-001",
    "transcript": "Meeting discussion transcript here...",
    "participants": ["user1@example.com", "user2@example.com"],
    "meeting_title": "Weekly Status Meeting",
    "meeting_date": "2025-11-14T10:00:00Z",
    "create_jira_tickets": True
}

# Process meeting
meeting_minutes = assistant.process_meeting(meeting_data)

# Print results
print(f"Summary: {meeting_minutes['summary']}")
print(f"Action Items: {len(meeting_minutes['action_items'])}")
```

**Command Line:**
```bash
cd agents
python meeting_assistant.py ../demo_data/meeting_request.json
```

**Output:**
```json
{
  "summary": "Meeting summary...",
  "agenda_items": [...],
  "key_points": [...],
  "action_items": [...],
  "next_steps": [...]
}
```

### 5.2 Meeting Assistant - Email Notifications

```python
from agents import MeetingAssistant

assistant = MeetingAssistant()
meeting_minutes = assistant.process_meeting(meeting_data)

# Generate email for specific recipient
email_html = assistant.generate_email_notification(
    meeting_minutes, 
    "user@example.com"
)

# Send email (requires SMTP configuration)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart('alternative')
msg['Subject'] = "Meeting Minutes"
msg['From'] = "noreply@example.com"
msg['To'] = "user@example.com"

msg.attach(MIMEText(email_html, 'html'))

# Send via SMTP
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')
    server.send_message(msg)
```

### 5.3 Meeting Assistant - Jira Integration

```python
from agents import MeetingAssistant
import requests

assistant = MeetingAssistant()
meeting_minutes = assistant.process_meeting(meeting_data)

# Export to Jira format
jira_tickets = assistant.export_to_jira_format(meeting_minutes)

# Create tickets in Jira
jira_url = "https://yourcompany.atlassian.net"
jira_token = "your-api-token"
project_key = "PROJ"

for ticket in jira_tickets:
    ticket['project'] = {'key': project_key}
    
    response = requests.post(
        f"{jira_url}/rest/api/3/issue",
        headers={
            "Authorization": f"Bearer {jira_token}",
            "Content-Type": "application/json"
        },
        json={"fields": ticket}
    )
    
    if response.status_code == 201:
        print(f"Created ticket: {response.json()['key']}")
```

### 5.4 PMO Report Generator - Basic Usage

**Python API:**
```python
from agents import PMOReportGenerator

# Initialize
generator = PMOReportGenerator()

# Prepare project data
project_data = {
    "projects": [
        {
            "key": "PROJ-1",
            "name": "User Authentication",
            "status": "In Progress",
            "progress": 80,
            "issues": {"total": 25, "open": 5, "in_progress": 8, "done": 12},
            "budget": {"planned": 50000, "actual": 48000, "currency": "EUR"}
        }
    ],
    "period": {
        "start": "2025-11-01",
        "end": "2025-11-14"
    }
}

# Generate report
report = generator.generate_report(project_data)

# Print results
print(f"Total Projects: {report['executive_summary']['key_metrics']['total_projects']}")
print(f"At Risk: {report['executive_summary']['key_metrics']['at_risk']}")
```

**Command Line:**
```bash
cd agents
python pmo_report_generator.py ../demo_data/jira_demo_data.json
```

### 5.5 PMO Report Generator - HTML Report

```python
from agents import PMOReportGenerator

generator = PMOReportGenerator()
report = generator.generate_report(project_data)

# Generate HTML report
html_report = generator.generate_html_report(
    report, 
    project_data['period']
)

# Save to file
with open('pmo_report.html', 'w', encoding='utf-8') as f:
    f.write(html_report)

print("HTML report saved to pmo_report.html")
```

### 5.6 PMO Report Generator - Excel Export

```python
from agents import PMOReportGenerator
import pandas as pd

generator = PMOReportGenerator()
report = generator.generate_report(project_data)

# Export to Excel format
excel_data = generator.export_to_excel_format(report)

# Create Excel file using pandas
with pd.ExcelWriter('pmo_report.xlsx', engine='openpyxl') as writer:
    for sheet_name, sheet_data in excel_data.items():
        df = pd.DataFrame(
            sheet_data['rows'],
            columns=sheet_data['headers']
        )
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Excel report saved to pmo_report.xlsx")
```

---

## 6. API Reference

### 6.1 MeetingAssistant Class

#### `__init__(api_key: Optional[str] = None)`

Initialize the Meeting Assistant.

**Parameters:**
- `api_key` (str, optional): OpenRouter API key. If not provided, reads from `OPENROUTER_API_KEY` environment variable.

**Raises:**
- `ValueError`: If API key is not provided and not found in environment.

**Example:**
```python
assistant = MeetingAssistant(api_key="sk-or-v1-...")
```

#### `process_meeting(meeting_data: Dict) -> Dict`

Process a meeting transcript and generate structured meeting minutes.

**Parameters:**
- `meeting_data` (dict): Dictionary containing:
  - `meeting_id` (str): Unique meeting identifier
  - `transcript` (str): Meeting transcript text
  - `participants` (list): List of participant email addresses
  - `meeting_title` (str): Title of the meeting
  - `meeting_date` (str): ISO format date string
  - `create_jira_tickets` (bool, optional): Flag for Jira integration

**Returns:**
- `dict`: Structured meeting minutes with:
  - `summary` (str): Executive summary
  - `agenda_items` (list): Discussion topics
  - `key_points` (list): Important points
  - `action_items` (list): Action items with assignments
  - `next_steps` (list): Recommended next steps

**Raises:**
- `ValueError`: If transcript is missing
- `Exception`: If API call fails

**Example:**
```python
minutes = assistant.process_meeting({
    "meeting_id": "m001",
    "transcript": "Discussion about project status...",
    "participants": ["user@example.com"],
    "meeting_title": "Status Meeting",
    "meeting_date": "2025-11-14T10:00:00Z"
})
```

#### `generate_email_notification(meeting_minutes: Dict, recipient: str) -> str`

Generate an HTML email notification for meeting minutes.

**Parameters:**
- `meeting_minutes` (dict): Structured meeting minutes
- `recipient` (str): Email address of the recipient

**Returns:**
- `str`: HTML email content

**Example:**
```python
email_html = assistant.generate_email_notification(
    minutes, 
    "user@example.com"
)
```

#### `export_to_jira_format(meeting_minutes: Dict) -> List[Dict]`

Convert action items to Jira ticket format.

**Parameters:**
- `meeting_minutes` (dict): Structured meeting minutes

**Returns:**
- `list`: List of Jira ticket dictionaries

**Example:**
```python
jira_tickets = assistant.export_to_jira_format(minutes)
```

### 6.2 PMOReportGenerator Class

#### `__init__(api_key: Optional[str] = None)`

Initialize the PMO Report Generator.

**Parameters:**
- `api_key` (str, optional): OpenRouter API key. If not provided, reads from `OPENROUTER_API_KEY` environment variable.

**Raises:**
- `ValueError`: If API key is not provided and not found in environment.

**Example:**
```python
generator = PMOReportGenerator(api_key="sk-or-v1-...")
```

#### `generate_report(project_data: Dict) -> Dict`

Generate a PMO report from project data.

**Parameters:**
- `project_data` (dict): Dictionary containing:
  - `projects` (list): List of project dictionaries
  - `period` (dict): Reporting period with `start` and `end` dates

**Returns:**
- `dict`: Structured report with:
  - `executive_summary` (dict): High-level overview
  - `detailed_analysis` (dict): In-depth analysis

**Raises:**
- `ValueError`: If projects data is missing
- `Exception`: If API call fails

**Example:**
```python
report = generator.generate_report({
    "projects": [...],
    "period": {"start": "2025-11-01", "end": "2025-11-14"}
})
```

#### `generate_html_report(report: Dict, period: Dict) -> str`

Generate an HTML version of the PMO report.

**Parameters:**
- `report` (dict): Structured report data
- `period` (dict): Reporting period information

**Returns:**
- `str`: HTML report content

**Example:**
```python
html = generator.generate_html_report(report, period)
```

#### `export_to_excel_format(report: Dict) -> Dict`

Convert report to Excel-friendly format.

**Parameters:**
- `report` (dict): Structured report data

**Returns:**
- `dict`: Dictionary with sheets data for Excel export

**Example:**
```python
excel_data = generator.export_to_excel_format(report)
```

---

## 7. Integration Guide

### 7.1 Jira Integration

**Setup:**
1. Get Jira API token from https://id.atlassian.com/manage-profile/security/api-tokens
2. Set environment variables:
```bash
export JIRA_URL="https://yourcompany.atlassian.net"
export JIRA_API_TOKEN="your-token"
export JIRA_PROJECT_KEY="PROJ"
```

**Integration Code:**
```python
import os
import requests
from agents import MeetingAssistant

def create_jira_tickets_from_meeting(meeting_data):
    assistant = MeetingAssistant()
    minutes = assistant.process_meeting(meeting_data)
    tickets = assistant.export_to_jira_format(minutes)
    
    jira_url = os.getenv('JIRA_URL')
    jira_token = os.getenv('JIRA_API_TOKEN')
    project_key = os.getenv('JIRA_PROJECT_KEY')
    
    created_tickets = []
    for ticket in tickets:
        ticket['project'] = {'key': project_key}
        
        response = requests.post(
            f"{jira_url}/rest/api/3/issue",
            headers={
                "Authorization": f"Bearer {jira_token}",
                "Content-Type": "application/json"
            },
            json={"fields": ticket}
        )
        
        if response.status_code == 201:
            created_tickets.append(response.json()['key'])
    
    return created_tickets
```

### 7.2 Microsoft Teams Integration

**Setup:**
1. Register app in Azure AD
2. Get Teams API permissions
3. Implement webhook for meeting events

**Integration Code:**
```python
from agents import MeetingAssistant
import requests

def process_teams_meeting(meeting_id, access_token):
    # Get meeting transcript from Teams
    teams_url = f"https://graph.microsoft.com/v1.0/me/onlineMeetings/{meeting_id}/transcripts"
    
    response = requests.get(
        teams_url,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    
    transcript_data = response.json()
    
    # Process with Meeting Assistant
    assistant = MeetingAssistant()
    meeting_data = {
        "meeting_id": meeting_id,
        "transcript": transcript_data['content'],
        "participants": [p['email'] for p in transcript_data['participants']],
        "meeting_title": transcript_data['subject'],
        "meeting_date": transcript_data['startDateTime']
    }
    
    return assistant.process_meeting(meeting_data)
```

### 7.3 Email Integration (SMTP)

**Setup:**
```bash
export SMTP_HOST="smtp.gmail.com"
export SMTP_PORT=587
export SMTP_USER="your-email@gmail.com"
export SMTP_PASSWORD="your-app-password"
```

**Integration Code:**
```python
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from agents import MeetingAssistant

def send_meeting_minutes(meeting_data, recipients):
    assistant = MeetingAssistant()
    minutes = assistant.process_meeting(meeting_data)
    
    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')
    
    for recipient in recipients:
        email_html = assistant.generate_email_notification(minutes, recipient)
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Meeting Minutes: {meeting_data['meeting_title']}"
        msg['From'] = smtp_user
        msg['To'] = recipient
        
        msg.attach(MIMEText(email_html, 'html'))
        
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
```

### 7.4 Database Integration (PostgreSQL)

**Setup:**
```bash
export DATABASE_URL="postgresql://user:pass@localhost/projman"
```

**Schema:**
```sql
CREATE TABLE meetings (
    id SERIAL PRIMARY KEY,
    meeting_id VARCHAR(255) UNIQUE NOT NULL,
    title VARCHAR(500),
    date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE meeting_transcripts (
    id SERIAL PRIMARY KEY,
    meeting_id INTEGER REFERENCES meetings(id),
    transcript TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE action_items (
    id SERIAL PRIMARY KEY,
    meeting_id INTEGER REFERENCES meetings(id),
    description TEXT,
    assignee VARCHAR(255),
    assignee_email VARCHAR(255),
    due_date DATE,
    priority VARCHAR(50),
    status VARCHAR(50) DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reports (
    id SERIAL PRIMARY KEY,
    report_type VARCHAR(100),
    period_start DATE,
    period_end DATE,
    report_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Integration Code:**
```python
import os
import psycopg2
from agents import MeetingAssistant

def save_meeting_to_database(meeting_data, meeting_minutes):
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    cur = conn.cursor()
    
    # Insert meeting
    cur.execute(
        "INSERT INTO meetings (meeting_id, title, date) VALUES (%s, %s, %s) RETURNING id",
        (meeting_data['meeting_id'], meeting_data['meeting_title'], meeting_data['meeting_date'])
    )
    meeting_db_id = cur.fetchone()[0]
    
    # Insert transcript
    cur.execute(
        "INSERT INTO meeting_transcripts (meeting_id, transcript) VALUES (%s, %s)",
        (meeting_db_id, meeting_data['transcript'])
    )
    
    # Insert action items
    for item in meeting_minutes['action_items']:
        cur.execute(
            """INSERT INTO action_items 
               (meeting_id, description, assignee, assignee_email, due_date, priority) 
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (meeting_db_id, item['description'], item['assignee'], 
             item['assignee_email'], item['due_date'], item['priority'])
        )
    
    conn.commit()
    cur.close()
    conn.close()
```

---

## 8. Testing

### 8.1 Unit Tests

Create `tests/test_meeting_assistant.py`:
```python
import unittest
from agents import MeetingAssistant

class TestMeetingAssistant(unittest.TestCase):
    def setUp(self):
        self.assistant = MeetingAssistant()
    
    def test_initialization(self):
        self.assertIsNotNone(self.assistant.api_key)
        self.assertEqual(self.assistant.model, "anthropic/claude-3.5-haiku")
    
    def test_process_meeting_with_demo_data(self):
        meeting_data = {
            "meeting_id": "test-001",
            "transcript": "Test meeting discussion",
            "participants": ["test@example.com"],
            "meeting_title": "Test Meeting",
            "meeting_date": "2025-11-14T10:00:00Z"
        }
        
        # This requires a valid API key
        # minutes = self.assistant.process_meeting(meeting_data)
        # self.assertIn('summary', minutes)
        # self.assertIn('action_items', minutes)

if __name__ == '__main__':
    unittest.main()
```

### 8.2 Integration Tests

```bash
# Test with demo data
cd agents
python meeting_assistant.py ../demo_data/meeting_request.json
python pmo_report_generator.py ../demo_data/jira_demo_data.json
```

### 8.3 Manual Testing Checklist

- [ ] Meeting Assistant processes demo data successfully
- [ ] PMO Report Generator processes demo data successfully
- [ ] Email notifications generate valid HTML
- [ ] Jira export format is correct
- [ ] HTML reports render properly
- [ ] Error handling works for invalid input
- [ ] API retry logic functions correctly

---

## 9. Deployment

### 9.1 Production Checklist

- [ ] Environment variables configured
- [ ] Database schema created
- [ ] Redis/queue system set up
- [ ] API keys secured
- [ ] Logging configured
- [ ] Monitoring set up
- [ ] Backup strategy in place
- [ ] SSL/TLS certificates installed

### 9.2 Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY agents/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY agents/ ./agents/
COPY demo_data/ ./demo_data/

ENV PYTHONPATH=/app

CMD ["python", "agents/meeting_assistant.py"]
```

Build and run:
```bash
docker build -t projman-agents .
docker run -e OPENROUTER_API_KEY="your-key" projman-agents
```

### 9.3 Production Configuration

**Environment Variables:**
```bash
# Production settings
export ENVIRONMENT="production"
export LOG_LEVEL="INFO"
export OPENROUTER_API_KEY="sk-or-v1-..."
export DATABASE_URL="postgresql://..."
export REDIS_URL="redis://..."

# Security
export SECRET_KEY="your-secret-key"
export ALLOWED_HOSTS="yourdomain.com"

# Monitoring
export SENTRY_DSN="https://..."
```

---

## 10. Troubleshooting

### 10.1 Common Issues

**Issue: "OpenRouter API key is required"**
- **Cause:** API key not set
- **Solution:** Set `OPENROUTER_API_KEY` environment variable

**Issue: "API call failed after 3 attempts"**
- **Cause:** Network issues or API rate limiting
- **Solution:** Check internet connection, verify API key, check rate limits

**Issue: "Failed to parse JSON response"**
- **Cause:** Unexpected API response format
- **Solution:** Check API model version, review prompt structure

**Issue: "No JSON found in API response"**
- **Cause:** API returned non-JSON content
- **Solution:** Check API status, verify model availability

### 10.2 Debug Mode

Enable debug logging:
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Your code here
```

### 10.3 Support Resources

- **Documentation:** `/docs` directory
- **Demo Data:** `/demo_data` directory
- **GitHub Issues:** https://github.com/markbunyevacz/ProjMAN/issues
- **OpenRouter Docs:** https://openrouter.ai/docs

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-14  
**Maintained By:** ProjMAN Development Team
