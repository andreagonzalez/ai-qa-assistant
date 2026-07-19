"""
Main entry point for the AI QA Assistant application.

This module provides the core functionality to run the QA analysis
pipeline on User Stories. It includes:
- run_analysis(): Main function to execute the full analysis
- main(): CLI entry point for running the tool

Usage:
    # Via CLI with direct input
    python -m ai_qa_assistant.app "Como cliente, quero recuperar minha senha para conseguir acessar novamente minha conta."

    # Via CLI with file input
    python -m ai_qa_assistant.app --file user-story.txt

    # As a module
    from ai_qa_assistant.app import run_analysis
    result = run_analysis("Como ...")
    print(result.report)
"""

import os
import sys
from pathlib import Path

from ai_qa_assistant.config import load_config
from ai_qa_assistant.graph import create_graph
from ai_qa_assistant.state import QAState


# Example User Story for testing
EXAMPLE_USER_STORY = """
Como cliente
quero recuperar minha senha
para conseguir acessar novamente minha conta.
"""


def run_analysis(user_story: str) -> QAState:
    """
    Run the QA analysis pipeline on a user story.
    
    Executes all nodes in the LangGraph in sequence:
    validate_input → load_checklist → analyze_story →
    generate_acceptance → generate_test_cases → identify_risks → build_report
    
    Args:
        user_story: User story text to analyze
        
    Returns:
        Final state with complete analysis and report populated
        
    Raises:
        ValueError: If OPENAI_API_KEY is not set in environment
    """
    # Load configuration
    config = load_config()
    
    # Validate API key
    if not config.get("openai_api_key"):
        raise ValueError("OPENAI_API_KEY not set in environment variables")
    
    # Initialize graph
    graph = create_graph()
    
    # Initialize state
    state = QAState(user_story=user_story)
    
    # Run analysis
    result = graph.invoke(state)
    
    return result


def main():
    """
    Main entry point for CLI usage.
    
    Usage:
        python -m ai_qa_assistant.app <user_story>
        python -m ai_qa_assistant.app --file <path_to_file>
    """
    if len(sys.argv) < 2:
        print("Usage: ai-qa-assistant <user_story>")
        print("       ai-qa-assistant --file <path_to_file>")
        print("       ai-qa-assistant --example  # Run with example user story")
        sys.exit(1)
    
    # Get user story
    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Error: --file requires a path argument")
            sys.exit(1)
        
        file_path = sys.argv[2]
        if not os.path.exists(file_path):
            print(f"Error: File not found: {file_path}")
            sys.exit(1)
        
        with open(file_path, "r", encoding="utf-8") as f:
            user_story = f.read()
    elif sys.argv[1] == "--example":
        user_story = EXAMPLE_USER_STORY
    else:
        user_story = " ".join(sys.argv[1:])
    
    # Run analysis
    try:
        result = run_analysis(user_story)
        print("\n" + "=" * 60)
        print("ANÁLISE CONCLUÍDA")
        print("=" * 60)
        print("\n" + result.report)
    except Exception as e:
        print(f"Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()