# AI Code Review Assignment (Python)

## Candidate
- Name: Belayneh Getachew
- Approximate time spent: 70 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function divides by len(orders) even though cancelled orders are excluded from the total, producing an incorrect average when any orders are cancelled.
- If orders is empty, the function raises ZeroDivisionError.
- If all orders are cancelled, the function also raises ZeroDivisionError.

### Edge cases & risks
- Orders may be missing the "amount" key.
- "amount" values may be non-numeric.
- "status" comparison is case-sensitive, which may lead to incorrect inclusion/exclusion.

### Code quality / design issues
- No explicit validation or error signaling for invalid input.
- The function silently returns incorrect results instead of failing fast on invalid scenarios.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track the count of non-cancelled orders separately.
- Divide by the number of included orders, not total orders.
- Raise a clear ValueError when no valid orders exist.
- Validate that amount exists and is numeric.
- Normalize order status comparison.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Orders list is empty.
    - To ensure the function fails gracefully and does not raise an unintended ZeroDivisionError.
- All orders are cancelled.
    - To verify that cancelled orders are correctly excluded and that the function handles the absence of valid data explicitly.
- Mixed cancelled and non-cancelled orders.
    - To confirm that only non-cancelled orders contribute to both the total and the divisor.
- Orders with missing or non-numeric amount.
    - To ensure invalid input is detected early and does not silently corrupt the calculation.
- Different casing of "cancelled" status.
    - To verify consistent behavior regardless of input normalization (e.g., "Cancelled", "CANCELLED").
## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Claims cancelled orders are excluded correctly, which is false due to incorrect denominator.
- Does not mention failure cases such as empty or all-cancelled input.
- Overstates correctness without addressing validation.

### Rewritten explanation
- This function computes the average order value across non-cancelled orders by summing their amounts and dividing by the number of included orders. Cancelled orders are excluded based on a case-insensitive status check. If there are no non-cancelled orders or if amounts are invalid, the function raises a clear error instead of returning an incorrect result.

## 4) Final Judgment
- Decision: Reject
- Justification: Produces incorrect averages and fails on common edge cases.
- Confidence & unknowns: Confident in correctness of issues identified; assumptions about order schema are based on typical usage.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The function treats any string containing "@" as a valid email, which is incorrect
- Strings like "@", "a@@b", or "a@ b.com" are counted as valid.

### Edge cases & risks
- Non-string inputs are not explicitly handled.
- The logic does not reflect real-world expectations of email validity.

### Code quality / design issues
- Validation logic is overly simplistic and misleading.
- Explanation claims correctness that the code does not provide.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Introduced a lightweight email validation helper.
- Ensured exactly one "@", no whitespace, non-empty local/domain parts.
- Ignored non-string inputs safely.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Incorrectly claims to count “valid email addresses”.
- Overstates safety and correctness of validation logic.

### Rewritten explanation
- This function counts email addresses that pass a basic structural validation. An email is considered valid if it is a string with exactly one "@", non-empty local and domain parts, no whitespace, and a domain containing at least one dot. Invalid or non-string entries are ignored.

## 4) Final Judgment
- Decision: Reject
- Justification: Validation logic does not match explanation or real-world expectations.
- Confidence & unknowns: Confident in identified issues; 
    
    Note: I intentionally avoided regex-based email validation to prioritize clarity and reviewability over superficial correctness. Full RFC-compliant validation is out of scope and better handled by dedicated libraries.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function divides by len(values) even though None values are excluded from the total.
- Raises ZeroDivisionError when input is empty or all values are None.

### Edge cases & risks
- Non-numeric values cause runtime exceptions.
- Explanation claims mixed input types are handled safely, which is false.

### Code quality / design issues
- Inconsistent handling of invalid values.
- Incorrect average computation logic.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only values successfully converted to float.
- Ignore None and non-numeric values.
- Raise a clear error when no valid numeric values exist.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty input.
- All None values.
- Mixed numeric and non-numeric values.
- String representations of numbers.
## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Incorrectly claims accurate averaging.
- Claims safe handling of mixed types when exceptions are possible.

### Rewritten explanation
- This function computes the average of valid numeric measurements by ignoring None and values that cannot be converted to float. Only successfully converted values are included in the calculation. If no valid numeric values exist, the function raises an error.

## 4) Final Judgment
- Decision: Reject
- Justification: Produces incorrect results and crashes on common inputs.
- Confidence & unknowns: High confidence in correctness of review; behavior choices are explicitly documented.
