"""
validate_input node - Validates the user story input.

This node is responsible for validating the user story input before
processing it. It checks if the input contains the required components
of a valid User Story (Como, Quero, Para).

The node updates the state with the validation result and any error
messages if validation fails.
"""

from typing import Tuple

from ai_qa_assistant.state import QAState
from ai_qa_assistant.prompts import VALIDATE_INPUT_PROMPT, VALIDATE_INPUT_SYSTEM_PROMPT


def validate_input(state: QAState) -> QAState:
    """
    Validate the user story input.
    
    This node checks if the user story contains the required components:
    - "Como" (actor/role)
    - "Quero" (feature/functionality)
    - "Para" (benefit/goal)
    
    It also validates the size and format of the input.
    
    Args:
        state: Current state containing user_story
        
    Returns:
        Updated state with validation result in user_story field.
        If invalid, the user_story field will be prefixed with "INVALID: "
        
    Notes:
        - This is a placeholder implementation
        - LLM call should be implemented using prompts.VALIDATE_INPUT_PROMPT
        - Should return state with valid/invalid status
    """
    # TODO: Call LLM with VALIDATE_INPUT_PROMPT and VALIDATE_INPUT_SYSTEM_PROMPT
    # TODO: Parse LLM response to determine validation result
    # TODO: Update state based on validation result
    # TODO: Return updated state
    
    # Placeholder: return state as-is
    # In production, this would call the LLM and validate the response
    pass