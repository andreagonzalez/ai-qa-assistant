"""
build_report node - Builds the final report.

This node consolidates all the information collected by the previous
nodes into a single, well-structured Markdown report. The report
includes all sections: summary, features, acceptance criteria,
test cases, risks, and recommendations.
"""

from ai_qa_assistant.state import QAState
from ai_qa_assistant.prompts import BUILD_REPORT_PROMPT, SYSTEM_PROMPT


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
        
    Notes:
        - This is a placeholder implementation
        - LLM call should be implemented using prompts.BUILD_REPORT_PROMPT
        - Should update state.report field with the final Markdown report
    """
    # TODO: Call LLM with BUILD_REPORT_PROMPT and SYSTEM_PROMPT
    # TODO: Parse LLM response to extract the full report
    # TODO: Update state.report with the generated Markdown report
    # TODO: Return updated state
    
    # Placeholder: return state as-is
    pass