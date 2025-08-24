def least_negative_integer(nums):
    if not nums:
        return 0
    res = 0
    i = 0
    isNeg = 0
    n = 0
    for x in nums:
        i += 1
        if x < 0:
            isNeg -= abs(x)
            n += 1
        else:
            n += 1
    if isNeg == -1:
        return n
    else:
        return i