def count_triples(n):
    triples_count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i * i - i + 1 == j * j - j + 1 == k * k - k + 1:
                    triples_count += 1
    return triples_count % 3