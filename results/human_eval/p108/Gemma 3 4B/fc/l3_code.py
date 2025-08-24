def count_trailing_zeros(arr):
    """
    Counts the number of trailing zeros in the integer array arr.

    Args:
        arr: A list of integers.

    Returns:
        The number of trailing zeros in the integer array.
    """
    res = 0
    i = 0
    while i < len(arr):
        n = arr[i]
        digits = []
        isNeg = False
        if n < 0:
            isNeg = -1
            n = abs(n)
        digits.append(n % 10)
        n = n // 10
        if n > 0:
            digits.append(n % 10)
            n = n // 10
        sum_digits = sum(digits)
        if sum_digits > 0:
            res += 1
        i += 1
    return res