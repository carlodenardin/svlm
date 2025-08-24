def sum_of_digits_positive_flag(arr):
    res = 0
    has_iterated = False
    while not has_iterated:
        if not arr:
            break
        value = arr[0]
        digits = []
        temp = abs(value)
        if temp == 0:
            digits = [0]
        else:
            while temp > 0:
                digits.append(temp % 10)
                temp //= 10
        digits_sum = sum(digits)
        if digits_sum > 0:
            res = 1
        has_iterated = True
    return res