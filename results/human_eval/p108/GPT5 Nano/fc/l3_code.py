def process_array(arr: list[int]) -> int:
    res = 0
    i = 0
    while i < len(arr):
        n = arr[i]
        digits = []
        isNeg = 1
        if n < 0:
            isNeg = -1
        else:
            n = abs(n)
        while n > 0:
            digits.append(n % 10)
            n = n // 10
        if digits:
            digits[-1] *= isNeg
        if sum(digits) > 0:
            res += 1
        i += 1
    return res