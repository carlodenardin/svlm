def binary_of_digit_ones(n: int) -> str:
    """
    Convert integer n to a binary string representing the count of '1' digits
    in the decimal representation of n.
    """
    count = 0
    m = n
    while m > 0:
        digit = m % 10
        if digit == 1:
            count += 1
        m //= 10
    return bin(count)[2:]