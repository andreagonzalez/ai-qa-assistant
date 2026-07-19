"""
State definition for the AI QA Assistant agent.

This module defines the shared state structure used by the LangGraph nodes.
TypedDict is used for better type hints and runtime validation.
"""

from typing import TypedDict


class QAState(TypedDict):
    """
    State shared across all nodes in the LangGraph.
    
    This TypedDict defines the contract for data passed between nodes
    in the graph. Each node reads and updates specific fields of the state.
    
    Attributes:
        user_story: Raw user story input text
        checklist: QA checklist content loaded from file
        analysis: Analysis of the user story
        acceptance_criteria: Generated acceptance criteria
        test_cases: Generated test cases (positive, negative, exceptions)
        risks: Identified technical and business risks
        recommendations: QA recommendations based on analysis
        report: Final consolidated Markdown report
    """
    
    user_story: str
    checklist: str
    analysis: str
    acceptance_criteria: str
    test_cases: str
    risks: str
    recommendations: str
    report: str