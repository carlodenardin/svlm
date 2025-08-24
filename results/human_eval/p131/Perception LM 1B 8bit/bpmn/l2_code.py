def odd_digits(n):
    if n % 2 == 0:
        return 0
    else:
        return n * (n // 2)