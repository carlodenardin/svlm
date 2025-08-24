def generate_res(n):
    res = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            x = 0
            j = 1
        else:
            x = 1
            j = 1
        if j <= i:
            x = x + j
            j = j + 1
        else:
            x = x * j
            j = j + 1
        res.append(x)
        i = i + 1
    return res