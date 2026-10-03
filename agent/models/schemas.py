"""
Data Models and State Schemas for Dynamic Pricing AI Agent.

Defines Pydantic data structures for product details, competitor pricing,
sales velocity metrics, inventory status, price recommendation outputs,
and the agent's state representation.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class CompetitorPrice(BaseModel):
    """Schema representing pricing data from a single competitor."""
    competitor_name: str
    price: float
    url: Optional[str] = None


class ProductState(BaseModel):
    """Schema representing the current product metrics and state."""
    product_id: str
    product_name: str
    current_price: float
    min_price: float
    max_price: float
    cost_price: float
    inventory_count: int
    sales_velocity: float  # e.g., units sold per day
    competitor_prices: List[CompetitorPrice] = Field(default_factory=list)


class PriceRecommendation(BaseModel):
    """Schema representing the agent's generated price recommendation."""
    product_id: str
    current_price: float
    recommended_price: float
    price_change_percentage: float
    reasoning: str
    is_validated: bool = False
    validation_message: str = ""
