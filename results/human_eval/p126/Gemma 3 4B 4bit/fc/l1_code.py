def check_list(numbers):
    """
    Checks if a list of integers is sorted in ascending order and has no duplicate numbers.

    Args:
        numbers: A list of integers.

    Returns:
        True if the list is sorted and has no duplicate numbers, False otherwise.
    """
    if not numbers:
        return True
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    if len(numbers) != len(set(numbers)):
        return False
    return True