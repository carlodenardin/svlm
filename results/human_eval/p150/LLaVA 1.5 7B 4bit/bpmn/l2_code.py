def find_divisor():
    if n // 2 == 0:
        return n
    else:
        return find_divisor(n // 2)