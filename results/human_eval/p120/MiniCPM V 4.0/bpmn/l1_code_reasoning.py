def sorted_last_k_elements(nums, k):
    """
    Receives a list of integers 'nums' and an integer 'k'.
    Sorts the entire list in ascending order and returns the last k elements.
    If k <= 0, returns an empty list.
    """
    sorted_nums = sorted(nums)
    if k <= 0:
        return []
    return sorted_nums[-k:]