"""Twin c02: price == 0.0 in discounts.is_free."""
from src.discounts import is_free


def test_is_free_float_equality():
    # 0.1 + 0.2 - 0.3 is not exactly 0.0 in IEEE-754 but is logically zero
    price = 0.1 + 0.2 - 0.3
    assert is_free(price), (
        "is_free returned False for a logically-zero price due to float == 0.0"
    )
