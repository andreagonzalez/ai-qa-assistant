"""
Tools available to the AI QA Assistant agent.
"""

import os
from typing import Optional


def load_checklist(checklist_path: str = "src/docs/checklist_qa.md") -> str:
    """
    Load QA checklist from file.
    
    Args:
        checklist_path: Path to the checklist file
        
    Returns:
        Checklist content as string
        
    Raises:
        FileNotFoundError: If checklist file doesn't exist
    """
    # TODO: Implement file reading logic
    pass


def save_report(report: str, output_path: str = "src/reports/report.md") -> bool:
    """
    Save the final report to a Markdown file.
    
    Args:
        report: Report content to save
        output_path: Output file path
        
    Returns:
        True if saved successfully, False otherwise
    """
    # TODO: Implement file writing logic
    pass


def validate_input(user_story: str) -> bool:
    """
    Validate user story input.
    
    Args:
        user_story: User story text to validate
        
    Returns:
        True if valid, False otherwise
    """
    # TODO: Implement validation logic
    pass