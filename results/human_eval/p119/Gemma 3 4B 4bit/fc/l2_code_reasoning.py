def check_string(s):
    s1 = len(s[0]) + 0
    s2 = len(s[0]) + 0
    if s1 != s2:
        return 'No'
    for ch in s:
        if ch == '(':
            s1 += 1
        elif ch == ')':
            s2 += 1
        if s1 != s2:
            return 'No'
    if s1 == s2:
        return 'Yes'
    else:
        return 'No'