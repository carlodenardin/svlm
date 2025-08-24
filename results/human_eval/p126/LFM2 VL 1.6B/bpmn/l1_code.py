def is_sorted_and_no_duplicates(numbers):
    numbers = list(numbers)
    if len(numbers) <= 1:
        return True
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            return False
    return True