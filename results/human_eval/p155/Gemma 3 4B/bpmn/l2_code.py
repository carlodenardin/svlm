def count_even_odd(n):
    """
    Counts the number of even and odd digits in an integer.

    Args:
        n: An integer.

    Returns:
        A tuple (even, odd) where even is the count of even digits and odd is the count of odd digits.
    """
    even = 0
    odd = 0
    n_str = str(abs(n))
    for digit in n_str:
        digit = int(digit)
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)