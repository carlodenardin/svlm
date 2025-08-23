def is_balanced(strings):
    """
    Checks if a list of strings is balanced, meaning that every opening parenthesis
    has a matching closing parenthesis and vice versa, and no openings exceed
    closures in order.

    Args:
        strings: A list of strings.

    Returns:
        True if the strings are balanced, False otherwise.
    """
    if not strings:
        return True
    combined_string = ''.join(strings)
    balance = 0
    for char in combined_string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0