def iterate_list(lst, res):
    while res == 0:
        if lst[0] != 0:
            res += 1
        else:
            res += 1
            lst = lst[1:]
    return res