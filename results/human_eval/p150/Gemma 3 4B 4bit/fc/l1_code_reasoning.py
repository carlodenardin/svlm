def is_prime_with_range(n, x, y):
    """
    Implements the described algorithm:
    1) Prime check for n.
    2) If n is prime, loop through values from x to y (inclusive) and check divisibility.
       If any value in that range divides n, return False (not prime).
    3) If no divisors in the range are found, return True (prime).
    """
    if n <= 1:
        return False
    limit = int(n ** 0.5)
    for d in range(2, limit + 1):
        if n % d == 0:
            return False
    for divisor in range(x, y + 1):
        if divisor == 0:
            continue
        if n % divisor == 0:
            return False
    return True