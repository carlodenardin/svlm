def count_integers_with_positive_digit_sum(nums):
    count = 0
    for n in nums:
        digit_sum = 0
        for ch in str(n):
            if ch.isdigit():
                digit_sum += int(ch)
        if digit_sum > 0:
            count += 1
    return count