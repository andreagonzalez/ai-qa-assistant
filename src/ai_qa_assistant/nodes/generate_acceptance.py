"""
generate_acceptance node - Generates acceptance criteria.

This node produces acceptance criteria based on the user story
analysis and the QA checklist. The criteria should be specific,
testable, and cover success and failure scenarios.
"""

from ai_qa_assistant.state import QAState
from ai_qa_assistant.prompts import GENERATE_ACCEPTANCE_PROMPT, SYSTEM_PROMPT
from ai_qa_assistant.llm import call_llm_with_template


def generate_acceptance(state: QAState) -> QAState:
    """
    Generate acceptance criteria based on user story analysis.
    
    Calls the LLM with the analysis and checklist to generate
    acceptance criteria that define when the feature is considered
    complete and ready for testing.
    
    Args:
        state: Current state with analysis and checklist
        
    Returns:
        Updated state with acceptance criteria in the acceptance_criteria field.
        Format: Markdown with numbered criteria (AC01, AC02, etc.)
    """
    # Format prompt with state data
    prompt_data = {
        "user_story": state["user_story"],
        "analysis": state.get("analysis", ""),
        "checklist": state.get("checklist", ""),
    }
    
    # Call LLM
    response = call_llm_with_template(
        GENERATE_ACCEPTANCE_PROMPT,
        **prompt_data,
        system_prompt=SYSTEM_PROMPT,
    )
    
    # Update state with acceptance criteria
    state["acceptance_criteria"] = response
    
    return state