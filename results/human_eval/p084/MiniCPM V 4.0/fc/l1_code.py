def int_to_binary(n: int) -> str:
    if n == 0:
        return '0'
    negative = n < 0
    if negative:
        n = -n
    binary = ''
    while n > 0:
        remainder = n % 2
        binary += str(remainder)
        n = n // 2
    binary = binary[::-1]
    return '-' + binary if negative else binary