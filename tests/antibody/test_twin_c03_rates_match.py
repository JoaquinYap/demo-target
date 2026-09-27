"""Twin c03: rate_a == rate_b in discounts.rates_match."""
from src.discounts import rates_match


def test_rates_match_float_equality():
    # 0.1 + 0.2 should equal 0.3 logically, but IEEE-754 disagrees
    rate_a = 0.1 + 0.2
    rate_b = 0.3
    assert rates_match(rate_a, rate_b), (
        "rates_match returned False due to float == precision error"
    )
