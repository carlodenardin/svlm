def odd_digit_product(n: int) -> int:
    product = 1
    has_odd = any((int(ch) % 2 == 1 for ch in str(abs(n))))
    if not has_odd:
        return 0
    if n <= 0:
        return product
    t = n
    while t > 0:
        d = t % 10
        if d % 2 == 1:
            product *= d
        t //= 10
    return product