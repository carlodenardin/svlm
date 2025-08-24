def count_triples(n):
    """
    Counts the number of triples (i, j, k) such that 0 <= i, j, k < n and A[i] + A[j] + A[k] == 3.

    Args:
        n: The dimension of the vector A.

    Returns:
        The number of triples (i, j, k) that satisfy the condition.
    """
    A = [i for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[i] + A[j] + A[k] == 3:
                    count += 1
    return count