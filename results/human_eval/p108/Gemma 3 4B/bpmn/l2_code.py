def count_positive_integers(numbers):
    """
    Counts the number of positive integers in a list.

    Args:
        numbers: A list of integers.

    Returns:
        The number of positive integers in the list.
    """
    res = 0
    for num in numbers:
        if num > 0:
            res += 1
    return res