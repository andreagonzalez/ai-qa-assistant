"""
LangGraph construction for the AI QA Assistant.
"""

from langgraph.graph import StateGraph
from ai_qa_assistant.state import QAState
from ai_qa_assistant.nodes.validate_input import validate_input
from ai_qa_assistant.nodes.load_checklist import load_checklist
from ai_qa_assistant.nodes.analyze_story import analyze_story
from ai_qa_assistant.nodes.generate_acceptance import generate_acceptance
from ai_qa_assistant.nodes.generate_test_cases import generate_test_cases
from ai_qa_assistant.nodes.identify_risks import identify_risks
from ai_qa_assistant.nodes.build_report import build_report


def create_graph() -> StateGraph:
    """
    Create and compile the LangGraph.
    
    Returns:
        Compiled StateGraph ready for execution
    """
    # Create the graph
    workflow = StateGraph(QAState)
    
    # Add nodes
    workflow.add_node("validate_input", validate_input)
    workflow.add_node("load_checklist", load_checklist)
    workflow.add_node("analyze_story", analyze_story)
    workflow.add_node("generate_acceptance", generate_acceptance)
    workflow.add_node("generate_test_cases", generate_test_cases)
    workflow.add_node("identify_risks", identify_risks)
    workflow.add_node("build_report", build_report)
    
    # Define edges (flow)
    workflow.add_edge("validate_input", "load_checklist")
    workflow.add_edge("load_checklist", "analyze_story")
    workflow.add_edge("analyze_story", "generate_acceptance")
    workflow.add_edge("generate_acceptance", "generate_test_cases")
    workflow.add_edge("generate_test_cases", "identify_risks")
    workflow.add_edge("identify_risks", "build_report")
    
    # Set entry point
    workflow.set_entry_point("validate_input")
    
    # Compile the graph
    return workflow.compile()