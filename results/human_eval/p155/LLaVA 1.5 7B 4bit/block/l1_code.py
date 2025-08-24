def count_even_and_odd_digits(digits):
    count = 0
    for digit in digits:
        if digit % 2 == 0:
            count += 1
        else:
            count += 2
    return count