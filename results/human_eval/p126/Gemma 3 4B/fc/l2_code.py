def check_list(l):
    """
    Checks if a list of integers is sorted in ascending order and has no duplicate numbers.

    Args:
        l: A list of integers.

    Returns:
        True if the list is sorted in ascending order and has no duplicate numbers, False otherwise.
    """
    if not l:
        return True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    counts = {}
    for num in l:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num in counts:
        if counts[num] > 1:
            return False
    return True