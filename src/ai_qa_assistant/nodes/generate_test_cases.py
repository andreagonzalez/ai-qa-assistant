"""
generate_test_cases node - Generates test cases.

This node produces comprehensive test cases based on the acceptance
criteria. It generates three types of test scenarios:
- Positive scenarios (happy path)
- Negative scenarios (error path)
- Exception scenarios (edge cases)

The test cases should be detailed enough to be directly implemented.
"""

from ai_qa_assistant.state import QAState
from ai_qa_assistant.prompts import GENERATE_TEST_CASES_PROMPT, SYSTEM_PROMPT
from ai_qa_assistant.llm import call_llm_with_template


def generate_test_cases(state: QAState) -> QAState:
    """
    Generate test cases based on acceptance criteria.
    
    Calls the LLM with the acceptance criteria to generate
    comprehensive test cases covering all scenarios.
    
    Args:
        state: Current state with acceptance_criteria
        
    Returns:
        Updated state with test_cases in the following format:
        
        ## Casos de Teste
        
        ### Cenários Positivos
        #### CT001 - [Description]
        **Precondição**: ...
        **Passos**: ...
        **Resultado Esperado**: ...
        
        ### Cenários Negativos
        #### CT002 - [Description]
        ...
        
        ### Exceções
        #### CT003 - [Description]
        ...
    """
    # Format prompt with state data
    prompt_data = {
        "user_story": state["user_story"],
        "acceptance_criteria": state.get("acceptance_criteria", ""),
    }
    
    # Call LLM
    response = call_llm_with_template(
        GENERATE_TEST_CASES_PROMPT,
        **prompt_data,
        system_prompt=SYSTEM_PROMPT,
    )
    
    # Update state with test cases
    state["test_cases"] = response
    
    return state