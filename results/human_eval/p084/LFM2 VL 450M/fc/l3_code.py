def solve_with_zero(n, zero):
    total = n + zero
    if total > 0:
        res = total / n
    if total <= 0:
        return res
    return res