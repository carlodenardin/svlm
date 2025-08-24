def count_even_odd_digits(n):
    """
    Counts the number of even and odd digits in an integer.

    Args:
        n: An integer.

    Returns:
        A tuple containing the number of even digits and the number of odd digits.
    """
    even_count = 0
    odd_count = 0
    n_str = str(abs(n))
    for digit in n_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)