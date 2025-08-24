def count_distinct_triplets(A):
    triplets = []
    n = len(A)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                triplets.append((A[i], A[j], A[k]))
    m = len(triplets)
    count = 0
    for p in range(m):
        t = triplets[p]
        is_distinct = True
        for q in range(m):
            if p == q:
                continue
            if triplets[q] == t:
                is_distinct = False
                break
        if is_distinct:
            count += 1
    return count