def compute_sum(n):
    if n == 1:
        return 1
    else:
        return n + compute_sum(n - 1)