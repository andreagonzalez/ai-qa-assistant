"""
Tools available to the AI QA Assistant agent.
"""

import os
from pathlib import Path


def load_checklist(checklist_path: str = "src/docs/checklist_qa.md") -> str:
    """
    Load QA checklist from a Markdown file.
    
    Args:
        checklist_path: Path to the checklist file (default: src/docs/checklist_qa.md)
        
    Returns:
        Checklist content as string
        
    Raises:
        FileNotFoundError: If checklist file doesn't exist
        IOError: If file cannot be read
    """
    # Resolve relative paths from the project root
    project_root = Path(__file__).parent.parent
    full_path = project_root / checklist_path
    
    if not full_path.exists():
        raise FileNotFoundError(f"Checklist file not found: {full_path}")
    
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    except IOError as e:
        raise IOError(f"Failed to read checklist file: {e}")