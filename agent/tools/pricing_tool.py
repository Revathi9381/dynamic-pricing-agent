"""
Pricing Validation and Guardrail Enforcement Tool.

Validates proposed prices against business safety rules (minimum price,
maximum price, and maximum allowable percentage price change).
"""

from typing import Tuple


def validate_price_recommendation(
    current_price: float,
    recommended_price: float,
    min_price: float,
    max_price: float,
    max_change_percent: float = 15.0
) -> Tuple[bool, str]:
    """
    Validate a recommended price against floor, ceiling, and maximum change rules.

    Args:
        current_price (float): Original product price.
        recommended_price (float): Proposed new price.
        min_price (float): Allowed floor price.
        max_price (float): Allowed ceiling price.
        max_change_percent (float): Maximum allowed percentage change (+/-).

    Returns:
        Tuple[bool, str]: (is_valid, reason_message)
    """
    if recommended_price < min_price:
        return False, f"Recommended price {recommended_price} below floor price {min_price}."
    if recommended_price > max_price:
        return False, f"Recommended price {recommended_price} above ceiling price {max_price}."

    change_pct = abs((recommended_price - current_price) / current_price) * 100
    if change_pct > max_change_percent:
        return False, f"Price change of {change_pct:.1f}% exceeds max threshold of {max_change_percent}%."

    return True, "Price recommendation is valid."
