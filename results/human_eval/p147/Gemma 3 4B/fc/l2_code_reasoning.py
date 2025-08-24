def count_triples_of_ones(n):
    """
    Counts the number of triples (i, j, k) with 1 <= i < j < k <= n
    such that vector[i], vector[j], vector[k] are all equal to 1.
    The vector is initialized with all ones. Implements the described
    nested loops inside a while loop (executed once).
    """
    vector = [1] * n
    count = 0
    while True:
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                for k in range(j + 1, n + 1):
                    if vector[i - 1] == 1 and vector[j - 1] == 1 and (vector[k - 1] == 1):
                        count += 1
        break
    return count