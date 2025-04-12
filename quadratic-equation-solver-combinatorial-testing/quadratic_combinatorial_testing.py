import time

start_time = time.time()

import cmath  # To handle both real and complex square roots


# Function to solve the quadratic equation ax² + bx + c = 0
def solve_quadratic(a, b, c):
    # Case 1: All coefficients are zero (0x² + 0x + 0 = 0)
    if a == 0 and b == 0 and c == 0:
        return "Infinite Solutions"  # Any x is a solution

    # Case 2: a=0, b=0 but c is not zero (Invalid equation)
    elif a == 0 and b == 0:
        return "No Solution"  # No valid solution exists

    # Case 3: a=0 (Linear equation bx + c = 0)
    elif a == 0:
        return (-c / b,)  # One solution (tuple)

    # Case 4: Quadratic Equation (Standard Case)
    else:
        # Calculate the discriminant (b² - 4ac)
        discriminant = (b ** 2) - (4 * a * c)

        # Calculate square root of discriminant (handles complex numbers)
        sqrt_val = cmath.sqrt(discriminant)

        # Calculate the two roots
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)

        # If both roots are the same (repeated root)
        if root1 == root2:
            return (root1,)

        # Otherwise return both roots
        return (root1, root2)


# Test Cases List based on Combinatorial Testing
# Each tuple represents a test case in the form (a, b, c)
test_cases = [
    (0, 2, 3),    # TC1 - Linear Equation
    (0, 0, 5),    # TC2 - No Solution
    (1, -3, 2),   # TC3 - Real Distinct Roots
    (1, 2, 1),    # TC4 - Real Repeated Roots
    (1, 2, 5),    # TC5 - Complex Roots
    (0, 0, 0),    # TC6 - Infinite Solutions
    (10, 5, 1),   # TC7 - Large Coefficients
    (-1, 2, -3),  # TC8 - Negative Coefficients
    (1, 0, -4),   # TC9 - b=0 Case, Real Roots
    (1, 0, 4),    # TC10 - b=0 Case, Complex Roots
    (1, -5, 0),   # TC11 - c=0 Case, Roots at 0 and another real number
]

# Running and Printing All Test Cases
print("Quadratic Equation Solver Test Cases:\n")

for idx, (a, b, c) in enumerate(test_cases, start=1):
    print(f"Test Case {idx}: a={a}, b={b}, c={c}")
    result = solve_quadratic(a, b, c)
    print("Roots / Output:", result)
    print("-" * 50)

end_time = time.time()
execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")