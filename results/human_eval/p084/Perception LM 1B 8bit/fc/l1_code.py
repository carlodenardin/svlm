def sum_digits_and_binary(n):
    """
    Sums the digits of an integer and returns the result as a binary string.

    Args:
        n (int): The input integer.

    Returns:
        str: The binary representation of the sum of the digits of n.
    """
    sum_of_digits = 0
    binary_string = ''
    for digit in str(n):
        sum_of_digits += int(digit)
    binary_string = bin(sum_of_digits)[2:]
    return binary_string