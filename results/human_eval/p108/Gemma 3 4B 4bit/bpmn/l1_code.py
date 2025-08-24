def count_positive_digits(numbers):
    """
  Counts the number of digits in each integer of a list that have a sum greater than 0.

  Args:
    numbers: A list of integers.

  Returns:
    The total count of integers with a sum of digits greater than 0.
  """
    total_count = 0
    for number in numbers:
        digit_sum = 0
        for digit in str(abs(number)):
            digit_sum += int(digit)
        if digit_sum > 0:
            total_count += 1
    return total_count