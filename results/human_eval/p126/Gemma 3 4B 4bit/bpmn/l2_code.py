def check_list(numbers):
    """
    Checks if a list of integers is sorted and if any number appears more than twice.

    Args:
        numbers: A list of integers.

    Returns:
        True if the list is sorted and no number appears more than twice, False otherwise.
    """
    if not sorted(numbers):
        return False
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    for number in counts:
        if counts[number] > 2:
            return False
    return True