def solve_quadratic(a, b, c):
    """
    Solve ax^2 + bx + c = 0 using the quadratic formula.
    Returns a tuple (x1, x2). Handles real and complex roots as per the described approach.
    """
    d = b * b - 4 * a * c

    def sqrt_like(z):
        if z >= 0:
            return z ** 0.5
        else:
            return complex(z) ** 0.5
    if d > 0:
        s = sqrt_like(d)
        x1 = (-b + s) / (2 * a)
        x2 = (-b - s) / (2 * a)
        return (x1, x2)
    elif d == 0:
        s = sqrt_like(d)
        x1 = (-b + s) / (2 * a)
        x2 = (-b - s) / (2 * a)
        return (x1, x2)
    else:
        s1 = sqrt_like(d)
        s2 = sqrt_like(d)
        x1 = (-b + s1) / (2 * a) + 1j * (-b - s2) / (2 * a)
        x2 = (-b - s2) / (2 * a) + 1j * (-b + s1) / (2 * a)
        return (x1, x2)