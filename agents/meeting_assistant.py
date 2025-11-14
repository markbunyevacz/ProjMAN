"""
Meeting Assistant AI Agent
Automatically generates meeting minutes and tracks action items from meeting transcripts.
"""

import os
import json
import re
from datetime import datetime
from typing import Dict, List, Optional
import requests


class MeetingAssistant:
    """
    AI-powered meeting assistant that processes meeting transcripts and generates
    structured meeting minutes with action items.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Meeting Assistant.
        
        Args:
            api_key: OpenRouter API key. If not provided, reads from OPENROUTER_API_KEY env var.
        """
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            raise ValueError("OpenRouter API key is required. Set OPENROUTER_API_KEY environment variable.")
        
        self.api_endpoint = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "anthropic/claude-3.5-haiku"
        self.max_retries = 3
        
    def process_meeting(self, meeting_data: Dict) -> Dict:
        """
        Process a meeting transcript and generate structured meeting minutes.
        
        Args:
            meeting_data: Dictionary containing:
                - meeting_id: Unique meeting identifier
                - transcript: Meeting transcript text
                - participants: List of participant emails
                - meeting_title: Title of the meeting
                - meeting_date: ISO format date string
                - create_jira_tickets: Boolean flag for Jira integration
        
        Returns:
            Dictionary containing structured meeting minutes with:
                - summary: Executive summary
                - agenda_items: List of discussion topics
                - key_points: Important points from the meeting
                - action_items: List of action items with assignments
                - next_steps: Recommended next steps
        """
        transcript = meeting_data.get('transcript', '')
        meeting_title = meeting_data.get('meeting_title', 'Meeting')
        meeting_date = meeting_data.get('meeting_date', datetime.now().isoformat())
        participants = meeting_data.get('participants', [])
        
        if not transcript:
            raise ValueError("Meeting transcript is required")
        
        prompt = self._build_meeting_analysis_prompt(
            transcript, meeting_title, meeting_date, participants
        )
        
        response = self._call_openrouter_api(prompt)
        meeting_minutes = self._parse_meeting_response(response)
        
        return meeting_minutes
    
    def _build_meeting_analysis_prompt(
        self, 
        transcript: str, 
        title: str, 
        date: str, 
        participants: List[str]
    ) -> str:
        """Build the prompt for meeting analysis."""
        return f"""You are an expert meeting assistant. Analyze the following meeting transcript and generate structured meeting minutes.

Meeting Title: {title}
Meeting Date: {date}
Participants: {', '.join(participants)}

Transcript:
{transcript}

Please provide a comprehensive analysis in the following JSON format:

{{
  "summary": "A concise executive summary of the meeting (2-3 sentences)",
  "agenda_items": [
    {{
      "topic": "Topic name",
      "discussion": "Summary of what was discussed",
      "decisions": "Key decisions made"
    }}
  ],
  "key_points": [
    "Important point 1",
    "Important point 2"
  ],
  "action_items": [
    {{
      "id": "AI-XXX",
      "description": "Clear description of the action item",
      "assignee": "Person's name from the transcript",
      "assignee_email": "email@example.com (extract from participants list)",
      "due_date": "YYYY-MM-DD (estimate based on context)",
      "priority": "high|medium|low"
    }}
  ],
  "next_steps": [
    "Next step 1",
    "Next step 2"
  ]
}}

Important guidelines:
1. Extract action items explicitly mentioned or implied in the transcript
2. Assign action items to specific people mentioned in the discussion
3. Estimate realistic due dates based on context (typically 3-7 days for urgent, 7-14 days for normal)
4. Prioritize action items as high (critical/urgent), medium (important), or low (nice to have)
5. Generate sequential action item IDs starting with AI-001
6. Be concise but comprehensive
7. Focus on actionable outcomes

Return ONLY the JSON object, no additional text."""

    def _call_openrouter_api(self, prompt: str) -> str:
        """
        Call the OpenRouter API with retry logic.
        
        Args:
            prompt: The prompt to send to the API
            
        Returns:
            The API response text
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/markbunyevacz/ProjMAN",
            "X-Title": "ProjMAN Meeting Assistant"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,
            "max_tokens": 4000
        }
        
        for attempt in range(self.max_retries):
            try:
                response = requests.post(
                    self.api_endpoint,
                    headers=headers,
                    json=payload,
                    timeout=60
                )
                response.raise_for_status()
                
                data = response.json()
                content = data['choices'][0]['message']['content']
                return content
                
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    raise Exception(f"API call failed after {self.max_retries} attempts: {str(e)}")
                continue
        
        raise Exception("Failed to get response from OpenRouter API")
    
    def _parse_meeting_response(self, response: str) -> Dict:
        """
        Parse the JSON response from the API.
        
        Args:
            response: Raw response text from API
            
        Returns:
            Parsed meeting minutes dictionary
        """
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError as e:
                raise Exception(f"Failed to parse JSON response: {str(e)}")
        else:
            raise Exception("No JSON found in API response")
    
    def generate_email_notification(self, meeting_minutes: Dict, recipient: str) -> str:
        """
        Generate an email notification for meeting minutes.
        
        Args:
            meeting_minutes: The structured meeting minutes
            recipient: Email address of the recipient
            
        Returns:
            HTML email content
        """
        action_items_html = ""
        for item in meeting_minutes.get('action_items', []):
            if item.get('assignee_email') == recipient:
                priority_color = {
                    'high': '#ff0000',
                    'medium': '#ff9900',
                    'low': '#00cc00'
                }.get(item.get('priority', 'medium'), '#000000')
                
                action_items_html += f"""
                <tr>
                    <td style="padding: 10px; border: 1px solid #ddd;">
                        <strong style="color: {priority_color};">[{item.get('priority', 'medium').upper()}]</strong>
                        {item.get('description', '')}
                    </td>
                    <td style="padding: 10px; border: 1px solid #ddd;">{item.get('due_date', 'TBD')}</td>
                </tr>
                """
        
        if not action_items_html:
            action_items_html = "<tr><td colspan='2' style='padding: 10px;'>No action items assigned to you.</td></tr>"
        
        email_html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
                h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
                h2 {{ color: #34495e; margin-top: 30px; }}
                .summary {{ background-color: #ecf0f1; padding: 15px; border-radius: 5px; margin: 20px 0; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                th {{ background-color: #3498db; color: white; padding: 12px; text-align: left; }}
                .key-points {{ list-style-type: none; padding-left: 0; }}
                .key-points li {{ padding: 8px; margin: 5px 0; background-color: #f8f9fa; border-left: 4px solid #3498db; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Meeting Minutes</h1>
                
                <div class="summary">
                    <h2>Summary</h2>
                    <p>{meeting_minutes.get('summary', '')}</p>
                </div>
                
                <h2>Key Points</h2>
                <ul class="key-points">
                    {''.join([f'<li>{point}</li>' for point in meeting_minutes.get('key_points', [])])}
                </ul>
                
                <h2>Your Action Items</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Action Item</th>
                            <th>Due Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        {action_items_html}
                    </tbody>
                </table>
                
                <h2>Next Steps</h2>
                <ul>
                    {''.join([f'<li>{step}</li>' for step in meeting_minutes.get('next_steps', [])])}
                </ul>
                
                <p style="margin-top: 40px; color: #7f8c8d; font-size: 12px;">
                    This email was automatically generated by the Meeting Assistant AI Agent.
                </p>
            </div>
        </body>
        </html>
        """
        
        return email_html
    
    def export_to_jira_format(self, meeting_minutes: Dict) -> List[Dict]:
        """
        Convert action items to Jira ticket format.
        
        Args:
            meeting_minutes: The structured meeting minutes
            
        Returns:
            List of Jira ticket dictionaries
        """
        jira_tickets = []
        
        for item in meeting_minutes.get('action_items', []):
            priority_map = {
                'high': 'Highest',
                'medium': 'Medium',
                'low': 'Low'
            }
            
            ticket = {
                'summary': item.get('description', ''),
                'description': f"Action item from meeting\n\nAssignee: {item.get('assignee', 'Unassigned')}",
                'issuetype': {'name': 'Task'},
                'priority': {'name': priority_map.get(item.get('priority', 'medium'), 'Medium')},
                'duedate': item.get('due_date', ''),
                'labels': ['meeting-action-item', item.get('id', '')]
            }
            
            jira_tickets.append(ticket)
        
        return jira_tickets


def main():
    """Example usage of the Meeting Assistant."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python meeting_assistant.py <meeting_request.json>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        meeting_data = json.load(f)
    
    assistant = MeetingAssistant()
    
    print("Processing meeting transcript...")
    meeting_minutes = assistant.process_meeting(meeting_data)
    
    print("\n" + "="*80)
    print("MEETING MINUTES")
    print("="*80)
    print(json.dumps(meeting_minutes, indent=2, ensure_ascii=False))
    
    output_file = 'meeting_minutes_output.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(meeting_minutes, f, indent=2, ensure_ascii=False)
    
    print(f"\nMeeting minutes saved to: {output_file}")
    
    if meeting_data.get('create_jira_tickets'):
        jira_tickets = assistant.export_to_jira_format(meeting_minutes)
        jira_file = 'jira_tickets_output.json'
        with open(jira_file, 'w', encoding='utf-8') as f:
            json.dump(jira_tickets, f, indent=2, ensure_ascii=False)
        print(f"Jira tickets saved to: {jira_file}")


if __name__ == '__main__':
    main()
