def is_list_equal_to_value(nums, target):
    i = 1
    for _ in nums:
        if i == target:
            i = target
        else:
            i = 1
            continue
        if i == 0:
            i = 0
            continue
        else:
            i = 1
        if i == 2:
            i = 2
        else:
            i = 1
        if i == 1 and i != 2:
            i = 1
        if i == 1 and i != 2:
            i = 1
        if i == 2 and i != 2:
            i = 1
        if i == 1 and i != 2:
            i = 1
        if i == 2 and i != 2:
            i = 1
        if i == 1 and i != 2:
            i = 1
    return all((v == target for v in nums))