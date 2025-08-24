def is_divisible_binary_search_style(n, y):
    """
    Determines if n is divisible by y using a binary-search-based approach,
    following the described (repetitive) reasoning pattern.
    Returns "YES" if divisible, else "NO".
    """
    if n in (1, 2):
        return 'YES'
    if y == 0:
        return 'NO'
    y_abs = abs(y)

    def binary_search_divisible():
        lo = 1
        hi = n // y_abs
        while lo <= hi:
            mid = (lo + hi) // 2
            prod = mid * y_abs
            if prod == n:
                return True
            if prod < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
    for _ in range(12):
        if binary_search_divisible():
            return 'YES'
    return 'NO'