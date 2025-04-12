import time
import re
from datetime import datetime, timedelta

start_time = time.time()

# ========================================
# Date Conversion Function
# Converts YYYY-MM-DD to DD/MM/YYYY
# ========================================
def convert_date(date_str):
    try:
        # Parse input date
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        # Additional validation
        if not (1 <= date_obj.month <= 12):
            return "Invalid Date"
        if not (1 <= date_obj.day <= 31):
            return "Invalid Date"

        return date_obj.strftime("%d/%m/%Y")
    except Exception:
        return "Invalid Date"

print("Metamorphic Testing for Date Conversion Program\n")

# ========================================
# Seed Test Case
seed_date = "2023-04-15"
converted_seed = convert_date(seed_date)
print("Seed Date:", seed_date)
print("Converted:", converted_seed)
print("=" * 50)

# MR1: Reversibility Test
def reverse_conversion(date_str):
    try:
        date_obj = datetime.strptime(convert_date(date_str), "%d/%m/%Y")
        return date_obj.strftime("%Y-%m-%d")
    except Exception:
        return "Invalid Date"

reconverted = reverse_conversion(seed_date)
print("MR1 - Reconverted:", reconverted)
print("MR1 Passed:", reconverted == seed_date)
print("=" * 50)

# MR2: Consistency with Leading Zeros
output_with_zeros = convert_date("2023-04-05")
output_without_zeros = convert_date("2023-4-5")
print("MR2 - With Leading Zeros Output:", output_with_zeros)
print("MR2 - Without Leading Zeros Output:", output_without_zeros)
print("MR2 Passed:", output_with_zeros == output_without_zeros)
print("=" * 50)

# MR3: Next Day Relation
def next_day(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        next_day_obj = date_obj + timedelta(days=1)
        return next_day_obj.strftime("%Y-%m-%d")
    except Exception:
        return "Invalid Date"

next_date = next_day("2023-01-31")
converted_next_date = convert_date(next_date)
print("MR3 - Next Day of 2023-01-31 is", next_date)
print("Converted Output:", converted_next_date)
print("=" * 50)

# MR4: Invalid Inputs
invalid_inputs = ["abcd-ef-gh", "2023-15-99", "", "2023/04/15"]
for input_str in invalid_inputs:
    output = convert_date(input_str)
    print(f"MR4 - Input: {input_str} | Output: {output} | Passed: {output == 'Invalid Date'}")
print("=" * 50)

# ========================================
# Enhanced Tests for Mutation Score Improvement
# ========================================

print("Enhanced Tests for Mutation Testing:\n")

# Output Format Check
def test_output_format():
    output = convert_date("2023-04-15")
    assert re.match(r"\d{2}/\d{2}/\d{4}", output), "Output format mismatch"

test_output_format()

# Earliest Valid Date
def test_earliest_date():
    output = convert_date("0001-01-01")
    assert output == "01/01/0001", "Earliest date conversion failed"

test_earliest_date()

# Latest Reasonable Date
def test_latest_date():
    output = convert_date("9999-12-31")
    assert output == "31/12/9999", "Latest date conversion failed"

test_latest_date()

# Invalid Inputs Handling
def test_invalid_inputs():
    for invalid in invalid_inputs:
        output = convert_date(invalid)
        assert output == "Invalid Date", f"Failed to detect invalid input: {invalid}"

test_invalid_inputs()

end_time = time.time()
execution_time = end_time - start_time
print("\nExecution Time:", execution_time, "seconds")
