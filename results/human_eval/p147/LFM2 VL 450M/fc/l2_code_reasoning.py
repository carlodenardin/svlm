def count_triplets_equal_k(n):
    rule = [0] * (n + 1)
    total_count = 0
    eq_count = 0
    non_eq_count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for k in range(1, n + 1):
                if a == b and a == k:
                    total_count += 1
                if a == k:
                    eq_count += 1
                if a != k:
                    non_eq_count += 1
    return eq_count