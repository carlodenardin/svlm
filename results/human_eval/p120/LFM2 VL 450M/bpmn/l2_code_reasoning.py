def solve(nums, k):
    sorted_nums = sorted(nums)
    if k <= 0:
        return []
    return sorted_nums[-k:]