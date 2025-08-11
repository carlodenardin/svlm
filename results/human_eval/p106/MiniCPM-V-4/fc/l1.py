def f(n):
    result = []
    counter = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(math.factorial(i))
        else:
            result.append(sum(range(1, i+1)))
            counter += 1
    return result