def flowchart_algorithm(n):
    A = [2 * i + 1 for i in range(n)]
    counter = 0
    for i in range(n):
        j = i + 1
        for j in range(i + 1, n):
            k = j + 1
            for k in range(j + 1, n):
                if A[i] <= 3:
                    counter += A[i] * A[i]
                if A[j] <= 3:
                    counter += A[j] * A[j]
                if A[k] <= 3:
                    counter += A[k] * A[k]
    return counter