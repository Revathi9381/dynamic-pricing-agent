"""
Pydantic Data Models for Dynamic Pricing AI Agent.

This module defines input payload schemas and decision output schemas
with Pydantic v2 validations for data integrity, business rules, and guardrails.
"""

from typing import List
from pydantic import BaseModel, Field, model_validator


class PricingInput(BaseModel):
    """
    Input schema containing all product metrics, market data, inventory status,
    and business guardrail constraints required for dynamic pricing evaluation.
    """
    product_id: str = Field(..., description="Unique product identifier")
    product_name: str = Field(..., description="Name of the product")
    current_price: float = Field(..., gt=0, description="Current price of the product (must be > 0)")
    cost_price: float = Field(..., gt=0, description="Cost price of the product (must be > 0)")
    competitor_average_price: float = Field(..., gt=0, description="Average price across competitors (must be > 0)")
    sales_velocity: float = Field(..., ge=0, description="Sales velocity e.g. units/day (must be >= 0)")
    inventory: int = Field(..., ge=0, description="Current stock count (must be >= 0)")
    business_objective: str = Field(..., description="Target business objective e.g. 'maximize_profit', 'clearance'")
    minimum_price: float = Field(..., gt=0, description="Minimum price floor constraint (must be > 0)")
    maximum_price: float = Field(..., gt=0, description="Maximum price ceiling constraint (must be > 0)")
    maximum_change_percentage: float = Field(..., gt=0, description="Maximum allowed percentage price change (must be > 0)")

    @model_validator(mode="after")
    def validate_price_boundaries(self) -> "PricingInput":
        """Validate that maximum_price is strictly greater than minimum_price."""
        if self.maximum_price <= self.minimum_price:
            raise ValueError(
                f"maximum_price ({self.maximum_price}) must be greater than minimum_price ({self.minimum_price})"
            )
        return self


class PricingDecision(BaseModel):
    """
    Output schema representing the agent's finalized price recommendation,
    including reasoning, contributing factor analysis, and confidence score.
    """
    product_id: str = Field(..., description="Unique product identifier")
    current_price: float = Field(..., gt=0, description="Original product price (must be > 0)")
    recommended_price: float = Field(..., gt=0, description="Agent recommended price (must be > 0)")
    action: str = Field(..., description="Pricing action e.g. 'increase', 'decrease', 'hold'")
    reason: str = Field(..., description="Detailed explanation for the recommended pricing decision")
    factors: List[str] = Field(default_factory=list, description="Key factors influencing the decision")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score between 0.0 and 1.0")
