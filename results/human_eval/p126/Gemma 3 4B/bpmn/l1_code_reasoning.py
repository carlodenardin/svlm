def is_valid_integer_list(integer_list):
    """
    Checks if a list of integers is sorted and has no duplicates.

    Args:
        integer_list: A list of integers.

    Returns:
        True if the list is sorted and has no duplicates, False otherwise.
    """
    if not integer_list:
        return True
    for i in range(len(integer_list) - 1):
        if integer_list[i] > integer_list[i + 1]:
            return False
    for i in range(len(integer_list) - 1):
        if integer_list[i] == integer_list[i + 1]:
            return False
    return True