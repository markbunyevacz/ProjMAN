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
    transcript: str = Field(..., description="Meeting transcript text")
    participants: List[str] = Field(..., description="List of participant emails")
    meeting_title: str = Field(..., description="Title of the meeting")
    meeting_date: str = Field(..., description="ISO format date string")
    create_jira_tickets: bool = Field(default=False, description="Create Jira tickets for action items")

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
        
        # Initialize agent
        agent = MeetingAssistant()
        
        # Prepare meeting data
        meeting_data = {
            "meeting_id": request.meeting_id,
            "transcript": request.transcript,
            "participants": request.participants,
            "meeting_title": request.meeting_title,
            "meeting_date": request.meeting_date,
            "create_jira_tickets": request.create_jira_tickets
        }
        
        # Process meeting
        minutes = agent.process_meeting(meeting_data)
        
        # Generate email notification (HTML)
        email_html = agent.generate_email_notification(minutes, request.participants[0] if request.participants else "")
        
        # Export to Jira format
        jira_tickets = agent.export_to_jira_format(minutes)
        
        logger.info(f"Meeting {request.meeting_id} processed successfully")
        
        return {
            "meeting_id": request.meeting_id,
            "status": "completed",
            "minutes": minutes,
            "email_html": email_html,
            "jira_tickets": jira_tickets
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
        
        # For demo purposes, use demo data if no projects provided
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
        
        logger.info(f"Report generated successfully")
        
        return {
            "report_id": f"report-{request.period_start}-{request.period_end}",
            "status": "completed",
            "report": report,
            "html_report": html_report,
            "excel_format": excel_format
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

