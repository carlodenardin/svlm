import math

def algorithm(n: int, x: int, y: int) -> int:
    if n == 1:
        return y
    i = 2
    while i <= math.isqrt(n):
        if n % i == 0:
            return y
        i += 1
    return x