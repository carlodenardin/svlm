def check_list_sorted_and_limited_duplicate(nums):
    """
    Checks whether the given list of integers is sorted in ascending order
    and contains no more than one duplicate of any value.
    - Sorting: non-decreasing (each a[i] <= a[i+1])
    - Duplicates: for each value, count <= 2
    Returns True if both conditions are satisfied, otherwise False.
    If the result is True, prints a message indicating the criteria were met.
    """
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    if not nums:
        print('True: The list is sorted in ascending order and contains at most one duplicate.')
        return True
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
            if count > 2:
                return False
        else:
            count = 1
    print('True: The list is sorted in ascending order and contains at most one duplicate.')
    return True