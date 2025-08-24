def last_element_after_descending_sort(input_list):
    """
    Takes a list of numbers, copies it, sorts the copy in descending order,
    and returns the last element of the sorted list.
    If the input list is empty, returns None.
    """
    copied = list(input_list)
    copied.sort(reverse=True)
    if not copied:
        return None
    return copied[-1]