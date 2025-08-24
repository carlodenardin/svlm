def check_list_condition(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return True
    return nums[1] <= nums[0]