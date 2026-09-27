"""Twin c06: computed_tax == expected_tax in billing.tax_is_correct."""
from src.billing import tax_is_correct


def test_tax_is_correct_float_equality():
    # Tax: 7% of 99.99 => 0.07 * 99.99; expected from a separate calculation
    rate = 0.07
    amount = 99.99
    computed_tax = rate * amount          # may have floating-point residual
    expected_tax = 6.9993                 # same mathematical result, may differ in bits
    # Force the residual: use a value that triggers the IEEE-754 mismatch
    computed_tax2 = 0.1 * 0.7
    expected_tax2 = 0.07
    assert tax_is_correct(computed_tax2, expected_tax2), (
        "tax_is_correct returned False due to float == precision error"
    )
