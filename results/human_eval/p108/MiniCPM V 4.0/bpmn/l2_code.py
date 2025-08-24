def calculate_sum_of_signed_digits(integers):
    res = 0
    for num in integers:
        if num < 0:
            num = -num
        sign_sum = sum((int(digit) for digit in str(abs(num))))
        if sign_sum > 0:
            res += 1
    return res