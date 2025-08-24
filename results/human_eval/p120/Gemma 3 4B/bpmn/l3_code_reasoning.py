def get_last_k_elements(list_of_integers, k):
    """
    Extracts the last k elements from a list of integers and returns them in a new list.

    The input list is sorted in ascending order in-place before slicing.
    """
    list_of_integers.sort()
    if k <= 0:
        return []
    return list_of_integers[-k:]