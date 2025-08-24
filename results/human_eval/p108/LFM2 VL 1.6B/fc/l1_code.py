def count_digits(numbers):
    count = 0
    for number in numbers:
        count += len(str(number))
    return count