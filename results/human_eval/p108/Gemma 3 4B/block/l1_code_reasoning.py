def count_numbers_with_positive_digit_sum(nums):
    """
    Counts how many integers in the input list have a sum of digits greater than 0.
    The sum is computed by summing the decimal digits of the number (ignoring any sign).
    """
    count = 0
    for num in nums:
        digit_sum = 0
        for ch in str(num):
            if ch.isdigit():
                digit_sum += int(ch)
        if digit_sum > 0:
            count += 1
    return count