def count_positive_by_flowchart(nums):
    res = 0
    i = 0
    while i < len(nums):
        val = nums[i]
        res = res + val
        if res > 0:
            res = res + 1
        i += 1
    return res