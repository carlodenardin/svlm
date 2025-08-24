def is_sorted(list):
    """
    Checks if a list of integers is sorted in ascending order.

    Args:
        list: A list of integers.

    Returns:
        True if the list is sorted, False otherwise.
    """
    if len(list) < 2:
        return True
    i = 1
    while i < len(list):
        if list[i] <= list[i - 1]:
            return False
        i += 1
    return True