def sum_digits_to_binary(n: int) -> str:
    sum = 0
    res = ''
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    res = bin(sum)[2:]
    return res