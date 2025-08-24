def count_distinct_triples(n, m):
    """
    Counts the number of distinct triples (a, b, c) in a list of n elements where a <= b <= c
    and a + b + c = m.

    Args:
        n: The number of elements in the list.
        m: The sum of the triples.

    Returns:
        The number of distinct triples.
    """
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if i + j + k == m:
                    count += 1
    return count