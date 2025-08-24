def generate_res(n: int):
    res = []
    i = 1
    j = 1
    x = 0
    while i <= n:
        if i % 2 == 0:
            x = 1
            j += 1
        elif j <= i:
            res.append(x)
            x = x + j
            j += 1
            i += 1
        else:
            x = x * j
            j += 1
        i += 1
    return res