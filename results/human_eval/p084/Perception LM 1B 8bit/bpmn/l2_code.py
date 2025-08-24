def convert_to_binary(n):
    """
    Convert an integer number to its binary representation.

    Args:
        n (int): The input integer number.

    Returns:
        str: The binary representation of the input number.
    """
    sum = 0
    res = ''
    while n > 0:
        digit = n % 10
        sum += digit
        res += str(digit)
        n //= 10
    return res