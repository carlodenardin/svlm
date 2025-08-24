def sum_digits_to_binary(num):
    sum = 0
    res = ''
    while num > 0:
        last_digit = num % 10
        sum += last_digit
        num = num // 10
    res = bin(sum)[2:]
    return res