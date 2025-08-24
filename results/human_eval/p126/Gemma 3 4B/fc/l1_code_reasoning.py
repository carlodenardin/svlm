def is_sorted_and_unique(nums):
    """
    Return True if the input list of integers is sorted in ascending order
    and contains no duplicates, False otherwise.
    Implements the pairwise check as described:
    - For each consecutive pair, nums[i] <= nums[i+1] must hold (sorted)
    - For each consecutive pair, nums[i] != nums[i+1] must hold (no duplicates)
    If any pair violates either condition, return False.
    """
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
        if nums[i] == nums[i + 1]:
            return False
    return True