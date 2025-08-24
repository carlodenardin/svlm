def odd_digit_product(n):
    """
    Calculates the product of odd digits in an integer.

    Args:
        n: An integer.

    Returns:
        The product of odd digits in n. If n has no odd digits, returns 0.
    """
    product = 1
    if n < 0:
        n = abs(n)
    if n == 0:
        return 0
    if not any((int(digit) % 2 != 0 for digit in str(n))):
        return 0
    while n > 0:
        d = n % 10
        if d % 2 != 0:
            product *= d
        n //= 10
    return product