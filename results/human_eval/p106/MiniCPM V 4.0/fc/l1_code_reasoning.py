def compute_final_result(n: int):
    results = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            prod = 1
            for k in range(1, i + 1):
                prod *= k
            results.append(prod)
        else:
            s = i * (i + 1) // 2
            results.append(s)
        i += 1
    return results[-1] if results else 0