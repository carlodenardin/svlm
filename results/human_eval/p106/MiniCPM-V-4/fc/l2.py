def f(n):
    res = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            res.append(math.factorial(i))
        else:
            res.append(sum(range(1, i+1)))
        i += 1
    return res