"""Twin c05: paid == owed in billing.is_paid_in_full."""
from src.billing import is_paid_in_full


def test_is_paid_in_full_float_equality():
    # 0.1 + 0.2 should equal 0.3 logically
    paid = 0.1 + 0.2
    owed = 0.3
    assert is_paid_in_full(paid, owed), (
        "is_paid_in_full returned False due to float == precision error"
    )
