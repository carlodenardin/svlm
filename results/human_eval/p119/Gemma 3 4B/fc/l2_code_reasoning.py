def check_string(s):
    s1 = 0  # count of opening parentheses
    s2 = 0  # count of closing parentheses
    for ch in s:
        if ch == '(':
            s1 += 1
        elif ch == ')':
            s2 += 1
        if s1 > s2:
            return False
    return s1 == s2

def is_balanced_vlm(s):
    # The described initialization requires at least three characters
    if not isinstance(s, str) or len(s) < 3:
        return 'No'
    s1 = len(s[0]) + len(s[1])
    s2 = len(s[1]) + len(s[2])
    if s1 == s2:
        result = check_string(s)
        return 'Yes' if result else 'No'
    else:
        return 'No'