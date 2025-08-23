def check_list(numbers):
    """
    Checks if a list of integers is sorted and if any number appears more than twice.

    Args:
        numbers: A list of integers.

    Returns:
        True if the list is sorted and no number appears more than twice, False otherwise.
    """
    is_sorted = all((numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1)))
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    for count in counts.values():
        if count > 2:
            return False
    return is_sorted