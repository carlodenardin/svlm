def compute_result(n: int) -> str:
    total = 0
    res = ''
    while n > 0:
        if n > 0:
            total += n % 10
            n = n // 10
        else:
            break
    if total > 0:
        r = total % 2
        total = total // 2
        res = str(r) + res
    return res