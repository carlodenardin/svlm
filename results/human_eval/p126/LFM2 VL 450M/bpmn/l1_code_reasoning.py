def check_sorted(nums):
    if len(nums) == 0:
        return ('No', 'No')
    if len(nums) == 1:
        return ('No', 'No')
    is_asc = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            is_asc = False
            break
    if is_asc:
        return ('Yes', 'No')
    is_desc = True
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            is_desc = False
            break
    if is_desc:
        return ('Yes', 'No')
    return ('No', 'No')