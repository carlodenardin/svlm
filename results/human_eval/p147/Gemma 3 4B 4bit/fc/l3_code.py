def count_distinct_characters(s):
    """
    Counts the number of distinct characters in a string.

    Args:
        s: The input string.

    Returns:
        The number of distinct characters in the string.
    """
    n = len(s)
    i = 1
    count = 0
    if i <= n:
        count = 0
        i = 0
        while i < len(s):
            j = i + 1
            k = i + 1
            while k < len(s):
                if s[i] != s[k]:
                    k += 1
                else:
                    break
            if k < len(s):
                count += 1
            i += 1
            j += 1
    return count