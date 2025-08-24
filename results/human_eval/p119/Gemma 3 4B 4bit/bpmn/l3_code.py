def check_string(list_of_strings, s):
    """
    Checks if the string s is a substring of any of the strings in the list_of_strings.

    Args:
        list_of_strings: A list of strings.
        s: The string to check if it is a substring.

    Returns:
        True if s is a substring of any string in the list, False otherwise.
    """
    i = 0
    c = 0
    for string in list_of_strings:
        if s in string:
            return True
    return False