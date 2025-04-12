from datetime import datetime

# Function to convert date from YYYY-MM-DD to DD/MM/YYYY
def convert_date_format(input_date):
    try:
        # Parse input date string into a datetime object
        date_obj = datetime.strptime(input_date, "%Y-%m-%d")
        # Reformat date to DD/MM/YYYY
        return date_obj.strftime("%d/%m/%Y")
    except ValueError:
        # Handle invalid date formats or non-existing dates
        return "Invalid Date"


# List of Test Cases (Generated using Combinatorial Testing)
# Each tuple is in the form (Test Case ID, Input Date)
test_cases = [
    ("TC1", "2023-04-15"),  # Normal Date
    ("TC2", "2020-02-29"),  # Leap Year Valid
    ("TC3", "2023-02-29"),  # Invalid Leap Day
    ("TC4", "2023-01-31"),  # End of Month
    ("TC5", "2023-00-10"),  # Invalid Month 00
    ("TC6", "2023-13-10"),  # Invalid Month 13
    ("TC7", "2023-03-00"),  # Invalid Day 00
    ("TC8", "2023-03-32"),  # Invalid Day 32
    ("TC9", "1900-01-01"),  # Boundary Year
    ("TC10", "2000-02-29"), # Leap Year 2000
]

print("Date Conversion Program Test Cases:\n")

# Loop to run all test cases
for test_id, input_date in test_cases:
    output_date = convert_date_format(input_date)
    print(f"{test_id}: Input Date = {input_date} | Converted Output = {output_date}")
    print("-" * 50)
