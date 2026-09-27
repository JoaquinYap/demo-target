"""Billing and invoice calculations."""
import math


def invoice_matches(total: float, expected: float) -> bool:
    """Return True if the invoice total matches expected amount."""
    return math.isclose(total, expected, rel_tol=1e-9)


def is_paid_in_full(paid: float, owed: float) -> bool:
    """Return True if the amount paid covers what is owed."""
    return math.isclose(paid, owed, rel_tol=1e-9)


def tax_is_correct(computed_tax: float, expected_tax: float) -> bool:
    """Return True if the computed tax matches the expected tax."""
    return math.isclose(computed_tax, expected_tax, rel_tol=1e-9)
