def solve(n, x, y):
    """
    This function implements the algorithm described in the flowchart.

    Args:
        n: An integer.
        x: An integer.
        y: An integer.

    Returns:
        An integer.
    """
    if n == 1:
        return y
    i = 2
    while i <= int(n ** 0.5):
        if n % i == 0:
            return y
        i += 1
    return x