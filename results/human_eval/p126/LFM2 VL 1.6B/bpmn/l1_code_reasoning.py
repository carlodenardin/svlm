def is_sorted_and_no_more_than_one_duplicate(nums):
    if len(nums) <= 1:
        return True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
            if count > 2:
                return False
        else:
            count = 1
    return True