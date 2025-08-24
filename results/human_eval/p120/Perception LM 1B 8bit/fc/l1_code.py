def sort_list(k, list_):
    """
    Sort the list and keep the last k elements.
    
    Args:
        k (int): The number of elements to keep in the sorted list.
        list_ (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    """
    original_list = list_
    sorted_list = sorted(original_list, k=k)
    return sorted_list