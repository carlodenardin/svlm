def factor_like(n):
    res = []
    i = 1
    while i < n:
        x = 0
        if i % 2 == 0:
            x = 1
            j = 0
            while j < i:
                x = x + j
                j += 1
        if x == n:
            res.append(i)
        i += 1
    return res