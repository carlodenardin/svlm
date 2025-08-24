import math
import cmath

def solve_quadratic(a, b, c):
    """
    Solve ax^2 + bx + c = 0.
    Returns a tuple (root1, root2). Roots may be real or complex numbers.
    """
    if a == 0:
        raise ValueError('Coefficient a must be non-zero for a quadratic equation.')
    discriminant = b * b - 4 * a * c
    two_a = 2 * a
    if discriminant > 0:
        sqrt_disc = math.sqrt(discriminant)
        root1 = (-b + sqrt_disc) / two_a
        root2 = (-b - sqrt_disc) / two_a
        return (root1, root2)
    elif discriminant == 0:
        root = -b / two_a
        return (root, root)
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / two_a
        root2 = (-b - cmath.sqrt(discriminant)) / two_a
        return (root1, root2)