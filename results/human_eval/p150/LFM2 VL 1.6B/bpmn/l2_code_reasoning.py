def find_divisor(n, range_start, range_end):
    if not isinstance(n, int) or n <= 0:
        return None
    if range_start < 2:
        range_start = 2
    for i in range(range_start, range_end):
        if n % i == 0:
            return i
    return None