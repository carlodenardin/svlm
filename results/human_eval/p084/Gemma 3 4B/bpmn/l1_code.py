def sum_digits_to_binary(n):
    """
  Calculates the sum of the digits of an integer and converts it to binary.

  Args:
    n: An integer number.

  Returns:
    The binary representation of the sum of the digits of n as a string.
  """
    sum_of_digits = 0
    for digit in str(n):
        sum_of_digits += int(digit)
    binary_result = bin(sum_of_digits)[2:]
    return binary_result