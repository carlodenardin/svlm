def calculate_sum_and_binary(n):
    """
    Calculate the sum of digits of a given number and convert it to binary.

    Args:
        n (int): The input number.

    Returns:
        str: The binary string representation of the sum of digits.
    """
    sum = 0
    res = ''
    for digit in str(n):
        sum += int(digit)
    res = bin(sum)[2:]
    return res