def product_of_odd_digits(n: int) -> int:
    has_odd = False
    product = 1
    for digit in str(abs(n)):
        d = int(digit)
        if d % 2 == 1:
            has_odd = True
            product *= d
    if not has_odd:
        return 0
    return product