def is_balanced(strings):
    """
    Checks if a list of strings is balanced.

    A balanced string is one where every opening parenthesis has a matching closing parenthesis,
    and closures never exceed openings in order.

    Args:
        strings: A list of strings.

    Returns:
        True if the strings are balanced, False otherwise.
    """
    concatenated_string = ''.join(strings)
    open_count = 0
    for char in concatenated_string:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
        if open_count < 0:
            return False
    return open_count == 0