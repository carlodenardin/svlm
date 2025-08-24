def count_distinct_indices(n):
    """
    Counts the number of distinct indices of a given range in a list.

    Args:
        n (int): The range of indices to count.

    Returns:
        int: The number of distinct indices.
    """
    count = 0
    for i in range(n):
        if i in range(n):
            count += 1
    return count