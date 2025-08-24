def is_balanced_pair(strings):
    """
    Determine if the concatenation of two strings of '(' and ')' is balanced.
    Returns "Yes" if balanced, "No" otherwise.
    """
    combined = strings[0] + strings[1]
    balance = 0
    for ch in combined:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
        else:
            continue
        if balance < 0:
            return 'No'
    return 'Yes' if balance == 0 else 'No'