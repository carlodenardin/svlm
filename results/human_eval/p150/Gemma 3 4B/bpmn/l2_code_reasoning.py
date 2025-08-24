import math

def algorithm(n: int, x: int, y: int) -> int:
    if n == 1:
        return y
    limit = int(math.isqrt(n))
    for d in range(2, limit + 1):
        if n % d == 0:
            return y
    return x