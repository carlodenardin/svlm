def has_duplicates(list_int):
    """
    Checks if a list of integers contains any duplicates.

    Args:
        list_int: A list of integers.

    Returns:
        True if the list contains duplicates, False otherwise.
    """
    for i in list_int:
        if i >= list_int[list_int.index(i) + 1]:
            count = 0
            for j in list_int:
                if j == i:
                    count += 1
            if count > 1:
                return False
    return True