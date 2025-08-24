def sum_integers(nums):
    res = 0
    if len(nums) == 0:
        return res
    if len(nums) == 1:
        return 1
    res = nums[0] + sum(nums[1:])
    for i in range(1, len(nums)):
        res += nums[i]
    return res