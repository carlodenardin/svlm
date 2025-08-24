def calculate_sum(arr):
    res = 0
    for num in arr:
        digits = [int(digit) for digit in str(num)]
        if len(digits) > 0:
            res += sum(digits)
    return res