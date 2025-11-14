#!/usr/bin/env python3
"""
Demo adatok betöltő script
Használat: python scripts/load_demo_data.py --meeting-transcript demo_data/meeting_demo_transcript.txt
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Projekt root hozzáadása a path-hoz
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def load_meeting_transcript(file_path: str):
    """Meeting átirat betöltése"""
    print(f"📝 Meeting átirat betöltése: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"✅ Betöltve: {len(content)} karakter")
    return content


def load_jira_data(file_path: str):
    """Jira adatok betöltése"""
    print(f"📊 Jira adatok betöltése: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"✅ Betöltve: {len(data.get('projects', []))} projekt")
    return data


def load_excel_file(file_path: str):
    """Excel fájl betöltése (struktúra ellenőrzés)"""
    print(f"📈 Excel fájl ellenőrzése: {file_path}")
    if not os.path.exists(file_path):
        print(f"⚠️  Figyelem: A fájl nem létezik: {file_path}")
        print("   Ez normális, ha még nincs Excel fájl. A struktúra:")
        print("   - Projekt | Tervezett költség | Tényleges költség | Különbség | Státusz")
        return None
    print(f"✅ Fájl megtalálva")
    return file_path


def main():
    parser = argparse.ArgumentParser(description='Demo adatok betöltése')
    parser.add_argument('--meeting-transcript', type=str, help='Meeting átirat fájl')
    parser.add_argument('--jira-data', type=str, help='Jira adatok JSON fájl')
    parser.add_argument('--excel-file', type=str, help='Excel fájl')
    parser.add_argument('--all', action='store_true', help='Összes demo adat betöltése')
    
    args = parser.parse_args()
    
    demo_data_dir = project_root / 'demo_data'
    
    if args.all or not any([args.meeting_transcript, args.jira_data, args.excel_file]):
        print("🔄 Összes demo adat betöltése...\n")
        
        # Meeting transcript
        transcript_file = demo_data_dir / 'meeting_demo_transcript.txt'
        if transcript_file.exists():
            load_meeting_transcript(str(transcript_file))
            print()
        
        # Jira data
        jira_file = demo_data_dir / 'jira_demo_data.json'
        if jira_file.exists():
            load_jira_data(str(jira_file))
            print()
        
        # Excel file
        excel_file = demo_data_dir / 'budget_demo.xlsx'
        load_excel_file(str(excel_file))
        print()
        
        print("✅ Demo adatok betöltése befejezve!")
        return
    
    if args.meeting_transcript:
        load_meeting_transcript(args.meeting_transcript)
    
    if args.jira_data:
        load_jira_data(args.jira_data)
    
    if args.excel_file:
        load_excel_file(args.excel_file)


if __name__ == '__main__':
    main()

