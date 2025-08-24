def sum_of_distinct_indices(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        if arr[i] in range(1, n + 1):
            sum += 1
    return sum