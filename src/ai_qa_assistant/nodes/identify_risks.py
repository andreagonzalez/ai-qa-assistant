"""
identify_risks node - Identifies risks in the user story.

This node identifies both technical and business risks associated
with the user story. For each risk, it assesses:
- Probability of occurrence
- Impact on the system/business
- Mitigation strategies
"""

from ai_qa_assistant.state import QAState
from ai_qa_assistant.prompts import IDENTIFY_RISKS_PROMPT, SYSTEM_PROMPT
from ai_qa_assistant.llm import call_llm_with_template


def identify_risks(state: QAState) -> QAState:
    """
    Identify technical and business risks.
    
    Calls the LLM with the user story, analysis, and acceptance criteria
    to identify potential risks that could affect the quality or delivery
    of the feature.
    
    Args:
        state: Current state with analysis and acceptance_criteria
        
    Returns:
        Updated state with risks in the following format:
        
        ## Riscos Identificados
        
        ### Risco Técnico
        **ID**: RSK-TEC-001
        **Descrição**: ...
        **Probabilidade**: [Alta/Média/Baixa]
        **Impacto**: [Alto/Médio/Baixo]
        **Prioridade**: [Alta/Média/Baixa]
        **Mitigação**: ...
        
        ### Risco de Negócio
        **ID**: RSK-NEG-001
        **Descrição**: ...
        ...
    """
    # Format prompt with state data
    prompt_data = {
        "user_story": state["user_story"],
        "analysis": state.get("analysis", ""),
        "acceptance_criteria": state.get("acceptance_criteria", ""),
    }
    
    # Call LLM
    response = call_llm_with_template(
        IDENTIFY_RISKS_PROMPT,
        **prompt_data,
        system_prompt=SYSTEM_PROMPT,
    )
    
    # Update state with risks
    state["risks"] = response
    
    return state