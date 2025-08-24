def gcd(n, y):
    """
    Compute the greatest common divisor (GCD) of two integers n and y
    using the Euclidean algorithm as described.
    """
    a = int(n)
    b = int(y)
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = (b, a % b)
    return a