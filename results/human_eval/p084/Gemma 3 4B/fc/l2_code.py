def sum_of_digits_to_binary(n: int) -> str:
    sum = 0
    if n < 0:
        n = -n
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10
    res = ''
    if sum == 0:
        res = '0'
    else:
        while sum > 0:
            res = str(sum % 2) + res
            sum //= 2
    return res