def count_triples(n):
    """
    Counts the number of triples in a vector of size n such that the sum of the triple is a multiple of 3.

    Args:
        n: An integer representing the size of the vector.

    Returns:
        The number of triples whose sum is a multiple of 3.
    """
    A = [i * i + i for i in range(1, n + 1)]
    counter = 0
    for i in range(n - 2):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                triple_sum = A[i] + A[j] + A[k]
                if triple_sum % 3 == 0:
                    counter += 1
    return counter