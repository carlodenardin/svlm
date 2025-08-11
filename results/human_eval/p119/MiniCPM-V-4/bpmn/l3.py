def match_parens(lst):
    s1, s2 = lst
    check_string(s1)
    check_string(s2)
    return 'Yes' if c1 or c2 else 'No'

def check_string(s):
    i = c = 0
    while i < len(s):
        if s[i] == '(':
            c += 1
        elif s[i] == ')':
            c -= 1
        if c < 0:
            return False
        i += 1
    return c == 0