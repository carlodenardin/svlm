def process_numbers(n: int):
    res = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            prod = 1
            for x in range(1, i + 1):
                prod *= x
            res.append(prod)
        else:
            total = 0
            for x in range(1, i + 1):
                total += x
            res.append(total)
        i += 1
    return res