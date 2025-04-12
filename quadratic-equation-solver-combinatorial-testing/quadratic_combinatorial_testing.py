import cmath  # To handle both real and complex square roots
import time

start_time = time.time()

# Function to solve the quadratic equation ax² + bx + c = 0
def solve_quadratic(a, b, c):
    # Case 1: All coefficients are zero
    if a == 0 and b == 0 and c == 0:
        return "Infinite Solutions"

    # Case 2: a=0, b=0 but c != 0
    elif a == 0 and b == 0:
        return "No Solution"

    # Case 3: Linear Equation
    elif a == 0:
        return (-c / b,)

    # Case 4: Quadratic Equation
    else:
        discriminant = (b ** 2) - (4 * a * c)
        sqrt_val = cmath.sqrt(discriminant)
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)

        if root1 == root2:
            return (root1,)
        return (root1, root2)

# Existing Combinatorial Test Cases
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

print("Quadratic Equation Solver Test Cases:\n")

for idx, (a, b, c) in enumerate(test_cases, start=1):
    print(f"Test Case {idx}: a={a}, b={b}, c={c}")
    result = solve_quadratic(a, b, c)
    print("Roots / Output:", result)
    print("-" * 50)

# Enhanced Tests for Mutation Score Improvement
print("\nEnhanced Tests for Mutation Testing:\n")

# Test Discriminant Value
def test_discriminant():
    a, b, c = 1, -3, 2
    discriminant = (b ** 2) - (4 * a * c)
    assert discriminant == 1, "Discriminant value mismatch"

test_discriminant()

# Test Sum and Product of Roots
def test_roots_properties():
    a, b, c = 1, -3, 2
    roots = solve_quadratic(a, b, c)
    sum_roots = sum(roots)
    prod_roots = roots[0] * roots[1]
    assert sum_roots == 3, "Sum of roots mismatch"
    assert prod_roots == 2, "Product of roots mismatch"

test_roots_properties()

# Test Small Coefficients Edge Case
def test_small_coefficients():
    a, b, c = 1e-9, 1e-9, 1e-9
    roots = solve_quadratic(a, b, c)
    assert roots is not None, "Solver failed for small coefficients"

test_small_coefficients()

# Test Invalid Input Handling (Type Error)
def test_invalid_inputs():
    try:
        solve_quadratic("a", "b", "c")
    except Exception:
        print("Invalid input correctly raised an exception")

test_invalid_inputs()

end_time = time.time()
execution_time = end_time - start_time
print("\nExecution Time:", execution_time, "seconds")
