def compute_value(n, x, y):
    if n == 1:
        return y
    i = 2
    import math
    sqrt_n = math.sqrt(n)
    while True:
        if sqrt_n <= i:
            return x
        if n % i == 0:
            return y
        i += 1