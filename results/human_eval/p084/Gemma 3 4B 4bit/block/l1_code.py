def vlm_to_binary(n: int) -> str:
    sum_digits = 0
    result = ''
    while n > 0:
        remainder = n % 10
        sum_digits += remainder
        n //= 10
        result += str(remainder)
    s = sum_digits
    while s >= 10:
        inner_sum = 0
        t = s
        while t > 0:
            inner_sum += t % 10
            t //= 10
        s = inner_sum
    if s == 0:
        return '0'
    bits = []
    while s > 0:
        bits.append(str(s % 2))
        s //= 2
    bits.reverse()
    return ''.join(bits)