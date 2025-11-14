"""
External integrations for ProjMAN
Jira, Email (SMTP), and Microsoft Teams integrations
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List, Optional
import requests
import logging

logger = logging.getLogger(__name__)

class JiraIntegration:
    """Jira API integration for ticket creation"""
    
    def __init__(self):
        self.jira_url = os.getenv("JIRA_URL", "https://yourcompany.atlassian.net")
        self.api_token = os.getenv("JIRA_API_TOKEN")
        self.project_key = os.getenv("JIRA_PROJECT_KEY", "PROJ")
        self.email = os.getenv("JIRA_EMAIL")  # optional - for basic auth
        
        if not self.api_token:
            logger.warning("JIRA_API_TOKEN not set. Jira integration will not work.")
    
    def create_ticket(self, action_item: Dict) -> Optional[str]:
        """
        Create a Jira ticket from action item
        
        Args:
            action_item: Dictionary with description, assignee, priority, due_date
        
        Returns:
            Jira ticket ID or None if failed
        """
        if not self.api_token:
            logger.warning("Jira API token not configured. Skipping ticket creation.")
            return None
        
        try:
            url = f"{self.jira_url}/rest/api/3/issue"
            headers = {
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "fields": {
                    "project": {"key": self.project_key},
                    "summary": action_item.get("description", "Action Item"),
                    "description": {
                        "type": "doc",
                        "version": 1,
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": action_item.get("description", "")
                                    }
                                ]
                            }
                        ]
                    },
                    "issuetype": {"name": "Task"},
                    "priority": {"name": action_item.get("priority", "Medium").capitalize()}
                }
            }
            
            # Add assignee if email provided
            assignee = action_item.get("assignee")
            if assignee:
                payload["fields"]["assignee"] = {"emailAddress": assignee}
            
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            
            ticket_data = response.json()
            ticket_id = ticket_data.get("key")
            logger.info(f"Jira ticket created: {ticket_id}")
            return ticket_id
            
        except Exception as e:
            logger.error(f"Failed to create Jira ticket: {str(e)}")
            return None
    
    def create_tickets_bulk(self, action_items: List[Dict]) -> List[Optional[str]]:
        """Create multiple Jira tickets"""
        ticket_ids = []
        for item in action_items:
            ticket_id = self.create_ticket(item)
            ticket_ids.append(ticket_id)
        return ticket_ids
    
    def fetch_project_data(self, project_keys: List[str]) -> List[Dict]:
        """Fetch basic project metrics from Jira"""
        if not self.api_token:
            logger.warning("Jira API token not configured. Cannot fetch project data.")
            return []
        
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        projects = []
        for key in project_keys:
            try:
                response = requests.get(
                    f"{self.jira_url}/rest/api/3/project/{key}",
                    headers=headers,
                    timeout=30
                )
                response.raise_for_status()
                project_info = response.json()
                projects.append(
                    {
                        "key": key,
                        "name": project_info.get("name", key),
                        "lead": project_info.get("lead", {}).get("displayName"),
                        "projectType": project_info.get("projectTypeKey"),
                        "simplified": project_info.get("simplified"),
                        "self": project_info.get("self")
                    }
                )
            except Exception as exc:
                logger.warning(f"Failed to fetch Jira project {key}: {exc}")
        return projects

class EmailService:
    """SMTP email service for notifications"""
    
    def __init__(self):
        self.smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.from_email = os.getenv("SMTP_FROM", self.smtp_user)
        
        if not self.smtp_user or not self.smtp_password:
            logger.warning("SMTP credentials not set. Email sending will not work.")
    
    def send_email(
        self,
        to_emails: List[str],
        subject: str,
        html_content: str,
        text_content: Optional[str] = None
    ) -> bool:
        """
        Send email via SMTP
        
        Args:
            to_emails: List of recipient email addresses
            subject: Email subject
            html_content: HTML email body
            text_content: Plain text email body (optional)
        
        Returns:
            True if sent successfully, False otherwise
        """
        if not self.smtp_user or not self.smtp_password:
            logger.warning("SMTP not configured. Email not sent.")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.from_email
            msg['To'] = ', '.join(to_emails)
            
            # Add text and HTML parts
            if text_content:
                part1 = MIMEText(text_content, 'plain')
                msg.attach(part1)
            
            part2 = MIMEText(html_content, 'html')
            msg.attach(part2)
            
            # Send via SMTP
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
            
            logger.info(f"Email sent successfully to {len(to_emails)} recipients")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return False

class TeamsIntegration:
    """Microsoft Teams API integration"""
    
    def __init__(self):
        self.client_id = os.getenv("TEAMS_CLIENT_ID")
        self.client_secret = os.getenv("TEAMS_CLIENT_SECRET")
        self.tenant_id = os.getenv("TEAMS_TENANT_ID")
        
        if not all([self.client_id, self.client_secret, self.tenant_id]):
            logger.warning("Teams credentials not set. Teams integration will not work.")
    
    def _get_access_token(self) -> Optional[str]:
        if not all([self.client_id, self.client_secret, self.tenant_id]):
            return None
        token_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "https://graph.microsoft.com/.default",
            "grant_type": "client_credentials"
        }
        try:
            response = requests.post(token_url, data=data, timeout=30)
            response.raise_for_status()
            return response.json().get("access_token")
        except Exception as exc:
            logger.warning(f"Failed to acquire Teams token: {exc}")
            return None
    
    def get_meeting_transcript(self, meeting_id: str) -> Optional[str]:
        """
        Get meeting transcript from Teams
        
        Args:
            meeting_id: Teams meeting ID
        
        Returns:
            Transcript text or None if failed
        """
        if not all([self.client_id, self.client_secret, self.tenant_id]):
            logger.warning("Teams not configured.")
            return None
        
        token = self._get_access_token()
        if not token:
            return None
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        # Microsoft Graph beta endpoint for transcripts
        url = f"https://graph.microsoft.com/beta/communications/onlineMeetings/{meeting_id}/transcripts"
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            data = response.json()
            transcript_entries = []
            for item in data.get("value", []):
                content = item.get("content", "")
                if content:
                    transcript_entries.append(content)
            transcript_text = "\n".join(transcript_entries).strip()
            if transcript_text:
                logger.info(f"Fetched transcript for meeting {meeting_id}")
                return transcript_text
        except Exception as exc:
            logger.warning(f"Failed to fetch Teams transcript: {exc}")
        return None

