def count_triples(n: int) -> int:
    A = [0] + [i * i + i for i in range(1, n + 1)]
    counter = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    counter += 1
    return counter