def decimal_to_binary(n: int) -> str:
    """
    Converts a positive decimal integer to its binary representation following the specified algorithm.
    If n <= 0, returns an error string.
    """
    if n <= 0:
        return 'Invalid input. Please enter a positive integer.'
    total = 0
    res = ''
    temp = n
    while temp > 0:
        total += temp % 10
        temp //= 10
    while total > 0:
        remainder = total % 2
        res += str(remainder)
        total //= 2
    binary_str = res[::-1]
    return binary_str