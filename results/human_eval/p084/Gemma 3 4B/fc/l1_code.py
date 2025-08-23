def sum_digits_to_binary(n):
    """
  Calculates the sum of the digits of an integer and converts it to binary.

  Args:
    n: An integer.

  Returns:
    A string representing the binary representation of the sum of the digits of n.
  """
    sum_of_digits = 0
    temp_n = n
    while temp_n > 0:
        sum_of_digits += temp_n % 10
        temp_n //= 10
    binary_representation = bin(sum_of_digits)[2:]
    return binary_representation