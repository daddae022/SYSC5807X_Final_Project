import time
import re
from datetime import datetime

start_time = time.time()

# ========================================
# Date Conversion Function
# Converts YYYY-MM-DD to DD/MM/YYYY
# ========================================
def convert_date(date_str):
    try:
        # Parse the input date
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        # Validate components (Extra validation for mutation testing)
        if not (1 <= date_obj.month <= 12):
            return "Invalid Date"
        if not (1 <= date_obj.day <= 31):
            return "Invalid Date"

        # Convert to desired format
        return date_obj.strftime("%d/%m/%Y")
    except Exception:
        return "Invalid Date"


# ========================================
# Existing Combinatorial Test Cases
# ========================================
test_cases = [
    "2023-04-15",  # Normal date
    "2020-02-29",  # Leap year
    "2023-12-01",  # Single digit day
    "2023-01-31",  # Month boundary
    "2023-06-00",  # Invalid day
    "2023-13-10",  # Invalid month
    "abcd-ef-gh",  # Completely invalid
    "2023/04/15",  # Wrong separator
    "",            # Empty string
]

print("Date Conversion Program Test Cases:\n")

for idx, date_str in enumerate(test_cases, start=1):
    print(f"Test Case {idx}: Input = {date_str}")
    result = convert_date(date_str)
    print("Output:", result)
    print("-" * 50)

# ========================================
# Enhanced Tests for Mutation Testing
# ========================================

print("\nEnhanced Tests for Mutation Testing:\n")

# Test for Output Pattern Verification
def test_output_pattern():
    date_str = "2023-04-15"
    output = convert_date(date_str)
    assert re.match(r"\d{2}/\d{2}/\d{4}", output), "Output format mismatch"

test_output_pattern()

# Edge Case: Smallest Valid Date
def test_earliest_date():
    date_str = "0001-01-01"
    output = convert_date(date_str)
    assert output == "01/01/0001", "Earliest date conversion failed"

test_earliest_date()

# Edge Case: Largest Reasonable Date
def test_latest_date():
    date_str = "9999-12-31"
    output = convert_date(date_str)
    assert output == "31/12/9999", "Latest date conversion failed"

test_latest_date()

# Test Invalid Inputs
def test_invalid_inputs():
    invalid_dates = ["abcd-ef-gh", "2023-15-99", "", "2023/04/15"]
    for date in invalid_dates:
        output = convert_date(date)
        assert output == "Invalid Date", f"Failed to detect invalid input: {date}"

test_invalid_inputs()

end_time = time.time()
execution_time = end_time - start_time
print("\nExecution Time:", execution_time, "seconds")
