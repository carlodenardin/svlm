def traversal_end(nums):
    if len(nums) == 0:
        res = 0
        return 'End'
    if len(nums) > 0:
        value = nums[0]
        digits = [int(ch) for ch in str(abs(value))]
        total = sum(digits)
        if total == 1:
            return 'End'
        else:
            return 'End'