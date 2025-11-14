"""
PMO Report Generator AI Agent
Automatically generates executive PMO reports from Jira data and other sources.
"""

import os
import json
import re
from datetime import datetime
from typing import Dict, List, Optional
import requests


class PMOReportGenerator:
    """
    AI-powered PMO report generator that analyzes project data and generates
    executive summaries with insights and recommendations.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the PMO Report Generator.
        
        Args:
            api_key: OpenRouter API key. If not provided, reads from OPENROUTER_API_KEY env var.
        """
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            raise ValueError("OpenRouter API key is required. Set OPENROUTER_API_KEY environment variable.")
        
        self.api_endpoint = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "anthropic/claude-3.5-haiku"
        self.max_retries = 3
    
    def generate_report(self, project_data: Dict) -> Dict:
        """
        Generate a PMO report from project data.
        
        Args:
            project_data: Dictionary containing:
                - projects: List of project dictionaries with status, issues, budget
                - period: Reporting period (start and end dates)
                - additional_context: Optional additional information
        
        Returns:
            Dictionary containing:
                - executive_summary: High-level overview with key metrics
                - detailed_analysis: In-depth analysis with trends
                - recommendations: Actionable recommendations
        """
        projects = project_data.get('projects', [])
        period = project_data.get('period', {})
        
        if not projects:
            raise ValueError("Project data is required")
        
        prompt = self._build_report_analysis_prompt(projects, period)
        response = self._call_openrouter_api(prompt)
        report = self._parse_report_response(response)
        
        return report
    
    def _build_report_analysis_prompt(self, projects: List[Dict], period: Dict) -> str:
        """Build the prompt for PMO report analysis."""
        projects_json = json.dumps(projects, indent=2, ensure_ascii=False)
        period_str = f"{period.get('start', 'N/A')} to {period.get('end', 'N/A')}"
        
        return f"""You are an expert PMO analyst. Analyze the following project data and generate a comprehensive PMO report.

Reporting Period: {period_str}

Project Data:
{projects_json}

Please provide a comprehensive PMO report in the following JSON format:

{{
  "executive_summary": {{
    "overview": "High-level summary of all projects (2-3 sentences)",
    "key_metrics": {{
      "total_projects": <number>,
      "on_track": <number>,
      "at_risk": <number>,
      "delayed": <number>,
      "budget_variance": "<percentage with + or - sign>"
    }},
    "critical_risks": [
      {{
        "project": "Project name",
        "risk": "Description of the risk",
        "impact": "high|medium|low",
        "mitigation": "Recommended mitigation strategy"
      }}
    ],
    "recommendations": [
      "Actionable recommendation 1",
      "Actionable recommendation 2"
    ]
  }},
  "detailed_analysis": {{
    "trends": [
      "Trend observation 1",
      "Trend observation 2"
    ],
    "resource_allocation": {{
      "PROJECT-KEY": {{
        "team_size": <number>,
        "utilization": <percentage>
      }}
    }},
    "budget_analysis": {{
      "total_planned": <number>,
      "total_actual": <number>,
      "variance_percentage": <number>,
      "projects_over_budget": <number>
    }}
  }}
}}

Analysis Guidelines:
1. Calculate accurate metrics from the provided data
2. Identify projects at risk based on:
   - Progress vs. timeline
   - Open issues count
   - Budget variance
3. Provide specific, actionable recommendations
4. Highlight trends and patterns across projects
5. Assess resource utilization and allocation
6. Calculate budget variance: ((actual - planned) / planned) * 100
7. Classify project status:
   - On Track: Progress >= 70% of expected, budget within 10%
   - At Risk: Progress < 70% or budget variance > 10%
   - Delayed: Significant progress issues or major budget overruns
8. Prioritize critical risks by impact

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
            "X-Title": "ProjMAN PMO Report Generator"
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
    
    def _parse_report_response(self, response: str) -> Dict:
        """
        Parse the JSON response from the API.
        
        Args:
            response: Raw response text from API
            
        Returns:
            Parsed report dictionary
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
    
    def generate_html_report(self, report: Dict, period: Dict) -> str:
        """
        Generate an HTML version of the PMO report.
        
        Args:
            report: The structured report data
            period: Reporting period information
            
        Returns:
            HTML report content
        """
        exec_summary = report.get('executive_summary', {})
        detailed = report.get('detailed_analysis', {})
        key_metrics = exec_summary.get('key_metrics', {})
        
        risks_html = ""
        for risk in exec_summary.get('critical_risks', []):
            impact_color = {
                'high': '#ff0000',
                'medium': '#ff9900',
                'low': '#00cc00'
            }.get(risk.get('impact', 'medium'), '#000000')
            
            risks_html += f"""
            <div style="margin: 15px 0; padding: 15px; border-left: 5px solid {impact_color}; background-color: #f8f9fa;">
                <h4 style="margin-top: 0; color: {impact_color};">
                    {risk.get('project', 'Unknown Project')} - {risk.get('impact', 'medium').upper()} IMPACT
                </h4>
                <p><strong>Risk:</strong> {risk.get('risk', '')}</p>
                <p><strong>Mitigation:</strong> {risk.get('mitigation', '')}</p>
            </div>
            """
        
        if not risks_html:
            risks_html = "<p>No critical risks identified.</p>"
        
        budget_variance_color = '#00cc00' if detailed.get('budget_analysis', {}).get('variance_percentage', 0) <= 0 else '#ff0000'
        
        html_report = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 20px; }}
                .container {{ max-width: 1200px; margin: 0 auto; }}
                .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; }}
                .header h1 {{ margin: 0; font-size: 32px; }}
                .header .period {{ font-size: 16px; opacity: 0.9; margin-top: 10px; }}
                .metrics-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0; }}
                .metric-card {{ background-color: #f8f9fa; padding: 20px; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                .metric-card .value {{ font-size: 36px; font-weight: bold; color: #667eea; margin: 10px 0; }}
                .metric-card .label {{ font-size: 14px; color: #666; text-transform: uppercase; }}
                .section {{ margin: 40px 0; }}
                .section h2 {{ color: #2c3e50; border-bottom: 3px solid #667eea; padding-bottom: 10px; }}
                .overview {{ background-color: #ecf0f1; padding: 20px; border-radius: 8px; margin: 20px 0; font-size: 16px; }}
                .recommendations {{ list-style-type: none; padding-left: 0; }}
                .recommendations li {{ padding: 12px; margin: 10px 0; background-color: #e8f5e9; border-left: 4px solid #4caf50; }}
                .trends {{ list-style-type: none; padding-left: 0; }}
                .trends li {{ padding: 10px; margin: 8px 0; background-color: #fff3e0; border-left: 4px solid #ff9800; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                th {{ background-color: #667eea; color: white; padding: 12px; text-align: left; }}
                td {{ padding: 12px; border-bottom: 1px solid #ddd; }}
                tr:hover {{ background-color: #f5f5f5; }}
                .footer {{ margin-top: 60px; padding-top: 20px; border-top: 2px solid #ddd; color: #7f8c8d; font-size: 12px; text-align: center; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>PMO Executive Report</h1>
                    <div class="period">Reporting Period: {period.get('start', 'N/A')} to {period.get('end', 'N/A')}</div>
                    <div class="period">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
                </div>
                
                <div class="section">
                    <h2>Key Metrics</h2>
                    <div class="metrics-grid">
                        <div class="metric-card">
                            <div class="label">Total Projects</div>
                            <div class="value">{key_metrics.get('total_projects', 0)}</div>
                        </div>
                        <div class="metric-card">
                            <div class="label">On Track</div>
                            <div class="value" style="color: #4caf50;">{key_metrics.get('on_track', 0)}</div>
                        </div>
                        <div class="metric-card">
                            <div class="label">At Risk</div>
                            <div class="value" style="color: #ff9800;">{key_metrics.get('at_risk', 0)}</div>
                        </div>
                        <div class="metric-card">
                            <div class="label">Delayed</div>
                            <div class="value" style="color: #f44336;">{key_metrics.get('delayed', 0)}</div>
                        </div>
                        <div class="metric-card">
                            <div class="label">Budget Variance</div>
                            <div class="value" style="color: {budget_variance_color};">{key_metrics.get('budget_variance', '0%')}</div>
                        </div>
                    </div>
                </div>
                
                <div class="section">
                    <h2>Executive Overview</h2>
                    <div class="overview">
                        {exec_summary.get('overview', 'No overview available.')}
                    </div>
                </div>
                
                <div class="section">
                    <h2>Critical Risks</h2>
                    {risks_html}
                </div>
                
                <div class="section">
                    <h2>Recommendations</h2>
                    <ul class="recommendations">
                        {''.join([f'<li>{rec}</li>' for rec in exec_summary.get('recommendations', [])])}
                    </ul>
                </div>
                
                <div class="section">
                    <h2>Detailed Analysis</h2>
                    
                    <h3>Trends</h3>
                    <ul class="trends">
                        {''.join([f'<li>{trend}</li>' for trend in detailed.get('trends', [])])}
                    </ul>
                    
                    <h3>Budget Analysis</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Metric</th>
                                <th>Value</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Total Planned Budget</td>
                                <td>€{detailed.get('budget_analysis', {}).get('total_planned', 0):,}</td>
                            </tr>
                            <tr>
                                <td>Total Actual Spend</td>
                                <td>€{detailed.get('budget_analysis', {}).get('total_actual', 0):,}</td>
                            </tr>
                            <tr>
                                <td>Variance</td>
                                <td style="color: {budget_variance_color};">
                                    {detailed.get('budget_analysis', {}).get('variance_percentage', 0):.1f}%
                                </td>
                            </tr>
                            <tr>
                                <td>Projects Over Budget</td>
                                <td>{detailed.get('budget_analysis', {}).get('projects_over_budget', 0)}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
                <div class="footer">
                    <p>This report was automatically generated by the PMO Report Generator AI Agent.</p>
                    <p>ProjMAN - AI-Powered Project Management</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html_report
    
    def export_to_excel_format(self, report: Dict) -> Dict:
        """
        Convert report to Excel-friendly format.
        
        Args:
            report: The structured report data
            
        Returns:
            Dictionary with sheets data for Excel export
        """
        exec_summary = report.get('executive_summary', {})
        detailed = report.get('detailed_analysis', {})
        
        excel_data = {
            'Summary': {
                'headers': ['Metric', 'Value'],
                'rows': [
                    ['Total Projects', exec_summary.get('key_metrics', {}).get('total_projects', 0)],
                    ['On Track', exec_summary.get('key_metrics', {}).get('on_track', 0)],
                    ['At Risk', exec_summary.get('key_metrics', {}).get('at_risk', 0)],
                    ['Delayed', exec_summary.get('key_metrics', {}).get('delayed', 0)],
                    ['Budget Variance', exec_summary.get('key_metrics', {}).get('budget_variance', '0%')]
                ]
            },
            'Risks': {
                'headers': ['Project', 'Risk', 'Impact', 'Mitigation'],
                'rows': [
                    [
                        risk.get('project', ''),
                        risk.get('risk', ''),
                        risk.get('impact', ''),
                        risk.get('mitigation', '')
                    ]
                    for risk in exec_summary.get('critical_risks', [])
                ]
            },
            'Budget': {
                'headers': ['Metric', 'Value'],
                'rows': [
                    ['Total Planned', detailed.get('budget_analysis', {}).get('total_planned', 0)],
                    ['Total Actual', detailed.get('budget_analysis', {}).get('total_actual', 0)],
                    ['Variance %', detailed.get('budget_analysis', {}).get('variance_percentage', 0)],
                    ['Projects Over Budget', detailed.get('budget_analysis', {}).get('projects_over_budget', 0)]
                ]
            }
        }
        
        return excel_data


def main():
    """Example usage of the PMO Report Generator."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python pmo_report_generator.py <jira_data.json>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        project_data = json.load(f)
    
    generator = PMOReportGenerator()
    
    print("Generating PMO report...")
    report = generator.generate_report(project_data)
    
    print("\n" + "="*80)
    print("PMO REPORT")
    print("="*80)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    
    output_file = 'pmo_report_output.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\nPMO report saved to: {output_file}")
    
    html_report = generator.generate_html_report(report, project_data.get('period', {}))
    html_file = 'pmo_report_output.html'
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_report)
    
    print(f"HTML report saved to: {html_file}")


if __name__ == '__main__':
    main()
