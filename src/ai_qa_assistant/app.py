"""
Main entry point for the AI QA Assistant application.
"""

import os
import sys
from pathlib import Path

from ai_qa_assistant.config import load_config
from ai_qa_assistant.graph import create_graph
from ai_qa_assistant.state import QAState


def run_analysis(user_story: str) -> QAState:
    """
    Run the QA analysis pipeline.
    
    Args:
        user_story: User story text to analyze
        
    Returns:
        Final state with complete analysis and report
    """
    # Load configuration
    config = load_config()
    
    # Validate API key
    if not config["openai_api_key"]:
        raise ValueError("OPENAI_API_KEY not set in environment variables")
    
    # Initialize graph
    graph = create_graph()
    
    # Initialize state
    state = QAState(user_story=user_story)
    
    # Run analysis
    result = graph.invoke(state.model_dump())
    
    return QAState(**result)


def main():
    """
    Main entry point for CLI usage.
    """
    if len(sys.argv) < 2:
        print("Usage: ai-qa-assistant <user_story>")
        print("       ai-qa-assistant --file <path_to_file>")
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
    else:
        user_story = " ".join(sys.argv[1:])
    
    # Run analysis
    try:
        result = run_analysis(user_story)
        print("\n" + "=" * 60)
        print("ANÁLISE CONCLUÍDA")
        print("=" * 60)
        print(result.report)
    except Exception as e:
        print(f"Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()