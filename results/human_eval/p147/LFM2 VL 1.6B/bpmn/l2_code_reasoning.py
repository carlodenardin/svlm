def gcd_steps(a, b):
    """
    Compute the number of iterations of the Euclidean algorithm
    (using a, b = b, a % b) needed to reach a remainder of 0.
    Returns the count of iterations.
    """
    a, b = (abs(int(a)), abs(int(b)))
    count = 0
    while b != 0:
        count += 1
        a, b = (b, a % b)
    return count