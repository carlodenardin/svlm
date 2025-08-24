def product_of_odd_digits(n):
    n = abs(n)
    product = 1
    has_odd = False
    for digit in str(n):
        d = int(digit)
        if d % 2 == 1:
            product *= d
            has_odd = True
    return product if has_odd else 0