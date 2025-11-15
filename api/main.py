"""
ProjMAN FastAPI Application
Main entry point for the REST API
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks, UploadFile, File, Form, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import os
import sys
from pathlib import Path
import logging
import time
import socket
import requests
from urllib.parse import urlparse
import uuid
import tempfile
import pandas as pd
from io import BytesIO

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.meeting_assistant import MeetingAssistant
from agents.pmo_report_generator import PMOReportGenerator
from core.database import DatabaseService
from core.integrations import JiraIntegration, EmailService, TeamsIntegration
from core.storage import StorageService
from core.logging_handler import get_log_handler

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add in-memory log handler
log_handler = get_log_handler()
logger.addHandler(log_handler)
# Also add to root logger to catch all logs
logging.getLogger().addHandler(log_handler)

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
        warnings: List[Dict[str, Any]] = []
        
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
            if not jira_service.api_token:
                warnings.append({
                    "type": "jira_not_configured",
                    "message": "Jira ticket creation requested but Jira integration is not configured. No tickets created.",
                    "severity": "warning"
                })

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
            if not (email_service.smtp_user and email_service.smtp_password):
                warnings.append({
                    "type": "email_not_configured",
                    "message": "Email notifications requested but SMTP is not configured.",
                    "severity": "warning"
                })
            if not email_sent and (email_service.smtp_user and email_service.smtp_password):
                warnings.append({
                    "type": "email_failed",
                    "message": "Email notification failed to send.",
                    "severity": "error"
                })
        
        logger.info(f"Meeting {request.meeting_id} processed successfully")
        
        return {
            "meeting_id": request.meeting_id,
            "status": "completed",
            "minutes": minutes,
            "email_html": email_html,
            "jira_tickets": jira_tickets,
            "created_jira_ids": created_jira_ids,
            "email_sent": email_sent,
            "meeting_record_id": meeting_record_id,
            "warnings": warnings,
            "info": {
                "data_source": "teams" if request.teams_meeting_id else "transcript",
                "integrations_used": [
                    name for name, used in [
                        ("jira", bool(created_jira_ids)),
                        ("email", email_sent)
                    ] if used
                ]
            }
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
        warnings: List[Dict[str, Any]] = []
        
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
            if not jira_service.api_token:
                warnings.append({
                    "type": "jira_not_configured",
                    "message": f"Jira projects requested ({', '.join(request.jira_projects)}) but Jira integration is not configured.",
                    "severity": "warning",
                    "fallback": True
                })

        # For demo purposes, use demo data if still no projects provided
        if not project_data["projects"]:
            demo_data_path = Path(__file__).parent.parent / "demo_data" / "jira_demo_data.json"
            if demo_data_path.exists():
                import json
                with open(demo_data_path, 'r', encoding='utf-8') as f:
                    demo_data = json.load(f)
                    project_data["projects"] = demo_data.get("projects", [])
                    logger.info("Using demo project data")
                    warnings.append({
                        "type": "demo_data_used",
                        "message": "Using demo data from demo_data/jira_demo_data.json.",
                        "severity": "info",
                        "fallback": True
                    })
            else:
                warnings.append({
                    "type": "no_project_data",
                    "message": "No project data available. Provide jira_projects or Excel data.",
                    "severity": "error"
                })
        
        # Excel input note (not implemented)
        if request.excel_files:
            warnings.append({
                "type": "excel_not_implemented",
                "message": f"Excel files provided ({len(request.excel_files)}) but processing is not implemented.",
                "severity": "warning"
            })
        
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
            if not (email_service.smtp_user and email_service.smtp_password):
                warnings.append({
                    "type": "email_not_configured",
                    "message": "Email recipients provided but SMTP is not configured.",
                    "severity": "warning"
                })
            if not email_sent and (email_service.smtp_user and email_service.smtp_password):
                warnings.append({
                    "type": "email_failed",
                    "message": "Email distribution failed.",
                    "severity": "error"
                })
        
        logger.info("Report generated successfully")
        
        return {
            "report_id": f"report-{request.period_start}-{request.period_end}",
            "status": "completed",
            "report": report,
            "html_report": html_report,
            "excel_format": excel_format,
            "report_record_id": report_record_id,
            "email_sent": email_sent,
            "warnings": warnings,
            "info": {
                "data_source": "jira" if warnings and not any(w.get("type") == "demo_data_used" for w in warnings) and project_data["projects"] else ("demo_data" if project_data["projects"] else "none"),
                "projects_count": len(project_data["projects"]),
                "integrations_used": [
                    name for name, used in [
                        ("email", email_sent)
                    ] if used
                ]
            }
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

# Integrations status endpoint
@app.get("/api/v1/integrations/status")
async def get_integrations_status():
    """Return status of configured integrations for UI visibility."""
    jira_service = JiraIntegration()
    email_service = EmailService()
    teams_service = TeamsIntegration()
    # Helpers
    def _uptime_seconds() -> int:
        # best-effort: use process start time stored in module global
        return int(time.time() - START_TIME)

    def _smtp_connect_ms(host: Optional[str], port: Optional[int], timeout: float = 3.0) -> Optional[int]:
        if not host or not port:
            return None
        try:
            t0 = time.time()
            with socket.create_connection((host, int(port)), timeout=timeout):
                return int((time.time() - t0) * 1000)
        except Exception:
            return None

    def _http_ping(url: Optional[str], headers: Optional[Dict[str, str]] = None, timeout: float = 3.0) -> Dict[str, Optional[int]]:
        if not url:
            return {"ms": None, "code": None}
        try:
            t0 = time.time()
            r = requests.get(url, headers=headers or {}, timeout=timeout)
            return {"ms": int((time.time() - t0) * 1000), "code": r.status_code}
        except Exception:
            return {"ms": None, "code": None}

    def _redis_connect_ms(redis_url: Optional[str], timeout: float = 2.0) -> Optional[int]:
        if not redis_url:
            return None
        try:
            parsed = urlparse(redis_url)
            host = parsed.hostname
            port = parsed.port or 6379
            t0 = time.time()
            with socket.create_connection((host, int(port)), timeout=timeout):
                return int((time.time() - t0) * 1000)
        except Exception:
            return None

    def _db_connect_ms() -> Optional[int]:
        try:
            from core.database import engine
            t0 = time.time()
            with engine.connect() as conn:
                conn.execute("SELECT 1")
            return int((time.time() - t0) * 1000)
        except Exception:
            return None

    def _db_counts() -> Dict[str, Optional[int]]:
        try:
            from core.database import SessionLocal, Meeting, Report
            db = SessionLocal()
            try:
                meetings_count = db.query(Meeting).count()
                reports_count = db.query(Report).count()
                return {"meetings": meetings_count, "reports": reports_count}
            finally:
                db.close()
        except Exception:
            return {"meetings": None, "reports": None}

    # Globals/env
    openrouter_model = os.getenv("OPENROUTER_MODEL")
    openrouter_key_present = bool(os.getenv("OPENROUTER_API_KEY"))
    app_version = app.version if hasattr(app, "version") else None
    redis_url = os.getenv("REDIS_URL")
    s3_endpoint = os.getenv("S3_ENDPOINT")
    smtp_host = email_service.smtp_host
    smtp_port = email_service.smtp_port

    # Pings
    openrouter_ping = _http_ping(
        "https://openrouter.ai/api/v1/models" if openrouter_key_present else "https://openrouter.ai/api/v1",
        headers={"Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY') or ''}"} if openrouter_key_present else None
    )
    jira_ping = _http_ping(
        f"{jira_service.jira_url}/rest/api/3/project" if jira_service.api_token else jira_service.jira_url,
        headers={"Authorization": f"Bearer {jira_service.api_token}"} if jira_service.api_token else None
    )
    smtp_connect_ms = _smtp_connect_ms(smtp_host, smtp_port)
    redis_connect_ms = _redis_connect_ms(redis_url)
    minio_ping = _http_ping(f"{s3_endpoint}/minio/health/live" if s3_endpoint else None)
    db_connect = _db_connect_ms()
    counts = _db_counts()

    return {
        "api": {
            "version": app_version,
            "uptime_seconds": _uptime_seconds()
        },
        "openrouter": {
            "configured": openrouter_key_present,
            "model": openrouter_model,
            "ping_ms": openrouter_ping.get("ms"),
            "last_code": openrouter_ping.get("code")
        },
        "jira": {
            "configured": bool(jira_service.api_token),
            "url": jira_service.jira_url if jira_service.api_token else None,
            "status": "configured" if jira_service.api_token else "not_configured",
            "message": "Jira integration is configured" if jira_service.api_token else "Jira API token not set",
            "ping_ms": jira_ping.get("ms"),
            "last_code": jira_ping.get("code")
        },
        "email_smtp": {
            "configured": bool(email_service.smtp_user and email_service.smtp_password),
            "host": email_service.smtp_host if email_service.smtp_user else None,
            "port": email_service.smtp_port if email_service.smtp_user else None,
            "status": "configured" if (email_service.smtp_user and email_service.smtp_password) else "not_configured",
            "message": "Email service is configured" if (email_service.smtp_user and email_service.smtp_password) else "SMTP credentials not set",
            "connect_ms": smtp_connect_ms
        },
        "teams": {
            "configured": bool(teams_service.client_id and teams_service.client_secret and teams_service.tenant_id),
            "status": "configured" if all([teams_service.client_id, teams_service.client_secret, teams_service.tenant_id]) else "not_configured",
            "message": "Teams integration is configured" if all([teams_service.client_id, teams_service.client_secret, teams_service.tenant_id]) else "Teams credentials not set"
        },
        "database_postgres": {
            "configured": bool(os.getenv("DATABASE_URL")),
            "status": "configured" if os.getenv("DATABASE_URL") else "optional",
            "message": "Database is configured" if os.getenv("DATABASE_URL") else "Database is optional (using defaults)",
            "connect_ms": db_connect,
            "counts": counts
        },
        "redis": {
            "configured": bool(redis_url),
            "url": redis_url,
            "connect_ms": redis_connect_ms
        },
        "minio": {
            "configured": bool(s3_endpoint),
            "endpoint": s3_endpoint,
            "ping_ms": minio_ping.get("ms"),
            "last_code": minio_ping.get("code")
        }
    }

# New API endpoints for enhanced UI functionality

@app.get("/api/v1/jira/projects")
async def list_jira_projects(search: Optional[str] = Query(None)):
    """
    List all accessible Jira projects for dynamic dropdown.
    Returns empty list if Jira is not configured.
    """
    jira_service = JiraIntegration()
    if not jira_service.api_token:
        return {"projects": [], "total": 0, "message": "Jira integration not configured"}
    
    projects = jira_service.list_projects(search=search)
    return {
        "projects": projects,
        "total": len(projects)
    }

@app.post("/api/v1/files/upload")
async def upload_file(
    file: UploadFile = File(...),
    purpose: str = Form("pmo_report")
):
    """
    Upload Excel file for PMO report processing.
    Stores file in S3/MinIO and returns file metadata.
    """
    try:
        # Validate file type
        if not file.filename.endswith(('.xlsx', '.xls')):
            raise HTTPException(
                status_code=400,
                detail="Only Excel files (.xlsx, .xls) are supported"
            )
        
        # Read file content
        contents = await file.read()
        file_size = len(contents)
        
        # Max file size: 10MB
        if file_size > 10 * 1024 * 1024:
            raise HTTPException(
                status_code=400,
                detail="File size exceeds 10MB limit"
            )
        
        # Generate unique file ID
        file_id = str(uuid.uuid4())
        file_ext = Path(file.filename).suffix
        object_name = f"{purpose}/{file_id}{file_ext}"
        
        # Upload to storage
        storage_service = StorageService()
        
        # Save to temp file first
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp_file:
            tmp_file.write(contents)
            tmp_path = tmp_file.name
        
        try:
            # Upload to S3
            url = storage_service.upload_file(tmp_path, object_name=object_name)
            
            # Try to parse Excel to validate
            try:
                df = pd.read_excel(BytesIO(contents))
                row_count = len(df)
                col_count = len(df.columns)
            except Exception as parse_error:
                logger.warning(f"Excel parse warning: {parse_error}")
                row_count = None
                col_count = None
            
            return {
                "file_id": file_id,
                "filename": file.filename,
                "url": url,
                "size": file_size,
                "rows": row_count,
                "columns": col_count,
                "processed": False,
                "message": "File uploaded successfully"
            }
        finally:
            # Clean up temp file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
                
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"File upload failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"File upload failed: {str(e)}"
        )

@app.get("/api/v1/logs/recent")
async def get_recent_logs(
    limit: int = Query(5, ge=1, le=50),
    level: Optional[str] = Query(None)
):
    """
    Get recent log entries for error panel display.
    """
    log_handler = get_log_handler()
    logs = log_handler.get_recent_logs(limit=limit, level=level)
    
    return {
        "logs": logs,
        "total": len(logs),
        "limit": limit,
        "level_filter": level
    }

@app.post("/api/v1/meetings/send-test-email")
async def send_test_email(request: Dict[str, Any]):
    """
    Send test email for meeting minutes preview.
    """
    recipient = request.get("recipient")
    subject = request.get("subject", "Test Email")
    html_content = request.get("html_content", "")
    
    if not recipient:
        raise HTTPException(status_code=400, detail="Recipient email is required")
    
    email_service = EmailService()
    success = email_service.send_email(
        [recipient],
        subject,
        html_content
    )
    
    if success:
        return {
            "sent": True,
            "message": "Email sent successfully"
        }
    else:
        raise HTTPException(
            status_code=500,
            detail="Email sending failed. Check SMTP configuration."
        )

@app.get("/api/v1/reports/download/{format}")
async def download_report(
    format: str,
    report_id: Optional[str] = Query(None)
):
    """
    Download report in specified format (html, excel, pdf).
    Currently returns mock data if report_id not provided.
    """
    if format not in ["html", "excel", "pdf"]:
        raise HTTPException(
            status_code=400,
            detail="Format must be one of: html, excel, pdf"
        )
    
    # For now, return error if no report_id
    # In full implementation, fetch from database
    if not report_id:
        raise HTTPException(
            status_code=400,
            detail="report_id query parameter is required"
        )
    
    # Mock implementation - in production, fetch from database
    # and generate file on-the-fly
    if format == "html":
        return {
            "message": "HTML download not yet implemented. Use html_report from generate endpoint."
        }
    elif format == "excel":
        return {
            "message": "Excel download not yet implemented. Use excel_format from generate endpoint."
        }
    elif format == "pdf":
        raise HTTPException(
            status_code=501,
            detail="PDF generation not yet implemented"
        )

# App start time (for uptime)
START_TIME = time.time()

