def count_digits_weird(n: int) -> int:
    """
    Implements the described algorithm:
    - Iterate over the digits of the absolute value of n from least significant to most significant.
    - If a digit is zero, increment the count by 1.
    - If a digit is non-zero, add its value to the count.
    - Stop when all digits have been processed.
    - Returns the computed count (note: if n == 0, returns 0 as the loop does not run).
    """
    m = abs(n)
    count = 0
    while m > 0:
        digit = m % 10
        if digit == 0:
            count += 1
        else:
            count += digit
        m //= 10
    return count