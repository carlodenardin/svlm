def final_sum_of_mixed_operations(n: int) -> int:
    """
    Generates a list of length n where:
      - for even i (1 <= i <= n): append factorial(i)
      - for odd i: append sum of 1..i
    Returns the sum of all elements in the list.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be a non-negative integer')
    import math
    results = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            results.append(math.factorial(i))
        else:
            results.append(i * (i + 1) // 2)
    return sum(results)