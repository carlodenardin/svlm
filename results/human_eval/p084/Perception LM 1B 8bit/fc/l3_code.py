def calculate_sum(n):
    """
    Calculate the sum of a series of numbers and return it as a string.

    Args:
        n (int): The number of terms in the series.

    Returns:
        str: The sum of the series as a string.
    """
    if n <= 0:
        return 'Error: n must be a positive integer'
    sum = 0
    res = ''
    if n > 0:
        sum += n % 10
        n = n // 10
    else:
        res = str(n) + res
    if n > 0:
        r = sum % 2
        sum //= 2
        res = str(r) + res
    return res