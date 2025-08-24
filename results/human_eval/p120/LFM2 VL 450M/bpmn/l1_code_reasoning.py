def sort_and_return_last_k(data, k):
    """
    Sort a list of (integer, variable_name) tuples by the integer in ascending order
    and return the last k elements of the sorted list.
    """
    sorted_list = sorted(data, key=lambda t: t[0])
    return sorted_list[-k:]