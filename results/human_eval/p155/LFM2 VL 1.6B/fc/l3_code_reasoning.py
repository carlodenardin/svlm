def compute_sum(n: int) -> int:
    total = 0
    if n % 2 == 0:
        for i in range(1, n // 2 + 1):
            total += i
    else:
        for i in range(n // 2 + 1, n + 1):
            total += i
    return total