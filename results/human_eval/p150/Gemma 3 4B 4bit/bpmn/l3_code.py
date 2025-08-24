def find_value(n, x, y):
    """
    Finds a value based on the input integers n, x, and y.

    Args:
        n: An integer.
        x: An integer.
        y: An integer.

    Returns:
        The value x if n is greater than 1 and the square root of n is less than or equal to x.
        The value y if n is equal to 1.
        The value y if n is divisible by i for any i from 2 to n.
    """
    if n == 1:
        return y
    i = 2
    while i <= n:
        if n <= n ** 0.5:
            return x
        if n % i == 0:
            return y
        i += 1
    return x