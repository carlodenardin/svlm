def convert_to_binary(n):
    if n == 0:
        return '0'
    total = 0
    temp = n
    while temp > 0:
        total += temp % 10
        temp //= 10
    if total == 0:
        return '0'
    binary_parts = []
    t = total
    while t > 0:
        digit = t % 10
        binary_parts.append(bin(digit)[2:])
        t //= 10
    return ''.join(reversed(binary_parts))