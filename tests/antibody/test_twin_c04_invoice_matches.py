"""Twin c04: total == expected in billing.invoice_matches."""
from src.billing import invoice_matches


def test_invoice_matches_float_equality():
    # 0.1 + 0.2 in IEEE-754 is 0.30000000000000004, not 0.3
    total = 0.1 + 0.2
    expected = 0.3
    assert invoice_matches(total, expected), (
        "invoice_matches returned False due to float == precision error"
    )
