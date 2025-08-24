def sum_digits_to_binary(n: int) -> str:
    total = 0
    res = ''
    temp = n
    while temp > 0:
        total += temp % 10
        temp //= 10
    res = bin(total)[2:]
    return res