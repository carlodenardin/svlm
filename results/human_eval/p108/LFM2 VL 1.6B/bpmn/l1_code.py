def count_sum_of_digits(numbers):
    count = 0
    for number in numbers:
        for digit in str(number):
            count += int(digit) - 1
    return count