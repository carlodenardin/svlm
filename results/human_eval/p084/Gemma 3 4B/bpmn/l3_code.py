def calculate_result(n):
    """
    Calculates a result based on the input integer n.

    Args:
        n: An integer.

    Returns:
        The calculated result.
    """
    sum_val = 0
    res = 0
    while n > 0:
        sum_val += n % 10
        n = n // 10
        if sum_val > 0:
            r = sum_val % 2
            sum_val = sum_val // 10
            res += str(r)
    return res