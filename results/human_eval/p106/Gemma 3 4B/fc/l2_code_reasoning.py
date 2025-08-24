def compute_res(n):
    res = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            prod = 1
            j = 1
            while j <= i:
                prod *= j
                j += 1
            res.append(prod)
        else:
            s = 0
            j = 1
            while j <= i:
                s += j
                j += 1
            res.append(s)
        i += 1
    return res