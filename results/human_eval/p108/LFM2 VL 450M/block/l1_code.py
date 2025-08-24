def count_sum_of_digits(input_list):
    """
    Counts the sum of all digits in a list of integers.
    """
    sum_of_digits = 0
    for num in input_list:
        sum_of_digits += int(num)
    return sum_of_digits