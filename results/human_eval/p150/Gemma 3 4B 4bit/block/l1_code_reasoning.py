def prime_output(n, x, y):
    if n < 2:
        return y
    limit = int(n ** 0.5)
    i = 2
    while i <= limit:
        if n % i == 0:
            return y
        i += 1
    return x