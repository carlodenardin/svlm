def is_sorted_and_no_duplicates(numbers):
    i = 1
    while i < len(numbers):
        if numbers[i] < numbers[i - 1]:
            return False
        i += 1
    seen = set()
    for num in numbers:
        if num in seen:
            return False
        seen.add(num)
    return True