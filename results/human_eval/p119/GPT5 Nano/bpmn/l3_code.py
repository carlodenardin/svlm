def check_string(s):
    i = 0
    c = 0
    while i < len(s):
        if s[i] == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
        i += 1
    return c == 0

def check_concatenation(lst):
    s1, s2 = lst
    comb1 = s1 + s2
    comb2 = s2 + s1
    c1 = check_string(comb1)
    c2 = check_string(comb2)
    if c1 or c2:
        return 'Yes'
    else:
        return 'No'