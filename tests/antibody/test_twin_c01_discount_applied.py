"""Twin c01: (original - discounted) == expected_saving in discounts.discount_applied."""
from src.discounts import discount_applied


def test_discount_applied_float_equality():
    # 1.0 - 0.9 in IEEE-754 is 0.09999999999999998, not 0.1
    original = 1.0
    discounted = 0.9
    expected_saving = 0.1
    # The saving IS logically correct; the function must return True
    assert discount_applied(original, discounted, expected_saving), (
        "discount_applied returned False due to float == precision error"
    )
