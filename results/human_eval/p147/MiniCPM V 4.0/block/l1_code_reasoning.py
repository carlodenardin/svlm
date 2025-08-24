def count_triplets_sum_multiple_of_3(n):
    """
    Generate A where A[i-1] = i*i - i + 1 for i in 1..n,
    then count distinct triplets (i, j, k) with i < j < k
    such that (A[i] + A[j] + A[k]) is divisible by 3.
    """
    if n < 3:
        return 0
    A = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    count += 1
    return count