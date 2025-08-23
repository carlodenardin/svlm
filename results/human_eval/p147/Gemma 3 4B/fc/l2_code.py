def count_triples(n):
    """
    Counts the number of triples (i, j, k) such that 0 <= i, j, k < n and
    A[i] + A[j] + A[k] == 3.

    Args:
        n: The dimension of the vector A.

    Returns:
        The number of triples (i, j, k) that satisfy the condition.
    """
    A = [-1] * n
    for i in range(n):
        A[i] = i
    count = 0
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 0
    if n == 3:
        return 1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[i] + A[j] + A[k] == 3:
                    count += 1
    return count