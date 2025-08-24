def is_sorted_and_unique(nums):
    """
    Returns True if the list of integers is sorted in ascending order
    and contains no duplicate numbers. Otherwise returns False.
    """
    sorted_nums = sorted(nums)
    is_sorted = nums == sorted_nums
    has_no_duplicates = True
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            has_no_duplicates = False
            break
    return is_sorted and has_no_duplicates