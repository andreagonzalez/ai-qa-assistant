"""
load_checklist node - Loads the QA checklist from file.

This node reads the QA checklist from the docs/checklist_qa.md file
and stores it in the state. The checklist is used as a reference
during the analysis of the user story.
"""

from pathlib import Path

from ai_qa_assistant.state import QAState
from ai_qa_assistant.tools import load_checklist as load_checklist_tool


def load_checklist(state: QAState) -> QAState:
    """
    Load QA checklist from file.
    
    Reads the checklist from the predefined path and stores it in the
    state for use by subsequent nodes.
    
    Args:
        state: Current state
        
    Returns:
        Updated state with checklist loaded in state.checklist
        
    Notes:
        - Loads checklist from src/docs/checklist_qa.md
        - Updates state.checklist with the file content
    """
    # Load checklist from tools
    checklist_content = load_checklist_tool()
    
    # Update state with checklist
    state["checklist"] = checklist_content
    
    return state