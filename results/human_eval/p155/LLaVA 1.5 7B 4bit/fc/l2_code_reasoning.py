import math

def quadratic_newton_style_root(a, b, c, x0, tol=1e-09, max_iter=1000):
    """
    Implements a flowchart-inspired procedure to approximate a quadratic root.
    Follows these steps:
    - Compute f'(x) = 2*a*x + b at current x.
    - Compute f''(x) = 2*a (constant) to determine its sign.
    - If f'' > 0, update x to the midpoint between current x and a chosen root.
    - If f'' < 0, update x to the negation of that midpoint.
    - Repeat until convergence criteria are met.
    
    This function selects the root to use for the midpoint as the real root
    closest to the current x (between the two algebraic roots).
    """
    if a == 0:
        if b == 0:
            raise ValueError('Invalid equation: both a and b are zero.')
        return -c / b
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        raise ValueError('The quadratic has no real roots.')
    sqrt_discriminant = math.sqrt(discriminant)
    r1 = (-b - sqrt_discriminant) / (2 * a)
    r2 = (-b + sqrt_discriminant) / (2 * a)
    x = float(x0)
    two_a = 2.0 * a
    iterations = 0
    while iterations < max_iter:
        fprime = 2.0 * a * x + b
        fdouble = two_a
        if fdouble > 0:
            sign = 1
        elif fdouble < 0:
            sign = -1
        else:
            break
        root = r1 if abs(x - r1) <= abs(x - r2) else r2
        midpoint = (x + root) / 2.0
        if sign > 0:
            x = midpoint
        else:
            x = -midpoint
        iterations += 1
        fx = a * x * x + b * x + c
        if abs(fx) <= tol:
            break
        if abs(x - root) <= tol:
            break
    return x