def count_triplets(n):
    A = [i * i - i + 1 for i in range(1, n + 1)]
    counter = 0
    i = 0
    while i < len(A):
        j = i + 1
        while j < len(A):
            k = j + 1
            while k < len(A):
                if (A[i] - A[j] - A[k]) % 3 == 0:
                    counter += 1
                k += 1
            j += 1
        i += 1
    return counter

print(count_triplets(20))