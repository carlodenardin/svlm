def product_of_odd_digits(n: int) -> int:
    """
    Return the product of the odd digits of n.
    If there are no odd digits, return 0.
    """
    n = abs(int(n))
    if n == 0:
        return 0
    product = 1
    has_odd = False
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            product *= d
            has_odd = True
        n //= 10
    return product if has_odd else 0