# Antibody 001: datetime.now() without a timezone produces a naive datetime that cannot be compared to an aware datetime.

Created 2026-09-26T00:04:39+00:00 from fix_commit `c056747`.

## What broke

Python forbids mixing naive and aware datetimes in comparisons or subtraction. Passing no argument to datetime.now() returns a naive local time; if any counterpart carries tzinfo the operation raises TypeError at runtime.

**Pattern:** datetime.now() called without timezone argument when the other operand is an aware datetime, causing a TypeError at comparison or arithmetic.

**Triggers when:** A timezone-aware datetime is compared with datetime.now() (no tz argument); Arithmetic (subtraction) is performed between an aware deadline and datetime.now() (no tz argument)

## How it was fixed

Replace every datetime.now() that interacts with an aware datetime with datetime.now(timezone.utc) so both operands share the same tzinfo.

Original instance: `src/tasks.py:15`

## Twins found and proven

| Twin | Location | Status | Test |
|---|---|---|---|
| c01 | `src/subscriptions.py:17` | fixed | `tests/antibody/test_twin_c01_subscriptions.py` |
| c02 | `src/tokens.py:17` | fixed | `tests/antibody/test_twin_c02_tokens.py` |
| c03 | `src/sessions.py:17` | fixed | `tests/antibody/test_twin_c03_sessions.py` |

## Immunity

| Round | Detected | Immunity |
|---|---|---|
| 0 (before Antibody) | 5/6 | 83% |
| 1 | 6/6 | 100% |

## Defenses

- Semgrep rule: `.antibody/antibodies/001-naive-vs-aware-datetime/rule.yml`
- Regression tests: listed in the twins table above.
