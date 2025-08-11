def count_nums(arr):
    res = 0
    for num in arr:
        if num < 0:
            sum_digits = sum(int(digit) for digit in str(abs(num)))
        else:
            sum_digits = sum(int(digit) for digit in str(num))
        if sum_digits > 0:
            res += 1
    return res