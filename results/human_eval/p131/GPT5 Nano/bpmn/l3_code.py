def product_of_odd_digits(n):
    has_odd = any((int(d) % 2 == 1 for d in str(abs(n))))
    if not has_odd:
        return 0
    product = 1
    n = abs(n)
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            product *= d
        n //= 10
    return product