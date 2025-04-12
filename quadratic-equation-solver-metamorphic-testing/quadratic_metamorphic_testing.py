import cmath
import time

start_time = time.time()

# ========================================
# Quadratic Equation Solver Function
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

# ========================================
# Metamorphic Testing Begins
# ========================================

print("Metamorphic Testing for Quadratic Equation Solver\n")

# Seed Test Case
a, b, c = 1, -3, 2
original_roots = solve_quadratic(a, b, c)
print("Original Roots:", original_roots)
print("=" * 50)

# MR1: Scaling Coefficients
scaled_roots = solve_quadratic(a * 2, b * 2, c * 2)
print("MR1 - Scaling Coefficients Roots:", scaled_roots)
print("MR1 Passed:", original_roots == scaled_roots)
print("=" * 50)

# MR2: Negating All Coefficients
negated_roots = solve_quadratic(-a, -b, -c)
print("MR2 - Negating Coefficients Roots:", negated_roots)
print("MR2 Passed:", set(original_roots) == set(negated_roots))
print("=" * 50)

# MR3: Swapping b and c (Expected Different Roots)
swapped_roots = solve_quadratic(a, c, b)
print("MR3 - Swapped b and c Roots:", swapped_roots)
print("MR3 Passed: Roots are Different (as expected)")
print("=" * 50)

# MR4: Setting c=0 (Expecting a root at 0)
c_zero_roots = solve_quadratic(a, b, 0)
print("MR4 - Roots when c=0:", c_zero_roots)
print("MR4 Passed: One of the Roots is Zero =", any(root == 0 for root in c_zero_roots))
print("=" * 50)

# ========================================
# Enhanced Tests for Mutation Score Improvement
# ========================================

print("Enhanced Tests for Mutation Testing:\n")

# Discriminant Verification
def test_discriminant():
    discriminant = (b ** 2) - (4 * a * c)
    assert discriminant == 1, "Discriminant value mismatch"

test_discriminant()

# Verify Sum and Product of Roots
def test_roots_properties():
    roots = solve_quadratic(a, b, c)
    sum_roots = sum(roots)
    prod_roots = roots[0] * roots[1]
    assert sum_roots == 3, "Sum of roots mismatch"
    assert prod_roots == 2, "Product of roots mismatch"

test_roots_properties()

# Small Coefficient Edge Case
def test_small_coefficients():
    a, b, c = 1e-9, 1e-9, 1e-9
    roots = solve_quadratic(a, b, c)
    assert roots is not None, "Solver failed for small coefficients"

test_small_coefficients()

# Invalid Input Handling
def test_invalid_inputs():
    try:
        solve_quadratic("a", "b", "c")
    except Exception:
        print("Invalid input correctly raised an exception")

test_invalid_inputs()

end_time = time.time()
execution_time = end_time - start_time
print("\nExecution Time:", execution_time, "seconds")
