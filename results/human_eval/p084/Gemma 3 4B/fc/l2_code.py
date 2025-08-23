def sum_digits_to_binary(n):
    """
    Calculates the sum of the digits of a number and converts it to binary.

    Args:
        n: An integer.

    Returns:
        A string representing the binary equivalent of the sum of the digits.
    """
    sum_of_digits = 0
    num_str = str(n)
    for digit in num_str:
        sum_of_digits += int(digit)
    binary_string = bin(sum_of_digits)[2:]
    return binary_string