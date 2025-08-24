def check_list_criteria(numbers):
    """
    Checks if a list of integers is sorted in ascending order
    and each distinct number appears at least three times.

    Args:
        numbers: A list of integers.

    Returns:
        True if both conditions hold, otherwise False.
    """
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    freq = {}
    for n in numbers:
        freq[n] = freq.get(n, 0) + 1
    for count in freq.values():
        if count < 3:
            return False
    return True