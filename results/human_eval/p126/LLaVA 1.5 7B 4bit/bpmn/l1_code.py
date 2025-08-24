def is_sorted_and_has_duplicate(numbers):
    for i in range(len(numbers)):
        if numbers[i] == numbers[i - 1]:
            return False
    return True