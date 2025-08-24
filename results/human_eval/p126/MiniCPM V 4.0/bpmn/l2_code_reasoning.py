def is_sorted_no_more_than_two(nums):
    """
    Determine if the given list of integers is sorted in non-decreasing order
    and no value occurs more than twice.
    Returns True if both conditions hold, otherwise False.
    """
    if not nums:
        return True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    counts = {}
    for val in nums:
        counts[val] = counts.get(val, 0) + 1
        if counts[val] > 2:
            return False
    return True