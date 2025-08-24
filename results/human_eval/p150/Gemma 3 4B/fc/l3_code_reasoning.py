def is_prime_flow(n: int) -> bool:
    import math
    x = 0
    y = 0
    if n == 1:
        return False
    i = 2
    while i <= math.isqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True