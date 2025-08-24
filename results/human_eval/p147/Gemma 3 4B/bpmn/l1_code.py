def count_triples_multiple_of_3(n):
    """
    Counts the number of distinct triples (i, j, k) such that 1 <= i, j, k <= n
    and the sum i + j + k is a multiple of 3.

    Args:
        n: An integer.

    Returns:
        The number of distinct triples (i, j, k) such that 1 <= i, j, k <= n
        and the sum i + j + k is a multiple of 3.
    """
    A = [0] * n
    for i in range(1, n + 1):
        A[i - 1] = i * i - i + 1
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    count += 1
    return count