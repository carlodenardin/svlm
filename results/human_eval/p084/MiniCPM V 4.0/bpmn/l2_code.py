def sum_of_digits_to_bin(number: int) -> str:
    sum = 0
    res = ''
    while number > 0:
        last_digit = number % 10
        sum += last_digit
        number = number // 10
    res = bin(sum)
    return res