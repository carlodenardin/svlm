def f(n):
    res = []
    for i in range(1, n+1):
        if i % 2 == 0:
            res.append(math.factorial(i))
        else:
            x = 0
            j = 1
            while j <= i:
                x += j
                j += 1
            res.append(x)
    return res