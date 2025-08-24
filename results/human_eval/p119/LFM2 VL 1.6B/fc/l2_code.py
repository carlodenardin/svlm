def check_balanced(strings):
    s1 = [0] + [1] + [1]
    s2 = [1] + [1] + [0]
    if check_string(s1):
        c1 = True
        c2 = False
    else:
        c1 = False
        c2 = True
    if check_string(s2):
        c1 = True
        c2 = False
    else:
        c1 = False
        c2 = True
    if c1 or c2:
        return 'End'
    else:
        return 'End'