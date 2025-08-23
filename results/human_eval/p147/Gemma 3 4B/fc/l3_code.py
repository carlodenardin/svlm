def count_occurrences(n):
    """
    Counts the number of occurrences of a substring within a string.

    Args:
        n: The string to search within.

    Returns:
        The number of occurrences of the substring.
    """
    a = n[0]
    count = 0
    i = 0
    len_a = len(a)
    j = 0
    k = 0
    while i < len_a:
        if i == len_a - 1:
            if a[i] == a[0]:
                count = 1
            break
        if a[i] == a[i + 1]:
            j += 1
        elif j > 0:
            k = j
            if k < len_a:
                if n[i - k + 1:i + 1] == a:
                    count += 1
            j = 0
        else:
            j = 0
        i += 1
    return count