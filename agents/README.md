# ProjMAN AI Agents

This directory contains the implementation of AI-powered agents for project management automation.

## Agents

### 1. Meeting Assistant (`meeting_assistant.py`)

Automatically generates meeting minutes and tracks action items from meeting transcripts.

**Features:**
- Processes meeting transcripts using Claude 3.5 Haiku via OpenRouter
- Extracts key discussion points and decisions
- Identifies and assigns action items
- Generates email notifications
- Exports to Jira ticket format

**Usage:**
```python
from agents import MeetingAssistant

assistant = MeetingAssistant()
meeting_minutes = assistant.process_meeting(meeting_data)
```

**Command Line:**
```bash
export OPENROUTER_API_KEY="your-api-key"
python meeting_assistant.py demo_data/meeting_request.json
```

### 2. PMO Report Generator (`pmo_report_generator.py`)

Automatically generates executive PMO reports from Jira data and other sources.

**Features:**
- Analyzes project data using Claude 3.5 Haiku via OpenRouter
- Identifies trends and risks
- Generates executive summaries
- Creates HTML reports
- Exports to Excel format

**Usage:**
```python
from agents import PMOReportGenerator

generator = PMOReportGenerator()
report = generator.generate_report(project_data)
```

**Command Line:**
```bash
export OPENROUTER_API_KEY="your-api-key"
python pmo_report_generator.py demo_data/jira_demo_data.json
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
export OPENROUTER_API_KEY="your-openrouter-api-key"
```

## Configuration

Both agents use the OpenRouter API with Claude 3.5 Haiku model. You need an OpenRouter API key to use these agents.

Get your API key from: https://openrouter.ai/

## API Reference

### MeetingAssistant

**`__init__(api_key: Optional[str] = None)`**
- Initialize the Meeting Assistant
- `api_key`: OpenRouter API key (optional, reads from env var if not provided)

**`process_meeting(meeting_data: Dict) -> Dict`**
- Process a meeting transcript and generate structured minutes
- `meeting_data`: Dictionary with transcript, participants, title, date
- Returns: Structured meeting minutes with action items

**`generate_email_notification(meeting_minutes: Dict, recipient: str) -> str`**
- Generate HTML email notification
- Returns: HTML email content

**`export_to_jira_format(meeting_minutes: Dict) -> List[Dict]`**
- Convert action items to Jira ticket format
- Returns: List of Jira ticket dictionaries

### PMOReportGenerator

**`__init__(api_key: Optional[str] = None)`**
- Initialize the PMO Report Generator
- `api_key`: OpenRouter API key (optional, reads from env var if not provided)

**`generate_report(project_data: Dict) -> Dict`**
- Generate a PMO report from project data
- `project_data`: Dictionary with projects list and period
- Returns: Structured report with executive summary and analysis

**`generate_html_report(report: Dict, period: Dict) -> str`**
- Generate HTML version of the report
- Returns: HTML report content

**`export_to_excel_format(report: Dict) -> Dict`**
- Convert report to Excel-friendly format
- Returns: Dictionary with sheets data

## Examples

See the `demo_data/` directory for example input files:
- `meeting_request.json`: Example meeting data
- `jira_demo_data.json`: Example Jira project data

## Error Handling

Both agents include:
- Retry logic for API calls (3 attempts)
- JSON parsing with error handling
- Validation of required fields
- Timeout handling (60 seconds)

## Performance

- Meeting processing: ~5-10 seconds
- PMO report generation: ~5-10 seconds
- API rate limit: 100 requests/minute (OpenRouter default)

## Security

- API keys should be stored in environment variables
- Never commit API keys to version control
- Use HTTPS for all API communications

## License

MIT License - See LICENSE file for details
