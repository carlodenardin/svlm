def count_digits_sum(arr):
    res = 0
    i = 0
    while i < len(arr):
        n = arr[i]
        digits = []
        isNeg = 1
        if n < 0:
            isNeg = -1
            n = abs(n)
        if n == 0:
            digits.append(0)
        else:
            while n > 0:
                digits.append(n % 10)
                n //= 10
        res += len(digits)
        i += 1
    return res