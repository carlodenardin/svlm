def is_any_string_balanced(strings):
    """
    Determine whether any string in the input array has balanced parentheses.
    A string is balanced if parentheses are properly matched.
    """
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0
    c = 0

    def is_balanced_parentheses(s):
        balance = 0
        for ch in s:
            if ch == '(':
                balance += 1
            elif ch == ')':
                balance -= 1
                if balance < 0:
                    return False
        return balance == 0
    for s in strings or []:
        if isinstance(s, str) and is_balanced_parentheses(s):
            return True
    return False