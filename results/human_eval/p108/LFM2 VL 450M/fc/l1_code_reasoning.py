def count_integers_with_positive_digit_sum(nums):
    count = 0
    for val in nums:
        n = abs(val)
        digit_sum = 0
        if n == 0:
            digit_sum = 0
        else:
            while n > 0:
                digit_sum += n % 10
                n //= 10
        if digit_sum > 0:
            count += 1
    return count