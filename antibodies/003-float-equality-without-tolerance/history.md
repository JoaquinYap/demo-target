# Antibody 003: Float equality compared with == instead of math.isclose(), causing false negatives due to floating-point precision.

Created 2026-09-27T02:27:08+00:00 from fix_commit `7a3e9e6`.

## What broke

Floating-point arithmetic accumulates rounding error, so two logically equal values (e.g. 0.1 + 0.2 and 0.3) are rarely bit-for-bit identical; == therefore returns False when it should return True (or vice-versa), producing silently wrong results in pricing, balance and threshold checks.

**Pattern:** A float value is compared using == (or !=) directly against another float or a float literal, rather than using math.isclose() or an absolute-tolerance check.

**Triggers when:** A float is the result of arithmetic (addition, subtraction, multiplication, division) and is then compared with ==; A float is compared with the literal 0.0 or any other float constant without a tolerance; The function is used in a financial, measurement or threshold context where small residuals matter

## How it was fixed

Replace every `float == float` and `float != float` comparison with math.isclose(a, b, rel_tol=...) for relative comparisons and math.isclose(a, 0.0, abs_tol=...) when checking for zero.

Original instance: `src/pricing.py:11`

## Twins found and proven

| Twin | Location | Status | Test |
|---|---|---|---|
| c01 | `src/discounts.py:10` | fixed | `tests/antibody/test_twin_c01_discount_applied.py` |
| c02 | `src/discounts.py:16` | fixed | `tests/antibody/test_twin_c02_is_free.py` |
| c03 | `src/discounts.py:22` | fixed | `tests/antibody/test_twin_c03_rates_match.py` |
| c04 | `src/billing.py:11` | fixed | `tests/antibody/test_twin_c04_invoice_matches.py` |
| c05 | `src/billing.py:17` | fixed | `tests/antibody/test_twin_c05_is_paid_in_full.py` |
| c06 | `src/billing.py:23` | fixed | `tests/antibody/test_twin_c06_tax_is_correct.py` |

## Immunity

| Round | Detected | Immunity |
|---|---|---|
| 0 (before Antibody) | 5/6 | 83% |
| 1 | 6/6 | 100% |
| 2 | 6/6 | 100% |

## Defenses

- Semgrep rule: `.antibody/antibodies/003-float-equality-without-tolerance/rule.yml`
- Regression tests: listed in the twins table above.
