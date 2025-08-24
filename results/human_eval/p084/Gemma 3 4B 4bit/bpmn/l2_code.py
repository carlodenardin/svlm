def sum_of_digits_to_binary(n: int) -> str:
    total = 0
    res = ''
    temp = int(n)
    while temp > 0:
        total += temp % 10
        temp //= 10
    if total == 0:
        res = '0'
    else:
        bits = []
        t = total
        while t > 0:
            bits.append(str(t % 2))
            t //= 2
        bits.reverse()
        res = ''.join(bits)
    return res