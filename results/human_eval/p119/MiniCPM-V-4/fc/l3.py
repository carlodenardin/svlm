def match_parens(lst):
    if len(lst) != 2:
        return 'No'
    s1, s2 = lst
    i = 0
    c = 0
    while i < len(s1) and c < len(s2):
        if s1[i] == '(':
            c += 1
        elif s1[i] == ')':
            c -= 1
        i += 1
    if c == 0:
        return 'Yes'
    else:
        return 'No'