# Dynamic Pricing AI Agent Module

This directory contains the Agentic AI module for the Dynamic Pricing System. It handles competitor data collection, sales velocity analysis, inventory status, LLM reasoning (via Gemini), pricing recommendation generation, guardrail validation, and action logging.

## Planned Workflow Architecture

```text
OBSERVE
  ↓
  ├── Collect competitor prices
  ├── Collect sales data
  ├── Calculate sales velocity
  └── Check inventory
  ↓
ANALYZE
  ↓
  └── Use Gemini for reasoning (LangGraph orchestration)
  ↓
DECIDE
  ↓
  └── Generate pricing recommendation
  ↓
VALIDATE
  ↓
  └── Check minimum price, maximum price, and maximum change percentage
  ↓
ACT
  ↓
  └── Return recommendation / update pricing
  ↓
LOG
  ↓
  └── Store agent activity & decision audit log
```

## Directory Structure

- `tools/`: LangGraph tools for fetching competitor prices, sales velocity, inventory levels, and pricing validation.
  - `competitor_tool.py`: Collects competitor pricing data.
  - `sales_tool.py`: Calculates sales velocity and demand trends.
  - `inventory_tool.py`: Monitors stock levels and reorder thresholds.
  - `pricing_tool.py`: Validates price recommendations against business guardrails.
- `graph/`: LangGraph state graph definition and execution nodes.
  - `pricing_agent.py`: Constructs and manages the agent execution flow.
- `prompts/`: System and task prompts for Gemini LLM.
  - `pricing_prompt.py`: Prompts for pricing analysis and decision reasoning.
- `models/`: Data structures and state definitions using Pydantic.
  - `schemas.py`: Input/output schemas and agent state models.
- `services/`: API client for interacting with the backend service.
  - `backend_client.py`: Async HTTP client for backend endpoints.
- `config.py`: Environment variables, model specs, and guardrail settings.
- `main.py`: Entry point for executing the agent module.
- `requirements.txt`: Agent dependencies (`langgraph`, `langchain-google-genai`, `pydantic`, `python-dotenv`, `httpx`).
