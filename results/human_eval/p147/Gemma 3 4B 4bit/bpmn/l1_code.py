def count_triples_with_sum_3(n):
    """
    Counts the number of distinct triples (i, j, k) such that A[i] + A[j] + A[k] is divisible by 3,
    where i, j, and k are indices within the range [1, n].

    Args:
        n (int): The size of the vector A.

    Returns:
        int: The number of distinct triples with sum divisible by 3.
    """
    A = []
    for i in range(1, n + 1):
        A.append(i * i - i + 1)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    count += 1
    return count