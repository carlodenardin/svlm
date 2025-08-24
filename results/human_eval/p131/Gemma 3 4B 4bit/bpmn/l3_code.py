def odd_digit_product(n):
    """
    Calculates the product of odd digits in a given integer.

    Args:
        n (int): The integer to process.

    Returns:
        int: The product of odd digits in n. Returns 0 if n is 0 or has no odd digits.
    """
    product = 1
    if n == 0:
        return 0
    n_str = str(n)
    for digit in n_str:
        digit = int(digit)
        if digit % 2 != 0:
            product *= digit
    return product