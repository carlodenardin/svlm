def running_digit_sum(nums):
    res = 0
    i = 0
    while i < len(nums):
        n = nums[i]
        digits = []
        isNeg = 1
        if n < 0:
            isNeg = -1
            n = abs(n)
        while n > 0:
            digits.append(n % 10)
            n //= 10
        sum_digits = sum(digits)
        res += isNeg * sum_digits
        i += 1
    return res