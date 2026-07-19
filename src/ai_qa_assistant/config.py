"""
Configuration management for the AI QA Assistant.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


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