def smallest_divisible_by_all_upto_n(n):
    dims = []
    i = 1
    n_minus_1 = max(0, n - 1)
    lst = [1] * n_minus_1
    for _ in range(n_minus_1):
        if all((i % d == 0 for d in range(1, n))):
            lst.append(i)
        else:
            for __ in range(n_minus_1):
                if all((i % d == 0 for d in range(1, n))):
                    lst.append(i)
            return lst
    return lst