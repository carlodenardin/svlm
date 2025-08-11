def count_nums(arr):
    res = 0
    for num in arr:
        if num < 0:
            num = abs(num)
        digit_sum = sum(int(digit) for digit in str(abs(num)))
        if digit_sum > 0:
            res += 1
    return res