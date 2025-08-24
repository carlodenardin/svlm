def count_numbers_by_positive_digit_sum(nums):
    """
    Counts how many numbers in the input list have a positive sum of digits
    (sum of digits of the absolute value). This mirrors the described algorithm:
    for each extracted integer, compute the sum of its digits and increment the
    counter if that sum is greater than 0.
    """
    res = 0
    data = list(nums)
    while data:
        x = data.pop(0)
        s = sum((int(ch) for ch in str(abs(int(x)))))
        if s > 0:
            res += 1
    return res