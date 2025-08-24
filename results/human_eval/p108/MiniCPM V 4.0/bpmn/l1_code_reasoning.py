def count_numbers_with_digit_sum_greater_than_zero(nums):
    """
    Counts how many integers in the input list have a sum of digits greater than zero.

    Args:
        nums (list of int): The input integers.

    Returns:
        int: The count of numbers whose sum of digits > 0.
    """
    counter = 0
    for num in nums:
        digit_sum = sum((int(ch) for ch in str(abs(num))))
        if digit_sum > 0:
            counter += 1
    return counter