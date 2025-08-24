def check_list(numbers):
    """
    Checks if a list of integers is sorted in ascending order and has no more than one duplicate of the same number.

    Args:
        numbers: A list of integers.

    Returns:
        True if both conditions are satisfied, False otherwise.
    """
    if not numbers:
        return True
    is_sorted = all((numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1)))
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
        if counts[number] > 1:
            return False
    return is_sorted