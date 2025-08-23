def is_balanced(strings):
    """
    Checks if a list of strings is balanced, meaning that every opening
    "(" has a matching closing ")" and closures never exceed openings
    in order.

    Args:
        strings: A list of strings, where each string is either an opening
                 "(" or a closing ")".

    Returns:
        True if the list is balanced, False otherwise.
    """
    balance = 0
    for s in strings:
        if s == '(':
            balance += 1
        elif s == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0