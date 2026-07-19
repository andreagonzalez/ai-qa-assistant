"""
LangChain LLM integration for the AI QA Assistant.

This module provides utilities for interacting with the LLM
using LangChain. It supports both OpenAI and Groq models.
"""

import os
from typing import Optional

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from ai_qa_assistant.config import load_config


def get_llm(model_name: Optional[str] = None) -> ChatOpenAI:
    """
    Create and return a configured LLM instance.
    
    Supports OpenAI and Groq models through LangChain.
    Uses the OPENAI_API_KEY from environment variables.
    
    Args:
        model_name: Model name to use. If None, uses config value.
                   Examples:
                   - "gpt-4o" (OpenAI)
                   - "llama-3.1-70b-versatile" (Groq)
                   
    Returns:
        Configured ChatOpenAI instance
        
    Raises:
        ValueError: If API key is not set
    """
    config = load_config()
    api_key = config.get("openai_api_key")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in environment variables")
    
    # Use provided model or default from config
    model = model_name or config.get("openai_model", "gpt-4o")
    
    # Configure the LLM
    llm = ChatOpenAI(
        model=model,
        api_key=api_key,
        temperature=0.1,  # Low temperature for more deterministic output
        model_kwargs={"response_format": {"type": "text"}},
    )
    
    return llm


def call_llm(prompt_text: str, system_prompt: str) -> str:
    """
    Call the LLM with a prompt and system message.
    
    Args:
        prompt_text: User prompt text
        system_prompt: System prompt for role definition
        
    Returns:
        LLM response as string
    """
    llm = get_llm()
    
    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", prompt_text),
    ])
    
    # Create chain
    chain = prompt | llm | StrOutputParser()
    
    # Invoke and return
    return chain.invoke({})


def call_llm_with_template(prompt_template: str, **kwargs) -> str:
    """
    Call the LLM with a templated prompt.
    
    Args:
        prompt_template: Prompt template with {placeholders}
        **kwargs: Arguments to fill the template
        
    Returns:
        LLM response as string
    """
    prompt_text = prompt_template.format(**kwargs)
    return call_llm(prompt_text, kwargs.get("system_prompt", ""))