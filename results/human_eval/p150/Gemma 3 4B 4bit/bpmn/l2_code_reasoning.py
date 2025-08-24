def coprime_flow(n, x, y):
    """
    Implements the described flow:
    - If n == 1: return y
    - Else, check for any divisor of n in [2, sqrt(n)]
      If found: return y
      If none found: return x
    """
    if n == 1:
        return y
    limit = int(n ** 0.5)
    for d in range(2, limit + 1):
        if n % d == 0:
            return y
    return x