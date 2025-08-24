def last_elements_of_sorted(nums):
    """
    Sorts the input list of integers in ascending order and returns the last element
    of the sorted list. If the list is empty, returns None.
    """
    sorted_list = sorted(nums)
    if not sorted_list:
        return None
    return sorted_list[-1]