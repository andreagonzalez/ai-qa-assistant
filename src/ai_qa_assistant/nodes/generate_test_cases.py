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
        
    Notes:
        - This is a placeholder implementation
        - LLM call should be implemented using prompts.GENERATE_TEST_CASES_PROMPT
        - Should update state.test_cases field with structured test cases
    """
    # TODO: Call LLM with GENERATE_TEST_CASES_PROMPT and SYSTEM_PROMPT
    # TODO: Parse LLM response to extract test cases
    # TODO: Update state.test_cases with the generated test cases
    # TODO: Return updated state
    
    # Placeholder: return state as-is
    pass