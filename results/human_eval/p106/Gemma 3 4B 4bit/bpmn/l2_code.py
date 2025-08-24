def factorial_sum(n):
    """
    Calculates the sum of factorials of numbers from 1 to n.

    Args:
        n: An integer representing the upper limit of the range.

    Returns:
        A list containing the sum of factorials and the factorials themselves.
    """
    result = []
    i = 1
    while i <= n:
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        result.append(factorial)
        result.append(i)
        i += 1
    return result