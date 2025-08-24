def check_string(s):
    i = 0
    c = 0
    while i < len(s):
        if s[i] == '':
            c += 1
            i += 1
        else:
            c = 0
    return c

def check_string(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    c1 = check_string(s1)
    c2 = check_string(s2)
    return c1 == c2