def int_to_binary_from_digit_sum(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 0:
        raise ValueError('n must be non-negative')
    digit_sum = sum((int(ch) for ch in str(n)))
    if digit_sum == 0:
        return '0'
    bits = []
    value = digit_sum
    while value > 0:
        bits.append('1' if value & 1 else '0')
        value >>= 1
    bits.reverse()
    return ''.join(bits)