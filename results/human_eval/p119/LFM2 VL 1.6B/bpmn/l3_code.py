def check_strings(strings):
    i = 0
    c = 0
    while i < len(strings):
        if strings[i] == '1':
            c += 1
        else:
            c = 0
        i += 1
    return True if c == 0 else False