def check_string_combination(strings, s):
    """
    Checks if a string 's' is a combination of the strings in a list 'strings'.

    Args:
        strings (list): A list of strings.
        s (str): The string to check.

    Returns:
        bool: True if 's' is a combination of the strings in 'strings', False otherwise.
    """
    for i in range(len(strings)):
        for j in range(len(strings)):
            combined_string = strings[i] + strings[j]
            if combined_string == s:
                c1 = len(strings[i])
                c2 = len(strings[j])
                return True
    return False