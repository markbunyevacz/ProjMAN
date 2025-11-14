"""
ProjMAN FastAPI Application
Main entry point for the REST API
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import os
import sys
from pathlib import Path
import logging

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.meeting_assistant import MeetingAssistant
from agents.pmo_report_generator import PMOReportGenerator
from core.database import DatabaseService
from core.integrations import JiraIntegration, EmailService, TeamsIntegration

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI(
    title="ProjMAN AI Agents API",
    description="REST API for Meeting Assistant and PMO Report Generator",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production: specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class MeetingProcessRequest(BaseModel):
    meeting_id: str = Field(..., description="Unique meeting identifier")
    transcript: Optional[str] = Field(None, description="Meeting transcript text")
    participants: List[str] = Field(default_factory=list, description="List of participant emails")
    meeting_title: str = Field(..., description="Title of the meeting")
    meeting_date: str = Field(..., description="ISO format date string")
    teams_meeting_id: Optional[str] = Field(
        default=None,
        description="Microsoft Teams meeting ID (optional - transcript fetch)"
    )
    create_jira_tickets: bool = Field(default=False, description="Create Jira tickets for action items")
    send_email_notifications: bool = Field(default=True, description="Send meeting minutes via email")

class ReportGenerateRequest(BaseModel):
    report_type: str = Field(..., description="Report type: weekly, monthly, quarterly")
    period_start: str = Field(..., description="Period start date (YYYY-MM-DD)")
    period_end: str = Field(..., description="Period end date (YYYY-MM-DD)")
    jira_projects: List[str] = Field(default=[], description="List of Jira project keys")
    excel_files: List[str] = Field(default=[], description="List of Excel file paths")
    recipients: List[str] = Field(default=[], description="Email recipients")

# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "agents": ["meeting_assistant", "pmo_report_generator"]
    }

# Meeting Assistant endpoints
@app.post("/api/v1/meetings/process")
async def process_meeting(request: MeetingProcessRequest, background_tasks: BackgroundTasks):
    """
    Process a meeting transcript and generate structured meeting minutes.
    
    This endpoint uses the Meeting Assistant AI agent to:
    - Analyze meeting transcripts
    - Extract key points and decisions
    - Identify action items with assignments
    - Generate structured meeting minutes
    """
    try:
        logger.info(f"Processing meeting: {request.meeting_id}")
        
        # Initialize services
        agent = MeetingAssistant()
        jira_service = JiraIntegration()
        email_service = EmailService()
        teams_service = TeamsIntegration()
        db_service = None
        transcript = request.transcript
        
        if not transcript and request.teams_meeting_id:
            transcript = teams_service.get_meeting_transcript(request.teams_meeting_id)

        if not transcript:
            raise HTTPException(status_code=400, detail="Transcript is required (provide text or teams_meeting_id)")

        # Prepare meeting data
        meeting_data = {
            "meeting_id": request.meeting_id,
            "transcript": transcript,
            "participants": request.participants,
            "meeting_title": request.meeting_title,
            "meeting_date": request.meeting_date,
            "create_jira_tickets": request.create_jira_tickets
        }
        
        # Process meeting
        minutes = agent.process_meeting(meeting_data)
        
        # Generate email notification (HTML)
        email_html = agent.generate_email_notification(
            minutes,
            request.participants[0] if request.participants else ""
        )

        # Export to Jira format
        jira_tickets = agent.export_to_jira_format(minutes)

        # Optional database save
        meeting_record_id = None
        try:
            db_service = DatabaseService()
            meeting_record_id = db_service.save_meeting(meeting_data, minutes)
        except Exception as db_error:
            logger.warning(f"Database save skipped: {db_error}")
        finally:
            if db_service:
                db_service.close()

        # Optional Jira ticket creation
        created_jira_ids: List[Optional[str]] = []
        if request.create_jira_tickets:
            created_jira_ids = jira_service.create_tickets_bulk(minutes.get("action_items", []))

        # Optional email notifications
        email_sent = False
        if request.participants and request.send_email_notifications:
            subject = f"Meeting Minutes - {request.meeting_title}"
            email_sent = email_service.send_email(
                request.participants,
                subject,
                email_html,
                minutes.get("summary", "")
            )
        
        logger.info(f"Meeting {request.meeting_id} processed successfully")
        
        return {
            "meeting_id": request.meeting_id,
            "status": "completed",
            "minutes": minutes,
            "email_html": email_html,
            "jira_tickets": jira_tickets,
            "created_jira_ids": created_jira_ids,
            "email_sent": email_sent,
            "meeting_record_id": meeting_record_id
        }
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error processing meeting: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/api/v1/meetings/{meeting_id}")
async def get_meeting(meeting_id: str):
    """
    Get meeting details by ID.
    Note: Currently returns mock data. Implement database storage for real data.
    """
    return {
        "meeting_id": meeting_id,
        "status": "completed",
        "message": "Meeting data retrieval requires database integration"
    }

# PMO Report Generator endpoints
@app.post("/api/v1/reports/generate")
async def generate_report(request: ReportGenerateRequest, background_tasks: BackgroundTasks):
    """
    Generate a PMO executive report from project data.
    
    This endpoint uses the PMO Report Generator AI agent to:
    - Analyze project data from Jira and Excel
    - Identify trends and risks
    - Generate executive summaries
    - Create actionable recommendations
    """
    try:
        logger.info(f"Generating {request.report_type} report for {request.period_start} to {request.period_end}")
        
        # Initialize agent
        agent = PMOReportGenerator()
        jira_service = JiraIntegration()
        email_service = EmailService()
        db_service = None
        
        # Prepare project data
        # Note: This is a simplified version. Full implementation should fetch from Jira API
        project_data = {
            "projects": [],  # Would be populated from Jira API
            "period": {
                "start": request.period_start,
                "end": request.period_end
            },
            "report_type": request.report_type
        }
        
        # Fetch Jira data if project keys provided
        if request.jira_projects:
            fetched_projects = jira_service.fetch_project_data(request.jira_projects)
            project_data["projects"] = fetched_projects

        # For demo purposes, use demo data if still no projects provided
        if not project_data["projects"]:
            demo_data_path = Path(__file__).parent.parent / "demo_data" / "jira_demo_data.json"
            if demo_data_path.exists():
                import json
                with open(demo_data_path, 'r', encoding='utf-8') as f:
                    demo_data = json.load(f)
                    project_data["projects"] = demo_data.get("projects", [])
                    logger.info("Using demo project data")
        
        # Generate report
        report = agent.generate_report(project_data)
        
        # Generate HTML report
        html_report = agent.generate_html_report(report, project_data["period"])
        
        # Generate Excel format
        excel_format = agent.export_to_excel_format(report)

        # Optional database save
        report_record_id = None
        try:
            db_service = DatabaseService()
            report_record_id = db_service.save_report(
                {
                    "report_type": request.report_type,
                    "period": {
                        "start": request.period_start,
                        "end": request.period_end
                    }
                },
                report
            )
        except Exception as db_error:
            logger.warning(f"Report database save skipped: {db_error}")
        finally:
            if db_service:
                db_service.close()

        # Optional email distribution
        email_sent = False
        if request.recipients:
            subject = f"PMO Report - {request.report_type.title()} ({request.period_start} → {request.period_end})"
            summary_text = report.get("executive_summary", {}).get("overview", "")
            email_sent = email_service.send_email(
                request.recipients,
                subject,
                html_report,
                summary_text
            )
        
        logger.info(f"Report generated successfully")
        
        return {
            "report_id": f"report-{request.period_start}-{request.period_end}",
            "status": "completed",
            "report": report,
            "html_report": html_report,
            "excel_format": excel_format,
            "report_record_id": report_record_id,
            "email_sent": email_sent
        }
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error generating report: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/api/v1/reports/{report_id}")
async def get_report(report_id: str):
    """
    Get report by ID.
    Note: Currently returns mock data. Implement database storage for real data.
    """
    return {
        "report_id": report_id,
        "status": "completed",
        "message": "Report data retrieval requires database integration"
    }

# Root endpoint
@app.get("/")
async def root():
    """API root endpoint with documentation links"""
    return {
        "message": "ProjMAN AI Agents API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "agents": {
            "meeting_assistant": "/api/v1/meetings/process",
            "pmo_report_generator": "/api/v1/reports/generate"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

