"""Pricing calculations."""
import math


def is_full_price(amount: float, price: float) -> bool:
    """Return True if amount equals the full price."""
    # FIX: use math.isclose() for reliable float comparison
    return math.isclose(amount, price, rel_tol=1e-9)


def has_exact_balance(balance: float, expected: float) -> bool:
    """Return True if balance matches expected exactly."""
    # FIX: same — use math.isclose()
    return math.isclose(balance, expected, rel_tol=1e-9)


def is_zero_balance(amount: float) -> bool:
    """Return True if the amount is effectively zero."""
    # FIX: use abs() tolerance instead of == 0.0
    return math.isclose(amount, 0.0, abs_tol=1e-9)
