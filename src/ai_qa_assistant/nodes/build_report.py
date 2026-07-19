"""
build_report node - Builds the final report.

This node consolidates all the information collected by the previous
nodes into a single, well-structured Markdown report. The report
includes all sections: summary, features, acceptance criteria,
test cases, risks, and recommendations.
"""

from ai_qa_assistant.state import QAState
from ai_qa_assistant.prompts import BUILD_REPORT_PROMPT, SYSTEM_PROMPT
from ai_qa_assistant.llm import call_llm_with_template


def build_report(state: QAState) -> QAState:
    """
    Build the final Markdown report from all collected information.
    
    Calls the LLM with all the analysis results to generate a
    comprehensive report that can be delivered to stakeholders.
    
    Args:
        state: Current state with all analysis results:
            - user_story
            - analysis
            - acceptance_criteria
            - test_cases
            - risks
            - recommendations
            
    Returns:
        Updated state with final report in the report field.
        The report includes all sections in Markdown format.
    """
    # Format prompt with state data
    prompt_data = {
        "user_story": state["user_story"],
        "analysis": state.get("analysis", ""),
        "acceptance_criteria": state.get("acceptance_criteria", ""),
        "test_cases": state.get("test_cases", ""),
        "risks": state.get("risks", ""),
        "recommendations": state.get("recommendations", ""),
    }
    
    # Call LLM
    response = call_llm_with_template(
        BUILD_REPORT_PROMPT,
        **prompt_data,
        system_prompt=SYSTEM_PROMPT,
    )
    
    # Update state with final report
    state["report"] = response
    
    return state