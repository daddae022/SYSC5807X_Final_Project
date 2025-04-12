import cmath  # To handle real and complex roots


# Function to solve ax² + bx + c = 0
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


# Function to compare roots (ignoring order)
def roots_are_equal(roots1, roots2, tolerance=1e-6):
    roots1 = sorted(roots1, key=lambda x: (x.real, x.imag))
    roots2 = sorted(roots2, key=lambda x: (x.real, x.imag))

    if len(roots1) != len(roots2):
        return False

    for r1, r2 in zip(roots1, roots2):
        if abs(r1 - r2) > tolerance:
            return False
    return True


# Test Case: a=1, b=-3, c=2 (Real Roots: x=1, x=2)
original_a, original_b, original_c = 1, -3, 2
original_roots = solve_quadratic(original_a, original_b, original_c)

print("Original Roots:", original_roots)
print("=" * 50)

# MR1: Scaling Coefficients by k=5
k = 5
scaled_roots = solve_quadratic(original_a * k, original_b * k, original_c * k)
print("MR1 - Scaling Coefficients Roots:", scaled_roots)
print("MR1 Passed:", roots_are_equal(original_roots, scaled_roots))
print("=" * 50)

# MR2: Negating All Coefficients
negated_roots = solve_quadratic(-original_a, -original_b, -original_c)
print("MR2 - Negating Coefficients Roots:", negated_roots)
print("MR2 Passed:", roots_are_equal(original_roots, negated_roots))
print("=" * 50)

# MR3: Swapping b and c
swapped_roots = solve_quadratic(original_a, original_c, original_b)
print("MR3 - Swapped b and c Roots:", swapped_roots)
print("MR3 Passed: Roots are Different (as expected)")
print("=" * 50)

# MR4: Setting c=0
zero_c_roots = solve_quadratic(original_a, original_b, 0)
print("MR4 - Roots when c=0:", zero_c_roots)
print("MR4 Passed: One of the Roots is Zero =", any(abs(root) < 1e-6 for root in zero_c_roots))
print("=" * 50)
