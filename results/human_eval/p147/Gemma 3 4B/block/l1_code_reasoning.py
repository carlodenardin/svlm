import sys

def count_triples_divisible_by_3(n: int) -> int:
    A = [i + 2 for i in range(n)]
    seen = set()
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                s = A[i] + A[j] + A[k]
                if s % 3 == 0:
                    triple = (A[i], A[j], A[k])
                    if triple not in seen:
                        seen.add(triple)
                        count += 1
    return count