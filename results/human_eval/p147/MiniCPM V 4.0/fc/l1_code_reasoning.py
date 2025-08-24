def count_triples_multiples_of_three(n: int) -> int:
    A = [0] * n
    for i in range(1, n + 1):
        A[i - 1] = i * i + i + 1
    count = 0
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    count += 1
    return count