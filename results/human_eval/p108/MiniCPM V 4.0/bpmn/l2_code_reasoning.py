def count_positive_signed_digit_sum(nums):
    res = 0
    i = 0
    while i < len(nums):
        n = nums[i]
        sign = 1 if n >= 0 else -1
        m = abs(n)
        digits_sum = 0
        if m == 0:
            digits_sum = 0
        else:
            while m > 0:
                digits_sum += m % 10
                m //= 10
        signed_sum = sign * digits_sum
        if signed_sum > 0:
            res += 1
        i += 1
    return res