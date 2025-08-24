def check_string(s):
    """
    Checks if the first and last characters of a string are the same.

    Args:
        s: The input string.

    Returns:
        True if the first and last characters are the same, False otherwise.
    """
    if len(s) == 0:
        return False
    s1 = s[0]
    s2 = s[-1]
    c1 = check_string(s1)
    c2 = check_string(s2)
    if c1 or c2:
        return True
    else:
        return False