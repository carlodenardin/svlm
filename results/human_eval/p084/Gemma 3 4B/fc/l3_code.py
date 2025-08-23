def algorithm(n):
    """
    Implements the algorithm described in the flowchart.

    Args:
        n: An integer.

    Returns:
        A string.
    """
    sum_val = 0
    res = ''
    while n > 0:
        sum_val += n % 10
        n = n // 10
        if sum_val > 0:
            r = sum_val % 2
            sum_val = sum_val // 2
            res += str(r)
    return res