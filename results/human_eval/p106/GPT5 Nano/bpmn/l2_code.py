def process_integer(n):
    result = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            result.append(factorial)
        else:
            total = sum(range(1, i + 1))
            result.append(total)
        i += 1
    return result