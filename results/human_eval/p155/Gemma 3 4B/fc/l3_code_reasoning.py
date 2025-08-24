def is_divisible_by_10(num: int) -> bool:
    """
    Implements the described digit-parity loop and then returns whether the original
    number is divisible by 10 (i.e., last decimal digit is 0).
    """
    even = 0
    odd = 0
    n = abs(int(num))
    while n > 0:
        d = n % 10
        if n > 0 and d % 2 == 0:
            even = 1
        else:
            odd = 1
        n = n // 10
    return abs(int(num)) % 10 == 0