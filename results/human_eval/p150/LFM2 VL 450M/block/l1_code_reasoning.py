def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    limit = int(n ** 0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True