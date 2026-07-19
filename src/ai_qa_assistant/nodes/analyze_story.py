"""
analyze_story node - Analyzes the user story using LLM.

This node interprets the user story and extracts key information
such as:
- Main functionality
- Actor (who uses it)
- Benefit (why it's important)
- Preconditions
- Postconditions
- Business rules
- Related data

The extracted information is used by subsequent nodes to generate
test cases and acceptance criteria.
"""

from ai_qa_assistant.state import QAState
from ai_qa_assistant.prompts import ANALYZE_STORY_PROMPT, SYSTEM_PROMPT
from ai_qa_assistant.llm import call_llm_with_template


def analyze_story(state: QAState) -> QAState:
    """
    Analyze the user story using LLM.
    
    Calls the LLM with the user story and checklist to extract
    analysis information that will be used by subsequent nodes.
    
    Args:
        state: Current state with user_story and checklist
        
    Returns:
        Updated state with analysis result in the analysis field
        
    Notes:
        - This node uses the LLM to interpret the user story
        - Extracts key information for downstream processing
    """
    # Format prompt with state data
    prompt_data = {
        "user_story": state["user_story"],
        "checklist": state.get("checklist", ""),
    }
    
    # Call LLM
    response = call_llm_with_template(
        ANALYZE_STORY_PROMPT,
        **prompt_data,
        system_prompt=SYSTEM_PROMPT,
    )
    
    # Update state with analysis result
    state["analysis"] = response
    
    return state