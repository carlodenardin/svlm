def algorithm(n: int) -> list[int]:
    res = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            x, j = (0, 1)
            while j <= i:
                x = x + j
                j = j + 1
            res = res + [x]
        else:
            x, j = (1, 1)
            while j <= i:
                x = x * j
                j = j + 1
            res = res + [x]
        i = i + 1
    return res