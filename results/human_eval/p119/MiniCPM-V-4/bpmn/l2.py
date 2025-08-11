def match_parens(lst):
    if len(lst) != 2:
        return 'No'
    s1, s2 = lst
    c1, c2 = check_string(s1), check_string(s2)
    if c1 or c2:
        return 'No'
    return 'Yes'