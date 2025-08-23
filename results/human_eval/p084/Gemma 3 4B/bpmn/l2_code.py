def sum_digits_to_binary(n):
    """
    Calculates the sum of the digits of an integer and converts it to binary.

    Args:
        n: An integer.

    Returns:
        The binary representation of the sum of the digits of the input integer.
    """
    sum_digits = 0
    num_str = str(n)
    for digit in num_str:
        sum_digits += int(digit)
    binary_sum = bin(sum_digits)[2:]
    return binary_sum