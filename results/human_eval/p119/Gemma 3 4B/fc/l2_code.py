def check_balanced_parentheses(s):
    """
    Checks if a string composed of rounded parentheses is balanced.

    Args:
        s: The input string.

    Returns:
        True if the string is balanced, False otherwise.
    """
    s1 = [0] + [0] * (len(s) - 1)
    s2 = [0] + [0] * (len(s) - 1)
    for i in range(len(s)):
        if s[i] == '(':
            s1[i] += 1
        elif s[i] == ')':
            s1[i] -= 1
        if s1[i] < 0:
            return False
    return True