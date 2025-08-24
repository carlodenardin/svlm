def iterate(n, i=1):
    while i <= n:
        if i % 2 == 0:
            res = [x for x in [0, 1] if x % 2 == 0]
        else:
            res = [x for x in [1, 2] if x % 2 == 1]
        i += 1
    return res