"""
Configuration management for the AI QA Assistant.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from project root
project_root = Path(__file__).parent.parent.parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)


def load_config() -> dict:
    """
    Load configuration from environment variables.
    
    Returns:
        Dictionary with configuration values:
            - openai_api_key: API key for OpenAI
            - openai_model: Model name (default: gpt-4o)
    """
    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "openai_model": os.getenv("OPENAI_MODEL", "gpt-4o"),
    }