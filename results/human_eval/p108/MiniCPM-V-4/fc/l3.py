def count_nums(arr):
    res = 0
    i = 0
    digits = []
    isNeg = 1
    while i < len(arr):
        n = arr[i]
        digits.append(n % 10)
        n = n // 10
        if digits[-1] != isNeg:
            sum(digits) > 0
            res += 1
        if n < 0:
            isNeg = -1
            n = abs(n)
        i += 1
    return res