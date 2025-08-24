def sum_digits_to_binary_string(n: int) -> str:
    total = 0
    for ch in str(abs(n)):
        if ch.isdigit():
            total += int(ch)
    if total == 0:
        return '0'
    bits = []
    t = total
    while t > 0:
        bits.append(str(t % 2))
        t //= 2
    bits.reverse()
    return ''.join(bits)