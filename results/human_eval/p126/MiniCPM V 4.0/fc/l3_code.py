def check_list(l):
    i = 1
    while i < len(l):
        if l[i] < l[i - 1]:
            i += 1
        else:
            if i > 1 and l[i] == l[i - 1] == l[i - 2]:
                return False
            break
    return True