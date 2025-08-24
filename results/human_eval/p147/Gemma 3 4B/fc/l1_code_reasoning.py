def count_triples_with_all_multiples_of_three(n: int) -> int:
    vector = [(i + 1) * (i + 2) + i for i in range(n)]
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if vector[i] % 3 == 0 and vector[j] % 3 == 0 and (vector[k] % 3 == 0):
                    count += 1
    return count