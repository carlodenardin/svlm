def product_of_odd_digits(n: int) -> int:
    product = 1
    temp = n
    has_odd = False
    while temp > 0:
        d = temp % 10
        if d % 2 == 1:
            has_odd = True
            break
        temp //= 10
    if not has_odd:
        return 0
    if n <= 0:
        return product
    m = n
    while m > 0:
        d = m % 10
        if d % 2 == 1:
            product *= d
        m //= 10
    return product