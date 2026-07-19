"""
State definition for the AI QA Assistant agent.
"""

from pydantic import BaseModel, Field


class QAState(BaseModel):
    """
    State shared across all nodes in the LangGraph.
    
    Fields:
        user_story: Raw user story input
        checklist: QA checklist loaded from file
        analysis: Analysis of the user story
        acceptance_criteria: Generated acceptance criteria
        test_cases: Generated test cases (positive, negative, exceptions)
        risks: Identified risks
        recommendations: QA recommendations
        report: Final Markdown report
    """
    
    user_story: str = Field(default="", description="Raw user story input")
    checklist: str = Field(default="", description="QA checklist loaded from file")
    analysis: str = Field(default="", description="Analysis of the user story")
    acceptance_criteria: str = Field(default="", description="Generated acceptance criteria")
    test_cases: str = Field(default="", description="Generated test cases")
    risks: str = Field(default="", description="Identified risks")
    recommendations: str = Field(default="", description="QA recommendations")
    report: str = Field(default="", description="Final Markdown report")