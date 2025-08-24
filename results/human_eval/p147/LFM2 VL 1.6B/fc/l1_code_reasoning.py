def count_distinct_triplets(values):
    if not values:
        return 0
    count = 0
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if values[i] != values[j] and values[i] != values[k] and (values[j] != values[k]):
                    count += 1
    return count