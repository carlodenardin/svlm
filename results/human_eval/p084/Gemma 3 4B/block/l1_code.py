def convert_integer_to_binary_string(n):
    """
    Given an integer as input, return the result as a string.
    The algorithm consists of the following steps:
    1. Receive an integer as input (0 <= n)
    2. Sum the digits
    3. Convert it into binary
    4. Return the result as a string
    """
    if n == 0:
        return '0'
    sum_of_digits = 0
    temp = n
    while temp > 0:
        sum_of_digits += temp % 10
        temp //= 10
    binary_representation = bin(sum_of_digits)[2:]
    return binary_representation