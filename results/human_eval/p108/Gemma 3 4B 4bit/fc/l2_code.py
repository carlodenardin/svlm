def has_sum_of_digits_greater_than_zero(arr):
    """
    Checks if the sum of the digits of an array is greater than zero.

    Args:
        arr: A list of integers.

    Returns:
        True if the sum of the digits is greater than zero, False otherwise.
    """
    res = 0
    has_been_fully_iterated = False
    while not has_been_fully_iterated:
        if not arr:
            break
        digits = [int(d) for d in str(arr[0])]
        sum_of_digits = sum(digits)
        if sum_of_digits > 0:
            res = 1
            has_been_fully_iterated = True
        else:
            arr.pop(0)
    return res