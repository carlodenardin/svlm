def odd_digit(n):
    if n % 10 != 0:
        return n
    else:
        return n // 10 + 1