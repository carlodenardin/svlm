def sortAndReturnLastKElements(nums, k):
    nums_list = list(nums)
    nums_list.sort()
    n = len(nums_list)
    if k <= 0:
        return []
    if k >= n:
        return nums_list[:]
    return nums_list[-k:]