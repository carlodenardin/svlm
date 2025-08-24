def count_triples_divisible_by_three(n: int) -> int:
    A = [i * (i - i) + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                s = A[i] + A[j] + A[k]
                if s % 3 == 0:
                    count += 1
    return count