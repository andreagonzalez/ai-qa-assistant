"""
validate_input node - Validates the user story input.

This node is responsible for validating the user story input before
processing it. It checks if the input contains the required components
of a valid User Story (Como, Quero, Para).

The node updates the state with the validation result and any error
messages if validation fails.
"""

from ai_qa_assistant.state import QAState
from ai_qa_assistant.prompts import VALIDATE_INPUT_PROMPT, VALIDATE_INPUT_SYSTEM_PROMPT
from ai_qa_assistant.llm import call_llm_with_template


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
    """
    prompt_data = {
        "user_story": state["user_story"],
    }

    response = call_llm_with_template(
        VALIDATE_INPUT_PROMPT,
        **prompt_data,
        system_prompt=VALIDATE_INPUT_SYSTEM_PROMPT,
    ).strip()

    normalized = response.strip()
    if normalized.upper().startswith("VALID"):
        return state

    if normalized.upper().startswith("INVALID"):
        reason = normalized[7:].strip()
        if reason.startswith(":"):
            reason = reason[1:].strip()
        invalid_message = reason or "User Story inválida"
        state["user_story"] = f"INVALID: {invalid_message}"
        raise ValueError(f"Invalid user story: {invalid_message}")

    raise ValueError(
        f"Unexpected validation response from LLM: '{response}'. Expected 'VALID' or 'INVALID: <motivo>'."
    )
