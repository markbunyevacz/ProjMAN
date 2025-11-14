"""
Database layer for ProjMAN
PostgreSQL connection and models using SQLAlchemy
"""

import os
from datetime import datetime
from typing import Optional, List
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Text, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

# Base
Base = declarative_base()

# Database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://demo:demo123@localhost:5432/agentize_demo")

# Create engine
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models
class Meeting(Base):
    """Meeting metadata table"""
    __tablename__ = "meetings"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    external_id = Column(String(255), unique=True, nullable=False)
    title = Column(String(500))
    date = Column(DateTime)
    duration_minutes = Column(Integer)
    participants = Column(JSON)  # ["email1", "email2"]
    audio_url = Column(Text)
    transcript = Column(Text)
    status = Column(String(50), default="pending")  # pending, processing, completed, failed
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    minutes = relationship("MeetingMinutes", back_populates="meeting", uselist=False)
    action_items = relationship("ActionItem", back_populates="meeting")

class MeetingMinutes(Base):
    """Meeting minutes table"""
    __tablename__ = "meeting_minutes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    meeting_id = Column(UUID(as_uuid=True), ForeignKey("meetings.id"))
    summary = Column(Text)
    agenda_items = Column(JSON)
    key_points = Column(JSON)
    action_items_data = Column(JSON)
    next_steps = Column(JSON)
    minutes_pdf_url = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    meeting = relationship("Meeting", back_populates="minutes")

class ActionItem(Base):
    """Action items table"""
    __tablename__ = "action_items"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    meeting_id = Column(UUID(as_uuid=True), ForeignKey("meetings.id"))
    description = Column(Text)
    assignee_email = Column(String(255))
    due_date = Column(DateTime)
    priority = Column(String(20))
    jira_ticket_id = Column(String(100))
    status = Column(String(50), default="open")  # open, in_progress, completed
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    meeting = relationship("Meeting", back_populates="action_items")

class Report(Base):
    """Reports table"""
    __tablename__ = "reports"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    report_type = Column(String(50))  # weekly, monthly, quarterly
    period_start = Column(DateTime)
    period_end = Column(DateTime)
    status = Column(String(50), default="generating")  # generating, completed, failed
    pdf_url = Column(Text)
    excel_url = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    data = relationship("ReportData", back_populates="report")
    analysis = relationship("ReportAnalysis", back_populates="report", uselist=False)

class ReportData(Base):
    """Report data table"""
    __tablename__ = "report_data"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    report_id = Column(UUID(as_uuid=True), ForeignKey("reports.id"))
    source = Column(String(50))  # jira, excel, manual
    data_type = Column(String(50))  # projects, tickets, budget
    raw_data = Column(JSON)
    processed_data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    report = relationship("Report", back_populates="data")

class ReportAnalysis(Base):
    """Report analysis table"""
    __tablename__ = "report_analysis"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    report_id = Column(UUID(as_uuid=True), ForeignKey("reports.id"))
    executive_summary = Column(JSON)
    trends = Column(JSON)
    risks = Column(JSON)
    recommendations = Column(JSON)
    ai_model_version = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    report = relationship("Report", back_populates="analysis")

# Database functions
def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized successfully")

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Database service layer
class DatabaseService:
    """Service layer for database operations"""
    
    def __init__(self):
        self.session = SessionLocal()
    
    def save_meeting(self, meeting_data: dict, minutes: dict) -> str:
        """Save meeting and minutes to database"""
        try:
            # Create meeting record
            meeting = Meeting(
                external_id=meeting_data["meeting_id"],
                title=meeting_data["meeting_title"],
                date=datetime.fromisoformat(meeting_data["meeting_date"].replace('Z', '+00:00')),
                participants=meeting_data["participants"],
                transcript=meeting_data["transcript"],
                status="completed"
            )
            self.session.add(meeting)
            self.session.flush()
            
            # Create meeting minutes
            meeting_minutes = MeetingMinutes(
                meeting_id=meeting.id,
                summary=minutes.get("summary"),
                agenda_items=minutes.get("agenda_items"),
                key_points=minutes.get("key_points"),
                action_items_data=minutes.get("action_items"),
                next_steps=minutes.get("next_steps")
            )
            self.session.add(meeting_minutes)
            
            # Create action items
            for item in minutes.get("action_items", []):
                action_item = ActionItem(
                    meeting_id=meeting.id,
                    description=item.get("description"),
                    assignee_email=item.get("assignee"),
                    priority=item.get("priority"),
                    status="open"
                )
                self.session.add(action_item)
            
            self.session.commit()
            return str(meeting.id)
            
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Database save failed: {str(e)}")
    
    def save_report(self, report_data: dict, analysis: dict) -> str:
        """Save report to database"""
        try:
            # Create report record
            report = Report(
                report_type=report_data.get("report_type"),
                period_start=datetime.fromisoformat(report_data["period"]["start"]),
                period_end=datetime.fromisoformat(report_data["period"]["end"]),
                status="completed"
            )
            self.session.add(report)
            self.session.flush()
            
            # Create report analysis
            report_analysis = ReportAnalysis(
                report_id=report.id,
                executive_summary=analysis.get("executive_summary"),
                trends=analysis.get("detailed_analysis", {}).get("trends"),
                risks=analysis.get("executive_summary", {}).get("critical_risks"),
                recommendations=analysis.get("executive_summary", {}).get("recommendations"),
                ai_model_version="claude-3.5-haiku"
            )
            self.session.add(report_analysis)
            
            self.session.commit()
            return str(report.id)
            
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Database save failed: {str(e)}")
    
    def close(self):
        """Close database session"""
        self.session.close()

