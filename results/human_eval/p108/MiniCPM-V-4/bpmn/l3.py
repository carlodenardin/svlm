def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            sign = -1
        else:
            sign = 1
        digits = [int(digit) for digit in str(abs(num))]
        digits.reverse()
        sum_digits = sum(digits)
        if sign * sum_digits > 0:
            count += 1
    return count