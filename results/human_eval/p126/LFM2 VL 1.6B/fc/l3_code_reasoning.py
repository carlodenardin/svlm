def is_prime(i: int) -> bool:
    if i <= 1:
        return False
    for d in range(2, i):
        if i % d == 0:
            return False
    if i % (i + 1) == 0:
        return False
    if i % (i + 2) == 0:
        return False
    return True