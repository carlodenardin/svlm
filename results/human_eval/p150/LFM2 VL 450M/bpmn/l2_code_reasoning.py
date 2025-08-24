def is_divisible_with_divisor_condition(n, y):
    if y == 0:
        return False
    if n % y != 0:
        return False
    divisor_found = False
    for d in range(2, n):
        if n % d == 0:
            divisor_found = True
            break
    if not divisor_found:
        return False
    return True