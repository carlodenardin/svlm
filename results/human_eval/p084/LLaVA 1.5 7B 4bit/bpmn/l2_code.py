def decimal_to_binary(n: int) -> str:
    """
    Convert a non-negative integer n to its binary representation as a string.
    Follows a loop-based approach:
    - Accumulate binary digits by repeatedly taking n % 2 while halving n.
    - If n is 0, return "0".
    """
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 0:
        raise ValueError('n must be non-negative')
    binary_reversed = ''
    if n == 0:
        return '0'
    while n > 0:
        binary_reversed += str(n % 2)
        n //= 2
    binary = binary_reversed[::-1]
    return binary