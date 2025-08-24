def product_of_odd_digits(n):
    """
    Calculates the product of the odd digits of an integer.

    Args:
        n: An integer.

    Returns:
        The product of the odd digits of n. Returns 0 if no odd digits are present.
    """
    product = 1
    has_odd = False
    for digit in str(n):
        digit = int(digit)
        if digit % 2 != 0:
            product *= digit
            has_odd = True
    if not has_odd:
        return 0
    return product