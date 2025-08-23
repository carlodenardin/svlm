def check_string(s):
    """
    Checks if two strings are anagrams of each other.

    Args:
        s: The input string.

    Returns:
        True if the string is an anagram, False otherwise.
    """
    len_s = len(s)
    s1 = s[0] + s[len_s - 1]
    s2 = s[1] + s[len_s - 2]
    c1 = check_string(s1)
    c2 = check_string(s2)
    if c1 or c2:
        return True
    else:
        return False