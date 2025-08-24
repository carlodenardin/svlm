def check_strings(s1, s2):
    c1 = check_string(s1)
    c2 = check_string(s2)
    if c1 or c2:
        return 'Yes'
    else:
        return 'No'