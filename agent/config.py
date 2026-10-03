"""
Configuration Settings for Dynamic Pricing AI Agent.

This module manages environment variables, model configurations, API keys,
and pricing guardrail thresholds (min/max price limits, max change percentage).
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini LLM Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-pro")

# Backend API Configuration
BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL", "http://localhost:8000")

# Default Pricing Guardrails
DEFAULT_MAX_PRICE_CHANGE_PERCENT = 15.0  # Maximum allowed price change (+/- %)
