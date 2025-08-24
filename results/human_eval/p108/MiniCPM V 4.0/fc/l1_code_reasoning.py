def count_integers_with_positive_digit_sum(numbers):
    """
    Counts how many integers in the input have a digit-sum greater than 0.
    Digit sum is computed from the absolute value of the integer.
    """
    count = 0
    for num in numbers:
        n = abs(int(num))
        digit_sum = 0
        if n == 0:
            digit_sum = 0
        else:
            while n > 0:
                digit_sum += n % 10
                n //= 10
        if digit_sum > 0:
            count += 1
    return count