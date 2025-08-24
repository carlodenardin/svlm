def is_balanced(strings):
    """
    Checks if a list of strings is balanced.

    A balanced list means that every '(' has a matching ')', and closures never exceed openings in order.

    Args:
        strings: A list of strings.

    Returns:
        True if the list is balanced, False otherwise.
    """
    if not strings:
        return False
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