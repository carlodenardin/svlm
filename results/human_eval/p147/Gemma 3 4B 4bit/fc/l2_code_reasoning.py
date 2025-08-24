def count_increasing_triples(n, A):
    A = [0] * n
    for i in range(n):
        A[i] = i + 1
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if A[i] < A[j] and A[j] < A[k]:
                    count += 1
    return count