import time

start_time = time.time()

from datetime import datetime, timedelta


# Function to convert date from YYYY-MM-DD to DD/MM/YYYY
def convert_date_format(input_date):
    try:
        date_obj = datetime.strptime(input_date, "%Y-%m-%d")
        return date_obj.strftime("%d/%m/%Y")
    except ValueError:
        return "Invalid Date"


print("Metamorphic Testing for Date Conversion Program\n")
print("=" * 50)

# MR1: Swapping formats twice should return original input
seed_date = "2023-04-15"
converted = convert_date_format(seed_date)

# Converting back from DD/MM/YYYY to YYYY-MM-DD
try:
    date_obj = datetime.strptime(converted, "%d/%m/%Y")
    reconverted = date_obj.strftime("%Y-%m-%d")
except ValueError:
    reconverted = "Invalid Date"

print("MR1 - Original Date:", seed_date)
print("Converted:", converted)
print("Reconverted:", reconverted)
print("MR1 Passed:", seed_date == reconverted)
print("=" * 50)

# MR2: Adding leading zeros
seed_date_no_zeros = "2023-4-5"
seed_date_with_zeros = "2023-04-05"

output1 = convert_date_format(seed_date_no_zeros)
output2 = convert_date_format(seed_date_with_zeros)

print("MR2 - No Leading Zeros Output:", output1)
print("MR2 - With Leading Zeros Output:", output2)
print("MR2 Passed:", output1 == output2)
print("=" * 50)

# MR3: Increasing day and checking date rollover
seed_date = "2023-01-31"
try:
    date_obj = datetime.strptime(seed_date, "%Y-%m-%d")
    new_date_obj = date_obj + timedelta(days=1)
    new_date = new_date_obj.strftime("%Y-%m-%d")
    output = convert_date_format(new_date)
except ValueError:
    output = "Invalid Date"

print("MR3 - Next Day of", seed_date, "is", new_date)
print("Converted Output:", output)
print("=" * 50)

# MR4: Invalid Input Always Returns "Invalid Date"
invalid_inputs = ["abcd-ef-gh", "2023-15-99", "2023/04/15", ""]

for invalid_date in invalid_inputs:
    output = convert_date_format(invalid_date)
    print(f"MR4 - Input: {invalid_date} | Output: {output} | Passed:", output == "Invalid Date")

print("=" * 50)

end_time = time.time()
execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")