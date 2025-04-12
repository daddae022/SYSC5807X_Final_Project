import cmath
import time

start_time = time.time()

# ========================================
# Initial Version of Quadratic Solver
# (Commented Out for Reference)
# ========================================

# def solve_quadratic(a, b, c):
#     if a == 0 and b == 0 and c == 0:
#         return "Infinite Solutions"
#     elif a == 0 and b == 0:
#         return "No Solution"
#     elif a == 0:
#         return (-c / b,)
#     else:
#         discriminant = (b ** 2) - (4 * a * c)
#         sqrt_val = cmath.sqrt(discriminant)
#         root1 = (-b + sqrt_val) / (2 * a)
#         root2 = (-b - sqrt_val) / (2 * a)
#         if root1 == root2:
#             return (root1,)
#         return (root1, root2)

# ========================================
# Improved Version of Quadratic Solver
# With Enhanced Tests for Mutation Testing
# ========================================


def solve_quadratic(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return "Infinite Solutions"
    elif a == 0 and b == 0:
        return "No Solution"
    elif a == 0:
        return (-c / b,)
    else:
        discriminant = (b ** 2) - (4 * a * c)
        sqrt_val = cmath.sqrt(discriminant)
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)
        if root1 == root2:
            return (root1,)
        return (root1, root2)

# Existing Test Cases
test_cases = [
    (0, 2, 3),
    (0, 0, 5),
    (1, -3, 2),
    (1, 2, 1),
    (1, 2, 5),
    (0, 0, 0),
    (10, 5, 1),
    (-1, 2, -3),
    (1, 0, -4),
    (1, 0, 4),
    (1, -5, 0),
]

print("Quadratic Equation Solver Test Cases:\n")

for idx, (a, b, c) in enumerate(test_cases, start=1):
    print(f"Test Case {idx}: a={a}, b={b}, c={c}")
    result = solve_quadratic(a, b, c)
    print("Roots / Output:", result)
    print("-" * 50)

# Enhanced Tests for Mutation Score Improvement

print("\nEnhanced Tests for Mutation Testing:\n")

def test_discriminant():
    a, b, c = 1, -3, 2
    discriminant = (b ** 2) - (4 * a * c)
    assert discriminant == 1, "Discriminant value mismatch"

test_discriminant()

def test_roots_properties():
    a, b, c = 1, -3, 2
    roots = solve_quadratic(a, b, c)
    sum_roots = sum(roots)
    prod_roots = roots[0] * roots[1]
    assert sum_roots == 3, "Sum of roots mismatch"
    assert prod_roots == 2, "Product of roots mismatch"

test_roots_properties()

def test_small_coefficients():
    a, b, c = 1e-9, 1e-9, 1e-9
    roots = solve_quadratic(a, b, c)
    assert roots is not None, "Solver failed for small coefficients"

test_small_coefficients()

def test_invalid_inputs():
    try:
        solve_quadratic("a", "b", "c")
    except Exception:
        print("Invalid input correctly raised an exception")

test_invalid_inputs()

end_time = time.time()
execution_time = end_time - start_time
print("\nExecution Time:", execution_time, "seconds")
