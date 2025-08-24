def lucas_series(n):
    if n <= 0:
        return []
    result = [0] * n
    i = 1
    j = 0
    t = 0
    while i <= n:
        if i % 2 == 0:
            x = 1
        else:
            x = 0
        j += 1
        if j <= i:
            result[t] = x
            t += 1
            i += 1
        else:
            pass
    return result