def algorithm(n):
    result = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            x = 1
            j = 1
            while j <= i:
                x *= j
                j += 1
        else:
            x = 0
            j = 1
            while j <= i:
                x += j
                j += 1
        result.append(x)
        i += 1
    return result