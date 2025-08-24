def primality_test(n: int) -> str:
    x = 0
    y = 0
    if n == 1:
        return 'no'
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 'no'
        i += 1
    return 'yes'