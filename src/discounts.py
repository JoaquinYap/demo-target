"""Discount engine."""
import math


def discount_applied(original: float, discounted: float, expected_saving: float) -> bool:
    """Return True if the saving equals the expected discount amount."""
    return math.isclose(original - discounted, expected_saving, rel_tol=1e-9)


def is_free(price: float) -> bool:
    """Return True if the item is free (price == 0)."""
    return math.isclose(price, 0.0, abs_tol=1e-9)


def rates_match(rate_a: float, rate_b: float) -> bool:
    """Return True if two discount rates are equal."""
    return math.isclose(rate_a, rate_b, rel_tol=1e-9)
