def last_k_of_sorted(nums, k):
    """
    Sort the input list in ascending order and return the last k elements.
    """
    sorted_list = sorted(nums)
    if k <= 0:
        return []
    return sorted_list[-k:]