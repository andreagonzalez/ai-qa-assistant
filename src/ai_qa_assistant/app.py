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
    print(result["report"])
"""

import os
import re
import sys
from pathlib import Path
from typing import List

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
        Returns a dict (QAState TypedDict) with all fields populated
        
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
    
    # Initialize state as dict (QAState is TypedDict)
    state: QAState = {
        "user_story": user_story,
        "checklist": "",
        "analysis": "",
        "acceptance_criteria": "",
        "test_cases": "",
        "risks": "",
        "recommendations": "",
        "report": "",
    }
    
    # Run analysis
    result: QAState = graph.invoke(state)
    
    return result


def load_user_stories_from_file(file_path: str) -> List[str]:
    """
    Load one or more user stories from a text file.

    The file may contain multiple user stories separated by one or more
    blank lines or by the separator line "---".
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # Split stories by blank lines or explicit separator lines, then
    # filter out any segments that are empty or contain only dashes
    raw_parts = re.split(r"(?:\n\s*\n+|\n-{3,}\s*\n)", content)
    stories = []
    for part in raw_parts:
        s = part.strip()
        if not s:
            continue
        # skip parts that are just separator lines like '---' or '-----'
        if re.fullmatch(r"-+", s):
            continue
        stories.append(s)

    if not stories:
        raise ValueError(f"No user stories found in file: {file_path}")

    return stories


def run_analysis_batch(user_stories: List[str]) -> List[QAState]:
    """
    Run analysis for multiple user stories sequentially.
    """
    results: List[QAState] = []
    for user_story in user_stories:
        results.append(run_analysis(user_story))
    return results


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
    
    # Get user stories
    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Error: --file requires a path argument")
            sys.exit(1)
        
        file_path = sys.argv[2]
        try:
            user_stories = load_user_stories_from_file(file_path)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    elif sys.argv[1] == "--example":
        user_stories = [EXAMPLE_USER_STORY]
    else:
        user_stories = [" ".join(sys.argv[1:])]
    
    # Run analysis for one or more stories
    try:
        results = run_analysis_batch(user_stories)
        for idx, result in enumerate(results, start=1):
            header = f"USER STORY {idx}/{len(results)}"
            print("\n" + "=" * 60)
            print(header)
            print("=" * 60)
            print(result["report"])
            if idx < len(results):
                print("\n" + "#" * 60 + "\n")
    except Exception as e:
        print(f"Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()