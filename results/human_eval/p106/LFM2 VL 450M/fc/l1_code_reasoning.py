def solve():
    import sys
    data = sys.stdin.read().strip()
    if not data:
        return
    i = int(data)
    results = []
    if i % 2 == 0:
        prod = 1
        for k in range(1, i + 1):
            prod *= k
        results.append(prod)
    else:
        s = sum(range(1, i + 1))
        results.append(s)
    i += 1
    total = sum(results)
    print(total)